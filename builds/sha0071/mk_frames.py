import json, sys
from strings import *
from mk_plate import LIGHT
AGE_P = ("deep nasolabial folds and marionette lines, a softening jawline with the start of jowls, hollows and dark circles under the eyes with crepey fine lines, two horizontal forehead creases, a thin everyday foundation settled into the lines around her eyes and mouth, the skin tone a little grey and flat")
AGE_R = ("fine crow's feet, faint lines from nose to mouth, light freckling across the nose, the skin just softening under the jaw, light everyday makeup")
SKIN = lambda age: (f"Real unretouched skin at near-macro fidelity: {age}, uneven individually resolved pores, vellus hair at the jaw catching the key, soft sheen breaking into separate micro-highlights on the forehead and nose against matte, slightly rough cheeks, dry lined lips. Every line and pore casts its own tiny shadow under the key. Highlights break at pore level, never smooth.")
SKIN_B1 = ("SKIN SURFACE IS GEOMETRY, NOT PATTERN — the face is not a flat surface with texture printed on it. Every pore is a small pit with one wall in shadow and one wall catching the light. Every line and crease is a groove the light falls into and does not fully reach the bottom of. "
 "The whole surface is minutely uneven, rising and dipping, so the light breaks across it into thousands of separate tiny highlights and thousands of separate tiny shadows rather than sweeping smoothly over it. The skin has relief and casts shadow onto itself.")
PAULA = ("PAULA, 58, exactly the woman in the attached Paula reference sheet — a Black American woman with deep brown, melanin-rich skin, an oval face with dropped cheekbones, heavy slightly hooded eyes, a broad nose, full lips turning down at the corners, black hair heavily streaked with grey pulled into a low loose bun with wisps at the temples, small silver hoop earrings. "
 "Wearing a charcoal grey textured wool-blend blazer worn open, a plain black scoop-neck knit top, charcoal tailored trousers and black low-heeled pumps, in charcoal and black.")
ROBIN = ("ROBIN, 48, exactly the woman in the attached Robin reference sheet — a white American woman with fair, lightly freckled skin, a heart-shaped face, warm brown eyes under arched dark brows, shoulder-length layered brown hair with caramel highlights worn loose with a side parting, small gold hoop earrings and a fine gold chain with a small round disc pendant. "
 "Wearing a navy tailored blazer over an ivory draped silk V-neck blouse, navy tailored trousers and black pumps, in navy and ivory.")
PROPS_P = "a buff manila folder held upright against her waist in both hands, her hands clasped over its lower edge, with a white plastic visitor badge clipped to the folder's top corner, a red band across the badge printed with the single word VISITOR"
PROPS_R = "a black leather padfolio held closed and low at her right hip in her right hand, her left arm relaxed at her side"
ST_P = lambda extra="nothing": (f"PAULA still carries exactly what this scene has done to her so far: eyes dry, face as in her sheet with the foundation settled in the lines, hair in its low bun with the loose wisps at the temples, blazer open, {PROPS_P}, standing a step out from the meeting-room glass facing down the corridor toward Robin. "
 f"None of it resets: it is the same as in the previous shot, except {extra}. It holds in every frame.")
ST_R = lambda extra="nothing": (f"ROBIN still carries exactly what this scene has done to her so far: eyes dry, face as in her sheet, hair loose, blazer buttoned, {PROPS_R}, standing about two metres further down the corridor toward the lift facing back up it toward Paula. "
 f"None of it resets: it is the same as in the previous shot, except {extra}. It holds in every frame.")
FRONT_END = ("the corridor running back behind her to frosted-glass double doors into the open-plan office, soft and out of focus")
def angle(h, side, subj, fg=None):
    H = {"eye":"the lens at the subject's eye height, level","high":"the lens above head height, looking down at the subject","low":"the lens at hip height, looking up at the subject","overhead":"the lens directly above, looking straight down"}[h]
    return f"THE CAMERA ANGLE: {H}, seen from {side} of {subj}" + (f", looking past {fg}, soft in the near foreground" if fg else "") + ". This exact angle, not a straight-on eye-level view."
def focus(plane, deep):
    return f"FOCUS: {plane} is in sharp focus; {deep}. The blur is optical: soft and round, never smeared."
FF = lambda scale, share: ("The frame is composed by a camera operator. The subject is placed deliberately off-centre, with looking room in the direction they face and headroom set for the shot size. The room is arranged in depth behind them, and no edge of the frame cuts the body at a joint. "
 f"The person never fills the frame edge to edge: this is a {scale}, and the person takes up {share} of the frame height, with the room around them part of the composition.")
EMO = lambda name, s: f"The face holds exactly where {name} is at this moment of the scene: {s}. Not a neutral face and not a posed expression, but a person in the middle of a feeling."
KEY = lambda scale, who, pos, off: ("THE SAME SCENE as the attached scene master frame: the same room, the same moment in the story, the same light from the same side, the same colours, the same wardrobe and the same prop positions. Nothing has changed and nothing has moved. "
 f"This is a {scale} of {who}, taken from {pos}, on the same side of the action line as the master. {off}")
CK = open('colour_key.txt').read().strip() if __import__('os').path.exists('colour_key.txt') else None
NEG_P = ", ".join([NEG_FILM, NEG_SCENECUT, NEG_BODY, NEG_SKIN, NEG_TEX, NEG_LIGHT, "no readable text anywhere except the single word VISITOR on the badge, no logos, no extra people, no tears"])
EMO_P0 = "composed and braced, jaw set a little, eyes steady on Robin and already reading her face, breath held high and shallow, a hope she is not letting show"
EMO_P1 = "the news half-landed: eyes steady but the lids a touch heavier, mouth pressed flat, the jaw holding, the breath let out slowly through the nose"
EMO_P2 = "listening hard and very still, eyes fixed on Robin, the brow faintly drawn, lips closed and slack, the first chill of what is coming arriving under the composure"
EMO_P3 = "stopped: eyes gone still and slightly unfocused, fixed just past Robin, the jaw loose, lips just parted, no breath moving, the face emptied rather than hurt"
EMO_R0 = "uncomfortable and kind, the brow slightly lifted in the middle, eyes soft and searching Paula's face, lips pressed together before speaking, shoulders a little drawn"
EMO_R1 = "decided: the chin lifted a fraction, eyes level and steady on Paula, lips parted on the first word, the kindness firm now"
def light(side): return LIGHT("THE OVERCAST DAYLIGHT THROUGH THE MEETING-ROOM GLASS", side)
def tail(depth_fg, depth_who):
    s = PROD_DEPTH(depth_fg, depth_who) 
    return s
F = {}
F["F-MASTER"] = " ".join([CAM(25, "T4", "a locked tripod at standing eye height"),
 "SCENE SC-01 MASTER FRAME: the establishing shot of this scene, and the reference every other shot in the scene is built against. The upper-floor office corridor outside the glass meeting room, exactly as in the attached location plate, at mid-morning on an overcast day, soft daylight through the meeting-room glass on frame left under the hard, cool overhead fluorescent panels. "
 "Everyone in the scene is in frame and placed where they will stay: PAULA stands in the near middle ground on the left, a step out from the meeting-room glass, turned toward Robin so her face is seen in a clear three-quarter profile; ROBIN stands about two metres further down the corridor on the right, just stopped, facing back up the corridor toward Paula, her face in three-quarter view and fully readable. Both stand; neither sits. "
 f"The action line runs down the corridor between them, and the camera sits on the meeting-room-glass side of it. Every prop is in its starting position: Paula has {PROPS_P}; Robin has {PROPS_R}.",
 angle("eye", "the side, in profile,", "the two women facing each other", "the brushed aluminium edge of the meeting-room glass wall"),
 focus("the nearest eye of Paula and Robin's face", "the lift lobby at the far end falls to a soft, recognisable shape"),
 FF("MEDIUM two-shot", "about three quarters"), PROD_DEPTH("the aluminium edge of the meeting-room glass wall", "Paula and Robin"),
 PAULA, ROBIN, BODY_WHOLE, EMO("Paula", EMO_P0), EMO("Robin", EMO_R0), ST_P(), ST_R(),
 light("FRAME LEFT"), LOOK, PHYS_FRAME, CAP, "NEGATIVES: " + NEG_P])
F["F-PAULA-OTS"] = " ".join([CAM(40, "T2.8", "a tripod raised above head height"),
 KEY("MCU", "PAULA", "further down the corridor, behind Robin's right shoulder, looking back up the corridor so the meeting-room glass is now on frame right and " + FRONT_END, "ROBIN is just off frame left, her shoulder and hair soft in the near foreground, so Paula's eyeline points just off the lens to frame left, toward her."),
 angle("high", "over the near shoulder of Robin", "Paula", "Robin's navy shoulder and brown hair"),
 focus("the nearest eye of Paula", "Robin's shoulder in front and the corridor behind her fall soft"),
 FF("MCU, chest up", "head and chest, the room readable to one side,"), PROD_DEPTH("Robin's navy shoulder", "Paula"),
 PAULA, BODY_WHOLE, EMO("Paula", EMO_P0), ST_P(), SKIN(AGE_P),
 light("FRAME RIGHT"), LOOK, "COLOUR_KEY", PHYS_FRAME, CAP, "NEGATIVES: " + NEG_P])
F["F-INS-BADGE"] = " ".join([CAM(65, "T2.8", "a tripod arm reaching out over the subject"),
 KEY("INSERT, ECU", "PAULA's hands and the folder", "just above and behind Paula's right shoulder, looking down over it at her hands, the way she sees them", "Robin stands just out of frame beyond the top edge."),
 angle("high", "over the near shoulder", "Paula's hands and the folder", "the charcoal shoulder of Paula's blazer"),
 focus("the hands and the badge they hold", "the charcoal trousers and grey carpet below fall soft"),
 f"INSERT: PAULA's two hands only — deep brown skin, short plain nails, the cuffs of the charcoal blazer at the wrists — holding the buff manila folder, which she has just tipped forward from her waist so its front cover faces up toward her eyes, the white plastic visitor badge clipped to its top corner. Her fingers are clasped over the folder's lower edge, her right thumb resting beside the badge. The badge is plain white plastic, a red band across it printed in bold white capitals with the single word VISITOR and nothing else, clearly readable. Nothing else on the folder reads.",
 BODY_WHOLE, ST_P("her eyes have dropped to the folder and she has tipped it forward toward her, the badge now facing up"), light("FRAME RIGHT"), LOOK, "COLOUR_KEY", PHYS_FRAME, CAP, "NEGATIVES: no face in frame, " + NEG_P])
F["F-ROBIN-OTS"] = " ".join([CAM(40, "T2.8", "a locked tripod at standing eye height"),
 KEY("MCU", "ROBIN", "just behind Paula's left shoulder, looking down the corridor toward the lift as the master does, tighter", "PAULA is just off frame left, her charcoal shoulder and the grey wisps of her bun soft in the near foreground, so Robin's eyeline points just off the lens to frame left, toward her."),
 angle("eye", "three-quarter front", "Robin", "Paula's charcoal shoulder and bun"),
 focus("the nearest eye of Robin", "Paula's shoulder in front and the lift lobby behind fall soft"),
 FF("MCU, chest up", "head and chest, the room readable to one side,"), PROD_DEPTH("Paula's charcoal shoulder", "Robin"),
 ROBIN, BODY_WHOLE, EMO("Robin", EMO_R0), ST_R(), SKIN(AGE_R),
 light("FRAME LEFT"), LOOK, "COLOUR_KEY", PHYS_FRAME, CAP, "NEGATIVES: " + NEG_P])
F["F-ROBIN-LOW"] = " ".join([CAM(40, "T2", "a low tripod at hip height"),
 KEY("MCU", "ROBIN", "Paula's position, lowered to hip height and a little to her right, looking up the line of her gaze at Robin with the lift lobby and ceiling panels behind", "PAULA is just off frame left, close, so Robin's eyeline points just off the lens to frame left and slightly down, toward her."),
 angle("low", "three-quarter front", "Robin", None),
 focus("the nearest eye of Robin", "the ceiling panels and lift lobby behind her fall to soft, recognisable shapes"),
 FF("MCU, chest up", "head and chest, the room readable to one side,"), PROD_DEPTH("nothing — the lens is clean —", "Robin"),
 ROBIN, BODY_WHOLE, EMO("Robin", EMO_R1), ST_R("she has just glanced back up the corridor and turned to Paula again, now decided"), SKIN(AGE_R),
 light("FRAME LEFT"), LOOK, "COLOUR_KEY", PHYS_FRAME, CAP, "NEGATIVES: " + NEG_P])
F["F-PAULA-MCU"] = " ".join([CAM(40, "T2", "a dolly at standing eye height"),
 KEY("MCU", "PAULA", "down the corridor on Robin's side, clean, level with Paula's eyes, looking back up the corridor so the meeting-room glass is on frame right and " + FRONT_END, "ROBIN is just off frame left, so Paula's eyeline points just off the lens to frame left, toward her."),
 angle("eye", "three-quarter front", "Paula", None),
 focus("the nearest eye of Paula", "the corridor behind her falls to a soft, recognisable shape"),
 FF("MCU, chest up", "head and chest, the room readable to one side,"), PROD_DEPTH("nothing — the lens is clean —", "Paula"),
 PAULA, BODY_WHOLE, EMO("Paula", EMO_P2), ST_P("the news of the third no has settled into her shoulders"), SKIN(AGE_P), SKIN_B1,
 light("FRAME RIGHT"), LOOK, "COLOUR_KEY", PHYS_FRAME, CAP, "NEGATIVES: " + NEG_P])
F["F-PAULA-CU"] = " ".join([CAM(50, "T2", "a locked tripod at standing eye height"),
 KEY("CU, head and shoulders", "PAULA", "the same side as the previous MCU, closer, level with her eyes, looking back up the corridor so the meeting-room glass is on frame right", "ROBIN is just off frame left, so Paula's eyeline points just off the lens to frame left, fixed just past her."),
 angle("eye", "three-quarter front", "Paula", None),
 focus("the nearest eye of Paula", "everything behind her falls to a soft blur of grey and pale glass"),
 FF("CU, head and shoulders", "a face about half the frame width, head and shoulders,"), PROD_DEPTH("nothing — the lens is clean —", "Paula"),
 PAULA, BODY_WHOLE, EMO("Paula", EMO_P3), ST_P("the word has landed: nothing visible has changed but the stillness"), SKIN(AGE_P), SKIN_B1,
 light("FRAME RIGHT"), LOOK, "COLOUR_KEY", PHYS_FRAME, CAP, "NEGATIVES: " + NEG_P])
for k, v in F.items():
    if CK: v = v.replace("COLOUR_KEY", CK)
    open(f"beats/SC01-{k}.t2i.txt", "w").write(v)
    print(k, len(v))
