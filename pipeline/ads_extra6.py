"""Extra ad layouts, set 6 (added 2026-10-30). Imported by ads.py — run `python3 pipeline/ads.py <spec>`.

ad_radio — carousel on warm sand: a navy radio with a dial screen. Static noise (many people, wrong frequency) turns into a
           clean mint wave when the dial is "tuned" to the relevant audience; later slides show the relevant-audience path as
           chips under the radio, the approved ForGrow wording, then an end/CTA slide. No numbers or results are shown.
Identity anchors kept: founder's original logo (navy tile on light backgrounds), mint #14D8A5, Heebo.
"""
import math
import random
from render import THEME as T
from ads_extra import logo_tile, pill, NAVY, NAVY2, NAVY3

MINT = T["acc"]
BG = "#F4EADB"
SW, SH = 800, 230  # dial screen size


def _wave(state, seed):
    rnd = random.Random(seed)
    mid = SH / 2 - 14
    if state == "clear":
        pts = " ".join(f"{x},{mid + 62 * math.sin(x / 800 * 2 * math.pi * 3):.1f}" for x in range(0, SW + 1, 8))
        return f"<polyline points='{pts}' fill='none' stroke='{MINT}' stroke-width='9' stroke-linecap='round' stroke-linejoin='round'/>"
    amp = 80 if state == "static" else 46
    col = "#8799DB" if state == "static" else "#C5CBEE"
    bars = "".join(
        f"<line x1='{x}' x2='{x}' y1='{mid - rnd.uniform(6, amp):.0f}' y2='{mid + rnd.uniform(6, amp):.0f}' "
        f"stroke='{col}' stroke-width='6' stroke-linecap='round' opacity='{rnd.uniform(.45, 1):.2f}'/>"
        for x in range(10, SW, 18))
    return bars


def radio(state="static", tune=0.15, label=None, seed=3):
    ticks = "".join(
        f"<line x1='{x}' x2='{x}' y1='{SH - 46}' y2='{SH - (22 if i % 5 == 0 else 34)}' stroke='#8799DB' stroke-width='{4 if i % 5 == 0 else 3}'/>"
        for i, x in enumerate(range(20, SW, 20)))
    nx = 40 + tune * (SW - 80)
    lab = ""
    if label:
        lab = (f"<div style='position:absolute;left:{nx}px;top:-26px;transform:translateX(-50%);background:{MINT};color:{NAVY3};"
               f"font-size:30px;font-weight:900;padding:6px 22px;border-radius:999px;white-space:nowrap'>{label}</div>")
    needle_col = MINT if state == "clear" else "#FF8A7A"
    glow = f"filter:drop-shadow(0 0 10px {needle_col})"
    screen = f"""<div style='position:relative;width:{SW}px;height:{SH}px;background:{NAVY3};border-radius:26px;border:6px solid #0A1238;overflow:visible'>
      <svg width='{SW}' height='{SH}' viewBox='0 0 {SW} {SH}' style='position:absolute;inset:0;border-radius:20px;overflow:hidden'>{_wave(state, seed)}{ticks}</svg>
      <div style='position:absolute;left:{nx - 3}px;top:6px;bottom:6px;width:6px;border-radius:3px;background:{needle_col};{glow}'></div>{lab}</div>"""
    grille = "".join(f"<i style='width:16px;height:16px;border-radius:50%;background:#0A1238;opacity:.8'></i>" for _ in range(40))
    knob = lambda: (f"<div style='width:112px;height:112px;border-radius:50%;background:#C5CBEE;border:8px solid #8799DB;position:relative'>"
                    f"<i style='position:absolute;left:50%;top:10px;width:8px;height:34px;margin-left:-4px;border-radius:4px;background:{NAVY}'></i></div>")
    return f"""<div style='position:relative;width:900px;padding-top:150px'>
      <div style='position:absolute;top:0;left:130px;width:10px;height:190px;background:{NAVY2};border-radius:5px;transform:rotate(-24deg);transform-origin:bottom center'></div>
      <div style='position:relative;background:{NAVY};border-radius:56px;padding:50px 50px 44px;display:flex;flex-direction:column;gap:34px;
           box-shadow:0 30px 50px rgba(16,27,79,.35)'>
        {screen}
        <div style='display:flex;align-items:center;justify-content:space-between;padding:0 10px'>
          <div style='display:grid;grid-template-columns:repeat(10,16px);gap:12px;direction:ltr'>{grille}</div>
          <div style='display:flex;gap:30px'>{knob()}{knob()}</div></div></div></div>"""


def chips(items):
    out = []
    for i, t in enumerate(items):
        out.append(f"<div style='display:flex;align-items:center;gap:14px;background:#FFFFFF;border-radius:999px;padding:12px 30px 12px 16px;"
                   f"box-shadow:0 8px 18px rgba(16,27,79,.14)'><span style='width:44px;height:44px;border-radius:50%;background:{NAVY};color:{MINT};"
                   f"display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:900'>{i + 1}</span>"
                   f"<span style='font-size:32px;font-weight:800;color:{NAVY}'>{t}</span></div>")
    return "<div style='display:flex;flex-wrap:wrap;gap:14px;justify-content:center;width:900px'>" + "".join(out) + "</div>"


def ad_radio(spec):
    slides = spec["slides"]; n = len(slides); out = []
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{NAVY if k <= i else 'rgba(16,27,79,.22)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.rd mark{{color:{NAVY};background:linear-gradient(transparent 60%, {MINT} 60%, {MINT} 92%, transparent 92%)}}</style>"
                f"<div class='rd' style='position:absolute;inset:0;overflow:hidden;background:{BG};color:{NAVY}'>"
                f"<div style='position:absolute;top:-260px;left:-220px;width:700px;height:700px;border-radius:50%;background:#FFFFFF;opacity:.45'></div>")
        if s.get("layout") == "end":
            body = wrap + f"""<div style='position:absolute;inset:0;padding:110px 90px;display:flex;flex-direction:column;justify-content:center;gap:40px'>
              <div style='align-self:flex-start'>{logo_tile(200, 30)}</div>
              <h2 style='font-size:{s.get('size', 60)}px;line-height:1.2;color:{NAVY}'>{s['head']}</h2>
              <p style='font-size:36px;color:{NAVY2};font-weight:700'>{s.get('body', '')}</p>
              <div><div style='display:inline-block;background:{MINT};color:{NAVY3};font-weight:800;font-size:40px;padding:24px 44px;border-radius:999px'>{s['cta']}</div></div>
              <div>{pill(s['tag'], NAVY2, NAVY2) if s.get('tag') else ''}</div></div></div>"""
        else:
            r = s["radio"]
            under = chips(s["chips"]) if s.get("chips") else ""
            stamp = (f"<div style='position:absolute;right:120px;bottom:{s.get('stamp_bottom', 560)}px;transform:rotate(7deg);border:6px solid {MINT};"
                     f"color:#0B9C77;border-radius:18px;padding:8px 26px;font-size:40px;font-weight:900;background:rgba(255,255,255,.92)'>{s['stamp']}</div>"
                     if s.get("stamp") else "")
            body = wrap + f"""<div style='position:absolute;top:56px;left:80px;right:80px;display:flex;gap:10px'>{dots}</div>
            <div style='position:absolute;top:112px;right:80px;left:80px;display:flex;flex-direction:column;gap:14px'>
              {f"<div style='font-size:32px;font-weight:900;color:{NAVY}'>{s['kicker']}</div>" if s.get('kicker') else ''}
              <h2 style='font-size:{s.get('size', 62)}px;line-height:1.12;color:{NAVY}'>{s['head']}</h2>
              {f"<p style='font-size:33px;color:{NAVY2};line-height:1.4;font-weight:700'>{s['body']}</p>" if s.get('body') else ''}</div>
            <div style='position:absolute;bottom:{s.get('radio_bottom', 150)}px;left:90px;display:flex;flex-direction:column;gap:30px;align-items:center'>
              {radio(r.get('state', 'static'), r.get('tune', .15), r.get('label'), r.get('seed', 3))}{under}</div>{stamp}
            <div style='position:absolute;bottom:40px;right:80px;left:80px;display:flex;justify-content:space-between;align-items:center'>{logo_tile(58, 12)}
              <span style='font-size:24px;color:{NAVY2};font-weight:700'>{s.get('note', spec.get('note', 'המחשה'))}</span></div></div>"""
        out.append(body)
    return out
