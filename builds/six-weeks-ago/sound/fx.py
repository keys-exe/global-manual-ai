#!/usr/bin/env python3
"""Six Weeks Ago — make the room tones and the SFX list in sound_plan.json (§24M, ElevenLabs sound effects).

Usage:
  fx.py [ID ...]        # generate every missing file (or only the named IDs) into fx/<ID>.mp3

One generation per call, eleven_text_to_sound_v2:
  room tones  (plan["tones"])  loop: true, 20–30s, ROOM-TONE wording
  effects     (plan["sfx"])    one sound per object, SFX-LINE wording, the entry's duration
An existing file is never regenerated unless its ID is named.
"""
import json, os, sys, urllib.request
from pathlib import Path

HERE = Path(__file__).parent
URL = "https://api.elevenlabs.io/v1/sound-generation?output_format=mp3_44100_192"


def generate(text, seconds, loop, out):
    body = {"text": text, "model_id": "eleven_text_to_sound_v2", "duration_seconds": seconds,
            "prompt_influence": 0.6, "loop": loop}
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), method="POST",
                                 headers={"xi-api-key": os.environ["ELEVENLABS_API_KEY"],
                                          "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        out.write_bytes(r.read())


def main():
    plan = json.loads((HERE / "sound_plan.json").read_text())
    want = set(sys.argv[1:])
    (HERE / "fx").mkdir(exist_ok=True)
    jobs = [(k, v["prompt"], v.get("duration", 25), True) for k, v in plan["tones"].items()]
    jobs += [(k, v["prompt"], v.get("duration", 1.5), False) for k, v in plan["sfx"].items()]
    for k, text, sec, loop in jobs:
        out = HERE / "fx" / f"{k}.mp3"
        if (want and k not in want) or (not want and out.exists()):
            continue
        generate(text, sec, loop, out)
        print(k, out.stat().st_size, flush=True)


if __name__ == "__main__":
    main()
