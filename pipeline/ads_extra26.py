"""Extra ad layouts, set 26 (added 2026-11-20).

ad_giftbox — carousel on a warm off-white background with scattered confetti: a giveaway gift box.
          Business problem: the owner ran a giveaway (contest) and got many followers at once — but a lot of them
          came for the prize, not for the business; once the prize is handed out they move on and do not keep
          seeing the content. A relevant audience comes because it is interested in what the business offers
          (discover -> follow -> keep seeing -> understand the offer -> maybe reach out).
          Route shown as five numbered small gift boxes. Illustration only. Original logo on a navy tile.
"""
import math
import random
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
MINT_L = "#B5F1DF"
INK = "#101B4F"
MINT_D = "#0B7F62"
GREY = "#D9DBE4"
GREY_D = "#6E7390"
SUB = "#33407F"
CORAL = "#F08A6C"
CORAL_D = "#C8614A"
GOLD = "#F5C451"
PERI = "#8799DB"


def label(x, y, txt, fill, size=34):
    return (f"<text x='{x}' y='{y}' font-family='Heebo' font-weight='900' font-size='{size}' text-anchor='middle' "
            f"fill='{fill}' direction='rtl'>{txt}</text>")


def person(cx, by, h, fill, stroke=INK, op=1, carry=None):
    r = h * 0.17
    hy = by - h + r
    bw = h * 0.52
    g = f"<g opacity='{op}'>"
    g += (f"<path d='M {cx - bw / 2:.1f},{by:.1f} Q {cx - bw / 2:.1f},{hy + r * 1.5:.1f} {cx:.1f},{hy + r * 1.5:.1f} "
          f"Q {cx + bw / 2:.1f},{hy + r * 1.5:.1f} {cx + bw / 2:.1f},{by:.1f} Z' fill='{fill}' stroke='{stroke}' stroke-width='4'/>")
    g += f"<circle cx='{cx:.1f}' cy='{hy:.1f}' r='{r:.1f}' fill='{fill}' stroke='{stroke}' stroke-width='4'/>"
    if carry:  # small gift held in front of the body
        s = h * 0.30
        g += gift(cx + carry * bw * .32, by - h * .18, s, s * .8, fill=carry_fill(fill), ribbon="#FFFFFF", bow=False)
    return g + "</g>"


def carry_fill(fill):
    return "#A9AEC4" if fill == GREY else CORAL


def gift(cx, by, w, h, fill=CORAL, ribbon=GOLD, stroke=INK, open_=False, bow=True, num=None, dash=False, glow=None):
    """Gift box standing on y=by. open_: lid lifted and tilted."""
    lid_h = h * 0.22
    bx, by0 = cx - w / 2, by - h + lid_h
    sw = 5 if w > 120 else 4
    d = " stroke-dasharray='10 7'" if dash else ""
    g = f"<ellipse cx='{cx:.1f}' cy='{by:.1f}' rx='{w * .58:.1f}' ry='{max(6, w * .05):.1f}' fill='{INK}' opacity='.13'/>"
    if glow:
        for k, a in enumerate((-60, -35, -12, 12, 35, 60)):
            g += (f"<line x1='{cx:.1f}' y1='{by0 - 6:.1f}' x2='{cx + w * .9 * math.sin(math.radians(a)):.1f}' "
                  f"y2='{by0 - 6 - w * .75 * math.cos(math.radians(a)):.1f}' stroke='{glow}' stroke-width='{sw + 3}' "
                  f"stroke-linecap='round' opacity='.85'/>")
    g += (f"<rect x='{bx:.1f}' y='{by0:.1f}' width='{w:.1f}' height='{h - lid_h:.1f}' rx='{w * .04:.1f}' fill='{fill}' stroke='{stroke}' stroke-width='{sw}'{d}/>"
          f"<rect x='{cx - w * .07:.1f}' y='{by0:.1f}' width='{w * .14:.1f}' height='{h - lid_h:.1f}' fill='{ribbon}' stroke='{stroke}' stroke-width='{sw - 1}'{d}/>")
    lw = w * 1.1
    if open_:
        ly = by0 - lid_h - h * .32
        g += f"<g transform='rotate(-16 {cx - lw / 2:.1f} {ly + lid_h:.1f})'>"
    else:
        ly = by0 - lid_h
        g += "<g>"
    g += (f"<rect x='{cx - lw / 2:.1f}' y='{ly:.1f}' width='{lw:.1f}' height='{lid_h:.1f}' rx='{w * .04:.1f}' fill='{fill}' stroke='{stroke}' stroke-width='{sw}'{d}/>"
          f"<rect x='{cx - w * .07:.1f}' y='{ly:.1f}' width='{w * .14:.1f}' height='{lid_h:.1f}' fill='{ribbon}' stroke='{stroke}' stroke-width='{sw - 1}'{d}/>")
    if bow:
        bs = w * .2
        g += (f"<path d='M {cx:.1f},{ly:.1f} C {cx - bs * 1.6:.1f},{ly - bs * 1.3:.1f} {cx - bs * 1.9:.1f},{ly + bs * .1:.1f} {cx:.1f},{ly:.1f} Z' fill='{ribbon}' stroke='{stroke}' stroke-width='{sw - 1}'/>"
              f"<path d='M {cx:.1f},{ly:.1f} C {cx + bs * 1.6:.1f},{ly - bs * 1.3:.1f} {cx + bs * 1.9:.1f},{ly + bs * .1:.1f} {cx:.1f},{ly:.1f} Z' fill='{ribbon}' stroke='{stroke}' stroke-width='{sw - 1}'/>"
              f"<circle cx='{cx:.1f}' cy='{ly:.1f}' r='{bs * .28:.1f}' fill='{ribbon}' stroke='{stroke}' stroke-width='{sw - 1}'/>")
    g += "</g>"
    if num:
        g += (f"<circle cx='{cx + w * .27:.1f}' cy='{by0 + (h - lid_h) * .5:.1f}' r='{w * .17:.1f}' fill='#FFFFFF' stroke='{stroke}' stroke-width='3'/>"
              f"<text x='{cx + w * .27:.1f}' y='{by0 + (h - lid_h) * .5 + w * .085:.1f}' font-family='Heebo' font-weight='900' font-size='{w * .23:.1f}' text-anchor='middle' fill='{INK}'>{num}</text>")
    return g


def confetti(seed=7, n=46, end=False):
    rnd = random.Random(seed)
    n = n + 30 if end else n
    cols = [CORAL, GOLD, MINT, PERI]
    g = ""
    for _ in range(n):
        x, y = rnd.uniform(0, 1080), rnd.uniform(0, 1350)
        # keep the text area calmer
        if (90 < y < 420 and 60 < x < 1020) or (end and 320 < y < 1030 and 60 < x < 1020):
            continue
        r = rnd.uniform(-50, 50); c = rnd.choice(cols)
        if rnd.random() < .5:
            g += f"<rect x='{x:.0f}' y='{y:.0f}' width='18' height='8' rx='3' fill='{c}' transform='rotate({r:.0f} {x:.0f} {y:.0f})'/>"
        else:
            g += f"<circle cx='{x:.0f}' cy='{y:.0f}' r='6' fill='{c}'/>"
    return f"<svg style='position:absolute;inset:0;opacity:{.35 if end else .55}' width='1080' height='1350' viewBox='0 0 1080 1350'>{g}</svg>"


def arrow(x1, y, x2, color=GREY_D):
    s = 1 if x2 > x1 else -1
    return (f"<line x1='{x1}' y1='{y}' x2='{x2}' y2='{y}' stroke='{color}' stroke-width='5' stroke-linecap='round' stroke-dasharray='12 10'/>"
            f"<path d='M {x2 - s * 18},{y - 14} L {x2},{y} L {x2 - s * 18},{y + 14}' fill='none' stroke='{color}' stroke-width='5' stroke-linecap='round' stroke-linejoin='round'/>")


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='640' viewBox='0 0 {w} 640'>"
        g += (f"<g transform='rotate(-6 760 70)'><rect x='672' y='38' width='176' height='64' rx='12' fill='{INK}'/>"
              f"<circle cx='690' cy='70' r='8' fill='#FBF5EF'/>{label(770, 84, 'הגרלה!', GOLD, 34)}</g>")
        g += gift(470, 470, 300, 300, open_=False)
        # a crowd of grey figures around the box, all looking at the prize
        for x, y, h in ((95, 560, 140), (215, 600, 160), (335, 625, 150), (605, 625, 150), (725, 600, 160), (845, 560, 140)):
            g += person(x, y, h, GREY, op=.95)
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='800' viewBox='0 0 {w} 800'>"
        g += f"<line x1='470' y1='20' x2='470' y2='640' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        # right (read first): empty open box, grey figures carrying a prize walk away to the edge
        g += gift(760, 330, 190, 190, fill="#F3D2C6", ribbon="#FBE7B5", open_=True)
        g += f"<circle cx='590' cy='230' r='34' fill='#FFFFFF' stroke='{GREY_D}' stroke-width='4'/>" + label(590, 243, "?", GREY_D, 38)
        for x, y, op in ((610, 590, .95), (735, 600, .75), (860, 590, .55)):
            g += person(x, y, 150, GREY, op=op, carry=1)
        g += arrow(560, 398, 900)
        g += label(705, 690, "באו בשביל הפרס", INK, 36) + label(705, 738, "וממשיכים הלאה", SUB, 29)
        # left: a navy box with a mint ribbon, mint figures gathered around because of what the business offers
        g += gift(235, 380, 200, 200, fill=NAVY, ribbon=MINT, open_=True, glow=MINT)
        for x, y, h, f in ((95, 600, 140, MINT), (235, 615, 150, MINT_L), (375, 600, 140, MINT)):
            g += person(x, y, h, f)
        g += label(235, 690, "קהל רלוונטי", MINT_D, 36) + label(235, 738, "בא בשביל מה שאתם מציעים", SUB, 29)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; n = len(labels); rows = ""
        for i, l in enumerate(labels):
            last = i == n - 1
            fill = "#FFFFFF" if last else (MINT if i % 2 == 0 else MINT_L)
            t = (f"<svg width='120' height='96' viewBox='0 0 120 96' style='flex:none'>"
                 f"{gift(60, 90, 78, 74, fill=fill, ribbon=NAVY if not last else MINT_D, stroke=MINT_D if last else INK, dash=last, num=str(i + 1))}</svg>")
            rows += (f"<div style='display:flex;align-items:center;gap:26px'>{t}"
                     f"<span style='font-size:42px;font-weight:900;color:{SUB if last else INK}'>{l}</span></div>")
        return (f"<div style='width:840px;background:#FFFFFF;border:6px solid {INK};border-radius:20px;overflow:hidden;"
                f"box-shadow:12px 14px 0 rgba(16,27,79,.14)'>"
                f"<div style='background:{NAVY};color:#fff;font-size:32px;font-weight:900;padding:18px 34px;display:flex;align-items:center;gap:18px'>"
                f"<span style='width:18px;height:18px;border-radius:50%;background:{MINT};flex:none'></span>לא פרס אחד, אלא דרך לאורך זמן</div>"
                f"<div style='padding:20px 40px 24px 40px;display:flex;flex-direction:column;gap:6px'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='600' viewBox='0 0 {w} 600'>"
        g += gift(470, 470, 280, 260, fill=NAVY, ribbon=MINT, open_=True, glow=MINT)
        for x, y, h, f in ((150, 560, 150, MINT), (270, 580, 130, MINT_L), (680, 580, 130, MINT_L), (800, 560, 150, MINT)):
            g += person(x, y, h, f)
        return g + "</svg>"
    return ""


def ad_giftbox(spec):
    slides = spec["slides"]; n = len(slides); out = []
    bg = "background:#FBF5EF"
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT_D if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        end = s.get("layout") == "end"
        wrap = (f"<style>.gb mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='gb' style='position:absolute;inset:0;overflow:hidden;color:{INK};{bg}'>{confetti(11 + i, end=end)}")
        tl = f"<div style='background:{NAVY};border-radius:22px;padding:14px 22px;display:inline-flex'>{logo(52)}</div>"
        if end:
            body = wrap + f"""<div style='position:absolute;inset:0;padding:110px 90px;display:flex;flex-direction:column;justify-content:center;gap:40px'>
              <div style='background:{NAVY};border-radius:30px;padding:24px 34px;align-self:flex-start;display:flex'>{logo(110)}</div>
              <h2 style='font-size:{s.get('size', 60)}px;line-height:1.2'>{s['head']}</h2>
              <p style='font-size:36px;color:{SUB};font-weight:700'>{s.get('body', '')}</p>
              <div><div style='display:inline-block;background:{MINT};color:{NAVY3};font-weight:800;font-size:40px;padding:24px 44px;border-radius:999px;box-shadow:0 6px 0 {INK}'>{s['cta']}</div></div>
              <div><span style='display:inline-block;font-size:26px;font-weight:700;padding:8px 20px;border-radius:999px;border:2px solid {SUB};color:{SUB};background:#FFFFFF'>{s.get('tag', '')}</span></div></div></div>"""
        else:
            st = (f"<div style='position:absolute;right:96px;bottom:{s.get('stamp_bottom', 640)}px;transform:rotate(-4deg);background:{NAVY};"
                  f"color:#fff;border-radius:10px;padding:6px;box-shadow:6px 8px 0 rgba(16,27,79,.15)'>"
                  f"<div style='border:3px solid {MINT};border-radius:6px;padding:8px 26px;font-size:38px;font-weight:900'>{s['stamp']}</div></div>"
                  if s.get("stamp") else "")
            body = wrap + f"""<div style='position:absolute;top:56px;left:80px;right:80px;display:flex;gap:10px'>{dots}</div>
            <div style='position:absolute;top:112px;right:80px;left:80px;display:flex;flex-direction:column;gap:14px'>
              {f"<div style='font-size:32px;font-weight:900;color:{MINT_D}'>{s['kicker']}</div>" if s.get('kicker') else ''}
              <h2 style='font-size:{s.get('size', 62)}px;line-height:1.12'>{s['head']}</h2>
              {f"<p style='font-size:33px;color:{SUB};line-height:1.4;font-weight:700'>{s['body']}</p>" if s.get('body') else ''}</div>
            <div style='position:absolute;top:{s.get('scene_top', 420)}px;bottom:{s.get('scene_bottom', 130)}px;left:0;right:0;display:flex;justify-content:center;align-items:center'>{scene(s['scene'])}</div>{st}
            <div style='position:absolute;bottom:40px;right:80px;left:80px;display:flex;justify-content:space-between;align-items:center'>{tl}
              <span style='font-size:24px;color:{SUB};font-weight:700;background:#FFFFFF;border-radius:6px;padding:2px 10px'>{spec.get('note', 'המחשה')}</span></div></div>"""
        out.append(body)
    return out
