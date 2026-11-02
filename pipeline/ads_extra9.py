"""Extra ad layouts, set 9 (added 2026-11-02). Imported by ads.py.

ad_keys — carousel on warm cream background: a key and locks. A good key (your content/offer) does not open every
          lock; locks that match are the relevant audience. Stages (discover -> follow -> keep seeing -> understand
          the offer -> may reach out) shown as a door that opens wider step by step. Illustration only: no numbers,
          results or dashboards. Original logo is used as supplied on a navy tile (light background).
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
BG = "#FFF4DF"
PERI = "#8799DB"
GREY = "#C9C4B8"
INK = "#101B4F"


def keyhole(cx, cy, shape, color, s=1.0):
    if shape == "round":
        return f"<circle cx='{cx}' cy='{cy}' r='{15 * s}' fill='{color}'/><rect x='{cx - 5 * s}' y='{cy}' width='{10 * s}' height='{34 * s}' fill='{color}'/>"
    if shape == "square":
        return f"<rect x='{cx - 15 * s}' y='{cy - 15 * s}' width='{30 * s}' height='{30 * s}' fill='{color}'/><rect x='{cx - 5 * s}' y='{cy}' width='{10 * s}' height='{34 * s}' fill='{color}'/>"
    return f"<path d='M{cx} {cy - 18 * s} l{18 * s} {32 * s} h{-36 * s}z' fill='{color}'/><rect x='{cx - 5 * s}' y='{cy}' width='{10 * s}' height='{34 * s}' fill='{color}'/>"


def door(x, y, shape, match=False, ajar=0, w=130, h=230, label=""):
    fill = MINT if match else GREY
    d = (f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='14' fill='{'#0E8F6E' if ajar else fill}'/>" if ajar == 0 else
         f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='14' fill='#FFE9A8'/>")
    if ajar:
        wd = w * (1 - ajar)
        d += f"<path d='M{x} {y} h{wd:.0f} l{-0 + ajar * 26:.0f} {ajar * 14:.0f} v{h - ajar * 28:.0f} l{-ajar * 26:.0f} {ajar * 14:.0f} h{-wd:.0f}z' fill='{MINT}'/>"
        return d
    d += keyhole(x + w / 2, y + h * .42, shape, INK if not match else NAVY3, .9)
    return d


def key(x, y, rot=0, s=1.0, color=INK):
    return (f"<g transform='translate({x} {y}) rotate({rot}) scale({s})'>"
            f"<circle cx='0' cy='0' r='62' fill='{color}'/><circle cx='0' cy='0' r='26' fill='{BG}'/>"
            f"<rect x='56' y='-14' width='300' height='28' rx='8' fill='{color}'/>"
            f"<rect x='270' y='10' width='34' height='60' rx='6' fill='{color}'/>"
            f"<rect x='322' y='10' width='34' height='44' rx='6' fill='{color}'/>"
            f"<circle cx='0' cy='0' r='62' fill='none' stroke='{MINT}' stroke-width='8'/></g>")


def many(w=940, h=620):
    shapes = ["round", "square", "tri", "tri", "round", "square"]
    xs = [20 + (i % 3) * 300 for i in range(6)]
    ys = [330 if i >= 3 else 60 for i in range(6)]
    ds = "".join(door(xs[i] + 40, ys[i] - 10 if i < 3 else ys[i] - 70, shapes[i], match=(i == 4)) for i in range(6))
    return f"<svg width='{w}' height='{h}' viewBox='0 0 {w} {h}'>{ds}</svg>"


def key_scene(kind, w=940, h=620):
    if kind == "lost":      # one key, six locked doors in a grid, none open
        return (f"<svg width='{w}' height='{h}' viewBox='0 0 {w} {h}'>"
                + "".join(door(20 + (i % 3) * 310 + 25, 20 + (i // 3) * 290, ["round", "square", "tri", "tri", "round", "square"][i], match=False, w=130, h=240) for i in range(6))
                + key(470, 300, -20, .001) + "</svg>")
    if kind == "fit":       # key matches one shape
        return (f"<svg width='{w}' height='{h}' viewBox='0 0 {w} {h}'>"
                + f"<g>{key(110, 120, 18, .8)}</g>"
                + "".join(door(430 + i * 160 - (i == 0) * 0, 40, ["tri", "square", "round"][i], match=(i == 2), w=130, h=240) for i in range(3))
                + f"<text x='110' y='400' font-size='34' font-weight='800' fill='{INK}' font-family='Heebo'></text>"
                + "</svg>")
    return ""


def scene(sc):
    k = sc["kind"]
    if k == "grid":
        shapes = ["round", "square", "tri", "tri", "round", "square"]
        ds = "".join(door(30 + (i % 3) * 300 + 40, 190 + (i // 3) * 270, shapes[i], match=(i == 4), w=150, h=230) for i in range(6))
        return f"<svg width='940' height='700' viewBox='0 0 940 700'>{key(250, 90, 0, .62)}{ds}</svg>"
    if k == "mismatch":
        ds = ""
        spec = [("tri", False), ("square", False), ("round", True)]
        for i, (sh, m) in enumerate(spec):
            ds += door(60 + i * 290, 230, sh, match=m, w=170, h=270)
        marks = (f"<g stroke='#C0392B' stroke-width='9' stroke-linecap='round'>"
                 f"<path d='M115 540 l60 60 M175 540 l-60 60'/><path d='M405 540 l60 60 M465 540 l-60 60'/></g>"
                 f"<g stroke='#0E8F6E' stroke-width='11' stroke-linecap='round' fill='none'><path d='M690 580 l36 38 l70 -76'/></g>")
        return f"<svg width='940' height='650' viewBox='0 0 940 650'>{key(330, 100, 0, .7)}{ds}{marks}</svg>"
    if k == "open":
        d = "".join(door(40 + i * 175, 100 + (4 - i) * 0, "round", ajar=[0, .15, .35, .55, .8][i]) if i else door(40, 100, "round", match=False)
                    for i in range(5))
        return f"<svg width='940' height='360' viewBox='0 0 940 360'>{d}</svg>"
    if k == "row":
        rows = ""
        for i, l in enumerate(sc["labels"]):
            lit = i >= 1
            orb = (f"<svg width='90' height='90' viewBox='0 0 90 90'><rect x='18' y='6' width='54' height='78' rx='8' fill='{MINT if lit else GREY}'/>"
                   f"<path d='M18 6 h{54 - i * 10} l{i * 4} 4 v70 l{-i * 4} 4 h{-(54 - i * 10)}z' fill='{'#FFE9A8' if lit else GREY}' opacity='{0 if i == 0 else .95}'/>"
                   f"<circle cx='{58}' cy='46' r='4' fill='{INK}'/></svg>")
            rows += (f"<div style='position:relative;display:flex;align-items:center;gap:30px;height:112px'>"
                     f"<div style='width:100px;flex:none;display:flex;justify-content:center'>{orb}</div>"
                     f"<div style='font-size:42px;font-weight:900;color:{INK}'>{l}</div></div>")
        line = f"<div style='position:absolute;right:54px;top:50px;bottom:50px;border-right:5px dashed {MINT};opacity:.7'></div>"
        return f"<div style='position:relative;width:900px;display:flex;flex-direction:column'>{line}{rows}</div>"
    if k == "one":
        return (f"<svg width='940' height='420' viewBox='0 0 940 420'>" + key(170, 210, 0, .95)
                + door(600, 60, "round", match=True, w=190, h=320) + "</svg>")
    return ""


def ad_keys(spec):
    slides = spec["slides"]; n = len(slides); out = []
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.ky mark{{color:#0E8F6E;background:none}}</style>"
                f"<div class='ky' style='position:absolute;inset:0;overflow:hidden;background:{BG};color:{INK}'>")
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
            <div style='position:absolute;top:{s.get('scene_top', 400)}px;bottom:{s.get('scene_bottom', 130)}px;left:0;right:0;display:flex;justify-content:center;align-items:center'>{scene(s['scene'])}</div>{stamp}
            <div style='position:absolute;bottom:40px;right:80px;left:80px;display:flex;justify-content:space-between;align-items:center'>{tile}
              <span style='font-size:24px;color:#3C4A8F;font-weight:700'>{spec.get('note', 'המחשה')}</span></div></div>"""
        out.append(body)
    return out
