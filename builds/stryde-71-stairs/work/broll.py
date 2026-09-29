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
WARD = {
 "N-D1": "a faded blue floral house dress falling to the knee, a grey cardigan and pink terry slippers",
}
N = SUBJ["N"]
M1 = ("no AI face, no plastic skin, no waxy skin, no extra fingers, no fused fingers, no melted hands, no deformed limbs, "
      "no warped background, no CGI look, no fake commercial gloss, no over-saturated colors, no vignette, no moody dark grade")
GREY = "a grey, overcast morning — flat, cool daylight, the problem days, plain and unflattering but never dark"
KITCH = "the same kitchen as the attached kitchen photo — cream vinyl tile, oak cabinets, the round table under the south window"
CLINIC = "the same exam room as the attached clinic photo — the padded table with its paper roll, the half-open blind, pale blue-grey walls"

def prop_ref():
    return S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", PROP_N_CARRIED)

def seed(beat, subject_word, focus_name, prose, light_subject, quality, neg, refs, house=True, side=None, through=None):
    r = dict(ROWS[beat]); r["angle"] = dict(r["angle"])
    if side: r["angle"]["side"] = side          # the act-map side word, corrected where it contradicts the staging
    a = angle_line(r, subject_word)
    if through: a = a.replace("looking past the white balusters", "looking past " + through)
    lt = light_line(r, light_subject, quality)
    if not r.get("face"):                        # no face in frame: the light line keeps the source and direction only
        lt = lt.replace(", so the face has a lit side toward " + {"L": "left", "R": "right", "back": "back", "front": "front"}[r["light"]["key_side"]] + " and a softer shadow side, with a small catchlight in the eyes", "")
    body = [S("CAM-LOCK"), a, focus_line(r, focus_name)]
    if house: body.append(prop_ref())
    body += prose
    body += [lt, S("CAP-FILE"),
             "AVOID: " + ", ".join([S("NEG-FILE"), M1, neg])]
    return dict(model=MODEL[r["model"]], refs=refs, body=body)

BEATS = {}

# ---------------------------------------------------------------- Act 1 — the problem days (N-D1, grey mornings)
def p_01a():
    return seed("P-01a", "her on the stairs", "her", [
      "Her staircase, exactly as in the attached hall photo: the straight open flight with the worn beige runner, the white balusters and dark oak handrail, the photo wall of framed family portraits. "
      "Seen from the top of the stairs looking down the flight. A woman of seventy-one — " + N["markers"] + ", exactly as in her attached reference sheet — is three steps down, "
      "going down her own stairs backwards: facing up the stairs toward the landing, both hands gripping the dark oak handrail, head bowed to watch her feet, her face mostly hidden. "
      "Caught mid-step: her right foot already lowered onto the step below and taking her weight, her left foot still on the step above, knees bent, careful and slow. "
      "She is wearing " + WARD["N-D1"] + ". The hall below is dim; nothing tidied."],
      "her and the stairs", GREY,
      "no fast movement, no stumbling, no fall, no one else on the stairs, no stairlift, no walking stick, no knee brace, no product, no smiling, no different staircase from the hall photo, no turn in the stairs",
      [("N sheet", REF["N"]), ("P0-PROP-N plate", REF["P0"])], side="front")
BEATS["P-01a"] = p_01a

def p_01b():
    return seed("P-01b", "her feet on the stairs", "her feet", [
      "Close on the stairs from the side, the lens at the height of the steps: two carpeted treads of the worn beige runner with their white-painted risers, a white baluster and the dark oak handrail post at the edge of the frame. "
      "Her feet in pink terry slippers, bare ankles, the hem of a faded blue floral house dress just in frame: she is going down backwards, her heels toward the bottom of the stairs. "
      "Caught mid-step: her left slipper is lowering onto the next step down, toes still on the edge of the step above, her right foot planted, both feet flat and careful. Only her feet and ankles in frame."],
      "her feet and the steps", GREY,
      "no full body, no face, no fast movement, no stumbling, no bare feet, no shoes, no knee brace, no product, no different carpet from the hall photo",
      [("P0-PROP-N plate", REF["P0"])])
BEATS["P-01b"] = p_01b

def p_02a():
    return seed("P-02a", "the empty staircase", "everything", [
      "Her staircase, exactly as in the attached landing and hall photos, seen from the top landing looking down the whole straight flight through the white balusters: "
      "the worn beige runner, the dark oak handrail, the photo wall of family portraits running down on the left, the front door closed at the bottom. "
      "Nobody on the stairs. The hall below is dim and still, a cardigan over the newel post; a strip of grey light from the landing window lies across the top steps."],
      "the staircase", GREY,
      "no people, no person on the stairs, no open door, no bright sunlight, no different staircase from the landing and hall photos, no turn in the stairs",
      [("P1-LANDING plate", REF["P1"]), ("P0-PROP-N plate", REF["P0"])])
BEATS["P-02a"] = p_02a

def p_03a():
    return seed("P-03a", "her right knee", "her hands", [
      "Close on her lap at the kitchen table, " + KITCH + ", looking down the way she sees it herself. "
      "Her right knee is bare, the hem of her faded blue floral house dress pushed up above it. A black hinged knee brace with metal side hinges and velcro straps, an ordinary unbranded one, "
      "has slid down her leg and sags below the kneecap. Caught mid-pull: both her hands grip the top of the brace and are hauling it back up, the fabric bunching and the straps twisted, the brace already starting to slip again. "
      "Deep brown skin on her knee and hands, fine creases, a plain wedding band."],
      "her knee and hands", GREY,
      "no face, no logo on the brace, no brand name, no readable text, no knee strap, no product, no bandage, no swelling, no injury, no hands inside the brace",
      [("N sheet", REF["N"]), ("P2-KITCHEN plate", REF["P2"])])
BEATS["P-03a"] = p_03a

def p_03b():
    return seed("P-03b", "her right ankle", "the brace around her ankle", [
      "Close to the floor of her kitchen, " + KITCH + ", the lens a few centimetres above the cream vinyl tile under the table. "
      "Her right foot in a pink terry slipper, and above it the same black hinged knee brace has slid all the way down her leg and sits bunched around her ankle, twisted, its velcro straps hanging loose. "
      "The hem of her faded blue floral house dress and her bare calf in frame. Caught as she shifts her foot a little on the tile. Evening: the light is low and fading."],
      "her foot and ankle", "the last low daylight of the evening, dimmer and warmer than the morning, still plain",
      "no face, no logo on the brace, no readable text, no knee strap, no product, no injury, no swelling",
      [("N sheet", REF["N"]), ("P2-KITCHEN plate", REF["P2"])])
BEATS["P-03b"] = p_03b

def p_04a():
    return seed("P-04a", "her on the treatment table", "the therapist's hands on her knee", [
      "In a physical therapy exam room, " + CLINIC + ". She lies on her back on the padded table — " + N["markers"] + ", exactly as in her attached reference sheet — "
      "in her faded blue floral house dress hitched above the knee, her head on the paper-covered pillow, looking at the ceiling, patient and tired. "
      "A physical therapist in navy scrubs, only his forearms and hands and the side of his torso in frame, holds her right leg: one hand under her calf, one on the front of her bare knee. "
      "Caught mid-bend: her right knee is bent to about ninety degrees and he is easing it a little further."],
      "her and the therapist's hands", "even afternoon daylight through the half-open blind, clinical and plain",
      "no therapist's face, no second patient, no machines, no readable text, no posters with words, no knee strap, no product, no smiling, no pain grimace",
      [("N sheet", REF["N"]), ("P7-CLINIC plate", REF["P7"])], house=False)
BEATS["P-04a"] = p_04a

def p_04b():
    return seed("P-04b", "the kitchen table", "her hand and the pills", [
      "Looking straight down at her kitchen table, " + KITCH + ": three orange prescription pill bottles with white caps and plain white labels with no readable writing, a silver blister pack half used, "
      "a white coffee mug with a ring of cold coffee, reading glasses, the worn wood of the table. Her left hand — deep brown skin, a plain wedding band — is cupped open and her right hand tips one bottle over it: "
      "caught as two small white tablets drop into her palm."],
      "her hands and the table", GREY,
      "no face, no readable labels, no brand names, no text, no knee strap, no product, no spilled pills everywhere",
      [("N sheet", REF["N"]), ("P2-KITCHEN plate", REF["P2"])])
BEATS["P-04b"] = p_04b

def p_04c():
    return seed("P-04c", "her right knee and the doctor's hands", "the needle and the gloved hands", [
      "Close on her bare right knee from the side, on the paper-covered exam table of " + CLINIC + ". Her skin deep brown, the hem of her faded blue floral house dress pushed up, a fresh wipe of antiseptic shining on the outer side of the knee. "
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
      "Her hand, deep brown skin with a plain wedding band, has just let go of one more grey elastic sleeve: caught mid-drop, a few centimetres above the pile."],
      "her hand and the pile", GREY,
      "no face, no logos, no brand names, no readable text or labels, no knee strap, no product, no new-looking packaging",
      [("N sheet", REF["N"]), ("P2-KITCHEN plate", REF["P2"])])
BEATS["P-04d"] = p_04d

def p_05a():
    return seed("P-05a", "her at the kitchen table", "her", [
      "Seen from the next room through the open kitchen doorway, the white casing soft at the edge of the frame: " + KITCH + ". "
      "She sits alone at the table in profile — " + N["markers"] + ", exactly as in her attached reference sheet — in her faded blue floral house dress and grey cardigan, "
      "among orange pill bottles, a heap of knee braces and sleeves and a mug of cold coffee, her hands in her lap, looking at nothing out of the window. "
      "Caught mid-breath: a long breath out, her shoulders dropping."],
      "her", GREY,
      "no smiling, no crying, no tears, no looking at the camera, no second person, no knee strap, no product, no bright sunlight",
      [("N sheet", REF["N"]), ("P2-KITCHEN plate", REF["P2"]), ("P0-PROP-N plate", REF["P0"])], through="the white casing of the open kitchen doorway")
BEATS["P-05a"] = p_05a

if __name__ == "__main__":
    out = HERE / "prompts"; out.mkdir(exist_ok=True)
    for b in sys.argv[1:] or BEATS:
        dd = BEATS[b](); p = "\n\n".join(dd["body"])
        (out / f"{b}.t2i.txt").write_text(p)
        (out / f"{b}.refs.json").write_text(json.dumps(dict(model=dd["model"], refs=[(k, str(v.relative_to(B))) for k, v in dd["refs"]]), indent=1))
        print(b, dd["model"], len(p), "chars", [k for k, _ in dd["refs"]])
