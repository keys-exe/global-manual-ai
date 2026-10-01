"""BR-039 image v8 (§6A, user Fix "USE THIS IMAGE BUT THE PRODUCT MUST ROTATE 180°", 2026-09-30, attaching v6): an edit of v6 with the shell turned 180° in its own plane (upside down): the curved cut-out edge moves from the bottom to the top, the bolster's thick end swaps sides. Hands, room, band, light kept."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "A silicone pad inside holds pressure on that one band instead of spreading it round the whole knee."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — her two hands in the same grip, the gold watch, the pale-blue bedroom, the window, the quilt, the sunlight, the camera angle and the band hanging below. Image 1 is that photo.\n'
    "Change only the strap's shell: turn it 180 degrees in its own plane, upside down, still back to the lens. Its curved cut-out edge, now along the bottom, moves to the top; its straighter wide edge moves to the bottom; the thick end of the raised bolster swaps from left to right. Copy the strap exactly from Image 2 — same shape, same parts, same markings, nothing redesigned. True size: the shell about 12 × 5 cm, a little wider than her palm.\n"
    "In frame: two hands, each thumb and finger pinching one chrome slide at the ends; the whole grey pad in view, about a third of the frame width.\n"
    "No lettering or logos, no holes in the pad, no extra fingers.")
call = {"beat": "BR-039", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": False, "room": True, "product": True, "body": True,
        "refs": [{"label": "BR-039 v6 frame (the user's pick)", "kind": "frame"}, {"label": "back_ref_v2.png", "kind": "product"}],
        "match": "frame", "edit_of": "bd6f0ed7-a9db-423b-a7a2-ea3ad0e56069", "taste": ["HT06", "HT07", "HT17", "HT18", "FP04", "FP06", "FP12"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "fix_note": "USE THIS IMAGE BUT THE PRODUCT MUST ROTATE 180°: edit of v6, shell turned 180° in plane"}
json.dump(call, open(D + "BR-039.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "BR-039.txt", "w").write(prompt)
print(len(prompt))
