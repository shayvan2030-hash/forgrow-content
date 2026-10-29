"""Extra ad layouts, set 3 (added 2026-10-29). Imported by ads.py — run `python3 pipeline/ads.py <spec>`.

ad_checklist — carousel on a lavender background: a clipboard self-check ("signs to check") that gets ticked
               slide by slide, then flips to the relevant-audience path, then an end/CTA slide.
Identity anchors kept: founder's original logo (navy tile on light backgrounds), mint #14D8A5, Heebo.
"""
from render import THEME as T, logo
from ads_extra import logo_tile, pill, NAVY, NAVY2, NAVY3, LIGHT_SUB

MINT = T["acc"]
BG = "#E4E8F8"
PAPER = "#FFFFFF"


def _check(state):
    """state: 'done' (mint tick), 'now' (mint tick, emphasised), 'open' (empty box), num:<n>, dash (dashed circle)."""
    if state in ("done", "now"):
        return (f"<div style='flex:none;width:60px;height:60px;border-radius:16px;background:{MINT};display:flex;"
                f"align-items:center;justify-content:center'><svg width='38' height='38' viewBox='0 0 38 38'>"
                f"<path d='M7 20 l8 8 l16 -18' fill='none' stroke='{NAVY3}' stroke-width='6' stroke-linecap='round' "
                f"stroke-linejoin='round'/></svg></div>")
    if state.startswith("num:"):
        return (f"<div style='flex:none;width:60px;height:60px;border-radius:50%;background:{NAVY};color:{MINT};display:flex;"
                f"align-items:center;justify-content:center;font-size:32px;font-weight:900'>{state[4:]}</div>")
    if state == "dash":
        return (f"<div style='flex:none;width:60px;height:60px;border-radius:50%;border:4px dashed {MINT};background:#F2FCF8;"
                f"display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:900;color:#0B9C77'>?</div>")
    return f"<div style='flex:none;width:60px;height:60px;border-radius:16px;border:4px solid #B9C1E6;background:#FFFFFF'></div>"


def clipboard(title, items, states, focus=None):
    rows = ""
    for k, (text, st) in enumerate(zip(items, states)):
        faded = st == "open" and focus is not None
        hl = (f"background:linear-gradient(transparent 58%, {MINT}66 58%, {MINT}66 94%, transparent 94%);"
              if k == focus else "")
        rows += (f"<div style='display:flex;align-items:center;gap:26px;padding:23px 0;border-bottom:3px solid #EDEFF8;"
                 f"opacity:{.42 if faded else 1}'>{_check(st)}"
                 f"<div style='font-size:35px;font-weight:{800 if k == focus else 700};color:{NAVY};line-height:1.25'>"
                 f"<span style='{hl}'>{text}</span></div></div>")
    return f"""<div style='position:relative;width:900px;padding-top:44px;transform:rotate(-1.2deg)'>
      <div style='position:absolute;top:0;left:50%;transform:translateX(-50%);width:270px;height:86px;border-radius:22px;
        background:{NAVY};box-shadow:0 10px 0 {NAVY3};display:flex;align-items:center;justify-content:center;z-index:2'>
        <div style='width:110px;height:22px;border-radius:11px;background:{BG}'></div></div>
      <div style='background:{NAVY2};border-radius:40px;padding:22px;box-shadow:0 30px 70px rgba(16,27,79,.28)'>
        <div style='background:{PAPER};border-radius:24px;padding:70px 54px 34px'>
          <div style='font-size:32px;font-weight:900;color:{LIGHT_SUB};margin-bottom:8px'>{title}</div>
          {rows}
        </div></div></div>"""


def ad_checklist(spec):
    slides = spec["slides"]; n = len(slides); out = []
    items = spec["items"]
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{NAVY if k <= i else 'rgba(16,27,79,.18)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.ck mark{{color:{NAVY};background:linear-gradient(transparent 60%, {MINT} 60%, {MINT} 92%, transparent 92%)}}</style>"
                f"<div class='ck' style='position:absolute;inset:0;overflow:hidden;background:{BG};color:{NAVY}'>"
                f"<div style='position:absolute;top:-240px;right:-220px;width:760px;height:620px;border-radius:50%;background:{MINT};opacity:.13'></div>")
        if s.get("layout") == "end":
            body = wrap + f"""<div style='position:absolute;inset:0;padding:110px 90px;display:flex;flex-direction:column;justify-content:center;gap:40px'>
              <div style='align-self:flex-start'>{logo_tile(200, 30)}</div>
              <h2 style='font-size:{s.get('size', 60)}px;line-height:1.2;color:{NAVY}'>{s['head']}</h2>
              <p style='font-size:36px;color:{LIGHT_SUB};font-weight:700'>{s.get('body', '')}</p>
              <div><div style='display:inline-block;background:{MINT};color:{NAVY3};font-weight:800;font-size:40px;padding:24px 44px;border-radius:999px'>{s['cta']}</div></div>
              <div>{pill(s['tag'], LIGHT_SUB, '#B9C1E6') if s.get('tag') else ''}</div></div></div>"""
        else:
            if s.get("board") == "path":
                p = spec["path"]
                board = clipboard(p["title"], p["items"],
                                  [f"num:{k + 1}" for k in range(len(p["items"]) - 1)] + ["dash"], focus=None)
            else:
                active = s.get("active", 0)
                states = ["done" if k < active - 1 else "now" if k == active - 1 else "open" for k in range(len(items))]
                board = clipboard(spec["title"], items, states, focus=(active - 1) if active else None)
            body = wrap + f"""<div style='position:absolute;top:56px;left:80px;right:80px;display:flex;gap:10px'>{dots}</div>
            <div style='position:absolute;top:112px;right:80px;left:80px;display:flex;flex-direction:column;gap:14px'>
              {f"<div style='font-size:32px;font-weight:900;color:#0B9C77'>{s['kicker']}</div>" if s.get('kicker') else ''}
              <h2 style='font-size:{s.get('size', 62)}px;line-height:1.12;color:{NAVY}'>{s['head']}</h2>
              {f"<p style='font-size:33px;color:{LIGHT_SUB};line-height:1.4;font-weight:700'>{s['body']}</p>" if s.get('body') else ''}</div>
            <div style='position:absolute;bottom:{s.get('board_bottom', 130)}px;left:90px'>{board}</div>
            <div style='position:absolute;bottom:40px;right:80px;display:flex;align-items:center;gap:24px'>{logo_tile(58, 12)}
              <span style='font-size:24px;color:{LIGHT_SUB};font-weight:700'>{s.get('note', spec.get('note', ''))}</span></div></div>"""
        out.append(body)
    return out
