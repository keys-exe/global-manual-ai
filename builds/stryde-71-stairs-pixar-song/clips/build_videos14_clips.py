#!/usr/bin/env python3
"""Clips 2026-10-02 ("generate the videos"): the first clips on the confirmed picks C-02a v5, C-02b v5, C-07a v3, C-08a v3 (Acts 7–8)
and PR-06a clip v2 from its new picked frame (image v7, the strap-size Fix). §35A, ≤ 1,000 chars, lips sealed on face shots.
Stairs: end frame waived by the user's 2026-10-01 words, the stairs pilot confirmed (HK clips). C-02b is an after-state: her hand leaves the rail;
C-08a is the struggle (eleven years of knee pain): both hands on the rail."""
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
SEAL_3 = "All three women keep their lips sealed and jaws still from the first frame to the last, each face holding the expression of the frame — a silent clip, nobody speaks or sings."
SEAL_4 = "All four women keep their lips sealed and jaws still from the first frame to the last, each face holding the expression of the frame — a silent clip, nobody speaks or sings."
PR06_FIX = 'image Fix "the strap is too big" → new start frame (image v7, the strap at true size beside the mug); same confirmed motion plan, the strap\'s size held from the frame'
C = {
 "C-02a": (CF + "hf_20261002_143722_e2b5d84f-a062-4a71-96b1-07a654cb631f.png", 5, None,
           SEAL_3 + " At the foot of the church steps, the woman in coral in the middle gives the woman in lilac one gentle nudge with the hand already on her shoulder, and the woman in lilac nods once, then all three stand still; the woman in cream on the right stays still, her bag in her right hand; each woman keeps her own face, build, hat and suit exactly as in the frame, three different women. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut.",
           1, None, "none", False),
 "C-02b": (CF + "hf_20261002_143848_08331be1-2e62-4fca-ac76-9cc7bf362bdf.png", 5, None,
           SEAL_4 + " The woman in green takes one easy step down onto the next church step, facing forwards; as she steps, her left hand leaves the rail and swings loose at her side, her right hand free, and she never takes hold of the rail again, then she stands still; the three women in lilac, coral and cream stay still on the pavement, each exactly as in the frame; the steps, rail, brick and street stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. The camera stays where it is; no cut.",
           1, None, "stairs", True),
 "C-07a": (CF + "hf_20261002_142838_973a3594-ad31-4351-872c-119f12c1cc75.png", 3, None,
           "Nobody speaks or sings; only her hand moves. Her right hand, already on the lid's right end, slides the lid a little further aside on the table, then lifts away out of the frame; it never crosses the stryde wordmark on the lid, which stays fully in view; the open box and the two straps inside stay exactly as in the frame, exactly two straps, black shell, two peaks together at its middle, chrome slides, rigid; the table and chair stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut.",
           1, None, "none", False),
 "C-08a": (CF + "hf_20261002_142835_1b392bfa-7f5b-4f7c-8e99-c475a58bf243.png", 3, None,
           SEAL + " Seen from the side, she takes one slow step down: her back foot in its pink slipper comes down onto the tread beside her front foot, about two seconds, both her hands gripping the wooden rail the whole clip, then she stands still; her knees bare of any strap; the runner, brass rods, rail and photo wall stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. The camera stays where it is; no cut.",
           1, None, "stairs", True),
 "PR-06a": (CF + "hf_20261002_142838_630351e6-7102-417e-a679-68ea52f670c2.png", 7, None,
           "Nobody in the frame, nobody speaks. Only the steam moves: a thin curl of steam rises from the coffee mug and drifts, about two seconds; beside it the strap stays rigid and exactly as in the frame — black shell, two peaks together at its middle, chrome slides, exactly one strap lying still, a little longer than the mug is tall, its band as short as in the frame; the table stays exactly as in the frame. Stylized 3D animation, exactly on model from the frame. The camera pushes in slowly on one straight axis, nothing more; no cut.",
           2, PR06_FIX, "none", False),
}
fails = 0
for b in (sys.argv[1:] or C):
    url, pick, mp, mt, cv, fix, rc, travel = C[b]; r = rows[b]
    line = re.sub(r'["“”]', "", r["line"])
    if mp is None:
        mp = json.load(open(f"/tmp/claude-0/-home-user-global-manual-ai/4a41b68d-7221-5f39-91cc-25c07de6bbd2/scratchpad/r26/generations/stryde-71-stairs-pixar-song__{b}.json"))["motionPlan"]
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
