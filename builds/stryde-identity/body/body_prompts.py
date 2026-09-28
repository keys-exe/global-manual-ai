#!/usr/bin/env python3
"""Body B-roll start images (act map STEP4_5.md rows MECH-01 … BR-26b) — Kie GPT Image prompts + refs.

Writes body/<BEAT>.t2i.txt and body/body_v1.json ({beat: {refs, prompt, line, clip_s}}).
Wardrobe from the Wardrobe Ledger (§14A), product blocks from the product sheet strings,
anatomy from Appendix A (ANAT-BASE + ANAT-LIGHT + ANAT-FIELD + ANAT-A/B) with the product sheet slots.
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "products/stryde"))
import stryde_product_sheet as P  # noqa: E402

LENGTHS = {r["beat"]: r for r in json.loads((HERE.parent / "work/body_lengths.json").read_text())}

CAP = ("Shot on an iPhone 17 Pro Max, handheld, the main camera at 24mm equivalent, everything left on automatic. "
       "An ordinary photo taken on an ordinary phone.")
FILE = ("An unremarkable photograph off a phone: nobody lit it or arranged it, sharpness uneven across the frame, "
        "soft edges, faint compression in the shadows, no grading, no retouching.")
AVOID_BASE = ("no text on screen, no captions, no logos other than the stryde wordmark, no extra fingers, no fused fingers, "
              "no AI face, no plastic skin, no polished render, no advertising image, no studio lighting, no vignette")

PRODUCT = ("The strap exactly as in the two attached product photos: a rigid matte-black shell, its top edge rising into two "
           "matching rounded peaks either side of a concave notch, the lowercase grey stryde wordmark horizontal beneath the "
           "notch, a brushed chrome slide with three dotted chevrons at each end, and a black coarse-knit elastic band about half "
           "the shell's height with two small matte-black keeper loops.")
WORN = ("The strap is worn on the RIGHT leg ON THE PATELLAR TENDON, directly BELOW the kneecap, centred on the FRONT of the knee: "
        "the concave notch cups the kneecap's lower border with no gap, the two peaks no higher than the base of the kneecap's "
        "sides, the kneecap's face bare above, a chrome slide at each outer side of the leg, the band running round behind the "
        "knee, snug and flat on bare skin, the wordmark horizontal and readable. " + P.SIZE_WORN)
WORN_NEG = ("no strap on the left knee, no second strap, no shell on the thigh, no shell on the kneecap, no shell low on the shin, "
            "no shell rotated to the side, no slide on the front of the knee, no strap over clothing, no loose band tail")
HELD_NEG = ("no fingers on the chrome slides, no fingers across the wordmark, no hands on the band, no twisted shell, no bent shell, "
            "no strap held upright on its end, no second strap, no buckles, no velcro, " + P.NEG_ADJUST)

C1 = ("THE SAME WOMAN exactly as in the attached character sheet — Maureen, seventy-four, soft-featured, silver hair — unchanged "
      "in face, age and build.")
C2 = ("THE SAME MAN exactly as in the attached character sheet — Dean, fifty-eight, barrel-chested and heavyset, thick forearms — "
      "unchanged in face, age and build.")
C3 = ("THE SAME WOMAN exactly as in the attached character sheet — Pat, sixty-six, sturdy and compact, strong shoulders — unchanged "
      "in face, age and build.")
C4 = ("THE SAME MAN exactly as in the attached character sheet — the orthopaedic surgeon, seventy-one, tall and slightly stooped, "
      "broad square jaw, close white hair at the sides, broad hands with long fingers — unchanged in face, age and build.")

SKIN_OLD = "Real unretouched skin: age spots, fine creases, fine hairs, visible pores, the band pressing a shallow dent into the flesh."

ANAT_SLOTS = {"[REGION]": "knee", "[STACK]": "quadriceps, hamstrings and calf", "[BONES]": "femur, patella and tibia",
              "[TARGET]": "the patellar tendon", "[TARGET JOINT]": "the knee joint",
              "[SITE]": "the patellar tendon immediately below the kneecap"}
ANAT_BASE = ("Premium 3D anatomical visualisation for medical education, broadcast-quality CGI render, cinematic and clean. "
             "Vertical composition. A stylised anatomical model of a single [REGION] viewed from a low three-quarter angle, "
             "foreshortened, [TARGET JOINT] sitting slightly off-centre and dominating the frame, the limb falling away out of frame "
             "at both ends. Deep near-black background with a faint cool blue tint. The outer body contour is a very faint "
             "translucent glass-like shell, barely visible, so the silhouette reads clearly as human. Rich, premium, cinematic.")
ANAT_LIGHT = ("Three-source render lighting, never flat ambient: a cool pale-cyan key raking across the form from upper camera-left, "
              "a low warm amber bounce from beneath picking out the underside of the bone, and a bright cool rim tracing the "
              "translucent silhouette. The limb is fully and evenly lit along its whole visible length, every structure readable "
              "end to end. Shallow depth of field, [TARGET] crisp. Light scatters volumetrically through the translucent tissue. "
              "Clean satin specular sheen on [TARGET] and the bone surfaces.")
ANAT_FIELD = ("The near-black field carries very faint drifting particulate at depth and a subtle tonal gradient across frame. "
              "Never a flat empty black.")
ANAT_A = ("Inside the model, the full muscle groups — [STACK] — in natural anatomical colour: warm red, deep rose and muted brick, "
          "semi-transparent and layered so deeper structures remain visible, soft inner glow at the thinner edges, broad directional "
          "grain along each belly, never individual fibres. [BONES] sit deepest, warm ivory-gold with soft low inner luminosity.")
ANAT_B = ("Inside the model, no muscle layer — the interior is soft empty translucency. Only [BONES] and [TARGET]. Bones in warm "
          "ivory-gold with soft low inner luminosity; [TARGET] in pearly ivory-white, dense, running its full length between its "
          "attachments. Clean and uncluttered.")
ANAT_NEG = ("no text, no labels, no arrows, no diagram lines, no glow on the tibial tuberosity, no glow spreading down the shin, "
            "no skin, no clothing, no real person, no blood, no gore, no second limb, no textbook flat illustration, no white background")


def anat(parts):
    t = " ".join(parts)
    for k, v in ANAT_SLOTS.items():
        t = t.replace(k, v)
    return t


def photo(shot, subject, product, light, avoid, skin=SKIN_OLD):
    return "\n\n".join(x for x in [CAP, shot, subject, product, skin, "Light: " + light, FILE, "AVOID: " + avoid + ", " + AVOID_BASE] if x)


ROWS = {}

# ── Act A — mechanism ────────────────────────────────────────────────────────
ROWS["MECH-01"] = (["front", "back"], anat([ANAT_BASE, ANAT_LIGHT, ANAT_FIELD, ANAT_A,
    "STATE — THE LOAD IS ARRIVING. The knee is mid-stride with the foot planted and the limb carrying the body's weight: [STACK] "
    "compressed and [TARGET] drawn taut. A near-white glow is already established at [SITE], mid-intensity, clearly the brightest "
    "element in frame, a faint wave of warm light running down through the femur toward it from above.", P.ANAT_A_POINT_TIGHT,
    "AVOID: " + ANAT_NEG]))
ROWS["MECH-02"] = (["front", "back"], anat([ANAT_BASE.replace("foreshortened, [TARGET JOINT] sitting slightly off-centre and dominating the frame",
    "framed tight on the front of [TARGET JOINT], the kneecap and the tendon below it filling the middle of the frame"),
    ANAT_LIGHT, ANAT_FIELD, ANAT_A,
    "STATE — ONE SMALL SPOT. The glow sits on [SITE] only, a single tight near-white point on the tendon just below the kneecap, "
    "the kneecap above it and the tibia below it calm.", P.ANAT_A_POINT_TIGHT, "AVOID: " + ANAT_NEG]))

# ── Act B ────────────────────────────────────────────────────────────────────
ROWS["BR-03"] = (["C4", "P2", "front", "back"], photo(
    "A medium close-up across the desk from eye level, three-quarter front, the phone propped against a book on the desk: the surgeon "
    "sits at his desk and turns the strap in the window light beside the plastic knee model on the desk. His face is in frame, calm, "
    "looking down at the strap. THE SAME CONSULTING ROOM exactly as in the second attached image — window on the left, the lightbox "
    "and bookshelf behind, softly out of focus.",
    C4 + " Wearing a white button-down shirt under a charcoal knitted waistcoat, charcoal trousers, a clinic lanyard with a blank card.",
    PRODUCT + " He holds it by its bottom edge, thumb in front below the wordmark and fingers behind on the pad, the front face "
    "turned to the window. " + P.SIZE_HELD,
    "cool daylight from the window on the left, the lightbox glowing softly behind.", HELD_NEG, skin=""))
ROWS["BR-04"] = (["P2", "front", "back", "worn_front"], photo(
    "An extreme close-up from a low angle beside the examination couch, looking along the couch: a patient's right knee lies straight "
    "on the blue couch with its white paper roll, the strap seated on it; the surgeon's index fingertip rests on the skin just beside "
    "the notch, pointing to where it sits. Only the knee, the top of the shin, the hem of grey running shorts and one fingertip in frame. "
    "The consulting room from the first attached image behind, far out of focus.",
    "The patient is a man in his sixties, knee only: grey running shorts, pale hairy leg. The surgeon's hand: broad, long-fingered, a "
    "white shirt cuff.",
    PRODUCT + " " + WORN + " Seated exactly as in the last attached worn reference.",
    "cool window daylight from the left, soft.", WORN_NEG + ", no face, no second hand gripping the strap"))
ROWS["BR-05"] = (["front", "back"], photo(
    "A close-up from overhead at a slight angle onto a pale wooden kitchen table in an ordinary home: two straps lie side by side, "
    "shells face up. Two hands in oatmeal long-sleeve cuffs rest at the table edge, the right index finger touching the smaller one.",
    "Anonymous hands of a woman in her sixties, oatmeal long-sleeve tee cuffs.",
    "On the LEFT, the real strap exactly as in the two attached product photos, perfect, undamaged. On the RIGHT, " + P.FAKE_BASE + " "
    "On top of that: " + dict(P.FAKE_ARCHETYPES)["too small"] + " — visibly smaller than the real one beside it.",
    "soft window daylight across the table.",
    P.NEG_FAKE_HERO + ", no packaging, no price tags, no third strap"))
ROWS["BR-06"] = (["C4", "P2", "front", "back"], photo(
    "A close-up from chest height across the desk: only the surgeon's two hands and the strap in frame, held up in front of his navy "
    "waistcoat, the strap turned round so its back faces the camera. The consulting room behind, far out of focus.",
    "The surgeon's hands exactly as in the attached character sheet: broad, long fingers, white shirt cuffs under a charcoal knitted "
    "waistcoat.",
    P.PAD_BACK_SHOT + " The strap exactly as in the last attached product photo (the back). Both hands hold it at its two ends by "
    "the shell's edge, fingers behind, thumbs on the lower edge. " + P.SIZE_HELD,
    "cool window daylight from the left.", HELD_NEG.replace("no fingers across the wordmark, ", "") + ", no wordmark visible", skin=""))
ROWS["MECH-07"] = (["front", "back"], anat([ANAT_BASE, ANAT_LIGHT, ANAT_FIELD, ANAT_A,
    "PROTECTION — THE PAD CATCHES THE FORCE. The strap is worn on the model exactly as in the attached product photos, its matte-black "
    "shell on [SITE], the band round the back of the knee. The load arriving from above lights the pad with a soft cool-white glow that "
    "spreads outward across the width of the shell and away to its two ends, carried off the tendon; [SITE] beneath it stays calm and "
    "dark.", "AVOID: " + ANAT_NEG + ", no glow on the tendon under the shell, no strap on the thigh"]))
ROWS["BR-08"] = (["C3", "P5", "front", "back", "worn_front"], photo(
    "A medium-wide from a three-quarter front angle at hip height in the gait lab: Pat walks on the treadmill, legs in frame from the "
    "waist down, the strap on her right knee; a sports scientist stands beside the treadmill with a tablet, watching her knee. THE SAME "
    "GAIT LAB exactly as in the second attached image.",
    C3 + " Wearing a coral technical polo, black running shorts ending just above the knee, grey running trainers, a fitness watch. "
    "The scientist: a man in his forties, blue gingham check shirt, navy chinos, a lanyard with a blank card, face turned to the knee.",
    PRODUCT + " " + WORN, "cool fluorescent overhead light with a high window.", WORN_NEG + ", no readable screen, no readable tablet"))
ROWS["BR-09"] = (["C3", "P5", "front", "back", "worn_front"], photo(
    "An extreme close-up at knee height from the side of the treadmill, three-quarter front: Pat's right knee mid-stride on the moving "
    "belt, from just above the kneecap to the top of the shin, the hem of black running shorts at the top edge. The treadmill rail and "
    "the gait lab from the second attached image softly out of focus behind.",
    C3 + " Black running shorts ending just above the knee.", PRODUCT + " " + WORN,
    "cool fluorescent overhead light.", WORN_NEG + ", no face, no hands"))

# ── Act C ────────────────────────────────────────────────────────────────────
ROWS["MECH-10"] = (["front"], anat([ANAT_BASE, ANAT_LIGHT, ANAT_FIELD, ANAT_B,
    "CONDITION — BONE ON BONE. Inside the knee joint the gap between the femur and the tibia has narrowed to almost nothing, the "
    "cartilage worn thin, the two bone ends nearly touching, a faint dull amber warmth where they meet.", "AVOID: " + ANAT_NEG + ", no strap"]))
ROWS["MECH-11"] = (["front"], anat([ANAT_BASE.replace("low three-quarter angle", "low front angle"), ANAT_LIGHT, ANAT_FIELD, ANAT_B,
    "CONDITION — WORN CARTILAGE AND MENISCUS. The pale cartilage lining the bone ends is thinned and frayed in patches, and the "
    "crescent-shaped meniscus between the femur and tibia shows a small tear at its inner edge, picked out in a faint dull amber.",
    "AVOID: " + ANAT_NEG + ", no strap"]))
ROWS["BR-12"] = (["C3", "front", "back", "worn_front"], photo(
    "A medium-wide from a low angle beside the park path, three-quarter front: Pat walking briskly along the tarmac path past the "
    "green-painted park railings, a long stride, full figure from head to trainers, sunlit grass and trees behind.",
    C3 + " Wearing a navy-and-cream Breton long-sleeve top, a rust quilted gilet, khaki shorts ending just above the knee, white canvas "
    "trainers.", PRODUCT + " " + WORN + " At this distance the strap reads small but clear on her right knee.",
    "bright sun, soft shadows under the trees.", WORN_NEG))
ROWS["BR-13"] = (["C1", "P0", "front", "back", "worn_front"], photo(
    "A medium-wide from the hall at the foot of the stairs, low angle looking up: Maureen climbing the carpeted stairs, mid-step, her "
    "right hand lifted clear of the mahogany handrail, not holding it. The stairs rise on the LEFT of frame. THE SAME HALL AND STAIRS "
    "exactly as in the second attached image.",
    C1 + " Wearing a burgundy long-sleeve jersey tunic, a denim skirt ending a hand above the knee, sheepskin slippers.",
    PRODUCT + " " + WORN, "soft east morning daylight through the front-door glass.", WORN_NEG + ", no hand gripping the rail"))
ROWS["BR-14"] = (["C1", "P0", "front", "back", "worn_front"], photo(
    "A medium close-up on the landing at eye level, three-quarter front: Maureen pausing at the top of the stairs, calm, her right palm "
    "resting lightly on her thigh just above the kneecap, the strap below it. The landing and the top of the handrail from the second "
    "attached image behind.",
    C1 + " Wearing a burgundy long-sleeve jersey tunic, a denim skirt ending a hand above the knee, sheepskin slippers.",
    PRODUCT + " " + WORN, "soft daylight from the landing window.", WORN_NEG + ", no pained face, no hand on the strap"))
ROWS["MECH-15"] = (["front", "back"], anat([ANAT_BASE, ANAT_LIGHT, ANAT_FIELD, ANAT_A,
    "PROTECTION — THE SITE CALM. The strap is worn on the model exactly as in the attached product photos, its shell on [SITE]. The "
    "pad holds a soft steady cool-white glow across the width of the shell, carrying the load; the tendon beneath it and the whole "
    "joint are calm, no hot spot anywhere.", "AVOID: " + ANAT_NEG + ", no hot glow on the tendon, no strap on the thigh"]))

# ── Act D ────────────────────────────────────────────────────────────────────
ROWS["BR-16"] = (["C2", "P4", "front", "back", "worn_front"], photo(
    "A medium close-up from low and in front: Dean sits on the rear step of the white van in the loading yard, right leg straight "
    "out in front, bending forward with both hands on the strap. THE SAME YARD AND VAN exactly as in the second attached image.",
    C2 + " Wearing a green-and-black check flannel shirt with the sleeves rolled, khaki cargo shorts, black steel-toe boots, a watch.",
    PRODUCT + " START OF THE SEATING MOVE: " + P.SEAT_LOCK.split(" Both hands")[0] + " Both hands hold the shell by its two sides, "
    "palms and fingertips flat on the matte shell, ready to slide it up.", "flat overcast daylight.", P.NEG_SEAT))
ROWS["BR-17"] = (["C2", "P3", "front", "back", "worn_bent"], photo(
    "A medium-wide from a low three-quarter angle in the warehouse aisle: Dean in a squat, knees bent, both hands under a cardboard "
    "box on the floor, beginning to lift it, the strap on his bent right knee. THE SAME WAREHOUSE AISLE exactly as in the second "
    "attached image, racking behind.",
    C2 + " Wearing a green-and-black check flannel shirt with the sleeves rolled, khaki cargo shorts, black steel-toe boots.",
    PRODUCT + " " + P.PLACE_BENT + " Worn exactly as in the last attached bent reference.", "high-bay LED light, daylight from the open shutter.",
    WORN_NEG))
ROWS["BR-18"] = (["C1", "P0", "front", "back", "worn_front"], photo(
    "A close-up at knee height in the hall: Maureen's hands lowering the wide leg of her navy trousers down over her right knee, the "
    "fabric half down — the strap still visible below the kneecap, the trouser leg about to cover it and lie flat. The stairs' "
    "bottom step and beige carpet from the second attached image behind.",
    C1 + " Wearing a cream roll-neck, a camel open draped cardigan, wide-leg navy trousers, brown loafers.",
    PRODUCT + " " + WORN, "soft east morning daylight from the front door.", WORN_NEG.replace(", no strap over clothing", "") + ", no face"))
ROWS["BR-19"] = (["C2", "P3", "front", "back", "worn_front"], photo(
    "A medium-wide at eye level, three-quarter front: Dean leaning back against the workbench in the warehouse aisle, a mug of tea in "
    "his hand, relaxed, the strap still in place on his right knee. THE SAME WAREHOUSE AISLE exactly as in the second attached image.",
    C2 + " Wearing a green-and-black check flannel shirt with the sleeves rolled, khaki cargo shorts, black steel-toe boots, a watch.",
    PRODUCT + " " + WORN, "high-bay LED light, late daylight from the open shutter.", WORN_NEG + ", no readable mug text"))

# ── Act E ────────────────────────────────────────────────────────────────────
ROWS["BR-20"] = (["C4", "P2", "front", "back"], photo(
    "A close-up across the desk from a slightly high angle over the patient's shoulder: the surgeon's hand passes the strap across the "
    "desk into the patient's open hand, both hands in frame. THE SAME CONSULTING ROOM exactly as in the second attached image behind.",
    "The surgeon's hand exactly as in the attached character sheet, a pale pink shirt cuff and a steel watch. The patient's hand: a man "
    "in his sixties, grey long-sleeve tee cuff, palm open.",
    PRODUCT + " The surgeon holds it by the shell's bottom edge, the front face and wordmark up. " + P.SIZE_HELD,
    "cool window daylight from the left.", HELD_NEG))
ROWS["BR-21"] = (["front", "back", "worn_front"], photo(
    "A medium-wide from a low angle beside the park path: a small group of four older walkers in their sixties and seventies passing "
    "the green-painted park railings, walking towards the camera, chatting; the nearest walker wears the strap on his right knee.",
    "The nearest walker: a man in his late sixties, sage-green T-shirt, navy walking shorts ending above the knee, walking boots, a cap. "
    "The others in ordinary walking clothes.", PRODUCT + " " + WORN.replace(" " + P.SIZE_WORN, "") + " Only the nearest walker wears one.",
    "bright sun through the trees.", WORN_NEG.replace("no second strap", "no strap on the other walkers")))
ROWS["BR-22"] = (["C1", "P1", "package_open", "front"], photo(
    "A close-up from a slightly high angle on the kitchen table with its checked cloth: the closed matte-black box sits on the table, "
    "Maureen's two hands on the lid, just beginning to lift it. THE SAME KITCHEN exactly as in the second attached image, soft behind.",
    "Maureen's hands exactly as in the attached character sheet, cornflower-blue sleeves of her cotton dress.",
    P.PACKAGE["box"].capitalize() + ". " + P.PACKAGE["logo"].capitalize() + ". The lid is closed, just lifting at the front edge.",
    "soft indirect west window light.", P.NEG_PACKAGE + ", no open box, no straps visible", skin=""))
ROWS["BR-23"] = (["C1", "P1", "package_open", "front"], photo(
    "A close-up from overhead on the kitchen table with its checked cloth: the box open, the lid set aside, the two straps lying flat "
    "in the insert exactly as in the third attached image; Maureen's fingertips at the box's front edge.",
    "Maureen's fingertips, cornflower-blue sleeve.", P.PACKAGE_LOCK, "soft indirect west window light.", P.NEG_PACKAGE, skin=""))
ROWS["BR-24"] = (["C1", "P1", "front", "back"], photo(
    "A medium close-up at eye level by the kitchen window: Maureen lifts one strap out of the open box on the table and turns it in "
    "the window light, looking at it, the open box with the second strap in front of her. THE SAME KITCHEN exactly as in the second "
    "attached image.",
    C1 + " Wearing a cornflower-blue cotton dress ending a hand above the knee.",
    PRODUCT + " She holds it by the shell's bottom edge, thumb in front below the wordmark, fingers behind on the pad, the band slack "
    "round her wrist. " + P.SIZE_HELD, "soft indirect west window light.", HELD_NEG.replace("no second strap, ", ""), skin=""))
ROWS["BR-25"] = (["C1", "P0", "front", "back", "worn_front"], photo(
    "A medium-wide from behind her and a little to the side, at eye level in the hall: Maureen at the foot of the stairs, looking up, "
    "her right foot on the first step, the strap on her right knee. The stairs rise on the LEFT of frame. THE SAME HALL AND STAIRS "
    "exactly as in the second attached image.",
    C1 + " Wearing a cornflower-blue cotton dress ending a hand above the knee, navy slip-on shoes.",
    PRODUCT + " " + WORN, "soft east morning daylight through the front-door glass.", WORN_NEG))
ROWS["BR-26a"] = (["C1", "P0", "front", "back", "worn_front"], photo(
    "A medium close-up from low and in front: Maureen sits on the bottom stair, her right leg straight out, bending forward with "
    "both hands on the strap on her shin. The hall from the second attached image behind.",
    C1 + " Wearing a cornflower-blue cotton dress ending a hand above the knee, navy slip-on shoes.",
    PRODUCT + " START OF THE SEATING MOVE: " + P.SEAT_LOCK.split(" Both hands")[0] + " Both hands hold the shell by its two sides, "
    "palms and fingertips flat on the matte shell, ready to slide it up.", "soft east morning daylight.", P.NEG_SEAT))
ROWS["BR-26b"] = (["C1", "P0", "front", "back", "worn_front"], photo(
    "A medium-wide from the landing looking down the stairs, high angle: Maureen climbing towards the camera, mid-step, her hand off "
    "the rail, the strap on her right knee. THE SAME HALL AND STAIRS exactly as in the second attached image, seen from the top.",
    C1 + " Wearing a cornflower-blue cotton dress ending a hand above the knee, navy slip-on shoes.",
    PRODUCT + " " + WORN, "soft east morning daylight from the front-door glass below.", WORN_NEG + ", no hand gripping the rail"))

REF = {"C1": "C1-MAUREEN_v1.jpg", "C2": "C2-DEAN_v1.jpg", "C3": "C3-PAT_v2.jpg", "C4": "C4-SURGEON_v2.jpg",
       "P0": "P0-PROP-M_v1.jpg", "P1": "P1-M-KITCHEN_v1.jpg", "P2": "P2-CONSULT_v1.jpg", "P3": "P3-WAREHOUSE_v1.jpg",
       "P4": "P4-YARD_v1.jpg", "P5": "P5-LAB_v1.jpg", "front": "front.webp", "back": "back.webp",
       "worn_front": "worn_front.jpg", "worn_bent": "worn_bent.jpg", "package_open": "package_open.jpg"}

if __name__ == "__main__":
    out = {}
    for beat, (refs, prompt) in ROWS.items():
        (HERE / f"{beat}.t2i.txt").write_text(prompt + "\n")
        L = LENGTHS[beat]
        out[beat] = {"refs": [REF[r] for r in refs], "prompt": prompt, "line": L["line"], "clip_s": L["clip_s"]}
    (HERE / "body_v1.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(len(out), "beats;", "longest prompt", max(len(v["prompt"]) for v in out.values()), "chars")
