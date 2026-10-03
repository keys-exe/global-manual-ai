"""Scene 4 — the GP appointment, story day D3 (a weekday morning) — two Seedance 2.5 takes on Kie, ingredients only, no frames
(act map takes SC04-T1, SC04-T2; this build keeps its pre-V7.96 format, PRE_DRAMA — the blocks pasted from Appendix A by ID).
Tony goes in as the face-and-hair crop + his D3 outfit card (HT26); the GP wears her sheet's work clothes on D3, so her sheet goes in whole.
Both takes carry their dialogue on the speakers' confirmed voice masters (Audio1/Audio2). Lengths from the act map: T1 19 s (the act map's 14.9 s is short of the §28H budget for its
34 words — 7 + 5 + 7 s by each line's words), T2 2.0 + 6.4 + 2.6 = 11.0 s → 11 s (18 words + the silent wide). Never trimmed (§24L)."""
import json, importlib.util, sys
from pathlib import Path

H = Path(__file__).parent
B = H.parents[1]
_s = importlib.util.spec_from_file_location("sc01", B / "hooks/SC01/build_takes.py"); S1 = importlib.util.module_from_spec(_s); _s.loader.exec_module(S1)
SERIES, LOOK, INHERIT, F2, PHYS, AUD = S1.SERIES, S1.LOOK, S1.INHERIT, S1.F2, S1.PHYS, S1.AUD
NEG_EQUIP, NEG_MORPH, NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND = S1.NEG_EQUIP, S1.NEG_MORPH, S1.NEG_FILM, S1.NEG_SCENECUT, S1.NEG_DRAMA, S1.NEG_SOUND
manifest, FACE, CARD, VOICE, state, focus, negs, business, dialogue, MULTI_HEAD = (S1.manifest, S1.FACE, S1.CARD, S1.VOICE, S1.state, S1.focus, S1.negs,
    S1.business, S1.dialogue, S1.MULTI_HEAD)
TONY_ID, VOICE_C1 = S1.TONY_ID, S1.VOICE_C1
ROWS = {r["beat"]: r for r in json.load(open(B / "step5/act_map.json"))}
L = {x["id"]: x["line"] for x in json.load(open(B / "work/lines.json")) if str(x.get("id", "")).startswith("L0")}

GP_ID = "a British Indian family doctor of forty-eight, slim and composed, black hair with a few grey threads in a neat low bun, a small dark mole on her left jaw"
GP_D3 = "a navy fine-knit cardigan over a pale-blue blouse buttoned to the collar, charcoal trousers and black flat shoes — exactly her sheet"
TONY_D3 = ("a plain navy zip fleece worn zipped halfway over a grey T-shirt, dark jeans down to his shoes so both knees are covered, "
           "and brown leather shoes — exactly his outfit card")
SHEET_GP = ("is the GP: face, age, hair, build and her work clothes exactly as on this sheet; the sheet's grey backdrop and panels never appear in the clip.")
PLACE = ("is the place: her consulting room at the surgery — the desk against the wall on the LEFT with her computer screen and keyboard, her office chair at it, "
         "the patient chair at the desk's corner, the blue examination couch under the window behind, vertical blinds, the small sink; its walls, furniture and light side exactly as shown.")
VOICE_C5 = ("A British Indian woman of forty-eight from the English Midlands, a family doctor: a calm, measured, warm mid-range voice, clear consonants, an easy professional pace; "
            "kind but brisk, used to giving the same answer many times a day. Natural, never theatrical.")
DAY = ("THE SCENE SO FAR, a weekday morning at the GP surgery, story day D3, one continuous moment: cool overhead light, about 4000K, with grey daylight through the vertical blinds behind; "
       "Tony has come in about his knee. The GP sits in her office chair at the desk; Tony sits in the patient chair at the desk's corner, his hands on his knees. Nobody else is in the room.")
START = ROWS["SC04-SH01"]["start_pos"]
T1_END = START
T2_END = "Tony in the patient chair at the desk's corner looking down at his right knee, the GP at her desk turned to her screen, typing"
GO = "chat: \"confirm and proceed\" (2026-10-03) — SC03 confirmed, on to SC04; Tony's D3 outfit card OUT-C1-D3 waits for the user's Confirm"
NEG_T = ("no work boots, no sweatshirt, no work trousers, no shorts, no bare knees, no knee support, no olive or charcoal top, no stethoscope, no lanyard, no badge, "
         "no white coat, no third person, no patient on the couch, no nurse")
SHOTS = []

SHOTS.append(dict(beat="SC04-T1", kind="multi", covers=["SC04-SH01", "SC04-SH02", "SC04-SH03"], duration=19, subject_motion="still",
    start_pos=START, end_pos=T1_END, line=" ".join([L["L018"], L["L019"], L["L020"]]), files=["C5", "C1-FACE", "L-GP", "OUT-C1-D3"], audios=["C5", "C1"],
    title="Scene 4 · T1 — \"For 64 you’re in decent nick.\" · \"I walk like I’m 85.\" · \"It’s very normal.\" (SH01–SH03)",
    prompt=" ".join([
        manifest([("@image1", SHEET_GP), ("@image2", FACE("Tony", "his")), ("@image3", PLACE),
                  ("@image4", CARD("Tony", "the navy zip fleece over a grey T-shirt, dark jeans, brown leather shoes")),
                  ("@audio1", VOICE("the GP")), ("@audio2", VOICE("Tony"))]),
        SERIES, LOOK, INHERIT, DAY,
        f"The GP is {GP_ID}, in {GP_D3}. Tony is {TONY_ID}, in {TONY_D3}.",
        MULTI_HEAD(3, START, True),
        f"THE EXCHANGE, word for word and in this order: {L['L018']} {L['L019']} {L['L020']} — the GP says the first and third, Tony the second. "
        f"SHOT 1, [0s-7s]: MEDIUM CLOSE-UP on the GP, three-quarter, eye height, the vertical blinds soft behind her: she turns from her screen to Tony, brisk and kind, and says: \"{L['L018']}\" "
        f"SHOT 2, [7s-12s]: MEDIUM CLOSE-UP over the GP's shoulder onto Tony in the patient chair, eye height, her shoulder and bun soft in the near frame: flat, rubbing his right knee with his right hand, he says: \"{L['L019']}\" "
        f"SHOT 3, [12s-19s]: MEDIUM CLOSE-UP on the GP from a little below, three-quarter: reasonable, a small shrug, she says: \"{L['L020']}\" "
        "Each cut lands on a completed line. The eyelines match across every reverse. Nobody looks into the lens. "
        f"Last frame: {T1_END}.",
        F2, PHYS,
        business("Tony", "his right hand rubbing slowly back and forth over his right knee through his jeans"),
        state("TONY", "tired, in the outfit of his card, in the patient chair at the desk's corner, hands on his knees", "nothing"),
        state("THE GP", "composed, in her work clothes, in her office chair at the desk, turned from her screen to Tony", "nothing"),
        focus("the nearest eye of whoever is speaking", "the room behind falls to a soft, recognisable shape"),
        dialogue("the GP", L["L018"] + " … " + L["L020"], VOICE_C5, "she has his results on the screen and many patients after him. Speaking to Tony, across the corner of her desk.",
                 "reassures him and closes the subject. Opens brisk on the results; turns on the exact words 'very normal', where her voice softens and settles it; exits kind and final. Stress on 'normal'.",
                 "calm, warm, unhurried, the same level from her first line to her last, matching the face in this shot.",
                 "she has said this many times today, which leaks only through the small shrug before the last line."),
        dialogue("Tony", L["L019"], VOICE_C1, "he has come to be told something can be done. Speaking to the GP, flat.",
                 "pushes back without raising his voice. Opens flat; turns on the exact words 'like I'm 85', where his voice drops; exits quiet. Stress on '85'.",
                 "low, rough and flat, matching the face in this shot.",
                 "he is ashamed to be saying it, which leaks only through his eyes going to his knee as he speaks."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, NEG_T, "no Tony saying the GP's lines, no GP saying Tony's line, no one standing up, no examination, no hands on his knee but his own", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the voices swap or the wrong person speaks a line", "prevented_by": "Audio1 the GP, Audio2 Tony, every line named with its speaker, swap negatives"},
           {"risk": "the sheet clothes return on Tony", "prevented_by": "face crop + D3 outfit card, clothing negatives (HT26)"},
           {"risk": "the room changes between reverses", "prevented_by": "the plate, STILL head, the desk on the left named in every shot, same light"}]))

SHOTS.append(dict(beat="SC04-T2", kind="multi", covers=["SC04-SH04", "SC04-SH05", "SC04-SH06"], duration=11, subject_motion="still",
    start_pos=T1_END, end_pos=T2_END, line=" ".join([L["L021"], L["L022"]]), files=["C5", "C1-FACE", "L-GP", "OUT-C1-D3"], audios=["C5", "C1"],
    title="Scene 4 · T2 — \"It’s not normal.\" · \"Keep moving… paracetamol.\" · Tony looks at his knee (SH04–SH06)",
    prompt=" ".join([
        manifest([("@image1", SHEET_GP), ("@image2", FACE("Tony", "his")), ("@image3", PLACE),
                  ("@image4", CARD("Tony", "the navy zip fleece over a grey T-shirt, dark jeans, brown leather shoes")),
                  ("@audio1", VOICE("the GP")), ("@audio2", VOICE("Tony"))]),
        SERIES, LOOK, INHERIT, DAY.replace("Tony has come in about his knee.", f"Tony has come in about his knee; the GP has just told him: \"{L['L020']}\""),
        f"The GP is {GP_ID}, in {GP_D3}. Tony is {TONY_ID}, in {TONY_D3}.",
        MULTI_HEAD(3, T1_END, True),
        f"THE EXCHANGE, word for word and in this order: {L['L021']} {L['L022']} — Tony says the first, the GP the second; then nobody speaks. "
        f"SHOT 1, [0s-2s]: CLOSE-UP on Tony, front-on, eye height: quiet, not accepting it, he says: \"{L['L021']}\" "
        f"SHOT 2, [2s-8.5s]: MEDIUM on the GP in clean profile at her desk, eye height: she turns back to her screen and types as she says: \"{L['L022']}\" "
        "SHOT 3, [8.5s-11s]: WIDE from high in the corner of the room, three-quarter: Tony sits in the patient chair looking down at his right knee while the GP types at her desk; nobody speaks. "
        "Each cut lands on a completed line or a held look. Nobody looks into the lens. "
        f"Last frame: {T2_END}.",
        F2, PHYS,
        business("the GP", "typing on her keyboard, her eyes on the screen"),
        state("TONY", "flat and shut out, in the outfit of his card, in the patient chair at the desk's corner, hands on his knees", "he looks down at his right knee at the end"),
        state("THE GP", "composed, in her work clothes, in her office chair, turned back to her screen", "she is typing"),
        focus("the nearest eye of whoever is speaking", "in the wide, both of them are sharp and the room falls soft"),
        dialogue("Tony", L["L021"], VOICE_C1, "the GP has just called his knee very normal. Speaking to her, quiet.",
                 "refuses it. One flat statement; turns on the exact word 'not', where his voice drops; exits quiet. Stress on 'not'.",
                 "low, rough and quiet, continuing from how Tony sounded on his last line, matching the face in this shot.",
                 "he knows she will not change her answer, which leaks only through his eyes staying on her."),
        dialogue("the GP", L["L022"], VOICE_C5, "she has given her answer and is writing it up. Speaking to Tony while typing, not looking at him.",
                 "closes the appointment. Opens brisk; turns on the exact word 'paracetamol', said like a routine; exits on 'most people', kind and final. Stress on 'most'.",
                 "calm and even, continuing from how the GP sounded on her last line, matching the face in this shot.",
                 "she is already on to the next patient, which leaks only through her eyes staying on the screen."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, NEG_T, "no Tony saying the GP's line, no GP saying Tony's line, no one standing up, no talking in the wide, no examination", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the voices swap or the wrong person speaks a line", "prevented_by": "Audio1 the GP, Audio2 Tony, every line named with its speaker, swap negatives"},
           {"risk": "someone speaks in the silent wide", "prevented_by": "'nobody speaks' in SHOT 3, no-talking-in-the-wide negative"},
           {"risk": "the sheet clothes return on Tony", "prevented_by": "face crop + D3 outfit card, clothing negatives (HT26)"}]))

FILES = {"C5": "cast/C5-GP_v1.png", "C1-FACE": "voice/C1_face.jpg", "L-GP": "plates/L-GP_v1.png", "OUT-C1-D3": "body/SC04/ingredients/OUT-C1-D3_v2.png"}
AUDIO = {"C1": "voice/C1_voice_master.mp3", "C5": "voice/C5_voice_master.mp3"}

if __name__ == "__main__":
    approved = "--approved" in sys.argv
    for s in SHOTS:
        call = {"beat": s["beat"], "build": "stryde-her-dad", "connector": "seedance", "model": "bytedance/seedance-2-5", "mode": 4, "kind": s["kind"], "prompt": s["prompt"],
                "take": s["beat"], "covers": s["covers"], "start_pos": s["start_pos"], "end_pos": s["end_pos"], "duration": s["duration"], "resolution": "720p",
                "aspect_ratio": "9:16", "start_image": None, "ingredients_approved": approved, "files": [FILES[f] for f in s["files"]],
                "audios": [AUDIO[a] for a in s["audios"]], "generate_audio": True, "dialogue": s["line"], "script_line": s["line"],
                "pace": "unhurried", "subject_motion": s["subject_motion"], "prefer_multi_shots": "false", "generation": 1, "user_go": GO, "legacy_build": True,
                "risks": s["risks"], "scene": 4, "title": s["title"], "taste": ["HT02", "HT17", "HT18", "HT22", "HT23", "HT26", "HT27"]}
        (H / f"{s['beat']}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{s['beat']}.prompt.txt").write_text(s["prompt"])
        print(s["beat"], s["duration"], "s", len(s["prompt"]), "chars")
