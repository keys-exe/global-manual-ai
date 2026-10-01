"""Hook C (the dead escalator) — Seedance 2.5 ingredients calls (user 2026-10-01: hooks on Seedance 2.5). Shared strings from Hook A.
Act-map deviations: SH04 and SH05 run on F2 (locked) instead of F1 — the HKB-SH05 Fix ("IT FEELS LIKE SLIDING") showed a push on a
standing subject reads as gliding. The tannoy line L009 is off-screen (SFX-TANNOY in the edit), never voiced in a clip."""
import json
import sys
from pathlib import Path

H = Path(__file__).parent
import importlib.util  # noqa: E402
_spec = importlib.util.spec_from_file_location("hka_calls", H.parent / "HKA" / "build_calls.py")
_hka = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_hka)
sys.modules["hka_calls"] = _hka
from hka_calls import (SERIES, LOOK, INHERIT, F2, PHYS, AUD, SILENT, NEG_EQUIP, NEG_MORPH, NEG_FILM,  # noqa: E402
                       NEG_SCENECUT, NEG_DRAMA, NEG_SOUND, NEG_STAIRS, VOICE_C2, VOICE_N, HER_ID, DAU_ID,
                       manifest, SHEET, VOICE, PLACE, state, negs)

HER_OUT = "a belted knee-length burgundy raincoat, slim black trousers and plain black trainers, a small black leather handbag on her right shoulder"
DAU_OUT = "a zipped black quilted puffer jacket, mid-blue jeans and tan ankle boots"
X2_ID = "a slim white man in his late twenties with a short dark beard and short dark hair faded at the sides"
X2_OUT = "a mid-grey zip-up hoodie over a white T-shirt, black trousers and canvas trainers, a black backpack on both shoulders"
CARD_N = ("is an info card: Her outfit on this day — the burgundy raincoat, black trousers, black trainers and the handbag on her shoulder; follow it exactly, "
          "and its caption strip and any text on it never appear in the clip.")
CARD_C2 = ("is an info card: the daughter's outfit on this day — the black puffer jacket, jeans and the plain white takeaway coffee cup in her right hand; follow it exactly, "
           "and its caption strip and any text on it never appear in the clip.")
VOICE_X2 = ("A man in his late twenties from London, a flat, tired, slightly nasal mid-range voice with plain estuary vowels; quick and clipped, "
            "the sound of someone already late.")
CONCOURSE = ("THE SET, exactly as in the location reference: a busy city railway station concourse on a weekday morning at the foot of a long climb to the street — "
             "on the right a stopped escalator with a yellow folding barrier across its foot, its steps still; on the left beside it a fixed staircase of about thirty steps with steel handrails climbing the same slope; "
             "tiled walls and a steel-and-glass roof high above. Every sign is a blank panel with no readable words. "
             "Light: cool morning daylight through the glass roof, about 6000K, falling from above and a little from the left; soft shadows under brows and chins. Other commuters stay small, soft and in the background.")
STATIC = "no sliding, no gliding, no drifting across the floor, no feet skating, no body moving without the feet stepping, no camera push, no zoom"
GEO = ("THE GEOGRAPHY, fixed for the whole scene: there is exactly one staircase here — the fixed staircase directly beside the stopped escalator, sharing its slope, on the escalator's left as you face up the climb, "
       "separated from it only by the escalator's steel side panel and handrail. There is no other staircase anywhere in the concourse. The escalator is switched off and out of service: its steps and its handrails are completely still for the whole clip, "
       "the yellow folding barrier stands across its foot, and nobody rides it.")
NEG_ESC = ("no moving escalator, no escalator steps moving, no moving escalator handrail, nobody riding the escalator, no second staircase, no other stairs, "
           "no staircase away from the escalator, no stairs on the far side of the concourse")
PLACE_C = PLACE("the station concourse with the stopped escalator and the fixed staircase beside it")

SHOTS = []

L10 = "You’re joking."
SHOTS.append(dict(
    beat="HKC-SH01", kind="dialogue", duration=4, line=L10, subject_motion="still",
    files=["X2", "L-ESCALATOR"], audios=["X2"],
    prompt=" ".join([
        manifest([("@image1", SHEET("the commuter", X2_OUT)), ("@image2", PLACE_C), ("@audio1", VOICE("the commuter"))]),
        SERIES, LOOK, INHERIT, CONCOURSE, GEO,
        "THE SHOT: a medium close-up at eye height, straight on: the commuter, " + X2_ID + ", in " + X2_OUT + ", stands at the foot of the stopped escalator with the yellow barrier just behind him, his phone in his right hand at chest height.",
        "He looks up from his phone toward the barrier, his shoulders drop, and he says flatly: \"" + L10 + "\" He stays where he stands.",
        F2, PHYS,
        "While the line is spoken, the commuter keeps doing one thing with their hands: his right hand lowering the phone slowly to his side, at one slow drop through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("THE COMMUTER", "tired, backpack on both shoulders, phone in his right hand, standing at the foot of the stopped escalator", "nothing"),
        "FOCUS: the nearest eye of the commuter is in sharp focus; the concourse behind falls to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
        "DIALOGUE (the commuter, verbatim): \"" + L10 + "\" " + VOICE_X2 + " IN THIS MOMENT: he has just heard the escalator is out of service and he is already late. Speaking to nobody, under his breath. "
        "PLAYING: complains to himself. Opens deflated; turns on the exact word 'joking', where his eyes close for a beat; exits resigned. Stress on 'joking'. "
        "VOICE NOW: low, flat, a sigh in it, continuing from how the commuter sounded on the previous line, and matching the face in this shot. "
        "UNDER THE LINE: thirty steps feels like a mountain this early, which leaks only through his shoulders dropping. Played small and true, for a camera close enough to see a thought. Never theatrical, never pushed, never performed to the lens.",
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, NEG_ESC, "no readable text on the phone screen", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the groan overacted", "prevented_by": "'flatly', 'under his breath', NEG-DRAMA"},
           {"risk": "phone screen shows text", "prevented_by": "phone at chest height, screen negative"},
           {"risk": "the tannoy line voiced in the clip", "prevented_by": "only his line in DIALOGUE; the tannoy is SFX-TANNOY in the edit"}]))

L11 = "It’s only stairs, love."
SHOTS.append(dict(
    beat="HKC-SH02", kind="dialogue", duration=4, line=L11, subject_motion="travels",
    files=["N", "X2", "L-ESCALATOR", "OUT-N-HC"], audios=["N"],
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", "the outfit on the info card")), ("@image2", SHEET("the commuter", X2_OUT)), ("@image3", PLACE_C),
                  ("@image4", CARD_N), ("@audio1", VOICE("Her"))]),
        SERIES, LOOK, INHERIT, CONCOURSE, GEO,
        "THE SHOT: a full-length shot from low at floor level behind and to the right of the commuter, looking toward the foot of the climb exactly as in the location reference: the stopped escalator with its yellow barrier is on the right of frame, and the fixed staircase directly beside it, on its left, rises in the centre of frame. "
        "The commuter's legs and backpack fill the near right edge, soft. Her, " + HER_ID + ", in " + HER_OUT + ", is in the near foreground with her back three-quarters to the camera, walking away from the camera toward the foot of that staircase.",
        "The commuter stands still facing the stopped escalator, staring at its yellow barrier, fed up. She walks past him at an even, brisk pace, one step per second, heading straight for the staircase beside the escalator, and as she draws level with him she says lightly to him, without stopping: \"" + L11 + "\" "
        "As she speaks, the commuter turns his head from the escalator to look at her, a beat after her first word, and watches her go; his feet stay where they are. "
        "Then she puts her right foot on the first step of that staircase — the one directly beside the stopped escalator — and her left foot on the second, both hands free, and starts to climb away from the camera.",
        F2, PHYS,
        "While the line is spoken, Her keeps doing one thing with their hands: her right hand resting on the strap of the handbag on her shoulder, at one steady hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("HER", "calm, bob and fringe in place, raincoat belted, handbag on her right shoulder, hands free, walking up to the foot of the stairs", "she reaches the stairs and starts up"),
        state("THE COMMUTER", "fed up, backpack on, phone lowered, standing at the foot of the stopped escalator looking at its barrier", "he turns his head to look at her as she speaks"),
        "FOCUS: everything from the commuter's legs to the stairs is in sharp focus; everything from near to far stays sharp. The blur is optical: soft and round, never smeared.",
        "DIALOGUE (Her, verbatim): \"" + L11 + "\" " + VOICE_N + " IN THIS MOMENT: she is breezy and a little amused at his fuss. Speaking to the commuter in passing, kindly. "
        "PLAYING: teases the commuter. Opens light in passing; turns on the exact word 'only', where a small smile lands; exits already on the stairs. Stress on 'only'. "
        "VOICE NOW: easy and bright, a little raised over the concourse, continuing from how Her sounded on the previous line, and matching the face in this shot. "
        "UNDER THE LINE: six weeks ago she would have been the one groaning, which leaks only through not breaking her stride. Played small and true, for a camera close enough to see a thought. Never theatrical, never pushed, never performed to the lens.",
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, NEG_STAIRS, NEG_ESC, "no stepping onto the escalator, no climbing the stopped escalator, no walking toward the camera, no walking away from the stairs", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    gen=3, go="FIX (user, 2026-10-01, after the v2 Fix note)", fix="User Fix v2: \"THE MAN SHOULD BE LOOKING AT THE ESCALATOR AND THEN LOOKS AT THE MAIN CHARACTER WHEN SHE TALKS\" → fault in the prompt's blocking: the commuter's gaze was never written, so he stared ahead → he faces and looks at the stopped escalator's barrier, then turns his head to her a beat after her first word and watches her go, feet planted; she speaks to him as she draws level. v1 Fix kept: User Fix: \"THEY ARE TAKING THE WRONG STAIRS, AND THE ESCALATOR SHOULD NOT BE MOVING CAUSE ITS NOT WORKING AND THE STAIRS THEY ARE TALKING IS BESIDE THE ESCALATOR\" → fault in the prompt's set and staging: the camera faced the escalator with the stairs hidden behind the commuter, so the model had her walk toward the camera across the floor and invented another staircase; the escalator was never stated as still → camera now looks up the climb as in the plate (escalator right, its staircase directly beside it on the left), she walks away from the camera onto that staircase, a GEOGRAPHY block (one staircase, beside the escalator; escalator switched off, steps and handrails still), moving-escalator / second-staircase negatives",
    risks=[{"risk": "the commuter looks the wrong way", "prevented_by": "gaze written: on the escalator barrier, then to her on her line"},
           {"risk": "she takes another staircase or walks toward the camera", "prevented_by": "plate viewpoint, GEOGRAPHY block, second-staircase and walk-toward-camera negatives"},
           {"risk": "the escalator moves", "prevented_by": "GEOGRAPHY: switched off, steps and handrails still; moving-escalator negatives"},
           {"risk": "she climbs the stopped escalator instead of the stairs", "prevented_by": "the fixed staircase named as hers, escalator negatives"},
           {"risk": "she stops to speak", "prevented_by": "'without stopping', one step per second"},
           {"risk": "the commuter's face takes over", "prevented_by": "only his legs and backpack, soft, at the near edge"}]))

SHOTS.append(dict(
    beat="HKC-SH03", kind="broll", duration=4, line="", subject_motion="travels",
    files=["N", "L-ESCALATOR", "OUT-N-HC"], audios=[],
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", "the outfit on the info card")), ("@image2", PLACE_C), ("@image3", CARD_N)]),
        SERIES, LOOK, INHERIT, CONCOURSE, GEO,
        "THE SHOT: a wide shot from a little above head height at the foot of the climb, behind her, the same view as the location reference: the fixed staircase rises up the centre of frame and the stopped escalator with its yellow barrier runs right beside it on the right. "
        "Her, " + HER_ID + ", in " + HER_OUT + ", is already a third of the way up that staircase, her back to the camera, climbing away from it; "
        "at the foot of the stairs, nearest the camera, a few commuters bunch up, small and soft.",
        "She climbs away from the camera at an even pace, one step up per second, one foot per step, up the staircase directly beside the escalator, hands free, her back to the camera the whole clip. "
        "The commuters at the foot shuffle onto the first steps behind her, slower. The escalator beside her stays completely still.",
        F2, PHYS,
        state("HER", "calm, bob and fringe in place, raincoat belted, handbag on her right shoulder, halfway up the stairs", "she is a few steps higher"),
        "FOCUS: everything from the top step to the crowd at the foot is in sharp focus; everything from near to far stays sharp. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, NEG_STAIRS, NEG_ESC, "no turning round, no walking down the stairs, no climbing the stopped escalator, no walking toward the camera", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    gen=2, fix="User Fix: \"THEY ARE TAKING THE WRONG STAIRS, AND THE ESCALATOR SHOULD NOT BE MOVING…\" → fault in the set and viewpoint: 'from the top looking down' made the model invent a second staircase at the left of the concourse and walk her across the floor → the plate's own viewpoint from the foot, behind her, climbing away up the staircase directly beside the stopped escalator, GEOGRAPHY block, moving-escalator / second-staircase negatives",
    risks=[{"risk": "another staircase invented", "prevented_by": "plate viewpoint, GEOGRAPHY block, second-staircase negatives"},
           {"risk": "the escalator moves", "prevented_by": "GEOGRAPHY: switched off and still; negatives"},
           {"risk": "she turns or walks away from the stairs", "prevented_by": "body locked facing up the stairs toward the camera (HKB-SH03 Fix)"},
           {"risk": "the crowd swallows her", "prevented_by": "the crowd small and soft at the foot"},
           {"risk": "sound generated", "prevented_by": "generate_audio false, SILENT, NEG-SOUND"}]))

L12 = "When did that happen?"
SHOTS.append(dict(
    beat="HKC-SH04", kind="dialogue", duration=4, line=L12, subject_motion="still",
    files=["C2", "L-ESCALATOR", "OUT-C2-HC"], audios=["C2"],
    prompt=" ".join([
        manifest([("@image1", SHEET("the daughter", "the outfit on the info card")), ("@image2", PLACE_C), ("@image3", CARD_C2), ("@audio1", VOICE("the daughter"))]),
        SERIES, LOOK, INHERIT, CONCOURSE,
        "THE SHOT: a medium close-up at eye height, three-quarter on: the daughter, " + DAU_ID + ", in " + DAU_OUT + ", stands at the foot of the fixed staircase holding a plain white takeaway coffee cup in her right hand, looking up the stairs after her mother, out of frame above.",
        "She stands still and grounded, both feet planted, staring up the stairs, and says, half to herself: \"" + L12 + "\" Her body does not travel at all.",
        F2, PHYS,
        "While the line is spoken, the daughter keeps doing one thing with their hands: holding the coffee cup still at chest height, at one steady hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("THE DAUGHTER", "a little stunned, hair in its loose low bun, puffer jacket zipped, the coffee cup in her right hand, standing at the foot of the stairs", "nothing"),
        "FOCUS: the nearest eye of the daughter is in sharp focus; the concourse behind falls to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
        "DIALOGUE (the daughter, verbatim): \"" + L12 + "\" " + VOICE_C2 + " IN THIS MOMENT: she is stunned to see her mother take the stairs first. Speaking half to herself, half after her mother. "
        "PLAYING: questions her mother. Opens quiet, amazed; turns on the exact word 'that', where her brows draw together; exits still staring up. Stress on 'that'. "
        "VOICE NOW: quiet and wondering, not out of breath, continuing from how the daughter sounded on the previous line, and matching the face in this shot. "
        "UNDER THE LINE: she is proud and a little worried at once, which leaks only through her grip tightening on the cup. Played small and true, for a camera close enough to see a thought. Never theatrical, never pushed, never performed to the lens.",
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, "no coffee spilling, no logo or writing on the cup", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "she reads as sliding (HKB-SH05)", "prevented_by": "F2 locked instead of the act map's F1, feet planted, sliding negatives"},
           {"risk": "cup changes hands or spills", "prevented_by": "STATE-CARRY, spill negative"},
           {"risk": "voice drifts from the master", "prevented_by": "VOICE-C2 master as @audio1"}]))

SHOTS.append(dict(
    beat="HKC-SH05", kind="broll", duration=7, line="", vo="L013", subject_motion="in_place",
    files=["N", "L-ESCALATOR", "OUT-N-HC"], audios=[],
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", "the outfit on the info card")), ("@image2", PLACE("the top of the fixed staircase, looking down the flight to the concourse")), ("@image3", CARD_N)]),
        SERIES, LOOK, INHERIT, CONCOURSE, GEO,
        "THE SHOT: a close-up from the top landing, the camera looking straight down the flight she has just climbed: Her, " + HER_ID + ", in " + HER_OUT + ", is on the top step facing the camera, the flight dropping away behind her to the concourse. "
        "LEFT AND RIGHT IN THIS FRAME, exactly: the stopped escalator runs down the LEFT side of the frame, right beside the stairs, its still steps and the yellow barrier at its foot far below on the left; "
        "she stands on the RIGHT half of the staircase, on the side away from the escalator — the same side of the stairs she climbed on — with the right-hand steel handrail beside her on the right of frame.",
        "She takes the last step onto the top landing, stops with both feet planted, and turns her head and shoulders back to look down the stairs at her daughter far below, out of frame. "
        "She is not out of breath at all: her breathing is easy and even, and a small private smile settles at the corner of her mouth and stays. She blinks naturally; after the turn her body stays where it is.",
        F2, PHYS,
        state("HER", "calm, not out of breath, bob and fringe in place, raincoat belted, handbag on her right shoulder, at the top of the stairs", "she turns to look back down"),
        "FOCUS: the nearest eye of Her is in sharp focus; the stairs and concourse below fall to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, NEG_ESC, "no escalator on the right of the frame, no mirrored layout, no standing beside the escalator, no talking, no mouth moving, no walking back down the stairs, no panting", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    gen=3, go="FIX (user, 2026-10-01, after the v2 Fix note)", fix="User Fix v2: \"SHE IS AT THE WRONG SIDE OF THE STAIRS\" → fault in the set's left/right: from the top looking down the layout mirrors, and v2 put the escalator on the frame's right and her on the left; in the confirmed SH03 she climbs on the left of the stairs with the escalator on her right → from the top looking down the escalator is on the frame's LEFT and she is on the RIGHT half of the stairs, stated explicitly, mirrored-layout negatives. v1 Fix kept: User Fix: \"THEY ARE TAKING THE WRONG STAIRS, AND THE ESCALATOR SHOULD NOT BE MOVING…\" → fault in the set: the escalator beside her stairs was never placed or stated as still → the stopped escalator placed right beside the staircase behind her, GEOGRAPHY block, moving-escalator / second-staircase negatives",
    risks=[{"risk": "the layout mirrors again", "prevented_by": "LEFT AND RIGHT IN THIS FRAME stated, mirrored-layout negatives"},
           {"risk": "the escalator moves or goes missing", "prevented_by": "escalator placed beside the stairs, GEOGRAPHY, negatives"},
           {"risk": "her mouth moves as if speaking", "prevented_by": "SILENT, 'no talking, no mouth moving', generate_audio false"},
           {"risk": "she reads as sliding (HKB-SH05)", "prevented_by": "F2 locked instead of F1, feet planted, sliding negatives"},
           {"risk": "she looks winded", "prevented_by": "easy breathing stated, 'no panting'"}]))

FILES = {"C2": "cast/C2-DAUGHTER_v1.png", "N": "cast/N-HER_v1.png", "X2": "cast/X2-COMMUTER_v1.png", "L-ESCALATOR": "plates/L-ESCALATOR_v1.png",
         "OUT-N-HC": "hooks/HKC/OUT-N-HC_v1.png", "OUT-C2-HC": "hooks/HKC/OUT-C2-HC_v1.png"}
AUDIO = {"C2": "voice/C2_voice_master.mp3", "N": "voice/N_voice_master.mp3", "X2": "voice/X2_voice_master.mp3"}

if __name__ == "__main__":
    for s in SHOTS:
        call = {"beat": s["beat"], "connector": "seedance", "mode": 4, "kind": s["kind"], "prompt": s["prompt"],
                "duration": s["duration"], "resolution": "720p", "aspect_ratio": "9:16", "start_image": None,
                "ingredients_approved": True, "files": [FILES[f] for f in s["files"]],
                "audios": [AUDIO[a] for a in s["audios"]], "generate_audio": bool(s["line"]),
                "dialogue": s["line"] or None, "script_line": s["line"] or None, "pace": "unhurried",
                "subject_motion": s["subject_motion"], "prefer_multi_shots": "false", "generation": s.get("gen", 1),
                "fix_note": s.get("fix"), "user_go": s.get("go"), "risks": s["risks"], "vo": s.get("vo")}
        (H / f"{s['beat']}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{s['beat']}.prompt.txt").write_text(s["prompt"])
        print(s["beat"], s["duration"], "s", len(s["prompt"]), "chars")
