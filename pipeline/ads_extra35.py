"""Extra ad layouts, set 35 (added 2026-11-26).

ad_manual — carousel on off-white paper with a faint isometric dot grid: a flat-pack assembly-instructions leaflet
          (generic line drawings, no brand). Business problem: the owner shares good professional tips, but most of
          the people who follow learn from them and then do it themselves. That is fine, yet the people who would
          rather have someone do the job for them are not the ones seeing the tips. A relevant audience can start a
          route (discover -> follow -> keep seeing -> understand the offer -> maybe reach out), shown as five numbered
          assembly steps. Illustration only. Original logo on a navy tile.
"""
from ads_extra import NAVY
from ads_extra28 import label, person, tag
from ads_extra31 import frame, MINT, MINT_L, INK, MINT_D, SUB, GREY, GREY_D

BG = "#F6F4EE"
WOOD = "#E3C79A"
WOOD_S = "#C9A672"
STEEL = "#AEB3C6"
RED = "#E8735A"


def screw(cx, cy, s=1.0, ang=0, col=STEEL):
    return (f"<g transform='translate({cx:.1f} {cy:.1f}) rotate({ang}) scale({s:.2f})'>"
            f"<path d='M -5,0 L 5,0 L 4,34 L 0,42 L -4,34 Z' fill='{col}' stroke='{INK}' stroke-width='3' stroke-linejoin='round'/>"
            f"<line x1='-5' y1='12' x2='5' y2='9' stroke='{INK}' stroke-width='2'/><line x1='-5' y1='22' x2='5' y2='19' stroke='{INK}' stroke-width='2'/>"
            f"<rect x='-12' y='-8' width='24' height='9' rx='4' fill='{col}' stroke='{INK}' stroke-width='3'/></g>")


def screwdriver(cx, cy, s=1.0, ang=0, handle=RED, dash=False):
    d = " stroke-dasharray='6 5'" if dash else ""
    return (f"<g transform='translate({cx:.1f} {cy:.1f}) rotate({ang}) scale({s:.2f})'>"
            f"<rect x='-4' y='-10' width='8' height='62' fill='{STEEL}' stroke='{INK}' stroke-width='3'{d}/>"
            f"<rect x='-13' y='-62' width='26' height='56' rx='11' fill='{handle}' stroke='{INK}' stroke-width='4'{d}/>"
            f"<line x1='-4' y1='-52' x2='-4' y2='-16' stroke='#FFFFFF' stroke-width='3' opacity='.6'/></g>")


def wrench(cx, cy, s=1.0, ang=0, col=STEEL):
    return (f"<g transform='translate({cx:.1f} {cy:.1f}) rotate({ang}) scale({s:.2f})'>"
            f"<path d='M -7,-40 L 7,-40 L 7,40 L -7,40 Z' fill='{col}' stroke='{INK}' stroke-width='3.5'/>"
            f"<path d='M -18,-62 A 20 20 0 1 0 18,-62 L 8,-62 L 8,-48 L -8,-48 L -8,-62 Z' fill='{col}' stroke='{INK}' stroke-width='3.5' stroke-linejoin='round'/>"
            f"<circle cx='0' cy='52' r='15' fill='{col}' stroke='{INK}' stroke-width='3.5'/><circle cx='0' cy='52' r='6' fill='{BG}' stroke='{INK}' stroke-width='3'/></g>")


def toolbox(cx, by, w, fill=RED, dash=False, op=1):
    d = " stroke-dasharray='8 6'" if dash else ""
    h = w * .52
    x, y = cx - w / 2, by - h
    return (f"<g opacity='{op}'><path d='M {cx - w * .2:.1f},{y:.1f} L {cx - w * .2:.1f},{y - h * .32:.1f} L {cx + w * .2:.1f},{y - h * .32:.1f} "
            f"L {cx + w * .2:.1f},{y:.1f}' fill='none' stroke='{INK}' stroke-width='6' stroke-linejoin='round'/>"
            f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h:.1f}' rx='10' fill='{fill}' stroke='{INK}' stroke-width='4'{d}/>"
            f"<line x1='{x:.1f}' y1='{y + h * .3:.1f}' x2='{x + w:.1f}' y2='{y + h * .3:.1f}' stroke='{INK}' stroke-width='4'/>"
            f"<rect x='{cx - w * .08:.1f}' y='{y + h * .22:.1f}' width='{w * .16:.1f}' height='{h * .18:.1f}' rx='3' fill='{STEEL}' stroke='{INK}' stroke-width='3'/></g>")


def shelf(cx, cy, w, fill=WOOD, dash=False, op=1):
    """Simple bookshelf drawn in isometric-ish line style."""
    d = " stroke-dasharray='8 6'" if dash else ""
    h = w * 1.05
    x, y = cx - w / 2, cy - h / 2
    g = f"<g opacity='{op}'>"
    g += f"<path d='M {x + w:.1f},{y:.1f} L {x + w + w * .16:.1f},{y - w * .1:.1f} L {x + w + w * .16:.1f},{y + h - w * .1:.1f} L {x + w:.1f},{y + h:.1f} Z' fill='{WOOD_S}' stroke='{INK}' stroke-width='4' stroke-linejoin='round'{d}/>"
    g += f"<path d='M {x:.1f},{y:.1f} L {x + w * .16:.1f},{y - w * .1:.1f} L {x + w + w * .16:.1f},{y - w * .1:.1f} L {x + w:.1f},{y:.1f} Z' fill='{WOOD_S}' stroke='{INK}' stroke-width='4' stroke-linejoin='round'{d}/>"
    g += f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h:.1f}' fill='{fill}' stroke='{INK}' stroke-width='4'{d}/>"
    for k in (1, 2):
        g += f"<rect x='{x + 10:.1f}' y='{y + h * k / 3 - 5:.1f}' width='{w - 20:.1f}' height='10' fill='{WOOD_S}' stroke='{INK}' stroke-width='3'{d}/>"
    return g + "</g>"


def leaflet(cx, cy, w, h, steps=True, stamp=None):
    """White instruction sheet with a folded corner and three little step panels."""
    x, y = cx - w / 2, cy - h / 2
    f = w * .12
    g = f"<rect x='{x + 12:.1f}' y='{y + 14:.1f}' width='{w:.1f}' height='{h:.1f}' rx='6' fill='{INK}' opacity='.1'/>"
    g += (f"<path d='M {x:.1f},{y:.1f} L {x + w - f:.1f},{y:.1f} L {x + w:.1f},{y + f:.1f} L {x + w:.1f},{y + h:.1f} L {x:.1f},{y + h:.1f} Z' "
          f"fill='#FFFFFF' stroke='{INK}' stroke-width='4' stroke-linejoin='round'/>"
          f"<path d='M {x + w - f:.1f},{y:.1f} L {x + w - f:.1f},{y + f:.1f} L {x + w:.1f},{y + f:.1f}' fill='#ECEAF3' stroke='{INK}' stroke-width='3' stroke-linejoin='round'/>")
    if steps:
        pw, ph = (w - 60) / 2, (h - 90) / 2
        cells = [(x + 20, y + 30), (x + 40 + pw, y + 30), (x + 20, y + 50 + ph)]
        for k, (px, py) in enumerate(cells):
            g += f"<rect x='{px:.1f}' y='{py:.1f}' width='{pw:.1f}' height='{ph:.1f}' rx='6' fill='none' stroke='{INK}' stroke-width='3' opacity='.85'/>"
            g += (f"<rect x='{px + 8:.1f}' y='{py + 8:.1f}' width='34' height='34' rx='5' fill='{INK}'/>"
                  + label(px + 25, py + 35, str(k + 1), "#FFFFFF", 24))
            mx, my = px + pw / 2 + 10, py + ph / 2 + 12
            if k == 0:
                g += f"<rect x='{mx - pw * .3:.1f}' y='{my - 12:.1f}' width='{pw * .6:.1f}' height='24' fill='{WOOD}' stroke='{INK}' stroke-width='3'/>"
                g += f"<rect x='{mx - pw * .3:.1f}' y='{my + 18:.1f}' width='{pw * .6:.1f}' height='24' fill='{WOOD}' stroke='{INK}' stroke-width='3'/>"
            elif k == 1:
                for j in range(3):
                    g += screw(mx - 30 + j * 30, my - 22, .8)
                g += label(mx + 52, my + 6, "x8", INK, 24)
            else:
                g += f"<rect x='{mx - pw * .3:.1f}' y='{my - 10:.1f}' width='{pw * .6:.1f}' height='22' fill='{WOOD}' stroke='{INK}' stroke-width='3'/>"
                g += screw(mx, my - 62, .8)
                g += (f"<path d='M {mx + 26:.1f},{my - 56:.1f} A 16 16 0 1 1 {mx + 26:.1f},{my - 24:.1f}' fill='none' stroke='{INK}' stroke-width='3'/>"
                      f"<path d='M {mx + 18:.1f},{my - 28:.1f} L {mx + 26:.1f},{my - 24:.1f} L {mx + 20:.1f},{my - 16:.1f}' fill='none' stroke='{INK}' stroke-width='3'/>")
        qx, qy = x + 40 + pw, y + 50 + ph
        g += f"<rect x='{qx:.1f}' y='{qy:.1f}' width='{pw:.1f}' height='{ph:.1f}' rx='6' fill='none' stroke='{INK}' stroke-width='3' opacity='.85'/>"
        g += shelf(qx + pw / 2, qy + ph / 2 + 6, pw * .32)
    if stamp:
        g += (f"<g transform='rotate(-8 {cx:.1f} {cy:.1f})'><rect x='{cx - w * .36:.1f}' y='{cy - 40:.1f}' width='{w * .72:.1f}' height='80' rx='12' "
              f"fill='#FFFFFF' stroke='{MINT_D}' stroke-width='6'/>" + label(cx, cy + 15, stamp, MINT_D, 40) + "</g>")
    return g


def diy(cx, by, h, dash=True, op=.9):
    """Grey dashed person busy doing the job alone (screwdriver in hand, small shelf beside)."""
    g = person(cx, by, h, GREY, op=op, dash=dash)
    g += screwdriver(cx + h * .36, by - h * .42, h / 150, 35)
    return g


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='700' viewBox='0 0 {w} 700'>"
        g += leaflet(560, 340, 560, 560)
        g += toolbox(150, 640, 210)
        g += screwdriver(110, 330, 1.2, -20)
        g += wrench(210, 330, 1.1, 18)
        g += tag(150, 150, "טיפ מקצועי", "#FFFFFF", SUB, 30)
        return g + "</svg>"
    if k == "away":
        g = f"<svg width='{w}' height='700' viewBox='0 0 {w} 700'>"
        g += f"<ellipse cx='470' cy='660' rx='440' ry='22' fill='{INK}' opacity='.07'/>"
        for x, by, h, op in ((170, 650, 220, .9), (465, 620, 195, .8), (740, 650, 220, .9)):
            g += shelf(x - h * .5, by - h * .36, h * .34, fill="#ECEDF2", dash=True, op=op)
            g += diy(x + 25, by, h, op=op)
        g += tag(470, 170, "לומדים ועושים לבד", "#FFFFFF", GREY_D, 34)
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='800' viewBox='0 0 {w} 800'>"
        g += f"<line x1='470' y1='20' x2='470' y2='640' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        # right (read first): learn the tip and do it alone
        g += shelf(590, 420, 150, fill="#ECEDF2", dash=True, op=.9)
        g += diy(760, 630, 240)
        g += label(705, 700, "לומדים ועושים לבד", INK, 34) + label(705, 746, "צריכים טיפ, לא שירות", SUB, 27)
        # left: people who would rather someone else did it
        g += f"<g transform='rotate(-12 150 520)'>" + shelf(150, 470, 140) + "</g>"
        g += person(335, 630, 240, MINT)
        g += (f"<circle cx='400' cy='300' r='46' fill='#FFFFFF' stroke='{MINT_D}' stroke-width='4'/>"
              + wrench(400, 300, .5, 40) + f"<path d='M 372,338 L 360,362 L 388,344' fill='#FFFFFF' stroke='{MINT_D}' stroke-width='4' stroke-linejoin='round'/>")
        g += label(235, 700, "מחפשים מי שיעשה את זה", MINT_D, 34) + label(235, 746, "ואולי צריכים בדיוק אתכם", SUB, 27)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; n = len(labels); rows = ""
        for i, l in enumerate(labels):
            last = i == n - 1
            num = (f"<span style='flex:none;width:58px;height:58px;border-radius:8px;background:{INK if not last else '#FFFFFF'};"
                   f"border:4px {'dashed' if last else 'solid'} {MINT_D if last else INK};display:flex;align-items:center;justify-content:center;"
                   f"font-size:30px;font-weight:900;color:{'#FFFFFF' if not last else INK}'>{i + 1}</span>")
            ic = (f"<svg width='60' height='70' viewBox='-30 -14 60 70' style='flex:none'>"
                  + screw(0, 0, 1.05, 0, MINT if not last else "#FFFFFF") + "</svg>")
            rows += (f"<div style='display:flex;align-items:center;gap:22px;padding:6px 0;border-bottom:3px dotted {GREY}'>{num}{ic}"
                     f"<span style='font-size:42px;font-weight:900;color:{SUB if last else INK}'>{l}</span></div>")
        return (f"<div style='width:840px;background:#FFFFFF;border:6px solid {INK};border-radius:8px;overflow:hidden;"
                f"box-shadow:12px 14px 0 rgba(16,27,79,.14)'>"
                f"<div style='background:{NAVY};color:#fff;font-size:32px;font-weight:900;padding:18px 34px;display:flex;align-items:center;gap:18px'>"
                f"<span style='width:18px;height:18px;border-radius:50%;background:{MINT};flex:none'></span>שלב אחרי שלב, לאורך זמן</div>"
                f"<div style='padding:8px 40px 14px 40px;display:flex;flex-direction:column'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='620' viewBox='0 0 {w} 620'>"
        g += f"<ellipse cx='470' cy='590' rx='420' ry='20' fill='{INK}' opacity='.07'/>"
        g += shelf(470, 400, 230)
        g += toolbox(150, 590, 170)
        for x, by, h, f in ((720, 590, 150, MINT), (850, 590, 125, MINT_L)):
            g += person(x, by, h, f)
        return g + "</svg>"
    return ""


def dotgrid(end=False):
    pts = []
    for row, y in enumerate(range(20, 1350, 34)):
        off = 0 if row % 2 == 0 else 29
        for x in range(10 + off, 1080, 58):
            pts.append(f"<circle cx='{x}' cy='{y}' r='2.4' fill='#8799DB'/>")
    return (f"<svg width='1080' height='1350' viewBox='0 0 1080 1350' style='position:absolute;inset:0;opacity:{.3 if end else .45}'>"
            f"{''.join(pts)}</svg>")


def ad_manual(spec):
    return frame(spec, scene, dotgrid, BG)
