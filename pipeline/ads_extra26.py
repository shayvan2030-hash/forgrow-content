"""Extra ad layouts, set 26 (added 2026-11-20).

ad_heartjar — carousel on a pale lilac background with a faint dot grid: a glass jar overflowing with hearts (likes).
          Business problem: the owner chases likes with trendy, entertaining posts; the jar fills with hearts, but the
          people who liked the video mostly keep scrolling and nobody asks about the service. A relevant audience is
          interested in what the business offers and walks the path to the door
          (discover -> follow -> keep seeing -> understand the offer -> maybe reach out).
          Route shown as five numbered stepping stones leading to a shop door. Illustration only.
          Original logo on a navy tile.
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
MINT_L = "#B5F1DF"
INK = "#101B4F"
MINT_D = "#0B7F62"
GREY = "#D9DBE4"
GREY_D = "#6E7390"
SUB = "#33407F"
PINK = "#F3A5B6"
PINK_D = "#D9738B"
GLASS = "#EAF4FB"
WOOD = "#C98B5E"
STONE = "#C9CCD8"
SAND = "#EADCC3"


def label(x, y, txt, fill, size=34):
    return (f"<text x='{x}' y='{y}' font-family='Heebo' font-weight='900' font-size='{size}' text-anchor='middle' "
            f"fill='{fill}' direction='rtl'>{txt}</text>")


def heart(cx, cy, s, fill=PINK, stroke=INK, rot=0, sw=3):
    return (f"<path transform='translate({cx:.1f} {cy:.1f}) rotate({rot}) scale({s / 40:.3f})' "
            f"d='M 0,14 C -26,-4 -22,-26 -9,-26 C -3,-26 0,-21 0,-17 C 0,-21 3,-26 9,-26 C 22,-26 26,-4 0,14 Z' "
            f"fill='{fill}' stroke='{stroke}' stroke-width='{sw * 40 / s:.2f}' stroke-linejoin='round'/>")


def person(cx, by, h, fill, stroke=INK, op=1):
    r = h * 0.17
    hy = by - h + r
    bw = h * 0.52
    return (f"<g opacity='{op}'><path d='M {cx - bw / 2:.1f},{by:.1f} Q {cx - bw / 2:.1f},{hy + r * 1.5:.1f} {cx:.1f},{hy + r * 1.5:.1f} "
            f"Q {cx + bw / 2:.1f},{hy + r * 1.5:.1f} {cx + bw / 2:.1f},{by:.1f} Z' fill='{fill}' stroke='{stroke}' stroke-width='4'/>"
            f"<circle cx='{cx:.1f}' cy='{hy:.1f}' r='{r:.1f}' fill='{fill}' stroke='{stroke}' stroke-width='4'/></g>")


def jar(cx, by, w, h, tag="לייקים", spill=True):
    """Glass jar standing on y=by, full of grey-pink hearts, a few spilling over the rim."""
    x0, x1 = cx - w / 2, cx + w / 2
    top = by - h
    neck = w * 0.78
    g = f"<ellipse cx='{cx:.1f}' cy='{by:.1f}' rx='{w * .6:.1f}' ry='{w * .06:.1f}' fill='{INK}' opacity='.13'/>"
    body = (f"M {cx - neck / 2:.1f},{top + h * .1:.1f} C {x0:.1f},{top + h * .16:.1f} {x0:.1f},{top + h * .2:.1f} {x0:.1f},{top + h * .3:.1f} "
            f"V {by - w * .08:.1f} Q {x0:.1f},{by:.1f} {x0 + w * .08:.1f},{by:.1f} H {x1 - w * .08:.1f} Q {x1:.1f},{by:.1f} {x1:.1f},{by - w * .08:.1f} "
            f"V {top + h * .3:.1f} C {x1:.1f},{top + h * .2:.1f} {x1:.1f},{top + h * .16:.1f} {cx + neck / 2:.1f},{top + h * .1:.1f} Z")
    g += f"<path d='{body}' fill='{GLASS}' stroke='{INK}' stroke-width='5'/>"
    g += f"<clipPath id='jc{int(cx)}{int(by)}'><path d='{body}'/></clipPath><g clip-path='url(#jc{int(cx)}{int(by)})'>"
    s = w * 0.16
    rows = int((h * 0.95) / (s * 0.8))
    k = 0
    for r in range(rows):
        y = by - s * .45 - r * s * .78
        off = (r % 2) * s * .5
        x = x0 + s * .3 + off
        while x < x1 + s * .2:
            fill = PINK if (k * 7 + r) % 3 else GREY
            g += heart(x, y, s, fill=fill, rot=((k * 37) % 50) - 25, sw=2.5)
            x += s * .95; k += 1
    g += "</g>"
    g += f"<path d='M {x0 + w * .1:.1f},{top + h * .35:.1f} V {by - w * .15:.1f}' stroke='#FFFFFF' stroke-width='10' stroke-linecap='round' opacity='.7'/>"
    # rim
    g += f"<rect x='{cx - neck / 2 - 8:.1f}' y='{top:.1f}' width='{neck + 16:.1f}' height='{h * .1:.1f}' rx='10' fill='{GLASS}' stroke='{INK}' stroke-width='5'/>"
    if spill:
        for dx, dy, rot in ((-.28, -.06, -20), (-.05, -.12, 8), (.22, -.05, 18), (.5, .25, 30), (.62, .62, -12), (-.58, .5, 15)):
            g += heart(cx + dx * w, top + dy * h, s * 1.05, fill=PINK if dx < .4 else GREY, rot=rot)
    if tag:
        g += (f"<g transform='rotate(-5 {cx:.1f} {top + h * .55:.1f})'><rect x='{cx - w * .3:.1f}' y='{top + h * .47:.1f}' width='{w * .6:.1f}' height='{h * .15:.1f}' rx='10' "
              f"fill='#FFFFFF' stroke='{INK}' stroke-width='4'/>{label(cx, top + h * .47 + h * .115, tag, INK, h * .085)}</g>")
    return g


def door(cx, by, w, h, open_=False, glow=True):
    """Shop front: wall chunk with a mint striped awning and a door; open_ shows mint light inside."""
    ww = w * 1.6
    g = f"<rect x='{cx - ww / 2:.1f}' y='{by - h * 1.1:.1f}' width='{ww:.1f}' height='{h * 1.1:.1f}' fill='#FFFFFF' stroke='{INK}' stroke-width='5'/>"
    # awning
    ay = by - h * 1.1
    n = 6; sw_ = (ww + 30) / n
    for i in range(n):
        f = MINT if i % 2 == 0 else "#FFFFFF"
        g += f"<path d='M {cx - ww / 2 - 15 + i * sw_:.1f},{ay:.1f} h {sw_:.1f} v {h * .14:.1f} q {-sw_ / 2:.1f},{h * .08:.1f} {-sw_:.1f},0 Z' fill='{f}' stroke='{INK}' stroke-width='4'/>"
    dx, dy, dw, dh = cx - w / 2, by - h * .8, w, h * .8
    inside = MINT_L if open_ else NAVY
    g += f"<rect x='{dx:.1f}' y='{dy:.1f}' width='{dw:.1f}' height='{dh:.1f}' fill='{inside}' stroke='{INK}' stroke-width='5'/>"
    if open_:
        if glow:
            g += f"<path d='M {dx:.1f},{by:.1f} L {dx - w * .5:.1f},{by + h * .12:.1f} H {dx + dw + w * .5:.1f} L {dx + dw:.1f},{by:.1f} Z' fill='{MINT}' opacity='.35'/>"
        g += (f"<path d='M {dx + dw:.1f},{dy:.1f} L {dx + dw + w * .32:.1f},{dy + h * .06:.1f} V {by + h * .04:.1f} L {dx + dw:.1f},{by:.1f} Z' "
              f"fill='{WOOD}' stroke='{INK}' stroke-width='5' stroke-linejoin='round'/>")
    else:
        g += (f"<rect x='{dx + 10:.1f}' y='{dy + 10:.1f}' width='{dw - 20:.1f}' height='{dh * .4:.1f}' fill='{GLASS}' stroke='{INK}' stroke-width='3'/>"
              f"<circle cx='{dx + dw - 22:.1f}' cy='{dy + dh * .58:.1f}' r='7' fill='{MINT}' stroke='{INK}' stroke-width='3'/>")
    return g


def stone(cx, cy, w, fill=STONE, num=None, dash=False, stroke=INK):
    d = " stroke-dasharray='10 7'" if dash else ""
    g = f"<ellipse cx='{cx:.1f}' cy='{cy:.1f}' rx='{w / 2:.1f}' ry='{w * .3:.1f}' fill='{fill}' stroke='{stroke}' stroke-width='4'{d}/>"
    if num:
        g += label(cx, cy + w * .11, num, INK, w * .32)
    return g


def arrow(x1, y, x2, color=GREY_D):
    s = 1 if x2 > x1 else -1
    return (f"<line x1='{x1}' y1='{y}' x2='{x2}' y2='{y}' stroke='{color}' stroke-width='5' stroke-linecap='round' stroke-dasharray='12 10'/>"
            f"<path d='M {x2 - s * 18},{y - 14} L {x2},{y} L {x2 - s * 18},{y + 14}' fill='none' stroke='{color}' stroke-width='5' stroke-linecap='round' stroke-linejoin='round'/>")


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='650' viewBox='0 0 {w} 650'>"
        g += jar(470, 600, 330, 470)
        g += f"<circle cx='790' cy='190' r='40' fill='#FFFFFF' stroke='{GREY_D}' stroke-width='4'/>" + label(790, 205, "?", GREY_D, 46)
        g += (f"<g transform='translate(150 210)'><rect x='-80' y='-40' width='160' height='80' rx='40' fill='#FFFFFF' stroke='{INK}' stroke-width='4'/>"
              f"{heart(-38, 6, 34, fill=PINK)}<text x='22' y='14' font-family='Heebo' font-weight='900' font-size='34' text-anchor='middle' fill='{INK}' direction='ltr' unicode-bidi='bidi-override'>+1</text></g>")
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='800' viewBox='0 0 {w} 800'>"
        g += f"<line x1='470' y1='20' x2='470' y2='640' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        # right (read first): a jar full of hearts, grey people liked it and keep scrolling past
        g += jar(705, 400, 210, 320, tag=None)
        for x, op in ((600, .95), (720, .75), (840, .55)):
            g += person(x, 600, 140, GREY, op=op)
        g += arrow(560, 440, 900)
        g += label(705, 690, "אהבו את הסרטון", INK, 36) + label(705, 738, "וממשיכים לגלול", SUB, 29)
        # left: shop door with mint awning, mint people walk the stepping stones towards it
        g += door(235, 400, 120, 240, open_=True)
        for i, (x, y) in enumerate(((235, 445), (180, 500), (250, 555))):
            g += stone(x, y, 90 - i * 0, fill=SAND)
        g += person(80, 600, 140, MINT) + person(395, 600, 140, MINT)
        g += label(235, 690, "קהל רלוונטי", MINT_D, 36) + label(235, 738, "מתעניין במה שאתם מציעים", SUB, 29)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; n = len(labels); rows = ""
        for i, l in enumerate(labels):
            last = i == n - 1
            fill = "#FFFFFF" if last else (MINT if i % 2 == 0 else MINT_L)
            t = (f"<svg width='140' height='84' viewBox='0 0 140 84' style='flex:none'>"
                 f"{stone(70, 42, 124, fill=fill, num=str(i + 1), dash=last, stroke=MINT_D if last else INK)}</svg>")
            rows += (f"<div style='display:flex;align-items:center;gap:26px'>{t}"
                     f"<span style='font-size:42px;font-weight:900;color:{SUB if last else INK}'>{l}</span></div>")
        return (f"<div style='width:840px;background:#FFFFFF;border:6px solid {INK};border-radius:20px;overflow:hidden;"
                f"box-shadow:12px 14px 0 rgba(16,27,79,.14)'>"
                f"<div style='background:{NAVY};color:#fff;font-size:32px;font-weight:900;padding:18px 34px;display:flex;align-items:center;gap:18px'>"
                f"<span style='width:18px;height:18px;border-radius:50%;background:{MINT};flex:none'></span>אבן אחרי אבן, עד הדלת</div>"
                f"<div style='padding:22px 40px 26px 40px;display:flex;flex-direction:column;gap:10px'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='600' viewBox='0 0 {w} 600'>"
        g += door(470, 420, 170, 320, open_=True)
        for x, y, s in ((470, 470, 100), (400, 515, 110), (480, 562, 120)):
            g += stone(x, y, s, fill=SAND)
        for x, h, f in ((150, 160, MINT), (260, 140, MINT_L), (690, 140, MINT_L), (800, 160, MINT)):
            g += person(x, 590, h, f)
        return g + "</svg>"
    return ""


def dotgrid(end=False):
    dots = "".join(f"<circle cx='{x}' cy='{y}' r='2.6' fill='#8799DB'/>" for x in range(30, 1080, 54) for y in range(30, 1350, 54))
    return f"<svg style='position:absolute;inset:0;opacity:{.22 if end else .32}' width='1080' height='1350'>{dots}</svg>"


def ad_heartjar(spec):
    slides = spec["slides"]; n = len(slides); out = []
    bg = "background:#F3EFFA"
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT_D if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        end = s.get("layout") == "end"
        wrap = (f"<style>.hj mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='hj' style='position:absolute;inset:0;overflow:hidden;color:{INK};{bg}'>{dotgrid(end)}")
        tl = f"<div style='background:{NAVY};border-radius:22px;padding:14px 22px;display:inline-flex'>{logo(52)}</div>"
        if end:
            body = wrap + f"""<div style='position:absolute;inset:0;padding:110px 90px;display:flex;flex-direction:column;justify-content:center;gap:40px'>
              <div style='background:{NAVY};border-radius:30px;padding:24px 34px;align-self:flex-start;display:flex'>{logo(110)}</div>
              <h2 style='font-size:{s.get('size', 60)}px;line-height:1.2'>{s['head']}</h2>
              <p style='font-size:36px;color:{SUB};font-weight:700'>{s.get('body', '')}</p>
              <div><div style='display:inline-block;background:{MINT};color:{NAVY3};font-weight:800;font-size:40px;padding:24px 44px;border-radius:999px;box-shadow:0 6px 0 {INK}'>{s['cta']}</div></div>
              <div><span style='display:inline-block;font-size:26px;font-weight:700;padding:8px 20px;border-radius:999px;border:2px solid {SUB};color:{SUB};background:#FFFFFF'>{s.get('tag', '')}</span></div></div></div>"""
        else:
            st = (f"<div style='position:absolute;right:96px;bottom:{s.get('stamp_bottom', 640)}px;transform:rotate(-4deg);background:{NAVY};"
                  f"color:#fff;border-radius:10px;padding:6px;box-shadow:6px 8px 0 rgba(16,27,79,.15)'>"
                  f"<div style='border:3px solid {MINT};border-radius:6px;padding:8px 26px;font-size:38px;font-weight:900'>{s['stamp']}</div></div>"
                  if s.get("stamp") else "")
            body = wrap + f"""<div style='position:absolute;top:56px;left:80px;right:80px;display:flex;gap:10px'>{dots}</div>
            <div style='position:absolute;top:112px;right:80px;left:80px;display:flex;flex-direction:column;gap:14px'>
              {f"<div style='font-size:32px;font-weight:900;color:{MINT_D}'>{s['kicker']}</div>" if s.get('kicker') else ''}
              <h2 style='font-size:{s.get('size', 62)}px;line-height:1.12'>{s['head']}</h2>
              {f"<p style='font-size:33px;color:{SUB};line-height:1.4;font-weight:700'>{s['body']}</p>" if s.get('body') else ''}</div>
            <div style='position:absolute;top:{s.get('scene_top', 420)}px;bottom:{s.get('scene_bottom', 130)}px;left:0;right:0;display:flex;justify-content:center;align-items:center'>{scene(s['scene'])}</div>{st}
            <div style='position:absolute;bottom:40px;right:80px;left:80px;display:flex;justify-content:space-between;align-items:center'>{tl}
              <span style='font-size:24px;color:{SUB};font-weight:700;background:#FFFFFF;border-radius:6px;padding:2px 10px'>{spec.get('note', 'המחשה')}</span></div></div>"""
        out.append(body)
    return out
