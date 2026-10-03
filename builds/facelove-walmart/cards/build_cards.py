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

# ---- Fix round 1 (user's board Fix notes, 2026-10-03) ----
# PROD-HAND-CARD "wrong size of product": v1 was sized by frame fraction in a close insert and came out fat (L53) —
#   v2 sizes it against her hand (sheet §4: closed, four and a half to five barrel widths tall), no fraction.
# COLOUR-FRONT-CARD "wrong product": v1 cropped the barrel to a stub with the face as Image 1 and the product second, and the model
#   invented a glossy deep-purple brush with a chrome collar — v2 puts the brush photo first, keeps the barrel and wordmark in frame,
#   and names the colour and finish.
LOOKS = ("The barrel is a soft pale violet-mauve, a light lilac, in satin anodised metal with one broad soft highlight — never deep purple, "
         "never glossy, never chrome; the stepped collar at the brush end is the same pale lilac satin with one fine machined slot in its face; "
         "one pale letterspaced FACELOVE wordmark runs up the barrel on its front.")
CARDS_V2 = {
 "PROD-HAND-CARD": dict(refs=[("CLOSED", "product", "Image 1 · the closed stick"), ("C3-ROSA", "character", "Image 2 · Rosa — her hand and skin tone only")], prompt=(
  "Image 1 is the product: the FACELOVE Changing Foundation Stick, closed — copied exactly, same shape, same parts, same wordmark, nothing redesigned. Image 2 is Rosa from this film; take only her skin tone and hand from it. "
  + RENDER + " A reference card of how the stick is held and how big it is: Rosa's right hand — warm medium-tan skin, four chunky rounded fingers and a thumb, short natural nails, "
  "the marigold-orange sleeve of her wrap blouse at the wrist — holding exactly one stick upright, seen at arm's length against the soft warm blur of a lamplit hallway, her whole hand and wrist in frame with room around them. "
  "TRUE SIZE: the stick is SLIM — its barrel only a little thicker than her thumb, and the whole closed stick about as long as her hand from the heel of the palm to the fingertips; "
  "four and a half to five times as tall as it is wide, like a slim lipstick-sized wand, never a thick tube; her fingers wrap almost all the way round it. "
  + LOOKS + " " + PS.REF_PROD + " here closed at both ends, both caps on. " + PS.HOLD_LOCK + " " + S("PIX-SPLIT") +
  " Warm lamplight from the left, one broad soft highlight down the barrel. NEGATIVES: " + PS.NEG_ORIENT + ", no oversized stick, no thick tube, no barrel wider than two of her fingers, no second stick, no second hand, no face, no rings, no cartoon version of the product, no lettering anywhere but the stick's own wordmark.")),
 "COLOUR-FRONT-CARD": dict(refs=[("BRUSH", "product", "Image 1 · the brush end — the product"), ("N-MICHELLE-AFTER", "character", "Image 2 · Michelle — face and skin tone")], prompt=(
  "Image 1 is the product: the FACELOVE stick with its brush end open — copied exactly, the same slim pale lilac barrel, the same stepped collar with its slot, the same domed white brush, the same wordmark; nothing redesigned. "
  "Image 2 is Michelle from this film; take her face and skin tone from it. " + RENDER +
  " A reference card of how the colour changes on her skin: a close shot of her right cheek and cheekbone in warm hallway light, her stylised skin with the fine lines and the crease at the corner of her eye exactly as in Image 2, "
  "her eye at the top of the frame. The stick comes in from the lower right, held at its lower barrel by a hand with warm medium-tan skin and chunky rounded fingers: "
  "the brush crown on her cheek and the barrel running down out of the lower right of the frame, with the FACELOVE wordmark visible on it. TRUE SIZE: the brush crown a little smaller than her eye is long, the barrel slim — a little thicker than the fingers holding it. "
  + LOOKS + " Across the cheekbone lies one short band of solid warm-neutral white balm. The brush works the lower end of the band in small circles: "
  + STYL(PS.CONTACT_LOCK_C.replace("[END]", "brush")) + " The colour resolves from inside the cream at the edge the brush has worked: white ahead of the brush crown, her own warm olive skin tone behind it. "
  + STYL(PS.TERRAIN_LOCK) + " " + S("PIX-SPLIT") + " NEGATIVES: no deep purple barrel, no glossy or chrome barrel or collar, no flared brush, no different product, " + STYL(PS.NEG_CONTACT) + ", " + PS.NEG_SURFACE_FAILURES + ", " + PS.NEG_LOOK + ", no lettering anywhere but the stick's wordmark.")),
}


# ---- Fix round 2 (user's board Fix on PROD-HAND-CARD v2: "reduce the size of product") ----
# v2 still drew the stick longer than her whole hand, the barrel nearly two fingers wide. Real: about three quarters of the hand's
# length, the barrel a little thicker than one finger (sheet §4: 4½–5 barrel widths tall). The rest of v2 is right → v3 is an image
# edit of v2 (§24O rule 7, §6A Part 2 rule 3), the product photo second, size said against her fingers and palm only.
HAND_V3 = (
  "Keep this picture exactly as it is — the same hand, the same orange sleeve, the same hallway, the same light, the same angle — and change only the size of the stick. "
  "Image 1 is the picture to keep. Image 2 is the product, the closed FACELOVE stick, copied exactly. "
  "Make the stick SMALLER: the whole closed stick only about three quarters as long as her hand, from the heel of her palm to the tip of her middle finger, "
  "and its barrel only a little thicker than one of her fingers — four and a half to five times as tall as it is wide, a slim lipstick-sized wand. "
  "Her four chunky fingers now wrap right round the slimmer barrel, her fingertips touching the base of her thumb, with the top third of the stick and the wordmark standing clear above her fingers. "
  "Exactly one stick, the same pale lilac satin barrel, the one FACELOVE wordmark running up it, both caps on, nothing else changed. "
  "NEGATIVES: no stick as long as her hand or longer, no barrel as wide as two fingers, no thick tube, no change to the hand, sleeve, hallway or light, no second stick, no lettering anywhere but the stick's own wordmark.")

if __name__ == "__main__":
    out = {}
    for k, c in CARDS.items():
        (H / f"{k}.prompt.txt").write_text(c["prompt"]); out[k] = {"prompt": c["prompt"], "refs": c["refs"], "media": [MEDIA[r[0]] for r in c["refs"]]}
        print(k, len(c["prompt"]))
    json.dump(out, open(H / "cards.json", "w"), indent=1, ensure_ascii=False)
    out2 = {}
    for k, c in CARDS_V2.items():
        (H / f"{k}.v2.prompt.txt").write_text(c["prompt"]); out2[k] = {"prompt": c["prompt"], "refs": c["refs"], "media": [MEDIA[r[0]] for r in c["refs"]]}
        print(k, "v2", len(c["prompt"]))
    json.dump(out2, open(H / "cards.v2.json", "w"), indent=1, ensure_ascii=False)
    (H / "PROD-HAND-CARD.v3.prompt.txt").write_text(HAND_V3); print("PROD-HAND-CARD v3", len(HAND_V3))
