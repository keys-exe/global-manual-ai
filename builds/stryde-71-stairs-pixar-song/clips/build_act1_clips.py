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
fails = 0
for arg in sys.argv[1:]:
    b, iv = arg.split(":"); r = rows[b]; k = f"{b}@v2A"
    mp = f"From this frame: {r['action']} — {r['pace']}; camera {r['camera']}"
    pr = f'For the line "{r["line"]}": {mp}. {MOTION[b]}'
    c = {"beat": b, "connector": "kling", "mode": 2, "kind": "broll", "prompt": pr, "duration": DUR[b], "resolution": "1080p", "aspect_ratio": "9:16",
         "start_image": urls[k], "start_approved": True, "pinned": False, "end_image": None, "end_approved": False, "script_line": r["line"], "motion_plan": mp,
         "motion_confirmed": True, "pace": r["pace"].split(",")[0], "subject_motion": "in_place", "prefer_multi_shots": "false", "generation": 1, "user_go": None,
         "fix_note": None, "risk_class": "none", "pin_waived": None, "pilot": None, "taste": ["HT03", "HT04", "HT09", "HT12", "HT22"],
         "risks": [{"risk": "a second action or a loop", "prevented_by": "one movement named, then rest"}, {"risk": "off model", "prevented_by": "exactly on model from the frame"},
                   {"risk": "the camera travels", "prevented_by": "no camera travel, RV sway only"}],
         "note": f"first clip of this beat (from the confirmed image v{iv} A, job {jobs[k]})"}
    (H / f"{b}.v1.call.json").write_text(json.dumps(c, indent=1, ensure_ascii=False)); (H / f"{b}.v1.prompt.txt").write_text(pr)
    res = subprocess.run([sys.executable, str(PF), str(H / f"{b}.v1.call.json")], capture_output=True, text=True)
    print(f"{b} clip: {len(pr)} chars {DUR[b]} s — {'PASS' if res.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in res.stdout.splitlines() if "FAIL" in l]
    fails += res.returncode != 0
sys.exit(1 if fails else 0)
