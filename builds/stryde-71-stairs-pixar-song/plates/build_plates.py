#!/usr/bin/env python3
"""Step-4 plates for stryde-71-stairs-pixar-song (§30C, §30G) — Mode 2 (3D Pixar), 16:9 (V7.68.1), assembled from Appendix A by ID.
Mode 2 adaptation (F10): a render opening in place of CAM-LOCK (§2: no photographic language in Mode 2), PLATE-PROP / PROP-SHELL / PROP-REF
with "photograph" read as "frame", the light profile written as PIX-LIGHT (three sources) in the room's own terms, CAP-ANIM in place of
CAP-A/CAP-FILE, negatives NEG-PROP / NEG-SCENE + NEG-PIX. Empty rooms: no people, no product."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
def fill(s, d):
    for k, v in d.items(): s = s.replace(k, v)
    assert "[" not in s, s[:200]; return s

OPEN = ("A single frame from a finished 3D animated feature film — an empty location plate, rendered through a virtual camera at standing eye level, "
        "deep focus, composed natively for a wide 16:9 frame. The world is stylized storybook-cinematic animation: rich, readable, warm, every surface "
        "with a material, set dressing that tells the story at a glance. A final render from the film — not concept art, not a storyboard, not a game, "
        "not a photograph. NO WRITING ANYWHERE IN THE FRAME: no readable lettering, logos or signage.")
PIX = "LIGHT. " + S("PIX-LIGHT")
CAP = "RENDER. " + S("CAP-ANIM")
def NEG(*ids, extra=""):
    return "AVOID: " + ", ".join(S(i) for i in ids) + ", " + S("NEG-PIX") + ", no people, no product, no staged objects, no readable text or signage, no photograph, no live-action, no logos" + (", " + extra if extra else "") + "."

PROP_N = {
 "[TYPE AND ERA]": "1960s two-storey red-brick colonial-style",
 "[WALL FINISH AND COLOUR]": "painted walls in a warm greige, softly scuffed at hip height along the stairs",
 "[SKIRTING]": "plain white baseboards about ten centimetres high",
 "[ARCHITRAVE]": "simple colonial-profile white door casings",
 "[INTERNAL DOOR AND HANDLE]": "white six-panel doors with round brass knobs",
 "[CEILING]": "a white ceiling with a brass-and-frosted-glass flush light",
 "[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]": "honey-coloured oak floorboards in the hall, the stairs carpeted in a worn beige runner held by brass rods",
 "[RADIATOR]": "a floor air-vent grille",
 "[SWITCHES AND SOCKETS]": "ivory rocker switches and outlets",
}
SHELL_N = {
 "[WALL FINISH AND COLOUR]": PROP_N["[WALL FINISH AND COLOUR]"], "[SKIRTING — profile, height, colour]": PROP_N["[SKIRTING]"],
 "[ARCHITRAVE]": PROP_N["[ARCHITRAVE]"], "[INTERNAL DOOR — style, colour, handle]": PROP_N["[INTERNAL DOOR AND HANDLE]"],
 "[CEILING]": PROP_N["[CEILING]"],
 "[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]": "honey-coloured oak floorboards, changing to worn beige carpet on the stairs and the upstairs landing, and to cream vinyl tile in the kitchen",
 "[RADIATOR TYPE]": "floor air-vent grilles", "[SWITCHES AND SOCKETS]": PROP_N["[SWITCHES AND SOCKETS]"],
}
CARRIED = "the warm greige walls, white baseboards and six-panel doors with brass knobs, honey oak floors turning to worn beige carpet on the stairs and landing, brass-and-frosted flush lights"
PHOTOS = ("the whole stair wall hung with family photographs in mismatched frames — graduation portraits in caps and gowns, a wedding photo, school pictures, "
          "a church-choir group photo, grandchildren at a birthday, every picture a soft painted blur with no readable faces or text — climbing the wall alongside the stairs")
PROP_REF = "PROP-REF: " + S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", CARRIED).replace("reference image", "reference image (Image 1)")

def photo2frame(s): return s.replace("A single photograph", "A single rendered frame").replace("tidied for the photograph", "tidied for the camera")

P = {}
P["P0-PROP-N"] = dict(loc="L-N-STAIRS", attach=[], body=[OPEN,
  photo2frame(fill(S("PLATE-PROP"), PROP_N)).replace("colonial-style house,", "colonial-style house in a tree-lined suburb of Atlanta, Georgia,") +
  " The straight staircase rises along the right-hand wall of the hall to an upstairs landing, open on its left side with white-painted balusters and a dark-stained oak handrail ending in a square newel post at the bottom step; "
  + PHOTOS + ". At the far end of the hall an open doorway on the left leads into the kitchen, its window bright. Near the door: a small console table with a bowl for keys, "
  "a coat tree with a navy raincoat and a straw sun hat. The oak floor is bare all the way down the hall: no rug, no mat, no runner on the floor. Lived-in and loved, a little worn, nothing new.",
  PIX + " Here: the key is warm afternoon daylight through the front door's narrow glass sidelights behind the camera, washing down the hall floor (the front faces west); the fill is the cooler daylight from the landing window at the top of the stairs lighting the upper flight from above, about a quarter as strong; the rim is the bright kitchen doorway at the far end edging the newel post and the console table. The middle of the hall sits a stop darker, warm bounce off the oak floor into the shadow side of the balusters.",
  CAP, NEG("NEG-PROP", "NEG-SCENE")])

P["P1-LANDING"] = dict(loc="L-N-LANDING", attach=["P0-PROP-N"], body=[OPEN, PROP_REF,
  "A single rendered frame of the upstairs landing of a " + PROP_N["[TYPE AND ERA]"] + " house in a tree-lined suburb of Atlanta, Georgia, from standing chest height on the landing looking back towards the top of the stairs: "
  "the white balusters and dark oak handrail running across the lower part of the frame where the stairs drop away, and behind them the same stair wall of family photographs in mismatched frames rising at an angle (soft painted blurs, no readable faces or text). " + fill(S("PROP-SHELL"), SHELL_N) +
  " Named anchors, all fixed: the handrail and balusters; the photo wall; a small window on the right-hand wall of the landing with a sheer white curtain; a white six-panel bedroom door ajar on the left. Empty — nobody in frame, nothing staged.",
  PIX + " Here: the key is soft daylight from the landing window on the right, about forty-five degrees to the camera (the window faces south); the fill is bounce off the warm greige wall opposite, a quarter as strong; the rim is the brighter hall below edging the top of the balusters. The photo glass catches a few small reflections; the far end of the landing a stop darker.",
  CAP, NEG("NEG-PROP", "NEG-SCENE")])

P["P2-KITCHEN"] = dict(loc="L-N-KITCHEN", attach=["P0-PROP-N"], body=[OPEN, PROP_REF,
  "A single rendered frame of the kitchen of a " + PROP_N["[TYPE AND ERA]"] + " house in a tree-lined suburb of Atlanta, Georgia, seen from the doorway from the hall: " + fill(S("PROP-SHELL"), SHELL_N) +
  " The kitchen is lived-in and a little dated: oak cabinets with brass pulls, a cream laminate countertop, a window over the sink on the far wall with a gingham half-curtain. "
  "Named anchors, all fixed: a round oak kitchen table with four spindle-back chairs in the middle of the room; on the table a lazy Susan crowded with orange prescription pill bottles (plain white labels, no readable text), a tube of pain-relief gel, a glass of water and a coffee mug; "
  "a plain wall calendar beside the refrigerator (no readable text); a fruit bowl of peaches on the counter; a cast-iron skillet on the stove. Empty — nobody in frame.",
  PIX + " Here: the key is cool morning daylight from the sink window on the far wall (the window faces south), broad and soft across the table; the fill is a faint warm under-cabinet light on the counter, a quarter as strong; the rim is the bright window edge behind the table catching the chair backs and the rim of the mug. Warm bounce off the oak cabinets into the shadow side of the table.",
  CAP, NEG("NEG-PROP", "NEG-SCENE")])

P["P3-RECEPTION"] = dict(loc="L-RECEPTION", attach=[], body=[OPEN,
  "A single rendered frame of an evening wedding reception in a rented banquet hall in Atlanta, from head height at the edge of the dance floor: a parquet dance floor in the middle, round tables with white tablecloths and gold chiavari chairs around it, "
  "centrepieces of white hydrangeas in glass vases, a DJ booth with speakers at the far end, a three-tier white cake on a side table, "
  "a ceiling hung with warm string lights and two crystal chandeliers, a gold balloon arch behind the head table. Empty — the party paused between songs, nobody in frame, no readable banners or signs.",
  PIX + " Here: the key is the warm tungsten glow of the string lights and the two chandeliers from above, pooling on the dance floor and the tables; the fill is the cooler spill from the DJ booth's small coloured lights at the far end, a quarter as strong; the rim is the chandelier light catching the gold chair backs and the glassware. The corners sit dim and warm.",
  CAP, NEG("NEG-SCENE")])

P["P4-STORE"] = dict(loc="L-STORE", attach=[], body=[OPEN,
  "A single rendered frame inside an ordinary American neighbourhood grocery store on a weekday afternoon, from head height standing in a checkout lane: a conveyor-belt checkout counter with a card reader on a post and a bagging carousel, "
  "a rack of gum and magazines with plain blank covers, the next checkout lanes along the front of the store with their lane-number lights, shopping carts nested by the entrance, the produce section soft in the background. Every sign is a plain coloured panel with no lettering. Empty — nobody in frame.",
  PIX + " Here: the key is the flat cool-white overhead panel lighting from above, even across the lanes; the fill is the warm daylight through the front windows at the far edge, a quarter as strong; the rim is the shine of the polished floor and the steel of the counter edges. The far aisle a stop darker.",
  CAP, NEG("NEG-SCENE")])

P["P5-CHURCH"] = dict(loc="L-CHURCH", attach=[], body=[OPEN,
  "A single rendered frame of the front of a red-brick Baptist church in suburban Georgia on a Sunday afternoon, from head height on the sidewalk at the foot of its front steps: "
  "a flight of eight wide concrete steps with a black iron handrail up the middle rising to double white doors under a white-columned portico, a white steeple above, trimmed boxwood bushes either side of the steps, "
  "a church sign on the lawn that is a plain white board with no lettering, a few parked cars along the curb. Empty — nobody in frame.",
  PIX + " Here: the key is hard warm afternoon sun from upper camera-left, short shadows under the portico and the step edges; the fill is the blue skylight on the shadow side, a quarter as strong; the rim is the sun catching the white columns' edges and the iron handrail. Warm bounce off the concrete into the shadows.",
  CAP, NEG("NEG-SCENE")])

P["P6-STREET"] = dict(loc="L-STREET", attach=[], body=[OPEN,
  "A single rendered frame of her street, a quiet tree-lined street of 1960s brick houses in a suburb of Atlanta, from head height standing on the sidewalk: a concrete sidewalk running away beside a strip of grass and big old oak trees, "
  "front lawns and driveways, mailboxes on posts at the curb (no lettering), and on the right a two-storey red-brick colonial with black shutters, a small white front porch with two rocking chairs and a straight concrete front path from the sidewalk to the porch steps. Empty — nobody in frame, no cars moving.",
  PIX + " Here: the key is hard warm afternoon sun from upper camera-left through the oak leaves, dappled on the sidewalk; the fill is open blue sky on the shadow side, a quarter as strong; the rim is sunlight edging the porch rail and the mailbox posts. Warm bounce off the concrete path.",
  CAP, NEG("NEG-SCENE")])

P["P7-CLINIC"] = dict(loc="L-CLINIC", attach=[], body=[OPEN,
  "A single rendered frame of an exam room in an American outpatient orthopaedic and sports-medicine clinic, from just inside the door: a padded treatment table with a paper roll in the middle of the room, a rolling stool, "
  "a small desk against the wall with a monitor turned away and a life-size anatomical knee model, a window with a half-open white blind on the left-hand wall, a rack of resistance bands and a foam roller in the corner, "
  "glove boxes on a wall shelf, a framed anatomy poster with no readable labels. Speckled grey vinyl floor, pale blue-grey walls. Empty — nobody in frame.",
  PIX + " Here: the key is soft daylight through the half-open blind on the left-hand wall (the window faces west), falling in soft bands across the treatment table; the fill is the flat cool overhead panel, a quarter as strong; the rim is the window light edging the stool and the knee model. The door side a stop darker.",
  CAP, NEG("NEG-SCENE")])

if __name__ == "__main__":
    out = {}
    for k, v in P.items():
        p = "\n\n".join(v["body"]); out[k] = dict(loc=v["loc"], attach=v["attach"], prompt=p)
        pathlib.Path(__file__).parent.joinpath(f"{k}.prompt.txt").write_text(p); print(k, len(p), v["attach"])
    json.dump(out, open(pathlib.Path(__file__).parent / "plates.json", "w"), indent=1)

# ---------------- v2 (user Fix, 2026-10-01) ----------------------------------------------------------------
# P1-LANDING: "NOT THE SAME AS THE P0 PROP N" → HT17 / §6A Part 2 rule 3: an image EDIT of the confirmed P0 (Image 1), the same
# flight seen from its top; every fixed feature on the correct screen side for the new angle.
# P2-KITCHEN: "I NEED A NEW UNIQUE ARANGEMENTS HERE" → a new, specific, personal kitchen of the same house (P0 attached), not a catalogue oak kitchen.
V2 = {}
V2["P1-LANDING"] = dict(loc="L-N-LANDING", attach=["P0-PROP-N"], edit_of="P0-PROP-N", body=[
  "Keep this house exactly as it is. Image 1 is the confirmed property plate of this hall: the straight staircase rising along the hall's right-hand wall, "
  "carpeted in the worn beige runner with brass rods, white balusters and a dark oak handrail on its open side, a square white newel post at the bottom step, "
  "the whole stair wall hung with the family photographs in mismatched frames climbing diagonally beside the steps, the brass-and-frosted flush light, "
  "the warm greige walls, white baseboards and casings, white six-panel doors with round brass knobs, honey oak floorboards in the hall, the front door with "
  "its narrow glass sidelights, the grey console table with the bowl, the coat tree with the navy raincoat and the straw hat, the open kitchen doorway at the far end. "
  "Change only the camera: now it stands on the upstairs landing at the TOP of that same flight, at standing chest height, looking straight back DOWN the stairs to the hall. "
  "So the same flight drops away from the bottom of the frame to the hall floor; the same photo wall with the same frames is now on the LEFT, the frames stepping down "
  "beside the steps; the same white balusters and dark oak rail run down the RIGHT side of the flight to the same square newel at the bottom; at the foot of the stairs "
  "the same honey oak hall floor, and beyond it the same front door with its glass sidelights glowing; the kitchen doorway is behind the camera and not in frame. "
  "Around the camera the landing itself: the worn beige carpet continuing from the stair runner across the landing floor, the greige walls, a white six-panel bedroom "
  "door ajar on the left wall of the landing, a small window with a sheer white curtain on the right wall of the landing throwing soft daylight across the top steps. "
  "Nothing else is new: no second staircase, no balustrade well, no gallery, no extra doors, no new furniture, no new pictures — the same house, the same stairs, from the top.",
  OPEN,
  PIX + " Here: the key is the soft daylight from the landing window on the right (the window faces south), about forty-five degrees to the camera; the fill is the warm "
  "afternoon light from the front-door sidelights rising up the flight from the hall below, a quarter as strong; the rim is that hall light edging the balusters and the "
  "top of the newel. The landing a stop darker than the hall below.",
  CAP, NEG("NEG-PROP", "NEG-SCENE", extra="no square stairwell, no balustrade on three sides, no gallery landing, no second flight, no photo wall on the right, no rail on the left, no frames in a new arrangement")])

V2["P2-KITCHEN"] = dict(loc="L-N-KITCHEN", attach=["P0-PROP-N"], body=[OPEN, PROP_REF,
  "A single rendered frame of the kitchen of a " + PROP_N["[TYPE AND ERA]"] + " house in a tree-lined suburb of Atlanta, Georgia — a Southern grandmother's kitchen, "
  "personal and particular, nothing from a catalogue — seen from the doorway from the hall: " + fill(S("PROP-SHELL"), SHELL_N) +
  " THE ARRANGEMENT, counted and closed. On the far wall, under the window over the sink (a sash window with a lace café curtain on a brass rod, a red geranium "
  "in a clay pot on the sill), a run of cabinets painted a soft sage green with worn brass pulls and a butter-yellow laminate counter; a white enamel double sink; "
  "an old cream electric range on the left wall with a row of three cast-iron skillets hanging on hooks above it and a tin of wooden spoons; a tall white refrigerator "
  "on the right wall with grandchildren's crayon drawings held by fruit magnets (no readable words) and a church hand-fan tucked in the door handle. In the window corner "
  "on the right, a breakfast nook: a round oak pedestal table with a white lace tablecloth and four spindle-back chairs, one with a floral seat cushion, set into the "
  "corner by the window. On the table: a wooden lazy Susan crowded with orange prescription pill bottles (plain white labels, no readable text), a tube of pain-relief "
  "gel, a glass of water, a coffee mug and a sweet-tea pitcher with lemon slices. On the counter: a wooden bowl of peaches and a glass cake stand with a pound cake "
  "under its dome. A wall-mounted beige telephone with its long coiled cord beside the doorway; a plain wall calendar beside the refrigerator (no readable text); "
  "a braided oval rag rug in front of the sink on the cream vinyl tile. Nothing else on the counters. Empty — nobody in frame.",
  PIX + " Here: the key is cool morning daylight from the sink window on the far wall (the window faces south), broad and soft across the nook table; the fill is "
  "a faint warm light from the range hood's small bulb on the left, a quarter as strong; the rim is the bright window edge behind the table catching the chair backs, "
  "the pitcher and the rim of the mug. Warm bounce off the yellow counter into the shadow side of the table.",
  CAP, NEG("NEG-PROP", "NEG-SCENE", extra="no oak cabinets, no plain modern kitchen, no island, no stainless steel, no gingham, no catalogue kitchen")])

if __name__ == "__main__" and True:
    for k, v in V2.items():
        p = "\n\n".join(v["body"]); pathlib.Path(__file__).parent.joinpath(f"{k}.v2.prompt.txt").write_text(p); print("v2", k, len(p))
    out = json.load(open(pathlib.Path(__file__).parent / "plates.json"))
    for k, v in V2.items(): out[k + "@v2"] = dict(loc=v["loc"], attach=v["attach"], edit_of=v.get("edit_of"), prompt="\n\n".join(v["body"]))
    json.dump(out, open(pathlib.Path(__file__).parent / "plates.json", "w"), indent=1)

# ---------------- v3 (user, 2026-10-01: "FIX THE P1 I WANT IT CONNECTED TO THE P0") -------------------------------------
# v2 drew a return stair with a half-landing. v3: the same ONE straight flight, counted, from its top — an edit of P0 on a true
# Nano Banana Pro route (Kie `nano-banana-pro`, P0 as image_input), since Higgsfield reroutes every Pro call to Nano Banana 2.
V3 = {}
V3["P1-LANDING"] = dict(loc="L-N-LANDING", attach=["P0-PROP-N"], edit_of="P0-PROP-N", body=[
  "Image 1 is the finished property plate of this hall and it is the truth: ONE straight staircase of fourteen steps rising along the hall's right-hand "
  "wall, a worn beige carpet runner held by brass rods on every step, white turned balusters and a dark oak handrail on its open left side, a square white "
  "newel post at the bottom step, the family photographs in mismatched frames climbing the stair wall beside the steps, the warm greige walls, white "
  "baseboards and casings, the brass-and-frosted flush light, honey oak floorboards in the hall, the front door with its narrow glass sidelights, the grey "
  "console table with a bowl, the coat tree with a navy raincoat and a straw hat. Keep every one of these exactly as they are. "
  "MAKE THIS PICTURE: the same flight, seen from its top. The camera stands on the upstairs landing at the head of that ONE straight flight, at standing "
  "chest height, looking straight down the whole run of fourteen carpeted steps to the hall floor, so the flight runs from the bottom edge of the frame away "
  "and down to the centre. There is no turn, no half-landing, no second flight, no bend: one straight run, top to bottom. On the LEFT of the flight, the same "
  "stair wall with the same photographs in the same frames, now seen descending beside the steps. On the RIGHT of the flight, the same white balusters and "
  "dark oak handrail running straight down to the same square newel post at the bottom. At the foot of the flight the same honey oak hall floor, the same "
  "grey console table and coat tree against the left wall, and straight ahead the same front door with its glass sidelights glowing with afternoon light. "
  "Around the camera, only the top of the landing: the beige carpet continuing from the top step across the landing floor at the bottom corners of the "
  "frame, a sliver of greige wall at each edge. Nothing else: no window in frame, no doors in frame, no gallery, no balustrade across the frame, "
  "no furniture on the landing, no new pictures. Counted and closed: one flight, one rail, one newel, one photo wall, one door at the bottom.",
  OPEN,
  PIX + " Here: the key is the warm afternoon daylight through the front-door sidelights at the bottom of the flight, rising up the steps toward the "
  "camera and catching the brass rods; the fill is soft daylight from the landing window behind the camera, a quarter as strong, on the top steps; "
  "the rim is the sidelight glow edging the balusters and the newel. The landing end a stop darker than the hall below.",
  CAP, NEG("NEG-PROP", "NEG-SCENE", extra="no turn in the stairs, no half-landing, no second flight, no return stair, no L-shaped stair, no square stairwell, no balustrade across the top of the frame, no window in frame, no door at the top, no photo wall on the right, no rail on the left, no landing furniture")])

if __name__ == "__main__" and True:
    for k, v in V3.items():
        p = "\n\n".join(v["body"]); pathlib.Path(__file__).parent.joinpath(f"{k}.v3.prompt.txt").write_text(p); print("v3", k, len(p))
    out = json.load(open(pathlib.Path(__file__).parent / "plates.json"))
    for k, v in V3.items(): out[k + "@v3"] = dict(loc=v["loc"], attach=v["attach"], edit_of=v.get("edit_of"), prompt="\n\n".join(v["body"]), route="Kie nano-banana-pro")
    json.dump(out, open(pathlib.Path(__file__).parent / "plates.json", "w"), indent=1)
