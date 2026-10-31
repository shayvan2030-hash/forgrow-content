"""Extra ad layouts, set 7 (added 2026-10-31). Imported by ads.py — run `python3 pipeline/ads.py <spec>`.

ad_garden — carousel on pale mint: flower pots. The same seed (a post) in dry, cracked soil does not grow; in rich soil
            (a relevant audience) it moves through stages: discover -> follow -> keep seeing -> understand the offer -> may reach out.
            Then the approved ForGrow wording and an end/CTA slide. Illustration only: no numbers or results.
Identity anchors kept: founder's original logo (navy tile on light backgrounds), mint #14D8A5, Heebo.
"""
from render import THEME as T
from ads_extra import logo_tile, pill, NAVY, NAVY2, NAVY3

MINT = T["acc"]
BG = "#E4F8F1"
GREEN = "#0B9C77"
POT = "#8799DB"


def pot(stage=0, soil="rich", w=300, label=None, tone=None, fs=30):
    """stage 0 = seed, 1 sprout, 2 stem+leaves, 3 bud, 4 flower. soil: rich | dry."""
    sc = "#5B4636" if soil == "rich" else "#CDBBA3"
    cracks = ("<path d='M100 218 l18 10 l-8 8 l16 8 M176 214 l-12 12 l12 8 M140 232 l8 6' stroke='#9C8668' stroke-width='4' fill='none' stroke-linecap='round'/>"
              if soil == "dry" else "")
    p = ""
    if stage == 0:
        p = f"<ellipse cx='150' cy='198' rx='24' ry='15' fill='{'#E8B04A' if soil == 'rich' else '#8A7656'}'/>"
    if stage >= 1:
        h = [0, 40, 100, 120, 120][stage]
        p += f"<path d='M150 216 L150 {216 - h}' stroke='{GREEN}' stroke-width='9' stroke-linecap='round'/>"
        p += f"<path d='M150 {216 - min(h, 44)} q-44 -6 -52 -40 q40 -2 52 40z' fill='{MINT}'/>"
    if stage >= 2:
        p += f"<path d='M150 {216 - 64} q44 -6 52 -40 q-40 -2 -52 40z' fill='{MINT}'/>"
    if stage == 3:
        p += f"<ellipse cx='150' cy='88' rx='20' ry='28' fill='{POT}'/><path d='M150 60 q-6 14 0 28' stroke='{NAVY}' stroke-width='3' fill='none'/>"
    if stage == 4:
        pet = "".join(f"<ellipse cx='150' cy='72' rx='17' ry='32' fill='#F7B7C6' transform='rotate({a} 150 102)'/>" for a in range(0, 360, 60))
        p += pet + f"<circle cx='150' cy='102' r='19' fill='#FFD36B'/>"
    svg = f"""<svg width='{w}' height='{int(w * 0.95)}' viewBox='0 0 300 285' style='overflow:visible'>
      {p}
      <ellipse cx='150' cy='222' rx='94' ry='20' fill='{sc}'/>{cracks}
      <path d='M62 222 h176 l-18 58 h-140z' fill='{NAVY}'/><rect x='54' y='214' width='192' height='20' rx='10' fill='{NAVY2}'/>
      </svg>"""
    lab = (f"<div style='font-size:{fs}px;font-weight:900;color:{tone or NAVY};text-align:center;line-height:1.2;max-width:{w}px'>{label}</div>"
           if label else "")
    return f"<div style='display:flex;flex-direction:column;align-items:center;gap:6px'>{svg}{lab}</div>"


def scene(sc):
    kind = sc["kind"]
    if kind == "one":
        return pot(sc.get("stage", 0), sc.get("soil", "dry"), 740, sc.get("label"))
    if kind == "two":
        return (f"<div style='display:flex;gap:20px;align-items:flex-end'>"
                f"{pot(0, 'dry', 480, 'קהל שהעסק לא בשבילו', '#8A6D3B')}{pot(2, 'rich', 480, 'קהל רלוונטי', GREEN)}</div>")
    if kind == "row":
        pots = "".join(pot(i, 'rich', 205, l, fs=27) for i, l in enumerate(sc["labels"]))
        return f"<div style='display:flex;gap:4px;align-items:flex-end;width:1040px;justify-content:center'>{pots}</div>"
    return ""


def ad_garden(spec):
    slides = spec["slides"]; n = len(slides); out = []
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{NAVY if k <= i else 'rgba(16,27,79,.22)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.gd mark{{color:{NAVY};background:linear-gradient(transparent 60%, {MINT} 60%, {MINT} 92%, transparent 92%)}}</style>"
                f"<div class='gd' style='position:absolute;inset:0;overflow:hidden;background:{BG};color:{NAVY}'>"
                f"<div style='position:absolute;bottom:-300px;right:-240px;width:800px;height:700px;border-radius:50%;background:#FFFFFF;opacity:.55'></div>")
        if s.get("layout") == "end":
            body = wrap + f"""<div style='position:absolute;inset:0;padding:110px 90px;display:flex;flex-direction:column;justify-content:center;gap:40px'>
              <div style='align-self:flex-start'>{logo_tile(200, 30)}</div>
              <h2 style='font-size:{s.get('size', 60)}px;line-height:1.2;color:{NAVY}'>{s['head']}</h2>
              <p style='font-size:36px;color:{NAVY2};font-weight:700'>{s.get('body', '')}</p>
              <div><div style='display:inline-block;background:{MINT};color:{NAVY3};font-weight:800;font-size:40px;padding:24px 44px;border-radius:999px'>{s['cta']}</div></div>
              <div>{pill(s['tag'], NAVY2, NAVY2) if s.get('tag') else ''}</div></div></div>"""
        else:
            stamp = (f"<div style='position:absolute;right:110px;bottom:{s.get('stamp_bottom', 560)}px;transform:rotate(7deg);border:6px solid {MINT};"
                     f"color:{GREEN};border-radius:18px;padding:8px 26px;font-size:40px;font-weight:900;background:rgba(255,255,255,.92)'>{s['stamp']}</div>"
                     if s.get("stamp") else "")
            body = wrap + f"""<div style='position:absolute;top:56px;left:80px;right:80px;display:flex;gap:10px'>{dots}</div>
            <div style='position:absolute;top:112px;right:80px;left:80px;display:flex;flex-direction:column;gap:14px'>
              {f"<div style='font-size:32px;font-weight:900;color:{NAVY}'>{s['kicker']}</div>" if s.get('kicker') else ''}
              <h2 style='font-size:{s.get('size', 62)}px;line-height:1.12;color:{NAVY}'>{s['head']}</h2>
              {f"<p style='font-size:33px;color:{NAVY2};line-height:1.4;font-weight:700'>{s['body']}</p>" if s.get('body') else ''}</div>
            <div style='position:absolute;bottom:{s.get('scene_bottom', 280)}px;left:0;right:0;display:flex;justify-content:center'>{scene(s['scene'])}</div>{stamp}
            <div style='position:absolute;bottom:40px;right:80px;left:80px;display:flex;justify-content:space-between;align-items:center'>{logo_tile(58, 12)}
              <span style='font-size:24px;color:{NAVY2};font-weight:700'>{s.get('note', spec.get('note', 'המחשה'))}</span></div></div>"""
        out.append(body)
    return out
