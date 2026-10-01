#!/usr/bin/env python3
"""stryde-lost-moments — Body 4 / Act 5 (Graham, golf, D-01…D-12) beat images, V7.74.0 (§6A + Part 2).

User 2026-10-01: "NEXT WE GO TO THE HOOK D" → variant D. Hook 4 (D-HKa, D-HKb) and VO-T1-HK4 are confirmed; the shared Act 1
shots in Body 4's cut order are confirmed. This writes the twelve Act 5 frames as A/B pairs on GPT Image 2.5 Sunburst (Kie,
image-to-image with the refs). Wardrobe: Gr-D2 (D-01…D-03, the bad round, overcast) navy golf polo, stone golf shorts;
Gr-D3 (D-04…D-12, the good round, sun) pale-blue polo under a navy sleeveless V-neck pullover, grey golf shorts; white-and-tan
golf shoes throughout. Product beats (D-04, D-09, D-10, D-11) carry the product photo first and frame the strap ≥ ¼ wide.
Usage: actD.py → work/prompts/D-xx.v74.txt + work/clips/D-xx.img.call.json
"""
import json, pathlib
HERE = pathlib.Path(__file__).parent
CF = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/"
C4 = CF + "hf_20260928_131042_2bd591b1-d203-465c-aa46-7753d7f613e6.png"
HKA = CF + "hf_20260929_091748_93103d12-eb4e-444a-b035-84ebaf026a33.png"
COURSE = CF + "hf_20260928_133541_e02553d3-aafb-4345-a6ef-97a97052c6fe.png"
GARAGE = CF + "hf_20260928_133539_86cd7faf-7c0d-44f0-8194-a7163d4c183a.png"
REF = "products/stryde/stryde_refs/"
FRONT, WF, TQ = REF + "front.webp", REF + "worn_front.jpg", REF + "product_tq_left.jpg"

REG = "An ordinary iPhone photo, 1x lens, nothing staged or retouched."
D2 = "a navy golf polo, stone golf shorts above the knee and white-and-tan golf shoes"
D3 = "a pale-blue golf polo under a navy sleeveless V-neck pullover, grey golf shorts above the knee and white-and-tan golf shoes"
STRAP = ("The strap in Image 1 copied exactly — same shell, band, slides and wordmark, nothing redesigned — 12 × 5 cm, "
         "about a quarter of the frame wide, seated just below his right kneecap as in Image 2, the kneecap uncovered.")
PLAIN = "Clothing, bag and signs plain — no lettering or logos{x}"
R = lambda label, kind, url: {"label": label, "kind": kind, "url": url}
B = {}
B["D-01"] = dict(line="A round is hours on your feet.", face=False, room=True, product=False, body=True,
  refs=[R("P6-COURSE plate", "location", COURSE)], taste=["HT02", "HT12", "HT18"],
  motion="From this frame: they walk on up the fairway at a normal walking pace, three steps each, about three seconds.",
  prompt=f"""For the line "A round is hours on your feet.": two golfers walk away up a long, empty fairway, small in the frame, the green far off ahead of them.
Wide shot from a slightly high angle, from behind them, the fairway stretching up the frame.
Image 1 is the golf course.
The fairway, trees and sky of Image 1, under a flat overcast afternoon sky. Two men in their sixties, one in {D2}, his bag on his shoulder; the other in a grey polo, pulling a trolley. Each mid-stride, one hand on his bag strap or trolley handle, the other loose at his side.
In the frame: two men, one bag, one trolley, the fairway; nothing else.
Flat grey overcast light. {REG}
{PLAIN.format(x='; no third person.')}""")
B["D-02"] = dict(line="Every stride,", face=False, room=False, product=False, body=True,
  refs=[R("C4 Graham sheet (shoes)", "frame", C4)], taste=["HT02", "HT12", "HT18"],
  motion="From this frame: his feet take two strides across the frame at one step per second, about two seconds.",
  prompt=f"""For the line "Every stride,": close on his golf shoes walking on fairway grass, caught mid-stride, the back heel lifting and the front foot landing.
Close-up at ground level, from the side, his feet and lower shins filling about half of the frame wide.
Image 1 shows his white-and-tan golf shoes.
The white-and-tan golf shoes of Image 1 copied exactly, his bare lower shins above them, grey sports socks; the short mown grass of the fairway, damp under an overcast sky.
Both hands outside the frame above. In the frame: two feet, two shins, the grass; nothing else. Exactly two legs, the left foot landing, the right heel lifting.
Flat grey overcast light. {REG}
Shoes and socks plain — no lettering or logos; no third foot.""")
B["D-03"] = dict(line="By the back nine, that spot is finished.", face=True, room=True, product=False, body=True,
  refs=[R("P6-COURSE plate", "location", COURSE), R("C4 Graham sheet", "character", C4)], taste=["HT02", "HT12", "HT18", "HT19"],
  motion="From this frame: he shifts his weight onto the club once and stays bent, about a second.",
  prompt=f"""For the line "By the back nine, that spot is finished.": he has stopped dead on the fairway, leaning hard on a golf club, his other hand clamped on his right knee, face tight with pain.
Medium shot, slightly high angle, three-quarter front, his whole body from head to shoes.
Image 1 is the golf course. Image 2 is the man.
The same man as Image 2 — same face, hair and build — in {D2}. The fairway and trees of Image 1 soft behind him under an overcast sky.
Left hand gripping the club head-down on the grass as a prop, right hand clamped over his right knee, weight on his left leg. Eyes down on the knee, jaw set, mouth closed.
In the frame: one man, one club, the fairway; nothing else.
Flat grey overcast light. {REG}
{PLAIN.format(x='; no second person.')}""")
B["D-04"] = dict(line="This strap sits two centimetres below the kneecap", face=False, room=False, product=True, body=True,
  refs=[R("front.webp", "product", FRONT), R("worn_front.jpg", "product", WF)], taste=["FP01", "FP02", "FP03", "FP11", "FP12", "HT06", "HT07", "HT14", "HT18"],
  motion="From this frame: his fingertip taps once on the gap between the kneecap and the strap, about a second.",
  prompt=f"""For the line "This strap sits two centimetres below the kneecap": extreme close-up of his right knee with the strap seated, his fingertip pointing at the small gap between the kneecap and the strap's top edge.
Extreme close-up, knee height, straight in front of the knee.
Image 1 is the strap (front photo). Image 2 is the strap worn.
The strap in Image 1 copied exactly — same shell, band, slides and wordmark, nothing redesigned — 12 × 5 cm, about half of the frame wide, its notch hugging the kneecap's lower edge exactly as in Image 2.
His right index fingertip touching the skin in the gap just above the shell's notch, the rest of the hand curled away to the side, nothing over the wordmark. The hem of his grey golf shorts at the top of the frame; bare knee and shin below.
In the frame: one knee, one strap, one hand; nothing else.
Bright afternoon sun from the left. {REG}
Shorts plain — no lettering or logos but the strap's own wordmark; no second hand.""")
B["D-05"] = dict(line="And the pain just lifts.", face=True, room=True, product=False, body=True,
  refs=[R("P6-COURSE plate", "location", COURSE), R("C4 Graham sheet", "character", C4)], taste=["HT12", "HT18", "HT20"],
  motion="From this frame: his shoulders drop on one long breath out and his face eases, about two seconds.",
  prompt=f"""For the line "And the pain just lifts.": standing on the tee in the sun, club in hand, his shoulders drop on a breath out and his face eases into relief.
Medium close-up, eye level, three-quarter front, from mid-chest up.
Image 1 is the golf course. Image 2 is the man.
The same man as Image 2 — same face, hair and build — in a pale-blue golf polo under a navy sleeveless V-neck pullover. The sunny fairway and trees of Image 1 soft behind him.
Eyes softly closing, looking down the fairway, the start of a small smile, mouth closed. Both hands resting on the grip of a club held upright in front of his chest.
In the frame: one man, one club; nothing else.
Warm afternoon sun from the left, lighting the window side of his face. {REG}
Clothing plain — no lettering or logos; no second person.""")
B["D-06"] = dict(line="So you walk the course instead of watching it.", face=True, room=True, product=False, body=True,
  refs=[R("P6-COURSE plate (buggy)", "location", COURSE), R("C4 Graham sheet", "character", C4), R("D-HKa (his golf bag)", "frame", HKA)],
  taste=["HT01", "HT12", "HT18"],
  motion="From this frame: he takes three steps toward the lens at one step per second, bag on his shoulder, about three seconds.",
  prompt=f"""For the line "So you walk the course instead of watching it.": he walks past the parked white buggy toward the lens, his golf bag on his shoulder, mid-stride and smiling.
Medium shot, waist up, low angle, three-quarter front, the empty buggy soft behind him.
Image 1 is the golf course and its buggy. Image 2 is the man. Image 3 shows his golf bag.
The same man as Image 2 — same face, hair and build — in a pale-blue golf polo under a navy sleeveless V-neck pullover, carrying the navy-and-white golf bag of Image 3 on his right shoulder. The white buggy and fairway of Image 1 behind him.
Right hand on the bag's shoulder strap, left arm swinging forward; looking ahead past the lens, mouth closed in an easy smile.
In the frame: one man, one bag, the buggy behind; nothing else.
Warm afternoon sun from the right. {REG}
{PLAIN.format(x='; no second person.')}""")
B["D-07"] = dict(line="All eighteen.", face=False, room=False, product=False, body=True,
  refs=[R("C4 Graham sheet (hand, sleeve)", "frame", C4)], taste=["HT12", "HT18"],
  motion="From this frame: the flagstick slides down into the cup once, about a second.",
  prompt=f"""For the line "All eighteen.": close on his hand dropping the flagstick back into the hole on the last green, the stick halfway into the cup.
Close-up, slightly high angle, three-quarter, the hand, the bottom of the flagstick and the hole about half of the frame wide.
Image 1 shows his hands and skin tone.
One hand only: his right, an older man's hand like Image 1, gripping the white flagstick a hand's width above the grass, a pale-blue polo cuff at the wrist. The cup's white rim sunk in the short green grass.
In the frame: one hand, one flagstick, the hole, the green; nothing else.
Bright afternoon sun from the left. {REG}
Flagstick and flag plain — no lettering, numbers or logos; no second hand.""")
B["D-08"] = dict(line="No buggy.", face=False, room=True, product=False, body=True,
  refs=[R("P6-COURSE plate (buggy)", "location", COURSE), R("D-HKa (his golf bag)", "frame", HKA)], taste=["HT01", "HT12", "HT18"],
  motion="From this frame: he walks away across the green at a normal walking pace, three steps, about three seconds.",
  prompt=f"""For the line "No buggy.": seen from behind, he walks off the green carrying his golf bag on his shoulder, past the empty white buggy left parked at the side.
Wide shot, eye level, from behind, his whole figure in the middle of the frame, the buggy to the left.
Image 1 is the golf course and its buggy. Image 2 shows his golf bag.
A man in his sixties in {D3}, the navy-and-white bag of Image 2 on his right shoulder, right hand on its strap, left arm swinging, mid-stride. The empty white buggy and fairway of Image 1.
In the frame: one man, one bag, one empty buggy, the green and trees; nothing else.
Warm afternoon sun from behind the camera. {REG}
{PLAIN.format(x='; no person in the buggy.')}""")
B["D-09"] = dict(line="Sports doctors recommend it.", face=True, room=False, product=True, body=True,
  refs=[R("front.webp", "product", FRONT), R("product_tq_left.jpg", "product", TQ)], taste=["FP01", "FP02", "FP06", "FP11", "HT06", "HT07", "HT16", "HT18"],
  motion="From this frame: he lifts his eyes from the strap to look ahead, about a second.",
  prompt=f"""For the line "Sports doctors recommend it.": a sports doctor in his clinic holds the strap up in one hand, looking at it with quiet approval.
Medium close-up, eye level, three-quarter front, from mid-chest up.
Image 1 is the strap (front photo). Image 2 is the strap from three-quarter.
The strap in Image 1 copied exactly — same shell, band, slides and wordmark, nothing redesigned — 12 × 5 cm, about a quarter of the frame wide, resting across his open right palm at chest height, wordmark to the lens, the band looping loosely below.
A Black British sports doctor in his fifties, short greying hair, a navy clinic polo; eyes on the strap, mouth closed. Left hand resting at his side. A bright, plain sports-medicine room soft behind him, a treatment couch and a window on the left.
In the frame: one man, one strap; nothing else.
Even daylight from the window on the left. {REG}
Clothing and walls plain — no lettering or logos but the strap's own wordmark; no second person.""")
B["D-10"] = dict(line="One for each knee.", face=False, room=True, product=True, body=True,
  refs=[R("front.webp", "product", FRONT), R("worn_front.jpg", "product", WF), R("P6-COURSE plate (bench)", "location", COURSE)],
  taste=["FP01", "FP02", "FP03", "FP06", "FP09", "FP11", "HT06", "HT07", "HT18"],
  motion="From this frame: he lifts the second strap a few centimetres into the light, about a second.",
  prompt=f"""For the line "One for each knee.": seated on the course bench, a strap worn on his right knee and the second strap of the pair held up in his hand beside it.
Close-up, knee height, three-quarter front, his knees and hand filling the frame.
Image 1 is the strap (front photo). Image 2 is the strap worn. Image 3 is the course and its bench.
Both straps copied exactly from Image 1 — same shell, band, slides and wordmark, nothing redesigned — 12 × 5 cm each, each about a quarter of the frame wide: one seated just below his right kneecap as in Image 2, the other resting across his open right palm just above his left knee, wordmark to the lens.
Grey golf shorts above the knee; his left hand resting on his left thigh. The wooden bench slats and fairway of Image 3 soft behind.
In the frame: two knees, two straps, two hands; nothing else.
Warm afternoon sun from the left. {REG}
Shorts and bench plain — no lettering or logos but the straps' own wordmarks; no third strap.""")
B["D-11"] = dict(line="Book the tee time.", face=True, room=True, product=True, body=True,
  refs=[R("front.webp", "product", FRONT), R("worn_front.jpg", "product", WF), R("P5-GARAGE plate", "location", GARAGE),
        R("C4 Graham sheet", "character", C4), R("D-HKa (his golf bag)", "frame", HKA)],
  taste=["FP01", "FP02", "FP03", "FP07", "FP11", "FP12", "HT01", "HT06", "HT18"],
  motion="From this frame: the bag settles onto his shoulder in one swing, about a second.",
  prompt=f"""For the line "Book the tee time.": in his open garage door he swings the uncovered golf bag onto his shoulder.
Medium shot, low angle, three-quarter front, head to shins, the strapped right knee nearest the lens.
Image 1 is the strap (front photo). Image 2 is the strap worn. Image 3 is the garage. Image 4 is the man. Image 5 shows his golf bag.
{STRAP} The same man as Image 4 in {D3}, the navy-and-white bag of Image 5 mid-swing onto his right shoulder, right hand on its strap, left hand loose. The garage of Image 3 behind, door open to the sunny drive.
Looking ahead out of the door, mouth closed, smiling.
In the frame: one man, one bag; nothing else.
Afternoon sun from the open door behind him. {REG}
{PLAIN.format(x=" but the strap's own wordmark; no second strap.")}""")
B["D-12"] = dict(line="Nothing to lose but the pain.", face=True, room=True, product=False, body=True,
  refs=[R("P6-COURSE plate", "location", COURSE), R("C4 Graham sheet", "character", C4)], taste=["HT12", "HT18", "HT20"],
  motion="From this frame: he smiles once, a small warm smile, about a second.",
  prompt=f"""For the line "Nothing to lose but the pain.": on the first tee, club in hand, he looks out over the course with a small, satisfied smile.
Medium close-up, slightly high angle, three-quarter front, from mid-chest up, the fairway laid out below him.
Image 1 is the golf course. Image 2 is the man.
The same man as Image 2 — same face, hair and build — in a pale-blue golf polo under a navy sleeveless V-neck pullover. The sunny fairway of Image 1 soft behind him.
Looking ahead down the fairway past the lens, a small warm smile, mouth closed. Right hand resting on the top of a club; left hand out of frame at his side.
In the frame: one man, one club; nothing else.
Warm afternoon sun from the left. {REG}
Clothing plain — no lettering or logos; no second person.""")

if __name__ == "__main__":
    for beat, b in B.items():
        (HERE / "prompts" / f"{beat}.v74.txt").write_text(b["prompt"])
        call = {"beat": beat, "kind": "image", "mode": 1, "prompt": b["prompt"], "script_line": b["line"], "face": b["face"],
                "room": b["room"], "product": b["product"], "body": b["body"], "refs": [{"label": r["label"], "kind": r["kind"]} for r in b["refs"]],
                "match": None, "edit_of": None, "taste": b["taste"], "anatomy": False, "pair": ["gpt_image_2_5", "gpt_image_2_5"],
                "motion_plan": b["motion"], "ref_urls": [r["url"] for r in b["refs"]]}
        (HERE / "clips" / f"{beat}.img.call.json").write_text(json.dumps(call, indent=1))
        print(beat, len(b["prompt"]))
