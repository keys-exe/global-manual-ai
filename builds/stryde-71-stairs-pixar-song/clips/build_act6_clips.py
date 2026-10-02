#!/usr/bin/env python3
"""Clips 2026-10-02 ~12:35 ("fix those and generate the next act"): M-02a v3 (user Fix "you should show blue glow to show that the stryde is better";
generation 3 — the user's message is the go), and the first clips on the confirmed picks M-05a v8, PR-01a v1, PR-02a v2, PR-04a v2, PR-05a v2.
§35A, ≤ 1,000 chars, no speech marks in the line (L30), lips sealed on face shots; "we dont need end frame" (user 2026-10-01) for the pinned class."""
import json, subprocess, sys, re
from pathlib import Path
H = Path(__file__).parent; B = H.parent
PF = B / "../../.claude/skills/ai-prompt-engineer/scripts/preflight.py"
rows = {r["beat"]: r for r in json.load(open(B / "work/actmap_rows.json"))}
CF = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/"
SEAL_HE = "His lips stay sealed and his jaw still from the first frame to the last, his face holding the expression of the frame — a silent clip, nobody speaks or sings."
SEAL = "Her lips stay sealed and her jaw still from the first frame to the last, her face holding the expression of the frame — a silent clip, nobody speaks or sings."
STRAP = "the strap stays rigid and exactly as in the frame — black shell, two peaks together at its middle, chrome slides"
ANAT = "the bones, the white tendon ribbons, the see-through peach outline and the pale grey backdrop stay exactly as in the frame"
RIGID = "the strap is one rigid solid object, its outline identical in every frame — the black shell with its two pointed peaks round the notch, a chrome slide at each end, the band the same width"
WAIVE = 'user 2026-10-01: "we dont need end frame"'
M02_FIX1 = 'user Fix "dont change the shape of the product" → locked camera, only the light changes, the strap one rigid object identical in every frame'
M02_FIX2 = 'user Fix "you should show blue glow to show that the stryde is better" → under the strap the warm glow cools to a calm blue (the relief colour), the left knee keeps its amber; camera still locked'
C = {
 "M-02a": (CF + "hf_20261002_111200_e2148ba2-e154-4ae6-8720-59489dc01597.png", 5,
           "From this frame: under the strap on the right knee model the warm glow cools into a calm soft blue and holds — about two seconds; camera locked, the frame holds still",
           "Only the light changes: on the right knee the glow behind the strap turns from warm amber to a calm cool blue and settles, while the left knee in its sleeve keeps its amber haze; " + RIGID + "; " + ANAT + "; nobody in the frame, nobody speaks. Stylized 3D animated anatomy, exactly on model from the frame. The camera does not move; no zoom; no cut.",
           3, M02_FIX2, [M02_FIX1, M02_FIX2], 'user 2026-10-02: "fix those and generate the next act" (the Fix on the board)', "none"),
 "M-05a": (CF + "hf_20261002_112006_38ff8120-0288-4b70-a50e-dcaced23625d.png", 8, None,
           "Soft warm pressure pulses down the faint lines of the thigh into the glowing spot on the tendon ribbon below the kneecap, one pulse per second; " + ANAT + "; the kneecap stays plain ivory; nobody in the frame, nobody speaks. Stylized 3D animated anatomy, exactly on model from the frame. The camera pushes in slowly on one straight axis, nothing more; no cut.",
           1, None, None, None, "none"),
 "PR-01a": (CF + "hf_20261002_113951_7b2096a2-c487-47d8-a429-1a122d30f152.png", 1, None,
            SEAL_HE + " Seated on the porch step, he slides the strap the last few centimetres up his right shin with both hands until its notch meets the bottom of his kneecap, then his hands rest; " + STRAP + "; the porch stays exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut.",
            1, None, None, None, "none"),
 "PR-02a": (CF + "hf_20261002_113413_e26c33e0-a524-414d-b98d-e29830006ca5.png", 2, None,
            SEAL + " At her desk she turns the strap once so its front faces the lens, then lowers it onto the knee model and presses it in place under the model's kneecap, then rests; " + STRAP + "; the knee model and desk stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut.",
            1, None, None, None, "product_angle"),
 "PR-04a": (CF + "hf_20261002_113515_027d407e-ad54-4f9a-9594-32cb4c047765.png", 2, None,
            SEAL + " She jogs three easy strides across the frame on the red track, arms bent, a steady jog; on her right knee " + STRAP + ", exactly one strap; the track lanes and the grass stay as in the frame. Stylized 3D animation, exactly on model from the frame. The camera stays where it is; no cut.",
            1, None, None, None, "none"),
 "PR-05a": (CF + "hf_20261002_113515_24dcdbbf-db60-4e98-a9cf-3833f2afb90c.png", 2, None,
            "Nobody speaks or sings. Seated on the bed's edge, she slides the strap the last few centimetres up her right shin with both hands until its notch meets the bottom of her kneecap, then her hands rest on her thighs; " + STRAP + "; the nightgown, quilt and floor stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut.",
            1, None, None, None, "none"),
}
fails = 0
for b in (sys.argv[1:] or C):
    url, pick, mp, mt, cv, fix, allfix, go, rc = C[b]; r = rows[b]
    line = re.sub(r'["“”]', "", r["line"])
    if mp is None:
        mp = json.load(open(f"/tmp/claude-0/-home-user-global-manual-ai/4a41b68d-7221-5f39-91cc-25c07de6bbd2/scratchpad/r21/generations/stryde-71-stairs-pixar-song__{b}.json"))["motionPlan"]
    pr = f'For the line "{line}": {mp}. {mt}'
    travel = b == "PR-04a"
    c = {"beat": b, "connector": "kling", "mode": 2, "kind": "broll", "prompt": pr, "duration": r["duration"], "resolution": "1080p", "aspect_ratio": "9:16",
         "start_image": url, "start_approved": True, "pinned": False, "end_image": None, "end_approved": False, "script_line": r["line"], "motion_plan": mp,
         "motion_confirmed": True, "pace": r["pace"].split(",")[0], "subject_motion": "travel" if travel else "in_place", "prefer_multi_shots": "false",
         "generation": cv, "user_go": go, "fix_note": fix, "fix_notes_all": allfix, "risk_class": rc,
         "pin_waived": WAIVE if rc != "none" else None, "pilot": "first" if rc != "none" else None,
         "taste": ["HT03", "HT04", "HT09", "HT12", "HT22", "HT25", "FP05", "FP07", "FP16", "FP18", "FP21"],
         "risks": [{"risk": "a second action or a loop", "prevented_by": "one movement named, then rest"}, {"risk": "off model / the strap redrawn", "prevented_by": "exactly on model from the frame; the strap rigid"},
                   {"risk": "the camera travels", "prevented_by": "no camera travel / one straight push / locked"}, {"risk": "a face mouths the lyric", "prevented_by": "the silent clause (HT25, L30)"}],
         "note": f"clip v{cv} of this beat (from the confirmed image v{pick})"}
    (H / f"{b}.v{cv}.call.json").write_text(json.dumps(c, indent=1, ensure_ascii=False)); (H / f"{b}.v{cv}.prompt.txt").write_text(pr)
    res = subprocess.run([sys.executable, str(PF), str(H / f"{b}.v{cv}.call.json")], capture_output=True, text=True)
    print(f"{b}: {len(pr)} chars {r['duration']} s — {'PASS' if res.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in res.stdout.splitlines() if "FAIL" in l]
    fails += res.returncode != 0
sys.exit(1 if fails else 0)
