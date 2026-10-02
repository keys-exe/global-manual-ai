"""Scenes 11–13 — SEEDANCE 2.5 takes on Kie AI, ingredients only, no frames.
The user: "lets do the remaining scenes", then "fix those and generate the videos" (2026-10-02): OUT-N-A3, OUT-N-A4, PROD-BOX confirmed;
OUT-C3-A2 Fix "i want a different outfit" → v2 (navy gilet, striped shirt, stone chinos) To check — SC11-T1 renders once it is confirmed.
Takes (L51, one take per place): SC11-T1 living room (L058/L059); SC12-T1 SH01–SH03 (cross the café, L062/L063; VO L060–L061 in the edit);
SC12-T2 SH04–SH07 (L064–L067, the strap under the trouser hem); SC12-T3 SH08–SH09 (the strap on the table, the three laughing; VO L068);
SC13-T1 SH01–SH02 kitchen (the real box with two straps; VO L069–L071); SC13-T2 SH03–SH05 door → stairs (L072/L073; VO L074).
The box is the real photo (FP09) and appears only in the offer scene (FP19). Stairs: seen from the landing, the sister climbing toward the camera (FP16)."""
import json
import sys
import importlib.util
from pathlib import Path

H = Path(__file__).parent
B = H.parents[1]
_spec = importlib.util.spec_from_file_location("sc09_clips", B / "body" / "SC09" / "build_clips.py")
S9 = importlib.util.module_from_spec(_spec)
_argv = sys.argv
sys.argv = [sys.argv[0], "__none__"]
_spec.loader.exec_module(S9)
sys.argv = _argv
S9.SHOTS.clear()
take, manifest, PLACE, VOICE, SHEET, dialogue = S9.take, S9.manifest, S9.PLACE, S9.VOICE, S9.SHEET, S9.dialogue
HER_ID, FACE_N, STRAP, KITCHEN, VOICE_N, HER_A2, CARD_A2, STRAP_PLACE = S9.HER_ID, S9.FACE_N, S9.STRAP, S9.KITCHEN, S9.VOICE_N, S9.HER_A2, S9.CARD_A2, S9.STRAP_PLACE
HOUSE, STAIRS, HALL = S9.S7.HOUSE, S9.S7.STAIRS, S9.S7.HALL
STEPS = "Each step is spelled out: one foot lifts onto the very next tread and lands flat, then the other foot onto the tread above it — one tread per step, never skipping a tread, never shuffling."

HUS_ID = "a solid, slightly stooped man of seventy-four with short thinning grey hair"
HUS_A2 = "a navy quilted zip-up gilet over a blue-and-white fine-striped shirt, stone-coloured chinos and dark-brown suede slippers — exactly his outfit card"
SIS_ID = "a short, heavy woman of sixty-eight with short strawberry-blonde permed curls greying at the roots and rosy cheeks"
SIS_W = "a lilac zip-up fleece over a navy-and-white floral blouse, navy trousers and beige walking shoes — exactly her sheet"
F1_ID = "a tall, lean woman of sixty-nine with short hennaed copper-red hair and freckles"
F1_W = "a navy pea coat worn open over a red-and-cream Breton striped top — exactly her sheet"
F2_ID = "a short, full-figured Black British woman of seventy-two with short salt-and-pepper natural hair in a close rounded afro"
F2_W = "a mustard corduroy jacket over a black polo-neck jumper — exactly her sheet"
HER_A3 = "a soft terracotta crew-neck jumper, navy wide-leg trousers and tan leather loafers — exactly her outfit card"
HER_A4 = "a soft cream cardigan open over a coral silk blouse, oatmeal trousers and white trainers — exactly her outfit card"
CARD = lambda who, what: f"is an info card: {who}'s outfit on this day — {what}; follow it exactly, and its caption strip never appears in the clip."
CAFE = PLACE("the café of the plate — the round wooden table by the big front window with three bentwood chairs, the counter with the glass cake display, the exposed brick wall, the warm pendant lights")
LIVING = PLACE("the front living room seen from the hall doorway — the bay window with net and green velvet curtains, the tiled fireplace on the right with the brown leather armchair angled beside it, the floral sofa, the standard lamp")
CAFE_SO_FAR = ("THE SCENE SO FAR, a weekday late morning a few weeks later, one continuous moment in the café: honeyed daylight about 4800K from the big front window on the left. "
               "Her two friends sit at the round window table: the copper-haired friend in the chair facing into the room, the friend in the mustard jacket beside the window; the third chair, facing the window, is empty for Her. "
               "Two cups of coffee and a third cup waiting. THE POSITIONS NEVER CHANGE once she sits. THE CLOTHES NEVER SWAP: the copper-haired friend wears the NAVY PEA COAT over the red-and-cream Breton top; the friend with the salt-and-pepper afro wears the MUSTARD CORDUROY JACKET over the black polo-neck; Her wears only her terracotta jumper, no coat.")
GO = "chat (2026-10-02): \"fix those and generate the videos\" — the ingredients confirmed on the board (OUT-N-A3, OUT-N-A4, PROD-BOX; OUT-C3-A2 v2 for SC11)"
GO3 = "board Fix note + chat \"fix those\" (2026-10-02) — the user's go for SC13-T2 gen 3 (gen 4 waits for a new go)"
NOTES_ALL = {"SC13-T2": ["agent's check of v1 (L16): Her and her sister swapped places → Her inside, the sister outside until SHOT 3", "the user (board Fix): she should not hold the hand rail → hands free, nobody touches the banister", "agent's check of v3 (L16): places swapped again, a hand on the newel post"]}
FIX = "first generation — every earlier note on this build kept: one strap only, small (12 × 5 cm), front side up, on the RIGHT knee, centred on the front of the knee; the box only in the offer (FP09, FP19); one take per place (L51); stairs foot by foot (FP16)"
L058, L059 = "You were gone a long time.", "I know."
L062 = "Right. What’s changed? And don’t say a haircut."
L063 = "Three weeks ago I couldn’t have crossed this room like that."
L064, L065, L066, L067 = "So what is it?", "It’s a strap.", "That little thing?", "That’s what I said."
L072, L073 = "All the way up?", "All the way up."
VOICE_C3 = "An English man of seventy-four from the north of England, a gruff, soft, low voice with a slight roughness, few words, plain northern vowels."
VOICE_C4 = "An English woman of sixty-eight, a soft, slightly breathless Midlands voice, warm and a little nervous."
VOICE_C5 = "An Irish woman of sixty-nine, a dry, quick, teasing voice with a soft Dublin lilt."
VOICE_C6 = "A Black British woman of seventy-two with a Jamaican-London lilt, warm, low and curious."

take("SC11-T1", 11, ["SC11-SH01", "SC11-SH02"], 6, "Scene 11 · T1 — You were gone a long time. / I know. (SH01–SH02)",
     ["C3", "OUT-C3-A2", "N-FACE", "OUT-N-A2", "L-LIVING"],
     [("@image1", SHEET("the husband", HUS_A2)), ("@image2", CARD("the husband", "the navy gilet, striped shirt, stone chinos, brown slippers")), ("@image3", FACE_N), ("@image4", CARD_A2), ("@image5", LIVING),
      ("@audio1", VOICE("the husband")), ("@audio2", VOICE("Her"))],
     f"THE SCENE SO FAR, the same afternoon, one continuous moment: warm afternoon light about 5000K through the bay window. Her husband sits in the brown leather armchair by the fire with his newspaper; Her has just come in from town and stands in the living-room doorway, two full brown paper shopping bags on the carpet at her feet. THE POSITIONS NEVER CHANGE. "
     f"SHOT 1, [0s-3s]: MEDIUM, eye level, three-quarter on the husband, {HUS_ID}, in {HUS_A2}, in the armchair, Camera on a tripod, locked: he lowers the newspaper, looks up at her across the room and says, plainly: " + L058 + " "
     f"SHOT 2, [3s-6s]: MCU, low and front-on on Her, {HER_ID}, in {HER_A2}, in the doorway, cheeks flushed from the walk, the two bags at her feet, Camera on a tripod, locked: she meets his eyes and says, with a small quiet smile: " + L059 + " "
     "The eyelines match across the room. Nobody looks into the lens.",
     None, "FOCUS: SHOT 1 his eyes; SHOT 2 her nearest eye. The blur is optical: soft and round, never smeared.",
     ("the husband in the leather armchair by the fire, newspaper up; Her in the doorway with two bags at her feet", "Her in the doorway smiling a little, the husband looking at her, newspaper lowered",
      ("HER", "home from town in her A2 outfit, two bags at her feet", "they have spoken")),
     [{"risk": "the voices swap", "prevented_by": "Audio1 husband, Audio2 Her, the exchange in order"},
      {"risk": "the room flips (HT22)", "prevented_by": "the plate from the doorway, the fire on the right"},
      {"risk": "a voice ref leaks words", "prevented_by": "the husband's ref is his own line; Her ref named voice only"}],
     "no strap visible, no third person, no voices swapped, no word left out",
     line=L058 + " " + L059, audios=["C3-L058", "N-STOOD"], kind="multi",
     dlg=["THE EXCHANGE, word for word and in this order: " + L058 + " " + L059 + " — the husband says the first line, Her answers with the second; nobody else speaks.",
          "Audio2 is only Her's voice: its words are never spoken in this clip.",
          dialogue("the husband", L058, VOICE_C3, "she has been out all day on her own, which hasn't happened in years.", "notices, gently. Stress on 'long'.", "plain, soft, matching the face in this shot.", "he is moved and won't say so, which leaks only through how long he looks at her."),
          dialogue("Her", L059, VOICE_N, "she knows exactly what he means.", "agrees, quietly happy. A beat before it.", "soft, warm, matching the face in this shot.", "she is back, which leaks only through the small smile.")])

take("SC12-T1", 12, ["SC12-SH01", "SC12-SH02", "SC12-SH03"], 14, "Scene 12 · T1 — she crosses the café to her friends; What's changed? / Three weeks ago… (SH01–SH03)",
     ["C5", "C6", "N-FACE", "OUT-N-A3", "L-CAFE"],
     [("@image1", SHEET("the copper-haired friend", F1_W)), ("@image2", SHEET("the friend in the mustard jacket", F2_W)), ("@image3", FACE_N), ("@image4", CARD("Her", "the terracotta jumper, navy wide-leg trousers, tan loafers")), ("@image5", CAFE),
      ("@audio1", VOICE("the copper-haired friend")), ("@audio2", VOICE("Her"))],
     CAFE_SO_FAR + " "
     f"SHOT 1, [0s-6.5s]: WIDE, eye level, three-quarter from behind the counter end, the back of a bentwood chair soft in the near foreground, Camera on a tripod, locked: Her, {HER_ID}, in {HER_A3}, comes in through the café door, no coat on, and walks across the open floor straight to the window table, easy and quick, and sits down in the empty chair; nobody speaks in this shot. "
     f"SHOT 2, [6.5s-10s]: MCU over Her's shoulder onto the copper-haired friend, {F1_ID}, in {F1_W}, who looks her up and down and says, dry and teasing: " + L062 + " "
     f"SHOT 3, [10s-14s]: CU, eye level, three-quarter on Her, settled in her chair, Camera on a tripod, locked: she meets her friend's eye and says, calm and sure: " + L063 + " "
     "Each cut lands on a completed action. The eyelines match across the table. Nobody looks into the lens.",
     "MOVE: in SHOT 1 she travels across the floor to the table and sits; the camera never moves.",
     "FOCUS: SHOT 1 deep; SHOT 2 the friend's eyes; SHOT 3 Her's nearest eye. The blur is optical: soft and round, never smeared.",
     ("Her comes in through the café door; her two friends at the window table", "the three seated at the window table, Her looking at her copper-haired friend",
      ("HER", "in the café in her A3 outfit", "she has sat down with her friends")),
     [{"risk": "the friends swap faces or seats", "prevented_by": "both sheets, seats fixed in the scene so far"},
      {"risk": "the voices swap", "prevented_by": "Audio1 the copper-haired friend, Audio2 Her, lines in order with speakers"},
      {"risk": "her walk turns into a limp", "prevented_by": "easy and quick, BRISK"}],
     "no swapped jackets, no copper-haired woman in a mustard jacket, no coat on Her, no limping, no running, no strap visible, no lettering or logos, no menu text, no voices swapped, no word left out",
     line=L062 + " " + L063, audios=["C5-L062", "N-STOOD"], kind="multi",
     dlg=["THE EXCHANGE, word for word and in this order: " + L062 + " " + L063 + " — the copper-haired friend says the first line, Her answers with the second; nobody else speaks.",
          "Audio2 is only Her's voice: its words are never spoken in this clip.",
          dialogue("the copper-haired friend", L062, VOICE_C5, "she has just watched Her cross the room like a younger woman.", "teases, curious. Stress on 'changed'.", "dry and quick, matching the face in this shot.", "she is genuinely amazed, which leaks only through the look up and down."),
          dialogue("Her", L063, VOICE_N, "three weeks ago she couldn't cross a room without holding on.", "states it, plain and proud. Stress on 'crossed'.", "calm and sure, matching the face in this shot.", "she is moved by it herself, which leaks only through the steadiness.")])

take("SC12-T2", 12, ["SC12-SH04", "SC12-SH05", "SC12-SH06", "SC12-SH07"], 11, "Scene 12 · T2 — So what is it? / It's a strap. / That little thing? / That's what I said. (SH04–SH07)",
     ["C6", "C5", "N-FACE", "OUT-N-A3", "L-CAFE", "PROD-FRONT", "INFO-KNEE-N"],
     [("@image1", SHEET("the friend in the mustard jacket", F2_W)), ("@image2", SHEET("the copper-haired friend", F1_W)), ("@image3", FACE_N), ("@image4", CARD("Her", "the terracotta jumper, navy wide-leg trousers, tan loafers")), ("@image5", CAFE),
      ("@image6", "is " + STRAP + "."), ("@image7", STRAP_PLACE), ("@audio1", VOICE("the friend in the mustard jacket")), ("@audio2", VOICE("the copper-haired friend")), ("@audio3", VOICE("Her"))],
     CAFE_SO_FAR.replace("the third chair, facing the window, is empty for Her", "Her sits in the third chair, facing the window") + " "
     f"SHOT 1, [0s-2.5s]: MCU, low, in profile on the friend in the mustard jacket, {F2_ID}, who leans forward over her coffee and asks: " + L064 + " "
     "SHOT 2, [2.5s-5s]: ECU, low three-quarter under the table, Camera on a tripod, locked: Her's hand lifts the hem of her navy wide-leg trouser an inch or two and the small strap of Image6 shows on her bare right knee, its shell on the front of the knee just under the kneecap as Image7 shows the place; her voice says, off-screen: " + L065 + " "
     f"SHOT 3, [5s-8s]: CU, eye level, front-on on the copper-haired friend, {F1_ID}, who peers down under the table, unconvinced, and says: " + L066 + " "
     f"SHOT 4, [8s-11s]: MCU, high three-quarter on Her, {HER_ID}, in {HER_A3}, who sits back and picks up her cup, and says with a little smile: " + L067 + " "
     "Each cut lands on a completed action. The eyelines match across the table. Nobody looks into the lens.",
     None, "FOCUS: SHOT 1 her eyes; SHOT 2 the strap sharp; SHOT 3 the friend's eyes; SHOT 4 Her's eyes. The blur is optical: soft and round, never smeared.",
     ("the three at the window table, the friend in the mustard jacket leaning forward", "Her sitting back with her cup, both friends looking at her",
      ("HER", "in the café in her A3 outfit, the strap under her trouser hem", "she has shown the strap")),
     [{"risk": "the strap wrong or oversized (FP01, FP02)", "prevented_by": "the real front photo, small, the place card for the place only"},
      {"risk": "the voices swap (three speakers)", "prevented_by": "three audio refs named, each line with its speaker"},
      {"risk": "a ref's words leak", "prevented_by": "refs named voice only, their words never spoken"}],
     "no strap on the left knee, no oversized strap, no strap on the kneecap, no second strap, no lettering or logos, no voices swapped, no word left out",
     line=" ".join([L064, L065, L066, L067]), audios=["C6-L064", "C5-L062", "N-STOOD"], kind="multi",
     dlg=["THE EXCHANGE, word for word and in this order: " + " ".join([L064, L065, L066, L067]) + " — the friend in the mustard jacket says the first line, Her the second, the copper-haired friend the third, Her the fourth; nobody else speaks.",
          "Audio2 and Audio3 are only voices: their words are never spoken in this clip.",
          dialogue("the friend in the mustard jacket", L064, VOICE_C6, "she can't wait any longer.", "asks, leaning in. Stress on 'what'.", "warm and curious, matching the face in this shot.", "she is excited, which leaks only through the lean."),
          dialogue("Her", L065 + " " + L067, VOICE_N, "she is showing them the thing that changed everything.", "plain, almost amused. Stress on 'strap' and 'said'.", "light and warm, matching the face.", "she was a sceptic too, which leaks only through the smile."),
          dialogue("the copper-haired friend", L066, VOICE_C5, "she expected something big.", "disbelieving, dry. Stress on 'little'.", "dry, matching the face in this shot.", "she is half-convinced, which leaks only through the second look.")])

take("SC12-T3", 12, ["SC12-SH08", "SC12-SH09"], 12, "Scene 12 · T3 — the strap on the café table; the three laughing together (SH08–SH09)",
     ["PROD-FRONT", "C5", "C6", "N-FACE", "OUT-N-A3", "L-CAFE"],
     [("@image1", "is " + STRAP + "."), ("@image2", SHEET("the copper-haired friend", F1_W)), ("@image3", SHEET("the friend in the mustard jacket", F2_W)), ("@image4", FACE_N), ("@image5", CARD("Her", "the terracotta jumper, navy wide-leg trousers, tan loafers")), ("@image6", CAFE)],
     CAFE_SO_FAR.replace("the third chair, facing the window, is empty for Her", "Her sits in the third chair, facing the window") + " "
     "SHOT 1, [0s-5s]: ECU, eye level, three-quarter on the café table, Camera on a tripod, locked: one strap of Image1 lies flat on the wood between the coffee cups, front side up, the grey stryde wordmark reading, its knit band one small closed loop folded flat under the shell; small, about 12 by 5 centimetres, smaller than the saucer beside it. Nothing moves but the steam from the cups. "
     f"SHOT 2, [5s-12s]: MEDIUM over the copper-haired friend's shoulder onto the window table, Camera on a tripod, locked: the three women laugh together, easy and warm — Her, {HER_ID}, in {HER_A3}, laughing with them, the friend in the mustard jacket wiping her eye, the strap still lying on the table between them. Nobody speaks words; only soft laughter.",
     None, "FOCUS: SHOT 1 the strap sharp; SHOT 2 their eyes, medium depth. The blur is optical: soft and round, never smeared.",
     ("one strap lying on the café table between the cups", "the three women laughing together at the window table, the strap between them",
      ("THE TABLE", "the strap lying among the cups", "they are laughing")),
     [{"risk": "the strap redesigned on the table (FP01, FP22)", "prevented_by": "the real front photo, band folded under, front side up"},
      {"risk": "the strap too big (FP02)", "prevented_by": "against the saucer, 12 × 5 cm"},
      {"risk": "someone speaks words", "prevented_by": "only laughter, silent words"}],
     "no long band, no strap bending, no second strap, no lettering or logos other than the strap's own wordmark, no words spoken, no music",
     vo="L068")

take("SC13-T1", 13, ["SC13-SH01", "SC13-SH02"], 13, "Scene 13 · T1 — the box with two straps on the kitchen table; she looks out of the window (SH01–SH02)",
     ["N-FACE", "OUT-N-A4", "L-KITCHEN", "PROD-BOX"],
     [("@image1", FACE_N), ("@image2", CARD("Her", "the cream cardigan, coral blouse, oatmeal trousers")), ("@image3", KITCHEN),
      ("@image4", "is the real product box, copied exactly: the small matte-black box with the grey stryde wordmark on its lid, and inside, two straps side by side in a black tray — two, never one, never three; its white background never appears in the clip.")],
     "THE SCENE SO FAR, a Sunday afternoon some weeks later, one continuous moment in her kitchen: warm afternoon light about 5000K from the window over the sink; on the scrubbed pine table, the small black box of Image4 with its lid on. "
     "SHOT 1, [0s-6s]: ECU, high three-quarter over the table, Camera on a tripod, locked: Her's hands lift the lid off the small box and set it beside it — inside, exactly two straps lie side by side in the black tray, as Image4 shows. The box is small, about the size of a paperback book. "
     f"SHOT 2, [6s-13s]: CU, eye level, three-quarter on Her, {HER_ID}, in {HER_A4}, seated at the table, Camera on a tripod, locked: she looks down at the open box, quiet and content, then lifts her eyes and looks out of the window, waiting for someone, a small expectant smile.",
     None, "FOCUS: SHOT 1 the straps in the box sharp; SHOT 2 her nearest eye. The blur is optical: soft and round, never smeared.",
     ("the small black box with its lid on, on the pine table", "Her looking out of the window, the open box with two straps on the table in front of her",
      ("HER", "in the kitchen in her A4 outfit", "she has opened the box")),
     [{"risk": "the box or straps redesigned (FP01, FP09)", "prevented_by": "the real box photo, exactly two straps"},
      {"risk": "the box too big", "prevented_by": "the size of a paperback book"},
      {"risk": "lettering appears", "prevented_by": "only the wordmark on the lid"}],
     "no third strap, no single strap, no strap taken out, no big box, no other packaging, no lettering other than the wordmark, no talking, no mouth moving",
     vo="L069")

take("SC13-T2", 13, ["SC13-SH03", "SC13-SH04", "SC13-SH05"], 11, "Scene 13 · T2 — the sister at the door: All the way up? / All the way up. — her first step up the stairs (SH03–SH05)",
     ["C4", "N-FACE", "OUT-N-A4", "P-HOUSE", "L-STAIRS"],
     [("@image1", SHEET("the sister", SIS_W)), ("@image2", FACE_N), ("@image3", CARD("Her", "the cream cardigan, coral blouse, oatmeal trousers")), ("@image4", HALL), ("@image5", STAIRS),
      ("@audio1", VOICE("the sister")), ("@audio2", VOICE("Her"))],
     HOUSE + " THE SCENE SO FAR, the same Sunday afternoon, one continuous moment: the doorbell has just rung; cool daylight through the front-door glass. WHO IS WHERE: Her is INSIDE the house, in her own hall, the staircase behind her; her sister is OUTSIDE on the front doorstep in the daylight, and only comes in for SHOT 3. "
     f"SHOT 1, [0s-3.5s]: MEDIUM over Her's shoulder from inside the hall, Camera on a tripod, locked: Her, inside, opens the green front door toward the street; her sister, OUTSIDE on the doorstep with the street behind her, {SIS_ID}, in {SIS_W}, stands on the step — behind HER the front path, the street and the daylight sky, never the staircase — her eyes going straight past Her to the staircase, and asks, hopeful and nervous: " + L072 + " "
     f"SHOT 2, [3.5s-6.5s]: MCU, low three-quarter on Her, {HER_ID}, in {HER_A4}, standing INSIDE her hall holding the door open — behind HER the hall and the staircase, never the sky or the street, the camera outside on the step looking in at her — Camera on a tripod, locked: she nods once and says, sure and warm: " + L073 + " "
     "SHOT 3, [6.5s-11s]: FULL, high, from the landing at the top of the stairs looking down the flight as Image5 shows it, Camera on a tripod, locked: the sister, both hands free and down at her sides, never touching the banister or the newel post, takes the first step up toward the camera, then the second, walking up on her own; Her one step below and behind her, close, smiling, her hands free too and never on the banister. " + STEPS + " "
     "The eyelines match. Nobody looks into the lens.",
     "MOVE: in SHOT 3 they travel up two steps toward the camera; the camera never moves.",
     "FOCUS: SHOT 1 the sister's eyes; SHOT 2 Her's nearest eye; SHOT 3 deep. The blur is optical: soft and round, never smeared.",
     ("Her opening the green front door to her sister on the step", "the sister two steps up the stairs, hands free at her sides, Her one step below her",
      ("THE SISTER", "arrived in her lilac fleece", "she has started up the stairs")),
     [{"risk": "the voices swap", "prevented_by": "Audio1 sister, Audio2 Her, lines in order"},
      {"risk": "feet skip on the stairs (FP16)", "prevented_by": "STEPS, two steps only"},
      {"risk": "the hall flips (HT22)", "prevented_by": "HOUSE block, both plates"}],
     "no sister inside the house before SHOT 3, no Her outside on the doorstep, no swapped places, no going down the stairs, no stepping backwards, no Her going first, no hand on the banister, no hand on the rail, no gripping the rail, no strap visible, no voices swapped, no word left out",
     line=L072 + " " + L073, audios=["C4-REF", "N-STOOD"], vo="L074", kind="multi",
     dlg=["THE EXCHANGE, word for word and in this order: " + L072 + " " + L073 + " — the sister says the first line, Her answers with the second; nobody else speaks.",
          "Audio1 and Audio2 are only voices: their words are never spoken in this clip.",
          dialogue("the sister", L072, VOICE_C4, "she has not climbed a full flight of stairs in years.", "hopes, nervous. Rises on 'up'.", "soft and a little breathless, matching the face in this shot.", "she is scared to believe it, which leaks only through her eyes on the stairs."),
          dialogue("Her", L073, VOICE_N, "she knows; she did it herself.", "promises, simple. Stress on 'all'.", "warm and sure, matching the face in this shot.", "she is proud for her sister, which leaks only through the nod.")])

FILES = dict(S9.FILES)
FILES.update({"C3": "cast/C3-HUSBAND_v1.png", "OUT-C3-A2": "body/SC11/ingredients/OUT-C3-A2_v2.png", "OUT-N-A2": "body/SC09/ingredients/OUT-N-A2_v1.png", "L-LIVING": "plates/L-LIVING_v1.png",
              "C4": "cast/C4-SISTER_v1.png", "C5": "cast/C5-FRIEND1_v2.png", "C6": "cast/C6-FRIEND2_v1.png", "OUT-N-A3": "body/SC11/ingredients/OUT-N-A3_v1.png", "OUT-N-A4": "body/SC11/ingredients/OUT-N-A4_v1.png",
              "L-CAFE": "plates/L-CAFE_v1.png", "PROD-BOX": "../../products/stryde/stryde_refs/package_open.jpg", "P-HOUSE": "plates/P-HOUSE_v1.png", "L-STAIRS": "plates/L-STAIRS_v4.png"})
AUDIO = {"N-STOOD": "voice/N_line_stood.mp3", "C3-L058": "voice/C3_line_L058.mp3", "C5-L062": "voice/C5_line_L062.mp3", "C6-L064": "voice/C6_line_L064.mp3", "C4-REF": "voice/C4_voice_ref.mp3"}

if __name__ == "__main__":
    only = sys.argv[1:]
    for s in S9.SHOTS:
        if only and s["beat"] not in only:
            continue
        call = {"beat": s["beat"], "build": "stryde-half-my-age", "connector": "seedance", "model": "bytedance/seedance-2-5", "mode": 4, "kind": s["kind"], "prompt": s["prompt"],
                "take": s["take"], "covers": s["covers"], "start_pos": s["start_pos"], "end_pos": s["end_pos"],
                "duration": s["duration"], "resolution": "720p", "aspect_ratio": "9:16", "start_image": None,
                "ingredients_approved": True, "files": [FILES[f] for f in s["files"]], "audios": [AUDIO[a] for a in s["audios"]],
                "generate_audio": bool(s["line"]), "dialogue": s["line"] or None, "script_line": s["line"] or None, "pace": "unhurried",
                "subject_motion": s["subject_motion"], "prefer_multi_shots": "false", "generation": {"SC12-T1": 2, "SC13-T2": 4}.get(s["beat"], 1), "user_go": GO3 if s["beat"] == "SC13-T2" else GO, "fix_notes_all": NOTES_ALL.get(s["beat"], []), "fix_note": {"SC12-T1": "agent's check of v1 (not put up, L16): the two friends' jackets were swapped and Her came in a coat → the clothes named per person, never swapped, no coat on Her", "SC13-T2": "agent's check of v3 (kept off, L16): Her and her sister swapped places again and the sister touched the newel post → what is behind each woman named in her shot (the sister: the street and sky; Her: the hall and stairs), the newel post added to the hands-off line; the user (board Fix): she should not hold the hand rail → hands free, nobody touches the banister (FP23)"}.get(s["beat"], FIX),
                "risks": s["risks"], "vo": s.get("vo"), "scene": s["scene"], "title": s["title"],
                "taste": ["HT02", "HT17", "HT18", "HT22", "HT23", "HT26", "FP01", "FP02", "FP03", "FP05", "FP09", "FP11", "FP16", "FP18", "FP19", "FP22"]}
        (H / f"{s['beat']}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{s['beat']}.prompt.txt").write_text(s["prompt"])
        print(s["beat"], s["duration"], "s", len(s["prompt"]), "chars")
