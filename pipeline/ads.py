"""Ad creatives with custom illustrations (built on render.py's brand, fonts and logo).

Usage: python3 pipeline/ads.py content/<date>/<slug>/spec.json
Supported spec types: "ad_local_map" (single 1080x1350 image), "ad_journey" (carousel, phone illustrations),
"ad_storefront" (single image, light background), "ad_calendar" (carousel, wall-calendar pages),
"ad_shape_video" (1080x1920 MP4, frame-by-frame shape-sorter animation) — the last three live in ads_extra.py;
"ad_scale" (image), "ad_signpost" (carousel), "ad_spotlight" (video) live in ads_extra2.py;
"ad_checklist" (carousel, clipboard self-check) lives in ads_extra3.py; "ad_theater" (carousel, theatre hall) in ads_extra4.py.
"""
import asyncio, base64, json, math, pathlib, random, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from playwright.async_api import async_playwright
from render import THEME as T, html, logo, shoot

W, H = 1080, 1350


def cta_button(text):
    return (f"<div style='display:inline-block;background:{T['acc']};color:{T['bg3']};font-weight:800;"
            f"font-size:38px;padding:22px 40px;border-radius:999px'>{text}</div>")


def tag(text):
    return (f"<span style='display:inline-block;font-size:26px;font-weight:700;padding:8px 20px;border-radius:999px;"
            f"border:2px solid {T['line']};color:{T['sub']}'>{text}</span>")


def top_bar(right_tag=None):
    return (f"<div style='position:absolute;top:64px;right:80px;left:80px;display:flex;justify-content:space-between;"
            f"align-items:flex-start'>{logo(118)}{tag(right_tag) if right_tag else ''}</div>")


# ---------------- Ad 1: local map ----------------
def map_svg(seed=4):
    rnd = random.Random(seed)
    w, h = 920, 420; cx, cy, r = 460, 210, 150
    streets = "".join(f"<line x1='{x}' y1='0' x2='{x + rnd.randint(-60, 60)}' y2='{h}' stroke='{T['line']}' stroke-width='2'/>"
                      for x in range(40, w, 92))
    streets += "".join(f"<line x1='0' y1='{y}' x2='{w}' y2='{y + rnd.randint(-40, 40)}' stroke='{T['line']}' stroke-width='2'/>"
                       for y in range(30, h, 84))
    inside, outside = [], []
    while len(inside) < 16:
        a = rnd.random() * 2 * math.pi; d = r * math.sqrt(rnd.random()) * 0.9
        if d > 46:
            inside.append((cx + d * math.cos(a), cy + d * math.sin(a)))
    while len(outside) < 70:
        x, y = rnd.uniform(14, w - 14), rnd.uniform(14, h - 14)
        if math.hypot(x - cx, y - cy) > r + 26:
            outside.append((x, y))
    dots = "".join(f"<circle cx='{x:.0f}' cy='{y:.0f}' r='9' fill='{T['peri']}' opacity='0.45'/>" for x, y in outside)
    dots += "".join(f"<circle cx='{x:.0f}' cy='{y:.0f}' r='12' fill='{T['acc']}'/>" for x, y in inside)
    icon = base64.b64encode((pathlib.Path(__file__).resolve().parents[1] / "brand" / "logo_icon.png").read_bytes()).decode()
    pin = f"<image href='data:image/png;base64,{icon}' x='{cx - 40}' y='{cy - 40}' width='80' height='80'/>"
    ring = (f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='{T['acc']}' fill-opacity='0.08' stroke='{T['acc']}' "
            f"stroke-width='3' stroke-dasharray='14 10'/>")
    return (f"<svg width='{w}' height='{h}' viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg'>"
            f"<rect width='{w}' height='{h}' rx='28' fill='rgba(255,255,255,0.03)'/>{streets}{ring}{dots}{pin}</svg>")


def ad_local_map(spec):
    s = spec["image"]
    legend = (f"<div style='display:flex;gap:36px;font-size:28px;color:{T['sub']}'>"
              f"<span><span style='display:inline-block;width:20px;height:20px;border-radius:50%;background:{T['acc']};margin-left:10px'></span>{s['legend_in']}</span>"
              f"<span><span style='display:inline-block;width:18px;height:18px;border-radius:50%;background:{T['peri']};opacity:.5;margin-left:10px'></span>{s['legend_out']}</span></div>")
    body = f"""{top_bar(s.get('tag'))}
    <div style='position:absolute;top:220px;right:80px;left:80px;display:flex;flex-direction:column;gap:22px'>
      <h1 style='font-size:70px;line-height:1.1'>{s['head']}</h1>
      <div style='display:flex;flex-direction:column;gap:14px;align-items:center'>{map_svg()}{legend}
        <div style='font-size:22px;color:{T['sub']};align-self:flex-start'>המחשה</div></div>
      <p style='font-size:36px;color:{T['ink']};line-height:1.4'>{s['value']}</p>
      <div>{cta_button(s['cta'])}</div>
    </div>"""
    return [body]


# ---------------- Ad 2: journey carousel ----------------
def phone(inner):
    return (f"<div style='width:430px;height:780px;border-radius:56px;background:#0B1238;border:10px solid #2A3A86;"
            f"box-shadow:0 30px 80px rgba(0,0,0,.35);padding:30px 22px;display:flex;flex-direction:column;gap:16px;overflow:hidden'>"
            f"<div style='align-self:center;width:120px;height:10px;border-radius:5px;background:#2A3A86'></div>{inner}</div>")


def tile(color, label="", h=170):
    return (f"<div style='height:{h}px;border-radius:18px;background:{color};display:flex;align-items:flex-end;"
            f"padding:14px;font-size:22px;font-weight:700;color:#0B1238'>{label}</div>")


SCREENS = {
    "explore": lambda: phone(
        "<div style='display:grid;grid-template-columns:repeat(3,1fr);gap:8px'>" +
        "".join(tile('#22306E', h=120) for _ in range(4)) + tile(T['acc'], 'פילאטיס', 120) +
        "".join(tile('#22306E', h=120) for _ in range(7)) + "</div>"),
    "post": lambda: phone(
        f"<div style='display:flex;gap:12px;align-items:center'><div style='width:54px;height:54px;border-radius:50%;background:{T['acc']}'></div>"
        f"<div style='font-size:24px;font-weight:700;color:#fff'>סטודיו פילאטיס · דוגמה</div></div>"
        + tile('#C5CBEE', 'שיעור ניסיון לנשים אחרי לידה', 430) +
        f"<div style='font-size:22px;color:{T['sub']}'>♡ 💬 ↗</div>"),
    "follow": lambda: phone(
        f"<div style='display:flex;gap:16px;align-items:center'><div style='width:96px;height:96px;border-radius:50%;background:{T['acc']}'></div>"
        f"<div style='font-size:26px;font-weight:800;color:#fff'>סטודיו פילאטיס<br><span style='font-weight:400;color:{T['sub']};font-size:22px'>דוגמה · הרצליה</span></div></div>"
        f"<div style='background:#2A3A86;color:#fff;text-align:center;border-radius:14px;padding:14px;font-size:26px;font-weight:800'>עוקבת ✓</div>"
        "<div style='display:grid;grid-template-columns:repeat(3,1fr);gap:8px'>" +
        "".join(tile(c, h=120) for c in ('#8799DB', '#C5CBEE', '#22306E', '#22306E', '#8799DB', '#22306E')) + "</div>"),
    "offer": lambda: phone(
        "<div style='display:flex;flex-direction:column;gap:12px'>" +
        tile('#C5CBEE', 'מה מקבלים בשיעור ניסיון', 170) + tile('#8799DB', 'למי זה מתאים', 170) +
        tile(T['acc'], 'לו״ז קבוצות בוקר', 170) + "</div>"),
    "contact": lambda: phone(
        f"<div style='flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:28px'>"
        f"<div style='width:190px;height:190px;border-radius:50%;background:{T['acc']};display:flex;align-items:center;justify-content:center;font-size:96px'>✉</div>"
        f"<div style='font-size:34px;font-weight:800;color:#fff'>פנייה חדשה</div>"
        f"<div style='font-size:24px;color:{T['sub']};text-align:center'>שאלה על שיעור ניסיון</div></div>"),
}


def ad_journey(spec):
    slides = spec["slides"]; n = len(slides); out = []
    for i, s in enumerate(slides):
        dots = "".join(f"<i style='flex:1;height:6px;border-radius:3px;background:{T['acc'] if k <= i else T['line']}'></i>"
                       for k in range(n))
        if s.get("layout") == "end":
            body = f"""<div style='position:absolute;inset:0;padding:110px 90px;display:flex;flex-direction:column;justify-content:center;gap:40px'>
              {logo(300)}
              <h2 style='font-size:62px;line-height:1.2'>{s['head']}</h2>
              <p style='font-size:36px;color:{T['sub']}'>{s.get('body', '')}</p>
              <div>{cta_button(s['cta'])}</div><div>{tag(s['tag']) if s.get('tag') else ''}</div></div>"""
        else:
            body = f"""<div style='position:absolute;top:56px;left:80px;right:80px;display:flex;gap:10px'>{dots}</div>
            <div style='position:absolute;inset:0;padding:120px 80px 90px;display:flex;gap:44px;align-items:center'>
              <div style='flex:1;display:flex;flex-direction:column;gap:24px;min-width:0'>
                {f"<div style='font-size:32px;font-weight:900;color:{T['acc']}'>{s['kicker']}</div>" if s.get('kicker') else ''}
                <h2 style='font-size:{s.get('size', 64)}px;line-height:1.15'>{s['head']}</h2>
                <p style='font-size:34px;color:{T['sub']};line-height:1.45'>{s.get('body', '')}</p>
                {f"<div style='font-size:22px;color:{T['sub']}'>{s['note']}</div>" if s.get('note') else ''}
              </div>
              <div style='flex:none'>{SCREENS[s['screen']]()}</div>
            </div>
            <div style='position:absolute;bottom:48px;right:80px'>{logo(96)}</div>"""
        out.append(body)
    return out


from ads_extra import ad_storefront, ad_calendar, ad_shape_video  # noqa: E402  (2026-10-28 layouts)

KINDS = {"ad_local_map": ad_local_map, "ad_journey": ad_journey, "ad_storefront": ad_storefront, "ad_calendar": ad_calendar}
from ads_extra2 import ad_scale, ad_signpost, ad_spotlight  # noqa: E402  (2026-10-28, run 2)

KINDS.update({"ad_scale": ad_scale, "ad_signpost": ad_signpost})
from ads_extra3 import ad_checklist  # noqa: E402  (2026-10-29)

KINDS["ad_checklist"] = ad_checklist
from ads_extra4 import ad_theater  # noqa: E402  (2026-10-29, run 2)

KINDS["ad_theater"] = ad_theater
from ads_extra5 import ad_receipt  # noqa: E402  (2026-10-29, run 3)

KINDS["ad_receipt"] = ad_receipt
from ads_extra6 import ad_radio  # noqa: E402  (2026-10-30)

KINDS["ad_radio"] = ad_radio
VIDEO_KINDS = {"ad_shape_video": ad_shape_video, "ad_spotlight": ad_spotlight}


async def main(spec_path):
    spec_path = pathlib.Path(spec_path).resolve()
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    out = spec_path.parent / "out"; out.mkdir(exist_ok=True)
    if spec["type"] in VIDEO_KINDS:
        await VIDEO_KINDS[spec["type"]](spec, out)
        print("rendered", spec["id"]); return
    bodies = KINDS[spec["type"]](spec)
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page()
        for i, body in enumerate(bodies):
            name = "image.jpg" if len(bodies) == 1 else f"slide_{i + 1:02d}.jpg"
            await shoot(pg, body, out / name, W, H)
        await b.close()
    for f in out.glob("*.png"):
        f.unlink()
    print("rendered", spec["id"])


if __name__ == "__main__":
    for a in sys.argv[1:]:
        asyncio.run(main(a))
