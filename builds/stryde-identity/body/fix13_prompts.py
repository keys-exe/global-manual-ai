#!/usr/bin/env python3
"""Fix round 12 (+13: "she should be at the top of the stairs going down") (user, 2026-09-28): BR-25 "i need a new going down the stairs — show her full body going down, not
just that". A full-figure shot, head to feet, from the hall at the foot of the flight. Higgsfield nano_banana_pro."""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import body_prompts as B  # noqa: E402
import fix2_prompts as F2  # noqa: E402
import fix3_prompts as F3  # noqa: E402
FIX = {"BR-25": ("nano_banana_pro", ["C1", "P0", "front", "back", "worn_front"], F2.photo(
    "A full-body shot from the hall floor at the foot of the stairs, looking UP the whole straight flight: Maureen is AT "
    "THE TOP OF THE STAIRS, just starting to come DOWN — standing on the top landing edge with her right foot already "
    "stepping down onto the first step below the landing, her WHOLE BODY in frame from the top of her silver hair to "
    "her shoes, the full flight of empty carpeted steps stretching down between her and the camera, a relaxed, "
    "confident face. She holds a folded cardigan in both hands in front of her. "
    + F3.RAIL_OFF + " The FRONT of her right knee faces the camera with the strap on it. " + F2.STAIRS,
    B.C1 + " Wearing a cornflower-blue cotton dress ending a hand above the knee, navy slip-on shoes.",
    B.PRODUCT + " " + B.WORN + " Seen from the front, exactly as in the last attached worn reference; at this "
    "distance the strap reads small but clear on her right knee.",
    "soft east morning daylight through the front-door glass.",
    B.WORN_NEG + ", " + F3.RAIL_NEG + ", no cropped head, no cropped feet, no close-up, no both feet on one step, no "
    "standing still, no going up, no back to the camera, " + F2.STAIRS_NEG))}
if __name__ == "__main__":
    out = {}
    for beat, (model, refs, prompt) in FIX.items():
        (HERE / f"{beat}.fix13.t2i.txt").write_text(prompt + "\n")
        out[beat] = {"model": model, "refs": refs, "prompt": prompt,
                     "medias": [{"value": F2.MEDIA[r], "role": "image_references"} for r in refs]}
        print(prompt.replace("\n\n", " "))
    (HERE / "fix13.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
