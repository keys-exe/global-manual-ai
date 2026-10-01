#!/usr/bin/env python3
"""E-03 round 3 — user Fix on the clip "MAKE HE STAND HAPPY" (2026-10-01).
Diagnosis: the confirmed frame is a kneeling medium shot framed head-to-rug; standing up in it would carry his head out of
frame (or need a camera that travels with him, §27G). Fix at the source: a new standing frame, happy, strap on the right knee
(low angle, the knee nearest the lens so the strap clears the quarter-frame floor), new A/B pair; the clip follows the pick.
"""
import json, pathlib
from actE import STRAP, REG, R, TQ, C5
HERE = pathlib.Path(__file__).parent
SP = "/tmp/claude-0/-home-user-global-manual-ai/d5ebeecb-012d-539f-a9cc-ff2ce5209b53/scratchpad/actE/"
WF = "products/stryde/stryde_refs/worn_front.jpg"
line = "And the pain just lifts."
motion = "From this frame: he straightens to his full height and breaks into a broad, happy smile, about two seconds."
prompt = f"""For the line "{line}": he stands tall on the rug, happy and free of pain, breaking into a broad smile.
Medium shot from a low angle at knee height, three-quarter front, from his head down to his shins, his strapped right knee nearest the lens.
Image 1 is the strap (three-quarter photo). Image 2 is the strap worn on a straight leg. Image 3 is the man in his room and clothes. Image 4 is his face.
{STRAP.replace('exactly as in Image 2', 'as in Image 2')} The same man as Image 4, in the mustard-and-green shirt, olive shorts and navy slippers of Image 3, the bright patio doors of Image 3 soft behind him.
Face lifted, eyes bright, looking ahead past the lens, a wide open smile. Both hands loose at his sides, neither touching the strap; weight even on both feet.
In the frame: one man, the red rug; nothing else.
Warm afternoon sun from the left. {REG}
Clothing plain — no lettering or logos but the strap's own wordmark; no second strap."""
refs = [R("product_tq_left.jpg", "product", TQ), R("worn_front.jpg", "product", WF),
        R("E-03 v3 (room, day-2 outfit)", "frame", SP + "E-03.v2.A.png"), R("C5 Clifton sheet", "character", C5)]
if __name__ == "__main__":
    (HERE / "prompts" / "E-03.v74c.txt").write_text(prompt)
    call = {"beat": "E-03", "kind": "image", "mode": 1, "prompt": prompt, "script_line": line, "face": True, "room": True, "product": True,
            "body": True, "refs": [{"label": r["label"], "kind": r["kind"]} for r in refs], "match": None, "edit_of": None,
            "taste": ["FP01", "FP02", "FP03", "FP07", "FP11", "FP12", "HT01", "HT06", "HT07", "HT18"], "anatomy": False,
            "pair": ["gpt_image_2_5", "gpt_image_2_5"], "motion_plan": motion, "ref_urls": [r["url"] for r in refs],
            "fix_note": "clip Fix MAKE HE STAND HAPPY → kneeling frame can't stand in shot → new standing, smiling frame (low angle, strapped knee nearest the lens)"}
    (HERE / "clips" / "E-03.img3.call.json").write_text(json.dumps(call, indent=1)); print(len(prompt))
