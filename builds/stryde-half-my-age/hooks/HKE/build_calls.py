"""Hook E (the floor) — Seedance 2.5 ingredients calls (user 2026-10-01: hooks on Seedance 2.5). Shared strings from Hook A.
House Taste applied: HT22 (one GEOGRAPHY block for the living room, left/right stated), the HKB-SH05 sliding note (F2 on every
standing subject — the act map's F1 on SH04/SH05 runs as F2), HT18 (the jigsaw box plain, no picture or writing)."""
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
                       NEG_SCENECUT, NEG_DRAMA, NEG_SOUND, VOICE_C2, HER_ID, DAU_ID,
                       manifest, SHEET, VOICE, PLACE, state, negs)

HER_OUT = "a long open oatmeal knitted cardigan over a plain teal top, straight mid-grey trousers and soft grey slippers"
DAU_OUT = "a mid-blue denim jacket over a plain grey hooded sweatshirt, mid-blue jeans and tan ankle boots"
CARD_N = ("is an info card: Her outfit on this day — the oatmeal cardigan, teal top, grey trousers and slippers; follow it exactly, "
          "and its caption strip and any text on it never appear in the clip.")
CARD_C2 = ("is an info card: the daughter's outfit on this day — the denim jacket over the grey hoodie and jeans; follow it exactly, "
           "and its caption strip and any text on it never appear in the clip.")
BOX = "a plain sky-blue cardboard jigsaw box with no picture and no writing on it"
ROOM = ("THE SET, exactly as in the location reference: her front living room on an ordinary afternoon — a deep bay window with net curtains and heavy green velvet curtains on the far wall; "
        "a 1930s tiled fireplace with a gas fire and a wooden mantel of small framed photographs on the right-hand wall; a worn brown leather armchair angled beside the fire; "
        "a faded rose-and-cream floral three-seat sofa facing the fire; a patterned red-and-cream rug over oatmeal carpet in the middle of the room. "
        "Light: soft, cool daylight from the bay window, about 5600K, from the far side of the room; the near side of every face falls into gentle shadow.")
GEO = ("THE GEOGRAPHY, fixed for the whole scene: seen from the hall doorway, the bay window is straight ahead on the far wall, the fireplace and mantel are on the RIGHT-hand wall, "
       "the sofa is on the LEFT facing the fire, and the rug lies in the open middle between them. The hall doorway is behind the viewer, and the daughter comes in through it. "
       "Small jigsaw pieces lie scattered on the rug; the jigsaw box is " + BOX + ". Nothing in the room moves except the people.")
STATIC = "no sliding, no gliding, no drifting across the floor, no feet skating, no body moving without the feet stepping, no camera push, no zoom"
NEG_BOX = "no picture on the jigsaw box, no writing or logo on the box, no box changing colour or size"
PLACE_L = PLACE("her front living room — the bay window, the tiled fireplace and mantel, the armchair, the floral sofa and the rug")

SHOTS = []

SHOTS.append(dict(
    beat="HKE-SH01", kind="broll", duration=4, line="", subject_motion="in_place",
    files=["N", "L-LIVING", "OUT-N-HE"], audios=[],
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", "the outfit on the info card")), ("@image2", PLACE_L), ("@image3", CARD_N)]),
        SERIES, LOOK, INHERIT, ROOM, GEO,
        "THE SHOT: a full-length shot from high, three-quarter on, looking down from just inside the hall doorway: Her, " + HER_ID + ", in " + HER_OUT + ", kneels on the rug in the middle of the room, "
        "small and low in the frame, the floral sofa on the left of frame and the fireplace on the right.",
        "She is kneeling on both knees, sitting back a little, the open jigsaw box on the rug in front of her. Slowly, piece by piece, she picks up one jigsaw piece at a time from the rug with her right hand and drops it into the box. "
        "Her knees stay on the rug the whole clip.",
        F2, PHYS,
        state("HER", "calm and absorbed, bob and fringe in place, cardigan open, kneeling on the rug picking up jigsaw pieces into the box", "a few more pieces are in the box"),
        "FOCUS: everything from the doorway to the bay window is in sharp focus; everything from near to far stays sharp. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, NEG_BOX, "no standing up in this shot, no other people, no talking, no mouth moving", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "she stands up too early", "prevented_by": "'knees stay on the rug the whole clip', 'no standing up in this shot'"},
           {"risk": "the box shows a printed picture or text", "prevented_by": "plain sky-blue box, box negatives (HT18)"},
           {"risk": "the room layout drifts", "prevented_by": "GEOGRAPHY block with left/right (HT22)"}]))

L14 = "Mum, wait, I’ll give you a…"
SHOTS.append(dict(
    beat="HKE-SH02", kind="dialogue", duration=4, line=L14, subject_motion="travels",
    files=["C2", "L-LIVING", "OUT-C2-HE"], audios=["C2"],
    prompt=" ".join([
        manifest([("@image1", SHEET("the daughter", "the outfit on the info card")), ("@image2", PLACE_L), ("@image3", CARD_C2), ("@audio1", VOICE("the daughter"))]),
        SERIES, LOOK, INHERIT, ROOM, GEO,
        "THE SHOT: a medium shot at eye height, three-quarter on, from inside the room by the sofa, looking back toward the hall doorway: the daughter, " + DAU_ID + ", in " + DAU_OUT + ", "
        "comes in through the white-painted doorway on the right of frame.",
        "She takes two quick steps into the room, sees her mother on the floor below frame, and already reaching her right hand down toward her, says quickly: \"" + L14 + "\" "
        "She stops after the two steps, her hand out and low.",
        F2, PHYS,
        "While the line is spoken, the daughter keeps doing one thing with their hands: her right hand reaching down and open toward her mother, at one slow reach through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("THE DAUGHTER", "a little worried, hair in its loose low bun, denim jacket open, coming in from the hall", "she stops two steps in with her hand reaching down"),
        "FOCUS: the nearest eye of the daughter is in sharp focus; the doorway and hall behind her fall to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
        "DIALOGUE (the daughter, verbatim): \"" + L14 + "\" " + VOICE_C2 + " IN THIS MOMENT: she sees her mother on the floor and her reflex is to rescue her. Speaking to her mother, kindly, a little alarmed. "
        "PLAYING: rushes to help her mother. Opens quick and caring; turns on the exact word 'wait', where her hand goes out; exits trailing off on 'a…' as if something has caught her eye. Stress on 'wait'. "
        "VOICE NOW: quick and warm, a touch of alarm, continuing from how the daughter sounded on the previous line, and matching the face in this shot. "
        "UNDER THE LINE: she has done this many times before and expects to do it again, which leaks only through how fast the hand goes out. Played small and true, for a camera close enough to see a thought. Never theatrical, never pushed, never performed to the lens.",
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, "no running, no kneeling down, no grabbing", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "she grabs or kneels instead of reaching", "prevented_by": "two steps then a reach, negatives"},
           {"risk": "the doorway on the wrong side", "prevented_by": "GEOGRAPHY block; the doorway named on the right of this frame"},
           {"risk": "voice drifts from the master", "prevented_by": "VOICE-C2 master as @audio1"}]))

SHOTS.append(dict(
    beat="HKE-SH03", kind="broll", duration=4, line="", subject_motion="in_place",
    files=["N", "C2", "L-LIVING", "OUT-N-HE", "OUT-C2-HE"], audios=[],
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", "the outfit on her info card")), ("@image2", SHEET("the daughter", "the outfit on her info card")), ("@image3", PLACE_L),
                  ("@image4", CARD_N), ("@image5", CARD_C2)]),
        SERIES, LOOK, INHERIT, ROOM, GEO,
        "THE SHOT: a full-length shot from low, in profile, at rug level: Her, " + HER_ID + ", in " + HER_OUT + ", kneels on the rug facing frame right, the jigsaw box held in both hands in front of her; "
        "the daughter's reaching hand and forearm, in the denim sleeve, come in from the top right of frame, open, a little above her.",
        "In one smooth movement over about two seconds, Her plants her right foot flat on the rug, shifts her weight forward over it, and stands straight up from kneeling to full height, "
        "the jigsaw box held in both hands at her waist the whole time — no hand touches the floor, the sofa or any furniture, and she does not take the offered hand. She ends standing upright and steady.",
        F2, PHYS,
        state("HER", "calm, bob and fringe in place, cardigan open, the jigsaw box in both hands", "she rises from kneeling to standing"),
        state("THE DAUGHTER", "reaching, hand open, mostly out of frame", "her hand stays where it is, untaken"),
        "FOCUS: everything in frame is in sharp focus; everything from near to far stays sharp. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, NEG_BOX, "no hands on the floor, no hand on the sofa or furniture, no taking the daughter's hand, no wobble, no stumble, no knees bending backwards, no legs passing through each other, no teleporting to standing, no talking, no mouth moving", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the rise breaks anatomy or teleports", "prevented_by": "one foot planted, weight forward, two seconds, PHYS, anatomy negatives"},
           {"risk": "she uses her hands or takes the offered hand", "prevented_by": "box in both hands the whole time, negatives"},
           {"risk": "box changes", "prevented_by": "plain box, box negatives"}]))

L15 = "...When did that happen?"
SHOTS.append(dict(
    beat="HKE-SH04", kind="dialogue", duration=4, line=L15, subject_motion="still",
    files=["C2", "N", "L-LIVING", "OUT-C2-HE", "OUT-N-HE"], audios=["C2"],
    prompt=" ".join([
        manifest([("@image1", SHEET("the daughter", "the outfit on her info card")), ("@image2", SHEET("Her", "the outfit on her info card")), ("@image3", PLACE_L),
                  ("@image4", CARD_C2), ("@image5", CARD_N), ("@audio1", VOICE("the daughter"))]),
        SERIES, LOOK, INHERIT, ROOM, GEO,
        "THE SHOT: a close-up over Her shoulder onto the daughter: the soft back of Her grey bob and oatmeal cardigan shoulder frame the near left edge, out of focus; "
        "the daughter, " + DAU_ID + ", in " + DAU_OUT + ", faces the camera a step away, her right hand still out in the air where she offered it, now level with her mother's waist.",
        "She stands still, both feet planted, her hand frozen in the air, staring at her mother, and says quietly: \"" + L15 + "\" Her hand stays out through the whole line.",
        F2, PHYS,
        "While the line is spoken, the daughter keeps doing one thing with their hands: her right hand frozen in the air, open, at one still hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("THE DAUGHTER", "stunned, hair in its loose low bun, denim jacket open, right hand still out in the air", "nothing"),
        state("HER", "standing, calm, the jigsaw box in both hands, back to the camera", "nothing"),
        "FOCUS: the nearest eye of the daughter is in sharp focus; Her shoulder in front and the room behind fall to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
        "DIALOGUE (the daughter, verbatim): \"" + L15 + "\" " + VOICE_C2 + " IN THIS MOMENT: she has just watched her mother stand up from the floor on her own and does not understand it. Speaking to her mother, genuinely asking. "
        "PLAYING: questions her mother. Opens a breath of silence, amazed; turns on the exact word 'that', where her brows draw together; exits still holding out the unneeded hand. Stress on 'that'. "
        "VOICE NOW: quiet and wondering, continuing from how the daughter sounded on the previous line, changed only by what she has just seen, and matching the face in this shot. "
        "UNDER THE LINE: she is not needed here any more and is half proud, half lost, which leaks only through her hand staying out a beat too long. Played small and true, for a camera close enough to see a thought. Never theatrical, never pushed, never performed to the lens.",
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, "no dropping the hand before the line ends", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "she reads as sliding (HKB-SH05)", "prevented_by": "F2 locked instead of F1, feet planted, sliding negatives"},
           {"risk": "the hand drops early", "prevented_by": "BUSINESS-LINE: frozen hand, negative"},
           {"risk": "voice drifts from the master", "prevented_by": "VOICE-C2 master as @audio1"}]))

SHOTS.append(dict(
    beat="HKE-SH05", kind="broll", duration=6, line="", vo="L016", subject_motion="in_place",
    files=["N", "L-LIVING", "OUT-N-HE"], audios=[],
    prompt=" ".join([
        manifest([("@image1", SHEET("Her", "the outfit on the info card")), ("@image2", PLACE_L), ("@image3", CARD_N)]),
        SERIES, LOOK, INHERIT, ROOM, GEO,
        "THE SHOT: a medium close-up at eye height, three-quarter on, by the fireplace: Her, " + HER_ID + ", in " + HER_OUT + ", stands at the tiled fireplace on the right-hand wall, the wooden mantel at her shoulder, holding the jigsaw box.",
        "She sets the jigsaw box down flat on the mantel beside the framed photographs with both hands, lets go, then turns her head to her daughter, who is off frame to the left, and gives her a small, dry look — "
        "a slight lift of the eyebrows and the corner of a smile — that holds. Her feet stay planted; she does not walk.",
        F2, PHYS,
        state("HER", "calm, not out of breath, bob and fringe in place, cardigan open, standing at the mantel, the box in her hands", "the box is on the mantel and she gives the look"),
        "FOCUS: the nearest eye of Her is in sharp focus; the room behind falls to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, STATIC, NEG_BOX, "no readable faces in the photographs, no talking, no mouth moving, no walking", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "her mouth moves as if speaking", "prevented_by": "SILENT, 'no talking, no mouth moving', generate_audio false"},
           {"risk": "the look overplayed", "prevented_by": "'small, dry', NEG-DRAMA"},
           {"risk": "the fireplace on the wrong wall", "prevented_by": "GEOGRAPHY block (HT22)"}]))

FILES = {"C2": "cast/C2-DAUGHTER_v1.png", "N": "cast/N-HER_v1.png", "L-LIVING": "plates/L-LIVING_v1.png",
         "OUT-N-HE": "hooks/HKE/OUT-N-HE_v1.png", "OUT-C2-HE": "hooks/HKE/OUT-C2-HE_v1.png"}
AUDIO = {"C2": "voice/C2_voice_master.mp3", "N": "voice/N_voice_master.mp3"}

if __name__ == "__main__":
    for s in SHOTS:
        call = {"beat": s["beat"], "connector": "seedance", "mode": 4, "kind": s["kind"], "prompt": s["prompt"],
                "duration": s["duration"], "resolution": "720p", "aspect_ratio": "9:16", "start_image": None,
                "ingredients_approved": True, "files": [FILES[f] for f in s["files"]],
                "audios": [AUDIO[a] for a in s["audios"]], "generate_audio": bool(s["line"]),
                "dialogue": s["line"] or None, "script_line": s["line"] or None, "pace": "unhurried",
                "subject_motion": s["subject_motion"], "prefer_multi_shots": "false", "generation": s.get("gen", 1),
                "fix_note": s.get("fix"), "user_go": s.get("go"), "risks": s["risks"], "vo": s.get("vo"),
                "taste": ["HT18", "HT22"]}
        (H / f"{s['beat']}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{s['beat']}.prompt.txt").write_text(s["prompt"])
        print(s["beat"], s["duration"], "s", len(s["prompt"]), "chars")
