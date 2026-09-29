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
 "N-D7":  "a lilac long-sleeve cotton top, a knee-length khaki skirt and white sneakers",
}
SHEET_DAYS = {"N-TODAY", "C1-D3"}   # the days the cast sheet's own outfit is worn
N = SUBJ["N"]
NID = N["skin"] + ", " + N["markers"]
M1 = ("no AI face, no plastic skin, no waxy skin, no extra fingers, no fused fingers, no melted hands, no deformed limbs, "
      "no warped background, no CGI look, no fake commercial gloss, no over-saturated colors, no vignette, no moody dark grade")
GREY = "a grey, overcast morning — flat, cool daylight, the problem days, plain and unflattering but never dark"
KITCH = "the same kitchen as the attached kitchen photo — cream vinyl tile, oak cabinets, the round table under the south window"
CLINIC = "the same exam room as the attached clinic photo — the padded table with its paper roll, the half-open blind, pale blue-grey walls"

def prop_ref():
    return S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", PROP_N_CARRIED)

def seed(beat, subject_word, focus_name, prose, light_subject, quality, neg, refs, house=True, side=None, through=None, height=None, clothes=None):
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
    if subj.startswith("N"):
        if clothes: txt += " Her clothes today: " + clothes + " — only as much of them as the frame shows."
        elif day in WARD and WARD[day] not in txt:
            txt += (" Her clothes today: " + WARD[day] + " — only as much of them as the frame shows.")
        if "deep brown skin" not in txt:   # user 2026-09-29: she rendered as a white woman on shots without her face
            txt += " She is a Black American woman: deep brown skin on every part of her that shows — face, hands, legs and feet."
        neg += ", no white woman, no light skin, no pale skin"
    if "Loretta" in txt:
        neg += ", no white woman, no light skin on Loretta"
    if day not in SHEET_DAYS:   # face and hair from the sheet, never its clothes (user 2026-09-29: same wardrobe on every day)
        txt = txt.replace("exactly as in her attached reference sheet", "her face, hair and build exactly as in her attached reference sheet, but not the clothes she wears on the sheet")
        if "reference sheet" in txt:
            neg += ", no outfit copied from the reference sheet, no cream open cardigan over a coral top, no plum blouse with khaki trousers"
    if any(l.startswith("STRYDE") for l, _ in refs):   # user 2026-09-29: "wrong product" x9 — the model invented braces and shields
        refs = ([x for x in refs if x[0].startswith("STRYDE worn")] + [x for x in refs if x[0].startswith("STRYDE") and not x[0].startswith("STRYDE worn")]
                + [x for x in refs if not x[0].startswith("STRYDE")])   # round 5: the worn photo leads
        txt = PROD_COPY + " " + txt
        neg += ", " + PROD_NEG
    body.append(txt)
    body += [lt, S("CAP-FILE"),
             "AVOID: " + ", ".join([S("NEG-FILE"), M1, neg])]
    return dict(model=MODEL[r["model"]], refs=refs, body=body)

PROD_COPY = ("THE STRAP — copy it EXACTLY from the first attached photos (the product photos; where a worn photo is attached, it shows exactly how it sits on the leg): ONE small, slim, matte-black curved shell only about 5 cm tall — "
  "about as tall as the kneecap — with two small rounded peaks and a shallow notch between them along its top edge, the lowercase grey stryde wordmark on its face, "
  "a small brushed-chrome slide at each end, and a thin black knit elastic band running from the slides around the back of the leg. It is NOT a knee brace, NOT a sleeve, NOT a pad and NOT a shield. "
  "Its top edge has TWO SMALL ROUNDED PEAKS with a notch between them that cups the bottom of the kneecap — never a flat straight band. "
  "When worn it sits HIGH, on BARE SKIN on the patellar tendon: its top edge TOUCHES the bottom edge of the kneecap, with NO bare skin showing between kneecap and strap; the whole strap fits inside the short "
  "space between the bottom of the kneecap and the bump at the top of the shin bone, the kneecap fully uncovered above it — never down on the shin, never over clothing. "
  "Its size against the knee: the shell is only about as wide as the kneecap plus a thumb's width on each side, and only about as tall as the kneecap — a small, slim strap, never wider than the front of the knee.")
PROD_NEG = ("no knee brace, no hinged brace, no metal side hinges, no brace with a hole for the kneecap, no knee sleeve, no wraparound pad, no tall shield, "
  "no strap over the kneecap, no strap low on the shin, no gap of skin between kneecap and strap, no oversized shell, no shell wider than the knee, no flat straight band, no strap without its two peaks, no strap over trousers or fabric, no velcro panel, no strap without its knit band, no different product from the product photos")

BEATS = {}

# ---------------------------------------------------------------- Act 1 — the problem days (N-D1, grey mornings)
def p_01a():   # Fix 2 2026-09-29: "she should be looking up the stairs and both her hands at the railing stepping down backwards slowly and struggling"
    return seed("P-01a", "her on the stairs", "her", [
      "Her staircase, exactly as in the attached hall photo: the straight open flight with the full-width oatmeal-beige stair carpet and its brass stair rods, the white balusters and dark oak handrail, the photo wall of small dark-framed family portraits. "
      "Seen from the hall floor at the foot of the stairs looking UP the flight, from the side and a little behind her, the way the hall photo sees the flight; the whole empty lower flight between the camera and her. A woman of seventy-one — " + NID + ", exactly as in her attached reference sheet — is HIGH ON THE FLIGHT, about ten steps up and only three steps below the top landing — nowhere near the bottom, most of the stairs still below her — "
      "going DOWN her stairs BACKWARDS, the way people do when the knees can't take it: her whole body faces UP the stairs toward the landing — chest, knees and the toes of both slippers pointing UP the flight, her back and her heels toward the hall below. "
      "She is LOOKING UP THE STAIRS, her face in profile turned toward the top of the flight. BOTH her hands grip the dark oak handrail beside her, one hand a little above the other, knuckles tight, her arms taking her weight. "
      "Caught mid-step, slow and struggling: her right leg reaching DOWN BEHIND her, the heel of that slipper feeling for the step below, toes still pointing up the stairs; her left foot flat on the step above carrying her, that knee bent and stiff, "
      "her shoulders hunched, her jaw set. "
      "She is wearing " + WARD["N-D1"] + ". The hall is dim; nothing tidied."],
      "her and the stairs", GREY,
      "no her at the bottom of the stairs, no her on the lowest steps, no facing down the stairs, no walking forwards down the stairs, no toes pointing down the stairs, no looking down the stairs toward the camera, no hand off the handrail, no hands at her sides, no fast movement, no stumbling, no fall, no one else on the stairs, no stairlift, no walking stick, no knee brace, no product, no smiling, no different staircase from the hall photo, no turn in the stairs, no narrow runner",
      [("N sheet", REF["N"]), ("P0-PROP-N plate", REF["P0"])], side="three-quarter-back", height="eye")
BEATS["P-01a"] = p_01a

def p_01b():   # Fix 3 2026-09-29: "i want a overall new one" — new framing, same beat: one step at a time, both feet on the same step
    return seed("P-01b", "her feet and hand on the stairs", "her feet", [
      "Her staircase, exactly as in the attached hall photo, halfway up the flight, seen from the side through the white balusters at knee height — two soft white balusters in the near foreground: "
      "the full-width oatmeal-beige stair carpet with its brass stair rods, steps climbing out of frame above and dropping away below. She is in the MIDDLE of the staircase. "
      "From her knees down, going down BACKWARDS one step at a time: BOTH her feet in pink terry slippers stand TOGETHER, side by side, on ONE AND THE SAME step, toes pointing UP the stairs, heels at the front edge of the tread; "
      "the hem of her faded blue floral house dress at her knees, her bare deep-brown calves, and at the top of the frame one hand gripping the dark oak handrail, knuckles tight. "
      "Caught in the pause between steps, both feet just settled, her weight on them, before the next slow step down."],
      "her feet and the steps", GREY,
      "no feet on two different steps, no one foot higher than the other, no mid-stride, no toes pointing down the stairs, no face, no hall floor, no bottom of the stairs, no fast movement, no stumbling, no bare feet, no shoes, no knee brace, no product, no narrow runner, no different carpet from the hall photo",
      [("N sheet", REF["N"]), ("P0-PROP-N plate", REF["P0"])], through="two white balusters")
BEATS["P-01b"] = p_01b

def p_02a():   # Fix 2026-09-29: "camera angle at her back and she just looking at the stairs then just leaves cause she dont want to go down"
    return seed("P-02a", "her at the top of the stairs", "everything", [
      "Her staircase, exactly as in the attached hall photo. Seen from behind her on the top landing: she — " + NID + ", exactly as in her attached reference sheet — "
      "stands at the head of the stairs with her back to the camera, the whole straight flight dropping away below her: the full-width oatmeal-beige stair carpet with its brass stair rods, the dark oak handrail, the photo wall of family portraits running down on the left, "
      "the front door closed at the bottom and the hall below dim. She has been looking down the stairs and has given up: caught just as she turns away from them, "
      "her shoulders sagging, her weight shifting back onto the landing, one hand letting go of the newel post, her head still half toward the drop. Her feet stay on the landing; she does not step down. "
      "She is wearing " + WARD["N-D1"] + ". A strip of grey light from the landing window lies across the top steps."],
      "her and the staircase", GREY,
      "no face to camera, no stepping down, no one else, no open door, no bright sunlight, no different staircase from the hall photo, no turn in the stairs, no knee brace, no product",
      [("N sheet", REF["N"]), ("P0-PROP-N plate", REF["P0"])])   # P1 removed (user 2026-09-29)
BEATS["P-02a"] = p_02a

def p_03a():   # Fix 2026-09-29 x2 ("fix the p03a too", "fix this"): her own view down at her lap, the brace clearly slid below the knee, same brace as v1
    return seed("P-03a", "her right knee", "her hands", [
      "Her own view, looking straight down at her lap as she sits on a kitchen chair at her table, " + KITCH + ": the phone held at her chest, the lens pointing down her legs. "
      "The hem of her faded blue floral house dress pushed up above her bare right knee, the grey cardigan sleeves pushed to her forearms, her feet in pink terry slippers on the cream tile below. "
      "The SAME black hinged knee brace as in the attached brace photo — identical fabric, metal side hinges, velcro straps, size and shape — has slid DOWN her leg: its top edge now sits below her kneecap, the kneecap bare above it, the brace sagging and bunched around her upper shin, its straps twisted. "
      "Caught mid-pull: both her hands grip the top edge of the brace and haul it back up toward the knee, the fabric bunching. Deep brown skin on her knee, shin and hands, fine creases, a plain wedding band."],
      "her knee and hands", GREY,
      "no face, no side view, no brace sitting correctly on the knee, no bare feet, no missing cardigan, no different brace from the brace photo, no logo on the brace, no brand name, no readable text, no knee strap, no product, no bandage, no swelling, no injury",
      [("N sheet", REF["N"]), ("P2-KITCHEN plate", REF["P2"]), ("P-03a brace photo (v1)", "job:5948917d-e509-41ad-a4f4-a524887d3a9e")])
BEATS["P-03a"] = p_03a

def p_03b():
    return seed("P-03b", "her right ankle", "the brace around her ankle", [
      "Close to the floor of her kitchen, " + KITCH + ", the lens a few centimetres above the cream vinyl tile under the table. "
      "Her right foot in a pink terry slipper, and above it the SAME black hinged knee brace as in the attached brace photo — identical: the same black fabric, the same metal side hinges, the same velcro straps, the same size and shape — has slid all the way down her leg and sits bunched around her ankle, twisted, its velcro straps hanging loose. "
      "The hem of her faded blue floral house dress and her bare calf in frame. Caught as she shifts her foot a little on the tile. Evening: the light is low and fading."],
      "her foot and ankle", "the last low daylight of the evening, dimmer and warmer than the morning, still plain",
      "no face, no different brace from the brace photo, no sleeve instead of the brace, no logo on the brace, no readable text, no knee strap, no product, no injury, no swelling",
      [("N sheet", REF["N"]), ("P2-KITCHEN plate", REF["P2"]), ("P-03a (latest)", B / "broll/images/P-03a_img_v3.png")])
BEATS["P-03b"] = p_03b   # Fix 2026-09-29: "this should be the same as the brace of the p03a"

def p_04a():
    return seed("P-04a", "her on the treatment table", "the therapist's hands on her knee", [
      "In a physical therapy exam room, " + CLINIC + ". She lies on her back on the padded table — " + NID + ", exactly as in her attached reference sheet — "
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
      "She sits alone at the table in profile — " + NID + ", exactly as in her attached reference sheet — in " + WARD["N-D1e"] + ", "
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
C1ID = C1["skin"] + ", " + C1["markers"]
REF["T01B"] = B / "broll/images/T-01b_img_v1.png"
REF["THF"] = B / "broll/images/TH-frame_ref.png"      # frame of the confirmed TH-09 talking head
REF["L01A"] = B / "broll/images/L-01a_tote_crop.png"  # the tote, cropped from confirmed L-01a
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
        "no silicone look, no glossy shell, no second strap unless stated, no product changing shape, no oversized strap, no strap wider than the knee, no knee sleeve, no band around the kneecap")
def prod(kind):
    if kind == "worn":   return REF_PROD + ". " + PS.fill(PS.PLACE_LOCK_C, "right") + " " + PS.SIZE_WORN
    if kind == "bent":   return REF_PROD + ". " + PS.fill(PS.PLACE_BENT, "right") + " " + PS.fill(PS.WORDMARK_LOCK, "right") + " " + PS.SIZE_WORN
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
def t_01a(): return seed("T-01a", "the bride", "the bride", [   # Fix 2026-09-29: "they all have the same faces"
    "At a Black American wedding reception in June, " + RECEP + ". The bride — a young Black woman of twenty-six, dark brown skin, a heart-shaped face with a wide gap-toothed laugh, short natural hair in a sleek pinned-up twist, in a white off-shoulder dress — "
    "sits at a reception table caught mid-laugh, her head tipped back, one hand on the arm of the guest beside her. Every guest around her is a DIFFERENT person with a clearly different face: "
    "beside her an older woman in her sixties, light-brown skin, round face with glasses and a grey bob; across the table a heavy-set man in his forties, very dark skin, shaved head and a full beard; "
    "a slim teenage girl with long braids and freckles; a tall man in his thirties with a narrow face, a thin moustache and a high-top fade; a woman in her fifties with a wide face and a head wrap. "
    "Glasses, a half-eaten slice of cake, a phone face-down on the cloth. Nobody looks at the camera."],
    "the bride and the guests", PARTY, "no two faces alike, no repeated face, no twins, no same hairstyle on everyone, no posing, no looking at the camera, no professional wedding photography look, no flash, no knee strap, no product, no readable text",
    R(("P3-RECEPTION plate", "P3")), house=False)
BEATS["T-01a"] = t_01a
def t_01b(): return seed("T-01b", "Loretta", "Loretta", [
    "At the same reception, " + RECEP + ". Loretta — " + C1ID + ", exactly as in her attached reference sheet — stands at the edge of the dance floor in " + WARD["C1-D2"] + ", "
    "caught mid-clap on the beat, both hands meeting in front of her chest, grinning, her eyes on the dancers off-frame; guests blurred behind her. " + C1["skin"].capitalize() + "."],
    "Loretta", PARTY, "no looking at the camera, no knee strap visible, no product, no flash, no readable text",
    R(("C1 sheet", "C1"), ("P3-RECEPTION plate", "P3")), house=False)
BEATS["T-01b"] = t_01b
def t_02a(): return seed("T-02a", "the line of dancers", "everything", [
    "The dance floor at the same reception, " + RECEP + ", seen past the backs of two chairs. A line of about eight guests — Black Americans of every age in their wedding clothes — is doing a line dance in step, "
    "and Loretta — " + C1ID + ", exactly as in her attached reference sheet, in " + WARD["C1-D2"] + " — is in the middle of the line, caught mid side-step with the others, arms loose, laughing. Her clothes exactly as in the attached T-01b photo of her: the same royal-blue sleeveless satin sheath dress to the knee and the same white slip-on sneakers. Her knees are covered by her dress. "
    "Every dancer has a DIFFERENT face — different ages, builds, skin tones, hairstyles and outfits."],
    "the dancers", PARTY, "no two faces alike, no repeated face, no different dress on Loretta, no posed group, no looking at the camera, no knee strap visible, no product, no flash, no readable text",
    R(("C1 sheet", "C1"), ("P3-RECEPTION plate", "P3"), ("T-01b Loretta's dress", "T01B")), house=False, through="the backs of two gold chairs")
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
    "Her hall, exactly as in the attached hall photo, seen from inside looking at the open front door. Loretta — " + C1ID + ", exactly as in her attached reference sheet — in " + WARD["C1-D3"] + ", "
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
    "Across her kitchen table, " + KITCH + ". Loretta — " + C1ID + ", exactly as in her attached reference sheet — sits in " + WARD["C1-D3"] + ", "
    "caught mid-roll as she pushes her right khaki trouser leg up past the knee, revealing the strap on her right knee, a knowing half-smile toward someone across the table. " + prod("bent")],
    "Loretta", "the morning light through the sink window", PNEG + ", no looking at the camera",
    R(("C1 sheet", "C1"), ("P2-KITCHEN plate", "P2"), *PR_REFS["bent"]))
BEATS["R-03a"] = r_03a
def r_04a(): return seed("R-04a", "Loretta's right knee", "the strap and its wordmark", [   # Fix 2026-09-29: "all of these are wrong"
    "Close on Loretta's right knee as she sits on a wooden kitchen chair at the table, " + KITCH + ". Loretta — " + C1ID + " — her face out of frame; her khaki trouser leg is rolled up ABOVE the right knee so the whole knee and shin are bare skin, "
    "the plum blouse cuff of her own right hand in frame. Medium-brown skin on her knee, shin and hand. Seen from the front of the bent knee so the shell's two small peaks and the notch cupping the bottom of her kneecap read clearly. "
    "Her OWN right index finger taps the chrome slide at the outer end of the strap once, caught as it touches, the whole shell and the wordmark uncovered. " + prod("bent")],
    "the knee and the strap", "the morning light through the sink window", PNEG + ", no face, no someone else's hand, no hand from outside the frame, no white skin, no sandals, no bare foot",
    R(("C1 sheet", "C1"), ("P2-KITCHEN plate", "P2"), *PR_REFS["bent"]))
BEATS["R-04a"] = r_04a
def r_05a(): return seed("R-05a", "her open palms", "the strap", [
    "Looking down at her own hands above the kitchen table, " + KITCH + ": one strap lies across her two open palms, small against her hands, the front of the shell up. Caught as she turns her hands a little to look at it. " + prod("held")],
    "her hands and the strap", "the morning light through the sink window", PNEG + ", no face, no second strap",
    R(("N sheet", "N"), *PR_REFS["held"]))
BEATS["R-05a"] = r_05a
def r_06a(): return seed("R-06a", "her right shin", "the strap", [   # Fix 2026-09-29: sitting on a chair; hands never cover the product
    "Close on her right leg as she SITS ON A WOODEN KITCHEN CHAIR at her table, " + KITCH + " — the chair seat and a chair leg in frame under her, her knee bent at a right angle, her foot in a tan house slipper flat on the cream tile, "
    "the hem of her denim skirt above the knee. She is sliding the strap up her shin with her two hands holding ONLY the band at the two outer sides of the leg, fingertips on the band beside the chrome slides — "
    "the whole front of the shell and its wordmark completely uncovered, nothing in front of it. " + PS.fill(PS.SEAT_LOCK, "right") + " Caught in the last few centimetres of the slide, just before contact."],
    "her leg and the strap", "the morning light through the sink window", PNEG + ", " + PS.fill(PS.NEG_SEAT, "right")[:500] + ", no face, no standing, no hands on the shell, no fingers over the wordmark, no hand covering the strap",
    R(("N sheet", "N"), ("P2-KITCHEN plate", "P2"), *PR_REFS["worn"]))
BEATS["R-06a"] = r_06a
def r_07a(): return seed("R-07a", "her coming down the stairs", "her", [   # Fix 2026-09-29 x3: very top, coming down, hands off the rail, her face, her staircase
    "THE SAME STAIRCASE AND THE SAME VIEWPOINT AS THE ATTACHED HALL PHOTO: taken from exactly where that photo was taken, in the hall by the front door, the straight flight rising away with the photo wall on its right and the white balusters and dark oak handrail on its left; "
    "the full-width oatmeal-beige carpet with its brass stair rods. She — " + NID + ", THE SAME WOMAN as in the attached talking-head frame and her reference sheet, the same face — in " + WARD["N-D3"] + ", "
    "is at the VERY TOP of that flight, on the top step, coming DOWN toward the camera, FACING FORWARDS: caught taking her first step down, one tan house slipper landing on the step below the top, the whole empty flight between her and the camera. "
    "Her hands NEVER touch the handrail: her right hand holds a white coffee mug in front of her, her left arm hangs free on the wall side, both hands well clear of the rail. Steady and easy, a small surprised smile. "
    "The strap on her right knee, visible below the hem of her denim skirt. " + prod("worn")],
    "her and the stairs", STAIRS_SUN, PNEG + ", no hands on the rail, no hand touching the handrail, no going down backwards, no one else on the stairs, no her halfway down, no her near the bottom, no different staircase, no different woman",
    R(("N sheet", "N"), ("Talking-head frame (her face)", "THF"), ("P0-PROP-N plate", "P0"), *PR_REFS["worn"]), height="eye", side="front")
BEATS["R-07a"] = r_07a

# ---------------------------------------------------------------- Act 4 — mechanism (Loretta's words)
def m_01a(): return seed("M-01a", "her on the treatment table", "her", [
    "In the physical therapy exam room, " + CLINIC + ". Seen the way a companion's phone sees it, from a chair at the foot of the table, at seated eye height, three-quarter on: she lies back on the padded table — " + NID + ", exactly as in her attached reference sheet — in " + WARD["N-D1b"] + ", the right trouser leg rolled above the knee, "
    "a heat pad over her right knee, eyes closed, caught as she settles her head back on the paper pillow, resigned."],
    "her", "even afternoon daylight through the half-open blind, clinical and plain", "no smiling, no second person, no machines, no readable text, no knee strap, no product",
    R(("N sheet", "N"), ("P7-CLINIC plate", "P7")), house=False, height="eye", side="three-quarter")   # Fix 2026-09-29: realistic camera, no overhead
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
def m_05a(): return anat("M-05a", HOT("a hot red"), neg="no glow on the kneecap, no red on the kneecap, no glow above the tendon", extra= "Pressure runs down the thigh as faint warm bands through the muscle and gathers into the tight red point ON THE PATELLAR TENDON — the thick cord running from the bottom tip of the kneecap down to the bump at the top of the shin bone — "
    "a thumb's width BELOW the kneecap, in the middle of that cord. The kneecap itself stays calm and unlit. " + S("ANAT-LOAD").replace("[STACK]", "the quadriceps").replace("[TARGET]", "the patellar tendon"))
BEATS["M-05a"] = m_05a
def m_05b(): return anat("M-05b", "STATE — the strap's pad sits on the spot and has taken the load: the glow at the spot has cooled from red to a calm, soft blue.", "The strap seated on the patellar tendon just below the kneecap, the pad pressing on the spot.", prod_in=True)
BEATS["M-05b"] = m_05b
def m_06a(): return seed("M-06a", "her first step down", "her", [   # Fix 2026-09-29: "everything is wrong we need an over all new"
    "Her staircase, exactly as in the attached hall photo. Seen from three steps below her, the lens at her knee height looking up the flight: she — " + NID + ", exactly as in her attached reference sheet — in " + WARD["N-D3"] + ", "
    "stands at the top of the stairs and takes her FIRST step down, FORWARDS, facing the camera: her right foot in a tan house slipper landing flat on the first step, her knee bending easily over it, "
    "both arms relaxed at her sides, well away from the handrail, her face breaking into a relieved, surprised smile — no pain. The strap on her right knee just below the hem of her denim skirt. " + prod("worn")],
    "her and the stairs", STAIRS_SUN, PNEG + ", no hands on the rail, no hand touching the handrail, no going down backwards, no sandals, no bare feet",
    R(("N sheet", "N"), ("P0-PROP-N plate", "P0"), *PR_REFS["worn"]), height="low", side="front")
BEATS["M-06a"] = m_06a

# ---------------------------------------------------------------- Act 5 — proof
def mont(beat, who, place, action, light_q, kind="bent"):
    return seed(beat, "his or her right knee", "the strap", [
        place + ". " + who + " " + action + " " + (PS.fill(PS.SEAT_LOCK, "right") if kind == "seat" else prod(kind))],
        "the knee and the strap", light_q, PNEG + ", no face in focus, " + PS.fill(PS.NEG_SEAT, "right")[:300],
        R(*PR_REFS["worn" if kind == "seat" else kind]), house=False)
BEATS["PR-01a"] = lambda: seed("PR-01a", "the person", "the strap", [   # Fix 2026-09-29: productive B-roll — what the strap lets them do
    'On the front steps of an ordinary brick house in the afternoon sun' + ". " + 'A Black man in his sixties, stocky, a grey goatee, in khaki shorts and a faded T-shirt,' + " " + 'carries a full 20 kg bag of garden mulch on his shoulder UP his porch steps, caught mid-step on the second step, his right knee bent and taking the load, the strap on his right knee below his shorts, easy and strong.' + " " + prod("worn")],
    "the person and the strap", MID, PNEG + ", no looking at the camera, no posing, no sitting, no putting the strap on",
    R(*PR_REFS["worn"]), house=False, side="three-quarter", height="low")
BEATS["PR-01b"] = lambda: seed("PR-01b", "the woman", "her", [   # Fix 2026-09-29: "the product should always be under the pants"
    "In her backyard vegetable garden in the afternoon, raised beds and a wooden fence behind. A Black woman in her fifties, a round face, short natural hair, in long olive work trousers down to her ankles and a T-shirt, garden gloves on, "
    "pushes a loaded wheelbarrow of soil up a short grassy slope between the beds, caught mid-stride, leaning into it, her right knee bent under the load, a satisfied grin. " + prod("hidden").replace("her clothes", "her trousers")],
    "the woman", MID, "no looking at the camera, no posing, no strap visible, no strap over the trousers, no knee brace, no rolled-up trousers, no shorts",
    [], house=False, side="three-quarter", height="low")
BEATS["PR-01c"] = lambda: seed("PR-01c", "the person", "the strap", [   # Fix 2026-09-29: productive B-roll — what the strap lets them do
    'In his open garage in the afternoon, a pegboard of tools and a workbench behind' + ". " + 'A Latino man in his seventies, lean, white hair and a trimmed white moustache, in work shorts and a plaid short-sleeve shirt,' + " " + 'stands on the second rung of an aluminium stepladder, reaching up to hang a bicycle on a wall hook, caught mid-reach, his weight on his right leg, the strap on his right knee below his shorts.' + " " + prod("worn")],
    "the person and the strap", MID, PNEG + ", no looking at the camera, no posing, no sitting, no putting the strap on, no crouching",
    R(*PR_REFS["worn"]), house=False, side="three-quarter", height="low")
BEATS["PR-01d"] = lambda: mont("PR-01d", "A Black woman in her forties in gym shorts sits on a bench,", "Close at a small neighbourhood gym, a rack of dumbbells soft behind",
    "caught in the last centimetres as both hands seat the strap under her right kneecap.", "daylight from the gym's big front windows", "seat")
def pr_02a(): return seed("PR-02a", "the doctor", "the strap", [
    "In a sports-medicine clinic office, " + CLINIC + ". A sports-medicine doctor — a Black man in his fifties in a navy polo shirt, short greying beard — sits at his desk beside a life-size knee model, "
    "holding up ONE complete strap between his thumb and two fingers by one chrome slide, the black knit band hanging below it as a loop, caught as he turns it toward a patient across the desk, explaining. "
    "Framed from his waist up, the strap SMALL in the frame and in his hand: about as wide as his four fingers laid side by side, about 12 cm, much smaller than his chest or his face. " + prod("held")],
    "the doctor", "even afternoon daylight through the half-open blind", PNEG + ", no looking at the camera, no white coat, no readable text, no strap wider than his hand, no strap as wide as his chest",
    R(*PR_REFS["held"], ("P7-CLINIC plate", "P7")), house=False)
BEATS["PR-02a"] = pr_02a
def pr_03a(): return seed("PR-03a", "the golfer", "the strap", [
    "On a golf course fairway in the afternoon. Loretta's husband — a Black man of seventy-six, lean, a white moustache, a navy golf polo, khaki shorts and golf shoes, a white cap — "
    "is caught holding his follow-through after a drive, club over his shoulder, weight on his front foot, watching the ball. Framed from mid-thigh up to his cap, his knees large enough in frame to read: "
    "ONE strap, on his RIGHT knee only, sitting HIGH directly under the kneecap — the notch touching the kneecap's lower edge, a hand's width above the middle of the shin — the kneecap bare above it; his left knee bare. " + prod("worn")],
    "the golfer", "open afternoon sun, clear sky", PNEG + ", no looking at the camera, no logos on clothes, no strap on both knees, no strap on the shin",
    R(*PR_REFS["worn"]), house=False, height="low")
BEATS["PR-03a"] = pr_03a
def pr_04a(): return seed("PR-04a", "the runner", "the strap", [
    "On a red running track in the afternoon. Loretta's niece — a young Black woman of twenty-two, natural hair in a high puff, a sports top and running shorts — jogs past, caught mid-stride, "
    "right foot pushing off; the strap on her right knee. " + prod("worn")],
    "the runner", "open afternoon sun, clear sky", PNEG + ", no looking at the camera, no logos on clothes, no race bib",
    R(*PR_REFS["worn"]), house=False)
BEATS["PR-04a"] = pr_04a
def pr_05a(): return seed("PR-05a", "her watering the garden", "her", [   # Fix 2026-09-29: "should be productive broll"
    "On " + STREET + ", in her front yard on an early morning. She — " + NID + ", exactly as in her attached reference sheet — waters the flower bed along her porch with a full green metal watering can, "
    "caught mid-stride as she steps up onto the low brick edging of the bed, her weight on her right leg, easy and steady, a small content smile. The strap on her right knee below the hem of her skirt. " + prod("worn")],
    "her and the yard", MORN, PNEG + ", no looking at the camera, no posing, no sitting",
    R(("N sheet", "N"), ("P6-STREET plate", "P6"), *PR_REFS["worn"]), house=False, height="low", side="three-quarter",
    clothes="a light-blue sleeveless cotton housedress to the knee and tan garden clogs")
BEATS["PR-05a"] = pr_05a
def pr_05b(): return seed("PR-05b", "her right leg", "the trouser leg", [   # Fix 2026-09-29: "dont show the product here"
    "Close from the side on her right leg as she stands by her bed in the morning, in her bedroom in the same house — greige wall, honey oak floor. She wears plain navy trousers and a plain white T-shirt, its hem at her hip. "
    "Her deep-brown hand smooths the navy trouser leg down over her knee, caught mid-smooth; the trouser leg hangs straight and plain to her ankle — nothing shows under it, no outline, no strap visible anywhere."],
    "her leg", MORN, "no face, no dress, no skirt, no nightgown, no strap visible, no product, no bulge under the fabric, no bare legs, no rolled trouser",
    R(("N sheet", "N"), ("P0-PROP-N plate", "P0")), clothes="plain navy trousers and a plain white T-shirt")
BEATS["PR-05b"] = pr_05b
def pr_06a(): return seed("PR-06a", "the kitchen table", "the strap", [
    "Looking straight down at her kitchen table in the morning, " + KITCH + ": the table cleared — no pills, no gel, no braces — just a white coffee mug with a wisp of steam and one strap lying beside it, the front of the shell up. " + REF_PROD + ". " + PS.fill(PS.WORDMARK_LOCK, "right")],
    "the table", "morning sun through the sink window", PNEG + ", no people, no pill bottles, no braces",
    R(("P2-KITCHEN plate", "P2"), *PR_REFS["held"]))
BEATS["PR-06a"] = pr_06a

# ---------------------------------------------------------------- Act 6 — life back (N-D6, afternoon)
BOXSIZE = " The box is SMALL against her: about as long as her forearm from elbow to wrist, only about a hand's height tall — a hand laid on the lid covers about half of it."
STREET = "her street exactly as in the attached street photo — a quiet tree-lined street of 1960s brick houses, a concrete sidewalk, big old oaks, her red-brick colonial with the white porch and two rocking chairs"
def l_01a(): return seed("L-01a", "her walking away", "everything", [
    "On " + STREET + ". Seen from behind: she — " + NID + ", exactly as in her attached reference sheet — walks away along the sidewalk in " + WARD["N-D6"] + ", a canvas tote on her shoulder, caught mid-stride, upright and brisk."],
    "her and the street", MID, "no looking at the camera, no walking stick, no knee strap visible, no product",
    R(("N sheet", "N"), ("P6-STREET plate", "P6")), house=False)
BEATS["L-01a"] = l_01a
def l_01b(): return seed("L-01b", "her passing three women", "her", [
    "On " + STREET + ". She — " + NID + ", exactly as in her attached reference sheet — in " + WARD["N-D6"] + ", a canvas tote on her shoulder, is caught drawing level with and passing three women in their thirties "
    "strolling slowly side by side with coffee cups, chatting; she is striding briskly past them on the outside, a small proud smile."],
    "her", MID, "no looking at the camera, no walking stick, no running, no knee strap visible, no product",
    R(("N sheet", "N"), ("P6-STREET plate", "P6")), house=False)
BEATS["L-01b"] = l_01b
def l_02a(): return seed("L-02a", "her in the checkout line", "her", [
    "In the grocery store, exactly as in the attached store photo — the checkout lane, the black conveyor belt, the card terminal on its post. She — " + NID + ", exactly as in her attached reference sheet — in " + WARD["N-D6"] + ", "
    "stands square in the checkout line holding a full shopping basket, on her shoulder THE SAME tote as in the attached tote photo: a slim, narrow natural-cream canvas tote with an olive-brown canvas bottom panel and two long olive-brown shoulder straps, hanging to her hip — small, not a big shopping bag — two shoppers ahead of her, caught as she moves the basket to her other hand, feet planted."],
    "her", "flat cool-white overhead store light", "no missing tote bag, no different bag from the tote photo, no big shopping tote, no all-cream bag, no looking at the camera, no leaning, no readable text or signs, no knee strap visible, no product",
    R(("N sheet", "N"), ("P4-STORE plate", "P4"), ("L-01a tote photo", "L01A")), house=False)
BEATS["L-02a"] = l_02a
def l_02b(): return seed("L-02b", "her going up the path", "everything", [
    "On " + STREET + ". Seen from behind and to one side: she walks up the straight concrete path to her porch, her canvas tote bag on her shoulder and a full brown paper grocery bag in each hand, caught mid-stride, in " + WARD["N-D6"] + "."],
    "her and the porch", MID, "no missing tote bag, no looking at the camera, no one helping, no knee strap visible, no product",
    R(("N sheet", "N"), ("P6-STREET plate", "P6")), house=False)
BEATS["L-02b"] = l_02b
def l_03a(): return seed("L-03a", "her husband in his recliner", "him", [
    "In her living room — greige walls, white six-panel doors, honey oak floor, a brown recliner by the front window. Her husband — a Black man in his late seventies, bald with a grey moustache, reading glasses, a cardigan over a plaid shirt — "
    "sits in the recliner and is caught lowering his newspaper, looking up toward the door with raised eyebrows."],
    "him", "afternoon sun through the front window", "no looking at the camera, no readable newspaper text, no knee strap, no product",
    R(("P0-PROP-N plate", "P0")))
BEATS["L-03a"] = l_03a

# ---------------------------------------------------------------- Act 7 — result and offer
def c_01a(): return seed("C-01a", "her right knee", "the strap", [   # Fix 2026-09-29: "wrong again all of the avatar and location"
    "Close on her right knee as she sits on the edge of her bed in the morning, in her bedroom in the same house — greige walls, a white six-panel door with a round brass knob, honey oak floor, a quilted bedspread in faded blues. "
    "She is in her pale-yellow cotton nightgown, the hem above the knee; deep brown skin on her knee, shin and hand, a plain wedding band; her hand resting beside the strap, caught as it pats her knee once. " + prod("bent")],
    "her knee and hand", MORN, PNEG + ", no face, no hotel room, no different house",
    R(("N sheet", "N"), ("P0-PROP-N plate", "P0"), *PR_REFS["bent"]))
BEATS["C-01a"] = c_01a
def c_02a(): return seed("C-02a", "her on the church steps", "everything", [
    "The church, exactly as in the attached church photo — red-brick front, white columns, the wide front steps with a metal handrail. She — " + NID + ", exactly as in her attached reference sheet — in " + WARD["N-D4"] + ", "
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
def c_05a(): return seed("C-05a", "a cheap knock-off strap", "the cheap strap", [   # Fix 2026-09-29: "distorted image i need a new one"
    "Close on her kitchen table, " + KITCH + ": a crumpled grey plastic mailer bag torn open, and her hand — deep brown skin, a plain wedding band — holding up ONE cheap generic knee strap by one end between finger and thumb, "
    "the strap hanging limp and flimsy. " + PS.FAKE_BASE + " It has " + PS.FAKE_ARCHETYPES[2][1] + ". Caught as it dangles. One simple, whole, undistorted object, clearly readable."],
    "the cheap strap and her hand", MORN_K, "no wordmark, no brand, no logo, no readable text, no chrome slides, no hero product, no distorted shapes, no melted object, no second strap",
    R(("N sheet", "N"), ("P2-KITCHEN plate", "P2")))
BEATS["C-05a"] = c_05a
def c_06a(): return seed("C-06a", "her on the landing", "the straps", [   # Fix 2026-09-29: "wrong product, person, location all are wrong" — person and place from the talking heads
    "EXACTLY the same woman and the same spot as in the attached talking-head frame: the top of her stairs on the carpeted upstairs landing — beige carpet, the white balusters and dark oak handrail going down on her right, "
    "a framed family photo on the warm greige wall behind her left, the window at the end of the landing. She — " + NID + ", the same face as in that frame and her reference sheet — in " + WARD["N-TODAY"] + ", "
    "is framed from mid-thigh up, standing a step back from a propped phone, and holds up TWO small straps toward the lens at chest height, one in each hand, each lying HORIZONTAL across her fingers, the shell's wordmark facing the lens, "
    "the black knit band drooping below each as a short loop. Each strap is SMALL: its shell is no longer than her hand from wrist to fingertip and only about as tall as two of her fingers are wide; "
    "the two straps together are narrower than her chest. Caught lifting them a little, smiling. " + prod("held")],
    "her", "midday light from the landing window, bright and soft", PNEG.replace(", no second strap unless stated", "") + ", no third strap, no single strap, no selfie arm, no strap as big as her face, no strap longer than her hand, no strap held vertically, no hall below, no front door, no different woman",
    R(("Talking-head frame (person + landing)", "THF"), ("N sheet", "N"), *PR_REFS["held"]))
BEATS["C-06a"] = c_06a
def c_07a(): return seed("C-07a", "her going out", "her", [   # Fix 2026-09-29: "should be a productive broll"
    "On " + STREET + ". She — " + NID + ", exactly as in her attached reference sheet — in " + WARD["N-D7"] + ", a straw sun hat on and a handbag on her arm, "
    "comes briskly down her own porch steps into the morning sun, facing forwards, hands free, caught mid-step, one sneaker landing on the path. The strap on her right knee below the hem of her skirt. " + prod("worn")],
    "her and the porch", MORN, PNEG + ", no hands on the rail, no looking at the camera, no box, no offer text",
    R(("N sheet", "N"), ("P6-STREET plate", "P6"), *PR_REFS["worn"]), house=False, height="low", side="three-quarter")
BEATS["C-07a"] = c_07a
def c_09a(): return seed("C-09a", "her hand and the box", "her hand and the card", [
    "Close on her kitchen table, " + KITCH + ": the closed matte-black box with the lowercase grey stryde wordmark centred on the lid, and a small white card lying on it." + BOXSIZE + " Her hand — deep brown skin, a plain wedding band, the cuff of her lilac long-sleeve cotton top at the wrist — "
    "writes on the card with a pen, caught mid-stroke; the writing is a short handwritten name, loose and not readable."],
    "her hand", MORN_K, "no oversized box, no box bigger than her forearm, no readable handwriting, no other text, no offer text, no stickers",
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
