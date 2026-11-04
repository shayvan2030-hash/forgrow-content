"""Extra ad layouts, set 11 (added 2026-11-04). Imported by ads.py.

ad_mail — carousel on warm peach background: every post is a letter. A great letter sent to the wrong address is not
          read; sent to a relevant address it starts a route (discover -> follow -> keep seeing -> understand the offer
          -> may reach out). Illustration only: no numbers, results or dashboards.
          Original logo used as supplied on a navy tile (light background).
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
BG = "#FFF0E3"
INK = "#101B4F"
GREY = "#B9B4BF"
GREY_D = "#8F8A97"
PAPER = "#FFFFFF"
MINT_D = "#0E8F6E"


def mailbox(x, base, color=GREY, dark=GREY_D, flag=False, s=1.0):
    """Post + arched box. (x, base) = bottom centre of the post."""
    w, h = 130 * s, 90 * s
    top = base - 130 * s - h
    g = f"<rect x='{x - 8 * s}' y='{base - 130 * s}' width='{16 * s}' height='{130 * s}' fill='{dark}'/>"
    g += (f"<path d='M{x - w / 2} {top + h} v{-h * .45} a{w / 2} {h * .55} 0 0 1 {w} 0 v{h * .45}z' fill='{color}'/>"
          f"<rect x='{x - w / 2 + 16 * s}' y='{top + h * .42}' width='{w - 32 * s}' height='{10 * s}' rx='{5 * s}' fill='{dark}' opacity='.55'/>")
    if flag:
        g += (f"<rect x='{x + w / 2 - 4 * s}' y='{top - 18 * s}' width='{8 * s}' height='{70 * s}' fill='{INK}'/>"
              f"<rect x='{x + w / 2 + 4 * s}' y='{top - 18 * s}' width='{40 * s}' height='{26 * s}' rx='4' fill='{INK}'/>")
    return g


def envelope(x, y, w=120, h=84, rot=0, fill=PAPER, line=INK, seal=None):
    cx, cy = x + w / 2, y + h / 2
    g = (f"<g transform='rotate({rot} {cx} {cy})'><rect x='{x}' y='{y}' width='{w}' height='{h}' rx='8' fill='{fill}' stroke='{line}' stroke-width='4'/>"
         f"<path d='M{x + 4} {y + 6} L{cx} {y + h * .56} L{x + w - 4} {y + 6}' fill='none' stroke='{line}' stroke-width='4' stroke-linejoin='round'/>")
    if seal:
        g += f"<circle cx='{cx}' cy='{y + h * .56}' r='11' fill='{seal}'/>"
    return g + "</g>"


def scene(sc, w=940):
    k = sc["kind"]
    lab = f"font-family='Heebo' font-weight='900' font-size='34' text-anchor='middle' fill='{INK}'"
    if k == "intro":
        g = f"<svg width='{w}' height='620' viewBox='0 0 {w} 620'>"
        for i, x in enumerate([150, 360, 580, 790]):
            g += mailbox(x, 590, s=1.0)
        g += envelope(400, 40, 140, 98, -8, seal=MINT)
        g += f"<path d='M470 160 v70' stroke='{INK}' stroke-width='5' stroke-dasharray='4 14' stroke-linecap='round'/>"
        g += f"<text x='470' y='290' font-family='Heebo' font-weight='900' font-size='120' text-anchor='middle' fill='{INK}'>?</text>"
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='640' viewBox='0 0 {w} 640'>"
        g += f"<path d='M470 40 v520' stroke='{INK}' stroke-opacity='.18' stroke-width='3' stroke-dasharray='10 12'/>"
        for x in (90, 235, 380):
            g += mailbox(x, 500, s=.8)
        g += envelope(40, 470, 96, 68, -14, fill="#F3EFF6", line=GREY_D) + envelope(250, 490, 96, 68, 18, fill="#F3EFF6", line=GREY_D)
        g += envelope(160, 300, 96, 68, 20, fill="#F3EFF6", line=GREY_D)
        g += mailbox(705, 500, color=MINT, dark=MINT_D, flag=True, s=1.15)
        g += envelope(630, 150, 120, 84, -10, seal=MINT) + f"<path d='M700 250 v36' stroke='{INK}' stroke-width='5' stroke-dasharray='4 12' stroke-linecap='round'/>"
        g += f"<text x='235' y='596' {lab}>כתובת לא מתאימה</text><text x='705' y='596' {lab}>כתובת רלוונטית</text></svg>"
        return g
    if k == "route":
        labels = sc["labels"]
        rows = ""
        for i, l in enumerate(labels):
            on = i  # more mint as route advances
            rows += (f"<div style='position:relative;z-index:1;height:104px;display:flex;align-items:center;gap:26px;font-size:42px;font-weight:900;color:{INK}'>"
                     f"<span style='display:inline-flex;width:64px;height:64px;border-radius:50%;background:{MINT if i else '#fff'};border:4px solid {INK};"
                     f"color:{NAVY3};align-items:center;justify-content:center;font-size:34px'>{i + 1}</span>{l}</div>")
        line = f"<div style='position:absolute;right:29px;top:52px;bottom:52px;width:6px;z-index:0;background:repeating-linear-gradient({'180deg'},{INK} 0 10px,transparent 10px 22px);opacity:.3'></div>"
        return (f"<div style='position:relative;width:860px;display:flex;flex-direction:column'>{line}{rows}</div>")
    if k == "one":
        g = f"<svg width='{w}' height='460' viewBox='0 0 {w} 460'>"
        g += mailbox(470, 450, color=MINT, dark=MINT_D, flag=True, s=1.5)
        g += envelope(410, 30, 120, 84, -8, seal=MINT) + envelope(230, 60, 100, 70, -14, seal=MINT)
        return g + "</svg>"
    return ""


def ad_mail(spec):
    slides = spec["slides"]; n = len(slides); out = []
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.ml mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='ml' style='position:absolute;inset:0;overflow:hidden;background:{BG};color:{INK}'>")
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
