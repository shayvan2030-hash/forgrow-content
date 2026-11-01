"""Extra ad layouts, set 8 (added 2026-11-01). Imported by ads.py.

ad_lighthouse — carousel on night navy: a lighthouse at sea. A light shining every day does not mean the right boats
                see it; boats that are on their way to the business's harbour (a relevant audience) notice the light and
                move through stages: discover -> follow -> keep seeing -> understand the offer -> may reach out.
                Illustration only: no numbers or results. Original logo is used as supplied (white on navy).
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY2, NAVY3

MINT = T["acc"]
BG = "#0A1238"
SEA = "#14246A"
PERI = "#8799DB"


def boat(x, y, s=1.0, color=PERI, flip=False, op=1.0):
    f = -1 if flip else 1
    return (f"<g transform='translate({x} {y}) scale({f * s} {s})' opacity='{op}'>"
            f"<path d='M-46 0 h92 l-16 26 h-60z' fill='{color}'/>"
            f"<rect x='-3' y='-70' width='6' height='70' fill='{color}'/>"
            f"<path d='M8 -66 L8 -8 L52 -8z' fill='#FFFFFF' opacity='.92'/>"
            f"<path d='M-8 -56 L-8 -8 L-40 -8z' fill='{color}' opacity='.8'/></g>")


def tower(x, y, h=330, glow=True):
    w0, w1 = 120, 72
    top = y - h
    stripes = "".join(
        f"<path d='M{x - w0 / 2 + (w0 - w1) / 2 * (k / 5):.1f} {y - h * k / 5 - h / 5:.1f} h{w0 - (w0 - w1) * (k / 5) - (w0 - w1) / 5:.1f} "
        f"l{(w0 - w1) / 10:.1f} {h / 5:.1f} h-{w0 - (w0 - w1) * k / 5:.1f}z' fill='{MINT}' opacity='0'/>" for k in range(0))
    return (f"<path d='M{x - w0 / 2} {y} L{x - w1 / 2} {top} H{x + w1 / 2} L{x + w0 / 2} {y}z' fill='#FFFFFF'/>"
            f"<path d='M{x - w0 / 2 + 9} {y - h * .34} L{x - w1 / 2 - 5} {y - h * .52} H{x + w1 / 2 + 5} L{x + w0 / 2 - 9} {y - h * .34}z' fill='{NAVY}' transform='translate(0 {-h * .0})' opacity='.0'/>"
            f"<path d='M{x - 63} {y - h * .30} h126 l-9 {h * .15:.0f} h-108z' fill='{MINT}'/>"
            f"<path d='M{x - 52} {y - h * .62} h104 l-8 {h * .15:.0f} h-88z' fill='{MINT}'/>"
            f"<rect x='{x - 52}' y='{top - 12}' width='104' height='16' rx='6' fill='{NAVY}'/>"
            f"<rect x='{x - 34}' y='{top - 58}' width='68' height='48' rx='8' fill='#FFE9A8'/>"
            f"<path d='M{x - 44} {top - 58} L{x} {top - 100} L{x + 44} {top - 58}z' fill='{NAVY}'/>"
            f"<rect x='{x - 17}' y='{y - 70}' width='34' height='70' rx='17' fill='{NAVY}'/>")


def lighthouse_scene(boats, w=1080, h=640, beam_op=.34):
    x, ground = 830, 520
    top = ground - 330 - 34
    beam = (f"<defs><linearGradient id='bm' x1='1' y1='0' x2='0' y2='0'><stop offset='0' stop-color='#FFE9A8' stop-opacity='.95'/>"
            f"<stop offset='1' stop-color='#FFE9A8' stop-opacity='0'/></linearGradient></defs>"
            f"<path d='M{x - 30} {top} L40 {top - 150} L40 {top + 330} Z' fill='url(#bm)' opacity='{beam_op * 2.2}'/>")
    sea = (f"<rect x='0' y='{ground - 6}' width='{w}' height='{h - ground + 6}' fill='{SEA}'/>"
           + "".join(f"<path d='M{a} {ground + 40 + k * 34} q30 -14 60 0 t60 0' stroke='{PERI}' stroke-opacity='.35' stroke-width='4' fill='none'/>"
                     for k in range(3) for a in range(20 + (k % 2) * 40, w, 190)))
    rock = f"<path d='M{x - 130} {ground + 4} q20 -52 130 -52 q110 0 130 52z' fill='#0E1A55'/>"
    return (f"<svg width='{w}' height='{h}' viewBox='0 0 {w} {h}'>{beam}{sea}{rock}{tower(x, ground - 30)}{boats}</svg>")


def stage_row(labels):
    """Vertical route: five lights that get brighter, joined by a dashed line (no numbers, just stages)."""
    rows = ""
    for i, l in enumerate(labels):
        r = 18 + i * 5
        lit = i >= 1
        orb = (f"<svg width='110' height='110' viewBox='0 0 110 110'>"
               f"<circle cx='55' cy='55' r='{r + 14}' fill='{MINT if lit else PERI}' opacity='{.16 + i * .06:.2f}'/>"
               f"<circle cx='55' cy='55' r='{r}' fill='{MINT if lit else '#FFE9A8'}'/></svg>")
        rows += (f"<div style='display:flex;align-items:center;gap:30px;height:118px'>"
                 f"<div style='width:110px;flex:none;display:flex;justify-content:center'>{orb}</div>"
                 f"<div style='font-size:42px;font-weight:900;color:#FFFFFF'>{l}</div></div>")
    line = f"<div style='position:absolute;right:54px;top:60px;bottom:60px;border-right:5px dashed {MINT};opacity:.5'></div>"
    return f"<div style='position:relative;width:900px;display:flex;flex-direction:column'>{line}{rows}</div>"


def scene(sc):
    k = sc["kind"]
    if k == "lost":      # boats sailing away from the light, none reach it
        b = (boat(150, 470, .9, PERI, op=.7) + boat(330, 410, .7, PERI, True, .55) + boat(250, 560, 1.0, PERI, True, .75)
             + boat(520, 570, .8, PERI, op=.7))
        return lighthouse_scene(b)
    if k == "found":     # relevant boats turning toward the light
        b = (boat(150, 470, .8, PERI, True, .5) + boat(250, 560, .9, PERI, op=.5)
             + boat(420, 430, 1.0, MINT) + boat(520, 575, 1.05, MINT))
        return lighthouse_scene(b, beam_op=.42)
    if k == "row":
        return stage_row(sc["labels"])
    if k == "one":       # closing: boat docked near lighthouse
        return lighthouse_scene(boat(560, 570, 1.1, MINT) + boat(380, 540, .9, MINT, op=.9), beam_op=.5)
    return ""


def ad_lighthouse(spec):
    slides = spec["slides"]; n = len(slides); out = []
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT if k <= i else 'rgba(255,255,255,.2)'}'></i>"
                       for k in range(n))
        stars = "".join(f"<i style='position:absolute;left:{(k * 197) % 1000}px;top:{(k * 89) % 520}px;width:{3 + k % 3}px;height:{3 + k % 3}px;"
                        f"border-radius:50%;background:#fff;opacity:{.25 + (k % 4) * .12:.2f}'></i>" for k in range(26))
        wrap = (f"<style>.lh mark{{color:{MINT};background:none}}</style>"
                f"<div class='lh' style='position:absolute;inset:0;overflow:hidden;background:linear-gradient(180deg,{BG} 0%,#101B4F 100%);color:#fff'>{stars}")
        if s.get("layout") == "end":
            body = wrap + f"""<div style='position:absolute;inset:0;padding:110px 90px;display:flex;flex-direction:column;justify-content:center;gap:40px'>
              {logo(300)}
              <h2 style='font-size:{s.get('size', 60)}px;line-height:1.2'>{s['head']}</h2>
              <p style='font-size:36px;color:{PERI};font-weight:700'>{s.get('body', '')}</p>
              <div><div style='display:inline-block;background:{MINT};color:{NAVY3};font-weight:800;font-size:40px;padding:24px 44px;border-radius:999px'>{s['cta']}</div></div>
              <div><span style='display:inline-block;font-size:26px;font-weight:700;padding:8px 20px;border-radius:999px;border:2px solid {PERI};color:{PERI}'>{s.get('tag', '')}</span></div></div></div>"""
        else:
            stamp = (f"<div style='position:absolute;right:100px;bottom:{s.get('stamp_bottom', 640)}px;transform:rotate(7deg);border:6px solid {MINT};"
                     f"color:{MINT};border-radius:18px;padding:8px 26px;font-size:40px;font-weight:900;background:rgba(10,18,56,.9)'>{s['stamp']}</div>"
                     if s.get("stamp") else "")
            body = wrap + f"""<div style='position:absolute;top:56px;left:80px;right:80px;display:flex;gap:10px'>{dots}</div>
            <div style='position:absolute;top:112px;right:80px;left:80px;display:flex;flex-direction:column;gap:14px'>
              {f"<div style='font-size:32px;font-weight:900;color:{MINT}'>{s['kicker']}</div>" if s.get('kicker') else ''}
              <h2 style='font-size:{s.get('size', 62)}px;line-height:1.12'>{s['head']}</h2>
              {f"<p style='font-size:33px;color:#C5CBEE;line-height:1.4;font-weight:700'>{s['body']}</p>" if s.get('body') else ''}</div>
            <div style='position:absolute;bottom:{s.get('scene_bottom', 120)}px;left:0;right:0;display:flex;justify-content:center'>{scene(s['scene'])}</div>{stamp}
            <div style='position:absolute;bottom:40px;right:80px;left:80px;display:flex;justify-content:space-between;align-items:center'>{logo(60)}
              <span style='font-size:24px;color:{PERI};font-weight:700'>{spec.get('note', 'המחשה')}</span></div></div>"""
        out.append(body)
    return out
