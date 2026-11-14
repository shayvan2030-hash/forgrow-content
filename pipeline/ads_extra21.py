"""Extra ad layouts, set 21 (added 2026-11-14).

ad_gift — carousel on a white background with scattered paper confetti: a wrapped gift box (הגרלה / מתנה).
          Business problem: after a giveaway many new followers came for the prize, not for the business; once the
          prize is handed out they move on. Grey dashed figures walk away from an opened, empty box (came for the
          prize) vs mint figures staying around an open box from which content cards rise (came for what the
          business does). Route shown as a ribbon with five numbered gift tags.
          Illustration only. Original logo on a navy tile.
"""
import random
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
BG = "#FFFFFF"
INK = "#101B4F"
MINT_D = "#0E8F6E"
GREY = "#B9BCC9"
GREY_D = "#6E7390"
SUB = "#3C4A8F"
CONF = ["#14D8A5", "#8799DB", "#C5CBEE", "#FFC9A8", "#FFE08A"]


def confetti(seed=7, n=90):
    r = random.Random(seed); s = ""
    for _ in range(n):
        x, y = r.randint(10, 1070), r.randint(10, 1340)
        if 100 < y < 1250 and 90 < x < 990:
            continue  # keep the middle calm, confetti mostly at the edges
        c = r.choice(CONF); rot = r.randint(0, 180)
        if r.random() < .5:
            s += f"<rect x='{x}' y='{y}' width='22' height='10' rx='3' fill='{c}' transform='rotate({rot} {x} {y})'/>"
        else:
            s += f"<circle cx='{x}' cy='{y}' r='7' fill='{c}'/>"
    return (f"<svg width='1080' height='1350' viewBox='0 0 1080 1350' style='position:absolute;inset:0'>{s}</svg>")


def person(x, y, s=1.0, mode="mint", away=False):
    """mode mint = relevant (solid), grey = came for the prize (dashed, walking away)."""
    if mode == "mint":
        fill, st, dash, op = MINT, INK, "", 1
    else:
        fill, st, dash, op = "none", GREY_D, "stroke-dasharray='9 7'", .9
    g = (f"<g transform='translate({x} {y}) scale({s})' opacity='{op}'>"
         f"<circle cx='0' cy='-70' r='24' fill='{fill}' stroke='{st}' stroke-width='5' {dash}/>"
         f"<path d='M -36,0 L -36,-24 Q -36,-40 -18,-40 L 18,-40 Q 36,-40 36,-24 L 36,0 Z' fill='{fill}' stroke='{st}' stroke-width='5' {dash}/>")
    if away:
        g += (f"<path d='M 46,-30 L 86,-30' stroke='{GREY_D}' stroke-width='5' stroke-linecap='round'/>"
              f"<path d='M 74,-42 L 88,-30 L 74,-18' fill='none' stroke='{GREY_D}' stroke-width='5' stroke-linecap='round' stroke-linejoin='round'/>")
    return g + "</g>"


def box(cx, top, s=1.0, mode="closed", tag=None, body=None, rib=None):
    """mode: closed (wrapped with bow), empty (lid off, nothing inside), content (lid off, post cards rising)."""
    body = body or NAVY; rib = rib or MINT
    g = f"<g transform='translate({cx} {top}) scale({s})'>"
    if mode == "content":
        for k, (dx, dy, rot) in enumerate([(-80, -40, -12), (80, -60, 10), (0, -120, 0)]):
            g += (f"<g transform='translate({dx} {dy + 130}) rotate({rot})'>"
                  f"<rect x='-58' y='-70' width='116' height='140' rx='14' fill='#fff' stroke='{INK}' stroke-width='5'/>"
                  f"<rect x='-42' y='-54' width='84' height='62' rx='8' fill='{MINT if k == 2 else '#C5CBEE'}'/>"
                  f"<rect x='-42' y='20' width='70' height='9' rx='4' fill='{INK}' opacity='.6'/>"
                  f"<rect x='-42' y='38' width='48' height='9' rx='4' fill='{INK}' opacity='.35'/></g>")
    # base box
    g += (f"<rect x='-170' y='170' width='340' height='250' rx='14' fill='{body}' stroke='{INK}' stroke-width='7'/>"
          f"<rect x='-26' y='170' width='52' height='250' fill='{rib}' stroke='{INK}' stroke-width='5'/>")
    if mode == "closed":
        g += (f"<rect x='-192' y='110' width='384' height='72' rx='12' fill='{body}' stroke='{INK}' stroke-width='7'/>"
              f"<rect x='-26' y='110' width='52' height='72' fill='{rib}' stroke='{INK}' stroke-width='5'/>"
              f"<path d='M 0,110 C -40,40 -130,40 -110,90 C -98,118 -40,116 0,110 Z' fill='{rib}' stroke='{INK}' stroke-width='6' stroke-linejoin='round'/>"
              f"<path d='M 0,110 C 40,40 130,40 110,90 C 98,118 40,116 0,110 Z' fill='{rib}' stroke='{INK}' stroke-width='6' stroke-linejoin='round'/>"
              f"<circle cx='0' cy='106' r='16' fill='{rib}' stroke='{INK}' stroke-width='6'/>")
    else:
        # lid tilted off to the side
        g += (f"<g transform='rotate(-24 -200 150)'><rect x='-300' y='92' width='384' height='72' rx='12' fill='{body}' stroke='{INK}' stroke-width='7'/>"
              f"<rect x='-134' y='92' width='52' height='72' fill='{rib}' stroke='{INK}' stroke-width='5'/></g>")
        g += f"<rect x='-150' y='170' width='300' height='22' fill='{INK}' opacity='.35'/>"
    if tag:
        g += (f"<line x1='26' y1='240' x2='86' y2='262' stroke='{INK}' stroke-width='3'/>"
              f"<g transform='rotate(12 140 270)'><path d='M 84,240 L 112,214 L 214,214 L 214,318 L 112,318 L 84,292 Z' fill='#fff' stroke='{INK}' stroke-width='5' stroke-linejoin='round'/>"
              f"<circle cx='104' cy='266' r='7' fill='{INK}'/>"
              f"<text x='160' y='286' font-family='Heebo' font-weight='900' font-size='54' text-anchor='middle' fill='{MINT_D if tag == '✓' else INK}'>{tag}</text></g>")
    return g + "</g>"


def label(x, y, txt, fill, size=34):
    return (f"<text x='{x}' y='{y}' font-family='Heebo' font-weight='900' font-size='{size}' text-anchor='middle' "
            f"fill='{fill}' direction='rtl'>{txt}</text>")


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='640' viewBox='0 0 {w} 640'>"
        g += box(470, 60, 1.15, "closed", tag="?")
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='820' viewBox='0 0 {w} 820'>"
        # right side (read first in RTL): came for the prize, empty box, figures walking away
        g += box(700, 110, 0.7, "empty", body="#E6E8F0", rib=GREY)
        g += person(640, 600, 0.85, "grey", away=True) + person(800, 560, 0.75, "grey", away=True)
        # left side: came for the business, content cards, figures staying
        g += box(240, 110, 0.7, "content")
        g += person(120, 600, 0.85, "mint") + person(240, 610, 0.85, "mint") + person(360, 600, 0.85, "mint")
        g += f"<line x1='470' y1='40' x2='470' y2='680' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        g += label(700, 690, "באו בשביל הפרס", INK, 38) + label(700, 740, "הפרס חולק, הם המשיכו הלאה", SUB, 30)
        g += label(240, 690, "באו בשביל העסק", MINT_D, 38) + label(240, 740, "נשארים לראות עוד", SUB, 30)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; rows = ""
        for i, l in enumerate(labels):
            last = i == len(labels) - 1
            tagc = (f"<div style='flex:none;width:96px;height:72px;position:relative;"
                    f"background:{'#fff' if last else MINT};border:5px {'dashed' if last else 'solid'} {INK if not last else MINT_D};"
                    f"border-radius:10px 22px 22px 10px;display:flex;align-items:center;justify-content:center;"
                    f"font-size:42px;font-weight:900;color:{INK}'>{i + 1}</div>")
            rows += (f"<div style='display:flex;align-items:center;gap:30px;padding:16px 0'>{tagc}"
                     f"<span style='font-size:42px;font-weight:900;color:{INK if not last else SUB}'>{l}</span></div>")
        return (f"<div style='width:840px;position:relative;background:#fff;border:6px solid {INK};border-radius:28px;overflow:hidden;"
                f"box-shadow:12px 14px 0 rgba(16,27,79,.12)'>"
                f"<div style='background:{NAVY};color:#fff;font-size:32px;font-weight:900;padding:16px 34px'>מה שנשאר אחרי ההגרלה</div>"
                f"<div style='position:absolute;top:70px;bottom:0;right:78px;width:24px;background:{MINT};opacity:.35'></div>"
                f"<div style='position:relative;padding:14px 30px 18px 30px'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='620' viewBox='0 0 {w} 620'>"
        g += box(470, 40, 1.15, "closed", tag="✓")
        return g + "</svg>"
    return ""


def ad_gift(spec):
    slides = spec["slides"]; n = len(slides); out = []
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.gf mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='gf' style='position:absolute;inset:0;overflow:hidden;background:{BG};color:{INK}'>{confetti(11 + i)}")
        tl = f"<div style='background:{NAVY};border-radius:22px;padding:14px 22px;display:inline-flex'>{logo(52)}</div>"
        if s.get("layout") == "end":
            body = wrap + f"""<div style='position:absolute;inset:0;padding:110px 90px;display:flex;flex-direction:column;justify-content:center;gap:40px'>
              <div style='background:{NAVY};border-radius:30px;padding:24px 34px;align-self:flex-start;display:flex'>{logo(110)}</div>
              <h2 style='font-size:{s.get('size', 60)}px;line-height:1.2'>{s['head']}</h2>
              <p style='font-size:36px;color:{SUB};font-weight:700'>{s.get('body', '')}</p>
              <div><div style='display:inline-block;background:{MINT};color:{NAVY3};font-weight:800;font-size:40px;padding:24px 44px;border-radius:999px'>{s['cta']}</div></div>
              <div><span style='display:inline-block;font-size:26px;font-weight:700;padding:8px 20px;border-radius:999px;border:2px solid {SUB};color:{SUB};background:{BG}'>{s.get('tag', '')}</span></div></div></div>"""
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
              <span style='font-size:24px;color:{SUB};font-weight:700;background:{BG};padding:2px 8px'>{spec.get('note', 'המחשה')}</span></div></div>"""
        out.append(body)
    return out
