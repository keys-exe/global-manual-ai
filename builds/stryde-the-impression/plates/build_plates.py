#!/usr/bin/env python3
"""§30G/§30C Mode 4 plates for stryde-the-impression (16:9, V7.68.1), strings pulled from Appendix A by ID.
Assembly: CAM-FILM (wide, tripod) → PLATE-PROP | PROP-REF + PROP-SHELL + room → VIEW-OUT → PROD-DEPTH → LIGHT-FILM → LOOK → PHYS-FRAME-C → CAP-FILM → negatives."""
import re, json, pathlib
HERE = pathlib.Path(__file__).parent
T = (HERE.parents[2] / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i):
    return re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S).group(1).strip()
LOOK = (HERE.parent / "cast/LOOK.txt").read_text().strip()
CAPF = S("CAP-FILM").replace("[HIGHLIGHT BEHAVIOUR]", "rolling off softly into white with a faint warm halation around bulbs and bright windows, never clipping to a hard edge")
NEGF = S("NEG-FILM").replace(", no actor looking into the lens", "")
def CAM(f, stop): return (S("CAM-FILM").replace("[CAMERA AND FORMAT]", "an ARRI Alexa 35").replace("[LENS FAMILY]", "a Cooke S4/i prime")
    .replace("[FOCAL]", str(f)).replace("[STOP]", stop).replace("[COLOUR SCIENCE]", "ARRI").replace("[RIG]", "a locked tripod at standing eye height")
    .replace("composed natively for a vertical 9:16 frame", "composed as a wide 16:9 reference frame of the whole space"))
def LIGHT(mot, side, q, r): return S("LIGHT-FILM").replace("[MOTIVATION]", mot).replace("[SIDE]", side).replace("[KEY QUALITY]", q).replace("[RATIO]", r)
def DEPTH(fg): return S("PROD-DEPTH").replace("[FOREGROUND ELEMENT]", fg).replace("[WHO] in the middle ground", "the empty space in the middle ground")
EMPTY = "Empty: nobody in frame, no person, no product, nothing held, nothing staged, nothing tidied for the photograph."
NEG_BASE = "no people, no person, no figures, no hands, no knee strap or product, no readable text, no signs with legible words, no logos, no brand names"

# Property Sheet (§30G) — Hazel and Roy's house; field 2, the shell, named once and pasted verbatim
SHELL = S("PROP-SHELL").replace("[WALL FINISH AND COLOUR]", "warm cream emulsion over slightly uneven old lime plaster").replace(
  "[SKIRTING — profile, height, colour]", "tall moulded Victorian skirting painted white and gone slightly yellow").replace(
  "[ARCHITRAVE]", "moulded white-painted architraves").replace("[INTERNAL DOOR — style, colour, handle]", "four-panel stripped and waxed pine doors with round brass knobs").replace(
  "[CEILING]", "high white ceilings with a plain plaster cornice").replace("[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]", "original Victorian red, black and cream geometric floor tiles in the hall, a sage-green stair carpet with brass stair rods up the stairs and across the landing, oatmeal carpet in the front room and bedroom, and terracotta quarry tiles in the kitchen").replace(
  "[RADIATOR TYPE]", "white-painted cast-iron column radiators").replace("[SWITCHES AND SOCKETS]", "white plastic rocker switches and sockets, slightly yellowed")
FINISHES = "cream walls over old plaster, yellowed white Victorian skirting, stripped pine four-panel doors with brass knobs, red-black-cream hall tiles, the sage-green stair carpet with brass rods"
NEGP = S("NEG-PROP")
EXTERIOR = "the steep street outside — gritstone terraced houses on the other side stepping down the hill, their slate roofs and chimneys, a stone pavement"

PLATES = {
 "P-HOUSE": dict(f=24, stop="T5.6", prop=False,
   body=S("PLATE-PROP").replace("[TYPE AND ERA]", "Victorian gritstone through-terraced").replace(
     "[WALL FINISH AND COLOUR]", "warm cream emulsion over slightly uneven old lime plaster").replace("[SKIRTING]", "tall moulded Victorian skirting painted white and gone slightly yellow").replace(
     "[ARCHITRAVE]", "moulded white-painted architraves").replace("[INTERNAL DOOR AND HANDLE]", "four-panel stripped and waxed pine doors with round brass knobs").replace(
     "[CEILING]", "a high white ceiling with a plain plaster cornice and a glass pendant shade").replace("[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]", "original Victorian red, black and cream geometric floor tiles down the hall, meeting a sage-green stair carpet held by brass stair rods on every tread").replace(
     "[RADIATOR]", "a white-painted cast-iron column radiator on the hall wall").replace("[SWITCHES AND SOCKETS]", "white plastic rocker switches, slightly yellowed")
     + " A long, narrow hall runs straight back from the front door to the kitchen door at the far end, which stands open onto a glimpse of the kitchen's terracotta floor and a window. The staircase rises along the LEFT-hand wall, starting a little way in from the front door and climbing away from the camera toward the back of the house: a straight flight of fourteen carpeted steps, its open side on the right with a dark-varnished wooden banister, plain turned spindles and a dark newel post at the bottom step. A row of small framed family photographs climbs the stair wall above a white dado rail, the faces too small to read. On the RIGHT-hand wall, just past the radiator, a stripped pine door stands open into the front room, showing the end of a dining table and the back of a chair. Brass coat hooks by the front door with two coats on them, a small oak hall table with a brass dish under a round mirror.",
   light=("THE DAYLIGHT THROUGH THE FRONT DOOR GLASS BEHIND THE CAMERA AND THROUGH THE KITCHEN WINDOW AT THE FAR END", "FRAME CENTRE, FAR", "soft, cool northern daylight", "3:1"),
   fg="the painted edge of the open front door"),
 "L-STAIRS": dict(f=32, stop="T5.6", prop=True,
   body="LOCATION PLATE: Image 1 is this house's hall seen from the front door. This picture is THE SAME STAIRCASE seen from the hall tiles a few feet in from the front door, the camera turned to the left and tilted up the flight at standing eye height: the straight flight of fourteen equal steps of sage-green carpet with a brass stair rod on every tread climbs straight away from the camera to a small landing with a white door at the top. The cream stair wall with its white dado rail and the climbing row of small framed family photographs is on the LEFT of the flight; the open side with the dark-varnished wooden banister, plain turned spindles and the dark newel post is on the RIGHT, the bottom newel post big in the near right foreground. The red, black and cream hall tiles at the foot. Everything exactly as in Image 1, only seen up the stairs. True-to-life proportions, verticals straight. Named anchors, all fixed: the photographs on the left wall; the banister and newel posts on the right; fourteen steps; the white landing door at the top.",
   light=("A SMALL LANDING WINDOW OUT OF FRAME AT THE TOP OF THE STAIRS AND THE FRONT DOOR GLASS BEHIND THE CAMERA", "FRAME TOP", "soft, cool northern daylight", "3:1"), fg="the rounded top of the bottom newel post",
   extra_neg="no photographs on the right, no banister on the left, no curved or winding stairs, no wide-angle distortion, no fisheye, no bent verticals, no steps of different sizes"),
 "L-DINING": dict(f=24, stop="T5.6", prop=True,
   body="LOCATION PLATE: the front room of this house, used as the dining room, seen from its doorway off the hall. A long dark oak extending dining table with six ladder-back chairs, cleared after Sunday lunch: a cream tablecloth, a jug of water, two glasses, a folded napkin, a gravy-stained serving spoon on a plate. Along the left-hand wall a dark oak sideboard with a fruit bowl and framed photographs, faces too small to read; a tiled Victorian fireplace on the right-hand wall with a clock on the mantel; a sash bay window on the far wall with net curtains and green velvet curtains. A clear strip of oatmeal carpet runs between the chair backs and the sideboard, the length of the table. Named anchors, all fixed: the oak table and six ladder-back chairs; the oak sideboard on the left; the tiled fireplace on the right; the bay window.",
   light=("THE BAY WINDOW", "FRAME CENTRE", "soft, cool overcast daylight", "3:1"), fg="the stripped pine doorframe", view=EXTERIOR),
 "L-KITCHEN": dict(f=24, stop="T5.6", prop=True,
   body="LOCATION PLATE: the kitchen at the back of this house, seen from its doorway from the hall. A long galley kitchen: on the right, cream-painted wooden cupboards with brass cup handles and a worn wooden worktop, a white butler sink under the back window, a kettle and a tea caddy, a small radio; on the left, a small square pine table with two chairs against the wall and a wall calendar with blank squares; a cream range-style cooker at the far end; terracotta quarry tiles. A back door with a glass upper panel beside the window. Named anchors, all fixed: the white butler sink under the back window; the square pine table with two chairs on the left; the cream range cooker; the back door.",
   light=("THE BACK WINDOW OVER THE SINK", "FRAME CENTRE-RIGHT", "soft warm daylight from the south-west", "3:1"), fg="the stripped pine doorframe", view="a small stone-flagged back yard with pots of geraniums, a stone wall and the backs of the next row of terraces climbing the hill"),
 "L-BEDROOM": dict(f=24, stop="T5.6", prop=True,
   body="LOCATION PLATE: the front bedroom of this house, seen from its doorway off the landing. A double bed with a carved oak headboard and a duck-egg blue quilted bedspread against the left-hand wall, its near edge clear to sit on; a bedside table with a small lamp; on the right-hand wall a tall oak chest of five drawers with brass drop handles, its second drawer from the bottom a little proud where it does not quite shut; a matching oak wardrobe beside it; a sash window on the far wall with net curtains; oatmeal carpet. Named anchors, all fixed: the tall oak chest of drawers on the right, second drawer from the bottom not quite shut; the duck-egg blue bedspread; the oak wardrobe; the sash window.",
   light=("THE SASH WINDOW", "FRAME CENTRE", "soft, cool morning daylight through net curtains", "3:1"), fg="the edge of the open bedroom door", view=EXTERIOR),
 "L-CHEMIST": dict(f=28, stop="T4", prop=False,
   body="LOCATION PLATE: a small independent high-street chemist in a West Yorkshire town, seen from just inside the door: a white dispensing counter across the back with a till, a glass-fronted dispensary behind it; on the left-hand wall a tall rack of hooks hung with boxed knee supports, wrist splints and beige elastic knee sleeves in clear packets; low shelves of plasters and creams in the middle aisle; walking sticks standing in a tall stand by the counter; a grey speckled vinyl floor; the shop window on the right onto the street. Every label and sign blank or unreadable, no logos. Named anchors, all fixed: the rack of hooks with the beige knee sleeves on the left; the white counter with the till; the stand of walking sticks by the counter.",
   light=("THE SHOP WINDOW AND THE CEILING PANELS", "FRAME RIGHT", "cool white shop light mixed with overcast daylight from the window", "3:1"), fg="the edge of a low shelf of plasters"),
 "L-HILL": dict(f=32, stop="T5.6", prop=False,
   body="LOCATION PLATE: a steep residential street in a West Yorkshire mill town, seen from the pavement near the bottom, looking straight up the hill: two long rows of blackened gritstone terraced houses step up both sides of the street, their front doors opening straight onto the pavement; on the left, the pavement runs beside a waist-high gritstone wall topped with coping stones, and set into that wall exactly halfway up the hill is one red cast-iron pillar box; a few parked cars nose to tail on the right; the street climbs to a crest where green-painted school railings and the top of a tree show against the sky. Named anchors, all fixed: the waist-high stone wall on the left; the red pillar box in the wall halfway up; the gritstone terraces on both sides; the green railings at the crest.",
   light=("THE OPEN SKY", "FRAME TOP", "soft, even overcast morning daylight", "2:1"), fg="the coping stone of the wall at the bottom of the hill"),
 "L-GATE": dict(f=28, stop="T5.6", prop=False,
   body="LOCATION PLATE: the gate of a Victorian stone primary school at the top of a steep hill in a West Yorkshire town, seen from across the road: a gritstone school building with tall arched windows behind green-painted iron railings; a double green iron gate standing open onto a tarmac playground; a zig-zag yellow line painted along the kerb outside the gate; a pedestrian crossing point with dropped kerbs; a low stone wall with a bench beside the gate; the street falling away steeply downhill on the right of the frame. No signs with readable words, no logos. Named anchors, all fixed: the open green double gate; the green railings; the zig-zag yellow kerb line; the bench by the wall; the road dropping away downhill on the right.",
   light=("THE LOW SUN", "FRAME LEFT", "soft late-afternoon sunlight", "3:1"), fg="a green railing upright"),
 "L-CAR": dict(f=28, stop="T4", prop=False,
   body="LOCATION PLATE: inside a family hatchback parked at the kerb outside a primary school, seen from the back seat between the two front seats: the driver's seat on the right and the passenger seat on the left, both empty, grey fabric seats, a child's booster seat on the back seat beside the camera, a dashboard with a phone holder, the windscreen and the passenger window showing a green-railed school gate and the pavement just outside. British right-hand drive. Named anchors, all fixed: the empty passenger seat on the left; the steering wheel on the right; the school gate seen through the passenger window.",
   light=("THE WINDSCREEN AND SIDE WINDOWS", "FRAME CENTRE", "soft late-afternoon daylight", "3:1"), fg="the edge of the child's booster seat"),
}

def build(k, c):
    parts = [CAM(c["f"], c["stop"])]
    if c["prop"]:
        parts.append(S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", FINISHES) + " " + SHELL)
    parts.append(c["body"])
    if k == "P-HOUSE": parts[-1] += " A West Yorkshire hill-town house, lived in by the same couple for forty years."
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
