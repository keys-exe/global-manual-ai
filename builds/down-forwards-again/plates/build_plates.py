#!/usr/bin/env python3
"""Step-4 plates for down-forwards-again (§30C, §30G, §30K), assembled from Appendix A by ID (never retyped),
plus the three LEFT-knee worn references (Product Sheet worn_ref_prompts('left'), SIDE_RULE clause 4)."""
import re, json, pathlib, importlib.util
ROOT = pathlib.Path(__file__).resolve().parents[3]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
NEGS = lambda *ids: ", ".join(S(i) for i in ids)

# ---- Property Sheet: the patient's house (PROP-P), field 2 as fills ------------------------------
SHELL = {
 "WALL": "magnolia emulsion above a dark-stained wooden dado rail, cream-painted embossed anaglypta paper below it, scuffed along the stairs",
 "SKIRT": "tall moulded Victorian skirting about twenty-two centimetres high, painted white gloss gone slightly yellow",
 "ARCH": "moulded white-gloss architraves to match",
 "DOOR": "four-panel pine doors stripped and waxed a warm orange, with round brass knobs",
 "CEIL": "a high white ceiling with a plain plaster cornice and a frosted glass pendant shade",
 "FLOOR": "a burgundy-and-cream patterned carpet runner held by brass stair rods up the stairs and along the hall over dark-stained floorboards, meeting red-and-black quarry tiles at the kitchen under a brass threshold strip",
 "RAD": "white cast-iron column radiators",
 "SW": "white plastic switches and sockets on older wiring, one brass dimmer in the front room",
}
PROP = {
 "[TYPE AND ERA]": "Victorian red-brick mid-terraced", "[WALL FINISH AND COLOUR]": SHELL["WALL"], "[SKIRTING]": SHELL["SKIRT"],
 "[SKIRTING — profile, height, colour]": SHELL["SKIRT"], "[ARCHITRAVE]": SHELL["ARCH"], "[INTERNAL DOOR AND HANDLE]": SHELL["DOOR"],
 "[INTERNAL DOOR — style, colour, handle]": SHELL["DOOR"], "[CEILING]": SHELL["CEIL"],
 "[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]": SHELL["FLOOR"], "[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]": SHELL["FLOOR"],
 "[RADIATOR]": "a white cast-iron column radiator", "[RADIATOR TYPE]": SHELL["RAD"], "[SWITCHES AND SOCKETS]": SHELL["SW"],
}
CARRIED = ("magnolia walls over a dark-stained dado rail with cream anaglypta below, tall white-gloss Victorian skirting, "
           "stripped pine four-panel doors with brass knobs, the burgundy-and-cream patterned runner")
def fillp(s):
    for k, v in PROP.items(): s = s.replace(k, v)
    assert "[" not in s, s[:200]; return s
TAIL = lambda *extra: [S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
    "AVOID: " + NEGS(*extra, "NEG-M1", "NEG-LIGHT", "NEG-FILE") + ", no people, no product, no readable text, logos or labels, no staged objects"]

PLATES = {}
# P0 — property plate: hall and stairs (TRAVERSED: HK1, B-05, B-06, B-08, B-19, B-23)
PLATES["P0-PROP-P"] = dict(model="gpt_image_2_5 sunburst", attach="nothing", body=[S("CAM-LOCK"), fillp(S("PLATE-PROP")) +
  " The staircase is a single steep straight flight rising away from the camera along the LEFT-hand wall, a dark-stained turned-wood banister and handrail on the open right side,"
  " the patterned runner and its brass rods on every tread; at the top a small landing with a closed door. The open doorway on the right of the hall shows the front room beyond."
  " Named anchors, all fixed: a coat hooks rail on the right-hand wall with a navy raincoat and a tartan shopping trolley bag beneath it; an old-fashioned telephone table with a cream telephone and a pad at the foot of the stairs;"
  " a small framed watercolour of a harbour halfway up the stair wall; a pair of brown walking boots on a newspaper by the door.",
  "Daylight only: the front of the house faces east, so on a grey morning the stained-glass panel in the front door behind the camera throws a soft pale wash down the runner and onto the first stairs,"
  " a small skylight over the landing is a second, weaker source from above, and the back of the hall towards the kitchen falls a stop darker with soft sensor noise.",
  *TAIL("NEG-PROP")])
# P1 — front room (PLATED: B-07 the armchair, B-09 the long walk / family at the door seen through the bay)
PLATES["P1-P-FRONTROOM"] = dict(model="gpt_image_2_5 sunburst", attach="P0-PROP-P (approved)", body=[S("CAM-LOCK"),
  S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", CARRIED) + " " + fillp(S("PROP-SHELL")),
  "The front room, seen from the doorway from the hall: a wide square bay window on the far wall with net curtains and heavy olive-green curtains tied back, "
  "and angled into the room beside the bay a high-backed fireside armchair with wooden arms and a faded mustard seat cushion, low and a little sagging, a small footstool in front of it. "
  "Named anchors, all fixed: the mustard fireside armchair; a Victorian cast-iron fireplace with a tiled surround and a mantel of framed family photographs, faces too small to read; "
  "a nest of three dark-wood side tables beside the chair holding a mug, a TV remote and a folded newspaper; a glass-fronted bookcase; a patterned rug over the runner-matching floorboards.",
  "THE LIGHT: the bay window on the far (east) wall is the only source, grey late-morning daylight through the net curtains, soft and even across the armchair from the window side, "
  "the corner behind the door a stop darker, the magnolia walls bouncing a gentle fill. " +
  S("VIEW-OUT").replace("[WHAT THE PROPERTY'S EXTERIOR SHOWS FROM THIS ROOM'S SIDE, NAMED]",
    "a small front garden with a low brick wall, a privet hedge, and the red-brick terrace opposite across a narrow street with parked cars"),
  *TAIL("NEG-SCENE", "NEG-PROP")])
# P2 — kitchen (PLATED: HK1-02 the drawer, B-10 physio band, B-09 garden, B-22 the box, the copy)
PLATES["P2-P-KITCHEN"] = dict(model="gpt_image_2_5 sunburst", attach="P0-PROP-P (approved)", body=[S("CAM-LOCK"),
  S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", CARRIED) + " " + fillp(S("PROP-SHELL")),
  "The narrow galley kitchen at the back of the house, seen from the doorway from the hall: cream shaker cupboards along the left, a white ceramic sink under the window at the far end, "
  "a small drop-leaf table with two spindle-back chairs against the right-hand wall, red-and-black quarry tiles underfoot. "
  "Named anchors, all fixed: an old pine Welsh dresser on the right beside the table, its top drawer pulled half open and overfilled with knee supports — a black stretchy sleeve, a grey hinged brace with metal side bars, a beige wrap, all blank, no brand, no writing; "
  "a tube of plain white gel with no label and a wall calendar with no readable dates on the dresser; a spider plant on the windowsill; a tea towel on the oven door.",
  "THE LIGHT: the window over the sink on the far (west) wall is the key, flat overcast daylight coming straight down the galley towards the camera and across the table from the right, "
  "the near end by the door a stop darker with soft sensor noise. " +
  S("VIEW-OUT").replace("[WHAT THE PROPERTY'S EXTERIOR SHOWS FROM THIS ROOM'S SIDE, NAMED]",
    "a long narrow back garden gone overgrown, the lawn uncut, a raised vegetable bed full of weeds and a wooden bench with peeling green paint by the fence"),
  *TAIL("NEG-SCENE", "NEG-PROP")])
# P3 — the doctor's consulting room (PLATED: every TH; HK3-01, B-15, B-20)
PLATES["P3-D-CONSULT"] = dict(model="gpt_image_2_5 sunburst", attach="nothing", body=[S("CAM-LOCK"),
  "A single photograph of a GP's consulting room in a surgery in a Yorkshire market town, taken from the patient's chair across the desk at seated eye height, looking at the doctor's empty chair: modest, bright and well used. "
  "A light-wood desk across the foreground with a closed laptop to one side, and behind it the doctor's black swivel chair pushed in slightly, its back to a pale grey wall. "
  "A tall window on the left of the frame with white vertical blinds open, an examination couch in dark blue vinyl with a white paper roll along the right-hand wall behind the chair, partly in frame. "
  "Named anchors, all fixed: a white plastic anatomical knee model on the desk; a wall-mounted blood-pressure unit on its coiled grey tube behind the chair on the right; "
  "a small cork noticeboard on the back wall with leaflets pinned to it, the writing too small and soft to read; a hand-gel dispenser and a paper-towel holder by a small sink in the far right corner; a potted peace lily on the windowsill.",
  "THE LIGHT: the window on the left is the key, steady overcast north daylight falling across the desk and onto the chair from camera-left at about forty-five degrees, "
  "the right-hand side of the room by the couch a stop darker, the ceiling panel light off; the grey wall behind the chair reads soft, a little out of focus.",
  *TAIL("NEG-SCENE")])

# ---- LEFT-knee worn references (Product Sheet SIDE_RULE 4): the scenes name the right leg, re-sided here ----
spec = importlib.util.spec_from_file_location("ps", ROOT / "products/stryde/stryde_product_sheet.py"); ps = importlib.util.module_from_spec(spec)
try: spec.loader.exec_module(ps)
except AssertionError: pass
WR = ps.worn_ref_prompts("left")
for k in WR:
    sc = ps.WORN_REF_SCENES[k]
    new = sc.replace("the right leg", "the left leg").replace("the right knee", "the left knee").replace("degrees to the right of", "degrees to the left of")
    WR[k] = WR[k].replace(sc, new)
    assert "right leg" not in WR[k] and "right knee" not in WR[k], k
ATT = {"front": "front.webp, product_tq_left.jpg", "rear": "back.webp, front.webp", "bent": "product_tq_left.jpg, front.webp"}

out = {}
for k, p in PLATES.items():
    txt = "\n\n".join(p["body"]); out[k] = dict(model=p["model"], attach=p["attach"], chars=len(txt), prompt=txt)
    pathlib.Path(f"{k}.prompt.txt").write_text(txt); print(f"{k:16s} {len(txt):5d}  attach: {p['attach']}")
for k, txt in WR.items():
    kid = f"W-L-{k.upper()}"; out[kid] = dict(model="nano_banana_pro 2k", attach=ATT[k], chars=len(txt), prompt=txt)
    pathlib.Path(f"{kid}.prompt.txt").write_text(txt); print(f"{kid:16s} {len(txt):5d}  attach: {ATT[k]}")
json.dump(out, open("plates.json", "w"), indent=1)
