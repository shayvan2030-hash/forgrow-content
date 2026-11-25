"""Extra ad layouts, set 33 (added 2026-11-25).

ad_hourglass — carousel on a dusk gradient (pale lilac to peach) with faint stars: sand hourglasses.
          Business problem: the owner spends hours on every post (filming, editing, writing the caption), usually in
          the evening after work, and has no idea whether the post reached anyone who might need the business; the
          people who see it are mostly unrelated and keep scrolling, so the hours run out like sand. The same hours in
          front of a relevant audience can start a route (discover -> follow -> keep seeing -> understand the offer ->
          maybe reach out), shown as five small hourglasses whose lower bulb fills step by step. Illustration only.
          Original logo on a navy tile.
"""
from ads_extra import NAVY
from ads_extra28 import label, person, tag
from ads_extra31 import frame, qbubble, MINT, MINT_L, INK, MINT_D, SUB, GREY, GREY_D

BG = "linear-gradient(180deg,#EFE6F5 0%,#F7E7EC 50%,#FCEBDC 100%)"
SAND = "#E9B95E"
WOOD = "#8A5A3B"
WOOD_L = "#B07A52"
GLASS = "#FFFFFF"

_cid = [0]


def hourglass(cx, cy, hh, top=.6, bot=.3, sand=SAND, stream=True, op=1, ww=None, frame_col=WOOD, dash=False):
    """Hourglass centred on (cx, cy) with half-height hh. top/bot = how full the upper/lower bulb is (0..1)."""
    _cid[0] += 1
    cid = f"hg{_cid[0]}"
    ww = ww or hh * .62
    n = ww * .1
    p = (f"M {cx - ww:.1f},{cy - hh:.1f} C {cx - ww:.1f},{cy - hh * .3:.1f} {cx - n:.1f},{cy - hh * .22:.1f} {cx - n:.1f},{cy:.1f} "
         f"C {cx - n:.1f},{cy + hh * .22:.1f} {cx - ww:.1f},{cy + hh * .3:.1f} {cx - ww:.1f},{cy + hh:.1f} "
         f"L {cx + ww:.1f},{cy + hh:.1f} C {cx + ww:.1f},{cy + hh * .3:.1f} {cx + n:.1f},{cy + hh * .22:.1f} {cx + n:.1f},{cy:.1f} "
         f"C {cx + n:.1f},{cy - hh * .22:.1f} {cx + ww:.1f},{cy - hh * .3:.1f} {cx + ww:.1f},{cy - hh:.1f} Z")
    sw = 5 if hh > 120 else 3.5
    d = " stroke-dasharray='8 6'" if dash else ""
    g = f"<g opacity='{op}'><defs><clipPath id='{cid}'><path d='{p}'/></clipPath></defs>"
    g += f"<path d='{p}' fill='{GLASS}' fill-opacity='.75'/>"
    sg = f"<g clip-path='url(#{cid})'>"
    if top > 0:
        ty = cy - hh * top
        sg += (f"<path d='M {cx - ww:.1f},{ty:.1f} Q {cx:.1f},{ty + hh * .12:.1f} {cx + ww:.1f},{ty:.1f} L {cx + ww:.1f},{cy:.1f} "
               f"L {cx - ww:.1f},{cy:.1f} Z' fill='{sand}'/>")
    if bot > 0:
        by = cy + hh - hh * bot
        sg += (f"<path d='M {cx - ww:.1f},{cy + hh:.1f} L {cx - ww:.1f},{by + hh * .08:.1f} Q {cx:.1f},{by - hh * .16:.1f} "
               f"{cx + ww:.1f},{by + hh * .08:.1f} L {cx + ww:.1f},{cy + hh:.1f} Z' fill='{sand}'/>")
    if stream and top > 0:
        end = cy + hh - hh * bot - hh * .06
        sg += f"<line x1='{cx:.1f}' y1='{cy - 2:.1f}' x2='{cx:.1f}' y2='{end:.1f}' stroke='{sand}' stroke-width='{max(3, ww * .06):.1f}'/>"
    g += sg + "</g>"
    g += f"<path d='{p}' fill='none' stroke='{INK}' stroke-width='{sw}' stroke-linejoin='round'{d}/>"
    # highlight on the glass
    g += (f"<path d='M {cx - ww * .72:.1f},{cy - hh * .86:.1f} C {cx - ww * .72:.1f},{cy - hh * .5:.1f} {cx - ww * .4:.1f},{cy - hh * .32:.1f} "
          f"{cx - ww * .28:.1f},{cy - hh * .24:.1f}' fill='none' stroke='#FFFFFF' stroke-width='{sw + 2}' stroke-linecap='round' opacity='.9'/>")
    # wooden frame: caps + posts
    cw, ch = ww * 1.22, max(7, hh * .12)
    for yy in (cy - hh - ch, cy + hh):
        g += (f"<rect x='{cx - cw:.1f}' y='{yy:.1f}' width='{cw * 2:.1f}' height='{ch:.1f}' rx='{ch * .35:.1f}' fill='{frame_col}' "
              f"stroke='{INK}' stroke-width='{sw}'{d}/>")
    pw = max(4, ww * .1)
    for xx in (cx - cw + pw * .4, cx + cw - pw * 1.4):
        g += (f"<rect x='{xx:.1f}' y='{cy - hh:.1f}' width='{pw:.1f}' height='{hh * 2:.1f}' fill='{WOOD_L if frame_col == WOOD else frame_col}' "
              f"stroke='{INK}' stroke-width='{sw * .7:.1f}'{d}/>")
    return g + "</g>"


def phone(cx, by, h, screen="#FFFFFF", play=True, op=1):
    w = h * .52
    x, y = cx - w / 2, by - h
    g = f"<g opacity='{op}'>"
    g += f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h:.1f}' rx='{w * .16:.1f}' fill='{NAVY}' stroke='{INK}' stroke-width='4'/>"
    g += f"<rect x='{x + w * .09:.1f}' y='{y + h * .07:.1f}' width='{w * .82:.1f}' height='{h * .84:.1f}' rx='{w * .08:.1f}' fill='{screen}'/>"
    if play:
        s = w * .22
        g += (f"<path d='M {cx - s * .6:.1f},{y + h * .45 - s:.1f} L {cx + s:.1f},{y + h * .45:.1f} L {cx - s * .6:.1f},{y + h * .45 + s:.1f} Z' "
              f"fill='{MINT}' stroke='{INK}' stroke-width='3' stroke-linejoin='round'/>")
        for k in range(2):
            g += (f"<rect x='{x + w * .2:.1f}' y='{y + h * (.7 + k * .08):.1f}' width='{w * (.6 - k * .2):.1f}' height='{h * .035:.1f}' "
                  f"rx='3' fill='{GREY}'/>")
    return g + "</g>"


def tripod(cx, by, h):
    top = by - h
    return (f"<g stroke='{INK}' stroke-width='5' stroke-linecap='round'>"
            f"<line x1='{cx}' y1='{top}' x2='{cx - h * .32:.1f}' y2='{by}'/><line x1='{cx}' y1='{top}' x2='{cx + h * .32:.1f}' y2='{by}'/>"
            f"<line x1='{cx}' y1='{top}' x2='{cx}' y2='{by}'/></g>")


def scroll_arrow(x, y, op=1):
    return (f"<g opacity='{op}' fill='none' stroke='{GREY_D}' stroke-width='5' stroke-linecap='round' stroke-linejoin='round'>"
            f"<line x1='{x}' y1='{y - 22}' x2='{x}' y2='{y + 22}'/><path d='M {x - 12},{y + 10} L {x},{y + 22} L {x + 12},{y + 10}'/></g>")


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='680' viewBox='0 0 {w} 680'>"
        g += f"<ellipse cx='470' cy='640' rx='380' ry='22' fill='{INK}' opacity='.08'/>"
        g += hourglass(610, 365, 225, top=.62, bot=.28)
        g += tripod(250, 636, 200)
        g += phone(250, 450, 250)
        g += tag(250, 150, "צילום · עריכה · כיתוב", "#FFFFFF", SUB, 28)
        g += qbubble(840, 120, 44)
        return g + "</svg>"
    if k == "away":
        g = f"<svg width='{w}' height='680' viewBox='0 0 {w} 680'>"
        g += f"<ellipse cx='470' cy='640' rx='420' ry='22' fill='{INK}' opacity='.08'/>"
        g += hourglass(760, 400, 200, top=.08, bot=.72, sand=SAND)
        g += phone(470, 630, 230)
        for x, by, h, op in ((110, 630, 122, .9), (245, 600, 108, .75)):
            g += person(x, by, h, GREY, op=op, dash=True)
            g += (f"<rect x='{x - h * .1:.1f}' y='{by - h * .5:.1f}' width='{h * .2:.1f}' height='{h * .3:.1f}' rx='4' "
                  f"fill='{NAVY}' stroke='{INK}' stroke-width='3' opacity='{op}'/>")
            g += scroll_arrow(x + h * .42, by - h * .62, op)
        g += tag(760, 120, "עוד ערב עבר", "#FFFFFF", SUB, 30)
        g += tag(190, 380, "גוללים הלאה", "#FFFFFF", GREY_D, 28)
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='800' viewBox='0 0 {w} 800'>"
        g += f"<line x1='470' y1='20' x2='470' y2='640' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        # right (read first): hours poured in front of people who keep scrolling
        g += hourglass(705, 330, 160, top=.2, bot=.6, sand="#C9CBD6", frame_col="#9C9FB2")
        for x, by, op in ((590, 620, .9), (820, 620, .8)):
            g += person(x, by, 96, GREY, op=op, dash=True)
            g += scroll_arrow(x + 44, by - 66, op)
        g += label(705, 700, "שעות שנגמרות בגלילה", INK, 34) + label(705, 746, "מי שרואה לא קשור לעסק", SUB, 27)
        # left: the same hours in front of a relevant audience
        g += hourglass(235, 330, 160, top=.2, bot=.6, sand=MINT)
        for x, f in ((120, MINT), (350, MINT_L)):
            g += person(x, 620, 104, f)
        g += label(235, 700, "אותן שעות", MINT_D, 36) + label(235, 746, "מול אנשים שאולי צריכים אתכם", SUB, 27)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; n = len(labels); rows = ""
        for i, l in enumerate(labels):
            last = i == n - 1
            hg = (f"<svg width='70' height='92' viewBox='0 0 70 92' style='flex:none'>"
                  + hourglass(35, 46, 36, ww=26, top=.75 - .13 * i, bot=.12 + .14 * i, sand=MINT if not last else MINT_L,
                              stream=False, dash=last) + "</svg>")
            num = (f"<span style='flex:none;width:52px;height:52px;border-radius:50%;background:{MINT if not last else '#FFFFFF'};"
                   f"border:4px {'dashed' if last else 'solid'} {MINT_D if last else INK};display:flex;align-items:center;justify-content:center;"
                   f"font-size:28px;font-weight:900;color:{INK}'>{i + 1}</span>")
            rows += (f"<div style='display:flex;align-items:center;gap:22px;padding:2px 0'>{num}{hg}"
                     f"<span style='font-size:42px;font-weight:900;color:{SUB if last else INK}'>{l}</span></div>")
        return (f"<div style='width:840px;background:#FFFFFF;border:6px solid {INK};border-radius:20px;overflow:hidden;"
                f"box-shadow:12px 14px 0 rgba(16,27,79,.14)'>"
                f"<div style='background:{NAVY};color:#fff;font-size:32px;font-weight:900;padding:18px 34px;display:flex;align-items:center;gap:18px'>"
                f"<span style='width:18px;height:18px;border-radius:50%;background:{MINT};flex:none'></span>לאט, לאורך זמן</div>"
                f"<div style='padding:12px 40px 18px 40px;display:flex;flex-direction:column'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='600' viewBox='0 0 {w} 600'>"
        g += f"<ellipse cx='470' cy='566' rx='400' ry='20' fill='{INK}' opacity='.08'/>"
        g += hourglass(470, 350, 180, top=.35, bot=.5, sand=MINT)
        for x, by, h, f in ((110, 560, 120, MINT), (235, 560, 100, MINT_L), (705, 560, 100, MINT), (830, 560, 120, MINT_L)):
            g += person(x, by, h, f)
        return g + "</svg>"
    return ""


def stars(end=False):
    import random
    rnd = random.Random(25)
    pts = "".join(f"<circle cx='{rnd.randint(10, 1070)}' cy='{rnd.randint(410, 1340)}' r='{rnd.choice((2, 3, 3, 4))}' fill='#8799DB'/>"
                  for _ in range(70))
    sparkle = "".join(
        f"<path transform='translate({x} {y})' d='M 0,-14 L 3,-3 L 14,0 L 3,3 L 0,14 L -3,3 L -14,0 L -3,-3 Z' fill='#C5CBEE'/>"
        for x, y in ((50, 520), (1030, 470), (90, 1180), (990, 1120)))
    return (f"<svg width='1080' height='1350' viewBox='0 0 1080 1350' style='position:absolute;inset:0;opacity:{.35 if end else .55}'>"
            f"{pts}{sparkle}</svg>")


def ad_hourglass(spec):
    return frame(spec, scene, stars, BG)
