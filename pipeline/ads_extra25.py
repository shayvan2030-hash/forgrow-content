"""Extra ad layouts, set 25 (added 2026-11-19).

ad_tickets — carousel on a warm cream background with a terracotta checkered floor: a "take a number" queue
          ticket dispenser. Business problem: the owner spends evenings answering messages, and many of them come
          from people who are not the business's audience at all (far away, looking for something else, just
          curious) — the queue never ends and most numbers are the wrong people. A relevant audience that
          discovered the business and kept seeing its content already understands the offer before it reaches out
          (discover -> follow -> keep seeing -> understand the offer -> maybe reach out).
          Route shown as five numbered paper tickets. Illustration only. Original logo on a navy tile.
"""
from render import THEME as T, logo
from ads_extra import NAVY, NAVY3

MINT = T["acc"]
MINT_L = "#B5F1DF"
INK = "#101B4F"
MINT_D = "#0B7F62"
GREY = "#D9DBE4"
GREY_D = "#6E7390"
SUB = "#33407F"
RED = "#E2574C"
RED_D = "#B63C33"
TILE = "#E9B79A"


def label(x, y, txt, fill, size=34):
    return (f"<text x='{x}' y='{y}' font-family='Heebo' font-weight='900' font-size='{size}' text-anchor='middle' "
            f"fill='{fill}' direction='rtl'>{txt}</text>")


def ticket_path(x, y, w, h):
    r = h * 0.16; m = y + h / 2
    return (f"M {x:.1f},{y:.1f} H {x + w:.1f} V {m - r:.1f} A {r:.1f} {r:.1f} 0 0 0 {x + w:.1f},{m + r:.1f} "
            f"V {y + h:.1f} H {x:.1f} V {m + r:.1f} A {r:.1f} {r:.1f} 0 0 0 {x:.1f},{m - r:.1f} Z")


def ticket(cx, cy, w, h, fill=GREY, txt="?", txt_fill=GREY_D, rot=0, stroke=INK, op=1, dash=False):
    x, y = cx - w / 2, cy - h / 2
    d = " stroke-dasharray='10 7'" if dash else ""
    return (f"<g opacity='{op}' transform='rotate({rot} {cx:.1f} {cy:.1f})'>"
            f"<path d='{ticket_path(x, y, w, h)}' fill='{fill}' stroke='{stroke}' stroke-width='4' stroke-linejoin='round'{d}/>"
            f"<line x1='{x + w * .22:.1f}' y1='{y + 8:.1f}' x2='{x + w * .22:.1f}' y2='{y + h - 8:.1f}' stroke='{stroke}' stroke-width='2' stroke-dasharray='5 6' opacity='.45'/>"
            f"<text x='{cx + w * .1:.1f}' y='{cy + h * .2:.1f}' font-family='Heebo' font-weight='900' font-size='{h * .55:.1f}' "
            f"text-anchor='middle' fill='{txt_fill}'>{txt}</text></g>")


def dispenser(cx, top, h, shown="?", disp_fill=INK, disp_txt=RED, body=RED, body_d=RED_D):
    """Ticket dispenser on a pole. (cx, top) = top of the number display; h = total height to the floor."""
    r = h * 0.17
    hy = top + h * 0.30
    g = f"<ellipse cx='{cx}' cy='{top + h:.1f}' rx='{r * 1.1:.1f}' ry='{r * .22:.1f}' fill='{INK}' opacity='.18'/>"
    g += f"<rect x='{cx - r * .12:.1f}' y='{hy:.1f}' width='{r * .24:.1f}' height='{h * .70:.1f}' rx='6' fill='#A9AEC4' stroke='{INK}' stroke-width='4'/>"
    g += f"<ellipse cx='{cx}' cy='{top + h:.1f}' rx='{r * .7:.1f}' ry='{r * .16:.1f}' fill='#A9AEC4' stroke='{INK}' stroke-width='4'/>"
    # display board
    dw, dh = r * 1.7, h * 0.13
    g += (f"<rect x='{cx - dw / 2:.1f}' y='{top:.1f}' width='{dw:.1f}' height='{dh:.1f}' rx='12' fill='{disp_fill}' stroke='{INK}' stroke-width='4'/>"
          f"<text x='{cx}' y='{top + dh * .76:.1f}' font-family='Heebo' font-weight='900' font-size='{dh * .78:.1f}' text-anchor='middle' fill='{disp_txt}'>{shown}</text>")
    g += f"<rect x='{cx - r * .1:.1f}' y='{top + dh:.1f}' width='{r * .2:.1f}' height='{hy - top - dh - r + 4:.1f}' fill='#A9AEC4' stroke='{INK}' stroke-width='3'/>"
    # round head with slot
    g += (f"<circle cx='{cx}' cy='{hy:.1f}' r='{r:.1f}' fill='{body}' stroke='{INK}' stroke-width='5'/>"
          f"<circle cx='{cx - r * .3:.1f}' cy='{hy - r * .35:.1f}' r='{r * .22:.1f}' fill='#FFFFFF' opacity='.35'/>"
          f"<rect x='{cx - r * .55:.1f}' y='{hy + r * .25:.1f}' width='{r * 1.1:.1f}' height='{r * .16:.1f}' rx='5' fill='{body_d}' stroke='{INK}' stroke-width='3'/>")
    return g, (cx, hy + r * .33)


def tile_floor(end=False):
    rows, cols, s = 4, 12, 90
    cells = "".join(f"<rect x='{c * s}' y='{r * s}' width='{s}' height='{s}' fill='{TILE}'/>"
                    for r in range(rows) for c in range(cols) if (r + c) % 2 == 0)
    return (f"<svg style='position:absolute;left:0;right:0;bottom:0;opacity:{.35 if end else .5}' width='1080' height='240' viewBox='0 0 1080 360' preserveAspectRatio='none'>"
            f"<rect width='1080' height='360' fill='#F6DCCB'/>{cells}</svg>")


def scene(sc, w=940):
    k = sc["kind"]
    if k == "intro":
        g = f"<svg width='{w}' height='660' viewBox='0 0 {w} 660'>"
        dg, (sx, sy) = dispenser(560, 20, 560)
        # a long strip of grey "?" tickets curls out of the slot down towards the floor
        pts = [(sx - 70, sy + 50, -8), (sx - 150, sy + 120, -18), (sx - 235, sy + 200, -26), (sx - 315, sy + 285, -30),
               (sx - 370, sy + 360, -22)]
        strip = "".join(ticket(x, y, 130, 66, rot=r) for x, y, r in reversed(pts))
        strip = ticket(150, 560, 130, 66, rot=-6) + ticket(300, 572, 130, 66, rot=9) + strip
        g += dg + strip
        for x, y in ((760, 90), (820, 300)):
            g += f"<circle cx='{x}' cy='{y}' r='34' fill='#FFFFFF' stroke='{GREY_D}' stroke-width='4'/>" + label(x, y + 13, "?", GREY_D, 38)
        g += label(560, 652, "עוד ערב של הודעות", SUB, 30)
        return g + "</svg>"
    if k == "split":
        g = f"<svg width='{w}' height='800' viewBox='0 0 {w} 800'>"
        g += f"<line x1='470' y1='20' x2='470' y2='640' stroke='{INK}' stroke-width='3' stroke-dasharray='12 12' opacity='.3'/>"
        # right (read first): grey "?" tickets on an order spike — a queue of people not related to the business
        g += (f"<ellipse cx='705' cy='600' rx='120' ry='16' fill='{INK}' opacity='.15'/>"
              f"<rect x='620' y='570' width='170' height='30' rx='10' fill='#A9AEC4' stroke='{INK}' stroke-width='4'/>"
              f"<line x1='705' y1='570' x2='705' y2='80' stroke='{INK}' stroke-width='6' stroke-linecap='round'/>")
        for dy, r in ((535, -6), (480, 7), (425, -11), (370, 5), (315, -4), (260, 12), (205, -8)):
            g += ticket(705, dy, 190, 70, rot=r)
        g += f"<circle cx='880' cy='130' r='30' fill='#FFFFFF' stroke='{GREY_D}' stroke-width='4'/>" + label(880, 142, "?", GREY_D, 34)
        g += label(705, 690, "קהל לא קשור לעסק", INK, 36) + label(705, 738, "הזמן הולך על הסברים", SUB, 29)
        # left: a few mint numbered tickets — a relevant audience that has seen the content over time
        g += f"<ellipse cx='235' cy='600' rx='170' ry='16' fill='{INK}' opacity='.12'/>"
        for x, y, r, n in ((150, 470, -8, "12"), (320, 455, 6, "13"), (235, 330, -3, "14")):
            g += ticket(x, y, 200, 96, fill=MINT if n != "13" else MINT_L, txt=n, txt_fill=INK, rot=r)
        g += (f"<g transform='translate(235 200)'><circle r='46' fill='{MINT}' stroke='{INK}' stroke-width='4'/>"
              f"<path d='M -20,2 L -5,17 L 22,-14' fill='none' stroke='{INK}' stroke-width='9' stroke-linecap='round' stroke-linejoin='round'/></g>")
        g += label(235, 690, "קהל רלוונטי", MINT_D, 36) + label(235, 738, "ראו תוכן לאורך זמן", SUB, 29)
        return g + "</svg>"
    if k == "route":
        labels = sc["labels"]; n = len(labels); rows = ""
        for i, l in enumerate(labels):
            last = i == n - 1
            fill = "#FFFFFF" if last else (MINT if i % 2 == 0 else MINT_L)
            t = (f"<svg width='150' height='76' viewBox='0 0 150 76' style='flex:none'>"
                 f"{ticket(75, 38, 140, 66, fill=fill, txt=str(i + 1), txt_fill=INK, stroke=MINT_D if last else INK, dash=last)}</svg>")
            rows += (f"<div style='display:flex;align-items:center;gap:26px'>{t}"
                     f"<span style='font-size:42px;font-weight:900;color:{SUB if last else INK}'>{l}</span></div>")
        return (f"<div style='width:840px;background:#FFFFFF;border:6px solid {INK};border-radius:20px;overflow:hidden;"
                f"box-shadow:12px 14px 0 rgba(16,27,79,.14)'>"
                f"<div style='background:{NAVY};color:#fff;font-size:32px;font-weight:900;padding:18px 34px;display:flex;align-items:center;gap:18px'>"
                f"<span style='width:18px;height:18px;border-radius:50%;background:{MINT};flex:none'></span>מספר אחרי מספר, לאורך זמן</div>"
                f"<div style='padding:26px 40px 30px 40px;display:flex;flex-direction:column;gap:12px'>{rows}</div></div>")
    if k == "one":
        g = f"<svg width='{w}' height='620' viewBox='0 0 {w} 620'>"
        dg, (sx, sy) = dispenser(470, 10, 560, shown="✓", disp_txt=MINT, body=MINT, body_d=MINT_D)
        g += dg
        g += ticket(sx - 120, sy + 70, 150, 74, fill=MINT_L, txt="21", txt_fill=INK, rot=-14)
        g += ticket(sx + 125, sy + 60, 150, 74, fill=MINT, txt="22", txt_fill=INK, rot=12)
        return g + "</svg>"
    return ""


def ad_tickets(spec):
    slides = spec["slides"]; n = len(slides); out = []
    bg = "background:#FBF3EA"
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{MINT_D if k <= i else 'rgba(16,27,79,.15)'}'></i>"
                       for k in range(n))
        end = s.get("layout") == "end"
        wrap = (f"<style>.tq mark{{color:{MINT_D};background:none}}</style>"
                f"<div class='tq' style='position:absolute;inset:0;overflow:hidden;color:{INK};{bg}'>{tile_floor(end)}")
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
