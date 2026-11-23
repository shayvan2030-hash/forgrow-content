"""Extra ad layouts, set 30 (added 2026-11-23).

ad_megaphone — carousel on a pale coral background with a faint pop-art halftone dot pattern: a megaphone.
          Business problem: a small-business owner who is uncomfortable "pushing sales" on Instagram, yet feels they
          have to shout louder (another promo, "last chance!!") because the people who see the content aren't related
          to the business and keep scrolling. With a relevant audience you can talk at eye level: people discover,
          follow, keep seeing the content, understand the offer and may reach out
          (route shown as numbered speech bubbles). Illustration only. Original logo on a navy tile.
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3
from ads_extra28 import label, person, tag

MINT = T["acc"]
MINT_L = "#B5F1DF"
INK = "#101B4F"
MINT_D = "#0B7F62"
SUB = "#33407F"
GREY = "#D3D5DE"
GREY_D = "#6E7390"
RED = "#E2574C"
BG = "#FCE6DD"
DOT = "#F2B9A6"


def megaphone(x, y, s=1.0, color=RED, flip=False, rot=0):
    """Megaphone whose mouthpiece is at (x, y); bell opens to the left (or right if flip)."""
    sx = s if flip else -s
    g = f"<g transform='translate({x:.1f} {y:.1f}) rotate({rot}) scale({sx:.2f} {s:.2f})'>"
    g += f"<rect x='-34' y='-20' width='40' height='40' rx='8' fill='{NAVY}' stroke='{INK}' stroke-width='4'/>"
    g += f"<path d='M 6,-34 L 170,-92 L 170,92 L 6,34 Z' fill='{color}' stroke='{INK}' stroke-width='5' stroke-linejoin='round'/>"
    g += f"<path d='M 40,-46 L 150,-85 L 150,-60 L 40,-26 Z' fill='#FFFFFF' opacity='.45'/>"
    g += f"<ellipse cx='170' cy='0' rx='20' ry='92' fill='#FFFFFF' stroke='{INK}' stroke-width='5'/>"
    g += f"<path d='M 30,30 L 46,92 L 74,92 L 66,40' fill='{NAVY}' stroke='{INK}' stroke-width='4' stroke-linejoin='round'/>"
    return g + "</g>"


def loud_waves(x, y, n=3, s=1.0, flip=False, color=RED):
    """Jagged shout lines fanning out from (x, y)."""
    d = 1 if flip else -1
    g = ""
    for k in range(n):
        r = (40 + k * 46) * s
        pts = []
        for j in range(9):
            t = -1 + j / 4
            rr = r + (12 * s if j % 2 else 0)
            pts.append((x + d * rr * (1 - .25 * t * t), y + t * r * .95))
        p = "M " + " L ".join(f"{a:.1f},{b:.1f}" for a, b in pts)
        g += f"<path d='{p}' fill='none' stroke='{color}' stroke-width='{7 * s:.1f}' stroke-linejoin='round' stroke-linecap='round'/>"
    return g


def soft_waves(x, y, n=2, s=1.0, flip=False, color=MINT_D):
    d = 1 if flip else -1
    g = ""
    for k in range(n):
        r = (34 + k * 32) * s
        g += (f"<path d='M {x + d * r * .55:.1f},{y - r * .8:.1f} Q {x + d * r * 1.1:.1f},{y:.1f} {x + d * r * .55:.1f},{y + r * .8:.1f}' "
              f"fill='none' stroke='{color}' stroke-width='{6 * s:.1f}' stroke-linecap='round'/>")
    return g


def shout(cx, cy, txt, size=34, rot=0):
    w = len(txt) * size * .56 + 44
    return (f"<g transform='rotate({rot} {cx} {cy})'><rect x='{cx - w / 2:.1f}' y='{cy - size * .95:.1f}' width='{w:.1f}' height='{size * 1.7:.1f}' "
            f"rx='12' fill='#FFFFFF' stroke='{RED}' stroke-width='4'/>" + label(cx, cy + size * .32, txt, RED, size, 900) + "</g>")


def walker(cx, by, h, phone=True, op=1):
    """Grey dashed figure with a phone (busy scrolling), and motion marks."""
    g = person(cx, by, h, GREY, op=op, dash=True)
    if phone:
        g += (f"<rect x='{cx - h * .1:.1f}' y='{by - h * .5:.1f}' width='{h * .2:.1f}' height='{h * .3:.1f}' rx='4' "
              f"fill='{NAVY}' stroke='{INK}' stroke-width='3' opacity='{op}'/>")
    return g


def bubble(cx, cy, w, h, fill, dots=True, stroke=INK):
    tx = cx + w * .18
    yb = cy + h / 2
    g = (f"<path d='M {tx:.1f},{yb - 4:.1f} L {tx + 6:.1f},{yb + 34:.1f} L {tx + 30:.1f},{yb - 4:.1f} Z' fill='{fill}' stroke='{stroke}' stroke-width='4' stroke-linejoin='round'/>"
         f"<rect x='{cx - w / 2:.1f}' y='{cy - h / 2:.1f}' width='{w:.1f}' height='{h:.1f}' rx='{h / 2:.1f}' fill='{fill}' stroke='{stroke}' stroke-width='4'/>"
         f"<rect x='{tx + 3:.1f}' y='{yb - 6:.1f}' width='24' height='9' fill='{fill}'/>")
    if dots:
        for k in (-1, 0, 1):
            g += f"<circle cx='{cx + k * h * .32:.1f}' cy='{cy:.1f}' r='{h * .09:.1f}' fill='{INK}'/>"
    return g


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='640' viewBox='0 0 {w} 640'>"
        g += loud_waves(470, 360, 3, 1.3)
        g += megaphone(720, 360, 1.5, rot=-8)
        g += shout(210, 150, "מבצע!!!", 40, -8)
        g += shout(150, 380, "רק היום!", 36, 5)
        g += shout(250, 560, "הזדמנות אחרונה!!", 32, -4)
        return g + "</svg>"
    if k == "away":
        g = f"<svg width='{w}' height='640' viewBox='0 0 {w} 640'>"
        g += megaphone(800, 300, 1.05, rot=-4)
        g += loud_waves(615, 290, 3, 1.0)
        for x, by, h, op in ((360, 420, 120, .95), (200, 560, 110, .8), (90, 330, 96, .65), (380, 620, 96, .7)):
            g += walker(x, by, h, op=op)
        g += tag(150, 70, "ממשיכים לגלול", "#FFFFFF", GREY_D, 28)
        g += tag(470, 120, "לא קשור אליהם", "#FFFFFF", GREY_D, 28)
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='800' viewBox='0 0 {w} 800'>"
        g += f"<line x1='470' y1='20' x2='470' y2='640' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        # right (read first): loud megaphone, people walking away with phones
        g += megaphone(890, 200, .75, rot=-6)
        g += loud_waves(755, 195, 3, .8)
        g += shout(640, 60, "קנו עכשיו!!", 26, -6)
        for x, by, h, op in ((560, 470, 92, .9), (700, 600, 92, .7), (850, 470, 84, .55)):
            g += walker(x, by, h, op=op)
        g += label(705, 700, "צועקים לכולם", INK, 36) + label(705, 746, "וזה מרגיש כמו לדחוף", SUB, 27)
        # left: megaphone resting on the ground, a calm speech bubble, mint people close by
        g += bubble(235, 150, 190, 92, "#FFFFFF")
        for x, by, h, f in ((110, 470, 96, MINT), (235, 500, 104, MINT_L), (360, 470, 96, MINT)):
            g += person(x, by, h, f)
        g += soft_waves(235, 300, 2, 1.0, flip=True) + soft_waves(235, 300, 2, 1.0)
        g += label(235, 700, "מדברים בגובה העיניים", MINT_D, 36) + label(235, 746, "עם אנשים שאולי צריכים אתכם", SUB, 27)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; n = len(labels); rows = ""
        for i, l in enumerate(labels):
            last = i == n - 1
            fill = "#FFFFFF" if last else (MINT if i % 2 == 0 else MINT_L)
            b = (f"<svg width='96' height='80' viewBox='0 0 96 80' style='flex:none'>"
                 f"<path d='M 30,58 l 4,18 l 18,-20 Z' fill='{fill}' stroke='{MINT_D if last else INK}' stroke-width='4' stroke-linejoin='round'"
                 f"{' stroke-dasharray=\"6 5\"' if last else ''}/>"
                 f"<rect x='4' y='4' width='88' height='56' rx='28' fill='{fill}' stroke='{MINT_D if last else INK}' stroke-width='4'"
                 f"{' stroke-dasharray=\"8 6\"' if last else ''}/>"
                 f"<rect x='28' y='54' width='22' height='8' fill='{fill}'/>"
                 + label(48, 44, str(i + 1), INK, 32) + "</svg>")
            rows += (f"<div style='display:flex;align-items:center;gap:26px;padding:6px 0'>{b}"
                     f"<span style='font-size:42px;font-weight:900;color:{SUB if last else INK}'>{l}</span></div>")
        return (f"<div style='width:840px;background:#FFFFFF;border:6px solid {INK};border-radius:20px;overflow:hidden;"
                f"box-shadow:12px 14px 0 rgba(16,27,79,.14)'>"
                f"<div style='background:{NAVY};color:#fff;font-size:32px;font-weight:900;padding:18px 34px;display:flex;align-items:center;gap:18px'>"
                f"<span style='width:18px;height:18px;border-radius:50%;background:{MINT};flex:none'></span>שיחה, לא צעקה</div>"
                f"<div style='padding:16px 40px 20px 40px;display:flex;flex-direction:column'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='600' viewBox='0 0 {w} 600'>"
        g += bubble(470, 120, 230, 104, "#FFFFFF")
        for x, by, h, f in ((250, 470, 110, MINT), (380, 520, 120, MINT_L), (560, 520, 120, MINT), (690, 470, 110, MINT_L)):
            g += person(x, by, h, f)
        g += soft_waves(470, 290, 2, 1.2, flip=True) + soft_waves(470, 290, 2, 1.2)
        return g + "</svg>"
    return ""


def halftone(end=False):
    dots = ""
    for r in range(0, 30):
        for c in range(0, 24):
            x = c * 48 + (24 if r % 2 else 0)
            y = r * 46
            # dots fade from the bottom-left corner
            d = ((x / 1080) + (1 - y / 1350)) / 2
            rad = max(0.0, 7 * (1 - d * 1.35)) * min(1.0, max(0.0, (y - 380) / 300))
            if rad > .6:
                dots += f"<circle cx='{x}' cy='{y}' r='{rad:.1f}' fill='{DOT}'/>"
    return (f"<svg width='1080' height='1350' viewBox='0 0 1080 1350' style='position:absolute;inset:0;opacity:{.45 if end else .7}'>"
            f"{dots}</svg>")


def ad_megaphone(spec):
    slides = spec["slides"]; n = len(slides); out = []
    bg = f"background:{BG}"
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT_D if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        end = s.get("layout") == "end"
        wrap = (f"<style>.bg mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='bg' style='position:absolute;inset:0;overflow:hidden;color:{INK};{bg}'>{halftone(end)}")
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
