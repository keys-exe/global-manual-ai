#!/usr/bin/env python3
# Round 15 (user, 2026-09-29): the real photo + footage of the inside (stryde_refs/back_real.jpg) replace the render back_pad.webp — the raised part is a curved comma-shaped bump, not a straight ridge.
"""Fix round 15 (after 14) (user, 2026-09-29, new back photo of the strap): "this is the back of the strap, can we redo the parts that
have the inner of the strap". The inside is a grey ridged pad with a raised centre ridge (products/stryde/stryde_refs/
back_pad.webp, Higgsfield media 086f75d7), not the plain black pad of back.webp. BR-06 (the only body beat showing the
inside) gets a new image; the hook top shots HK1-T/HK2-T/HK3-T keep their start images (front) and get new videos with
back_pad as the back reference. Higgsfield nano_banana_pro, one render."""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[2] / "products" / "stryde"))
import body_prompts as B  # noqa: E402
import fix2_prompts as F2  # noqa: E402
import fix3_prompts as F3  # noqa: E402
import stryde_product_sheet as PS  # noqa: E402
MEDIA = dict(F2.MEDIA, back_real="22b9a20f-e671-414f-b7c0-f16b48bcb943")
PAD_NEG = ("no plain black inner pad, no smooth pad without ridges, no black pad, no pad in any colour but mid-grey, "
           "no straight ridge along the pad, no missing raised bump, no glossy gel, no blue pad")
FIX = {"BR-06": ("nano_banana_pro", ["C4", "P2", "back_real", "front"], F2.photo(
    "A close-up from chest height across the desk: only the surgeon's two hands and the strap in frame, held up in front "
    "of his charcoal waistcoat, the strap turned so its INSIDE faces the camera, exactly as in the first attached product "
    "photo (the real photo of the inside of the strap: the grey grooved pad with its curved raised bump). The consulting room behind, far out of focus.",
    "The surgeon's hands exactly as in the attached character sheet: broad, long fingers, white shirt cuffs under a "
    "charcoal knitted waistcoat.",
    "The strap in its own natural resting shape: a closed loop — the rigid matte-black shell at the top with its two "
    "rounded peaks and centre notch, a brushed chrome slide at each end, the soft black knit band looping down below. "
    "The shell keeps its moulded curve — it is rigid and is NOT bent, flexed, flattened or pulled open. The hands barely "
    "hold it: fingertips lightly behind the shell's two ends, thumbs resting on its lower edge, no force at all. Facing "
    "the camera: " + PS.INNER_PAD + " " + F3.SMALL,
    "cool window daylight from the left, raking gently across the pad's ridges.",
    "no bent shell, no flexed shell, no flattened shell, no shell pulled wide, no stretched strap, no hands pulling the "
    "ends apart, no wordmark visible, no open band, " + PAD_NEG + ", " + F3.SMALL_NEG + ", " + F2.LOOP_NEG, skin=""))}
if __name__ == "__main__":
    out = {}
    for beat, (model, refs, prompt) in FIX.items():
        (HERE / f"{beat}.fix15.t2i.txt").write_text(prompt + "\n")
        out[beat] = {"model": model, "refs": refs, "prompt": prompt,
                     "medias": [{"value": MEDIA[r], "role": "image_references"} for r in refs]}
        print(len(prompt)); print(prompt)
    (HERE / "fix15.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
