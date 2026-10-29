# forgrow-content

Marketing assets and the daily content pipeline for ForGrow (@forgrow_social).
Contains NO product code and NO customer/candidate data. Everything here is meant to become public.

## How a day works
1. A Claude scheduled task (cloud, runs when your computer is off) runs `prompts/daily_run.md` every morning.
2. It writes `content/<date>/<slug>/spec.json`, renders with `pipeline/render.py`
   (voice-over via `pipeline/tts.py`), and checks with `pipeline/qa.py` plus a visual check.
3. Files are committed here; their raw GitHub URLs are what Metricool fetches.
4. Through the Metricool connector it schedules tomorrow's posts and verifies yesterday's.
5. `content_log.csv` is the single content log.

## Requirements
- Python 3 + Playwright (Chromium) + Pillow + ffmpeg (present in the Claude cloud environment)
- Secret `GOOGLE_TTS_API_KEY` and `texttospeech.googleapis.com` allowed in the environment's network settings
- Metricool connector connected to Claude, with @forgrow_social (professional account) connected in Metricool

## Local test
    python3 pipeline/render.py content/2026-10-29/carousel-profile-visits/spec.json
    python3 pipeline/qa.py content/*/*/spec.json
