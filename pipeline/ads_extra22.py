"""Extra ad layouts, set 22 (added 2026-11-15).

ad_mirror — carousel on a dusty-blue striped wallpaper: a framed oval mirror vs an open window on the same wall.
            Business problem: most of the account's followers are colleagues from the same field — supportive,
            but they don't need the offer. A mirror shows people like you; a window opens onto people who might
            need what you offer (discover -> follow -> keep seeing -> understand the offer -> maybe reach out).
            Route shown as five window panes. Illustration only. Original logo on a navy tile.
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
MINT_L = "#B5F1DF"
BG = "#D7E0EA"
INK = "#101B4F"
MINT_D = "#0B7F62"
GREY = "#B9BECF"
GREY_D = "#6E7390"
SUB = "#33407F"
WOOD = "#B98A5A"
GLASS = "#EEF3F8"
SKY = "#CFEFF7"


def person(cx, by, h, fill, apron=False, stroke=INK, op=1):
    """Simple figure standing on baseline by; h = total height."""
    r = h * 0.17
    hy = by - h + r
    bw = h * 0.52
    g = f"<g opacity='{op}'>"
    g += (f"<path d='M {cx - bw / 2:.1f},{by:.1f} Q {cx - bw / 2:.1f},{hy + r * 1.5:.1f} {cx:.1f},{hy + r * 1.5:.1f} "
          f"Q {cx + bw / 2:.1f},{hy + r * 1.5:.1f} {cx + bw / 2:.1f},{by:.1f} Z' fill='{fill}' stroke='{stroke}' stroke-width='4'/>")
    g += f"<circle cx='{cx:.1f}' cy='{hy:.1f}' r='{r:.1f}' fill='{fill}' stroke='{stroke}' stroke-width='4'/>"
    if apron:
        aw = bw * 0.46
        top = hy + r * 2.1
        g += (f"<rect x='{cx - aw / 2:.1f}' y='{top:.1f}' width='{aw:.1f}' height='{by - top - 4:.1f}' rx='6' "
              f"fill='#FFFFFF' stroke='{stroke}' stroke-width='3'/>")
    return g + "</g>"


def mirror(cx, cy, rw, rh, figs):
    """Oval mirror with a wooden frame; figs = list of (dx, h) colleague reflections."""
    cid = f"m{cx}{cy}"
    g = (f"<defs><clipPath id='{cid}'><ellipse cx='{cx}' cy='{cy}' rx='{rw}' ry='{rh}'/></clipPath></defs>"
         f"<ellipse cx='{cx + 10}' cy='{cy + 14}' rx='{rw + 22}' ry='{rh + 22}' fill='rgba(16,27,79,.14)'/>"
         f"<ellipse cx='{cx}' cy='{cy}' rx='{rw + 22}' ry='{rh + 22}' fill='{WOOD}' stroke='{INK}' stroke-width='5'/>"
         f"<ellipse cx='{cx}' cy='{cy}' rx='{rw}' ry='{rh}' fill='#E4E8F0' stroke='{INK}' stroke-width='4'/>"
         f"<g clip-path='url(#{cid})'>")
    for dx, h in figs:
        g += person(cx + dx, cy + rh + 10, h, GREY, apron=True, stroke=GREY_D)
    g += (f"<path d='M {cx - rw * 0.55},{cy - rh * 0.35} L {cx - rw * 0.15},{cy - rh * 0.75}' stroke='#fff' stroke-width='14' "
          f"stroke-linecap='round' opacity='.7'/>"
          f"<path d='M {cx - rw * 0.55},{cy - rh * 0.05} L {cx - rw * 0.32},{cy - rh * 0.28}' stroke='#fff' stroke-width='8' "
          f"stroke-linecap='round' opacity='.6'/></g>")
    return g


def window(x, y, w, h, figs, open_=False):
    """Window frame with sky outside; figs = list of (dx, height, fill) people outside looking in."""
    cid = f"w{x}{y}"
    g = (f"<defs><clipPath id='{cid}'><rect x='{x}' y='{y}' width='{w}' height='{h}'/></clipPath></defs>"
         f"<rect x='{x - 14 + 10}' y='{y - 14 + 14}' width='{w + 28}' height='{h + 28}' rx='10' fill='rgba(16,27,79,.14)'/>"
         f"<rect x='{x - 14}' y='{y - 14}' width='{w + 28}' height='{h + 28}' rx='10' fill='#FFFFFF' stroke='{INK}' stroke-width='5'/>"
         f"<rect x='{x}' y='{y}' width='{w}' height='{h}' fill='{SKY}' stroke='{INK}' stroke-width='4'/>"
         f"<g clip-path='url(#{cid})'>"
         f"<rect x='{x}' y='{y + h * 0.72}' width='{w}' height='{h}' fill='#BFE6C9'/>")
    for dx, fh, fill in figs:
        g += person(x + dx, y + h + 8, fh, fill)
    g += "</g>"
    if open_:
        # two sashes swung open
        g += (f"<path d='M {x},{y} L {x - w * 0.22},{y + 24} L {x - w * 0.22},{y + h - 24} L {x},{y + h} Z' fill='{GLASS}' "
              f"stroke='{INK}' stroke-width='4' opacity='.95'/>"
              f"<path d='M {x + w},{y} L {x + w * 1.22},{y + 24} L {x + w * 1.22},{y + h - 24} L {x + w},{y + h} Z' fill='{GLASS}' "
              f"stroke='{INK}' stroke-width='4' opacity='.95'/>")
    else:
        g += (f"<line x1='{x + w / 2}' y1='{y}' x2='{x + w / 2}' y2='{y + h}' stroke='#FFFFFF' stroke-width='12'/>"
              f"<line x1='{x + w / 2}' y1='{y}' x2='{x + w / 2}' y2='{y + h}' stroke='{INK}' stroke-width='3'/>"
              f"<line x1='{x}' y1='{y + h * 0.45}' x2='{x + w}' y2='{y + h * 0.45}' stroke='#FFFFFF' stroke-width='12'/>"
              f"<line x1='{x}' y1='{y + h * 0.45}' x2='{x + w}' y2='{y + h * 0.45}' stroke='{INK}' stroke-width='3'/>")
    g += (f"<rect x='{x - 30}' y='{y + h + 14}' width='{w + 60}' height='22' rx='6' fill='#FFFFFF' stroke='{INK}' stroke-width='4'/>")
    return g


def label(x, y, txt, fill, size=34):
    return (f"<text x='{x}' y='{y}' font-family='Heebo' font-weight='900' font-size='{size}' text-anchor='middle' "
            f"fill='{fill}' direction='rtl'>{txt}</text>")


def heart(cx, cy, s, fill):
    return (f"<path d='M {cx},{cy + s * 0.35} C {cx - s},{cy - s * 0.3} {cx - s * 0.45},{cy - s} {cx},{cy - s * 0.45} "
            f"C {cx + s * 0.45},{cy - s} {cx + s},{cy - s * 0.3} {cx},{cy + s * 0.35} Z' fill='{fill}' stroke='{INK}' stroke-width='3'/>")


OUT = [(70, 170, MINT), (165, 205, MINT_L), (265, 150, MINT), (360, 190, MINT_L)]


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='640' viewBox='0 0 {w} 640'>"
        g += mirror(470, 320, 210, 270, [(-128, 290), (128, 290), (0, 330)])
        g += heart(745, 170, 40, "#FFFFFF") + heart(800, 260, 30, "#FFFFFF") + heart(190, 220, 34, "#FFFFFF")
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='760' viewBox='0 0 {w} 760'>"
        # right (read first in RTL): mirror — colleagues from the same field
        g += mirror(705, 300, 150, 215, [(-88, 215), (88, 215), (0, 245)])
        # left: window — people who might need the offer
        g += window(70, 110, 330, 400, [(55, 150, MINT), (135, 185, MINT_L), (215, 140, MINT), (285, 175, MINT_L)])
        g += f"<line x1='470' y1='40' x2='470' y2='590' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        g += label(705, 650, "מראה: קולגות מהתחום", INK, 36) + label(705, 700, "מפרגנים, אבל לא צריכים אתכם", SUB, 29)
        g += label(235, 650, "חלון: קהל רלוונטי", MINT_D, 36) + label(235, 700, "אנשים שאולי צריכים אתכם", SUB, 29)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; rows = ""
        for i, l in enumerate(labels):
            last = i == len(labels) - 1
            pane = (f"<div style='flex:none;width:86px;height:86px;border:5px {'dashed' if last else 'solid'} {MINT_D if last else INK};"
                    f"border-radius:10px;background:{'rgba(255,255,255,.6)' if last else (SKY if i % 2 == 0 else MINT_L)};"
                    f"display:flex;align-items:center;justify-content:center;font-size:44px;font-weight:900;color:{INK}'>{i + 1}</div>")
            rows += (f"<div style='display:flex;align-items:center;gap:26px;padding:7px 0'>{pane}"
                     f"<span style='font-size:42px;font-weight:900;color:{INK if not last else SUB}'>{l}</span></div>")
        return (f"<div style='width:840px;background:#FFFFFF;border:6px solid {INK};border-radius:20px;overflow:hidden;"
                f"box-shadow:12px 14px 0 rgba(16,27,79,.14)'>"
                f"<div style='background:{NAVY};color:#fff;font-size:32px;font-weight:900;padding:16px 34px'>מה שקורה מעבר לחלון</div>"
                f"<div style='padding:14px 30px 18px 30px'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='620' viewBox='0 0 {w} 620'>"
        g += window(300, 70, 340, 420, [(60, 165, MINT), (140, 200, MINT_L), (215, 150, MINT), (290, 185, MINT_L)], open_=True)
        return g + "</svg>"
    return ""


def ad_mirror(spec):
    slides = spec["slides"]; n = len(slides); out = []
    paper = (f"background:{BG};background-image:"
             f"repeating-linear-gradient(90deg, rgba(255,255,255,.28) 0 26px, transparent 26px 80px),"
             f"linear-gradient(180deg, transparent 0 1180px, rgba(16,27,79,.06) 1180px)")
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT_D if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        wrap = (f"<style>.mw mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='mw' style='position:absolute;inset:0;overflow:hidden;color:{INK};{paper}'>")
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
