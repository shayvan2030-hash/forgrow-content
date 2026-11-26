"""Extra ad layouts, set 34 (added 2026-11-26).

ad_merrygoround — carousel on a pale butter-yellow background with faint bunting garlands: a fairground merry-go-round.
          Business problem: the business has been active on Instagram for a while, but every post reaches the same
          people again and again. They already know everything the business offers, and the people who might need it
          have never heard of it, so the circle does not widen. A relevant audience that does not know the business yet
          can start a route (discover -> follow -> keep seeing -> understand the offer -> maybe reach out), shown as
          five small horses turning mint one by one. Illustration only. Original logo on a navy tile.
"""
from ads_extra import NAVY
from ads_extra28 import label, person, tag
from ads_extra31 import frame, qbubble, MINT, MINT_L, INK, MINT_D, SUB, GREY, GREY_D

BG = "#FBF1D2"
GOLD = "#E2B04A"
RED = "#E8735A"
CREAM = "#FFFDF6"
LAV = "#C5CBEE"
PERI = "#8799DB"
GREY_C = "#BFC2CF"


def horse(cx, cy, s, fill="#FFFFFF", mane=PERI, face=1, dash=False, op=1):
    """Simple carousel horse centred on (cx, cy) (centre of the body), length ~2*s. face=1 looks right, -1 left."""
    d = " stroke-dasharray='7 6'" if dash else ""
    sw = 4 if s > 40 else 3
    g = f"<g opacity='{op}' transform='translate({cx:.1f} {cy:.1f}) scale({face} 1)'>"
    # legs (galloping pose)
    for x0, x1, y1 in ((-s * .55, -s * .72, s * .62), (-s * .3, -s * .34, s * .7), (s * .32, s * .4, s * .7), (s * .55, s * .8, s * .5)):
        g += (f"<path d='M {x0:.1f},{s * .1:.1f} L {x1:.1f},{y1:.1f}' stroke='{INK}' stroke-width='{s * .16:.1f}' stroke-linecap='round'/>"
              f"<path d='M {x0:.1f},{s * .1:.1f} L {x1:.1f},{y1:.1f}' stroke='{fill}' stroke-width='{s * .16 - sw * 1.6:.1f}' stroke-linecap='round'/>")
    # tail
    g += (f"<path d='M {-s * .78:.1f},{-s * .12:.1f} C {-s * 1.15:.1f},{-s * .2:.1f} {-s * 1.2:.1f},{s * .25:.1f} {-s * 1.05:.1f},{s * .45:.1f}' "
          f"fill='none' stroke='{mane}' stroke-width='{s * .14:.1f}' stroke-linecap='round'/>")
    # body
    g += f"<ellipse cx='0' cy='0' rx='{s * .82:.1f}' ry='{s * .32:.1f}' fill='{fill}' stroke='{INK}' stroke-width='{sw}'{d}/>"
    # neck + head
    g += (f"<path d='M {s * .45:.1f},{-s * .2:.1f} L {s * .72:.1f},{-s * .85:.1f} L {s * 1.18:.1f},{-s * .62:.1f} "
          f"L {s * 1.12:.1f},{-s * .45:.1f} L {s * .86:.1f},{-s * .5:.1f} L {s * .8:.1f},{-s * .05:.1f} Z' fill='{fill}' "
          f"stroke='{INK}' stroke-width='{sw}' stroke-linejoin='round'{d}/>")
    g += f"<path d='M {s * .68:.1f},{-s * .86:.1f} L {s * .74:.1f},{-s * 1.05:.1f} L {s * .84:.1f},{-s * .84:.1f}' fill='{fill}' stroke='{INK}' stroke-width='{sw * .8:.1f}' stroke-linejoin='round'/>"
    # mane
    g += (f"<path d='M {s * .7:.1f},{-s * .8:.1f} C {s * .52:.1f},{-s * .6:.1f} {s * .48:.1f},{-s * .45:.1f} {s * .42:.1f},{-s * .22:.1f}' "
          f"fill='none' stroke='{mane}' stroke-width='{s * .14:.1f}' stroke-linecap='round'/>")
    g += f"<circle cx='{s * .92:.1f}' cy='{-s * .64:.1f}' r='{max(2.5, s * .05):.1f}' fill='{INK}'/>"
    # saddle
    g += f"<path d='M {-s * .25:.1f},{-s * .3:.1f} Q 0,{-s * .1:.1f} {s * .25:.1f},{-s * .3:.1f}' fill='none' stroke='{RED}' stroke-width='{s * .12:.1f}' stroke-linecap='round'/>"
    return g + "</g>"


def merry(cx, by, r, riders=(), canopy=(RED, CREAM), horse_fill="#FFFFFF", mane=PERI, dash=False, op=1, spin=True,
          gate=False, grey=False):
    """Merry-go-round; platform bottom at by, radius r. riders: list of (fill, dash) for the three front horses (or None)."""
    d = " stroke-dasharray='9 7'" if dash else ""
    pole = GREY_C if grey else GOLD
    top = by - r * 1.95           # tip of the roof
    cb = by - r * 1.35            # canopy bottom edge
    py = by - r * .16             # platform top centre
    g = f"<g opacity='{op}'>"
    g += f"<ellipse cx='{cx}' cy='{by + r * .04:.1f}' rx='{r * 1.15:.1f}' ry='{r * .12:.1f}' fill='{INK}' opacity='.08'/>"
    # centre column (behind)
    g += f"<rect x='{cx - r * .12:.1f}' y='{cb:.1f}' width='{r * .24:.1f}' height='{py - cb:.1f}' fill='{canopy[1]}' stroke='{INK}' stroke-width='4'{d}/>"
    g += f"<rect x='{cx - r * .12:.1f}' y='{cb + (py - cb) * .3:.1f}' width='{r * .24:.1f}' height='{(py - cb) * .12:.1f}' fill='{canopy[0]}' opacity='.7'/>"
    # platform
    g += (f"<path d='M {cx - r:.1f},{py:.1f} L {cx - r:.1f},{by - r * .02:.1f} A {r:.1f} {r * .16:.1f} 0 0 0 {cx + r:.1f},{by - r * .02:.1f} "
          f"L {cx + r:.1f},{py:.1f} Z' fill='{canopy[0]}' stroke='{INK}' stroke-width='4'{d}/>")
    g += f"<ellipse cx='{cx}' cy='{py:.1f}' rx='{r:.1f}' ry='{r * .16:.1f}' fill='{canopy[1]}' stroke='{INK}' stroke-width='4'{d}/>"
    # poles + horses (three in front)
    xs = (cx - r * .64, cx, cx + r * .64)
    ys = (py - r * .02, py + r * .1, py - r * .02)
    hs = r * .27
    for k, (x, yb) in enumerate(zip(xs, ys)):
        hy = yb - r * (.55 if k != 1 else .42)
        g += f"<line x1='{x:.1f}' y1='{cb + r * .1:.1f}' x2='{x:.1f}' y2='{yb:.1f}' stroke='{INK}' stroke-width='{r * .05 + 4:.1f}' stroke-linecap='round'/>"
        g += f"<line x1='{x:.1f}' y1='{cb + r * .1:.1f}' x2='{x:.1f}' y2='{yb:.1f}' stroke='{pole}' stroke-width='{r * .05:.1f}' stroke-linecap='round'/>"
        g += horse(x, hy, hs, horse_fill, mane, face=-1 if k == 2 else 1, dash=dash)
        rd = riders[k] if k < len(riders) else None
        if rd:
            g += person(x - hs * .05, hy - hs * .22, hs * 1.55, rd[0], dash=rd[1])
    # roof
    g += f"<path d='M {cx},{top:.1f} L {cx + r * 1.08:.1f},{cb:.1f} L {cx - r * 1.08:.1f},{cb:.1f} Z' fill='{canopy[1]}' stroke='{INK}' stroke-width='4' stroke-linejoin='round'{d}/>"
    n = 6
    for k in range(n):
        if k % 2 == 0:
            x0 = cx - r * 1.08 + k * (2.16 * r / n); x1 = x0 + 2.16 * r / n
            g += f"<path d='M {cx},{top:.1f} L {x1:.1f},{cb:.1f} L {x0:.1f},{cb:.1f} Z' fill='{canopy[0]}'/>"
    g += f"<path d='M {cx},{top:.1f} L {cx + r * 1.08:.1f},{cb:.1f} L {cx - r * 1.08:.1f},{cb:.1f} Z' fill='none' stroke='{INK}' stroke-width='4' stroke-linejoin='round'{d}/>"
    # scalloped valance
    m = 8; sw_ = 2.16 * r / m
    for k in range(m):
        x0 = cx - r * 1.08 + k * sw_
        g += (f"<path d='M {x0:.1f},{cb:.1f} A {sw_ / 2:.1f} {sw_ / 2.4:.1f} 0 0 0 {x0 + sw_:.1f},{cb:.1f} Z' "
              f"fill='{canopy[k % 2]}' stroke='{INK}' stroke-width='3.5'{d}/>")
    # finial flag
    g += (f"<line x1='{cx}' y1='{top:.1f}' x2='{cx}' y2='{top - r * .25:.1f}' stroke='{INK}' stroke-width='4'/>"
          f"<path d='M {cx},{top - r * .25:.1f} L {cx + r * .2:.1f},{top - r * .19:.1f} L {cx},{top - r * .13:.1f} Z' fill='{canopy[0]}' stroke='{INK}' stroke-width='3'/>")
    if spin:
        col = GREY_D if grey else SUB
        ay = py + r * .28
        g += (f"<path d='M {cx + r * .9:.1f},{ay:.1f} A {r * 1.05:.1f} {r * .2:.1f} 0 0 1 {cx - r * .9:.1f},{ay:.1f}' fill='none' "
              f"stroke='{col}' stroke-width='5' stroke-linecap='round' stroke-dasharray='2 12'/>")
    if gate:
        gx = cx + r * 1.02
        g += (f"<path d='M {gx:.1f},{by - r * .02:.1f} L {gx + r * .35:.1f},{by + r * .02:.1f}' stroke='{INK}' stroke-width='5' stroke-linecap='round'/>"
              f"<rect x='{gx + r * .02:.1f}' y='{by - r * .12:.1f}' width='{r * .33:.1f}' height='{r * .1:.1f}' rx='4' fill='{MINT}' stroke='{INK}' stroke-width='3'/>")
    return g + "</g>"


def fence(x0, x1, by, h=60):
    g = f"<g stroke='{INK}' stroke-width='4' opacity='.55'>"
    g += f"<line x1='{x0}' y1='{by - h * .7:.1f}' x2='{x1}' y2='{by - h * .7:.1f}'/><line x1='{x0}' y1='{by - h * .25:.1f}' x2='{x1}' y2='{by - h * .25:.1f}'/>"
    for x in range(int(x0), int(x1) + 1, 40):
        g += f"<line x1='{x}' y1='{by:.1f}' x2='{x}' y2='{by - h:.1f}'/>"
    return g + "</g>"


def scene(sc, w=940):
    k = sc["kind"]
    familiar = [(LAV, False), (PERI, False), (LAV, False)]
    if k == "intro":
        g = f"<svg width='{w}' height='700' viewBox='0 0 {w} 700'>"
        g += merry(470, 650, 290, familiar)
        g += tag(150, 90, "עוד סיבוב", "#FFFFFF", SUB, 30)
        g += tag(800, 90, "אותם אנשים", "#FFFFFF", SUB, 30)
        return g + "</svg>"
    if k == "away":
        g = f"<svg width='{w}' height='700' viewBox='0 0 {w} 700'>"
        g += merry(640, 640, 220, familiar)
        g += fence(30, 330, 650, 70)
        for x, by, h, op in ((90, 640, 128, .9), (230, 610, 112, .75)):
            g += person(x, by, h, GREY, op=op, dash=True)
            g += qbubble(int(x + h * .4), int(by - h - 20), 30)
        g += tag(185, 400, "לא יודעים שאתם קיימים", "#FFFFFF", GREY_D, 27)
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='800' viewBox='0 0 {w} 800'>"
        g += f"<line x1='470' y1='20' x2='470' y2='640' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        # right (read first): the same circle again and again
        g += merry(705, 600, 165, [(GREY, False), (GREY, False), (GREY, False)], canopy=("#9C9FB2", "#E6E7EE"),
                   horse_fill="#F1F2F6", mane=GREY_C, grey=True)
        g += label(705, 700, "אותו סיבוב", INK, 34) + label(705, 746, "אותם אנשים, שוב ושוב", SUB, 27)
        # left: room for people who do not know the business yet
        g += merry(215, 600, 150, [(MINT, False), None, (MINT_L, False)], canopy=(MINT, CREAM), mane=MINT_D)
        g += person(405, 640, 88, MINT_L)
        g += label(235, 700, "מקום לאנשים חדשים", MINT_D, 36) + label(235, 746, "שאולי צריכים אתכם", SUB, 27)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; n = len(labels); rows = ""
        for i, l in enumerate(labels):
            last = i == n - 1
            hg = (f"<svg width='96' height='76' viewBox='0 0 96 76' style='flex:none'>"
                  + horse(44, 40, 30, MINT if not last else "#FFFFFF", MINT_D if not last else GREY_C, dash=last) + "</svg>")
            num = (f"<span style='flex:none;width:52px;height:52px;border-radius:50%;background:{MINT if not last else '#FFFFFF'};"
                   f"border:4px {'dashed' if last else 'solid'} {MINT_D if last else INK};display:flex;align-items:center;justify-content:center;"
                   f"font-size:28px;font-weight:900;color:{INK}'>{i + 1}</span>")
            rows += (f"<div style='display:flex;align-items:center;gap:22px;padding:4px 0'>{num}{hg}"
                     f"<span style='font-size:42px;font-weight:900;color:{SUB if last else INK}'>{l}</span></div>")
        return (f"<div style='width:840px;background:#FFFFFF;border:6px solid {INK};border-radius:20px;overflow:hidden;"
                f"box-shadow:12px 14px 0 rgba(16,27,79,.14)'>"
                f"<div style='background:{NAVY};color:#fff;font-size:32px;font-weight:900;padding:18px 34px;display:flex;align-items:center;gap:18px'>"
                f"<span style='width:18px;height:18px;border-radius:50%;background:{MINT};flex:none'></span>מעגל שמתרחב, לאט</div>"
                f"<div style='padding:12px 40px 18px 40px;display:flex;flex-direction:column'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='620' viewBox='0 0 {w} 620'>"
        g += merry(560, 580, 230, [(MINT, False), (MINT_L, False), (MINT, False)], canopy=(MINT, CREAM), mane=MINT_D)
        for x, by, h, f in ((120, 590, 110, MINT_L), (230, 590, 96, MINT)):
            g += person(x, by, h, f)
        return g + "</svg>"
    return ""


def bunting(end=False):
    cols = (RED, MINT, PERI, GOLD)
    g = ""
    rows_ = ((1290, 40),) if end else ((470, 60), (1290, 40))
    for row, (y0, sag) in enumerate(rows_):
        g += f"<path d='M -10,{y0} Q 540,{y0 + sag * 2} 1090,{y0}' fill='none' stroke='{SUB}' stroke-width='3'/>"
        for k in range(14):
            t = (k + .5) / 14
            x = -10 + 1100 * t
            y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * (y0 + sag * 2) + t ** 2 * y0
            g += f"<path d='M {x - 22:.0f},{y:.0f} L {x + 22:.0f},{y:.0f} L {x:.0f},{y + 40:.0f} Z' fill='{cols[(k + row) % 4]}'/>"
    import random
    rnd = random.Random(26)
    g += "".join(f"<circle cx='{rnd.randint(10, 1070)}' cy='{rnd.randint(560, 1240)}' r='{rnd.choice((3, 4, 5))}' fill='{cols[rnd.randint(0, 3)]}'/>"
                 for _ in range(40))
    return (f"<svg width='1080' height='1350' viewBox='0 0 1080 1350' style='position:absolute;inset:0;opacity:{.22 if end else .3}'>"
            f"{g}</svg>")


def ad_merrygoround(spec):
    return frame(spec, scene, bunting, BG)
