"""Extra ad layouts, set 14 (added 2026-11-07). Imported by ads.py.

ad_dominoes — carousel on warm sand background: a row of dominoes = the chain discover -> follow -> keep seeing ->
              understand the offer -> may reach out. A gap breaks the chain; a connected row (mint) continues.
              Illustration only. Original logo on a navy tile.
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
BG = "#F6EBDD"
INK = "#101B4F"
MINT_D = "#0E8F6E"
GREY = "#B9B4AC"


def tile(x, y, fill, rot=0, w=84, h=170, pips=0):
    g = (f"<g transform='rotate({rot} {x + w / 2} {y + h})'>"
         f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='14' fill='{fill}' stroke='{INK}' stroke-width='5'/>"
         f"<line x1='{x + 10}' y1='{y + h / 2}' x2='{x + w - 10}' y2='{y + h / 2}' stroke='{INK}' stroke-width='4' opacity='.6'/>")
    for k in range(pips):
        g += f"<circle cx='{x + w / 2}' cy='{y + 28 + k * 30}' r='7' fill='{INK}'/>"
    return g + "</g>"


def row(y, fills, rots, x0=50, step=108):
    return "".join(tile(x0 + i * step, y, f, r, pips=(i % 3) + 1) for i, (f, r) in enumerate(zip(fills, rots)) if f)


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='460' viewBox='0 0 {w} 460'>"
        # right-to-left: first tile (right) fallen, then gap, remaining stand alone
        g += row(130, [GREY] * 5 + [None, "#fff", "#fff"], [0, 0, 0, 0, 0, 0, 0, 0])
        g += f"<text x='{50 + 5 * 108 + 42}' y='150' font-family='Heebo' font-weight='900' font-size='110' text-anchor='middle' fill='{MINT_D}'>?</text>"
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='620' viewBox='0 0 {w} 620'>"
        g += row(20, [GREY, GREY, GREY, GREY, GREY, None, "#fff", "#fff"], [0, 0, 0, 0, 0, 0, 0, 0])
        g += f"<text x='{w / 2}' y='235' font-family='Heebo' font-weight='900' font-size='34' text-anchor='middle' fill='{INK}'>השרשרת נעצרת אחרי הראשון</text>"
        g += row(300, ["#fff", MINT, MINT, MINT, MINT, MINT, MINT, MINT], [0, 0, 0, 0, 0, 0, 0, 0])
        g += f"<text x='{w / 2}' y='515' font-family='Heebo' font-weight='900' font-size='34' text-anchor='middle' fill='{MINT_D}'>כשהקהל רלוונטי, יש סיכוי שהשרשרת תימשך</text>"
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]
        rows = ""
        for i, l in enumerate(labels):
            pips = "".join("<i style='width:14px;height:14px;border-radius:50%;background:" + INK + "'></i>" for _ in range(i + 1))
            rows += (f"<div style='display:flex;align-items:center;gap:24px;width:{820 - i * 0}px;height:96px;border-radius:18px;padding:0 24px;"
                     f"background:{MINT if i else '#fff'};border:5px solid {INK};font-size:40px;font-weight:900;color:{NAVY3};"
                     f"margin-right:{i * 0}px'>"
                     f"<span style='display:inline-flex;gap:6px;flex:none'>{pips}</span>{l}</div>")
            if i < len(labels) - 1:
                rows += f"<div style='width:8px;height:16px;background:{INK};opacity:.5'></div>"
        return f"<div style='display:flex;flex-direction:column;align-items:center'>{rows}</div>"
    if k == "one":
        g = f"<svg width='{w}' height='460' viewBox='0 0 {w} 460'>"
        g += row(120, ["#fff"] + [MINT] * 7, [0] * 8)
        return g + "</svg>"
    return ""


def ad_dominoes(spec):
    slides = spec["slides"]; n = len(slides); out = []
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.dm mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='dm' style='position:absolute;inset:0;overflow:hidden;background:{BG};color:{INK}'>")
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
