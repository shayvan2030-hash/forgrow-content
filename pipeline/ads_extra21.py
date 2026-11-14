"""Extra ad layouts, set 21 (added 2026-11-14).

ad_puzzle — carousel on a warm honey wooden-table background (faint planks): jigsaw puzzle pieces.
            Business problem: people ask "how much?" and disappear — someone who saw one post holds one piece
            of the picture. A relevant audience that keeps seeing the content assembles the picture over time
            (discover -> follow -> keep seeing -> understand the offer -> maybe reach out).
            Grey single piece next to an almost empty frame vs a mint picture nearly complete.
            Route shown as five numbered puzzle pieces. Illustration only. Original logo on a navy tile.
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
MINT_L = "#B5F1DF"
BG = "#EED9B4"
INK = "#101B4F"
MINT_D = "#0B7F62"
GREY = "#CBCDD8"
GREY_D = "#6E7390"
SUB = "#33407F"


def _edge(x0, y0, x1, y1, sign):
    """Path segment from (x0,y0) to (x1,y1); sign 1 = tab outward, -1 = blank inward, 0 = straight."""
    if sign == 0:
        return f" L {x1:.1f},{y1:.1f}"
    dx, dy = x1 - x0, y1 - y0
    nx, ny = dy, -dx  # outward normal for clockwise traversal (scaled by length)
    h = 0.30 * sign

    def p(t, k):
        return f"{x0 + dx * t + nx * k:.1f},{y0 + dy * t + ny * k:.1f}"
    return (f" L {p(0.36, 0)} C {p(0.30, h * 0.55)} {p(0.22, h)} {p(0.5, h)}"
            f" C {p(0.78, h)} {p(0.70, h * 0.55)} {p(0.64, 0)} L {x1:.1f},{y1:.1f}")


def piece(x, y, s, edges, fill, stroke=INK, sw=5, dash=False, extra=""):
    t, r, b, l = edges
    d = (f"M {x},{y}" + _edge(x, y, x + s, y, t) + _edge(x + s, y, x + s, y + s, r)
         + _edge(x + s, y + s, x, y + s, b) + _edge(x, y + s, x, y, l) + " Z")
    da = "stroke-dasharray='10 8'" if dash else ""
    return f"<path d='{d}' fill='{fill}' stroke='{stroke}' stroke-width='{sw}' stroke-linejoin='round' {da} {extra}/>"


# fixed tab pattern for a 3x3 puzzle: H[r][c] = sign of the bottom edge of (r,c); V[r][c] = sign of the right edge
H = [[1, -1, 1], [-1, 1, -1]]
V = [[1, -1], [-1, 1], [1, -1]]


def edges_of(r, c):
    top = -H[r - 1][c] if r > 0 else 0
    bottom = H[r][c] if r < 2 else 0
    right = V[r][c] if c < 2 else 0
    left = -V[r][c - 1] if c > 0 else 0
    return (top, right, bottom, left)


def puzzle(x, y, s, placed, colors=None, ghost=True, sw=5):
    """placed: set of (r,c) drawn solid; others drawn as dashed outlines when ghost."""
    colors = colors or {}
    g = ""
    for r in range(3):
        for c in range(3):
            px, py = x + c * s, y + r * s
            if (r, c) in placed:
                g += piece(px, py, s, edges_of(r, c), colors.get((r, c), MINT), sw=sw)
            elif ghost:
                g += piece(px, py, s, edges_of(r, c), "rgba(255,255,255,.35)", stroke=GREY_D, sw=3, dash=True)
    return g


def loose(cx, cy, s, rot, fill, edges=(1, -1, 1, -1), mark=None, mark_fill=INK, sw=5):
    g = f"<g transform='rotate({rot} {cx} {cy})'>" + piece(cx - s / 2, cy - s / 2, s, edges, fill, sw=sw)
    if mark:
        g += (f"<text x='{cx}' y='{cy + s * 0.2}' font-family='Heebo' font-weight='900' font-size='{s * 0.55:.0f}' "
              f"text-anchor='middle' fill='{mark_fill}'>{mark}</text>")
    return g + "</g>"


def label(x, y, txt, fill, size=34):
    return (f"<text x='{x}' y='{y}' font-family='Heebo' font-weight='900' font-size='{size}' text-anchor='middle' "
            f"fill='{fill}' direction='rtl'>{txt}</text>")


ALL = {(r, c) for r in range(3) for c in range(3)}
CHECK = {(r, c): (MINT if (r + c) % 2 == 0 else MINT_L) for r in range(3) for c in range(3)}


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='640' viewBox='0 0 {w} 640'>"
        g += puzzle(250, 100, 150, set(), ghost=True)
        g += loose(720, 470, 150, 14, GREY, mark="?")
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='760' viewBox='0 0 {w} 760'>"
        # right (read first in RTL): one post seen = one piece, frame almost empty
        g += puzzle(575, 120, 100, {(1, 1)}, colors={(1, 1): GREY})
        g += loose(640, 520, 90, -18, GREY, edges=(-1, 1, 1, -1)) + loose(800, 500, 90, 22, GREY, edges=(1, 1, -1, -1))
        # left: relevant audience that keeps seeing content = picture almost complete
        g += puzzle(65, 120, 100, ALL - {(0, 2)}, colors=CHECK)
        g += loose(330, 60, 100, 12, MINT, edges=edges_of(0, 2))
        g += f"<line x1='470' y1='30' x2='470' y2='600' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        g += label(705, 650, "ראו פוסט אחד", INK, 38) + label(705, 700, "רואים מחיר, לא רואים תמונה", SUB, 30)
        g += label(235, 650, "ממשיכים לראות", MINT_D, 38) + label(235, 700, "התמונה מתרכבת לאורך זמן", SUB, 30)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; rows = ""
        for i, l in enumerate(labels):
            last = i == len(labels) - 1
            pc = (f"<svg width='110' height='100' viewBox='-20 -15 120 110' style='flex:none'>"
                  + piece(0, 0, 80, (0, 1, 0, -1), "rgba(255,255,255,.6)" if last else (MINT if i % 2 == 0 else MINT_L),
                          stroke=MINT_D if last else INK, sw=5, dash=last)
                  + f"<text x='46' y='56' font-family='Heebo' font-weight='900' font-size='42' text-anchor='middle' fill='{INK}'>{i + 1}</text></svg>")
            rows += (f"<div style='display:flex;align-items:center;gap:24px;padding:4px 0'>{pc}"
                     f"<span style='font-size:42px;font-weight:900;color:{INK if not last else SUB}'>{l}</span></div>")
        return (f"<div style='width:840px;background:#FFFBF2;border:6px solid {INK};border-radius:28px;overflow:hidden;"
                f"box-shadow:12px 14px 0 rgba(16,27,79,.14)'>"
                f"<div style='background:{NAVY};color:#fff;font-size:32px;font-weight:900;padding:16px 34px'>התמונה שמתרכבת</div>"
                f"<div style='padding:14px 30px 18px 30px'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='620' viewBox='0 0 {w} 620'>"
        g += puzzle(260, 80, 140, ALL, colors=CHECK)
        g += (f"<text x='470' y='365' font-family='Heebo' font-weight='900' font-size='92' text-anchor='middle' fill='{INK}'>✓</text>")
        return g + "</svg>"
    return ""


def ad_puzzle(spec):
    slides = spec["slides"]; n = len(slides); out = []
    wood = (f"background:{BG};background-image:"
            f"repeating-linear-gradient(0deg, rgba(120,80,30,.10) 0 2px, transparent 2px 225px),"
            f"repeating-linear-gradient(0deg, rgba(120,80,30,.035) 0 1px, transparent 1px 19px)")
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT_D if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.pz mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='pz' style='position:absolute;inset:0;overflow:hidden;color:{INK};{wood}'>")
        tl = f"<div style='background:{NAVY};border-radius:22px;padding:14px 22px;display:inline-flex'>{logo(52)}</div>"
        if s.get("layout") == "end":
            body = wrap + f"""<div style='position:absolute;inset:0;padding:110px 90px;display:flex;flex-direction:column;justify-content:center;gap:40px'>
              <div style='background:{NAVY};border-radius:30px;padding:24px 34px;align-self:flex-start;display:flex'>{logo(110)}</div>
              <h2 style='font-size:{s.get('size', 60)}px;line-height:1.2'>{s['head']}</h2>
              <p style='font-size:36px;color:{SUB};font-weight:700'>{s.get('body', '')}</p>
              <div><div style='display:inline-block;background:{MINT};color:{NAVY3};font-weight:800;font-size:40px;padding:24px 44px;border-radius:999px;box-shadow:0 6px 0 {INK}'>{s['cta']}</div></div>
              <div><span style='display:inline-block;font-size:26px;font-weight:700;padding:8px 20px;border-radius:999px;border:2px solid {SUB};color:{SUB};background:#FFFBF2'>{s.get('tag', '')}</span></div></div></div>"""
        else:
            st = (f"<div style='position:absolute;right:96px;bottom:{s.get('stamp_bottom', 640)}px;transform:rotate(-5deg);background:{NAVY};"
                  f"color:#fff;border-radius:10px;padding:6px;box-shadow:6px 8px 0 rgba(16,27,79,.15)'>"
                  f"<div style='border:3px dashed {MINT};border-radius:6px;padding:8px 26px;font-size:38px;font-weight:900'>{s['stamp']}</div></div>"
                  if s.get("stamp") else "")
            body = wrap + f"""<div style='position:absolute;top:56px;left:80px;right:80px;display:flex;gap:10px'>{dots}</div>
            <div style='position:absolute;top:112px;right:80px;left:80px;display:flex;flex-direction:column;gap:14px'>
              {f"<div style='font-size:32px;font-weight:900;color:{MINT_D}'>{s['kicker']}</div>" if s.get('kicker') else ''}
              <h2 style='font-size:{s.get('size', 62)}px;line-height:1.12'>{s['head']}</h2>
              {f"<p style='font-size:33px;color:{SUB};line-height:1.4;font-weight:700'>{s['body']}</p>" if s.get('body') else ''}</div>
            <div style='position:absolute;top:{s.get('scene_top', 420)}px;bottom:{s.get('scene_bottom', 130)}px;left:0;right:0;display:flex;justify-content:center;align-items:center'>{scene(s['scene'])}</div>{st}
            <div style='position:absolute;bottom:40px;right:80px;left:80px;display:flex;justify-content:space-between;align-items:center'>{tl}
              <span style='font-size:24px;color:{SUB};font-weight:700;background:#FFFBF2;border-radius:6px;padding:2px 10px'>{spec.get('note', 'המחשה')}</span></div></div>"""
        out.append(body)
    return out
