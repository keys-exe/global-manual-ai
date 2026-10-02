#!/usr/bin/env python3
"""Act 2 clips (§35A, Mode 2): one Kling 3.0 clip per confirmed beat image (the user's picks 2026-10-02), the act-map motion verbatim,
≤ 1,000 chars, the no-speech clause first on every face shot (HT25). python3 clips/build_act2_clips.py <BEAT>:<img key> ..."""
import json, subprocess, sys
from pathlib import Path
H = Path(__file__).parent; B = H.parent
PF = B / "../../.claude/skills/ai-prompt-engineer/scripts/preflight.py"
rows = {r["beat"]: r for r in json.load(open(B / "work/actmap_rows.json"))}
urls = json.load(open(B / "body/urls.json")); jobs = json.load(open(B / "body/jobs.json"))
SILENT = "Their lips stay closed and still from the first frame to the last — a silent clip, nobody speaks or sings."
MOTION = {
 "T-01a": SILENT + " The bride and her grandmother rock together slowly once to one side and back in the hug, eyes closed, smiling, arms around each other; the hall, the lights and the balloon arch behind stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; nobody else moves; no cut.",
 "T-01b": "Her lips stay closed in a grin from the first frame to the last — a silent clip, she never speaks or sings. Her two raised hands wave once side to side above her head on the beat and stay up, her eyes on the dancers beside her; the guest at the left edge and the hall behind stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut; she never turns to the lens.",
 "T-03a": "On the X-ray, the red-orange glow where bone meets bone in each knee swells brighter once and fades back, slowly; the bones stay still and rigid, the blue-white X-ray look and the dark field exactly as in the frame. Stylized 3D animation, exactly on model from the frame. The camera pushes in slowly on one straight axis, nothing more; nothing else moves; nobody speaks; no cut.",
 "T-04a": "Her lips stay closed and still from the first frame to the last — a silent clip, nobody speaks or sings. She watches Loretta dancing beyond, then lowers her eyes and her head a little toward her own right knee, her hand resting on it; beyond the table, Loretta keeps dancing in place, arms up; the table, the glasses and the hall stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut; she never turns to the lens.",
 "T-04b": "Her right hand rubs slowly across her knee once through the burgundy chiffon and rests on it; her gold heels stay on the parquet; the dancing feet beyond keep stepping, soft and out of focus; the tablecloth and the chair stay exactly as in the frame; nobody speaks. Stylized 3D animation, exactly on model from the frame. No camera travel; nobody else in focus; no cut.",
}
MOTION["T-02a"] = "Her lips stay closed in a grin from the first frame to the last — a silent clip, nobody speaks or sings. Loretta, at the front nearest the lens, takes one side step to her right on the beat and lands, the guests in the line behind her stepping with her in unison; arms loose, the hall and the lights stay exactly as in the frame. Stylized 3D animation, exactly on model from the frame. No camera travel; no cut; nobody turns to the lens."
MOTION["T-02b"] = "Her white slip-on nearest the lens steps forward once and lands flat on the parquet, the other foot following, the dress shoes and gold heels beside her stepping forward with her in unison; the fuchsia hem sways with the step; the parquet and the lights stay exactly as in the frame; nobody speaks. Stylized 3D animation, exactly on model from the frame. No camera travel; nobody else in focus; no cut."
fails = 0
for arg in sys.argv[1:]:
    b, k = arg.split(":"); r = rows[b]; cv = 1
    mp = f"From this frame: {r['action']} — {r['pace']}; camera {r['camera']}"
    pr = f'For the line "{r["line"]}": {mp}. {MOTION[b]}'
    c = {"beat": b, "connector": "kling", "mode": 2, "kind": "broll", "prompt": pr, "duration": r["duration"], "resolution": "1080p", "aspect_ratio": "9:16",
         "start_image": urls[k], "start_approved": True, "pinned": False, "end_image": None, "end_approved": False, "script_line": r["line"], "motion_plan": mp,
         "motion_confirmed": True, "pace": r["pace"].split(",")[0], "subject_motion": "in_place", "prefer_multi_shots": "false", "generation": cv, "user_go": None,
         "fix_note": None, "fix_notes_all": None, "risk_class": "none", "pin_waived": None, "pilot": None, "taste": ["HT03", "HT04", "HT09", "HT12", "HT22", "HT25"],
         "risks": [{"risk": "a second action or a loop", "prevented_by": "one movement named, then rest"}, {"risk": "off model", "prevented_by": "exactly on model from the frame"},
                   {"risk": "the camera travels", "prevented_by": "no camera travel, RV sway only"}, {"risk": "a face mouths the lyric", "prevented_by": "the silent clause first (HT25)"}],
         "note": f"clip v{cv} of this beat (from the confirmed image {k}, job {jobs[k]})"}
    (H / f"{b}.v{cv}.call.json").write_text(json.dumps(c, indent=1, ensure_ascii=False)); (H / f"{b}.v{cv}.prompt.txt").write_text(pr)
    res = subprocess.run([sys.executable, str(PF), str(H / f"{b}.v{cv}.call.json")], capture_output=True, text=True)
    print(f"{b} clip: {len(pr)} chars {r['duration']} s — {'PASS' if res.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in res.stdout.splitlines() if "FAIL" in l]
    fails += res.returncode != 0
sys.exit(1 if fails else 0)
