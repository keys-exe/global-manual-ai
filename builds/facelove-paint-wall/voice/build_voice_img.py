#!/usr/bin/env python3
"""§22U step 1 — the talking-head images (also the Kling voice-source start frame and the HeyGen avatar images).
One recording day (REC), three looks: N-VOICE-SHELF-B (bare, at the shelves — hook + Act 1), N-VOICE-WALL-B (bare, at the plaster wall — Acts 2–3),
N-VOICE-SHELF-A (finished, at the shelves — Acts 4–5). The phone on a tripod at chest height (the inspo's presenter set-up, §22E).
Refs: Image 1 the confirmed plate (L-SHELF / L-WALL), Image 2 her confirmed sheet (N-BEFORE v4 / N-AFTER v1) — the REC outfit is the sheet outfit."""
import re, pathlib
HERE = pathlib.Path(__file__).parent
T = (HERE.parents[2] / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i): return re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S).group(1).strip()
FRAME = ("THE PERSON DOES NOT FILL THE FRAME. The phone stands on a tripod at her chest height about two metres in front of her, pointing straight at her, "
         "so the room is part of the picture: she stands waist-up in the centre of a vertical 9:16 frame, a clear band of the room above her head, "
         "her arms relaxed at her sides with both hands out of frame below the waist. Nobody is holding the camera.")
ROOM = {
 "SHELF": ("Image 1 is her dressing room seen toward the shelves: the same two long white floating shelves lined with about forty unlabelled foundation bottles of different shapes and caps, "
           "the same low white dresser under them, the same tall window with the sheer linen curtain on the left, the same white door on the right — copied exactly, nothing redesigned, "
           "recomposed into a vertical 9:16 frame with the shelves of bottles filling the wall behind her head and shoulders."),
 "WALL": ("Image 1 is the same room seen toward the bare wall: the same warm peach-beige plaster wall prepared for painting, the masking tape along the white skirting, "
          "the same tall window with the sheer linen curtain on the right — copied exactly, nothing redesigned, recomposed into a vertical 9:16 frame: "
          "she stands a step to the right of the wall's centre with the bare plaster filling the frame behind her and to her side."),
}
WHO = ("Image 2 is her reference sheet — the FACE CLOSE-UP panel is how her face must look here: a white American woman of fifty-seven with light warm-beige skin, a long oval face with high cheekbones "
       "and a firm jaw, light grey-green almond eyes under full softly arched brown brows, a straight narrow nose, full lips; shoulder-length layered mid-brown hair with caramel-blonde highlights "
       "and a little silver at the parting, worn loose with a soft side parting falling forward over the left side of her face — unchanged in face, age and build. "
       "Wearing the oatmeal textured-linen blazer open over the white ribbed scoop-neck tank, exactly as on her sheet. No glasses, no jewellery.")
POSE = ("CAMERA STRAIGHT IN FRONT OF HER AT CHEST HEIGHT, square to her — not above, not below, not to one side. FULL FACE TO THE CAMERA: nose pointing at the lens, both eyes on the lens, "
        "head upright and level, shoulders square. Mouth closed, about to speak, ")
SKIN = {
 "B": ("a bold, knowing look — a woman about to tell you something you didn't know. "
       "HER SKIN EXACTLY AS ON HER SHEET: bare face, no makeup at all — clearly visible deep brownish-plum dark circles under both eyes with puffy bags, deep crow's feet, "
       "four deep forehead furrows, two frown lines, deep folds from the nose to the mouth and marionette lines, dull grey-sallow matte skin with no glow. "
       "SKIN SURFACE IS GEOMETRY, NOT PATTERN: every pore a small pit, every line a groove the light falls into, never one smooth sheen. Bare skin, unflattering."),
 "A": ("a warm, certain look — a woman who has the answer. "
       "HER SKIN EXACTLY AS ON HER SHEET: one thin, even layer of foundation exactly matched to her light warm-beige skin and nothing else — no eye makeup, no lipstick: "
       "the tone even, the dark circles and sun spots covered, pores still visible on the nose and cheeks, the crow's feet, the forehead lines and the folds from the nose to the mouth all still there; "
       "the skin reads as skin. SKIN SURFACE IS GEOMETRY, NOT PATTERN: every pore a small pit, every line a groove the light falls into, never one smooth sheen."),
}
EYES = "EYES — a small catchlight from the window in each eye, both in the same position; a wet line of tear film along each lower lid; lashes natural and uneven."
LIGHT = {
 "SHELF": ("Bright midday daylight through the sheer curtain of the tall window on the left — camera-left — at about forty-five degrees off the lens, soft and clean, "
           "the left side of her face as we see it brighter, the far side a little darker with open shadows, the room high-key and airy. White balance about 5600K. Daylight only, the downlights off."),
 "WALL": ("Bright midday daylight through the sheer curtain of the tall window on the right — camera-right — at about forty-five degrees off the lens, soft and clean, "
          "the right side of her face as we see it brighter, the far side a little darker with open shadows, the plaster's fine texture just showing. White balance about 5600K. Daylight only."),
}
NEG = ("no selfie, no arm reaching toward the camera, no hand holding a phone, no phone in frame, no front-camera wide-angle distortion, no camera above her, no camera below her, "
       "no three-quarter view, no profile, no head turned, no eyes looking off-camera, no head touching the top edge, no background hidden behind the body, no different room from Image 1, "
       "no different woman from Image 2, no makeup stick in frame, no bottle in her hands, no product in frame, no jewellery, no poreless skin, no airbrushed skin, no glowing skin, no glamour portrait, "
       "no lash extensions, no lip gloss, no readable text, no labels on the bottles, no logos")
LOOKS = {"N-VOICE-SHELF-B": ("SHELF", "B"), "N-VOICE-WALL-B": ("WALL", "B"), "N-VOICE-SHELF-A": ("SHELF", "A")}
for k, (room, face) in LOOKS.items():
    neg = NEG + (", no foundation, no concealer, no even skin tone, no hidden dark circles, no smooth young skin" if face == "B" else ", no heavy makeup, no eye makeup, no contour")
    p = "\n\n".join([S("CAM-LOCK"), FRAME, ROOM[room], WHO, POSE + SKIN[face], EYES, LIGHT[room], S("CAP-A"), S("CAP-FILE"),
                     "AVOID: " + neg + ", " + S("NEG-M1") + "."])
    (HERE / f"{k}.prompt.txt").write_text(p); print(k, len(p))
