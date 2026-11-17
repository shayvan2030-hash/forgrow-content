"""Extra ad layouts, set 23 (added 2026-11-17).

ad_tincans — carousel on a pale pistachio ruled-notebook background: tin-can string phones.
             Business problem: new clients come only from referrals (word of mouth). Referrals are great, but
             they depend on someone remembering to mention you — one string, passed person to person, that can
             go slack. A relevant audience can hear the business directly, over time
             (discover -> follow -> keep seeing -> understand the offer -> maybe reach out).
             Route shown as five numbered tin cans on one string. Illustration only. Original logo on a navy tile.
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
MINT_L = "#B5F1DF"
BG = "#E6EFD9"
INK = "#101B4F"
MINT_D = "#0B7F62"
GREY = "#C3C7D4"
GREY_D = "#6E7390"
SUB = "#33407F"
TIN = "#D9DEE8"
STRING = "#B5523B"


def can(cx, cy, s, fill=TIN, stroke=INK, tilt=0, op=1):
    """Tin can seen from the side, open end facing -x when tilt=0 (rotated by tilt deg). s = height."""
    w = s * 0.78
    g = f"<g opacity='{op}' transform='rotate({tilt} {cx} {cy})'>"
    g += (f"<rect x='{cx - w / 2:.1f}' y='{cy - s / 2:.1f}' width='{w:.1f}' height='{s:.1f}' rx='{s * 0.08:.1f}' "
          f"fill='{fill}' stroke='{stroke}' stroke-width='4'/>")
    for k in (0.28, 0.5, 0.72):
        y = cy - s / 2 + s * k
        g += f"<line x1='{cx - w / 2 + 4:.1f}' y1='{y:.1f}' x2='{cx + w / 2 - 4:.1f}' y2='{y:.1f}' stroke='{stroke}' stroke-width='2' opacity='.35'/>"
    g += (f"<ellipse cx='{cx:.1f}' cy='{cy - s / 2:.1f}' rx='{w / 2:.1f}' ry='{s * 0.1:.1f}' fill='#FFFFFF' stroke='{stroke}' stroke-width='4'/>")
    g += f"<rect x='{cx - w / 2 + 6:.1f}' y='{cy - s * 0.32:.1f}' width='{w * 0.14:.1f}' height='{s * 0.6:.1f}' rx='4' fill='#fff' opacity='.55'/>"
    return g + "</g>"


def person(cx, by, h, fill, stroke=INK, op=1, arm=None):
    """Simple figure; arm = (x, y) point the raised hand reaches to (holding a can)."""
    r = h * 0.17
    hy = by - h + r
    bw = h * 0.52
    g = f"<g opacity='{op}'>"
    if arm:
        g += (f"<path d='M {cx:.1f},{hy + r * 2.4:.1f} Q {(cx + arm[0]) / 2:.1f},{hy + r * 3.2:.1f} {arm[0]:.1f},{arm[1]:.1f}' "
              f"fill='none' stroke='{stroke}' stroke-width='14' stroke-linecap='round'/>"
              f"<path d='M {cx:.1f},{hy + r * 2.4:.1f} Q {(cx + arm[0]) / 2:.1f},{hy + r * 3.2:.1f} {arm[0]:.1f},{arm[1]:.1f}' "
              f"fill='none' stroke='{fill}' stroke-width='7' stroke-linecap='round'/>")
    g += (f"<path d='M {cx - bw / 2:.1f},{by:.1f} Q {cx - bw / 2:.1f},{hy + r * 1.5:.1f} {cx:.1f},{hy + r * 1.5:.1f} "
          f"Q {cx + bw / 2:.1f},{hy + r * 1.5:.1f} {cx + bw / 2:.1f},{by:.1f} Z' fill='{fill}' stroke='{stroke}' stroke-width='4'/>")
    g += f"<circle cx='{cx:.1f}' cy='{hy:.1f}' r='{r:.1f}' fill='{fill}' stroke='{stroke}' stroke-width='4'/>"
    return g + "</g>"


def string(x1, y1, x2, y2, sag=0, dash=None, color=STRING, w=5):
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2 + sag
    d = f" stroke-dasharray='{dash}'" if dash else ""
    return (f"<path d='M {x1:.1f},{y1:.1f} Q {mx:.1f},{my:.1f} {x2:.1f},{y2:.1f}' fill='none' stroke='{color}' "
            f"stroke-width='{w}' stroke-linecap='round'{d}/>")


def label(x, y, txt, fill, size=34):
    return (f"<text x='{x}' y='{y}' font-family='Heebo' font-weight='900' font-size='{size}' text-anchor='middle' "
            f"fill='{fill}' direction='rtl'>{txt}</text>")


def qmark(cx, cy, s, fill=INK):
    return (f"<circle cx='{cx}' cy='{cy}' r='{s}' fill='#FFFFFF' stroke='{fill}' stroke-width='4'/>"
            f"<text x='{cx}' y='{cy + s * 0.38}' font-family='Heebo' font-weight='900' font-size='{s * 1.1}' "
            f"text-anchor='middle' fill='{fill}'>?</text>")


def waves(cx, cy, s, color=MINT_D, n=3, flip=False):
    g = ""
    sg = -1 if flip else 1
    for k in range(n):
        r = s * (0.5 + k * 0.45)
        g += (f"<path d='M {cx + sg * r * 0.5:.1f},{cy - r:.1f} Q {cx + sg * r * 1.1:.1f},{cy:.1f} {cx + sg * r * 0.5:.1f},{cy + r:.1f}' "
              f"fill='none' stroke='{color}' stroke-width='5' stroke-linecap='round' opacity='{1 - k * 0.25}'/>")
    return g


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='640' viewBox='0 0 {w} 640'>"
        # the business (right) holds a can to the ear; a long slack string leads off to one recommender far left
        g += string(612, 300, 268, 330, sag=170)
        g += person(760, 600, 330, MINT, arm=(690, 300))
        g += can(660, 300, 96, tilt=90)
        g += person(150, 600, 270, GREY, stroke=GREY_D, arm=(205, 335))
        g += can(230, 332, 80, fill="#E9ECF2", stroke=GREY_D, tilt=-90)
        g += qmark(440, 120, 46)
        g += label(760, 632, "העסק", INK, 30) + label(150, 632, "מישהו שממליץ", GREY_D, 30)
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='780' viewBox='0 0 {w} 780'>"
        # right (read first in RTL): referrals only — one string, passed person to person, with a gap
        g += can(840, 140, 74, tilt=90)
        g += string(803, 140, 742, 300, sag=30)
        g += can(715, 310, 60, fill="#E9ECF2", stroke=GREY_D, tilt=-90)
        g += string(688, 310, 650, 470, sag=20, dash="14 16", color=GREY_D)
        g += can(625, 480, 54, fill="#E9ECF2", stroke=GREY_D, tilt=-90, op=.75)
        g += string(600, 480, 580, 580, sag=10, dash="6 22", color=GREY_D, w=4)
        g += qmark(572, 612, 30, GREY_D)
        g += label(840, 70, "העסק", INK, 28)
        g += f"<line x1='470' y1='40' x2='470' y2='620' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        # left: relevant audience — several mint cans hearing the business directly
        hub = (380, 330)
        g += can(hub[0], hub[1], 74, tilt=90)
        pts = [(95, 110), (70, 300), (95, 490), (210, 600)]
        for i, (x, y) in enumerate(pts):
            g += string(hub[0] - 30, hub[1], x + 26, y, sag=18, color=MINT_D)
            g += can(x, y, 60, fill=MINT if i % 2 == 0 else MINT_L, tilt=-90)
        g += label(380, 260, "העסק", INK, 28)
        g += label(705, 690, "רק המלצות", INK, 36) + label(705, 738, "תלוי שמישהו יזכיר אתכם", SUB, 29)
        g += label(235, 690, "גם קהל רלוונטי", MINT_D, 36) + label(235, 738, "שומעים אתכם ישירות", SUB, 29)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; rows = ""
        for i, l in enumerate(labels):
            last = i == len(labels) - 1
            icon = (f"<div style='flex:none;width:78px;height:92px;position:relative'>"
                    f"<div style='position:absolute;inset:10px 0 0 0;border:5px {'dashed' if last else 'solid'} {MINT_D if last else INK};"
                    f"border-radius:10px;background:{'rgba(255,255,255,.6)' if last else (MINT if i % 2 == 0 else MINT_L)};"
                    f"display:flex;align-items:center;justify-content:center;font-size:42px;font-weight:900;color:{INK}'>{i + 1}</div>"
                    f"<div style='position:absolute;top:0;left:0;right:0;height:20px;border:5px {'dashed' if last else 'solid'} "
                    f"{MINT_D if last else INK};border-radius:50%;background:#fff'></div></div>")
            line = (f"<div style='width:6px;height:18px;background:{STRING};margin-right:36px;border-radius:3px'></div>"
                    if not last else "")
            rows += (f"<div style='display:flex;align-items:center;gap:26px'>{icon}"
                     f"<span style='font-size:42px;font-weight:900;color:{INK if not last else SUB}'>{l}</span></div>{line}")
        return (f"<div style='width:840px;background:#FFFFFF;border:6px solid {INK};border-radius:20px;overflow:hidden;"
                f"box-shadow:12px 14px 0 rgba(16,27,79,.14)'>"
                f"<div style='background:{NAVY};color:#fff;font-size:32px;font-weight:900;padding:16px 34px'>מה שקהל רלוונטי שומע לאורך זמן</div>"
                f"<div style='padding:20px 30px 22px 30px'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='620' viewBox='0 0 {w} 620'>"
        hub = (470, 300)
        pts = [(150, 120), (110, 330), (220, 520), (790, 120), (830, 330), (720, 520)]
        for i, (x, y) in enumerate(pts):
            g += string(hub[0] + (-40 if x < hub[0] else 40), hub[1], x, y, sag=20, color=MINT_D)
        for i, (x, y) in enumerate(pts):
            g += can(x, y, 70, fill=MINT if i % 2 == 0 else MINT_L, tilt=-90 if x < hub[0] else 90)
        g += can(hub[0], hub[1], 110)
        g += waves(hub[0] + 70, hub[1] - 40, 22) + waves(hub[0] - 70, hub[1] - 40, 22, flip=True)
        return g + "</svg>"
    return ""


def ad_tincans(spec):
    slides = spec["slides"]; n = len(slides); out = []
    paper = (f"background:{BG};background-image:"
             f"linear-gradient(90deg, transparent 0 1040px, rgba(181,82,59,.28) 1040px 1043px, transparent 1043px),"
             f"repeating-linear-gradient(180deg, transparent 0 52px, rgba(16,27,79,.09) 52px 54px)")
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT_D if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.tc mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='tc' style='position:absolute;inset:0;overflow:hidden;color:{INK};{paper}'>")
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
