"""Extra ad layouts, set 13 (added 2026-11-06). Imported by ads.py.

ad_ripples — carousel on pale aqua background: concentric rings like ripples on water. Inner ring = people close to the
             business (friends, supporters); outer ring = people interested in the field (illustration only).
             The route (discover -> follow -> keep seeing -> understand the offer -> may reach out) is a numbered list.
             Original logo as supplied on a navy tile (light background).
"""
import math
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
BG = "#DDF3F5"
INK = "#101B4F"
MINT_D = "#0E8F6E"
LAV = "#C5CBEE"
PERI = "#8799DB"


def dot(x, y, c, r=22):
    return (f"<circle cx='{x:.0f}' cy='{y:.0f}' r='{r}' fill='{c}' stroke='{INK}' stroke-width='4'/>")


def ring(cx, cy, r, dash=False, op=.28, c=INK):
    d = " stroke-dasharray='6 14'" if dash else ""
    return f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='none' stroke='{c}' stroke-opacity='{op}' stroke-width='5'{d}/>"


def on_ring(cx, cy, r, angles, c):
    return "".join(dot(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)), c) for a in angles)


def chip(x, y, text, fill, w=300, color=None):
    color = color or INK
    return (f"<rect x='{x - w / 2}' y='{y - 30}' width='{w}' height='60' rx='30' fill='{fill}' stroke='{INK}' stroke-width='4'/>"
            f"<text x='{x}' y='{y + 12}' font-family='Heebo' font-weight='900' font-size='31' text-anchor='middle' fill='{color}'>{text}</text>")


def center(cx, cy):
    return (f"<circle cx='{cx}' cy='{cy}' r='52' fill='{INK}'/>"
            f"<text x='{cx}' y='{cy + 14}' font-family='Heebo' font-weight='900' font-size='38' text-anchor='middle' fill='#fff'>אתם</text>")


def scene(sc, w=940):
    k = sc["kind"]
    cx, cy = 470, 330
    if k == "intro":
        cy = 290
        g = f"<svg width='{w}' height='640' viewBox='0 0 {w} 640'>"
        g += ring(cx, cy, 255, True, .22) + ring(cx, cy, 185, True, .3) + ring(cx, cy, 110, False, .4)
        g += on_ring(cx, cy, 110, [20, 100, 170, 245, 320], LAV)
        g += f"<text x='{cx}' y='{cy - 200}' font-family='Heebo' font-weight='900' font-size='76' text-anchor='middle' fill='{MINT_D}'>?</text>"
        g += f"<text x='{cx - 185}' y='{cy + 28}' font-family='Heebo' font-weight='900' font-size='66' text-anchor='middle' fill='{MINT_D}'>?</text>"
        g += f"<text x='{cx + 185}' y='{cy + 28}' font-family='Heebo' font-weight='900' font-size='66' text-anchor='middle' fill='{MINT_D}'>?</text>"
        g += center(cx, cy)
        g += chip(cx, 600, "חברים ומשפחה בפנים", "#fff", 440)
        return g + "</svg>"
    if k == "split":
        cy = 290
        g = f"<svg width='{w}' height='640' viewBox='0 0 {w} 640'>"
        g += ring(cx, cy, 255, True, .35, MINT_D) + ring(cx, cy, 110, False, .4)
        g += on_ring(cx, cy, 110, [15, 95, 175, 250, 330], LAV)
        g += on_ring(cx, cy, 255, [-70, -20, 35, 150, 205], MINT)
        g += center(cx, cy)
        g += chip(250, 600, "תומכים וקרובים", "#fff", 380)
        g += chip(690, 600, "מתעניינים בתחום", MINT, 380, NAVY3)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]
        rows = ""
        for i, l in enumerate(labels):
            rows += (f"<div style='display:flex;align-items:center;gap:24px;width:{820 - i * 0}px;height:90px;border-radius:45px;padding:0 20px;"
                     f"margin-right:{(len(labels) - 1 - i) * 0}px;background:{MINT if i else '#fff'};border:5px solid {INK};font-size:40px;font-weight:900;color:{NAVY3}'>"
                     f"<span style='display:inline-flex;width:{44 + i * 6}px;height:{44 + i * 6}px;border-radius:50%;background:{BG};border:4px solid {INK};"
                     f"align-items:center;justify-content:center;font-size:30px;flex:none'>{i + 1}</span>{l}</div>")
            if i < len(labels) - 1:
                rows += f"<div style='width:8px;height:20px;background:{INK};opacity:.5'></div>"
        return f"<div style='display:flex;flex-direction:column;align-items:center'>{rows}</div>"
    if k == "one":
        g = f"<svg width='{w}' height='560' viewBox='0 0 {w} 560'>"
        c2 = 280
        g += ring(cx, c2, 250, True, .3, MINT_D) + ring(cx, c2, 160, False, .35) + ring(cx, c2, 90, False, .45)
        g += on_ring(cx, c2, 250, [-60, 10, 80, 150, 215], MINT)
        g += on_ring(cx, c2, 160, [-30, 110, 200], MINT)
        g += center(cx, c2).replace("r='52'", "r='46'")
        return g + "</svg>"
    return ""


def ad_ripples(spec):
    slides = spec["slides"]; n = len(slides); out = []
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.rp mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='rp' style='position:absolute;inset:0;overflow:hidden;background:{BG};color:{INK}'>")
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
