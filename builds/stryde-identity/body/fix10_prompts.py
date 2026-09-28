#!/usr/bin/env python3
"""Fix round 10 (user, 2026-09-28): BR-25 image "i need new here" (video: "go down fast, not stopping every step").
New setup: a close low shot at the foot of the flight, waist to feet, coming down towards the camera mid-stride.
Line: "If it doesn't change your stairs, you get your money back." Higgsfield nano_banana_pro."""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import body_prompts as B  # noqa: E402
import fix2_prompts as F2  # noqa: E402
import fix3_prompts as F3  # noqa: E402
FIX = {"BR-25": ("nano_banana_pro", ["C1", "P0", "front", "back", "worn_front"], F2.photo(
    "A close shot from a low angle at the bottom of the staircase, looking up the flight, framed from her waist down to "
    "her feet: Maureen coming DOWN the carpeted stairs towards the camera briskly, caught mid-stride — her right foot "
    "just landing flat on the step below with her right knee flexing and the strap on it facing the camera, her left "
    "foot already lifting off the step above, her dress hem swinging forward with her pace. A folded cardigan is tucked "
    "in both hands at her waist, well away from the handrail. The beige carpet treads with thin brass stair rods run "
    "across the frame. THE SAME STAIRCASE as in the second attached image.",
    "THE SAME WOMAN exactly as in the attached character sheet — Maureen, seventy-four. Wearing a cornflower-blue cotton "
    "dress ending a hand above the knee, navy slip-on shoes.",
    B.PRODUCT + " " + B.WORN + " Seen from the front, exactly as in the last attached worn reference.",
    "soft east morning daylight through the front-door glass.",
    B.WORN_NEG + ", " + F3.RAIL_NEG + ", no both feet on one step, no standing still, no going up, no face in frame, "
    + F2.STAIRS_NEG))}
if __name__ == "__main__":
    out = {}
    for beat, (model, refs, prompt) in FIX.items():
        (HERE / f"{beat}.fix10.t2i.txt").write_text(prompt + "\n")
        out[beat] = {"model": model, "refs": refs, "prompt": prompt,
                     "medias": [{"value": F2.MEDIA[r], "role": "image_references"} for r in refs]}
        print(json.dumps(out[beat]["medias"])); print(prompt.replace("\n\n", " "))
    (HERE / "fix10.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
