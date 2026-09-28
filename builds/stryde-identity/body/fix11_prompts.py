#!/usr/bin/env python3
"""Fix round 11 (user, 2026-09-28): BR-25 "i want a new one where she is going up". Close shot from a few steps above,
looking down the flight, waist to feet, Maureen climbing briskly towards the camera. Higgsfield nano_banana_pro."""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import body_prompts as B  # noqa: E402
import fix2_prompts as F2  # noqa: E402
import fix3_prompts as F3  # noqa: E402
FIX = {"BR-25": ("nano_banana_pro", ["C1", "P0", "front", "back", "worn_front"], F2.photo(
    "A close shot from a few steps higher up the staircase, looking down the flight at a slight downward angle, framed "
    "from her waist down to her feet: Maureen coming UP the carpeted stairs towards the camera briskly, caught "
    "mid-stride — her right foot planted flat on the next step up with her right knee bent and the strap on it facing "
    "the camera, her left foot pushing off from the step below, heel lifting. A folded cardigan is held in both hands "
    "at her waist, well away from the handrail. The beige carpet treads with thin brass stair rods run across the frame "
    "below her. THE SAME STAIRCASE as in the second attached image.",
    "THE SAME WOMAN exactly as in the attached character sheet — Maureen, seventy-four. Wearing a cornflower-blue cotton "
    "dress ending a hand above the knee, navy slip-on shoes.",
    B.PRODUCT + " " + B.WORN + " Seen from the front, exactly as in the last attached worn reference.",
    "soft east morning daylight through the front-door glass below.",
    B.WORN_NEG + ", " + F3.RAIL_NEG + ", no both feet on one step, no standing still, no going down, no face in frame, "
    + F2.STAIRS_NEG))}
if __name__ == "__main__":
    out = {}
    for beat, (model, refs, prompt) in FIX.items():
        (HERE / f"{beat}.fix11.t2i.txt").write_text(prompt + "\n")
        out[beat] = {"model": model, "refs": refs, "prompt": prompt,
                     "medias": [{"value": F2.MEDIA[r], "role": "image_references"} for r in refs]}
        print(prompt.replace("\n\n", " "))
    (HERE / "fix11.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
