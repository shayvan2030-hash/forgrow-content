"""Extra ad layouts, set 16 (added 2026-11-09). Imported by ads.py.

ad_busstop — carousel on pale rose background: a bus-stop sign by the road. Grey buses pass by without stopping;
             one mint bus stops and mint passengers get off. Route shown as a vertical metro-style line with five
             stations. Illustration only. Original logo on a navy tile.
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
BG = "#FDE6EF"
INK = "#101B4F"
MINT_D = "#0E8F6E"
GREY = "#B9B4AC"
ROAD = "#6B7399"


def bus(x, y, fill, flip=1):
    wins = "".join(f"<rect x='{-96 + k * 52}' y='-46' width='40' height='34' rx='6' fill='#fff' stroke='{INK}' stroke-width='4'/>" for k in range(4))
    return (f"<g transform='translate({x} {y}) scale({flip} 1)'>"
            f"<rect x='-120' y='-70' width='240' height='110' rx='24' fill='{fill}' stroke='{INK}' stroke-width='6'/>{wins}"
            f"<circle cx='-62' cy='42' r='20' fill='{INK}'/><circle cx='62' cy='42' r='20' fill='{INK}'/>"
            f"<circle cx='-62' cy='42' r='7' fill='#fff'/><circle cx='62' cy='42' r='7' fill='#fff'/></g>")


def person(x, y, fill):
    return (f"<circle cx='{x}' cy='{y - 34}' r='15' fill='{fill}' stroke='{INK}' stroke-width='4'/>"
            f"<path d='M{x - 18} {y + 22} v-24 a18 18 0 0 1 36 0 v24 Z' fill='{fill}' stroke='{INK}' stroke-width='4' stroke-linejoin='round'/>")


def sign(x, y, fill=MINT):
    return (f"<rect x='{x - 4}' y='{y}' width='8' height='150' fill='{INK}'/>"
            f"<circle cx='{x}' cy='{y}' r='38' fill='{fill}' stroke='{INK}' stroke-width='6'/>"
            f"<text x='{x}' y='{y + 14}' font-family='Heebo' font-weight='900' font-size='40' text-anchor='middle' fill='{INK}'>H</text>")


def road(y, w):
    return (f"<rect x='0' y='{y}' width='{w}' height='56' fill='{ROAD}'/>"
            f"<line x1='0' y1='{y + 28}' x2='{w}' y2='{y + 28}' stroke='#fff' stroke-width='5' stroke-dasharray='34 26'/>")


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='520' viewBox='0 0 {w} 520'>"
        g += road(330, w)
        g += bus(250, 290, GREY) + bus(720, 290, GREY, -1)
        g += sign(470, 80)
        g += person(420, 255, "#C5CBEE") + person(520, 255, "#C5CBEE")
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='640' viewBox='0 0 {w} 640'>"
        g += road(130, w) + bus(250, 90, GREY) + bus(700, 90, GREY, -1)
        g += f"<text x='{w / 2}' y='235' font-family='Heebo' font-weight='900' font-size='34' text-anchor='middle' fill='{INK}'>אוטובוס שלא מתאים: ממשיך בלי לעצור</text>"
        g += road(430, w) + bus(470, 390, MINT)
        g += person(150, 385, MINT) + person(250, 385, MINT) + person(770, 385, MINT)
        g += sign(870, 250)
        g += f"<text x='{w / 2}' y='620' font-family='Heebo' font-weight='900' font-size='34' text-anchor='middle' fill='{MINT_D}'>קהל רלוונטי: יש מי שיורד בתחנה</text>"
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; rows = ""
        for i, l in enumerate(labels):
            rows += (f"<div style='display:flex;align-items:center;gap:30px;height:92px;position:relative;z-index:1'>"
                     f"<span style='flex:none;width:52px;height:52px;border-radius:50%;background:{MINT if i else '#fff'};border:8px solid {INK}'></span>"
                     f"<span style='font-size:44px;font-weight:900;color:{INK}'>{l}</span></div>")
        return (f"<div style='position:relative;width:820px'>"
                f"<div style='position:absolute;right:30px;top:46px;bottom:46px;width:14px;background:{INK};border-radius:7px'></div>{rows}</div>")
    if k == "one":
        g = f"<svg width='{w}' height='460' viewBox='0 0 {w} 460'>"
        g += road(300, w) + bus(400, 260, MINT)
        g += person(130, 255, MINT) + person(230, 255, MINT) + person(780, 255, MINT)
        g += sign(870, 70)
        return g + "</svg>"
    return ""


def ad_busstop(spec):
    slides = spec["slides"]; n = len(slides); out = []
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.bs mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='bs' style='position:absolute;inset:0;overflow:hidden;background:{BG};color:{INK}'>")
        tl = f"<div style='background:{NAVY};border-radius:22px;padding:14px 22px;display:inline-flex'>{logo(52)}</div>"
        if s.get("layout") == "end":
            body = wrap + f"""<div style='position:absolute;inset:0;padding:110px 90px;display:flex;flex-direction:column;justify-content:center;gap:40px'>
              <div style='background:{NAVY};border-radius:30px;padding:24px 34px;align-self:flex-start;display:flex'>{logo(110)}</div>
              <h2 style='font-size:{s.get('size', 60)}px;line-height:1.2'>{s['head']}</h2>
              <p style='font-size:36px;color:#3C4A8F;font-weight:700'>{s.get('body', '')}</p>
              <div><div style='display:inline-block;background:{MINT};color:{NAVY3};font-weight:800;font-size:40px;padding:24px 44px;border-radius:999px'>{s['cta']}</div></div>
              <div><span style='display:inline-block;font-size:26px;font-weight:700;padding:8px 20px;border-radius:999px;border:2px solid #3C4A8F;color:#3C4A8F'>{s.get('tag', '')}</span></div></div></div>"""
        else:
            stamp = (f"<div style='position:absolute;right:100px;bottom:{s.get('stamp_bottom', 640)}px;transform:rotate(7deg);border:6px solid {MINT_D};"
                     f"color:{MINT_D};border-radius:18px;padding:8px 26px;font-size:40px;font-weight:900;background:{BG}'>{s['stamp']}</div>"
                     if s.get("stamp") else "")
            body = wrap + f"""<div style='position:absolute;top:56px;left:80px;right:80px;display:flex;gap:10px'>{dots}</div>
            <div style='position:absolute;top:112px;right:80px;left:80px;display:flex;flex-direction:column;gap:14px'>
              {f"<div style='font-size:32px;font-weight:900;color:{MINT_D}'>{s['kicker']}</div>" if s.get('kicker') else ''}
              <h2 style='font-size:{s.get('size', 62)}px;line-height:1.12'>{s['head']}</h2>
              {f"<p style='font-size:33px;color:#3C4A8F;line-height:1.4;font-weight:700'>{s['body']}</p>" if s.get('body') else ''}</div>
            <div style='position:absolute;top:{s.get('scene_top', 420)}px;bottom:{s.get('scene_bottom', 130)}px;left:0;right:0;display:flex;justify-content:center;align-items:center'>{scene(s['scene'])}</div>{stamp}
            <div style='position:absolute;bottom:40px;right:80px;left:80px;display:flex;justify-content:space-between;align-items:center'>{tl}
              <span style='font-size:24px;color:#3C4A8F;font-weight:700'>{spec.get('note', 'המחשה')}</span></div></div>"""
        out.append(body)
    return out
