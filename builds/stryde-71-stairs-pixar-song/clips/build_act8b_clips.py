#!/usr/bin/env python3
"""Clips 2026-10-02 ~14:40 ("fix those and generate the clips"): PR-05b v2 (user clip Fix "she should not touch the hand rail") and the first
clips on the confirmed picks C-06a v1, C-08b v2, C-09a v1, C-09c v1 (Act 8). §35A, ≤ 1,000 chars, lips sealed on face shots.
Stairs: end frame waived by the user's 2026-10-01 words, the stairs pilot confirmed (HK clips); hands named off the rail on every stairs clip (PR-05b Fix)."""
import json, subprocess, sys, re
from pathlib import Path
H = Path(__file__).parent; B = H.parent
PF = B / "../../.claude/skills/ai-prompt-engineer/scripts/preflight.py"
rows = {r["beat"]: r for r in json.load(open(B / "work/actmap_rows.json"))}
CF = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/"
SEAL = "Her lips stay sealed and her jaw still from the first frame to the last, her face holding the expression of the frame — a silent clip, nobody speaks or sings."
SEAL_HE = "His lips stay sealed and his jaw still from the first frame to the last, his face holding the expression of the frame — a silent clip, nobody speaks or sings."
SEAL_2 = "Both their lips stay sealed and jaws still from the first frame to the last, each face holding the expression of the frame — a silent clip, nobody speaks or sings."
STRAP = "the strap stays rigid and exactly as in the frame — black shell, two peaks together at its middle, chrome slides"
ANAT = "the bones, the white tendon ribbons, the see-through peach outline and the pale grey backdrop stay exactly as in the frame"
WAIVE = 'user 2026-10-01: "we dont need end frame"'
CF = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/"
PR05_FIX = 'user clip Fix "she should not touch the hand rail" → both hands stay on the basket handles the whole clip, she keeps to the middle of the runner away from the rail, exactly one step then still'
C = {
 "C-06a": (CF + "hf_20261002_134620_f73ce643-8de3-47ea-b7b8-cadca4d1146b.png", 1, None,
           SEAL + " Seated on the sofa, she lifts both straps a little higher in front of her, one easy lift, then holds them still; in each hand " + STRAP + ", exactly two straps; the sofa and room stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut.",
           1, None, "none", False),
 "C-08b": (CF + "hf_20261002_134619_826c4f6e-4e9d-4877-99bd-ea51ee1d95a8.png", 2, None,
           SEAL + " Facing the lens, she takes one easy step down onto the next tread, her hands free at her sides the whole clip, never on the rail, then she stands still; on her right knee " + STRAP + "; the runner, brass rods, rail and photo wall stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. The camera stays where it is; no cut.",
           1, None, "stairs", True),
 "C-09a": (CF + "hf_20261002_134650_dd93d505-a84f-4f14-bca6-ebdc2a30438f.png", 1, None,
           "Nobody speaks or sings. Her two hands pull the red ribbon's bow tight on the box lid, one slow pull, then rest on the box; the black box and its wordmark stay exactly as in the frame, the bow neat; the table stays exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut.",
           1, None, "none", False),
 "C-09c": (CF + "hf_20261002_134650_2908e4c7-9b56-44fa-b52c-b2ccb78d07b0.png", 1, None,
           SEAL + " Her sister climbs two easy steps toward the lens at one step per second, the ribboned box steady under her left arm, her right hand free and never on the rail, then she stands still; the silver hair and mustard shoulder in the near foreground stay still; the runner, rods and photo wall stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. The camera stays where it is; no cut.",
           1, None, "stairs", True),
 "PR-05b": (CF + "hf_20261002_131240_4efeb531-6b4c-4596-9739-48aabc3be13c.png", 5, None,
           SEAL + " Facing the lens in the middle of the runner, away from the rail, she takes exactly one easy step down onto the next tread with the laundry basket at her waist, then stands still; both her hands keep hold of the basket's two handles from the first frame to the last and never touch the rail; her navy trousers fall smooth over both knees; the runner, brass rods, rail and photo wall stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. The camera stays where it is; no cut.",
           2, PR05_FIX, "stairs", True),
}
fails = 0
for b in (sys.argv[1:] or C):
    url, pick, mp, mt, cv, fix, rc, travel = C[b]; r = rows[b]
    line = re.sub(r'["“”]', "", r["line"])
    if mp is None:
        mp = json.load(open(f"/tmp/claude-0/-home-user-global-manual-ai/4a41b68d-7221-5f39-91cc-25c07de6bbd2/scratchpad/r24/generations/stryde-71-stairs-pixar-song__{b}.json"))["motionPlan"]
    pr = f'For the line "{line}": {mp}. {mt}'
    c = {"beat": b, "connector": "kling", "mode": 2, "kind": "broll", "prompt": pr, "duration": r["duration"], "resolution": "1080p", "aspect_ratio": "9:16",
         "start_image": url, "start_approved": True, "pinned": False, "end_image": None, "end_approved": False, "script_line": r["line"], "motion_plan": mp,
         "motion_confirmed": True, "pace": r["pace"].split(",")[0], "subject_motion": "travel" if travel else "in_place", "prefer_multi_shots": "false",
         "generation": cv, "user_go": None, "fix_note": fix, "fix_notes_all": None, "risk_class": rc,
         "pin_waived": WAIVE if rc != "none" else None, "pilot": "confirmed" if rc != "none" else None,
         "pilot_ref": {"travel": "PR-04a clip v1 (confirmed)", "stairs": "HK-01a/HK-02a stairs clips (confirmed)"}.get(rc),
         "taste": ["HT03", "HT04", "HT09", "HT12", "HT22", "HT25", "FP05", "FP07", "FP16", "FP18", "FP21", "FP22"],
         "risks": [{"risk": "a second action or a loop", "prevented_by": "one movement named, then rest"}, {"risk": "off model / the strap redrawn", "prevented_by": "exactly on model from the frame; the strap rigid"},
                   {"risk": "the camera travels", "prevented_by": "the camera stays where it is / one straight push"}, {"risk": "a face mouths the lyric", "prevented_by": "the silent clause (HT25, L30)"}],
         "note": f"clip v{cv} of this beat (from the confirmed image v{pick})"}
    (H / f"{b}.v{cv}.call.json").write_text(json.dumps(c, indent=1, ensure_ascii=False)); (H / f"{b}.v{cv}.prompt.txt").write_text(pr)
    res = subprocess.run([sys.executable, str(PF), str(H / f"{b}.v{cv}.call.json")], capture_output=True, text=True)
    print(f"{b}: {len(pr)} chars {r['duration']} s — {'PASS' if res.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in res.stdout.splitlines() if "FAIL" in l]
    fails += res.returncode != 0
sys.exit(1 if fails else 0)
