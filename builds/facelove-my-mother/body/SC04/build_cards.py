"""Scene 4 ingredient cards (Seedance information, never frames — §4). One GPT Image 2.5 Sunburst render each (high, 2k, 9:16), as CAKE-CARD was.
INVITE-CARD / OLD-FOUNDATION-CARD: the props on their surface, top-down, counted (HT23, F11: no lettering).
OUTFIT-N-D2 / OUTFIT-N-D3: Susan's day clothes laid flat — her sheet's outfit is the party outfit, so the face goes in as a face-and-hair crop
of the sheet's close-up panel and these cards carry the clothes (HT26, L21). N-FACE is that crop (no render)."""
import json
from pathlib import Path
from PIL import Image
H = Path(__file__).parent; B = H.parents[1]
FILM = "Natural, neutral colour, real texture, a still from a feature film."
CARDS = {
 "INVITE-CARD": dict(refs=[("P-HOUSE", "71bf2c97-0a9a-49bf-9304-f92e1ad36677", "location", "Image 1 · the same house")], prompt=(
  "Image 1 is the hall of a two-storey 1990s American suburban family house. This picture is a layout card of THAT SAME HOUSE's kitchen island top, seen from directly above, "
  "the camera looking straight down, the frame filled edge to edge by a speckled beige-and-brown granite countertop with a softly rounded edge along the bottom of the frame. "
  "The same era and upkeep as Image 1: nothing new, nothing designer. In the exact centre: exactly one plain cream party invitation card, about the size of a postcard, lying face up, "
  "thick matte card stock with a thin gold border and nothing printed or written on it. Counted, and only these, around it: exactly one black smartphone lying face down near the right edge, "
  "exactly one white ceramic mug of coffee near the top edge, exactly one small stack of three envelopes near the left edge. Cool flat overcast morning daylight from a window on the right, "
  "soft shadows to the left. " + FILM + " No writing, lettering or printing on the invitation, no names, no dates, no people, no hands, no text or captions anywhere.")),
 "OLD-FOUNDATION-CARD": dict(refs=[("L-VANITY", "aeb31e74-e06d-4fdc-9c39-0893e78f59bd", "location", "Image 1 · the same dressing table")], prompt=(
  "Image 1 is the main bedroom of this house with its white dressing table and large mirror under the window. This picture is a layout card of THAT SAME DRESSING TABLE's top, "
  "seen from directly above, the camera looking straight down, the frame filled edge to edge by the white painted wooden tabletop. Copied exactly from Image 1: the same plain unlabelled "
  "cosmetic jars, the hairbrush, the small ceramic dish and the pale wooden jewellery box, pushed to the back edge. In the centre: exactly one plain frosted-glass foundation bottle about "
  "the height of a hand, with a black screw cap, no label, no logo and no writing, a little beige foundation dried round its neck; beside it exactly one beige teardrop makeup sponge with "
  "a smear of beige foundation on its tip. Cool flat morning light through sheer white curtains from the right, soft shadows. " + FILM +
  " No brand, label, logo or writing on any bottle or jar, no second foundation bottle, no people, no hands, no text or captions anywhere.")),
 "OUTFIT-N-D2": dict(refs=[], prompt=(
  "A wardrobe reference card from a film's costume department: one woman's everyday at-home outfit laid out flat on a plain pale grey linen background, seen from directly above, "
  "neatly arranged as if worn, nothing folded away. Counted, and only these: exactly one long grey marl knit cardigan, open, with six small grey buttons, worn soft at the cuffs; "
  "exactly one plain white crew-neck cotton T-shirt laid inside it; exactly one pair of grey cotton jersey lounge trousers with a drawstring waist; exactly one plain tortoiseshell "
  "claw hair clip beside the collar. Ordinary, slightly worn, comfortable clothes of a woman of forty-nine, nothing new, nothing styled. Soft even daylight. " + FILM +
  " No person, no body, no mannequin, no shoes, no jewellery, no logos, no text or captions anywhere.")),
 "OUTFIT-N-D3": dict(refs=[], prompt=(
  "A wardrobe reference card from a film's costume department: one woman's casual Sunday outfit laid out flat on a plain pale grey linen background, seen from directly above, "
  "neatly arranged as if worn. Counted, and only these: exactly one oatmeal-coloured chunky crew-neck knit sweater with ribbed cuffs and hem; exactly one pair of dark indigo straight-leg "
  "jeans with a plain brown leather belt; exactly one pair of plain white leather trainers with white laces. Neat everyday clothes of a woman of forty-nine, nothing styled. "
  "Soft even daylight. " + FILM + " No person, no body, no mannequin, no jewellery, no logos on the trainers or anywhere, no text or captions anywhere.")),
}

if __name__ == "__main__":
    for k, c in CARDS.items():
        (H / "ingredients" / f"{k}.prompt.txt").write_text(c["prompt"])
    json.dump({k: {"prompt": c["prompt"], "refs": c["refs"], "model": "gpt_image_2_5 · sunburst · high · 2k · 9:16"} for k, c in CARDS.items()},
              open(H / "ingredients" / "cards.json", "w"), indent=1, ensure_ascii=False)
    # N-FACE: the face-and-hair crop of the confirmed sheet's close-up panel (bottom right), no clothes (HT26)
    im = Image.open(B / "cast/N-SUSAN_v1.png"); im.crop((660, 1300, 1520, 2210)).save(H / "ingredients/N-FACE.png")
    print({k: len(c["prompt"]) for k, c in CARDS.items()})
