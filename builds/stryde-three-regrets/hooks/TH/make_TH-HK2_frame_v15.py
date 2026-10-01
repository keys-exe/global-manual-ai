"""TH-HK2 frame v15 (§6A, user Fix "remove the second box on the near desk in front of the laptop", 2026-10-01): an edit of v14 (job d8287710) — only the near box removed, bare desk in its place; the closed box by the wall, the woman, laptop, light and camera kept."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — the same camera, framing, light and colour, the same woman, her face, hair, rust-orange needlecord overshirt and cream T-shirt, her hands on the laptop, the laptop, the closed black stryde box by the brick wall, the chair, pinboard, shelves, window and desk. Image 1 is that photo.\n'
    "Change only one thing: remove the black box on the near desk, in front of the laptop at the bottom of the frame. Where it stood, show the bare wooden desk — the same planks, grain and light as the rest of the desk, the desk's front edge running on unbroken.\n"
    "In frame: one woman, both hands on the keyboard; on the desk only the laptop and the one closed box by the wall, every other surface bare. Her face square to the lens, both eyes on it, mouth closed.\n"
    "Clothing, walls and papers plain — no lettering, logos or labels except the product's own wordmark on that box; no extra fingers.")
call = {"beat": "TH-HK2", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": True, "room": True, "product": False, "body": True,
        "refs": [{"label": "TH-HK2 frame v14", "kind": "frame"}],
        "match": "frame", "edit_of": "d8287710-2cf7-4846-9541-390e023e40f9", "taste": ["HT12", "HT17", "HT18", "HT19", "HT20"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "fix_note": "remove the second box on the near desk in front of the laptop: edit of v14"}
json.dump(call, open(D + "TH-HK2_frame.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "TH-HK2_frame.txt", "w").write(prompt)
print(len(prompt))
