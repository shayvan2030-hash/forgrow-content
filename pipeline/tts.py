"""Hebrew voice-over via Google Cloud Text-to-Speech (REST, API key).

Needs:
  - env/network secret GOOGLE_TTS_API_KEY
  - texttospeech.googleapis.com allowed in the cloud environment's network settings
Usage:
  python3 pipeline/tts.py --list                     # list he-IL voices actually available
  python3 pipeline/tts.py content/<date>/<slug>/spec.json   # writes out/vo/scene_XX.mp3
Then re-run pipeline/render.py on the same spec to mix the narration into reel.mp4.
"""
import base64, json, os, pathlib, sys, urllib.request

API = "https://texttospeech.googleapis.com/v1"


def call(path, body=None):
    key = os.environ["GOOGLE_TTS_API_KEY"]
    req = urllib.request.Request(f"{API}/{path}{'&' if '?' in path else '?'}key={key}",
                                 data=json.dumps(body).encode() if body else None,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def list_voices():
    for v in call("voices?languageCode=he-IL").get("voices", []):
        print(v["name"], v.get("ssmlGender"))


def synth(spec_path):
    spec_path = pathlib.Path(spec_path).resolve()
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    voice = spec.get("voice", {"languageCode": "he-IL"})
    vo = spec_path.parent / "out" / "vo"; vo.mkdir(parents=True, exist_ok=True)
    chars = 0
    for i, s in enumerate(spec["scenes"]):
        text = s["vo"]; chars += len(text)
        res = call("text:synthesize", {
            "input": {"text": text},
            "voice": {"languageCode": voice["languageCode"], "name": voice.get("name")},
            "audioConfig": {"audioEncoding": "MP3", "speakingRate": voice.get("speakingRate", 1.0)}})
        (vo / f"scene_{i + 1:02d}.mp3").write_bytes(base64.b64decode(res["audioContent"]))
    print(f"voice-over written ({chars} characters billed)")


if __name__ == "__main__":
    if sys.argv[1:] == ["--list"]:
        list_voices()
    else:
        for p in sys.argv[1:]:
            synth(p)
