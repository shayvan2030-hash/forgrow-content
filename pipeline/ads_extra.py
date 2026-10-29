"""Extra ad layouts (added 2026-10-28). Imported by ads.py — run through `python3 pipeline/ads.py <spec>`.

ad_storefront  — single 1080x1350 image on a LIGHT background: a shop-window illustration (profile = shop window).
ad_calendar    — carousel of wall-calendar pages on navy: exposure over time until the day of need.
ad_shape_video — 1080x1920 MP4, frame-by-frame shape-sorter animation (fit, not reach) + original music.
Identity anchors kept: founder's original logo (on a navy tile on light backgrounds), mint #14D8A5, Heebo.
"""
import base64, json, math, pathlib, random, subprocess
from render import THEME as T, html, logo, shoot, ROOT

ICON = "data:image/png;base64," + base64.b64encode((ROOT / "brand" / "logo_icon.png").read_bytes()).decode()
NAVY, NAVY2, NAVY3 = T["bg"], T["bg2"], T["bg3"]
LIGHT_BG, LIGHT_SUB = "#F2F4FC", "#3A4785"


def logo_tile(h=96, pad=18):
    """Original logo on a navy rounded tile — for light backgrounds (docs/brand.md)."""
    return (f"<div style='display:inline-block;background:{NAVY};border-radius:{pad + 8}px;padding:{pad}px {pad + 6}px'>"
            f"{logo(h)}</div>")


def cta_button(text, size=38):
    return (f"<div style='display:inline-block;background:{T['acc']};color:{NAVY3};font-weight:800;"
            f"font-size:{size}px;padding:22px 40px;border-radius:999px'>{text}</div>")


def pill(text, color, border, size=26):
    return (f"<span style='display:inline-block;font-size:{size}px;font-weight:700;padding:8px 20px;border-radius:999px;"
            f"border:2px solid {border};color:{color}'>{text}</span>")


# ======================= 1. Storefront (light) =======================
def person(x, y, color, badge=False, trail=0):
    """Flat figure: head + body. trail = dashed motion lines (walking past)."""
    g = ""
    if trail:
        for k in range(3):
            yy = y + 30 + k * 18
            g += (f"<line x1='{x + trail * 34}' y1='{yy}' x2='{x + trail * (34 + 30 - k * 6)}' y2='{yy}' "
                  f"stroke='{T['peri']}' stroke-width='4' stroke-linecap='round' opacity='.55'/>")
    g += f"<circle cx='{x}' cy='{y}' r='17' fill='{color}'/>"
    g += f"<rect x='{x - 19}' y='{y + 22}' width='38' height='70' rx='18' fill='{color}'/>"
    if badge:
        g += (f"<circle cx='{x + 30}' cy='{y - 34}' r='21' fill='{T['acc']}' stroke='{NAVY3}' stroke-width='4'/>"
              f"<path d='M{x + 30} {y - 45} v22 M{x + 19} {y - 34} h22' stroke='{NAVY3}' stroke-width='5' stroke-linecap='round'/>")
    return g


def storefront_svg(shop_name):
    w, h = 920, 560
    stripes = "".join(
        f"<path d='M{150 + i * 62} 70 h62 v54 a31 31 0 0 1 -62 0 z' fill='{T['acc'] if i % 2 == 0 else '#FFFFFF'}'/>"
        for i in range(10))
    tiles = "".join(
        f"<rect x='{222 + (k % 3) * 108}' y='{192 + (k // 3) * 106}' width='96' height='94' rx='12' "
        f"fill='{['#C5CBEE', '#8799DB', '#14D8A5', '#8799DB', '#C5CBEE', '#8799DB'][k]}'/>" for k in range(6))
    people = (person(60, 432, T['peri'], trail=1) + person(140, 440, T['peri'], trail=1) +
              person(300, 430, T['acc'], badge=True) + person(420, 434, T['acc'], badge=True) +
              person(560, 440, T['peri'], trail=-1) + person(800, 432, T['peri'], trail=-1) +
              person(875, 442, T['peri'], trail=-1))
    return f"""<svg width='780' height='{h * 780 // w}' viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg'>
      <rect x='130' y='40' width='660' height='450' rx='18' fill='{NAVY2}'/>
      <rect x='130' y='40' width='660' height='34' rx='12' fill='{NAVY}'/>
      <text x='460' y='64' text-anchor='middle' font-family='Heebo' font-weight='800' font-size='22' fill='#FFFFFF' direction='rtl'>{shop_name}</text>
      {stripes}
      <rect x='200' y='174' width='370' height='240' rx='14' fill='#0B1238' stroke='#C5CBEE' stroke-width='6'/>
      {tiles}
      <rect x='614' y='210' width='132' height='280' rx='12' fill='#0B1238' stroke='#C5CBEE' stroke-width='6'/>
      <circle cx='636' cy='352' r='7' fill='{T['acc']}'/>
      <rect x='0' y='486' width='{w}' height='74' rx='10' fill='#DDE2F6'/>
      {people}
    </svg>"""


def ad_storefront(spec):
    s = spec["image"]
    legend = (f"<div style='display:flex;gap:40px;font-size:28px;color:{LIGHT_SUB};font-weight:700'>"
              f"<span><span style='display:inline-block;width:22px;height:22px;border-radius:50%;background:{T['acc']};margin-left:10px;vertical-align:-3px'></span>{s['legend_in']}</span>"
              f"<span><span style='display:inline-block;width:22px;height:22px;border-radius:50%;background:{T['peri']};margin-left:10px;vertical-align:-3px'></span>{s['legend_out']}</span></div>")
    body = f"""<style>.lt mark{{color:{NAVY};background:linear-gradient(transparent 60%, {T['acc']} 60%, {T['acc']} 92%, transparent 92%)}}</style>
    <div class='lt' style='position:absolute;inset:0;background:{LIGHT_BG};color:{NAVY}'>
      <div style='position:absolute;top:0;left:0;right:0;height:14px;background:{T['acc']}'></div>
      <div style='position:absolute;top:66px;right:80px;left:80px;display:flex;justify-content:space-between;align-items:flex-start'>
        {logo_tile(84)}{pill(s['tag'], LIGHT_SUB, '#B9C1E6') if s.get('tag') else ''}</div>
      <div style='position:absolute;top:220px;right:80px;left:80px;display:flex;flex-direction:column;gap:16px'>
        <h1 style='font-size:66px;line-height:1.1;color:{NAVY}'>{s['head']}</h1>
        <div style='display:flex;flex-direction:column;gap:14px;align-items:center;margin-top:6px'>{storefront_svg(s['shop'])}{legend}
          <div style='font-size:22px;color:{LIGHT_SUB};align-self:flex-start'>{s.get('note', 'המחשה')}</div></div>
        <p style='font-size:33px;color:{NAVY};line-height:1.4;font-weight:400;margin-top:6px'>{s['value'].replace(' — ', '&nbsp;— ')}</p>
        <div>{cta_button(s['cta'])}</div>
      </div></div>"""
    return [body]


# ======================= 2. Calendar carousel =======================
DOW = ["א", "ב", "ג", "ד", "ה", "ו", "ש"]


def cal_page(title, marks, start=3, days=30):
    """Wall-calendar page. marks: {day: (kind, label)} kinds: discover | post | offer | need."""
    cells = "".join(f"<div style='font-size:22px;font-weight:800;color:{LIGHT_SUB};text-align:center'>{d}</div>" for d in DOW)
    cells += "<div></div>" * start
    for d in range(1, days + 1):
        kind, label = marks.get(d, (None, ""))
        style = f"background:#EEF1FB;color:{NAVY}"
        inner = f"<span style='font-size:23px;font-weight:700;line-height:1.1'>{d}</span>"
        if kind == "discover":
            style = f"background:{T['acc']};color:{NAVY3}"
        elif kind == "post":
            style = f"background:#C5CBEE;color:{NAVY}"
        elif kind == "offer":
            style = f"background:{NAVY2};color:#FFFFFF"
        elif kind == "need":
            style = f"background:#FFFFFF;color:{NAVY};box-shadow:0 0 0 6px {T['acc']}"
        if label:
            inner += f"<span style='font-size:21px;font-weight:800;line-height:1.05'>{label}</span>"
        cells += (f"<div style='{style};border-radius:12px;height:74px;display:flex;flex-direction:column;"
                  f"align-items:center;justify-content:center;gap:1px'>{inner}</div>")
    rings = "".join(f"<i style='width:22px;height:46px;border-radius:11px;background:{NAVY3};border:5px solid #8799DB'></i>"
                    for _ in range(6))
    return f"""<div style='position:relative;width:920px;background:#FFFFFF;border-radius:30px;padding:46px 34px 30px;
        box-shadow:0 30px 80px rgba(0,0,0,.35)'>
      <div style='position:absolute;top:-24px;left:90px;right:90px;display:flex;justify-content:space-between'>{rings}</div>
      <div style='display:flex;justify-content:space-between;align-items:baseline;margin-bottom:16px'>
        <div style='font-size:34px;font-weight:900;color:{NAVY}'>{title}</div>
        <div style='font-size:20px;color:{LIGHT_SUB}'>המחשה</div></div>
      <div style='display:grid;grid-template-columns:repeat(7,1fr);gap:8px;direction:rtl'>{cells}</div></div>"""


def ad_calendar(spec):
    slides = spec["slides"]; n = len(slides); out = []
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{T['acc'] if k <= i else T['line']}'></i>"
                       for k in range(n))
        if s.get("layout") == "end":
            body = f"""<div style='position:absolute;inset:0;padding:110px 90px;display:flex;flex-direction:column;justify-content:center;gap:40px'>
              {logo(280)}
              <h2 style='font-size:62px;line-height:1.2'>{s['head']}</h2>
              <p style='font-size:36px;color:{T['sub']}'>{s.get('body', '')}</p>
              <div>{cta_button(s['cta'])}</div><div>{pill(s['tag'], T['sub'], T['line']) if s.get('tag') else ''}</div></div>"""
        else:
            marks = {int(k): tuple(v) for k, v in s.get("marks", {}).items()}
            body = f"""<div style='position:absolute;top:56px;left:80px;right:80px;display:flex;gap:10px'>{dots}</div>
            <div style='position:absolute;top:100px;bottom:130px;right:80px;left:80px;display:flex;flex-direction:column;justify-content:center;gap:48px'>
              <div style='display:flex;flex-direction:column;gap:16px'>
              {f"<div style='font-size:34px;font-weight:900;color:{T['acc']}'>{s['kicker']}</div>" if s.get('kicker') else ''}
              <h2 style='font-size:{s.get('size', 70)}px;line-height:1.12'>{s['head']}</h2>
              <p style='font-size:36px;color:{T['sub']};line-height:1.4'>{s.get('body', '')}</p></div>
              <div style='margin-top:14px'>{cal_page(s['month'], marks, s.get('start', 3))}</div></div>
            <div style='position:absolute;bottom:44px;right:80px;display:flex;align-items:center;gap:30px'>{logo(80)}
              {f"<span style='font-size:24px;color:{T['sub']}'>{s['note']}</span>" if s.get('note') else ''}</div>"""
        out.append(body)
    return out


# ======================= 3. Shape-sorter video =======================
SHAPES = {
    "square": "<rect x='-62' y='-62' width='124' height='124' rx='16' fill='{c}'/>",
    "triangle": "<path d='M0 -72 L70 58 L-70 58 Z' fill='{c}' stroke='{c}' stroke-width='14' stroke-linejoin='round'/>",
    "star": "<path d='M0 -74 L20 -24 L72 -22 L31 10 L45 62 L0 32 L-45 62 L-31 10 L-72 -22 L-20 -24 Z' fill='{c}' stroke='{c}' stroke-width='8' stroke-linejoin='round'/>",
    "circle": "<circle r='64' fill='{c}'/>",
}


def video_page(spec):
    v = spec["video"]
    texts = "".join(
        f"<div class='txt' id='t{k}' style='opacity:0'>"
        f"{f'<div class=kick>{x[1]}</div>' if x[1] else ''}<h1 style='font-size:{x[2]}px'>{x[0]}</h1></div>"
        for k, x in enumerate([(b["head"], b.get("kicker", ""), b.get("size", 92)) for b in v["beats"]]))
    drift = ""
    rnd = random.Random(spec.get("seed", 11))
    kinds = ["square", "triangle", "star", "square", "triangle"]
    for k in range(22):
        sh = SHAPES[kinds[k % 5]].format(c=T['peri'])
        drift += (f"<g class='drift' data-x='{rnd.uniform(60, 1020):.0f}' data-sp='{rnd.uniform(90, 190):.0f}' "
                  f"data-ph='{rnd.uniform(0, 2000):.0f}' data-s='{rnd.uniform(.35, .6):.2f}' data-r='{rnd.uniform(-40, 40):.0f}' opacity='.18'>{sh}</g>")
    pieces = "".join(f"<g id='p{k}' opacity='0'>{SHAPES[p['shape']].format(c=T['acc'] if p['shape'] == 'circle' else '#8799DB')}</g>"
                     for k, p in enumerate(v["pieces"]))
    chips = "".join(
        f"<div class='chip' id='c{k}' style='opacity:0'><span class='dot'></span>{c}</div>" for k, c in enumerate(v["chips"]))
    end = v["end"]
    css = f"""
    .stage{{position:absolute;inset:0;background:radial-gradient(1200px 900px at 50% 62%, {NAVY2} 0%, {NAVY} 45%, {NAVY3} 100%)}}
    .txt{{position:absolute;top:290px;right:100px;left:100px}}
    .txt h1{{line-height:1.12}}
    .kick{{font-size:40px;font-weight:900;color:{T['acc']};margin-bottom:20px}}
    .chips{{position:absolute;top:760px;right:130px;left:130px;display:flex;flex-direction:column;gap:30px}}
    .chip{{display:flex;align-items:center;gap:26px;font-size:50px;font-weight:800;background:rgba(255,255,255,.07);
           border:2px solid {T['line']};border-radius:26px;padding:26px 34px}}
    .dot{{width:28px;height:28px;border-radius:50%;background:{T['acc']};flex:none}}
    #end{{position:absolute;inset:0;padding:300px 100px 420px;display:flex;flex-direction:column;justify-content:center;gap:40px;opacity:0}}
    #note{{position:absolute;bottom:430px;left:100px;font-size:26px;color:{T['sub']}}}
    """
    body = f"""<style>{css}</style><div class='stage'></div>
    <svg id='svg' width='1080' height='1920' viewBox='0 0 1080 1920' style='position:absolute;inset:0' xmlns='http://www.w3.org/2000/svg'>
      {drift}
      <g id='box' opacity='0'>
        <ellipse id='glow' cx='540' cy='1110' rx='300' ry='60' fill='{T['acc']}' opacity='0'/>
        <rect x='300' y='1100' width='480' height='330' rx='34' fill='{NAVY2}' stroke='#8799DB' stroke-width='6' id='boxrect'/>
        <path d='M300 1134 Q300 1100 334 1100 L746 1100 Q780 1100 780 1134 L740 1060 Q735 1040 712 1040 L368 1040 Q345 1040 340 1060 Z' fill='#22306E' stroke='#8799DB' stroke-width='6' stroke-linejoin='round'/>
        <ellipse cx='540' cy='1070' rx='92' ry='24' fill='{NAVY3}' stroke='#C5CBEE' stroke-width='4'/>
        <text x='540' y='1300' text-anchor='middle' font-family='Heebo' font-weight='900' font-size='54' fill='#FFFFFF'>{v['box_label']}</text>
        <image id='icon' href='{ICON}' x='490' y='1160' width='100' height='96' opacity='0'/>
      </g>
      {pieces}
    </svg>
    {texts}<div class='chips'>{chips}</div>
    <div id='note' style='opacity:0'>המחשה</div>
    <div id='brand' style='position:absolute;bottom:300px;right:100px;opacity:0'>{logo(110)}</div>
    <div id='end'>{logo(250)}
      <h1 style='font-size:{end.get('size', 64)}px;line-height:1.18'>{end['head'].replace(' — ', '&nbsp;— ')}</h1>
      <div id='cta' style='display:inline-block;align-self:flex-start;background:{T['acc']};color:{NAVY3};font-weight:800;font-size:46px;padding:26px 44px;border-radius:999px'>{end['cta']}</div>
      <span class='tag' style='font-size:30px;align-self:flex-start'>{end['tag']}</span></div>
    <script>
    const V = {json.dumps(v, ensure_ascii=False)};
    const cl=(x,a=0,b=1)=>Math.max(a,Math.min(b,x)), ease=u=>u<.5?2*u*u:1-Math.pow(-2*u+2,2)/2;
    const fade=(t,a,b,f=.35)=>cl((t-a)/f)*cl((b-t)/f);
    function render(t){{
      V.beats.forEach((b,k)=>{{const e=document.getElementById('t'+k);const o=fade(t,b.from,b.to);
        e.style.opacity=o; e.style.transform=`translateY(${{(1-cl((t-b.from)/.45))*30}}px)`;}});
      document.querySelectorAll('.drift').forEach(g=>{{const sp=+g.dataset.sp, y=2050-((t*sp+ +g.dataset.ph)%2300);
        g.setAttribute('transform',`translate(${{g.dataset.x}},${{y}}) rotate(${{g.dataset.r*t/3}}) scale(${{g.dataset.s}})`);
        g.setAttribute('opacity', ((.18+.2*cl((V.box.in-t)/.6))*cl((V.box.out- t)/.6)).toFixed(3));}});
      const bo=fade(t,V.box.in,V.box.out,.5); document.getElementById('box').setAttribute('opacity',bo.toFixed(3));
      document.getElementById('note').style.opacity=bo;
      V.pieces.forEach((p,k)=>{{const g=document.getElementById('p'+k); const u=t-p.at;
        if(u<0||u>2.0){{g.setAttribute('opacity',0);return;}}
        let x=540,y,r=0,s=1,o=1;
        if(u<.7){{const q=ease(u/.7); y=640+q*(p.shape=='circle'?430:350);}}
        else if(p.shape=='circle'){{const q=cl((u-.7)/.45); y=1070+q*40; s=1-.55*q; o=1-q;}}
        else{{const q=(u-.7)/1.1; x=540+p.dir*560*q; y=990-260*q+700*q*q; r=p.dir*220*q; o=cl(1-(q-.75)*4);}}
        g.setAttribute('opacity',o.toFixed(3)); g.setAttribute('transform',`translate(${{x}},${{y}}) rotate(${{r}}) scale(${{s}})`);}});
      const hit=V.pieces.find(p=>p.shape=='circle'); const hu=t-(hit.at+1.05);
      document.getElementById('glow').setAttribute('opacity',(cl(hu/.3)*cl((1.6-hu)/.6)*.35).toFixed(3));
      document.getElementById('icon').setAttribute('opacity',cl(hu/.3).toFixed(3));
      document.getElementById('boxrect').setAttribute('stroke', hu>0?'{T['acc']}':'#8799DB');
      V.chips.forEach((c,k)=>{{const e=document.getElementById('c'+k); const a=V.chip_at+k*V.chip_gap;
        const o=fade(t,a,V.chips_out,.35); e.style.opacity=o; e.style.transform=`translateX(${{(1-cl((t-a)/.4))*-40}}px)`;}});
      document.getElementById('brand').style.opacity=fade(t,.2,V.end.at,.4);
      document.getElementById('end').style.opacity=cl((t-V.end.at)/.5);
      document.getElementById('cta').style.transform=`scale(${{1+.04*Math.sin(Math.max(0,t-V.end.at-.8)*4)*cl(t-V.end.at-.8)}})`;
    }}
    </script>"""
    return body


async def ad_shape_video(spec, out):
    from playwright.async_api import async_playwright
    v = spec["video"]; fps = 30; total = v["seconds"]
    frames = out / "_frames"; frames.mkdir(exist_ok=True)
    for f in frames.glob("*"): f.unlink()
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page()
        await pg.set_viewport_size({"width": 1080, "height": 1920})
        await pg.set_content(html(1080, 1920, video_page(spec)), wait_until="load")
        await pg.evaluate("document.fonts.ready")
        if not await pg.evaluate("document.fonts.check('900 40px Heebo', 'אבג')"):
            raise RuntimeError("Hebrew font failed to load")
        n = int(total * fps)
        for i in range(n):
            await pg.evaluate(f"render({i / fps:.4f})")
            await pg.screenshot(path=str(frames / f"f_{i:04d}.jpg"), type="jpeg", quality=93)
        # cover = a still of the hook beat
        await pg.evaluate(f"render({v.get('cover_t', 2.0)})")
        await pg.screenshot(path=str(out / "cover.png"))
        await b.close()
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(out / "cover.png"), "-q:v", "2", str(out / "cover.jpg")], check=True)
    music = ROOT / spec["music"]
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(fps), "-i", str(frames / "f_%04d.jpg"),
                    "-i", str(music), "-filter_complex",
                    f"[1:a]atrim=0:{total},afade=t=in:d=0.4,afade=t=out:st={total - 1.8}:d=1.8,volume=0.85[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-crf", "19", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "160k", "-t", str(total), "-movflags", "+faststart", str(out / "reel.mp4")], check=True)
    for f in frames.glob("*"): f.unlink()
    frames.rmdir()
    (out / "subtitles.srt").write_text("\n".join(
        f"{k + 1}\n{_ts(bt['from'])} --> {_ts(bt['to'])}\n{bt['head'].replace('<br>', ' ').replace('<mark>', '').replace('</mark>', '')}\n"
        for k, bt in enumerate(v["beats"])), encoding="utf-8")


def _ts(t):
    ms = int(round(t * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"
