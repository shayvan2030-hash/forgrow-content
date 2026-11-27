"""Extra ad layouts, set 36 (added 2026-11-27).

ad_departures — carousel on a pale steel-blue background with faint dashed flight arcs: an airport-style split-flap
          departures board. Business problem: a local business (fictional neighbourhood studio) gets lots of love for its
          content, but most of the people who see it live far away and cannot actually come in. A relevant audience —
          people who can realistically become customers — can start a route (discover -> follow -> keep seeing ->
          understand the offer -> maybe reach out), shown as five numbered flap rows. Illustration only.
          Original logo on a navy tile.
"""
from ads_extra import NAVY
from ads_extra28 import label, person, tag
from ads_extra31 import frame, MINT, MINT_L, INK, MINT_D, SUB, GREY, GREY_D

BG = "#E6ECF5"
BOARD = "#1C2438"
FLAP = "#2B3550"
AMBER = "#F3C35B"
RED = "#E8735A"
BRICK = "#F2E6D8"


def flap(x, y, w, h, txt, col=AMBER, size=None, fill=FLAP, dash=False):
    """One split-flap tile: dark rounded tile, a hairline split across the middle, text centred."""
    size = size or h * .55
    d = f" stroke='{MINT}' stroke-width='3' stroke-dasharray='7 6'" if dash else ""
    return (f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h:.1f}' rx='7' fill='{fill}'{d}/>"
            f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h / 2:.1f}' rx='7' fill='#FFFFFF' opacity='.04'/>"
            + label(x + w / 2, y + h / 2 + size * .36, txt, col, size, 800)
            + f"<line x1='{x:.1f}' y1='{y + h / 2:.1f}' x2='{x + w:.1f}' y2='{y + h / 2:.1f}' stroke='{BOARD}' stroke-width='3'/>")


def board(cx, y, w, rows, title, heads=("מאיפה", "מה עשו"), hl=None):
    """Departures board. rows: list of (place, status). RTL: place column on the right."""
    rh, gap, top = 62, 14, 112
    h = top + len(rows) * (rh + gap) + 22
    x = cx - w / 2
    g = f"<rect x='{x + 14:.1f}' y='{y + 16:.1f}' width='{w:.1f}' height='{h:.1f}' rx='22' fill='{INK}' opacity='.14'/>"
    g += f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h:.1f}' rx='22' fill='{BOARD}' stroke='{INK}' stroke-width='5'/>"
    g += f"<line x1='{cx - w * .2:.1f}' y1='{y - 40:.1f}' x2='{cx - w * .2:.1f}' y2='{y:.1f}' stroke='{INK}' stroke-width='6'/>"
    g += f"<line x1='{cx + w * .2:.1f}' y1='{y - 40:.1f}' x2='{cx + w * .2:.1f}' y2='{y:.1f}' stroke='{INK}' stroke-width='6'/>"
    g += plane(x + w - 52, y + 42, .55, 0, "#FFFFFF")
    g += f"<text x='{x + w - 96:.1f}' y='{y + 54:.1f}' font-family='Heebo' font-weight='900' font-size='36' text-anchor='start' fill='#FFFFFF' direction='rtl'>{title}</text>"
    pw, sw = w * .58, w * .32
    px = x + w - 24 - pw
    sx = x + 24
    g += f"<text x='{px + pw - 6:.1f}' y='{y + 96:.1f}' font-family='Heebo' font-weight='700' font-size='22' text-anchor='start' fill='#AEB6CF' direction='rtl'>{heads[0]}</text>"
    g += f"<text x='{sx + sw - 6:.1f}' y='{y + 96:.1f}' font-family='Heebo' font-weight='700' font-size='22' text-anchor='start' fill='#AEB6CF' direction='rtl'>{heads[1]}</text>"
    for i, (pl, stt) in enumerate(rows):
        ry = y + top + i * (rh + gap)
        c = MINT if hl is not None and i in hl else AMBER
        g += flap(px, ry, pw, rh, pl, c, 34)
        g += flap(sx, ry, sw, rh, stt, c, 32)
    return g


def plane(cx, cy, s=1.0, ang=0, col="#FFFFFF", stroke=INK, op=1):
    """Side-view-ish plane silhouette pointing left (= forward in RTL reading), centred at cx, cy."""
    return (f"<g transform='translate({cx:.1f} {cy:.1f}) rotate({ang}) scale({s:.2f})' opacity='{op}'>"
            f"<path d='M -62,0 C -62,-10 -48,-14 -36,-14 L 46,-14 L 64,-38 L 76,-38 L 68,-12 C 74,-8 74,8 68,10 L 46,14 L -36,14 C -48,14 -62,10 -62,0 Z' "
            f"fill='{col}' stroke='{stroke}' stroke-width='5' stroke-linejoin='round'/>"
            f"<path d='M 4,4 L 28,44 L 42,44 L 32,4 Z' fill='{col}' stroke='{stroke}' stroke-width='5' stroke-linejoin='round'/>"
            f"<path d='M 6,-6 L 26,-34 L 38,-34 L 30,-6 Z' fill='{col}' stroke='{stroke}' stroke-width='4' stroke-linejoin='round' opacity='.85'/>"
            f"<circle cx='-40' cy='-2' r='4' fill='{stroke}'/><circle cx='-26' cy='-2' r='4' fill='{stroke}'/><circle cx='-12' cy='-2' r='4' fill='{stroke}'/></g>")


def traveller(cx, by, h, op=.9):
    """Grey dashed person pulling a small suitcase."""
    g = person(cx, by, h, GREY, op=op, dash=True)
    sw, sh = h * .3, h * .36
    sx = cx + h * .34
    g += (f"<g opacity='{op}'><line x1='{sx + sw * .5:.1f}' y1='{by - sh - 4:.1f}' x2='{cx + h * .26:.1f}' y2='{by - h * .4:.1f}' stroke='{INK}' stroke-width='4'/>"
          f"<rect x='{sx:.1f}' y='{by - sh - 8:.1f}' width='{sw:.1f}' height='{sh:.1f}' rx='8' fill='#FFFFFF' stroke='{INK}' stroke-width='4' stroke-dasharray='7 6'/>"
          f"<line x1='{sx + sw * .35:.1f}' y1='{by - sh:.1f}' x2='{sx + sw * .35:.1f}' y2='{by - 16:.1f}' stroke='{GREY_D}' stroke-width='3'/>"
          f"<line x1='{sx + sw * .65:.1f}' y1='{by - sh:.1f}' x2='{sx + sw * .65:.1f}' y2='{by - 16:.1f}' stroke='{GREY_D}' stroke-width='3'/>"
          f"<circle cx='{sx + 8:.1f}' cy='{by - 4:.1f}' r='5' fill='{INK}'/><circle cx='{sx + sw - 8:.1f}' cy='{by - 4:.1f}' r='5' fill='{INK}'/></g>")
    return g


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


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='720' viewBox='0 0 {w} 720'>"
        g += board(470, 50, 860, [("עיר אחרת", "לייק"), ("חו״ל", "לייק"), ("שעתיים נסיעה", "שמירה"), ("הצד השני של הארץ", "לייק")],
                   "מאיפה העוקבים?")
        g += f"<ellipse cx='470' cy='700' rx='430' ry='16' fill='{INK}' opacity='.07'/>"
        g += shop(720, 700, 250)
        g += f"<path d='M 90,700 Q 200,660 300,600' fill='none' stroke='{GREY_D}' stroke-width='5' stroke-dasharray='4 14' stroke-linecap='round'/>"
        g += plane(350, 580, .9, -28)
        return g + "</svg>"
    if k == "away":
        g = f"<svg width='{w}' height='700' viewBox='0 0 {w} 700'>"
        g += f"<ellipse cx='470' cy='660' rx='440' ry='20' fill='{INK}' opacity='.07'/>"
        g += shop(780, 660, 250)
        g += (f"<circle cx='890' cy='290' r='42' fill='#FFFFFF' stroke='{GREY_D}' stroke-width='4'/>"
              + label(890, 306, "?", GREY_D, 48))
        for x, h, op in ((500, 200, .9), (300, 180, .8), (110, 160, .7)):
            g += traveller(x, 660, h, op)
        g += f"<path d='M 560,250 Q 300,120 90,180' fill='none' stroke='{GREY_D}' stroke-width='5' stroke-dasharray='4 14' stroke-linecap='round'/>"
        g += plane(110, 170, .8, -8, "#FFFFFF")
        g += tag(330, 300, "אוהבים מרחוק", "#FFFFFF", GREY_D, 34)
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='800' viewBox='0 0 {w} 800'>"
        g += f"<line x1='470' y1='20' x2='470' y2='640' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        # right (read first): far away, can't come in
        g += plane(720, 170, 1.1, -14)
        g += f"<path d='M 880,330 Q 800,260 760,210' fill='none' stroke='{GREY_D}' stroke-width='5' stroke-dasharray='4 14' stroke-linecap='round'/>"
        g += traveller(760, 630, 230)
        g += traveller(560, 630, 190, .75)
        g += label(705, 700, "רחוק מדי להגיע", INK, 34) + label(705, 746, "נהנים מהתוכן, ונשארים שם", SUB, 27)
        # left: people who can actually come in
        g += shop(260, 600, 260, door_open=True)
        g += person(85, 630, 170, MINT) + person(410, 630, 180, MINT) + person(325, 640, 140, MINT_L)
        g += label(235, 700, "יכולים להגיע אליכם", MINT_D, 34) + label(235, 746, "ואולי צריכים בדיוק אתכם", SUB, 27)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; n = len(labels); rows = ""
        for i, l in enumerate(labels):
            last = i == n - 1
            num = (f"<span style='flex:none;width:66px;height:66px;border-radius:8px;background:{FLAP};"
                   f"border:3px {'dashed' if last else 'solid'} {MINT if last else FLAP};display:flex;align-items:center;justify-content:center;"
                   f"font-size:34px;font-weight:900;color:{MINT};position:relative'>{i + 1}"
                   f"<i style='position:absolute;left:0;right:0;top:50%;height:3px;background:{BOARD}'></i></span>")
            txt = (f"<span style='flex:1;height:66px;border-radius:8px;background:{FLAP};display:flex;align-items:center;padding:0 24px;"
                   f"font-size:40px;font-weight:800;color:{'#AEB6CF' if last else '#FFFFFF'};position:relative;"
                   f"{'border:3px dashed ' + MINT + ';' if last else ''}'>{l}"
                   f"<i style='position:absolute;left:0;right:0;top:50%;height:3px;background:{BOARD}'></i></span>")
            rows += f"<div style='display:flex;align-items:center;gap:14px'>{num}{txt}</div>"
        return (f"<div style='width:860px;background:{BOARD};border:6px solid {INK};border-radius:22px;overflow:hidden;"
                f"box-shadow:14px 16px 0 rgba(16,27,79,.14)'>"
                f"<div style='color:#fff;font-size:34px;font-weight:900;padding:24px 34px 8px;display:flex;align-items:center;gap:18px'>"
                f"<span style='width:18px;height:18px;border-radius:50%;background:{MINT};flex:none'></span>שלב אחרי שלב, לאורך זמן</div>"
                f"<div style='padding:14px 30px 30px;display:flex;flex-direction:column;gap:14px'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='620' viewBox='0 0 {w} 620'>"
        g += f"<ellipse cx='470' cy='590' rx='420' ry='20' fill='{INK}' opacity='.07'/>"
        g += shop(440, 590, 360, door_open=True)
        for x, h, f in ((150, 170, MINT), (770, 180, MINT), (870, 130, MINT_L)):
            g += person(x, 590, h, f)
        return g + "</svg>"
    return ""


def arcs(end=False):
    g = (f"<svg width='1080' height='1350' viewBox='0 0 1080 1350' style='position:absolute;inset:0;opacity:{.35 if end else .55}'>")
    for (x1, y1, qx, qy, x2, y2) in ((-40, 420, 540, 120, 1120, 360), (-40, 980, 400, 700, 1120, 880), (-40, 1300, 620, 1080, 1120, 1240)):
        g += (f"<path d='M {x1},{y1} Q {qx},{qy} {x2},{y2}' fill='none' stroke='#8799DB' stroke-width='3' "
              f"stroke-dasharray='6 16' stroke-linecap='round'/>")
    return g + "</svg>"


def ad_departures(spec):
    return frame(spec, scene, arcs, BG)
