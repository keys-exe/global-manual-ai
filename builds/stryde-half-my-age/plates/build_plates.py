#!/usr/bin/env python3
"""§30G/§30C Mode 4 plates for stryde-half-my-age (16:9, V7.68.1), strings pulled from Appendix A by ID.
Assembly: CAM-FILM (wide, tripod) → PLATE-PROP | PROP-REF + PROP-SHELL + room → VIEW-OUT → PROD-DEPTH → LIGHT-FILM → LOOK → PHYS-FRAME-C → CAP-FILM → negatives."""
import re, json, pathlib
HERE = pathlib.Path(__file__).parent
T = (HERE.parents[2] / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i):
    return re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S).group(1).strip()
LOOK = (HERE.parent / "cast/LOOK.txt").read_text().strip()
CAPF = S("CAP-FILM").replace("[HIGHLIGHT BEHAVIOUR]", "rolling off softly into white with a faint warm halation around bulbs and bright windows, never clipping to a hard edge")
NEGF = S("NEG-FILM").replace(", no actor looking into the lens", "")
def CAM(f, stop): return (S("CAM-FILM").replace("[CAMERA AND FORMAT]", "an ARRI Alexa Mini LF in large format").replace("[LENS FAMILY]", "an ARRI Signature Prime")
    .replace("[FOCAL]", str(f)).replace("[STOP]", stop).replace("[COLOUR SCIENCE]", "ARRI").replace("[RIG]", "a locked tripod at standing eye height")
    .replace("composed natively for a vertical 9:16 frame", "composed as a wide 16:9 reference frame of the whole space"))
def LIGHT(mot, side, q, r): return S("LIGHT-FILM").replace("[MOTIVATION]", mot).replace("[SIDE]", side).replace("[KEY QUALITY]", q).replace("[RATIO]", r)
def DEPTH(fg): return S("PROD-DEPTH").replace("[FOREGROUND ELEMENT]", fg).replace("[WHO] in the middle ground", "the empty space in the middle ground")
EMPTY = "Empty: nobody in frame, no person, no product, nothing held, nothing staged, nothing tidied for the photograph."
NEG_BASE = "no people, no person, no figures, no hands, no knee strap or product, no readable text, no signs with legible words, no logos, no brand names"

# Property Sheet field 2 — the shell, named once, pasted verbatim
SHELL = S("PROP-SHELL").replace("[WALL FINISH AND COLOUR]", "warm off-white magnolia emulsion over slightly uneven old plaster").replace(
  "[SKIRTING — profile, height, colour]", "tall moulded 1930s skirting gloss-painted white and gone slightly yellow").replace(
  "[ARCHITRAVE]", "moulded white gloss architraves").replace("[INTERNAL DOOR — style, colour, handle]", "white-painted 1930s doors with three horizontal panels and worn brass lever handles").replace(
  "[CEILING]", "plain white ceilings with a small plaster ceiling rose").replace("[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]", "worn oatmeal wool carpet through the hall, stairs, landing, bedrooms and living room, changing to brown-and-cream patterned vinyl at the kitchen threshold").replace(
  "[RADIATOR TYPE]", "white steel panel radiators under the windows").replace("[SWITCHES AND SOCKETS]", "white plastic rocker switches and sockets, slightly yellowed")
FINISHES = "magnolia walls over old plaster, yellowed white 1930s skirting, three-panel white doors with brass levers, oatmeal carpet"
NEGP = S("NEG-PROP")

PLATES = {
 "P-HOUSE": dict(f=24, stop="T5.6", prop=False,
   body=S("PLATE-PROP").replace("[TYPE AND ERA]", "1930s red-brick semi-detached").replace(
     "[WALL FINISH AND COLOUR]", "magnolia emulsion over slightly uneven old plaster with a dado rail in the hall").replace("[SKIRTING]", "tall moulded skirting gloss-painted white and gone slightly yellow").replace(
     "[ARCHITRAVE]", "moulded white gloss architraves").replace("[INTERNAL DOOR AND HANDLE]", "white-painted 1930s doors with three horizontal panels and worn brass lever handles").replace(
     "[CEILING]", "a plain white ceiling with a small plaster rose and a glass pendant shade").replace("[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]", "worn oatmeal wool carpet down the hall and up the stairs, held by brass stair rods on every tread").replace(
     "[RADIATOR]", "a white steel panel radiator on the hall wall").replace("[SWITCHES AND SOCKETS]", "white plastic rocker switches, slightly yellowed")
     + " The staircase rises along the left-hand wall, a straight flight of thirteen carpeted steps to a small landing, with a dark-varnished wooden banister and square spindles on its open right-hand side; framed family photographs climb the stair wall, the faces too small to read. At the foot of the stairs a small dark-wood telephone table with a cream telephone, and a brass barometer on the wall above it. On the right, an open doorway into the front living room shows a patterned rug and the arm of a brown leather armchair.",
   light=("THE DAYLIGHT THROUGH THE FRONT DOOR GLASS BEHIND THE CAMERA AND THROUGH THE LIVING-ROOM DOORWAY", "FRAME RIGHT", "soft, cool northern daylight", "3:1"),
   fg="the painted edge of the open front door", neg=[NEG_BASE, "no dado-free walls in the hall"][:1]),
 "L-STAIRS": dict(f=35, stop="T5.6", prop=True,   # v3 — user Fix "it doesnt feel like connected to the p-house": v2 had the stair mirrored
   body="LOCATION PLATE: Image 1 is this house's hall and staircase seen from the front door. This picture is THE SAME STAIRCASE seen from the other end: the camera stands level on the small upstairs landing at eye height, at the top of the flight, looking straight down the stairs toward the front door. Because we now look back the way the stairs climbed, every feature of Image 1 is mirrored left-to-right: the magnolia stair wall with its dado rail and the climbing row of small framed black-and-white family photographs is now on the RIGHT side of the flight; the open side with the dark-varnished wooden banister, square spindles and the dark newel post is now on the LEFT, the top newel post big in the near left foreground. A straight flight of thirteen equal steps of the same oatmeal carpet with a brass stair rod on every tread runs straight down to the hall. At the bottom of the flight, at the far end of the hall and facing the camera: the same dark green front door with its frosted glass panel and brass lever handle, daylight glowing through the glass; the same small dark-wood telephone table with the cream telephone at the foot of the stairs and the brass barometer on the wall; the open doorway into the living room on the LEFT at the bottom; the same glass pendant light hanging over the hall. Everything exactly as in Image 1, only seen from the top. True-to-life proportions, verticals straight. Named anchors, all fixed: the banister and newel posts on the left; the photographs on the right-hand wall; the green front door at the bottom; the telephone table and barometer at the foot.",
   light=("THE FRONT DOOR GLASS AT THE BOTTOM OF THE FLIGHT", "FRAME CENTRE, FAR", "soft, cool northern daylight", "3:1"), fg="the rounded top of the newel post", view=None,
   extra_neg="no photographs on the left wall, no banister on the right, no different front door, no floor tiles in the hall, no landing window in frame, no wide-angle distortion, no fisheye, no bent or curving verticals, no stretched steps, no steps of different sizes"),
 "L-KITCHEN": dict(f=24, stop="T5.6", prop=True,
   body="LOCATION PLATE: the kitchen at the back of the house, seen from the doorway from the hall. Along the back wall a window over a white ceramic sink looks onto the back garden, a spider plant in a pot on the sill; pale sage-green 1980s wall cupboards and worktops of cream laminate run along the right-hand wall with a white gas cooker and a round-shouldered cream fridge; on the left, under a second smaller window, a scrubbed pine kitchen table with four ladder-back chairs and a folded blue-and-white checked tea towel on its corner. A small transistor radio on the worktop, a biscuit tin beside the kettle. Brown-and-cream patterned vinyl floor. Named anchors, all fixed: the scrubbed pine table and four ladder-back chairs by the left window; the sage-green wall cupboards; the white sink under the back window with the spider plant; the cream fridge.",
   light=("THE BACK WINDOW OVER THE SINK AND THE SMALL LEFT WINDOW", "FRAME LEFT", "soft warm afternoon daylight from the south-west", "3:1"), fg="the white-painted doorframe", view="the back garden — a lawn, a washing line and a brown wooden fence with a garden shed"),
 "L-BEDROOM": dict(f=24, stop="T5.6", prop=True,
   body="LOCATION PLATE: the back bedroom, seen from the doorway from the landing. A double bed with a dark-wood headboard and a pale green candlewick bedspread against the right-hand wall; beside it a bedside table with a small lamp with a pleated shade; on the far wall, under the window, a tall dark-wood chest of five drawers with brass handles, its bottom drawer a little proud where it does not quite shut; a walnut wardrobe on the left-hand wall; net curtains and floral cotton curtains at the window. Named anchors, all fixed: the tall dark-wood chest of drawers under the window, bottom drawer not quite shut; the pale green candlewick bedspread; the walnut wardrobe; the bedside lamp with the pleated shade.",
   light=("THE WINDOW OVER THE CHEST OF DRAWERS", "FRAME CENTRE-RIGHT", "soft warm daylight from the south-west through net curtains", "3:1"), fg="the edge of the open bedroom door", view="the back garden and the backs of the houses beyond"),
 "L-LIVING": dict(f=24, stop="T5.6", prop=True,
   body="LOCATION PLATE: the front living room, seen from the doorway from the hall. A deep bay window with net curtains and heavy green velvet curtains on the far wall; a 1930s tiled fireplace with a gas fire and a wooden mantel of framed photographs, faces too small to read, on the right-hand wall; a worn brown leather armchair angled beside the fire; a three-seat sofa in faded rose-and-cream floral fabric facing it; a standard lamp with a fringed shade beside the armchair; a patterned red-and-cream rug over the oatmeal carpet in the middle of the room, a clear stretch of carpet between the sofa and the fire. Named anchors, all fixed: the brown leather armchair by the fire; the tiled 1930s fireplace and mantel; the floral three-seat sofa; the bay window with green velvet curtains.",
   light=("THE BAY WINDOW", "FRAME CENTRE-LEFT", "soft, cool northern daylight", "3:1"), fg="the white-painted doorframe", view="the street — a privet hedge, a low brick wall and the red-brick semis opposite"),
 "L-STATION": dict(f=24, stop="T5.6", prop=False,
   body="LOCATION PLATE: a Victorian railway station in a northern English town, seen from the top of a wide stone staircase that leads down from the footbridge to the platform: about twenty worn sandstone steps with a black iron handrail down the middle and down each side, cream-and-green painted cast-iron columns and a glass-and-iron canopy over the platform below, a local passenger train in plain unbranded livery standing at the platform with its doors open. Named anchors, all fixed: the worn sandstone steps with the black iron centre handrail; the green-and-cream cast-iron columns; the glass canopy; the waiting train with its doors open. Platform signs are blank panels with no readable words.",
   light=("THE OVERCAST SKY THROUGH THE GLASS CANOPY", "FRAME TOP", "soft, cool overcast daylight", "3:1"), fg="the black iron handrail post at the top of the stairs", view=None),
 "L-CARRIAGE": dict(f=24, stop="T4", prop=False,
   body="LOCATION PLATE: inside the carriage of a local passenger train, seen from the vestibule looking down the aisle: pairs of seats in worn blue patterned moquette facing each other across small tables, grey plastic panels, grab poles, luggage racks overhead, wide windows on both sides showing a blurred northern town going past. Named anchors, all fixed: the blue patterned moquette seats in facing pairs; the small grey tables; the yellow grab poles by the doors. No readable text on any panel.",
   light=("THE CARRIAGE WINDOWS", "FRAME LEFT", "soft overcast daylight", "3:1"), fg="the edge of a seat back", view=None),
 "L-ESCALATOR": dict(f=28, stop="T5.6", prop=False,
   body="LOCATION PLATE: a busy city railway station concourse at the foot of a long escalator bank rising to the street: a stopped escalator on the right with a yellow folding barrier across its foot, its steps still, and beside it on the left a fixed staircase of about thirty steps with steel handrails climbing the same slope, tiled walls, a steel-and-glass roof high above. Named anchors, all fixed: the stopped escalator with the yellow barrier; the fixed staircase beside it with steel handrails; the glass roof. Every sign is a blank panel with no readable words.",
   light=("THE GLASS ROOF", "FRAME TOP", "cool, diffused daylight mixed with the white light of the station", "3:1"), fg="a steel handrail end at the foot of the stairs", view=None),
 "L-SHOPCENTRE": dict(f=24, stop="T5.6", prop=False,
   body="LOCATION PLATE: the atrium of an ordinary town-centre shopping centre, seen from the lower floor: a glass lift in a steel frame on the left with its doors closed, and to its right a wide flight of about twenty tiled steps with chrome handrails climbing to the upper gallery of shopfronts; pale stone-effect floor tiles, a skylight above. Shopfronts are plain with blank signs, no readable words, no logos. Named anchors, all fixed: the glass lift on the left; the wide tiled staircase with chrome handrails; the upper gallery rail; the skylight.",
   light=("THE SKYLIGHT", "FRAME TOP", "soft daylight from above", "3:1"), fg="the chrome handrail end at the foot of the stairs", view=None),
 "L-WEDDING": dict(f=24, stop="T4", prop=False,
   body="LOCATION PLATE: an evening wedding reception in the function room of a country hotel in the north of England, seen from the edge of the dance floor: a wooden parquet dance floor in the middle, round tables with white cloths, small candle jars and flower centrepieces around it, strings of warm fairy lights looped across the ceiling, a small raised stage at the back with a DJ desk, chairs dressed in ivory covers, the tables' glasses half-drunk. Named anchors, all fixed: the parquet dance floor; the looped fairy lights; the round white-clothed tables with candle jars; the small stage at the back. No banners or signs with words.",
   light=("THE FAIRY LIGHTS AND CANDLE JARS", "FRAME TOP AND ALL AROUND", "warm, low tungsten practical light with a soft top spill", "4:1"), fg="the edge of a white-clothed table with a candle jar", view=None),
 "L-SHOP": dict(f=28, stop="T4", prop=False,
   body="LOCATION PLATE: the checkout lane of a small town-centre supermarket, seen from the queue: a conveyor belt checkout with a till and a bagging area, a cashier's empty seat, a short queue space marked by a low chrome rail, shelves of sweets and magazines with unreadable covers along the lane, the shop floor and aisles beyond. Every label and price sign blank or unreadable, no logos. Named anchors, all fixed: the conveyor-belt checkout and till; the chrome queue rail; the rack beside the lane.",
   light=("THE CEILING LIGHTS AND THE SHOP'S GLASS FRONT", "FRAME LEFT", "soft white shop light mixed with daylight from the glass front", "3:1"), fg="the end of the chrome queue rail", view=None),
 "L-CAFE": dict(f=28, stop="T4", prop=False,
   body="LOCATION PLATE: a warm, independent café on a northern English high street, seen from near the door: small round wooden tables with bentwood chairs, a long wooden counter with a glass cake display and a coffee machine at the back, exposed brick on one wall and pale sage-green paint on the other, pendant lights with warm bulbs, a big front window onto the street on the left. A clear stretch of floor between the door and the tables. Named anchors, all fixed: the round wooden table by the front window with three bentwood chairs; the counter with the glass cake display; the exposed brick wall; the warm pendant lights. No readable menu boards, no logos.",
   light=("THE BIG FRONT WINDOW", "FRAME LEFT", "soft, warm late-morning daylight", "3:1"), fg="the back of a bentwood chair", view=None),
}

def build(k, c):
    parts = [CAM(c["f"], c["stop"])]
    if c["prop"]:
        parts.append(S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", FINISHES) + " " + SHELL)
    parts.append(c["body"])
    if k == "P-HOUSE": parts[-1] += " A northern English town house, lived in by the same couple for forty years."
    if c.get("view"):
        parts.append(S("VIEW-OUT").replace("[WHAT THE PROPERTY'S EXTERIOR SHOWS FROM THIS ROOM'S SIDE, NAMED]", c["view"]))
    parts += ([] if k == "P-HOUSE" else [EMPTY]) + [DEPTH(c["fg"]), LIGHT(*c["light"]), LOOK, S("PHYS-FRAME-C"), CAPF]
    neg = [NEG_BASE] + ([c["extra_neg"]] if c.get("extra_neg") else []) + ([NEGP] if c["prop"] or k == "P-HOUSE" else []) + [NEGF, S("NEG-LIGHT")]
    parts.append("AVOID: " + ", ".join(neg) + ".")
    p = "\n\n".join(parts); assert "[" not in p, k
    return p

if __name__ == "__main__":
    out = {}
    for k, c in PLATES.items():
        out[k] = build(k, c); (HERE / f"{k}.prompt.txt").write_text(out[k]); print(k, len(out[k]))
    json.dump(out, open(HERE / "prompts.json", "w"), indent=1, ensure_ascii=False)
