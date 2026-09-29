#!/usr/bin/env python3
"""Step-4 plates for stryde-too-bad (§30C, §30G, §30K), 16:9 (V7.68.1), assembled from Appendix A by ID (never retyped)."""
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

# ---- Property Sheet: Fiona's house (PROP-F), field 2 as fills ----
PROP_F = {
 "[TYPE AND ERA]": "1900s Edwardian stone terraced",
 "[WALL FINISH AND COLOUR]": "smooth plaster painted a soft sage green",
 "[SKIRTING]": "tall moulded skirting about twenty centimetres high painted white",
 "[ARCHITRAVE]": "moulded white architraves",
 "[INTERNAL DOOR AND HANDLE]": "white four-panel internal doors with round brass knobs",
 "[CEILING]": "a white ceiling with a plaster cornice and a simple glass pendant shade",
 "[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]": "honey-coloured stripped pine floorboards in the hall, a plain oatmeal wool carpet up the stairs, meeting black-and-white quarry tiles in the porch",
 "[RADIATOR]": "a white cast-iron column radiator",
 "[SWITCHES AND SOCKETS]": "brushed brass switches and sockets",
}
def fillp(s):
    for k, v in PROP_F.items(): s = s.replace(k, v)
    assert "[" not in s, s[:200]; return s

PLATES = {}
PLATES["P0-A-KITCHEN"] = dict(model="gpt_image_2_5 sunburst", attach="nothing", beats="HK2-01, B2-02, B2-12",
  body=[S("CAM-LOCK"), WIDE + " "
   "A single photograph of the kitchen of a 1930s brick semi-detached house in the English Midlands, taken from the doorway from the hall: lived in, a little dated, tidy. "
   "The window over a white ceramic sink on the left-hand (east) wall looking onto the back garden, a white uPVC back door beside it with a frosted pane, "
   "cream shaker-style units with brushed steel bar handles along the left and far walls under a light oak-effect laminate worktop, and a small pine table with two chairs on the right. "
   "Named anchors, all fixed: the wide top drawer of the unit nearest the camera, closed; a red enamel kettle on the worktop by the sink; a wooden mug tree with four odd mugs; "
   "a wall calendar with a garden photograph above the table, no readable writing; a spider plant on the windowsill. "
   "Terracotta-effect vinyl floor tiles, walls painted pale butter yellow, a white strip light on the ceiling, switched off.",
   "THE LIGHT: the window over the sink on the left-hand (east) wall is the only source, flat grey-white morning daylight falling across the worktop from the left, "
   "the corner by the table a stop darker with soft sensor noise. " +
   S("VIEW-OUT").replace("[WHAT THE PROPERTY'S EXTERIOR SHOWS FROM THIS ROOM'S SIDE, NAMED]",
     "the back lawn, a raised vegetable bed with runner-bean canes and a wooden shed at the far fence"),
   *TAIL("NEG-SCENE")])
PLATES["P1-A-GARDEN"] = dict(model="gpt_image_2_5 sunburst", attach="P0-A-KITCHEN (approved)", beats="B1-09a, B1-09b, B2-14",
  body=[S("CAM-LOCK"), WIDE + " "
   "A single photograph of the back garden of the same 1930s brick semi-detached house as the attached kitchen reference image, taken from the end of the lawn looking back towards the house: "
   "the red-brick back of the house with the kitchen window and the white uPVC back door, a narrow concrete path running from the back door down the right-hand side of the lawn to the camera, "
   "a close-cut lawn in the middle, and down the left-hand side a raised timber vegetable bed with runner-bean canes and lettuces. "
   "Named anchors, all fixed: the raised vegetable bed with the bean canes; a green plastic watering can on the path by the bed; a weathered teak bench against the right-hand fence; "
   "a small wooden shed in the near left corner, its door shut; a wooden panel fence down both sides with a climbing rose on the right.",
   "THE LIGHT: bright late-morning sun from the south, coming over the left-hand fence at camera-left, raking across the lawn so the bean canes throw shadows to the right, "
   "the back of the house lit from the side, the sky blown white where it enters frame at the top.",
   *TAIL("NEG-SCENE")])
PLATES["P2-D-LOUNGE"] = dict(model="gpt_image_2_5 sunburst", attach="nothing", beats="HK1-01, B1-02, B1-04b, B1-05b, B1-06, B2-09b, B1-12a",
  body=[S("CAM-LOCK"), WIDE + " "
   "A single photograph of the front lounge of a Victorian terraced house in south London, taken from the corner by the door: bright, warm, a lived-in home with a lot of colour. "
   "A deep bay window on the left-hand (south) wall with white wooden shutters folded open, a long teal velvet three-seater sofa facing the bay with its back to the camera's right, "
   "and a low oak coffee table in front of it on a patterned red-and-cream kilim rug. "
   "Named anchors, all fixed: the teal velvet sofa with two mustard cushions; the low oak coffee table with a stack of books and a small bowl of clementines; "
   "a tall rubber plant in a woven basket in the bay; a wall of framed family photographs and prints over the cast-iron fireplace on the right-hand wall, faces too small to read; "
   "a record player on a teak sideboard beside the fireplace. Original pine floorboards stained dark round the rug, walls painted warm white, a paper globe pendant, switched off.",
   "THE LIGHT: the bay window on the left-hand (south) wall is the only source, bright morning daylight pouring across the rug and the sofa from the left, "
   "the fireplace wall a stop darker with soft sensor noise. " +
   S("VIEW-OUT").replace("[WHAT THE PROPERTY'S EXTERIOR SHOWS FROM THIS ROOM'S SIDE, NAMED]",
     "the terraced houses opposite, a London plane tree and a low front wall"),
   *TAIL("NEG-SCENE")])
PLATES["P3-C-SHOP"] = dict(model="gpt_image_2_5 sunburst", attach="nothing", beats="B1-10, B2-06a",
  body=[S("CAM-LOCK"), WIDE + " "
   "A single photograph of a small independent hardware shop on a Bristol high street, taken from the back of the shop looking towards the front: busy, well stocked, a bit cramped. "
   "One long central aisle between two runs of tall painted wooden shelving to the ceiling, the shop windows and a glazed door at the far (front, north) end letting in the street light, "
   "a wooden counter on the right near the front with an old grey till. "
   "Named anchors, all fixed: the long central aisle; the bottom shelves on the left stacked with paint tins; the right-hand shelves of boxed screws, brushes and rolled doormats; "
   "a galvanised metal bucket of brooms and rakes standing at the end of the aisle; a stack of flattened cardboard boxes by the counter. "
   "All tins, boxes and packets plain or with labels too small and soft to read; no signs, no shop name. Worn grey lino floor.",
   "THE LIGHT: bright even working light — the shop windows at the far (north) end glowing white, and a row of fluorescent strip lights along the ceiling lighting the aisle evenly from above; "
   "the corners behind the shelving a little darker with mild sensor noise.",
   *TAIL("NEG-SCENE")])
PLATES["P4-CONSULT"] = dict(model="gpt_image_2_5 sunburst", attach="nothing", beats="B1-01a, B2-11",
  body=[S("CAM-LOCK"), WIDE + " "
   "A single photograph of an orthopaedic consulting room in a small private clinic in an English county town, taken from just inside the door: calm, modern, a little plain. "
   "A window on the right-hand wall with pale roller blinds half down, a white desk under it facing into the room with a desk chair and a visitor's chair, "
   "a padded grey examination couch against the left-hand wall under a paper roll, and a wall-mounted X-ray light box on the far wall, switched off. "
   "Named anchors, all fixed: a life-size plastic anatomical knee model on a stand on the desk, the bones cream, the tendons red; the grey couch with its paper roll; "
   "the X-ray light box; a tall potted fig in the far corner; a hand-gel dispenser by the door. Pale grey walls, light oak-effect vinyl floor.",
   "THE LIGHT: overcast daylight through the window on the right-hand wall as the key, falling across the desk and fading towards the couch; the ceiling panel light on and flat. "
   "The couch end of the room sits slightly dim with mild sensor noise.",
   *TAIL("NEG-SCENE")])
PLATES["P5-PROP-F"] = dict(model="gpt_image_2_5 sunburst", attach="nothing", beats="B1-13a, B1-13b",
  body=[S("CAM-LOCK"), WIDE + " " + fillp(S("PLATE-PROP")) +
   " The staircase is a single straight flight rising away from the camera along the left-hand wall, with a white-painted handrail and white square spindles and the oatmeal carpet running up every tread to a small landing with a window at the top; "
   "the open doorway on the right of the hall shows the front sitting room beyond. A tall wooden coat stand by the door with a red waterproof jacket, "
   "a small half-moon table with a blue glass bowl of keys at the foot of the stairs, a striped runner rug on the hall boards.",
   "Daylight only: the house faces south at the front, so in the morning the front door glass behind the camera throws a bright wash down the hall and up the first few stairs, "
   "the landing window at the top of the stairs is a second, softer source, and the far end of the hall falls a stop darker with soft sensor noise on the back wall.",
   *TAIL("NEG-PROP")])

out = {}
for k, p in PLATES.items():
    txt = "\n\n".join(p["body"]); out[k] = dict(model=p["model"], attach=p["attach"], beats=p["beats"], chars=len(txt), prompt=txt)
    pathlib.Path(f"{k}.prompt.txt").write_text(txt)
    print(f"{k:14s} {len(txt):5d}  attach: {p['attach']}")
json.dump(out, open("plates.json", "w"), indent=1)
