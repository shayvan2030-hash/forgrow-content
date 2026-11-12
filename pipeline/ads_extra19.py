"""Extra ad layouts, set 19 (added 2026-11-12).

ad_stamps — carousel on a cool paper-blue dotted background: a loyalty stamp card (כרטיסיית ניקובים).
            A customer is not made in one visit: someone who saw the content once and never came back leaves a card
            with one stamp; a relevant audience keeps coming back, so the card fills stamp by stamp.
            Route shown as the five stamp boxes of one card. Illustration only. Original logo on a navy tile.
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
BG = "#E6ECF6"
INK = "#101B4F"
MINT_D = "#0E8F6E"
GREY = "#B8BED0"
CARD = "#FFFDF8"


def stamp(cx, cy, r, on, grey=False):
    """A stamp slot: empty dashed circle, or an inked mint stamp with a star."""
    if not on:
        return (f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='none' stroke='{GREY if grey else INK}' stroke-width='5' "
                f"stroke-dasharray='10 9' opacity='{.9 if grey else .45}'/>")
    col = GREY if grey else MINT
    pts = []
    import math
    for k in range(10):
        a = -math.pi / 2 + k * math.pi / 5
        rr = r * (.55 if k % 2 == 0 else .24)
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    return (f"<g transform='rotate(-9 {cx} {cy})'><circle cx='{cx}' cy='{cy}' r='{r}' fill='{col}' stroke='{INK}' stroke-width='5'/>"
            f"<circle cx='{cx}' cy='{cy}' r='{r - 10}' fill='none' stroke='{INK}' stroke-width='3' opacity='.35'/>"
            f"<polygon points='{' '.join(pts)}' fill='{INK}'/></g>")


def card(x, y, w, h, filled, grey=False, title="הכרטיסייה של העסק", tilt=0, r=44):
    g = (f"<g transform='rotate({tilt} {x + w / 2} {y + h / 2})'>"
         f"<rect x='{x + 10}' y='{y + 12}' width='{w}' height='{h}' rx='26' fill='{INK}' opacity='.12'/>"
         f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='26' fill='{CARD}' stroke='{GREY if grey else INK}' stroke-width='6'/>"
         f"<rect x='{x}' y='{y}' width='{w}' height='62' rx='26' fill='{GREY if grey else NAVY}'/>"
         f"<rect x='{x}' y='{y + 36}' width='{w}' height='26' fill='{GREY if grey else NAVY}'/>"
         f"<text x='{x + w - 30}' y='{y + 43}' font-family='Heebo' font-weight='900' font-size='28' text-anchor='start' "
         f"fill='{INK if grey else '#fff'}' direction='rtl'>{title}</text>")
    gap = (w - 60) / 5
    for k in range(5):
        cx = x + w - 30 - gap / 2 - k * gap   # RTL: first slot on the right
        g += stamp(cx, y + 62 + (h - 62) / 2, r, k < filled, grey)
    return g + "</g>"


def label(w, y, txt, fill):
    return (f"<text x='{w / 2}' y='{y}' font-family='Heebo' font-weight='900' font-size='34' text-anchor='middle' "
            f"fill='{fill}' direction='rtl'>{txt}</text>")


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='560' viewBox='0 0 {w} 560'>"
        g += card(70, 120, 800, 300, 1, tilt=-4, r=56)
        g += (f"<circle cx='190' cy='104' r='46' fill='{INK}'/>"
              f"<text x='190' y='124' font-family='Heebo' font-weight='900' font-size='60' text-anchor='middle' fill='{MINT}'>?</text>")
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='780' viewBox='0 0 {w} 780'>"
        g += card(120, 20, 700, 230, 1, grey=True, title="ראו פעם אחת", r=42)
        g += label(w, 310, "קהל לא רלוונטי: ביקור אחד ולא חוזרים", INK)
        g += card(120, 400, 700, 230, 4, title="חוזרים לראות", r=42)
        g += label(w, 690, "קהל רלוונטי: חוזרים, ועוד חותמת נוספת", MINT_D)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; rows = ""
        for i, l in enumerate(labels):
            on = i < 4
            dot = (f"<svg width='92' height='92' viewBox='0 0 92 92'>{stamp(46, 46, 40, True)}</svg>" if on else
                   f"<svg width='92' height='92' viewBox='0 0 92 92'>{stamp(46, 46, 40, False)}</svg>")
            rows += (f"<div style='display:flex;align-items:center;gap:28px;padding:10px 0;"
                     f"{'border-top:3px dashed rgba(16,27,79,.2);' if i else ''}'>{dot}"
                     f"<span style='font-size:30px;font-weight:900;color:{MINT_D};width:40px'>{i + 1}</span>"
                     f"<span style='font-size:42px;font-weight:900;color:{INK}'>{l}</span></div>")
        return (f"<div style='width:820px;background:{CARD};border:6px solid {INK};border-radius:28px;overflow:hidden;"
                f"box-shadow:12px 14px 0 rgba(16,27,79,.12)'>"
                f"<div style='background:{NAVY};color:#fff;font-size:30px;font-weight:900;padding:16px 34px'>חותמת אחרי חותמת</div>"
                f"<div style='padding:10px 40px 14px'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='440' viewBox='0 0 {w} 440'>"
        g += card(120, 60, 700, 260, 5, r=48)
        return g + "</svg>"
    return ""


def ad_stamps(spec):
    slides = spec["slides"]; n = len(slides); out = []
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.st mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='st' style='position:absolute;inset:0;overflow:hidden;background:{BG};color:{INK};"
                f"background-image:radial-gradient(rgba(16,27,79,.13) 2.5px, transparent 2.6px);background-size:36px 36px'>")
        tl = f"<div style='background:{NAVY};border-radius:22px;padding:14px 22px;display:inline-flex'>{logo(52)}</div>"
        if s.get("layout") == "end":
            body = wrap + f"""<div style='position:absolute;inset:0;padding:110px 90px;display:flex;flex-direction:column;justify-content:center;gap:40px'>
              <div style='background:{NAVY};border-radius:30px;padding:24px 34px;align-self:flex-start;display:flex'>{logo(110)}</div>
              <h2 style='font-size:{s.get('size', 60)}px;line-height:1.2'>{s['head']}</h2>
              <p style='font-size:36px;color:#3C4A8F;font-weight:700'>{s.get('body', '')}</p>
              <div><div style='display:inline-block;background:{MINT};color:{NAVY3};font-weight:800;font-size:40px;padding:24px 44px;border-radius:999px'>{s['cta']}</div></div>
              <div><span style='display:inline-block;font-size:26px;font-weight:700;padding:8px 20px;border-radius:999px;border:2px solid #3C4A8F;color:#3C4A8F;background:{BG}'>{s.get('tag', '')}</span></div></div></div>"""
        else:
            st = (f"<div style='position:absolute;right:100px;bottom:{s.get('stamp_bottom', 640)}px;transform:rotate(7deg);border:6px solid {MINT_D};"
                  f"color:{MINT_D};border-radius:18px;padding:8px 26px;font-size:40px;font-weight:900;background:{BG}'>{s['stamp']}</div>"
                  if s.get("stamp") else "")
            body = wrap + f"""<div style='position:absolute;top:56px;left:80px;right:80px;display:flex;gap:10px'>{dots}</div>
            <div style='position:absolute;top:112px;right:80px;left:80px;display:flex;flex-direction:column;gap:14px'>
              {f"<div style='font-size:32px;font-weight:900;color:{MINT_D}'>{s['kicker']}</div>" if s.get('kicker') else ''}
              <h2 style='font-size:{s.get('size', 62)}px;line-height:1.12'>{s['head']}</h2>
              {f"<p style='font-size:33px;color:#3C4A8F;line-height:1.4;font-weight:700'>{s['body']}</p>" if s.get('body') else ''}</div>
            <div style='position:absolute;top:{s.get('scene_top', 420)}px;bottom:{s.get('scene_bottom', 130)}px;left:0;right:0;display:flex;justify-content:center;align-items:center'>{scene(s['scene'])}</div>{st}
            <div style='position:absolute;bottom:40px;right:80px;left:80px;display:flex;justify-content:space-between;align-items:center'>{tl}
              <span style='font-size:24px;color:#3C4A8F;font-weight:700;background:{BG};padding:2px 8px'>{spec.get('note', 'המחשה')}</span></div></div>"""
        out.append(body)
    return out
