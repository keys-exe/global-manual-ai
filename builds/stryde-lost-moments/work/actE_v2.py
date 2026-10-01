#!/usr/bin/env python3
"""stryde-lost-moments — Body 5 round 2 (2026-10-01, user "FIX THOSE").
E-03 Fix "MAKE HE WEARING STRYDE STRAP" → new A/B pair: kneeling as in the confirmed E-04 (A), strap on the right knee, face easing.
Eight picked frames → Kling clips (§35A short prompt, the confirmed motion plan word for word, E6 length).
"""
import json, pathlib
from actE import B, STRAP, REG, R, TQ, BENT, C5
HERE = pathlib.Path(__file__).parent
SP = "/tmp/claude-0/-home-user-global-manual-ai/d5ebeecb-012d-539f-a9cc-ff2ce5209b53/scratchpad/actE/"
E04A = SP + "E-04.A.png"
CAM = "Handheld phone, a gentle breath sway, the camera stays where it is."

e03 = dict(line="And the pain just lifts.", face=True, room=True, product=True, body=True,
  refs=[R("product_tq_left.jpg", "product", TQ), R("worn_bent.jpg", "product", BENT), R("E-04 v1 A (kneel, room, day-2 outfit)", "frame", E04A), R("C5 Clifton sheet", "character", C5)],
  taste=["FP01", "FP02", "FP03", "FP07", "FP11", "FP12", "HT06", "HT07", "HT18", "HT20"],
  motion=B["E-03"]["motion"],
  prompt=f"""For the line "And the pain just lifts.": kneeling on his left knee, right knee up and forward with the strap on it, his shoulders drop on a breath out and his face eases into relief.
Medium shot, low angle, three-quarter front, from his head down to the rug, the strapped right knee in the lower half of the frame.
Image 1 is the strap (three-quarter photo). Image 2 is the strap worn on a bent knee. Image 3 is the man kneeling. Image 4 is his face.
{STRAP} The same man as Image 4, kneeling as in Image 3, in the shirt, shorts and slippers of Image 3.
Eyes softly closing, looking down, a small relieved smile, mouth closed. Both hands resting on his right thigh above the knee, neither touching the strap.
In the frame: one man, the red rug; nothing else.
Warm afternoon sun from the left, lighting the window side of his face. {REG}
Clothing plain — no lettering or logos but the strap's own wordmark; no second strap.""")

PICK = {"E-01": "B", "E-02": "A", "E-04": "A", "E-05": "B", "E-06": "B", "E-07": "A", "E-08": "A", "E-09": "A"}
LEN = json.load(open(HERE / "broll_lengths.json"))
V = {}
V["E-01"] = ("Then he holds, still seated on the sofa edge, both hands on his knees. The same man, cardigan and room as the frame. No standing up, no speaking, no smile.",
  "in_place", [("he stands up", "'still seated', no standing up"), ("he talks", "no speaking"), ("the face changes person", "the same man as the frame")])
V["E-02"] = ("One hand only, five fingers, the cardigan sleeve on the arm; the sofa fabric dents under the palm and springs back a little. No second hand, no fingers merging.",
  "in_place", [("a second hand appears", "one hand only; no second hand"), ("fingers melt into the fabric", "five fingers; no fingers merging"), ("the sofa warps", "fabric dents and springs back")])
V["E-04"] = ("His right hand pushes the small engine along the track. The strap stays rigid and in place just below his right kneecap, wordmark to us; the same rug and track. No standing up, no second strap, no strap sliding.",
  "in_place", [("the strap slides or bends", "strap rigid and in place"), ("he stands back up", "no standing up"), ("the track changes", "the same rug and track")])
V["E-05"] = ("Both hands stay loose at his sides, touching nothing. The strap stays rigid and in place just below his right kneecap. No hands on the knees, no hands on the rug, no second strap.",
  "in_place", [("he pushes up with his hands", "hands loose, touching nothing; no hands on the knees or rug"), ("the strap slides", "strap rigid and in place"), ("he walks off", "ends upright and still")])
V["E-06"] = ("Two hands only, ten fingers; the engine stays one rigid wooden piece, its wheels turning. The sofa arm behind stays empty. No extra fingers, no engine changing shape.",
  "in_place", [("extra fingers", "ten fingers; no extra fingers"), ("the engine morphs", "one rigid wooden piece; no engine changing shape"), ("a hand lands on the sofa", "the sofa arm stays empty")])
V["E-07"] = ("He stays standing in place, legs straight, the strap rigid just below his right kneecap; the girl and boy stay beside him holding his hands. No pulling, no walking, no lifting.",
  "in_place", [("the kids haul him", "no pulling"), ("they walk out of frame", "stays in place; no walking"), ("the strap slides", "strap rigid")])
V["E-08"] = ("The boy keeps one hand on the engine; their grandfather stays kneeling behind the track, watching. Every track piece stays whole. No extra children, no pieces appearing.",
  "in_place", [("a third child appears", "no extra children"), ("track pieces multiply", "every piece whole; no pieces appearing"), ("grandfather gets up", "stays kneeling behind the track")])
V["E-09"] = ("His right hand stays on his chest, his left on his thigh; he stays kneeling. No standing up, no speaking.",
  "in_place", [("he stands", "stays kneeling"), ("he speaks", "no speaking"), ("the laugh becomes a grimace", "settles into a wide smile")])

if __name__ == "__main__":
    (HERE / "prompts" / "E-03.v74b.txt").write_text(e03["prompt"])
    call = {"beat": "E-03", "kind": "image", "mode": 1, "prompt": e03["prompt"], "script_line": e03["line"], "face": True, "room": True,
            "product": True, "body": True, "refs": [{"label": r["label"], "kind": r["kind"]} for r in e03["refs"]], "match": None, "edit_of": None,
            "taste": e03["taste"], "anatomy": False, "pair": ["gpt_image_2_5", "gpt_image_2_5"], "motion_plan": e03["motion"],
            "ref_urls": [r["url"] for r in e03["refs"]], "fix_note": "MAKE HE WEARING STRYDE STRAP → reframed from MCU to a kneeling medium shot, strap on the right knee a quarter of the frame wide"}
    (HERE / "clips" / "E-03.img2.call.json").write_text(json.dumps(call, indent=1)); print("E-03 img", len(e03["prompt"]))
    for b, (facts, sm, risks) in V.items():
        p = f'For the line "{B[b]["line"]}": {B[b]["motion"]} {CAM} {facts}'
        (HERE / "prompts" / f"{b}.v1.video.txt").write_text(p)
        c = {"beat": b, "connector": "kling", "mode": 1, "kind": "broll", "prompt": p, "duration": LEN[b]["call_s"], "resolution": "1080p",
             "aspect_ratio": "9:16", "start_image": SP + f"{b}.{PICK[b]}.png", "start_approved": True,
             "approved_by": f"user picked {PICK[b]} on the board (2026-10-01)", "pinned": False, "end_image": None, "end_approved": False,
             "subject_motion": sm, "prefer_multi_shots": "false", "generation": 1, "script_line": B[b]["line"], "motion_plan": B[b]["motion"],
             "motion_confirmed": True, "risk_class": None, "taste": B[b]["taste"], "risks": [{"risk": r, "prevented_by": q} for r, q in risks]}
        (HERE / "clips" / f"{b}.v1.call.json").write_text(json.dumps(c, indent=1)); print(b, len(p))
