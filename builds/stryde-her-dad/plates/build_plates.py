#!/usr/bin/env python3
"""§30G/§30C Mode 4 plates for stryde-her-dad (16:9, V7.68.1), strings pulled from Appendix A by ID.
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
SHELL = S("PROP-SHELL").replace("[WALL FINISH AND COLOUR]", "warm white emulsion over slightly uneven old plaster").replace(
  "[SKIRTING — profile, height, colour]", "tall ogee Victorian skirting gloss-painted white, scuffed").replace(
  "[ARCHITRAVE]", "plain white gloss architraves").replace("[INTERNAL DOOR — style, colour, handle]", "white-painted four-panel Victorian doors with brushed-steel lever handles").replace(
  "[CEILING]", "plain white ceilings").replace("[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]", "mid-grey wool-mix carpet through the hall, stairs, landing and bedrooms, changing to oak-effect laminate at the kitchen threshold").replace(
  "[RADIATOR TYPE]", "white steel panel radiators").replace("[SWITCHES AND SOCKETS]", "white plastic switches and sockets")
FINISHES = "warm white walls over old plaster, scuffed white Victorian skirting, four-panel white doors with steel levers, mid-grey carpet"
NEGP = S("NEG-PROP")
NOCAR = "no car badges, no manufacturer logos, no readable number plates"

PLATES = {
 "P-HOUSE": dict(f=24, stop="T5.6", prop=False,
   body=S("PLATE-PROP").replace("[TYPE AND ERA]", "Victorian two-up two-down red-brick terraced").replace(
     "[WALL FINISH AND COLOUR]", "warm white emulsion over slightly uneven old plaster").replace("[SKIRTING]", "tall ogee skirting gloss-painted white and scuffed").replace(
     "[ARCHITRAVE]", "plain white gloss architraves").replace("[INTERNAL DOOR AND HANDLE]", "white-painted four-panel Victorian doors with brushed-steel lever handles").replace(
     "[CEILING]", "a plain white ceiling with a simple white drum pendant shade").replace("[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]", "mid-grey wool-mix carpet down the narrow hall and up the stairs, changing to oak-effect laminate at the kitchen door at the far end").replace(
     "[RADIATOR]", "a white steel panel radiator on the hall wall").replace("[SWITCHES AND SOCKETS]", "white plastic switches, a little grubby round the edges")
     + " The hall is narrow, barely a metre wide. The staircase rises straight up along the right-hand wall, a steep, narrow flight of thirteen carpeted steps to a small landing, with a plain white-painted wooden handrail fixed to the left-hand side on a plain white balustrade of square spindles; the right-hand stair wall is bare except for one small framed print. At the foot of the stairs a row of coat hooks with a navy work jacket and a woman's camel coat, and a pair of tan leather work boots on the floor beneath. On the left, an open doorway into the front room shows the arm of a grey fabric sofa; at the far end of the hall the open kitchen door. A builder's house: everything straight, square and well made, nothing fancy.",
   light=("THE DAYLIGHT THROUGH THE FRONT DOOR GLASS BEHIND THE CAMERA AND THROUGH THE FRONT-ROOM DOORWAY", "FRAME LEFT", "soft, cool overcast daylight", "3:1"),
   fg="the painted edge of the open front door"),
 "L-STAIRS": dict(f=35, stop="T5.6", prop=True,   # v2 — user Fix: "revised the image besides is stares and on the right side looks the same floor" (v1 drew the front room at landing height beside the stairs)
   body="LOCATION PLATE: Image 1 is this house's hall and staircase seen from the front door. This picture is THE SAME STAIRCASE seen from the other end: the camera stands on the small upstairs landing at eye height, at the top of the flight, looking straight down the stairs toward the front door. Because we now look back the way the stairs climbed, the white handrail and white square spindles are on the RIGHT of the flight and the bare stair wall with its one small framed print is on the LEFT; the top newel post stands big in the near right foreground. A steep, narrow straight flight of thirteen equal steps of the same mid-grey carpet drops away from the camera down to the narrow hall a full storey below. ONE FLOOR ABOVE THE OTHER: to the right of the handrail there is no room and no floor at this height — only the open stairwell, a sheer drop past the spindles down to the hall carpet far below, and beyond the drop the plain white upper part of the hall wall rising past the ceiling of the floor beneath. Every door and room downstairs is seen only at the very bottom of the picture, at hall-floor level, a storey below the camera: the white front door with its frosted glass panel at the far end of the hall, daylight glowing through it; the coat hooks on the wall at the foot of the stairs; the open doorway into the front room down at the bottom on the right, at the hall's floor level, only its frame and a strip of its carpet visible. Nothing beside the top of the stairs is at the camera's height except the landing floor right under the camera. True-to-life proportions, verticals straight. Named anchors, all fixed: the white handrail and spindles on the right with the stairwell drop beyond them; the bare wall with one framed print on the left; the white front door with frosted glass at the bottom; the coat hooks at the foot.",
   light=("THE FRONT DOOR GLASS AT THE BOTTOM OF THE FLIGHT", "FRAME CENTRE, FAR", "soft, cool overcast daylight", "3:1"), fg="the square top of the newel post",
   extra_neg="no room beside the top of the stairs, no sofa or furniture at landing height, no doorway at the camera's height on the right, no second floor level beside the flight, no handrail on the left, no different front door, no landing window in frame, no wide-angle distortion, no fisheye, no bent or curving verticals, no stretched steps, no steps of different sizes"),
 "L-BEDROOM": dict(f=24, stop="T5.6", prop=True,
   body="LOCATION PLATE: the back bedroom, seen from the doorway from the landing. A double bed with a plain grey upholstered headboard and a navy duvet against the left-hand wall; beside it a pine bedside table with a small lamp; on the far wall, under a sash window, a low wide pine chest of drawers with plain wooden knobs, its top drawer pulled half open and packed full of soft knee supports bought from the chemist — beige pull-on knee sleeves, a black neoprene knee support with a hole for the kneecap, a rolled elastic bandage, a strip of painkillers and a tube of gel; a white built-in wardrobe on the right-hand wall; plain grey curtains. Named anchors, all fixed: the low wide pine chest of drawers under the window with its top drawer half open and full of soft knee supports; the grey headboard and navy duvet; the white wardrobe.",
   light=("THE SASH WINDOW OVER THE CHEST OF DRAWERS", "FRAME CENTRE", "soft cool evening daylight, the bedside lamp switched on and warm", "4:1"), fg="the edge of the open bedroom door", view="the back gardens and the backs of the terrace opposite"),
 "L-KITCHEN": dict(f=24, stop="T4", prop=True,
   body="LOCATION PLATE: the narrow galley kitchen at the back of the house at night, seen from the doorway from the hall. Shaker-style cream units with oak worktops along both walls, a white butler sink under the back window, a small round oak table with two chairs at the far end by a glazed back door onto the garden, a fruit bowl and a stack of post on the table; a warm glass pendant light hangs over the table; the window is dark blue night. Named anchors, all fixed: the small round oak table with two chairs by the glazed back door; the cream shaker units with oak worktops; the white butler sink under the back window; the pendant light over the table.",
   light=("THE GLASS PENDANT OVER THE TABLE", "FRAME TOP", "warm tungsten pendant light at night with cool blue night through the windows", "4:1"), fg="the white-painted doorframe", view="the dark back garden"),
 "L-GARDEN": dict(f=24, stop="T5.6", prop=False,
   body="LOCATION PLATE: the long narrow back garden of a Victorian red-brick terraced house, seen from the back door: a newly laid patio of pale sandstone flags filling the near half of the garden, half of it finished and half still a bed of levelled sand and mortar with a stack of new sandstone slabs on a pallet, a builder's spirit level, a rubber mallet, a pointing trowel and a bucket beside them; beyond, a strip of lawn, raised timber beds, a shed at the end and a brick wall and fence on each side, the backs of the neighbouring terraces. Named anchors, all fixed: the half-laid pale sandstone patio and the pallet of new slabs; the spirit level and rubber mallet; the shed at the end of the lawn.",
   light=("THE LOW SUN FROM THE WEST OVER THE LEFT-HAND WALL", "FRAME LEFT", "warm, low late-afternoon sun with long soft shadows", "3:1"), fg="the edge of the back-door step"),
 "L-CARPARK": dict(f=24, stop="T5.6", prop=False,
   body="LOCATION PLATE: the open-air car park of a garden centre on the edge of a Kent town on an ordinary weekday, seen standing between the parked cars: wet grey tarmac with faded white bay lines, a row of parked ordinary family cars, a silver five-door hatchback in the near bay with its boot open and a few potted plants and a bag of compost inside; a plain white panel van parked two bays along with its back doors toward the hatchback; the low glass-and-green-steel front of the garden centre behind with racks of plants, trolleys and stacked terracotta pots outside, a trolley bay, young trees in tubs. Named anchors, all fixed: the silver hatchback with its boot open in the near bay; the white panel van two bays along, its back toward the hatchback; the garden centre's glass front with the racks of plants; the trolley bay. All signs blank, no readable words.",
   light=("THE OVERCAST SKY", "FRAME TOP", "flat, cool grey overcast daylight", "2:1"), fg="the edge of a trolley in the trolley bay", extra_neg=NOCAR),
 "L-CAR": dict(f=28, stop="T4", prop=False,
   body="LOCATION PLATE: inside an ordinary ten-year-old five-door hatchback parked in a car park, seen from the middle of the back seat looking forward between the two front seats: two cloth front seats in charcoal grey, an empty driver's seat on the right (a British right-hand-drive car) and an empty passenger seat on the left, the steering wheel, a plain dashboard with no screen lit, a parking ticket and a pair of sunglasses on the dash, the windscreen showing the grey car park and the green front of a garden centre beyond. Named anchors, all fixed: the charcoal cloth front seats; the steering wheel on the right; the windscreen onto the car park.",
   light=("THE WINDSCREEN AND SIDE WINDOWS", "FRAME CENTRE", "flat, cool overcast daylight from all the glass", "3:1"), fg="the headrest of the passenger seat", extra_neg=NOCAR),
 "L-GP": dict(f=24, stop="T4", prop=False,
   body="LOCATION PLATE: an NHS GP's consulting room in a 1990s health centre in Kent, seen from the door: a plain desk against the left-hand wall with a computer monitor turned away, a keyboard and a blood-pressure cuff, a black office chair at the desk and a padded patient chair beside it at the desk's corner; a blue examination couch with a paper roll along the far wall under a window with vertical blinds half open; a sink with a paper-towel dispenser; a pinboard of leaflets too small to read; pale blue-grey walls, grey speckled vinyl floor. Named anchors, all fixed: the desk on the left with the patient chair at its corner; the blue examination couch under the window; the vertical blinds; the sink.",
   light=("THE WINDOW WITH VERTICAL BLINDS AND THE CEILING PANEL LIGHT", "FRAME CENTRE-RIGHT", "cool, flat daylight mixed with white overhead panel light", "3:1"), fg="the edge of the open door"),
 "L-YARD": dict(f=24, stop="T5.6", prop=False,
   body="LOCATION PLATE: a builders' merchant's yard in Kent on a working morning, seen from the yard gate: a concrete yard with puddles, steel racking stacked with bagged sand and cement in plain bags, pallets of grey concrete paving slabs and stacked kerbs in the foreground, a pallet of pale sandstone flags, a forklift parked under an open-sided steel shed at the back, a white flatbed truck loaded with bricks, a portable cabin office with a window. Named anchors, all fixed: the pallets of grey paving slabs in the foreground; the open-sided steel shed with the parked forklift; the white flatbed truck with bricks; the portable cabin office. Every bag and sign plain with no readable words, no logos.",
   light=("THE BRIGHT OVERCAST SKY", "FRAME TOP", "bright, soft overcast daylight", "2:1"), fg="the corner of a pallet of paving slabs", extra_neg=NOCAR),
 "L-STREET": dict(f=24, stop="T5.6", prop=False,
   body="LOCATION PLATE: a long straight street of Victorian red-brick two-up two-down terraced houses in a Kent town, seen from the pavement outside one front door: small front walls and gates, bins in the tiny front yards, cars parked nose to tail along both kerbs, the terrace running away in perspective on both sides, a few street trees, a red post box on the corner far down. Named anchors, all fixed: the run of red-brick terraced fronts with white sash windows and front doors opening straight off the pavement; the low brick front walls; the cars parked along both kerbs; the red post box on the far corner.",
   light=("THE LOW MORNING SUN DOWN THE STREET", "FRAME RIGHT", "soft, warm low morning sun", "3:1"), fg="a low brick front wall and gate post", extra_neg=NOCAR),
}

def build(k, c):
    parts = [CAM(c["f"], c["stop"])]
    if c["prop"]:
        parts.append(S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", FINISHES) + " " + SHELL)
    parts.append(c["body"])
    if k == "P-HOUSE": parts[-1] += " A Kent working town's terraced house, lived in by the same couple for thirty years."
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
