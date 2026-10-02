#!/usr/bin/env python3
"""§30G/§30C Mode 4 plates for facelove-my-mother (16:9, V7.68.1), strings pulled from Appendix A by ID.
Assembly: CAM-FILM (wide, tripod) → PLATE-PROP | PROP-REF + PROP-SHELL + room → VIEW-OUT → EMPTY → PROD-DEPTH → LIGHT-FILM → LOOK → PHYS-FRAME-C → CAP-FILM → negatives.
Wave 1 (no reference): P-HOUSE, L-YARD, L-GATHERING. Wave 2 (attached): L-VANITY (P-HOUSE), L-YARD-REV, L-PORCH-IN, L-HOSTS-FRONT (L-YARD). Wave 3: L-VANITY-REV (L-VANITY)."""
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
NEG_BASE = "no people, no person, no figures, no hands, no makeup stick or cosmetics product, no readable text, no signs with legible words, no logos, no brand names"
NEGP = S("NEG-PROP")

# Property Sheet field 2 — Susan's house, the shell named once, pasted verbatim
SHELL = S("PROP-SHELL").replace("[WALL FINISH AND COLOUR]", "warm greige eggshell paint on smooth drywall").replace(
  "[SKIRTING — profile, height, colour]", "plain white colonial baseboards about a hand high").replace(
  "[ARCHITRAVE]", "plain white colonial door casings").replace("[INTERNAL DOOR — style, colour, handle]", "white six-panel interior doors with brushed-nickel knobs").replace(
  "[CEILING]", "flat white ceilings with recessed can lights").replace("[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]", "honey-toned oak hardwood through the downstairs, changing to beige carpet on the stairs and in the bedrooms").replace(
  "[RADIATOR TYPE]", "no radiators, white metal floor vents").replace("[SWITCHES AND SOCKETS]", "white decora rocker switches and outlets")
FINISHES = "greige walls on smooth drywall, white colonial baseboards and casings, white six-panel doors with brushed-nickel knobs, honey oak floors downstairs and beige bedroom carpet"

PLATES = {
 "P-HOUSE": dict(f=24, stop="T5.6", prop=False, wave=1,
   body=S("PLATE-PROP").replace("[TYPE AND ERA]", "two-storey 1990s American suburban family").replace(
     "[WALL FINISH AND COLOUR]", "warm greige eggshell paint on smooth drywall").replace("[SKIRTING]", "plain white colonial baseboards about a hand high").replace(
     "[ARCHITRAVE]", "plain white colonial casings").replace("[INTERNAL DOOR AND HANDLE]", "white six-panel doors with brushed-nickel knobs").replace(
     "[CEILING]", "a flat white ceiling with recessed can lights").replace("[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]", "honey-toned oak hardwood running from the kitchen into the family room").replace(
     "[RADIATOR]", "white metal floor vents").replace("[SWITCHES AND SOCKETS]", "white decora rocker switches")
     + " The staircase rises along the left-hand wall, a straight flight of carpeted beige stairs with a white-painted banister and oak handrail on its open right-hand side, framed family photographs going up the stair wall, the faces too small to read. A narrow console table by the stairs with a bowl for keys. On the right, a wide open doorway into the open kitchen: white shaker cabinets with brushed-nickel pulls, speckled beige granite counters, the end of a granite kitchen island with a wooden bar stool, a stainless fridge, a window onto the back yard beyond.",
   light=("THE FRONT DOOR GLASS BEHIND THE CAMERA AND THE KITCHEN WINDOW BEYOND THE DOORWAY", "FRAME RIGHT", "soft, cool overcast morning daylight", "3:1"),
   fg="the painted edge of the open front door", view=None),
 "L-YARD": dict(f=24, stop="T5.6", prop=False, wave=1,
   body="LOCATION PLATE: the big back yard of a two-storey suburban family house at golden hour, laid out for an anniversary dinner party, seen from the far end of the lawn looking back toward the house. One long dinner table runs straight down the middle of the lawn toward the house — several trestle tables end to end under one long white linen cloth, about thirty mismatched wooden chairs along both sides, white plates, wine glasses, small glass candle holders, low jars of white garden roses, and in the very middle of the table one plain white rectangular sheet cake on a cake board, its top white frosting with no writing, uncut. Above the whole table, strings of warm bulb lights run in loose swags from the house to tall wooden posts on either side. Beyond the near end of the table, the back of the house, pale grey clapboard with white trim: a raised wooden deck with three steps up to it, white railings, and a back door with a glass pane in the middle of the deck; to the left of the steps, on the lawn, a small drinks table with a white cloth, bottles and an ice bucket. Mature trees and a tall green hedge close the yard on both sides. Named anchors, all fixed: the long white-clothed table down the middle of the lawn; the uncut white sheet cake in the middle of the table; the swags of warm bulb lights; the deck steps and the glass-paned back door; the drinks table left of the steps.",
   light=("THE LOW SUN BEHIND THE HOUSE AND THE WARM BULB LIGHTS", "FRAME LEFT, LOW", "warm golden-hour sunlight raking across the lawn from the left, the bulbs glowing", "3:1"),
   fg="the back of an empty wooden chair at the end of the table", view=None),
 "L-GATHERING": dict(f=24, stop="T4", prop=False, wave=1,
   body="LOCATION PLATE: the family room of a young couple's small rented house on a Sunday afternoon, laid out for a family birthday: a grey fabric sectional sofa against the back wall under a big window, a low wooden coffee table in front of it with a plain white birthday cake with no writing and a stack of paper plates, three bunches of plain pastel balloons tied to the sofa arm, a light wood floor with a cream rug, a bookshelf with plants on the left, an open doorway on the right through to a small kitchen. A clear stretch of floor between the coffee table and the camera, where a person would stand to take a family photo. Named anchors, all fixed: the grey sectional under the big window; the coffee table with the plain white birthday cake; the pastel balloons on the sofa arm; the bookshelf with plants on the left.",
   light=("THE BIG WINDOW BEHIND THE SOFA AND A SIDE WINDOW ON THE LEFT", "FRAME LEFT", "soft warm afternoon daylight", "3:1"), fg="the edge of a wooden dining chair", view=None),
 "L-HOSTS-FRONT": dict(f=32, stop="T4", prop=False, wave=2, ref="L-YARD",
   body="LOCATION PLATE: Image 1 is the back yard of this house, set for the party. This picture is the FRONT of the same two-storey suburban family house on a late summer afternoon, seen from across its quiet tree-lined street at the curb: a pale grey clapboard house with white trim, a red front door, a lawn and a concrete path to the door, a driveway on the right with three cars parked in a row and more cars along the curb; a bunch of plain white balloons tied to the mailbox post by the drive; a glow of string lights just visible over the side gate to the back yard, which stands half open. Named anchors, all fixed: the pale grey clapboard house with the red front door; the mailbox with white balloons; the half-open side gate with string lights beyond; the parked cars along the curb. No house numbers, no readable plates.",
   light=("THE LOW SUN BEHIND THE CAMERA", "FRAME RIGHT", "warm late-afternoon golden sunlight", "3:1"), fg="the edge of a parked car's side mirror", view=None),
 "L-VANITY": dict(f=28, stop="T4", prop=True, wave=2, ref="P-HOUSE",
   body="LOCATION PLATE: the main bedroom upstairs in this house, seen from the bedroom doorway. Against the right-hand wall, under a window, a white wooden dressing table with a large rectangular mirror fixed on top of it and a small upholstered stool tucked under it; on the dressing table a few plain unlabelled cosmetic jars and bottles, a hairbrush and a small ceramic dish, a pale wooden jewellery box; on the left, the end of a queen bed with a dusty-blue quilt and white pillows against the far wall; a tall chest of drawers beside the bed; sheer white curtains at the window over the dressing table. A clear space in front of the dressing table where two people can stand. Named anchors, all fixed: the white dressing table with the large rectangular mirror under the right-hand window; the small upholstered stool; the queen bed with the dusty-blue quilt; the sheer white curtains.",
   light=("THE WINDOW OVER THE DRESSING TABLE", "FRAME RIGHT", "soft warm daylight through sheer curtains", "2:1"), fg="the white-painted door casing", view="the front lawn and the maple tree across the street"),
 "L-VANITY-REV": dict(f=28, stop="T4", prop=True, wave=3, ref="L-VANITY",
   body="LOCATION PLATE: Image 1 is this bedroom seen from its doorway. This picture is THE SAME BEDROOM seen from the other side: the camera stands just behind the dressing-table stool, at seated eye height, looking past the dressing table's mirror edge across the room toward the bedroom door. Because we now look back the way Image 1 looked in, the room is reversed: the white six-panel bedroom door stands open in the middle of the far wall with the landing beyond; the end of the queen bed with the dusty-blue quilt is now on the RIGHT; the tall chest of drawers beside the bed; the near-left edge of frame is the white dressing table's corner and the edge of its mirror, the window's sheer curtain light falling from behind the camera. Everything exactly as in Image 1, only seen from the other side. Named anchors, all fixed: the open white bedroom door in the far wall; the bed with the dusty-blue quilt on the right; the corner of the white dressing table and mirror at near left.",
   light=("THE WINDOW BEHIND THE CAMERA OVER THE DRESSING TABLE", "FRAME LEFT, BEHIND", "soft warm daylight through sheer curtains", "2:1"), fg="the corner of the white dressing table and the mirror's edge", view=None,
   extra_neg="no different bed, no different door, no window on the far wall, no wide-angle distortion, no bent verticals"),
 "L-YARD-REV": dict(f=24, stop="T5.6", prop=False, wave=2, ref="L-YARD",
   body="LOCATION PLATE: Image 1 is this back yard seen from the far end of the lawn looking toward the house. This picture is THE SAME YARD seen from the other end: the camera stands on the wooden deck at the top of its three steps, beside the glass-paned back door, at standing eye height, looking straight down the long table toward the far end of the lawn. Because we now look back the way Image 1 looked in, the yard is reversed: the small drinks table with its white cloth is now at the near RIGHT, at the foot of the deck steps; the long white-clothed table runs away from us down the middle of the lawn, the about thirty mismatched wooden chairs along both sides, the same white plates, glasses, candle holders and jars of white roses, and the same plain white uncut sheet cake in the middle of the table; the same swags of warm bulb lights run from the house over our heads out to the tall wooden posts; at the far end, the tall green hedge and mature trees, the low sun sitting in the trees beyond. Everything exactly as in Image 1, only seen from the house. Named anchors, all fixed: the long table down the middle; the uncut white sheet cake; the bulb lights; the drinks table at near right; the hedge at the far end.",
   light=("THE LOW SUN IN THE TREES AT THE FAR END AND THE WARM BULB LIGHTS", "FRAME CENTRE, FAR, BACKLIGHT", "warm golden-hour backlight with the bulbs glowing overhead", "4:1"), fg="the white deck railing post", view=None,
   extra_neg="no drinks table on the left, no house at the far end, no different table, no cake with writing, no cut cake, no wide-angle distortion"),
 "L-PORCH-IN": dict(f=32, stop="T2.8", prop=False, wave=2, ref="L-YARD",
   body="LOCATION PLATE: Image 1 is this house's back yard with its deck and glass-paned back door. This picture is from INSIDE the house, in the dim back hall just inside that same back door, at dusk: the camera stands in the hall at standing eye height looking straight at the closed back door from inside. The white wooden door fills the middle of the frame, its upper half one glass pane through which the party glows outside — the warm swags of bulb lights over the long table, soft and out of focus, the deck railing just beyond the glass. Inside it is dark: a coat hook rail with two jackets on the left wall, a small bench with a pair of garden shoes under it, greige walls and an oak floor in deep shadow, a light switch beside the door. The only light in the hall is the warm party glow through the glass. Named anchors, all fixed: the white back door with the glass upper pane; the party bulb glow through the glass; the coat hooks and bench on the left.",
   light=("THE PARTY'S BULB LIGHTS OUTSIDE THE GLASS PANE", "FRAME CENTRE, BACKLIGHT", "warm amber glow through the glass, the hall in cool blue dusk shadow", "8:1"), fg="the dark edge of the hall wall", view=None,
   extra_neg="no lamp on in the hall, no ceiling light, no daylight, no open door"),
}

def build(k, c):
    parts = [CAM(c["f"], c["stop"])]
    if c["prop"]:
        parts.append(S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", FINISHES) + " " + SHELL)
    parts.append(c["body"])
    if c.get("view"):
        parts.append(S("VIEW-OUT").replace("[WHAT THE PROPERTY'S EXTERIOR SHOWS FROM THIS ROOM'S SIDE, NAMED]", c["view"]))
    parts += [EMPTY, DEPTH(c["fg"]), LIGHT(*c["light"]), LOOK, S("PHYS-FRAME-C"), CAPF]
    neg = [NEG_BASE] + ([c["extra_neg"]] if c.get("extra_neg") else []) + ([NEGP] if c["prop"] or k == "P-HOUSE" else []) + [NEGF, S("NEG-LIGHT")]
    parts.append("AVOID: " + ", ".join(neg) + ".")
    p = "\n\n".join(parts); assert "[" not in p, k
    return p

if __name__ == "__main__":
    out = {}
    for k, c in PLATES.items():
        out[k] = {"prompt": build(k, c), "wave": c["wave"], "ref": c.get("ref")}
        (HERE / f"{k}.prompt.txt").write_text(out[k]["prompt"]); print(k, c["wave"], c.get("ref"), len(out[k]["prompt"]))
    json.dump(out, open(HERE / "prompts.json", "w"), indent=1, ensure_ascii=False)
