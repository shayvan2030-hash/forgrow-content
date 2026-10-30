"""Pre-publish quality gate. Exit code 0 = pass, 1 = fail (the item must NOT be scheduled).

Usage: python3 pipeline/qa.py content/<date>/<slug>/spec.json [...]
"""
import json, pathlib, re, subprocess, sys
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1]
LOG = ROOT / "content_log.csv"

# Phrases that need founder approval or are never allowed (see claims_register.md)
BLOCKED = [r"מובטח", r"מבטיח(ים|ה)? (עוקבים|מכירות|תוצאות|לקוחות)", r"ללא סיכון", r"בלי סיכון", r"בלי חסימ", r"ללא חסימ", r"עובד תמיד",
           r"\bMeta\b.*(מאשר|שות)", r"שותף רשמי", r"עוקבים אמיתיים מובטחים", r"\d+\s*עוקבים בחודש",
           r"לקוחות שלנו", r"תוצאות של לקוח", r"ForGrow (מביא|מגדיל|מבטיח|מוסיף)"]
MAX_CAPTION = 2200          # Instagram caption limit
MAX_HASHTAGS = 5            # conservative house rule


def fail(errors, msg):
    errors.append(msg)


def check(spec_path):
    spec_path = pathlib.Path(spec_path).resolve()
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    out = spec_path.parent / "out"
    errors = []
    text = json.dumps(spec, ensure_ascii=False)
    for pat in BLOCKED:
        if re.search(pat, text):
            fail(errors, f"blocked phrase /{pat}/ — needs founder approval")
    cap = spec.get("caption", "")
    if spec["type"] != "story":
        if not cap:
            fail(errors, "missing caption")
        full = cap + "\n\n" + " ".join(spec.get("hashtags", []))
        if len(full) > MAX_CAPTION:
            fail(errors, f"caption too long ({len(full)})")
        if len(spec.get("hashtags", [])) > MAX_HASHTAGS:
            fail(errors, "too many hashtags")
    if spec.get("illustrative") and "דוגמה להמחשה" not in text and spec["type"] == "carousel":
        # beforeafter layout adds the label by default; only flag if overridden away
        if any(s.get("note") == "" for s in spec.get("slides", [])):
            fail(errors, "illustrative example without label")
    if spec["type"] in ("ad_local_map", "ad_storefront", "ad_scale"):
        im = out / "image.jpg"
        if not im.exists() or Image.open(im).size != (1080, 1350): fail(errors, "image.jpg missing or wrong size")
    if spec["type"] in ("carousel", "ad_journey", "ad_calendar", "ad_signpost", "ad_checklist", "ad_theater", "ad_receipt", "ad_radio"):
        imgs = sorted(out.glob("slide_*.jpg"))
        if not 2 <= len(imgs) <= 10:
            fail(errors, f"carousel needs 2–10 slides for API publishing, has {len(imgs)}")
        for im in imgs:
            w, h = Image.open(im).size
            if (w, h) != (1080, 1350): fail(errors, f"{im.name} is {w}x{h}")
            if im.stat().st_size > 8_000_000: fail(errors, f"{im.name} > 8MB")
    elif spec["type"] == "story":
        imgs = sorted(out.glob("frame_*.jpg"))
        if not imgs: fail(errors, "no story frames")
        for im in imgs:
            if Image.open(im).size != (1080, 1920): fail(errors, f"{im.name} wrong size")
    elif spec["type"] in ("reel", "ad_shape_video", "ad_spotlight"):
        mp4 = out / "reel.mp4"
        if not mp4.exists():
            fail(errors, "reel.mp4 missing")
        else:
            probe = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                    "stream=codec_name,width,height:format=duration", "-of", "json", str(mp4)],
                                   capture_output=True, text=True).stdout
            info = json.loads(probe)
            d = float(info["format"]["duration"])
            v = [s for s in info["streams"] if s["codec_name"] == "h264"]
            if not v or (v[0]["width"], v[0]["height"]) != (1080, 1920): fail(errors, "video must be H.264 1080x1920")
            if not 3 <= d <= 90: fail(errors, f"duration {d:.1f}s outside 3–90s house range")
            if spec.get("music") and not (ROOT / spec["music"]).exists(): fail(errors, "music file missing")
            if not (out / "vo").exists():
                fail(errors, "no voice-over yet — reel is a DRAFT (set allow_silent=true in spec to override)") \
                    if not spec.get("allow_silent") else None
        if not (out / "cover.jpg").exists(): fail(errors, "cover.jpg missing")
    # duplicate guard: same id already logged as scheduled/published
    if LOG.exists():
        for line in LOG.read_text(encoding="utf-8").splitlines()[1:]:
            cols = line.split(",")
            if cols and cols[0] == spec["id"] and len(cols) > 6 and cols[6] in ("scheduled", "published"):
                fail(errors, "already scheduled/published — duplicate")
    return spec["id"], errors


if __name__ == "__main__":
    bad = False
    for p in sys.argv[1:]:
        sid, errs = check(p)
        print(("PASS " if not errs else "FAIL ") + sid)
        for e in errs:
            print("   -", e)
        bad |= bool(errs)
    sys.exit(1 if bad else 0)
