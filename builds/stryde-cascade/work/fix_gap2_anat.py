"""stryde-cascade Current 2, Fix round (user, 2026-09-30):
A2-M6 "fix this distortions" — two legs crossed, a second kneecap → one leg only, clean side profile, the confirmed A2-M5 frame as the leg reference.
A4-B1b "anatomy here" — real knee → anatomy render of the strap on the tendon as the knee bends.
Writes calls/<BEAT>.gap2.image.json + preflight."""
import json, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from fill_gaps import B, PF, ANAT, ANATS, ANATREG

M5 = ("bbfc6a69-c3c8-49b0-8d3e-5b1c9419ebe6", "A2-M5 confirmed (the same leg going up)", "frame")
CALLS = [
 dict(beat="A2-M6", line="Coming down, nothing does.", refs=[M5, ANAT], taste=["HT11"],
      fix='user Fix: "fix this distortions" → two legs crossed with a second kneecap; now exactly one leg in clean side profile, A2-M5 attached as the leg',
      motion="the leg lowers the body down one step; the thigh muscle dims and the tendon under the kneecap flares red, 2s",
      prompt='For the line "Coming down, nothing does.": the same single leg as the attached going-up frame, now stepping down: side view, the knee bent as the body drops onto the lower step, the thigh muscle dim and slack, and the tendon just below the kneecap flaring hot red as it takes the whole landing. Exactly one leg, hip to foot, in clean side profile: one thigh bone, one kneecap, one shin, one foot flat on a simple translucent step. The other leg out of frame. ' + ANATREG + ' No text, no arrows, no second leg.'),
 dict(beat="A4-B1b", line="It never crosses the joint.", refs=[ANATS, ANAT], taste=["HT11", "FP03", "FP02"],
      fix='user Fix: "anatomy here" → real-knee photo replaced by an anatomy render of the strap on the tendon',
      motion="the knee bends slowly to a right angle and back; the strap stays on the tendon below the kneecap and never crosses the joint, 2s",
      prompt='For the line "It never crosses the joint.": the knee from the side, bent halfway as it moves, with the small rigid black strap exactly as in the attached strap anatomy frame, wrapped just below the kneecap on the patellar tendon. The joint line glows a soft cool blue above the strap and the bend happens there, above it; the strap sits wholly on the tendon below, never over the kneecap or the joint. Side view, the knee filling the frame, one leg. ' + ANATREG + ' No text, no arrows.'),
]
bad = 0
for b in CALLS:
    c = {"beat": b["beat"], "kind": "image", "mode": 1, "prompt": b["prompt"], "script_line": b["line"],
         "face": False, "room": False, "product": False, "body": False,
         "refs": [{"label": r[1], "kind": r[2], "id": r[0]} for r in b["refs"]], "taste": b["taste"],
         "anatomy": True, "pair": ["nano_banana_pro", "nano_banana_pro"], "motion_plan": b["motion"],
         "model": "nano_banana_pro", "render_count": 1, "fix_note": b["fix"]}
    p = B / f"calls/{b['beat']}.gap2.image.json"
    json.dump(c, open(p, "w"), indent=1, ensure_ascii=False)
    out = subprocess.run(["python3", str(PF), str(p)], capture_output=True, text=True).stdout
    real = [l.strip() for l in out.splitlines() if l.strip().startswith("FAIL")]
    bad += bool(real)
    print(f"{b['beat']:7} {len(b['prompt']):5} chars  {'PASS' if not real else 'FAIL ' + ' | '.join(real)}")
sys.exit(1 if bad else 0)
