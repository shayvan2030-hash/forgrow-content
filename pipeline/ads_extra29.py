"""Extra ad layouts, set 29 (added 2026-11-23).

ad_windows — carousel on a dusk-sky gradient (lavender to peach) with a few faint stars: a neighbourhood street
          of building facades seen from the front, with a small bakery at street level.
          Business problem: a neighbourhood business gets likes from far away (another city, abroad, random scrolling),
          while the people who live nearby don't know it exists — the windows on its own street stay dark.
          A relevant audience = windows that light up near the business, one by one
          (discover -> follow -> keep seeing -> understand the offer -> maybe reach out).
          Illustration only (fictional bakery, labelled "המחשה"). Original logo on a navy tile.
"""
import math

from render import THEME as T, logo
from ads_extra import NAVY, NAVY3
from ads_extra28 import label, person, arrow, tag

MINT = T["acc"]
MINT_L = "#B5F1DF"
INK = "#101B4F"
MINT_D = "#0B7F62"
SUB = "#33407F"
DARK_WIN = "#5A628F"
GREY = "#D3D5DE"
GREY_D = "#6E7390"
WALLS = ("#F3E6D8", "#E7D3C3", "#DCDDF1", "#F1DCCF")
RED = "#E2574C"
BREAD = "#D99A55"


def heart(cx, cy, s, fill="#FFFFFF", stroke=RED, op=1):
    return (f"<path transform='translate({cx:.1f} {cy:.1f}) scale({s:.2f})' opacity='{op}' "
            f"d='M 0,9 C -14,-1 -18,-10 -11,-16 C -6,-20 -1,-17 0,-12 C 1,-17 6,-20 11,-16 C 18,-10 14,-1 0,9 Z' "
            f"fill='{fill}' stroke='{stroke}' stroke-width='{2.6 / s:.2f}' stroke-linejoin='round'/>")


def window(x, y, w, h, lit):
    if lit:
        return (f"<rect x='{x - 6:.1f}' y='{y - 6:.1f}' width='{w + 12:.1f}' height='{h + 12:.1f}' rx='8' fill='{MINT}' opacity='.28'/>"
                f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h:.1f}' rx='4' fill='{MINT}' stroke='{INK}' stroke-width='3'/>"
                f"<line x1='{x + w / 2:.1f}' y1='{y:.1f}' x2='{x + w / 2:.1f}' y2='{y + h:.1f}' stroke='{INK}' stroke-width='2' opacity='.5'/>")
    return (f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h:.1f}' rx='4' fill='{DARK_WIN}' stroke='{INK}' stroke-width='3'/>"
            f"<line x1='{x + w / 2:.1f}' y1='{y:.1f}' x2='{x + w / 2:.1f}' y2='{y + h:.1f}' stroke='{INK}' stroke-width='2' opacity='.35'/>")


def building(x, by, w, floors, cols, wall, lit=(), roof="flat", fh=78, clear_y=None):
    """Facade with `floors` rows of `cols` windows; `lit` = set of (floor, col), floor 0 = top."""
    h = floors * fh + 24
    y = by - h
    g = f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h:.1f}' fill='{wall}' stroke='{INK}' stroke-width='4'/>"
    if roof == "flat":
        g += f"<rect x='{x - 8:.1f}' y='{y - 14:.1f}' width='{w + 16:.1f}' height='16' fill='{wall}' stroke='{INK}' stroke-width='4'/>"
    elif roof == "tank":
        g += f"<rect x='{x - 8:.1f}' y='{y - 14:.1f}' width='{w + 16:.1f}' height='16' fill='{wall}' stroke='{INK}' stroke-width='4'/>"
        g += (f"<rect x='{x + w * .62:.1f}' y='{y - 52:.1f}' width='{w * .22:.1f}' height='38' rx='6' fill='#FFFFFF' stroke='{INK}' stroke-width='3'/>"
              f"<line x1='{x + w * .66:.1f}' y1='{y - 14:.1f}' x2='{x + w * .66:.1f}' y2='{y - 22:.1f}' stroke='{INK}' stroke-width='3'/>")
    else:
        g += f"<path d='M {x - 10:.1f},{y:.1f} L {x + w / 2:.1f},{y - 60:.1f} L {x + w + 10:.1f},{y:.1f} Z' fill='{RED}' stroke='{INK}' stroke-width='4' stroke-linejoin='round'/>"
    ww = w / cols * .5
    wh = fh * .52
    for r in range(floors):
        for c in range(cols):
            wx = x + w / cols * (c + .5) - ww / 2
            wy = y + 22 + r * fh
            if clear_y is not None and wy + wh > clear_y:
                continue
            g += window(wx, wy, ww, wh, (r, c) in lit)
    return g


def bakery(cx, by, w=230, open_=False, s=1.0):
    """Street-level bakery front: awning, sign with a loaf, door, display window."""
    return f"<g transform='translate({cx:.1f} {by:.1f}) scale({s:.3f}) translate({-cx:.1f} {-by:.1f})'>" + _bakery(cx, by, w, open_) + "</g>"


def _bakery(cx, by, w, open_):
    x = cx - w / 2
    h = 150
    y = by - h
    g = f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h:.1f}' fill='#FFFFFF' stroke='{INK}' stroke-width='4'/>"
    # sign
    g += f"<rect x='{x + 14:.1f}' y='{y - 56:.1f}' width='{w - 28:.1f}' height='48' rx='10' fill='{NAVY}' stroke='{INK}' stroke-width='3'/>"
    g += label(cx + 22, y - 21, "מאפייה", "#FFFFFF", 28)
    g += (f"<g transform='translate({x + 52:.1f} {y - 32:.1f})'><ellipse rx='24' ry='13' fill='{BREAD}' stroke='#FFFFFF' stroke-width='2.5'/>"
          + "".join(f"<line x1='{dx - 4}' y1='-8' x2='{dx + 4}' y2='8' stroke='#FFFFFF' stroke-width='2.5' stroke-linecap='round'/>" for dx in (-10, 0, 10))
          + "</g>")
    # awning
    n = 6
    for k in range(n):
        g += (f"<path d='M {x + k * w / n:.1f},{y:.1f} h {w / n:.1f} v 24 a {w / n / 2:.1f} {w / n / 2:.1f} 0 0 1 {-w / n:.1f} 0 Z' "
              f"fill='{MINT if k % 2 == 0 else '#FFFFFF'}' stroke='{INK}' stroke-width='3'/>")
    # door (right) + display window (left)
    dx = x + w - 78
    door_fill = "#FFE9A8" if open_ else NAVY
    g += f"<rect x='{dx:.1f}' y='{by - 96:.1f}' width='56' height='96' fill='{door_fill}' stroke='{INK}' stroke-width='3'/>"
    g += f"<circle cx='{dx + 12:.1f}' cy='{by - 46:.1f}' r='4' fill='{INK}'/>"
    g += f"<rect x='{x + 18:.1f}' y='{by - 96:.1f}' width='{w - 120:.1f}' height='62' rx='4' fill='#FFF6E8' stroke='{INK}' stroke-width='3'/>"
    for k in range(3):
        g += f"<ellipse cx='{x + 44 + k * 38:.1f}' cy='{by - 52:.1f}' rx='15' ry='9' fill='{BREAD}' stroke='{INK}' stroke-width='2'/>"
    return g


def street(x0, by, w, lit_sets, s=1.0, open_=False, shop=True):
    """Three buildings across width w starting at x0; bakery in the middle ground floor; sidewalk."""
    bw = (w - 20) / 3
    g = f"<rect x='{x0 - 20:.1f}' y='{by:.1f}' width='{w + 40:.1f}' height='22' fill='#B7BBD6' stroke='{INK}' stroke-width='4'/>"
    roofs = ("tank", "flat", "pitched")
    floors = (5, 4, 4)
    for k in range(3):
        bx = x0 + k * (bw + 10)
        cy = (by - 225 * s) if (shop and k == 1) else None
        g += building(bx, by, bw, floors[k] + (1 if k == 1 else 0), 2, WALLS[k], lit=lit_sets[k], roof=roofs[k], fh=78 * s, clear_y=cy)
    if shop:
        g += bakery(x0 + 1.5 * bw + 10, by, w=230, open_=open_, s=min(1.0, (bw + 40) / 230))
    return g


def lamp(x, by, h=210, on=False):
    g = f"<line x1='{x}' y1='{by}' x2='{x}' y2='{by - h}' stroke='{INK}' stroke-width='6' stroke-linecap='round'/>"
    g += f"<path d='M {x},{by - h} q 0,-26 30,-26' fill='none' stroke='{INK}' stroke-width='6' stroke-linecap='round'/>"
    if on:
        g += f"<circle cx='{x + 34}' cy='{by - h - 18}' r='30' fill='{MINT}' opacity='.3'/>"
    g += f"<ellipse cx='{x + 34}' cy='{by - h - 22}' rx='18' ry='9' fill='{MINT if on else '#FFFFFF'}' stroke='{INK}' stroke-width='3'/>"
    return g


ALL_DARK = (set(), set(), set())


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='680' viewBox='0 0 {w} 680'>"
        g += street(90, 640, 760, ALL_DARK)
        g += lamp(40, 640)
        for hx, hy, s, tx, ty in ((560, 150, 1.4, 820, 30), (380, 160, 1.2, 140, 40), (720, 215, 1.0, 905, 150)):
            g += heart(hx, hy, s)
            g += arrow(hx + (tx - hx) * .18, hy + (ty - hy) * .18, tx - (tx - hx) * .1, ty - (ty - hy) * .1, w=5)
        return g + "</svg>"
    if k == "far":
        g = f"<svg width='{w}' height='640' viewBox='0 0 {w} 640'>"
        g += street(250, 610, 440, ALL_DARK, s=.72, shop=True)
        cx, cy = 470, 300
        targets = ((150, 70, "עיר אחרת"), (470, 40, "צד שני של הארץ"), (790, 70, "חו״ל"),
                   (110, 260, "סתם גלילה"), (830, 260, "מכרים מפעם"))
        for tx, ty, txt in targets:
            a = math.atan2(ty - cy, tx - cx)
            g += arrow(cx + math.cos(a) * 40, cy + math.sin(a) * 40, tx - math.cos(a) * 90, ty - math.sin(a) * 40, w=5)
            g += heart(tx - math.cos(a) * 130, ty - math.sin(a) * 75 + 10, 1.0)
        for tx, ty, txt in targets:
            g += tag(tx, ty, txt, "#FFFFFF", GREY_D, 27)
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='800' viewBox='0 0 {w} 800'>"
        g += f"<line x1='470' y1='10' x2='470' y2='650' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        # right (read first): dark windows, hearts flying away off the top-right corner
        g += street(520, 600, 380, ALL_DARK, s=.72)
        for hx, hy, s in ((640, 150, 1.1), (760, 95, 1.3), (880, 60, .9)):
            g += heart(hx, hy, s)
        g += arrow(600, 200, 905, 30, w=5)
        g += label(705, 700, "לייקים מרחוק", INK, 36) + label(705, 746, "בשכונה לא יודעים עליכם", SUB, 27)
        # left: windows light up nearby, a neighbour walks to the bakery
        lit = ({(1, 0), (2, 1), (3, 0), (4, 1)}, {(0, 1), (2, 0)}, {(1, 1), (2, 0), (3, 1)})
        g += street(40, 600, 380, lit, s=.72, open_=True)
        g += person(95, 600, 80, MINT)
        g += label(235, 700, "חלונות נדלקים", MINT_D, 36) + label(235, 746, "אנשים שאולי צריכים אתכם", SUB, 27)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; n = len(labels); rows = ""
        for i, l in enumerate(labels):
            last = i == n - 1
            win = (f"<div style='width:70px;height:54px;flex:none;border-radius:6px;border:3px {'dashed' if last else 'solid'} "
                   f"{MINT_D if last else INK};background:{'#FFFFFF' if last else (MINT if i % 2 == 0 else MINT_L)};"
                   f"box-shadow:{'none' if last else '0 0 0 8px rgba(20,216,165,.22)'};display:flex;align-items:center;justify-content:center;"
                   f"font-size:30px;font-weight:900;color:{INK}'>{i + 1}</div>")
            rows += (f"<div style='display:flex;align-items:center;gap:30px;padding:12px 0'>{win}"
                     f"<span style='font-size:42px;font-weight:900;color:{SUB if last else INK}'>{l}</span></div>")
        return (f"<div style='width:840px;background:{WALLS[0]};border:6px solid {INK};border-radius:20px;overflow:hidden;"
                f"box-shadow:12px 14px 0 rgba(16,27,79,.14)'>"
                f"<div style='background:{NAVY};color:#fff;font-size:32px;font-weight:900;padding:18px 34px;display:flex;align-items:center;gap:18px'>"
                f"<span style='width:18px;height:18px;border-radius:50%;background:{MINT};flex:none'></span>חלון אחרי חלון</div>"
                f"<div style='padding:14px 44px 18px 44px;display:flex;flex-direction:column'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='620' viewBox='0 0 {w} 620'>"
        lit = ({(0, 0), (1, 1), (2, 0), (3, 1), (4, 0)}, {(0, 1), (1, 0), (2, 1), (3, 0)}, {(0, 0), (1, 1), (3, 0)})
        g += street(300, 590, 600, lit, s=.82, open_=True)
        g += lamp(215, 590, 200, on=True)
        g += person(140, 590, 100, MINT)
        g += person(55, 590, 86, MINT_L)
        return g + "</svg>"
    return ""


def sky(end=False):
    stars = ""
    for x, y, r in ((120, 210, 3), (300, 120, 2), (520, 260, 2.5), (760, 150, 3), (960, 90, 2), (880, 330, 2), (60, 420, 2)):
        stars += f"<circle cx='{x}' cy='{y}' r='{r}' fill='#FFFFFF'/>"
    return (f"<svg width='1080' height='1350' viewBox='0 0 1080 1350' style='position:absolute;inset:0;opacity:{.5 if end else .8}'>"
            f"{stars}</svg>")


def ad_windows(spec):
    slides = spec["slides"]; n = len(slides); out = []
    bg = "background:linear-gradient(180deg,#C9CDEF 0%,#E4D6EC 45%,#FBDCC8 100%)"
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT_D if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        end = s.get("layout") == "end"
        wrap = (f"<style>.bg mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='bg' style='position:absolute;inset:0;overflow:hidden;color:{INK};{bg}'>{sky(end)}")
        tl = f"<div style='background:{NAVY};border-radius:22px;padding:14px 22px;display:inline-flex'>{logo(52)}</div>"
        if end:
            body = wrap + f"""<div style='position:absolute;inset:0;padding:110px 90px;display:flex;flex-direction:column;justify-content:center;gap:40px'>
              <div style='background:{NAVY};border-radius:30px;padding:24px 34px;align-self:flex-start;display:flex'>{logo(110)}</div>
              <h2 style='font-size:{s.get('size', 60)}px;line-height:1.2'>{s['head']}</h2>
              <p style='font-size:36px;color:{SUB};font-weight:700'>{s.get('body', '')}</p>
              <div><div style='display:inline-block;background:{MINT};color:{NAVY3};font-weight:800;font-size:40px;padding:24px 44px;border-radius:999px;box-shadow:0 6px 0 {INK}'>{s['cta']}</div></div>
              <div><span style='display:inline-block;font-size:26px;font-weight:700;padding:8px 20px;border-radius:999px;border:2px solid {SUB};color:{SUB};background:#FFFFFF'>{s.get('tag', '')}</span></div></div></div>"""
        else:
            st = (f"<div style='position:absolute;left:96px;bottom:{s.get('stamp_bottom', 640)}px;transform:rotate(4deg);background:{NAVY};"
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
