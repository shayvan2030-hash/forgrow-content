"""Extra ad layouts, set 25 (added 2026-11-19).

ad_hourglass — carousel on a dusk (lilac -> apricot) evening background with soft sand dunes: an hourglass.
          Business problem: the owner spends evenings answering messages, and many of them come from people who are
          not the business's audience at all (far away, looking for something else, just curious) — the owner's
          time runs out like sand on the wrong people. A relevant audience that discovers the business and keeps
          seeing its content over time already understands the offer before it reaches out
          (discover -> follow -> keep seeing -> understand the offer -> maybe reach out).
          Route shown as five numbered sand layers. Illustration only. Original logo on a navy tile.
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
MINT_L = "#B5F1DF"
INK = "#101B4F"
MINT_D = "#0B7F62"
GREY = "#C9CBD6"
GREY_D = "#6E7390"
SUB = "#33407F"
WOOD = "#8A5A3C"
WOOD_L = "#B07A52"

_uid = [0]


def label(x, y, txt, fill, size=34):
    return (f"<text x='{x}' y='{y}' font-family='Heebo' font-weight='900' font-size='{size}' text-anchor='middle' "
            f"fill='{fill}' direction='rtl'>{txt}</text>")


def qmark(cx, cy, s, fill=INK):
    return (f"<circle cx='{cx}' cy='{cy}' r='{s}' fill='#FFFFFF' stroke='{fill}' stroke-width='4'/>"
            f"<text x='{cx}' y='{cy + s * 0.38}' font-family='Heebo' font-weight='900' font-size='{s * 1.1}' "
            f"text-anchor='middle' fill='{fill}'>?</text>")


def hourglass(cx, cy, h, sand=GREY, sand_d=GREY_D, top=0.45, bottom=0.5, stream=True, grains=None):
    """Wooden-frame hourglass centred at (cx, cy); h = glass height.
    top / bottom = how full the upper / lower bulb is (0..1)."""
    _uid[0] += 1
    cid = f"hg{_uid[0]}"
    w = h * 0.58; nw = h * 0.035
    y0, y1 = cy - h / 2, cy + h / 2
    L, R = cx - w / 2, cx + w / 2
    glass = (f"M {L:.1f},{y0:.1f} C {L:.1f},{cy - h * .2:.1f} {cx - nw:.1f},{cy - h * .08:.1f} {cx - nw:.1f},{cy:.1f} "
             f"C {cx - nw:.1f},{cy + h * .08:.1f} {L:.1f},{cy + h * .2:.1f} {L:.1f},{y1:.1f} L {R:.1f},{y1:.1f} "
             f"C {R:.1f},{cy + h * .2:.1f} {cx + nw:.1f},{cy + h * .08:.1f} {cx + nw:.1f},{cy:.1f} "
             f"C {cx + nw:.1f},{cy - h * .08:.1f} {R:.1f},{cy - h * .2:.1f} {R:.1f},{y0:.1f} Z")
    g = f"<defs><clipPath id='{cid}'><path d='{glass}'/></clipPath></defs>"
    g += f"<path d='{glass}' fill='#FFFFFF' fill-opacity='.55'/>"
    g += f"<g clip-path='url(#{cid})'>"
    if top > 0:
        ty = cy - (h / 2) * top
        g += (f"<path d='M {L - 10:.1f},{ty + h * .02:.1f} Q {cx:.1f},{ty - h * .03:.1f} {R + 10:.1f},{ty + h * .02:.1f} "
              f"L {R + 10:.1f},{cy:.1f} L {L - 10:.1f},{cy:.1f} Z' fill='{sand}'/>")
    if bottom > 0:
        by = y1 - (h / 2) * bottom
        g += (f"<path d='M {L - 10:.1f},{y1:.1f} L {L - 10:.1f},{by + h * .06:.1f} Q {cx:.1f},{by - h * .08:.1f} "
              f"{R + 10:.1f},{by + h * .06:.1f} L {R + 10:.1f},{y1:.1f} Z' fill='{sand}'/>")
        if grains:
            for gx, gy in grains:
                g += f"<circle cx='{cx + gx * w / 2:.1f}' cy='{y1 - gy * h / 2:.1f}' r='{h * .012:.1f}' fill='{sand_d}' opacity='.55'/>"
    if stream and top > 0:
        g += f"<line x1='{cx:.1f}' y1='{cy - h * .02:.1f}' x2='{cx:.1f}' y2='{y1 - (h / 2) * bottom + 4:.1f}' stroke='{sand}' stroke-width='{max(3, h * .014):.1f}'/>"
    g += "</g>"
    g += f"<path d='{glass}' fill='none' stroke='{INK}' stroke-width='5' stroke-linejoin='round'/>"
    g += (f"<path d='M {L + w * .12:.1f},{y0 + h * .06:.1f} Q {L + w * .1:.1f},{cy - h * .22:.1f} {cx - w * .16:.1f},{cy - h * .1:.1f}' "
          f"fill='none' stroke='#FFFFFF' stroke-width='{h * .018:.1f}' stroke-linecap='round' opacity='.8'/>")
    pw, ph = w + h * 0.16, h * 0.07
    for py in (y0 - ph, y1):
        g += (f"<rect x='{cx - pw / 2:.1f}' y='{py:.1f}' width='{pw:.1f}' height='{ph:.1f}' rx='{ph * .35:.1f}' "
              f"fill='{WOOD}' stroke='{INK}' stroke-width='4'/>"
              f"<rect x='{cx - pw / 2 + 8:.1f}' y='{py + 5:.1f}' width='{pw - 16:.1f}' height='{ph * .28:.1f}' rx='3' fill='{WOOD_L}' opacity='.7'/>")
    for px in (cx - pw / 2 + h * .04, cx + pw / 2 - h * .04):
        g += (f"<rect x='{px - h * .014:.1f}' y='{y0:.1f}' width='{h * .028:.1f}' height='{h:.1f}' rx='4' "
              f"fill='{WOOD_L}' stroke='{INK}' stroke-width='3'/>")
    return g


def moon(cx, cy, r):
    return (f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='#FFF4D6'/>"
            f"<circle cx='{cx + r * .45}' cy='{cy - r * .25}' r='{r * .85}' fill='#E9DDF0'/>")


G1 = ((-.5, .1), (-.2, .25), (.15, .12), (.45, .2), (.0, .35), (-.35, .4), (.3, .45))


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='660' viewBox='0 0 {w} 660'>"
        g += f"<ellipse cx='470' cy='612' rx='300' ry='26' fill='{INK}' opacity='.10'/>"
        g += hourglass(470, 320, 500, top=.32, bottom=.62, grains=G1)
        g += qmark(780, 200, 44, GREY_D) + qmark(165, 300, 36, GREY_D) + qmark(760, 440, 30, GREY_D)
        g += label(470, 652, "עוד ערב של הודעות", SUB, 30)
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='800' viewBox='0 0 {w} 800'>"
        g += f"<line x1='470' y1='20' x2='470' y2='640' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        # right (read first): grey sand — time spent on people who are not the audience
        g += f"<ellipse cx='705' cy='600' rx='170' ry='18' fill='{INK}' opacity='.10'/>"
        g += hourglass(705, 320, 470, top=.2, bottom=.78, grains=G1)
        g += qmark(905, 250, 28, GREY_D) + qmark(505, 400, 24, GREY_D)
        g += label(705, 690, "קהל לא קשור לעסק", INK, 36) + label(705, 738, "הזמן הולך על הסברים", SUB, 29)
        # left: mint sand — a relevant audience that has seen the content over time
        g += f"<ellipse cx='235' cy='600' rx='170' ry='18' fill='{INK}' opacity='.10'/>"
        g += hourglass(235, 320, 470, sand=MINT, sand_d=MINT_D, top=.55, bottom=.38, grains=G1[:4])
        g += label(235, 690, "קהל רלוונטי", MINT_D, 36) + label(235, 738, "ראו תוכן לאורך זמן", SUB, 29)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; n = len(labels); rows = ""
        for i, l in enumerate(labels):
            last = i == n - 1
            fill = "#FFFFFF" if last else (MINT if i % 2 == 0 else MINT_L)
            border = f"border:4px dashed {MINT_D}" if last else f"border:4px solid {INK}"
            rows += (f"<div style='position:relative;display:flex;align-items:center;gap:24px;background:{fill};{border};"
                     f"border-radius:16px;padding:12px 26px;margin-right:{(n - 1 - i) * 10}px;margin-left:{(n - 1 - i) * 10}px'>"
                     f"<span style='flex:none;width:58px;height:58px;border-radius:50%;background:{NAVY};color:#fff;display:flex;"
                     f"align-items:center;justify-content:center;font-size:30px;font-weight:900'>{i + 1}</span>"
                     f"<span style='font-size:42px;font-weight:900;color:{SUB if last else INK}'>{l}</span></div>")
        icon = f"<svg width='70' height='100' viewBox='0 0 140 200' style='flex:none'>{hourglass(70, 100, 150, sand=MINT, sand_d=MINT_D, top=.4, bottom=.5)}</svg>"
        return (f"<div style='width:840px;background:#FFFFFF;border:6px solid {INK};border-radius:20px;overflow:hidden;"
                f"box-shadow:12px 14px 0 rgba(16,27,79,.14)'>"
                f"<div style='background:{NAVY};color:#fff;font-size:32px;font-weight:900;padding:12px 34px;display:flex;align-items:center;gap:20px'>"
                f"{icon}<span>שכבה אחרי שכבה, לאורך זמן</span></div>"
                f"<div style='padding:30px 30px 30px 30px;display:flex;flex-direction:column;gap:16px'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='620' viewBox='0 0 {w} 620'>"
        g += f"<ellipse cx='470' cy='585' rx='260' ry='24' fill='{INK}' opacity='.10'/>"
        g += hourglass(470, 300, 470, sand=MINT, sand_d=MINT_D, top=.5, bottom=.45, grains=G1[:5])
        return g + "</svg>"
    return ""


def dunes(end=False):
    op = .55 if end else .8
    return (f"<svg style='position:absolute;left:0;right:0;bottom:0' width='1080' height='300' viewBox='0 0 1080 300' preserveAspectRatio='none'>"
            f"<path d='M0,170 Q220,80 470,150 T1080,120 L1080,300 L0,300 Z' fill='#F6C9A0' opacity='{op}'/>"
            f"<path d='M0,230 Q300,160 600,220 T1080,200 L1080,300 L0,300 Z' fill='#EFB383' opacity='{op}'/></svg>")


def ad_hourglass(spec):
    slides = spec["slides"]; n = len(slides); out = []
    sky = "background:linear-gradient(180deg,#E9DDF0 0%,#F6E3E3 50%,#FBE7D3 100%)"
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT_D if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        end = s.get("layout") == "end"
        show_moon = end or s.get('scene', {}).get('kind') in ('intro', 'one')
        deco = dunes(end) + ('' if not show_moon else f"<svg style='position:absolute;left:96px;top:{150 if end else 440}px' width='120' height='120' viewBox='0 0 120 120'>{moon(60, 60, 44)}</svg>")
        wrap = (f"<style>.hg mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='hg' style='position:absolute;inset:0;overflow:hidden;color:{INK};{sky}'>{deco}")
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
