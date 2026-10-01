#!/usr/bin/env python3
"""Act 1 clips (§35A, Mode 2): one Kling 3.0 clip per confirmed beat image, the motionPlan verbatim, ≤ 1,000 chars, preflight kind broll.
python3 clips/build_act1_clips.py <BEAT>:<imgver> ...  → clips/<BEAT>.v1.call.json + .prompt.txt, runs preflight."""
import json, subprocess, sys
from pathlib import Path
H = Path(__file__).parent; B = H.parent
PF = B / "../../.claude/skills/ai-prompt-engineer/scripts/preflight.py"
rows = {r["beat"]: r for r in json.load(open(B / "work/actmap_rows.json"))}
urls = json.load(open(B / "body/urls.json")); jobs = json.load(open(B / "body/jobs.json"))
MOTION = {
 "P-03a": "In close on her knee, her right hand hauls the brace's top strap up over the kneecap in one pull, holds a moment, and the brace sags back down below the kneecap as the hand eases; her left hand stays on the table edge; the knee, the slipper and the kitchen behind stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame, the brace rigid in shape. No camera travel; nobody else; no cut; the brace never changes design.",
 "P-04a": "Overhead on the table, her two hands push outward once and the heap slides apart a little across the wood — a bottle tips and rolls a few centimetres, a sleeve slips — then the hands rest flat on the table; nothing new appears on it. Stylized 3D animation, every object exactly as in the frame, rigid in shape. No camera travel; nobody else; no cut; the hands stay in frame.",
 "P-04b": "The therapist's two hands bend her right knee a little further toward her chest, slowly, and hold it there; she stays on her back, head on the pillow, eyes on the ceiling, hands folded on her stomach; the therapist's head stays out of frame above. Stylized 3D animation, both exactly on model from the frame. No camera travel; no third person; no cut; nobody turns to the lens.",
 "P-05a": "The back of her right hand pushes the heap once across the table away from her, the bottles and sleeves sliding to the far edge, then she sits back in the chair, shoulders dropping, eyes on nothing past the lens, her left hand slack in her lap. Stylized 3D animation, exactly on model from the frame, every object rigid. No camera travel; nobody else; no cut; she never looks into the lens.",
}
DUR = {"P-03a": 5, "P-04a": 4, "P-04b": 5, "P-05a": 6}
MOTION["P-01b"] = "In close at step height, she steps backwards down the flight: the lower slipper's heel settles on the step below and takes her weight, then the upper foot lifts and reaches back and down to join it — each foot moves downward and away from the top, toes always pointing up the stairs; the hand stays on the rail; nobody speaks. Stylized 3D animation, exactly on model from the frame. No camera travel; nobody else; no cut; the feet never turn around or climb."
MOTION["P-02a"] = "From the hall floor looking up the flight, she looks down the stairs toward the lens, holds, then turns her face away to the side, her mouth closed the whole time — she never speaks or sings, her lips still; her hand stays on the newel, she stays seated on the top step; the staircase stays exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; nobody else; no cut; she never stands."
MOTION["P-05a"] = "The back of her right hand pushes the heap once across the table to its far edge — every bottle, sleeve and brace slides and stays on the table — then she sits back in the chair, shoulders dropping, her mouth closed and her lips still from the first frame to the last, she never speaks or sings, eyes on nothing past the lens, her left hand slack in her lap. Stylized 3D animation, exactly on model from the frame, every object rigid and present to the last frame. No camera travel; nobody else; no cut."
DUR.update({"P-01b": 4, "P-02a": 6})
FIXN = {"P-01b": "user Fix: this should be stepping backwards → each foot moves down and away from the top, toes up the stairs, the feet never climb; nobody speaks (§35A rule 6)",
        "P-02a": "user: never talk the lyrics/script in B-roll → mouth closed, lips still, she never speaks or sings (§35A rule 6, HT25)",
        "P-05a_old": "user: make this into 3 brolls (the beat split; this clip re-cut to its own line) · §22X on v1: the heap vanished and her mouth moved → prompt: every object stays on the table to the last frame, mouth closed, she never speaks"}
fails = 0
for arg in sys.argv[1:]:
    parts = arg.split(":"); b, iv = parts[0], parts[1]; k = parts[2] if len(parts) > 2 else f"{b}@v2A"; cv = int(parts[3]) if len(parts) > 3 else 1; r = rows[b]
    if b == "P-05a": DUR[b] = r["duration"]
    mp = f"From this frame: {r['action']} — {r['pace']}; camera {r['camera']}"
    pr = f'For the line "{r["line"]}": {mp}. {MOTION[b]}'
    USERGO = {"P-05a": 'user 2026-10-01: "i want new ones on the brolls. i dont like these, you should never talk the lyrics/script in broll"'}
    if cv >= 3: FIXN[b] = "user: never talk the lyrics/script in B-roll (third generation on the user's own ask) → mouth closed and lips still first frame to last, she never speaks or sings (§35A rule 6, HT25)"
    c = {"beat": b, "connector": "kling", "mode": 2, "kind": "broll", "prompt": pr, "duration": DUR[b], "resolution": "1080p", "aspect_ratio": "9:16",
         "start_image": urls[k], "start_approved": True, "pinned": False, "end_image": None, "end_approved": False, "script_line": r["line"], "motion_plan": mp,
         "motion_confirmed": True, "pace": r["pace"].split(",")[0], "subject_motion": "in_place", "prefer_multi_shots": "false", "generation": cv, "user_go": USERGO.get(b) if cv >= 3 else None,
         "fix_note": FIXN.get(b) if cv > 1 else None, "risk_class": "none", "pin_waived": None, "pilot": None, "taste": ["HT03", "HT04", "HT09", "HT12", "HT22"],
         "risks": [{"risk": "a second action or a loop", "prevented_by": "one movement named, then rest"}, {"risk": "off model", "prevented_by": "exactly on model from the frame"},
                   {"risk": "the camera travels", "prevented_by": "no camera travel, RV sway only"}],
         "note": f"clip v{cv} of this beat (from the confirmed image v{iv} {k[-1]}, job {jobs[k]})"}
    (H / f"{b}.v{cv}.call.json").write_text(json.dumps(c, indent=1, ensure_ascii=False)); (H / f"{b}.v{cv}.prompt.txt").write_text(pr)
    res = subprocess.run([sys.executable, str(PF), str(H / f"{b}.v{cv}.call.json")], capture_output=True, text=True)
    print(f"{b} clip: {len(pr)} chars {DUR[b]} s — {'PASS' if res.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in res.stdout.splitlines() if "FAIL" in l]
    fails += res.returncode != 0
sys.exit(1 if fails else 0)
