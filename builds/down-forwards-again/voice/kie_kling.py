#!/usr/bin/env python3
"""Kling 3.0 Omni image-to-video through the Kie AI API — BUILD-LOCAL, user override 2026-09-28
("USE KEI AI AS SUBSTITUTE FOR NOW": Kling connector at 3 credits). Same model family as the §5 lock
(kling-video-v3_0_omni), Kie id `kling-3.0-omni/image-to-video` (docs.kie.ai/market/kling/v3-omni-image-to-video):
prompt <= 3,072 chars, 1 first-frame image, duration 3-15, resolution 720p|1080p|4k, aspect_ratio, audio, prefer_multi_shots.
Refuses to send unless preflight.py passes on the call file. One task per call.

Usage: kie_kling.py send <call.json> [--out clip.mp4]   ·   kie_kling.py wait <taskId> --out clip.mp4
"""
import sys, json, subprocess, pathlib
SCR = pathlib.Path(__file__).resolve().parents[3] / ".claude/skills/ai-prompt-engineer/scripts"
sys.path.insert(0, str(SCR)); import kie
MODEL = "kling-3.0-omni/image-to-video"
def send(call_path):
    pf = subprocess.run([sys.executable, str(SCR / "preflight.py"), call_path], capture_output=True, text=True)
    if pf.returncode != 0:
        sys.exit(pf.stdout + "\nNOT SENT (preflight)")
    c = json.load(open(call_path))
    assert len(c["prompt"]) <= 3072, len(c["prompt"])
    inp = {"prompt": c["prompt"], "image_urls": [kie.as_url(c["start_image"])], "duration": int(c["duration"]),
           "resolution": c.get("resolution", "1080p"), "aspect_ratio": c.get("aspect_ratio", "9:16"),
           "audio": c.get("kind") == "dialogue" or bool(c.get("audio")), "prefer_multi_shots": False}
    return kie.create(MODEL, inp)
if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "send":
        t = send(sys.argv[2]); print(json.dumps({"taskId": t, "model": MODEL}))
    elif cmd == "wait":
        out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else None
        res, rc = kie.wait(sys.argv[2], out); print(json.dumps(res, indent=1)); sys.exit(rc)
