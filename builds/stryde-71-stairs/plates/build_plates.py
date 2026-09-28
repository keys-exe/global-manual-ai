#!/usr/bin/env python3
"""Step-4 plates for stryde-71-stairs (§30C, §30G), assembled from Appendix A by ID (never retyped)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
NEGS = lambda *ids: ", ".join(S(i) for i in ids)
TAIL = lambda *ids: [S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
                     "AVOID: " + NEGS(*ids, "NEG-M1", "NEG-FILE") + ", no people, no product, no staged objects, no readable text or signage"]
def fill(s, d):
    for k, v in d.items(): s = s.replace(k, v)
    assert "[" not in s, s[:200]; return s

# ---- her house (PROP-N) — Property Sheet fields 1-2 ----------------------------------------
PROP_N = {
 "[TYPE AND ERA]": "1960s two-storey red-brick colonial-style",
 "[WALL FINISH AND COLOUR]": "painted drywall in a warm greige, scuffed at hip height along the stairs",
 "[SKIRTING]": "plain white baseboards about ten centimetres high",
 "[ARCHITRAVE]": "simple colonial-profile white door casings",
 "[INTERNAL DOOR AND HANDLE]": "white six-panel doors with round brass knobs",
 "[CEILING]": "a white ceiling with a brass-and-frosted-glass flush light",
 "[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]": "honey-coloured oak floorboards in the hall, the stairs carpeted in a worn beige runner held by brass rods",
 "[RADIATOR]": "a floor air-vent grille",
 "[SWITCHES AND SOCKETS]": "ivory plastic rocker switches and outlets",
}
SHELL_N = {
 "[WALL FINISH AND COLOUR]": PROP_N["[WALL FINISH AND COLOUR]"],
 "[SKIRTING — profile, height, colour]": PROP_N["[SKIRTING]"],
 "[ARCHITRAVE]": PROP_N["[ARCHITRAVE]"],
 "[INTERNAL DOOR — style, colour, handle]": PROP_N["[INTERNAL DOOR AND HANDLE]"],
 "[CEILING]": PROP_N["[CEILING]"],
 "[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]": "honey-coloured oak floorboards, changing to worn beige carpet on the stairs and the upstairs landing, and to cream vinyl tile in the kitchen",
 "[RADIATOR TYPE]": "floor air-vent grilles",
 "[SWITCHES AND SOCKETS]": PROP_N["[SWITCHES AND SOCKETS]"],
}
PHOTOS = ("the whole stair wall hung with family photographs in mismatched frames — graduation portraits in caps and gowns, a black-and-white wedding photo, "
          "school pictures, a church-choir group photo, grandchildren at a birthday — climbing the wall alongside the stairs")

P = {}
P["P0-PROP-N"] = dict(loc="L-N-STAIRS", body=[S("CAM-LOCK"), fill(S("PLATE-PROP"), PROP_N).replace("colonial-style house,", "colonial-style house in a tree-lined suburb of Atlanta, Georgia,") +
  " The straight staircase rises along the right-hand wall of the hall to an upstairs landing, open on its left side with white-painted balusters and a dark-stained oak handrail ending in a square newel post at the bottom step; "
  + PHOTOS + ". At the far end of the hall an open doorway on the left leads into the kitchen, its window bright. Near the door: a small console table with a bowl for keys and a folded church bulletin, "
  "a coat tree with a navy raincoat and a straw sun hat, a braided rag rug on the oak floor.",
  "Daylight only: the front door's narrow glass sidelights behind the camera throw a soft wash down the hall floor, a window on the upstairs landing lights the top of the stairs from above, "
  "and the middle of the hall sits a stop darker with soft sensor noise on the far wall. The front faces west, so the afternoon sun comes in through the sidelights; on a morning the hall is lit indirectly from the landing window."] + TAIL("NEG-PROP"))

P["P1-LANDING"] = dict(loc="L-N-LANDING", body=[S("CAM-LOCK"),
  "A single photograph of the upstairs landing of a " + PROP_N["[TYPE AND ERA]"] + " house in a tree-lined suburb of Atlanta, Georgia, taken at standing chest height from the landing looking back towards the top of the stairs: "
  "the white balusters and dark oak handrail running across the lower part of the frame where the stairs drop away, and behind them the stair wall hung with family photographs in mismatched frames — graduation portraits, a black-and-white wedding photo, grandchildren — rising at an angle. " + fill(S("PROP-SHELL"), SHELL_N) +
  " Named anchors, all fixed: the handrail and balusters; the photo wall; a small window on the right-hand wall of the landing with a sheer white curtain; a white bedroom door ajar on the left.",
  "Soft daylight from the landing window on the right as the key, at about forty-five degrees to the camera, the photo glass catching a few small reflections, the far end of the landing a stop darker. The window faces south."] + TAIL("NEG-PROP"))

P["P2-KITCHEN"] = dict(loc="L-N-KITCHEN", body=[S("CAM-LOCK"),
  "A single photograph of the kitchen of a " + PROP_N["[TYPE AND ERA]"] + " house in a tree-lined suburb of Atlanta, Georgia, taken from the doorway from the hall: " + fill(S("PROP-SHELL"), SHELL_N) +
  " The kitchen is lived-in and a little dated: oak cabinets with brass pulls, a cream laminate countertop, a window over the sink on the far wall with a gingham half-curtain. "
  "Named anchors, all fixed: a round oak kitchen table with four spindle-back chairs in the middle of the room; on the table a lazy Susan crowded with orange prescription pill bottles, a tube of pain-relief gel, a glass of water and a coffee mug; "
  "a wall calendar from a church beside the refrigerator; a fruit bowl of peaches on the counter; a cast-iron skillet on the stove.",
  S("LOC-KITCHEN-DAY") + " The sink window faces south."] + TAIL("NEG-PROP"))

P["P3-RECEPTION"] = dict(loc="L-RECEPTION", body=[S("CAM-LOCK"),
  "A single photograph of an evening wedding reception in a rented banquet hall in Atlanta, taken at head height from the edge of the dance floor: a parquet dance floor in the middle, round tables with white tablecloths and gold chiavari chairs around it, "
  "centerpieces of white hydrangeas in glass vases, a DJ booth with a laptop and speakers at the far end, a three-tier white cake on a side table, "
  "a ceiling hung with warm string lights and two crystal chandeliers, a gold balloon arch behind the head table. Empty — the party paused between songs.",
  "Warm tungsten light from the string lights and the chandeliers as the only source, pools of warm light on the tables, the dance floor a little brighter under the chandeliers, the corners dim with visible sensor noise, highlights on the glassware clipping. The phone has balanced for the warm light, so whites read cream."] + TAIL("NEG-SCENE"))

P["P4-STORE"] = dict(loc="L-STORE", body=[S("CAM-LOCK"),
  "A single photograph inside an ordinary American neighborhood grocery store on a weekday afternoon, taken at head height standing in a checkout lane: a conveyor belt checkout counter with a card reader and a bagging area, "
  "a rack of gum and magazines with unreadable covers, the next checkout lanes along the front of the store, shopping carts nested by the entrance, the produce section soft in the background. Every sign is a plain coloured panel with no readable lettering.",
  "Flat cool-white overhead fluorescent panels as the only key, even and shadowless from above, the floor shining, daylight through the front windows blowing out at the far edge of frame, mild sensor noise in the aisle behind."] + TAIL("NEG-SCENE"))

P["P5-CHURCH"] = dict(loc="L-CHURCH", body=[S("CAM-LOCK"),
  "A single photograph of the front of a red-brick Baptist church in suburban Georgia on a Sunday afternoon, taken at head height from the sidewalk at the foot of its front steps: "
  "a flight of eight wide concrete steps with a black iron handrail up the middle rising to double white doors under a white-columned portico, a white steeple above, trimmed boxwood bushes either side of the steps, "
  "a church sign on the lawn that is a plain white board with no readable lettering, a few parked cars along the curb.",
  S("LOC-EXT-SUN")] + TAIL("NEG-SCENE"))

P["P6-STREET"] = dict(loc="L-STREET", body=[S("CAM-LOCK"),
  "A single photograph of her street, a quiet tree-lined street of 1960s brick houses in a suburb of Atlanta, taken at head height standing on the sidewalk: a concrete sidewalk running away beside a strip of grass and big old oak trees, "
  "front lawns and driveways, mailboxes on posts at the curb, and on the right a two-storey red-brick colonial with black shutters, a small white front porch with two rocking chairs and a straight concrete front path from the sidewalk to the porch steps.",
  S("LOC-EXT-SUN")] + TAIL("NEG-SCENE"))

P["P7-CLINIC"] = dict(loc="L-CLINIC", body=[S("CAM-LOCK"),
  "A single photograph of an exam room in an American outpatient orthopedic and sports-medicine clinic, taken from just inside the door: a padded treatment table with a paper roll in the middle of the room, a rolling stool, "
  "a small desk against the wall with a computer monitor turned away and a life-size anatomical knee model, a window with a half-open white blind on the left-hand wall, a rack of resistance bands and a foam roller in the corner, "
  "a sharps container and glove boxes on a wall shelf, a framed anatomy poster with no readable labels. Speckled grey vinyl floor, pale blue-grey walls.",
  "Soft daylight through the half-open blind on the left-hand wall as the key, falling across the treatment table and fading towards the door, a flat overhead panel light on and doing little. The window side a stop brighter, highlights clipping on the blind slats, mild sensor noise in the far corner. The window faces west."] + TAIL("NEG-SCENE"))

P["P8-MALL"] = dict(loc="L-MALL", body=[S("CAM-LOCK"),
  "A single photograph inside an ordinary two-level American suburban shopping mall outside Atlanta on a Sunday afternoon, taken at head height from the ground-floor concourse at the foot of the central staircase: "
  "a wide straight open staircase of about twenty pale terrazzo steps with brushed-steel handrails and glass balustrade panels rising to the upper-level walkway, "
  "an up escalator running right beside it on its left, the upper walkway with a glass railing crossing the frame above, shopfronts on both levels with plain coloured panels where the signs are and no readable lettering, "
  "a potted ficus in a planter at the foot of the stairs, a bench, pale speckled terrazzo floor. Empty for a moment.",
  "Soft daylight from a long skylight in the atrium roof above the staircase as the key, falling on the steps and the escalator from above and slightly behind the camera, the shopfronts lit by their own warm-white downlights, "
  "highlights on the steel handrails and the terrazzo clipping, the far end of the concourse a stop darker with mild sensor noise."] + TAIL("NEG-SCENE"))

if __name__ == "__main__":
    out = {}
    for k, v in P.items():
        p = "\n\n".join(v["body"]); out[k] = dict(loc=v["loc"], prompt=p)
        pathlib.Path(f"{k}.prompt.txt").write_text(p); print(k, len(p))
    json.dump(out, open("plates.json", "w"), indent=1)
