"""TH-HK2 frame v14 (§6A, user Fix "change the grey post trays into a close package of stryde", 2026-10-01): an edit of v13 (Image 1); the grey post trays replaced by one closed STRYDE box per the Product Sheet §16 (PACKAGE: rigid two-piece, matte black, ~28 × 16 × 8 cm, the lowercase grey stryde wordmark centred on the lid). Image 2 = PR-061a (confirmed, this build) for the box's look; package_closed.jpg is still missing, so the lid is described in words."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
prompt = (f'For the line "{LINE}": keep this photo exactly as it is — the same camera, framing, light and colour, the same woman, her face, hair, rust-orange needlecord overshirt and cream T-shirt, her hands on the laptop, the laptop, the chair, brick wall, pinboard, shelves, window and desk. Image 1 is that photo.\n'
    "Change only the grey post trays: replace them with one closed stryde box in the same spot, the box in Image 2 copied exactly — same shape, same parts, same markings, nothing redesigned — with its lid on. A rigid two-piece box, a lid over a base, matte black all over, about 28 cm wide, 16 cm deep and 8 cm tall, about a quarter of the frame wide, lying flat. The only print is the lowercase grey stryde wordmark centred on the lid.\n"
    "In frame: one woman, both hands on the keyboard; on the desk only the laptop and the closed box, every other surface bare. Her face square to the lens, both eyes on it, mouth closed.\n"
    "Clothing, walls and papers plain — no lettering, logos or labels except the product's own wordmark; no extra fingers.")
call = {"beat": "TH-HK2", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": True, "room": True, "product": True, "body": True,
        "refs": [{"label": "TH-HK2 frame v13", "kind": "frame"}, {"label": "PR-061a (STRYDE box, confirmed)", "kind": "product"}],
        "match": "frame", "edit_of": "338ef3bd-e344-4fc2-a9ce-a814f6e5d003", "taste": ["HT12", "HT17", "HT18", "HT19", "HT20", "FP02"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "fix_note": "change the grey post trays into a closed package of stryde: edit of v13"}
json.dump(call, open(D + "TH-HK2_frame.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "TH-HK2_frame.txt", "w").write(prompt)
print(len(prompt))
