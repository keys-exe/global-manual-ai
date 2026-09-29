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
# v2 (user Fix 2026-09-29: "shots don't match script") — every frame now shows exactly what its line says.
B["A-01"] = (1, False, "THE CAMERA ANGLE: at knee height, from the side, in profile, the camera still, so her leg and the step are large in frame and her face is visible above.\nFOCUS: sharp on her right knee and her face.",
  "ON EVERY STEP DOWN — the pain: from the side, she is caught mid-step coming DOWN her stairs, her right foot lowering onto the next step, her right knee bending under her full weight, and her face screwed up in a sharp wince of knee pain, eyes squeezed, lips pressed, one hand on the mahogany handrail. Framed from her head to her feet, the stair runner and white spindles behind her. Her face visible. A real, particular face — not a catalogue face.",
  GREY, "no smile, no relaxed face, " + NOSTRAP)
B["A-02"] = (1, False, "THE CAMERA ANGLE: at eye height, from the foot of the stairs, looking up the flight at her, the camera still.\nFOCUS: sharp on her; the stairs above fall slightly soft.",
  "THAT'S WHY YOU TURN SIDEWAYS: on her stairs she is coming down SIDEWAYS — her whole body turned side-on to the flight, her shoulder pointing down the stairs, both feet placed sideways across the same tread, one foot reaching sideways down to the step below, knees stiff, both hands on the mahogany handrail beside her. Unmistakably sideways, the awkward way people with bad knees get down. Full body in frame, head to feet. Her face in profile, concentrating. A real, particular face — not a catalogue face.",
  GREY, "no facing forwards, no facing down the stairs, no backwards, " + NOSTRAP)
B["A-03"] = (1, False, "THE CAMERA ANGLE: at eye height, three-quarter on to her, the camera still.\nFOCUS: sharp on her hands on the rail; her face stays clear.",
  "THAT'S WHY YOU GRIP THE RAILING: halfway down her stairs she clutches the dark mahogany handrail with BOTH HANDS, one over the other, knuckles pale, arms locked, leaning her weight onto the rail as she lowers herself one step, face tense. Framed from the waist up, the rail running diagonally across the frame, the white spindles below. Her face visible. A real, particular face — not a catalogue face.",
  GREY, "no one-handed grip, no relaxed hands, " + NOSTRAP)
B["A-04"] = (2, True, "THE CAMERA ANGLE: at eye height, three-quarter on to her, the camera still.\nFOCUS: sharp on her nearest eye.",
  "AND THE PAIN JUST LIFTS: on her stairs, one step down from the landing, the strap on her right knee, she has just stepped down and stopped — and it doesn't hurt. Surprise and relief on her face: eyebrows lifting, mouth opening into a disbelieving smile, one hand resting lightly on the rail. Framed from head to knees so the strap on her knee shows. Her face fully visible. A real, particular face — not a catalogue face.",
  "THE LIGHT: soft afternoon light from the landing window on the left of frame — the turn, the window side of her face lit.", "no grin to camera, " + STRAPNEG)
B["A-05"] = (2, True, "THE CAMERA ANGLE: from the hall at the foot of the stairs, at eye height, looking straight UP the flight at her as she comes down toward the lens, the camera still.\nFOCUS: sharp on her face and the strap.",
  "SO YOU COME DOWN FACING FORWARDS: seen from the front, from the bottom of the stairs, she walks down the middle of the flight FACING FORWARDS toward the lens, caught mid-step, one foot on the step below, the other lifting, hands free at her sides, head up, a relaxed confident smile. Full body, head to feet, the strap visible on her right knee below the skirt hem. Her face fully visible. A real, particular face — not a catalogue face.",
  SUN, "no sideways, no backwards, no gripping the rail, " + STRAPNEG)
B["A-06"] = (2, True, "THE CAMERA ANGLE: low, a few centimetres above the stair treads, from the front, looking up the steps at her feet and knees coming down, the camera still.\nFOCUS: sharp on her feet and the strap.",
  "ONE FOOT PER STEP: close on her feet and lower legs coming down the stairs normally, one foot per step — her left foot landing on one step while her right foot is already lifting toward the next step below, alternating like anyone walking downstairs, the deep-red runner and brass rods under her burgundy slippers, the strap on her right knee in the upper part of the frame, the wordmark readable. Framed from the knees down; no face.",
  SUN, "no two feet on the same step, no sideways feet, no face, " + STRAPNEG)
B["A-07"] = (2, True, "THE CAMERA ANGLE: at eye height from the hall, three-quarter on to her, the camera still.\nFOCUS: sharp on her.",
  "LIKE A NORMAL PERSON AGAIN: she comes down her stairs at an ordinary easy pace, carrying a small laundry basket on her hip with one hand, not holding the rail at all, chatting over her shoulder toward the kitchen with a laugh — an ordinary busy moment, the stairs no longer a problem. Caught mid-step near the bottom of the flight. Full body in frame, the strap on her right knee. Her face fully visible. A real, particular face — not a catalogue face.",
  SUN, "no holding the rail, no careful steps, " + STRAPNEG)
B["A-08"] = (2, True, "THE CAMERA ANGLE: from above, three-quarter on, looking down at her right knee as she sees it, the camera still.\nFOCUS: sharp on the strap and her hands.",
  "PUT ONE ON: she sits on the bottom stair of her staircase, her right leg bent, and fits the strap: both hands hold the strap by the band ends and it is sitting snug just below her right kneecap, fingertips beside the chrome slides, the wordmark readable. The deep-red runner under her, the turned newel post and white spindles beside her, the red-and-cream tiles at her feet. Framed on her knee, hands and lap; her face out of frame above.",
  "THE LIGHT: morning daylight through the front-door glass from the right — the turn, soft and clean.", "no face, no hand covering the wordmark, " + STRAPNEG)
B["A-09"] = (2, True, "THE CAMERA ANGLE: from the hall at the foot of the stairs, at hip height, looking up the flight past her, the camera still.\nFOCUS: sharp on her.",
  "GO TO YOUR OWN STAIRS: she walks UP her stairs with ease, caught mid-step two steps up from the bottom, her back three-quarter to the lens, one hand brushing the handrail without holding it, looking up the flight, the strap on her right knee visible from behind-side. Full body in frame.",
  SUN, "no struggling, no gripping, " + STRAPNEG)
B["A-10"] = (2, False, "THE CAMERA ANGLE: at eye height on the landing, three-quarter on to her, the camera still.\nFOCUS: sharp on her nearest eye.",
  "NOTHING TO LOSE BUT THE PAIN: at the top of her stairs, she looks back over her shoulder toward the lens with a warm, knowing, confident smile, one hand light on the newel at the top, about to go down the stairs without a care. Framed from the waist up, the flight falling away beside her. Her face fully visible. A real, particular face — not a catalogue face.",
  "THE LIGHT: warm afternoon sun from the landing window — after, bright.", "no big grin, no strap in frame")

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
