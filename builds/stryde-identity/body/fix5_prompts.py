#!/usr/bin/env python3
"""Fix round 5 (user Fix note, hourly check 2026-09-28 14:32): BR-22 "remove the hands off the stryde box first in the
image so that there's no distortion in the broll". The closed box alone on the checked cloth, no hands.
Higgsfield nano_banana_pro, no phone. Writes BR-22.fix5.t2i.txt + fix5.json."""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import body_prompts as B  # noqa: E402
import fix2_prompts as F2  # noqa: E402
P = B.P
FIX = {"BR-22": ("nano_banana_pro", ["P1", "package_open", "front"], F2.photo(
    "A close-up from a slightly high angle on the kitchen table with its checked cloth: the closed matte-black stryde box "
    "sits alone on the table, lid firmly on, centred in the frame, soft window light gliding across its matte lid. No one "
    "is touching it. THE SAME KITCHEN exactly as in the first attached image, soft behind.",
    "",
    P.PACKAGE["box"].capitalize() + ". " + P.PACKAGE["logo"].capitalize() + ", exactly as on the lid in the second "
    "attached image. The lid is fully closed and flush all round.",
    "soft indirect west window light.",
    P.NEG_PACKAGE + ", no hands, no fingers, no arms, no person, no open box, no lifted lid, no gap under the lid, no "
    "straps visible", skin=""))}
if __name__ == "__main__":
    out = {}
    for beat, (model, refs, prompt) in FIX.items():
        (HERE / f"{beat}.fix5.t2i.txt").write_text(prompt + "\n")
        out[beat] = {"model": model, "refs": refs, "prompt": prompt,
                     "medias": [{"value": F2.MEDIA[r], "role": "image_references"} for r in refs]}
        print(json.dumps(out[beat]["medias"])); print(prompt.replace("\n\n", " "))
    (HERE / "fix5.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
