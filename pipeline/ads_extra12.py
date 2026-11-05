"""Extra ad layouts, set 12 (added 2026-11-05). Imported by ads.py.

ad_magnet — carousel on pale sky background: a magnet and scattered objects. Objects that do not fit (wood, paper, stones)
            stay put; relevant ones (metal, mint) are drawn in; the pulled pieces form a chain of five links
            (discover -> follow -> keep seeing -> understand the offer -> may reach out). Illustration only.
            Original logo as supplied on a navy tile (light background).
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
BG = "#E6F0FF"
INK = "#101B4F"
MINT_D = "#0E8F6E"
GREY = "#B8BED3"
GREY_D = "#8991AE"
WOOD = "#D9B88A"


def magnet(x, y, s=1.0, rot=0):
    """U magnet, opening downward. (x, y) = top centre."""
    w, t, h = 150 * s, 44 * s, 130 * s
    return (f"<g transform='rotate({rot} {x} {y + h / 2})'>"
            f"<path d='M{x - w / 2} {y + h} V{y + w / 2} a{w / 2} {w / 2} 0 0 1 {w} 0 V{y + h} h{-t} V{y + w / 2} a{w / 2 - t} {w / 2 - t} 0 0 0 {-(w - 2 * t)} 0 V{y + h}z' fill='#E5484D'/>"
            f"<rect x='{x - w / 2}' y='{y + h - 34 * s}' width='{t}' height='{34 * s}' fill='#F4F5FA'/>"
            f"<rect x='{x + w / 2 - t}' y='{y + h - 34 * s}' width='{t}' height='{34 * s}' fill='#F4F5FA'/></g>")


def clip(x, y, c=MINT, rot=0, s=1.0):
    return (f"<g transform='rotate({rot} {x} {y}) scale(1)'><rect x='{x - 22 * s}' y='{y - 12 * s}' width='{44 * s}' height='{24 * s}' rx='{12 * s}' "
            f"fill='{c}' stroke='{INK}' stroke-width='4'/></g>")


def wood(x, y, rot=0):
    return (f"<g transform='rotate({rot} {x} {y})'><rect x='{x - 26}' y='{y - 16}' width='52' height='32' rx='6' fill='{WOOD}' stroke='{GREY_D}' stroke-width='3'/>"
            f"<path d='M{x - 14} {y - 4} h28 M{x - 8} {y + 6} h20' stroke='{GREY_D}' stroke-width='3' stroke-linecap='round'/></g>")


def stone(x, y, rot=0):
    return (f"<g transform='rotate({rot} {x} {y})'><ellipse cx='{x}' cy='{y}' rx='28' ry='20' fill='{GREY}' stroke='{GREY_D}' stroke-width='3'/></g>")


def scene(sc, w=940):
    k = sc["kind"]
    lab = f"font-family='Heebo' font-weight='900' font-size='34' text-anchor='middle' fill='{INK}'"
    if k == "intro":
        g = f"<svg width='{w}' height='620' viewBox='0 0 {w} 620'>"
        g += magnet(470, 30, 1.5)
        g += f"<path d='M430 270 v40 M470 270 v60 M510 270 v40' stroke='{INK}' stroke-opacity='.3' stroke-width='5' stroke-dasharray='4 12' stroke-linecap='round'/>"
        g += f"<text x='470' y='380' font-family='Heebo' font-weight='900' font-size='90' text-anchor='middle' fill='{INK}'>?</text>"
        for x, y, r in [(110, 560, 8), (310, 575, -12), (640, 570, 14), (840, 560, -6)]:
            g += wood(x, y, r)
        for x, y, r in [(210, 520, 0), (540, 585, 10), (740, 520, -10)]:
            g += stone(x, y, r)
        for x, y, r in [(430, 520, 20), (880, 590, -20)]:
            g += clip(x, y, GREY, r)
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='640' viewBox='0 0 {w} 640'>"
        g += f"<path d='M470 40 v560' stroke='{INK}' stroke-opacity='.18' stroke-width='3' stroke-dasharray='10 12'/>"
        g += magnet(235, 60, 1.0)
        for x, y, r in [(80, 480, 8), (240, 520, -10), (385, 485, 12)]:
            g += wood(x, y, r)
        for x, y, r in [(160, 400, 0), (330, 420, 10)]:
            g += stone(x, y, r)
        g += clip(235, 340, GREY, 14)
        g += magnet(705, 60, 1.0)
        g += f"<path d='M650 270 v30 M705 270 v50 M760 270 v30' stroke='{MINT_D}' stroke-width='5' stroke-dasharray='4 12' stroke-linecap='round'/>"
        for x, y, r in [(650, 360, 20), (760, 350, -16), (705, 420, 4)]:
            g += clip(x, y, MINT, r)
        for x, y, r in [(610, 520, 6), (800, 515, -8)]:
            g += clip(x, y, MINT, r)
        g += f"<text x='235' y='596' {lab}>לא מתאים — לא נמשך</text><text x='705' y='596' {lab}>מתאים — מתקרב</text></svg>"
        return g
    if k == "route":
        labels = sc["labels"]
        rows = ""
        for i, l in enumerate(labels):
            link = (f"<div style='display:flex;align-items:center;gap:24px;width:760px;height:92px;border-radius:46px;padding:0 20px;"
                    f"background:{MINT if i else '#fff'};border:5px solid {INK};font-size:40px;font-weight:900;color:{NAVY3}'>"
                    f"<span style='display:inline-flex;width:56px;height:56px;border-radius:50%;background:{BG};border:4px solid {INK};"
                    f"align-items:center;justify-content:center;font-size:32px'>{i + 1}</span>{l}</div>")
            rows += link
            if i < len(labels) - 1:
                rows += f"<div style='width:8px;height:30px;background:{INK}'></div>"
        mg = f"<svg width='200' height='170' viewBox='0 0 200 170'>{magnet(100, 10, .9)}</svg>"
        return f"<div style='display:flex;flex-direction:column;align-items:center'>{mg}{rows}</div>"
    if k == "one":
        g = f"<svg width='{w}' height='460' viewBox='0 0 {w} 460'>"
        g += magnet(470, 20, 1.3)
        for x, y, r in [(410, 245, 10), (530, 250, -12), (470, 305, 0), (350, 320, -18), (590, 325, 16)]:
            g += clip(x, y, MINT, r)
        return g + "</svg>"
    return ""


def ad_magnet(spec):
    slides = spec["slides"]; n = len(slides); out = []
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.mg mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='mg' style='position:absolute;inset:0;overflow:hidden;background:{BG};color:{INK}'>")
        tile = f"<div style='background:{NAVY};border-radius:22px;padding:14px 22px;display:inline-flex'>{logo(52)}</div>"
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
            <div style='position:absolute;bottom:40px;right:80px;left:80px;display:flex;justify-content:space-between;align-items:center'>{tile}
              <span style='font-size:24px;color:#3C4A8F;font-weight:700'>{spec.get('note', 'המחשה')}</span></div></div>"""
        out.append(body)
    return out
