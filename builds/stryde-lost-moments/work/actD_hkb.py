#!/usr/bin/env python3
"""stryde-lost-moments — D-HKb image Fix (board, 2026-10-01): "MAKE HE WALKING ON THE GOLF CORSE".
The confirmed D-HKb (garage, hopping off the step ladder) → a new frame: Graham walking the fairway with his bag,
strap on, the payoff of "not for much longer". A/B pair, GPT Image 2.5 Sunburst i2i (the build's lock), §6A Part 2."""
import json, pathlib
from actD import C4, HKA, COURSE, TQ, WF, STRAP, REG, R
from actD_v2 import SP
HERE = pathlib.Path(__file__).parent
LINE = "Thanks to these life-changing knee straps, not for much longer."
MOTION = "From this frame: he strides on along the fairway at a normal walking pace, three steps, about three seconds."
D3IMG = SP + "D-05.A.png"
REFS = [R("product_tq_left.jpg", "product", TQ), R("worn_front.jpg", "product", WF), R("P6-COURSE plate", "location", COURSE),
        R("C4 Graham sheet", "character", C4), R("D-HKa (his golf bag)", "frame", HKA), R("D-05 (good-round outfit)", "frame", D3IMG)]
PROMPT = f"""For the line "{LINE}": he walks along the sunny fairway bag on his shoulder, his strapped right leg stepping forward.
Medium shot, low angle, side-on from his right, head to shins, the strapped right knee nearest the lens, the fairway behind him.
Image 1: the strap (three-quarter). Image 2: the strap worn. Image 3: the course. Image 4: the man. Image 5: his bag. Image 6: his outfit.
{STRAP} The same man as Image 4 in the polo and sleeveless pullover of Image 6, grey shorts, white-and-tan golf shoes, the bag of Image 5 on his right shoulder; the fairway and trees of Image 3.
Right hand on the bag strap, left arm swinging forward; looking ahead, smiling, mouth closed.
In the frame: one man, one bag, the fairway; nothing else.
Afternoon sun from the right. {REG}
Clothing and bag plain — no lettering or logos but the strap's own wordmark; no second strap."""
if __name__ == "__main__":
    (HERE / "prompts" / "D-HKb.v74.txt").write_text(PROMPT)
    c = {"beat": "D-HKb", "kind": "image", "mode": 1, "prompt": PROMPT, "script_line": LINE, "face": True, "room": True, "product": True,
         "body": True, "refs": [{"label": r["label"], "kind": r["kind"]} for r in REFS], "match": None, "edit_of": None,
         "taste": ["FP01", "FP02", "FP03", "FP07", "FP11", "FP12", "HT01", "HT06", "HT18"], "anatomy": False,
         "pair": ["gpt_image_2_5", "gpt_image_2_5"], "motion_plan": MOTION, "ref_urls": [r["url"] for r in REFS],
         "fix_note": "MAKE HE WALKING ON THE GOLF CORSE → new frame: walking the sunny fairway, bag on shoulder, side-on low angle, strapped right knee nearest the lens"}
    (HERE / "clips" / "D-HKb.img2.call.json").write_text(json.dumps(c, indent=1)); print(len(PROMPT))

# Round 2 (board, 2026-10-01): A picked (v2) → walking = travel, pinned → end-frame A/B pair as an edit of the pick (§6A rule 3).
END_CHANGE = ("Change only where he is: he has taken three more steps along the fairway, his left leg now forward, the same bag on his right shoulder, "
              "the strap still seated below his right kneecap, the camera and the fairway behind him unchanged.")
def write_end():
    start = SP + "D-HKb.v2.A.png"
    p = (f'For the line "{LINE}": Keep this photo exactly as it is — the place, the camera, the light, the clothes, the strap and everything in it. '
         f'Image 1 is the photo. {END_CHANGE} Right hand stays on the bag strap, left arm swinging; looking ahead, smiling, mouth closed. '
         f'An ordinary iPhone photo, nothing restyled. Clothing and bag plain — no lettering or logos but the strap\'s own wordmark; no second strap.')
    (HERE / "prompts" / "D-HKb-END.v74.txt").write_text(p)
    c = {"beat": "D-HKb-END", "kind": "image", "mode": 1, "prompt": p, "script_line": LINE, "face": True, "room": True, "product": False,
         "body": True, "refs": [{"label": "D-HKb start (picked A, v2)", "kind": "frame"}], "match": "frame", "edit_of": start,
         "taste": ["FP01", "FP03", "FP11", "HT01", "HT13"], "anatomy": False, "pair": ["gpt_image_2_5", "gpt_image_2_5"], "ref_urls": [start]}
    (HERE / "clips" / "D-HKb-END.img.call.json").write_text(json.dumps(c, indent=1)); print("END", len(p))

# Round 3 (board, 2026-10-01): end frame A picked → pinned first-and-last clip (travel, 4s; the line holds ~3.6s on the tight VO).
CLIP_FACTS = ("He ends exactly as in the end frame; the same man, bag on his right shoulder and strap below his right kneecap the whole way, "
              "the fairway unchanged. No second person, no camera move.")
def write_clip():
    from actD_v4 import CAM
    p = f'For the line "{LINE}": {MOTION} {CAM} {CLIP_FACTS}'
    (HERE / "prompts" / "D-HKb.v2.video.txt").write_text(p)
    c = {"beat": "D-HKb", "connector": "kling", "mode": 1, "kind": "hook", "prompt": p, "duration": 4, "resolution": "1080p", "aspect_ratio": "9:16",
         "start_image": SP + "D-HKb.v2.A.png", "start_approved": True, "pinned": True, "end_image": SP + "D-HKb-END.A.png", "end_approved": True,
         "approved_by": "user picked the start (A) and end frame (A) on the board + confirm (2026-10-01)", "subject_motion": "travels",
         "prefer_multi_shots": "false", "generation": 2, "fix_note": "MAKE HE WALKING ON THE GOLF CORSE: garage step-ladder frame → new walking-the-fairway frame (picked A) + pinned end frame (A)", "script_line": LINE, "motion_plan": MOTION,
         "motion_confirmed": True, "risk_class": "travel", "pilot": "confirmed", "taste": ["HT01", "HT12", "HT18"],
         "risks": [{"risk": "the man morphs", "prevented_by": "the same man, bag and strap the whole way"},
                   {"risk": "he overshoots", "prevented_by": "ends exactly as in the end frame"},
                   {"risk": "strap slides", "prevented_by": "strap below his right kneecap the whole way"}]}
    (HERE / "clips" / "D-HKb.v2.call.json").write_text(json.dumps(c, indent=1)); print("CLIP", len(p))

# Round 4 (user "FIX THOSE" = go for the third video, 2026-10-01): clip Fix "look too AI".
# Restage at the source: hip-height normal-lens phone shot, soft late light, natural colour; strap framed large, no wide-angle stretch.
PROMPT2 = f"""For the line "{LINE}": he walks the fairway, mid-stride, strapped right leg forward.
Medium-full shot from hip height, side-on from his right, a normal phone lens, head to feet, the fairway behind him.
Image 1: the strap (three-quarter). Image 2: the strap worn. Image 3: the course. Image 4: the man. Image 5: his bag. Image 6: his outfit.
{STRAP} The same man as Image 4 in the polo and sleeveless pullover of Image 6, grey shorts, white-and-tan golf shoes, the bag of Image 5 on his right shoulder; the fairway of Image 3.
Right hand on the bag strap, left arm swinging; looking ahead, a small smile, mouth closed.
In the frame: one man, one bag, the fairway; nothing else.
Soft late-afternoon light through thin cloud, muted natural colour, real skin texture. An ordinary iPhone photo, nothing retouched.
Clothing and bag plain — no lettering or logos but the strap's own wordmark."""
def write_start2():
    (HERE / "prompts" / "D-HKb.v74b.txt").write_text(PROMPT2)
    c = json.load(open(HERE / "clips" / "D-HKb.img2.call.json"))
    c.update(prompt=PROMPT2, fix_note="look too AI (clip) → frames glossy/saturated + low wide-angle stretch → restaged: hip height, normal lens, soft late light, natural colour")
    (HERE / "clips" / "D-HKb.img3.call.json").write_text(json.dumps(c, indent=1)); print("START2", len(PROMPT2))

# Round 5 (board Fix "CHANGE THE ANGLE", 2026-10-01): side-on → three-quarter front, walking diagonally toward the camera; same natural look.
PROMPT3 = PROMPT2.replace(
    "Medium-full shot from hip height, side-on from his right, a normal phone lens, head to feet, the fairway behind him.",
    "Medium-full shot from hip height, three-quarter front from his right, normal phone lens, head to feet, coming toward the camera at an angle, a flag far off.").replace(
    "looking ahead, a small smile", "looking ahead past the camera, a small smile").replace(
    "In the frame: one man, one bag, the fairway; nothing else.", "In the frame: one man, one bag, the fairway, a flag; nothing else.").replace(
    "Soft late-afternoon light through thin cloud, muted natural colour, real skin texture.", "Soft late light through thin cloud, muted natural colour, real skin.")
def write_start3():
    (HERE / "prompts" / "D-HKb.v74c.txt").write_text(PROMPT3)
    c = json.load(open(HERE / "clips" / "D-HKb.img3.call.json"))
    c.update(prompt=PROMPT3, fix_note="CHANGE THE ANGLE → side-on → three-quarter front, walking diagonally toward the camera")
    (HERE / "clips" / "D-HKb.img4.call.json").write_text(json.dumps(c, indent=1)); print("START3", len(PROMPT3))
