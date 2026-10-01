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
