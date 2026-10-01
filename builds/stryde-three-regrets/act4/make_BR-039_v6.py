"""BR-039 image v6 (§6A, user Fix "USE THIS AS IMAGE BUT CHANGE THE PRODUCT INTO LAST IMAGE I HAVE GIVEN", 2026-09-30): the image given = BR-039 v2 (pixel-matched, job f2032c5a) → an edit of v2 (her hands, gold watch, blue bedroom, quilt, window light, angle kept) with the product replaced by the back in back_ref_v2.png (the user's last image), copied exactly."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "A silicone pad inside holds pressure on that one band instead of spreading it round the whole knee."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — her two hands, the gold watch, the pale-blue bedroom, the window, the quilt, the sunlight and the camera angle. Image 1 is that photo.\n'
    "Change only the product in her hands: replace it with the strap in Image 2, its back facing the lens — copy it exactly, same shape, same parts, same markings, nothing redesigned: a matte-black shell; set into it a mid-grey rubbery pad in a curved bow-tie outline covered in fine curved grooves, one smooth raised bolster down its middle; a polished chrome slide at each end with the black knit band looped through. True size: the shell about 12 × 5 cm, a little wider than her palm.\n"
    "In frame: two hands, each thumb and finger pinching one end of the shell, held flat and level; the whole grey pad in view, taking about a third of the frame width; the band hangs below in a loop.\n"
    "No lettering or logos, no holes in the pad, no extra fingers.")
call = {"beat": "BR-039", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": False, "room": True, "product": True, "body": True,
        "refs": [{"label": "BR-039 v2 frame (the user's pick)", "kind": "frame"}, {"label": "back_ref_v2.png (the user's last image)", "kind": "product"}],
        "match": "frame", "edit_of": "f2032c5a-e864-4626-96f6-77f30b779ba6", "taste": ["HT06", "HT07", "HT17", "HT18", "FP04", "FP06", "FP12"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "fix_note": "USE THIS AS IMAGE BUT CHANGE THE PRODUCT INTO LAST IMAGE I HAVE GIVEN: edit of v2 with the back from back_ref_v2"}
json.dump(call, open(D + "BR-039.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "BR-039.txt", "w").write(prompt)
print(len(prompt))
