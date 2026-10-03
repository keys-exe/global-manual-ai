#!/usr/bin/env python3
"""Step-4 product info cards for facelove-walmart (Seedance ingredients — information, never frames, §4 V7.68.0), Mode 5.
The product sheet's locked strings (facelove_product_sheet.py) + PIX-SPLIT (the product photoreal in the stylised world) + the render line.
Mode 5 adaptation: the sheet's pore clauses are read as stylised skin (no pores in Mode 5, NEG-PIX) — every line and crease kept."""
import importlib.util, json, re, pathlib
H = pathlib.Path(__file__).parent; B = H.parent
_p = importlib.util.spec_from_file_location("ps", B / "product/facelove_product_sheet.py"); PS = importlib.util.module_from_spec(_p); _p.loader.exec_module(PS)
T = (B.parents[1] / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i): return re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S).group(1).strip()
RENDER = "A final frame from a 3D animated feature film, stylised storybook render, the product the one photoreal object in it."
STYL = lambda s: s.replace("Pores stay open and individually resolved, fine lines stay legible", "Fine lines stay legible").replace(", no pores closed over", "").replace(", no skin rendered poreless", "")
MEDIA = {"CLOSED": "47b23ddf-c6c4-4ffa-89c2-77a4ddc312f1", "BALM": "ab69219d-f5c7-448d-92e5-056867ad5ad7", "BRUSH": "aa71f71b-7076-495c-a7d6-8c68af08fce9",
         "C3-ROSA": "702ccb5a-64ac-4585-af45-b7b8443efba6", "N-MICHELLE-AFTER": "7ee60be8-ae88-458d-8d13-d5ebfc2ff6a7"}
CARDS = {
 "PROD-HAND-CARD": dict(refs=[("CLOSED", "product", "Image 1 · the closed stick"), ("C3-ROSA", "character", "Image 2 · Rosa — her hand and skin tone only")], prompt=(
  "Image 1 is the product: the FACELOVE Changing Foundation Stick, closed — copied exactly, same shape, same parts, same wordmark, nothing redesigned. Image 2 is Rosa from this film; take only her skin tone and hand from it. "
  + RENDER + " A reference card of how the stick is held: a close insert of Rosa's right hand — warm medium-tan skin, four chunky rounded fingers and a thumb, short natural nails, "
  "the marigold-orange sleeve of her wrap blouse at the wrist — holding exactly one stick upright by its middle against the soft warm blur of a lamplit hallway. The stick is a little longer than her hand is wide "
  "and fills about a third of the frame's height. " + PS.REF_PROD + " here closed at both ends, both caps on. " + PS.HOLD_LOCK + " " + S("PIX-SPLIT") +
  " Warm lamplight from the left, one broad soft highlight down the barrel. NEGATIVES: " + PS.NEG_ORIENT + ", no second stick, no second hand, no face, no rings, no cartoon version of the product, no lettering anywhere but the stick's own wordmark.")),
 "COLOUR-FRONT-CARD": dict(refs=[("N-MICHELLE-AFTER", "character", "Image 1 · Michelle — her face and skin tone"), ("BRUSH", "product", "Image 2 · the brush end")], prompt=(
  "Image 1 is Michelle from this film; Image 2 is the brush end of the FACELOVE stick, copied exactly. " + RENDER +
  " A reference card of how the colour changes on her skin: an extreme close-up of her right cheekbone in warm hallway light, her stylised skin with the fine lines and the crease at the corner of her eye exactly as in Image 1. "
  "Across the cheekbone lies one short band of solid warm-neutral white balm. The brush end from Image 2 works the lower end of the band in small circles: "
  + STYL(PS.CONTACT_LOCK_C.replace("[END]", "brush")) + " The colour resolves from inside the cream at the edge the brush has worked: white ahead of the brush crown, her own warm olive skin tone behind it. "
  + STYL(PS.TERRAIN_LOCK) + " " + S("PIX-SPLIT") + " NEGATIVES: " + STYL(PS.NEG_CONTACT) + ", " + PS.NEG_SURFACE_FAILURES + ", " + PS.NEG_LOOK + ", no lettering anywhere.")),
}
if __name__ == "__main__":
    out = {}
    for k, c in CARDS.items():
        (H / f"{k}.prompt.txt").write_text(c["prompt"]); out[k] = {"prompt": c["prompt"], "refs": c["refs"], "media": [MEDIA[r[0]] for r in c["refs"]]}
        print(k, len(c["prompt"]))
    json.dump(out, open(H / "cards.json", "w"), indent=1, ensure_ascii=False)
