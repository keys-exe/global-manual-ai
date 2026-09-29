#!/usr/bin/env python3
"""Step-4 plates for stryde-not-your-cartilage (§30C, §30G, §30K), 16:9 (V7.68.1), assembled from Appendix A by ID (never retyped)."""
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
    assert "[" not in s, s[:300]; return s
def shell(d):
    m = {"[SKIRTING — profile, height, colour]": d["[SKIRTING]"], "[INTERNAL DOOR — style, colour, handle]": d["[INTERNAL DOOR AND HANDLE]"],
         "[RADIATOR TYPE]": d["[RADIATOR]"], "[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]": d["[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]"]}
    return fill(S("PROP-SHELL"), dict(d, **m))
def pref(clause): return fill(S("PROP-REF"), {"[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]": clause})
VIEW = lambda what: S("VIEW-OUT").replace("[WHAT THE PROPERTY'S EXTERIOR SHOWS FROM THIS ROOM'S SIDE, NAMED]", what)

# ---- Property Sheets, field 2 as fills ----
PROP_FO = {  # Folake's house
 "[TYPE AND ERA]": "1960s brick terraced",
 "[WALL FINISH AND COLOUR]": "woodchip wallpaper painted warm magnolia",
 "[SKIRTING]": "plain white skirting about twelve centimetres high",
 "[ARCHITRAVE]": "plain flat white architraves",
 "[INTERNAL DOOR AND HANDLE]": "white flush internal doors with chrome lever handles",
 "[CEILING]": "a white textured ceiling with a flush frosted dome light",
 "[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]": "mid-oak wood-effect laminate in the hall, a deep red carpet up the stairs, meeting a coir doormat inside the front door",
 "[RADIATOR]": "a white steel panel radiator",
 "[SWITCHES AND SOCKETS]": "white plastic switches and sockets",
}
PROP_H = {  # Hassan's house
 "[TYPE AND ERA]": "1930s pebble-dashed semi-detached",
 "[WALL FINISH AND COLOUR]": "smooth plaster painted a pale sage green",
 "[SKIRTING]": "tall moulded skirting about eighteen centimetres high painted white",
 "[ARCHITRAVE]": "moulded white architraves",
 "[INTERNAL DOOR AND HANDLE]": "dark-stained wooden panel doors with brass lever handles",
 "[CEILING]": "a white ceiling with a simple cornice and a fabric drum lampshade",
 "[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]": "a busy brown-and-gold patterned carpet running through the hall and straight up every stair, meeting red quarry tiles in the porch",
 "[RADIATOR]": "a white steel panel radiator",
 "[SWITCHES AND SOCKETS]": "white plastic switches and sockets",
}

PLATES = {}
PLATES["P0-PROP-FO"] = dict(attach="nothing", beats="B-07 (and the house of P1)", neg="NEG-PROP",
  body=[S("CAM-LOCK"), WIDE + " " + fill(S("PLATE-PROP"), PROP_FO) +
   " The staircase is a single straight flight rising away from the camera along the right-hand wall, with a plain white-painted handrail on the open side and white square spindles, the red carpet running up every tread to a small landing; "
   "the open doorway on the left of the hall shows the front lounge beyond, a corner of a burgundy armchair just visible. A wall-mounted coat rack by the door with a navy raincoat and a patterned headscarf, "
   "a small telephone table with a cream corded telephone and a glass bowl of keys at the foot of the stairs, a framed print of a harbour on the wall.",
   "Daylight only: the frosted glass panel in the front door behind the camera throws a soft bright wash down the hall and onto the first stairs; the landing at the top of the stairs gets light from a small window out of sight, "
   "and the far end of the hall falls a stop darker with soft sensor noise.",
   *TAIL("NEG-PROP", "NEG-SCENE")])
PLATES["P1-F-LOUNGE"] = dict(attach="P0-PROP-FO", beats="HK2-01, B-01a, B-03c, B-13a", neg="NEG-SCENE",
  body=[S("CAM-LOCK"), WIDE + " " + pref("the magnolia woodchip walls, plain white woodwork, white flush doors with chrome levers and the mid-oak laminate floor") + " " + shell(PROP_FO) + " "
   "A single photograph of the front lounge of this same 1960s brick terraced house in south London, taken from the doorway from the hall: warm, full of colour and family, very tidy. "
   "A wide window on the left-hand (east) wall with net curtains and heavy gold curtains tied back, a high-backed burgundy armchair with wooden arms side-on to the window, "
   "a low glass-topped coffee table in front of it on a cream rug, and a cream three-seater sofa along the right-hand wall under a long row of framed family photographs, faces too small to read. "
   "Named anchors, all fixed: the burgundy armchair with a crocheted cream cushion; the glass-topped coffee table with a coaster and a folded newspaper; a tall glass-fronted display cabinet of patterned china on the far wall; "
   "a brass standard lamp with a pleated shade beside the armchair, switched off; a large rubber plant in a glazed pot by the window.",
   "THE LIGHT: the window on the left-hand (east) wall is the only source, bright morning daylight through the nets falling across the armchair and the coffee table from the left, "
   "the sofa wall a stop darker with soft sensor noise. " + VIEW("a row of brick terraced houses across the street and a parked blue hatchback"),
   *TAIL("NEG-SCENE", "NEG-PROP")])
PLATES["P2-D-TOWPATH"] = dict(attach="nothing", beats="B-03a, B-14", neg="NEG-SCENE",
  body=[S("CAM-LOCK"), WIDE + " "
   "A single photograph of a canal towpath on the edge of a northern English town, taken standing on the path looking along it: ordinary, a bit muddy, well used. "
   "A straight gravel-and-earth towpath running away from the camera, the still brown-green canal on the left edged with worn stone coping, a thick hawthorn hedgerow and a field gate on the right. "
   "Named anchors, all fixed: an old humped stone bridge crossing the canal in the middle distance, the path passing under its arch; two narrowboats moored along the far bank, one dark green, one maroon, their names too small to read; "
   "a wooden bench set back into the hedgerow on the right; a black-and-white painted mooring bollard on the canal edge near the camera; a row of stone mill cottages beyond the far bank.",
   "THE LIGHT: bright soft daylight under a high thin layer of cloud, the sun a pale disc high on the left, gentle shadows falling to the right, the sky a flat pale grey-white where it enters frame at the top.",
   *TAIL("NEG-SCENE")])
PLATES["P3-PROP-H"] = dict(attach="nothing", beats="B-03b, B-06 (and the house of P4)", neg="NEG-PROP",
  body=[S("CAM-LOCK"), WIDE + " " + fill(S("PLATE-PROP"), PROP_H) +
   " The staircase is a single steep straight flight rising away from the camera along the left-hand wall, with a dark-stained wooden handrail on turned white spindles, the patterned carpet running up every tread to a half-landing with a window; "
   "the open doorway at the far end of the hall on the right shows the kitchen beyond, a white cupboard door just visible. A wooden shoe rack with three pairs of men's shoes by the door, "
   "a narrow hall table with a pile of post and a small brass bowl, a framed woven wall hanging in sand and indigo on the right-hand wall.",
   "Daylight only: the front door's coloured-glass panel behind the camera throws a warm wash down the hall and up the first stairs; the half-landing window at the top of the flight is a second, cooler source, "
   "and the middle of the hall falls a stop darker with soft sensor noise.",
   *TAIL("NEG-PROP", "NEG-SCENE")])
PLATES["P4-H-KITCHEN"] = dict(attach="P3-PROP-H", beats="B-08", neg="NEG-SCENE",
  body=[S("CAM-LOCK"), WIDE + " " + pref("the pale sage walls, tall white moulded skirting, dark-stained panel doors with brass levers and the brown-and-gold patterned carpet") + " " + shell(PROP_H) + " "
   "A single photograph of the kitchen at the back of this same 1930s semi-detached house, taken from the doorway from the hall: a narrow galley kitchen, older units, very clean. "
   "Cream units with wooden trim along both sides under a dark speckled laminate worktop, a window over a stainless-steel sink on the far (east) wall looking onto the back garden, and a white back door with a glass panel on the right beside it. "
   "Named anchors, all fixed: a white electric kettle on the worktop by the sink; a round tin tea caddy and a row of glass spice jars; a wall clock above the door; "
   "a small folding table against the left-hand wall with one chair; a potted mint plant on the windowsill. Beige-and-brown chequered vinyl floor, white wall tiles above the worktop.",
   "THE LIGHT: the window over the sink on the far (east) wall is the key, bright morning sun falling along the worktop towards the camera, the near end of the kitchen a stop darker with mild sensor noise. " +
   VIEW("a narrow back garden with a washing line and a wooden fence, a neighbour's apple tree over it"),
   *TAIL("NEG-SCENE", "NEG-PROP")])
PLATES["P5-E-BEDROOM"] = dict(attach="nothing", beats="B-09a, B-09b, B-11a", neg="NEG-SCENE",
  body=[S("CAM-LOCK"), WIDE + " "
   "A single photograph of the main bedroom of a small Victorian stone terraced house in Cardiff, taken from the doorway: calm, pale, lived in. "
   "A double bed with its headboard against the far wall, a sash window on the right-hand (south) wall with a white roller blind pulled up, a white wooden wardrobe on the left-hand wall and a chest of drawers with a round mirror beside it. "
   "Named anchors, all fixed: the bed with a white-and-grey striped duvet cover pulled straight and two grey pillows; a pale wooden bedside table with a brass reading lamp, switched off, and a paperback; "
   "a cane-seated wooden chair by the window with a folded cardigan on it; a woven runner rug beside the bed; a small framed seaside watercolour over the bed. Painted pale dove-grey walls, stripped pine floorboards.",
   "THE LIGHT: the sash window on the right-hand (south) wall is the only source, bright morning daylight falling across the bed and the rug from the right, the wardrobe side of the room a stop darker with soft sensor noise. " +
   VIEW("the backs of the terraced houses opposite and a strip of sky"),
   *TAIL("NEG-SCENE")])
PLATES["P6-CONSULT"] = dict(attach="nothing", beats="HK3-01, B-02b, B-12", neg="NEG-SCENE",
  body=[S("CAM-LOCK"), WIDE + " "
   "A single photograph of a consultant's room in a hospital outpatients clinic in an English city, taken from just inside the door: plain, clean, a little worn. "
   "A window on the left-hand wall with a vertical blind half open, a light wood-effect desk against it with a computer monitor, the consultant's chair and two visitor's chairs, "
   "a padded blue examination couch against the right-hand wall under a paper roll, and a wall-mounted X-ray light box on the far wall, switched off, its white panel empty. "
   "Named anchors, all fixed: the X-ray light box; the blue couch with its paper roll and a two-step footstool; a plastic anatomical knee model on the desk, the bones cream and the ligaments red; "
   "a hand-gel dispenser by the door; a grey filing cabinet in the far corner. Pale grey-blue walls, speckled grey vinyl floor.",
   "THE LIGHT: bright overcast daylight through the window on the left-hand wall as the key, falling across the desk and fading towards the couch; the ceiling panel light on and flat. "
   "The couch end of the room sits slightly dim with mild sensor noise.",
   *TAIL("NEG-SCENE")])

out = {}
for k, p in PLATES.items():
    txt = "\n\n".join(p["body"]); out[k] = dict(model="gpt_image_2_5 sunburst", attach=p["attach"], beats=p["beats"], chars=len(txt), prompt=txt)
    pathlib.Path(f"{k}.prompt.txt").write_text(txt)
    print(f"{k:14s} {len(txt):5d}  attach: {p['attach']}")
json.dump(out, open("plates.json", "w"), indent=1)
