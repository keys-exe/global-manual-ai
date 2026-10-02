#!/usr/bin/env python3
"""Clips 2026-10-02 ~14:00 ("fix those and generate the next act"): the first clips on the confirmed picks C-01a, C-03b, C-04a, C-05a (Act 7)
and PR-05b v5, PR-06a v5 (Act 5 Fixes). §35A, ≤ 1,000 chars, no speech marks in the line (L30), lips sealed on face shots.
PR-05b: stairs class, end frame waived by the user's 2026-10-01 words, the stairs pilot confirmed (HK clips)."""
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
 "C-01a": (CF + "hf_20261002_131241_5b983506-90c9-4ece-92a1-6e583880e2e4.png", 1, None,
           "Nobody speaks or sings. Her right hand lifts a little off her right knee and pats it once, just above the strap, then rests; on her right knee " + STRAP + ", exactly one strap; the nightgown, quilt and bed stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut.",
           1, None, "none", False),
 "C-03b": (CF + "hf_20261002_131325_12582952-8dc8-42c1-b2a3-efc9c7304f4b.png", 1, None,
           "Only the glow moves: the soft cool blue light under the strap's pad swells slowly once along the tendon ribbon and settles, about two seconds; " + STRAP + "; " + ANAT + "; nobody in the frame, nobody speaks. Stylized 3D animated anatomy, exactly on model from the frame. The camera pushes in slowly on one straight axis, nothing more; no cut.",
           1, None, "none", False),
 "C-04a": (CF + "hf_20261002_131325_89231e64-c9f5-4102-907a-6432bf99659d.png", 1, None,
           SEAL_2 + " Crouched at his knee, the surgeon presses the strap flat under his kneecap with both thumbs, one gentle press, then her hands rest on it; he sits still on the table edge, his hands on the table; " + STRAP + ", exactly one strap on his right knee; the exam room stays exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut.",
           1, None, "none", False),
 "C-05a": (CF + "hf_20261002_131324_de248045-0d11-4d23-998a-3365a3308091.png", 1, None,
           "Nobody speaks or sings. Her two hands pull the cheap grey copy a little wider by its band, one slow stretch, and the thin band sags and the soft shell bends in the middle, then her hands hold still; the second copy lies still on the table; both copies stay one piece each, never turning into the real strap; the table stays exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut.",
           1, None, "none", False),
 "PR-05b": (CF + "hf_20261002_131240_4efeb531-6b4c-4596-9739-48aabc3be13c.png", 5, None,
           SEAL + " Facing the lens, she takes one easy step down onto the next tread, the laundry basket steady at her waist in both hands, hands off the rail, her navy trousers falling smooth over both knees, then she holds; the runner, brass rods, rail and photo wall stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. The camera stays where it is; no cut.",
           1, None, "stairs", True),
 "PR-06a": (CF + "hf_20261002_131240_bff302b8-80ad-40ab-815d-4ce947fe34f4.png", 5, None,
           "Nobody in the frame, nobody speaks. Only the steam moves: a thin curl of steam rises from the coffee mug and drifts, about two seconds; beside it " + STRAP + ", exactly one strap lying still, its band as short as in the frame; the table stays exactly as in the frame. Stylized 3D animation, exactly on model from the frame. The camera pushes in slowly on one straight axis, nothing more; no cut.",
           1, None, "none", False),
}
fails = 0
for b in (sys.argv[1:] or C):
    url, pick, mp, mt, cv, fix, rc, travel = C[b]; r = rows[b]
    line = re.sub(r'["“”]', "", r["line"])
    if mp is None:
        mp = json.load(open(f"/tmp/claude-0/-home-user-global-manual-ai/4a41b68d-7221-5f39-91cc-25c07de6bbd2/scratchpad/r23/generations/stryde-71-stairs-pixar-song__{b}.json"))["motionPlan"]
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
