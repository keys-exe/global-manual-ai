"""Scene 2 (Rock bottom) — SEEDANCE 2.5 clips on Kie AI, ingredients only, no frames (user 2026-10-01: "i want new ones in scene 2,
lets not use wan, lets do seedance" — the Wan 3.0 Prime pilots SH01/SH03 are retired to Old). Earlier note: Wan 3.0 Prime, INGREDIENTS ONLY, no frames
(user 2026-10-01: "use wan 3.0 prime the ingredients and not frames"; "we will not use frames so we will redo the scene 2").
Each clip: ≤ 4 image ingredients (Image1…: cast sheets, plates, the confirmed info/prop cards) + the speaker's voice master
as Audio1 on spoken shots; silent otherwise (VO laid in the edit). The framing of each shot follows the act map and the
three key frames the user confirmed before the frame route was retired (SH01 from the hall up to the landing at night in her
sheet outfit with black shoes; SH03 close from the landing, backwards; SH07 a close profile on the bed edge).
House Taste: HT02 (the struggle for real), HT04 (from the very top), HT09/HT17 (the plates), HT18 (plain), HT22 (the house's
geography fixed), HT23 (one scene, one continuous moment — THE SCENE SO FAR per segment)."""
import json
import sys
from pathlib import Path

H = Path(__file__).parent
B = H.parents[1]
import importlib.util  # noqa: E402
_spec = importlib.util.spec_from_file_location("hka_calls", B / "hooks" / "HKA" / "build_calls.py")
_hka = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_hka)
sys.modules["hka_calls"] = _hka
from hka_calls import (SERIES, LOOK, INHERIT, F2, PHYS, AUD, SILENT, NEG_EQUIP, NEG_MORPH, NEG_FILM,  # noqa: E402
                       NEG_SCENECUT, NEG_DRAMA, NEG_SOUND, NEG_STAIRS, VOICE_N, HER_ID,
                       manifest, SHEET, VOICE, PLACE, state, negs)

# V7.83.2 (LESSONS L13): the audio line no longer names a boom microphone — the model drew it into SH05 v3
AUD = AUD.replace("Audio is clean production sound from a boom microphone just out of frame above the speaker: close, clear and even,",
                  "Audio is clean, close production dialogue sound: clear and even,").replace(
          "The microphone and all sound equipment stay completely outside the picture: nothing hangs into the top of the frame. ", "")
assert "boom" not in AUD
HUS_ID = "a solid, slightly stooped man of seventy-four with short thinning grey hair"
VOICE_C3 = ("An English man of seventy-four from the north of England, a gruff, soft, low voice with a slight roughness, few words, plain northern vowels. "
            "He says kind things a little too quickly and lets them drop.")
HER_B1 = "a green crew-neck jumper, a charcoal skirt and black low-heeled shoes — exactly her clothes on her sheet"
HER_B2 = "a pale-blue quilted dressing gown tied at the waist over a grey nightdress, and grey slippers — exactly the outfit card"
HUS_OUT = "a brown V-neck wool cardigan over a blue-and-white checked shirt, grey flannel trousers and brown leather slippers — exactly his clothes on his sheet"
CARD_B2 = ("is an info card: Her outfit this morning — the pale-blue quilted dressing gown, grey nightdress and grey slippers; follow it exactly, "
           "and its caption strip and any text on it never appear in the clip.")
CARD_BAGS = ("is a prop card: the two plain brown paper shopping bags of this scene — copy them exactly, the same size and fill in every frame; "
             "its caption strip and grey backdrop never appear in the clip.")
HALL = PLACE("her hall seen from the front door — the straight staircase up the left-hand wall, the banister on its open right side, the telephone table, the doorways on the right")
STAIRS = PLACE("the same staircase seen from the landing at the top, looking down the flight to the green front door — the banister down the left, the photographs on the right-hand wall")
BEDROOM = PLACE("her bedroom upstairs — the bed with the pale green candlewick bedspread, the dark-wood chest of drawers under the window with its net curtains")
HOUSE = ("THE HOUSE, fixed for the whole scene: her 1930s semi. From the front door the hall runs straight ahead; one straight staircase of thirteen oatmeal-carpeted steps with brass stair rods "
         "rises along the LEFT-hand wall, small framed photographs climbing that wall; the open RIGHT side of the flight has a dark-varnished banister with square spindles and a dark newel post "
         "at the bottom and at the top; at the foot a small dark-wood telephone table with a cream telephone, a brass barometer above it; the doorways open off the right of the hall; "
         "at the top a small landing. Nothing in the house moves except the people.")
NIGHT = ("THE SCENE SO FAR, one continuous moment: evening; the hall's glass pendant and the landing lamp are lit, warm 2800K, the front-door glass is dark. Her stands on the landing at the very top "
         "of the stairs, her right hand on the top newel post; she has not come down and does not. Her husband is in the hall at the foot of the stairs. Two plain brown paper shopping bags full of "
         "groceries stand on the hall carpet at the foot of the bottom step, exactly the bags on the prop card.")
MORNING = ("THE SCENE SO FAR, the next morning, one continuous moment: cold grey daylight, about 6500K, from the frosted landing window and the front-door glass; the lamps are off. Her, in the "
           "dressing gown of the outfit card, is coming down the stairs BACKWARDS: she faces UP the flight, looking up toward the landing, both hands holding the banister rail, and lowers herself "
           "one step down at a time behind her, both feet together on each step before the next. The hall is empty. The shopping bags are gone from the hall.")
MORNING_SLOW = (  # SH03 v5: the user's Fix — slower, looking down at the step behind
    "THE SCENE SO FAR, the next morning, one continuous moment: cold grey daylight, about 6500K, from the frosted landing window and the front-door glass; the lamps are off. Her, in the "
           "dressing gown of the outfit card, is coming down the stairs BACKWARDS: she faces UP the flight, both hands holding the banister rail, looking down over her shoulder to see where she steps, and lowers herself "
           "very slowly one step down at a time behind her, both feet together on each step before the next. The hall is empty. The shopping bags are gone from the hall.")
KITCHEN_SC = ("THE SCENE SO FAR, the same morning, one continuous moment, DOWNSTAIRS IN THE KITCHEN: cold grey daylight, about 6500K, from the window over the sink and the small left window; "
              "the lamps are off. Her husband has been waiting in the kitchen for her with a plain white mug of tea he made for her. Her, in the dressing gown of the outfit card, has just got "
              "down the stairs and comes into the kitchen from the hall doorway. Nobody mentions the stairs.")
KITCHEN = PLACE("her kitchen at the back of the house — the scrubbed pine table and four ladder-back chairs by the small left window, the sage-green wall cupboards and cream worktops on the right, the white sink under the back window with the spider plant, the cream fridge")
AFTERNOON = ("THE SCENE SO FAR, the same day, afternoon: flat grey overcast light through the net curtains, about 6500K; the bedside lamp is off. Her, still in the dressing gown of the outfit card, "
             "has gone back upstairs and sits alone on her bed.")
STATIC = "no sliding, no gliding, no drifting across the floor, no feet skating, no camera push, no zoom"

L017 = "Just leave it by the stairs, love. I’ll get it later."
L018 = "I’ll bring it up."
L020 = "Sleep alright?"
L021 = "Fine, love."
GO_SC02B = ("Six weeks ago, I was going down my stairs backwards. One step at a time. it should her looking up then stepping backwards one at a time same steps both feet, both hand on the banister / "
            "HUSBAND: Sleep alright? HER: Fine, love. they should be at the 2nd floor not at the bottom cause the next line is VO: If I'm being honest, some days I wasn't going down them at all. I'd just stay upstairs. (user 2026-10-01)")
GO_KITCHEN = "lets do this at the kitchen where he is wating for the main character (user 2026-10-01)"
GO = "i want new ones in scene 2, lets not use wan, lets do seedance (user 2026-10-01) / we will not use frames / confirme and remove the previouse scene 2"


def dialogue(who, line, voice, moment, playing, now, under):
    return (f"DIALOGUE ({who}, verbatim): \"{line}\" {voice} IN THIS MOMENT: {moment} PLAYING: {playing} VOICE NOW: {now} "
            f"UNDER THE LINE: {under} Played small and true, for a camera close enough to see a thought. Never theatrical, never pushed, never performed to the lens.")


SHOTS = []
SHOTS.append(dict(beat="SC02-SH01", kind="dialogue", duration=7, line=L017, subject_motion="still", files=["N", "P-HOUSE"], audios=["N"], pilot=False, gen=3,
    fix="User (chat): \"i want new ones in scene 2, lets not use wan, lets do seedance\" → Seedance 2.5 ingredients; and the framing that keeps her at the top: a long lens on ONLY the top four steps and the landing, the flight below the frame, so a walk down would leave the shot. Wan v2 Fix (board): \"she should be at the top and not going down the stairs\" → fault in the action: 'stands still' left 7 s with nothing to do, so the model walked her down → she is planted on the landing for the whole clip with three small written movements (mouth, a weight shift, the hand tightening), leaving-the-landing negatives",
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", HER_B1)), ("@image2", HALL), ("@audio1", VOICE("Her"))]),
        SERIES, LOOK, INHERIT, HOUSE, NIGHT,
        "THE SHOT: a long-lens shot from low in the hall at the foot of the stairs, looking up: the frame holds ONLY the top four steps, the top newel post and the small landing — the rest of the flight "
        f"is below the bottom edge of the frame, so the stairs cannot be walked inside the shot. On the landing, framed from the knees up, stands Her, {HER_ID}, in {HER_B1}.",
        "She stays exactly where she is, on the landing at the very top, for the WHOLE clip: both feet planted on the landing, she never takes a step and never sets a foot on the stairs. "
        "Her right hand holds the top newel post, her left hand loose at her side; she looks down the stairs toward the hall and calls down: \"" + L017 + "\" "
        "The only movements are her mouth, a small shift of her weight from one foot to the other, and her right hand tightening on the post on 'later'.",
        F2, PHYS,
        "While the line is spoken, Her keeps doing one thing with their hands: her right hand resting on the top newel post, at one steady hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("HER", "tired, bob and fringe in place, in her own clothes, on the landing at the very top of the stairs", "nothing"),
        "FOCUS: her face is in sharp focus; the top steps in the near foreground fall a little soft. The blur is optical: soft and round, never smeared.",
        dialogue("Her", L017, VOICE_N, "she cannot face the stairs tonight and covers it with a light voice. Speaking down the stairs to her husband in the hall.",
                 "covers her fear. Opens light and easy; turns on 'later', where her eyes leave the stairs; exits looking away. Stress on 'later'.",
                 "light and a little tired, raised to carry down the stairs, matching the face in this shot.",
                 "she knows she will not come down, which leaks only through her hand tightening on the post."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, NEG_STAIRS, STATIC, "no walking down the stairs, no stepping onto the stairs, no coming down, no leaving the landing, no walking toward the camera", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the house drifts from the plate", "prevented_by": "the hall plate as Image2, THE HOUSE block with left/right (HT22)"},
           {"risk": "she steps down", "prevented_by": "only the top steps and the landing in frame; planted feet; leaving-the-landing negatives"},
                      {"risk": "voice drifts from the master", "prevented_by": "her voice master as Audio1"}]))

SHOTS.append(dict(beat="SC02-SH02", kind="dialogue", duration=4, line=L018, subject_motion="in_place", files=["C3", "L-STAIRS", "PROP-BAGS"], audios=["C3"],
    prompt=" ".join([
        manifest([("@image1", SHEET("the husband", HUS_OUT)), ("@image2", STAIRS), ("@image3", CARD_BAGS), ("@audio1", VOICE("the husband"))]),
        SERIES, LOOK, INHERIT, HOUSE, NIGHT,
        "THE SHOT: a medium shot from high on the landing looking down the flight, exactly as the place reference shows it, a longer lens holding the foot of the stairs and the hall below: "
        f"the husband, {HUS_ID}, in {HUS_OUT}, stands at the foot of the stairs beside the telephone table, the two bags on the carpet in front of him.",
        "He bends and snatches up both bags by their handles, one in each hand, a little too fast, straightens, and says without looking up the stairs: \"" + L018 + "\" His feet stay at the foot of the stairs; he does not climb.",
        F2, PHYS,
        "While the line is spoken, the husband keeps doing one thing with their hands: both hands holding the bag handles at his sides, at one steady hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("THE HUSBAND", "worried and hiding it, in his own clothes, at the foot of the stairs", "the bags are in his hands"),
        "FOCUS: the nearest eye of the husband is in sharp focus; the stairs between him and the camera fall a little soft. The blur is optical: soft and round, never smeared.",
        dialogue("the husband", L018, VOICE_C3, "he will not let her see that it frightens him. Speaking to his wife at the top of the stairs without looking at her.",
                 "takes the weight off her. Opens brisk; turns on 'up', where the bags come off the floor; exits already turning away. Stress on 'bring'.",
                 "quick and gruff, a little too quick, matching the face in this shot.",
                 "he is scared for her, which leaks only through how fast the bags come up."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, "no climbing the stairs, no looking up at the camera, no third bag", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the bags change", "prevented_by": "the prop card"}, {"risk": "he climbs", "prevented_by": "feet stay at the foot, negative"},
           {"risk": "voice drifts", "prevented_by": "his voice master as Audio1"}]))

SHOTS.append(dict(beat="SC02-SH03", kind="broll", duration=6, line="", vo="L019", subject_motion="travels", files=["N", "L-STAIRS", "OUT-N-B2"], audios=[], pilot=False, gen=5, go=GO_SC02B,
    fix="User Fix (board, v4): \"she should not be going down so fast and she should be looking down to know where she is stepping backwards\" → half the pace: ONE step in the whole clip, the foot feeling for it; before and during the step she looks down over her shoulder at the step behind her. Earlier — User (chat): \"Six weeks ago, I was going down my stairs backwards. One step at a time. it should her looking up then stepping backwards one at a time same steps both feet, both hand on the banister\" → back to the script line (LESSONS L11): she faces UP the flight looking up, and steps DOWN backwards, both feet together on each step, both hands on the banister; the camera on the landing looking down at her so her face and the direction both read (she moves away from the camera, down). Seedance v3 had her facing forwards on an earlier note that contradicted the line",
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", HER_B2)), ("@image2", STAIRS), ("@image3", CARD_B2)]),
        SERIES, LOOK, INHERIT, HOUSE, MORNING_SLOW,
        "THE SHOT: a medium shot from the landing at the top of the stairs, looking down the flight, exactly as the place reference shows it: "
        f"Her, {HER_ID}, in {HER_B2}, stands three steps below the landing FACING UP THE STAIRS toward the camera, her head turned and lowered, looking down over her shoulder at the step behind her; the rest of the flight and the hall fall away below and behind her.",
        "She goes DOWN the stairs BACKWARDS, away from the camera, very slowly, ONE step in the whole clip: both hands grip the banister rail beside her; she turns her head and looks down over her shoulder at the step behind her, "
        "slowly reaches one foot down behind her, feels for the edge of the step with her toe, finds it and puts her weight on it, still looking down at it; then brings the other foot down beside it, both feet together on the same step, "
        "and stops, breathing out, her eyes still down on her feet. It takes the whole clip; she never hurries and never takes a second step; she never turns round.",
        F2, PHYS,
        state("HER", "tired, bob and fringe in place, in the dressing gown, three steps below the landing, facing up the stairs, both hands on the banister", "she is one step lower, still facing up the stairs, looking down at her feet"),
        "FOCUS: her face and hands are in sharp focus; the hall far below her falls soft. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, NEG_STAIRS, "no turning round, no facing down the stairs, no walking forwards, no climbing up toward the camera, no second step, no hurrying, no looking up at the camera, no letting go of the banister with either hand, no talking, no mouth moving", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "she turns and walks down facing forwards", "prevented_by": "facing up the stairs toward the camera written at start and end state; turning negatives"},
           {"risk": "she climbs toward the camera instead of descending", "prevented_by": "'away from the camera, down', the foot reaching behind her, climbing negative"},
           {"risk": "she goes down too fast", "prevented_by": "one step in the whole clip, the foot feeling for the edge, no second step, negative"},
           {"risk": "the gown changes", "prevented_by": "the outfit card as Image3"}]))

SHOTS.append(dict(beat="SC02-SH04", kind="broll", duration=4, line="", vo="L019", subject_motion="in_place", files=["N", "P-HOUSE", "OUT-N-B2"], audios=[], gen=2, go=GO_SC02B,
    fix="User (chat): \"it should her looking up then stepping backwards one at a time same steps both feet, both hand on the banister\" → the profile now shows her facing UP the flight and lowering backwards onto the step behind her, both feet together, both hands on the rail (v1 had her facing down the flight)",
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", HER_B2)), ("@image2", HALL), ("@image3", CARD_B2)]),
        SERIES, LOOK, INHERIT, HOUSE, MORNING,
        "THE SHOT: a medium close-up in profile at her eye level, seen from the hall side through the square spindles of the banister, a long lens, shallow focus on her eye: "
        f"Her, {HER_ID}, in {HER_B2}, mid-flight, FACING UP THE STAIRS toward the top of the frame's slope, her face lifted toward the landing; the bottom of the flight lies behind her back.",
        "Both hands grip the banister rail in front of her; she reaches her foot down behind her onto the next step down, lowers her weight onto it, brings the other foot down beside it so both feet stand together on the same step, and breathes out slowly through her mouth, eyes still up. One step only.",
        F2, PHYS,
        state("HER", "tired, in the dressing gown, mid-flight, facing up the stairs, both hands on the banister", "she is one step lower, still facing up"),
        "FOCUS: the nearest eye of Her is in sharp focus; the spindles in front and the stair wall with its photographs behind fall to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, NEG_STAIRS, "no turning round, no facing down the stairs, no stepping up, no talking, no mouth moving, no letting go of the banister with either hand", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "she faces down the flight", "prevented_by": "facing up the stairs, the bottom of the flight behind her back, turning negatives"},
           {"risk": "she steps up instead of down", "prevented_by": "the foot reaching down behind her, stepping-up negative"},
           {"risk": "she lets go of the banister", "prevented_by": "both hands on the rail, negative"}, {"risk": "the gown changes", "prevented_by": "outfit card"}]))

SHOTS.append(dict(beat="SC02-SH05", kind="dialogue", duration=4, line=L020, subject_motion="still", files=["C3", "L-KITCHEN"], audios=["C3"], gen=4, go=GO_KITCHEN + " / remove the mic at the top (board Fix) / fix those (chat go)",
    fix="User Fix (board, v3): \"remove the mic at the top\" → fault in the frame: the model hung a furry boom microphone over his head (a dialogue shot, nothing written for the top of frame); the plate is clean. Now the top of the frame is written — only the plain white ceiling and the cream enamel pendant on its flex — with the boom and windshield named in the negatives. Earlier — User (chat): \"lets do this at the kitchen where he is wating for the main character\" → the tea moment moved from the landing to the kitchen: he has been waiting there with her tea and she comes in from the hall after the backwards descent (SH03/SH04). Third generation of this shot at the user's call",
    prompt=" ".join([
        manifest([("@image1", SHEET("the husband", HUS_OUT)), ("@image2", KITCHEN), ("@audio1", VOICE("the husband"))]),
        SERIES, LOOK, INHERIT, KITCHEN_SC,
        f"THE SHOT: a medium close-up at his eye level, three-quarter on, from the kitchen doorway where she has just come in: the husband, {HUS_ID}, in {HUS_OUT}, stands by the scrubbed pine table, "
        "the sage-green cupboards and the window over the sink soft behind him, exactly the kitchen of the place reference. "
        "The top of the frame holds only the plain white ceiling and the cream enamel pendant lamp on its flex, exactly as in the place reference; nothing else hangs or reaches into the top of the frame.",
        "He has been waiting for her; he holds a plain white mug of tea out toward her at chest height in his right hand, his left hand resting on the back of a ladder-back chair; he glances at her, then a little away, not quite looking at her, and says: \"" + L020 + "\" His feet stay where they are.",
        F2, PHYS,
        "While the line is spoken, the husband keeps doing one thing with their hands: his right hand holding the mug out still at chest height, at one steady hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("THE HUSBAND", "worried and hiding it, in his own clothes, in the kitchen by the table with her tea", "nothing"),
        "FOCUS: the nearest eye of the husband is in sharp focus; the kitchen behind him falls to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
        dialogue("the husband", L020, VOICE_C3, "he has waited in the kitchen while she came down backwards and will not mention it. Speaking to his wife as she comes in.",
                 "makes it ordinary. Opens light; turns on 'alright', where his eyes slide away; exits holding the mug out a little. Stress on 'alright'.",
                 "gruff and soft, an ordinary morning voice, matching the face in this shot.",
                 "he heard every step and it frightens him, which leaks only through his eyes not staying on her."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, "no boom microphone above his head, no furry windshield, no fluffy grey object hanging at the top of the frame, nothing hanging from the ceiling except the pendant lamp, no logo or writing on the mug, no stairs, no hall, no walking, no sitting down", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "a boom mic hangs into the top of the frame", "prevented_by": "the top of frame written (ceiling and pendant only), boom and windshield negatives"}, {"risk": "the room drifts from the kitchen plate", "prevented_by": "the kitchen plate as Image2, named anchors (table, cupboards, sink window) (HT17)"},
           {"risk": "he stares straight at her", "prevented_by": "the glance and away written (the act map's 'not quite looking')"},
           {"risk": "voice drifts", "prevented_by": "his voice master as Audio1"},
           {"risk": "a logo on the mug", "prevented_by": "a plain white mug, negative (HT18)"}]))

SHOTS.append(dict(beat="SC02-SH06", kind="dialogue", duration=4, line=L021, subject_motion="still", files=["N", "C3", "L-KITCHEN", "OUT-N-B2"], audios=["N"], gen=3, go=GO_KITCHEN,
    fix="User (chat): \"lets do this at the kitchen where he is wating for the main character\" → she takes the tea in the kitchen, just inside the doorway from the hall, over his shoulder. Third generation of this shot at the user's call",
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", HER_B2)), ("@image2", SHEET("the husband", HUS_OUT)), ("@image3", KITCHEN), ("@image4", CARD_B2), ("@audio1", VOICE("Her"))]),
        SERIES, LOOK, INHERIT, KITCHEN_SC,
        "THE SHOT: a close-up over the husband's shoulder at her eye level, in the kitchen: the soft back of his grey head and his brown cardigan shoulder fill the near left edge, out of focus; "
        f"beyond him, sharp, Her, {HER_ID}, in {HER_B2}, stands just inside the kitchen, the end of the scrubbed pine table and the sage-green cupboards soft beside her.",
        "She takes the plain white mug from his hand with both hands, looks at him, and gives a small tight smile that does not reach her eyes, and says: \"" + L021 + "\"",
        F2, PHYS,
        "While the line is spoken, Her keeps doing one thing with their hands: both hands around the mug at chest height, at one steady hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("HER", "tired, in the dressing gown, just come into the kitchen", "the mug is in her hands"),
        state("THE HUSBAND", "in the near foreground in the kitchen, his back to the camera, out of focus", "the mug has left his hand"),
        "FOCUS: the nearest eye of Her is in sharp focus; his shoulder in the foreground and the kitchen behind her fall to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
        dialogue("Her", L021, VOICE_N, "she has just got down the stairs backwards and will not let him say anything about it. Speaking to her husband, close, in the kitchen.",
                 "closes the subject. Opens on the smile; turns on 'love', where her eyes drop to the mug; exits looking down. Stress on 'Fine'.",
                 "quiet and a little bright, too quick to be true, matching the face in this shot.",
                 "it is not fine, which leaks only through the smile stopping short of her eyes."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, "no logo or writing on the mug, no spilling, no crying, no stairs, no front door", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "they are in the hall or on the stairs", "prevented_by": "the kitchen plate, KITCHEN scene block, stairs/front-door negatives"},
           {"risk": "the wrong person in the foreground", "prevented_by": "his sheet as Image2, named as the soft foreground"},
           {"risk": "the smile overplayed", "prevented_by": "'small tight', NEG-DRAMA"}, {"risk": "voice drifts", "prevented_by": "her voice master"}]))

SHOTS.append(dict(beat="SC02-SH07", kind="broll", duration=6, line="", vo="L022", subject_motion="still", files=["N", "L-BEDROOM", "OUT-N-B2"], audios=[],
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", HER_B2)), ("@image2", BEDROOM), ("@image3", CARD_B2)]),
        SERIES, LOOK, INHERIT, AFTERNOON,
        f"THE SHOT: a close profile at her eye level, a long lens, very shallow focus on her eye: Her, {HER_ID}, in {HER_B2}, sits on the near edge of her bed, her face filling the left half of the frame, the window and its net curtains soft in the right half.",
        "She sits still, both hands in her lap, one thumb moving slowly over the back of the other hand; her eyes are on the grey garden through the window, wet but no tears. She blinks once. Nothing else moves.",
        F2, PHYS,
        state("HER", "tired and still, in the dressing gown, alone on the bed edge", "nothing"),
        "FOCUS: the nearest eye of Her is in sharp focus; the window and the room behind fall to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, "no tears falling, no talking, no mouth moving, no standing up", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "overplayed sadness", "prevented_by": "wet eyes, no tears, NEG-DRAMA"}, {"risk": "the gown changes", "prevented_by": "outfit card"},
           {"risk": "she stands up or leaves", "prevented_by": "sits still, nothing else moves, negative"}]))

FILES = {"N": "cast/N-HER_v1.png", "C3": "cast/C3-HUSBAND_v1.png", "P-HOUSE": "plates/P-HOUSE_v1.png", "L-STAIRS": "plates/L-STAIRS_v4.png",
         "L-BEDROOM": "plates/L-BEDROOM_v1.png", "L-KITCHEN": "plates/L-KITCHEN_v1.png", "OUT-N-B2": "body/SC02/ingredients/OUT-N-B2_v1.png", "PROP-BAGS": "body/SC02/ingredients/PROP-BAGS_v1.png"}
AUDIO = {"N": "voice/N_voice_master.mp3", "C3": "voice/C3_voice_master.mp3"}

if __name__ == "__main__":
    for s in SHOTS:
        call = {"beat": s["beat"], "connector": "seedance", "model": "bytedance/seedance-2-5", "mode": 4, "kind": s["kind"], "prompt": s["prompt"],
                "duration": s["duration"], "resolution": "720p", "aspect_ratio": "9:16", "start_image": None,
                "ingredients_approved": True, "files": [FILES[f] for f in s["files"]], "audios": [AUDIO[a] for a in s["audios"]],
                "generate_audio": bool(s["line"]), "dialogue": s["line"] or None, "script_line": s["line"] or None, "pace": "unhurried",
                "subject_motion": s["subject_motion"], "prefer_multi_shots": "false", "generation": s.get("gen", 1), "fix_note": s.get("fix"), "user_go": s.get("go", GO),
                "risks": s["risks"], "vo": s.get("vo"), "pilot": s.get("pilot", False), "scene": 2,
                "taste": ["HT02", "HT04", "HT09", "HT17", "HT18", "HT22", "HT23"]}
        (H / f"{s['beat']}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{s['beat']}.prompt.txt").write_text(s["prompt"])
        print(s["beat"], s["duration"], "s", len(s["prompt"]), "chars", "PILOT" if s.get("pilot") else "")
