"""Extra ad layouts, set 5 (added 2026-10-29, run 3). Imported by ads.py — run `python3 pipeline/ads.py <spec>`.

ad_receipt — carousel on periwinkle: a paper receipt ("the invoice of one post"). Every investment line is itemised,
             but the line "who did it reach" stays blank; later slides fill the receipt with the relevant-audience path,
             then an end/CTA slide. No numbers or results are shown.
Identity anchors kept: founder's original logo (navy tile on light backgrounds), mint #14D8A5, Heebo.
"""
from render import THEME as T, logo
from ads_extra import logo_tile, pill, NAVY, NAVY2, NAVY3, LIGHT_SUB

MINT = T["acc"]
BG = "#8799DB"
ZIG = "conic-gradient(from -45deg at bottom, transparent 90deg, #FFFFFF 0) 0 100%/36px 100% repeat-x"


def _row(r):
    kind = r.get("kind", "line")
    t, v = r["t"], r.get("v", "")
    if kind == "blank":
        val = (f"<span style='flex:none;min-width:170px;height:58px;border:4px dashed {MINT};border-radius:14px;background:#F2FCF8;"
               f"display:flex;align-items:center;justify-content:center;font-size:38px;font-weight:900;color:#0B9C77'>?</span>")
        return (f"<div style='display:flex;align-items:center;justify-content:space-between;gap:20px;padding:24px 0'>"
                f"<span style='font-size:38px;font-weight:900;color:{NAVY}'>{t}</span>{val}</div>")
    if kind == "good":
        return (f"<div style='display:flex;align-items:center;justify-content:space-between;gap:20px;padding:18px 22px;margin:8px -22px;"
                f"background:{MINT};border-radius:18px'><span style='font-size:36px;font-weight:900;color:{NAVY3}'>{t}</span>"
                f"<span style='font-size:34px;font-weight:900;color:{NAVY3}'>{v}</span></div>")
    if kind == "step":
        return (f"<div style='display:flex;align-items:center;gap:22px;padding:17px 0;border-bottom:3px dashed #D5DAF0'>"
                f"<span style='flex:none;width:50px;height:50px;border-radius:50%;background:{NAVY};color:{MINT};display:flex;"
                f"align-items:center;justify-content:center;font-size:28px;font-weight:900'>{v}</span>"
                f"<span style='font-size:35px;font-weight:800;color:{NAVY}'>{t}</span></div>")
    return (f"<div style='display:flex;align-items:center;justify-content:space-between;gap:20px;padding:19px 0;"
            f"border-bottom:3px dashed #D5DAF0'><span style='font-size:35px;font-weight:800;color:{NAVY}'>{t}</span>"
            f"<span style='font-size:34px;font-weight:900;color:#0B9C77'>{v}</span></div>")


def receipt(title, rows, stamp=None):
    body = "".join(_row(r) for r in rows)
    st = (f"<div style='position:absolute;left:26px;top:-34px;transform:rotate(-7deg);border:6px solid {MINT};color:#0B9C77;"
          f"border-radius:18px;padding:8px 26px;font-size:40px;font-weight:900;background:rgba(255,255,255,.85)'>{stamp}</div>"
          if stamp else "")
    return f"""<div style='position:relative;width:860px;transform:rotate(-1.4deg);filter:drop-shadow(0 26px 40px rgba(10,18,56,.35))'>
      <div style='background:#FFFFFF;padding:46px 52px 40px;border-radius:14px 14px 0 0'>
        <div style='text-align:center;font-size:30px;font-weight:900;color:{LIGHT_SUB};letter-spacing:2px;padding-bottom:16px;border-bottom:4px solid {NAVY}'>{title}</div>
        {body}</div>
      <div style='height:34px;background:#FFFFFF;-webkit-mask:conic-gradient(from -45deg at bottom,#0000 90deg,#000 0) 0 100%/34px 100% repeat-x;mask:conic-gradient(from -45deg at bottom,#0000 90deg,#000 0) 0 100%/34px 100% repeat-x'></div>
      {st}</div>"""


def ad_receipt(spec):
    slides = spec["slides"]; n = len(slides); out = []
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{NAVY if k <= i else 'rgba(16,27,79,.25)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.rc mark{{color:{NAVY};background:linear-gradient(transparent 60%, {MINT} 60%, {MINT} 92%, transparent 92%)}}</style>"
                f"<div class='rc' style='position:absolute;inset:0;overflow:hidden;background:{BG};color:{NAVY}'>"
                f"<div style='position:absolute;bottom:-260px;left:-240px;width:760px;height:620px;border-radius:50%;background:#C5CBEE;opacity:.35'></div>")
        if s.get("layout") == "end":
            body = wrap + f"""<div style='position:absolute;inset:0;padding:110px 90px;display:flex;flex-direction:column;justify-content:center;gap:40px'>
              <div style='align-self:flex-start'>{logo_tile(200, 30)}</div>
              <h2 style='font-size:{s.get('size', 60)}px;line-height:1.2;color:{NAVY}'>{s['head']}</h2>
              <p style='font-size:36px;color:{NAVY2};font-weight:700'>{s.get('body', '')}</p>
              <div><div style='display:inline-block;background:{MINT};color:{NAVY3};font-weight:800;font-size:40px;padding:24px 44px;border-radius:999px'>{s['cta']}</div></div>
              <div>{pill(s['tag'], NAVY2, NAVY2) if s.get('tag') else ''}</div></div></div>"""
        else:
            r = s["receipt"]
            body = wrap + f"""<div style='position:absolute;top:56px;left:80px;right:80px;display:flex;gap:10px'>{dots}</div>
            <div style='position:absolute;top:112px;right:80px;left:80px;display:flex;flex-direction:column;gap:14px'>
              {f"<div style='font-size:32px;font-weight:900;color:{NAVY}'>{s['kicker']}</div>" if s.get('kicker') else ''}
              <h2 style='font-size:{s.get('size', 62)}px;line-height:1.12;color:{NAVY}'>{s['head']}</h2>
              {f"<p style='font-size:33px;color:{NAVY2};line-height:1.4;font-weight:700'>{s['body']}</p>" if s.get('body') else ''}</div>
            <div style='position:absolute;bottom:{s.get('board_bottom', 150)}px;left:110px'>{receipt(r['title'], r['rows'], r.get('stamp'))}</div>
            <div style='position:absolute;bottom:40px;right:80px;left:80px;display:flex;justify-content:space-between;align-items:center'>{logo_tile(58, 12)}
              <span style='font-size:24px;color:{NAVY2};font-weight:700'>{s.get('note', spec.get('note', 'המחשה'))}</span></div></div>"""
        out.append(body)
    return out
