"""Extra ad layouts, set 36 (added 2026-11-27).

ad_corkboard — carousel on a warm pinstriped wall: a cork pin-board with postcards that arrive from far away
          (each with a heart and a postmark place), next to a small neighbourhood shop. Business problem: a local business (fictional neighbourhood studio) gets lots of love for its
          content, but most of the people who see it live far away and cannot actually come in. A relevant audience —
          people who can realistically become customers — can start a route (discover -> follow -> keep seeing ->
          understand the offer -> maybe reach out), shown as five numbered notes pinned on a cork strip. Illustration only.
          Original logo on a navy tile.
"""
from ads_extra import NAVY
from ads_extra28 import label, person, tag
from ads_extra31 import frame, MINT, MINT_L, INK, MINT_D, SUB, GREY, GREY_D

BG = "#F4EEE6"
CORK = "#D9B07E"
CORK_D = "#B98A55"
FRAME = "#8A5A33"
POST = "#FFFDF7"
RED = "#E8735A"
BRICK = "#F2E6D8"


def shop(cx, by, w, sign="הסטודיו", awn=MINT, door_open=False, op=1):
    """Small neighbourhood shop front with a striped awning."""
    h = w * .78
    x, y = cx - w / 2, by - h
    g = f"<g opacity='{op}'>"
    g += f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h:.1f}' fill='{BRICK}' stroke='{INK}' stroke-width='5'/>"
    g += f"<rect x='{x + w * .1:.1f}' y='{y - h * .2:.1f}' width='{w * .8:.1f}' height='{h * .18:.1f}' rx='8' fill='{NAVY}' stroke='{INK}' stroke-width='4'/>"
    g += label(cx, y - h * .2 + h * .13, sign, "#FFFFFF", h * .12)
    n = 6; sw = (w + 24) / n
    for k in range(n):
        f = awn if k % 2 == 0 else "#FFFFFF"
        ax = x - 12 + k * sw
        g += (f"<path d='M {ax:.1f},{y:.1f} L {ax + sw:.1f},{y:.1f} L {ax + sw:.1f},{y + h * .16:.1f} "
              f"Q {ax + sw / 2:.1f},{y + h * .26:.1f} {ax:.1f},{y + h * .16:.1f} Z' fill='{f}' stroke='{INK}' stroke-width='4' stroke-linejoin='round'/>")
    dw, dh = w * .26, h * .56
    dx = x + w * .62
    dfill = "#FFF6C8" if door_open else "#C5CBEE"
    g += f"<rect x='{dx:.1f}' y='{by - dh:.1f}' width='{dw:.1f}' height='{dh:.1f}' fill='{dfill}' stroke='{INK}' stroke-width='4'/>"
    if door_open:
        g += f"<path d='M {dx:.1f},{by - dh:.1f} L {dx - dw * .45:.1f},{by - dh + 14:.1f} L {dx - dw * .45:.1f},{by + 6:.1f} L {dx:.1f},{by:.1f} Z' fill='{MINT_L}' stroke='{INK}' stroke-width='4' stroke-linejoin='round'/>"
    else:
        g += f"<circle cx='{dx + dw * .2:.1f}' cy='{by - dh * .45:.1f}' r='5' fill='{INK}'/>"
    g += f"<rect x='{x + w * .1:.1f}' y='{by - dh:.1f}' width='{w * .4:.1f}' height='{dh * .58:.1f}' fill='#DDE7F7' stroke='{INK}' stroke-width='4'/>"
    g += f"<line x1='{x + w * .3:.1f}' y1='{by - dh:.1f}' x2='{x + w * .3:.1f}' y2='{by - dh * .42:.1f}' stroke='{INK}' stroke-width='3'/>"
    return g + "</g>"


def pushpin(cx, cy, col=RED, r=13):
    return (f"<ellipse cx='{cx + 6:.1f}' cy='{cy + 10:.1f}' rx='{r:.1f}' ry='{r * .5:.1f}' fill='{INK}' opacity='.18'/>"
            f"<circle cx='{cx:.1f}' cy='{cy:.1f}' r='{r:.1f}' fill='{col}' stroke='{INK}' stroke-width='3.5'/>"
            f"<circle cx='{cx - r * .35:.1f}' cy='{cy - r * .35:.1f}' r='{r * .3:.1f}' fill='#FFFFFF' opacity='.7'/>")


def heart(cx, cy, s=1.0, fill=RED):
    return (f"<path transform='translate({cx:.1f} {cy:.1f}) scale({s:.2f})' d='M 0,14 C -26,-4 -18,-26 0,-14 C 18,-26 26,-4 0,14 Z' "
            f"fill='{fill}' stroke='{INK}' stroke-width='3.5' stroke-linejoin='round'/>")


def postcard(cx, cy, w, place, ang=0, pin_col=RED, grey=False, op=1):
    """Postcard: picture half with a heart on the left, address lines + stamp + round postmark (place) on the right."""
    h = w * .64
    x, y = -w / 2, -h / 2
    edge = GREY_D if grey else INK
    d = " stroke-dasharray='8 6'" if grey else ""
    g = f"<g transform='translate({cx:.1f} {cy:.1f}) rotate({ang})' opacity='{op}'>"
    g += f"<rect x='{x + 8:.1f}' y='{y + 10:.1f}' width='{w:.1f}' height='{h:.1f}' rx='6' fill='{INK}' opacity='.12'/>"
    g += f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h:.1f}' rx='6' fill='{POST}' stroke='{edge}' stroke-width='4'{d}/>"
    g += f"<rect x='{x + 12:.1f}' y='{y + 12:.1f}' width='{w * .42:.1f}' height='{h - 24:.1f}' rx='4' fill='{'#E4E6EE' if grey else '#DDE7F7'}'/>"
    g += heart(x + 12 + w * .21, 6, w / 260, GREY if grey else RED)
    g += f"<line x1='{x + w * .5:.1f}' y1='{y + 16:.1f}' x2='{x + w * .5:.1f}' y2='{y + h - 16:.1f}' stroke='{edge}' stroke-width='2' opacity='.5'/>"
    sx = x + w - 14 - w * .16
    g += f"<rect x='{sx:.1f}' y='{y + 14:.1f}' width='{w * .16:.1f}' height='{w * .19:.1f}' fill='{MINT_L if not grey else '#ECEDF2'}' stroke='{edge}' stroke-width='2.5' stroke-dasharray='4 3'/>"
    for k in range(3):
        ly = y + h * .55 + k * h * .14
        g += f"<line x1='{x + w * .56:.1f}' y1='{ly:.1f}' x2='{x + w - 16:.1f}' y2='{ly:.1f}' stroke='{edge}' stroke-width='2' opacity='.35'/>"
    fs = max(18, w * .085)
    fs = min(fs, (w * .38) / max(1, len(place) * .55))
    px0, py0 = x + w * .6, y + h * .26
    for k in range(3):
        yy = py0 + k * 10
        g += (f"<path d='M {px0:.1f},{yy:.1f} q 8,-6 16,0 t 16,0 t 16,0 t 16,0' fill='none' stroke='{SUB}' stroke-width='2.5' opacity='.6'/>")
    g += (f"<rect x='{x + w * .54:.1f}' y='{y + h * .5 - fs * .1:.1f}' width='{w * .42:.1f}' height='{fs * 1.5:.1f}' rx='6' fill='{'#FFFFFF' if grey else NAVY}'/>"
          + label(x + w * .75, y + h * .5 + fs * 1.0, place, GREY_D if grey else "#FFFFFF", fs))
    if pin_col:
        g += pushpin(0, y + 6, pin_col)
    return g + "</g>"


def corkboard(x, y, w, h):
    g = f"<rect x='{x + 14:.1f}' y='{y + 16:.1f}' width='{w:.1f}' height='{h:.1f}' rx='14' fill='{INK}' opacity='.14'/>"
    g += f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h:.1f}' rx='14' fill='{FRAME}' stroke='{INK}' stroke-width='5'/>"
    g += f"<rect x='{x + 18:.1f}' y='{y + 18:.1f}' width='{w - 36:.1f}' height='{h - 36:.1f}' rx='6' fill='{CORK}' stroke='{INK}' stroke-width='3'/>"
    import random
    rnd = random.Random(7)
    for _ in range(int(w * h / 1400)):
        px, py = x + 24 + rnd.random() * (w - 48), y + 24 + rnd.random() * (h - 48)
        g += f"<circle cx='{px:.1f}' cy='{py:.1f}' r='{1.5 + rnd.random() * 2:.1f}' fill='{CORK_D}' opacity='.7'/>"
    return g


def note(cx, cy, txt, ang=-3, w=330, fill="#FFFFFF", col=INK, size=36):
    return (f"<g transform='rotate({ang} {cx:.1f} {cy:.1f})'><rect x='{cx - w / 2 + 6:.1f}' y='{cy - 36:.1f}' width='{w:.1f}' height='72' fill='{INK}' opacity='.12'/>"
            f"<rect x='{cx - w / 2:.1f}' y='{cy - 42:.1f}' width='{w:.1f}' height='72' fill='{fill}' stroke='{INK}' stroke-width='3.5'/>"
            + label(cx, cy + 6, txt, col, size) + pushpin(cx, cy - 42, MINT) + "</g>")


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='720' viewBox='0 0 {w} 720'>"
        g += corkboard(40, 20, 860, 470)
        g += note(470, 92, "מאיפה העוקבים?", -2, 380)
        for cx, cy, pl, ang, pc in ((735, 230, "עיר אחרת", 5, RED), (470, 250, "חו״ל", -4, MINT), (210, 230, "רחוק", 3, "#8799DB"),
                                    (600, 390, "בצד השני", -3, "#F3C35B"), (300, 395, "שעה נסיעה", 4, RED)):
            g += postcard(cx, cy, 230, pl, ang, pc)
        g += f"<ellipse cx='470' cy='705' rx='430' ry='14' fill='{INK}' opacity='.07'/>"
        g += shop(470, 705, 220)
        return g + "</svg>"
    if k == "away":
        g = f"<svg width='{w}' height='700' viewBox='0 0 {w} 700'>"
        g += f"<ellipse cx='470' cy='660' rx='440' ry='20' fill='{INK}' opacity='.07'/>"
        g += shop(760, 660, 280)
        g += (f"<circle cx='890' cy='300' r='42' fill='#FFFFFF' stroke='{GREY_D}' stroke-width='4'/>"
              + label(890, 316, "?", GREY_D, 48))
        for (x1, y1, qx, qy) in ((60, 120, 300, 40), (40, 330, 300, 250), (80, 560, 330, 430)):
            g += f"<path d='M {x1},{y1} Q {qx},{qy} 600,440' fill='none' stroke='{GREY_D}' stroke-width='4' stroke-dasharray='4 14' stroke-linecap='round'/>"
        for cx, cy, pl, ang in ((250, 120, "עיר אחרת", -8), (150, 330, "חו״ל", 6), (290, 520, "רחוק", -5)):
            g += postcard(cx, cy, 200, pl, ang, None)
        g += tag(470, 610, "אוהבים מרחוק", "#FFFFFF", GREY_D, 32)
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='800' viewBox='0 0 {w} 800'>"
        g += f"<line x1='470' y1='20' x2='470' y2='640' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        # right (read first): far away — a pile of postcards, tiny dashed figures on a far horizon
        g += f"<path d='M 500,250 Q 700,220 930,250' fill='none' stroke='{GREY_D}' stroke-width='3' opacity='.5'/>"
        for x in (590, 680, 770, 860):
            g += person(x, 250, 70, GREY, op=.8, dash=True)
        g += f"<path d='M 705,290 L 705,340' stroke='{GREY_D}' stroke-width='4' stroke-dasharray='4 10' stroke-linecap='round'/>"
        for cx, cy, pl, ang in ((660, 450, "חו״ל", -10), (740, 430, "רחוק", 6), (705, 490, "עיר אחרת", -2)):
            g += postcard(cx, cy, 220, pl, ang, None, grey=True)
        g += label(705, 700, "רחוק מדי להגיע", INK, 34) + label(705, 746, "נהנים מהתוכן, ונשארים שם", SUB, 27)
        # left: people who can actually come in
        g += shop(260, 600, 260, door_open=True)
        g += person(85, 630, 170, MINT) + person(410, 630, 180, MINT) + person(325, 640, 140, MINT_L)
        g += label(235, 700, "יכולים להגיע אליכם", MINT_D, 34) + label(235, 746, "ואולי צריכים בדיוק אתכם", SUB, 27)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; n = len(labels); rows = ""
        pins = [RED, MINT, "#8799DB", "#F3C35B", MINT]
        for i, l in enumerate(labels):
            last = i == n - 1
            rot = (-.8, .7, -.5, .8, -.6)[i % 5]
            rows += (f"<div style='position:relative;display:flex;align-items:center;gap:22px;background:{'#FFFFFF' if not last else POST};"
                     f"border:3.5px {'dashed' if last else 'solid'} {MINT_D if last else INK};padding:6px 26px;transform:rotate({rot}deg);"
                     f"box-shadow:6px 8px 0 rgba(16,27,79,.15)'>"
                     f"<span style='position:absolute;top:-12px;right:50%;width:24px;height:24px;border-radius:50%;background:{pins[i]};border:3px solid {INK}'></span>"
                     f"<span style='flex:none;width:58px;height:58px;border-radius:50%;background:{INK if not last else '#FFFFFF'};"
                     f"border:3px solid {INK};display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:900;"
                     f"color:{'#FFFFFF' if not last else INK}'>{i + 1}</span>"
                     f"<span style='font-size:40px;font-weight:900;color:{SUB if last else INK}'>{l}</span></div>")
        return (f"<div style='width:860px;background:{FRAME};border:5px solid {INK};border-radius:16px;padding:18px;"
                f"box-shadow:14px 16px 0 rgba(16,27,79,.14)'>"
                f"<div style='background:{CORK};border:3px solid {INK};border-radius:6px;padding:34px 40px 34px;display:flex;flex-direction:column;gap:44px'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='620' viewBox='0 0 {w} 620'>"
        g += f"<ellipse cx='470' cy='590' rx='420' ry='20' fill='{INK}' opacity='.07'/>"
        g += shop(440, 590, 360, door_open=True)
        for x, h, f in ((150, 170, MINT), (770, 180, MINT), (870, 130, MINT_L)):
            g += person(x, 590, h, f)
        return g + "</svg>"
    return ""


def pinstripes(end=False):
    lines = "".join(f"<line x1='{x}' y1='0' x2='{x}' y2='1350' stroke='#E6D9C6' stroke-width='3'/>" for x in range(18, 1080, 36))
    return (f"<svg width='1080' height='1350' viewBox='0 0 1080 1350' style='position:absolute;inset:0;opacity:{.5 if end else .9}'>{lines}</svg>")


def ad_corkboard(spec):
    return frame(spec, scene, pinstripes, BG)
