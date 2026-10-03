#!/usr/bin/env python3
"""Step-4 plates for facelove-walmart (§30C, §30G) — Mode 5 Pixar Film, 16:9 (V7.68.1), assembled from Appendix A by ID.
Mode 5 plate: CAM-ANIM (wide focal, deep focus, 16:9 for the plate only) → the frame → PROP-SHELL / PROP-REF (the house's finishes)
→ LIGHT-ANIM in the room's own terms → LOOK-WALMART → CAP-ANIM; negatives NEG-ANIMFILM + NEG-PIX + NEG-PROP / NEG-SCENE.
Empty rooms: no people, no product, no readable lettering or logos anywhere (§10A: the store is a generic big-box store, never named)."""
import re, json, pathlib
HERE = pathlib.Path(__file__).parent
T = (HERE.resolve().parents[2] / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
def fill(s, d):
    for k, v in d.items(): s = s.replace(k, v)
    assert "[" not in s, s[:200]; return s
LOOK = (HERE.parent / "cast/LOOK.txt").read_text().strip()

CAM = fill(S("CAM-ANIM"), {"[VIRTUAL PACKAGE]": "a large-format sensor with spherical primes", "[FOCAL]": "24",
                           "[DEPTH OF FIELD]": "deep focus, the whole set sharp"}).replace(
    "composed natively for a vertical 9:16 frame with no letterbox bars", "composed as a wide 16:9 location plate with no letterbox bars")
NOTEXT = "AN EMPTY LOCATION PLATE: nobody in frame, nothing held. NO WRITING ANYWHERE IN THE FRAME: no readable lettering, numbers, logos or signage on any surface, package, sign or screen."
CAP = "RENDER. " + S("CAP-ANIM")
def LIGHT(motivation, side, key_q, key_c, fill_c, ratio, extra):
    return fill(S("LIGHT-ANIM"), {"[MOTIVATION]": motivation, "[SIDE]": side, "[KEY QUALITY]": key_q, "[KEY COLOUR]": key_c,
                                  "[FILL COLOUR]": fill_c, "[RATIO]": ratio}) + " " + extra
def NEG(*ids, extra=""):
    return "AVOID: " + ", ".join([S("NEG-ANIMFILM"), S("NEG-PIX")] + [S(i) for i in ids]) + \
        ", no people, no product, no readable text, no logos, no brand names, no store name, no photograph, no live-action" + (", " + extra if extra else "") + "."

SHELL = {"[WALL FINISH AND COLOUR]": "smooth sand-coloured painted walls, a little faded",
         "[SKIRTING — profile, height, colour]": "plain white baseboards about ten centimetres high",
         "[ARCHITRAVE]": "rounded stucco archways between rooms and simple white door casings",
         "[INTERNAL DOOR — style, colour, handle]": "white flat-panel doors with brushed-nickel lever handles",
         "[CEILING]": "white ceilings with a soft knockdown texture",
         "[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]": "large warm terracotta floor tiles through the hall and living room, changing to a soft oatmeal carpet at the bedroom doorway",
         "[RADIATOR TYPE]": "white ceiling air vents", "[SWITCHES AND SOCKETS]": "white rocker switches and outlets"}
CARRIED = "the faded sand walls, white baseboards, rounded stucco archways, white flat-panel doors with nickel levers, terracotta floor tiles turning to oatmeal carpet in the bedroom"
PROP_REF = "Image 1 is the property reference. " + S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", CARRIED)
HOUSE = "a 1990s single-storey stucco ranch house in a quiet suburb of Phoenix, Arizona, lived in by the same woman for thirty years"

P = {}
P["P-HOUSE"] = dict(loc="L-HALL", attach=[], body=[CAM,
  f"A single rendered frame of the entry hall of {HOUSE}, from the middle of the hall at standing eye level, looking toward the front door: "
  "the front door straight ahead at the end of the hall — a solid white door with a tall frosted-glass sidelight on its left and a brass knob, a woven doormat inside it; "
  "a round globe pendant light hanging from the ceiling in the middle of the hall; on the LEFT wall a narrow dark-wood console table with a ceramic bowl for keys and, above it, a round mirror in a thin brass frame; "
  "on the RIGHT wall a wide rounded stucco archway opening into the living room, a lamp glowing faintly beyond it; framed family photographs (soft painted blurs, no readable faces) on the left wall beyond the mirror. "
  + fill(S("PROP-SHELL"), SHELL) + " Lived-in and a little tired, nothing new. " + NOTEXT,
  LIGHT("the globe pendant light overhead and the frosted sidelight", "the hall's left side", "soft and warm", "warm 2900K tungsten",
        "a cool blue-grey dusk through the frosted sidelight", "a quarter",
        "At night: the pendant pools warm light on the terracotta tiles and the console; the frosted glass reads cool blue; the archway glows faintly amber from a lamp in the living room."),
  LOOK, CAP, NEG("NEG-PROP")])

P["L-LIVING"] = dict(loc="L-LIVING", attach=["P-HOUSE"], body=[CAM, PROP_REF,
  f"A single rendered frame of the living room of {HOUSE}, from standing eye level near the window wall, looking across the room toward the archway to the entry hall: "
  "on the LEFT a dusty-rose upholstered wingback armchair angled toward the room, beside it a small round side table with a ceramic table lamp with a pleated cream shade; "
  "in the MIDDLE a low rectangular walnut coffee table, bare except for a small dish; on the RIGHT a long oatmeal three-seat sofa against the wall with two faded cushions; "
  "beyond them, at the back of the frame, the wide rounded archway into the entry hall, and through it the white front door with its frosted sidelight; "
  "a bookshelf of soft blurred books and framed photos on the back wall left of the archway; a woven rug under the coffee table. "
  + fill(S("PROP-SHELL"), SHELL) + " Lived-in, a marriage of thirty years in the objects, nothing new. " + NOTEXT,
  LIGHT("the ceramic table lamp beside the armchair and the dusk through the window behind the camera", "frame left", "soft and warm", "amber 2700K",
        "the cool blue of dusk falling through the window", "a quarter",
        "Early evening: the lamp makes a warm pool around the armchair and the coffee table; the rest of the room falls into soft blue-grey; the hall beyond the archway is dim."),
  LOOK, CAP, NEG("NEG-PROP", "NEG-SCENE")])

P["L-VANITY"] = dict(loc="L-VANITY", attach=["P-HOUSE"], body=[CAM, PROP_REF,
  f"A single rendered frame of the main bedroom of {HOUSE}, from standing eye level just inside the bedroom door, looking at the vanity: "
  "against the far wall a white wooden vanity table with two drawers and a large oval mirror on a stand, a small upholstered stool in faded lilac in front of it, "
  "three vanity bulbs in a strip above the mirror; on the vanity top a few plain unlabelled bottles and jars and a small tray; "
  "on the RIGHT, a window with sheer white curtains beside the vanity; on the LEFT, the corner of a made bed with a cream chenille bedspread and a nightstand with a lamp. "
  + fill(S("PROP-SHELL"), SHELL) + " Lived-in and quiet. " + NOTEXT,
  LIGHT("the vanity bulbs above the mirror and the window to its right", "frame right", "soft", "neutral warm-white 3500K",
        "cool morning daylight from the sheer curtains", "a third",
        "Morning: soft daylight through the sheer curtains from the right; the vanity bulbs on; the mirror reflects the soft blur of the room behind the camera, never a person."),
  LOOK, CAP, NEG("NEG-PROP", "NEG-SCENE", extra="no person reflected in the mirror")])

P["L-PATIO"] = dict(loc="L-PATIO", attach=["P-HOUSE"], body=[CAM, PROP_REF.replace("in a different room of that same house", "at the back of that same house, outdoors"),
  f"A single rendered frame of the back patio of {HOUSE}, from standing eye level under the edge of the patio cover looking out across it: "
  "terracotta tiles, a round wrought-iron table with a mosaic top and two cushioned wrought-iron chairs in the middle; a sand-coloured stucco garden wall at the back, "
  "covered on the RIGHT with magenta bougainvillea; tall terracotta pots with an agave and a lemon tree on the LEFT; a small desert garden of round cacti and gravel beyond the table; "
  "a string of unlit bulbs along the patio beam overhead; a blue sky above the wall. " + NOTEXT,
  LIGHT("the low morning sun over the garden wall", "frame left", "warm and clear", "golden 4300K",
        "cool sky-blue bounce from the open sky", "a quarter",
        "Morning: long soft shadows of the chairs across the tiles toward the camera, the bougainvillea glowing where the sun catches it, the patio cover's shade at the bottom of the frame."),
  LOOK, CAP, NEG("NEG-SCENE")])

STORE = ("inside a huge generic American big-box superstore — bright, clean and endless, with polished pale floors, tall steel shelving, cool blue and white colours, "
         "and plain blue or white overhead sign panels that carry no words at all")
P["L-AISLE"] = dict(loc="L-AISLE", attach=[], body=[CAM,
  f"A single rendered frame {STORE}. From standing eye level a little way down a long household-goods aisle, looking along it toward its end: "
  "tall steel shelves on both sides stocked with brightly coloured packages of paper towels, toilet paper, detergent bottles and boxes (no readable writing on any of them); "
  "at the end of the aisle the wide main walkway crosses left to right; on the RIGHT, the aisle ends in a tall end-cap display stacked with plain blue boxes — the blind corner where the walkway meets the aisle; "
  "beyond the walkway, the next aisles recede into the distance; long rows of cool-white overhead light panels; blank blue hanging aisle markers. " + NOTEXT,
  LIGHT("the long rows of overhead light panels", "above", "broad and even but soft", "cool white 4500K",
        "warm bounce off the polished pale floor", "a quarter",
        "Midday: the floor shines with soft reflections of the shelves; the end-cap and the walkway are a little brighter than the aisle."),
  LOOK, CAP, NEG(extra="no Walmart, no spark logo, no price tags with numbers, no shopping carts, no staff")])

P["L-AISLE-REV"] = dict(loc="L-AISLE", attach=["L-AISLE"], body=[CAM,
  "Image 1 is the same aisle from its other end. This is THE SAME AISLE in the same store, seen from the opposite direction — the same shelves, the same packages, the same floor and lights, nothing restocked or moved.",
  f"A single rendered frame {STORE}. From standing eye level on the wide main walkway, looking straight back into the same long household-goods aisle: "
  "the tall end-cap of plain blue boxes now on the LEFT at the corner of the aisle, the shelves of paper towels, toilet paper and detergent receding on both sides, "
  "and far at the other end of the aisle another cross walkway; cool-white light panels in long rows overhead. " + NOTEXT,
  LIGHT("the long rows of overhead light panels", "above", "broad and even but soft", "cool white 4500K",
        "warm bounce off the polished pale floor", "a quarter", "Midday, the same light as Image 1."),
  LOOK, CAP, NEG("NEG-SCENE", extra="no Walmart, no spark logo, no price tags with numbers, no shopping carts, no staff")])

P["L-STORE-DOORS"] = dict(loc="L-STORE-DOORS", attach=["L-AISLE"], body=[CAM,
  "Image 1 is an aisle of the same store. This is THE SAME STORE — the same polished pale floor, the same cool-white light panels, the same blue-and-white colours.",
  f"A single rendered frame {STORE}. From standing eye level inside the store's front, looking toward the entrance: a wide pair of automatic sliding glass doors standing open in the middle of a glass front wall, "
  "a second pair of glass doors beyond them in the vestibule, also open; through them, a parking lot bathed in golden late-afternoon sun, a few parked cars and palm trees soft in the distance; "
  "a row of nested shopping carts along the RIGHT wall inside the doors; a plain blue welcome mat on the floor between the doors. " + NOTEXT,
  LIGHT("the low golden sun pouring in through the open sliding doors", "straight ahead, behind the doors", "warm and bright", "golden 3800K",
        "the cool-white store light panels overhead", "a quarter",
        "The sunlight throws long warm streaks across the polished floor toward the camera; the store side stays cool; a soft glow blooms around the door frames."),
  LOOK, CAP, NEG(extra="no Walmart, no spark logo, no lettering on the glass, no people outside")])

if __name__ == "__main__":
    out = {}
    for k, p in P.items():
        txt = "\n\n".join(p["body"]); out[k] = {"loc": p["loc"], "attach": p["attach"], "prompt": txt}
        (HERE / f"{k}.prompt.txt").write_text(txt); print(k, len(txt), p["attach"])
    json.dump(out, open(HERE / "plates.json", "w"), indent=1, ensure_ascii=False)
