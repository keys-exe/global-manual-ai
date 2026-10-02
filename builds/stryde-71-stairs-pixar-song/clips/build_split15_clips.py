#!/usr/bin/env python3
"""Clips 2026-10-02 ("confirm"): P-04c "Pain pills." and P-04d "Cortisone shots." on the user's A picks (line 15 split).
§35A, ≤ 1,000 chars; P-04d's frame shows her chin at the top edge, so it carries the sealed-lips clause."""
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
C = {
 "P-04c": ("https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20261002_162148_e9220323-fe36-4aa0-a7cb-449febde36be.png", 1, None,
           "Nobody speaks or sings; only her hands move. Her right hand tips the amber bottle a little further and two small white pills drop into her open left palm, one tip, then both hands hold still; the bottle, the pills, the glass of water and the round wooden table stay exactly as in the frame, exactly one bottle, exactly two pills. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut.",
           1, None, "none", False),
 "P-04d": ("https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20261002_162148_c0c9db71-6b63-4cdf-9ab3-8fc4a5d69d45.png", 1, None,
           SEAL + " The doctor's gloved thumb presses the syringe's plunger down slowly, one press, about a second, the needle held still at the side of her knee, the other gloved hand steady on her knee; her own hand stays gripping the paper sheet; her knee, the table, the window and the blind stay exactly as in the frame, exactly one syringe. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut.",
           1, None, "none", False),
}
fails = 0
for b in (sys.argv[1:] or C):
    url, pick, mp, mt, cv, fix, rc, travel = C[b]; r = rows[b]
    line = re.sub(r'["“”]', "", r["line"])
    if mp is None:
        mp = json.load(open(f"/tmp/claude-0/-home-user-global-manual-ai/4a41b68d-7221-5f39-91cc-25c07de6bbd2/scratchpad/r29/generations/stryde-71-stairs-pixar-song__{b}.json"))["motionPlan"]
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
