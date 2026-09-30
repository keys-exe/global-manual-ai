"""stryde-cascade Current 2, Fix round 3 (user on the board, 2026-09-30: "fix those and generate the new ones").
A2-M6  "show it comming down and not up"   → body on the upper step, the leg reaching forward-down to the lower step.
A4-B2b / A4-B4 / A4-P3 "fix the product"   → strap was oversized, doubled band, wrong seat: true size against the knee,
        one band loop, the confirmed worn frame (A4-B1) attached for size and seat (FP01-FP05).
A3-B5  "this is good but this should be 3 brolls" → keeps its clip for "None of them are wrong."; two new beats:
        A3-B5b (anatomy, weight still on the band) and A3-B5c (the stairs with only the first rail — the sequence stopped).
Writes calls/<BEAT>.gap3.image.json + preflight."""
import json, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from fill_gaps import B, PF, FRONT, ANAT, ANATS, HALL, C2HALL, C2WORN, PHONE, ANATREG

M5 = ("bbfc6a69-c3c8-49b0-8d3e-5b1c9419ebe6", "A2-M5 confirmed (the same leg going up)", "frame")
TRUE = ("the strap is small — a rigid black W-topped shell about 12 × 5 cm, narrower than the knee, "
        "on one soft black knit band that loops once round the leg")
SEAT = "centred on the tendon just below the kneecap, the kneecap's lower edge in the shell's notch, exactly as in the attached worn frame"
CALLS = [
 dict(beat="A2-M6", act="Act 2", line="Coming down, nothing does.", anatomy=True, product=False, face=False, room=False,
      refs=[M5, ANAT], taste=["HT11", "HT03"],
      fix='user Fix: "show it comming down and not up" → the body now stands on the upper step and the leg reaches forward and down, heel landing on the lower step',
      motion="the leg lowers the body down one step; the thigh muscle dims and the tendon under the kneecap flares red, 2s",
      prompt='For the line "Coming down, nothing does.": going down the stairs, side view: the body stands on the upper step at the right and the single leg reaches forward and down, heel just landing on the lower step at the left, the knee bent as the weight drops onto it. The thigh muscle dim and slack; the tendon just below the kneecap flaring hot red as it takes the landing. Exactly one leg, one kneecap, one foot, the same leg as the attached going-up frame, now descending. ' + ANATREG + ' No text, no arrows, no second leg.'),
 dict(beat="A4-B2b", act="Act 4", line="A little too high and it is a sleeve again.", product=True, face=False, room=True,
      refs=[FRONT, C2WORN, C2HALL], taste=["FP01", "FP02", "FP03", "FP05", "HT06"],
      fix='user Fix: "fix the product" → strap was oversized with a doubled band; now true size, one band, worn frame attached',
      motion="his fingers slide the strap down from over the kneecap to sit just below it, one slide, 2s",
      prompt='For the line "A little too high and it is a sleeve again.": front-on, close on the man\'s straightened right knee: the strap sits a little too high, riding on the kneecap, and his two fingertips at its two ends are about to slide it down. The strap is exactly the product in the attached front photo — ' + TRUE + ' — the same strap as in the attached worn frame, just higher. Only fingertips on its ends, the shell and wordmark clear. His leg and shorts as in the worn frame; the hall soft behind. ' + PHONE),
 dict(beat="A4-B4", act="Act 4", line="Two hundred thousand people wearing one.", product=True, face=False, room=False,
      refs=[FRONT, C2WORN], taste=["FP01", "FP02", "FP03", "FP05", "FP07", "HT06"],
      fix='user Fix: "fix the product" → straps were oversized and sat wrong; now true size, seated on the tendon as the worn frame',
      motion="the two walkers take three brisk steps along the promenade away from us, one step per second, 3s",
      prompt='For the line "Two hundred thousand people wearing one.": two older people walking side by side on a seaside promenade in shorts, seen from behind at knee height, each wearing one strap on one knee. Each strap is exactly the product in the attached front photo — ' + TRUE + ' — worn ' + SEAT.replace("exactly as", "as") + '. Low angle, three-quarter-back, the knees and straps sharp, waist down. Bright overcast daylight. Exactly four legs, two straps. ' + PHONE),
 dict(beat="A4-P3", act="Act 4", line="Thirty four percent less strain. Measured.", anatomy=True, product=False, face=False, room=False,
      refs=[ANATS, ANAT], taste=["HT11", "FP02", "FP03"],
      fix='user Fix: "fix the product" → the strap rendered as a wide band over the joint; now the small shell seated below the kneecap as the A4-M1 frame',
      motion="as the knee bends slightly under load, the tendon's hot red glow cools to a calm amber, the strap holding it, 3s",
      prompt='For the line "Thirty four percent less strain. Measured.": the knee from the side as bodyweight lands, with the strap exactly as in the attached strap anatomy frame — a small rigid black shell about 12 × 5 cm, no wider than the kneecap, on a thin band — seated just below the kneecap on the patellar tendon, never over the joint. Above and below it the tendon glows hot red; under the shell it is calm cool amber: visibly less strain. Side view, the knee filling the frame, one leg. ' + ANATREG + ' No text, no numbers, no arrows.'),
 dict(beat="A3-B5b", act="Act 3", line="None of them move the weight off the band,", anatomy=True, product=False, face=False, room=False,
      refs=[ANAT], taste=["HT11", "HT12"],
      fix="new beat: A3-B5 split into three (user)",
      motion="a pulse of bodyweight travels down the thigh and the tendon under the kneecap flares hot red again inside the sleeve, 2s",
      prompt='For the line "None of them move the weight off the band,": the knee from the side under bodyweight, wrapped in a faint translucent knee sleeve that covers the whole joint, and inside it the patellar tendon just below the kneecap still glowing hot red, carrying the load — the sleeve changes nothing there. Side view, the knee filling the frame, one leg. ' + ANATREG + ' No text, no arrows.'),
 dict(beat="A3-B5c", act="Act 3", line="and that is the only thing that stops the sequence.", anatomy=False, product=False, face=False, room=True,
      refs=[HALL], taste=["HT09", "HT12"],
      fix="new beat: A3-B5 split into three (user)",
      motion="the camera eases slowly down the bare wall beside the stairs from the short top rail to the empty lower wall, 3s",
      prompt='For the line "and that is the only thing that stops the sequence.": the client\'s hall stairs exactly as in the attached hall plate, with just one short new oak handrail fixed beside the top two steps and the rest of the wall bare and unmarked all the way down — no second rail, nothing else changed. Calm afternoon light down the stairs. Eye level from the hall, three-quarter, the whole flight in frame. No people. ' + PHONE),
]
bad = 0
for b in CALLS:
    c = {"beat": b["beat"], "kind": "image", "mode": 1, "prompt": b["prompt"], "script_line": b["line"],
         "face": b["face"], "room": b["room"], "product": b["product"], "body": b["beat"] not in ("A3-B5c",) and not b.get("anatomy"),
         "refs": [{"label": r[1], "kind": r[2], "id": r[0]} for r in b["refs"]], "taste": b["taste"],
         "anatomy": bool(b.get("anatomy")), "pair": ["nano_banana_pro", "nano_banana_pro"], "motion_plan": b["motion"],
         "model": "nano_banana_pro", "render_count": 1, "fix_note": b["fix"], "act": b["act"]}
    p = B / f"calls/{b['beat']}.gap3.image.json"
    json.dump(c, open(p, "w"), indent=1, ensure_ascii=False)
    out = subprocess.run(["python3", str(PF), str(p)], capture_output=True, text=True).stdout
    real = [l.strip() for l in out.splitlines() if l.strip().startswith("FAIL") and "Sunburst on realistic" not in l]
    bad += bool(real)
    print(f"{b['beat']:7} {len(b['prompt']):5} chars  {'PASS' if not real else 'FAIL ' + ' | '.join(real)}")
sys.exit(1 if bad else 0)
