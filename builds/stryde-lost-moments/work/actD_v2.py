#!/usr/bin/env python3
"""stryde-lost-moments — Body 4 round 2 (user "CONFIRM AND FIX THOSE", 2026-10-01).
Picks: D-01 A, D-02 A, D-03 B, D-04 A, D-05 A, D-07 A, D-09 B, D-10 B, D-11 B, D-12 A. D-06, D-08 Both wrong · Fix "HE WEARING STRYDE STRAP".
- 7 clips now (§35A): D-03, D-04, D-05, D-07, D-09, D-11, D-12.
- Pinned classes (§35A rule 3): D-01, D-02 travel; D-10 hand on product → end-frame A/B pairs (image edits of the picked start,
  §6A rule 3), on the board as D-xx-END cards; their clips after the pick. Pilots: travel and hand-on-product classes already have
  confirmed clips in this build (SH-04c / B-HKb / C-HKb walks; NS-03b / D-HKb hands on the strap).
- D-06, D-08 re-framed so the strap shows: low angle, head to shins, the strapped right knee nearest the lens; new A/B pairs.
"""
import json, pathlib
from actD import B, REG, STRAP, R, COURSE, C4, HKA, WF, TQ, FRONT
HERE = pathlib.Path(__file__).parent
SP = "/tmp/claude-0/-home-user-global-manual-ai/d5ebeecb-012d-539f-a9cc-ff2ce5209b53/scratchpad/actD/"
PICK = {"D-01": "A", "D-02": "A", "D-03": "B", "D-04": "A", "D-05": "A", "D-07": "A", "D-09": "B", "D-10": "B", "D-11": "B", "D-12": "A"}
LEN = json.load(open(HERE / "broll_lengths.json"))
CAM = "Handheld phone, a gentle breath sway, the camera stays where it is."
V = {
 "D-03": ("His left hand stays on the club, his right hand stays on his right knee; the club stays one straight rigid shaft. No walking, no standing up straight, no speaking.",
          [("he walks off", "no walking"), ("the club bends", "one straight rigid shaft"), ("hands swap places", "left on club, right on knee")]),
 "D-04": ("One hand only; the fingertip lifts and lands once on the skin above the notch. The strap stays rigid and still, the wordmark readable. No hand over the wordmark, no strap sliding.",
          [("the finger covers the wordmark", "no hand over the wordmark"), ("the strap slides", "rigid and still"), ("a second hand appears", "one hand only")]),
 "D-05": ("Both hands stay on the club grip; the club stays rigid and upright. No speaking, no walking.",
          [("he talks", "no speaking"), ("he walks off", "no walking"), ("the club bends", "rigid and upright")]),
 "D-07": ("One hand only; the flagstick stays one straight white rod and the cup's rim stays round. No second hand, no stick bending.",
          [("second hand", "no second hand"), ("the stick bends", "one straight rod; no stick bending"), ("the hole warps", "rim stays round")]),
 "D-09": ("The strap stays still and rigid on his open palm, wordmark to us; his hand does not move. No speaking, no second strap.",
          [("the strap deforms", "still and rigid"), ("he talks", "no speaking"), ("hand regrips", "his hand does not move")]),
 "D-11": ("The strap stays rigid and in place just below his right kneecap; the bag stays one bag with its clubs. No second strap, no second bag.",
          [("strap slides", "rigid and in place"), ("bag duplicates", "no second bag"), ("clubs morph", "one bag with its clubs")]),
 "D-12": ("His right hand stays on the club; he stays where he is. No speaking, no walking.",
          [("he talks", "no speaking"), ("he walks", "stays where he is"), ("club bends", "hand stays on the club")]),
}
END = {
 "D-01": ("Change only where the two men are: both have walked three steps further up the fairway, a little smaller in the frame, each mid-stride, same hands on bag strap and trolley handle.",
          "Clothing, bag and trolley plain — no lettering or logos; no third person.", dict(product=False, face=False, body=True)),
 "D-02": ("Change only the feet: one stride later — the right shoe now landing ahead, the left heel lifting behind; both hands still outside the frame above.",
          "Shoes and socks plain — no lettering or logos; no third foot.", dict(product=False, face=False, body=True)),
 "D-10": ("Change only his right hand: it has lifted the second strap a few centimetres higher into the light, the same strap as Image 2 copied exactly, wordmark to the lens; his left hand stays on his left thigh, the worn strap unchanged.",
          "Shorts and bench plain, the bench otherwise bare — no lettering or logos but the straps' own wordmarks; no third strap.", dict(product=False, face=False, body=True)),
}
NEW = {}
D3IMG = SP + "D-05.A.png"
NEW["D-06"] = dict(line=B["D-06"]["line"], motion=B["D-06"]["motion"],
  refs=[R("product_tq_left.jpg", "product", TQ), R("worn_front.jpg", "product", WF), R("P6-COURSE plate (buggy)", "location", COURSE),
        R("C4 Graham sheet", "character", C4), R("D-HKa (his golf bag)", "frame", HKA), R("D-05 (good-round outfit)", "frame", D3IMG)],
  prompt=f"""For the line "{B['D-06']['line']}": he walks toward the lens past the parked white buggy, bag on his shoulder, his right leg stepping forward.
Medium shot, low angle, three-quarter front, head to shins, the strapped right knee nearest the lens.
Image 1: the strap (three-quarter). Image 2: the strap worn. Image 3: the course and buggy. Image 4: the man. Image 5: his bag. Image 6: his outfit.
{STRAP} The same man as Image 4 in the polo and sleeveless pullover of Image 6, grey shorts, white-and-tan golf shoes, the bag of Image 5 on his right shoulder; the empty buggy of Image 3 behind him.
Right hand on the bag strap, left arm swinging forward; looking ahead past the lens, smiling, mouth closed.
In the frame: one man, one bag, the buggy behind; nothing else.
Afternoon sun from the right. {REG}
Clothing and bag plain — no lettering or logos but the strap's own wordmark; no second strap.""")
NEW["D-08"] = dict(line=B["D-08"]["line"], motion="From this frame: he walks on past the empty buggy at a normal walking pace, three steps, about three seconds.",
  refs=NEW["D-06"]["refs"],
  prompt=f"""For the line "{B['D-08']['line']}": he walks off the green with his bag, striding past the empty white buggy parked just behind him.
Medium shot, low angle, three-quarter front from his right, head to shins, the strapped right knee nearest the lens, the buggy on the left.
Image 1: the strap (three-quarter). Image 2: the strap worn. Image 3: the course and buggy. Image 4: the man. Image 5: his bag. Image 6: his outfit.
{STRAP} The same man as Image 4 in the polo and sleeveless pullover of Image 6, grey shorts, white-and-tan golf shoes, the bag of Image 5 on his right shoulder; the empty buggy of Image 3, its seats bare.
Right hand on the bag strap, left arm swinging; looking ahead, smiling, mouth closed.
In the frame: one man, one bag, one empty buggy, the green; nothing else.
Afternoon sun from behind the lens. {REG}
Clothing and bag plain — no lettering or logos but the strap's own wordmark; no second strap.""")

if __name__ == "__main__":
    for b, (facts, risks) in V.items():
        p = f'For the line "{B[b]["line"]}": {B[b]["motion"]} {CAM} {facts}'
        (HERE / "prompts" / f"{b}.v1.video.txt").write_text(p)
        c = {"beat": b, "connector": "kling", "mode": 1, "kind": "broll", "prompt": p, "duration": LEN[b]["call_s"], "resolution": "1080p",
             "aspect_ratio": "9:16", "start_image": SP + f"{b}.{PICK[b]}.png", "start_approved": True, "approved_by": f"user picked {PICK[b]} + CONFIRM (2026-10-01)",
             "pinned": False, "end_image": None, "end_approved": False, "subject_motion": "in_place", "prefer_multi_shots": "false", "generation": 1,
             "script_line": B[b]["line"], "motion_plan": B[b]["motion"], "motion_confirmed": True, "risk_class": None, "taste": B[b]["taste"],
             "risks": [{"risk": r, "prevented_by": q} for r, q in risks]}
        (HERE / "clips" / f"{b}.v1.call.json").write_text(json.dumps(c, indent=1)); print(b, len(p))
    for b, (change, plain, flags) in END.items():
        start = SP + f"{b}.{PICK[b]}.png"
        refs = [R(f"{b} start (picked {PICK[b]})", "frame", start)] + ([R("front.webp", "product", FRONT)] if b == "D-10" else [])
        p = (f'For the line "{B[b]["line"]}": Keep this photo exactly as it is — the place, the camera, the light, the clothes and everything in it. '
             f'Image 1 is the photo.{" Image 2 is the strap." if b == "D-10" else ""} {change} An ordinary iPhone photo, nothing restyled. {plain}')
        (HERE / "prompts" / f"{b}-END.v74.txt").write_text(p)
        c = {"beat": f"{b}-END", "kind": "image", "mode": 1, "prompt": p, "script_line": B[b]["line"], "face": flags["face"], "room": True,
             "product": flags["product"], "body": flags["body"], "refs": [{"label": r["label"], "kind": r["kind"]} for r in refs], "match": "frame",
             "edit_of": start, "taste": B[b]["taste"], "anatomy": False, "pair": ["gpt_image_2_5", "gpt_image_2_5"], "ref_urls": [r["url"] for r in refs]}
        (HERE / "clips" / f"{b}-END.img.call.json").write_text(json.dumps(c, indent=1)); print(b + "-END", len(p))
    for b, n in NEW.items():
        (HERE / "prompts" / f"{b}.v74b.txt").write_text(n["prompt"])
        c = {"beat": b, "kind": "image", "mode": 1, "prompt": n["prompt"], "script_line": n["line"], "face": True, "room": True, "product": True,
             "body": True, "refs": [{"label": r["label"], "kind": r["kind"]} for r in n["refs"]], "match": None, "edit_of": None,
             "taste": ["FP01", "FP02", "FP03", "FP07", "FP11", "FP12", "HT01", "HT06", "HT18"], "anatomy": False,
             "pair": ["gpt_image_2_5", "gpt_image_2_5"], "motion_plan": n["motion"], "ref_urls": [r["url"] for r in n["refs"]],
             "fix_note": "HE WEARING STRYDE STRAP → reframed: low angle, head to shins, strapped right knee nearest the lens"}
        (HERE / "clips" / f"{b}.img2.call.json").write_text(json.dumps(c, indent=1)); print(b, len(n["prompt"]))
