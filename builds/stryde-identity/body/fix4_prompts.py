#!/usr/bin/env python3
"""Fix round 4 (user, 2026-09-28): BR-24 "this should be a productive broll" · BR-25 "she should be going down the
stairs, not already down the stairs". Higgsfield nano_banana_pro, no phone. Writes <BEAT>.fix4.t2i.txt + fix4.json."""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import body_prompts as B  # noqa: E402
import fix2_prompts as F2  # noqa: E402
import fix3_prompts as F3  # noqa: E402
photo, STAIRS, STAIRS_NEG, MEDIA = F2.photo, F2.STAIRS, F2.STAIRS_NEG, F2.MEDIA

FIX = {}
FIX["BR-24"] = ("nano_banana_pro", ["C1", "front", "back", "worn_front"], photo(
    "A medium shot at hip height, three-quarter front, in a small sunny back garden: Maureen pegs a sheet on the washing "
    "line, reaching up with both arms, weight on her right leg, busy and easy, a basket of washing on the lawn beside her. "
    "Framed from her shoulders to her feet so her right knee and the strap on it read clearly.",
    B.C1 + " Wearing a cornflower-blue cotton dress ending a hand above the knee, navy slip-on shoes.",
    B.PRODUCT + " " + B.WORN + " Seated exactly as in the last attached worn reference.",
    "bright late-morning sun, soft shadows on the grass.", B.WORN_NEG))
FIX["BR-25"] = ("nano_banana_pro", ["C1", "P0", "front", "back", "worn_front"], photo(
    "A medium-wide from the hall floor at the foot of the stairs, looking UP the flight, three-quarter front: Maureen is "
    "HALFWAY DOWN the staircase, coming down towards the camera mid-step — her left foot on the sixth step from the bottom "
    "and her right foot reaching down onto the fifth, five empty carpeted steps still below her, carrying a folded cardigan "
    "in both hands in front of her. " + F3.RAIL_OFF + " The FRONT of her right knee faces the camera with the strap on it. "
    + STAIRS,
    B.C1 + " Wearing a cornflower-blue cotton dress ending a hand above the knee, navy slip-on shoes.",
    B.PRODUCT + " " + B.WORN + " Seen from the front: the shell and its wordmark on the FRONT of the knee, facing the "
    "camera, exactly as in the last attached worn reference.",
    "soft east morning daylight through the front-door glass.",
    B.WORN_NEG + ", " + F3.RAIL_NEG + ", no woman at the bottom of the stairs, no woman standing in the hall, no feet on "
    "the hall floor, no woman going up, no back to the camera, " + STAIRS_NEG))

if __name__ == "__main__":
    out = {}
    for beat, (model, refs, prompt) in FIX.items():
        (HERE / f"{beat}.fix4.t2i.txt").write_text(prompt + "\n")
        out[beat] = {"model": model, "refs": refs, "prompt": prompt,
                     "medias": [{"value": MEDIA[r], "role": "image_references"} for r in refs]}
    (HERE / "fix4.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    for k, v in out.items(): print("##", k, json.dumps(v["medias"])); print(v["prompt"].replace("\n\n", " ")); print()
