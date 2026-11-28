"""Extra ad layouts, set 37 (added 2026-11-28).

ad_dough — carousel on a white subway-tile kitchen wall with a wooden counter: dough in a mixing bowl that needs time
          to rise, a kitchen timer, an oven and a finished loaf. Business problem: a seasonal business (fictional event
          photographer before wedding season) starts posting only a week or two before the busy season — the people who
          see it don't know the business yet, and trust is not built in the last minute. A relevant audience that keeps
          seeing the business over time can start a route (discover -> follow -> keep seeing -> understand the offer ->
          maybe reach out), shown as a numbered recipe card. Illustration only. Original logo on a navy tile.
"""
from ads_extra import NAVY
from ads_extra28 import label, person, tag
from ads_extra31 import frame, MINT, MINT_L, INK, MINT_D, SUB, GREY, GREY_D

BG = "#F7F5F0"
GROUT = "#E2DED4"
WOOD = "#C48A55"
WOOD_D = "#9A6537"
DOUGH = "#F6E3B8"
DOUGH_D = "#E3C68C"
CRUST = "#D99A4E"
CRUST_D = "#B8742F"
BOWL = "#8799DB"
BOWL_D = "#6676BF"
RED = "#E8735A"


def counter(y, w=940):
    return (f"<rect x='0' y='{y}' width='{w}' height='26' rx='6' fill='{WOOD}' stroke='{INK}' stroke-width='4'/>"
            f"<rect x='14' y='{y + 26}' width='{w - 28}' height='18' fill='{WOOD_D}' stroke='{INK}' stroke-width='4'/>")


def bowl(cx, by, w, rise=0.0, txt=None, grey=False, fs=None):
    """Mixing bowl standing on `by`; the dough dome above the rim grows with `rise` (0..1)."""
    h = w * .46
    rim = by - h
    col, cold = (GREY, GREY_D) if grey else (BOWL, BOWL_D)
    dh = w * (.04 + .34 * rise)
    g = ""
    # dough dome
    g += (f"<path d='M {cx - w * .44:.1f},{rim + 6:.1f} C {cx - w * .44:.1f},{rim - dh:.1f} {cx + w * .44:.1f},{rim - dh:.1f} "
          f"{cx + w * .44:.1f},{rim + 6:.1f} Z' fill='{'#EEE9DC' if grey else DOUGH}' stroke='{INK}' stroke-width='4' stroke-linejoin='round'/>")
    if rise > .5:
        for dx, dy, r in ((-.16, .45, .025), (.12, .6, .02), (.02, .3, .018)):
            g += f"<circle cx='{cx + w * dx:.1f}' cy='{rim - dh * dy:.1f}' r='{w * r:.1f}' fill='{DOUGH_D}' opacity='.7'/>"
    # bowl body
    g += (f"<path d='M {cx - w / 2:.1f},{rim:.1f} L {cx + w / 2:.1f},{rim:.1f} C {cx + w * .48:.1f},{by - h * .25:.1f} "
          f"{cx + w * .3:.1f},{by:.1f} {cx + w * .18:.1f},{by:.1f} L {cx - w * .18:.1f},{by:.1f} C {cx - w * .3:.1f},{by:.1f} "
          f"{cx - w * .48:.1f},{by - h * .25:.1f} {cx - w / 2:.1f},{rim:.1f} Z' fill='{col}' stroke='{INK}' stroke-width='5' stroke-linejoin='round'/>")
    g += f"<rect x='{cx - w * .52:.1f}' y='{rim - 9:.1f}' width='{w * 1.04:.1f}' height='18' rx='9' fill='{cold}' stroke='{INK}' stroke-width='4'/>"
    if txt:
        fs = fs or min(38, w * .12)
        lw = len(txt) * fs * .56 + 34
        ly = rim + h * .5
        g += (f"<rect x='{cx - lw / 2:.1f}' y='{ly - fs * .95:.1f}' width='{lw:.1f}' height='{fs * 1.55:.1f}' rx='10' fill='#FFFFFF' stroke='{INK}' stroke-width='3'/>"
              + label(cx, ly + fs * .3, txt, GREY_D if grey else INK, fs))
    return g


def timer(cx, cy, r, frac=.9, col=MINT):
    """Round kitchen timer; the red wedge shows how much time is left (frac of the dial)."""
    import math
    g = f"<rect x='{cx - r * .18:.1f}' y='{cy - r * 1.22:.1f}' width='{r * .36:.1f}' height='{r * .3:.1f}' rx='5' fill='{INK}'/>"
    g += f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='{col}' stroke='{INK}' stroke-width='5'/>"
    g += f"<circle cx='{cx}' cy='{cy}' r='{r * .78:.1f}' fill='#FFFFFF' stroke='{INK}' stroke-width='3'/>"
    a = frac * 2 * math.pi
    x2, y2 = cx + r * .7 * math.sin(a), cy - r * .7 * math.cos(a)
    big = 1 if frac > .5 else 0
    g += f"<path d='M {cx},{cy} L {cx},{cy - r * .7:.1f} A {r * .7:.1f} {r * .7:.1f} 0 {big} 1 {x2:.1f},{y2:.1f} Z' fill='{RED}' opacity='.85'/>"
    for k in range(12):
        t = k / 12 * 2 * math.pi
        g += (f"<line x1='{cx + r * .66 * math.sin(t):.1f}' y1='{cy - r * .66 * math.cos(t):.1f}' x2='{cx + r * .76 * math.sin(t):.1f}' "
              f"y2='{cy - r * .76 * math.cos(t):.1f}' stroke='{INK}' stroke-width='3'/>")
    g += f"<line x1='{cx}' y1='{cy}' x2='{x2:.1f}' y2='{y2:.1f}' stroke='{INK}' stroke-width='5' stroke-linecap='round'/>"
    g += f"<circle cx='{cx}' cy='{cy}' r='{r * .1:.1f}' fill='{INK}'/>"
    return g


def oven(cx, by, w, open_=False, tray=None):
    h = w * .9
    x, y = cx - w / 2, by - h
    g = f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h:.1f}' rx='16' fill='#FFFFFF' stroke='{INK}' stroke-width='5'/>"
    g += f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h * .17:.1f}' rx='16' fill='{NAVY}' stroke='{INK}' stroke-width='5'/>"
    for k in range(3):
        g += f"<circle cx='{x + w * (.2 + k * .14):.1f}' cy='{y + h * .085:.1f}' r='{h * .045:.1f}' fill='#FFFFFF' stroke='{INK}' stroke-width='3'/>"
    g += f"<rect x='{x + w * .66:.1f}' y='{y + h * .05:.1f}' width='{w * .22:.1f}' height='{h * .07:.1f}' rx='5' fill='{MINT}'/>"
    wx, wy, ww, wh = x + w * .1, y + h * .27, w * .8, h * .6
    g += f"<rect x='{wx:.1f}' y='{wy:.1f}' width='{ww:.1f}' height='{wh:.1f}' rx='12' fill='{'#FFE3A6' if open_ else '#3A4370'}' stroke='{INK}' stroke-width='4'/>"
    g += f"<rect x='{wx + 16:.1f}' y='{wy + wh * .62:.1f}' width='{ww - 32:.1f}' height='8' rx='4' fill='{GREY_D}'/>"
    if tray:
        g += tray
    g += f"<rect x='{x + w * .2:.1f}' y='{y + h * .2:.1f}' width='{w * .6:.1f}' height='14' rx='7' fill='{GREY_D}' stroke='{INK}' stroke-width='3'/>"
    return g


def flat_tray(cx, by, w, grey=True):
    return (f"<rect x='{cx - w / 2:.1f}' y='{by - 16:.1f}' width='{w:.1f}' height='16' rx='4' fill='{GREY_D}' stroke='{INK}' stroke-width='3'/>"
            f"<path d='M {cx - w * .44:.1f},{by - 16:.1f} C {cx - w * .44:.1f},{by - 46:.1f} {cx + w * .44:.1f},{by - 46:.1f} {cx + w * .44:.1f},{by - 16:.1f} Z' "
            f"fill='{'#EEE9DC' if grey else DOUGH}' stroke='{INK}' stroke-width='3.5'/>")


def loaf(cx, by, w):
    """Oval bread loaf (batard) on a small cutting board, diagonal scores, light steam."""
    h = w * .42
    g = f"<rect x='{cx - w * .6:.1f}' y='{by - 24:.1f}' width='{w * 1.2:.1f}' height='24' rx='12' fill='{WOOD}' stroke='{INK}' stroke-width='4'/>"
    g += f"<rect x='{cx + w * .6 - 2:.1f}' y='{by - 18:.1f}' width='{w * .14:.1f}' height='12' rx='6' fill='{WOOD}' stroke='{INK}' stroke-width='4'/>"
    cy = by - 24 - h * .5
    g += f"<ellipse cx='{cx:.1f}' cy='{cy:.1f}' rx='{w / 2:.1f}' ry='{h / 2:.1f}' fill='{CRUST}' stroke='{INK}' stroke-width='5'/>"
    g += f"<ellipse cx='{cx - w * .04:.1f}' cy='{cy - h * .12:.1f}' rx='{w * .4:.1f}' ry='{h * .26:.1f}' fill='#EDB873' opacity='.8'/>"
    for k in (-.26, -.09, .08, .25):
        x0 = cx + w * k
        g += (f"<path d='M {x0 - w * .06:.1f},{cy + h * .2:.1f} Q {x0:.1f},{cy - h * .02:.1f} {x0 + w * .07:.1f},{cy - h * .26:.1f}' "
              f"fill='none' stroke='{CRUST_D}' stroke-width='9' stroke-linecap='round'/>"
              f"<path d='M {x0 - w * .05:.1f},{cy + h * .16:.1f} Q {x0 + w * .005:.1f},{cy - h * .03:.1f} {x0 + w * .06:.1f},{cy - h * .22:.1f}' "
              f"fill='none' stroke='{DOUGH}' stroke-width='3' stroke-linecap='round'/>")
    for dx in (-.14, .02, .18):
        g += f"<path d='M {cx + w * dx:.1f},{cy - h * .62:.1f} q -12,-20 0,-40 q 12,-20 0,-40' fill='none' stroke='{GREY_D}' stroke-width='4' stroke-linecap='round' opacity='.4'/>"
    return g


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='740' viewBox='0 0 {w} 740'>"
        g += counter(660)
        g += bowl(610, 660, 520, .08, "קהל שמכיר אתכם", fs=38)
        g += timer(175, 400, 140, .93)
        g += tag(175, 615, "הזמן כמעט נגמר", "#FFFFFF", RED, 30)
        g += tag(610, 300, "הבצק עוד לא תפח", "#FFFFFF", GREY_D, 32)
        g += f"<path d='M 610,330 L 610,390' stroke='{GREY_D}' stroke-width='4' stroke-dasharray='4 10' stroke-linecap='round'/>"
        return g + "</svg>"
    if k == "late":
        g = f"<svg width='{w}' height='700' viewBox='0 0 {w} 700'>"
        g += counter(660)
        ov = 500
        tray = flat_tray(680, 660 - ov * .9 + ov * .27 + ov * .6 * .62, 300)
        g += oven(680, 660, ov, open_=True, tray=tray)
        for x in (90, 205, 320):
            g += person(x, 645, 150, GREY, op=.85, dash=True)
        g += f"<circle cx='205' cy='390' r='42' fill='#FFFFFF' stroke='{GREY_D}' stroke-width='4'/>" + label(205, 407, "?", GREY_D, 50)
        g += tag(205, 290, "עוד לא מכירים אתכם", "#FFFFFF", GREY_D, 30)
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='800' viewBox='0 0 {w} 800'>"
        g += f"<line x1='470' y1='20' x2='470' y2='650' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        g += counter(560)
        # right (read first): started a week before
        g += tag(705, 70, "שבוע לפני העונה", "#FFFFFF", GREY_D, 30)
        for x in (600, 705, 810):
            g += person(x, 255, 100, GREY, op=.8, dash=True)
        g += bowl(705, 560, 330, .05, "רק התחלנו", grey=True, fs=30)
        g += label(705, 680, "פוגשים אתכם בפעם הראשונה", INK, 30) + label(705, 724, "ועוד לא יודעים מה אתם מציעים", SUB, 26)
        # left: started months before
        g += tag(235, 70, "חודשים לפני העונה", "#FFFFFF", MINT_D, 30)
        g += bowl(235, 560, 330, 1.0, "תפח עם הזמן", fs=30)
        for x, h, f in ((130, 105, MINT), (235, 95, MINT_L), (340, 105, MINT)):
            g += person(x, 255, h, f)
        g += label(235, 680, "כבר מכירים אתכם", MINT_D, 30) + label(235, 724, "ראו את העבודה לאורך זמן", SUB, 26)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; n = len(labels); rows = ""
        for i, l in enumerate(labels):
            last = i == n - 1
            rows += (f"<div style='display:flex;align-items:center;gap:24px;padding:14px 0;border-bottom:3px {'none' if last else 'dotted'} {GREY}'>"
                     f"<span style='flex:none;width:62px;height:62px;border-radius:50%;background:{'#FFFFFF' if last else MINT};"
                     f"border:3.5px {'dashed' if last else 'solid'} {INK};display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:900;color:{INK}'>{i + 1}</span>"
                     f"<span style='font-size:42px;font-weight:900;color:{SUB if last else INK}'>{l}</span></div>")
        return (f"<div style='width:820px;background:#FFFDF6;border:5px solid {INK};border-radius:22px;padding:34px 54px 26px;"
                f"box-shadow:14px 16px 0 rgba(16,27,79,.14);transform:rotate(-1deg)'>"
                f"<div style='display:flex;justify-content:space-between;align-items:center;border-bottom:5px solid {INK};padding-bottom:14px;margin-bottom:6px'>"
                f"<span style='font-size:40px;font-weight:900;color:{INK}'>מתכון: קהל רלוונטי</span>"
                f"<span style='font-size:28px;font-weight:800;color:#FFFFFF;background:{RED};border-radius:999px;padding:6px 20px'>זמן: לאורך זמן</span></div>"
                f"{rows}</div>")
    if k == "one":
        g = f"<svg width='{w}' height='600' viewBox='0 0 {w} 600'>"
        g += counter(530)
        g += loaf(450, 530, 400)
        for x, h, f in ((95, 170, MINT), (855, 180, MINT), (750, 120, MINT_L)):
            g += person(x, 530, h, f)
        return g + "</svg>"
    return ""


def tiles(end=False):
    rows = ""
    tw, th = 120, 60
    for r in range(0, 1350 // th + 1):
        off = 0 if r % 2 == 0 else tw / 2
        for c in range(-1, 1080 // tw + 2):
            rows += f"<rect x='{c * tw + off:.0f}' y='{r * th}' width='{tw}' height='{th}' fill='none' stroke='{GROUT}' stroke-width='4'/>"
    return f"<svg width='1080' height='1350' viewBox='0 0 1080 1350' style='position:absolute;inset:0;opacity:{.55 if end else 1}'>{rows}</svg>"


def ad_dough(spec):
    return frame(spec, scene, tiles, BG)
