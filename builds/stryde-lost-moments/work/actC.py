#!/usr/bin/env python3
"""stryde-lost-moments — Body 3 / Act 4 (Winston + Bramble, C-01…C-09) beat images, V7.74.0 (§6A + Part 2).

User 2026-10-01: "GIVE ME NOW THE HOOK C FINAL" — Hook 3, VO and the shared Act 1 shots are confirmed; Act 4 was only planned.
A/B pairs on GPT Image 2.5 Sunburst (Kie i2i). Wardrobe: W-D1 (C-01, C-02, problem, overcast) red-and-navy check flannel shirt,
open olive waxed jacket, navy shorts; W-D2 (C-03…C-09, after) grey sweatshirt under a burgundy quilted gilet, stone shorts;
brown walking boots throughout. House taste from today's D Fixes ("look too AI"): hip-height normal phone lens, soft light,
muted natural colour, real skin; strap clearly in frame on every after-shot that shows his legs.
Usage: actC.py → work/prompts/C-xx.v74.txt + work/clips/C-xx.img.call.json
"""
import json, pathlib
HERE = pathlib.Path(__file__).parent
CF = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/"
C3 = CF + "hf_20260928_131042_a6a36eec-ccb0-49a2-a70c-e29c191c9c4d.png"
DOG = CF + "hf_20260928_133540_378e491a-bdcc-4504-b470-2b4c2c32cc76.png"
PROPW = CF + "hf_20260928_133541_b2ba5e02-c0a7-4ed9-bbcb-8eb33c4e04aa.png"
FIELD = CF + "hf_20260928_133537_c94f2912-3e28-4a7b-9ee6-211deebf9143.png"
HKA = CF + "hf_20260928_204703_48a7897f-b698-41b9-b867-c2f8073021b4.png"
HKB = CF + "hf_20260929_124230_f91a9b21-6419-4779-af8c-b8d704ff7f89.png"
REF = "products/stryde/stryde_refs/"
WF, TQ = REF + "worn_front.jpg", REF + "product_tq_left.jpg"
D1 = "a red-and-navy check flannel shirt under an open olive waxed jacket, navy shorts above the knee and brown walking boots"
D2 = "a grey sweatshirt under a burgundy quilted gilet, stone shorts above the knee and brown walking boots"
GREY = "Flat grey overcast morning light, muted colour, real skin. An ordinary iPhone photo, nothing retouched."
SOFT = "Soft afternoon light through thin cloud, muted natural colour, real skin. An ordinary iPhone photo, nothing retouched."
STRAP = ("The strap in Image 1 copied exactly — same shell, band, slides and wordmark — 12 × 5 cm, about a quarter of the frame wide, "
         "seated just below his right kneecap as in Image 2, the kneecap uncovered.")
R = lambda label, kind, url: {"label": label, "kind": kind, "url": url}
B = {}
B["C-01"] = dict(line="Here's why the walks got shorter.", face=True, room=True, product=False, body=True,
  refs=[R("C-HKb (outside his house)", "location", HKB), R("C3 Winston sheet", "character", C3), R("DOG-BRAMBLE sheet", "character", DOG), R("C-HKa (day-1 outfit)", "frame", HKA)],
  taste=["HT01", "HT12", "HT18"], motion="From this frame: the dog leans on the lead; he stays put at the gate, about two seconds.",
  prompt=f"""For the line "Here's why the walks got shorter.": at his front gate, Bramble strains ahead on the red lead and he holds back, one hand on his right knee.
Medium shot from hip height, three-quarter front, normal phone lens, head to knees, the dog in front of him.
Image 1: his house and gate. Image 2: the man. Image 3: the dog. Image 4: his outfit.
The same man as Image 2 in {D1}, as in Image 4. The springer spaniel of Image 3, red collar, pulling on a red lead toward the pavement.
Left hand holds the lead, right hand pressed on his right knee; looking down at the dog, brow tight, mouth closed.
In the frame: one man, one dog, one lead, the gate and house front; nothing else.
{GREY}
Clothing plain — no lettering or logos.""")
B["C-02"] = dict(line="Every stride,", face=False, room=False, product=False, body=True,
  refs=[R("C3 Winston sheet (boots)", "frame", C3), R("DOG-BRAMBLE sheet", "character", DOG)],
  taste=["HT02", "HT12", "HT18"], motion="From this frame: two strides along the pavement, one step per second, the dog's paws beside his boots.",
  prompt=f"""For the line "Every stride,": his brown walking boots and the dog's paws step along a grey pavement, side by side.
Close shot at ground level, side profile, normal phone lens, knees down, the kerb running across the frame.
Image 1: the man's boots and legs. Image 2: the dog.
Exactly two boots (Image 1's brown walking boots, grey socks, the hem of navy shorts at the top edge) and the four paws and legs of the springer spaniel of Image 2, one boot mid-stride.
Both of his hands outside the frame above; the dog's head out of frame.
In the frame: two boots, one dog's legs, the pavement, the kerb; nothing else.
{GREY}
Boots and pavement plain — no lettering or logos.""")
B["C-03"] = dict(line="And the pain just lifts.", face=True, room=True, product=False, body=True,
  refs=[R("P4-FIELD plate", "location", FIELD), R("C3 Winston sheet", "character", C3), R("C-HKb (day-2 outfit)", "frame", HKB)],
  taste=["HT01", "HT12", "HT18"], motion="From this frame: his shoulders drop on one breath out and his face eases, about two seconds.",
  prompt=f"""For the line "And the pain just lifts.": standing in the open field, he breathes out and his face eases into relief.
Medium close-up from chest height, three-quarter front, normal phone lens, mid-chest up, the field soft behind.
Image 1: the field. Image 2: the man. Image 3: his outfit.
The same man as Image 2 in {D2}, as in Image 3; the grass and hedges of Image 1 behind.
Both hands down out of frame; eyes half-closed, looking down past the camera, a small easing smile, mouth closed.
In the frame: one man, the field behind; nothing else.
{SOFT}
Clothing plain — no lettering or logos.""")
B["C-04"] = dict(line="So you take the lead back.", face=False, room=True, product=False, body=True,
  refs=[R("C-HKb (gate, red lead)", "location", HKB), R("C3 Winston sheet (hands)", "frame", C3)],
  taste=["HT01", "HT12", "HT18"], motion="From this frame: the lead passes from her hand to his, one pass, about a second.",
  prompt=f"""For the line "So you take the lead back.": at his front gate a woman's hand passes the red dog lead into his big hand.
Close shot at chest height, side profile, normal phone lens, two hands meeting over the gate top, the gate between them.
Image 1: the gate and the red lead. Image 2: the man's hands and skin.
His right hand (Image 2's hands, a grey sweatshirt cuff under a burgundy gilet edge) closing on the lead handle; her left hand (a white woman in her forties, plain blue cardigan cuff) letting go of it.
Exactly two hands, one red lead looping down out of frame.
In the frame: two hands, one lead, the gate top; nothing else.
{SOFT}
Clothing plain — no lettering or logos.""")
B["C-05"] = dict(line="Round the block first.", face=True, room=True, product=True, body=True,
  refs=[R("product_tq_left.jpg", "product", TQ), R("worn_front.jpg", "product", WF), R("C-HKb (his street)", "location", HKB), R("C3 Winston sheet", "character", C3), R("DOG-BRAMBLE sheet", "character", DOG)],
  taste=["FP01", "FP02", "FP03", "FP11", "HT01", "HT12", "HT18"], motion="From this frame: he walks toward the camera along the street, the dog at heel, two steps, about three seconds.",
  prompt=f"""For the line "Round the block first.": he walks toward the camera along his residential street, Bramble trotting at heel on the red lead.
Medium-full shot from hip height, three-quarter front, normal phone lens, head to feet, the houses of Image 3 behind.
Image 1: the strap. Image 2: the strap worn. Image 3: his street. Image 4: the man. Image 5: the dog.
{STRAP} The same man as Image 4 in {D2}; the springer spaniel of Image 5 at his left side.
Left hand holds the lead, right arm swinging; looking ahead past the camera, a small smile, mouth closed.
In the frame: one man, one dog, one lead, the pavement and houses; nothing else.
{SOFT}
Clothing plain — no lettering or logos but the strap's own wordmark.""")
B["C-06"] = dict(line="Then the field.", face=False, room=True, product=False, body=True,
  refs=[R("P4-FIELD plate", "location", FIELD), R("C3 Winston sheet (build, clothes)", "frame", C3), R("DOG-BRAMBLE sheet", "character", DOG)],
  taste=["HT02", "HT12", "HT18"], motion="From this frame: they walk on along the field path at a normal walking pace, the dog bounding ahead, about three seconds.",
  prompt=f"""For the line "Then the field.": man and dog small on the field path, the dog bounding ahead of him off the lead.
Wide shot from a slightly high angle, three-quarter, normal phone lens, the whole field open, the path curving away.
Image 1: the field. Image 2: the man. Image 3: the dog.
A man in his sixties with the build of Image 2, in {D2}, small in the frame mid-stride, the red lead coiled in his left hand; the springer spaniel of Image 3 a few metres ahead, mid-bound.
His right arm swinging; facing along the path.
In the frame: one man, one dog, the path, the field and hedges; nothing else.
{SOFT}
Clothing plain — no lettering or logos; no second person.""")
B["C-07"] = dict(line="Then the long loop you both miss.", face=False, room=True, product=True, body=True,
  refs=[R("product_tq_left.jpg", "product", TQ), R("worn_front.jpg", "product", WF), R("P4-FIELD plate (hedge path)", "location", FIELD), R("C3 Winston sheet (legs, boots)", "frame", C3), R("DOG-BRAMBLE sheet", "character", DOG)],
  taste=["FP01", "FP02", "FP03", "FP11", "HT02", "HT12", "HT18"], motion="From this frame: three steps away along the hedge path, one step per second, the dog trotting ahead.",
  prompt=f"""For the line "Then the long loop you both miss.": from behind, he walks away along the hedge path, Bramble trotting ahead on the red lead.
Medium shot from knee height, three-quarter back from his right, normal phone lens, waist down, the path leading away.
Image 1: the strap. Image 2: the strap worn. Image 3: the hedge path. Image 4: the man. Image 5: the dog.
{STRAP} A man with the legs and skin of Image 4, stone shorts, brown walking boots, the hem of a burgundy gilet at the top edge; the springer spaniel of Image 5 ahead on the path.
Left hand at his side holding the red lead, right hand out of frame above.
In the frame: one man from the waist down, one dog, one lead, the path and hedge; nothing else.
{SOFT}
Clothing plain — no lettering or logos but the strap's own wordmark.""")
B["C-08"] = dict(line="Get the lead.", face=False, room=True, product=False, body=True,
  refs=[R("P3-PROP-W (his house, sage walls, quarry tiles)", "location", PROPW), R("C3 Winston sheet (hands)", "frame", C3), R("DOG-BRAMBLE sheet", "character", DOG)],
  taste=["HT01", "HT12", "HT18"], motion="From this frame: his hand lifts the lead off the hook, one lift, about a second.",
  prompt=f"""For the line "Get the lead.": in his hall, his hand lifts the red dog lead off a brass hook, Bramble's head at his knee looking up.
Close shot from low, three-quarter, normal phone lens, the hook and his hand at the top, the dog's head below.
Image 1: his house — sage walls, quarry-tiled floor. Image 2: the man's hands and skin. Image 3: the dog.
His right hand (Image 2, a grey sweatshirt cuff) gripping the red lead on the hook; the head of the springer spaniel of Image 3 looking up, ears forward; stone shorts at the edge.
His left hand out of frame.
In the frame: one hand, one red lead, one hook, the dog's head, the sage wall; nothing else.
Soft daylight through front-door glass, muted natural colour. An ordinary iPhone photo, nothing retouched.
Wall and hook plain — no lettering or logos.""")
B["C-09"] = dict(line="Nothing to lose but the pain.", face=True, room=True, product=False, body=True,
  refs=[R("P4-FIELD plate", "location", FIELD), R("C3 Winston sheet", "character", C3), R("DOG-BRAMBLE sheet", "character", DOG), R("C-HKb (day-2 outfit)", "frame", HKB)],
  taste=["HT01", "HT12", "HT18"], motion="From this frame: he laughs once and settles into a wide smile, about a second.",
  prompt=f"""For the line "Nothing to lose but the pain.": in the field, Bramble sitting at his side, he laughs — a real, unguarded laugh.
Medium close-up from chest height, three-quarter front, normal phone lens, chest up, the dog's head at the lower edge.
Image 1: the field. Image 2: the man. Image 3: the dog. Image 4: his outfit.
The same man as Image 2 in {D2}, as in Image 4; the springer spaniel of Image 3 sitting beside him; the field of Image 1 soft behind.
Mouth open in the laugh, eyes creased, looking down at the dog. Left hand resting on the dog's head, right hand out of frame.
In the frame: one man, one dog, the field behind; nothing else.
{SOFT}
Clothing plain — no lettering or logos.""")

if __name__ == "__main__":
    (HERE / "prompts").mkdir(exist_ok=True); (HERE / "clips").mkdir(exist_ok=True)
    for beat, b in B.items():
        (HERE / "prompts" / f"{beat}.v74.txt").write_text(b["prompt"])
        call = {"beat": beat, "kind": "image", "mode": 1, "prompt": b["prompt"], "script_line": b["line"],
                "face": b["face"], "room": b["room"], "product": b["product"], "body": b["body"],
                "refs": [{"label": r["label"], "kind": ("frame" if (not b["face"] and "DOG" in r["label"]) else r["kind"])} for r in b["refs"]], "match": None, "edit_of": None,
                "taste": b["taste"], "anatomy": False, "pair": ["gpt_image_2_5", "gpt_image_2_5"],
                "motion_plan": b["motion"], "ref_urls": [r["url"] for r in b["refs"]]}
        (HERE / "clips" / f"{beat}.img.call.json").write_text(json.dumps(call, indent=1))
        print(beat, len(b["prompt"]))
