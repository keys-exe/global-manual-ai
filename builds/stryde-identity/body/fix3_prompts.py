#!/usr/bin/env python3
"""Fix round 3 (user, 2026-09-28): the 9 images the user marked Fix on the fix-2 renders.

BR-03 "so big, not correct product size" · BR-24 "a bit too big" · BR-06 "don't bend it" · BR-20 "the strap is floating"
· BR-04 "make a new productive B-roll here" · BR-13 / BR-26b "no gripping the rail" · BR-25 "going DOWN the stairs,
hands off the rail" · BR-26a "not sitting on the right spot" (she sat on a stool in the hall, not on the stair).
Same rules: Higgsfield nano_banana_pro, no phone, one render each. Writes body/<BEAT>.fix3.t2i.txt + body/fix3.json.
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import body_prompts as B  # noqa: E402
import fix2_prompts as F2  # noqa: E402
P = B.P
photo, STAIRS, STAIRS_NEG, MEDIA = F2.photo, F2.STAIRS, F2.STAIRS_NEG, F2.MEDIA

SMALL = ("TRUE SIZE — it is a SMALL strap: the shell is about 12 cm across and 5 cm tall, NARROWER than the holder's own "
         "hand is wide and no taller than a thumb is long; the closed band loop is only about 35 cm round, so it hangs just "
         "a hand's length below the shell. Next to the hand it reads small, like a watch strap scaled up a little, never "
         "like a belt or a harness.")
SMALL_NEG = ("no oversized strap, no giant shell, no shell wider than the hand, no long hanging band, no belt-sized loop, "
             "no harness")
LOOP_S = ("The band is a closed loop of soft black coarse-knit elastic joined to the two chrome slides; held up, it hangs "
          "slack in a short soft loop just below the shell.")
RAIL_OFF = ("BOTH her hands are full and held in front of her body, well away from the handrail — the rail is untouched, "
            "no hand anywhere near it.")
RAIL_NEG = "no hand on the rail, no hand gripping the rail, no hand touching the banister, no hand on the balustrade"

FIX = {}
FIX["BR-03"] = ("nano_banana_pro", ["C4", "P2", "front", "back"], photo(
    "A medium close-up across the desk from eye level, three-quarter front: the surgeon sits at his desk beside the plastic "
    "knee model and holds the strap up in the window light in one hand, looking at it. His face is in frame, calm. THE SAME "
    "CONSULTING ROOM exactly as in the second attached image — window on the left, the lightbox and bookshelf behind, softly "
    "out of focus.",
    B.C4 + " Wearing a white button-down shirt under a charcoal knitted waistcoat, charcoal trousers, a clinic lanyard with a "
    "blank card.",
    B.PRODUCT + " He pinches it by the shell's bottom edge between thumb and fingers, thumb in front below the wordmark. "
    + LOOP_S + " " + SMALL,
    "cool daylight from the window on the left, the lightbox glowing softly behind.",
    B.HELD_NEG + ", " + SMALL_NEG + ", " + F2.LOOP_NEG, skin=""))

FIX["BR-24"] = ("nano_banana_pro", ["C1", "P1", "package_open", "front", "back"], photo(
    "A medium close-up at chest height by the kitchen table, three-quarter front, framed from her shoulders to the table top: "
    "Maureen holds one strap up in front of her in the window light, looking at it, pleased; on the table in front of her "
    "sits the open box exactly as in the third attached image — the matte-black box, the lid with the grey stryde wordmark "
    "set beside it, the black insert with two shaped wells, one strap still lying in its well and the other well empty. The "
    "strap in her hand is exactly the same size as the one still in the box. THE SAME KITCHEN exactly as in the second "
    "attached image, soft behind.",
    B.C1 + " Wearing a cornflower-blue cotton dress.",
    B.PRODUCT + " She pinches it by the shell's bottom edge, thumb in front below the wordmark, front face to the camera. "
    + LOOP_S + " " + SMALL,
    "soft indirect west window light.",
    B.HELD_NEG.replace("no second strap, ", "") + ", " + SMALL_NEG + ", " + F2.LOOP_NEG + ", no cardboard box, no brown box, "
    "no white box, no strap in her hand bigger than the one in the box", skin=""))

FIX["BR-06"] = ("nano_banana_pro", ["C4", "P2", "back", "front"], photo(
    "A close-up from chest height across the desk: only the surgeon's two hands and the strap in frame, held up in front of "
    "his charcoal waistcoat, the strap turned so its INSIDE faces the camera, exactly as in the first attached product photo "
    "(the back view). The consulting room behind, far out of focus.",
    "The surgeon's hands exactly as in the attached character sheet: broad, long fingers, white shirt cuffs under a "
    "charcoal knitted waistcoat.",
    "The whole strap exactly as in the attached back-view product photo, in its own natural resting shape: a closed loop — "
    "the rigid matte-black shell at the top with its two rounded peaks and centre notch, a brushed chrome slide at each end, "
    "the soft black knit band looping down below with its two keeper loops. The shell keeps its moulded curve EXACTLY as in "
    "the photo — it is rigid plastic and is NOT bent, flexed, flattened, stretched or pulled open. The hands barely hold it: "
    "fingertips lightly behind the shell's two ends, thumbs resting on its lower edge, no force at all. Seen from inside the "
    "loop, the smooth matte-black inner pad faces the camera. " + SMALL,
    "cool window daylight from the left.",
    "no bent shell, no flexed shell, no flattened shell, no shell pulled wide, no stretched strap, no hands pulling the ends "
    "apart, no wordmark visible, no flat panel without a band, no open band, " + SMALL_NEG + ", " + F2.LOOP_NEG, skin=""))

FIX["BR-20"] = ("nano_banana_pro", ["C4", "P2", "front", "back"], photo(
    "A close-up across the desk from a slightly high angle over the patient's shoulder: the strap LIES IN the patient's open "
    "palm, resting on his skin with its weight in his hand; the surgeon's fingertips are still touching the shell's edge as "
    "he lets go. THE SAME CONSULTING ROOM exactly as in the second attached image behind.",
    "The surgeon's hand exactly as in the attached character sheet, a pale pink shirt cuff and a steel watch. The patient's "
    "hand: a man in his sixties, grey long-sleeve tee cuff, palm open and cupped under the strap.",
    B.PRODUCT + " The shell sits in the patient's palm, front face and wordmark up; the soft knit band loop drapes over the "
    "edge of his hand and his fingers, touching them. Every part of the strap is in contact with a hand — nothing hovers. "
    + SMALL,
    "cool window daylight from the left.",
    "no floating strap, no strap hovering above the hand, no gap between strap and palm, no levitating object, "
    + SMALL_NEG + ", " + F2.LOOP_NEG))

FIX["BR-04"] = ("nano_banana_pro", ["front", "back", "worn_front"], photo(
    "A medium shot at knee-to-chest height, three-quarter front, in a sunny back garden: a man in his sixties strides "
    "across the lawn carrying a full metal watering can in his right hand towards the flower bed, busy and easy, mid-step, "
    "his right knee in the middle of the frame with the strap on it, large and clear.",
    "A man in his sixties, sturdy, grey hair, a navy T-shirt, grey shorts ending above the knee, old canvas trainers; real "
    "firm leg muscle.",
    B.PRODUCT + " " + B.WORN + " Seated exactly as in the last attached worn reference.",
    "bright late-morning sun, soft shadows on the grass.", B.WORN_NEG))

FIX["BR-13"] = ("nano_banana_pro", ["C1", "P0", "front", "back", "worn_front"], photo(
    "A medium-wide from the hall floor beside the newel post, low three-quarter angle looking up the flight: Maureen is ON "
    "THE STAIRS, climbing, her left foot on the third step and her right foot lifting onto the fourth, carrying a small "
    "stack of folded towels against her chest in BOTH arms. " + RAIL_OFF + " " + STAIRS,
    B.C1 + " Wearing a burgundy long-sleeve jersey tunic, a denim skirt ending a hand above the knee, sheepskin slippers.",
    B.PRODUCT + " " + B.WORN + " The strap on her right knee faces the camera as she climbs.",
    "soft east morning daylight through the front-door glass.",
    B.WORN_NEG + ", " + RAIL_NEG + ", " + STAIRS_NEG + ", no woman standing in the hall"))

FIX["BR-26b"] = ("nano_banana_pro", ["C1", "P0", "front", "back", "worn_front"], photo(
    "A wide shot from the landing looking straight down the whole flight, high angle: Maureen is near the BOTTOM of the "
    "stairs, on the second step, just starting to climb up towards the camera, mid-step, her right knee lifting, holding a "
    "mug of tea in both hands in front of her. " + RAIL_OFF + " Most of the flight of empty steps stretches between her and "
    "the camera. " + STAIRS.replace("the flight rising away from the hall on the LEFT of frame",
                                    "seen from the top, the hall floor visible at the bottom"),
    B.C1 + " Wearing a cornflower-blue cotton dress ending a hand above the knee, navy slip-on shoes.",
    B.PRODUCT + " " + B.WORN, "soft east morning daylight from the front-door glass below.",
    B.WORN_NEG + ", " + RAIL_NEG + ", no woman near the top of the stairs, " + STAIRS_NEG))

FIX["BR-25"] = ("nano_banana_pro", ["C1", "P0", "front", "back", "worn_front"], photo(
    "A medium-wide at knee-to-waist height from the hall, three-quarter front, looking at the bottom of the flight: Maureen "
    "is coming DOWN the stairs towards the camera, facing down the flight, her left foot on the second step and her right "
    "foot reaching down to the bottom step, carrying a folded cardigan in both hands in front of her. " + RAIL_OFF +
    " The FRONT of her right knee faces the camera with the strap on it. " + STAIRS,
    B.C1 + " Wearing a cornflower-blue cotton dress ending a hand above the knee, navy slip-on shoes.",
    B.PRODUCT + " " + B.WORN + " Seen from the front: the shell and its wordmark on the FRONT of the knee, facing the "
    "camera, exactly as in the last attached worn reference.",
    "soft east morning daylight through the front-door glass.",
    B.WORN_NEG + ", " + RAIL_NEG + ", no woman going up the stairs, no back to the camera, no strap on the back of the "
    "knee, " + STAIRS_NEG))

FIX["BR-26a"] = ("nano_banana_pro", ["C1", "P0", "front", "back", "worn_front"], photo(
    "A medium close-up from low and in front: Maureen SITS ON THE BOTTOM STEP OF THE STAIRCASE itself — her bottom on the "
    "carpeted tread of the lowest stair, the brass stair rod and the next steps rising behind her, the white newel post "
    "and the mahogany handrail beside her. Her right leg is straight out along the hall carpet, and she bends forward with "
    "both hands on the strap on her shin. " + STAIRS.replace("the flight rising away from the hall on the LEFT of frame",
                                                             "the flight rising behind her"),
    B.C1 + " Wearing a cornflower-blue cotton dress ending a hand above the knee, navy slip-on shoes.",
    B.PRODUCT + " " + F2.SEAT_START.replace("his shin", "her right shin"), "soft east morning daylight.",
    P.NEG_SEAT + ", no stool, no chair, no bench, no sitting in the hall, no sitting on the floor, no strap on the kneecap, "
    "no strap on the left leg, " + STAIRS_NEG))

if __name__ == "__main__":
    out = {}
    for beat, (model, refs, prompt) in FIX.items():
        (HERE / f"{beat}.fix3.t2i.txt").write_text(prompt + "\n")
        out[beat] = {"model": model, "refs": refs, "prompt": prompt,
                     "medias": [{"value": MEDIA[r], "role": "image_references"} for r in refs]}
    (HERE / "fix3.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(len(out), "images")
