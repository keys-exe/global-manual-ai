#!/usr/bin/env python3
"""stryde-71-stairs — B-roll T2I seeds (step 7), Mode 1 candid seeds (§22T) with the §30I–§30K lines.

Order: CAM-LOCK → ANGLE-LINE → FOCUS-LINE → PROP-REF (rooms of her house, plate attached) → the moment in plain prose
(subject + markers, the clothes she has on, what she is doing caught mid-action per §27G, the room in one sentence) →
REF-PROD where the product appears → LIGHT-SHOT → CAP-FILE → AVOID (NEG-FILE + selected NEG-M1 + beat negatives).
Refs are local files (uploaded to the image route at generation). Model per the act map (NB2 → nano_banana_2).
Usage: broll.py P-01a P-01b …   → work/prompts/<beat>.t2i.txt + <beat>.refs.json
"""
import json, sys, pathlib
from beats import S, ROWS, SUBJ, PROP_N_CARRIED, angle_line, focus_line, light_line

HERE = pathlib.Path(__file__).parent
B = HERE.parent
REF = {
 "N": B / "cast/N-NARR_v1.png", "C1": B / "cast/C1-LORETTA_v1.png", "C2": B / "cast/C2-DAUGHTER_v1.png",
 "P0": B / "plates/P0-PROP-N_v3.png", "P1": B / "plates/P1-LANDING_v5.png", "P2": B / "plates/P2-KITCHEN_v2.png",
 "P3": B / "plates/P3-RECEPTION_v2.png", "P4": B / "plates/P4-STORE_v4.png", "P5": B / "plates/P5-CHURCH_v2.png",
 "P6": B / "plates/P6-STREET_v2.png", "P7": B / "plates/P7-CLINIC_v2.png", "P8": B / "plates/P8-MALL_v4.png",
}
MODEL = {"NB2": "nano_banana_2", "NBP": "nano_banana_pro", "GPT": "gpt_image_2_5"}
WARD = {   # one outfit per story day / event (wardrobe map, STEP4_5.md) — no two days share a top or a dress
 "N-D1":  "a faded blue floral house dress falling to the knee, a grey cardigan and pink terry slippers",
 "N-D1b": "a burgundy velour zip-up tracksuit jacket with matching trousers and white sneakers",
 "N-D1c": "a mustard-yellow long-sleeve cable-knit sweater, black stretch trousers and brown moccasin slippers",
 "N-D1d": "a navy-and-white striped button-up blouse, a knee-length navy skirt and black flats",
 "N-D1e": "an olive-green long-sleeve knit top, charcoal stretch trousers and brown moccasin slippers",
 "N-D7":  "a lilac long-sleeve cotton top",
}
SHEET_DAYS = {"N-TODAY", "C1-D3"}   # the days the cast sheet's own outfit is worn
N = SUBJ["N"]
M1 = ("no AI face, no plastic skin, no waxy skin, no extra fingers, no fused fingers, no melted hands, no deformed limbs, "
      "no warped background, no CGI look, no fake commercial gloss, no over-saturated colors, no vignette, no moody dark grade")
GREY = "a grey, overcast morning — flat, cool daylight, the problem days, plain and unflattering but never dark"
KITCH = "the same kitchen as the attached kitchen photo — cream vinyl tile, oak cabinets, the round table under the south window"
CLINIC = "the same exam room as the attached clinic photo — the padded table with its paper roll, the half-open blind, pale blue-grey walls"

def prop_ref():
    return S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", PROP_N_CARRIED)

def seed(beat, subject_word, focus_name, prose, light_subject, quality, neg, refs, house=True, side=None, through=None, height=None):
    r = dict(ROWS[beat]); r["angle"] = dict(r["angle"])
    if side: r["angle"]["side"] = side          # the act-map side word, corrected where it contradicts the staging
    if height: r["angle"]["height"] = height
    a = angle_line(r, subject_word)
    if through: a = a.replace("looking past the white balusters", "looking past " + through)
    lt = light_line(r, light_subject, quality)
    if not r.get("face"):                        # no face in frame: the light line keeps the source and direction only
        lt = lt.replace(", so the face has a lit side toward " + {"L": "left", "R": "right", "back": "back", "front": "front"}[r["light"]["key_side"]] + " and a softer shadow side, with a small catchlight in the eyes", "")
    body = [S("CAM-LOCK"), a, focus_line(r, focus_name)]
    if house: body.append(prop_ref())
    day, subj = r["story_day"], r["subject"]
    txt = " ".join(prose)
    if subj.startswith("N") and day in WARD and WARD[day] not in txt:
        txt += (" Her clothes today: " + WARD[day] + " — only as much of them as the frame shows.")
    if day not in SHEET_DAYS:   # face and hair from the sheet, never its clothes (user 2026-09-29: same wardrobe on every day)
        txt = txt.replace("exactly as in her attached reference sheet", "her face, hair and build exactly as in her attached reference sheet, but not the clothes she wears on the sheet")
        if "reference sheet" in txt:
            neg += ", no outfit copied from the reference sheet, no cream open cardigan over a coral top, no plum blouse with khaki trousers"
    body.append(txt)
    body += [lt, S("CAP-FILE"),
             "AVOID: " + ", ".join([S("NEG-FILE"), M1, neg])]
    return dict(model=MODEL[r["model"]], refs=refs, body=body)

BEATS = {}

# ---------------------------------------------------------------- Act 1 — the problem days (N-D1, grey mornings)
def p_01a():   # Fix 2 2026-09-29: "she should be looking up the stairs and both her hands at the railing stepping down backwards slowly and struggling"
    return seed("P-01a", "her on the stairs", "her", [
      "Her staircase, exactly as in the attached hall photo: the straight open flight with the full-width oatmeal-beige stair carpet and its brass stair rods, the white balusters and dark oak handrail, the photo wall of small dark-framed family portraits. "
      "Seen from the hall floor near the foot of the stairs, from the side and a little behind her, the way the hall photo sees the flight. A woman of seventy-one — " + N["markers"] + ", exactly as in her attached reference sheet — is four steps up, "
      "going DOWN her stairs BACKWARDS, the way people do when the knees can't take it: her whole body faces UP the stairs toward the landing — chest, knees and the toes of both slippers pointing UP the flight, her back and her heels toward the hall below. "
      "She is LOOKING UP THE STAIRS, her face in profile turned toward the top of the flight. BOTH her hands grip the dark oak handrail beside her, one hand a little above the other, knuckles tight, her arms taking her weight. "
      "Caught mid-step, slow and struggling: her right leg reaching DOWN BEHIND her, the heel of that slipper feeling for the step below, toes still pointing up the stairs; her left foot flat on the step above carrying her, that knee bent and stiff, "
      "her shoulders hunched, her jaw set. "
      "She is wearing " + WARD["N-D1"] + ". The hall is dim; nothing tidied."],
      "her and the stairs", GREY,
      "no facing down the stairs, no walking forwards down the stairs, no toes pointing down the stairs, no looking down the stairs toward the camera, no hand off the handrail, no hands at her sides, no fast movement, no stumbling, no fall, no one else on the stairs, no stairlift, no walking stick, no knee brace, no product, no smiling, no different staircase from the hall photo, no turn in the stairs, no narrow runner",
      [("N sheet", REF["N"]), ("P0-PROP-N plate", REF["P0"])], side="three-quarter-back", height="eye")
BEATS["P-01a"] = p_01a

def p_01b():   # Fix 2 2026-09-29: "she should show one step at a time same step both feet"
    return seed("P-01b", "her feet on the stairs", "her feet", [
      "Close on the stairs from the side, the lens at the height of the steps, halfway up the flight: the full-width oatmeal-beige stair carpet with its brass stair rods, several steps above her and more steps below her, "
      "a white baluster and the dark oak handrail at the edge of the frame. She is in the MIDDLE of the staircase, nowhere near the bottom — no hall floor in frame. "
      "She is going down backwards, one step at a time: BOTH her feet stand TOGETHER, side by side, on ONE AND THE SAME step — both pink terry slippers on the same tread, touching each other, "
      "their toes pointing UP the stairs and their heels at the front edge of the tread, toward the drop below. The step below them is empty, the step above them is empty. "
      "Bare brown ankles, the hem of a faded blue floral house dress just in frame above them. Caught in the pause between steps, her weight settling on both feet. Only her feet, ankles and the hem in frame."],
      "her feet and the steps", GREY,
      "no feet on two different steps, no one foot higher than the other, no mid-stride, no toes pointing down the stairs, no full body, no face, no hall floor, no bottom of the stairs, no fast movement, no stumbling, no bare feet, no shoes, no knee brace, no product, no narrow runner, no different carpet from the hall photo",
      [("P0-PROP-N plate", REF["P0"])])
BEATS["P-01b"] = p_01b

def p_02a():   # Fix 2026-09-29: "camera angle at her back and she just looking at the stairs then just leaves cause she dont want to go down"
    return seed("P-02a", "her at the top of the stairs", "everything", [
      "Her staircase, exactly as in the attached landing and hall photos. Seen from behind her on the top landing: she — " + N["markers"] + ", exactly as in her attached reference sheet — "
      "stands at the head of the stairs with her back to the camera, the whole straight flight dropping away below her: the full-width oatmeal-beige stair carpet with its brass stair rods, the dark oak handrail, the photo wall of family portraits running down on the left, "
      "the front door closed at the bottom and the hall below dim. She has been looking down the stairs and has given up: caught just as she turns away from them, "
      "her shoulders sagging, her weight shifting back onto the landing, one hand letting go of the newel post, her head still half toward the drop. Her feet stay on the landing; she does not step down. "
      "She is wearing " + WARD["N-D1"] + ". A strip of grey light from the landing window lies across the top steps."],
      "her and the staircase", GREY,
      "no face to camera, no stepping down, no one else, no open door, no bright sunlight, no different staircase from the landing and hall photos, no turn in the stairs, no knee brace, no product",
      [("N sheet", REF["N"]), ("P1-LANDING plate", REF["P1"]), ("P0-PROP-N plate", REF["P0"])])
BEATS["P-02a"] = p_02a

def p_03a():
    return seed("P-03a", "her right knee", "her hands", [
      "Close on her lap at the kitchen table, " + KITCH + ", looking down the way she sees it herself. "
      "Her right knee is bare, the hem of her faded blue floral house dress pushed up above it. A black hinged knee brace with metal side hinges and velcro straps, an ordinary unbranded one, "
      "has slid down her leg and sags below the kneecap. Caught mid-pull: both her hands grip the top of the brace and are hauling it back up, the fabric bunching and the straps twisted, the brace already starting to slip again. "
      "Deep brown skin on her knee and hands, fine creases, a plain wedding band. The day's clothes all show: the grey cardigan sleeves pushed to her forearms, the faded blue floral house dress, "
      "and her feet in pink terry slippers on the cream tile. The brace is the SAME black hinged knee brace as in the attached brace photo — identical fabric, hinges, straps, size and shape."],
      "her knee and hands", GREY,
      "no face, no bare feet, no missing cardigan, no different brace from the brace photo, no logo on the brace, no brand name, no readable text, no knee strap, no product, no bandage, no swelling, no injury, no hands inside the brace",
      [("N sheet", REF["N"]), ("P2-KITCHEN plate", REF["P2"]), ("P-03a brace photo (v1)", "job:5948917d-e509-41ad-a4f4-a524887d3a9e")])   # Fix 2026-09-29 (user: "fix the p03a too"): the day's full outfit, same brace
BEATS["P-03a"] = p_03a

def p_03b():
    return seed("P-03b", "her right ankle", "the brace around her ankle", [
      "Close to the floor of her kitchen, " + KITCH + ", the lens a few centimetres above the cream vinyl tile under the table. "
      "Her right foot in a pink terry slipper, and above it the SAME black hinged knee brace as in the attached brace photo — identical: the same black fabric, the same metal side hinges, the same velcro straps, the same size and shape — has slid all the way down her leg and sits bunched around her ankle, twisted, its velcro straps hanging loose. "
      "The hem of her faded blue floral house dress and her bare calf in frame. Caught as she shifts her foot a little on the tile. Evening: the light is low and fading."],
      "her foot and ankle", "the last low daylight of the evening, dimmer and warmer than the morning, still plain",
      "no face, no different brace from the brace photo, no sleeve instead of the brace, no logo on the brace, no readable text, no knee strap, no product, no injury, no swelling",
      [("N sheet", REF["N"]), ("P2-KITCHEN plate", REF["P2"]), ("P-03a brace photo (confirmed)", "job:5948917d-e509-41ad-a4f4-a524887d3a9e")])
BEATS["P-03b"] = p_03b   # Fix 2026-09-29: "this should be the same as the brace of the p03a"

def p_04a():
    return seed("P-04a", "her on the treatment table", "the therapist's hands on her knee", [
      "In a physical therapy exam room, " + CLINIC + ". She lies on her back on the padded table — " + N["markers"] + ", exactly as in her attached reference sheet — "
      "in " + WARD["N-D1b"] + ", the right trouser leg rolled up above the knee, her head on the paper-covered pillow, looking at the ceiling, patient and tired. "
      "A physical therapist in navy scrubs, only his forearms and hands and the side of his torso in frame, holds her right leg: one hand under her calf, one on the front of her bare knee. "
      "Caught mid-bend: her right knee is bent to about ninety degrees and he is easing it a little further."],
      "her and the therapist's hands", "even afternoon daylight through the half-open blind, clinical and plain",
      "no therapist's face, no second patient, no machines, no readable text, no posters with words, no knee strap, no product, no smiling, no pain grimace",
      [("N sheet", REF["N"]), ("P7-CLINIC plate", REF["P7"])], house=False)
BEATS["P-04a"] = p_04a

def p_04b():
    return seed("P-04b", "the kitchen table", "her hand and the pills", [
      "Looking straight down at her kitchen table, " + KITCH + ": three orange prescription pill bottles with white caps and plain white labels with no readable writing, a silver blister pack half used, "
      "a white coffee mug with a ring of cold coffee, reading glasses, the worn wood of the table. Her left hand — deep brown skin, a plain wedding band, the ribbed cuff of her mustard-yellow cable-knit sweater at the wrist — is cupped open and her right hand tips one bottle over it: "
      "caught as two small white tablets drop into her palm."],
      "her hands and the table", GREY,
      "no face, no readable labels, no brand names, no text, no knee strap, no product, no spilled pills everywhere",
      [("N sheet", REF["N"]), ("P2-KITCHEN plate", REF["P2"])])
BEATS["P-04b"] = p_04b

def p_04c():
    return seed("P-04c", "her right knee and the doctor's hands", "the needle and the gloved hands", [
      "Close on her bare right knee from the side, on the paper-covered exam table of " + CLINIC + ". Her skin deep brown, the hem of her knee-length navy skirt pushed up above the knee, the striped blouse cuff of her resting hand just in frame, a fresh wipe of antiseptic shining on the outer side of the knee. "
      "A doctor's hands in blue nitrile gloves hold a small syringe with a clear barrel horizontally against the side of her knee; the other gloved hand steadies the joint. "
      "Caught as the needle tip meets the skin, the plunger not yet pressed. The room behind is soft."],
      "her knee and the gloved hands", "even afternoon daylight through the half-open blind, clinical and plain",
      "no face, no blood, no bruise, no graphic injection, no needle through the skin, no readable text on the syringe, no knee strap, no product",
      [("N sheet", REF["N"]), ("P7-CLINIC plate", REF["P7"])], house=False)
BEATS["P-04c"] = p_04c

def p_04d():
    return seed("P-04d", "the pile of braces", "her hand and the pile", [
      "From above at a three-quarter angle, a corner of her kitchen table, " + KITCH + ": a heap of knee braces and sleeves she has given up on — a black hinged brace, two beige elastic sleeves, "
      "a blue neoprene sleeve with a hole for the kneecap, a padded wrap with velcro — all ordinary and unbranded, tangled together. "
      "Her hand, deep brown skin with a plain wedding band, the cuff of her olive-green long-sleeve knit top at the wrist, has just let go of one more grey elastic sleeve: caught mid-drop, a few centimetres above the pile."],
      "her hand and the pile", GREY,
      "no face, no logos, no brand names, no readable text or labels, no knee strap, no product, no new-looking packaging",
      [("N sheet", REF["N"]), ("P2-KITCHEN plate", REF["P2"])])
BEATS["P-04d"] = p_04d

def p_05a():
    return seed("P-05a", "her at the kitchen table", "her", [
      "Seen from the next room through the open kitchen doorway, the white casing soft at the edge of the frame: " + KITCH + ". "
      "She sits alone at the table in profile — " + N["markers"] + ", exactly as in her attached reference sheet — in " + WARD["N-D1e"] + ", "
      "among orange pill bottles, a heap of knee braces and sleeves and a mug of cold coffee, her hands in her lap, looking at nothing out of the window. "
      "Caught mid-breath: a long breath out, her shoulders dropping."],
      "her", GREY,
      "no smiling, no crying, no tears, no looking at the camera, no second person, no knee strap, no product, no bright sunlight",
      [("N sheet", REF["N"]), ("P2-KITCHEN plate", REF["P2"]), ("P0-PROP-N plate", REF["P0"])], through="the white casing of the open kitchen doorway")
BEATS["P-05a"] = p_05a


# ---------------------------------------------------------------- shared: wardrobe, cast, product, anatomy
import sys as _sys
_sys.path.insert(0, str(B.parents[1] / "products/stryde"))
import stryde_product_sheet as PS
WARD.update({
 "N-D3": "a rose-pink short-sleeve blouse, a knee-length denim skirt and tan house slippers",
 "N-D4": "an emerald-green church dress falling to mid-calf, a matching wide-brim hat and low black pumps",
 "N-D5": "a pale-yellow cotton nightgown falling to the knee",
 "N-D6": "a coral windbreaker over a white T-shirt, light-blue straight jeans and white walking sneakers",
 "N-TODAY": "a cream open cardigan over a coral top and small gold stud earrings",
 "C1-D2": "a royal-blue satin dress to the knee and white slip-on sneakers for dancing",
 "C1-D3": "a plum-coloured blouse with a small collar, loose khaki cotton trousers and white canvas slip-on sneakers",
})
C1 = dict(markers="a short silver-white natural curly crop, a long oval face with high sharp cheekbones, a thin pale scar through the middle of her right eyebrow, tall and lean and straight-backed",
          skin="a Black American woman of seventy-four, medium-brown skin, long creases on the cheeks, a scatter of dark spots along the cheekbones")
REF.update({"PF": B.parents[1] / "products/stryde/stryde_refs/front.webp", "PB": B.parents[1] / "products/stryde/stryde_refs/back.webp",
            "WORN": "job:f5263ed7-0667-4ebd-977e-9bfd835d5036", "BENT": "job:8a8979ac-9eb1-4398-b41b-eea793a99a26",
            "BOX": B.parents[1] / "products/stryde/stryde_refs/package_open.jpg"})
PR_REFS = {"worn": [("STRYDE front", "PF"), ("STRYDE back", "PB"), ("STRYDE worn (front)", "WORN")],
           "bent": [("STRYDE front", "PF"), ("STRYDE back", "PB"), ("STRYDE worn (bent)", "BENT")],
           "held": [("STRYDE front", "PF"), ("STRYDE back", "PB")],
           "box":  [("STRYDE front", "PF"), ("STRYDE box open", "BOX")]}
def R(*keys): return [(k, REF[v]) for k, v in keys]
REF_PROD = PS.fill(PS.REF_PROD, "right").rstrip(" —")
PNEG = ("no strap on the left knee, no strap over the kneecap, no strap low on the shin, no blank shell, no misplaced wordmark, no velcro, no buckle, "
        "no silicone look, no glossy shell, no second strap unless stated, no product changing shape")
def prod(kind):
    if kind == "worn":   return REF_PROD + ". " + PS.fill(PS.PLACE_LOCK_C, "right")
    if kind == "bent":   return REF_PROD + ". " + PS.fill(PS.PLACE_BENT, "right") + " " + PS.fill(PS.WORDMARK_LOCK, "right")
    if kind == "held":   return REF_PROD + ". " + PS.fill(PS.SIZE_HELD, "right") + " " + PS.fill(PS.WORDMARK_LOCK, "right")
    if kind == "hidden": return "She wears the strap on her right knee under her clothes; it is completely hidden and nothing of it shows."
MID = "a clear spring afternoon — warm, bright daylight, the after days, never moody"
MORN = "a bright, fresh morning — clean daylight, the after days"
STAIRS_SUN = "Sunday-style afternoon sun through the front door's sidelights, warm and clear — the after state, never moody"

def anat(beat, state, extra, prod_in=False, neg=""):
    r = ROWS[beat]
    sl = dict(PS.SLOTS)
    f = lambda t: (t.replace("[REGION]", "right knee, from mid-thigh to mid-shin, the leg upright").replace("[TARGET JOINT]", sl["TARGET_JOINT"])
                    .replace("[STACK]", sl["STACK"]).replace("[BONES]", "The " + sl["BONES"]).replace("[TARGET]", sl["TARGET"]).replace("[SITE]", sl["SITE"]))
    body = [f(S("ANAT-BASE")), f(S("ANAT-LIGHT")), S("ANAT-FIELD"), f(S("ANAT-A")), f(state), extra]
    refs = []
    if prod_in:
        body.append(REF_PROD + ". " + S("ANAT-PROD"))
        refs = R(*PR_REFS["worn"])
    ang = r["angle"]
    body.append("Seen from a " + {"eye": "level", "low": "low", "high": "high"}.get(ang["height"], "level") + " " + {"profile": "side-on profile", "three-quarter": "three-quarter", "front": "front"}.get(ang["side"], "three-quarter") + " angle.")
    body.append("AVOID: " + f(S("ANAT-NEG")).replace("no sleeve, ", "" if "sleeve" in extra else "no sleeve, ") + (", " + neg if neg else ""))
    return dict(model=MODEL[r["model"]], refs=refs, body=body)
HOT = lambda col: "STATE — the patellar tendon just below the kneecap is under load and already glowing " + col + " at one tight spot. " + PS.ANAT_A_POINT_TIGHT
CALM = "STATE — " + S("ANAT-REST")

# ---------------------------------------------------------------- Act 2 — the wedding (N-D2, evening, tungsten)
RECEP = "the same reception hall as the attached reception photo — round tables in white cloths, gold chairs, string lights and crystal chandeliers, a parquet dance floor, a gold balloon arch"
PARTY = "warm tungsten party light from the string lights and chandeliers, evening"
def t_01a(): return seed("T-01a", "the bride", "the bride", [
    "At a Black American wedding reception in June, " + RECEP + ". The bride — a young Black woman in her twenties in a white dress, her hair up — sits at a reception table with guests around her, "
    "caught mid-laugh, her head thrown back, one hand on the arm of the woman beside her; glasses, a half-eaten slice of cake, a phone face-down on the cloth. Nobody looks at the camera."],
    "the bride and the guests", PARTY, "no posing, no looking at the camera, no professional wedding photography look, no flash, no knee strap, no product, no readable text",
    R(("P3-RECEPTION plate", "P3")), house=False)
BEATS["T-01a"] = t_01a
def t_01b(): return seed("T-01b", "Loretta", "Loretta", [
    "At the same reception, " + RECEP + ". Loretta — " + C1["markers"] + ", exactly as in her attached reference sheet — stands at the edge of the dance floor in " + WARD["C1-D2"] + ", "
    "caught mid-clap on the beat, both hands meeting in front of her chest, grinning, her eyes on the dancers off-frame; guests blurred behind her. " + C1["skin"].capitalize() + "."],
    "Loretta", PARTY, "no looking at the camera, no knee strap visible, no product, no flash, no readable text",
    R(("C1 sheet", "C1"), ("P3-RECEPTION plate", "P3")), house=False)
BEATS["T-01b"] = t_01b
def t_02a(): return seed("T-02a", "the line of dancers", "everything", [
    "The dance floor at the same reception, " + RECEP + ", seen past the backs of two chairs. A line of about eight guests — Black Americans of every age in their wedding clothes — is doing a line dance in step, "
    "and Loretta — " + C1["markers"] + ", exactly as in her attached reference sheet, in " + WARD["C1-D2"] + " — is in the middle of the line, caught mid side-step with the others, arms loose, laughing. Her knees are covered by her dress."],
    "the dancers", PARTY, "no posed group, no looking at the camera, no knee strap visible, no product, no flash, no readable text",
    R(("C1 sheet", "C1"), ("P3-RECEPTION plate", "P3")), house=False, through="the backs of two gold chairs")
BEATS["T-02a"] = t_02a
def t_02b(): return seed("T-02b", "the dancing feet", "the feet", [
    "Close to the parquet dance floor of the same reception, the lens a few centimetres above the floor: a row of dancing feet — heels, loafers, dress shoes, and Loretta's white slip-on sneakers among them — "
    "caught mid-step as the whole line steps back together, hems and trouser cuffs swinging, string lights soft in the background."],
    "the feet", PARTY, "no faces, no bare feet, no knee strap, no product, no readable text",
    R(("P3-RECEPTION plate", "P3")), house=False)
BEATS["T-02b"] = t_02b
def t_03a(): return anat("T-03a", HOT("a hot red"),
    "The joint surfaces inside the knee are worn thin — bone close to bone, the cartilage almost gone, rough and pale at the contact — and the tight red spot sits on the tendon just below the kneecap, pulsing once.")
BEATS["T-03a"] = t_03a

# ---------------------------------------------------------------- Act 3 — Loretta's visit and the first stairs (N-D3a / N-D3)
def r_01a(): return seed("R-01a", "Loretta at the front door", "Loretta", [
    "Her hall, exactly as in the attached hall photo, seen from inside looking at the open front door. Loretta — " + C1["markers"] + ", exactly as in her attached reference sheet — in " + WARD["C1-D3"] + ", "
    "is stepping in over the threshold with a small overnight bag in one hand, caught mid-step, one foot on the hall floor, smiling at someone inside; afternoon light behind her through the door."],
    "Loretta", "afternoon daylight through the open door and the sidelights, warm and clear", "no looking at the camera, no suitcase on wheels, no knee strap visible, no product",
    R(("C1 sheet", "C1"), ("P0-PROP-N plate", "P0")))
BEATS["R-01a"] = r_01a
MORN_K = "a plain weekday morning — even daylight through the sink window"
def r_02a(): return seed("R-02a", "the kitchen table", "her hands", [
    "Looking straight down at her kitchen table, " + KITCH + ": two white tablets beside a glass of water, a plain unbranded white tube of pain-relief gel. Her hands — deep brown skin, a plain wedding band — "
    "squeeze a line of clear gel from the tube onto two fingertips, caught mid-squeeze."],
    "her hands and the table", MORN_K, "no face, no readable labels, no brand names, no text, no knee strap, no product",
    R(("N sheet", "N"), ("P2-KITCHEN plate", "P2")))
BEATS["R-02a"] = r_02a
def r_02b(): return seed("R-02b", "her right knee", "her hands", [
    "Close on her lap at the kitchen table, " + KITCH + ", looking down the way she sees it herself. Her right knee under the hem of her knee-length denim skirt wears the black hinged brace, "
    "and both hands press a blue gel ice pack down onto it, caught as she presses. Deep brown skin, a plain wedding band."],
    "her knee and hands", MORN_K, "no face, no logo on the brace, no readable text, no knee strap, no product",
    R(("N sheet", "N"), ("P2-KITCHEN plate", "P2")))
BEATS["R-02b"] = r_02b
def r_03a(): return seed("R-03a", "Loretta across the table", "the strap", [
    "Across her kitchen table, " + KITCH + ". Loretta — " + C1["markers"] + ", exactly as in her attached reference sheet — sits in " + WARD["C1-D3"] + ", "
    "caught mid-roll as she pushes her right khaki trouser leg up past the knee, revealing the strap on her right knee, a knowing half-smile toward someone across the table. " + prod("bent")],
    "Loretta", "the morning light through the sink window", PNEG + ", no looking at the camera",
    R(("C1 sheet", "C1"), ("P2-KITCHEN plate", "P2"), *PR_REFS["bent"]))
BEATS["R-03a"] = r_03a
def r_04a(): return seed("R-04a", "her right knee", "the strap and its wordmark", [
    "Very close on Loretta's right knee as she sits at the kitchen table, her khaki trouser leg rolled above it, medium-brown skin. Her index finger taps the strap once, caught as it touches the shell. " + prod("bent")],
    "the knee and the strap", "the morning light through the sink window", PNEG + ", no face",
    R(("C1 sheet", "C1"), *PR_REFS["bent"]), house=False)
BEATS["R-04a"] = r_04a
def r_05a(): return seed("R-05a", "her open palms", "the strap", [
    "Looking down at her own hands above the kitchen table, " + KITCH + ": one strap lies across her two open palms, small against her hands, the front of the shell up. Caught as she turns her hands a little to look at it. " + prod("held")],
    "her hands and the strap", "the morning light through the sink window", PNEG + ", no face, no second strap",
    R(("N sheet", "N"), *PR_REFS["held"]))
BEATS["R-05a"] = r_05a
def r_06a(): return seed("R-06a", "her right shin", "the strap", [
    "Close on her right leg as she sits at the kitchen table, the hem of her denim skirt above the knee. " + PS.fill(PS.SEAT_LOCK, "right") + " Caught in the last few centimetres of the slide, just before contact."],
    "her hands and the strap", "the morning light through the sink window", PNEG + ", " + PS.fill(PS.NEG_SEAT, "right")[:500] + ", no face",
    R(("N sheet", "N"), *PR_REFS["worn"]))
BEATS["R-06a"] = r_06a
def r_07a(): return seed("R-07a", "her at the top of the stairs", "the strap", [
    "Her staircase, exactly as in the attached hall photo, seen from the hall floor looking up the straight flight. She — " + N["markers"] + ", exactly as in her attached reference sheet — in " + WARD["N-D3"] + ", "
    "is at the top of the stairs taking her first step down FACING FORWARDS, hands at her sides, not touching the rail, caught with one foot on the step below. The strap is on her right knee, visible below her skirt. " + prod("worn")],
    "her and the stairs", STAIRS_SUN, PNEG + ", no hands on the rail, no going down backwards, no one else on the stairs",
    R(("N sheet", "N"), ("P0-PROP-N plate", "P0"), *PR_REFS["worn"]))
BEATS["R-07a"] = r_07a
def r_07b(): return seed("R-07b", "her feet on the stairs", "the strap", [
    "Close on the stairs from the side at step height: the full-width oatmeal-beige stair carpet with its brass stair rods, white risers, a white baluster. Her feet in tan house slippers come down the stairs facing forwards, one foot per step, "
    "caught mid-step; the strap on her right knee is at the top of the frame, below the hem of her denim skirt. " + prod("worn")],
    "her feet and the steps", STAIRS_SUN, PNEG + ", no going down backwards, no face",
    R(("P0-PROP-N plate", "P0"), *PR_REFS["worn"]))
BEATS["R-07b"] = r_07b
def r_07c(): return seed("R-07c", "her stepping off the stairs", "the strap", [
    "Her hall, exactly as in the attached hall photo, seen from the side through the white balusters: she — " + N["markers"] + ", exactly as in her attached reference sheet — in " + WARD["N-D3"] + ", "
    "steps off the last stair onto the hall floor facing forwards, caught mid-step, one foot on the oak floor, a small surprised smile. The strap on her right knee. " + prod("worn")],
    "her", STAIRS_SUN, PNEG + ", no hands on the rail, no one else",
    R(("N sheet", "N"), ("P0-PROP-N plate", "P0"), *PR_REFS["worn"]), through="the white balusters")
BEATS["R-07c"] = r_07c

# ---------------------------------------------------------------- Act 4 — mechanism (Loretta's words)
def m_01a(): return seed("M-01a", "her on the treatment table", "her", [
    "In the physical therapy exam room, " + CLINIC + ". Seen from above: she lies back on the padded table — " + N["markers"] + ", exactly as in her attached reference sheet — in " + WARD["N-D1b"] + ", the right trouser leg rolled above the knee, "
    "a heat pad over her right knee, eyes closed, caught as she settles her head back on the paper pillow, resigned."],
    "her", "even afternoon daylight through the half-open blind, clinical and plain", "no smiling, no second person, no machines, no readable text, no knee strap, no product",
    R(("N sheet", "N"), ("P7-CLINIC plate", "P7")), house=False)
BEATS["M-01a"] = m_01a
def m_01b(): return anat("M-01b", HOT("a hot red, a little wider than before"), "The red at the spot on the tendon has spread a little further into the tissue around it, the worn joint behind it rough and pale.")
BEATS["M-01b"] = m_01b
def m_02a():
    r = anat("M-02a", CALM, "TWO RIGHT KNEES SIDE BY SIDE in the same anatomical world, the same size and angle. LEFT: a plain full-length knee sleeve covers the whole knee, the pressure spread evenly everywhere as a faint orange haze, nothing focused. "
             "RIGHT: the strap seated on the patellar tendon just below the kneecap, and one soft calm-blue glow settling on exactly that spot.", prod_in=True, neg="no text, no labels")
    return r
BEATS["M-02a"] = m_02a
def m_03a(): return anat("M-03a", HOT("a hot red"), "The tight red point on the patellar tendon just under the kneecap pulses with a walking cadence, one pulse per step.")
BEATS["M-03a"] = m_03a
def m_04a(): return seed("M-04a", "the kitchen table", "everything", [
    "Looking straight down at her kitchen table, " + KITCH + ": the heap of knee braces and sleeves — black hinged brace, beige and blue elastic sleeves, a padded wrap — beside the three orange pill bottles, the blister pack and a cold coffee. Nobody in frame."],
    "the table", GREY, "no people, no hands, no readable labels, no brand names, no text, no knee strap, no product",
    R(("P2-KITCHEN plate", "P2")))
BEATS["M-04a"] = m_04a
def m_04b(): return anat("M-04b", HOT("a hot red"), "A generic elastic knee sleeve is drawn around the whole knee as a faint translucent layer, and under it the tight red point below the kneecap keeps glowing, untouched by it.")
BEATS["M-04b"] = m_04b
def m_05a(): return anat("M-05a", HOT("a hot red"), "Pressure runs down the thigh as faint warm bands through the muscle and gathers into the tight red point just under the kneecap. " + S("ANAT-LOAD").replace("[STACK]", "the quadriceps").replace("[TARGET]", "the patellar tendon"))
BEATS["M-05a"] = m_05a
def m_05b(): return anat("M-05b", "STATE — the strap's pad sits on the spot and has taken the load: the glow at the spot has cooled from red to a calm, soft blue.", "The strap seated on the patellar tendon just below the kneecap, the pad pressing on the spot.", prod_in=True)
BEATS["M-05b"] = m_05b
def m_06a(): return seed("M-06a", "her foot on the top step", "the strap", [
    "Close on the top of her staircase from one step below, the lens at step height: the full-width oatmeal-beige stair carpet with its brass stair rods. Her foot in a tan house slipper settles flat on the top step, caught as it lands, "
    "and above it her right knee with the strap on it, the hem of her denim skirt. " + prod("worn")],
    "her foot and knee", STAIRS_SUN, PNEG + ", no face",
    R(("P0-PROP-N plate", "P0"), *PR_REFS["worn"]))
BEATS["M-06a"] = m_06a

# ---------------------------------------------------------------- Act 5 — proof
def mont(beat, who, place, action, light_q, kind="bent"):
    return seed(beat, "his or her right knee", "the strap", [
        place + ". " + who + " " + action + " " + (PS.fill(PS.SEAT_LOCK, "right") if kind == "seat" else prod(kind))],
        "the knee and the strap", light_q, PNEG + ", no face in focus, " + PS.fill(PS.NEG_SEAT, "right")[:300],
        R(*PR_REFS["worn" if kind == "seat" else kind]), house=False)
BEATS["PR-01a"] = lambda: mont("PR-01a", "A Black man in his sixties in shorts sits on the step,", "Close on a wooden front-porch step of an ordinary house in the afternoon sun",
    "his right leg out; caught in the last centimetres as both hands seat the strap on his right knee.", MID, "seat")
BEATS["PR-01b"] = lambda: mont("PR-01b", "A white woman in her fifties in a sleep shirt sits on the edge of her bed,", "Close on a bedroom, an unmade bed, a window with light curtains",
    "her right leg straight; caught in the last centimetres as both hands slide the strap up her shin to seat it.", "soft afternoon daylight through the bedroom window", "seat")
BEATS["PR-01c"] = lambda: mont("PR-01c", "A Latino man in his seventies in work trousers rolled up has one foot up on a low stool,", "Close in an open garage, a workbench and tools behind",
    "caught as his hand presses the strap flat under his right kneecap.", MID, "bent")
BEATS["PR-01d"] = lambda: mont("PR-01d", "A Black woman in her forties in gym shorts sits on a bench,", "Close at a small neighbourhood gym, a rack of dumbbells soft behind",
    "caught in the last centimetres as both hands seat the strap under her right kneecap.", "daylight from the gym's big front windows", "seat")
def pr_02a(): return seed("PR-02a", "the doctor", "the strap", [
    "In a sports-medicine clinic office, " + CLINIC + ". A sports-medicine doctor — a Black man in his fifties in a navy polo shirt, short greying beard — sits at his desk beside a life-size knee model, "
    "holding the strap up in a bottom-edge pinch, caught as he turns it toward a patient across the desk, explaining. " + prod("held")],
    "the doctor", "even afternoon daylight through the half-open blind", PNEG + ", no looking at the camera, no white coat, no readable text",
    R(*PR_REFS["held"], ("P7-CLINIC plate", "P7")), house=False)
BEATS["PR-02a"] = pr_02a
def pr_03a(): return seed("PR-03a", "the golfer", "the strap", [
    "On a golf course fairway in the afternoon. Loretta's husband — a Black man of seventy-six, lean, a white moustache, a navy golf polo, khaki shorts and golf shoes, a white cap — "
    "is caught holding his follow-through after a drive, club over his shoulder, weight on his front foot, watching the ball. The strap on his right knee, visible below his shorts. " + prod("worn")],
    "the golfer", "open afternoon sun, clear sky", PNEG + ", no looking at the camera, no logos on clothes",
    R(*PR_REFS["worn"]), house=False)
BEATS["PR-03a"] = pr_03a
def pr_04a(): return seed("PR-04a", "the runner", "the strap", [
    "On a red running track in the afternoon. Loretta's niece — a young Black woman of twenty-two, natural hair in a high puff, a sports top and running shorts — jogs past, caught mid-stride, "
    "right foot pushing off; the strap on her right knee. " + prod("worn")],
    "the runner", "open afternoon sun, clear sky", PNEG + ", no looking at the camera, no logos on clothes, no race bib",
    R(*PR_REFS["worn"]), house=False)
BEATS["PR-04a"] = pr_04a
def pr_05a(): return seed("PR-05a", "her right knee", "the strap", [
    "Close on her right leg as she sits on the edge of her bed in the morning, " + WARD["N-D5"] + " hitched above the knee; greige walls, a white six-panel door soft behind. " + PS.fill(PS.SEAT_LOCK, "right") + " Caught in the last few centimetres of the slide."],
    "her knee and the strap", MORN, PNEG + ", no face, " + PS.fill(PS.NEG_SEAT, "right")[:300],
    R(("N sheet", "N"), ("P0-PROP-N plate", "P0"), *PR_REFS["worn"]))
BEATS["PR-05a"] = pr_05a
def pr_05b(): return seed("PR-05b", "her right leg", "the trouser leg", [
    "Close from the side on her right leg as she stands by her bed in the morning: the leg of her navy trousers is caught falling down over the strap on her right knee, half covering it, the shell's edge still showing at the hem; greige wall and oak floor behind."],
    "her leg", MORN, "no face, no strap on the left knee, no bare legs, no second strap",
    R(("N sheet", "N"), ("P0-PROP-N plate", "P0"), *PR_REFS["worn"]))
BEATS["PR-05b"] = pr_05b
def pr_06a(): return seed("PR-06a", "the kitchen table", "the strap", [
    "Looking straight down at her kitchen table in the morning, " + KITCH + ": the table cleared — no pills, no gel, no braces — just a white coffee mug with a wisp of steam and one strap lying beside it, the front of the shell up. " + REF_PROD + ". " + PS.fill(PS.WORDMARK_LOCK, "right")],
    "the table", "morning sun through the sink window", PNEG + ", no people, no pill bottles, no braces",
    R(("P2-KITCHEN plate", "P2"), *PR_REFS["held"]))
BEATS["PR-06a"] = pr_06a

# ---------------------------------------------------------------- Act 6 — life back (N-D6, afternoon)
STREET = "her street exactly as in the attached street photo — a quiet tree-lined street of 1960s brick houses, a concrete sidewalk, big old oaks, her red-brick colonial with the white porch and two rocking chairs"
def l_01a(): return seed("L-01a", "her walking away", "everything", [
    "On " + STREET + ". Seen from behind: she — " + N["markers"] + ", exactly as in her attached reference sheet — walks away along the sidewalk in " + WARD["N-D6"] + ", a canvas tote on her shoulder, caught mid-stride, upright and brisk."],
    "her and the street", MID, "no looking at the camera, no walking stick, no knee strap visible, no product",
    R(("N sheet", "N"), ("P6-STREET plate", "P6")), house=False)
BEATS["L-01a"] = l_01a
def l_01b(): return seed("L-01b", "her passing three women", "her", [
    "On " + STREET + ". She — " + N["markers"] + ", exactly as in her attached reference sheet — in " + WARD["N-D6"] + ", a canvas tote on her shoulder, is caught drawing level with and passing three women in their thirties "
    "strolling slowly side by side with coffee cups, chatting; she is striding briskly past them on the outside, a small proud smile."],
    "her", MID, "no looking at the camera, no walking stick, no running, no knee strap visible, no product",
    R(("N sheet", "N"), ("P6-STREET plate", "P6")), house=False)
BEATS["L-01b"] = l_01b
def l_02a(): return seed("L-02a", "her in the checkout line", "her", [
    "In the grocery store, exactly as in the attached store photo — the checkout lane, the black conveyor belt, the card terminal on its post. She — " + N["markers"] + ", exactly as in her attached reference sheet — in " + WARD["N-D6"] + ", "
    "stands square in the checkout line holding a full shopping basket, two shoppers ahead of her, caught as she moves the basket to her other hand, feet planted."],
    "her", "flat cool-white overhead store light", "no looking at the camera, no leaning, no readable text or signs, no knee strap visible, no product",
    R(("N sheet", "N"), ("P4-STORE plate", "P4")), house=False)
BEATS["L-02a"] = l_02a
def l_02b(): return seed("L-02b", "her going up the path", "everything", [
    "On " + STREET + ". Seen from behind and to one side: she walks up the straight concrete path to her porch, a full brown paper grocery bag in each hand, caught mid-stride, in " + WARD["N-D6"] + "."],
    "her and the porch", MID, "no looking at the camera, no one helping, no knee strap visible, no product",
    R(("N sheet", "N"), ("P6-STREET plate", "P6")), house=False)
BEATS["L-02b"] = l_02b
def l_03a(): return seed("L-03a", "her husband in his recliner", "him", [
    "In her living room — greige walls, white six-panel doors, honey oak floor, a brown recliner by the front window. Her husband — a Black man in his late seventies, bald with a grey moustache, reading glasses, a cardigan over a plaid shirt — "
    "sits in the recliner and is caught lowering his newspaper, looking up toward the door with raised eyebrows."],
    "him", "afternoon sun through the front window", "no looking at the camera, no readable newspaper text, no knee strap, no product",
    R(("P0-PROP-N plate", "P0")))
BEATS["L-03a"] = l_03a

# ---------------------------------------------------------------- Act 7 — result and offer
def c_01a(): return seed("C-01a", "her right knee", "the strap", [
    "Close on her right knee as she sits on the edge of her bed in the morning in " + WARD["N-D5"] + ", the hem above the knee; her hand resting beside the strap, caught as it pats her knee once. " + prod("bent")],
    "her knee and hand", MORN, PNEG + ", no face",
    R(("N sheet", "N"), ("P0-PROP-N plate", "P0"), *PR_REFS["bent"]))
BEATS["C-01a"] = c_01a
def c_02a(): return seed("C-02a", "her on the church steps", "everything", [
    "The church, exactly as in the attached church photo — red-brick front, white columns, the wide front steps with a metal handrail. She — " + N["markers"] + ", exactly as in her attached reference sheet — in " + WARD["N-D4"] + ", "
    "comes down the church steps facing forwards, hands free, caught mid-step; three ladies in Sunday hats and dresses stand to one side at the foot of the steps watching her, one with a hand on her chest."],
    "her and the ladies", "Sunday afternoon sun, clear", "no hands on the rail, no looking at the camera, no knee strap visible, no product, no readable text",
    R(("N sheet", "N"), ("P5-CHURCH plate", "P5")), house=False)
BEATS["C-02a"] = c_02a
def c_03a(): return anat("C-03a", "STATE — calm: the strap on the spot, the glow at the patellar tendon a soft steady blue.", "The strap seated on the patellar tendon just below the kneecap, a slow soft glow at the pad.", prod_in=True)
BEATS["C-03a"] = c_03a
def c_04a(): return seed("C-04a", "the surgeon and the patient", "the strap", [
    "In the exam room, " + CLINIC + ". Over the shoulder of an orthopedic surgeon in navy scrubs: a seated patient — a Black woman in her sixties, trouser leg rolled up — rests her right leg out, "
    "and the surgeon's hands press the strap flat under her kneecap, caught at the moment of contact. " + prod("bent")],
    "the patient's knee", "even afternoon daylight through the half-open blind", PNEG + ", no looking at the camera, no readable text",
    R(("P7-CLINIC plate", "P7"), *PR_REFS["bent"]), house=False)
BEATS["C-04a"] = c_04a
def c_05a(): return seed("C-05a", "two cheap straps", "the curled tab", [
    "Close on her kitchen table, " + KITCH + ": two cheap generic knee straps lie side by side. " + PS.FAKE_BASE + " One of them has " + PS.FAKE_ARCHETYPES[2][1] + ". "
    "A fingertip flicks the curled velcro tab, caught mid-flick."],
    "the straps", MORN_K, "no wordmark, no brand, no logo, no packaging, no screen, no readable text, no chrome slides, no hero product",
    R(("P2-KITCHEN plate", "P2")))
BEATS["C-05a"] = c_05a
def c_06a(): return seed("C-06a", "her on the landing", "the straps", [
    "Her upstairs landing, exactly as in the attached landing photo — the photo wall behind her, the dark oak rail and newel. She — " + N["markers"] + ", exactly as in her attached reference sheet — in " + WARD["N-TODAY"] + ", "
    "stands waist-up to a propped phone and holds up two straps toward the lens, one in each hand in a bottom-edge pinch, caught lifting them a little higher, smiling. " + prod("held")],
    "her", "midday light from the landing window, bright and soft", PNEG.replace(", no second strap unless stated", "") + ", no third strap, no selfie arm",
    R(("N sheet", "N"), ("P1-LANDING plate", "P1"), *PR_REFS["held"]))
BEATS["C-06a"] = c_06a
def c_07a(): return seed("C-07a", "the open box", "everything", [
    "Looking straight down at her kitchen table in the morning, " + KITCH + ": the open box. " + PS.PACKAGE_LOCK + " Her hand, the cuff of her lilac long-sleeve cotton top at the wrist, sets the lid down beside the box, caught as it lands."],
    "the box", "bright morning daylight through the sink window", "no third strap, no single strap, no other items in the box, no offer text, no stickers, no readable text except the wordmark",
    R(("P2-KITCHEN plate", "P2"), *PR_REFS["box"]))
BEATS["C-07a"] = c_07a
def c_09a(): return seed("C-09a", "her hand and the box", "her hand and the card", [
    "Close on her kitchen table, " + KITCH + ": the closed matte-black box with the lowercase grey stryde wordmark centred on the lid, and a small white card lying on it. Her hand — deep brown skin, a plain wedding band, the cuff of her lilac long-sleeve cotton top at the wrist — "
    "writes on the card with a pen, caught mid-stroke; the writing is a short handwritten name, loose and not readable."],
    "her hand", MORN_K, "no readable handwriting, no other text, no offer text, no stickers",
    R(("N sheet", "N"), ("P2-KITCHEN plate", "P2"), *PR_REFS["box"]))
BEATS["C-09a"] = c_09a

if __name__ == "__main__":
    out = HERE / "prompts"; out.mkdir(exist_ok=True)
    for b in sys.argv[1:] or BEATS:
        dd = BEATS[b](); p = "\n\n".join(dd["body"])
        (out / f"{b}.t2i.txt").write_text(p)
        rr = [(k, v if isinstance(v, str) else (str(v.relative_to(B)) if B in v.parents else str(v.relative_to(B.parents[1])))) for k, v in dd["refs"]]
        (out / f"{b}.refs.json").write_text(json.dumps(dict(model=dd["model"], refs=rr), indent=1))
        print(b, dd["model"], len(p), "chars", [k for k, _ in dd["refs"]])
