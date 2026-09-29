#!/usr/bin/env python3
"""Step-4 plates for stryde-failed-alternatives (§30C, §30G, §30K), 16:9 (V7.68.1), assembled from Appendix A by ID (never retyped)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
NEGS = lambda *ids: ", ".join(S(i) for i in ids)
WIDE = "A wide landscape photograph, the phone held sideways, so the whole space reads in one frame."
TAIL = lambda *extra: [S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
    "AVOID: " + NEGS(*extra, "NEG-M1", "NEG-LIGHT", "NEG-FILE") + ", no people, no product, no readable text, logos or labels, no staged objects"]
def fill(s, d):
    for k, v in d.items(): s = s.replace(k, v)
    assert "[" not in s, s[:200]; return s

# ---- Property Sheet: Bernadette's house (PROP-B), field 2 as fills ----
PROP_B = {
 "[TYPE AND ERA]": "1890s Victorian red-brick terraced",
 "[WALL FINISH AND COLOUR]": "papered walls in a faded cream embossed paper painted over many times",
 "[SKIRTING]": "tall moulded skirting painted gloss white and chipped at the corners",
 "[ARCHITRAVE]": "moulded white architraves",
 "[INTERNAL DOOR AND HANDLE]": "dark-stained four-panel internal doors with round wooden knobs",
 "[CEILING]": "a white ceiling with an ornate plaster ceiling rose and a fabric lampshade",
 "[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]": "red, cream and black Victorian encaustic floor tiles in the hall, a deep green patterned stair carpet held by brass stair rods, and a coir doormat at the front door",
 "[RADIATOR]": "a white column radiator under a shelf",
 "[SWITCHES AND SOCKETS]": "white plastic switches and sockets",
}
# ---- Property Sheet: Sian's house (PROP-S), field 2 as fills ----
PROP_S = {
 "[TYPE AND ERA]": "1900s Welsh valleys stone-built terraced miner's cottage",
 "[WALL FINISH AND COLOUR]": "uneven plastered walls painted a plain chalky white",
 "[SKIRTING]": "plain square skirting boards painted soft grey",
 "[ARCHITRAVE]": "plain square architraves painted soft grey",
 "[INTERNAL DOOR AND HANDLE]": "ledged-and-braced pine doors with black iron thumb latches",
 "[CEILING]": "a low white ceiling with a single plain pendant bulb in a paper shade",
 "[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]": "worn grey slate flagstones in the passage, bare varnished pine treads up a steep narrow staircase, and a rag rug at the front door",
 "[RADIATOR]": "a narrow white panel radiator",
 "[SWITCHES AND SOCKETS]": "white plastic switches and sockets",
}

PLATES = {}
PLATES["P0-PROP-B"] = dict(model="gpt_image_2_5 sunburst", attach="nothing", ar="16:9",
  beats="HK1-01, B1-02b, B1-05a, B1-11a, B1-12a, B1-12b, B2-03, B2-04, B3-06",
  body=[S("CAM-LOCK"), WIDE + " " + fill(S("PLATE-PROP"), PROP_B) +
   " The staircase is a single straight flight rising away from the camera along the right-hand wall, a dark-varnished handrail on turned white spindles, the green carpet running up every tread; "
   "the open doorway on the left of the hall shows the front room beyond. Named anchors, all fixed: a dark oak hall dresser with two wide drawers and a mirror above it against the left-hand wall, its top drawer closed; "
   "a small telephone table with a lace runner at the foot of the stairs; a row of coat hooks by the door with a camel coat; a framed print of a harbour by the stairs; the bottom stair, wide and carpeted.",
   "Daylight only: the house faces east at the front, so in the morning the stained-glass panel of the front door behind the camera throws a bright wash down the hall tiles and onto the bottom stairs, "
   "the landing window at the top of the stairs is a second, softer source, and the far end of the hall falls a stop darker with soft sensor noise on the back wall.",
   *TAIL("NEG-PROP")])
PLATES["P1-G-KITCHEN"] = dict(model="gpt_image_2_5 sunburst", attach="nothing", ar="16:9",
  beats="HK2-01, B2-06, B2-12a",
  body=[S("CAM-LOCK"), WIDE + " "
   "A single photograph of the kitchen of a 1960s ex-council semi-detached house in West Yorkshire, taken from the doorway from the hall: lived in, practical, a bit worn. "
   "The window over a stainless-steel sink on the far wall, a white uPVC back door beside it, pale wood-effect units with round chrome knobs along the far and right-hand walls under a speckled grey laminate worktop, "
   "and a small square table with two chairs on the left. "
   "Named anchors, all fixed: a tall floor-to-ceiling larder cabinet in the same pale wood effect beside the fridge on the right-hand wall, its door closed; "
   "a white kettle and a toaster on the worktop; a radio on the windowsill; a cork noticeboard by the back door with a few soft postcards, no readable writing; "
   "a green tea towel over the oven door. Brown-and-cream vinyl floor tiles, walls painted pale blue, a round flush ceiling light switched off.",
   "THE LIGHT: the window over the sink on the far wall is the only source, flat grey-white overcast morning daylight coming straight down the room towards the camera and falling across the table from the far end, "
   "the corners by the door a stop darker with soft sensor noise. " +
   S("VIEW-OUT").replace("[WHAT THE PROPERTY'S EXTERIOR SHOWS FROM THIS ROOM'S SIDE, NAMED]",
     "a small paved back yard, a rotary washing line and the pebble-dashed backs of the houses opposite"),
   *TAIL("NEG-SCENE")])
PLATES["P2-D-BOWLS"] = dict(model="gpt_image_2_5 sunburst", attach="nothing", ar="16:9",
  beats="B1-08",
  body=[S("CAM-LOCK"), WIDE + " "
   "A single photograph of the outdoor bowling green of a small community bowls club in south London, taken from one corner of the green at standing height: well kept, ordinary, a little old-fashioned. "
   "The flat, close-mown square green in the middle, divided into rinks by thin white string lines, a shallow gravel ditch and a low white-painted wooden bank all round it, "
   "and along the far side a single-storey clubhouse in cream-painted timber with a green roof and a veranda with a row of white plastic chairs. "
   "Named anchors, all fixed: the clubhouse veranda with its white chairs; a green wooden bench on the near bank; a black bowls bag on the bench; a few dark bowls and one small white jack resting at the far end of the nearest rink; "
   "a tall privet hedge behind the clubhouse and plane trees beyond it.",
   "THE LIGHT: bright midday sun high and to the left of the camera, short shadows falling right off the bowls and the bench, the clubhouse front lit, the sky pale blue with a few small clouds blown white near the sun.",
   *TAIL("NEG-SCENE")])
PLATES["P3-PROP-S"] = dict(model="gpt_image_2_5 sunburst", attach="nothing", ar="16:9",
  beats="B3-05, B3-07 (and the carried finishes of P4-S-KITCHEN)",
  body=[S("CAM-LOCK"), WIDE + " " + fill(S("PLATE-PROP"), PROP_S) +
   " The staircase is a steep straight flight rising away from the camera along the left-hand wall, a plain round pine handrail fixed to the wall and no spindles, the bare varnished treads worn pale in the middle; "
   "the open doorway on the right of the passage shows the kitchen beyond, a glimpse of a pine table. Named anchors, all fixed: a row of iron coat pegs by the door with a purple waterproof and a dog lead; "
   "a pair of muddy walking boots on the rag rug; a small framed photograph of hills on the wall halfway up the stairs; a narrow window at the top of the stairs.",
   "Daylight only: the house faces west at the front, so in the late morning the small window at the top of the stairs is the brighter source, spilling down the treads, the front door's small glass pane behind the camera a second, softer source, "
   "and the passage floor a stop darker with soft sensor noise on the far wall.",
   *TAIL("NEG-PROP")])
PLATES["P4-S-KITCHEN"] = dict(model="gpt_image_2_5 sunburst", attach="P3-PROP-S (landed; regenerated if P3 is sent to Fix)", ar="16:9",
  beats="HK3-01, B1-02a, B3-08",
  body=[S("CAM-LOCK"), WIDE + " " +
   S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", "chalky white uneven plaster, soft grey square skirting and architraves, ledged pine doors with black iron thumb latches and grey slate flagstones") + " "
   "A single photograph of the small kitchen at the back of that cottage, taken from the doorway from the passage: plain, warm, lived in. "
   "A deep white ceramic sink under a small window on the far wall, cream painted units with wooden knobs under a wooden worktop along the far and right-hand walls, a cream range cooker, "
   "and a scrubbed pine table with two mismatched wooden chairs in the middle of the room. "
   "Named anchors, all fixed: the pine table with a blue-and-white striped jug and a fruit bowl; a wall calendar with a landscape photograph hanging by the back door, its grid of days too small to read; "
   "a dog bed with a tartan blanket under the window; a row of hooks with mugs under a shelf of jars.",
   "THE LIGHT: the small window over the sink on the far wall is the only source, soft overcast morning daylight falling across the table from the far end, "
   "the corners by the door a stop darker with soft sensor noise. " +
   S("VIEW-OUT").replace("[WHAT THE PROPERTY'S EXTERIOR SHOWS FROM THIS ROOM'S SIDE, NAMED]",
     "a small back yard with a stone wall and, above the roofs, a green hillside with sheep fields"),
   *TAIL("NEG-PROP")])
PLATES["P5-CLINIC"] = dict(model="gpt_image_2_5 sunburst", attach="nothing", ar="16:9",
  beats="HK-BR, B1-01a, B1-10",
  body=[S("CAM-LOCK"), WIDE + " "
   "A single photograph of an orthopaedic consulting room in a small private clinic in an English market town, taken from just inside the door: calm, modern, plain. "
   "A tall window on the left-hand wall with white venetian blinds half open, a light oak desk under it facing into the room with a desk chair and a visitor's chair, "
   "a padded navy examination couch against the right-hand wall with a paper roll and a low step in front of it, and a wall-mounted X-ray light box on the far wall, switched off. "
   "Named anchors, all fixed: a life-size plastic anatomical knee model on a stand on the desk, the bones cream, the tendons red; the navy couch with its step; "
   "the X-ray light box; a large leafy monstera in a white pot in the far corner; a hand-gel dispenser by the door. Soft white walls with one sage-green feature wall behind the couch, light grey vinyl floor.",
   "THE LIGHT: bright overcast daylight through the window on the left-hand wall as the key, falling across the desk and fading towards the couch; the ceiling panel light on and flat. "
   "The couch end of the room sits slightly dim with mild sensor noise.",
   *TAIL("NEG-SCENE")])

out = {}
for k, p in PLATES.items():
    txt = "\n\n".join(p["body"]); out[k] = dict(model=p["model"], attach=p["attach"], ar=p["ar"], beats=p["beats"], chars=len(txt), prompt=txt)
    pathlib.Path(f"{k}.prompt.txt").write_text(txt)
    print(f"{k:14s} {len(txt):5d}  attach: {p['attach']}")
json.dump(out, open("plates.json", "w"), indent=1)
