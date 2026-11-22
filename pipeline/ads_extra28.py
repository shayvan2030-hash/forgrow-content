"""Extra ad layouts, set 28 (added 2026-11-22).

ad_compass — carousel on a parchment map background with faint topographic contour lines: a hiking compass.
          Business problem: a new business starts on Instagram from zero and chases whatever brings quick numbers —
          a trend, a giveaway, friends of friends — so the needle keeps spinning and there is no clear direction.
          A relevant audience gives one direction, from which a route can start
          (discover -> follow -> keep seeing -> understand the offer -> maybe reach out).
          Route shown as five numbered map pins. Illustration only. Original logo on a navy tile.
"""
import math

from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
MINT_L = "#B5F1DF"
INK = "#101B4F"
MINT_D = "#0B7F62"
GREY = "#D3D5DE"
GREY_D = "#6E7390"
SUB = "#33407F"
PAPER = "#F4EEDF"
RED = "#E2574C"


def label(x, y, txt, fill, size=34, weight=900):
    return (f"<text x='{x}' y='{y}' font-family='Heebo' font-weight='{weight}' font-size='{size}' text-anchor='middle' "
            f"fill='{fill}' direction='rtl'>{txt}</text>")


def needle(r, ang, tip=MINT, tail="#FFFFFF", op=1):
    """Diamond needle centred at 0,0, tip pointing at `ang` degrees (0 = up, clockwise)."""
    w = r * .2
    return (f"<g transform='rotate({ang})' opacity='{op}'>"
            f"<path d='M 0,{-r:.1f} L {w:.1f},0 L {-w:.1f},0 Z' fill='{tip}' stroke='{INK}' stroke-width='4' stroke-linejoin='round'/>"
            f"<path d='M 0,{r:.1f} L {w:.1f},0 L {-w:.1f},0 Z' fill='{tail}' stroke='{INK}' stroke-width='4' stroke-linejoin='round'/></g>")


def compass(cx, cy, r, ang=0, spin=False, tip=MINT):
    g = f"<g transform='translate({cx:.1f} {cy:.1f})'>"
    g += f"<circle cx='8' cy='12' r='{r + 18:.1f}' fill='{INK}' opacity='.13'/>"
    g += f"<circle r='{r + 18:.1f}' fill='{NAVY}' stroke='{INK}' stroke-width='5'/>"
    g += f"<circle r='{r:.1f}' fill='#FFFFFF' stroke='{INK}' stroke-width='4'/>"
    for k in range(36):
        a = math.radians(k * 10)
        l = r * (.16 if k % 9 == 0 else .07)
        x1, y1 = math.sin(a) * (r - 6), -math.cos(a) * (r - 6)
        x2, y2 = math.sin(a) * (r - 6 - l), -math.cos(a) * (r - 6 - l)
        g += f"<line x1='{x1:.1f}' y1='{y1:.1f}' x2='{x2:.1f}' y2='{y2:.1f}' stroke='{INK}' stroke-width='{4 if k % 9 == 0 else 2}' opacity='.7'/>"
    if spin:
        for gh in (-70, 55, 150):
            g += needle(r * .72, ang + gh, tip=GREY, tail="#FFFFFF", op=.35)
        for a0 in (20, 200):
            a1, a2 = math.radians(a0), math.radians(a0 + 70)
            rr = r * .86
            g += (f"<path d='M {math.sin(a1) * rr:.1f},{-math.cos(a1) * rr:.1f} A {rr:.1f} {rr:.1f} 0 0 1 "
                  f"{math.sin(a2) * rr:.1f},{-math.cos(a2) * rr:.1f}' fill='none' stroke='{GREY_D}' stroke-width='6' "
                  f"stroke-linecap='round' stroke-dasharray='3 13'/>")
        g += needle(r * .72, ang, tip=GREY, tail="#FFFFFF")
    else:
        g += needle(r * .72, ang, tip=tip)
    g += f"<circle r='{r * .07:.1f}' fill='{INK}'/>"
    return g + "</g>"


def person(cx, by, h, fill, op=1, dash=False):
    d = " stroke-dasharray='7 6'" if dash else ""
    hr = h * .19
    return (f"<g opacity='{op}'><circle cx='{cx:.1f}' cy='{by - h + hr:.1f}' r='{hr:.1f}' fill='{fill}' stroke='{INK}' stroke-width='4'{d}/>"
            f"<path d='M {cx - h * .3:.1f},{by:.1f} Q {cx - h * .3:.1f},{by - h * .56:.1f} {cx:.1f},{by - h * .56:.1f} "
            f"Q {cx + h * .3:.1f},{by - h * .56:.1f} {cx + h * .3:.1f},{by:.1f} Z' fill='{fill}' stroke='{INK}' stroke-width='4' stroke-linejoin='round'{d}/></g>")


def pin(cx, by, h, fill, num=None, fs=None, dash=False, stroke=INK):
    d = " stroke-dasharray='8 6'" if dash else ""
    r = h * .36
    cy = by - h + r
    g = (f"<path d='M {cx:.1f},{by:.1f} C {cx - r * .5:.1f},{by - h * .28:.1f} {cx - r:.1f},{cy + r * .55:.1f} {cx - r:.1f},{cy:.1f} "
         f"A {r:.1f} {r:.1f} 0 0 1 {cx + r:.1f},{cy:.1f} C {cx + r:.1f},{cy + r * .55:.1f} {cx + r * .5:.1f},{by - h * .28:.1f} {cx:.1f},{by:.1f} Z' "
         f"fill='{fill}' stroke='{stroke}' stroke-width='4' stroke-linejoin='round'{d}/>")
    if num:
        f = fs or r
        g += label(cx, cy + f * .36, num, INK, f)
    else:
        g += f"<circle cx='{cx:.1f}' cy='{cy:.1f}' r='{r * .38:.1f}' fill='#FFFFFF' stroke='{INK}' stroke-width='3'/>"
    return g


def arrow(x1, y1, x2, y2, color=GREY_D, w=6, dash=True):
    a = math.atan2(y2 - y1, x2 - x1)
    hx1, hy1 = x2 - 22 * math.cos(a - .45), y2 - 22 * math.sin(a - .45)
    hx2, hy2 = x2 - 22 * math.cos(a + .45), y2 - 22 * math.sin(a + .45)
    d = " stroke-dasharray='4 12'" if dash else ""
    return (f"<line x1='{x1:.1f}' y1='{y1:.1f}' x2='{x2:.1f}' y2='{y2:.1f}' stroke='{color}' stroke-width='{w}' stroke-linecap='round'{d}/>"
            f"<path d='M {hx1:.1f},{hy1:.1f} L {x2:.1f},{y2:.1f} L {hx2:.1f},{hy2:.1f}' fill='none' stroke='{color}' stroke-width='{w}' "
            f"stroke-linecap='round' stroke-linejoin='round'/>")


def tag(cx, cy, txt, fill="#FFFFFF", color=GREY_D, size=28, stroke=None):
    w = len(txt) * size * .55 + 40
    return (f"<rect x='{cx - w / 2:.1f}' y='{cy - size * .9:.1f}' width='{w:.1f}' height='{size * 1.6:.1f}' rx='{size * .8:.1f}' "
            f"fill='{fill}' stroke='{stroke or color}' stroke-width='3'/>" + label(cx, cy + size * .3, txt, color, size, 800))


def bubble(cx, cy, r=40, color=GREY_D):
    return f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='#FFFFFF' stroke='{color}' stroke-width='4'/>" + label(cx, cy + r * .38, "?", color, r * 1.15)


def trail(pts, color=GREY_D, w=6):
    p = "M " + " L ".join(f"{x:.0f},{y:.0f}" for x, y in pts)
    return (f"<path d='{p}' fill='none' stroke='{color}' stroke-width='{w}' stroke-linecap='round' "
            f"stroke-linejoin='round' stroke-dasharray='3 14'/>")


def shop(cx, by, s=1.0):
    """Small new shop with a mint awning and a 'חדש' flag."""
    w, h = 150 * s, 110 * s
    x, y = cx - w / 2, by - h
    g = f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h:.1f}' fill='#FFFFFF' stroke='{INK}' stroke-width='4'/>"
    n = 5
    for k in range(n):
        g += (f"<path d='M {x + k * w / n:.1f},{y:.1f} h {w / n:.1f} v {22 * s:.1f} a {w / n / 2:.1f} {w / n / 2:.1f} 0 0 1 {-w / n:.1f} 0 Z' "
              f"fill='{MINT if k % 2 == 0 else '#FFFFFF'}' stroke='{INK}' stroke-width='3'/>")
    g += f"<rect x='{cx - 22 * s:.1f}' y='{by - 58 * s:.1f}' width='{44 * s:.1f}' height='{58 * s:.1f}' fill='{NAVY}' stroke='{INK}' stroke-width='3'/>"
    g += f"<line x1='{x + w - 18 * s:.1f}' y1='{y:.1f}' x2='{x + w - 18 * s:.1f}' y2='{y - 62 * s:.1f}' stroke='{INK}' stroke-width='4'/>"
    g += (f"<path d='M {x + w - 18 * s:.1f},{y - 62 * s:.1f} h {-62 * s:.1f} l {12 * s:.1f},{14 * s:.1f} l {-12 * s:.1f},{14 * s:.1f} h {62 * s:.1f} Z' "
          f"fill='{RED}' stroke='{INK}' stroke-width='3'/>")
    g += label(x + w - 47 * s, y - 40 * s, "חדש", "#FFFFFF", 19 * s)
    return g


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='660' viewBox='0 0 {w} 660'>"
        g += compass(470, 330, 205, ang=38, spin=True)
        g += bubble(770, 110, 46)
        g += shop(150, 610, .9)
        g += tag(150, 640 - 8, "0 עוקבים", "#FFFFFF", SUB, 24)
        return g + "</svg>"
    if k == "many":
        g = f"<svg width='{w}' height='620' viewBox='0 0 {w} 620'>"
        cx, cy = 470, 320
        targets = ((470, 50, "טרנד"), (790, 140, "הגרלה"), (840, 410, "מכרים"),
                   (640, 585, "משפחה"), (290, 585, "מכל מקום"), (110, 410, "סתם סקרנים"), (150, 140, "מה שמביא מספרים"))
        for tx, ty, txt in targets:
            a = math.atan2(ty - cy, tx - cx)
            g += arrow(cx + math.cos(a) * 160, cy + math.sin(a) * 160, tx - math.cos(a) * 70, ty - math.sin(a) * 52)
        g += compass(cx, cy, 120, ang=-25, spin=True)
        for tx, ty, txt in targets:
            g += tag(tx, ty, txt, "#FFFFFF", GREY_D, 27)
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='800' viewBox='0 0 {w} 800'>"
        g += f"<line x1='470' y1='20' x2='470' y2='640' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        # right (read first): spinning needle, arrows scattered everywhere, grey dashed figures far apart
        g += compass(705, 300, 120, ang=120, spin=True)
        for a in (-60, 10, 80, 150, 220, 290):
            ar = math.radians(a)
            g += arrow(705 + math.cos(ar) * 152, 300 + math.sin(ar) * 152, 705 + math.cos(ar) * 215, 300 + math.sin(ar) * 215, w=5)
        g += bubble(880, 70, 32)
        for x, op in ((560, .9), (705, .7), (850, .5)):
            g += person(x, 625, 92, GREY, op=op, dash=True)
        g += label(705, 700, "לכל הכיוונים", INK, 36) + label(705, 746, "קשה לדעת למי זה הגיע", SUB, 27)
        # left: needle points to one place — a cluster of mint people, with a dotted trail from the compass
        g += compass(330, 470, 105, ang=-39)
        g += trail([(246, 366), (222, 337)], MINT_D, 7)
        g += f"<ellipse cx='150' cy='250' rx='125' ry='92' fill='{MINT_L}' opacity='.7' stroke='{MINT_D}' stroke-width='3' stroke-dasharray='8 8'/>"
        for x, y, f in ((95, 270, MINT), (160, 290, MINT), (225, 265, MINT_L), (125, 215, MINT_L), (190, 205, MINT)):
            g += person(x, y, 68, f)
        g += pin(150, 160, 70, RED)
        g += label(235, 700, "כיוון אחד", MINT_D, 36) + label(235, 746, "אנשים שאולי צריכים אתכם", SUB, 27)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; n = len(labels); rows = ""
        for i, l in enumerate(labels):
            last = i == n - 1
            fill = "#FFFFFF" if last else (MINT if i % 2 == 0 else MINT_L)
            t = (f"<svg width='86' height='100' viewBox='0 0 86 100' style='flex:none'>"
                 f"{pin(43, 94, 88, fill, num=str(i + 1), fs=34, dash=last, stroke=MINT_D if last else INK)}</svg>")
            rows += (f"<div style='display:flex;align-items:center;gap:26px'>{t}"
                     f"<span style='font-size:42px;font-weight:900;color:{SUB if last else INK}'>{l}</span></div>")
        return (f"<div style='width:840px;background:#FFFFFF;border:6px solid {INK};border-radius:20px;overflow:hidden;"
                f"box-shadow:12px 14px 0 rgba(16,27,79,.14)'>"
                f"<div style='background:{NAVY};color:#fff;font-size:32px;font-weight:900;padding:18px 34px;display:flex;align-items:center;gap:18px'>"
                f"<span style='width:18px;height:18px;border-radius:50%;background:{MINT};flex:none'></span>נקודה אחרי נקודה</div>"
                f"<div style='position:relative;padding:18px 40px 22px 40px;display:flex;flex-direction:column;gap:4px'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='600' viewBox='0 0 {w} 600'>"
        g += compass(720, 330, 150, ang=-78)
        pts = [(580, 255), (500, 300), (420, 250), (345, 295)]
        g += trail(pts, MINT_D, 7)
        for i, (x, y) in enumerate(pts[1:3]):
            g += f"<circle cx='{x}' cy='{y}' r='11' fill='{MINT}' stroke='{INK}' stroke-width='3'/>"
        g += f"<ellipse cx='170' cy='300' rx='150' ry='120' fill='{MINT_L}' opacity='.7' stroke='{MINT_D}' stroke-width='3' stroke-dasharray='8 8'/>"
        for x, y, f in ((95, 330, MINT), (170, 355, MINT), (245, 330, MINT_L), (130, 265, MINT_L), (210, 262, MINT)):
            g += person(x, y, 76, f)
        g += pin(170, 205, 80, RED)
        return g + "</svg>"
    return ""


def contours(end=False):
    """Faint topographic contour lines (map paper)."""
    paths = ""
    for i, (cx, cy) in enumerate(((180, 1150), (930, 260))):
        for k in range(1, 9):
            rx, ry = 70 * k, 50 * k
            paths += (f"<ellipse cx='{cx}' cy='{cy}' rx='{rx + (k % 3) * 14}' ry='{ry}' fill='none' stroke='#8799DB' "
                      f"stroke-width='3' transform='rotate({-18 + i * 30} {cx} {cy})'/>")
    return (f"<svg width='1080' height='1350' viewBox='0 0 1080 1350' style='position:absolute;inset:0;opacity:{.16 if end else .22}'>"
            f"{paths}</svg>")


def ad_compass(spec):
    slides = spec["slides"]; n = len(slides); out = []
    bg = f"background:{PAPER}"
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT_D if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        end = s.get("layout") == "end"
        wrap = (f"<style>.bg mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='bg' style='position:absolute;inset:0;overflow:hidden;color:{INK};{bg}'>{contours(end)}")
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
