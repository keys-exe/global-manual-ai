"""Scene 2 (Rock bottom) — Wan 3.0 Prime clips on Kie AI, INGREDIENTS ONLY, no frames
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
           "dressing gown of the outfit card, is coming down the stairs slowly, facing down the flight, one step at a time, both feet together on each step before the next, her right hand gripping the banister rail. Her husband "
           "waits in the hall at the foot of the stairs holding a plain white mug of tea. The shopping bags are gone from the hall.")
AFTERNOON = ("THE SCENE SO FAR, the same day, afternoon: flat grey overcast light through the net curtains, about 6500K; the bedside lamp is off. Her, still in the dressing gown of the outfit card, "
             "has gone back upstairs and sits alone on her bed.")
STATIC = "no sliding, no gliding, no drifting across the floor, no feet skating, no camera push, no zoom"

L017 = "Just leave it by the stairs, love. I’ll get it later."
L018 = "I’ll bring it up."
L020 = "Sleep alright?"
L021 = "Fine, love."
GO = "use wan 3.0 prime the ingredients and not frames / we will not use frames so we will re do the scene 2 / confirme and remove the previouse scene 2"


def dialogue(who, line, voice, moment, playing, now, under):
    return (f"DIALOGUE ({who}, verbatim): \"{line}\" {voice} IN THIS MOMENT: {moment} PLAYING: {playing} VOICE NOW: {now} "
            f"UNDER THE LINE: {under} Played small and true, for a camera close enough to see a thought. Never theatrical, never pushed, never performed to the lens.")


SHOTS = []
SHOTS.append(dict(beat="SC02-SH01", kind="dialogue", duration=7, line=L017, subject_motion="still", files=["N", "P-HOUSE", "PROP-BAGS"], audios=["N"], pilot=True, gen=2,
    fix="User Fix (board): \"she should be at the top and not going down the stairs\" → fault in the action: 'stands still' left 7 s with nothing to do, so the model walked her down → she is planted on the landing for the whole clip with three small written movements (mouth, a weight shift, the hand tightening), leaving-the-landing negatives",
    prompt=" ".join([
        manifest([("Image1", SHEET("Her", HER_B1)), ("Image2", HALL), ("Image3", CARD_BAGS), ("Audio1", VOICE("Her"))]),
        SERIES, LOOK, INHERIT, HOUSE, NIGHT,
        "THE SHOT: a full-length shot from low in the hall just inside the front door, looking straight down the hall and up the whole flight to the landing, exactly as the place reference "
        f"shows it: the two bags near in the foreground at the foot of the stairs; at the very top, small in the frame, Her, {HER_ID}, in {HER_B1}.",
        "She stays exactly where she is, on the landing at the very top, for the WHOLE clip: both feet planted on the landing, she never takes a step and never sets a foot on the stairs. "
        "Her right hand holds the top newel post, her left hand loose at her side; she looks down the stairs toward the hall and calls down: \"" + L017 + "\" "
        "The only movements are her mouth, a small shift of her weight from one foot to the other, and her right hand tightening on the post on 'later'.",
        F2, PHYS,
        "While the line is spoken, Her keeps doing one thing with their hands: her right hand resting on the top newel post, at one steady hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("HER", "tired, bob and fringe in place, in her own clothes, on the landing at the very top of the stairs", "nothing"),
        "FOCUS: everything from the bags in the foreground to her on the landing is in sharp focus; everything from near to far stays sharp. The blur is optical: soft and round, never smeared.",
        dialogue("Her", L017, VOICE_N, "she cannot face the stairs tonight and covers it with a light voice. Speaking down the stairs to her husband in the hall.",
                 "covers her fear. Opens light and easy; turns on 'later', where her eyes leave the stairs; exits looking away. Stress on 'later'.",
                 "light and a little tired, raised to carry down the stairs, matching the face in this shot.",
                 "she knows she will not come down, which leaks only through her hand tightening on the post."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, NEG_STAIRS, STATIC, "no walking down the stairs, no stepping onto the stairs, no coming down, no leaving the landing, no walking toward the camera", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the house drifts from the plate", "prevented_by": "the hall plate as Image2, THE HOUSE block with left/right (HT22)"},
           {"risk": "she steps down", "prevented_by": "feet stay on the landing, stair negatives"},
           {"risk": "the bags change", "prevented_by": "the prop card as Image3"},
           {"risk": "voice drifts from the master", "prevented_by": "her voice master as Audio1"}]))

SHOTS.append(dict(beat="SC02-SH02", kind="dialogue", duration=4, line=L018, subject_motion="in_place", files=["C3", "L-STAIRS", "PROP-BAGS"], audios=["C3"],
    prompt=" ".join([
        manifest([("Image1", SHEET("the husband", HUS_OUT)), ("Image2", STAIRS), ("Image3", CARD_BAGS), ("Audio1", VOICE("the husband"))]),
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

SHOTS.append(dict(beat="SC02-SH03", kind="broll", duration=6, line="", vo="L019", subject_motion="travels", files=["N", "P-HOUSE", "OUT-N-B2"], audios=[], pilot=True, gen=2,
    fix="User Fix (board): \"it should be going down the stairs and not backwards\" → change of action at the user's call: she comes down facing forwards, slowly, one step at a time (HT02); the camera moved to the foot of the stairs looking up so the descent can only read one way — toward the camera",
    prompt=" ".join([
        manifest([("Image1", SHEET("Her", HER_B2)), ("Image2", HALL), ("Image3", CARD_B2)]),
        SERIES, LOOK, INHERIT, HOUSE, MORNING,
        "THE SHOT: a medium-wide shot from the hall at the foot of the stairs, looking straight up the flight, exactly as the place reference shows the staircase: "
        f"Her, {HER_ID}, in {HER_B2}, is near the top of the flight, facing down the stairs toward the camera.",
        "She comes DOWN the stairs toward the camera, slowly, one step at a time: her right hand grips the banister rail and slides down it, her left hand flat against the stair wall; "
        "she lowers one foot onto the next step down, then brings the other foot down beside it, both feet together on each step before the next, about one step every three seconds, "
        "eyes on the step below her, jaw set. Two steps down in the clip, never faster.",
        F2, PHYS,
        state("HER", "tired, bob and fringe in place, in the dressing gown, near the top of the flight, right hand on the banister", "she is two steps lower"),
        "FOCUS: her face and hands are in sharp focus; the stair wall behind her falls soft. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, NEG_STAIRS, "no going up the stairs, no walking backwards, no turning round, no letting go of the banister, no talking, no mouth moving", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "she climbs instead of descending", "prevented_by": "the camera at the foot, she comes down toward it, going-up negatives"},
           {"risk": "the stairs bend or her feet slide", "prevented_by": "NEG_STAIRS, one step every three seconds, both feet on each step (HT02)"},
           {"risk": "the gown changes", "prevented_by": "the outfit card as Image3"}]))

SHOTS.append(dict(beat="SC02-SH04", kind="broll", duration=4, line="", vo="L019", subject_motion="in_place", files=["N", "L-STAIRS", "OUT-N-B2"], audios=[],
    prompt=" ".join([
        manifest([("Image1", SHEET("Her", HER_B2)), ("Image2", STAIRS), ("Image3", CARD_B2)]),
        SERIES, LOOK, INHERIT, HOUSE, MORNING,
        f"THE SHOT: a medium close-up in profile at her eye level from beside the banister, a long lens, shallow focus on her eye: Her, {HER_ID}, in {HER_B2}, mid-flight, coming down the stairs facing down the flight.",
        "Her right hand grips the banister rail; she lowers her weight onto the next step down, brings her other foot beside it, and breathes out slowly through her mouth, eyes down on the step, jaw set. One step only.",
        F2, PHYS,
        state("HER", "tired, in the dressing gown, mid-flight, both hands on the banister", "she is one step lower"),
        "FOCUS: the nearest eye of Her is in sharp focus; the stair wall and its photographs behind fall to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, NEG_STAIRS, "no talking, no mouth moving, no letting go of the banister", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "she goes up instead of down", "prevented_by": "facing down the flight, lowering onto the next step down"}, {"risk": "the gown changes", "prevented_by": "outfit card"},
           {"risk": "she lets go of the banister", "prevented_by": "both hands on the rail, negative"}]))

SHOTS.append(dict(beat="SC02-SH05", kind="dialogue", duration=4, line=L020, subject_motion="still", files=["C3", "P-HOUSE"], audios=["C3"],
    prompt=" ".join([
        manifest([("Image1", SHEET("the husband", HUS_OUT)), ("Image2", HALL), ("Audio1", VOICE("the husband"))]),
        SERIES, LOOK, INHERIT, HOUSE, MORNING,
        f"THE SHOT: a medium close-up at his eye level, three-quarter on, in the hall at the foot of the stairs: the husband, {HUS_ID}, in {HUS_OUT}, beside the bottom newel post, the stairs rising soft behind him.",
        "He holds a plain white mug of tea at chest height in his right hand, his left hand on the newel post; he glances up the stairs, then a little away, not quite looking at how she is coming down, and says: \"" + L020 + "\"",
        F2, PHYS,
        "While the line is spoken, the husband keeps doing one thing with their hands: his right hand holding the mug still at chest height, at one steady hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("THE HUSBAND", "worried and hiding it, in his own clothes, at the foot of the stairs with her tea", "nothing"),
        "FOCUS: the nearest eye of the husband is in sharp focus; the stairs behind him fall to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
        dialogue("the husband", L020, VOICE_C3, "he will not watch her come down backwards. Speaking to his wife on the stairs.",
                 "makes it ordinary. Opens light; turns on 'alright', where his eyes slide away; exits holding the mug out a little. Stress on 'alright'.",
                 "gruff and soft, an ordinary morning voice, matching the face in this shot.",
                 "he has seen it every morning and it frightens him, which leaks only through his eyes not staying on her."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, "no logo or writing on the mug, no climbing the stairs", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "he stares straight at her", "prevented_by": "the glance up and away written (the act map's 'not quite looking')"},
           {"risk": "voice drifts", "prevented_by": "his voice master as Audio1"},
           {"risk": "a logo on the mug", "prevented_by": "a plain white mug, negative (HT18)"}]))

SHOTS.append(dict(beat="SC02-SH06", kind="dialogue", duration=4, line=L021, subject_motion="still", files=["N", "C3", "P-HOUSE", "OUT-N-B2"], audios=["N"],
    prompt=" ".join([
        manifest([("Image1", SHEET("Her", HER_B2)), ("Image2", SHEET("the husband", HUS_OUT)), ("Image3", HALL), ("Image4", CARD_B2), ("Audio1", VOICE("Her"))]),
        SERIES, LOOK, INHERIT, HOUSE, MORNING,
        "THE SHOT: a close-up over the husband's shoulder at her eye level: the soft back of his grey head and his brown cardigan shoulder fill the near left edge, out of focus; "
        f"beyond him, sharp, Her, {HER_ID}, in {HER_B2}, stands on the bottom step of the stairs, a little above him, the banister beside her.",
        "She takes the plain white mug from his hand with both hands, looks at him, and gives a small tight smile that does not reach her eyes, and says: \"" + L021 + "\"",
        F2, PHYS,
        "While the line is spoken, Her keeps doing one thing with their hands: both hands around the mug at chest height, at one steady hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("HER", "tired, in the dressing gown, on the bottom step", "the mug is in her hands"),
        state("THE HUSBAND", "in the near foreground, his back to the camera, out of focus", "the mug has left his hand"),
        "FOCUS: the nearest eye of Her is in sharp focus; his shoulder in the foreground and the hall behind fall to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
        dialogue("Her", L021, VOICE_N, "she has just come down backwards and will not let him say anything about it. Speaking to her husband, close.",
                 "closes the subject. Opens on the smile; turns on 'love', where her eyes drop to the mug; exits looking down. Stress on 'Fine'.",
                 "quiet and a little bright, too quick to be true, matching the face in this shot.",
                 "it is not fine, which leaks only through the smile stopping short of her eyes."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, "no logo or writing on the mug, no spilling, no crying", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the wrong person in the foreground", "prevented_by": "his sheet as Image2, named as the soft foreground"},
           {"risk": "the smile overplayed", "prevented_by": "'small tight', NEG-DRAMA"}, {"risk": "voice drifts", "prevented_by": "her voice master"}]))

SHOTS.append(dict(beat="SC02-SH07", kind="broll", duration=6, line="", vo="L022", subject_motion="still", files=["N", "L-BEDROOM", "OUT-N-B2"], audios=[],
    prompt=" ".join([
        manifest([("Image1", SHEET("Her", HER_B2)), ("Image2", BEDROOM), ("Image3", CARD_B2)]),
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
         "L-BEDROOM": "plates/L-BEDROOM_v1.png", "OUT-N-B2": "body/SC02/ingredients/OUT-N-B2_v1.png", "PROP-BAGS": "body/SC02/ingredients/PROP-BAGS_v1.png"}
AUDIO = {"N": "voice/N_voice_master.mp3", "C3": "voice/C3_voice_master.mp3"}

if __name__ == "__main__":
    for s in SHOTS:
        call = {"beat": s["beat"], "connector": "wan", "model": "wan/3-0-video-prime", "mode": 4, "kind": s["kind"], "prompt": s["prompt"],
                "duration": s["duration"], "resolution": "720p", "aspect_ratio": "9:16", "start_image": None, "end_image": None,
                "ingredients_approved": True, "files": [FILES[f] for f in s["files"]], "audios": [AUDIO[a] for a in s["audios"]],
                "generate_audio": bool(s["line"]), "dialogue": s["line"] or None, "script_line": s["line"] or None, "pace": "unhurried",
                "subject_motion": s["subject_motion"], "prefer_multi_shots": "false", "generation": s.get("gen", 1), "fix_note": s.get("fix"), "user_go": GO,
                "risks": s["risks"], "vo": s.get("vo"), "pilot": s.get("pilot", False), "scene": 2,
                "taste": ["HT02", "HT04", "HT09", "HT17", "HT18", "HT22", "HT23"]}
        (H / f"{s['beat']}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{s['beat']}.prompt.txt").write_text(s["prompt"])
        print(s["beat"], s["duration"], "s", len(s["prompt"]), "chars", "PILOT" if s.get("pilot") else "")
