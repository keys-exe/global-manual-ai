#!/usr/bin/env python3
"""Clips from the user's picks 2026-10-02 ~11:30 (Pixar anatomy M-02a, M-05b, T-03a); was: picks 10:20–10:23: M-01a, M-04a, M-06a (Act 4), R-04a, R-07a (Act 3; R-07a one take for both lines, 9 s).
§35A, ≤ 1,000 chars, no speech marks in the line (L30), lips sealed on face shots."""
import json, subprocess, sys, re
from pathlib import Path
H = Path(__file__).parent; B = H.parent
PF = B / "../../.claude/skills/ai-prompt-engineer/scripts/preflight.py"
rows = {r["beat"]: r for r in json.load(open(B / "work/actmap_rows.json"))}
u = json.load(open(B / "body4/urls.json"))
SEAL = "Her lips stay sealed and her jaw still from the first frame to the last, her face holding the expression of the frame — a silent clip, nobody speaks or sings."
STRAP = "the strap stays rigid and exactly as in the frame — black shell, two peaks, chrome slides"
ANAT = "the bones, the white tendon ribbons, the see-through peach outline and the pale grey backdrop stay exactly as in the frame"
MP = {"M-02a": "From this frame: a slow soft warm glow settles on the right knee's spot — about two seconds; camera R4 — slow single-axis push on a stabilised virtual rig",
      "M-05b": "From this frame: the warm glow under the pad fades to a soft cool blue as the pad takes the load — one fade, about two seconds; camera R4 — slow single-axis push on a stabilised virtual rig",
      "T-03a": "From this frame: the warm glow where the bones touch pulses once — one pulse, about a second; camera R4 — slow single-axis push on a stabilised virtual rig"}
C = {
 "M-02a": ("M-02a@v6A2", None, "A slow soft warm glow settles under the strap on the right knee model and holds; the left knee's amber haze stays as it is; on the right knee " + STRAP + "; " + ANAT + "; nobody in the frame, nobody speaks. Stylized 3D animated anatomy, exactly on model from the frame. The camera pushes in slowly on one straight axis, nothing more; no cut; the strap never bends."),
 "M-05b": ("M-05b@v3A", None, "Under the strap's pad the warm glow fades into a soft cool blue that spreads down the tendon ribbon, once; " + STRAP + ", seated under the kneecap; " + ANAT + "; nobody in the frame, nobody speaks. Stylized 3D animated anatomy, exactly on model from the frame. The camera pushes in slowly on one straight axis, nothing more; no cut; the strap never bends."),
 "T-03a": ("T-03a@v6A2", None, "In both knee models the small warm glow where the bones touch swells once and settles back; " + ANAT + "; nobody in the frame, nobody speaks. Stylized 3D animated anatomy, exactly on model from the frame. The camera pushes in slowly on one straight axis, nothing more; no cut.", 2,
           'user "the t03a too" → the image redone in the Pixar anatomy, so a new clip on the new frame (clip v1 was on the old X-ray frame)'),
}
fails = 0
for b in (sys.argv[1:] or C):
    k, mp, mt, *more = C[b]; r = rows[b]; cv = more[0] if more else 1
    line = re.sub(r'["“”]', "", r["line"])
    mp = mp or MP[b]
    pr = f'For the line "{line}": {mp}. {mt}'
    stairs = b == "R-07a"
    c = {"beat": b, "connector": "kling", "mode": 2, "kind": "broll", "prompt": pr, "duration": r["duration"], "resolution": "1080p", "aspect_ratio": "9:16",
         "start_image": u[k]["url"], "start_approved": True, "pinned": False, "end_image": None, "end_approved": False, "script_line": r["line"], "motion_plan": mp,
         "motion_confirmed": True, "pace": "one step per second" if stairs else r["pace"].split(",")[0], "subject_motion": "travel" if stairs else "in_place", "prefer_multi_shots": "false",
         "generation": cv, "user_go": None, "fix_note": more[1] if len(more) > 1 else None, "fix_notes_all": [more[1]] if len(more) > 1 else None, "risk_class": "stairs" if stairs else "none",
         "pin_waived": "user 2026-10-01: \"we dont need end frame\"" if stairs else None, "pilot": "confirmed" if stairs else None,
         "taste": ["HT03", "HT04", "HT09", "HT12", "HT22", "HT25", "FP05", "FP07", "FP16", "FP18"],
         "risks": [{"risk": "a second action or a loop", "prevented_by": "one movement named, then rest"}, {"risk": "off model", "prevented_by": "exactly on model from the frame"},
                   {"risk": "the camera travels", "prevented_by": "no camera travel / one straight push"}, {"risk": "a face mouths the lyric", "prevented_by": "the silent clause (HT25, L30)"}],
         "note": f"clip v{cv} of this beat (from the confirmed image {k}, job {u[k]['job']})"}
    (H / f"{b}.v{cv}.call.json").write_text(json.dumps(c, indent=1, ensure_ascii=False)); (H / f"{b}.v{cv}.prompt.txt").write_text(pr)
    res = subprocess.run([sys.executable, str(PF), str(H / f"{b}.v{cv}.call.json")], capture_output=True, text=True)
    print(f"{b}: {len(pr)} chars {r['duration']} s — {'PASS' if res.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in res.stdout.splitlines() if "FAIL" in l]
    fails += res.returncode != 0
sys.exit(1 if fails else 0)
