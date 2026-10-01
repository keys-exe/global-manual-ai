"""BR-039 image v7 (§6A, user Fix "ROTATE THE PRODUCT", 2026-09-30): v6 held the strap sideways (long side horizontal) → an edit of v6 rotated 90° upright, as in back_ref_v2.png (Image 2): long side vertical, one chrome slide at the top, one at the bottom, her hands holding the two ends. Room, hands, watch, light kept."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "A silicone pad inside holds pressure on that one band instead of spreading it round the whole knee."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — her two hands, the gold watch, the pale-blue bedroom, the window, the quilt, the sunlight and the camera angle. Image 1 is that photo.\n'
    "Change only the strap's orientation: rotate it a quarter turn so it stands upright exactly as in Image 2 — its long side vertical, one chrome slide at the top and one at the bottom, the grey pad with its curved grooves and the raised bolster running top to bottom, back to the lens. Copy the strap exactly from Image 2 — same shape, same parts, same markings, nothing redesigned. True size: the shell about 12 × 5 cm, a little longer than her palm.\n"
    "In frame: two hands — her left hand pinches the top end below the top slide, her right hand pinches the bottom end above the bottom slide; the band hangs down in a loop below; the strap takes about a quarter of the frame width.\n"
    "No lettering or logos, no holes in the pad, no extra fingers.")
call = {"beat": "BR-039", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": False, "room": True, "product": True, "body": True,
        "refs": [{"label": "BR-039 v6 frame", "kind": "frame"}, {"label": "back_ref_v2.png (upright)", "kind": "product"}],
        "match": "frame", "edit_of": "bd6f0ed7-a9db-423b-a7a2-ea3ad0e56069", "taste": ["HT06", "HT07", "HT17", "HT18", "FP04", "FP06", "FP12"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "fix_note": "ROTATE THE PRODUCT: v6 sideways → rotated a quarter turn upright as in back_ref_v2"}
json.dump(call, open(D + "BR-039.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "BR-039.txt", "w").write(prompt)
print(len(prompt))
