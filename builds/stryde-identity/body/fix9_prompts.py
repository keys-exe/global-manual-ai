#!/usr/bin/env python3
"""Fix round 9 (user, 2026-09-28): BR-13 image "hands should be off the rail and will never touch it" · BR-25 "create
a new image and new video — she should never go down slow, she should go down fast". Higgsfield nano_banana_pro."""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import body_prompts as B  # noqa: E402
import fix2_prompts as F2  # noqa: E402
import fix3_prompts as F3  # noqa: E402
RAIL_FAR = ("She walks up close to the WALL side of the staircase, on the left of the treads, far from the handrail, "
            "which runs along the opposite side of the stairs out of her reach. BOTH hands hold a folded bath towel "
            "against her stomach, well away from the rail.")
FIX = {
 "BR-13": ("nano_banana_pro", ["C1", "P0", "front", "back", "worn_front"], F2.photo(
    "A close shot from a low angle at step height, three-quarter front, framed from her chest down to her feet: Maureen "
    "walking UP the carpeted stairs mid-stride — her right foot planted flat on the tread above, right knee bent with the "
    "strap on it facing the camera, her left foot pushing off from the step below. " + RAIL_FAR + " The beige carpet "
    "treads with thin brass stair rods run across the frame. THE SAME STAIRCASE as in the second attached image.",
    "THE SAME WOMAN exactly as in the attached character sheet — Maureen, seventy-four. Wearing a burgundy long-sleeve "
    "jersey tunic, a denim skirt ending a hand above the knee, sheepskin slippers.",
    B.PRODUCT + " " + B.WORN + " Seated exactly as in the last attached worn reference.",
    "soft east morning daylight through the front-door glass.",
    B.WORN_NEG + ", " + F3.RAIL_NEG + ", no hand near the rail, no hand reaching out, no both feet on one step, no face "
    "in frame, " + F2.STAIRS_NEG)),
 "BR-25": ("nano_banana_pro", ["C1", "P0", "front", "back", "worn_front"], F2.photo(
    "A medium-wide from the hall at the foot of the stairs, looking up the flight, three-quarter front: Maureen coming "
    "DOWN the carpeted stairs FAST and confident, caught mid-stride in quick motion — her left foot just leaving the step "
    "above, her right foot swinging down onto the next step, her weight moving forward, the hem of her dress swinging "
    "with the pace, a slight natural motion blur on her swinging foot. She is still on the upper-middle part of the "
    "flight with several steps below her. She carries a folded cardigan in both hands in front of her. " + F3.RAIL_OFF
    + " The FRONT of her right knee faces the camera with the strap on it. " + F2.STAIRS,
    B.C1 + " Wearing a cornflower-blue cotton dress ending a hand above the knee, navy slip-on shoes.",
    B.PRODUCT + " " + B.WORN + " Seen from the front, exactly as in the last attached worn reference.",
    "soft east morning daylight through the front-door glass.",
    B.WORN_NEG + ", " + F3.RAIL_NEG + ", no standing still, no careful slow step, no both feet on one step, no woman at "
    "the bottom of the stairs, no going up, no back to the camera, " + F2.STAIRS_NEG)),
}
if __name__ == "__main__":
    out = {}
    for beat, (model, refs, prompt) in FIX.items():
        (HERE / f"{beat}.fix9.t2i.txt").write_text(prompt + "\n")
        out[beat] = {"model": model, "refs": refs, "prompt": prompt,
                     "medias": [{"value": F2.MEDIA[r], "role": "image_references"} for r in refs]}
        print("##", beat, json.dumps(out[beat]["medias"])); print(prompt.replace("\n\n", " ")); print()
    (HERE / "fix9.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
