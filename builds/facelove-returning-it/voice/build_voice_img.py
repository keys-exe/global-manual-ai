#!/usr/bin/env python3
"""§22U step 1 — the talking-head image (also the Kling voice-source start frame and the HeyGen avatar image).
Two looks of one sitting (one recording day, §19): N-VOICE-IMG (finished face, N-AFTER — the body) and N-VOICE-IMG-B (bare face, N-BEFORE — the hooks).
Propped phone on the vanity = the L-VANITY plate's own viewpoint. Refs: Image 1 the L-VANITY plate, Image 2 her sheet."""
import re, pathlib
HERE = pathlib.Path(__file__).parent
T = (HERE.parents[2] / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i): return re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S).group(1).strip()
FRAME = ("THE PERSON DOES NOT FILL THE FRAME. The phone sits where a creator filming themselves would actually put it: propped against a jar on her white vanity desk, "
         "at her chest height and about a metre away, pointing straight at her, so the room is part of the picture — a clear band of the bedroom wall above her head, "
         "the end of the made bed behind her, the window with sheer curtains on the left. She sits in the white upholstered vanity chair, chest-up, the near edge of the white vanity top "
         "across the bottom of the frame, her hands resting on the vanity edge in the lower third. Nobody is holding the camera.")
ROOM = ("Image 1 is her bedroom, seen from the vanity: the same white upholstered chair with the low curved back, the same made bed with the cream knit throw and two linen pillows behind it, "
        "the same tall window with sheer white curtains on the left-hand wall, the same framed print in clay and sand colours above the bed, the same cream lamp on the nightstand on the right — "
        "copied exactly, nothing redesigned, recomposed into a vertical 9:16 frame around her.")
WHO = ("Image 2 is her reference sheet — the FACE CLOSE-UP panel is how her face must look here: a Latina American woman of forty-six with warm olive-tan skin, a long oval face with high full cheekbones, "
       "warm brown almond eyes under softly arched dark-brown brows, a straight slim nose, full lips, the fold from the left side of her nose to her mouth a touch deeper than the right; "
       "long thick dark-brown hair with warm caramel highlights in big soft waves, deep side parting, falling over her shoulders — unchanged in face, age and build. "
       "Wearing the cream-white fluffy sherpa bathrobe with the wide shawl collar over a white camisole, exactly as on her sheet. No glasses, no jewellery.")
POSE = ("CAMERA STRAIGHT IN FRONT OF HER AT CHEST HEIGHT, square to her — not above, not below, not to one side. FULL FACE TO THE CAMERA: nose pointing at the lens, both eyes on the lens, "
        "head upright and level, shoulders square. Mouth closed, about to speak, ")
SKIN = {
 "N-VOICE-IMG": ("an amused, slightly exasperated look — a friend about to tell you something. "
   "HER SKIN: one thin, even layer of foundation exactly matched to her olive-tan skin and nothing else — no eye makeup, no lipstick: the tone even, no redness, no brown patches, "
   "pores still visible on the nose and cheeks, the crow's feet, the forehead lines, the frown lines and the folds from the nose to the mouth all still there; the skin reads as skin. "
   "SKIN SURFACE IS GEOMETRY, NOT PATTERN: every pore a small pit, every line a groove the light falls into; the light breaks across it into many tiny highlights and shadows, never one smooth sheen."),
 "N-VOICE-IMG-B": ("a cross, fed-up look — a friend about to vent. "
   "HER SKIN: bare face, no makeup at all — blotchy redness across both cheeks and around the nostrils, uneven patches of darker brown pigmentation high on the cheekbones and the forehead, "
   "a scatter of small flat brown post-acne marks along the jaw and chin, brownish-violet dark circles, deep crow's feet, three forehead lines, two frown lines, deep folds from the nose to the mouth. "
   "SKIN SURFACE IS GEOMETRY, NOT PATTERN: every pore a small pit, every line a groove the light falls into; the light breaks across it into many tiny highlights and shadows, never one smooth sheen. Bare skin, unflattering."),
}
EYES = ("EYES — a small catchlight from the window in each eye, both in the same position; a wet line of tear film along each lower lid; lashes natural and uneven.")
LIGHT = ("Late-afternoon daylight through the sheer curtains of the window on her right-hand side — camera-left — at about forty-five degrees off the lens, soft and warm, "
         "the left side of her face as we see it brighter, the bed and the far side of the room a stop darker, shadows open. White balance about 5000K. Daylight only, the lamp off.")
NEG = ("no selfie, no arm reaching toward the camera, no hand holding a phone, no phone in frame, no front-camera wide-angle distortion, no camera above her, no camera below her, "
       "no three-quarter view, no profile, no head turned, no eyes looking off-camera, no head touching the top edge, no background hidden behind the body, no different room from Image 1, "
       "no different woman from Image 2, no makeup stick in frame, no product in frame, no jewellery, no poreless skin, no airbrushed skin, no glowing skin, no glamour portrait, no lash extensions, no lip gloss")
for k, sk in SKIN.items():
    neg = NEG + (", no foundation, no concealer, no even skin tone" if k.endswith("-B") else ", no heavy makeup, no eye makeup, no contour")
    p = "\n\n".join([S("CAM-LOCK"), FRAME, ROOM, WHO, POSE + sk, EYES, LIGHT, S("CAP-A"), S("CAP-FILE"),
                     "AVOID: " + neg + ", " + S("NEG-M1") + "."])
    (HERE / f"{k}.prompt.txt").write_text(p); print(k, len(p))
