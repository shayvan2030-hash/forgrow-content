"""Builds the private review page (index.html) of the "ForGrow daily ads" artifact from content_log.csv.

Usage: python3 pipeline/gallery.py <site_dir>
<site_dir> must contain content_log.csv and the published media under days/<date>/<slug>/.
content_log.csv columns used: id,date,format,hook,status,files,caption,music_suggestion,angle
  files = semicolon-separated paths relative to <site_dir> (jpg/mp4)
Writes <site_dir>/index.html (no <html>/<head>/<body>: the Artifact tool wraps it).
"""
import csv, html, pathlib, sys

STATUS = {"ready_for_approval": ("מוכן — ממתין לאישורך", "ok"), "approved": ("אושר", "ok"),
          "published": ("פורסם", "ok"), "paused": ("מושהה", "info"), "rejected": ("נדחה", "warn")}

CSS = """
:root{--bg:#F2F3FA;--surface:#FFFFFF;--ink:#0B1238;--muted:#4D5680;--line:#DADDF0;--accent:#0C9A78;--ok:#DDF5EE;--warnbg:#FBEFD9;--warn:#9A5B06}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#0A1238;--surface:#121D52;--ink:#F2F4FF;--muted:#AEB6E0;--line:#26336F;--accent:#14D8A5;--ok:#0F3A3A;--warnbg:#3A2A10;--warn:#F2B661;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#0A1238;--surface:#121D52;--ink:#F2F4FF;--muted:#AEB6E0;--line:#26336F;--accent:#14D8A5;--ok:#0F3A3A;--warnbg:#3A2A10;--warn:#F2B661;color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font-family:"Heebo",system-ui,sans-serif;direction:rtl;margin:0;line-height:1.6}
.wrap{max-width:1040px;margin:0 auto;padding-block:28px 60px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:flex;flex-direction:column;gap:32px}
h1{font-weight:900;font-size:clamp(26px,5vw,38px);margin:0}
.lead{color:var(--muted);margin:0;max-width:66ch}
section{border-top:2px solid var(--line);padding-top:20px;display:flex;flex-direction:column;gap:12px}
.head{display:flex;flex-wrap:wrap;justify-content:space-between;gap:8px;align-items:baseline}
h2{font-size:21px;margin:0;font-weight:800}
.meta{color:var(--muted);font-size:14px}
.pill{border-radius:999px;padding:2px 12px;font-size:13px;font-weight:700;white-space:nowrap}
.pill.ok{background:var(--ok);color:var(--accent)}.pill.info{border:1px solid var(--line);color:var(--muted)}.pill.warn{background:var(--warnbg);color:var(--warn)}
.rail{display:flex;gap:10px;overflow-x:auto;padding-bottom:6px}
.rail img,.rail video{flex:none;width:min(300px,72vw);height:auto;border-radius:10px;border:1px solid var(--line)}
details{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:10px 14px}
summary{cursor:pointer;font-weight:700}
pre{white-space:pre-wrap;font-family:inherit;margin:8px 0 0}
.song{font-size:14px;color:var(--muted)}
"""


def build(site):
    site = pathlib.Path(site)
    rows = list(csv.DictReader((site / "content_log.csv").open(encoding="utf-8")))
    rows = [r for r in rows if r.get("files")]
    rows.sort(key=lambda r: (r.get("date", ""), r.get("id", "")), reverse=True)
    parts = ['<title>מודעות ForGrow</title>',
             '<meta name="claude:viewport-fit-sides" content="cover">',
             '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;700;800;900&display=swap">',
             f"<style>{CSS}</style>", '<div class="wrap">',
             '<header><h1>מודעות ForGrow</h1><p class="lead">מודעה חדשה בכל יום, מוכנה לבדיקה. '
             'שום דבר כאן לא פורסם ולא תוזמן. השיר מתווסף באפליקציית אינסטגרם בזמן הפרסום.</p></header>']
    for r in rows:
        label, cls = STATUS.get(r.get("status", ""), (r.get("status", ""), "info"))
        media = []
        for f in [x for x in r["files"].split(";") if x]:
            src = html.escape(f)
            if f.endswith(".mp4"):
                media.append(f'<video controls playsinline preload="metadata" src="{src}"></video>')
            else:
                media.append(f'<img src="{src}" alt="" loading="lazy">')
        song = f'<div class="song">שיר מוצע: {html.escape(r["music_suggestion"])}</div>' if r.get("music_suggestion") else ""
        cap = f'<details><summary>כיתוב והנעה לפעולה</summary><pre>{html.escape(r.get("caption", ""))}</pre></details>' if r.get("caption") else ""
        parts.append(f'<section><div class="head"><h2>{html.escape(r.get("hook", ""))}</h2>'
                     f'<span class="pill {cls}">{html.escape(label)}</span></div>'
                     f'<div class="meta">{html.escape(r.get("date", ""))} · {html.escape(r.get("format", ""))}'
                     f'{" · " + html.escape(r["angle"]) if r.get("angle") else ""}</div>'
                     f'<div class="rail">{"".join(media)}</div>{song}{cap}</section>')
    parts.append("</div>")
    (site / "index.html").write_text("\n".join(parts), encoding="utf-8")
    print(f"index.html: {len(rows)} ads")


if __name__ == "__main__":
    build(sys.argv[1])
