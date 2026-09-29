#!/usr/bin/env python3
"""Fix round 2 (user, 2026-09-28): the 19 B-roll cards the user marked Fix — new start images from each Fix note.

User rules added this round: never a phone in any B-roll (no phone in frame, no phone named as the camera in a
video prompt), Kling video prompts in §35 JSON. Images: Higgsfield nano_banana_pro (realistic), nano_banana_2 (anatomy).
BR-16 and BR-26a get a pinned end image too (§27G rule 5: the strap changes position).

Writes body/<BEAT>.fix2.t2i.txt and body/fix2.json ({beat: {model, refs, prompt}}).
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import body_prompts as B  # noqa: E402
P = B.P

NO_PHONE = ("no phone, no smartphone, no mobile phone anywhere in the frame, no phone on the ground, no phone on a table, "
            "no phone in a hand, no camera in frame")

LOOP = ("The band is a CLOSED LOOP of soft black coarse-knit elastic joined to the shell's two chrome slides, exactly as in the "
        "attached back-view product photo: when the strap is held, the loop hangs slack and soft under its own weight below the "
        "shell, bending and sagging like fabric, never stiff, never straight, never standing out flat to the sides.")
LOOP_NEG = ("no stiff band, no band sticking straight out, no flat bar-shaped strap, no open-ended band, no band tails, "
            "no shell without its band")

STAIRS = ("THE SAME HALL AND STAIRCASE exactly as in the second attached image: a straight single flight of carpeted stairs in "
          "beige carpet with a thin brass stair rod across the back of every tread, the dark mahogany handrail on a white panelled "
          "balustrade with a square white newel post at the bottom, the flight rising away from the hall on the LEFT of frame. "
          "Every step is clearly readable as a step.")
STAIRS_NEG = "no spiral stairs, no open-tread stairs, no different staircase, no ramp, no floor where the steps should be, no missing brass rods"

MECH_SIDE = ("Viewed from the FRONT and slightly to the side, so the patellar tendon reads plainly: the thick pearly band running "
             "straight down from the lower tip of the kneecap to the bump at the top of the shin, in front of the joint.")

FIX = {}


CAP2 = ("The look of the iPhone 17 Pro Max main camera at 24mm equivalent, handheld, everything on automatic: an ordinary, "
        "candid snapshot. The camera itself is never in the picture.")
FILE2 = ("An unremarkable everyday snapshot: nobody lit it or arranged it, sharpness uneven across the frame, soft edges, faint "
         "compression in the shadows, no grading, no retouching.")


def photo(shot, subject, product, light, avoid, skin=B.SKIN_OLD):
    t = B.photo(shot, subject, product, light, avoid + ", " + NO_PHONE, skin)
    return t.replace(B.CAP, CAP2).replace(B.FILE, FILE2)


# ── mechanism (nano_banana_2) ───────────────────────────────────────────────
FIX["MECH-01"] = ("nano_banana_2", [], B.anat([B.ANAT_BASE.replace("viewed from a low three-quarter angle, foreshortened, "
    "[TARGET JOINT] sitting slightly off-centre", "viewed from the front and slightly to the side, [TARGET JOINT] sitting centre "
    "frame"), B.ANAT_LIGHT, B.ANAT_FIELD, B.ANAT_A, MECH_SIDE,
    "STATE — THE LOAD IS ARRIVING. The foot is planted and the limb carries the body's weight, [STACK] braced, [TARGET] drawn taut. "
    "The glow sits ON THE PATELLAR TENDON ITSELF, on the band between the kneecap and the shin, a near-white spot on the tendon's "
    "front surface just below the kneecap, clearly the brightest thing in frame; a faint wave of warm light runs down the thigh "
    "toward it.", P.ANAT_A_POINT_TIGHT,
    "AVOID: " + B.ANAT_NEG + ", no glow on the side of the joint, no glow between the femur and tibia, no glow on the meniscus, "
    "no glow on the kneecap, no glow behind the knee, no strap"]))

FIX["MECH-10"] = ("nano_banana_2", [], B.anat([B.ANAT_BASE, B.ANAT_LIGHT, B.ANAT_FIELD, B.ANAT_B,
    "CONDITION — BONE ON BONE, ARTHRITIS, made unmistakable. Inside the knee joint the cartilage is completely worn away: the "
    "rounded end of the femur rests DIRECTLY on the flat top of the tibia, bare bone pressing on bare bone with no gap and no "
    "cushion between them. The bone ends are rough and pitted, with small jagged bony spurs growing from their edges. At the point "
    "where they grind together a hot, angry red-orange glow burns, clearly the brightest thing in frame, a little heat haze around "
    "it; the rest of the joint stays cool ivory.",
    "AVOID: " + B.ANAT_NEG + ", no healthy joint space, no smooth cartilage, no strap"]))

FIX["MECH-15"] = ("nano_banana_2", ["front", "back"], B.anat([B.ANAT_BASE, B.ANAT_LIGHT, B.ANAT_FIELD, B.ANAT_A,
    "PROTECTION — THE SITE CALM. The strap is worn on the model exactly as in the attached product photos, its matte-black shell on "
    "[SITE]. A soft, low, steady pale-cyan glow lies across the pad — dim, never white, never bright, never flaring — carrying the "
    "load; the tendon beneath and the whole joint are calm, no hot spot anywhere. The frame is evenly dark and settled from the start.",
    "AVOID: " + B.ANAT_NEG + ", no white glow, no white flash, no bright white light, no overexposed area, no bloom, no hot glow on "
    "the tendon, no strap on the thigh"]))

# ── Act B ────────────────────────────────────────────────────────────────────
FIX["BR-03"] = ("nano_banana_pro", ["C4", "P2", "front", "back"], photo(
    "A medium close-up across the desk from eye level, three-quarter front: the surgeon sits at his desk beside the plastic knee "
    "model and holds the strap up in the window light, looking at it. His face is in frame, calm. THE SAME CONSULTING ROOM exactly "
    "as in the second attached image — window on the left, the lightbox and bookshelf behind, softly out of focus.",
    B.C4 + " Wearing a white button-down shirt under a charcoal knitted waistcoat, charcoal trousers, a clinic lanyard with a "
    "blank card.",
    B.PRODUCT + " He holds it by the shell's bottom edge in one hand, thumb in front below the wordmark, fingers behind on the pad, "
    "the front face turned to the window. " + LOOP + " " + P.SIZE_HELD,
    "cool daylight from the window on the left, the lightbox glowing softly behind.", B.HELD_NEG + ", " + LOOP_NEG, skin=""))

FIX["BR-04"] = ("nano_banana_pro", ["P2", "front", "back", "worn_front"], photo(
    "A close-up from a low angle at the foot of the examination couch, looking up along it: a patient lies on his back on the blue "
    "couch with its white paper roll, his right leg straight, the strap seated on the knee in the foreground. The surgeon's index "
    "fingertip touches the bare skin of the patellar tendon in the small space between the lower tip of the kneecap and the "
    "strap's centre notch — pointing straight at that one spot, from above, the fingertip resting on it. THE WHOLE PATIENT IS "
    "THERE: behind the knee, softly out of focus, his thigh runs up into grey running shorts, his hips, stomach and chest in a navy "
    "T-shirt along the couch, his head on the couch's pillow at the far end; his left leg lies beside the right. The consulting "
    "room from the first attached image behind, far out of focus.",
    "The patient is a man in his sixties, his whole body lying on the couch: navy T-shirt, grey running shorts, pale hairy legs, "
    "firm real leg muscle. The surgeon's hand: broad, long-fingered, a white shirt cuff.",
    B.PRODUCT + " " + B.WORN + " Seated exactly as in the last attached worn reference. The shell is hard moulded plastic.",
    "cool window daylight from the left, soft.",
    B.WORN_NEG + ", no finger at the side of the knee, no finger on the strap's end, no finger on the kneecap's face, no cut-off "
    "body, no missing torso, no floating leg, no second hand"))

FIX["BR-06"] = ("nano_banana_pro", ["C4", "P2", "back", "front"], photo(
    "A close-up from chest height across the desk: only the surgeon's two hands and the strap in frame, held up in front of his "
    "charcoal waistcoat, the strap turned so its INSIDE faces the camera, exactly as in the first attached product photo (the back "
    "view). The consulting room behind, far out of focus.",
    "The surgeon's hands exactly as in the attached character sheet: broad, long fingers, white shirt cuffs under a charcoal "
    "knitted waistcoat.",
    "The whole strap exactly as in the attached back-view product photo: a CLOSED LOOP — the rigid matte-black shell at the top of "
    "the loop with its two rounded peaks and centre notch, a brushed chrome slide at each end of the shell, and the black "
    "coarse-knit elastic band running from both slides down and round in a closed loop with its two small keeper loops at the "
    "bottom. Seen from inside the loop: the inner face of the shell is the smooth matte-black pad that sits against the skin, "
    "filling the upper middle of the frame. " + P.PAD_BACK_SHOT.split(" -- ")[0] + ". He holds the loop open with one hand on "
    "each chrome-slide end of the shell, fingers behind the shell, thumbs on its lower edge, the band loop hanging softly below. "
    + P.SIZE_HELD,
    "cool window daylight from the left.",
    B.HELD_NEG.replace("no fingers on the chrome slides, ", "").replace("no fingers across the wordmark, ", "")
    + ", no wordmark visible, no flat panel without a band, no shell on its own, no open-ended band, " + LOOP_NEG, skin=""))

# ── Act C ────────────────────────────────────────────────────────────────────
FIX["BR-12"] = ("nano_banana_pro", ["C3", "front", "back", "worn_front"], photo(
    "A medium-wide from a low angle beside the park path, three-quarter front: Pat walking briskly along the tarmac path past the "
    "green-painted park railings, a long stride, full figure from head to trainers, sunlit grass and trees behind. The path is "
    "clear and empty in front of her.",
    B.C3 + " Wearing a navy-and-cream Breton long-sleeve top, a rust quilted gilet, khaki shorts ending just above the knee, "
    "white canvas trainers. Both hands empty, swinging.",
    B.PRODUCT + " " + B.WORN + " At this distance the strap reads small but clear on her right knee.",
    "bright sun, soft shadows under the trees.", B.WORN_NEG + ", no objects on the path"))

FIX["BR-13"] = ("nano_banana_pro", ["C1", "P0", "front", "back", "worn_front"], photo(
    "A medium-wide from the hall floor beside the newel post, low three-quarter angle looking up the flight: Maureen is ON THE "
    "STAIRS, climbing, her left foot on the third step and her right foot lifting onto the fourth, her whole body on the flight, "
    "her right hand lifted clear of the mahogany handrail, not holding it. " + STAIRS,
    B.C1 + " Wearing a burgundy long-sleeve jersey tunic, a denim skirt ending a hand above the knee, sheepskin slippers.",
    B.PRODUCT + " " + B.WORN + " The strap on her right knee faces the camera as she climbs.",
    "soft east morning daylight through the front-door glass.",
    B.WORN_NEG + ", no hand gripping the rail, " + STAIRS_NEG + ", no woman standing in the hall, no woman on the landing"))

FIX["BR-14"] = ("nano_banana_pro", ["C1", "P0", "front", "back", "worn_front"], photo(
    "A medium shot from the landing at eye level, three-quarter front: Maureen arriving at the top of the stairs carrying a full "
    "wicker laundry basket against her hip in both hands, stepping up onto the landing easily, a small contented smile — busy, "
    "getting on with her day. The top of the mahogany handrail and the stairs dropping away behind her. " + STAIRS.replace(
        "the flight rising away from the hall on the LEFT of frame", "seen from the top"),
    B.C1 + " Wearing a burgundy long-sleeve jersey tunic, a denim skirt ending a hand above the knee, sheepskin slippers.",
    B.PRODUCT + " " + B.WORN, "soft daylight from the landing window.",
    B.WORN_NEG + ", no pained face, no hand on the knee, no hand on the rail, " + STAIRS_NEG))

# ── Act D ────────────────────────────────────────────────────────────────────
SEAT_START = ("START OF THE SEATING MOVE: the strap is already closed and formed, sitting LOW on the front of his shin, about a "
              "hand's width below the kneecap — clearly off position, the kneecap and the tendon below it bare above it. Both hands "
              "hold the shell by its two ends, palms and fingertips flat on the matte shell, ready to slide it straight up.")
SEAT_END = ("END OF THE SEATING MOVE: the strap has just been slid up and now sits seated ON THE PATELLAR TENDON directly below the "
            "kneecap — " + B.WORN.split(": ", 1)[1] + " Both hands are just lifting away from the shell's two ends, fingertips "
            "still touching.")

FIX["BR-16"] = ("nano_banana_pro", ["C2", "P4", "front", "back", "worn_front"], photo(
    "A medium close-up from low and in front: Dean sits on the rear step of the white van in the loading yard, right leg straight "
    "out in front, bending forward with both hands on the strap on his shin. THE SAME YARD AND VAN exactly as in the second "
    "attached image.",
    B.C2 + " Wearing a green-and-black check flannel shirt with the sleeves rolled, khaki cargo shorts, black steel-toe boots, a "
    "watch.", B.PRODUCT + " " + SEAT_START.replace("his shin", "his right shin"), "flat overcast daylight.",
    P.NEG_SEAT + ", no strap on the kneecap, no strap above the kneecap, no strap on the left leg"))
FIX["BR-16-END"] = ("nano_banana_pro", ["C2", "P4", "front", "back", "worn_front"], photo(
    "The SAME moment one second later, the same framing: a medium close-up from low and in front, Dean on the rear step of the "
    "white van, right leg straight out, bending forward. THE SAME YARD AND VAN exactly as in the second attached image.",
    B.C2 + " Wearing a green-and-black check flannel shirt with the sleeves rolled, khaki cargo shorts, black steel-toe boots, a "
    "watch.", B.PRODUCT + " " + SEAT_END + " Seated exactly as in the last attached worn reference.", "flat overcast daylight.",
    B.WORN_NEG + ", no strap on the kneecap, no strap low on the shin"))

FIX["BR-17"] = ("nano_banana_pro", ["C2", "P3", "front", "back", "worn_bent"], photo(
    "A medium-wide from a low three-quarter angle in the warehouse aisle: Dean mid-lift of a BIG, HEAVY cardboard box — a large "
    "double-wall box about 60cm wide and 50cm tall, taped shut, clearly heavy. Correct safe lifting: feet planted shoulder-width "
    "either side of the box, knees deeply bent in a squat, back straight and upright, chest up, the box pulled in tight against "
    "his body, both hands gripping underneath its two bottom corners, arms straight, his legs doing the work as he begins to "
    "stand. The strap on his bent right knee. THE SAME WAREHOUSE AISLE exactly as in the second attached image, racking behind.",
    B.C2 + " Wearing a green-and-black check flannel shirt with the sleeves rolled, khaki cargo shorts, black steel-toe boots.",
    B.PRODUCT + " " + P.PLACE_BENT + " Worn exactly as in the last attached bent reference.",
    "high-bay LED light, daylight from the open shutter.",
    B.WORN_NEG + ", no small box, no box held at arm's length, no rounded back, no bending at the waist, no one-handed lift"))

FIX["BR-19"] = ("nano_banana_pro", ["C2", "P3", "front", "back", "worn_front"], photo(
    "A medium shot at hip height, three-quarter front, framed from his chest down to his boots so the knee and strap are large and "
    "clear: Dean leaning back against the wooden workbench in the warehouse aisle, a mug of tea in his right hand at chest height, "
    "relaxed, weight on his left leg, the strap on his right knee in the middle of the frame. THE SAME WAREHOUSE AISLE exactly as "
    "in the second attached image, soft behind.",
    B.C2 + " Wearing a green-and-black check flannel shirt with the sleeves rolled, khaki cargo shorts, black steel-toe boots, a watch.",
    B.PRODUCT + " " + B.WORN + " Exactly as in the last attached worn reference: the matte-black shell with its two peaks and the "
    "grey stryde wordmark, one strap on the right knee only.", "high-bay LED light, late daylight from the open shutter.",
    B.WORN_NEG + ", no knee pads, no kneepad, no padded knee guard, no knee sleeve, no strap on the left knee, no readable mug text"))

# ── Act E ────────────────────────────────────────────────────────────────────
FIX["BR-20"] = ("nano_banana_pro", ["C4", "P2", "back", "front"], photo(
    "A close-up across the desk from a slightly high angle over the patient's shoulder: the surgeon's hand passes the strap across "
    "the desk into the patient's open hand, both hands in frame. THE SAME CONSULTING ROOM exactly as in the second attached image "
    "behind.",
    "The surgeon's hand exactly as in the attached character sheet, a pale pink shirt cuff and a steel watch. The patient's hand: "
    "a man in his sixties, grey long-sleeve tee cuff, palm open and cupped.",
    B.PRODUCT + " The surgeon holds it by the shell's bottom edge, the front face and wordmark up. " + LOOP + " " + P.SIZE_HELD,
    "cool window daylight from the left.", B.HELD_NEG + ", " + LOOP_NEG))

FIX["BR-21"] = ("nano_banana_pro", ["front", "back", "worn_front"], photo(
    "A medium-wide from a low angle beside the park path: a small group of four older walkers in their sixties and seventies "
    "passing the green-painted park railings, walking towards the camera, chatting; the nearest walker wears the strap on his "
    "right knee. The path in front of them is clear and empty.",
    "The nearest walker: a man in his late sixties, sage-green T-shirt, navy walking shorts ending above the knee, walking boots, "
    "a cap. The others in ordinary walking clothes. All hands empty or on backpack straps.",
    B.PRODUCT + " " + B.WORN.replace(" " + P.SIZE_WORN, "") + " Only the nearest walker wears one.",
    "bright sun through the trees.", B.WORN_NEG.replace("no second strap", "no strap on the other walkers") + ", no objects on the path"))

FIX["BR-22"] = ("nano_banana_pro", ["C1", "P1", "package_open", "front"], photo(
    "A close-up from a slightly high angle on the kitchen table with its checked cloth: the closed matte-black box sits on the "
    "table, lid firmly on; Maureen's two hands rest flat on top of the lid, fingertips gently feeling the smooth surface — she is "
    "not opening it. THE SAME KITCHEN exactly as in the second attached image, soft behind.",
    "Maureen's hands exactly as in the attached character sheet, cornflower-blue sleeves of her cotton dress.",
    P.PACKAGE["box"].capitalize() + ". " + P.PACKAGE["logo"].capitalize() + ". The lid is fully closed and flush all round.",
    "soft indirect west window light.",
    P.NEG_PACKAGE + ", no open box, no lifted lid, no gap under the lid, no fingers under the lid edge, no straps visible", skin=""))

FIX["BR-24"] = ("nano_banana_pro", ["C1", "P1", "package_open", "front", "back"], photo(
    "A medium close-up at chest height by the kitchen table, three-quarter front, framed from her shoulders to the table top so the "
    "strap and the box are large and clear: Maureen holds one strap up in front of her in the window light, looking at it, "
    "pleased; on the table in front of her sits the open box exactly as in the third attached image — the matte-black box, the "
    "lid with the grey stryde wordmark set beside it, the black insert with two shaped wells, one strap still lying in its well and "
    "the other well empty. THE SAME KITCHEN exactly as in the second attached image, soft behind.",
    B.C1 + " Wearing a cornflower-blue cotton dress.",
    B.PRODUCT + " She holds it by the shell's bottom edge, thumb in front below the wordmark, fingers behind on the pad, front face "
    "to the camera. " + LOOP + " " + P.SIZE_HELD, "soft indirect west window light.",
    B.HELD_NEG.replace("no second strap, ", "") + ", " + LOOP_NEG + ", no cardboard box, no brown box, no kraft box, no white box, "
    "no box flaps, no shoebox, no loose band beside the strap in the box, no shell separate from its band, no woman far from "
    "camera", skin=""))

FIX["BR-25"] = ("nano_banana_pro", ["C1", "P0", "front", "back", "worn_front"], photo(
    "A medium-wide at knee-to-waist height from the hall, a little in FRONT of her and to the side, three-quarter front: Maureen at "
    "the foot of the stairs beside the white newel post, looking up the flight, her right foot lifted onto the first carpeted step "
    "with its brass stair rod, the FRONT of her right knee turned towards the camera with the strap on it. " + STAIRS,
    B.C1 + " Wearing a cornflower-blue cotton dress ending a hand above the knee, navy slip-on shoes.",
    B.PRODUCT + " " + B.WORN + " Seen from the front three-quarter: the shell and its wordmark on the FRONT of the knee, facing the "
    "camera, only the black band passing round the back, exactly as in the last attached worn reference.",
    "soft east morning daylight through the front-door glass.",
    B.WORN_NEG + ", no strap on the back of the knee, no shell behind the knee, no view from behind, no view from the side, "
    + STAIRS_NEG))

FIX["BR-26a"] = ("nano_banana_pro", ["C1", "P0", "front", "back", "worn_front"], photo(
    "A medium close-up from low and in front: Maureen sits on the bottom stair of the carpeted flight, her right leg straight out, "
    "bending forward with both hands on the strap on her shin. The hall and stairs from the second attached image behind.",
    B.C1 + " Wearing a cornflower-blue cotton dress ending a hand above the knee, navy slip-on shoes.",
    B.PRODUCT + " " + SEAT_START.replace("his shin", "her right shin"), "soft east morning daylight.",
    P.NEG_SEAT + ", no strap on the kneecap, no strap above the kneecap, no strap on the left leg"))
FIX["BR-26a-END"] = ("nano_banana_pro", ["C1", "P0", "front", "back", "worn_front"], photo(
    "The SAME moment one second later, the same framing: a medium close-up from low and in front, Maureen on the bottom stair, "
    "right leg straight out, bending forward. The hall and stairs from the second attached image behind.",
    B.C1 + " Wearing a cornflower-blue cotton dress ending a hand above the knee, navy slip-on shoes.",
    B.PRODUCT + " " + SEAT_END + " Seated exactly as in the last attached worn reference.", "soft east morning daylight.",
    B.WORN_NEG + ", no strap on the kneecap, no strap low on the shin"))

FIX["BR-26b"] = ("nano_banana_pro", ["C1", "P0", "front", "back", "worn_front"], photo(
    "A wide shot from the landing looking straight down the whole flight, high angle: Maureen is near the BOTTOM of the stairs, on "
    "the second step, just starting to climb up towards the camera, mid-step, her right knee lifting, her hand off the rail; most "
    "of the flight of empty steps stretches between her and the camera. " + STAIRS.replace(
        "the flight rising away from the hall on the LEFT of frame", "seen from the top, the hall floor visible at the bottom"),
    B.C1 + " Wearing a cornflower-blue cotton dress ending a hand above the knee, navy slip-on shoes.",
    B.PRODUCT + " " + B.WORN, "soft east morning daylight from the front-door glass below.",
    B.WORN_NEG + ", no hand gripping the rail, no woman near the top of the stairs, no woman on the landing, " + STAIRS_NEG))

# Higgsfield media ids (uploaded this build)
MEDIA = {"C1": "1d353e88-0042-4021-9a6c-e7b8f93d5baa", "C2": "486a2651-f372-4671-9cce-b208d84b54ef",
         "C3": "265e4775-20c1-4799-85da-7d204469c229", "C4": "b055a260-6dde-43d3-a148-0be4da237ebe",
         "P0": "8bebe73c-ca40-4bc9-8c16-c5210738431e", "P1": "a45c1f15-8798-4387-9881-549f39195163",
         "P2": "c839311c-6655-4c8c-86c9-2bfdcddb3270", "P3": "2ead204b-15b9-423d-b1c8-60e137f8df87",
         "P4": "f37c1477-2764-4915-bc29-db7fe65d9743", "P5": "dccfee40-d133-4724-954f-d60b7084ec25",
         "front": "69584572-60fd-44a3-a2e0-ef49d4b1b0d2", "back": "c4213a99-5f07-4eb8-92e7-0b03c1bd297b",
         "worn_front": "c993bd6d-53ab-4b71-9bbe-261b7961eea6", "worn_bent": "fd03b356-8aec-462d-bdeb-a7d7ee2f6406",
         "package_open": "fc6b25cb-8d85-4d1b-83e4-abfafa55ff73"}

if __name__ == "__main__":
    out = {}
    for beat, (model, refs, prompt) in FIX.items():
        assert "phone propped" not in prompt and "the phone" not in prompt.lower(), beat
        (HERE / f"{beat}.fix2.t2i.txt").write_text(prompt + "\n")
        out[beat] = {"model": model, "refs": refs, "prompt": prompt,
                     "medias": [{"value": MEDIA[r], "role": "image_references"} for r in refs]}
    (HERE / "fix2.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(len(out), "images;", "longest", max(len(v["prompt"]) for v in out.values()), "chars")
