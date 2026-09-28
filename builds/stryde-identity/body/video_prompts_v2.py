#!/usr/bin/env python3
"""Body B-roll video prompts, fix round 2 (user, 2026-09-28) — Kling kling-video-v3_0_omni, §35 JSON, minified.

User rules this round: Kling prompts in §35 JSON (supersedes the plain-text rule for Kling); never a phone in any
B-roll — no phone in frame and no phone named anywhere in a prompt (the old "the phone stays still" lines put phones
on the street in BR-12 / BR-21). §27G: one action at a named pace, camera sways but never travels with a moving
subject, the product rigid, prefer_multi_shots false. BR-16 / BR-26a are pinned (first-and-last frame, E7).

Writes body/<BEAT>.v2.i2v.json (the minified prompt) and body/<BEAT>.v2.call.json (preflight.py input).
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEN = {r["beat"]: r["clip_s"] for r in json.loads((HERE.parent / "work/body_lengths.json").read_text())}

RIG = ("Already drifting on frame one. Low breath sway throughout, vertical with slight roll. Camera lags the subject, "
       "never anticipates, never travels with it. Still drifting at the cut.")
RIG_V = ("Virtual camera already drifting on frame one: a slow steady lateral drift, constant unhurried speed, mechanically "
         "smooth, no orbit, no sway. Still drifting at the cut.")
INHERIT = ("Capture exactly as in the start frame: same tone, noise and colour temperature, no grading change across the "
           "clip.")
HOLD = ("Everything keeps the exact form, proportion and count it has in the start frame; nothing melts, merges, splits or "
        "grows. Subject fully in frame throughout.")
HOLD_H = ("Same person every frame: same face, age, hair and wardrobe; five separate fingers on each hand; limbs keep "
          "their length and bend only at real joints.")
HOLD_P = ("The strap keeps the start frame's exact geometry every frame: same two equal peaks, same centred notch, same "
          "chrome slides and grey stryde wordmark. The shell is hard moulded plastic and never bends, flexes, wobbles or "
          "jiggles.")
HOLD_A = ("The anatomy keeps its structure every frame: bones hold shape and spacing, joints never separate, muscle keeps "
          "its volume, layer order holds.")
PHYS = ("Mass and momentum: heavy starts and settles slow, nothing at uniform speed, nothing stops instantly; fabric and "
        "the soft elastic band lag and settle after the body stops.")
NEG_WARP = ("no morphing, no warping, no melting, no shape shifting, no merging, no splitting, no duplicate objects, no "
            "background bending, no texture swimming, no flickering geometry")
NEG_PROD = "no bending, no curling, no folding, no melting, no flipping of the product, no jelly wobble, no rubbery shell"
NEG_M1 = ("no phone, no smartphone, no mobile phone anywhere in the frame, no camera in frame, no AI face, no plastic skin, "
          "no extra fingers, no fused fingers, no deformed limbs, no CGI look, no text, no music")
NEG_A = "no text, no labels, no arrows, no flash, no white frame, no strobe, no camera shake"

STYLE = "Ordinary everyday footage, natural daylight colour, unretouched."
STYLE_A = "Premium 3D anatomical render exactly as in the start frame, deep near-black field."


def photo(shot, subject, framing, motion, neg="", product=True, person=True):
    m = motion + " " + HOLD + (" " + HOLD_H if person else "") + (" " + HOLD_P if product else "") + " " + PHYS
    n = NEG_WARP + (", " + NEG_PROD if product else "") + (", " + neg if neg else "") + ", " + NEG_M1
    return {"shot": shot, "subject": subject, "camera": {"movement": RIG, "framing": framing}, "motion": m,
            "lighting": INHERIT, "style": STYLE, "negatives": n}


def anat(shot, subject, motion, neg=""):
    return {"shot": shot, "subject": subject, "camera": {"movement": RIG_V, "framing": "as in the start frame"},
            "motion": motion + " " + HOLD_A, "lighting": "exactly as in the start frame, no change in brightness",
            "style": STYLE_A, "negatives": NEG_WARP + ", " + NEG_A + (", " + neg if neg else "")}


P = {}
P["MECH-01"] = anat("patellar_tendon_load",
    "Translucent anatomical knee from the front, the patellar tendon a pearly band from the kneecap down to the shin.",
    "The body's weight arrives from above: over two seconds the small glow on the patellar tendon just below the kneecap "
    "brightens once, steadily, then holds. Nothing else lights.", "no glow on the side of the joint, no glow on the meniscus")
P["MECH-10"] = anat("bone_on_bone",
    "Translucent anatomical knee, bare femur resting directly on bare tibia, rough spurred bone ends, a red-orange glow "
    "where they meet.",
    "The knee bends a little under load, one slow press over two seconds: the femur grinds down onto the tibia, bone on "
    "bone, and the red-orange glow at the contact flares hotter, pulsing once like pain, then holds hot.")
P["MECH-15"] = anat("pad_carries_load",
    "Translucent anatomical knee with the matte-black strap on the patellar tendon, a dim pale-cyan glow on the pad.",
    "The whole clip stays dark and calm from the very first frame. The dim pale-cyan glow on the pad breathes softly "
    "once, a little brighter then back, slow; the tendon and joint stay calm, no hot spot.",
    "no white, no white glow, no white flash, no bright start, no fade from white, no overexposure, no bloom")

P["BR-03"] = photo("surgeon_holds_strap",
    "The seventy-one-year-old surgeon, white hair, white shirt under a charcoal knitted waistcoat, at his desk holding "
    "the stryde strap by the shell's bottom edge, its soft black elastic loop hanging below.",
    "Medium close-up across the desk, as in the start frame.",
    "He tilts the strap slowly towards the window, one turn of the wrist over about two seconds, looking at it. The hard "
    "shell turns as one rigid piece; the soft knit band hanging below swings gently with the turn, sags under its own "
    "weight and settles, like real elastic fabric.", "no stiff band, no band standing out straight")
P["BR-04"] = photo("surgeon_points_tendon",
    "A man in his sixties lying on the examination couch, navy T-shirt, grey shorts, the strap on his right knee; the "
    "surgeon's index finger at the patellar tendon.",
    "Low close-up from the foot of the couch, as in the start frame.",
    "The surgeon's fingertip taps twice, lightly, on the bare patellar tendon between the kneecap and the strap's notch, "
    "one tap per second, then rests there. The patient lies completely still. The leg is firm real muscle and bone; the "
    "skin moves only where the fingertip presses.",
    "no jelly skin, no wobbling leg, no rippling flesh, no hand leaving frame, no finger moving to the side of the knee")
P["BR-06"] = photo("pad_inside",
    "The surgeon's two hands holding the stryde strap as a closed loop, its inside facing the camera: the smooth "
    "matte-black inner pad, a chrome slide at each end, the knit band looping below.",
    "Close-up, as in the start frame.",
    "His hands tilt the strap slowly back a little, over about two seconds, so window light slides across the smooth "
    "matte-black inner pad. The loop stays closed; the band hangs and sways softly.",
    "no front face turning to camera, no wordmark, no flat panel without a band, no open band")
P["BR-12"] = photo("walk_further",
    "Pat, sixty-six, Breton top, rust gilet, khaki shorts, white trainers, the strap on her right knee, on the park path "
    "by the green railings.",
    "Wide, full figure, as in the start frame.",
    "She walks briskly towards and past the camera along the path, about two steps per second, long easy strides, arms "
    "swinging. The strap stays exactly in place below her right kneecap.",
    "no objects on the path, nothing on the ground")
P["BR-13"] = photo("climb_stairs",
    "Maureen, seventy-four, burgundy tunic, denim skirt, sheepskin slippers, the strap on her right knee, on the "
    "carpeted staircase with brass stair rods and the mahogany handrail.",
    "Wide from the foot of the stairs looking up, as in the start frame.",
    "She climbs up the stairs, one step per second, placing each foot flat on the next carpeted tread, two steps in the "
    "clip, her hand free of the rail. The steps stay fixed, straight and evenly spaced.",
    "no floating, no sliding feet, no steps changing shape, no hand on the rail")
P["BR-14"] = photo("busy_on_the_landing",
    "Maureen, burgundy tunic, denim skirt, slippers, the strap on her right knee, carrying a wicker laundry basket onto "
    "the landing.",
    "Medium from the landing, as in the start frame.",
    "She steps up onto the landing with the basket on her hip, one easy step, then walks on past the camera at a normal "
    "pace, a small contented smile.", "no pained face, no hand on the knee")
P["BR-16"] = photo("seat_strap_up",
    "Dean, fifty-eight, heavyset, check flannel shirt, cargo shorts, steel-toe boots, on the van's rear step, both hands "
    "on the closed strap low on his right shin.",
    "Medium close-up from low in front, as in the start frame; the end frame is the attached last frame.",
    "Both hands slide the closed strap straight UP the front of his shin in one smooth move, about one second, and stop "
    "it against the underside of the kneecap exactly as in the end frame; the hands then lift away a little. It only "
    "moves up. Nothing is opened, threaded or tightened.",
    "no strap past the kneecap, no strap on the kneecap, no strap moving down, no band being pulled")
P["BR-17"] = photo("heavy_box_lift",
    "Dean in a deep squat in the warehouse aisle, back straight, hugging a big heavy double-wall box, hands under its "
    "bottom corners, the strap on his bent right knee.",
    "Medium-wide from a low three-quarter angle, as in the start frame.",
    "He stands up with the heavy box in one slow, strained squat-lift over about three seconds: legs drive, back stays "
    "straight, the box stays tight against his chest and belly. The box is heavy and rigid; his face shows the effort.",
    "no box floating, no box changing size, no rounded back, no bending at the waist")
P["BR-19"] = photo("tea_break",
    "Dean leaning on the workbench, check flannel shirt, cargo shorts, boots, a mug of tea, the stryde strap on his "
    "right knee in the middle of the frame.",
    "Medium from chest to boots, as in the start frame.",
    "He lifts the mug and takes one slow sip, then lowers it, relaxed; his legs stay still, the strap unchanged on the "
    "right knee.", "no knee pads, no second strap, no strap on the left knee")
P["BR-20"] = photo("surgeon_hands_over",
    "The surgeon's hand passing the stryde strap across the desk into a patient's open hand; the strap's soft black "
    "elastic loop hangs below the shell.",
    "Close-up over the patient's shoulder, as in the start frame.",
    "The surgeon's hand lowers the strap slowly into the open palm, about two seconds; the patient's fingers close "
    "gently round the shell. The soft band loop drapes over the patient's fingers and settles like fabric.",
    "no stiff band, no band sticking out straight, no strap changing shape")
P["BR-21"] = photo("walking_group",
    "Four older walkers on the park path by the green railings, the nearest man in a sage T-shirt and navy shorts "
    "wearing the strap on his right knee.",
    "Medium-wide from low beside the path, as in the start frame.",
    "They walk towards the camera, chatting, one step per second, the nearest man passing close by. The strap stays in "
    "place on his right knee.", "no objects on the path, nothing on the ground")
P["BR-22"] = photo("feel_the_box",
    "Maureen's hands resting on the lid of the closed matte-black stryde box on the checked tablecloth.",
    "Close-up from slightly above, as in the start frame.",
    "Her fingertips glide slowly across the smooth lid, one slow stroke over about two seconds, feeling it. The lid "
    "stays closed the whole clip; the box does not move.",
    "no opening, no lid lifting, no gap under the lid, no fingers under the lid", person=False)
P["BR-24"] = photo("look_at_strap",
    "Maureen, seventy-four, cornflower-blue dress, holding one stryde strap up, the open black stryde box with the "
    "second strap on the table in front of her.",
    "Medium close-up, as in the start frame.",
    "She turns the strap slowly in the window light, one turn of the wrist over about two seconds, looking at it, "
    "pleased; the soft band loop swings gently and settles. The box stays still.",
    "no cardboard box, no box changing, no stiff band")
P["BR-25"] = photo("first_step",
    "Maureen, cornflower-blue dress, navy shoes, the strap on the front of her right knee, at the foot of the carpeted "
    "staircase by the white newel post.",
    "Medium-wide three-quarter front, as in the start frame.",
    "She steps up onto the first carpeted step in one easy move, weight shifting onto her right foot, about one second, "
    "and settles, looking up the stairs. The strap stays on the front of her knee.",
    "no strap turning to the back of the knee, no steps changing shape, no floating")
P["BR-26a"] = photo("seat_strap_up_home",
    "Maureen on the bottom stair, cornflower-blue dress, both hands on the closed strap low on her right shin.",
    "Medium close-up from low in front, as in the start frame; the end frame is the attached last frame.",
    "Both hands slide the closed strap straight UP the front of her shin in one smooth move, about one second, and stop "
    "it against the underside of the kneecap exactly as in the end frame; the hands then lift away a little. It only "
    "moves up. Nothing is opened, threaded or tightened.",
    "no strap past the kneecap, no strap on the kneecap, no strap moving down, no band being pulled")
P["BR-26b"] = photo("climb_to_camera",
    "Maureen near the bottom of the carpeted staircase, cornflower-blue dress, navy shoes, the strap on her right knee.",
    "Wide from the landing looking down the flight, as in the start frame.",
    "She climbs up the stairs towards the camera, one step per second, three steps in the clip, hand free of the rail; "
    "she is still well below the landing at the cut. The steps stay fixed and evenly spaced.",
    "no reaching the top, no floating, no sliding feet, no steps changing shape")

# ── fix round 3 (user, 2026-09-28) — overrides ─────────────────────────────────
# BR-16: the user confirmed the end frame and said to use it as the solo start image (no pinned tail frame).
P["BR-16"] = photo("strap_seated_straighten",
    "Dean, fifty-eight, heavyset, check flannel shirt, cargo shorts, steel-toe boots, by the open van, both hands on the "
    "strap seated below his right kneecap.",
    "Medium from low in front, as in the start frame.",
    "His hands lift off the seated strap and he straightens up slowly, one easy move over about two seconds, looking down "
    "at his knee, satisfied. The strap stays exactly where it is below the kneecap; nothing is pulled or adjusted.",
    "no strap moving, no strap sliding down, no band being pulled, no hands on the band")
P["BR-04"] = photo("garden_watering_can",
    "A man in his sixties, grey hair, navy T-shirt, grey shorts, canvas trainers, the strap on his right knee, carrying a "
    "full watering can across a sunny garden lawn.",
    "Medium at knee-to-chest height, as in the start frame.",
    "He strides across the lawn towards the flower bed, one step per second, the watering can swinging a little with its "
    "weight. The strap stays in place below his right kneecap.", "no objects appearing, no water spilling everywhere")
P["BR-13"] = photo("climb_stairs_towels",
    "Maureen, seventy-four, burgundy tunic, denim skirt, sheepskin slippers, the strap on her right knee, climbing the "
    "carpeted staircase with brass stair rods, a stack of folded towels held against her chest in both arms.",
    "Wide from the foot of the stairs looking up, as in the start frame.",
    "She climbs up the stairs, one step per second, two steps in the clip, both arms round the towels the whole time, "
    "never touching the handrail. The steps stay fixed, straight and evenly spaced.",
    "no hand on the rail, no hand reaching for the rail, no floating, no sliding feet, no steps changing shape")
P["BR-25"] = photo("down_last_step",
    "Maureen, cornflower-blue dress, navy shoes, the strap on the front of her right knee, coming down the carpeted "
    "staircase, a folded cardigan in both hands.",
    "Medium-wide three-quarter front from the hall, as in the start frame.",
    "She steps down off the bottom stair onto the hall carpet, one easy step down, about one second, weight settling "
    "onto her right leg, both hands holding the cardigan, never touching the rail. The strap stays on the front of her knee.",
    "no hand on the rail, no going up, no strap turning to the back of the knee, no steps changing shape, no floating")
P["BR-26b"] = photo("climb_to_camera_tea",
    "Maureen near the bottom of the carpeted staircase, cornflower-blue dress, navy shoes, the strap on her right knee, a "
    "mug of tea held in both hands.",
    "Wide from the landing looking down the flight, as in the start frame.",
    "She climbs up the stairs towards the camera, one step per second, three steps in the clip, both hands round the mug, "
    "never touching the rail; she is still well below the landing at the cut. The steps stay fixed and evenly spaced.",
    "no hand on the rail, no reaching the top, no floating, no sliding feet, no tea spilling, no steps changing shape")
P["BR-20"] = photo("strap_in_palm",
    "The surgeon's fingertips letting go of the stryde strap as it rests in a patient's open palm; the soft black band "
    "loop drapes over the patient's fingers.",
    "Close-up over the patient's shoulder, as in the start frame.",
    "The surgeon's fingertips lift away and the patient's fingers close gently round the shell, about two seconds. The "
    "strap stays resting in his hand the whole time, its weight in his palm; the band settles over his fingers.",
    "no floating strap, no strap lifting out of the hand, no strap changing size")

# ── fix round 4 (user, 2026-09-28) — overrides ─────────────────────────────────
# BR-26a: the user said to use the confirmed end frame (BR-26a-END) as the image and NOT the start frame — solo start.
P["BR-26a"] = photo("strap_seated_sit_up",
    "Maureen on the bottom stair, cornflower-blue dress, navy shoes, both hands on the strap seated below her right "
    "kneecap.",
    "Medium close-up from low in front, as in the start frame.",
    "Her hands lift off the seated strap and she sits back up slowly, one easy move over about two seconds, looking at "
    "her knee, pleased. The strap stays exactly where it is below the kneecap; nothing is pulled or adjusted.",
    "no strap moving, no strap sliding down, no band being pulled, no hands on the band")
P["BR-24"] = photo("washing_line",
    "Maureen, seventy-four, cornflower-blue dress, navy shoes, the strap on her right knee, pegging a sheet on a washing "
    "line in a sunny back garden.",
    "Medium from shoulders to feet, as in the start frame.",
    "She reaches up and pegs the sheet on the line, one easy reach over about two seconds, then lowers her arms; the "
    "sheet sways gently in the breeze. Her weight stays on her right leg; the strap stays in place below the kneecap.",
    "no objects appearing, no sheet flying away")
P["BR-25"] = photo("down_the_stairs",
    "Maureen halfway down the carpeted staircase, cornflower-blue dress, navy shoes, the strap on the front of her right "
    "knee, a folded cardigan in both hands.",
    "Medium-wide from the foot of the stairs looking up, as in the start frame.",
    "She comes down the stairs towards the camera, one step per second, two steps in the clip, both hands on the "
    "cardigan, never touching the rail; she is still on the stairs at the cut. The steps stay fixed and evenly spaced.",
    "no hand on the rail, no reaching the bottom, no going up, no floating, no sliding feet, no steps changing shape")

# ── fix round 5 (user, 2026-09-28): BR-22 image has no hands now — the box alone, the camera does the moving ──
P["BR-22"] = {"shot": "box_reveal",
    "subject": "The closed matte-black stryde box alone on the checked tablecloth, grey stryde wordmark on the lid.",
    "camera": {"movement": "A slow, steady push in towards the box, one direction, constant unhurried speed, a faint "
                           "handheld breath sway on top. Still moving at the cut.",
               "framing": "Close-up from slightly above, as in the start frame; the box stays centred."},
    "motion": "Nothing in the scene moves except soft window light sliding slowly across the matte lid. The lid stays "
              "closed; the box stays exactly where it is and keeps its exact shape and wordmark every frame. "
              + HOLD,
    "lighting": INHERIT, "style": STYLE,
    "negatives": NEG_WARP + ", no hands, no fingers, no person entering, no lid opening, no box moving, no box changing "
                 "shape, no text changing, " + NEG_M1}

# ── fix round 6 (user video Fix notes, 2026-09-28) ─────────────────────────────
P["BR-06"] = photo("pad_inside_still",
    "The surgeon's two hands holding the one stryde strap as a closed loop, its inside facing the camera: the smooth "
    "matte-black inner pad, a chrome slide at each end, the knit band looping below.",
    "Close-up, as in the start frame.",
    "Almost nothing moves: the hands hold the same one strap steady the whole clip, with only a tiny slow tilt of a few "
    "degrees so the window light slides across the smooth inner pad. The strap never leaves the hands, never jumps, "
    "never swaps, never turns round; no other strap appears.",
    "no second strap, no strap appearing, no strap disappearing, no teleporting, no jump cut, no strap swapping, no "
    "strap flipping round, no front face turning to camera, no wordmark, no open band")
P["BR-13"] = photo("climb_stairs_towels",
    "Maureen, seventy-four, burgundy tunic, denim skirt, sheepskin slippers, the strap on her right knee, climbing the "
    "carpeted staircase with brass stair rods, a stack of folded towels held against her chest in both arms.",
    "Wide from the foot of the stairs looking up, as in the start frame.",
    "She walks up the stairs easily and normally, one foot per step, alternating: her right foot goes onto the next "
    "step, then her left foot onto the step above that, never both feet on the same step, never pausing, about one "
    "step per second, two steps in the clip. Both arms stay round the towels; she never touches the rail. The steps "
    "stay fixed, straight and evenly spaced.",
    "no both feet on one step, no stepping together, no pausing between steps, no hand on the rail, no floating, no "
    "sliding feet, no steps changing shape")
P["BR-14"] = photo("busy_on_the_landing",
    "Maureen, burgundy tunic, denim skirt, slippers, the strap on her right knee, carrying a wicker laundry basket on "
    "the landing, held exactly as in the start frame.",
    "Medium from the landing, as in the start frame.",
    "She steps up onto the landing and walks on at a normal pace, a small contented smile. She carries the basket "
    "EXACTLY as in the start frame the whole clip: the same arms, the same grip, the same position against her body; "
    "the grip never changes and the basket never moves to her other side.",
    "no change of grip, no basket switching sides, no basket moving to the hip, no basket lifted higher, no hand leaving "
    "the basket, no pained face, no hand on the knee")
P["BR-17"] = photo("easy_box_lift",
    "Dean in a squat in the warehouse aisle, back straight, holding a big cardboard box close to his body, the strap on "
    "his bent right knee.",
    "Medium-wide from a low three-quarter angle, as in the start frame.",
    "He stands up with the box in one smooth, easy squat-lift over about two seconds, as if it were no trouble at all: "
    "relaxed face, a small easy smile, steady breathing, back straight, the box held close. A positive, strong, "
    "comfortable moment; his knee feels fine.",
    "no struggling, no strain, no grimace, no wincing, no shaking arms, no groaning face, no box floating, no box "
    "changing size, no rounded back")

# ── fix round 7 (user video Fix notes, 2026-09-28) ─────────────────────────────
ONE_TAKE = ("One single continuous take from the first frame to the last: no cut, no jump, no skipped moment, no change "
            "of angle, nothing appearing or disappearing.")
ONE_TAKE_NEG = "no cut, no jump cut, no teleporting, no skipped frames, no scene change, no second shot"
P["BR-13"] = photo("one_step_up",
    "Maureen on the carpeted stairs, burgundy tunic, the strap on her right knee, folded towels in both arms.",
    "Wide from the foot of the stairs looking up, as in the start frame.",
    "ONE step only, slowly: her lifting right foot comes down flat on the next step up and her weight moves onto it, "
    "then her left foot starts to lift towards the step above. One foot per step: her two feet are never on the same "
    "step. Both arms stay round the towels; she never touches the rail. " + ONE_TAKE,
    "no two feet on one step, no hand on the rail, no steps changing shape, " + ONE_TAKE_NEG)
P["BR-25"] = photo("one_step_down",
    "Maureen halfway down the carpeted stairs, blue dress, the strap on her right knee, a cardigan in both hands.",
    "Medium-wide from the foot of the stairs looking up, as in the start frame.",
    "ONE step down only, slowly: her reaching right foot comes down flat on the next step below and her weight moves "
    "onto it, then her left foot starts to lift towards the step below that. One foot per step: her two feet are never "
    "on the same step. Both hands stay on the cardigan; she never touches the rail. " + ONE_TAKE,
    "no two feet on one step, no hand on the rail, no going up, no steps changing shape, " + ONE_TAKE_NEG)
P["BR-24"] = photo("washing_line",
    "Maureen, seventy-four, cornflower-blue dress, navy shoes, the strap on her right knee, pegging a sheet on a washing "
    "line in a sunny back garden.",
    "Medium from shoulders to feet, as in the start frame.",
    "She presses the peg onto the sheet on the line and slowly lowers her arms, one easy move over about two seconds; "
    "the sheet sways gently. She stays standing in the same spot the whole clip. " + ONE_TAKE,
    "no walking away, no objects appearing, no sheet flying away, " + ONE_TAKE_NEG)

# ── fix round 8 (user, 2026-09-28) ─────────────────────────────────────────────
P["BR-25"] = photo("down_the_stairs_brisk",
    "Maureen halfway down the carpeted stairs, blue dress, the strap on her right knee, a cardigan in both hands.",
    "Medium-wide from the foot of the stairs looking up, as in the start frame.",
    "She walks down the stairs quickly in one smooth continuous rhythm, about two steps per second, never pausing: "
    "one foot per step, alternating, never two feet on one step. Both hands stay on the cardigan, off the rail. "
    + ONE_TAKE,
    "no slow motion, no pausing, no two feet on one step, no hand on the rail, no going up, " + ONE_TAKE_NEG)
P["BR-13"] = photo("climb_close_brisk",
    "Maureen's legs walking up the carpeted stairs, the strap on her right knee, her empty hand by the rail.",
    "Close, hips to feet, as in the start frame.",
    "She walks up the stairs at a brisk normal pace in one smooth continuous rhythm, about two steps per second, never "
    "pausing: one foot per step, alternating, never two feet on one step. Her right hand swings loosely and never "
    "touches the rail. " + ONE_TAKE,
    "no slow motion, no pausing, no two feet on one step, no hand on the rail, " + ONE_TAKE_NEG)

# ── fix round 9 (user, 2026-09-28) ─────────────────────────────────────────────
P["BR-13"] = photo("climb_towel_wall_side",
    "Maureen walking up the stairs on the wall side, the strap on her right knee, a towel in both hands.",
    "Close, chest to feet, as in the start frame.",
    "She walks up the stairs at real-time normal speed, never slow motion, in one smooth continuous rhythm, about two "
    "steps per second, three steps in the clip, never pausing: one foot per step, alternating. Both hands stay on the "
    "towel the whole clip and never go near the rail. " + ONE_TAKE,
    "no slow motion, no pausing, no two feet on one step, no hand on the rail, no hand reaching out, " + ONE_TAKE_NEG)
P["BR-25"] = photo("down_the_stairs_fast",
    "Maureen coming down the carpeted stairs fast, blue dress, the strap on her right knee, a cardigan in both hands.",
    "Medium-wide from the foot of the stairs looking up, as in the start frame.",
    "She comes down the stairs FAST at real-time speed, never slow motion, like someone in a hurry: about two and a half "
    "steps per second, four steps in the clip, one smooth continuous rhythm, never pausing, one foot per step, "
    "alternating. Both hands stay on the cardigan, off the rail. " + ONE_TAKE,
    "no slow motion, no slow careful steps, no pausing, no two feet on one step, no hand on the rail, no going up, "
    + ONE_TAKE_NEG)

# ── fix round 10 (user, 2026-09-28): BR-25 new close low setup ────────────────
P["BR-25"] = photo("down_to_camera_fast",
    "Maureen's legs coming down the stairs, the strap on her right knee, a cardigan in her hands.",
    "Close, waist to feet, as in the start frame.",
    "She comes down the stairs towards the camera FAST at real-time speed, never slow motion, like someone in a hurry: "
    "about two and a half steps per second, three steps in the clip, one smooth continuous rhythm, never pausing, one "
    "foot per step, alternating. Her hands stay on the cardigan, off the rail. " + ONE_TAKE,
    "no slow motion, no slow careful steps, no pausing, no two feet on one step, no hand on the rail, " + ONE_TAKE_NEG)

FIX_NOTE = {  # user's Fix note -> where it was fixed (frame, prompt or motion, §22X)
 "MECH-01": "not the patellar tendon -> frame: front view, glow on the tendon itself",
 "MECH-10": "express the line more -> frame: bare bone on bone with spurs + red glow; motion: grind + flare",
 "MECH-15": "white at first -> frame: dim cyan, no white; prompt: dark from frame one, no flash",
 "BR-03": "strap stiff, no real physics -> frame: band as a slack closed loop; motion: band swings and settles",
 "BR-04": "wrong point, gelatin -> frame: fingertip on the tendon under the notch; motion: firm leg, no wobble",
 "BR-06": "wrong product, show the back pad -> frame: whole closed-loop strap from inside (back.webp)",
 "BR-12": "phone on the street -> prompt: no phone named anywhere, phone negatives",
 "BR-13": "not the stairs -> frame: on the P0 flight itself, mid-climb; motion: step per second",
 "BR-14": "should show a productive result -> frame: carrying laundry up onto the landing",
 "BR-16": "wrong placement -> user: use the confirmed seated end frame as the solo start image",
 "BR-17": "big box, wrong carry -> frame: big heavy box, safe squat lift, box hugged",
 "BR-19": "wrong product -> frame: tighter, strap large and clear, no knee pads",
 "BR-20": "strap wrong -> frame + motion: band as a soft closed loop draping",
 "BR-21": "phone on the street -> prompt: no phone named anywhere, phone negatives",
 "BR-22": "remove the hands so nothing distorts -> frame: the closed box alone; motion: slow push in only",
 "BR-24": "wrong product -> user: a productive B-roll -> frame: hanging washing in the garden, strap on the knee",
 "BR-25": "wrong stairs / going down, not already down -> frame: halfway down the P0 flight, hands full",
 "BR-26a": "wrong placement -> user: use the confirmed seated end frame BR-26a-END as the solo image, not the start frame",
 "BR-26b": "should be going up, not at the top -> frame: near the bottom; motion: climbs, still below at the cut",
}

PINNED = set()
SUBJECT_MOTION = {"BR-12": "travels", "BR-13": "travels", "BR-14": "travels", "BR-21": "travels", "BR-26b": "travels"}

if __name__ == "__main__":
    for b, j in P.items():
        s = json.dumps(j, ensure_ascii=False, separators=(",", ":"))
        assert "phone" not in s.lower().replace("no phone", "").replace("no smartphone", "").replace("no mobile phone", ""), b
        (HERE / f"{b}.v2.i2v.json").write_text(s + "\n")
        mech = b.startswith("MECH")
        c = {"beat": b, "connector": "kling", "mode": 1, "kind": "broll", "prompt": s, "duration": LEN[b],
             "resolution": "1080p", "aspect_ratio": "9:16", "start_image": f"{b} confirmed image", "start_approved": False, "fix_note": FIX_NOTE[b],
             "pinned": b in PINNED, "end_image": f"{b}-END fix2 image" if b in PINNED else None,
             "end_approved": False, "prefer_multi_shots": "false", "generation": 2,
             "subject_motion": "still" if mech else SUBJECT_MOTION.get(b, "in_place"), "pace": "named",
             "risks": [{"risk": "phone appears in frame", "prevented_by": "no phone named anywhere; phone negatives"},
                       {"risk": "product bends or wobbles", "prevented_by": "HOLD-PC rigid-shell clause + product negatives"},
                       {"risk": "the Fix-note fault repeats", "prevented_by": "fault fixed at source in image + motion"}]}
        (HERE / f"{b}.v2.call.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
        print(b, len(s))
