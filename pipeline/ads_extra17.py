"""Extra ad layouts, set 17 (added 2026-11-10).

ad_table — carousel on soft sage background: a dining table seen from above, set with plates. Empty grey chairs
           (invited the wrong crowd) vs mint guests seated and eating. Route shown as five numbered plates.
           Illustration only. Original logo on a navy tile.
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
BG = "#E4EEDD"
INK = "#101B4F"
MINT_D = "#0E8F6E"
GREY = "#B9B4AC"
WOOD = "#D9B98C"


def chair(x, y, fill, empty=True):
    return (f"<rect x='{x - 34}' y='{y - 30}' width='68' height='60' rx='16' fill='{GREY if empty else '#fff'}' "
            f"stroke='{INK}' stroke-width='5' stroke-dasharray='{'10 8' if empty else '0'}'/>")


def guest(x, y, fill):
    return (f"<ellipse cx='{x}' cy='{y + 8}' rx='34' ry='22' fill='{fill}' stroke='{INK}' stroke-width='5'/>"
            f"<circle cx='{x}' cy='{y - 4}' r='18' fill='{fill}' stroke='{INK}' stroke-width='5'/>")


def plate(x, y, fill="#fff"):
    return (f"<circle cx='{x}' cy='{y}' r='22' fill='{fill}' stroke='{INK}' stroke-width='5'/>"
            f"<circle cx='{x}' cy='{y}' r='11' fill='none' stroke='{INK}' stroke-width='3' opacity='.35'/>")


def table(x0, y0, w, h, seats, guests, plate_fill="#fff"):
    """seats = number per long side; guests = set of (side, idx) occupied by mint guests."""
    g = f"<rect x='{x0}' y='{y0}' width='{w}' height='{h}' rx='30' fill='{WOOD}' stroke='{INK}' stroke-width='6'/>"
    gap = w / seats
    for side in (0, 1):
        for i in range(seats):
            cx = x0 + gap * (i + .5)
            cy = y0 - 40 if side == 0 else y0 + h + 40
            py = y0 + 36 if side == 0 else y0 + h - 36
            occ = (side, i) in guests
            if occ:
                g += guest(cx, cy, MINT) + plate(cx, py, "#fff")
            else:
                g += chair(cx, cy, GREY) + plate(cx, py, "#F4EFE6")
    return g


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        return f"<svg width='{w}' height='520' viewBox='0 0 {w} 520'>" + table(60, 190, 820, 140, 5, set()) + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='730' viewBox='0 0 {w} 730'>"
        g += table(110, 75, 720, 130, 4, set())
        g += f"<text x='{w / 2}' y='330' font-family='Heebo' font-weight='900' font-size='34' text-anchor='middle' fill='{INK}'>הוזמנו הלא נכונים: הכיסאות נשארים ריקים</text>"
        g += table(110, 425, 720, 130, 4, {(0, 0), (0, 2), (1, 1), (1, 3), (0, 3)})
        g += f"<text x='{w / 2}' y='700' font-family='Heebo' font-weight='900' font-size='34' text-anchor='middle' fill='{MINT_D}'>קהל רלוונטי: יש מי שמתיישב ונשאר</text>"
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; rows = ""
        for i, l in enumerate(labels):
            rows += (f"<div style='display:flex;align-items:center;gap:30px;height:96px'>"
                     f"<span style='flex:none;width:76px;height:76px;border-radius:50%;background:{MINT if i else '#fff'};border:7px solid {INK};"
                     f"display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:900;color:{INK}'>{i + 1}</span>"
                     f"<span style='font-size:44px;font-weight:900;color:{INK}'>{l}</span></div>")
        return f"<div style='width:820px'>{rows}</div>"
    if k == "one":
        return (f"<svg width='{w}' height='460' viewBox='0 0 {w} 460'>"
                + table(60, 150, 820, 140, 5, {(0, 0), (0, 1), (0, 3), (1, 1), (1, 2), (1, 4)}) + "</svg>")
    return ""


def ad_table(spec):
    slides = spec["slides"]; n = len(slides); out = []
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.tb mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='tb' style='position:absolute;inset:0;overflow:hidden;background:{BG};color:{INK}'>")
        tl = f"<div style='background:{NAVY};border-radius:22px;padding:14px 22px;display:inline-flex'>{logo(52)}</div>"
        if s.get("layout") == "end":
            body = wrap + f"""<div style='position:absolute;inset:0;padding:110px 90px;display:flex;flex-direction:column;justify-content:center;gap:40px'>
              <div style='background:{NAVY};border-radius:30px;padding:24px 34px;align-self:flex-start;display:flex'>{logo(110)}</div>
              <h2 style='font-size:{s.get('size', 60)}px;line-height:1.2'>{s['head']}</h2>
              <p style='font-size:36px;color:#3C4A8F;font-weight:700'>{s.get('body', '')}</p>
              <div><div style='display:inline-block;background:{MINT};color:{NAVY3};font-weight:800;font-size:40px;padding:24px 44px;border-radius:999px'>{s['cta']}</div></div>
              <div><span style='display:inline-block;font-size:26px;font-weight:700;padding:8px 20px;border-radius:999px;border:2px solid #3C4A8F;color:#3C4A8F'>{s.get('tag', '')}</span></div></div></div>"""
        else:
            stamp = (f"<div style='position:absolute;right:100px;bottom:{s.get('stamp_bottom', 640)}px;transform:rotate(7deg);border:6px solid {MINT_D};"
                     f"color:{MINT_D};border-radius:18px;padding:8px 26px;font-size:40px;font-weight:900;background:{BG}'>{s['stamp']}</div>"
                     if s.get("stamp") else "")
            body = wrap + f"""<div style='position:absolute;top:56px;left:80px;right:80px;display:flex;gap:10px'>{dots}</div>
            <div style='position:absolute;top:112px;right:80px;left:80px;display:flex;flex-direction:column;gap:14px'>
              {f"<div style='font-size:32px;font-weight:900;color:{MINT_D}'>{s['kicker']}</div>" if s.get('kicker') else ''}
              <h2 style='font-size:{s.get('size', 62)}px;line-height:1.12'>{s['head']}</h2>
              {f"<p style='font-size:33px;color:#3C4A8F;line-height:1.4;font-weight:700'>{s['body']}</p>" if s.get('body') else ''}</div>
            <div style='position:absolute;top:{s.get('scene_top', 420)}px;bottom:{s.get('scene_bottom', 130)}px;left:0;right:0;display:flex;justify-content:center;align-items:center'>{scene(s['scene'])}</div>{stamp}
            <div style='position:absolute;bottom:40px;right:80px;left:80px;display:flex;justify-content:space-between;align-items:center'>{tl}
              <span style='font-size:24px;color:#3C4A8F;font-weight:700'>{spec.get('note', 'המחשה')}</span></div></div>"""
        out.append(body)
    return out
