#!/usr/bin/env python3
"""Act 3 clips + T-04a (§35A, Mode 2): one Kling 3.0 clip per confirmed beat image (the user's picks 2026-10-02), the act-map motion verbatim,
≤ 1,000 chars, the no-speech clause first on every face shot (HT25). python3 clips/build_act3_clips.py <BEAT>:<url key> ..."""
import json, subprocess, sys
from pathlib import Path
H = Path(__file__).parent; B = H.parent
PF = B / "../../.claude/skills/ai-prompt-engineer/scripts/preflight.py"
rows = {r["beat"]: r for r in json.load(open(B / "work/actmap_rows.json"))}
urls = json.load(open(B / "body3/urls.json"))
SILENT = "Their lips stay closed and still from the first frame to the last — a silent clip, nobody speaks or sings."
STRAP = "the strap stays rigid and exactly as in the frame — black shell, two peaks, chrome slides"
MOTION = {
 "R-01a": SILENT + " Loretta takes one step forward over the threshold onto the hall floor and lands, her bag swinging a little in her hand, a small smile, eyes ahead into the hall; the open door, the stairs and the hall stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut; she never turns to the lens.",
 "R-02a": SILENT + " At the table she sets the gel tube down beside the pill bottles with one hand and lets go; Loretta, in the foreground, holds her cup still and watches; the table, the bottles and the kitchen stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut; nobody turns to the lens.",
 "R-02b": "Seen from above, her right hand squeezes the white tube once and a short line of clear gel lands on the fingertips of her other hand, then both hands hold still; the tablets, the glass, the ice packs and the old brace on the lace stay exactly as in the frame; nobody speaks. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut; the tube keeps its shape.",
 "R-03a": SILENT + " Loretta leans in a little toward the lens across the table with a half smile and her right hand reaches down toward her own right knee, then stops; the table, her cup and the kitchen stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut; she never turns away.",
 "R-03b": SILENT + " Loretta pulls the rolled khaki hem up a little higher above her right knee with both hands and lets go; on her bare knee " + STRAP + "; the chair and the kitchen stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut; the strap never bends or slides.",
 "R-06a": SILENT + " She lifts her open palm with the strap on it a little toward Loretta and tilts her head, one eyebrow up; on her palm " + STRAP + "; Loretta keeps her cup still and listens; the table and the kitchen stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut; the strap never bends.",
 "T-04a": SILENT + " She watches Loretta dancing beyond, then lowers her eyes and her head a little toward her own right knee, her hand resting on it; beyond the table Loretta and the guests round her keep dancing in place; the table, the glasses and the hall stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut; she never turns to the lens.",
}
HAND = {"R-03b", "R-06a"}
fails = 0
for arg in sys.argv[1:]:
    b, k = arg.split(":"); r = rows[b]; cv = 1
    mp = f"From this frame: {r['action']} — {r['pace']}; camera {r['camera']}"
    pr = f'For the line "{r["line"]}": {mp}. {MOTION[b]}'
    c = {"beat": b, "connector": "kling", "mode": 2, "kind": "broll", "prompt": pr, "duration": r["duration"], "resolution": "1080p", "aspect_ratio": "9:16",
         "start_image": urls[k]["url"], "start_approved": True, "pinned": False, "end_image": None, "end_approved": False, "script_line": r["line"], "motion_plan": mp,
         "motion_confirmed": True, "pace": r["pace"].split(",")[0], "subject_motion": "in_place", "prefer_multi_shots": "false", "generation": cv, "user_go": None,
         "fix_note": None, "fix_notes_all": None, "risk_class": "none", "pin_waived": None, "pilot": None, "taste": ["HT03", "HT04", "HT09", "HT12", "HT22", "HT25", "FP05", "FP07"],
         "risks": [{"risk": "a second action or a loop", "prevented_by": "one movement named, then rest"}, {"risk": "off model", "prevented_by": "exactly on model from the frame"},
                   {"risk": "the camera travels", "prevented_by": "no camera travel, RV sway only"}, {"risk": "a face mouths the lyric", "prevented_by": "the silent clause first (HT25)"}],
         "note": f"clip v{cv} of this beat (from the confirmed image {k}, job {urls[k]['job']})"}
    (H / f"{b}.v{cv}.call.json").write_text(json.dumps(c, indent=1, ensure_ascii=False)); (H / f"{b}.v{cv}.prompt.txt").write_text(pr)
    res = subprocess.run([sys.executable, str(PF), str(H / f"{b}.v{cv}.call.json")], capture_output=True, text=True)
    print(f"{b} clip: {len(pr)} chars {r['duration']} s — {'PASS' if res.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in res.stdout.splitlines() if "FAIL" in l or "WARN" in l]
    fails += res.returncode != 0
sys.exit(1 if fails else 0)
