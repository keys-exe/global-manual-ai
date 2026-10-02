"""Scene 4 (the wedding, story day B4) — SEEDANCE 2.5 takes on Kie AI, ingredients only, no frames.
Planned as two takes (§24K part 5, V7.88.0), as the user asked on Scene 3 ("make it in one video so it is a continuous one",
"the 9 and 10 too"): T1 = SH01+SH02 (Barbara dancing, MULTI-SHOT MOVE, silent — VO L030 laid in the edit);
T2 = SH03–SH05 (at their table, one-take: L031 · L032 · L033, then the push-in held under VO L034).
Ingredient cards confirmed by the user ("confirmed", 2026-10-02): OUT-N-B4 v2, OUT-C3-B4 v2, OUT-C1-B4 v2, INFO-WEDDING.
Faces go in as face-and-hair crops (HT26/L21/L28) — the day's clothes come only from the outfit cards.
The plate L-WEDDING is shot from the edge of the floor: their table is the plate's near-left table (L17: the plate's own side)."""
import json
import sys
import importlib.util
from pathlib import Path

H = Path(__file__).parent
B = H.parents[1]
_spec = importlib.util.spec_from_file_location("sc03_clips", B / "body" / "SC03" / "build_clips.py")
S3 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(S3)
SERIES, LOOK, INHERIT, F2, F1, PHYS, AUD, SILENT = S3.SERIES, S3.LOOK, S3.INHERIT, S3.F2, S3.F1, S3.PHYS, S3.AUD, S3.SILENT
NEG_EQUIP, NEG_MORPH, NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND = S3.NEG_EQUIP, S3.NEG_MORPH, S3.NEG_FILM, S3.NEG_SCENECUT, S3.NEG_DRAMA, S3.NEG_SOUND
VOICE_N, HER_ID, HUS_ID, VOICE_C3 = S3.VOICE_N, S3.HER_ID, S3.HUS_ID, S3.VOICE_C3
manifest, PLACE, VOICE, state, negs, dialogue = S3.manifest, S3.PLACE, S3.VOICE, S3.state, S3.negs, S3.dialogue

BARB_ID = "an upright, sturdy woman of seventy-four with a short tousled white-grey crop and brown eyes"
HER_B4 = ("a dusty-rose silk-chiffon midi dress with flowing elbow-length sleeves and a thin self-fabric belt, sheer nude tights, "
          "nude satin low-heeled courts and pearl drop earrings — exactly her outfit card, no jacket")
HUS_B4 = "a navy two-piece suit, a pale-blue shirt and a plain dark-burgundy tie — exactly his outfit card"
BARB_B4 = ("a royal-blue lace midi dress with sheer lace three-quarter sleeves and a skirt that swings, silver satin low-heeled shoes "
           "and a fine silver necklace — exactly her outfit card, no cardigan")
BRIDE = "the bride, about twenty-five, light-brown hair pinned up with a sprig of white gypsophila, in the simple ivory dress of her card"
FACE = lambda who: f"is {who}: face and hair only, a close crop — her clothes come from the outfit card, never from this picture.".replace(
    "her clothes", "his clothes" if who.startswith("the husband") else "her clothes")
CARD = lambda who, outfit: (f"is an info card: {who}'s outfit on this day — {outfit}; follow it exactly, and its caption strip and any text on it never appear in the clip.")
WEDDING = PLACE("the wedding reception room of a country hotel, seen from the edge of the dance floor — the parquet dance floor in the middle, the looped fairy lights and the chandelier "
                "overhead, round white-clothed tables with ivory chair covers and candle jars around it, the small stage with the DJ desk at the back right; "
                "their own table is the round table in the near left of this view")
WEDDING_EVE = ("THE SCENE SO FAR, a June evening at her granddaughter's wedding reception, one continuous evening: the fairy lights and candle jars are lit, warm 2700K, "
               "the tall windows dark blue behind the curtains. The parquet floor is full of guests dancing; Barbara, in the outfit of her card, dances in the middle of it, "
               "the bride in ivory dancing near her. Her and her husband, each in the outfit of their card, sit at their round table in the near left of the room, "
               "at the edge of the floor: Her on the right-hand chair of that table, turned toward the floor, her husband on the chair to her left, his pint of bitter on the cloth "
               "in front of him. Nobody at their table dances.")
NOMUS = "The guests dance to a beat that is laid in later in the edit; no music, no score in this clip."
GUESTS = "The other guests are ordinary wedding guests in suits and summer dresses, soft and never in focus long enough to read a face."
L031 = "Her knees were worse than mine. Both of them. Bone on bone."
L032 = "Whose?"
L033 = "Barbara’s."
GO = "chat: \"confirmed\" (2026-10-02) — the SC04 ingredient cards confirmed; SC04 as two takes, as asked on SC03"

T1_START = ("Barbara dances in the middle of the parquet floor among the guests, mid-step, facing the camera, arms loose; the bride in ivory dances beside her on her left; "
            "the near-left table with its candle jar, glasses and flowers soft in the foreground; nobody at that table")
T1_END = ("Barbara has turned once on the beat and faces the camera again, knees bent, laughing, in the middle of the floor where she started; the bride still dancing just behind her")
T2_START = ("Her sits on the right-hand chair of the near-left table in clean profile facing RIGHT, toward the dance floor, her hands in her lap; her husband sits on the chair to her left, "
            "nearer the camera, his face in three-quarter turned toward her, his right hand round his pint on the cloth; Barbara dances soft in the background on the floor")
T2_END = ("a close shot of Her's face in profile facing RIGHT, still watching the dance floor, the fairy-light glow moving on her cheek; her husband's shoulder soft at the left edge of frame")

SHOTS = []
SHOTS.append(dict(beat="SC04-T1", take="SC04-T1", kind="multi", covers=["SC04-SH01", "SC04-SH02"], duration=10, line="", vo="L030", subject_motion="in_place",
    start_pos=T1_START, end_pos=T1_END,
    files=["C1-FACE", "L-WEDDING", "OUT-C1-B4", "INFO-WEDDING"], audios=[],
    title="Scene 4 · T1 — Barbara on the dance floor (SH01 + SH02)",
    prompt=" ".join([
        manifest([("@image1", FACE("Barbara")), ("@image2", WEDDING), ("@image3", CARD("Barbara", "the royal-blue lace midi dress, silver satin shoes, silver necklace")),
                  ("@image4", "is a character card for a one-off extra: the bride in her simple ivory dress; copy her look, and its caption strip never appears in the clip.")]),
        SERIES, LOOK, INHERIT, WEDDING_EVE, GUESTS,
        "Nobody speaks and nobody sings; every mouth is closed or laughing silently.",
        "One scene covered in 2 shots within a single take, all on the same side of the action line, with the same light, look and wardrobe throughout. Frame 1: " + T1_START + ". "
        "The action carries straight across every cut: each shot picks up the movement exactly where the last one left it — the same step, the same hand, the same direction — and everyone is where the last shot left them. "
        f"SHOT 1, [0s-5s]: WIDE, exactly the view of Image2 from the edge of the dance floor, the near-left table soft in the foreground; Camera on a tripod, locked: Barbara, {BARB_ID}, in {BARB_B4}, "
        f"dances in the middle of the parquet floor among the guests, easy and strong, stepping side to side on the beat; {BRIDE} dances beside her and laughs with her. "
        "SHOT 2, [5s-10s]: MEDIUM, low at hip height, Barbara three-quarter to the camera: carrying straight on from her step, she bends her knees, turns once right round on the beat, "
        "her skirt swinging out, and comes back facing us, laughing, her hands up at shoulder height; the fairy lights soft above her. "
        "Each cut lands on a completed step. Nobody looks into the lens. Last frame: " + T1_END + ".",
        F2, PHYS, NOMUS,
        state("BARBARA", "joyful, in the outfit of her card, dancing in the middle of the floor", "she has turned once and faces us again, knees bent, laughing"),
        "FOCUS: SHOT 1 deep, the whole floor sharp, the foreground table soft; SHOT 2 Barbara sharp, the guests behind soft. The blur is optical: soft and round, never smeared.",
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, "no cardigan, no gilet, no knee brace on Barbara, no walking stick, no falling, no stumbling, no bride's veil, no words on banners", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "Barbara in her cast-sheet gilet or a cardigan", "prevented_by": "face-and-hair crop only, the lace-dress card, cardigan/gilet negatives (HT26)"},
           {"risk": "the second shot restarts the dance", "prevented_by": "MULTI-FILM MOVE: SHOT 2 picks up her step, start and end positions written"},
           {"risk": "generated music under the dance", "prevented_by": "silent call, NOMUS, NEG-SOUND"}]))

SHOTS.append(dict(beat="SC04-T2", take="SC04-T2", kind="take", covers=["SC04-SH03", "SC04-SH04", "SC04-SH05"], duration=14, line=L031 + " " + L032 + " " + L033, vo="L034",
    subject_motion="still", start_pos=T2_START, end_pos=T2_END,
    files=["N-FACE", "C3-FACE", "L-WEDDING", "OUT-N-B4", "OUT-C3-B4", "OUT-C1-B4"], audios=["N", "C3"],
    title="Scene 4 · T2 — \"Bone on bone.\" · \"Whose?\" · \"Barbara’s.\" (SH03–SH05, one take)",
    prompt=" ".join([
        manifest([("@image1", FACE("Her")), ("@image2", FACE("the husband")), ("@image3", WEDDING),
                  ("@image4", CARD("Her", "the dusty-rose silk-chiffon midi dress, nude satin courts, pearl drops — no jacket")),
                  ("@image5", CARD("the husband", "the navy suit, pale-blue shirt and burgundy tie")),
                  ("@image6", CARD("Barbara", "the royal-blue lace midi dress — she is only ever soft in the background here")),
                  ("@audio1", VOICE("Her")), ("@audio2", VOICE("the husband"))]),
        SERIES, LOOK, INHERIT, WEDDING_EVE, GUESTS,
        "One continuous shot, never cut and never restarted, 14s, in one place with the same light, look and wardrobe throughout. Frame 1: " + T2_START + ". "
        f"Her is {HER_ID}, in {HER_B4}. Her husband is {HUS_ID}, in {HUS_B4}. "
        "THE EXCHANGE, word for word and in this order: " + L031 + " " + L032 + " " + L033 + " — she says the first line, he asks the second, she answers the third; nobody else speaks. "
        "[0s-1s]: she watches the dance floor, the fairy-light glow moving on her face. "
        "[1s-6s]: never taking her eyes off Barbara on the floor, she says it low to him: \"" + L031 + "\" "
        "[6s-8s]: carrying straight on, he leans in toward her a little, his pint still in his hand, and asks quietly: \"" + L032 + "\" "
        "[8s-10s]: without looking at him, still watching the floor, she answers: \"" + L033 + "\" "
        "[10s-14s]: she keeps watching the dance floor in silence, her mouth closed, a slow thought on her face. Last frame: " + T2_END + ". "
        "The movement is continuous from the first frame to the last: nobody jumps position or appears somewhere new, and the room behind them stays the same room.",
        F1(80), PHYS, NOMUS,
        "While the lines are spoken, Her keeps doing one thing with their hands: her hands resting together in her lap, at one steady hold through the line. It is ordinary and unhurried, and the hands never stop to gesture.",
        state("HER", "watchful, in the outfit of her card, seated at the near-left table, watching Barbara dance", "nothing — she is still watching, quietly shaken"),
        "FOCUS: her nearest eye is in sharp focus throughout; her husband is a little soft, the dance floor behind soft and glowing. The blur is optical: soft and round, never smeared.",
        dialogue("Her", L031 + " … " + L033, VOICE_N, "she has just seen her cousin dancing on knees she knows are worse than her own. Speaking low to her husband beside her, watching the dance floor, never him.",
                 "realises, out loud, half to herself. Opens low and level; turns on 'Bone on bone', where her voice drops; exits still watching the floor. Stress on 'worse'.",
                 "low and quiet under the party, a little stunned, matching the face in this shot.",
                 "if Barbara can dance on knees like that, her own story about her knees may be wrong, which leaks only through how still she goes."),
        dialogue("the husband", L032, VOICE_C3, "he has half-heard her over the party. Leaning in to his wife.", "asks simply. One word, quiet. Stress on 'Whose'.",
                 "soft and gruff, a little loud over the room then dropping.", "he has not noticed what she has."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, "no cut, no second camera angle, no looking at the camera, no eyes to the lens, no jacket on her, no cardigan, no green jumper, no standing up, no dancing at their table, no husband saying her lines", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the model cuts or restarts inside the take", "prevented_by": "TAKE-FILM, both positions written, NEG-SCENECUT, no-cut negative"},
           {"risk": "the voices swap", "prevented_by": "Audio1 Her, Audio2 the husband, every line named with its speaker, 'no husband saying her lines'"},
           {"risk": "she looks at him or the lens instead of the floor", "prevented_by": "profile facing RIGHT toward the floor, 'without looking at him', lens negatives (L22)"},
           {"risk": "the cast-sheet clothes return (L21)", "prevented_by": "face crops only, the two v2 outfit cards, jacket/cardigan/jumper negatives"}]))

FILES = {"N-FACE": "cast/N-HER_face.png", "C3-FACE": "cast/C3-HUSBAND_face.png", "C1-FACE": "cast/C1-BARBARA_face.png", "L-WEDDING": "plates/L-WEDDING_v1.png",
         "OUT-N-B4": "body/SC04/ingredients/OUT-N-B4_v2.png", "OUT-C3-B4": "body/SC04/ingredients/OUT-C3-B4_v1.png",
         "OUT-C1-B4": "body/SC04/ingredients/OUT-C1-B4_v2.png", "INFO-WEDDING": "body/SC04/ingredients/INFO-WEDDING_v1.png"}
AUDIO = {"N": "voice/N_voice_master.mp3", "C3": "voice/C3_voice_master.mp3"}

if __name__ == "__main__":
    only = sys.argv[1:]
    for s in SHOTS:
        if only and s["beat"] not in only:
            continue
        call = {"beat": s["beat"], "build": "stryde-half-my-age", "connector": "seedance", "model": "bytedance/seedance-2-5", "mode": 4, "kind": s["kind"], "prompt": s["prompt"],
                "take": s["take"], "covers": s["covers"], "start_pos": s["start_pos"], "end_pos": s["end_pos"],
                "duration": s["duration"], "resolution": "720p", "aspect_ratio": "9:16", "start_image": None,
                "ingredients_approved": True, "files": [FILES[f] for f in s["files"]], "audios": [AUDIO[a] for a in s["audios"]],
                "generate_audio": bool(s["line"]), "dialogue": s["line"] or None, "script_line": s["line"] or None, "pace": "unhurried",
                "subject_motion": s["subject_motion"], "prefer_multi_shots": "false", "generation": s.get("gen", 1), "user_go": GO,
                "risks": s["risks"], "vo": s.get("vo"), "scene": 4, "title": s["title"],
                "taste": ["HT02", "HT17", "HT18", "HT22", "HT23", "HT24", "HT26"]}
        (H / f"{s['beat']}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{s['beat']}.prompt.txt").write_text(s["prompt"])
        print(s["beat"], s["duration"], "s", len(s["prompt"]), "chars")
