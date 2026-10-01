"""TH-HK2 frame v2 (§6A, user Fix "make the laptop facing to her just slight face into the camera", 2026-10-01): v1's screen faced the camera full-on (and showed an app logo + model name) → an edit of v1: the laptop turned to face her, angled only slightly toward the lens, a plain unbranded screen. Woman, room, light, her face to the lens kept."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — the same woman, her face, hair, rust-orange needlecord overshirt and cream T-shirt, the wooden chair, the brick wall, the pinboard, the window, the grey post trays, the desk, the light and the camera. Image 1 is that photo.\n'
    "Change only the laptop: turn it on the desk so its screen faces her, angled just slightly toward the lens — we see the screen edge-on at a steep angle, a narrow sliver of a pale inbox list, mostly the plain grey back of the lid and its side. A plain silver laptop, its lid and keys blank and unmarked. Her right hand stays on its keyboard.\n"
    "In frame: one woman, both hands placed as before; on the desk only the laptop and the grey post trays, every other surface bare. Her face square to the lens, both eyes on it, mouth closed.\n"
    "No readable text or logos, no app names, no extra fingers.")
call = {"beat": "TH-HK2", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": True, "room": True, "product": False, "body": True,
        "refs": [{"label": "TH-HK2 frame v1", "kind": "frame"}],
        "match": "frame", "edit_of": "3f68de11-9346-45f8-91bf-a58399251574", "taste": ["HT12", "HT17", "HT18", "HT19", "HT20"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "fix_note": "make the laptop facing to her just slight face into the camera: edit of v1, laptop turned toward her, unbranded"}
json.dump(call, open(D + "TH-HK2_frame.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "TH-HK2_frame.txt", "w").write(prompt)
print(len(prompt))
