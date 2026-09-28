#!/usr/bin/env python3
"""Step-4 plates for stryde-three-regrets (§30C, §30G, §30K), assembled from Appendix A by ID (never retyped)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
NEGS = lambda *ids: ", ".join(S(i) for i in ids)

# ---- Property Sheet: Gail's house (PROP-G), field 2 as fills --------------------------------
SHELL = {
 "WALL": "woodchip wallpaper painted a pale duck-egg blue, scuffed at shoulder height along the stairs",
 "SKIRT": "plain bullnose pine skirting about twelve centimetres high, varnished a honey orange",
 "ARCH": "plain varnished pine architraves to match",
 "DOOR": "flush sapele-veneer internal doors with brushed aluminium lever handles",
 "CEIL": "a plain white ceiling with a round white paper lantern shade",
 "FLOOR": "a moss-green twist carpet through the hall, up the stairs, along the landing and into the bedrooms, meeting beige vinyl at the kitchen under an aluminium threshold strip",
 "RAD": "white double-panel convector radiators",
 "SW": "square white plastic switches and sockets, a little scuffed",
}
PROP = {
 "[TYPE AND ERA]": "1960s pebble-dashed semi-detached",
 "[WALL FINISH AND COLOUR]": SHELL["WALL"], "[SKIRTING]": SHELL["SKIRT"], "[SKIRTING — profile, height, colour]": SHELL["SKIRT"],
 "[ARCHITRAVE]": SHELL["ARCH"], "[INTERNAL DOOR AND HANDLE]": SHELL["DOOR"], "[INTERNAL DOOR — style, colour, handle]": SHELL["DOOR"],
 "[CEILING]": SHELL["CEIL"], "[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]": SHELL["FLOOR"],
 "[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]": SHELL["FLOOR"], "[RADIATOR]": "a white double-panel convector radiator",
 "[RADIATOR TYPE]": SHELL["RAD"], "[SWITCHES AND SOCKETS]": SHELL["SW"],
}
CARRIED = ("pale duck-egg blue woodchip walls, honey-varnished pine skirting and architraves, flush sapele doors with aluminium lever handles, "
           "moss-green twist carpet")
def fillp(s):
    for k, v in PROP.items(): s = s.replace(k, v)
    assert "[" not in s, s[:200]; return s

TAIL = lambda *extra: [S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
    "AVOID: " + NEGS(*extra, "NEG-M1", "NEG-LIGHT", "NEG-FILE") + ", no people, no product, no readable text, logos or labels, no staged objects"]

PLATES = {}

# P0 — property plate: Gail's hall and stairs (TRAVERSED stairs: P-032–P-034, P-050–P-053)
PLATES["P0-PROP-G"] = dict(model="gpt_image_2_5 sunburst", attach="nothing",
  body=[S("CAM-LOCK"), fillp(S("PLATE-PROP")) +
   " The staircase is a single straight flight rising away from the camera along the right-hand wall, with a varnished pine handrail on white square spindles and the moss-green carpet running up every tread; "
   "the open doorway on the left of the hall shows the front room beyond. A barometer in a wooden case on the left-hand wall, a wooden umbrella stand by the door holding a walking stick and a folded umbrella, "
   "a small telephone table with a spider plant at the foot of the stairs, a coir doormat inside the door.",
   "Daylight only: the house faces south at the front, so late in the morning the front door glass behind the camera throws a bright pale wash down the carpet and up the first few stairs, "
   "the landing window at the top of the stairs is a second, softer source, and the far end of the hall falls a stop darker with soft sensor noise on the back wall.",
   *TAIL("NEG-PROP")])

# P1 — Gail's bedroom (PLATED: HK1, P-005–P-008, P-012, P-016, P-037–P-042, P-047)
PLATES["P1-G-BEDROOM"] = dict(model="gpt_image_2_5 sunburst", attach="P0-PROP-G (approved)",
  body=[S("CAM-LOCK"),
   S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", CARRIED) + " " + fillp(S("PROP-SHELL")),
   "The front bedroom upstairs, seen from the corner just inside the door: the window on the right-hand wall, a double bed with its headboard against the far wall and a faded patchwork quilt, "
   "and against the left-hand wall a tall five-drawer pine chest of drawers with round wooden knobs, its top drawer pulled half open and overfilled with knee supports — a black stretchy sleeve, a grey hinged brace with metal side bars, a beige wrap with hook-and-loop tails, a blue gel pad, "
   "all blank, no brand, no writing — one strap hanging over the drawer edge. "
   "Named anchors, all fixed: the pine chest of drawers with the open top drawer; the patchwork quilt; a bedside table on the near side of the bed with a lamp, a glass of water and a paperback; "
   "a white wicker chair under the window with a folded cardigan on it; a framed wedding photograph on the chest of drawers, faces too small to read.",
   "THE LIGHT: the bedroom window on the right-hand (south) wall is the only source, late-morning daylight coming in at an angle across the quilt and onto the front of the chest of drawers, "
   "the far corner behind the door a stop darker, the pale blue walls bouncing a soft fill into the shadows. " +
   S("VIEW-OUT").replace("[WHAT THE PROPERTY'S EXTERIOR SHOWS FROM THIS ROOM'S SIDE, NAMED]",
     "the front of the house opposite: a pebble-dashed semi, a privet hedge and a parked silver hatchback"),
   *TAIL("NEG-SCENE", "NEG-PROP")])

# P2 — the narrator's workroom (PLATED: N TH, HK2, P-002, P-023, P-057–P-058)
PLATES["P2-N-WORKROOM"] = dict(model="gpt_image_2_5 sunburst", attach="nothing",
  body=[S("CAM-LOCK"),
   "A single photograph of a small first-floor workroom above a shop in a West Yorkshire mill town, where a small company answers its customers' messages, taken from just inside the door: lived in, not designed. "
   "A tall Victorian sash window on the left-hand wall, a bare red-brick back wall, and a long worktop desk along the right-hand wall. "
   "Named anchors, all fixed: a large cork pinboard on the brick wall covered edge to edge with printed messages and handwritten cards pinned in overlapping rows, the writing too small and soft to read; "
   "three grey plastic post trays on the desk stacked with printed letters and opened envelopes; a closed laptop; a green anglepoise lamp, switched off; "
   "a steel shelving unit in the far corner holding plain brown cardboard shipping cartons with blank white labels; a kettle and two mugs on a small tray on the windowsill. "
   "Worn floorboards with a faded red runner, a wooden office chair pushed back from the desk.",
   "THE LIGHT: the sash window on the left-hand (east) wall is the key, soft morning daylight falling across the desk and the pinboard from the left, the brick wall warm where it catches it; "
   "the far corner by the shelving falls a stop darker with soft sensor noise; no lamp is on.",
   *TAIL("NEG-SCENE")])

# P3 — Ken's high-street bus stop (PLATED: P-018, P-020, P-022, P-061)
PLATES["P3-K-BUSSTOP"] = dict(model="gpt_image_2_5 sunburst", attach="nothing",
  body=[S("CAM-LOCK"),
   "A single photograph of a bus stop on an ordinary British market-town high street, taken from the pavement about four metres from the shelter at head height: "
   "a glass-and-steel bus shelter with a narrow red perch bench, a high granite kerb dropping to the road, a zebra crossing a few metres beyond with its black-and-white poles and orange globes, "
   "and a row of two-storey brick shops on the far side with plain painted fascias. "
   "Named anchors, all fixed: the bus shelter with the red perch bench; the high granite kerb; the zebra crossing and its orange globes; a green litter bin on a post; "
   "a hanging basket of red geraniums on a lamp post. Shop fascias carry no readable names; there is no bus and no timetable text.",
   S("LOC-EXT-OVERCAST"),
   *TAIL("NEG-SCENE")])

# P4 — Joan's lounge in a ground-floor retirement flat (PLATED: P-025–P-027, P-029)
PLATES["P4-J-LOUNGE"] = dict(model="gpt_image_2_5 sunburst", attach="nothing",
  body=[S("CAM-LOCK"),
   "A single photograph of the lounge of a small ground-floor retirement flat in a 1970s brick block, taken from the corner by the door: tidy, warm, a little crowded. "
   "A wide window on the left-hand wall with net curtains and floral draw curtains tied back, a high-backed wing armchair in rose-pink velour beside the window angled into the room, "
   "and a teak side table beside it with a cream landline telephone, a cup and saucer and a pair of reading glasses. "
   "Named anchors, all fixed: the rose-pink wing armchair; the cream landline telephone on the teak side table; a glass-fronted display cabinet of china against the far wall; "
   "a gas fire with a tiled surround and a mantel of framed family photographs, faces too small to read; a crocheted blanket over the arm of the chair. "
   "Swirl-patterned brown-and-gold carpet, magnolia walls, a ceiling light with three glass shades, switched off.",
   "THE LIGHT: the lounge window on the left-hand (west) wall is the only source, flat grey daylight through the net curtains filling the room evenly and softly from the left, "
   "the far corner by the cabinet a little darker with soft sensor noise. " +
   S("VIEW-OUT").replace("[WHAT THE PROPERTY'S EXTERIOR SHOWS FROM THIS ROOM'S SIDE, NAMED]",
     "the communal lawn of the block, a wooden bench and a row of parked cars"),
   *TAIL("NEG-SCENE")])

# P5 — her daughter's front steps (PLATED: P-028, P-030, P-065)
PLATES["P5-J-STEPS"] = dict(model="gpt_image_2_5 sunburst", attach="nothing",
  body=[S("CAM-LOCK"),
   "A single photograph of the front of a Victorian stone terraced house on a steep northern street, taken from the pavement at the foot of its steps, looking up: "
   "a flight of seven worn sandstone steps rising from the pavement to a glossy dark-red front door with a brass knocker and a fanlight, black iron railings on the left side of the steps only, "
   "a bay window to the right of the door with a white-painted sill. "
   "Named anchors, all fixed: the seven sandstone steps, each dipped in the middle from wear; the black iron railing on the left; the dark-red front door; a terracotta pot of lavender on the top step. "
   "The neighbouring houses step down the hill to the left. The house number is not readable.",
   S("LOC-EXT-OVERCAST"),
   *TAIL("NEG-SCENE")])

# P6 — consulting room (PLATED: HK3, P-009, P-015, P-045)
PLATES["P6-CONSULT"] = dict(model="gpt_image_2_5 sunburst", attach="nothing",
  body=[S("CAM-LOCK"),
   "A single photograph of an orthopaedic consulting room in a British NHS hospital outpatients department, taken from just inside the door: modest and well used. "
   "The window on the right-hand wall with vertical blinds half open, a desk under it facing into the room, the examination couch against the left-hand wall under a paper roll, "
   "and a wall-mounted X-ray viewing screen on the back wall showing one knee X-ray, side view, glowing white. "
   "Named anchors, all fixed: the X-ray viewing screen with the single knee X-ray; a grey hinged knee brace with metal side bars lying on the desk, blank, no brand; "
   "a plastic anatomical knee model on the desk; the green vinyl examination couch with its paper roll; a sharps bin and a hand gel dispenser by the door. "
   "Grey speckled vinyl floor, pale green walls scuffed at chair height.",
   "THE LIGHT: overcast daylight through the right-hand window as the key, falling across the desk and fading towards the couch; the X-ray screen adds its own cold glow on the back wall; "
   "the ceiling panel light is on and flat. The room sits slightly dim away from the window with mild sensor noise in the far corner.",
   *TAIL("NEG-SCENE")])

out = {}
for k, p in PLATES.items():
    txt = "\n\n".join(p["body"]); out[k] = dict(model=p["model"], attach=p["attach"], chars=len(txt), prompt=txt)
    pathlib.Path(f"{k}.prompt.txt").write_text(txt)
    print(f"{k:14s} {len(txt):5d}  attach: {p['attach']}")
json.dump(out, open("plates.json", "w"), indent=1)
