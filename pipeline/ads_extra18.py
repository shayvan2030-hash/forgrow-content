"""Extra ad layouts, set 18 (added 2026-11-11).

ad_shelf — carousel on warm stone background: a bookcase. The business's content is a good book (mint spine).
           On the wrong shelf people walk past (grey figures); on the right shelf relevant readers stop and reach
           for it (mint figures). Route shown as a pile of five labelled books. Illustration only.
           Original logo on a navy tile.
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
BG = "#ECE7E1"
INK = "#101B4F"
MINT_D = "#0E8F6E"
GREY = "#BDB7AF"
WOOD = "#C99A66"
SPINES = ["#8799DB", "#C5CBEE", "#E9DCC7", "#9FA7C9", "#D7CFC4", "#B4BCE0"]


def book(x, base, w, h, fill, tilt=0):
    cx = x + w / 2
    return (f"<g transform='rotate({tilt} {cx} {base})'>"
            f"<rect x='{x}' y='{base - h}' width='{w}' height='{h}' rx='6' fill='{fill}' stroke='{INK}' stroke-width='5'/>"
            f"<line x1='{x + 8}' y1='{base - h + 22}' x2='{x + w - 8}' y2='{base - h + 22}' stroke='{INK}' stroke-width='3' opacity='.45'/>"
            f"<line x1='{x + 8}' y1='{base - 22}' x2='{x + w - 8}' y2='{base - 22}' stroke='{INK}' stroke-width='3' opacity='.45'/></g>")


def shelf_row(x0, base, w, hero_at=None, seed=0):
    """A wooden plank with books standing on it; hero_at = index of the mint book."""
    g = f"<rect x='{x0 - 14}' y='{base}' width='{w + 28}' height='22' rx='6' fill='{WOOD}' stroke='{INK}' stroke-width='5'/>"
    x = x0 + 6; i = 0
    widths = [46, 38, 54, 42, 60, 36, 50, 44, 40, 56]
    heights = [128, 110, 140, 118, 132, 104, 146, 122, 112, 136]
    while True:
        k = (i + seed) % len(widths)
        bw, bh = widths[k], heights[k]
        if i == hero_at:
            bw, bh = 66, 158
        if x + bw > x0 + w - 4:
            break
        fill = MINT if i == hero_at else SPINES[(i + seed) % len(SPINES)]
        g += book(x, base, bw, bh, fill)
        x += bw + 4; i += 1
    return g


def hero_x(x0, hero_at, seed=0):
    widths = [46, 38, 54, 42, 60, 36, 50, 44, 40, 56]
    x = x0 + 6
    for i in range(hero_at):
        x += widths[(i + seed) % len(widths)] + 4
    return x + 33


def person(x, foot, fill, dashed=False, reach=None):
    """Simple figure: head + rounded body. reach = (x, y) the arm points to."""
    dash = "stroke-dasharray='9 7'" if dashed else ""
    g = ""
    if reach:
        g += (f"<line x1='{x}' y1='{foot - 92}' x2='{reach[0]}' y2='{reach[1]}' stroke='{INK}' stroke-width='12' stroke-linecap='round'/>"
              f"<line x1='{x}' y1='{foot - 92}' x2='{reach[0]}' y2='{reach[1]}' stroke='{fill}' stroke-width='5' stroke-linecap='round'/>")
    g += (f"<rect x='{x - 30}' y='{foot - 112}' width='60' height='112' rx='28' fill='{fill}' stroke='{INK}' stroke-width='5' {dash}/>"
          f"<circle cx='{x}' cy='{foot - 140}' r='24' fill='{fill}' stroke='{INK}' stroke-width='5' {dash}/>")
    return g


def walk_away(x, y):
    return (f"<path d='M{x} {y} h-70' stroke='{INK}' stroke-width='6' stroke-linecap='round' opacity='.5' stroke-dasharray='4 14'/>"
            f"<path d='M{x - 70} {y} l16 -12 M{x - 70} {y} l16 12' stroke='{INK}' stroke-width='6' stroke-linecap='round' opacity='.5'/>")


def label(w, y, txt, fill):
    return (f"<text x='{w / 2}' y='{y}' font-family='Heebo' font-weight='900' font-size='34' text-anchor='middle' "
            f"fill='{fill}' direction='rtl'>{txt}</text>")


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='560' viewBox='0 0 {w} 560'>"
        g += f"<rect x='40' y='20' width='860' height='520' rx='24' fill='#F7F3EE' stroke='{INK}' stroke-width='6'/>"
        g += shelf_row(80, 214, 780, seed=0)
        g += shelf_row(80, 500, 780, hero_at=7, seed=3)
        hx = hero_x(80, 7, seed=3)
        g += (f"<circle cx='{hx}' cy='292' r='34' fill='{INK}'/>"
              f"<text x='{hx}' y='307' font-family='Heebo' font-weight='900' font-size='44' text-anchor='middle' fill='{MINT}'>?</text>"
              f"<path d='M{hx} 326 v14' stroke='{INK}' stroke-width='6' stroke-linecap='round'/>")
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='760' viewBox='0 0 {w} 760'>"
        # wrong shelf: people walk past
        g += shelf_row(300, 230, 600, hero_at=0, seed=1)
        g += person(110, 250, GREY, dashed=True) + person(210, 250, GREY, dashed=True)
        g += walk_away(90, 268)
        g += label(w, 320, "המדף הלא נכון: עוברים בלי לעצור", INK)
        # right shelf: relevant readers stop and reach
        g += shelf_row(300, 600, 600, hero_at=0, seed=4)
        hx = hero_x(300, 0, seed=4)
        g += person(110, 620, MINT) + person(220, 620, MINT, reach=(hx - 14, 506))
        g += label(w, 700, "קהל רלוונטי: עוצרים ומעיינים", MINT_D)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; rows = ""
        fills = ["#fff", MINT, "#C5CBEE", MINT, "#fff"]
        offs = [40, 0, 60, 20, 0]
        widths = [700, 760, 680, 740, 800]
        for i, l in enumerate(labels):
            rows += (f"<div style='margin-right:{offs[i]}px;width:{widths[i]}px;height:92px;margin-top:-5px;background:{fills[i % 5]};"
                     f"border:6px solid {INK};border-radius:14px;display:flex;align-items:center;gap:26px;padding:0 26px;position:relative'>"
                     f"<span style='flex:none;width:62px;height:62px;border-radius:50%;background:{INK};color:{MINT};"
                     f"display:flex;align-items:center;justify-content:center;font-size:34px;font-weight:900'>{i + 1}</span>"
                     f"<span style='font-size:42px;font-weight:900;color:{INK}'>{l}</span>"
                     f"<i style='position:absolute;left:22px;top:12px;bottom:12px;width:10px;border-left:4px solid rgba(16,27,79,.35);border-right:4px solid rgba(16,27,79,.35)'></i></div>")
        return (f"<div style='width:820px;display:flex;flex-direction:column;align-items:flex-start'>{rows}"
                f"<div style='margin-top:4px;width:840px;height:22px;background:{WOOD};border:5px solid {INK};border-radius:6px'></div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='440' viewBox='0 0 {w} 440'>"
        g += shelf_row(300, 330, 600, hero_at=0, seed=2)
        hx = hero_x(300, 0, seed=2)
        g += person(110, 360, MINT) + person(220, 360, MINT, reach=(hx - 14, 236))
        g += f"<rect x='20' y='360' width='900' height='8' rx='4' fill='{INK}' opacity='.15'/>"
        return g + "</svg>"
    return ""


def ad_shelf(spec):
    slides = spec["slides"]; n = len(slides); out = []
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.sh mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='sh' style='position:absolute;inset:0;overflow:hidden;background:{BG};color:{INK}'>")
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
