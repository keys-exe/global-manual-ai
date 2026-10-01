#!/usr/bin/env python3
"""stryde-lost-moments — Body 5 / Act 6 (Clifton, E-01…E-09) beat images, V7.74.0 (§6A + Part 2).

User 2026-10-01: "I NEED THE BODY AND HOOK E ONLY" → variant E first. Hook 5 and the shared Act 1 shots are confirmed;
this writes the nine Act 6 frames. Each prompt ≤ 1,200 chars, refs numbered `Image n`, A/B pair on two GPT Image 2.5
Sunburst renders (Kie, image-to-image with the refs). Day 1 (E-01, E-02) carries the E-HKa frame; day 2 (E-03…E-09)
carries the E-HKb frame (outfit, rug, track, room). Product beats E-04, E-05, E-07: three-quarter product photo first.
Usage: actE.py → work/prompts/E-xx.v74.txt + work/clips/E-xx.img.call.json, then preflight each.
"""
import json, pathlib
HERE = pathlib.Path(__file__).parent
CF = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/"
C5 = CF + "hf_20260928_131041_578389bd-200a-401e-a6d9-c0ec3c5f32fe.png"
GK1 = CF + "hf_20260928_133636_85af6d78-2a9d-482e-a244-0cccff1e525c.png"
GK2 = CF + "hf_20260928_133636_76c6d8b2-e636-4ec6-af0f-589208186857.png"
HKA = CF + "hf_20260929_070753_27963c08-22a2-42cd-a1c5-460bdfb761cc.png"
HKB = CF + "hf_20260929_122408_93a5c907-3c21-46d7-ba71-a92f59a3ecb0.png"
REF = "products/stryde/stryde_refs/"
TQ, BENT = REF + "product_tq_left.jpg", REF + "worn_bent.jpg"

REG = "An ordinary iPhone photo, 1x lens, nothing staged or retouched."
STRAP = ("The strap in Image 1 copied exactly — same shell, band, slides and wordmark, nothing redesigned — 12 × 5 cm, "
         "about a quarter of the frame wide, seated just below his right kneecap exactly as in Image 2, the kneecap uncovered.")
D2 = "the mustard-and-green patterned short-sleeve shirt, olive shorts and navy slippers of Image 3"

R = lambda label, kind, url: {"label": label, "kind": kind, "url": url}
B = {}
B["E-01"] = dict(line="It's not getting down that stops you.", face=True, room=True, product=False, body=True,
  refs=[R("E-HKa (room, day-1 outfit)", "frame", HKA), R("C5 Clifton sheet", "character", C5)],
  taste=["HT02", "HT12", "HT18", "HT19"],
  motion="From this frame: he lowers his eyes once and stays still, about a second.",
  prompt=f"""For the line "It's not getting down that stops you.": he sits on the edge of the sofa, still and heavy, looking down — stuck where he is.
Medium close-up, eye level, three-quarter front, from the waist up.
Image 1 is the living room and his day-one clothes. Image 2 is the man.
The same man as Image 2 — same face, hair and build — in the clothes of Image 1: white T-shirt under a burgundy cardigan, grey shorts. The brown patterned sofa and curtained patio doors of Image 1 soft behind him.
Face turned down, eyes lowered, looking down, mouth closed — a quiet, defeated look. Both hands resting on his knees at the bottom of the frame, forearms on his thighs.
In the frame: one man, the sofa, the patio doors; nothing else.
Grey, flat morning daylight from the patio doors on the right. {REG}
Clothing, cushions and walls plain — no lettering, logos or labels; no second person.""")
B["E-02"] = dict(line="It's getting back up.", face=False, room=True, product=False, body=True,
  refs=[R("E-HKa (sofa, day-1 cardigan)", "frame", HKA)],
  taste=["HT02", "HT12", "HT18"],
  motion="From this frame: his hand presses down once harder into the sofa arm, knuckles whitening, and holds, about a second.",
  prompt=f"""For the line "It's getting back up.": close on his right hand pushing down hard on the padded arm of the sofa as he tries to lever himself up — knuckles pale, tendons standing out on the back of the hand.
Close-up from slightly above, three-quarter, the hand and sofa arm about half of the frame wide.
Image 1 is the sofa, the room and his clothes.
One hand only: his right, fingers spread, the palm sinking into the brown patterned sofa fabric copied from Image 1; his forearm in the burgundy cardigan sleeve of Image 1 entering from the top of the frame, the arm straight and braced.
In the frame: one hand and forearm, the sofa arm, the red rug soft below; nothing else.
Grey, flat morning daylight from the left. {REG}
Sleeve and sofa plain — no lettering, logos or labels; no second hand.""")
B["E-03"] = dict(line="And the pain just lifts.", face=True, room=True, product=False, body=True,
  refs=[R("E-HKb (room, day-2 outfit)", "frame", HKB), R("C5 Clifton sheet", "character", C5)],
  taste=["HT12", "HT18", "HT20"],
  motion="From this frame: his shoulders drop on one long breath out and his face eases into relief, about two seconds.",
  prompt=f"""For the line "And the pain just lifts.": kneeling on the rug, his shoulders drop on a long breath out and his face eases into quiet relief.
Medium close-up, low angle from just below his eye line, three-quarter front, from mid-chest up.
Image 1 is the room and his day-two clothes. Image 2 is the man.
The same man as Image 2 — same face, hair and build — in the mustard-and-green patterned short-sleeve shirt of Image 1. The bright patio doors and cream wall of Image 1 soft behind him.
Eyes softening, looking down at the rug in front of him, the first small relieved smile, mouth closed. Both hands resting on his thighs, low in the frame.
In the frame: one man, the soft room behind; nothing else.
Warm afternoon sun from the patio doors on the left, lighting the window side of his face. {REG}
Shirt and walls plain — no lettering, logos or labels; no second person.""")
B["E-04"] = dict(line="So you get down among the toys.", face=False, room=True, product=True, body=True,
  refs=[R("product_tq_left.jpg", "product", TQ), R("worn_bent.jpg", "product", BENT), R("E-HKb (room, rug, track, day-2 outfit)", "frame", HKB)],
  taste=["FP01", "FP02", "FP03", "FP11", "FP12", "HT01", "HT06", "HT07", "HT18"],
  motion="From this frame: he finishes lowering onto his left knee until it rests on the rug, and stays kneeling, about a second and a half.",
  prompt=f"""For the line "So you get down among the toys.": he lowers onto one knee on the red rug beside the train track — mid-kneel, left knee a hand's width above the rug, right foot flat, right knee bent forward.
Medium shot from above, three-quarter front, chest down to the rug, the strapped right knee centred.
Image 1 is the strap (three-quarter photo). Image 2 is the strap worn on a bent knee. Image 3 is the man, the room and his clothes.
{STRAP} The man of Image 3 in {D2}.
In the frame: one man, the rug, the oval wooden track with one small engine; the rest of the rug bare. His right hand reaching down toward the track, left hand out to the side for balance, neither touching the strap.
Warm afternoon sun from the left. {REG}
Clothing, slippers and toys plain — no lettering or logos but the strap's own wordmark; no second strap.""")
B["E-05"] = dict(line="And you get back up on your own.", face=False, room=True, product=True, body=True,
  refs=[R("product_tq_left.jpg", "product", TQ), R("worn_bent.jpg", "product", BENT), R("E-HKb (room, rug, day-2 outfit)", "frame", HKB)],
  taste=["FP01", "FP02", "FP03", "FP11", "FP12", "HT01", "HT04", "HT06", "HT07", "HT18"],
  motion="From this frame: he rises the rest of the way to standing on his legs alone, hands loose, and ends upright and still, about a second and a half.",
  prompt=f"""For the line "And you get back up on your own.": he stands up from kneeling on the rug on his legs alone — caught halfway up, right foot planted, right knee bent with the strap on it, left knee just lifting off the rug.
Medium shot, low angle, three-quarter front, from his chest down to the rug, the strapped right knee in the centre of the frame.
Image 1 is the strap (three-quarter photo). Image 2 is the strap worn on a bent knee. Image 3 is the man, the room and his clothes.
{STRAP} The man of Image 3 in {D2}.
Both hands loose at his sides in the air, touching nothing — his legs do all the work. In the frame: one man, the red rug, the wooden track soft behind him; nothing else.
Warm afternoon sun from the right. {REG}
Clothing, slippers and toys plain — no lettering or logos but the strap's own wordmark; no second strap.""")
B["E-06"] = dict(line="No hand on the sofa.", face=False, room=True, product=False, body=True,
  refs=[R("E-HKb (sofa, room, day-2 shirt)", "frame", HKB)],
  taste=["HT01", "HT12", "HT18", "HT19"],
  motion="From this frame: his fingers turn the wooden engine over once, about a second.",
  prompt=f"""For the line "No hand on the sofa.": close on his two hands holding a small wooden toy engine at chest height, turning it over — the empty brown sofa arm soft behind them.
Close-up, eye level, three-quarter, the hands and engine about half of the frame wide.
Image 1 is the room, the sofa and his shirt.
Exactly two hands, his own: the right holding the engine, the left thumb turning one of its wheels; his forearms in the mustard-and-green short sleeves of Image 1. The empty sofa arm of Image 1 out of focus behind.
In the frame: two hands, one plain wooden engine, the soft sofa arm; nothing else.
Warm afternoon sun from the left. {REG}
Engine, shirt and sofa plain — no lettering, logos or labels.""")
B["E-07"] = dict(line="Nobody hauling you up.", face=True, room=True, product=True, body=True,
  refs=[R("product_tq_left.jpg", "product", TQ), R("worn_bent.jpg", "product", BENT), R("E-HKb (room, rug, day-2 outfit)", "frame", HKB),
        R("GK1 Amara sheet", "character", GK1), R("GK2 Tobi sheet", "character", GK2)],
  taste=["FP01", "FP02", "FP03", "FP11", "FP12", "HT01", "HT06", "HT12", "HT18"],
  motion="From this frame: the children take his hands and he stands still, smiling down at them, about a second.",
  prompt=f"""For the line "Nobody hauling you up.": he stands upright on the rug on his own, legs straight, as his two grandchildren reach up and take his hands.
Medium shot, high angle, three-quarter front, from his waist to his feet, the children either side with their heads at his waist.
Image 1 is the strap (three-quarter photo). Image 2 is the strap worn. Image 3 is the man, the room and his clothes. Image 4 is the girl. Image 5 is the boy.
The strap in Image 1 copied exactly — same shell, band, slides and wordmark, nothing redesigned — 12 × 5 cm, about a quarter of the frame wide, just below his right kneecap as in Image 2, his leg straight. The man of Image 3 in his olive shorts and navy slippers.
The same girl as Image 4 in a purple T-shirt and denim shorts holds his left hand; the same boy as Image 5 in a green T-shirt and grey shorts holds his right hand; both looking up at him, smiling, mouths closed.
In the frame: one man, two children, the red rug; nothing else.
Afternoon sun from the right. {REG}
Clothing plain — no lettering or logos but the strap's own wordmark; no second strap.""")
B["E-08"] = dict(line="They won't be little for long.", face=True, room=True, product=False, body=True,
  refs=[R("E-HKb (room, rug, track, day-2 shirt)", "frame", HKB), R("GK1 Amara sheet", "character", GK1),
        R("GK2 Tobi sheet", "character", GK2), R("C5 Clifton sheet", "character", C5)],
  taste=["HT12", "HT18", "HT19"],
  motion="From this frame: the girl clicks the track piece into place once, about a second.",
  prompt=f"""For the line "They won't be little for long.": his two grandchildren kneel on the rug building the wooden train track, the girl clicking one curved piece into place, while he kneels just behind the track watching them with a soft smile.
Ground-level shot from behind the children, three-quarter back, their backs and hands sharp in the foreground, him softer behind.
Image 1 is the room and his shirt. Image 2 is the girl. Image 3 is the boy. Image 4 is the man.
The girl of Image 2 in a purple T-shirt and denim shorts, both hands pressing the track piece together; the boy of Image 3 in a green T-shirt and grey shorts, one hand on a small wooden engine, the other flat on the rug. The same man as Image 4 in the mustard-and-green shirt of Image 1, seen from the waist up behind the track, his legs hidden by the children, both hands on his thighs, looking down at the girl's hands.
In the frame: two children, one man, the oval track, one engine; the rest of the rug bare.
Afternoon sun from the patio doors on the left. {REG}
Clothing and toys plain — no lettering, logos or labels.""")
B["E-09"] = dict(line="Nothing to lose but the pain.", face=True, room=True, product=False, body=True,
  refs=[R("E-HKb (room, day-2 shirt)", "frame", HKB), R("C5 Clifton sheet", "character", C5)],
  taste=["HT12", "HT18"],
  motion="From this frame: he laughs once, shoulders shaking, then settles into a wide smile, about a second.",
  prompt=f"""For the line "Nothing to lose but the pain.": kneeling on the rug, he laughs out loud — head tipped back a little, eyes creased, a real, unguarded laugh.
Medium close-up, eye level, three-quarter front, from mid-chest up.
Image 1 is the room and his day-two shirt. Image 2 is the man.
The same man as Image 2 — same face, hair and build — in the mustard-and-green patterned shirt of Image 1; the bright patio doors of Image 1 soft behind him.
Mouth open in the laugh, eyes creased, looking down to his right at the rug. Right hand raised to his chest, left hand resting on his thigh low in the frame.
In the frame: one man, the soft room behind; nothing else.
Warm afternoon sun from the left. {REG}
Shirt and walls plain — no lettering, logos or labels; no second person.""")

if __name__ == "__main__":
    (HERE / "prompts").mkdir(exist_ok=True); (HERE / "clips").mkdir(exist_ok=True)
    for beat, b in B.items():
        (HERE / "prompts" / f"{beat}.v74.txt").write_text(b["prompt"])
        call = {"beat": beat, "kind": "image", "mode": 1, "prompt": b["prompt"], "script_line": b["line"],
                "face": b["face"], "room": b["room"], "product": b["product"], "body": b["body"],
                "refs": [{"label": r["label"], "kind": r["kind"]} for r in b["refs"]], "match": None, "edit_of": None,
                "taste": b["taste"], "anatomy": False, "pair": ["gpt_image_2_5", "gpt_image_2_5"],
                "motion_plan": b["motion"], "ref_urls": [r["url"] for r in b["refs"]]}
        (HERE / "clips" / f"{beat}.img.call.json").write_text(json.dumps(call, indent=1))
        print(beat, len(b["prompt"]))
