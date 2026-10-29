"""Extra ad layouts, set 2 (added 2026-10-28, run 2). Imported by ads.py — run `python3 pipeline/ads.py <spec>`.

ad_scale      — single 1080x1350 image, white background: balance scale (big unrelated crowd vs. relevant group).
ad_signpost   — carousel on a mint background: a signpost whose boards fill in (what / for whom / how to reach out).
ad_spotlight  — 1080x1920 MP4: a dark path lit step by step by a moving spotlight ("what happens after the follow").
Identity anchors kept: founder's original logo (navy tile on light backgrounds), mint #14D8A5, Heebo.
"""
import json, subprocess
from render import THEME as T, html, logo, ROOT
from ads_extra import logo_tile, cta_button, pill, NAVY, NAVY2, NAVY3, LIGHT_SUB, _ts

MINT = T["acc"]


# ======================= 1. Balance scale (white) =======================
def fig(x, y, color, s=1.0):
    return (f"<circle cx='{x}' cy='{y}' r='{11 * s}' fill='{color}'/>"
            f"<rect x='{x - 12 * s}' y='{y + 14 * s}' width='{24 * s}' height='{40 * s}' rx='{11 * s}' fill='{color}'/>")


def scale_svg():
    w, h = 920, 560
    cx, top = 460, 120
    tilt = 9  # degrees: heavy (relevant, right side in RTL reading = drawn on the right) goes down
    import math
    arm = 330
    dx, dy = arm * math.cos(math.radians(tilt)), arm * math.sin(math.radians(tilt))
    rx, ry = cx + dx, top + dy      # right end (down) — relevant group
    lx, ly = cx - dx, top - dy      # left end (up) — big unrelated crowd

    def pan(x, y, people):
        return (f"<line x1='{x}' y1='{y}' x2='{x - 120}' y2='{y + 150}' stroke='#8799DB' stroke-width='4'/>"
                f"<line x1='{x}' y1='{y}' x2='{x + 120}' y2='{y + 150}' stroke='#8799DB' stroke-width='4'/>"
                f"{people}<path d='M{x - 150} {y + 150} h300 q-20 46 -150 46 q-130 0 -150 -46 z' fill='{NAVY2}'/>")
    crowd = ""
    for r_, n in ((0, 9), (1, 8), (2, 7)):
        for k in range(n):
            crowd += fig(lx - 120 + k * 30 + r_ * 15, ly + 92 - r_ * 40, "#8799DB" if (k + r_) % 3 else "#C5CBEE", .8)
    group = "".join(fig(rx - 64 + k * 32, ry + 92, MINT, .95) for k in range(5))
    return f"""<svg width='{w}' height='{h}' viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg'>
      <rect x='{cx - 14}' y='{top}' width='28' height='{h - top - 60}' rx='10' fill='{NAVY}'/>
      <path d='M{cx - 130} {h - 30} q130 -70 260 0 z' fill='{NAVY}'/>
      <line x1='{lx}' y1='{ly}' x2='{rx}' y2='{ry}' stroke='{NAVY}' stroke-width='18' stroke-linecap='round'/>
      <circle cx='{cx}' cy='{top}' r='26' fill='{MINT}' stroke='{NAVY}' stroke-width='8'/>
      {pan(lx, ly, crowd)}{pan(rx, ry, group)}
    </svg>"""


def ad_scale(spec):
    s = spec["image"]
    labels = (f"<div style='display:flex;justify-content:space-between;width:920px;font-size:28px;font-weight:800;color:{NAVY}'>"
              f"<span style='width:400px;text-align:center'><span style='color:#0B9C77'>●</span> {s['label_relevant']}</span>"
              f"<span style='width:400px;text-align:center;color:{LIGHT_SUB}'><span style='color:#8799DB'>●</span> {s['label_crowd']}</span></div>")
    body = f"""<style>.lt mark{{color:{NAVY};background:linear-gradient(transparent 60%, {MINT} 60%, {MINT} 92%, transparent 92%)}}</style>
    <div class='lt' style='position:absolute;inset:0;overflow:hidden;background:#FFFFFF;color:{NAVY}'>
      <div style='position:absolute;bottom:-260px;left:-200px;width:900px;height:620px;border-radius:50%;background:{MINT};opacity:.12'></div>
      <div style='position:absolute;top:66px;right:80px;left:80px;display:flex;justify-content:space-between;align-items:flex-start'>
        {logo_tile(84)}{pill(s['tag'], LIGHT_SUB, '#B9C1E6') if s.get('tag') else ''}</div>
      <div style='position:absolute;top:240px;right:80px;left:80px;display:flex;flex-direction:column;gap:18px'>
        <h1 style='font-size:76px;line-height:1.08;color:{NAVY}'>{s['head']}</h1>
        <div style='display:flex;flex-direction:column;align-items:center;gap:8px'>{scale_svg()}{labels}
          <div style='font-size:22px;color:{LIGHT_SUB};align-self:flex-start;margin-top:6px'>{s.get('note', 'המחשה')}</div></div>
        <p style='font-size:33px;color:{NAVY};line-height:1.4'>{s['value'].replace(' — ', '&nbsp;— ')}</p>
        <div>{cta_button(s['cta'])}</div>
      </div></div>"""
    return [body]


# ======================= 2. Signpost carousel (mint) =======================
def board(text, side, filled, highlight=False):
    clip = ("polygon(0 0, 88% 0, 100% 50%, 88% 100%, 0 100%)" if side == "right"
            else "polygon(12% 0, 100% 0, 100% 100%, 12% 100%, 0 50%)")
    bg = "#FFFFFF" if highlight else (NAVY if filled else "rgba(16,27,79,.22)")
    col = NAVY if highlight else "#FFFFFF"
    pad = "padding:0 90px 0 40px" if side == "right" else "padding:0 40px 0 90px"
    return (f"<div style='width:560px;height:118px;clip-path:{clip};background:{bg};color:{col};display:flex;align-items:center;"
            f"justify-content:center;{pad};font-size:{38 if filled else 64}px;font-weight:900;text-align:center;line-height:1.1'>"
            f"{text if filled else '?'}</div>")


def signpost(boards, active):
    sides = ["left", "right", "left"]
    rows = ""
    for k, b in enumerate(boards):
        filled = k < active
        offset = "margin-right:-200px" if sides[k] == "right" else "margin-left:-200px"
        rows += (f"<div style='display:flex;justify-content:center'><div style='{offset}'>"
                 f"{board(b, sides[k], filled, highlight=(k == active - 1))}</div></div>")
    return f"""<div style='position:relative;width:920px;height:640px'>
      <div style='position:absolute;left:446px;top:20px;width:28px;height:620px;border-radius:10px;background:{NAVY}'></div>
      <div style='position:absolute;left:400px;top:600px;width:120px;height:40px;border-radius:20px 20px 0 0;background:{NAVY}'></div>
      <div style='position:absolute;inset:50px 0 0 0;display:flex;flex-direction:column;gap:36px'>{rows}</div></div>"""


def ad_signpost(spec):
    slides = spec["slides"]; n = len(slides); out = []
    boards = spec["boards"]
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{NAVY if k <= i else 'rgba(16,27,79,.2)'}'></i>"
                       for k in range(n))
        wrap = f"<div style='position:absolute;inset:0;background:linear-gradient(160deg,#3FE5BA 0%,{MINT} 50%,#0FC293 100%);color:{NAVY}'>"
        if s.get("layout") == "end":
            body = wrap + f"""<div style='position:absolute;inset:0;padding:110px 90px;display:flex;flex-direction:column;justify-content:center;gap:40px'>
              <div style='align-self:flex-start'>{logo_tile(200, 30)}</div>
              <h2 style='font-size:62px;line-height:1.2;color:{NAVY}'>{s['head']}</h2>
              <p style='font-size:36px;color:{NAVY}'>{s.get('body', '')}</p>
              <div><div style='display:inline-block;background:{NAVY};color:{MINT};font-weight:800;font-size:38px;padding:22px 40px;border-radius:999px'>{s['cta']}</div></div>
              <div>{pill(s['tag'], NAVY, 'rgba(16,27,79,.35)') if s.get('tag') else ''}</div></div></div>"""
        else:
            body = wrap + f"""<div style='position:absolute;top:56px;left:80px;right:80px;display:flex;gap:10px'>{dots}</div>
            <div style='position:absolute;top:110px;right:80px;left:80px;display:flex;flex-direction:column;gap:14px'>
              {f"<div style='font-size:34px;font-weight:900;color:{NAVY};opacity:.75'>{s['kicker']}</div>" if s.get('kicker') else ''}
              <h2 style='font-size:{s.get('size', 68)}px;line-height:1.1;color:{NAVY}'>{s['head']}</h2>
              <p style='font-size:35px;color:{NAVY};line-height:1.4'>{s.get('body', '')}</p></div>
            <div style='position:absolute;bottom:110px;left:80px'>{signpost(boards, s.get('active', 0))}</div>
            <div style='position:absolute;bottom:40px;right:80px;display:flex;align-items:center;gap:26px'>{logo_tile(60, 12)}
              <span style='font-size:24px;color:{NAVY};font-weight:700'>{s.get('note', spec.get('note', 'המחשה'))}</span></div></div>"""
        out.append(body)
    return out


# ======================= 3. Spotlight video =======================
def spotlight_page(spec):
    v = spec["video"]; nodes = v["nodes"]
    path_d = "M" + " ".join(f"{x},{y}" for x, y, _ in nodes)
    pts = [(x, y) for x, y, _ in nodes]
    curve = f"M{pts[0][0]},{pts[0][1]}"
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        my = (y0 + y1) / 2
        curve += f" C{x0},{my} {x1},{my} {x1},{y1}"
    node_svg = ""
    for k, (x, y, label) in enumerate(nodes):
        side = 1 if x < 540 else -1
        lx = x + side * 74
        anchor = "end" if side > 0 else "start"  # direction=rtl flips start/end
        node_svg += (f"<g id='n{k}'><circle cx='{x}' cy='{y}' r='44' fill='{NAVY2}' stroke='#8799DB' stroke-width='6' class='ring'/>"
                     f"<circle cx='{x}' cy='{y}' r='18' fill='#8799DB' class='core'/>"
                     f"<text x='{lx}' y='{y + 16}' text-anchor='{anchor}' font-family='Heebo' font-weight='800' font-size='44' fill='#FFFFFF' direction='rtl'>{label}</text></g>")
    holes = "".join(f"<circle id='h{k}' cx='{x + (100 if x < 540 else -100)}' cy='{y}' r='0' fill='url(#hole)'/>"
                    for k, (x, y, _) in enumerate(nodes))  # centred between node and its label
    texts = "".join(f"<div class='txt' id='t{k}' style='opacity:0'><h1 style='font-size:{b.get('size', 88)}px'>{b['head']}</h1></div>"
                    for k, b in enumerate(v["beats"]))
    end = v["end"]
    css = f"""
    .stage{{position:absolute;inset:0;background:radial-gradient(1100px 1300px at 50% 60%, {NAVY2} 0%, {NAVY} 50%, {NAVY3} 100%)}}
    .txt{{position:absolute;top:290px;right:100px;left:100px}} .txt h1{{line-height:1.12}}
    #end{{position:absolute;inset:0;padding:300px 100px 420px;display:flex;flex-direction:column;justify-content:center;gap:40px;opacity:0}}
    """
    return f"""<style>{css}</style><div class='stage'></div>
    <svg id='scene' width='1080' height='1920' viewBox='0 0 1080 1920' style='position:absolute;inset:0'>
      <defs>
        <radialGradient id='hole'><stop offset='0' stop-color='#000' stop-opacity='1'/><stop offset='.55' stop-color='#000' stop-opacity='.95'/><stop offset='1' stop-color='#000' stop-opacity='0'/></radialGradient>
        <radialGradient id='spotg'><stop offset='0' stop-color='#000' stop-opacity='1'/><stop offset='.6' stop-color='#000' stop-opacity='.9'/><stop offset='1' stop-color='#000' stop-opacity='0'/></radialGradient>
        <linearGradient id='topfade' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#000' stop-opacity='1'/><stop offset='.62' stop-color='#000' stop-opacity='1'/><stop offset='1' stop-color='#000' stop-opacity='0'/></linearGradient>
        <mask id='dark' maskUnits='userSpaceOnUse' x='0' y='0' width='1080' height='1920'>
          <rect width='1080' height='1920' fill='#fff'/>{holes}<circle id='spot' cx='0' cy='0' r='0' fill='url(#spotg)'/>
          <rect x='0' y='0' width='1080' height='760' fill='url(#topfade)'/>
        </mask>
      </defs>
      <g id='world'>
        <path d='{curve}' fill='none' stroke='#8799DB' stroke-width='10' stroke-dasharray='4 26' stroke-linecap='round' opacity='.9'/>
        {node_svg}
      </g>
      <rect id='shade' width='1080' height='1920' fill='#050A24' opacity='.93' mask='url(#dark)'/>
    </svg>
    {texts}
    <div id='note' style='position:absolute;bottom:420px;left:100px;font-size:26px;color:{T['sub']}'>המחשה</div>
    <div id='brand' style='position:absolute;top:150px;right:100px'>{logo(96)}</div>
    <div id='end'>{logo(250)}
      <h1 style='font-size:{end.get('size', 60)}px;line-height:1.18'>{end['head']}</h1>
      <div id='cta' style='display:inline-block;align-self:flex-start;background:{MINT};color:{NAVY3};font-weight:800;font-size:46px;padding:26px 44px;border-radius:999px'>{end['cta']}</div>
      <span class='tag' style='font-size:30px;align-self:flex-start'>{end['tag']}</span></div>
    <script>
    const V={json.dumps(v, ensure_ascii=False)};
    const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)), ease=u=>u<.5?2*u*u:1-Math.pow(-2*u+2,2)/2;
    const fade=(t,a,b,f=.35)=>cl((t-a)/f)*cl((b-t)/f);
    function render(t){{
      V.beats.forEach((b,k)=>{{const e=document.getElementById('t'+k);e.style.opacity=fade(t,b.from,b.to);
        e.style.transform=`translateY(${{(1-cl((t-b.from)/.45))*30}}px)`;}});
      // spotlight keyframes: [time, nodeIndex]
      const K=V.spot; let x=V.nodes[K[0][1]][0], y=V.nodes[K[0][1]][1];
      for(let i=1;i<K.length;i++){{ if(t>=K[i-1][0]){{ const a=K[i-1], b=K[i]; const u=ease(cl((t-a[0])/(b[0]-a[0])));
          x=V.nodes[a[1]][0]+(V.nodes[b[1]][0]-V.nodes[a[1]][0])*u; y=V.nodes[a[1]][1]+(V.nodes[b[1]][1]-V.nodes[a[1]][1])*u; }} }}
      const spot=document.getElementById('spot'); spot.setAttribute('cx',x); spot.setAttribute('cy',y);
      spot.setAttribute('r', 260*cl((t-V.spot_on)/.6));
      V.nodes.forEach((n,k)=>{{ const d=Math.hypot(n[0]-x,n[1]-y); const lit=(V.lit_at[k]!==null && t>=V.lit_at[k]);
        const hr=lit? 250*cl((t-V.lit_at[k])/.5):0; document.getElementById('h'+k).setAttribute('r',hr);
        const g=document.getElementById('n'+k); const near=d<60 && t>V.spot_on;
        g.querySelector('.ring').setAttribute('stroke', (lit||near)?'{MINT}':'#8799DB');
        g.querySelector('.core').setAttribute('fill', (lit||near)?'{MINT}':'#8799DB');}});
      const endo=cl((t-V.end.at)/.5);
      document.getElementById('shade').setAttribute('opacity',(.93*cl((V.reveal_all-t)/1.2)).toFixed(3));
      document.getElementById('world').setAttribute('opacity',(1-endo).toFixed(3));
      document.getElementById('note').style.opacity=1-endo;
      document.getElementById('brand').style.opacity=1-endo;
      document.getElementById('end').style.opacity=endo;
      document.getElementById('cta').style.transform=`scale(${{1+.04*Math.sin(Math.max(0,t-V.end.at-.8)*4)*cl(t-V.end.at-.8)}})`;
    }}
    </script>"""


async def ad_spotlight(spec, out):
    from playwright.async_api import async_playwright
    v = spec["video"]; fps = 30; total = v["seconds"]
    frames = out / "_frames"; frames.mkdir(exist_ok=True)
    for f in frames.glob("*"): f.unlink()
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page()
        await pg.set_viewport_size({"width": 1080, "height": 1920})
        await pg.set_content(html(1080, 1920, spotlight_page(spec)), wait_until="load")
        await pg.evaluate("document.fonts.ready")
        if not await pg.evaluate("document.fonts.check('900 40px Heebo', 'אבג')"):
            raise RuntimeError("Hebrew font failed to load")
        for i in range(int(total * fps)):
            await pg.evaluate(f"render({i / fps:.4f})")
            await pg.screenshot(path=str(frames / f"f_{i:04d}.jpg"), type="jpeg", quality=93)
        await pg.evaluate(f"render({v.get('cover_t', 2.5)})")
        await pg.screenshot(path=str(out / "cover.jpg"), type="jpeg", quality=95)
        await b.close()
    music = ROOT / spec["music"]
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(fps), "-i", str(frames / "f_%04d.jpg"),
                    "-i", str(music), "-filter_complex",
                    f"[1:a]atrim=0:{total},afade=t=in:d=0.4,afade=t=out:st={total - 1.8}:d=1.8,volume=0.85[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-crf", "19", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "160k", "-t", str(total), "-movflags", "+faststart", str(out / "reel.mp4")], check=True)
    for f in frames.glob("*"): f.unlink()
    frames.rmdir()
    clean = lambda s: s.replace('<br>', ' ').replace('<mark>', '').replace('</mark>', '')
    (out / "subtitles.srt").write_text("\n".join(
        f"{k + 1}\n{_ts(bt['from'])} --> {_ts(bt['to'])}\n{clean(bt['head'])}\n" for k, bt in enumerate(v["beats"])), encoding="utf-8")
