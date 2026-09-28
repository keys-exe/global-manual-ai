#!/usr/bin/env python3
"""§22U step 9 by API — Eleven v3 TTS with pace control (V7.65.0).

The ElevenLabs connector's eleven_v3 node has no speed setting; the API does (voice_settings.speed,
0.7–1.2). Pace is set by the tags in the text ([slowly], [pause] — tags only, never a word changed,
tts_budget.py --script-lines still gates the text) and, where still needed, by --speed.

Needs ELEVENLABS_API_KEY in the environment (an environment secret; never pasted in chat).

  tts_api.py TAGGED.txt --voice VOICE_ID --out-prefix vo/T --takes 4 [--speed 0.8] [--script LINES.txt]

Writes <prefix>1.mp3 … <prefix>N.mp3 (one API call per take — one render per call, §5) and prints
per take: duration and, with --script, the words-per-minute of the speech (first word to last).
"""
import argparse, json, os, sys, urllib.request
from pathlib import Path

API = "https://api.elevenlabs.io/v1"


def tts(text, voice, speed, out):
    body = {"text": text, "model_id": "eleven_v3", "voice_settings": {"speed": speed}}
    req = urllib.request.Request(f"{API}/text-to-speech/{voice}?output_format=mp3_44100_192", method="POST",
                                 data=json.dumps(body).encode(),
                                 headers={"xi-api-key": os.environ["ELEVENLABS_API_KEY"], "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as r:
        Path(out).write_bytes(r.read())


def pace(path, script):
    sys.path.insert(0, str(Path(__file__).parent))
    from trim import words
    ws = words(Path(path), "base.en")
    n = len(Path(script).read_text().split())
    span = ws[-1][1] - ws[0][0] if ws else 0
    return round(n / span * 60) if span else None


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("tagged"); ap.add_argument("--voice", required=True); ap.add_argument("--out-prefix", required=True)
    ap.add_argument("--takes", type=int, default=4); ap.add_argument("--speed", type=float, default=1.0)
    ap.add_argument("--script", help="spoken lines, to report words per minute")
    a = ap.parse_args()
    if "ELEVENLABS_API_KEY" not in os.environ:
        sys.exit(json.dumps({"error": "ELEVENLABS_API_KEY is not set in the environment"}))
    if not 0.7 <= a.speed <= 1.2:
        sys.exit(json.dumps({"error": "speed must be 0.7-1.2"}))
    text = Path(a.tagged).read_text(encoding="utf-8")
    if len(text) > 5000:
        sys.exit(json.dumps({"error": f"{len(text)} characters > 5,000 per request (§22U budget ladder)"}))
    sys.path.insert(0, str(Path(__file__).parent))
    from trim import duration
    rep = []
    for k in range(1, a.takes + 1):
        out = f"{a.out_prefix}{k}.mp3"
        tts(text, a.voice, a.speed, out)
        row = {"take": k, "file": out, "duration_s": round(duration(out), 2)}
        if a.script:
            row["wpm"] = pace(out, a.script)
        rep.append(row)
    print(json.dumps({"speed": a.speed, "takes": rep}, indent=2))
