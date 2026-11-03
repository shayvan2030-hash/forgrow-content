"""Extra ad layouts, set 10 (added 2026-11-03). Imported by ads.py.

ad_bricks — carousel on pale lavender background: every post is a brick. Bricks on shaky ground do not add up to a wall;
            on a relevant-audience foundation they pile up in courses (discover -> follow -> keep seeing -> understand
            the offer -> may reach out). Illustration only: no numbers, results or dashboards.
            Original logo used as supplied on a navy tile (light background).
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
BG = "#ECEFFB"
INK = "#101B4F"
BRICK = "#E58F6C"
BRICK_D = "#C96F4C"
SAND = "#D9CFC0"


def brick(x, y, w=120, h=48, rot=0, fill=BRICK):
    cx, cy = x + w / 2, y + h / 2
    return (f"<g transform='rotate({rot} {cx} {cy})'><rect x='{x}' y='{y}' width='{w}' height='{h}' rx='6' fill='{fill}'/>"
            f"<rect x='{x}' y='{y + h - 8}' width='{w}' height='8' rx='4' fill='{BRICK_D if fill == BRICK else '#0E8F6E'}' opacity='.55'/></g>")


def shaky_tower(ox, base_y, n=5):
    """Bricks stacked unevenly on cracked sand; two have fallen."""
    g = f"<path d='M{ox - 150} {base_y} h300 v26 h-300z' fill='{SAND}'/>"
    g += f"<path d='M{ox - 40} {base_y} l14 26 M{ox + 60} {base_y} l-12 26' stroke='#9C917F' stroke-width='4' fill='none'/>"
    offs = [0, 18, -22, 26, -30, 34]
    rots = [0, 3, -5, 6, -8, 11]
    for i in range(n):
        g += brick(ox - 60 + offs[i], base_y - 48 * (i + 1), 120, 48, rots[i])
    g += brick(ox + 90, base_y - 36, 100, 40, 14) + brick(ox - 230, base_y - 34, 100, 40, -12)
    return g


def solid_wall(ox, base_y, rows=5):
    g = f"<rect x='{ox - 160}' y='{base_y}' width='320' height='34' rx='6' fill='{MINT}'/>"
    for r in range(rows):
        shift = 0 if r % 2 == 0 else 30
        for c in range(2):
            g += brick(ox - 120 + c * 120 + shift - (30 if shift else 0) + (0), base_y - 48 * (r + 1), 120, 48)
    return g


def scene(sc, w=940):
    k = sc["kind"]
    if k == "wobble":
        return (f"<svg width='{w}' height='620' viewBox='0 0 {w} 620'>" + shaky_tower(470, 520, 6)
                + "</svg>")
    if k == "split":
        lab = (f"font-family='Heebo' font-weight='900' font-size='34' text-anchor='middle' fill='{INK}'")
        return (f"<svg width='{w}' height='640' viewBox='0 0 {w} 640'>"
                + shaky_tower(235, 500, 5) + solid_wall(705, 500, 5)
                + f"<text x='235' y='596' {lab}>קהל לא מתאים</text><text x='705' y='596' {lab}>קהל רלוונטי</text>"
                + f"<path d='M470 60 v500' stroke='{INK}' stroke-opacity='.18' stroke-width='3' stroke-dasharray='10 12'/></svg>")
    if k == "rise":
        labels = sc["labels"]
        wall = f"<svg width='360' height='560' viewBox='0 0 360 560'><rect x='10' y='520' width='340' height='34' rx='6' fill='{MINT}'/>"
        for r in range(5):
            cnt = 5 - r
            total = cnt * 64
            x0 = 180 - total / 2
            for c in range(cnt):
                wall += brick(x0 + c * 64 + 2, 520 - 96 * (r + 1) + 48 + 0, 60, 44) if False else ""
        # five courses, each course one wide band that narrows upward
        for r in range(5):
            wband = 340 - r * 56
            x0 = 180 - wband / 2
            wall += (f"<rect x='{x0}' y='{520 - 96 * (r + 1)}' width='{wband}' height='88' rx='8' fill='{BRICK}'/>"
                     f"<g stroke='{BRICK_D}' stroke-width='3' opacity='.6'><path d='M{x0} {520 - 96 * (r + 1) + 44} h{wband}'/>"
                     f"<path d='M{x0 + wband * .33:.0f} {520 - 96 * (r + 1)} v44 M{x0 + wband * .66:.0f} {520 - 96 * (r + 1) + 44} v44'/></g>")
        wall += "</svg>"
        rows = "".join(f"<div style='height:96px;display:flex;align-items:center;font-size:40px;font-weight:900;color:{INK}'>"
                       f"<span style='color:#0E8F6E;margin-left:18px'>{len(labels) - i}</span>{l}</div>"
                       for i, l in enumerate(reversed(labels)))
        rows = "".join(f"<div style='height:96px;display:flex;align-items:center;gap:18px;font-size:40px;font-weight:900;color:{INK}'>"
                       f"<span style='display:inline-flex;width:54px;height:54px;border-radius:50%;background:{MINT};color:{NAVY3};"
                       f"align-items:center;justify-content:center;font-size:32px'>{len(labels) - i}</span>{l}</div>"
                       for i, l in enumerate(reversed(labels)))
        return (f"<div style='display:flex;align-items:flex-end;gap:40px;width:940px;justify-content:space-between'>"
                f"<div style='display:flex;flex-direction:column;padding-bottom:36px'>{rows}</div>{wall}</div>")
    if k == "one":
        return (f"<svg width='{w}' height='460' viewBox='0 0 {w} 460'>" + solid_wall(470, 370, 4)
                + f"<path d='M300 178 L470 70 L640 178z' fill='{INK}'/></svg>")
    return ""


def ad_bricks(spec):
    slides = spec["slides"]; n = len(slides); out = []
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.bk mark{{color:#0E8F6E;background:none}}</style>"
                f"<div class='bk' style='position:absolute;inset:0;overflow:hidden;background:{BG};color:{INK}'>")
        tile = f"<div style='background:{NAVY};border-radius:22px;padding:14px 22px;display:inline-flex'>{logo(52)}</div>"
        if s.get("layout") == "end":
            body = wrap + f"""<div style='position:absolute;inset:0;padding:110px 90px;display:flex;flex-direction:column;justify-content:center;gap:40px'>
              <div style='background:{NAVY};border-radius:30px;padding:24px 34px;align-self:flex-start;display:flex'>{logo(110)}</div>
              <h2 style='font-size:{s.get('size', 60)}px;line-height:1.2'>{s['head']}</h2>
              <p style='font-size:36px;color:#3C4A8F;font-weight:700'>{s.get('body', '')}</p>
              <div><div style='display:inline-block;background:{MINT};color:{NAVY3};font-weight:800;font-size:40px;padding:24px 44px;border-radius:999px'>{s['cta']}</div></div>
              <div><span style='display:inline-block;font-size:26px;font-weight:700;padding:8px 20px;border-radius:999px;border:2px solid #3C4A8F;color:#3C4A8F'>{s.get('tag', '')}</span></div></div></div>"""
        else:
            stamp = (f"<div style='position:absolute;right:100px;bottom:{s.get('stamp_bottom', 640)}px;transform:rotate(7deg);border:6px solid #0E8F6E;"
                     f"color:#0E8F6E;border-radius:18px;padding:8px 26px;font-size:40px;font-weight:900;background:{BG}'>{s['stamp']}</div>"
                     if s.get("stamp") else "")
            body = wrap + f"""<div style='position:absolute;top:56px;left:80px;right:80px;display:flex;gap:10px'>{dots}</div>
            <div style='position:absolute;top:112px;right:80px;left:80px;display:flex;flex-direction:column;gap:14px'>
              {f"<div style='font-size:32px;font-weight:900;color:#0E8F6E'>{s['kicker']}</div>" if s.get('kicker') else ''}
              <h2 style='font-size:{s.get('size', 62)}px;line-height:1.12'>{s['head']}</h2>
              {f"<p style='font-size:33px;color:#3C4A8F;line-height:1.4;font-weight:700'>{s['body']}</p>" if s.get('body') else ''}</div>
            <div style='position:absolute;top:{s.get('scene_top', 420)}px;bottom:{s.get('scene_bottom', 130)}px;left:0;right:0;display:flex;justify-content:center;align-items:center'>{scene(s['scene'])}</div>{stamp}
            <div style='position:absolute;bottom:40px;right:80px;left:80px;display:flex;justify-content:space-between;align-items:center'>{tile}
              <span style='font-size:24px;color:#3C4A8F;font-weight:700'>{spec.get('note', 'המחשה')}</span></div></div>"""
        out.append(body)
    return out
