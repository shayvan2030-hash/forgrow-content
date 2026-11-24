"""Extra ad layouts, set 32 (added 2026-11-24).

ad_eggs — carousel on a pale-blue gingham (picnic tablecloth) background: eggs and wicker baskets.
          Business problem: a small business whose work comes mostly from two or three regular clients
          ("all the eggs in one basket"). When one of them leaves or cuts back, the month looks different and the owner
          starts looking for clients from zero, while the people who see the business on Instagram aren't related to it.
          A relevant audience that keeps getting to know the business over time — alongside the regular clients, not
          instead of them — can start a route (discover -> follow -> keep seeing -> understand the offer -> maybe reach
          out), shown as five numbered eggs. Illustration only. Original logo on a navy tile.
"""
from ads_extra import NAVY
from ads_extra28 import label, person, tag
from ads_extra31 import frame, qbubble, MINT, MINT_L, INK, MINT_D, SUB, GREY, GREY_D

BG = "#E6EEF8"
CHECK = "#C6D4EE"
WICKER = "#C98B4A"
WICKER_D = "#9A6430"
WICKER_L = "#E2AE72"
EGG = "#FFF8EC"
EGG_S = "#F2E3C8"


def egg(cx, cy, s=1.0, fill=EGG, crack=False, rot=0, dash=False, stroke=INK, num=None):
    rx, ry = 30 * s, 39 * s
    d = " stroke-dasharray='8 6'" if dash else ""
    g = (f"<g transform='rotate({rot} {cx:.1f} {cy:.1f})'><path d='M {cx:.1f},{cy - ry:.1f} "
         f"C {cx + rx * 1.05:.1f},{cy - ry:.1f} {cx + rx * 1.1:.1f},{cy + ry:.1f} {cx:.1f},{cy + ry:.1f} "
         f"C {cx - rx * 1.1:.1f},{cy + ry:.1f} {cx - rx * 1.05:.1f},{cy - ry:.1f} {cx:.1f},{cy - ry:.1f} Z' "
         f"fill='{fill}' stroke='{stroke}' stroke-width='{4 if s >= .8 else 3}'{d}/>")
    if not dash and fill == EGG:
        g += f"<ellipse cx='{cx - rx * .35:.1f}' cy='{cy - ry * .35:.1f}' rx='{rx * .18:.1f}' ry='{ry * .25:.1f}' fill='#FFFFFF'/>"
    if crack:
        g += (f"<path d='M {cx - rx * .9:.1f},{cy - ry * .05:.1f} l {rx * .35:.1f},{-ry * .2:.1f} l {rx * .3:.1f},{ry * .25:.1f} "
              f"l {rx * .35:.1f},{-ry * .25:.1f} l {rx * .3:.1f},{ry * .2:.1f} l {rx * .3:.1f},{-ry * .15:.1f}' fill='none' stroke='{INK}' stroke-width='3.5' stroke-linejoin='round'/>")
    if num is not None:
        g += label(cx, cy + ry * .32, str(num), INK, ry * .95)
    return g + "</g>"


def basket(cx, by, w, h, eggs=(), tilt=0, fill=WICKER, op=1, ribbon=None):
    """Wicker basket (trapezoid with weave lines and a handle); `eggs` = list of (dx, dy) offsets peeking over the rim."""
    x0, x1 = cx - w / 2, cx + w / 2
    top = by - h
    g = f"<g transform='rotate({tilt} {cx:.1f} {by:.1f})' opacity='{op}'>"
    g += (f"<path d='M {x0 + w * .1:.1f},{top:.1f} Q {cx:.1f},{top - h * 1.25:.1f} {x1 - w * .1:.1f},{top:.1f}' fill='none' "
          f"stroke='{INK}' stroke-width='{w * .07 + 6:.1f}' stroke-linecap='round'/>"
          f"<path d='M {x0 + w * .1:.1f},{top:.1f} Q {cx:.1f},{top - h * 1.25:.1f} {x1 - w * .1:.1f},{top:.1f}' fill='none' "
          f"stroke='{WICKER_L}' stroke-width='{w * .07:.1f}' stroke-linecap='round'/>")
    for dx, dy, *rest in eggs:
        g += egg(cx + dx, top + dy, rest[0] if rest else 1.0)
    g += (f"<path d='M {x0:.1f},{top:.1f} L {x1:.1f},{top:.1f} L {x1 - w * .12:.1f},{by:.1f} L {x0 + w * .12:.1f},{by:.1f} Z' "
          f"fill='{fill}' stroke='{INK}' stroke-width='4' stroke-linejoin='round'/>")
    rows = 3
    for r in range(1, rows):
        yy = top + h * r / rows
        k = .12 * r / rows
        g += f"<line x1='{x0 + w * k:.1f}' y1='{yy:.1f}' x2='{x1 - w * k:.1f}' y2='{yy:.1f}' stroke='{WICKER_D}' stroke-width='4'/>"
    for c in range(1, 6):
        xt = x0 + w * c / 6
        xb = x0 + w * .12 + (w * .76) * c / 6
        g += f"<line x1='{xt:.1f}' y1='{top + 4:.1f}' x2='{xb:.1f}' y2='{by - 4:.1f}' stroke='{WICKER_D}' stroke-width='3' opacity='.7'/>"
    g += f"<rect x='{x0 - 8:.1f}' y='{top - 10:.1f}' width='{w + 16:.1f}' height='20' rx='10' fill='{WICKER_L}' stroke='{INK}' stroke-width='4'/>"
    if ribbon:
        g += f"<rect x='{cx - w * .3:.1f}' y='{top + h * .36:.1f}' width='{w * .6:.1f}' height='{h * .26:.1f}' rx='8' fill='{ribbon}' stroke='{INK}' stroke-width='3'/>"
    return g + "</g>"


FULL = ((-90, -20, 1.05), (-30, -34, 1.05), (30, -26, 1.05), (90, -18, 1.05), (-60, -6, 1.0), (0, -10, 1.0), (60, -4, 1.0))


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='660' viewBox='0 0 {w} 660'>"
        g += f"<ellipse cx='470' cy='622' rx='300' ry='22' fill='{INK}' opacity='.08'/>"
        g += basket(470, 610, 360, 220, FULL + ((-120, -6, .95), (120, -2, .95)), tilt=-4)
        g += qbubble(160, 200, 46)
        g += tag(720, 130, "2–3 לקוחות קבועים", "#FFFFFF", SUB, 30)
        return g + "</svg>"
    if k == "away":
        g = f"<svg width='{w}' height='660' viewBox='0 0 {w} 660'>"
        g += f"<ellipse cx='470' cy='622' rx='420' ry='22' fill='{INK}' opacity='.08'/>"
        g += basket(640, 610, 300, 190, ((-60, -14, 1.0), (0, -24, 1.0), (60, -10, 1.0)), tilt=-12)
        g += egg(400, 575, 1.05, crack=True, rot=50)
        g += f"<path d='M 470,560 q -20,-30 -50,-40' fill='none' stroke='{GREY_D}' stroke-width='5' stroke-linecap='round' stroke-dasharray='4 10'/>"
        for x, by, h, op in ((110, 615, 118, .9), (230, 590, 104, .75)):
            g += person(x, by, h, GREY, op=op, dash=True)
            g += (f"<rect x='{x - h * .1:.1f}' y='{by - h * .5:.1f}' width='{h * .2:.1f}' height='{h * .3:.1f}' rx='4' "
                  f"fill='{NAVY}' stroke='{INK}' stroke-width='3' opacity='{op}'/>")
        g += tag(650, 140, "לקוח אחד מצמצם", "#FFFFFF", GREY_D, 30)
        g += tag(190, 330, "לא קשורים לעסק", "#FFFFFF", GREY_D, 28)
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='800' viewBox='0 0 {w} 800'>"
        g += f"<line x1='470' y1='20' x2='470' y2='640' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        # right (read first): one heavy basket
        g += basket(705, 540, 260, 170, ((-70, -14, .9), (-24, -26, .9), (24, -20, .9), (70, -12, .9), (-46, -2, .85), (46, 0, .85)), tilt=-5)
        g += label(705, 700, "הכול בסל אחד", INK, 36) + label(705, 746, "לקוח אחד עוזב, והחודש משתנה", SUB, 27)
        # left: people who keep getting to know the business, each a small basket
        for x, f in ((60, MINT), (230, MINT_L), (400, MINT)):
            g += person(x, 560, 130, f)
        for x in (145, 315):
            g += basket(x, 560, 84, 60, ((0, -8, .5),), ribbon=MINT)
        g += label(235, 700, "קהל שמכיר אתכם", MINT_D, 36) + label(235, 746, "לצד הלקוחות הקבועים", SUB, 27)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; n = len(labels); rows = ""
        for i, l in enumerate(labels):
            last = i == n - 1
            fill = "#FFFFFF" if last else (MINT if i % 2 == 0 else MINT_L)
            e = (f"<svg width='72' height='88' viewBox='0 0 72 88' style='flex:none'>"
                 + egg(36, 44, 1.0, fill=fill, dash=last, stroke=MINT_D if last else INK, num=i + 1) + "</svg>")
            rows += (f"<div style='display:flex;align-items:center;gap:26px;padding:4px 0'>{e}"
                     f"<span style='font-size:42px;font-weight:900;color:{SUB if last else INK}'>{l}</span></div>")
        return (f"<div style='width:840px;background:#FFFFFF;border:6px solid {INK};border-radius:20px;overflow:hidden;"
                f"box-shadow:12px 14px 0 rgba(16,27,79,.14)'>"
                f"<div style='background:{NAVY};color:#fff;font-size:32px;font-weight:900;padding:18px 34px;display:flex;align-items:center;gap:18px'>"
                f"<span style='width:18px;height:18px;border-radius:50%;background:{MINT};flex:none'></span>צעד אחרי צעד</div>"
                f"<div style='padding:12px 40px 18px 40px;display:flex;flex-direction:column'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='600' viewBox='0 0 {w} 600'>"
        g += f"<ellipse cx='470' cy='566' rx='400' ry='20' fill='{INK}' opacity='.08'/>"
        g += basket(470, 560, 230, 150, ((-50, -10, .85), (0, -20, .85), (50, -8, .85)))
        for x, by, h, f, bx in ((110, 470, 116, MINT, 110), (240, 440, 104, MINT_L, 240), (700, 440, 104, MINT, 700), (830, 470, 116, MINT_L, 830)):
            g += person(x, by, h, f)
            g += basket(bx, 560, 92, 62, ((0, -8, .5),), ribbon=MINT)
        return g + "</svg>"
    return ""


def gingham(end=False):
    bands = "".join(f"<rect x='{x}' y='0' width='45' height='1350' fill='{CHECK}' opacity='.55'/>" for x in range(0, 1080, 90))
    bands += "".join(f"<rect x='0' y='{y}' width='1080' height='45' fill='{CHECK}' opacity='.55'/>" for y in range(0, 1350, 90))
    return (f"<svg width='1080' height='1350' viewBox='0 0 1080 1350' style='position:absolute;inset:0;opacity:{.4 if end else .65}'>"
            f"{bands}</svg>")


def ad_eggs(spec):
    return frame(spec, scene, gingham, BG)
