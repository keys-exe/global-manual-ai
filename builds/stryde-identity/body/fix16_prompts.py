#!/usr/bin/env python3
"""Fix round 16 (user, 2026-09-29, on BR-06 fix15): "that is too big". Both renders held the strap across two hands with
a long hanging band. The real photo (stryde_refs/back_real.jpg) is the size anchor: ONE hand, the strap resting across
the palm and fingers, thumb on its lower edge, the shell no longer than the hand, the band's two short ends just past
the slides. Tighter close-up so the hand, not the room, sets the scale. Higgsfield nano_banana_pro, one render."""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[2] / "products" / "stryde"))
import fix2_prompts as F2  # noqa: E402
import stryde_product_sheet as PS  # noqa: E402
MEDIA = dict(F2.MEDIA, back_real="22b9a20f-e671-414f-b7c0-f16b48bcb943")
PAD_NEG = ("no plain black inner pad, no smooth pad without grooves, no black pad, no pad in any colour but mid-grey, "
           "no straight ridge along the pad, no missing raised bump, no glossy gel, no blue pad")
SIZE_NEG = ("no two-handed hold, no strap spanning both hands, no shell longer than the hand, no long hanging band, "
            "no band loop hanging down, no belt, no harness, no oversized strap, no giant shell")
FIX = {"BR-06": ("nano_banana_pro", ["back_real", "C4", "P2", "front"], F2.photo(
    "A close-up, held exactly like the first attached photo (a real photo of this strap in a hand): the surgeon holds "
    "the strap in ONE hand, resting across his open palm and fingers, his thumb pressing lightly on its lower edge, "
    "the inside of the strap turned up towards the camera. Only his one hand, the strap and a little of his charcoal "
    "waistcoat cuff in frame; his desk and the consulting room behind, far out of focus.",
    "The surgeon's hand exactly as in the attached character sheet: broad, long fingers, a white shirt cuff under a "
    "charcoal knitted waistcoat.",
    "TRUE SIZE, exactly as in the real photo: the strap is SMALL — from slide to slide it is no longer than his hand "
    "from wrist crease to fingertips, and its shell is about as tall as his thumb is long. The rigid shell keeps its "
    "moulded curve and is not bent. Only the band's two short ends show, just past each chrome slide, closed round "
    "behind his hand — no loop hangs down. Facing the camera: " + PS.INNER_PAD,
    "cool window daylight from the left, raking gently across the pad's grooves.",
    "no bent shell, no flexed shell, no wordmark visible, " + SIZE_NEG + ", " + PAD_NEG, skin=""))}
if __name__ == "__main__":
    out = {}
    for beat, (model, refs, prompt) in FIX.items():
        (HERE / f"{beat}.fix16.t2i.txt").write_text(prompt + "\n")
        out[beat] = {"model": model, "refs": refs, "prompt": prompt,
                     "medias": [{"value": MEDIA[r], "role": "image_references"} for r in refs]}
        print(len(prompt))
    (HERE / "fix16.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
