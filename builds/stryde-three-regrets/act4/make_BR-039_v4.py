"""BR-039 image v4 (§6A, user Fix "USE THE LATEST BACK OF THE STRYDE PRODUCT", 2026-09-30): the latest back reference is products/stryde/stryde_refs/back_ref_v2.png (clean studio back view, added 2026-09-30) → an edit of the confirmed v3 frame (her hands, the bedroom, the hold kept), the back copied exactly from back_ref_v2 (Image 2). FP04/FP12."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "A silicone pad inside holds pressure on that one band instead of spreading it round the whole knee."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — her two hands, the thin gold watch, the sunny pale-blue bedroom, the quilt, the hold, the close angle slightly above and the window light from the right. Image 1 is that photo.\n'
    "Change only the back of the strap she holds up: Image 2 is the real back of the product — copy it exactly, same shape, same parts, same markings, nothing redesigned. A matte-black shell; set into it a mid-grey rubbery pad in a curved bow-tie outline, wide at both ends and pinched in the middle, covered in fine curved grooves; down its middle one smooth, ungrooved raised bolster, thick at both ends and waisted in the centre; a polished chrome slide at each end with the black knit band looped through. True size: the shell about 12 × 5 cm, a little wider than her palm.\n"
    "In frame: two hands, her fingertips holding the shell's two ends from behind; the strap's back takes about a third of the frame width, the whole grey pad in view.\n"
    "No lettering or logos, no holes in the pad, no extra fingers.")
call = {"beat": "BR-039", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": False, "room": True, "product": True, "body": True,
        "refs": [{"label": "BR-039 v3 frame", "kind": "frame"}, {"label": "back_ref_v2.png (latest back)", "kind": "product"}],
        "match": "frame", "edit_of": "5c53a554-ec93-4e7e-9394-4717d1247696", "taste": ["HT06", "HT07", "HT17", "HT18", "FP04", "FP06", "FP12"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "fix_note": "USE THE LATEST BACK OF THE STRYDE PRODUCT: v3's back came from the user's earlier phone photo → edit of v3 with back_ref_v2.png (the latest studio back) copied exactly"}
json.dump(call, open(D + "BR-039.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "BR-039.txt", "w").write(prompt)
print(len(prompt))
