#!/usr/bin/env python3
"""Step-4 plates and prop cards for facelove-paint-wall (§30C, §30G; plates 16:9 per V7.68.1), assembled from Appendix A by ID (never retyped).
One room — her bright dressing room — seen two ways: L-SHELF (the shelf of collected foundations, the talking-head set) and
L-WALL (the reverse: the bare warm plaster wall prepared for painting). Empty plates, no people, no FACELOVE product, one render each.
Prop cards (9:16): the generic foundation bottle and the generic paint can + roller, so every beat copies the same unbranded props (ED04)."""
import re, json, pathlib
HERE = pathlib.Path(__file__).parent
T = (HERE.parents[2] / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
NEGS = lambda *ids: ", ".join(S(i) for i in ids)
WIDE = "A wide 16:9 reference photograph of the whole space."
TAIL = lambda *ids, extra="": [S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
    "AVOID: " + NEGS(*ids, "NEG-M1", "NEG-FILE") + ", no people, no makeup stick, no staged objects, no readable text, no labels on any bottle or can, no signage, no logos, no brand names" + extra]
def fill(s, d):
    for k, v in d.items(): s = s.replace(k, v)
    assert "[" not in s, s[:200]; return s

# ---- her house (PROP-H): Property Sheet fields 1-2 ----
SHELL = {
 "[WALL FINISH AND COLOUR]": "smooth plaster painted a soft warm white",
 "[SKIRTING — profile, height, colour]": "plain square white skirting about a hand high",
 "[ARCHITRAVE]": "plain flat white door casings",
 "[INTERNAL DOOR — style, colour, handle]": "a white flat-panel door with a slim brushed-brass lever",
 "[CEILING]": "a flat white ceiling with two small recessed downlights, switched off",
 "[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]": "pale whitewashed oak floorboards running through to the hall",
 "[RADIATOR TYPE]": "a slim white ceiling air vent",
 "[SWITCHES AND SOCKETS]": "flat white rocker switches and outlets",
}
BOTTLES = ("a long white floating shelf at shoulder height running most of the wall's width, with a second shelf above it, both lined edge to edge with about forty "
           "foundation bottles she has collected — frosted and clear glass bottles in different shapes and sizes, squat, tall, square and round, with black, gold and white caps and pumps, "
           "each holding a slightly different shade of beige, tan or pinkish liquid foundation, every bottle and cap plain with no label, no lettering and no logo")
P = {}
P["L-SHELF"] = dict(loc="L-SHELF", ar="16:9", body=[S("CAM-LOCK"), WIDE + " " +
  "A single photograph of a bright, clean, uncluttered dressing room in a modern single-storey house in a quiet American suburb, taken at standing chest height from the middle of the room, "
  "looking straight at the back wall: " + fill(S("PROP-SHELL"), SHELL) +
  " On the back wall, " + BOTTLES + ". Below the shelves, a low white dresser with nothing on it but a white ceramic tray; a tall window on the left-hand wall with a sheer white linen curtain; "
  "a white door on the right, closed; an open floor in front of the dresser, about three steps deep, with nothing on it. "
  "Named anchors, all fixed: the two white shelves of unlabelled foundation bottles centred on the back wall; the low white dresser under them; the tall window on the left; the white door on the right.",
  "Bright daylight through the sheer curtain of the tall window on the left as the key, about forty-five degrees to the camera, soft and clean, the room high-key and airy, "
  "the right-hand corner by the door a stop darker with soft sensor noise, the glass bottles catching small highlights. Daylight only, the downlights off."] + TAIL("NEG-PROP"))

P["L-WALL"] = dict(loc="L-WALL", ar="16:9", body=[S("CAM-LOCK"), WIDE + " " +
  "A single photograph of the same bright dressing room turned the other way, taken at standing chest height from in front of the shelves, looking at the opposite wall: "
  "the whole opposite wall is bare, smooth plaster in a warm peach-beige, close to the colour of light warm skin, unpainted and prepared for painting — smooth at a distance, "
  "and up close a network of fine hairline cracks and a soft texture across it, the way skin has fine lines. Masking tape runs along the white skirting; a cream canvas drop cloth covers the floor along the wall; "
  "on the drop cloth near the left end, a plain white metal paint can with its lid off full of a flat pinkish-beige paint, a black plastic paint tray with a little of the same paint in it and a paint roller resting in the tray. "
  "The tall window with the sheer white linen curtain is now on the right-hand wall; pale whitewashed oak floorboards; nothing hangs on the bare wall. "
  "Named anchors, all fixed: the bare warm peach-beige plaster wall; the drop cloth; the open paint can, the tray and roller at its left end; the tall window on the right.",
  "Bright daylight through the sheer curtain of the tall window on the right as the key, raking gently across the plaster so its fine texture just shows, the room high-key and airy, "
  "the far left corner a stop darker with soft sensor noise. Daylight only, the downlights off."] + TAIL("NEG-PROP"))

CARD = ("A plain product reference photograph of one object alone, standing on a plain matte white tabletop against a plain warm-white wall, taken at eye level from about an arm's length, "
        "soft daylight from a window on the left, a soft contact shadow under it, the whole object sharp and centred, filling about a third of the frame's height. ")
P["PROP-BOTTLE"] = dict(loc="PROP", ar="9:16", body=[S("CAM-LOCK"), CARD +
  "The object: one ordinary liquid foundation bottle — a squat square frosted-glass bottle about as tall as a hand is wide, with a matte black pump and a short black cap set beside it, "
  "holding a flat, slightly orange-beige liquid foundation that shows through the frosted glass; the glass and the pump completely plain, no label, no lettering, no logo, no printed shade name. "
  "Exactly one bottle, upright, the cap off and lying on its side beside it.",
  "Soft daylight from the left, a gentle highlight down the left edge of the glass, the wall behind plain and a little brighter on the left."] + TAIL("NEG-PROP"))
P["PROP-PAINT"] = dict(loc="PROP", ar="9:16", body=[S("CAM-LOCK"), CARD.replace("standing on a plain matte white tabletop against a plain warm-white wall", "standing on a cream canvas drop cloth on pale oak floorboards against a bare warm plaster wall").replace("filling about a third of the frame's height", "filling about half of the frame's height") +
  "The objects: one plain white metal paint can, the size of an ordinary one-gallon can, its lid off and leaning against it, full almost to the rim of a smooth, flat pinkish-beige paint; "
  "in front of it a black plastic paint tray with a shallow pool of the same paint, and a paint roller with a white handle and a cream nap roller resting in the tray, the nap half wet with the beige paint. "
  "The can, the lid, the tray and the roller completely plain: no label, no lettering, no colour swatch, no logo. Exactly one can, one tray, one roller.",
  "Soft daylight from the left, the paint surface catching one soft highlight, the drop cloth's folds casting small soft shadows."] + TAIL("NEG-PROP"))

if __name__ == "__main__":
    out = {}
    for k, v in P.items():
        p = "\n\n".join(v["body"])
        p = p.replace("no staged objects, ", "")   # the shelf of bottles, the paint kit and the prop cards are placed on purpose
        out[k] = dict(loc=v["loc"], ar=v["ar"], prompt=p)
        (HERE / f"{k}.prompt.txt").write_text(p); print(k, len(p))
    json.dump(out, open(HERE / "plates.json", "w"), indent=1, ensure_ascii=False)
