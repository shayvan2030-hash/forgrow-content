"""Extra ad layouts, set 20 (added 2026-11-13).

ad_tailor — carousel on a warm linen background with a fine woven texture: a tailor's dress form (בובת תופרת).
            Business problem: when the reactions come from people who are not the business's audience, it is easy to
            start "sewing" the content to their measurements, and then it fits nobody who actually needs the offer.
            Grey loose garment pinned on a grey form (random audience) vs a mint garment fitted to the form
            (relevant audience). Route shown as a vertical measuring tape with five numbered marks.
            Illustration only. Original logo on a navy tile.
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
BG = "#F3ECE2"
INK = "#101B4F"
MINT_D = "#0E8F6E"
GREY = "#B9BCC9"
FORM = "#E4D6C1"
SUB = "#3C4A8F"

TORSO = ("M -40,30 C -80,40 -115,50 -122,80 C -132,130 -125,170 -100,220 C -88,250 -88,270 -105,310 "
         "C -120,345 -118,370 -110,385 L 110,385 C 118,370 120,345 105,310 C 88,270 88,250 100,220 "
         "C 125,170 132,130 122,80 C 115,50 80,40 40,30 Z")


def pin(x, y, rot=0):
    return (f"<g transform='rotate({rot} {x} {y})'><line x1='{x}' y1='{y}' x2='{x}' y2='{y + 34}' stroke='{INK}' stroke-width='3'/>"
            f"<circle cx='{x}' cy='{y}' r='8' fill='#D9534F' stroke='{INK}' stroke-width='2'/></g>")


def form(cx, top, s=1.0, mode="plain", tag=None):
    """mode: plain (bare form), loose (grey oversized garment, pinned), fitted (mint garment)."""
    g = f"<g transform='translate({cx} {top}) scale({s})'>"
    # stand
    g += (f"<rect x='-8' y='380' width='16' height='190' fill='{INK}'/>"
          f"<path d='M 0,565 L -95,625 M 0,565 L 95,625 M 0,565 L 0,632' stroke='{INK}' stroke-width='12' stroke-linecap='round'/>"
          f"<circle cx='-95' cy='627' r='11' fill='{INK}'/><circle cx='95' cy='627' r='11' fill='{INK}'/><circle cx='0' cy='634' r='11' fill='{INK}'/>")
    # neck + knob
    g += (f"<rect x='-24' y='0' width='48' height='36' rx='6' fill='{FORM}' stroke='{INK}' stroke-width='6'/>"
          f"<circle cx='0' cy='-10' r='16' fill='{INK}'/>")
    body_fill = MINT if mode == "fitted" else FORM
    g += f"<path d='{TORSO}' fill='{body_fill}' stroke='{INK}' stroke-width='7' stroke-linejoin='round'/>"
    if mode == "plain":
        g += (f"<path d='M 0,40 L 0,380' stroke='{INK}' stroke-width='3' stroke-dasharray='10 10' opacity='.35'/>"
              f"<path d='M -95,250 Q 0,268 95,250' stroke='{INK}' stroke-width='3' stroke-dasharray='10 10' opacity='.35' fill='none'/>")
    if mode == "fitted":
        g += (f"<path d='M -40,32 L 0,110 L 40,32' fill='{FORM}' stroke='{INK}' stroke-width='6' stroke-linejoin='round'/>"
              f"<path d='M 0,110 L 0,380' stroke='{INK}' stroke-width='3' stroke-dasharray='12 9' opacity='.55'/>"
              f"<path d='M -92,248 Q 0,266 92,248' stroke='{INK}' stroke-width='4' stroke-dasharray='12 9' fill='none' opacity='.7'/>"
              f"<circle cx='0' cy='160' r='7' fill='{INK}'/><circle cx='0' cy='205' r='7' fill='{INK}'/>")
    if mode == "loose":
        g += (f"<g transform='rotate(7 0 200)'>"
              f"<path d='M -62,22 L -200,72 L -248,215 L -180,232 L -158,160 L -175,450 L 175,450 L 158,160 L 180,232 "
              f"L 248,215 L 200,72 L 62,22 Q 0,62 -62,22 Z' fill='{GREY}' fill-opacity='.92' stroke='#6E7390' stroke-width='6' stroke-linejoin='round'/>"
              f"<path d='M -150,300 Q -60,330 0,300 Q 70,270 150,310' stroke='#6E7390' stroke-width='4' fill='none' opacity='.6'/>"
              f"<path d='M -120,390 Q -40,420 30,390' stroke='#6E7390' stroke-width='4' fill='none' opacity='.6'/>"
              f"</g>" + pin(-120, 120, -20) + pin(110, 160, 25) + pin(-40, 300, 10) + pin(140, 360, -15))
    if tag:
        g += (f"<g transform='rotate(-8 170 70)'><line x1='118' y1='72' x2='150' y2='72' stroke='{INK}' stroke-width='3'/>"
              f"<rect x='150' y='40' width='130' height='64' rx='10' fill='#fff' stroke='{INK}' stroke-width='4'/>"
              f"<circle cx='166' cy='72' r='6' fill='{INK}'/>"
              f"<text x='222' y='88' font-family='Heebo' font-weight='900' font-size='44' text-anchor='middle' fill='{MINT_D if mode == 'fitted' else INK}'>{tag}</text></g>")
    return g + "</g>"


def tape_around(cx, y, w, s=1.0):
    """A mint tape measure draped around the neck of a form, hanging down both sides."""
    ticks = "".join(f"<line x1='{cx - w / 2 + 15}' y1='{y + 40 + k * 22}' x2='{cx - w / 2 + 27}' y2='{y + 40 + k * 22}' stroke='{INK}' stroke-width='3'/>"
                    for k in range(10))
    ticks += "".join(f"<line x1='{cx + w / 2 - 15}' y1='{y + 60 + k * 22}' x2='{cx + w / 2 - 27}' y2='{y + 60 + k * 22}' stroke='{INK}' stroke-width='3'/>"
                     for k in range(11))
    return (f"<path d='M {cx - w / 2 + 22},{y + 250} L {cx - w / 2 + 22},{y + 30} Q {cx - w / 2 + 22},{y} {cx},{y} "
            f"Q {cx + w / 2 - 22},{y} {cx + w / 2 - 22},{y + 30} L {cx + w / 2 - 22},{y + 290}' fill='none' stroke='{INK}' stroke-width='38' stroke-linecap='butt'/>"
            f"<path d='M {cx - w / 2 + 22},{y + 250} L {cx - w / 2 + 22},{y + 30} Q {cx - w / 2 + 22},{y} {cx},{y} "
            f"Q {cx + w / 2 - 22},{y} {cx + w / 2 - 22},{y + 30} L {cx + w / 2 - 22},{y + 290}' fill='none' stroke='{MINT}' stroke-width='28' stroke-linecap='butt'/>"
            + ticks)


def label(x, y, txt, fill, size=34):
    return (f"<text x='{x}' y='{y}' font-family='Heebo' font-weight='900' font-size='{size}' text-anchor='middle' "
            f"fill='{fill}' direction='rtl'>{txt}</text>")


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='700' viewBox='0 0 {w} 700'>"
        g += form(470, 40, 1.0, "plain", tag="?")
        g += tape_around(470, 50, 124)
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='820' viewBox='0 0 {w} 820'>"
        g += form(690, 60, 0.92, "loose")
        g += form(250, 60, 0.92, "fitted")
        g += f"<line x1='470' y1='40' x2='470' y2='640' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        g += label(690, 720, "לפי קהל מקרי", INK, 38) + label(690, 770, "גדול, עקום, מחזיק בסיכות", SUB, 30)
        g += label(250, 720, "לפי קהל רלוונטי", MINT_D, 38) + label(250, 770, "נתפר למי שצריך אותו", SUB, 30)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; rows = ""
        for i, l in enumerate(labels):
            last = i == len(labels) - 1
            seg = (f"<div style='width:120px;align-self:stretch;flex:none;position:relative;"
                   f"background:{MINT if not last else 'transparent'};"
                   f"{'border:4px dashed ' + MINT_D + ';' if last else ''}"
                   f"border-left:{'4px' if not last else '4px'} solid {INK};"
                   f"background-image:repeating-linear-gradient(180deg, {INK} 0 3px, transparent 3px 18px);"
                   f"background-size:26px 100%;background-repeat:no-repeat;background-position:left top'>"
                   f"<span style='position:absolute;right:16px;top:50%;transform:translateY(-50%);font-size:46px;font-weight:900;color:{INK}'>{i + 1}</span></div>")
            rows += (f"<div style='display:flex;align-items:center;gap:32px;min-height:104px;"
                     f"{'border-top:4px solid ' + INK + ';' if i else ''}'>{seg}"
                     f"<span style='font-size:42px;font-weight:900;color:{INK if not last else SUB}'>{l}</span></div>")
        return (f"<div style='width:840px;background:#FFFDF8;border:6px solid {INK};border-radius:28px;overflow:hidden;"
                f"box-shadow:12px 14px 0 rgba(16,27,79,.12)'>"
                f"<div style='background:{NAVY};color:#fff;font-size:32px;font-weight:900;padding:16px 34px'>המידות של קהל רלוונטי</div>"
                f"<div style='padding:0 0 0 30px'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='640' viewBox='0 0 {w} 640'>"
        g += form(470, 22, 0.92, "fitted", tag="✓")
        return g + "</svg>"
    return ""


def ad_tailor(spec):
    slides = spec["slides"]; n = len(slides); out = []
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.tl mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='tl' style='position:absolute;inset:0;overflow:hidden;background:{BG};color:{INK};"
                f"background-image:repeating-linear-gradient(0deg, rgba(16,27,79,.045) 0 2px, transparent 2px 7px),"
                f"repeating-linear-gradient(90deg, rgba(16,27,79,.045) 0 2px, transparent 2px 7px)'>")
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
