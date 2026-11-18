"""Extra ad layouts, set 24 (added 2026-11-18).

ad_kite — carousel on a pale morning-sky background with soft clouds: paper planes vs. a kite on a string.
          Business problem: "feast or famine" — every promotion brings a few inquiries, then silence, and the next
          promotion starts from zero again (a paper plane: launched, glides, lands). A relevant audience that keeps
          seeing the business between promotions is like a kite that stays up while the string holds
          (discover -> follow -> keep seeing -> understand the offer -> maybe reach out).
          Route shown as five numbered bows on the kite's tail. Illustration only. Original logo on a navy tile.
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
MINT_L = "#B5F1DF"
INK = "#101B4F"
MINT_D = "#0B7F62"
GREY = "#C3C7D4"
GREY_D = "#6E7390"
SUB = "#33407F"
GRASS = "#CFE7C4"
STRING = "#33407F"


def label(x, y, txt, fill, size=34):
    return (f"<text x='{x}' y='{y}' font-family='Heebo' font-weight='900' font-size='{size}' text-anchor='middle' "
            f"fill='{fill}' direction='rtl'>{txt}</text>")


def qmark(cx, cy, s, fill=INK):
    return (f"<circle cx='{cx}' cy='{cy}' r='{s}' fill='#FFFFFF' stroke='{fill}' stroke-width='4'/>"
            f"<text x='{cx}' y='{cy + s * 0.38}' font-family='Heebo' font-weight='900' font-size='{s * 1.1}' "
            f"text-anchor='middle' fill='{fill}'>?</text>")


def plane(cx, cy, s, rot=0, fill="#FFFFFF", stroke=GREY_D, op=1):
    """Paper plane pointing +x (before rotation). s = length."""
    p = lambda x, y: f"{cx + x * s:.1f},{cy + y * s:.1f}"
    g = f"<g opacity='{op}' transform='rotate({rot} {cx} {cy})'>"
    g += f"<polygon points='{p(.5, 0)} {p(-.5, -.32)} {p(-.28, 0)}' fill='{fill}' stroke='{stroke}' stroke-width='4' stroke-linejoin='round'/>"
    g += f"<polygon points='{p(.5, 0)} {p(-.28, 0)} {p(-.5, .22)}' fill='{GREY}' stroke='{stroke}' stroke-width='4' stroke-linejoin='round'/>"
    return g + "</g>"


def flight(pts, color=GREY_D, w=4, dash="10 14"):
    d = "M " + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts[:1]) + " Q " + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts[1:])
    return f"<path d='{d}' fill='none' stroke='{color}' stroke-width='{w}' stroke-linecap='round' stroke-dasharray='{dash}'/>"


def kite(cx, cy, s, fill=MINT, stroke=INK, tail=True, bows=4):
    """Diamond kite centred at (cx, cy); s = height. Returns (svg, tail-bottom point)."""
    w = s * 0.72
    top, bot, l, r = (cx, cy - s * .45), (cx, cy + s * .55), (cx - w / 2, cy - s * .08), (cx + w / 2, cy - s * .08)
    g = (f"<polygon points='{top[0]:.1f},{top[1]:.1f} {r[0]:.1f},{r[1]:.1f} {bot[0]:.1f},{bot[1]:.1f} {l[0]:.1f},{l[1]:.1f}' "
         f"fill='{fill}' stroke='{stroke}' stroke-width='5' stroke-linejoin='round'/>")
    g += (f"<polygon points='{top[0]:.1f},{top[1]:.1f} {r[0]:.1f},{r[1]:.1f} {cx:.1f},{r[1]:.1f}' fill='{MINT_L}' opacity='.9'/>"
          f"<polygon points='{bot[0]:.1f},{bot[1]:.1f} {l[0]:.1f},{l[1]:.1f} {cx:.1f},{l[1]:.1f}' fill='{MINT_L}' opacity='.9'/>")
    g += (f"<line x1='{top[0]:.1f}' y1='{top[1]:.1f}' x2='{bot[0]:.1f}' y2='{bot[1]:.1f}' stroke='{stroke}' stroke-width='3'/>"
          f"<line x1='{l[0]:.1f}' y1='{l[1]:.1f}' x2='{r[0]:.1f}' y2='{r[1]:.1f}' stroke='{stroke}' stroke-width='3'/>")
    end = bot
    if tail:
        pts = [bot]
        for k in range(1, bows + 1):
            pts.append((bot[0] + (24 if k % 2 else -24), bot[1] + k * s * 0.32))
        d = f"M {pts[0][0]:.1f},{pts[0][1]:.1f} " + " ".join(f"T {x:.1f},{y:.1f}" for x, y in pts[1:])
        g = f"<path d='{d}' fill='none' stroke='{stroke}' stroke-width='3'/>" + g
        for x, y in pts[1:]:
            g += bow(x, y, s * 0.12)
        end = pts[-1]
    return g, end


def bow(x, y, s, fill=MINT, stroke=INK):
    return (f"<polygon points='{x:.1f},{y:.1f} {x - s:.1f},{y - s * .6:.1f} {x - s:.1f},{y + s * .6:.1f}' fill='{fill}' stroke='{stroke}' stroke-width='3' stroke-linejoin='round'/>"
            f"<polygon points='{x:.1f},{y:.1f} {x + s:.1f},{y - s * .6:.1f} {x + s:.1f},{y + s * .6:.1f}' fill='{fill}' stroke='{stroke}' stroke-width='3' stroke-linejoin='round'/>")


def person(cx, by, h, fill, stroke=INK, op=1, arm=None, look_up=False):
    r = h * 0.17
    hy = by - h + r
    bw = h * 0.52
    g = f"<g opacity='{op}'>"
    if arm:
        g += (f"<path d='M {cx:.1f},{hy + r * 2.4:.1f} Q {(cx + arm[0]) / 2:.1f},{hy + r * 2.6:.1f} {arm[0]:.1f},{arm[1]:.1f}' "
              f"fill='none' stroke='{stroke}' stroke-width='14' stroke-linecap='round'/>"
              f"<path d='M {cx:.1f},{hy + r * 2.4:.1f} Q {(cx + arm[0]) / 2:.1f},{hy + r * 2.6:.1f} {arm[0]:.1f},{arm[1]:.1f}' "
              f"fill='none' stroke='{fill}' stroke-width='7' stroke-linecap='round'/>")
    g += (f"<path d='M {cx - bw / 2:.1f},{by:.1f} Q {cx - bw / 2:.1f},{hy + r * 1.5:.1f} {cx:.1f},{hy + r * 1.5:.1f} "
          f"Q {cx + bw / 2:.1f},{hy + r * 1.5:.1f} {cx + bw / 2:.1f},{by:.1f} Z' fill='{fill}' stroke='{stroke}' stroke-width='4'/>")
    g += f"<circle cx='{cx:.1f}' cy='{hy:.1f}' r='{r:.1f}' fill='{fill}' stroke='{stroke}' stroke-width='4'/>"
    if look_up:
        g += f"<circle cx='{cx - r * .3:.1f}' cy='{hy - r * .3:.1f}' r='{r * .13:.1f}' fill='{stroke}'/><circle cx='{cx + r * .3:.1f}' cy='{hy - r * .3:.1f}' r='{r * .13:.1f}' fill='{stroke}'/>"
    return g + "</g>"


def ground(w, y, h=60):
    return f"<path d='M 0,{y + 14} Q {w / 4},{y - 6} {w / 2},{y + 6} T {w},{y} L {w},{y + h} L 0,{y + h} Z' fill='{GRASS}' stroke='{INK}' stroke-width='3' stroke-opacity='.25'/>"


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='640' viewBox='0 0 {w} 640'>"
        g += ground(w, 560, 80)
        # business (right) launches a paper plane; it glides left and lands in the grass; ? above
        g += person(810, 590, 260, MINT, arm=(735, 375))
        g += flight([(720, 360), (430, 60), (170, 520)])
        g += plane(400, 235, 120, rot=182, fill="#FFFFFF", stroke=INK)
        g += plane(160, 535, 100, rot=168, op=.85)
        g += qmark(150, 420, 40, GREY_D)
        g += label(810, 630, "העסק", INK, 30) + label(250, 630, "המבצע נחת", GREY_D, 30)
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='780' viewBox='0 0 {w} 780'>"
        g += ground(w, 560, 70)
        g += f"<line x1='470' y1='30' x2='470' y2='620' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        # right (read first): one plane after another, each lands — start from zero again
        g += person(860, 590, 200, MINT, arm=(805, 430))
        g += flight([(800, 420), (700, 120), (560, 540)])
        g += plane(690, 280, 84, rot=182, fill="#FFFFFF", stroke=INK)
        for x, r in ((560, 168), (630, 172), (750, 165)):
            g += plane(x, 560, 70, rot=r, op=.8)
        g += label(705, 670, "מבצע אחרי מבצע", INK, 36) + label(705, 718, "כל פעם מתחילים מאפס", SUB, 29)
        # left: kite stays up on a string; mint people look up at it
        kg, _ = kite(230, 170, 190, bows=3)
        g += f"<path d='M 380,450 Q 300,330 230,274' fill='none' stroke='{STRING}' stroke-width='3'/>"
        g += kg
        g += person(400, 590, 200, MINT, arm=(380, 450))
        for i, x in enumerate((90, 200, 300)):
            g += person(x, 590, 120, MINT if i % 2 == 0 else MINT_L, look_up=True)
        g += label(235, 670, "קהל רלוונטי", MINT_D, 36) + label(235, 718, "ממשיכים לראות גם בין המבצעים", SUB, 29)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; rows = ""
        for i, l in enumerate(labels):
            last = i == len(labels) - 1
            b = (f"<svg width='90' height='60' viewBox='0 0 90 60' style='flex:none'>"
                 f"<polygon points='45,30 6,6 6,54' fill='{'#fff' if last else (MINT if i % 2 == 0 else MINT_L)}' stroke='{MINT_D if last else INK}' stroke-width='4' stroke-linejoin='round'{' stroke-dasharray=\"8 6\"' if last else ''}/>"
                 f"<polygon points='45,30 84,6 84,54' fill='{'#fff' if last else (MINT if i % 2 == 0 else MINT_L)}' stroke='{MINT_D if last else INK}' stroke-width='4' stroke-linejoin='round'{' stroke-dasharray=\"8 6\"' if last else ''}/>"
                 f"<circle cx='45' cy='30' r='17' fill='{NAVY}'/>"
                 f"<text x='45' y='39' font-family='Heebo' font-weight='900' font-size='26' text-anchor='middle' fill='#fff'>{i + 1}</text></svg>")
            rows += (f"<div style='display:flex;align-items:center;gap:26px;position:relative;z-index:1'>{b}"
                     f"<span style='font-size:42px;font-weight:900;color:{INK if not last else SUB}'>{l}</span></div>")
        kg, _ = kite(60, 70, 120, tail=False)
        top = f"<svg width='120' height='140' viewBox='0 0 120 140' style='display:block;margin-right:16px'>{kg}</svg>"
        return (f"<div style='width:840px;background:#FFFFFF;border:6px solid {INK};border-radius:20px;overflow:hidden;"
                f"box-shadow:12px 14px 0 rgba(16,27,79,.14)'>"
                f"<div style='background:{NAVY};color:#fff;font-size:32px;font-weight:900;padding:16px 34px'>הזנב של העפיפון: מה שקורה לאורך זמן</div>"
                f"<div style='padding:14px 30px 26px 30px;position:relative'>{top}"
                f"<div style='position:absolute;right:89px;top:140px;bottom:50px;width:3px;background:{INK}'></div>"
                f"<div style='display:flex;flex-direction:column;gap:14px'>{rows}</div></div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='620' viewBox='0 0 {w} 620'>"
        g += ground(w, 540, 80)
        kg, _ = kite(520, 150, 210, bows=3)
        g += f"<path d='M 640,420 Q 600,320 520,265' fill='none' stroke='{STRING}' stroke-width='3'/>" + kg
        g += person(660, 570, 190, MINT, arm=(640, 420))
        for i, (x, h) in enumerate(((130, 130), (240, 150), (350, 125), (800, 140), (890, 120))):
            g += person(x, 570, h, MINT if i % 2 == 0 else MINT_L, look_up=True)
        return g + "</svg>"
    return ""


def clouds(end=False):
    c = ""
    pos = ((70, 140, .9), (760, 120, .8), (60, 1150, .8), (800, 1190, .7)) if end else \
          ((60, 450, .9), (820, 430, .7), (330, 1170, .6), (620, 1195, .5))
    for x, y, s in pos:
        c += (f"<div style='position:absolute;left:{x}px;top:{y}px;width:{180 * s:.0f}px;height:{56 * s:.0f}px;background:#fff;"
              f"border-radius:999px;opacity:.75;box-shadow:{50 * s:.0f}px -{24 * s:.0f}px 0 -{4 * s:.0f}px #fff'></div>")
    return c


def ad_kite(spec):
    slides = spec["slides"]; n = len(slides); out = []
    sky = "background:linear-gradient(180deg,#CFE6F7 0%,#E4F1FA 55%,#F4F8FC 100%)"
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT_D if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.kt mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='kt' style='position:absolute;inset:0;overflow:hidden;color:{INK};{sky}'>{clouds(s.get('layout') == 'end')}")
        tl = f"<div style='background:{NAVY};border-radius:22px;padding:14px 22px;display:inline-flex'>{logo(52)}</div>"
        if s.get("layout") == "end":
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
