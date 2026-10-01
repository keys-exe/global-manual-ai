"""stryde-cascade Current 2: §35A video calls for confirmed gap frames (Kie Kling 3.0, one render each).
usage: gap_video.py [--gen 2 --fix "diagnosis → change"] BEAT...  → calls/<BEAT>.gapv<gen>.json + preflight.
Line, motion plan and taste come from the beat's newest image call (calls/<BEAT>.gapN.image.json); the start frame is
its newest render (renders/gapN/<BEAT>.png). Length = the line's span in the v9 edit + 0.4 skipped opening + 0.5,
rounded up, min 3 (E6) — the rows are not in variants.json yet."""
import argparse, json, math, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from fill_gaps import B, PF

SPANS = {b: (t0, t1) for b, hk, t0, t1 in json.load(open(B / "work/gap_spans.json"))}
ANAT_CAM = "The camera holds still on the render, one slow even light pulse, nothing else moves."
REAL_CAM = "Handheld phone, a slight natural sway, the camera never follows the subject."
FACTS = {
 "A2-M2b": "The knee and bones keep their exact shape and count.",
 "A2-M5":  "Exactly one leg, one kneecap, one foot, the step rigid.",
 "A2-M6":  "Exactly one leg, one kneecap, one foot, both steps rigid.",
 "A2-M7":  "The tendon and kneecap keep their exact shape; only the glow changes.",
 "A3-B0":  "Her face, phone and chair stay as in the frame; one nod only.",
 "A3-B5":  "Exactly four things on the table and one hand; objects keep their shape.",
 "A3-B5b": "The knee, sleeve and bones keep their exact shape; only the glow changes.",
 "A3-B5c": "The stairs, the one short rail and the bare wall keep their exact shape.",
 "HK3-B4": "She stays seated on the bed edge; her hands stay in her lap.",
 "A1-B1b": "The stairs keep the same steps; she stays on the same step, one foot lifting only.",
 "A1-B2b": "The stairs keep the same steps; she climbs exactly one step, slowly.",
 "HK2-B0": "The rail stays leaning on the wall; the stairs and wall keep their shape.",
 "HK2-B3": "He stays seated in the van door; phone and hand stay at his ear.",
 "A4-B2b": "The small strap stays rigid in one piece, one band; fingertips only on its ends.",
 "A4-B3":  "The knee model stays upright and still; the small strap stays rigid; one gloved hand only.",
 "A4-P3":  "The small strap stays rigid below the kneecap; only the glow changes.",
 "A5-M1":  "The small black strap is a rigid printed object: its shape, band and wordmark never change or move.",
 "A5-B4b": "He steps down one step only; the small strap stays rigid below his kneecap.",
 "A5-P2":  "The box and exactly two small straps stay still and rigid; one hand only.",
 "A4-B1b": "The small strap stays rigid below the kneecap; one leg, bones keep their shape.",
 "A4-B4":  "Exactly six legs and three small straps, all rigid; the people stay seated.",
 "A5-B1":  "Exactly two small straps, rigid; his face and hands keep their shape.",
 "A5-B1b": "The diary stays on his knee; his hands stay clear of the wheel.",
}
# a Fix that changes the confirmed motion (user's words) — the card's motionPlan is updated to match
MOTION = {"A4-B3": "the gloved hand holds the knee model still while the camera eases slowly in towards the strap, the model never turning, 2s",
          "A4-P3": "as the knee bends slightly under load, the tendon's hot red glow cools to a calm cool blue under the strap, the strap holding it, 3s"}
NEG = {True: "No text, no arrows, no extra limbs.", False: "No morphing, no extra fingers, no music."}
NEG_M1 = "No warping of the strap, no text changes, no extra limbs."
RISK = {"A1-B1b": "stairs", "A1-B2b": "stairs", "A5-B4b": "stairs", "A4-B3": "hand_product", "A4-B2b": "hand_product", "A5-B1": "hand_product"}
WAIVE = 'user, 2026-09-30: "Run from the start frame" (asked: clips without a picked end frame — this board has no end-frame step)'

def newest(b):
    for n in (5, 4, 3, 2, 1):
        c = B / f"calls/{b}.gap{n}.image.json"
        if c.exists():
            img = B / f"renders/gap{n}/{b}.png"
            return json.load(open(c)), img
    raise SystemExit(f"no image call for {b}")

ap = argparse.ArgumentParser(); ap.add_argument("beats", nargs="+"); ap.add_argument("--gen", type=int, default=1); ap.add_argument("--fix", default=""); ap.add_argument("--tag", default="")
a = ap.parse_args()
out = 0
for b in a.beats:
    ic, img = newest(b)
    anat = bool(ic.get("anatomy"))
    if b in MOTION: ic["motion_plan"] = MOTION[b]
    t0, t1 = SPANS[b]
    dur = max(3, math.ceil((t1 - t0) + 0.9))
    neg = NEG_M1 if b == "A5-M1" else NEG[anat]
    cam = ANAT_CAM if anat else REAL_CAM
    if b == "A5-M1": cam = "The camera is locked off; nothing moves except the glow."
    prompt = f'For the line "{ic["script_line"]}": from this frame, {ic["motion_plan"]}. {cam} {FACTS[b]} {neg}'
    rc = RISK.get(b)
    c = {"beat": b, "connector": "kling", "route": "kie kling-3.0/video (§5)", "mode": 1, "kind": "broll",
         "prompt": prompt, "duration": dur, "resolution": "1080p", "aspect_ratio": "9:16",
         "start_image": str(img), "start_approved": True, "pinned": False, "end_image": None, "end_approved": False,
         "subject_motion": "in_place", "prefer_multi_shots": "false", "generation": a.gen,
         "script_line": ic["script_line"], "motion_plan": ic["motion_plan"], "motion_confirmed": True,
         "risk_class": rc, "pilot": "confirmed" if rc else None, "pin_waived": WAIVE if rc else None,
         "taste": ic["taste"],
         "risks": [{"risk": "shape drifts", "prevented_by": "one action, shape-and-count fact"},
                   {"risk": "camera wanders", "prevented_by": "one camera clause"},
                   {"risk": "extra limbs/fingers", "prevented_by": "count fact + negative"}]}
    if a.gen >= 2: c["fix_note"] = a.fix
    p = B / f"calls/{b}.gapv{a.gen}{a.tag}.json"
    json.dump(c, open(p, "w"), indent=1, ensure_ascii=False)
    r = subprocess.run(["python3", str(PF), str(p)], capture_output=True, text=True).stdout
    fails = [l.strip() for l in r.splitlines() if l.strip().startswith("FAIL")]
    out += bool(fails)
    print(f"{b:7} {dur}s {len(prompt)} chars {img.parent.name} {'PASS' if not fails else ' | '.join(fails)}")
sys.exit(1 if out else 0)
