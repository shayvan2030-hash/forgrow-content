"""Extra ad layouts, set 27 (added 2026-11-21).

ad_boardgame — carousel on a pale lime background with faint diagonal stripes: a board game with dice and pawns.
          Business problem: a great customer once came from Instagram — by chance. Since then inquiries arrive like a
          dice roll: sometimes, mostly not, and the owner cannot tell when the next one comes. A relevant audience
          that keeps seeing the business moves along a track, square by square
          (discover -> follow -> keep seeing -> understand the offer -> maybe reach out).
          Route shown as five numbered board squares. Illustration only. Original logo on a navy tile.
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
MINT_L = "#B5F1DF"
INK = "#101B4F"
MINT_D = "#0B7F62"
GREY = "#D9DBE4"
GREY_D = "#6E7390"
SUB = "#33407F"
BOARD = "#FFF8EA"
SQ = ("#F6D98B", "#C5CBEE", "#F4B7A6", "#FFFFFF")
RED = "#E2574C"


def label(x, y, txt, fill, size=34):
    return (f"<text x='{x}' y='{y}' font-family='Heebo' font-weight='900' font-size='{size}' text-anchor='middle' "
            f"fill='{fill}' direction='rtl'>{txt}</text>")


PIPS = {1: [(0, 0)], 2: [(-1, -1), (1, 1)], 3: [(-1, -1), (0, 0), (1, 1)], 4: [(-1, -1), (1, -1), (-1, 1), (1, 1)],
        5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)], 6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)]}


def die(cx, cy, s, face, fill="#FFFFFF", pip=INK, rot=0, shadow=True):
    g = f"<g transform='translate({cx:.1f} {cy:.1f}) rotate({rot})'>"
    if shadow:
        g += f"<rect x='{-s / 2 + 8:.1f}' y='{-s / 2 + 10:.1f}' width='{s:.1f}' height='{s:.1f}' rx='{s * .2:.1f}' fill='{INK}' opacity='.14'/>"
    g += f"<rect x='{-s / 2:.1f}' y='{-s / 2:.1f}' width='{s:.1f}' height='{s:.1f}' rx='{s * .2:.1f}' fill='{fill}' stroke='{INK}' stroke-width='5'/>"
    for dx, dy in PIPS[face]:
        g += f"<circle cx='{dx * s * .26:.1f}' cy='{dy * s * .26:.1f}' r='{s * .085:.1f}' fill='{pip}'/>"
    return g + "</g>"


def pawn(cx, by, h, fill, stroke=INK, op=1, dash=False):
    d = " stroke-dasharray='8 6'" if dash else ""
    bw, hr = h * .62, h * .2
    hy = by - h + hr
    return (f"<g opacity='{op}'><ellipse cx='{cx:.1f}' cy='{by + 2:.1f}' rx='{bw * .62:.1f}' ry='{h * .07:.1f}' fill='{INK}' opacity='.14'/>"
            f"<path d='M {cx - bw / 2:.1f},{by:.1f} Q {cx - bw / 2:.1f},{by - h * .14:.1f} {cx - bw * .3:.1f},{by - h * .16:.1f} "
            f"L {cx - bw * .14:.1f},{hy + hr * .9:.1f} H {cx + bw * .14:.1f} L {cx + bw * .3:.1f},{by - h * .16:.1f} "
            f"Q {cx + bw / 2:.1f},{by - h * .14:.1f} {cx + bw / 2:.1f},{by:.1f} Z' fill='{fill}' stroke='{stroke}' stroke-width='4' stroke-linejoin='round'{d}/>"
            f"<circle cx='{cx:.1f}' cy='{hy:.1f}' r='{hr:.1f}' fill='{fill}' stroke='{stroke}' stroke-width='4'{d}/></g>")


def square(x, y, s, fill, num=None, dash=False, stroke=INK, fs=None):
    d = " stroke-dasharray='10 7'" if dash else ""
    g = f"<rect x='{x:.1f}' y='{y:.1f}' width='{s:.1f}' height='{s:.1f}' rx='{s * .14:.1f}' fill='{fill}' stroke='{stroke}' stroke-width='4'{d}/>"
    if num:
        g += label(x + s / 2, y + s / 2 + (fs or s * .42) * .36, num, INK, fs or s * .42)
    return g


def motion(x1, y1, x2, y2, cx, cy, color=GREY_D):
    return (f"<path d='M {x1},{y1} Q {cx},{cy} {x2},{y2}' fill='none' stroke='{color}' stroke-width='5' "
            f"stroke-linecap='round' stroke-dasharray='4 14'/>")


def bubble(cx, cy, r=40, color=GREY_D):
    return f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='#FFFFFF' stroke='{color}' stroke-width='4'/>" + label(cx, cy + r * .38, "?", color, r * 1.15)


def track(pts, s, finish=True):
    """Squares at the given top-left points, alternating board colours; the last one is the mint goal square."""
    g = ""
    for i, (x, y) in enumerate(pts):
        last = finish and i == len(pts) - 1
        g += square(x, y, s, MINT if last else SQ[i % 3])
        if last:
            g += f"<path d='M {x + s * .3:.1f},{y + s * .52:.1f} L {x + s * .45:.1f},{y + s * .68:.1f} L {x + s * .72:.1f},{y + s * .34:.1f}' fill='none' stroke='{INK}' stroke-width='7' stroke-linecap='round' stroke-linejoin='round'/>"
    return g


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='660' viewBox='0 0 {w} 660'>"
        # board seen from above, track of squares around the edge
        g += f"<rect x='110' y='330' width='720' height='300' rx='26' fill='{BOARD}' stroke='{INK}' stroke-width='6'/>"
        s = 70
        for i in range(9):
            g += square(125 + i * 78, 345, s, SQ[i % 4]) + square(125 + i * 78, 545, s, SQ[(i + 2) % 4])
        g += square(125, 445, s, SQ[1]) + square(749, 445, s, SQ[0])
        g += f"<text x='470' y='508' font-family='Heebo' font-weight='900' font-size='46' text-anchor='middle' fill='{INK}' opacity='.18' direction='rtl'>אולי הפעם?</text>"
        g += pawn(318, 418, 92, MINT)
        # dice tumbling through the air
        g += motion(150, 300, 400, 190, 230, 120) + motion(820, 290, 590, 175, 760, 110)
        g += die(410, 175, 130, 5, rot=-18) + die(560, 210, 120, 2, rot=14)
        g += bubble(790, 120, 44)
        return g + "</svg>"
    if k == "rolls":
        g = f"<svg width='{w}' height='560' viewBox='0 0 {w} 560'>"
        items = (("עוד פוסט", 2, False), ("עוד פוסט", 1, False), ("עוד פוסט", 3, False), ("פנייה במקרה", 6, True))
        for j, (txt, face, hit) in enumerate(items):
            cx = 820 - j * 225  # RTL: first item on the right
            g += die(cx, 190, 150, face, fill=MINT if hit else "#FFFFFF", rot=(-8, 6, -4, 10)[j])
            if hit:
                g += pawn(cx, 450, 120, MINT)
            else:
                g += pawn(cx, 450, 120, GREY, dash=True, op=.85)
            g += label(cx, 525, txt, MINT_D if hit else GREY_D, 32)
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='800' viewBox='0 0 {w} 800'>"
        g += f"<line x1='470' y1='20' x2='470' y2='640' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        # right (read first): waiting for luck — dice and grey pawns scattered, no track
        g += die(640, 200, 120, 1, rot=-14) + die(790, 260, 110, 3, rot=16)
        g += motion(560, 120, 700, 90, 620, 40) + bubble(860, 110, 34)
        for x, y, op in ((590, 560, .95), (720, 600, .75), (850, 540, .55)):
            g += pawn(x, y, 120, GREY, op=op)
        g += label(705, 690, "מחכים למזל", INK, 36) + label(705, 738, "לא ברור מתי תגיע הפנייה הבאה", SUB, 27)
        # left: a track of squares, mint pawns moving along it towards the goal
        s = 78
        pts = [(30, 520), (110, 470), (190, 420), (270, 370), (350, 320), (350, 230), (270, 150)]
        g += f"<rect x='10' y='130' width='440' height='490' rx='24' fill='{BOARD}' stroke='{INK}' stroke-width='5'/>"
        g += track(pts, s)
        g += pawn(69, 552, 74, MINT) + pawn(229, 452, 74, MINT_L) + pawn(389, 352, 74, MINT)
        g += label(235, 690, "קהל רלוונטי", MINT_D, 36) + label(235, 738, "מתקדם משבצת אחרי משבצת", SUB, 27)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; n = len(labels); rows = ""
        for i, l in enumerate(labels):
            last = i == n - 1
            fill = "#FFFFFF" if last else (MINT if i % 2 == 0 else MINT_L)
            t = (f"<svg width='96' height='96' viewBox='0 0 96 96' style='flex:none'>"
                 f"{square(8, 8, 80, fill, num=str(i + 1), dash=last, stroke=MINT_D if last else INK, fs=40)}</svg>")
            rows += (f"<div style='display:flex;align-items:center;gap:26px'>{t}"
                     f"<span style='font-size:42px;font-weight:900;color:{SUB if last else INK}'>{l}</span></div>")
        return (f"<div style='width:840px;background:#FFFFFF;border:6px solid {INK};border-radius:20px;overflow:hidden;"
                f"box-shadow:12px 14px 0 rgba(16,27,79,.14)'>"
                f"<div style='background:{NAVY};color:#fff;font-size:32px;font-weight:900;padding:18px 34px;display:flex;align-items:center;gap:18px'>"
                f"<span style='width:18px;height:18px;border-radius:5px;background:{MINT};flex:none'></span>משבצת אחרי משבצת</div>"
                f"<div style='padding:20px 40px 24px 40px;display:flex;flex-direction:column;gap:6px'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='560' viewBox='0 0 {w} 560'>"
        g += f"<rect x='90' y='170' width='760' height='300' rx='26' fill='{BOARD}' stroke='{INK}' stroke-width='6'/>"
        s = 86
        pts = [(730 - i * 112, 330 - (i % 2) * 90) for i in range(6)]
        g += "<polyline points='" + " ".join(f"{x + s / 2:.0f},{y + s / 2:.0f}" for x, y in pts) + f"' fill='none' stroke='{GREY_D}' stroke-width='6' stroke-dasharray='4 12' stroke-linecap='round' stroke-linejoin='round'/>"
        g += track(pts, s)
        for i, (x, y) in enumerate(pts[:5]):
            if i in (0, 2, 3):
                g += pawn(x + s / 2, y + s * .78, 84, MINT if i != 2 else MINT_L)
        g += die(170, 110, 96, 4, rot=-10, fill="#FFFFFF")
        return g + "</svg>"
    return ""


def stripes(end=False):
    return (f"<div style='position:absolute;inset:0;opacity:{.35 if end else .5};"
            f"background:repeating-linear-gradient(135deg,rgba(135,153,219,.18) 0 18px,transparent 18px 54px)'></div>")


def ad_boardgame(spec):
    slides = spec["slides"]; n = len(slides); out = []
    bg = "background:#EEF3D6"
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT_D if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        end = s.get("layout") == "end"
        wrap = (f"<style>.bg mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='bg' style='position:absolute;inset:0;overflow:hidden;color:{INK};{bg}'>{stripes(end)}")
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
