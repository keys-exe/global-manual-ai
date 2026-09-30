"""stryde-cascade Current 2: §35A video calls for confirmed gap frames (Kie Kling 3.0, one render each).
usage: gap_video.py BEAT...  → calls/<BEAT>.gapv1.json + preflight. Length = the line's span in the v9 edit
(+0.4 skipped opening +0.5, rounded up, min 3) — E6; the rows are not in variants.json yet."""
import json, math, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from fill_gaps import BEATS, B, PF

SPANS = {b: (t0, t1) for b, hk, t0, t1 in json.load(open(B / "work/gap_spans.json"))}
ANAT_CAM = "The camera holds still on the render, one slow even light pulse, nothing else moves."
REAL_CAM = "Handheld phone, a slight natural sway, the camera never follows her."
FACTS = {
 "A2-M2b": "The knee and bones keep their exact shape and count.",
 "A2-M5":  "Exactly one leg, one kneecap, one foot, the step rigid.",
 "A2-M7":  "The tendon and kneecap keep their exact shape; only the glow changes.",
 "A3-B0":  "Her face, phone and chair stay as in the frame; one nod only.",
 "A3-B5":  "Exactly four things on the table and one hand; objects keep their shape.",
 "HK3-B4": "She stays seated on the bed edge; her hands stay in her lap.",
}
NEG = {True: "No text, no arrows, no extra limbs.", False: "No morphing, no extra fingers, no music."}
out = 0
for b in sys.argv[1:]:
    d = next(x for x in BEATS if x["beat"] == b)
    anat = bool(d.get("anatomy"))
    t0, t1 = SPANS[b]
    dur = max(3, math.ceil((t1 - t0) + 0.9))
    prompt = f'For the line "{d["line"]}": from this frame, {d["motion"]}. {ANAT_CAM if anat else REAL_CAM} {FACTS[b]} {NEG[anat]}'
    c = {"beat": b, "connector": "kling", "route": "kie kling-3.0/video (§5)", "mode": 1, "kind": "broll",
         "prompt": prompt, "duration": dur, "resolution": "1080p", "aspect_ratio": "9:16",
         "start_image": str(B / f"renders/gap1/{b}.png"), "start_approved": True,
         "pinned": False, "end_image": None, "end_approved": False,
         "subject_motion": "in_place", "prefer_multi_shots": "false", "generation": 1,
         "script_line": d["line"], "motion_plan": d["motion"], "motion_confirmed": True,
         "risk_class": None, "pilot": None, "taste": d["taste"],
         "risks": [{"risk": "shape drifts", "prevented_by": "one action, shape-and-count fact"},
                   {"risk": "camera wanders", "prevented_by": "one camera clause"},
                   {"risk": "extra limbs/fingers", "prevented_by": "count fact + negative"}]}
    p = B / f"calls/{b}.gapv1.json"
    json.dump(c, open(p, "w"), indent=1, ensure_ascii=False)
    r = subprocess.run(["python3", str(PF), str(p)], capture_output=True, text=True).stdout
    fails = [l.strip() for l in r.splitlines() if l.strip().startswith("FAIL")]
    out += bool(fails)
    print(f"{b:7} {dur}s {len(prompt)} chars {'PASS' if not fails else ' | '.join(fails)}")
sys.exit(1 if out else 0)
