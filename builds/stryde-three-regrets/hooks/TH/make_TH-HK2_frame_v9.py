"""TH-HK2 frame v9 (§6A, user Fix "place the laptop to the left side of the woman", 2026-10-01): she sits side-on to the desk facing frame-right, so her left side is the far side, away from the camera — the same direction as the earlier notes ("farther from the camera"). An edit of v8, same camera: the laptop moves past her far (left) arm, back along the desk toward the grey post trays, its screen turned toward her and so showing to the lens at an angle."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — the same camera angle, distance and framing, the same woman, her face, hair, rust-orange needlecord overshirt and cream T-shirt, the chair, brick wall, pinboard, shelves, window, grey post trays, desk and light. Image 1 is that photo.\n'
    "Change only the laptop's position: move it to her left side, the far side of her away from the camera — back along the desk past her left arm, just in front of the grey post trays, so it sits beyond her rather than between her and the lens. Its screen faces her, so from the camera we see the screen at an angle: a pale inbox of soft grey lines too small to read. A plain silver laptop, lid and keys blank. Her left hand rests on its keyboard, her right forearm on the near desk edge. The near desk is bare.\n"
    "In frame: one woman; on the desk only the laptop and the grey post trays, every other surface bare. Her face square to the lens, both eyes on it, mouth closed.\n"
    "No readable text or logos, no extra fingers.")
call = {"beat": "TH-HK2", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": True, "room": True, "product": False, "body": True,
        "refs": [{"label": "TH-HK2 frame v8", "kind": "frame"}],
        "match": "frame", "edit_of": "89378502-0d1c-40e1-b5f2-dca476986b45", "taste": ["HT12", "HT17", "HT18", "HT19", "HT20"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "fix_note": "place the laptop to the left side of the woman: edit of v8, laptop to her far (left) side"}
json.dump(call, open(D + "TH-HK2_frame.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "TH-HK2_frame.txt", "w").write(prompt)
print(len(prompt))
