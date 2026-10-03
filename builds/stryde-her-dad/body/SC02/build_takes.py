"""Scene 2 — the car, straight after the car park, story day D1 — four Seedance 2.5 takes on Kie AI, ingredients only, no frames
(act map step5/act_map.json, takes SC02-T1..T4). Film blocks and helpers come from hooks/SC01/build_takes.py (Appendix A by ID).
Ingredients all confirmed: face-and-hair crops + D1 outfit cards (HT26), the L-CAR plate, the voice masters of Tony and Sue.
Sue's inner VO L006 is laid in the edit over SH01 (VO-T1-L006); her mouth stays closed there. Durations: the act map's
11.4 / 12.9 / 11.4 / 6.3 s rounded up to the §28H word budget of each take's lines — 12 / 15 / 14 / 7 s (Mode 4 never trimmed, §24L)."""
import json, sys, importlib.util
from pathlib import Path

H = Path(__file__).parent
B = H.parents[1]
_spec = importlib.util.spec_from_file_location("sc01", B / "hooks/SC01/build_takes.py")
S1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(S1)
(SERIES, LOOK, INHERIT, F2, F1, PHYS, AUD, SILENT, NEG_EQUIP, NEG_MORPH, NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND) = (
    S1.SERIES, S1.LOOK, S1.INHERIT, S1.F2, S1.F1, S1.PHYS, S1.AUD, S1.SILENT, S1.NEG_EQUIP, S1.NEG_MORPH, S1.NEG_FILM,
    S1.NEG_SCENECUT, S1.NEG_DRAMA, S1.NEG_SOUND)
manifest, FACE, CARD, VOICE, state, focus, business, negs, dialogue, MULTI_HEAD = (
    S1.manifest, S1.FACE, S1.CARD, S1.VOICE, S1.state, S1.focus, S1.business, S1.negs, S1.dialogue, S1.MULTI_HEAD)
TONY_ID, SUE_ID, TONY_D1, SUE_D1, VOICE_C1, VOICE_C2 = S1.TONY_ID, S1.SUE_ID, S1.TONY_D1, S1.SUE_D1, S1.VOICE_C1, S1.VOICE_C2
LN = {r["id"]: r["line"] for r in json.load(open(B / "work/lines.json"))}

PLACE = ("is the place: inside their ordinary ten-year-old silver five-door hatchback, a British right-hand-drive car, parked in the garden-centre car park — the charcoal cloth front seats, "
         "the steering wheel on the RIGHT, a plain dashboard with a parking ticket and sunglasses on it, the windscreen onto the wet grey car park and the green glass front of the garden centre; "
         "its seats, dashboard, windows and light side exactly as shown.")
DAY = ("THE SCENE SO FAR, the same wet Saturday midday, a minute after the near miss, one continuous moment: flat grey overcast through the windscreen, about 6500K, rain on the glass; "
       "inside the car it is quiet and a little dim. Sue sits in the DRIVER'S seat on the RIGHT, behind the steering wheel; Tony sits in the PASSENGER seat on the LEFT. Both face the windscreen. "
       "The car key is in the ignition, not turned; the engine is off. Tony's right trouser knee is dark and wet with a smear of grit from the tarmac. Nobody else is in the car.")
SEATS = ("Sue is always on the RIGHT in the driver's seat behind the wheel, Tony always on the LEFT in the passenger seat; they never swap seats, the wheel never moves to the left, "
         "and the car stays parked and still.")
NEG_CAR = ("no car moving, no engine running before the key turns, no left-hand-drive car, no steering wheel on the left, no Sue in the passenger seat, no Tony driving, "
           "no seatbelt changes, no shorts, no bare knees, no camel coat, no third person in the car, no one outside the car close to the windows")
START = ("Sue in the driver's seat (right), hands on the wheel; Tony in the passenger seat (left), his trouser knee dirty from the tarmac, both facing the windscreen")
GO = "chat: \"confirm and proceed\" (2026-10-03) — SC01 confirmed, on to SC02; every ingredient already confirmed"
ING = [("@image1", FACE("Sue", "her")), ("@image2", FACE("Tony", "his")), ("@image3", PLACE),
       ("@image4", CARD("Sue", "the navy quilted jacket open over a white T-shirt, light jeans, white trainers")),
       ("@image5", CARD("Tony", "the charcoal sweatshirt, navy work trousers to the boots, tan work boots")),
       ("@audio1", VOICE("Sue")), ("@audio2", VOICE("Tony"))]
FILES = ["C2-FACE", "C1-FACE", "L-CAR", "OUT-C2-D1", "OUT-C1-D1"]
WHO = f"Sue is {SUE_ID}, in {SUE_D1}. Tony is {TONY_ID}, in {TONY_D1}."
RHYTHM = "The lines land on each other in the rhythm this scene needs: {r}. Each cut lands on a completed line, action or reaction. The eyelines match across every reverse. Nobody looks into the lens."


def exchange(ids):
    return "THE EXCHANGE, word for word and in this order: " + " ".join(LN[i] for i in ids) + " — "


def take(beat, covers, dur, ids, who_says, shots, rhythm, sue_hands, tony_hands, sue_state, tony_state, dlg, end, extra_neg="", start=START, audios=("C2", "C1"), title=""):
    line = " ".join(LN[i] for i in ids)
    p = " ".join([
        manifest(ING if "C1" in audios and "C2" in audios else [x for x in ING if not x[0].startswith("@audio")] + [("@audio1", VOICE("Tony" if audios[0] == "C1" else "Sue"))]),
        SERIES, LOOK, INHERIT, DAY, WHO, SEATS,
        MULTI_HEAD(len(shots), start, True),
        exchange(ids) + who_says + ". " + " ".join(f"SHOT {n + 1}, [{a}]: {t}" for n, (a, t) in enumerate(shots)),
        RHYTHM.format(r=rhythm) + " Last frame: " + end + ".",
        F2, PHYS,
        business("Sue", sue_hands), business("Tony", tony_hands),
        state("SUE", sue_state[0], sue_state[1]), state("TONY", tony_state[0], tony_state[1]),
        focus("the nearest eye of whoever is speaking", "the windscreen and the car park behind fall to a soft, recognisable shape"),
        *dlg, AUD,
        negs(NEG_EQUIP, NEG_MORPH, NEG_CAR, extra_neg, NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)])
    return dict(beat=beat, kind="multi", covers=covers, duration=dur, line=line, start_pos=start, end_pos=end, files=FILES, audios=list(audios),
                subject_motion="still", prompt=p, title=title)


END4 = "both facing the windscreen, Sue's hand on the key"
SHOTS = []
SHOTS.append(take("SC02-T1", ["SC02-SH01", "SC02-SH02", "SC02-SH03"], 12, ["L007", "L008"], "Sue asks the first, Tony answers with the second",
    [("0s-5s", "MEDIUM CLOSE-UP of Sue in clean profile, eye height, from the passenger side past Tony's shoulder, soft; Camera on a tripod, locked: Sue sits with both hands on the wheel, "
               "the key in the ignition not turned, staring ahead through the rain on the windscreen; her mouth stays closed — this is her silent thought, nobody speaks."),
     ("5s-8.5s", "MEDIUM CLOSE-UP on Sue, three-quarter, eye height: she turns her head to Tony and asks, quiet and level: \"" + LN["L007"] + "\""),
     ("8.5s-12s", "MEDIUM CLOSE-UP on Tony, three-quarter, eye height, from the driver's side: he keeps looking out of the windscreen, not at her, and says flatly: \"" + LN["L008"] + "\"")],
    "a long held silence first, then her question, a beat, then his answer", "both hands resting on the steering wheel at ten and two, still", "his hands resting on his thighs, still",
    ("shaken, in the outfit of her card, in the driver's seat, both hands on the wheel", "she has turned her head to him"),
    ("shut, in the outfit of his card, in the passenger seat, his right trouser knee wet and gritty", "nothing — he still faces the windscreen"),
    [dialogue("Sue", LN["L007"], VOICE_C2, "she has just watched her husband fall in front of a stranger. Speaking to Tony beside her, careful.",
              "presses Tony. Opens quiet and level; turns on the exact word 'talk', where her voice firms; exits waiting. Stress on 'talk'.",
              "quiet, low, steady with effort, continuing from her silence, and matching the face in this shot.", "she is frightened, which leaks only through her hands tightening on the wheel."),
     dialogue("Tony", LN["L008"], VOICE_C1, "he is humiliated and will not look at her. Speaking to Sue without turning his head.",
              "deflects Sue. Opens flat; turns on the exact word 'want', where his voice drops; exits shut. Stress on 'want'.",
              "low, rough and flat, continuing from how Tony sounded in the car park, and matching the face in this shot.", "he knows exactly what she wants, which leaks only through his jaw setting.")],
    START, extra_neg="no Sue speaking in the first five seconds, no mouth moving on Sue before her line", title="Scene 2 · T1 — Sue at the wheel; \"Are we going to talk about it?\" · \"What do you want me to say?\" (SH01–SH03)"))

SHOTS.append(take("SC02-T2", ["SC02-SH04", "SC02-SH05", "SC02-SH06"], 15, ["L009", "L010", "L011"], "Sue says the first, Tony the second, Sue the third",
    [("0s-7s", "MEDIUM CLOSE-UP over Tony's left shoulder onto Sue, eye height, his shoulder soft in the near frame; Camera on a tripod, locked: Sue, at him, her voice tight: \"" + LN["L009"] + "\" — she stops before the end of the sentence and cannot finish it."),
     ("7s-10.5s", "CLOSE-UP on Tony from a little below, front-on through the windscreen side: quiet, still facing ahead: \"" + LN["L010"] + "\""),
     ("10.5s-15s", "CLOSE-UP on Sue, three-quarter, eye height: flat, looking straight at him: \"" + LN["L011"] + "\"")],
    "her line breaking off, a beat, his quiet answer, a beat held on her, then her flat reply", "her right hand still on the wheel, her left hand in her lap", "his hands resting on his thighs, still",
    ("angry and frightened, in the outfit of her card, in the driver's seat, turned toward him", "nothing"),
    ("shut, in the outfit of his card, in the passenger seat facing the windscreen, his right trouser knee wet and gritty", "nothing"),
    [dialogue("Sue", LN["L009"] + " … " + LN["L011"], VOICE_C2, "the fear of what nearly happened has turned into anger. Speaking to Tony, close, in the car.",
              "confronts Tony. Opens tight and quick; turns on the exact word 'Tony', where her voice catches and stops; exits flat and cold on the second line. Stress on 'something'.",
              "tight, clipped, a little shaky, continuing from her question a moment ago, and matching the face in this shot.", "she cannot say 'you'd have watched me die', which leaks only through the sentence stopping."),
     dialogue("Tony", LN["L010"], VOICE_C1, "he cannot admit it. Speaking to Sue without looking at her.",
              "insists to Sue. Opens quiet; turns on the exact word 'got', where his voice goes rough; exits shut. Stress on 'got'.",
              "low, quiet and rough, continuing from his last line, and matching the face in this shot.", "he does not believe it himself, which leaks only through a swallow.")],
    START, title="Scene 2 · T2 — \"…if that lad hadn’t been there, Tony…\" · \"I’d have got to you.\" · \"You didn’t make it one step.\" (SH04–SH06)"))

SHOTS.append(take("SC02-T3", ["SC02-SH07", "SC02-SH08", "SC02-SH09"], 14, ["L012", "L013", "L014"], "Sue says the first, Tony the second, Sue the third",
    [("0s-6s", "MEDIUM CLOSE-UP over Tony's left shoulder onto Sue, eye height; Camera on a tripod, locked: her eyes wet, holding it together: \"" + LN["L012"] + "\""),
     ("6s-8.5s", "MEDIUM CLOSE-UP of Tony in clean profile, eye height, from the driver's side: jaw set, facing the windscreen: \"" + LN["L013"] + "\""),
     ("8.5s-14s", "CLOSE-UP on Sue, front-on, eye height, from the dashboard: quietly, the line that lands: \"" + LN["L014"] + "\"")],
    "her plea, his fast hard answer cutting in, a held beat, then her quiet question", "her hands in her lap, still", "his hands resting on his thighs, his right hand closing into a loose fist on his knee",
    ("eyes wet but no tears falling, in the outfit of her card, in the driver's seat, turned toward him", "nothing"),
    ("hurt and hard, in the outfit of his card, in the passenger seat facing the windscreen, his right trouser knee wet and gritty", "nothing"),
    [dialogue("Sue", LN["L012"] + " … " + LN["L014"], VOICE_C2, "she is scared of the life ahead. Speaking to Tony beside her.",
              "pleads with Tony. Opens thick and quiet; turns on the exact word 'chair', where her voice nearly goes; exits very quiet on the last line. Stress on 'dad'.",
              "quiet, thick with held tears, continuing from her flat reply a moment ago, and matching the face in this shot.", "she is ashamed she said it, which leaks only through a glance away."),
     dialogue("Tony", LN["L013"], VOICE_C1, "the word 'chair' has hit him. Speaking to Sue without looking at her.",
              "refuses Sue. Opens hard and fast; turns on the exact word 'Nobody', where his voice hardens; exits shut. Stress on 'Nobody'.",
              "low and hard, continuing from his last line, and matching the face in this shot.", "he is afraid she is right, which leaks only through his fist closing.")],
    START, extra_neg="no streaming tears, no sobbing", title="Scene 2 · T3 — \"I’m not ready to push you round in a chair.\" · \"Nobody’s pushing me anywhere.\" · \"Then why did he think you were my dad?\" (SH07–SH09)"))

SHOTS.append(take("SC02-T4", ["SC02-SH10", "SC02-SH11"], 7, ["L015"], "Tony says it; Sue does not answer",
    [("0s-4s", "CLOSE-UP on Tony, three-quarter, eye height, from the driver's side: he finally turns his head and looks at her: \"" + LN["L015"] + "\""),
     ("4s-7s", "MEDIUM from the middle of the back seat, exactly the view of Image3: the two of them sit side by side, Sue on the right behind the wheel, Tony on the left, both looking out at the garden centre through the rain; "
               "neither moves; then Sue reaches to the key in the ignition and turns it.")],
    "his line, then a long silence from behind them before the key turns", "her hands on the wheel, then her right hand going to the key", "his hands resting on his thighs, still",
    ("drained, in the outfit of her card, in the driver's seat", "she has turned the key"),
    ("shut, in the outfit of his card, in the passenger seat, his right trouser knee wet and gritty", "he has turned to look at her, then back to the windscreen"),
    [dialogue("Tony", LN["L015"], VOICE_C1, "he cannot bear the word 'dad'. Speaking to Sue, looking at her for the first time.",
              "promises Sue. Opens low; turns on the exact word 'sort', where his voice firms; exits quiet and set. Stress on 'not'.",
              "low and rough but steady, continuing from his last line, and matching the face in this shot.", "he has no idea how, which leaks only through him looking away again.")],
    END4, audios=("C1",), extra_neg="no Sue speaking", title="Scene 2 · T4 — \"I’ll sort it. I’m not living like this.\" · the key turns (SH10–SH11)"))

FMAP = {"C1-FACE": "voice/C1_face.jpg", "C2-FACE": "voice/C2_face.jpg", "L-CAR": "plates/L-CAR_v1.png",
        "OUT-C1-D1": "hooks/SC01/ingredients/OUT-C1-D1_v1.png", "OUT-C2-D1": "hooks/SC01/ingredients/OUT-C2-D1_v1.png"}
AMAP = {"C1": "voice/C1_voice_master.mp3", "C2": "voice/C2_voice_master.mp3"}

if __name__ == "__main__":
    for s in SHOTS:
        call = {"beat": s["beat"], "build": "stryde-her-dad", "connector": "seedance", "model": "bytedance/seedance-2-5", "mode": 4, "kind": s["kind"], "prompt": s["prompt"],
                "take": s["beat"], "covers": s["covers"], "start_pos": s["start_pos"], "end_pos": s["end_pos"], "duration": s["duration"], "resolution": "720p",
                "aspect_ratio": "9:16", "start_image": None, "ingredients_approved": True, "files": [FMAP[f] for f in s["files"]],
                "audios": [AMAP[a] for a in s["audios"]], "generate_audio": True, "dialogue": s["line"], "script_line": s["line"],
                "pace": "brisk" if s["beat"] == "SC02-T2" else "unhurried", "subject_motion": s["subject_motion"], "prefer_multi_shots": "false", "generation": 1, "user_go": GO,
                "vo": "L006" if s["beat"] == "SC02-T1" else None, "scene": 2, "title": s["title"],
                "risks": [{"risk": "the seats swap or the wheel moves to the left", "prevented_by": "the plate, SEATS clause, left-hand-drive negatives"},
                          {"risk": "the voices swap", "prevented_by": "Audio1 Sue, Audio2 Tony, every line named with its speaker"},
                          {"risk": "the cast-sheet clothes return", "prevented_by": "face crops + the confirmed D1 outfit cards (HT26)"}],
                "taste": ["HT02", "HT17", "HT18", "HT22", "HT23", "HT26", "HT27"]}
        (H / f"{s['beat']}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{s['beat']}.prompt.txt").write_text(s["prompt"])
        print(s["beat"], s["duration"], "s", len(s["prompt"]), "chars")
