#!/usr/bin/env python3
"""stryde-lost-moments — Body 4 round 4 (board, 2026-10-01): D-01/D-02/D-10 pinned clips confirmed;
D-06-END A, D-08-END A picked → pinned first-and-last clips for D-06, D-08 (travel, 3s, §35A rule 3)."""
import json, pathlib
from actD import B
HERE = pathlib.Path(__file__).parent
SP = "/tmp/claude-0/-home-user-global-manual-ai/d5ebeecb-012d-539f-a9cc-ff2ce5209b53/scratchpad/actD/"
CAM = "Handheld phone, a gentle breath sway, the camera stays where it is."
MOTION = {"D-06": B["D-06"]["motion"],
          "D-08": "From this frame: he walks on past the empty buggy at a normal walking pace, three steps, about three seconds."}
PIN = {
 "D-06": ("He ends exactly as in the end frame; the same man, bag on his right shoulder and strap below his right kneecap the whole way, the course unchanged. No second person, no camera move.",
          [("the man morphs", "the same man, bag and strap the whole way"), ("he overshoots", "ends exactly as in the end frame"), ("strap slides", "strap below his right kneecap the whole way")]),
 "D-08": ("He ends exactly as in the end frame; the same man, bag on his right shoulder and strap below his right kneecap the whole way, the empty buggy parked and still. No second person, no camera move.",
          [("the buggy moves", "the empty buggy parked and still"), ("he overshoots", "ends exactly as in the end frame"), ("strap slides", "strap below his right kneecap the whole way")]),
}
if __name__ == "__main__":
    for b, (facts, risks) in PIN.items():
        p = f'For the line "{B[b]["line"]}": {MOTION[b]} {CAM} {facts}'
        (HERE / "prompts" / f"{b}.v1.video.txt").write_text(p)
        c = {"beat": b, "connector": "kling", "mode": 1, "kind": "broll", "prompt": p, "duration": 3, "resolution": "1080p", "aspect_ratio": "9:16",
             "start_image": SP + f"{b}.v2.A.png", "start_approved": True, "pinned": True, "end_image": SP + f"{b}-END.A.png", "end_approved": True,
             "approved_by": "user picked the start (A, v3) and end frame (A) on the board (2026-10-01)", "subject_motion": "travels",
             "prefer_multi_shots": "false", "generation": 1, "script_line": B[b]["line"], "motion_plan": MOTION[b], "motion_confirmed": True,
             "risk_class": "travel", "pilot": "confirmed", "taste": B[b]["taste"], "risks": [{"risk": r, "prevented_by": q} for r, q in risks]}
        (HERE / "clips" / f"{b}.v1.call.json").write_text(json.dumps(c, indent=1)); print(b, len(p))
