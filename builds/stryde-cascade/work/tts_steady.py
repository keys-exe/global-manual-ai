"""stryde-cascade only (user 2026-09-29: "the voice change in the middle").
One Eleven v4 take like tts_api.py, plus voice_settings.stability (1.0 = Robust: the most consistent
timbre across a long read). Usage: tts_steady.py TEXT.txt VOICE_ID OUT.mp3 [--stability 1.0] [--speed 1.0]"""
import argparse, json, os, urllib.request
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("text"); ap.add_argument("voice"); ap.add_argument("out")
ap.add_argument("--stability", type=float, default=1.0); ap.add_argument("--speed", type=float, default=1.0)
a = ap.parse_args()
body = {"text": Path(a.text).read_text(), "model_id": "eleven_v4",
        "voice_settings": {"speed": a.speed, "stability": a.stability}}
req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{a.voice}?output_format=mp3_44100_192",
                             method="POST", data=json.dumps(body).encode(),
                             headers={"xi-api-key": os.environ["ELEVENLABS_API_KEY"], "Content-Type": "application/json"})
with urllib.request.urlopen(req, timeout=600) as r:
    Path(a.out).write_bytes(r.read())
print(a.out)
