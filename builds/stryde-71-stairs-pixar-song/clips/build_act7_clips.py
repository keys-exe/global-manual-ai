#!/usr/bin/env python3
"""Clips 2026-10-02 ~13:05 ("fix those and generate the next act"): M-05a v2 (user Fix "should showcase the patellartendon is the one getting
that animatuon"), and the first clips on the confirmed picks L-01a, L-01b, L-02a, L-02b, L-03a (Act 6), M-06a v9, PR-03a v3.
§35A, ≤ 1,000 chars, no speech marks in the line (L30), lips sealed on face shots. Walks: travel class, end frame waived by the user's 2026-10-01
words, the class pilot already confirmed (PR-04a jog); M-06a: stairs, waived, the stairs pilot confirmed (HK clips)."""
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
M05_FIX = 'user Fix "should showcase the patellartendon is the one getting that animatuon" → the glow now travels down the tendon ribbon itself and pulses on it; the thigh lines stay still'
M05_MP = "From this frame: a soft warm glow runs down the patellar tendon ribbon from the bottom of the kneecap to the shin bump and pulses on it — one pulse per second; camera R4 — slow single-axis push on a stabilised virtual rig"
# beat: (start url, pick, motion plan or None, body, generation, fix, risk class, travel)
C = {
 "M-05a": (CF + "hf_20261002_112006_38ff8120-0288-4b70-a50e-dcaced23625d.png", 8, M05_MP,
           "Only the patellar tendon is animated: the soft warm glow runs down the white tendon ribbon below the kneecap and pulses on the ribbon itself, one pulse per second, while the thigh lines and the kneecap stay still and plain; " + ANAT + "; nobody in the frame, nobody speaks. Stylized 3D animated anatomy, exactly on model from the frame. The camera pushes in slowly on one straight axis, nothing more; no cut.",
           2, M05_FIX, "none", False),
 "L-01a": (CF + "hf_20261002_122611_be81df2f-2d46-4f76-b944-00108eeca0c6.png", 1, None,
           "Nobody speaks or sings. Her back to the lens, she walks away down the middle of the sidewalk, three easy steps at one step per second, the tote steady on her right shoulder, her left arm swinging; the trees, mailboxes, houses and street stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. The camera stays where it is; no cut.",
           1, None, "travel", True),
 "L-01b": (CF + "hf_20261002_123531_08631d8d-dca5-4829-ae25-77361852e965.png", 1, None,
           SEAL + " Walking toward the lens with a steady stride, she takes two easy steps and draws a step further ahead of the three younger women, who stroll slowly beside her with their coffee cups; the sidewalk, trees and houses stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. The camera stays where it is; no cut.",
           1, None, "travel", True),
 "L-02a": (CF + "hf_20261002_122659_fbb33633-d7ab-4892-a098-4cf2d37dd851.png", 1, None,
           SEAL + " Standing square in the checkout line, both feet planted, she moves the red basket from her right hand to her left hand once, then stands calm; the two shoppers ahead keep unloading slowly; the counter and store stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut.",
           1, None, "none", False),
 "L-02b": (CF + "hf_20261002_122700_278742db-bb92-4e47-8faa-1a3736aeddfa.png", 1, None,
           "Nobody speaks or sings. Her back to the lens, she walks two easy steps up the front path toward the porch at one step per second, a paper bag steady in each hand; the red-brick house, porch and lawn stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. The camera stays where it is; no cut.",
           1, None, "travel", True),
 "L-03a": (CF + "hf_20261002_123223_33a46fcb-fb02-47be-9204-52a797a36aaf.png", 1, None,
           SEAL_2 + " In his recliner he lowers the newspaper onto his lap and looks up at her with one raised eyebrow; she stands still in the doorway with her two bags and a small knowing smile; the room stays exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut.",
           1, None, "none", False),
 "M-06a": (CF + "hf_20261002_123022_52597e35-aee3-4e75-96a4-938f708c7114.png", 9, None,
           "Nobody speaks or sings. Her leading slipper lands flat on the next tread down and her weight settles onto it, one step, then she holds; on her right knee " + STRAP + "; the runner, brass rods and balusters stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut.",
           1, None, "stairs", True),
 "PR-03a": (CF + "hf_20261002_122610_dd1ab9cf-79df-43a6-8b9f-d9f0f6fde96d.png", 3, None,
            SEAL_HE + " At the finish of his golf swing he lets the club settle over his shoulder and holds the pose, one easy settle; on his right knee " + STRAP + ", exactly one strap; the fairway and sky stay as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut.",
            1, None, "none", False),
}
fails = 0
for b in (sys.argv[1:] or C):
    url, pick, mp, mt, cv, fix, rc, travel = C[b]; r = rows[b]
    line = re.sub(r'["“”]', "", r["line"])
    if mp is None:
        mp = json.load(open(f"/tmp/claude-0/-home-user-global-manual-ai/4a41b68d-7221-5f39-91cc-25c07de6bbd2/scratchpad/r22/generations/stryde-71-stairs-pixar-song__{b}.json"))["motionPlan"]
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
