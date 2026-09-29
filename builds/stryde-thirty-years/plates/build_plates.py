#!/usr/bin/env python3
"""Step-4 plates for stryde-thirty-years (§30C, §30G, §30K), assembled from Appendix A by ID (never retyped)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
NEGS = lambda *ids: ", ".join(S(i) for i in ids)

# ---- Property Sheet: the wearer's house (PROP-S), fields 1-4 as fills ---------------------
PROP = {
 "[TYPE AND ERA]": "1970s brick semi-detached",
 "[WALL FINISH AND COLOUR]": "smooth painted plaster walls in a warm cream, scuffed at shoulder height along the stairs",
 "[SKIRTING]": "plain square-edged pine skirting, varnished and gone orange with age",
 "[SKIRTING — profile, height, colour]": "plain square-edged pine skirting about twelve centimetres high, varnished and gone orange with age",
 "[ARCHITRAVE]": "matching plain pine architraves",
 "[INTERNAL DOOR AND HANDLE]": "flush pine-veneer internal doors with brushed-steel lever handles",
 "[INTERNAL DOOR — style, colour, handle]": "flush pine-veneer internal doors with brushed-steel lever handles",
 "[CEILING]": "a flat white ceiling with a round white paper lampshade",
 "[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]": "a pale fawn twist-pile carpet on the hall, stairs and living room, changing to beige vinyl tiles only at the kitchen threshold under a silver carpet strip",
 "[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]": "a pale fawn twist-pile carpet on the hall, stairs and living room, changing to beige vinyl tiles only at the kitchen threshold under a silver carpet strip",
 "[RADIATOR]": "a white double-panel radiator under a narrow shelf",
 "[RADIATOR TYPE]": "white double-panel steel radiators",
 "[SWITCHES AND SOCKETS]": "white plastic switches and sockets",
}
CARRIED = ("warm cream walls, orange-varnished pine skirting and architraves, flush pine-veneer doors with brushed-steel levers, "
           "pale fawn carpet")
def fillp(s):
    for k, v in PROP.items(): s = s.replace(k, v)
    assert "[" not in s, s[:200]; return s

PLATES = {}
M1NEG = lambda *extra: "AVOID: " + NEGS(*extra, "NEG-M1", "NEG-FILE", "NEG-LIGHT")

# P0 — the wearer's hall and stairs: property plate, nothing attached (TRAVERSED stairs beats read it)
PLATES["P0-PROP-S"] = dict(model="gpt_image_2_5 sunburst", attach="nothing",
  body=[S("CAM-LOCK"), fillp(S("PLATE-PROP")) +
   " The staircase is a straight flight rising away up the left-hand side of the hall to a landing, with white-painted square spindles and a plain varnished pine handrail on the open side; "
   "the open doorway on the right-hand side of the hall, halfway down, shows the living room beyond, bright with daylight. "
   "At the far end of the hall, under the stairs, a closed pine-veneer door. Named anchors, all fixed: the pine handrail and white spindles; a brass-cased barometer on the wall at the foot of the stairs; "
   "a small oak telephone table with a lamp against the right-hand wall; a row of coat hooks by the front door with a green waxed jacket and a red dog lead hanging from them; a coir doormat.",
   "Daylight only: the frosted glass panel of the white front door behind the camera throws a pale, even wash down the hall carpet, and the landing window at the top of the stairs lights the stairwell from above. "
   "The house faces north at the front, so neither window takes direct sun: the light is soft, cool-neutral and even, the living-room doorway on the right the brightest thing in the hall because that room faces south. "
   "The middle of the hall falls a stop darker, with soft sensor noise on the wall under the stairs.",
   S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
   M1NEG("NEG-PROP") + ", no people, no product, no staged objects"])

# P1 — the wearer's living room: PLATED (chair, drawer, dog), property plate attached
PLATES["P1-S-LIVING"] = dict(model="gpt_image_2_5 sunburst", attach="P0-PROP-S (approved)",
  body=[S("CAM-LOCK"),
   S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", CARRIED) + " " + fillp(S("PROP-SHELL")),
   "The living room at the back of the house, seen from the hall doorway looking in, exactly as it shows through the open doorway on the right of the hall in the attached property reference: "
   "white-framed glazed patio doors in the middle of the far wall looking onto the back garden, a brick fireplace with a gas fire on the left-hand wall, and the sofa along the right-hand wall. "
   "Named anchors, all fixed: a high-backed wing armchair in faded bottle-green velour beside the fireplace, facing into the room, a folded tartan blanket over one arm; "
   "a dark oak sideboard against the right-hand wall under a mirror, with two top drawers and cupboard doors below; a round tartan dog bed on the floor by the patio doors, empty, with a chewed rope toy in it; "
   "a small nest of oak side tables by the armchair with a mug and a paperback on top. A beige three-seater sofa with two cushions. Framed family photographs on the fireplace shelf, faces too small to read.",
   "The room faces south onto the garden: mid-morning sun comes in low through the patio doors on the far wall, laying a warm bright patch across the carpet in front of them, "
   "and the rest of the room is lit by that window's bounce off the cream walls, bright and open to the corners. Highlights clip on the patio-door frames and the glass. No lamps on. "
   "Ambient palette warm neutral: cream walls, fawn carpet, the green of the armchair the strongest colour in the room.",
   S("VIEW-OUT").replace("[WHAT THE PROPERTY'S EXTERIOR SHOWS FROM THIS ROOM'S SIDE, NAMED]",
     "the back garden: a small square of lawn, a paved patio with a bird table, a larch-lap fence and a neighbour's apple tree over it"),
   S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
   M1NEG("NEG-SCENE", "NEG-PROP") + ", no people, no dog, no product, no staged objects"])

WORKSHOP = ("a small orthotics and brace-making workshop in a converted Victorian red-brick back-street unit in the Black Country, Walsall: "
            "whitewashed brick walls gone pale grey, a grey concrete floor worn smooth and scuffed, exposed timber roof trusses with two fluorescent tubes hanging from chains, switched off")
# P2 — workshop, the bench: PLATED (HK2, HK3, every body TH, bench B-roll). Master view of the workshop.
PLATES["P2-WORKSHOP-BENCH"] = dict(model="gpt_image_2_5 sunburst", attach="nothing",
  body=[S("CAM-LOCK"),
   "A single photograph of " + WORKSHOP + ". Taken standing at one end of the long workbench, looking along it: the bench runs down the left-hand side of the frame under a row of three tall iron-framed factory windows set in the brick. "
   "Named anchors, all fixed: the long workbench of thick scarred beech boards, dark with years of glue and oil; a heavy blue cast-iron engineer's vice bolted to the near end of the bench; "
   "a pegboard on the brick wall between the windows hung with shears, hole punches, rivet setters, a rubber mallet and a heat gun; rolls of black neoprene, beige elastic and grey webbing stacked on a low shelf under the bench; "
   "a tall stool at the vice; a battered anglepoise lamp clamped to the bench, switched off. On the bench, loose: a steel rule, a pencil, offcuts of neoprene, a tin of rivets, a mug of tea. "
   "At the far end of the room, blurred, the edge of a rail of finished knee braces hanging on the right, and a pair of green-painted double doors to the yard.",
   "Morning daylight through the three factory windows along the left-hand wall is the only light: the windows face east, so a low, pale sun comes in at an angle across the bench top and falls off towards the right-hand side of the room, "
   "which sits a stop darker with open shadow and soft sensor noise on the far brick. The window panes blow to flat white. Ambient palette: grey-white brick, worn beech, black neoprene, the blue vice the strongest colour.",
   S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
   M1NEG("NEG-SCENE") + ", no people, no product, no readable text, labels or logos, no staged objects"])

# P3 — workshop, the rail aisle: PLATED (HK1 walking selfie), P2 attached (same room, other end)
PLATES["P3-WORKSHOP-RAIL"] = dict(model="gpt_image_2_5 sunburst", attach="P2-WORKSHOP-BENCH (approved)",
  body=[S("CAM-LOCK"),
   "This is THE SAME WORKSHOP as the attached reference image, seen from its other end: the same whitewashed pale grey brick, the same worn grey concrete floor, the same timber trusses and hanging fluorescent tubes, switched off. "
   "Taken standing just inside the green-painted double doors, looking back up the room: the long beech workbench with the blue vice and the three factory windows is now on the right-hand side of the frame, "
   "and down the left-hand side runs a long steel clothes rail on castors hung with finished knee braces on wire hangers — hinged braces with black straps and steel side bars, neoprene knee sleeves in black and beige, "
   "wrap-around supports with velcro — twenty or thirty of them, plain and unbranded, some with brown paper tags on string. Named anchors, all fixed: the steel rail of finished braces on the left; "
   "a wide cutting table in the middle of the floor with a paper pattern, a roll of kraft paper and a pair of shears; the workbench, vice and windows on the right; a wall calendar with a photograph of a canal boat and no readable writing on the brick by the doors.",
   "The same morning light as the reference: the east-facing factory windows, now on the right-hand side of the frame, throw low pale sun across the cutting table and the floor towards the rail, "
   "so the braces on the rail are lit on their right-hand side and fall into open shadow on the left. The windows blow to flat white. Sensor noise in the dark corner behind the rail.",
   S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
   M1NEG("NEG-SCENE") + ", no people, no product, no readable text, labels, tags or logos, no brand names, no staged objects"])

out = {}
for k, p in PLATES.items():
    txt = "\n\n".join(p["body"]); out[k] = dict(model=p["model"], attach=p["attach"], chars=len(txt), prompt=txt)
    pathlib.Path(f"{k}.prompt.txt").write_text(txt)
    print(f"{k:18s} {len(txt):5d}  attach: {p['attach']}")
json.dump(out, open("plates.json", "w"), indent=1)
