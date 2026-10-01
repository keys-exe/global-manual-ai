"""Hook B (the lift queue) — Seedance 2.5 ingredients calls (user 2026-10-01: hooks on Seedance 2.5). Shared strings from Hook A."""
import json
import sys
from pathlib import Path

H = Path(__file__).parent
import importlib.util  # noqa: E402
_spec = importlib.util.spec_from_file_location("hka_calls", H.parent / "HKA" / "build_calls.py")
_hka = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_hka)
sys.modules["hka_calls"] = _hka
from hka_calls import (SERIES, LOOK, INHERIT, F2, F1, PHYS, AUD, SILENT, NEG_EQUIP, NEG_MORPH, NEG_FILM,  # noqa: E402
                         NEG_SCENECUT, NEG_DRAMA, NEG_SOUND, NEG_STAIRS, VOICE_C2, VOICE_N, HER_ID, DAU_ID,
                         manifest, SHEET, VOICE, PLACE, state, negs)

HER_OUT = "a hip-length navy quilted jacket zipped halfway over a cream crew-neck jumper, dark blue jeans and plain white trainers"
DAU_OUT = "an open knee-length charcoal wool coat over a plain dark top, mid-blue jeans and tan ankle boots"
CARD_N = ("is an info card: Her outfit on this day — the navy quilted jacket, cream jumper, dark jeans and white trainers; follow it exactly, "
          "and its caption strip and any text on it never appear in the clip.")
CARD_C2 = ("is an info card: the daughter's outfit on this day — the charcoal wool coat, jeans and tan ankle boots; follow it exactly, "
           "and its caption strip and any text on it never appear in the clip.")
CENTRE = ("THE SET, exactly as in the location reference: a bright two-level shopping centre atrium on an ordinary afternoon — a glass lift on the left with a small queue waiting at its doors, "
          "a wide flight of pale tiled stairs with chrome handrails rising to the upper gallery on the right, a glass gallery rail along the top, and a big skylight overhead. "
          "Light: soft daylight from the skylight above, about 5600K, a little stronger from the left; gentle shadows under the brows and chins. Ordinary shoppers stay small and far off in the background.")
BAGS_N = "two full paper shopping bags, one in each hand, carried by their handles"
BAGS_C2 = "three full shopping bags hooked over her forearms, two on the left, one on the right"

SHOTS = []

L5 = "Mum, the lift’s just there."
SHOTS.append(dict(
    beat="HKB-SH01", kind="dialogue", duration=4, line=L5, subject_motion="still",
    files=["C2", "L-SHOPCENTRE", "OUT-C2-HB"], audios=["C2"],
    prompt=" ".join([
        manifest([("@image1", SHEET("the daughter", "the outfit on the info card")), ("@image2", PLACE("the shopping centre atrium with the glass lift and the wide stairs")),
                  ("@image3", CARD_C2), ("@audio1", VOICE("the daughter"))]),
        SERIES, LOOK, INHERIT, CENTRE,
        "THE SHOT: a medium shot at eye height, straight on: the daughter, " + DAU_ID + ", in " + DAU_OUT + ", stands near the foot of the stairs with " + BAGS_C2 + "; the glass lift and its small queue are behind her to frame left.",
        "She tips her head toward the lift once, a small nod, and says: \"" + L5 + "\" She stays where she stands.",
        F2, PHYS,
        "While the line is spoken, the daughter keeps doing one thing with their hands: hitching the bag handles a little higher on her left forearm, at one slow hitch through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("THE DAUGHTER", "loaded with three shopping bags on her forearms, coat open, hair in its loose low bun, standing near the foot of the stairs", "nothing"),
        "FOCUS: the nearest eye of the daughter is in sharp focus; the atrium behind falls to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
        "DIALOGUE (the daughter, verbatim): \"" + L5 + "\" " + VOICE_C2 + " IN THIS MOMENT: she is being sensible and assumes her mother will agree. Speaking to her mother, practical and fond. "
        "PLAYING: steers her mother. Opens matter-of-fact; turns on the exact word 'lift', where she nods toward it; exits expecting a yes. Stress on 'lift'. "
        "VOICE NOW: easy, a little tired from the shopping, continuing from how the daughter sounded on the previous line, and matching the face in this shot. "
        "UNDER THE LINE: she is the one who wants the lift, which leaks only through the bags sagging on her arm. Played small and true, for a camera close enough to see a thought. Never theatrical, never pushed, never performed to the lens.",
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "bags change count or float", "prevented_by": "bag count stated, STATE-CARRY, PHYS"},
           {"risk": "the lift queue crowds the frame", "prevented_by": "SET line: shoppers small and far off"},
           {"risk": "voice drifts from the master", "prevented_by": "VOICE-C2 master as @audio1"}]))

SHOTS.append(dict(
    beat="HKB-SH02", kind="broll", duration=4, line="", subject_motion="travels",
    files=["N", "L-SHOPCENTRE", "OUT-N-HB"], audios=[],
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", "the outfit on the info card")), ("@image2", PLACE("the shopping centre atrium with the wide stairs")), ("@image3", CARD_N)]),
        SERIES, LOOK, INHERIT, CENTRE,
        "THE SHOT: a full-length shot from low at the foot of the stairs, three-quarter from behind: Her, " + HER_ID + ", in " + HER_OUT + ", already three steps up the wide tiled staircase with " + BAGS_N + ", the flight rising ahead of her to the gallery.",
        "She climbs at an even pace, one step per second, one foot per step, the bags swinging a little at her sides, and on the fourth step glances back over her left shoulder toward the camera side, then faces forward and keeps climbing.",
        F2, PHYS,
        state("HER", "calm, bob and fringe in place, jacket zipped halfway, a full shopping bag in each hand, three steps up and climbing", "she is a few steps higher"),
        "FOCUS: everything from the foot of the stairs to the gallery is in sharp focus; everything from near to far stays sharp. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, NEG_STAIRS, NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the camera follows her up", "prevented_by": "F2 locked tripod, one late partial tilt only"},
           {"risk": "steps warp or feet skate", "prevented_by": "stairs negatives, PHYS, one foot per step"},
           {"risk": "sound generated", "prevented_by": "generate_audio false, SILENT, NEG-SOUND"}]))

L6 = "So are the stairs."
SHOTS.append(dict(
    beat="HKB-SH03", kind="dialogue", duration=4, line=L6, subject_motion="travels",
    files=["N", "L-SHOPCENTRE", "OUT-N-HB"], audios=["N"],
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", "the outfit on the info card")), ("@image2", PLACE("the shopping centre atrium with the wide stairs")),
                  ("@image3", CARD_N), ("@audio1", VOICE("Her"))]),
        SERIES, LOOK, INHERIT, CENTRE,
        "THE SHOT: a medium close-up from the top of the stairs, the camera on the upper landing looking straight down the flight: Her, " + HER_ID + ", in " + HER_OUT + ", is halfway up the wide tiled stairs, facing up the stairs and climbing up toward the camera with " + BAGS_N + ", the steps below her falling away to the ground floor.",
        "Her body, chest and feet face up the stairs for the whole clip and she keeps climbing upward toward the camera, one step up per second, one foot per step, each foot landing on the next higher step. "
        "Without stopping and without turning round, she flicks her eyes and chin a little down to her left toward her daughter, who is out of frame at the foot of the stairs, and says: \"" + L6 + "\" Then her eyes come back up the stairs and she climbs on, closer to the camera.",
        F2, PHYS,
        "While the line is spoken, Her keeps doing one thing with their hands: carrying a full bag in each hand, at one easy swing per step. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("HER", "calm, not out of breath, bob and fringe in place, jacket zipped halfway, a full shopping bag in each hand, halfway up the stairs", "she is a few steps higher"),
        "FOCUS: the nearest eye of Her is in sharp focus; the stairs and atrium below fall to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
        "DIALOGUE (Her, verbatim): \"" + L6 + "\" " + VOICE_N + " IN THIS MOMENT: she is amused that the lift was ever an option. Speaking to her daughter, dry and fond. "
        "PLAYING: teases her daughter. Opens light over her shoulder; turns on the exact word 'stairs', where a dry little smile lands; exits already climbing. Stress on 'stairs'. "
        "VOICE NOW: easy, steady breath, a little raised to carry down the stairs, continuing from how Her sounded on the previous line, and matching the face in this shot. "
        "UNDER THE LINE: she is quietly proud her knees let her do this now, which leaks only through not slowing down at all. Played small and true, for a camera close enough to see a thought. Never theatrical, never pushed, never performed to the lens.",
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, NEG_STAIRS, "no turning round, no turning her back to the camera, no walking down the stairs, no walking away from the stairs, no stepping off the stairs, no walking along the landing", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    gen=2, fix="User Fix: \"she should be going to the stairs and not away from it\" → fault in the prompt's motion: 'turns her head back over her shoulder… then faces up again' let the model turn her whole body and walk away from the flight → body, chest and feet locked facing up the stairs, climbing toward the camera, only a glance down to the left, no turn; turn-round / walk-down / walk-away negatives added",
    risks=[{"risk": "she turns round or walks away from the stairs", "prevented_by": "body locked facing up the stairs, glance not a turn, explicit negatives"},
           {"risk": "she stops to speak", "prevented_by": "'Without breaking stride', one step per second"},
           {"risk": "bags change hands or vanish", "prevented_by": "STATE-CARRY, bag count stated"},
           {"risk": "voice not hers", "prevented_by": "VOICE-N master as @audio1"}]))

L7 = "When did that happen?"
SHOTS.append(dict(
    beat="HKB-SH04", kind="dialogue", duration=4, line=L7, subject_motion="in_place",
    files=["C2", "L-SHOPCENTRE", "OUT-C2-HB"], audios=["C2"],
    prompt=" ".join([
        manifest([("@image1", SHEET("the daughter", "the outfit on the info card")), ("@image2", PLACE("the upper gallery at the top of the stairs")),
                  ("@image3", CARD_C2), ("@audio1", VOICE("the daughter"))]),
        SERIES, LOOK, INHERIT, CENTRE,
        "THE SHOT: a medium close-up in profile at eye height on the upper gallery: the daughter, " + DAU_ID + ", in " + DAU_OUT + ", has just reached the top step with " + BAGS_C2 + ", facing frame left toward her mother out of frame.",
        "The clip opens with her on the top step. She stops, chest heaving, the bags sagging on her forearms, looks across at her mother, and between breaths says: \"" + L7 + "\" Her feet stay where they are.",
        F2, PHYS,
        "While the line is spoken, the daughter keeps doing one thing with their hands: her right hand gripping the chrome handrail, still, at one grip through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("THE DAUGHTER", "out of breath from the climb, a few strands loose from her low bun, coat open, three bags sagging on her forearms, on the top step", "her breathing is heavier"),
        "FOCUS: the nearest eye of the daughter is in sharp focus; the atrium behind falls to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
        "DIALOGUE (the daughter, verbatim): \"" + L7 + "\" " + VOICE_C2 + " IN THIS MOMENT: she is winded and astonished. Speaking to her mother, genuinely asking. "
        "PLAYING: questions her mother. Opens puffing, a breath first; turns on the exact word 'that', where her brows draw together; exits waiting for an answer. Stress on 'that'. "
        "VOICE NOW: breathless from the climb, broken by a breath, continuing from how the daughter sounded on the previous line, changed only by the stairs, and matching the face in this shot. "
        "UNDER THE LINE: she is a little embarrassed to be the one puffing, which leaks only through a glance down at the bags. Played small and true, for a camera close enough to see a thought. Never theatrical, never pushed, never performed to the lens.",
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "she keeps walking out of frame", "prevented_by": "'Her feet stay where they are', in_place, F2"},
           {"risk": "overplayed panting", "prevented_by": "NEG-DRAMA, 'played small and true'"},
           {"risk": "voice drifts from the master", "prevented_by": "VOICE-C2 master as @audio1"}]))

SHOTS.append(dict(
    beat="HKB-SH05", kind="broll", duration=7, line="", vo="L008", subject_motion="still",
    files=["N", "C2", "L-SHOPCENTRE", "OUT-N-HB", "OUT-C2-HB"], audios=[],
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", "the outfit on the info card")), ("@image2", SHEET("the daughter", "the outfit on her info card")),
                  ("@image3", PLACE("the shopping centre atrium, seen from its upper floor")), ("@image4", CARD_N), ("@image5", CARD_C2)]),
        SERIES, LOOK, INHERIT, CENTRE,
        "THE SHOT: a close-up over the daughter's shoulder, up on the second floor of the atrium, one full storey above the ground floor: the soft back of the daughter's head and charcoal coat shoulder frame the near right edge, out of focus; "
        "Her, " + HER_ID + ", in " + HER_OUT + ", stands on the upper-floor gallery with her back to the glass gallery rail, facing the camera side, her two shopping bags set down by her feet. "
        "Behind her, beyond the glass rail, the atrium drops away a full storey: the ground floor is far below and small, the glass lift shaft rises past the rail, and the skylight is close overhead — the shot is unmistakably upstairs.",
        "She stands still and grounded: both feet flat on the gallery floor, planted the whole clip, her weight settling once onto her left leg near the start. She waits, breathing easily — her shoulders rise and fall with each breath — looking at her daughter, and her eyebrows lift a little: a small, dry, unbothered look that stays. She blinks naturally. Her body does not travel at all; she and the floor under her stay exactly where they are relative to the rail and the lift shaft behind her.",
        F2, PHYS,
        state("HER", "calm, not out of breath, bob and fringe in place, jacket zipped halfway, both shopping bags on the floor by her feet, at the upper-floor gallery rail", "her eyebrows lift a little"),
        state("THE DAUGHTER", "out of breath, coat open, bags on her forearms, back to the camera", "nothing"),
        "FOCUS: the nearest eye of Her is in sharp focus; the daughter's shoulder in front and the atrium behind fall to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, "no sliding, no gliding, no drifting across the floor, no feet skating, no body moving without the feet stepping, no camera push, no zoom, no background sliding behind her, no talking, no mouth moving, no ground-floor setting, no shopfronts at her level behind her, no floor tiles stretching away behind her at her level", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    gen=3, go="FIX THOSE (user, 2026-10-01, after the v2 Fix note)", fix="User Fix v2: \"IT FEELS LIKE SLIDING\" → fault in the motion: an F1 dolly push on a standing subject with nothing else moving read as her gliding across the floor (the background slid while she stayed still) → camera locked on a tripod (F2, no push), her feet planted with one weight shift and visible breathing so the body is grounded, sliding / gliding / camera-push negatives; v1 Fix kept: \"this should be on the second floor\" → fault in the prompt's set: 'on the upper gallery' was one phrase the model ignored, so it staged her at ground level → the second floor stated three ways (one storey up, the drop to the ground floor behind her through the glass rail, the lift shaft and skylight close), the place clause reworded to the upper floor, ground-floor negatives added",
    risks=[{"risk": "she still looks like she glides", "prevented_by": "F2 locked camera, feet planted, weight shift, sliding negatives"},
           {"risk": "staged on the ground floor again", "prevented_by": "the drop behind her through the glass rail, ground-floor negatives"},
           {"risk": "her mouth moves as if speaking", "prevented_by": "SILENT, 'no talking, no mouth moving', generate_audio false"},
           {"risk": "the look overplayed", "prevented_by": "'a little', NEG-DRAMA"},
           {"risk": "bags jump back into her hands", "prevented_by": "STATE-CARRY: bags on the floor"}]))

FILES = {"C2": "cast/C2-DAUGHTER_v1.png", "N": "cast/N-HER_v1.png", "L-SHOPCENTRE": "plates/L-SHOPCENTRE_v1.png",
         "OUT-N-HB": "hooks/HKB/OUT-N-HB_v1.png", "OUT-C2-HB": "hooks/HKB/OUT-C2-HB_v1.png"}
AUDIO = {"C2": "voice/C2_voice_master.mp3", "N": "voice/N_voice_master.mp3"}

if __name__ == "__main__":
    for s in SHOTS:
        call = {"beat": s["beat"], "connector": "seedance", "mode": 4, "kind": s["kind"], "prompt": s["prompt"],
                "duration": s["duration"], "resolution": "720p", "aspect_ratio": "9:16", "start_image": None,
                "ingredients_approved": True, "files": [FILES[f] for f in s["files"]],
                "audios": [AUDIO[a] for a in s["audios"]], "generate_audio": bool(s["line"]),
                "dialogue": s["line"] or None, "script_line": s["line"] or None, "pace": "unhurried",
                "subject_motion": s["subject_motion"], "prefer_multi_shots": "false", "generation": s.get("gen", 1), "fix_note": s.get("fix"), "user_go": s.get("go"),
                "risks": s["risks"], "vo": s.get("vo")}
        (H / f"{s['beat']}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{s['beat']}.prompt.txt").write_text(s["prompt"])
        print(s["beat"], s["duration"], "s", len(s["prompt"]), "chars")
