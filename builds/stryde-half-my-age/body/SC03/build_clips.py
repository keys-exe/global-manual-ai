"""Scene 3 (Tried everything + the Sunday plant) — SEEDANCE 2.5 clips on Kie AI, ingredients only, no frames (the body lock, §18A;
user 2026-10-01 "CONFIRMED PROCEED" after the five SC03 ingredient cards were confirmed).
Story days: B3 montage (landing evening, physio, kitchen morning) → B3d evening in the bedroom. Her outfit OUT-N-B3 throughout
(the brace worn over it); the husband's OUT-C3-B3 (green crew-neck jumper — the user's Fix: not the Scene 2 outfit).
VO L023/L024/L029 are laid in the edit; the sister's line L027 is her confirmed voice master (it speaks the line verbatim),
laid in the edit through a phone EQ under SH09 — only Her's answer L028 is generated in that clip.
House Taste: HT02 (the struggle for real), HT17 (the plates), HT18 (plain — no brands), HT22 (the house's geography fixed),
HT23 (one continuous moment per segment). V7.83.2: the audio line never names a microphone (LESSONS L13)."""
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
from hka_calls import (SERIES, LOOK, INHERIT, F2, F1, PHYS, AUD, SILENT, NEG_EQUIP, NEG_MORPH, NEG_FILM,  # noqa: E402
                       NEG_SCENECUT, NEG_DRAMA, NEG_SOUND, VOICE_N, HER_ID,
                       manifest, SHEET, VOICE, PLACE, state, negs)

AUD = AUD.replace("Audio is clean production sound from a boom microphone just out of frame above the speaker: close, clear and even,",
                  "Audio is clean, close production dialogue sound: clear and even,").replace(
      "The microphone and all sound equipment stay completely outside the picture: nothing hangs into the top of the frame. ", "")
assert "boom" not in AUD and "microphone stay" not in AUD

HUS_ID = "a solid, slightly stooped man of seventy-four with short thinning grey hair"
VOICE_C3 = ("An English man of seventy-four from the north of England, a gruff, soft, low voice with a slight roughness, few words, plain northern vowels. "
            "He says kind things a little too quickly and lets them drop.")
HER_B3 = "a buttoned slate-grey wool cardigan over a cream blouse with a small round collar, a navy knee-length skirt, flesh-tone tights and black low-heeled shoes — exactly the outfit card"
HUS_B3 = "a bottle-green crew-neck lambswool jumper over a pale-blue oxford shirt, charcoal corduroy trousers and dark-brown lace-up shoes — exactly his outfit card"
CARD_N = ("is an info card: Her outfit on this day — the slate-grey cardigan, cream blouse, navy knee-length skirt and black low-heeled shoes; follow it exactly, "
          "and its caption strip and any text on it never appear in the clip.")
CARD_C3 = ("is an info card: the husband's outfit on this day — the bottle-green crew-neck jumper, pale-blue shirt, charcoal cords and brown lace-ups; follow it exactly, "
           "and its caption strip and any text on it never appear in the clip.")
CARD_BRACE = ("is a prop card: the bulky black hinged knee brace — black neoprene, hook-and-loop straps, a silver hinge bar down each side; copy it exactly, "
              "with no brand or writing; its caption strip and grey backdrop never appear in the clip.")
CARD_DRAWER = ("is a prop card: her chest's bottom drawer crammed with braces, sleeves and supports — the drawer exactly the chest's own size; "
               "copy its contents, and its caption strip never appears in the clip.")
STAIRS = PLACE("the staircase seen from the landing at the top — the landing carpet, the banister down the left, the photographs on the right-hand wall")
BEDROOM = PLACE("her bedroom upstairs — the bed with the pale green candlewick bedspread, the dark-wood chest of drawers under the window with its net curtains, the door to the landing")
KITCHEN = PLACE("her kitchen at the back of the house — the scrubbed pine table and ladder-back chairs by the small left window, the sage-green cupboards, the sink under the back window")
PHYSIO = PLACE("a small physiotherapy room — the padded blue treatment couch with its paper sheet along the left wall, white vertical blinds on the back window, a trolley with a box of blue gloves")

LANDING_EVE = ("THE SCENE SO FAR, one evening, one continuous moment: the landing lamp is lit, warm 2800K, the landing window dark blue with dusk. Her, in the outfit of the card, "
               "stands on the landing at the top of the stairs. Over her right knee, on top of her tights, she wears the hinged knee brace of the prop card. Nobody else is there.")
CLINIC = ("THE SCENE SO FAR, a weekday morning at the clinic, one continuous moment: cool daylight about 5600K slices through the half-closed white blinds; the room is quiet. "
          "Her, in the outfit of the card, has come for her physiotherapy. Only the clinician's hands and forearms are ever seen: blue nitrile gloves, navy tunic sleeves; never a face.")
KITCHEN_AM = ("THE SCENE SO FAR, a cold grey morning in her kitchen, one continuous moment: flat grey daylight about 6500K from the window over the sink and the small left window — "
              "cool and overcast, no sunshine, no warm light on the table; the lamps are off. Her, in the outfit of the card, sits at the pine table with a plain white mug of tea.")
BEDROOM_EVE = ("THE SCENE SO FAR, the same evening in her bedroom, one continuous moment: the bedside lamp is lit, warm 2800K, the window dark blue with dusk behind the net curtains. "
               "Her, in the outfit of the card, has taken the hinged brace off; the chest of drawers stands under the window, its bottom drawer crammed, exactly as the drawer card shows it. "
               "Her husband, in the outfit of his card, has come to the open bedroom door from the landing.")
DOORWAY_GEO = ("THE ROOM FROM THE WINDOW SIDE, the same in both shots of this exchange: the camera stands in the corner between the window and the foot of the bed, looking back across the room "
              "toward the bedroom door. The chest of drawers is beside the camera under the window; the open bedroom door is in the far wall on the RIGHT half of the frame, the tall dark wardrobe "
              "beside it on the right; the bed with the pale green candlewick bedspread runs along the LEFT of the frame. She stands at the chest of drawers in the near frame, side-on to the camera, "
              "facing the chest, with her back to the door. He stands IN the open doorway on the threshold, never inside the room, and looks straight across the room AT HER the whole time.")
STATIC = "no sliding, no gliding, no drifting across the floor, no feet skating, no camera push, no zoom"
F6 = ("Camera pulling back on a dolly, already moving on the first frame: a slow, steady pull away from the subject covering about 60 centimetres across the whole clip, "
      "perfectly level, with no bounce and no sway, revealing more of the room around them as it goes. The subject stays in place and never walks while the camera moves. Still pulling back on the final frame.")

PHONE = "a slim modern smartphone with a pale champagne-gold back and rounded corners (one phone, the same in every shot of this call),"
PHONE_SHORT = "the slim champagne-gold smartphone"
L025 = "That drawer won’t shut soon."
L026 = "It shuts."
L028 = "Course, love. Easier."
GO = "CONFIRMED PROCEED (user 2026-10-01) — Scene 3 on Seedance 2.5, ingredients only"


def dialogue(who, line, voice, moment, playing, now, under):
    return (f"DIALOGUE ({who}, verbatim): \"{line}\" {voice} IN THIS MOMENT: {moment} PLAYING: {playing} VOICE NOW: {now} "
            f"UNDER THE LINE: {under} Played small and true, for a camera close enough to see a thought. Never theatrical, never pushed, never performed to the lens.")


NOFACE = "no face in frame"
SHOTS = []
SHOTS.append(dict(beat="SC03-SH01", kind="broll", duration=4, line="", vo="L023", subject_motion="in_place", files=["N", "L-STAIRS", "OUT-N-B3", "INFO-BRACE"], audios=[],
    title="Scene 3 · The brace slides down her leg",
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", HER_B3)), ("@image2", STAIRS), ("@image3", CARD_N), ("@image4", CARD_BRACE)]),
        SERIES, LOOK, INHERIT, LANDING_EVE,
        "THE SHOT: an extreme close-up from low on the landing carpet, at knee height, on her right leg from just above the knee to the ankle: the navy skirt hem at the top of the frame, "
        "the hinged knee brace over her tights on the knee, her black shoe at the bottom of the frame; the landing carpet and the top of the banister soft behind.",
        "She stands still. The hinged brace slowly slips down her shin under its own weight, about ten centimetres over the clip, the straps sagging, the silver hinges sliding off the knee "
        "and the neoprene bunching at the top; her leg does not move.",
        F2, PHYS,
        state("HER", "tired, in the outfit of the card, standing on the landing, the brace on her right knee", "the brace has slid down onto her shin"),
        "FOCUS: the brace and her knee are in sharp focus; the landing behind falls soft. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, "no brand or writing on the brace, no hands, no walking, no brace on the other leg", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the brace changes design", "prevented_by": "the brace prop card as Image4, described"},
           {"risk": "the brace teleports instead of sliding", "prevented_by": "about ten centimetres over the clip, the straps sagging, end state written"},
           {"risk": "a brand or logo on the brace", "prevented_by": "plain card, negative (HT18)"}]))

SHOTS.append(dict(beat="SC03-SH02", kind="broll", duration=4, line="", vo="L023", subject_motion="still", files=["N", "L-STAIRS", "OUT-N-B3", "INFO-BRACE"], audios=[],
    title="Scene 3 · By evening, round her ankle",
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", HER_B3)), ("@image2", STAIRS), ("@image3", CARD_N), ("@image4", CARD_BRACE)]),
        SERIES, LOOK, INHERIT, LANDING_EVE.replace("Over her right knee, on top of her tights, she wears the hinged knee brace of the prop card.",
                                                   "The hinged knee brace of the prop card has slipped all the way down her right leg."),
        "THE SHOT: an extreme close-up in profile at floor level on the landing carpet: her right ankle and black shoe fill the lower half of the frame; the hinged brace of the prop card "
        "sits bunched and twisted round her ankle just above the shoe, one strap undone and trailing on the carpet; the lamp-lit landing soft behind.",
        "Nothing moves except her weight settling a little onto that foot and the loose strap end trembling slightly. It holds.",
        F2, PHYS,
        state("HER", "in the outfit of the card, standing on the landing, the brace bunched round her right ankle", "nothing"),
        "FOCUS: the bunched brace and her ankle are in sharp focus; the carpet behind falls soft. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, "no brand or writing on the brace, no hands, no walking, no slippers", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the brace back on the knee", "prevented_by": "the SCENE SO FAR changed: slipped all the way down, bunched round the ankle"},
           {"risk": "slippers instead of her shoes", "prevented_by": "outfit card, black shoe, slippers negative"},
           {"risk": "a brand on the brace", "prevented_by": "plain card, negative"}]))

SHOTS.append(dict(beat="SC03-SH03", kind="broll", duration=4, line="", vo="L023", subject_motion="in_place", files=["N", "INFO-PHYSIO", "OUT-N-B3"], audios=[],
    title="Scene 3 · Physiotherapy",
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", HER_B3)), ("@image2", PHYSIO), ("@image3", CARD_N)]),
        SERIES, LOOK, INHERIT, CLINIC,
        f"THE SHOT: a medium shot from high above the couch at three-quarter, looking down: Her, {HER_ID}, in {HER_B3}, lies on her back on the blue treatment couch, "
        "her head on the paper sheet, small on the couch; two gloved hands at the right of the frame hold her right leg — one under the heel, one under the knee.",
        "The hands slowly bend her right knee up toward her chest, a few centimetres at a time; she winces once, her jaw tightening, and looks at the ceiling. One slow bend.",
        F2, PHYS,
        state("HER", "tired, in the outfit of the card, lying on the couch", "her right knee is bent"),
        "FOCUS: her face and her right knee are in sharp focus; the blinds behind fall soft. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, "no clinician's face, no third hand, no text on the walls, no talking, no mouth moving", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "an extra hand or arm", "prevented_by": "two gloved hands placed (heel, knee), third-hand negative"},
           {"risk": "the clinician's face appears", "prevented_by": "hands and forearms only, negative"},
           {"risk": "the room drifts", "prevented_by": "the physio room card as Image2"}]))

SHOTS.append(dict(beat="SC03-SH04", kind="broll", duration=4, line="", vo="L023", subject_motion="in_place", files=["N", "L-KITCHEN", "OUT-N-B3"], audios=[],
    title="Scene 3 · Painkillers",
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", HER_B3)), ("@image2", KITCHEN), ("@image3", CARD_N)]),
        SERIES, LOOK, INHERIT, KITCHEN_AM,
        "THE SHOT: an extreme close-up from directly overhead on the scrubbed pine table: a plain white mug of tea at the top of the frame, a silver blister strip of white tablets "
        "in the middle, and her two hands — the cuffs of the slate-grey cardigan at the wrists.",
        "Her right thumb presses one white tablet through the foil into her left palm, then a second beside it; two tablets in her palm. Unhurried, a routine.",
        F2, PHYS,
        state("HER", "in the outfit of the card, at the kitchen table", "two tablets lie in her left palm"),
        "FOCUS: the blister strip and her fingers are in sharp focus; the mug and the table grain fall a little soft. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, NOFACE, "no brand, writing or label on the strip, the box or the mug, no sunshine on the table, no warm light, no third tablet", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "a brand on the pills", "prevented_by": "a plain silver strip, negative (HT18)"},
           {"risk": "warm sunny light (the kitchen plate is afternoon)", "prevented_by": "KITCHEN_AM: flat grey 6500K, no sunshine, warm-light negative"},
           {"risk": "fingers fuse on the foil", "prevented_by": "PHYS, one thumb pressing, count written"}]))

SHOTS.append(dict(beat="SC03-SH05", kind="broll", duration=4, line="", vo="L023", subject_motion="still", files=["N", "INFO-PHYSIO", "OUT-N-B3"], audios=[],
    title="Scene 3 · Cortisone injections",
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", HER_B3)), ("@image2", PHYSIO), ("@image3", CARD_N)]),
        SERIES, LOOK, INHERIT, CLINIC,
        "THE SHOT: an extreme close-up in profile at the height of her knee as she sits on the edge of the treatment couch, her navy skirt pulled just above her right knee, "
        "her tights rolled down to the shin: a gloved hand in the foreground swabs the outer side of her right knee with a small white swab in one slow stroke; "
        "behind it, soft and out of focus, the other gloved hand holds a small syringe, needle cap on.",
        "One slow swab, then the hand lifts away. Her knee stays still; her own hand, at the edge of the frame, grips the edge of the couch.",
        F2, PHYS,
        state("HER", "in the outfit of the card, sitting on the couch edge, knee bared", "the side of her knee has been swabbed"),
        "FOCUS: the swab and the skin of her knee are in sharp focus; the syringe behind is soft. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, NOFACE, "no needle going in, no blood, no writing on the syringe, no third hand", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the needle goes in on screen", "prevented_by": "swab only, needle cap on, negative"},
           {"risk": "an extra hand", "prevented_by": "two gloved hands and her one hand placed, negative"},
           {"risk": "writing on the syringe", "prevented_by": "negative (HT18)"}]))

SHOTS.append(dict(beat="SC03-SH06", kind="broll", duration=5, line="", vo="L023 L024", subject_motion="in_place", files=["N", "L-BEDROOM", "OUT-N-B3", "INFO-DRAWER", "INFO-BRACE"], audios=[],
    title="Scene 3 · Into the drawer",
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", HER_B3)), ("@image2", BEDROOM), ("@image3", CARD_N), ("@image4", CARD_DRAWER), ("@image5", CARD_BRACE)]),
        SERIES, LOOK, INHERIT, BEDROOM_EVE.replace(" Her husband, in the outfit of his card, has come to the open bedroom door from the landing.", ""),
        f"THE SHOT: a medium shot from high over her right shoulder, from behind, looking down: Her, {HER_ID}, in {HER_B3}, stands at the chest of drawers under the window; "
        "the bottom drawer is pulled half open, crammed with braces, sleeves and supports exactly as the drawer card shows it; she holds the hinged brace of the prop card in her right hand.",
        "She drops the brace onto the pile in the drawer, then pushes the drawer shut with the side of her right foot; it slides most of the way in and stops, still standing proud by a few centimetres, a strap caught at the edge.",
        F2, PHYS,
        state("HER", "tired, in the outfit of the card, at the chest of drawers, the brace in her hand", "the brace is in the drawer and the drawer is shut but still proud"),
        "FOCUS: the drawer and her hand are in sharp focus; the window and net curtains fall soft. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, "no drawer bigger than the chest, no drawer closing fully, no brand or writing on anything in the drawer, no talking", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the drawer grows (the user's Fix on the card)", "prevented_by": "the drawer card at the chest's own size, negative"},
           {"risk": "the drawer shuts cleanly (the line needs it proud)", "prevented_by": "stops a few centimetres proud, a strap caught, negative"},
           {"risk": "the brace changes", "prevented_by": "brace card as Image5"}]))

SHOTS.append(dict(beat="SC03-SH07", kind="dialogue", duration=4, line=L025, subject_motion="still", gen=2,
    fix="user (chat): \"THIS TWO SHOULD BE CONNECTED AND HUSBAND SHOULD BE LOOKING FROM THE DOORWAY INTO THE BEDROOM LOOKING TO HER\" — v1 framed him alone, from inside, looking at the drawer, in the Scene 2 cardigan → v2 is a two-shot: her in the near frame at the chest, him in the doorway looking at her (HT24), the same set-up as SH08",
    files=["C3", "N", "L-BEDROOM", "OUT-C3-B3", "OUT-N-B3", "INFO-DRAWER"], audios=["C3"],
    title="Scene 3 · \"That drawer won’t shut soon.\"",
    prompt=" ".join([
        manifest([("@image1", SHEET("the husband", HUS_B3)), ("@image2", SHEET("Her", HER_B3)), ("@image3", BEDROOM), ("@image4", CARD_C3), ("@image5", CARD_N), ("@image6", CARD_DRAWER),
                  ("@audio1", VOICE("the husband"))]),
        SERIES, LOOK, INHERIT, BEDROOM_EVE, DOORWAY_GEO,
        f"THE SHOT: a medium two-shot at standing eye level: in the near frame on the left, soft, Her, {HER_ID}, in {HER_B3}, in profile at the chest of drawers, looking down at its bottom drawer, "
        f"which stands proud by a few centimetres; across the room, sharp, in the open doorway on the right half of the frame, the husband, {HUS_ID}, in {HUS_B3}, "
        "his left hand resting on the door frame, the dim landing behind him; the bedside lamp's warm light on his face.",
        "He looks across the room at her, at her back and the drawer, and says softly: \"" + L025 + "\" A small breath out through the nose at the end, half a smile that doesn't stay. She does not turn.",
        F2, PHYS,
        "While the line is spoken, the husband keeps doing one thing with their hands: his left hand resting on the door frame, at one steady hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("THE HUSBAND", "soft worry, in the outfit of his card, on the bedroom threshold, looking at her", "nothing"),
        "FOCUS: the husband's nearest eye is in sharp focus; Her in the near frame falls soft. The blur is optical: soft and round, never smeared.",
        dialogue("the husband", L025, VOICE_C3, "he has watched her drop another brace in and tries to make it light. Speaking to his wife across the room, at the chest of drawers.",
                 "teases to cover the worry. Opens light; turns on 'soon', where the smile goes; exits looking at her. Stress on 'won’t'.",
                 "soft and gruff, a little quiet for the late evening, matching the face in this shot.",
                 "he is worried there is nothing left to try, which leaks only through the smile not staying."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, "no cardigan, no checked shirt, no stepping into the room, no looking away from her, no second door", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the two read as separate shots again (the user's Fix)", "prevented_by": "both in one frame, the DOORWAY_GEO set-up shared with SH08, his eyline on her written (HT24)"},
           {"risk": "the Scene 2 outfit returns (v1)", "prevented_by": "his B3 card as Image4, cardigan/checked-shirt negatives"},
           {"risk": "he walks into the room", "prevented_by": "on the threshold, hand on the frame, negative"}]))

SHOTS.append(dict(beat="SC03-SH08", kind="dialogue", duration=4, line=L026, subject_motion="still", gen=2,
    fix="user (chat): \"THIS TWO SHOULD BE CONNECTED AND HUSBAND SHOULD BE LOOKING FROM THE DOORWAY INTO THE BEDROOM LOOKING TO HER\" — v1 had her alone → v2 keeps SH07's set-up, closer on her, him still in the doorway behind her looking at her",
    files=["N", "C3", "L-BEDROOM", "OUT-N-B3", "OUT-C3-B3", "INFO-DRAWER"], audios=["N"],
    title="Scene 3 · \"It shuts.\"",
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", HER_B3)), ("@image2", SHEET("the husband", HUS_B3)), ("@image3", BEDROOM), ("@image4", CARD_N), ("@image5", CARD_C3), ("@image6", CARD_DRAWER),
                  ("@audio1", VOICE("Her"))]),
        SERIES, LOOK, INHERIT, BEDROOM_EVE, DOORWAY_GEO,
        f"THE SHOT: the same set-up as the shot before, closer: a close-up of Her, {HER_ID}, in {HER_B3}, in profile on the left of the frame at the chest of drawers, her eyes down on the drawer; "
        f"behind her, small and soft across the room in the open doorway on the right half of the frame, the husband in {HUS_B3}, his hand on the door frame, still looking at her.",
        "She does not turn round. Her eyes stay down on the drawer; she says, flat and quiet: \"" + L026 + "\" and presses her lips together. In the doorway behind her he stays where he is, watching her.",
        F2, PHYS,
        "While the line is spoken, Her keeps doing one thing with their hands: her right hand resting on the top of the chest of drawers, at one steady hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("HER", "tired, in the outfit of the card, at the chest of drawers, back to the door", "nothing"),
        "FOCUS: the nearest eye of Her is in sharp focus; the doorway and the husband behind her fall soft. The blur is optical: soft and round, never smeared.",
        dialogue("Her", L026, VOICE_N, "she will not let him make it a joke, or a conversation. Speaking to her husband in the doorway behind her without turning.",
                 "closes the subject. Opens flat; turns on 'shuts', where her lips press; exits looking down. Stress on 'shuts'.",
                 "quiet, flat and dry, matching the face in this shot.",
                 "she knows nothing has worked, which leaks only through her not turning round."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, "no turning round, no husband leaving the doorway, no husband speaking, no crying", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the husband drops out of the frame (v1)", "prevented_by": "him in the doorway behind her written into the shot, sheet + card attached (HT24)"},
           {"risk": "she turns to him", "prevented_by": "'does not turn round', eyes down, negative"},
           {"risk": "the husband speaks her line", "prevented_by": "only her voice master as Audio1, negative"}]))

SHOTS.append(dict(beat="SC03-SH09", kind="dialogue", duration=7, line=L028, subject_motion="still", gen=2,
    fix="user (chat): \"HERE SHE IS NOT USING THE SAME PHONE AS THE NEXT SHOT\" — v1 a cream cordless handset, SH10 a slim gold smartphone → v2 uses SH10's phone, named the same way in both", files=["N", "L-BEDROOM", "OUT-N-B3"], audios=["N"],
    title="Scene 3 · The sister on the phone — \"Course, love. Easier.\"",
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", HER_B3)), ("@image2", BEDROOM), ("@image3", CARD_N), ("@audio1", VOICE("Her"))]),
        SERIES, LOOK, INHERIT, BEDROOM_EVE.replace(" Her husband, in the outfit of his card, has come to the open bedroom door from the landing.", " Her husband has gone downstairs."),
        f"THE SHOT: a medium close-up from the front at her eye level: Her, {HER_ID}, in {HER_B3}, sits on the near edge of the bed, "
        f"{PHONE} held flat to her right ear; the bedside lamp warm beside her, the chest of drawers soft behind.",
        "For the first four seconds she listens: her sister is speaking on the phone, unheard; Her's eyes drop to the floor, a small breath, her face settling. "
        "Then she answers, gently, and it costs her: \"" + L028 + "\"",
        F2, PHYS,
        "While the line is spoken, Her keeps doing one thing with their hands: her right hand holding the phone to her ear, at one steady hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("HER", "tired, in the outfit of the card, on the bed edge with the phone", "nothing"),
        "FOCUS: the nearest eye of Her is in sharp focus; the room behind falls soft. The blur is optical: soft and round, never smeared.",
        dialogue("Her", L028, VOICE_N, "her sister has just suggested the garden centre because it is all on one level. Speaking into the phone.",
                 "agrees to make it easy for both of them. Opens warm; turns on 'Easier', where her eyes close for a moment; exits looking at the floor. Stress on 'Course'.",
                 "soft and warm, a little tired, matching the face in this shot.",
                 "she minds that their Sundays are planned around their knees, which leaks only through her eyes closing on 'Easier'."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, "no cordless handset, no landline, no lit screen, no speaking before the fourth second, no second voice", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "she speaks during the sister's line", "prevented_by": "four listening seconds written, negative; the sister's line is laid in the edit"},
           {"risk": "a second voice generated", "prevented_by": "only her voice master attached, second-voice negative"},
           {"risk": "a different phone from SH10 (the user's Fix)", "prevented_by": "PHONE named identically in SH09 and SH10, handset/landline negative"}]))

SHOTS.append(dict(beat="SC03-SH10", kind="broll", duration=6, line="", vo="L029", subject_motion="still", files=["N", "L-BEDROOM", "OUT-N-B3"], audios=[],
    title="Scene 3 · A life on one level",
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", HER_B3)), ("@image2", BEDROOM), ("@image3", CARD_N)]),
        SERIES, LOOK, INHERIT, BEDROOM_EVE.replace(" Her husband, in the outfit of his card, has come to the open bedroom door from the landing.", " Her husband has gone downstairs."),
        f"THE SHOT: a high wide shot from the corner of the bedroom near the ceiling, at three-quarter: Her, {HER_ID}, in {HER_B3}, sits on the near edge of the bed, small in the room; "
        "the chest of drawers with its proud bottom drawer under the window, the lamp, the door to the landing open and dark.",
        f"She slowly lowers {PHONE_SHORT} from her ear to her lap and holds it there in both hands, still, looking at nothing. Nothing else moves.",
        F6, PHYS,
        state("HER", "tired, in the outfit of the card, on the bed edge", "the phone is in her lap"),
        "FOCUS: deep focus, the whole room sharp; she is small in the middle of it. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, "no standing up, no walking, no talking, no mouth moving, no tears falling", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "she stands or walks during the pull-back", "prevented_by": "F6: subject stays in place, negative"},
           {"risk": "the drawer shut flat", "prevented_by": "proud bottom drawer written"},
           {"risk": "overplayed sadness", "prevented_by": "still, looking at nothing, NEG-DRAMA"}]))

FILES = {"N": "cast/N-HER_v1.png", "C3": "cast/C3-HUSBAND_v1.png", "L-STAIRS": "plates/L-STAIRS_v4.png", "L-BEDROOM": "plates/L-BEDROOM_v1.png",
         "L-KITCHEN": "plates/L-KITCHEN_v1.png", "INFO-PHYSIO": "body/SC03/ingredients/INFO-PHYSIO_v1.png",
         "OUT-N-B3": "body/SC03/ingredients/OUT-N-B3_v1.png", "OUT-C3-B3": "body/SC03/ingredients/OUT-C3-B3_v2.png",
         "INFO-BRACE": "body/SC03/ingredients/INFO-BRACE_v1.png", "INFO-DRAWER": "body/SC03/ingredients/INFO-DRAWER_v2.png"}
AUDIO = {"N": "voice/N_voice_master.mp3", "C3": "voice/C3_voice_master.mp3"}

if __name__ == "__main__":
    for s in SHOTS:
        call = {"beat": s["beat"], "connector": "seedance", "model": "bytedance/seedance-2-5", "mode": 4, "kind": s["kind"], "prompt": s["prompt"],
                "duration": s["duration"], "resolution": "720p", "aspect_ratio": "9:16", "start_image": None,
                "ingredients_approved": True, "files": [FILES[f] for f in s["files"]], "audios": [AUDIO[a] for a in s["audios"]],
                "generate_audio": bool(s["line"]), "dialogue": s["line"] or None, "script_line": s["line"] or None, "pace": "unhurried",
                "subject_motion": s["subject_motion"], "prefer_multi_shots": "false", "generation": s.get("gen", 1), "fix_note": s.get("fix"), "user_go": GO,
                "risks": s["risks"], "vo": s.get("vo"), "pilot": s.get("pilot", False), "scene": 3, "title": s["title"],
                "taste": ["HT02", "HT17", "HT18", "HT22", "HT23"] + (["HT24"] if s["beat"] in ("SC03-SH07", "SC03-SH08") else [])}
        (H / f"{s['beat']}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{s['beat']}.prompt.txt").write_text(s["prompt"])
        print(s["beat"], s["duration"], "s", len(s["prompt"]), "chars")
