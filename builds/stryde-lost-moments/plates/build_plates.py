#!/usr/bin/env python3
"""Step-4 plates for stryde-lost-moments (§30C, §30G), assembled from Appendix A by ID (never retyped)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
NEGS = lambda *ids: ", ".join(S(i) for i in ids)
TAIL = lambda *ids: [S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
                     "AVOID: " + NEGS(*ids, "NEG-M1", "NEG-FILE") + ", no people, no product, no staged objects, no readable text or signage"]

# ---- Gloria's house (PROP-G) — Property Sheet fields 1-2 ----------------------------------
PROP_G = {
 "[TYPE AND ERA]": "Victorian red-brick terraced",
 "[WALL FINISH AND COLOUR]": "slightly uneven painted plaster walls in a soft buttermilk yellow, scuffed at hip height along the stairs",
 "[SKIRTING]": "tall torus-profile wooden skirting painted in chipped white gloss",
 "[ARCHITRAVE]": "wide moulded architraves in the same chipped white gloss",
 "[INTERNAL DOOR AND HANDLE]": "Victorian four-panel doors stripped to honey-coloured pine with black iron lever handles",
 "[CEILING]": "a high white ceiling with a plaster cornice and a fabric-shaded pendant",
 "[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]": "red-and-cream Victorian encaustic tiles in the hall, changing at the foot of the stairs to a deep-red patterned stair runner held by brass rods",
 "[RADIATOR]": "a white column radiator",
 "[SWITCHES AND SOCKETS]": "old white plastic switches with a round brass bell-push by the door",
}
def fill(s, d):
    for k, v in d.items(): s = s.replace(k, v)
    assert "[" not in s, s[:200]; return s

P = {}
P["P0-PROP-G"] = dict(loc="L-G-STAIRS", attach="nothing", body=[S("CAM-LOCK"), fill(S("PLATE-PROP"), PROP_G) +
  " The staircase rises straight up along the left-hand wall of the narrow hall, open on its right side with white-painted spindles and a dark polished mahogany handrail ending in a turned newel post at the bottom step; "
  "at the far end of the hall a doorway on the right opens into the back kitchen, its window bright. Near the door: a coir doormat, a low wooden shelf with a china bowl for keys and a church newsletter face down, "
  "a row of coat hooks with a lilac raincoat and a tartan shopping trolley folded beneath. A framed family photograph collage hangs halfway up the stair wall.",
  "Daylight only: the front door's stained-glass panel behind the camera throws a soft coloured wash across the tiles, a small landing window at the top of the stairs lights the upper steps from above, "
  "and the middle of the hall sits a stop darker with soft sensor noise on the far wall. The front faces west, so on a morning the hall is lit indirectly from the door glass and the landing window."] + TAIL("NEG-PROP"))

P["P1-HIGHST"] = dict(loc="L-HIGHST", attach="nothing", body=[S("CAM-LOCK"),
  "A single photograph along the pavement of an ordinary British town high street on a weekday, taken at head height from the edge of the kerb: a row of two-storey brick shopfronts running away on the right — a greengrocer with crates of fruit out front under a green awning, a charity shop, a key-cutting kiosk, a café with two metal chairs outside — "
  "a wide paving-slab pavement with a black cast-iron lamppost and a green metal bench bolted to the paving in the foreground left, a litter bin beside it, the road on the left with parked cars. Every shop sign is plain coloured board with no readable lettering.",
  S("LOC-EXT-OVERCAST")] + TAIL("NEG-SCENE"))

P["P2-PARK"] = dict(loc="L-PARK", attach="nothing", body=[S("CAM-LOCK"),
  "A single photograph of a large municipal park in an English town in early autumn, taken at head height from a path junction: a grey tarmac path running away across open mown grass and forking ahead — the short branch turns left back towards the gates, the long branch curves away right around a pond and under a line of big old plane trees — "
  "a green wooden bench at the fork, a black metal waymarker post with blank arrow plates, a few fallen leaves on the path.",
  S("LOC-EXT-SUN")] + TAIL("NEG-SCENE"))

PROP_W = {
 "[TYPE AND ERA]": "1950s pebble-dashed semi-detached house in the Midlands",
 "[WALL FINISH AND COLOUR]": "smooth painted walls in sage green",
 "[SKIRTING — profile, height, colour]": "plain square-edged skirting about twelve centimetres high painted white",
 "[ARCHITRAVE]": "plain flat white architraves",
 "[INTERNAL DOOR — style, colour, handle]": "flush hardboard doors painted white with brushed aluminium lever handles",
 "[CEILING]": "a plain white ceiling with a glass bowl light",
 "[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]": "a mid-brown twist-pile carpet through the front room, changing to red quarry tiles in the hall under a wooden threshold strip",
 "[RADIATOR TYPE]": "white single-panel steel radiators",
 "[SWITCHES AND SOCKETS]": "white plastic switches and sockets",
}
P["P3-PROP-W"] = dict(loc="L-W-FRONTROOM", attach="nothing", body=[S("CAM-LOCK"),
  "A single photograph of the front room of a " + PROP_W["[TYPE AND ERA]"] + ", taken from the doorway looking across the room to the big bay window that faces the street. " + fill(S("PROP-SHELL"), PROP_W) +
  " Named anchors, all fixed: a worn tan leather armchair turned towards the bay window; a dog bed of faded tartan on the floor beside it; a low wooden side table with a folded newspaper and reading glasses; net curtains pulled back in the bay; "
  "on the windowsill a framed photograph and a pot plant. Through the bay: the front garden's low brick wall and gate, the pavement and the houses opposite.",
  S("LOC-LIVING-DAY") + " In this view the bay window is straight ahead, so the daylight comes towards the camera across the room. The front faces south-east.",
  S("VIEW-OUT").replace("[WHAT THE PROPERTY'S EXTERIOR SHOWS FROM THIS ROOM'S SIDE, NAMED]", "the front garden wall and gate, the pavement and the semis opposite")] + TAIL("NEG-PROP"))

P["P4-FIELD"] = dict(loc="L-FIELD", attach="nothing", body=[S("CAM-LOCK"),
  "A single photograph of a big open recreation field on the edge of an English town, taken at head height from a gap in the hedge: rough mown grass running away to a line of oaks, a worn earth path looping along the hedgerow on the left and away round the far edge of the field, "
  "a wooden kissing gate in the foreground right, a dog-waste bin on a post, the backs of houses just visible beyond the far hedge.",
  S("LOC-EXT-SUN")] + TAIL("NEG-SCENE"))

P["P5-GARAGE"] = dict(loc="L-GARAGE", attach="nothing", body=[S("CAM-LOCK"),
  "A single photograph inside a single domestic garage attached to a 1980s brick house, taken from the back of the garage looking out: the white up-and-over door raised, grey daylight from the driveway beyond, a bare concrete floor with an old oil stain, "
  "breeze-block walls painted white long ago. Named anchors, all fixed: a golf bag with its clubs standing against the right-hand wall under a dusty grey dust sheet, only the club heads' shapes showing through it; "
  "a pegboard of hand tools above a workbench on the left; a chest freezer; a folding step stool; a lawnmower; stacked paint tins on a shelf.",
  "Flat grey daylight through the raised door as the only key, falling off towards the back of the garage, the driveway outside blown bright, the corners a stop darker with soft sensor noise; a bare fluorescent tube overhead is off."] + TAIL("NEG-SCENE"))

P["P6-COURSE"] = dict(loc="L-COURSE", attach="nothing", body=[S("CAM-LOCK"),
  "A single photograph of an ordinary members' golf course in England, taken at head height from the edge of a fairway: a long mown fairway running away between rough and a line of silver birches, a putting green in the middle distance with its flag and pin, "
  "a sand bunker to its right, a parked white two-seat golf buggy on the cart path in the foreground left, a wooden bench and a ball-washer post. No club crest, no signage, no lettering.",
  S("LOC-EXT-SUN")] + TAIL("NEG-SCENE"))

PROP_C = {
 "[TYPE AND ERA]": "1970s brick semi-detached house in Birmingham",
 "[WALL FINISH AND COLOUR]": "painted walls in warm terracotta, one chimney-breast wall papered in a faint gold pattern",
 "[SKIRTING — profile, height, colour]": "plain rounded skirting about ten centimetres high in white gloss",
 "[ARCHITRAVE]": "plain rounded white architraves",
 "[INTERNAL DOOR — style, colour, handle]": "dark-stained oak-effect panel doors with brass lever handles",
 "[CEILING]": "a white ceiling with a brass three-arm light fitting",
 "[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]": "honey oak laminate throughout, a large faded red-and-cream patterned rug in the middle of the room",
 "[RADIATOR TYPE]": "white double-panel steel radiators",
 "[SWITCHES AND SOCKETS]": "brushed brass switches and sockets",
}
P["P7-PROP-C"] = dict(loc="L-C-LIVING", attach="nothing", body=[S("CAM-LOCK"),
  "A single photograph of the living room of a " + PROP_C["[TYPE AND ERA]"] + ", taken from beside the door looking across the room to glazed patio doors onto the back garden. " + fill(S("PROP-SHELL"), PROP_C) +
  " Named anchors, all fixed: a deep three-seat sofa in brown velour against the left-hand wall with crocheted blankets over its arms; the patterned rug in front of it scattered with children's toys — a wooden train track in a loop, two small engines, a box of building blocks, a soft rabbit; "
  "a glass-fronted cabinet of family photographs and ornaments; a television on a low unit, its screen dark; a pot plant by the patio doors.",
  S("LOC-LIVING-DAY") + " In this view the patio doors are straight ahead, so the daylight comes towards the camera and across the rug. The back of the house faces south.",
  S("VIEW-OUT").replace("[WHAT THE PROPERTY'S EXTERIOR SHOWS FROM THIS ROOM'S SIDE, NAMED]", "the back garden: a patio, a strip of lawn, a child's slide and a wooden fence")] + TAIL("NEG-PROP"))

P["P8-CONSULT"] = dict(loc="L-CONSULT", attach="nothing", body=[S("CAM-LOCK"),
  "A single photograph of an orthopaedic consulting room in a British hospital outpatients' department, taken from just inside the door: a small, practical room. The window on the right-hand wall with a vertical blind half open, a desk under it facing into the room with a computer monitor turned away, "
  "an examination couch in pale green vinyl with a paper roll against the left-hand wall, a curtain rail around it. Named anchors, all fixed: a life-size anatomical knee model with coloured ligaments on the desk; a wall-mounted lightbox, switched off, beside the door; "
  "a corkboard with pinned leaflets, all blank or unreadable; a pair of crutches leaning in the corner; a hand-gel dispenser. Grey speckled vinyl floor, off-white walls with scuff marks at chair height.",
  "Soft daylight through the half-open blind on the right-hand wall as the key, falling across the desk and fading towards the couch, a flat overhead panel light on and doing little. The window side a stop brighter, highlights clipping on the blind slats, mild sensor noise in the far corner. Ambient palette cool neutral."] + TAIL("NEG-SCENE"))

P["P9-KITCHEN"] = dict(loc="L-KITCHEN", attach="nothing", body=[S("CAM-LOCK"),
  "A single photograph of a bright, ordinary family kitchen in a British 1990s house, taken from the doorway: a large square oak table in the middle of the room with four chairs, a window over the sink on the far wall, cream shaker-style units and a dark laminate worktop running along it, "
  "an oak Welsh dresser against the right-hand wall with plates on its rack and two deep drawers below. Named anchors, all fixed: the oak table with a woven placemat and a fruit bowl of apples; the dresser and its drawers; a kettle and a tea caddy on the worktop; a radio on the windowsill.",
  S("LOC-KITCHEN-DAY")] + TAIL("NEG-SCENE"))

# ---- the dog (C3's dog, recurring in Hook C / Act 4) — property reference, not a §19 person sheet ----
P["DOG-BRAMBLE"] = dict(loc="—", attach="nothing", body=[S("CAM-LOCK"),
  "A reference photo sheet of one dog: THREE PHOTOGRAPHS OF THE SAME ONE DOG stacked on a single tall 9:16 canvas, top to bottom in three equal rows divided by thin pale seams: TOP, the dog standing in full side profile facing left, the whole dog in frame; MIDDLE, the same dog standing facing the camera; BOTTOM, a close-up of the same dog's head facing the camera. "
  "The dog is a middle-aged English springer spaniel, liver-brown and white: a liver-brown head with long wavy liver ears and a white blaze up the muzzle, a white chest and legs heavily flecked with liver ticking, a big liver patch over the back and a docked tail, a slightly grey muzzle, a well-fed build. "
  "A worn red nylon collar with no tag. The same dog, the same markings, the same size in every panel, standing on a plain grey concrete garden patio against a white-painted brick wall, soft overcast daylight from the left in all three.",
  S("CAP-A"), S("CAP-FILE"),
  "AVOID: no different dogs, no markings changing between panels, no second dog, no people, no lead, no harness, no toys, no text, no labels, no studio backdrop, no cartoon, no CGI, " + S("NEG-FILE")])

if __name__ == "__main__":
    out = {}
    for k, v in P.items():
        p = "\n\n".join(v["body"]); out[k] = dict(loc=v["loc"], attach=v["attach"], prompt=p)
        pathlib.Path(f"{k}.prompt.txt").write_text(p); print(k, len(p))
    json.dump(out, open("plates.json", "w"), indent=1)
