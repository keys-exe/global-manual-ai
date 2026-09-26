#!/usr/bin/env python3
"""Step-4 plates for stryde-identity (§30C, §30G), assembled from Appendix A by ID (never retyped)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

# ---- Property Sheet: Maureen's house (PROP-M), fields 1-4 as fills ------------------------
PROP = {
 "[TYPE AND ERA]": "1930s red-brick end-of-terrace",
 "[WALL FINISH AND COLOUR]": "slightly uneven painted plaster walls in a faded magnolia with a hairline crack or two",
 "[SKIRTING]": "deep ogee-profile wooden skirting painted in yellowed white gloss",
 "[SKIRTING — profile, height, colour]": "deep ogee-profile wooden skirting about twenty centimetres high, painted in yellowed white gloss",
 "[ARCHITRAVE]": "matching moulded architraves in the same yellowed gloss",
 "[INTERNAL DOOR AND HANDLE]": "four-panel wooden internal doors painted white with round brass knobs worn dull at the grip",
 "[INTERNAL DOOR — style, colour, handle]": "four-panel wooden internal doors painted white with round brass knobs worn dull at the grip",
 "[CEILING]": "a plain white ceiling with a faint Artex swirl and a simple pendant light",
 "[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]": "a worn beige carpet on the hall and stairs held by brass stair rods, changing to brown-and-cream patterned vinyl at the kitchen threshold under a brass carpet strip",
 "[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]": "a worn beige carpet on the hall and stairs held by brass stair rods, changing to brown-and-cream patterned vinyl at the kitchen threshold under a brass carpet strip",
 "[RADIATOR]": "a white single-panel steel radiator under a small shelf",
 "[RADIATOR TYPE]": "white single-panel steel radiators",
 "[SWITCHES AND SOCKETS]": "slightly yellowed white plastic switches and sockets",
}
CARRIED = ("faded magnolia walls, yellowed white gloss ogee skirting and architraves, white four-panel doors with dull brass knobs, "
           "worn beige carpet with brass stair rods")
def fillp(s):
    for k, v in PROP.items(): s = s.replace(k, v)
    assert "[" not in s, s[:200]; return s

NEGS = lambda *ids: ", ".join(S(i) for i in ids)

PLATES = {}

# P0 — property plate (PLATE-PROP), nothing attached
PLATES["P0-PROP-M"] = dict(model="gpt_image_2_5 sunburst", attach="nothing",
  body=[S("CAM-LOCK"), fillp(S("PLATE-PROP")) +
   " The staircase rises on the left of frame with a plain white-painted wooden banister and a mahogany-stained handrail; "
   "the open doorway at the far end of the hall on the right shows the kitchen beyond, its window bright. A brown doormat inside the front door, "
   "a small half-moon hall table with a china dish for keys against the right-hand wall, a framed print of a harbour above it, a coat hook with one navy raincoat by the door.",
   "Daylight only: the front door glass behind the camera throws a pale wash down the carpet, the kitchen window at the far end blows to flat white, and the middle of the hall falls a stop darker with soft sensor noise on the far wall. The house faces east at the front; it is morning, so the door glass is the brighter of the two sources.",
   S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
   "AVOID: " + NEGS("NEG-PROP", "NEG-M1", "NEG-FILE") + ", no people, no product, no staged objects"])

# P1 — Maureen's kitchen (PLATED: BR-22, BR-23, BR-24), property plate attached
PLATES["P1-M-KITCHEN"] = dict(model="gpt_image_2_5 sunburst", attach="P0-PROP-M (approved)",
  body=[S("CAM-LOCK"),
   S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", CARRIED) + " " + fillp(S("PROP-SHELL")),
   "The small galley kitchen at the back of the house, seen from the hall doorway looking in: the window over a white ceramic sink on the far wall, "
   "worktops running down both sides, and a small square pine table pushed against the left-hand wall with two chairs. "
   "Named anchors, all fixed: the square pine table with a blue-and-white checked wipe-clean cloth; the cream enamel bread bin on the right-hand worktop; "
   "the wall calendar with a garden photograph and no readable writing, hanging beside the window; the potted red geranium on the windowsill. "
   "Loose on the table: a mug with a tea stain, a folded newspaper face down, a pair of reading glasses. Cupboards are 1980s oak-effect with brass handles, a little tired at the edges.",
   S("LOC-KITCHEN-MORN") + " The kitchen is at the back of the house, facing west, so the morning light here is indirect and even, the sky through the window a flat pale grey.",
   S("VIEW-OUT").replace("[WHAT THE PROPERTY'S EXTERIOR SHOWS FROM THIS ROOM'S SIDE, NAMED]",
     "the narrow back garden: a strip of lawn, a wooden fence and the backs of the terrace opposite"),
   S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
   "AVOID: " + NEGS("NEG-SCENE", "NEG-PROP", "NEG-M1", "NEG-FILE") + ", no people, no product, no staged objects"])

# P2 — consulting room (standalone, PLATED: HK1-T, BR-03, BR-04, BR-06, BR-20)
PLATES["P2-CONSULT"] = dict(model="gpt_image_2_5 sunburst", attach="nothing",
  body=[S("CAM-LOCK"),
   "A single photograph of an orthopaedic consulting room in a British private clinic, taken from just inside the door: a modest room, lived in rather than designed. "
   "The window on the left-hand wall, a desk under it facing into the room, the examination couch against the right-hand wall under a paper roll, and the back wall behind the desk. "
   "Named anchors, all fixed: an X-ray lightbox on the back wall showing two knee X-rays side by side, glowing cool white; a life-size plastic anatomical knee model on the desk; "
   "a tall bookshelf of worn orthopaedic textbooks and box files beside the lightbox; the blue vinyl examination couch with its paper roll. "
   "Loose on the desk: a closed laptop, a pen pot, a small stack of folders, a mug. Grey hard-wearing floor, pale blue-grey walls with scuffs at chair height, a wall-mounted hand gel dispenser by the door.",
   "Cool overcast daylight through the left-hand window as the key, falling across the desk and fading towards the couch; the lightbox adds its own cold glow on the back wall; "
   "a flat overhead ceiling panel light is on and does little. Highlights clip on the window frame and on the lightbox. The room sits slightly dim away from the window with mild sensor noise in the far corner. "
   "Ambient palette cool neutral, the lightbox the brightest thing in the room.",
   S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
   "AVOID: " + NEGS("NEG-SCENE", "NEG-M1", "NEG-FILE") + ", no people, no product, no readable text on any screen, label or X-ray, no staged objects"])

# P3 — warehouse aisle (PLATED: HK2-T, BR-17, BR-19)
PLATES["P3-WAREHOUSE"] = dict(model="gpt_image_2_5 sunburst", attach="nothing",
  body=[S("CAM-LOCK"),
   "A single photograph down one aisle of a small distribution warehouse on a British industrial estate, taken at head height from the aisle end: "
   "tall orange-and-blue steel pallet racking on both sides loaded with brown cardboard boxes and shrink-wrapped pallets, a painted concrete floor with worn yellow walkway lines, "
   "and a roller shutter door open at the far end letting in daylight. "
   "Named anchors, all fixed: the orange-and-blue racking; the yellow walkway lines on the grey floor; the open roller shutter at the far end; a red pallet truck parked against the left-hand racking; "
   "a battered wooden workbench at the aisle end on the right with a tape gun and a roll of stretch film. Box labels are blank or unreadable.",
   "High-bay LED fittings overhead give a flat, slightly green-white light down the aisle; the open shutter at the far end blows to flat white and throws a band of cooler daylight across the floor near it. "
   "Shadows under the racking are deep but open, with sensor noise in the gaps between boxes. Ambient palette industrial: orange, blue, grey concrete, brown cardboard.",
   S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
   "AVOID: " + NEGS("NEG-SCENE", "NEG-M1", "NEG-FILE") + ", no people, no product, no readable text or logos, no staged objects"])

# P4 — loading yard, the van (PLATED: HK2-B, BR-16)
PLATES["P4-YARD"] = dict(model="gpt_image_2_5 sunburst", attach="nothing",
  body=[S("CAM-LOCK"),
   "A single photograph of the loading yard outside the same small warehouse, taken from about three metres behind a parked van: "
   "a white panel van, a few years old with a scuffed rear bumper and a grubby step, its rear doors both open, parked with its back to the camera on cracked tarmac. "
   "Named anchors, all fixed: the white van with open rear doors and a black rubber step under the bumper; the corrugated grey warehouse wall on the right with the roller shutter half open; "
   "a stack of wooden pallets against that wall; a yellow-painted steel bollard on the left. Inside the van, cardboard boxes strapped to the side. No lettering on the van, number plate blank.",
   S("LOC-EXT-OVERCAST"),
   S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
   "AVOID: " + NEGS("NEG-SCENE", "NEG-M1", "NEG-FILE") + ", no people, no product, no readable number plate, no lettering or logos, no staged objects"])

# P5 — gait lab (PLATED: BR-08, BR-09)
PLATES["P5-LAB"] = dict(model="gpt_image_2_5 sunburst", attach="nothing",
  body=[S("CAM-LOCK"),
   "A single photograph of a university sports-science gait lab, taken from one corner: a working room, not a showroom. "
   "A long grey treadmill in the middle of the room with its side rails, a pressure-sensor walkway strip laid on the floor beside it, and two small cameras on tripods at knee height aimed at the treadmill. "
   "Named anchors, all fixed: the grey treadmill with black side rails; the long black pressure walkway strip; the two knee-height tripod cameras; a whiteboard on the back wall wiped nearly clean with faint marker ghosts and no readable writing; "
   "a desk with a closed laptop against the right-hand wall. Any monitor is switched off. Blue-grey rubber sports flooring, white block walls.",
   "Cold fluorescent ceiling panels as the main light, even and slightly flat, with a high window on the left adding a patch of brighter daylight on the wall that clips to white. "
   "Shadows shallow and open under the treadmill, mild sensor noise in the far corner. Ambient palette cool white and grey, the black treadmill belt the darkest thing in frame.",
   S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
   "AVOID: " + NEGS("NEG-SCENE", "NEG-M1", "NEG-FILE") + ", no people, no product, no readable screen, numbers, graphs or writing, no staged objects"])

out = {}
for k, p in PLATES.items():
    txt = "\n\n".join(p["body"]); out[k] = dict(model=p["model"], attach=p["attach"], chars=len(txt), prompt=txt)
    pathlib.Path(f"{k}.prompt.txt").write_text(txt)
    print(f"{k:14s} {len(txt):5d}  attach: {p['attach']}")
json.dump(out, open("plates.json", "w"), indent=1)
