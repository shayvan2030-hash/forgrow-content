"""Extra ad layouts, set 31 (added 2026-11-24).

ad_boxes — carousel on a kraft-cardboard background with faint corrugated stripes: moving boxes.
          Business problem: the business moved on (it started as a hobby, a previous field or a personal page), but
          most followers arrived in the earlier stage. They know the owner and are supportive, yet what the business
          offers today is less relevant to them, so new content has nobody to connect with. A relevant audience for
          today's business can start a route (discover -> follow -> keep seeing -> understand the offer -> maybe reach
          out), shown as a stack of five numbered boxes being unpacked. Illustration only. Original logo on a navy tile.
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3
from ads_extra28 import label, person, tag

MINT = T["acc"]
MINT_L = "#B5F1DF"
INK = "#101B4F"
MINT_D = "#0B7F62"
SUB = "#33407F"
GREY = "#D3D5DE"
GREY_D = "#6E7390"
BG = "#EEDDC2"
STRIPE = "#E2CCA8"
BOX = "#C99A62"
BOX_S = "#A97B47"
BOX_T = "#DDB680"
INSIDE = "#6E4C27"
TAPE = "#F1D9A8"
OLD = "#D9CDBB"
OLD_S = "#BDB09C"
OLD_T = "#E8DFD1"


def box(cx, by, w, h, txt=None, open_=False, tape=TAPE, old=False, fs=None, op=1, txtc=INK):
    """Cardboard box in 3/4 view: front face centred on cx, bottom at by. Old boxes are faded."""
    f, s, t = (OLD, OLD_S, OLD_T) if old else (BOX, BOX_S, BOX_T)
    x, y = cx - w / 2, by - h
    d, e = w * .22, w * .13
    g = f"<g opacity='{op}' stroke='{INK}' stroke-width='4' stroke-linejoin='round'>"
    g += f"<path d='M {x + w:.1f},{y:.1f} L {x + w + d:.1f},{y - e:.1f} L {x + w + d:.1f},{by - e:.1f} L {x + w:.1f},{by:.1f} Z' fill='{s}'/>"
    if open_:
        g += f"<path d='M {x:.1f},{y:.1f} L {x + d:.1f},{y - e:.1f} L {x + w + d:.1f},{y - e:.1f} L {x + w:.1f},{y:.1f} Z' fill='{INSIDE}'/>"
        fl = h * .42
        g += (f"<path d='M {x + d:.1f},{y - e:.1f} L {x + w + d:.1f},{y - e:.1f} L {x + w + d * .7:.1f},{y - e - fl * .8:.1f} "
              f"L {x + d * .7:.1f},{y - e - fl * .8:.1f} Z' fill='{t}'/>")
        g += f"<path d='M {x:.1f},{y:.1f} L {x + d:.1f},{y - e:.1f} L {x + d - w * .2:.1f},{y - e - fl * .55:.1f} L {x - w * .2:.1f},{y - fl * .55:.1f} Z' fill='{t}'/>"
        g += f"<path d='M {x + w:.1f},{y:.1f} L {x + w + d:.1f},{y - e:.1f} L {x + w + d + w * .2:.1f},{y - e - fl * .55:.1f} L {x + w + w * .2:.1f},{y - fl * .55:.1f} Z' fill='{t}'/>"
    else:
        g += f"<path d='M {x:.1f},{y:.1f} L {x + d:.1f},{y - e:.1f} L {x + w + d:.1f},{y - e:.1f} L {x + w:.1f},{y:.1f} Z' fill='{t}'/>"
        tw = w * .16
        g += (f"<path d='M {cx - tw / 2:.1f},{y:.1f} L {cx - tw / 2 + d:.1f},{y - e:.1f} L {cx + tw / 2 + d:.1f},{y - e:.1f} "
              f"L {cx + tw / 2:.1f},{y:.1f} Z' fill='{tape}' stroke-width='3'/>")
    g += f"<rect x='{x:.1f}' y='{y:.1f}' width='{w:.1f}' height='{h:.1f}' fill='{f}'/>"
    if not open_:
        tw = w * .16
        g += f"<rect x='{cx - tw / 2:.1f}' y='{y:.1f}' width='{tw:.1f}' height='{h * .3:.1f}' fill='{tape}' stroke-width='3'/>"
    g += "</g>"
    if txt:
        fs = fs or min(40, w * .14)
        lw = min(w * .82, len(txt) * fs * .56 + 36)
        ly = y + h * (.62 if not open_ else .5)
        g += (f"<rect x='{cx - lw / 2:.1f}' y='{ly - fs * .95:.1f}' width='{lw:.1f}' height='{fs * 1.6:.1f}' rx='8' fill='#FFFFFF' "
              f"stroke='{INK}' stroke-width='3' opacity='{op}'/>" + label(cx, ly + fs * .28, txt, txtc, fs))
    return g


def heart(cx, cy, s=1.0, fill="#FFFFFF", stroke=GREY_D):
    return (f"<path transform='translate({cx:.1f} {cy:.1f}) scale({s:.2f})' d='M 0,14 C -26,-4 -20,-26 -6,-24 C 0,-23 0,-18 0,-16 "
            f"C 0,-18 0,-23 6,-24 C 20,-26 26,-4 0,14 Z' fill='{fill}' stroke='{stroke}' stroke-width='3.5' stroke-linejoin='round'/>")


def qbubble(cx, cy, r=40, color=GREY_D):
    return f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='#FFFFFF' stroke='{color}' stroke-width='4'/>" + label(cx, cy + r * .38, "?", color, r * 1.15)


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='660' viewBox='0 0 {w} 660'>"
        g += f"<ellipse cx='470' cy='630' rx='380' ry='22' fill='{INK}' opacity='.08'/>"
        g += box(640, 630, 300, 200, "פעם", old=True, fs=40)
        g += box(330, 630, 300, 200, "תחביב", old=True, fs=40)
        g += box(500, 430, 330, 230, "העסק היום", open_=True, tape=MINT, fs=40)
        g += qbubble(200, 130, 46)
        g += tag(640, 60, "למי זה מגיע עכשיו?", "#FFFFFF", SUB, 30)
        return g + "</svg>"
    if k == "away":
        g = f"<svg width='{w}' height='660' viewBox='0 0 {w} 660'>"
        g += f"<ellipse cx='470' cy='620' rx='420' ry='22' fill='{INK}' opacity='.08'/>"
        g += box(160, 610, 210, 150, "העסק היום", open_=True, tape=MINT, fs=28)
        g += qbubble(150, 330, 40)
        g += box(450, 610, 230, 180, "פעם", old=True, fs=40)
        for x, by, h, op in ((680, 615, 124, .95), (780, 590, 112, .8), (875, 615, 124, .7)):
            g += person(x, by, h, GREY, op=op, dash=True)
            g += heart(x, by - h - 38, 1.1)
        g += tag(700, 180, "מכירים אתכם מפעם", "#FFFFFF", GREY_D, 30)
        g += tag(660, 260, "פחות צריכים את מה שיש היום", "#FFFFFF", GREY_D, 28)
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='800' viewBox='0 0 {w} 800'>"
        g += f"<line x1='470' y1='20' x2='470' y2='640' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        # right (read first): old box, grey followers from back then
        g += box(705, 560, 250, 180, "פעם", old=True, fs=38)
        for x, by, h, op in ((625, 372, 92, 1), (715, 372, 92, 1), (805, 372, 92, 1)):
            g += person(x, by, h, GREY, op=op, dash=True)
            g += heart(x, by - h - 34, 1.0)
        g += label(705, 700, "קהל מהתקופה הקודמת", INK, 34) + label(705, 746, "מפרגנים, פחות צריכים", SUB, 27)
        # left: open box of today's business, mint people close by
        g += box(230, 560, 250, 180, "היום", open_=True, tape=MINT, fs=38)
        for x, by, h, f in ((150, 372, 96, MINT), (235, 350, 104, MINT_L), (320, 372, 96, MINT)):
            g += person(x, by, h, f)
        g += label(235, 700, "קהל של העסק היום", MINT_D, 34) + label(235, 746, "אנשים שאולי צריכים אתכם", SUB, 27)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; n = len(labels); rows = ""
        for i, l in enumerate(labels):
            last = i == n - 1
            fill = "#FFFFFF" if last else (MINT if i % 2 == 0 else MINT_L)
            b = (f"<div style='width:84px;height:68px;flex:none;border:4px {'dashed' if last else 'solid'} {MINT_D if last else INK};"
                 f"border-radius:8px;background:{BOX};position:relative;display:flex;align-items:center;justify-content:center'>"
                 f"<div style='position:absolute;top:0;left:30px;width:16px;height:12px;background:{fill};border-left:3px solid {INK};border-right:3px solid {INK}'></div>"
                 f"<div style='background:#FFFFFF;border:3px solid {INK};border-radius:6px;font-size:30px;font-weight:900;line-height:1;padding:3px 10px;margin-top:14px'>{i + 1}</div></div>")
            rows += (f"<div style='display:flex;align-items:center;gap:26px;padding:8px 0'>{b}"
                     f"<span style='font-size:42px;font-weight:900;color:{SUB if last else INK}'>{l}</span></div>")
        return (f"<div style='width:840px;background:#FFFFFF;border:6px solid {INK};border-radius:20px;overflow:hidden;"
                f"box-shadow:12px 14px 0 rgba(16,27,79,.14)'>"
                f"<div style='background:{NAVY};color:#fff;font-size:32px;font-weight:900;padding:18px 34px;display:flex;align-items:center;gap:18px'>"
                f"<span style='width:18px;height:18px;border-radius:50%;background:{MINT};flex:none'></span>ארגז אחרי ארגז</div>"
                f"<div style='padding:14px 40px 20px 40px;display:flex;flex-direction:column'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='600' viewBox='0 0 {w} 600'>"
        g += f"<ellipse cx='470' cy='560' rx='360' ry='20' fill='{INK}' opacity='.08'/>"
        g += box(470, 560, 300, 200, "העסק היום", open_=True, tape=MINT, fs=38)
        for x, by, h, f in ((120, 560, 124, MINT), (225, 560, 104, MINT_L), (785, 560, 104, MINT), (880, 560, 124, MINT_L)):
            g += person(x, by, h, f)
        return g + "</svg>"
    return ""


def stripes(end=False):
    lines = "".join(f"<rect x='{x}' y='0' width='10' height='1350' fill='{STRIPE}'/>" for x in range(14, 1080, 36))
    return (f"<svg width='1080' height='1350' viewBox='0 0 1080 1350' style='position:absolute;inset:0;opacity:{.35 if end else .55}'>"
            f"{lines}</svg>")


def ad_boxes(spec):
    slides = spec["slides"]; n = len(slides); out = []
    bg = f"background:{BG}"
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT_D if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        end = s.get("layout") == "end"
        wrap = (f"<style>.bg mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='bg' style='position:absolute;inset:0;overflow:hidden;color:{INK};{bg}'>{stripes(end)}")
        tl = f"<div style='background:{NAVY};border-radius:22px;padding:14px 22px;display:inline-flex'>{logo(52)}</div>"
        if end:
            body = wrap + f"""<div style='position:absolute;inset:0;padding:110px 90px;display:flex;flex-direction:column;justify-content:center;gap:40px'>
              <div style='background:{NAVY};border-radius:30px;padding:24px 34px;align-self:flex-start;display:flex'>{logo(110)}</div>
              <h2 style='font-size:{s.get('size', 60)}px;line-height:1.2'>{s['head']}</h2>
              <p style='font-size:36px;color:{SUB};font-weight:700'>{s.get('body', '')}</p>
              <div><div style='display:inline-block;background:{MINT};color:{NAVY3};font-weight:800;font-size:40px;padding:24px 44px;border-radius:999px;box-shadow:0 6px 0 {INK}'>{s['cta']}</div></div>
              <div><span style='display:inline-block;font-size:26px;font-weight:700;padding:8px 20px;border-radius:999px;border:2px solid {SUB};color:{SUB};background:#FFFFFF'>{s.get('tag', '')}</span></div></div></div>"""
        else:
            st = (f"<div style='position:absolute;left:96px;bottom:{s.get('stamp_bottom', 640)}px;transform:rotate(4deg);background:{NAVY};"
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
