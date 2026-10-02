"""Scene 5 ingredient cards (Seedance information, never frames — §4). GPT Image 2.5 Sunburst high 2k 9:16, one render each, as Scene 4's cards.
OUTFIT-N-D4 / OUTFIT-C3-D4: the day-4 clothes laid flat (HT26 — both differ from the sheets). C3-FACE / N-AFTER-FACE: face-and-hair crops of the
confirmed sheets (no render). PROD-HAND-CARD / COLOUR-FRONT-CARD: the product, with the product sheet's locked strings (facelove_product_sheet.py)
and the client's photos attached (Canonical set — attachable)."""
import importlib.util, json
from pathlib import Path
H = Path(__file__).parent; B = H.parents[1]
_p = importlib.util.spec_from_file_location("ps", B / "product/facelove_product_sheet.py"); PS = importlib.util.module_from_spec(_p); _p.loader.exec_module(PS)
FILM = "Natural, neutral colour, real texture, a still from a feature film."
MEDIA = {"CLOSED": "7278afd1-9898-41bb-a85f-e23b1e645a73", "BALM": "e85268b0-5816-4e38-bf31-5f7f829ae31e", "BRUSH": "10c8c91d-dff7-4675-b394-d414a19f9ec8",
         "C3-FACE": "16a0127c-0945-4187-ae78-eabf7c732819", "N-AFTER-FACE": "860d3197-f292-42d0-9357-6d8b2427389a", "N-FACE": "67d1090e-3546-45d1-ae77-8a07bb5709fa"}
CARDS = {
 "OUTFIT-N-D4": dict(refs=[], prompt=(
  "A wardrobe reference card from a film's costume department: one woman's at-home outfit laid out flat on a plain pale grey linen background, seen from directly above, "
  "neatly arranged as if worn. Counted, and only these: exactly one faded sage-green cotton crew-neck sweatshirt, soft and slightly pilled, the cuffs a little stretched; "
  "exactly one pair of grey cotton jersey lounge trousers with a drawstring waist; exactly one pair of plain grey socks; exactly one plain black hair elastic beside the collar. "
  "Ordinary worn-in clothes of a woman of forty-nine who has stopped making an effort, nothing new, nothing styled. Soft even daylight. " + FILM +
  " No person, no body, no mannequin, no shoes, no jewellery, no logos or print on the sweatshirt, no text or captions anywhere.")),
 "OUTFIT-C3-D4": dict(refs=[], prompt=(
  "A wardrobe reference card from a film's costume department: one woman's smart-casual afternoon outfit laid out flat on a plain pale grey linen background, seen from directly above, "
  "neatly arranged as if worn. Counted, and only these: exactly one light-blue chambray button-front shirt with the sleeves rolled to the elbow; exactly one pair of white straight-leg jeans; "
  "exactly one pair of tan leather ballet flats; exactly one black zip garment bag on a hanger laid beside them. Neat, easy clothes of a confident woman of forty-nine. "
  "Soft even daylight. " + FILM + " No person, no body, no mannequin, no jewellery, no logos anywhere, no text or captions anywhere.")),
 "PROD-HAND-CARD": dict(refs=[("CLOSED", "product", "Image 1 · the closed stick")], prompt=(
  "Image 1 is the product: the FACELOVE Changing Foundation Stick, closed. This picture is a reference card of how it is held: a close-up of one woman's right hand, fair skin, "
  "short natural nails, the light-blue chambray cuff of a rolled sleeve at the wrist, holding exactly one stick against a plain soft blush-beige background. "
  + PS.REF_PROD + " here closed at both ends, both caps on. " + PS.HOLD_LOCK + " Soft daylight from the left, one broad soft highlight down the barrel. " + FILM +
  " NEGATIVES: " + PS.NEG_ORIENT + ", no second hand, no face, no text or captions anywhere.")),
 "COLOUR-FRONT-CARD": dict(refs=[("N-FACE", "character", "Image 1 · Susan's own skin"), ("BRUSH", "product", "Image 2 · the brush end")], prompt=(
  "Image 1 is Susan's face; Image 2 is the brush end of the FACELOVE stick. This picture is a reference card of how the colour changes on her skin: an extreme close-up of her "
  "left cheekbone in soft window light, her real mature skin with every pore, fine line and the crease at the corner of her eye exactly as in Image 1. Across the cheekbone lies one "
  "short band of solid warm-neutral white balm. The brush end from Image 2 works the lower end of the band in small circles: "
  + PS.CONTACT_LOCK_C.replace("[END]", "brush") + " The colour resolves from inside the cream at the edge the brush has worked: white ahead of the brush crown, her own skin tone behind it. "
  + PS.TERRAIN_LOCK + " " + FILM + " NEGATIVES: " + PS.NEG_CONTACT + ", " + PS.NEG_SURFACE_FAILURES + ", " + PS.NEG_LOOK + ", no text or captions anywhere.")),
}
if __name__ == "__main__":
    for k, c in CARDS.items():
        (H / "ingredients" / f"{k}.prompt.txt").write_text(c["prompt"])
    json.dump({k: {"prompt": c["prompt"], "refs": c["refs"], "media": [MEDIA[r[0]] for r in c["refs"]], "model": "gpt_image_2_5 · sunburst · high · 2k · 9:16"} for k, c in CARDS.items()},
              open(H / "ingredients" / "cards.json", "w"), indent=1, ensure_ascii=False)
    json.dump(MEDIA, open(H / "ingredients" / "media.json", "w"), indent=1)
    print({k: len(c["prompt"]) for k, c in CARDS.items()})
