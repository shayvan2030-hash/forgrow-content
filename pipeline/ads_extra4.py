"""Extra ad layouts, set 4 (added 2026-10-29, run 2). Imported by ads.py — run `python3 pipeline/ads.py <spec>`.

ad_theater — carousel on navy: a theatre hall seen from the back. The content is on a lit stage; the slides change who
             sits in the seats (empty / people who came for another show and look at their phones / a relevant
             audience watching), then a ticket-stub strip for the relevant-audience path, then an end/CTA slide.
Identity anchors kept: founder's original logo, mint #14D8A5, Heebo.
"""
import random
from render import THEME as T, logo
from ads_extra import pill, NAVY, NAVY2, NAVY3

MINT = T["acc"]
PERI, LAV = T["peri"], T["sub"]


def _person(x, y, s, color, phone=False, tilt=0):
    g = (f"<g transform='rotate({tilt} {x} {y + 30 * s})'><circle cx='{x}' cy='{y}' r='{15 * s}' fill='{color}'/>"
         f"<path d='M{x - 26 * s} {y + 44 * s} q0 -26 {26 * s} -26 q{26 * s} 0 {26 * s} 26 z' fill='{color}'/></g>")
    if phone:
        g += (f"<rect x='{x + 10 * s}' y='{y + 14 * s}' width='{14 * s}' height='{20 * s}' rx='{3 * s}' fill='#FFFFFF' opacity='.95'/>"
              f"<circle cx='{x + 17 * s}' cy='{y + 24 * s}' r='{22 * s}' fill='#FFFFFF' opacity='.12'/>")
    return g


def hall_svg(state, seed=7):
    """state: empty | mismatch | relevant"""
    rnd = random.Random(seed)
    w, h = 920, 640
    # stage
    curtains = ""
    for side in (0, 1):
        x0 = 40 if side == 0 else w - 40
        sgn = 1 if side == 0 else -1
        for k in range(5):
            xx = x0 + sgn * k * 24
            curtains += (f"<path d='M{xx} 30 q{sgn * 14} 120 0 250' stroke='{'#6F82CF' if k % 2 else PERI}' "
                         f"stroke-width='24' fill='none' stroke-linecap='round'/>")
    valance = "".join(f"<path d='M{40 + i * 84} 30 q42 46 84 0 z' fill='{PERI}'/>" for i in range(10))
    lit = state != "empty" or True
    cone = (f"<polygon points='400,30 520,30 640,250 280,250' fill='{MINT}' opacity='.10'/>" if lit else "")
    post = (f"<g transform='translate(390 120)'><rect width='140' height='140' rx='18' fill='#FFFFFF'/>"
            f"<rect x='14' y='14' width='112' height='70' rx='10' fill='{LAV}'/>"
            f"<rect x='14' y='96' width='80' height='10' rx='5' fill='{NAVY2}'/>"
            f"<rect x='14' y='114' width='56' height='10' rx='5' fill='{MINT}'/></g>")
    stage = (f"<rect x='40' y='30' width='{w - 80}' height='230' fill='#0A1238'/>{cone}"
             f"<ellipse cx='460' cy='262' rx='230' ry='22' fill='{MINT}' opacity='.18'/>{post}"
             f"<rect x='20' y='255' width='{w - 40}' height='28' rx='8' fill='{NAVY2}'/>{curtains}"
             f"<rect x='20' y='12' width='{w - 40}' height='24' rx='8' fill='#6F82CF'/>{valance}")
    # seats: 4 rows from front (top, smaller) to back (bottom, larger)
    seats = ""
    rows = [(340, 11, .72), (408, 10, .82), (484, 9, .94), (568, 8, 1.06)]
    for r, (y, n, s) in enumerate(rows):
        span = 640 + r * 70
        for k in range(n):
            x = 460 - span / 2 + span * (k + .5) / n
            seats += (f"<rect x='{x - 34 * s}' y='{y + 22 * s}' width='{68 * s}' height='{40 * s}' rx='{10 * s}' "
                      f"fill='{NAVY2}' stroke='#2A3A86' stroke-width='3'/>")
            if state == "mismatch":
                if rnd.random() < .78:
                    seats += _person(x, y, s, PERI, phone=rnd.random() < .7, tilt=rnd.choice((-14, -8, 8, 14)))
            elif state == "relevant":
                if r <= 1 or (r == 2 and k % 3 != 1) or (r == 3 and k % 3 == 0):
                    seats += _person(x, y, s, MINT)
    return f"<svg width='{w}' height='{h}' viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg'>{stage}{seats}</svg>"


def tickets(steps):
    out = ""
    for k, t in enumerate(steps):
        last = k == len(steps) - 1
        bd = f"3px dashed {MINT}" if last else f"3px solid {MINT}"
        out += (f"<div style='display:flex;align-items:center;gap:22px;border:{bd};border-radius:20px;padding:16px 26px;"
                f"background:{'transparent' if last else 'rgba(20,216,165,.09)'}'>"
                f"<span style='flex:none;width:52px;height:52px;border-radius:50%;background:{MINT if not last else 'transparent'};"
                f"border:{'none' if not last else '3px dashed ' + MINT};color:{NAVY3 if not last else MINT};display:flex;"
                f"align-items:center;justify-content:center;font-size:28px;font-weight:900'>{'?' if last else k + 1}</span>"
                f"<span style='font-size:36px;font-weight:800;color:#FFFFFF'>{t}</span></div>")
    return f"<div style='width:920px;display:flex;flex-direction:column;gap:16px'>{out}</div>"


def ad_theater(spec):
    slides = spec["slides"]; n = len(slides); out = []
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT if k <= i else T['line']}'></i>"
                       for k in range(n))
        wrap = (f"<div style='position:absolute;inset:0;overflow:hidden;background:radial-gradient(1000px 900px at 50% 20%, {NAVY2} 0%, {NAVY} 55%, {NAVY3} 100%)'>")
        if s.get("layout") == "end":
            body = wrap + f"""<div style='position:absolute;inset:0;padding:110px 90px;display:flex;flex-direction:column;justify-content:center;gap:40px'>
              {logo(300)}
              <h2 style='font-size:{s.get('size', 56)}px;line-height:1.2'>{s['head']}</h2>
              <p style='font-size:36px;color:{LAV};font-weight:700'>{s.get('body', '')}</p>
              <div><div style='display:inline-block;background:{MINT};color:{NAVY3};font-weight:800;font-size:40px;padding:24px 44px;border-radius:999px'>{s['cta']}</div></div>
              <div>{pill(s['tag'], LAV, T['line']) if s.get('tag') else ''}</div></div></div>"""
        else:
            visual = tickets(spec["steps"]) if s.get("visual") == "tickets" else hall_svg(s.get("hall", "empty"))
            body = wrap + f"""<div style='position:absolute;top:56px;left:80px;right:80px;display:flex;gap:10px'>{dots}</div>
            <div style='position:absolute;top:112px;right:80px;left:80px;display:flex;flex-direction:column;gap:14px'>
              {f"<div style='font-size:32px;font-weight:900;color:{MINT}'>{s['kicker']}</div>" if s.get('kicker') else ''}
              <h2 style='font-size:{s.get('size', 62)}px;line-height:1.12'>{s['head']}</h2>
              {f"<p style='font-size:33px;color:{LAV};line-height:1.4'>{s['body']}</p>" if s.get('body') else ''}</div>
            <div style='position:absolute;bottom:{s.get('visual_bottom', 175)}px;left:80px'>{visual}</div>
            <div style='position:absolute;bottom:40px;right:80px;left:80px;display:flex;justify-content:space-between;align-items:center'>{logo(70)}
              <span style='font-size:24px;color:{LAV};font-weight:700'>{s.get('note', spec.get('note', 'המחשה'))}</span></div></div>"""
        out.append(body)
    return out
