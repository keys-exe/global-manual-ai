#!/usr/bin/env python3
"""stryde-lost-moments — Hook 1 + Act 2 (Gloria, A-01…A-10) image prompts, condensed as sent.

Beats and camera come from actmap_rows.json (step 5); Gloria, the house and both outfits are carried by the confirmed
renders: C1 sheet (face, build), A-HKa (house, day-1 outfit), A-HKb (stairs from the side, day-2 outfit, strap worn).
A-08 reuses A-HKb (no new image). Higgsfield image jobs are failing (2026-09-29) → sent through Kie nano-banana-pro.
Usage: act2.py [BEAT …] → work/prompts/<beat>.sent.txt + <beat>.refs.json
"""
import json, sys, pathlib
HERE = pathlib.Path(__file__).parent
REF = "products/stryde/stryde_refs/"
C1 = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260928_131042_ded1fa0c-1546-421d-adb5-94c1baee2800.png"
HKA = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260928_190431_4c4ab2b6-976c-45ee-94a2-b5744f34eab4.png"
HKB = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_124144_f1d7edd9-45a2-42a4-bd8c-3b770ce383fe.png"

PHONE = ("Shot on an iPhone 17 Pro Max, the main 1x camera at 24mm, everything on automatic. An ordinary photo taken on an "
         "ordinary phone, propped still.")
GLORIA = ("GLORIA exactly as in image 1: a Black British woman of seventy-three, dark brown skin, short silver-white natural hair "
          "in small neat twists, tall and slender with a slight stoop, a thin pale scar through the outer end of her left eyebrow.")
HOUSE = ("HER HALL AND STAIRS exactly as in image 2: buttermilk-yellow plaster walls, chipped white gloss skirting, a deep-red "
         "patterned stair runner held by brass rods, white spindles, a dark mahogany handrail and turned newel post, "
         "red-and-cream encaustic hall tiles, the landing window at the top.")
D1 = ("Wearing her day-one outfit exactly as in image 2: a lilac knitted cardigan over a white blouse, a navy-and-green floral "
      "cotton skirt ending a hand's width above the knee so both knees are bare, flat burgundy house slippers.")
D2 = ("Wearing her day-two outfit exactly as in image 3: a coral short-sleeve blouse, a navy linen skirt ending above the knee, "
      "flat burgundy slippers.")
STRAP = ("THE STRAP exactly as in images 4 and 5 — a matte-black shell with two rounded peaks either side of a concave notch, "
         "black knit band, a brushed chrome slide at each end, a lowercase grey stryde wordmark centred and readable — a single "
         "unit on her RIGHT leg, snug directly under the kneecap exactly as in image 5, the kneecap uncovered. About as wide as the knee.")
FILE = "Candid phone file: Smart HDR flat shadows, natural colour, real skin with pores and lines, no retouching, framing off-centre."
NEG = ("no camera app interface, no on-screen buttons, no icons, no text overlays, no stock retiree face, no AI face, no plastic "
       "skin, no CGI look, no film grain, no vignette, no second person")
NOSTRAP = "no knee strap, no knee support, no brace, no walking stick, no stairlift"
STRAPNEG = "no strap on the left knee, no second strap, no strap low on the shin, no strap over the kneecap, no misspelled wordmark"
GREY = "THE LIGHT: grey, soft morning light from the landing window — the problem state, flat and cool, never moody."
SUN = "THE LIGHT: warm afternoon sun through the front-door glass — after, bright and clean."

def refs(day, strap=False):
    r = [("C1 sheet", C1), ("A-HKa (house, day-1)", HKA)]
    if day == 2: r.append(("A-HKb (day-2 outfit)", HKB))
    if strap: r += [("front.webp", REF + "front.webp"), ("worn_front.jpg", REF + "worn_front.jpg")]
    return r

def head(day, strap=False):
    n = ["1 = Gloria", "2 = her hall and stairs"] + (["3 = her day-two outfit"] if day == 2 else [])
    if strap: n += [f"{len(n)+1} = the product", f"{len(n)+2} = the product worn"]
    return "Attached images, in order: " + "; ".join(n) + "."

B = {}
B["A-01"] = (1, False, "THE CAMERA ANGLE: from above, three-quarter on to her, so the drop of the stairs in front of her looks long and she looks small.\nFOCUS: sharp on her nearest eye; the stairs below fall soft.",
  "Medium close-up at the TOP of the stairs on the landing: she stands at the edge of the first step looking down the flight, her right hand on the mahogany handrail, caught mid-breath before the first step, lips slightly parted, brow tight with dread. Her face fully visible. A real, particular face — not a catalogue face.",
  GREY, "no smile, " + NOSTRAP)
B["A-02"] = (1, False, "THE CAMERA ANGLE: the lens a few centimetres off the stair, three-quarter on to her feet.\nFOCUS: sharp on the nearest slipper; everything beyond falls soft.",
  "Extreme close-up of her feet on the stairs: both burgundy slippers turned SIDEWAYS across the deep-red runner, her right foot caught mid-slide sideways down onto the next step, her left foot still on the step above taking the weight, the brass stair rod gleaming, her bare ankles and the hem of the floral skirt at the top edge of the frame. Only feet, ankles and shins in frame.",
  GREY, "no face in frame, no feet facing forwards, " + NOSTRAP)
B["A-03"] = (1, False, "THE CAMERA ANGLE: at eye height, from the side, in profile, so the handrail runs across the frame.\nFOCUS: sharp on her hand; the stairs behind fall soft.",
  "Close-up of her right hand clamped hard on the dark mahogany handrail, white-knuckled, the tendons standing out, caught as her weight comes down onto it, the lilac cardigan cuff at the edge of the frame, the white spindles below. Only the hand, wrist and rail in frame.",
  GREY, "no face in frame, no relaxed grip, no gloves")
B["A-04"] = (2, False, "THE CAMERA ANGLE: at eye height, three-quarter on to her.\nFOCUS: sharp on her nearest eye; the landing behind falls soft.",
  "Medium close-up on the landing at the top of the stairs: her face easing, eyes closing for a moment, shoulders caught dropping as she breathes out, the first real relief in months, a hint of a smile coming. Framed from mid-chest up; her knees are below the frame. Her face fully visible. A real, particular face — not a catalogue face.",
  "THE LIGHT: soft afternoon light from the landing window on the left of frame — the turn, the window side of her face lit.", "no strap in frame, no grin, no hands on the face")
B["A-05"] = (2, True, "THE CAMERA ANGLE: at eye height, from the side, in profile, the camera still — like image 3.\nFOCUS: sharp on the strap and its wordmark; everything else stays clear.",
  "From the side and waist-down, framed like image 3: she comes down the stairs FACING FORWARDS, caught mid-step, her left foot reaching down onto the next step, her right foot on the step above, the strap on her right knee, one hand resting lightly on the mahogany handrail, knees bending easily, balanced and confident. Her face is above the frame.",
  SUN, "no gripping, no sideways, no backwards, " + STRAPNEG)
B["A-06"] = (2, True, "THE CAMERA ANGLE: the lens on the hall tiles at the foot of the stairs, looking up the last steps from the front.\nFOCUS: sharp on the bottom step; the steps above fall slightly soft.",
  "Extreme close-up from the hall floor: her feet in burgundy slippers coming down the last two steps TOWARD the lens, one foot per step, her right foot caught landing on the bottom step, her left foot lifting off the step above, the deep-red runner and brass rods, the red-and-cream tiles in the near foreground. Her right knee with the strap on it just visible at the top edge of the frame, the wordmark readable.",
  SUN, "no face in frame, no sideways feet, " + STRAPNEG)
B["A-07"] = (2, False, "THE CAMERA ANGLE: at eye height, directly behind her, the camera still.\nFOCUS: everything sharp from near to far.",
  "Medium shot from behind, waist-up: she walks away from the lens down the hall toward the bright kitchen doorway at the far end, caught mid-stride, arms swinging loosely, shoulders straight, an easy pace. The hall tiles and the foot of the stairs at the side of the frame.",
  "THE LIGHT: bright afternoon light spilling from the kitchen doorway ahead — after, open and warm.", "no face in frame, no stick, no hand on the wall")
B["A-09"] = (1, True, "THE CAMERA ANGLE: low, at hip height, three-quarter on to her, looking up the flight past her.\nFOCUS: sharp on her nearest eye; the stairs above stay clear.",
  "Medium shot from the hall: she stands at the foot of the stairs, her hand on the turned newel post, caught as she lifts her eyes up the flight, chin up, ready, the strap on her right knee below the hem of her floral skirt. Her face fully visible, calm resolve. A real, particular face — not a catalogue face.",
  "THE LIGHT: morning daylight through the front-door glass from the right — the turn, the window side, soft and clean.", STRAPNEG)
B["A-10"] = (2, False, "THE CAMERA ANGLE: from above, three-quarter on to her, the stairs below her.\nFOCUS: sharp on her nearest eye.",
  "Medium close-up on the landing at the top of the stairs: she is caught as a small, private smile starts, looking down the flight she has beaten, one hand resting lightly on the handrail, about to step down. Framed from the waist up. Her face fully visible. A real, particular face — not a catalogue face.",
  "THE LIGHT: warm afternoon sun from the landing window on the left of frame — after, bright.", "no big grin, no looking at the camera")

def build(b):
    day, strap, cam, frame, light, neg = B[b]
    parts = [head(day, strap), PHONE, cam, HOUSE, GLORIA, frame, D1 if day == 1 else D2]
    if strap:
        k = 4 if day == 2 else 3
        parts.append(STRAP.replace("images 4 and 5", f"images {k} and {k+1}").replace("image 5", f"image {k+1}"))
    parts += [light, FILE, "AVOID: " + neg + ", " + NEG]
    return "\n\n".join(parts), refs(day, strap)

if __name__ == "__main__":
    out = HERE / "prompts"
    for b in sys.argv[1:] or B:
        p, r = build(b)
        (out / f"{b}.sent.txt").write_text(p)
        (out / f"{b}.refs.json").write_text(json.dumps(dict(model="nano-banana-pro (Kie)", refs=r), indent=1))
        print(b, len(p), [x[0] for x in r])
