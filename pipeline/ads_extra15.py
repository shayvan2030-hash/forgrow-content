"""Extra ad layouts, set 15 (added 2026-11-08). Imported by ads.py.

ad_pond — carousel on pale butter background: fishing line over a pond. Grey fish in the wrong pond ignore the hook;
          mint fish in the right pond swim toward it. Five-step route as numbered bubbles. Illustration only.
          Original logo on a navy tile.
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
BG = "#FFF4CF"
INK = "#101B4F"
MINT_D = "#0E8F6E"
GREY = "#B9B4AC"
WATER = "#BFE3F2"


def fish(x, y, fill, flip=1, s=1.0):
    return (f"<g transform='translate({x} {y}) scale({flip * s} {s})'>"
            f"<path d='M-46 0 C-20 -30 22 -30 40 0 C22 30 -20 30 -46 0 Z' fill='{fill}' stroke='{INK}' stroke-width='5'/>"
            f"<path d='M40 0 L66 -20 L66 20 Z' fill='{fill}' stroke='{INK}' stroke-width='5' stroke-linejoin='round'/>"
            f"<circle cx='-22' cy='-5' r='5' fill='{INK}'/></g>")


def pond(y, w, h, fishes, hook_to=None):
    g = f"<ellipse cx='{w / 2}' cy='{y + h / 2}' rx='{w / 2 - 20}' ry='{h / 2}' fill='{WATER}' stroke='{INK}' stroke-width='6'/>"
    for fx, fy, fill, fl in fishes:
        g += fish(fx, fy, fill, fl)
    return g


def hook(x, top, bottom):
    return (f"<line x1='{x}' y1='{top}' x2='{x}' y2='{bottom}' stroke='{INK}' stroke-width='5'/>"
            f"<path d='M{x} {bottom} v26 a16 16 0 0 1 -32 0' fill='none' stroke='{INK}' stroke-width='6' stroke-linecap='round'/>")


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='520' viewBox='0 0 {w} 520'>"
        g += pond(150, w, 340, [(200, 300, GREY, 1), (330, 400, GREY, -1), (640, 290, GREY, 1), (740, 400, GREY, -1), (520, 360, GREY, 1)])
        g += hook(470, 0, 250)
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='640' viewBox='0 0 {w} 640'>"
        g += pond(10, w, 250, [(130, 130, GREY, 1), (300, 190, GREY, -1), (730, 120, GREY, 1), (700, 205, GREY, -1)])
        g += hook(600, 0, 90)
        g += f"<text x='{w / 2}' y='305' font-family='Heebo' font-weight='900' font-size='34' text-anchor='middle' fill='{INK}'>בריכה שלא מתאימה: הדג ממשיך הלאה</text>"
        g += pond(340, w, 250, [(260, 480, MINT, -1), (390, 440, MINT, -1), (330, 540, MINT, -1)])
        g += hook(560, 330, 420)
        g += f"<text x='{w / 2}' y='630' font-family='Heebo' font-weight='900' font-size='34' text-anchor='middle' fill='{MINT_D}'>בריכה רלוונטית: יש למי להתעניין</text>"
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]
        rows = ""
        for i, l in enumerate(labels):
            rows += (f"<div style='display:flex;align-items:center;gap:26px;width:820px;height:96px;border-radius:999px;padding:0 20px;"
                     f"background:{MINT if i else '#fff'};border:5px solid {INK};font-size:40px;font-weight:900;color:{NAVY3}'>"
                     f"<span style='flex:none;width:58px;height:58px;border-radius:50%;background:{INK};color:#fff;display:flex;align-items:center;justify-content:center;font-size:34px'>{i + 1}</span>{l}</div>")
            if i < len(labels) - 1:
                rows += f"<div style='width:8px;height:14px;background:{INK};opacity:.45'></div>"
        return f"<div style='display:flex;flex-direction:column;align-items:center'>{rows}</div>"
    if k == "one":
        g = f"<svg width='{w}' height='460' viewBox='0 0 {w} 460'>"
        g += pond(110, w, 330, [(220, 290, MINT, -1), (360, 360, MINT, -1), (520, 300, MINT, -1), (680, 370, MINT, -1)])
        g += hook(130, 0, 200)
        return g + "</svg>"
    return ""


def ad_pond(spec):
    slides = spec["slides"]; n = len(slides); out = []
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.pd mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='pd' style='position:absolute;inset:0;overflow:hidden;background:{BG};color:{INK}'>")
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
