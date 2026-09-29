#!/usr/bin/env python3
"""Fix round 8 (user, 2026-09-28): BR-13 "give me a new set up … new image and new video". New setup: a low side-on
close shot on the stairs, hips to feet, her free hand hanging beside the untouched rail — easier motion for the model
than a wide full-body climb. Line: "and take the stairs without gripping the rail." Higgsfield nano_banana_pro."""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import body_prompts as B  # noqa: E402
import fix2_prompts as F2  # noqa: E402
import fix3_prompts as F3  # noqa: E402
FIX = {"BR-13": ("nano_banana_pro", ["C1", "P0", "front", "back", "worn_front"], F2.photo(
    "A close shot from a low side angle at step height on the staircase, three-quarter front, framed from her hips down "
    "to her feet: Maureen is walking UP the carpeted stairs mid-stride — her right foot planted flat on the tread above, "
    "right knee bent and taking her weight with the strap on it facing the camera, her left foot pushing off from the "
    "step below, her heel lifting. Her right hand hangs relaxed and empty beside her hip, clearly NOT touching the "
    "mahogany handrail just above it. The beige carpet treads with thin brass stair rods run across the frame; the white "
    "balustrade and the handrail cross the top of the frame. THE SAME STAIRCASE as in the second attached image.",
    F2.B.C1.split(" — ")[0] + " — Maureen, seventy-four. Wearing a burgundy long-sleeve jersey tunic, a denim skirt ending "
    "a hand above the knee, sheepskin slippers.",
    B.PRODUCT + " " + B.WORN + " Seated exactly as in the last attached worn reference.",
    "soft east morning daylight through the front-door glass.",
    B.WORN_NEG + ", " + F3.RAIL_NEG + ", no both feet on one step, no face in frame, " + F2.STAIRS_NEG))}
if __name__ == "__main__":
    out = {}
    for beat, (model, refs, prompt) in FIX.items():
        (HERE / f"{beat}.fix8.t2i.txt").write_text(prompt + "\n")
        out[beat] = {"model": model, "refs": refs, "prompt": prompt,
                     "medias": [{"value": F2.MEDIA[r], "role": "image_references"} for r in refs]}
        print(json.dumps(out[beat]["medias"])); print(prompt.replace("\n\n", " "))
    (HERE / "fix8.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
