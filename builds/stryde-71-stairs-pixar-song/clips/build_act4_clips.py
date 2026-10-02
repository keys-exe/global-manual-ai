#!/usr/bin/env python3
"""Clips from the user's picks 2026-10-02 10:20–10:23: M-01a, M-04a, M-06a (Act 4), R-04a, R-07a (Act 3; R-07a one take for both lines, 9 s).
§35A, ≤ 1,000 chars, no speech marks in the line (L30), lips sealed on face shots."""
import json, subprocess, sys, re
from pathlib import Path
H = Path(__file__).parent; B = H.parent
PF = B / "../../.claude/skills/ai-prompt-engineer/scripts/preflight.py"
rows = {r["beat"]: r for r in json.load(open(B / "work/actmap_rows.json"))}
u = json.load(open(B / "body4/urls.json"))
SEAL = "Her lips stay sealed and her jaw still from the first frame to the last, her face holding the expression of the frame — a silent clip, nobody speaks or sings."
STRAP = "the strap stays rigid and exactly as in the frame — black shell, two peaks, chrome slides"
C = {
 "M-01a": ("M-01a@v1B", None, SEAL + " Lying on the treatment table, she lets her head settle back into the pillow once, eyes closed, and rests; her hands stay on her stomach; the heat pad stays on her knee; the room stays exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut."),
 "M-04a": ("M-04a@v1A", "From this frame: nothing moves, held — about two seconds; camera R4 — a slow single-axis push in on a stabilised virtual rig",
           "The camera pushes in slowly on one straight axis toward the heap; the braces, sleeves, bottles, gel tube, ice pack and syringe box stay perfectly still exactly as in the frame; nobody speaks; nobody in the frame. Stylized 3D animation, exactly on model from the frame. No cut."),
 "M-06a": ("M-06a@v1C", None, "Her right slipper lands flat on the step's carpet runner and her weight settles onto it, once; on her bare right knee " + STRAP + "; the brass rod and the stairs stay exactly as in the frame; nobody speaks. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut; the strap never slides."),
 "R-04a": ("R-04a@v7A", "From this frame: one tap on the strap — one tap, about a second; camera R4 — a slow single-axis push in on a stabilised virtual rig",
           "Her right fingertip taps the top of the shell once and rests on it; on her right knee " + STRAP + "; her left knee stays bare; nobody speaks. Stylized 3D animation, exactly on model from the frame. The camera pushes in slowly on one straight axis, nothing more; no cut; the strap never bends."),
 "R-07a": ("R-07a@v8A", "From this frame: she walks down the whole flight toward the lens, one step a second, facing forwards, hands off the rail, to the hall floor; camera RV sway — the virtual camera breathes in place, never travels",
           SEAL + " One continuous walk down: right foot, then left, one step per tread, each foot flat on the runner, hands loose at her sides off the rail, a proud smile, to the hall floor; on her right knee " + STRAP + "; the stairs and photo wall stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut; no skipped step."),
}
# M-01a clip v1 kept off (L16): her mouth opened as her head settled (HT25) → v2 holds her still and moves only the camera
C["M-01a"] = ("M-01a@v1B", "From this frame: nothing moves, held — she rests still, about two seconds; camera R4 — a slow single-axis push down toward her face on a stabilised virtual rig",
           SEAL + " She lies still on the treatment table, eyes closed, a calm resting face, breathing unseen; her hands stay on her stomach; the heat pad stays on her knee; the room stays exactly as in the frame. Stylized 3D animation, exactly on model from the frame. The camera pushes down slowly on one straight axis, nothing more; no cut.", 2,
           'kept off clip v1: her mouth opened as her head settled → held still, camera push only')
fails = 0
for b in (sys.argv[1:] or C):
    k, mp, mt, *more = C[b]; r = rows[b]; cv = more[0] if more else 1
    line = re.sub(r'["“”]', "", r["line"])
    mp = mp or f"From this frame: {r['action']} — {r['pace']}; camera {r['camera']}"
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
