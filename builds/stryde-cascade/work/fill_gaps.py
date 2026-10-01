"""User 2026-09-29: "generate the missing brolls … the 34% less strain should be anatomy … fix the character,
the TH should be the one here". §6A beat image prompts (≤ 1,200 chars, the line first), one render per beat
(this board has no A/B view; the build keeps its step-2 image model, nano_banana_pro — V7.72 routing is new builds only).
Writes calls/<BEAT>.gap1.image.json and runs preflight on each."""
import json, subprocess, sys
from pathlib import Path

B = Path(__file__).resolve().parents[1]
PF = B.parents[1] / ".claude/skills/ai-prompt-engineer/scripts/preflight.py"

# references (Higgsfield media / job ids)
FRONT = ("f0b4f34e-379b-4b41-84de-dcbea3cd8ad5", "STRYDE front photo", "product")
BACK = ("ab66e7e3-48f6-4eb3-8d03-511380b723c0", "user's inside-pad photo", "product")
FITTER = ("8cc4a583-5d7d-4f39-9ef7-7fe7899d298b", "N-CHINESE cast sheet", "character")
THF = ("af785dc9-5a0d-4e5e-8952-752be522bf08", "C-TH-FRAME (his workwear, his hands)", "frame")
C1 = ("d04d6e8f-70cf-46ff-ba67-b6bc563a45a2", "C1 cast sheet", "character")
C2 = ("cd219dc4-2b30-4e18-ae35-d702e05fba56", "C2 cast sheet", "character")
HALL = ("f1f1e0b0-a384-409c-a5b1-f063dfdc99e9", "PLATE-P1-PROP (C1's hall and stairs)", "location")
FRONTRM = ("719c268b-14df-47b6-afab-35f0efdb8a2b", "PLATE-P1-FRONT (C1's front room)", "location")
C2HALL = ("1e46a65f-f165-4694-b5b6-1f92ea2688b3", "PLATE-C2-HALL", "location")
VAN = ("b1cc1764-3e34-4b37-b8c6-0abf55cfe68e", "PLATE-VAN", "location")
WORK = ("ba654d79-751c-4833-8780-a58cb4ef6e80", "PLATE-WORK", "location")
C1D1 = ("510dfcbc-e44c-43ee-b934-c6f39d431e99", "A1-B1 confirmed (C1, day 1 outfit)", "frame")
C1D1L = ("bdfa2632-e1da-4449-859e-56b47d749586", "A1-B2 confirmed (C1's legs, day 1)", "frame")
C1D2 = ("cc76ef4c-a2a6-40d1-a009-d5064e250995", "A3-B1 confirmed (C1, day 2, front room)", "frame")
C1D3 = ("6abf4de5-2aa7-4af0-9b92-5dd5033318f5", "A1-B7 confirmed (C1, day 3, bed downstairs)", "frame")
C2D1 = ("d3b2b233-a03c-4ab9-b76e-144efd825469", "A2-B2 confirmed (C2, day 1 outfit)", "frame")
C2WORN = ("6c8f404b-135e-4b02-b48a-3ef1f2cea15a", "A4-B1 confirmed (C2 wearing the strap)", "frame")
C2STAIR = ("1b5f56a4-b6d8-4d1c-9535-73c75d354f35", "A5-B4 confirmed (C2 on his stairs)", "frame")
BOX = ("b45f9d2e-6b61-46d2-a59d-9db19e83232e", "A5-P1 v1 (the Stryde box, two straps)", "frame")
ANAT = ("72d41a87-6298-4032-b626-2ca1e7e571bd", "A2-M3 confirmed (anatomy style)", "frame")
ANATS = ("fc400c13-25a4-409a-b275-0ccf9d5a18a4", "A4-M1 confirmed (anatomy with the strap)", "frame")

PHONE = "An ordinary iPhone photo, 1x lens, daylight, nothing staged or retouched."
ANATREG = ("Premium 3D anatomical render exactly in the style of the attached anatomy frame: near-black background, "
           "faint translucent body shell, warm red layered muscle, ivory bone, cool key light and warm under-glow.")
SIZE = "the strap is small — a rigid black shell about 12 × 5 cm, no longer than a palm, on a black knit band"

BEATS = [
 # ---- the narrator: the Chinese fitter from the talking head (user: "the TH should be the one here")
 dict(beat="HK1-B2", act="Hook 1", line="I fit stair rails for a living.", redo=True, face=False, room=True, product=False,
      refs=[THF, HALL], taste=["HT12", "HT09"],
      motion="his right hand turns the screwdriver one full turn and the screw seats flush in the brass bracket, 2s",
      prompt='For the line "I fit stair rails for a living.": a close shot of the fitter\'s hands driving the last screw into a round brass bracket that holds a new varnished oak handrail to the stair wall — the right hand mid-turn on a yellow-handled screwdriver, the left hand steadying the rail. Eye level, three-quarter, close, the hands sharp. The hands and cuffs match the attached talking-head frame: an older Chinese fitter\'s weathered hands, the faded navy fleece cuffs at the wrists. The wall and stair carpet as in the attached hall plate, soft behind. Exactly two hands, one screwdriver, the bracket fixed to the wall. ' + PHONE),
 dict(beat="HK2-B1", act="Hook 2", line="The first one goes at the top of the stairs.", redo=True, face=True, room=True, product=False,
      refs=[FITTER, THF, HALL], taste=["HT09", "HT12"],
      motion="standing on the landing, his hand slides once along the short new rail from end to end, checking it, 2s",
      prompt='For the line "The first one goes at the top of the stairs.": the fitter stands on the landing at the top of the stairs, running his right hand along a short new oak handrail fixed beside the top two steps, a spirit level resting on it, checking his work. High angle from the landing, three-quarter, medium shot. He is the same man as the attached cast sheet, in the navy fleece from the attached talking-head frame. The stairs, wall and carpet exactly as in the attached hall plate. One short rail at the top only; the rest of the wall bare. Window light from the landing window. ' + PHONE),
 dict(beat="HK2-B3", act="Hook 2", line="I would like to stop being called back for the second one.", redo=True, face=True, room=True, product=False,
      refs=[FITTER, THF, VAN], taste=["HT12"],
      motion="sitting still in the van's side door, phone at his ear, he lowers his eyes and gives one small nod, 3s",
      prompt='For the line "I would like to stop being called back for the second one.": the fitter sits in the open side door of his van, phone to his ear, listening, his eyes just lowering — a quiet, tired moment. Eye level, profile, medium shot, his face sharp. He is the same man as the attached cast sheet, in the navy fleece from the attached talking-head frame. The van exactly as in the attached van plate: shelving with clear organiser boxes, handrail lengths strapped to the wall. Afternoon light from the street side. ' + PHONE),
 dict(beat="A4-P1", act="Act 4", line="The strap I keep in the van now is called Stryde.", redo=True, face=False, room=True, product=True,
      refs=[FRONT, THF, VAN], taste=["FP01", "FP02", "FP06", "HT06", "HT07"],
      motion="his hand lifts the strap out of the open organiser box and turns it to face the lens, one slow lift, 2s",
      prompt='For the line "The strap I keep in the van now is called Stryde.": the fitter\'s hand lifts one strap out of a clear organiser box on the van shelf, turning it towards the lens, caught mid-lift. The strap is exactly the product in the attached front photo — ' + SIZE + ', the wordmark readable; it rests across his palm with his thumb beside it, nothing covering the shell. His hand and navy fleece cuff match the attached talking-head frame. Eye level, close, the strap sharp; the van shelf from the attached van plate soft behind. One hand only. ' + PHONE),
 dict(beat="A5-B1", act="Act 5", line="I started carrying a couple because I was tired of fitting the second rail.", redo=True, face=True, room=True, product=True,
      refs=[FRONT, FITTER, THF, VAN], taste=["FP01", "FP02", "HT06"],
      motion="he drops two straps into the organiser box on the van shelf and slides the lid shut, one drop, one slide, 3s",
      prompt='For the line "I started carrying a couple because I was tired of fitting the second rail.": inside the open back of his van the fitter drops two straps into a clear organiser box on the shelf, a spare length of oak handrail strapped to the wall beside him. Eye level, three-quarter, medium shot, his face and hands visible. Each strap is exactly the product in the attached front photo — ' + SIZE + '. He is the same man as the attached cast sheet, in the navy fleece from the attached talking-head frame. The van exactly as in the attached van plate. ' + PHONE),
 dict(beat="A5-P1", act="Act 5", line="Two for one, so you do both knees, which is the point.", redo=True, face=False, room=True, product=True,
      refs=[FRONT, BOX, THF, WORK], taste=["FP09", "FP02", "HT06", "HT07"],
      motion="his hands lift the lid off the small box, revealing the two straps side by side, one slow lift, 2s",
      prompt='For the line "Two for one, so you do both knees, which is the point.": on the oak workbench the fitter\'s hands lift the lid off the small matte-black Stryde box, showing two straps side by side in their wells. Each strap exactly the product in the attached front photo — ' + SIZE + '; the box only a little bigger than the two straps, like the attached box frame. His hands and navy fleece cuffs as in the attached talking-head frame, clear of the straps. Overhead, close, the straps sharp; the workbench from the attached workshop plate. Exactly two straps. ' + PHONE),
 dict(beat="A4-P3", act="Act 4", line="Thirty four percent less strain. Measured.", redo=True, face=False, room=False, product=False, anatomy=True,
      refs=[ANATS, ANAT], taste=["HT11", "FP03"],
      motion="as the knee bends slightly under load, the tendon's hot red glow cools to a calm amber, the strap holding it, 3s",
      prompt='For the line "Thirty four percent less strain. Measured.": the knee from the side as bodyweight lands, a small rigid black strap wrapped just below the kneecap exactly as in the attached strap anatomy frame, pressing on the patellar tendon — and the tendon, which glows hot red above and below the strap, is calm cool amber where the strap holds it: visibly less strain. The kneecap sits just above the strap, the strap never over it. Side view, the knee filling the frame. ' + ANATREG + ' No text, no numbers, no arrows.'),
 # ---- the gaps
 dict(beat="HK2-B0", act="Hook 2", line="I can tell how long someone has had a bad knee by which rail they ask me to fit.", face=True, room=True, product=False,
      refs=[FITTER, THF, HALL], taste=["HT05", "HT09"],
      motion="at the foot of the stairs he looks up the flight, rail on his shoulder, and pulls the tape measure out along the wall, one pull, 2s",
      prompt='For the line "I can tell how long someone has had a bad knee by which rail they ask me to fit.": the fitter stands at the foot of a client\'s stairs with a length of oak handrail on his shoulder and a tape measure in his hand, looking up the flight, sizing up the job. Low angle from the hall, three-quarter, medium-full shot. He is the same man as the attached cast sheet, in the navy fleece from the attached talking-head frame. The stairs and hall exactly as in the attached hall plate. One rail on his shoulder, the wall still bare. ' + PHONE),
 dict(beat="HK3-B4", act="Hook 3", line="Nobody plans for that.", face=True, room=True, product=False,
      refs=[C1, C1D3, FRONTRM], taste=["HT02", "HT08", "HT09"],
      motion="sitting on the edge of the bed she looks through the doorway at the stairs, then down at her hands, one slow look, 3s",
      prompt='For the line "Nobody plans for that.": the older woman sits on the edge of a single bed made up in her front room, looking through the open doorway at the stairs she no longer climbs, her hands in her lap. Eye level, three-quarter, medium shot, her face sharp. She is the same woman as the attached cast sheet, in the same outfit as the attached bed-downstairs frame. The front room exactly as in the attached plate; the bed where it stands in that frame. Soft window light. ' + PHONE),
 dict(beat="A1-B1b", act="Act 1", line="So you favour it.", face=True, room=True, product=False,
      refs=[C1, C1D1, HALL], taste=["HT02", "HT08", "HT12"],
      motion="on the step she shifts all her weight onto her right leg and lifts her left foot just off the stair, one shift, slow, 2s",
      prompt='For the line "So you favour it.": the older woman on her stairs puts all her weight on her right leg, her left foot barely touching the step, one hand on the banister, easing the sore knee. Low angle from the hall, three-quarter, full body, her face and both legs visible. She is the same woman as the attached cast sheet, in the same outfit as the attached day-one frame. The stairs exactly as in the attached hall plate. Exactly two legs, the same length. ' + PHONE),
 dict(beat="A1-B2b", act="Act 1", line="The good leg is now doing the work of two.", face=False, room=True, product=False,
      refs=[C1D1L, HALL], taste=["HT02", "HT12"],
      motion="her right leg straightens and lifts her up one step while the left leg trails, one step, slow, 2s",
      prompt='For the line "The good leg is now doing the work of two.": close on the older woman\'s legs on the stairs — her right leg bent on the step above, pushing her whole weight up, the left leg trailing behind on the lower step, carrying nothing. Ground level, profile, close, the right knee sharp. Legs, skirt hem and slippers exactly as in the attached day-one legs frame; the stair carpet as in the attached hall plate. Exactly two legs. ' + PHONE),
 dict(beat="A2-M2b", act="Act 2", line="That is the band.", face=False, room=False, product=False, anatomy=True,
      refs=[ANAT], taste=["HT11"],
      motion="the patellar tendon brightens slowly from a soft glow to a clear warm highlight, the knee still, 2s",
      prompt='For the line "That is the band.": the knee from the front, the patellar tendon — the short flat band as wide as a thumb running from the lower edge of the kneecap to the shin — lit in a clear warm highlight, everything else dimmed. The band starts right under the kneecap; the kneecap sits above it, unlit. Front view, the knee centred and filling the frame. ' + ANATREG + ' No text, no arrows.'),
 dict(beat="A2-M5", act="Act 2", line="Going up, your muscles lift you.", face=False, room=False, product=False, anatomy=True,
      refs=[ANAT], taste=["HT11"],
      motion="the leg straightens to lift the body up the step; the thigh muscle glows brighter as it works, 2s",
      prompt='For the line "Going up, your muscles lift you.": a leg on a step, side view, mid-way through pushing up: the big thigh muscle above the knee glows bright warm red, working, while the tendon below the kneecap stays calm and cool. A simple translucent step under the foot. ' + ANATREG + ' No text, no arrows.'),
 dict(beat="A2-M6", act="Act 2", line="Coming down, nothing does.", face=False, room=False, product=False, anatomy=True,
      refs=[ANAT], taste=["HT11"],
      motion="the leg lowers the body down one step; the thigh muscle dims and the tendon under the kneecap flares red, 2s",
      prompt='For the line "Coming down, nothing does.": the same leg stepping down, side view, the knee bent as the body drops: the thigh muscle dim and slack, and the tendon just below the kneecap flaring hot red as it takes the whole landing. A simple translucent step under the foot. ' + ANATREG + ' No text, no arrows.'),
 dict(beat="A2-M7", act="Act 2", line="The pain is not the first thing that happened. It is the first thing you noticed.", face=False, room=False, product=False, anatomy=True,
      refs=[ANAT], taste=["HT11"],
      motion="faint frayed fibres along the tendon glow a dull orange, then one sharp red pulse spreads from them, 3s",
      prompt='For the line "The pain is not the first thing that happened. It is the first thing you noticed.": close on the patellar tendon just below the kneecap, side view: along the band, fine frayed fibres glow a dull worn orange — damage built up quietly — and a first sharp red pulse is just starting from them. The kneecap above, the shin below. ' + ANATREG + ' No text, no arrows.'),
 dict(beat="A3-B0", act="Act 3", line="You have been told it is your age. Or your weight. Or that the muscle is weak.", face=True, room=True, product=False,
      refs=[C1, C1D2, FRONTRM], taste=["HT08", "HT09"],
      motion="in her armchair, phone at her ear, she listens and gives one small tired nod, 3s",
      prompt='For the line "You have been told it is your age. Or your weight. Or that the muscle is weak.": the older woman sits in her armchair with the phone to her ear, listening, a folded hospital letter on her lap, her face patient and unconvinced. Eye level, three-quarter, medium shot, her face sharp. She is the same woman as the attached cast sheet, in the same outfit as the attached day-two frame. The front room exactly as in the attached plate. Window light from the side. ' + PHONE),
 dict(beat="A3-B5", act="Act 3", line="None of them are wrong. None of them move the weight off the band, and that is the only thing that stops the sequence.", face=False, room=True, product=False,
      refs=[C1D2, FRONTRM], taste=["HT10", "HT12"],
      motion="her hand sets the beige knee sleeve down beside the other three things on the table, one placing, 2s",
      prompt='For the line "None of them are wrong. None of them move the weight off the band, and that is the only thing that stops the sequence.": on the side table beside her armchair lie the things she has tried — a coiled physio exercise band, a tube of pain gel, a blister pack of pills — and her hand is setting down a beige knee sleeve beside them. High angle, close, the four things sharp. Her hand and cardigan cuff as in the attached day-two frame; the front room from the attached plate soft behind. Exactly four things, one hand. ' + PHONE),
 dict(beat="A4-B1b", act="Act 4", line="It never crosses the joint.", face=False, room=True, product=True,
      refs=[FRONT, C2WORN, C2HALL], taste=["FP01", "FP02", "FP03", "FP07", "HT06"],
      motion="sitting, he bends his right knee to a right angle and back; the strap stays below the kneecap, 2s",
      prompt='For the line "It never crosses the joint.": front-on, close on the man\'s right knee as he sits and bends it: the strap sits centred on the tendon right under the kneecap, the kneecap\'s lower edge in its notch, the bend happening above the strap. The strap is exactly the product in the attached front photo — ' + SIZE + ' — worn as in the attached worn frame, his shorts and leg as there. The hall from the attached plate soft behind. Hands off the knee. ' + PHONE),
 dict(beat="A4-B2b", act="Act 4", line="A little too high and it is a sleeve again.", face=False, room=True, product=True,
      refs=[FRONT, C2WORN, C2HALL], taste=["FP01", "FP02", "FP03", "FP10", "HT07"],
      motion="his fingers slide the strap down from over the kneecap to sit just below it, one slide, 2s",
      prompt='For the line "A little too high and it is a sleeve again.": front-on, close on the man\'s straightened right knee: the strap sits too high, over the kneecap, and his two fingertips at its edges are just starting to slide it down. The strap is exactly the product in the attached front photo — ' + SIZE + ' — the shell uncovered, fingertips only at its ends. His leg and shorts as in the attached worn frame; the hall soft behind from the attached plate. ' + PHONE),
 dict(beat="A4-B3", act="Act 4", line="Three years with orthopedic surgeons.", face=False, room=False, product=True,
      refs=[FRONT], taste=["FP01", "FP02", "FP03", "HT06"],
      motion="a gloved hand turns the knee model a quarter turn to show the strap on the tendon, one turn, 2s",
      prompt='For the line "Three years with orthopedic surgeons.": on a clean clinic desk, a white life-size knee joint model with the strap fitted just below its kneecap, and a clinician\'s gloved hand turning the model towards us. The strap is exactly the product in the attached front photo — ' + SIZE + ' — centred on the model\'s tendon below the kneecap. Eye level, close, the model and strap sharp; a plain clinic room soft behind. One hand, no face, nothing written. ' + PHONE),
 dict(beat="A4-B4", act="Act 4", line="Two hundred thousand people wearing one.", face=False, room=False, product=True,
      refs=[FRONT], taste=["FP01", "FP02", "FP03", "HT01", "HT06"],
      motion="the two walkers take three brisk steps along the promenade away from us, one step per second, 3s",
      prompt='For the line "Two hundred thousand people wearing one.": two older people out walking briskly on a seaside promenade in shorts, seen from behind at knee height, each wearing the strap on one knee, just below the kneecap. The strap is exactly the product in the attached front photo — ' + SIZE + '. Low angle, three-quarter-back, the knees and straps sharp, the people seen from the waist down. Bright overcast daylight. Exactly four legs. ' + PHONE),
 dict(beat="A5-B1b", act="Act 5", line="Three houses this year have not called me back.", face=True, room=True, product=False,
      refs=[FITTER, THF, VAN], taste=["HT12"],
      motion="in the van's driver seat he runs a pen down a page of his job diary and stops, a small smile, 3s",
      prompt='For the line "Three houses this year have not called me back.": the fitter sits in the driver\'s seat of his van with a paper job diary open against the steering wheel, running his pen down the page, a small satisfied smile. Eye level through the open door, three-quarter, medium shot, his face sharp. He is the same man as the attached cast sheet, in the navy fleece from the attached talking-head frame; the van as in the attached plate. Handwriting unreadable. ' + PHONE),
 dict(beat="A5-M1", act="Act 5", line="Not because the arthritis is gone. It is still there.", face=False, room=False, product=False, anatomy=True,
      refs=[ANATS, ANAT], taste=["HT11", "FP03"],
      motion="the worn joint surfaces glow a faint grey-blue while the strap below the kneecap keeps the tendon calm, 3s",
      prompt='For the line "Not because the arthritis is gone. It is still there.": the knee joint from the side: the worn, thinned cartilage between thigh bone and shin glows a faint grey-blue — the arthritis still there — while the small black strap just below the kneecap, exactly as in the attached strap anatomy frame, keeps the tendon under it calm. The strap below the kneecap, never over it. ' + ANATREG + ' No text, no arrows.'),
 dict(beat="A5-B4b", act="Act 5", line="You will know in a minute.", face=True, room=True, product=True,
      refs=[FRONT, C2, C2STAIR, C2HALL], taste=["FP01", "FP02", "FP07", "HT03", "HT04"],
      motion="he steps off the last stair onto the hall floor, hands free, and looks down at his knee with a small smile, one step, 2s",
      prompt='For the line "You will know in a minute.": the man is taking his last step off the bottom stair onto the hall floor, hands free at his sides, glancing down at his knee with a small pleased smile. The strap on his right knee just below the kneecap is exactly the product in the attached front photo — ' + SIZE + ' — his leg straight enough that it shows. Eye level from the hall, front, full body, his face sharp. He is the same man as the attached cast sheet, dressed as in the attached stairs frame; the hall exactly as in the attached plate. ' + PHONE),
 dict(beat="A5-P2", act="Act 5", line="Sixty days, and you keep the straps.", face=False, room=True, product=True,
      refs=[FRONT, BOX, C2HALL], taste=["FP01", "FP02", "FP09", "HT06"],
      motion="the camera holds; his hand sets his house keys down beside the open box, one placing, 2s",
      prompt='For the line "Sixty days, and you keep the straps.": on a hall table the small open Stryde box with its two straps side by side, and a man\'s hand setting his house keys down beside it — the straps are his now. Each strap exactly the product in the attached front photo — ' + SIZE + '; the box like the attached box frame, only a little bigger than the two straps. High angle, close, the straps sharp; the hall from the attached plate soft behind. Exactly two straps, one hand. ' + PHONE),
]

if __name__ == "__main__":
    (B / "calls").mkdir(exist_ok=True)
    bad = 0
    for b in BEATS:
        c = {"beat": b["beat"], "kind": "image", "mode": 1, "prompt": b["prompt"], "script_line": b["line"],
             "face": b["face"], "room": b["room"], "product": b["product"], "body": not b.get("anatomy"),
             "refs": [{"label": r[1], "kind": r[2], "id": r[0]} for r in b["refs"]], "taste": b["taste"],
             "anatomy": bool(b.get("anatomy")), "pair": ["nano_banana_pro", "nano_banana_pro"],
             "motion_plan": b["motion"], "model": "nano_banana_pro", "render_count": 1,
             "note": "build keeps its step-2 image lock (nano_banana_pro); one render — this board has no A/B view"}
        p = B / f"calls/{b['beat']}.gap1.image.json"
        json.dump(c, open(p, "w"), indent=1, ensure_ascii=False)
        out = subprocess.run(["python3", str(PF), str(p)], capture_output=True, text=True).stdout
        fails = [l.strip() for l in out.splitlines() if l.strip().startswith("FAIL")]
        real = [f for f in fails if "Sunburst on realistic" not in f]
        bad += bool(real)
        print(f"{b['beat']:7} {len(b['prompt']):5} chars  {'PASS' if not fails else ('LOCK-ONLY' if not real else 'FAIL')}  {' | '.join(real)}")
    sys.exit(1 if bad else 0)
