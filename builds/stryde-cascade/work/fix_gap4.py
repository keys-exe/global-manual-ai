"""stryde-cascade Current 2, Fix round 4 (user on the board, 2026-09-30). Writes calls/<BEAT>.gap4.image.json + preflight.
A4-B1b "product placement is too low"  → strap was on the shin; seat it right under the kneecap, notch hugging its lower edge.
A4-B3  "remove that excess strap inside the silicon pad" → a second band and grey inner strip showed; one band, clean shell, below the kneecap.
A4-B4  "i need a new style of image"   → promenade from behind replaced by three people on a park bench, front-on, knees in frame.
A5-B1  "this should be at his bag"     → straps go into his open tool bag on the van floor, not the shelf box.
A5-B1b "distorted image"               → hand/diary/wheel tangled; diary resting on his knee, pen hand only, wheel behind.
HK2-B0 "this is distorted i need a new image" → rail on the shoulder warped; rail now leans against the wall, tape measure in hand."""
import json, subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from fill_gaps import B, PF, FRONT, FITTER, ANAT, ANATS, HALL, VAN, C2WORN, PHONE, ANATREG

TRUE = ("the strap is small — a rigid black W-topped shell about 12 × 5 cm, narrower than the knee, "
        "on one soft black knit band that loops once round the leg")
OUTFIT = "a worn tan canvas work jacket open over a dark green work shirt, charcoal work trousers"
CALLS = [
 dict(beat="A4-B1b", line="It never crosses the joint.", anatomy=True, product=False, face=False, room=False,
      refs=[ANATS, ANAT], taste=["HT11", "FP02", "FP03"],
      fix='user Fix: "product placement is too low" → strap sat on the shin; now right under the kneecap, the notch hugging its lower edge',
      motion="the knee bends slowly to a right angle and back; the strap stays on the tendon below the kneecap and never crosses the joint, 2s",
      prompt='For the line "It never crosses the joint.": the knee from the side, bent halfway, with the small rigid black strap exactly as in the attached strap anatomy frame seated high on the patellar tendon, right under the kneecap — the kneecap\'s lower edge sits in the shell\'s notch, no gap between them, not down on the shin. The joint line glows a soft cool blue just above; the bend happens there, above the strap. Side view, the knee filling the frame, one leg. ' + ANATREG + ' No text, no arrows.'),
 dict(beat="A4-B3", line="Three years with orthopedic surgeons.", anatomy=False, product=True, face=False, room=True,
      refs=[FRONT, C2WORN], taste=["FP01", "FP02", "FP03", "FP05", "HT06"],
      fix='user Fix: "remove that excess strap inside the silicon pad" → a second band and grey inner strip showed; now one band, clean shell',
      motion="a gloved hand turns the knee model a quarter turn to show the strap on the tendon, one turn, 2s",
      prompt='For the line "Three years with orthopedic surgeons.": on a clean clinic desk, a white life-size knee joint model, and a clinician\'s gloved hand holding its base. The strap is fitted just below the model\'s kneecap on its tendon, exactly the product in the attached front photo — ' + TRUE + ' — one band only, fastened once behind, the black shell clean with nothing inside or under it. Seated as in the attached worn frame. Eye level, close, the model and strap sharp; a plain clinic room soft behind. One hand, no face, nothing written. ' + PHONE),
 dict(beat="A4-B4", line="Two hundred thousand people wearing one.", anatomy=False, product=True, face=False, room=False,
      refs=[FRONT, C2WORN], taste=["FP01", "FP02", "FP03", "FP07", "HT06", "HT01"],
      fix='user Fix: "i need a new style of image" → new idea: three people side by side on a park bench, front-on, each wearing one strap',
      motion="the camera glides slowly past the three knees from left to right while they sit still, 3s",
      prompt='For the line "Two hundred thousand people wearing one.": front-on at knee height, three different older people sit side by side on a wooden park bench in shorts and summer clothes, seen from the waist down, each wearing one strap on one knee. Each strap is exactly the product in the attached front photo — ' + TRUE + ' — centred on the tendon just below the kneecap as in the attached worn frame. Different skin tones, shoes and shorts; sunny park path and grass soft behind. Exactly six legs, three straps. ' + PHONE),
 dict(beat="A5-B1", line="I started carrying a couple because I was tired of fitting the second rail.", anatomy=False, product=True, face=True, room=True,
      refs=[FRONT, FITTER, VAN], taste=["FP01", "FP02", "HT06", "HT09"],
      fix='user Fix: "this should be at his bag and not there" → straps now go into his open tool bag on the van floor',
      motion="crouched by his open tool bag on the van floor, he drops two straps into its side pocket, one drop, 2s",
      prompt='For the line "I started carrying a couple because I was tired of fitting the second rail.": in the open back of his van the fitter crouches by his open black canvas tool bag on the van floor and drops two straps into its side pocket among his screwdrivers and tape measure. Each strap is exactly the product in the attached front photo — ' + TRUE + '. Eye level, three-quarter, medium shot, his face and hands visible. He is the same man as the attached cast sheet, in ' + OUTFIT + '. The van as in the attached van plate. ' + PHONE),
 dict(beat="A5-B1b", line="Three houses this year have not called me back.", anatomy=False, product=False, face=True, room=True,
      refs=[FITTER, VAN], taste=["HT12", "HT09"],
      fix='user Fix: "distorted image" → hand, diary and wheel were tangled; diary now rests on his knee, one pen hand, wheel behind',
      motion="sitting in the driver's seat, he runs his pen down the diary page on his knee and smiles slightly, one stroke, 2s",
      prompt='For the line "Three houses this year have not called me back.": the fitter sits sideways in the driver\'s seat of his van, door open, a paper job diary resting open on his knee, his right hand running a pen down the page and his left hand holding the diary\'s edge, a small satisfied smile. The steering wheel behind him, his hands clear of it. Eye level through the open door, three-quarter, medium shot, his face sharp. He is the same man as the attached cast sheet, in ' + OUTFIT + '. The van as in the attached plate. Handwriting unreadable. ' + PHONE),
 dict(beat="HK2-B0", line="I can tell how long someone has had a bad knee by which rail they ask me to fit.", anatomy=False, product=False, face=True, room=True,
      refs=[FITTER, HALL], taste=["HT05", "HT09"],
      fix='user Fix: "this is ditorted i need a new image too" → the rail on his shoulder was warped; the rail now leans on the wall, tape measure in hand',
      motion="at the foot of the stairs he looks up the flight and pulls the tape measure out along the wall, one pull, 2s",
      prompt='For the line "I can tell how long someone has had a bad knee by which rail they ask me to fit.": the fitter stands at the foot of a client\'s stairs holding a yellow tape measure, looking up the flight, sizing up the job. One straight length of oak handrail leans against the hall wall beside him. Eye level from the hall, three-quarter, medium-full shot, his face sharp. He is the same man as the attached cast sheet, in ' + OUTFIT + '. The stairs and hall exactly as in the attached hall plate, the wall still bare. ' + PHONE),
]
bad = 0
for b in CALLS:
    c = {"beat": b["beat"], "kind": "image", "mode": 1, "prompt": b["prompt"], "script_line": b["line"],
         "face": b["face"], "room": b["room"], "product": b["product"], "body": not b.get("anatomy"),
         "refs": [{"label": r[1], "kind": r[2], "id": r[0]} for r in b["refs"]], "taste": b["taste"],
         "anatomy": bool(b.get("anatomy")), "pair": ["nano_banana_pro", "nano_banana_pro"], "motion_plan": b["motion"],
         "model": "nano_banana_pro", "render_count": 1, "fix_note": b["fix"]}
    p = B / f"calls/{b['beat']}.gap4.image.json"
    json.dump(c, open(p, "w"), indent=1, ensure_ascii=False)
    out = subprocess.run(["python3", str(PF), str(p)], capture_output=True, text=True).stdout
    real = [l.strip() for l in out.splitlines() if l.strip().startswith("FAIL") and "Sunburst on realistic" not in l]
    bad += bool(real)
    print(f"{b['beat']:7} {len(b['prompt']):5} chars  {'PASS' if not real else 'FAIL ' + ' | '.join(real)}")
sys.exit(1 if bad else 0)
