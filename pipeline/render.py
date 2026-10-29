"""ForGrow render pipeline — turns a content spec (JSON) into upload-ready files.

Usage:  python3 pipeline/render.py content/<date>/<slug>/spec.json
Outputs next to the spec, in ./out/:
  carousel -> slide_01.jpg ...  (1080x1350, JPEG — the only image format the Instagram API accepts)
  story    -> frame_01.jpg ...  (1080x1920)
  reel     -> reel.mp4 (1080x1920, H.264/AAC) + cover.jpg + subtitles.srt
Voice-over: if out/vo/scene_XX.mp3 exist (made by pipeline/tts.py), they are laid under the reel
and each scene is stretched to fit its narration. Without them the reel is silent (draft).
"""
import asyncio, base64, json, pathlib, subprocess, sys
from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]
FONTS_DIR = ROOT / "brand" / "fonts"


def _ensure_fonts():
    """Fonts are not stored in the repo: fetch Heebo (OFL) from the npm registry on first use."""
    if (FONTS_DIR / "heebo-hebrew-900-normal.woff2").exists():
        return
    import tarfile, tempfile
    FONTS_DIR.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as d:
        subprocess.run(["npm", "pack", "@fontsource/heebo@5", "--silent"], cwd=d, check=True, capture_output=True)
        tgz = next(pathlib.Path(d).glob("*.tgz"))
        with tarfile.open(tgz) as t:
            for m in t.getmembers():
                name = pathlib.Path(m.name).name
                if m.isfile() and name.startswith(("heebo-hebrew-", "heebo-latin-")) and name.endswith("-normal.woff2") \
                        and any(w in name for w in ("-400-", "-700-", "-800-", "-900-")):
                    (FONTS_DIR / name).write_bytes(t.extractfile(m).read())


_ensure_fonts()

# Brand palette sampled from the founder's original logo (brand/logo_original.png)
THEME = dict(bg="#101B4F", bg2="#14246A", bg3="#0A1238", ink="#FFFFFF", sub="#C5CBEE", peri="#8799DB",
             acc="#14D8A5", hi="#14D8A5", card="rgba(255,255,255,0.07)", line="rgba(255,255,255,0.16)")


def _fonts():
    css = ""
    for w in (400, 700, 800, 900):
        for sub, rng in (("hebrew", "U+0590-05FF, U+200C-2010, U+20AA, U+25CC, U+FB1D-FB4F"),
                         ("latin", "U+0000-00FF, U+2000-206F, U+2190-21FF, U+2260")):
            b = base64.b64encode((FONTS_DIR / f"heebo-{sub}-{w}-normal.woff2").read_bytes()).decode()
            css += (f"@font-face{{font-family:Heebo;font-weight:{w};"
                    f"src:url(data:font/woff2;base64,{b}) format('woff2');unicode-range:{rng};}}\n")
    return css


FONTS = _fonts()


def css(w, h):
    t = THEME
    return f"""{FONTS}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{w}px;height:{h}px}}
body{{font-family:Heebo,sans-serif;background:linear-gradient(135deg,{t['bg2']} 0%,{t['bg']} 55%,{t['bg3']} 100%);color:{t['ink']};direction:rtl;overflow:hidden;position:relative}}
.pad{{position:absolute;inset:0;padding:96px 92px;display:flex;flex-direction:column}}
.brand{{position:absolute;bottom:64px;right:92px;font-weight:800;font-size:30px;direction:ltr}}
.brand b{{color:{t['acc']}}}
.handle{{position:absolute;bottom:68px;left:92px;font-size:26px;color:{t['sub']};direction:ltr}}
.num{{font-weight:900;color:{t['acc']};font-size:34px}}
h1{{font-weight:900;font-size:104px;line-height:1.05;letter-spacing:-1px}}
h2{{font-weight:900;font-size:76px;line-height:1.1;letter-spacing:-.5px}}
p{{font-size:40px;line-height:1.45;color:{t['sub']}}}
mark{{background:none;color:{t['acc']}}}
.card{{background:{t['card']};border:2px solid {t['line']};border-radius:28px;padding:36px 40px}}
.tag{{display:inline-block;font-size:24px;font-weight:700;padding:8px 18px;border-radius:999px;border:2px solid {t['line']};color:{t['sub']}}}
.prog{{position:absolute;top:56px;left:92px;right:92px;display:flex;gap:10px}}
.prog i{{flex:1;height:6px;border-radius:3px;background:{t['line']}}}
.prog i.on{{background:{t['acc']}}}
.note{{font-size:22px;color:{t['sub']}}}
"""


def html(w, h, body):
    return (f"<!doctype html><html lang='he' dir='rtl'><head><meta charset='utf-8'>"
            f"<style>{css(w, h)}</style></head><body>{body}</body></html>")


def _logo_src():
    for name, mime in (("logo.svg", "image/svg+xml"), ("logo.png", "image/png")):
        f = ROOT / "brand" / name
        if f.exists():
            return f"data:{mime};base64," + base64.b64encode(f.read_bytes()).decode()
    return None


LOGO_SRC = _logo_src()


def logo(h=72, style=""):
    """The founder's original logo (brand/logo.svg|png). Until it is supplied, a clearly marked empty slot."""
    if LOGO_SRC:
        return f"<img src='{LOGO_SRC}' style='height:{h}px;width:auto;max-width:none;display:block;align-self:flex-start;flex:none;object-fit:contain;{style}' alt='ForGrow'>"
    return (f"<div style='height:{h}px;min-width:{int(h * 2.6)}px;border:3px dashed {THEME['sub']};border-radius:14px;"
            f"display:flex;align-items:center;justify-content:center;font-size:{max(16, h // 4)}px;font-weight:700;"
            f"color:{THEME['sub']};padding:0 14px;{style}'>מקום ללוגו המקורי</div>")


BRAND = (f"<div style='position:absolute;bottom:48px;right:92px'>{logo(104)}</div>"
         "<div class='handle'>@forgrow_social</div>")


def prog(i, n):
    return "<div class='prog'>" + "".join(
        f"<i class='{'on' if k <= i else ''}'></i>" for k in range(n)) + "</div>"


# ---------- feed (4:5) layouts ----------
def L_cover(s, i, n):
    return f"""<div class='pad' style='justify-content:center'>
      {f"<span class='tag' style='align-self:flex-start;margin-bottom:48px'>{s['tag']}</span>" if s.get('tag') else ''}
      <h1>{s['title']}</h1>
      {f"<p style='margin-top:48px;font-size:46px;color:{THEME['ink']};font-weight:700'>{s['sub']}</p>" if s.get('sub') else ''}
      <p style='margin-top:20px'>{s.get('hint', 'החליקו ←')}</p></div>{BRAND}"""


def L_statement(s, i, n):
    return f"""{prog(i, n)}<div class='pad' style='justify-content:center'>
      <h2>{s['title']}</h2>
      {f"<p style='margin-top:44px'>{s['body']}</p>" if s.get('body') else ''}
      {f"<div class='card' style='margin-top:44px;text-align:center'><span style='font-size:56px;font-weight:900'>{s['quote']}</span></div>" if s.get('quote') else ''}
      {f"<p style='margin-top:44px;font-size:34px'>{s['foot']}</p>" if s.get('foot') else ''}</div>{BRAND}"""


def L_beforeafter(s, i, n):
    return f"""{prog(i, n)}<div class='pad' style='padding-top:130px'>
      <div class='num'>{s.get('label', '')}</div>
      <h2 style='margin-top:18px'>{s['title']}</h2>
      <p style='margin-top:30px;font-size:42px'>{s['body']}</p>
      <div style='margin-top:auto;margin-bottom:96px;display:flex;flex-direction:column;gap:22px'>
        <div class='card' style='opacity:.75'><div style='font-size:24px;font-weight:700;color:{THEME['sub']};margin-bottom:10px'>{s.get('before_label', 'לפני')}</div><div style='font-size:40px;line-height:1.4'>{s['before']}</div></div>
        <div class='card' style='border-color:{THEME['acc']};border-width:3px'><div style='font-size:24px;font-weight:700;color:{THEME['acc']};margin-bottom:10px'>{s.get('after_label', 'אחרי')}</div><div style='font-size:40px;line-height:1.4;font-weight:700'>{s['after']}</div></div>
        <div class='note'>{s.get('note', 'דוגמה להמחשה · עסק לא אמיתי')}</div>
      </div></div>{BRAND}"""


def L_steps(s, i, n):
    items = "".join(
        f"<div class='card' style='display:flex;gap:28px;align-items:center;padding:26px 34px'>"
        f"<span style='font-weight:900;font-size:44px;color:{THEME['acc']};min-width:44px'>{k + 1}</span>"
        f"<span><span style='font-size:38px;font-weight:800;display:block'>{x[0]}</span>"
        f"<span style='font-size:30px;color:{THEME['sub']}'>{x[1]}</span></span></div>"
        for k, x in enumerate(s['items']))
    return f"""{prog(i, n)}<div class='pad' style='padding-top:130px'>
      <h2>{s['title']}</h2>
      <div style='margin-top:44px;display:flex;flex-direction:column;gap:18px'>{items}</div>
      {f"<p style='margin-top:36px;font-size:34px'>{s['foot']}</p>" if s.get('foot') else ''}</div>{BRAND}"""


def L_checklist(s, i, n):
    items = "".join(
        f"<div class='card' style='display:flex;gap:24px;align-items:center;padding:28px 36px'>"
        f"<span style='width:44px;height:44px;border:3px solid {THEME['acc']};border-radius:12px;flex:none'></span>"
        f"<span style='font-size:38px;font-weight:700'>{x}</span></div>" for x in s['items'])
    return f"""{prog(i, n)}<div class='pad' style='padding-top:130px'>
      <h2>{s['title']}</h2>
      <div style='margin-top:48px;display:flex;flex-direction:column;gap:20px'>{items}</div>
      {f"<p style='margin-top:48px;color:{THEME['ink']};font-weight:700;font-size:42px'>{s['cta']}</p>" if s.get('cta') else ''}
      {f"<p style='margin-top:12px;font-size:34px'>{s['cta_sub']}</p>" if s.get('cta_sub') else ''}</div>{BRAND}"""


# ---------- vertical (9:16) layouts: story frames + reel scenes ----------
def V_frame(s, i, n, reveal=99, progress=True):
    """Vertical frame. Text kept inside the centre safe area (top 250px / bottom 400px free)."""
    lines = s.get('lines', [])
    shown = lines[:reveal]
    body_lines = "".join(f"<p style='margin-top:36px;font-size:52px'>{l}</p>" for l in shown)
    kicker = f"<div class='num' style='font-size:40px;margin-bottom:22px'>{s['kicker']}</div>" if s.get('kicker') else ''
    bar = ""
    if progress and n > 1:
        bar = ("<div class='prog' style='top:180px;left:100px;right:100px'>" + "".join(
            f"<i class='{'on' if k <= i else ''}'></i>" for k in range(n)) + "</div>")
    return f"""{bar}<div class='pad' style='justify-content:center;padding:300px 100px 420px'>
      {kicker}<h1 style='font-size:{s.get('size', 96)}px;line-height:1.12'>{s['head']}</h1>{body_lines}
      {f"<div class='card' style='margin-top:44px'><span style='font-size:42px;font-weight:800'>{s['card']}</span></div>" if s.get('card') and reveal >= len(lines) else ''}
      {f"<div class='note' style='margin-top:30px;font-size:26px'>{s['note']}</div>" if s.get('note') else ''}</div>
      <div style='position:absolute;bottom:300px;right:100px'>{logo(120)}</div>"""


def V_end(s, i, n, reveal=99, progress=True):
    """Ad end card: logo, value line, CTA button, pilot tag."""
    show_cta = reveal >= 1 or not s.get('lines')
    return f"""<div class='pad' style='justify-content:center;align-items:flex-start;padding:300px 100px 420px;gap:40px'>
      {logo(260)}
      <h1 style='font-size:{s.get('size', 76)}px;line-height:1.15'>{s['head']}</h1>
      {f"<div style='background:{THEME['acc']};color:{THEME['bg3']};font-weight:800;font-size:46px;padding:26px 44px;border-radius:999px'>{s['cta']}</div>" if s.get('cta') and show_cta else ''}
      {f"<span class='tag' style='font-size:30px'>{s['tag']}</span>" if s.get('tag') else ''}
      {f"<div class='note' style='font-size:26px'>{s['note']}</div>" if s.get('note') else ''}</div>"""


FEED = dict(cover=L_cover, statement=L_statement, beforeafter=L_beforeafter, steps=L_steps, checklist=L_checklist)


async def shoot(pg, body, path, w, h):
    await pg.set_viewport_size({"width": w, "height": h})
    await pg.set_content(html(w, h, body), wait_until="load")
    await pg.evaluate("document.fonts.ready")
    ok = await pg.evaluate("document.fonts.check('900 40px Heebo', 'אבג')")
    if not ok:
        raise RuntimeError("Hebrew font failed to load")
    png = path.with_suffix(".png")
    await pg.screenshot(path=str(png))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(png), "-q:v", "2", str(path)], check=True)
    return png


def dur(p):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                         capture_output=True, text=True, check=True).stdout
    return float(out.strip())


def srt_time(t):
    ms = int(round(t * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


async def render(spec_path):
    spec_path = pathlib.Path(spec_path).resolve()
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    out = spec_path.parent / "out"; out.mkdir(exist_ok=True)
    tmp = out / "_tmp"; tmp.mkdir(exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page()
        kind = spec["type"]
        if kind == "carousel":
            n = len(spec["slides"])
            for i, s in enumerate(spec["slides"]):
                await shoot(pg, FEED[s["layout"]](s, i, n), out / f"slide_{i + 1:02d}.jpg", 1080, 1350)
        elif kind == "story":
            n = len(spec["frames"])
            for i, s in enumerate(spec["frames"]):
                await shoot(pg, V_frame(s, i, n), out / f"frame_{i + 1:02d}.jpg", 1080, 1920)
        elif kind == "reel":
            await reel(pg, spec, out, tmp)
        await b.close()
    for f in tmp.glob("*"):
        f.unlink()
    tmp.rmdir()
    for f in out.glob("*.png"):
        f.unlink()
    print("rendered", spec["id"], "->", out)


async def reel(pg, spec, out, tmp):
    scenes = spec["scenes"]; n = len(scenes); fade = 0.3
    vo_dir = out / "vo"
    clips, durations, srt, t = [], [], [], 0.0
    for i, s in enumerate(scenes):
        vo = vo_dir / f"scene_{i + 1:02d}.mp3"
        d = max(s.get("dur", 4.0), (dur(vo) + 0.35) if vo.exists() else 0)
        steps = len(s.get("lines", [])) + 1
        imgs = []
        for r in range(steps):
            fn = V_end if s.get('layout') == 'end' else V_frame
            png = await shoot(pg, fn(s, i, n, reveal=r), tmp / f"s{i:02d}_{r}.jpg", 1080, 1920)
            imgs.append(png)
        # reveal: headline first, then each line; last state holds
        first = min(1.2, d * 0.35) if steps > 1 else d
        each = [first] + [max(0.8, (d - first) / (steps - 1))] * (steps - 1) if steps > 1 else [d]
        lst = tmp / f"s{i:02d}.txt"
        lst.write_text("".join(f"file '{im.name}'\nduration {x:.3f}\n" for im, x in zip(imgs, each)) +
                       f"file '{imgs[-1].name}'\n")
        clip = tmp / f"s{i:02d}.mp4"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                        "-vf", "fps=30,format=yuv420p,scale=1080:1920", "-t", f"{d + fade:.3f}",
                        "-c:v", "libx264", "-crf", "19", str(clip)], check=True, cwd=tmp)
        clips.append(clip); durations.append(d)
        srt.append((t, t + d, s.get("vo") or s["head"]))
        t += d
    # chain xfades
    inputs = sum([["-i", str(c)] for c in clips], [])
    fc, last, off = [], "0:v", 0.0
    for k in range(1, len(clips)):
        off += durations[k - 1]
        lbl = f"v{k}"
        fc.append(f"[{last}][{k}:v]xfade=transition=fade:duration={fade}:offset={off:.3f}[{lbl}]")
        last = lbl
    video = tmp / "video.mp4"
    total = sum(durations)
    cmd = ["ffmpeg", "-y", "-loglevel", "error", *inputs]
    if fc:
        cmd += ["-filter_complex", ";".join(fc), "-map", f"[{last}]"]
    cmd += ["-t", f"{total:.3f}", "-c:v", "libx264", "-crf", "19", "-pix_fmt", "yuv420p", str(video)]
    subprocess.run(cmd, check=True)
    # audio: narration per scene placed at scene start, or silence
    final = out / "reel.mp4"
    vos = [vo_dir / f"scene_{i + 1:02d}.mp3" for i in range(n)]
    have_vo = all(v.exists() for v in vos)
    music = (ROOT / spec["music"]) if spec.get("music") else None
    a_in, a_fc, labels = [], [], []
    k = 1
    if music and music.exists():
        a_in += ["-i", str(music)]
        vol = 0.22 if have_vo else 0.85
        a_fc.append(f"[{k}:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.4,"
                    f"afade=t=out:st={max(0, total - 1.8):.3f}:d=1.8,volume={vol}[mus]")
        labels.append("[mus]"); k += 1
    if have_vo:
        starts = 0.0
        for i, v in enumerate(vos):
            a_in += ["-i", str(v)]
            ms = int(starts * 1000)
            a_fc.append(f"[{k}:a]adelay={ms}|{ms}[a{i}]"); labels.append(f"[a{i}]")
            starts += durations[i]; k += 1
    if labels:
        a_fc.append("".join(labels) + f"amix=inputs={len(labels)}:normalize=0,alimiter=limit=0.9[aout]")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(video), *a_in,
                        "-filter_complex", ";".join(a_fc), "-map", "0:v", "-map", "[aout]",
                        "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-t", f"{total:.3f}",
                        "-movflags", "+faststart", str(final)], check=True)
    else:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(video), "-f", "lavfi",
                        "-i", "anullsrc=r=44100:cl=stereo", "-shortest", "-c:v", "copy", "-c:a", "aac",
                        "-movflags", "+faststart", str(final)], check=True)
    cover = spec.get("cover") or scenes[0]
    await shoot(pg, V_frame(cover, 0, 1, progress=False), out / "cover.jpg", 1080, 1920)
    (out / "subtitles.srt").write_text("\n".join(
        f"{k + 1}\n{srt_time(a)} --> {srt_time(b)}\n{txt}\n" for k, (a, b, txt) in enumerate(srt)), encoding="utf-8")


if __name__ == "__main__":
    for path in sys.argv[1:]:
        asyncio.run(render(path))
