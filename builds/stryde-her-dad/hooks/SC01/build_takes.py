"""Hook SC01 — the garden-centre car park, story day D1 — three Seedance 2.5 takes on Kie AI, ingredients only, no frames
(§24K part 5, V7.88.0; act map step5/act_map.json, takes SC01-T1..T3).
Film blocks pasted from Appendix A by ID (SERIES-LOOK, INHERIT-FILM, MULTI-FILM / TAKE-FILM, RIG-F*, PHYS-MOTION, STATE-CARRY,
FOCUS-LINE, BUSINESS-LINE, DRAMA-DELIVERY, AUD-FILM, NEG-*). Faces of Tony and Sue go in as face-and-hair crops with their D1 outfit
cards (HT26); the lad wears his sheet's uniform on D1, so his sheet goes in whole. Each MULTI-SHOT shot runs at least 2.5 s, so the
takes run T1 10 s, T2 13 s, T3 8 s (the act map's 8.7 / 11.8 / 7.1 s rounded up; T2 13 s for the §28H word budget of its 24 words — Mode 4 is never trimmed, §24L; the edit cuts whole).
Tony's inner VO L005 is laid in the edit over T3 (VO-T1-L005); T3 is silent."""
import json, re, sys
from pathlib import Path

H = Path(__file__).parent
B = H.parents[1]
T = (B.parents[1] / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
S = lambda i: re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S).group(1).strip()
ROWS = {r["beat"]: r for r in json.load(open(B / "step5/act_map.json"))}

SERIES = S("SERIES-LOOK")
LOOK = (B / "cast/LOOK.txt").read_text().strip()
INHERIT = S("INHERIT-FILM").replace("exactly as in the start frame", "exactly as set out here, from the first frame to the last")
F1 = lambda cm: S("RIG-F1").replace("[DISTANCE]", str(cm))
F2 = S("RIG-F2")
PHYS = S("PHYS-MOTION")
AUD = S("AUD-FILM")
NEG_SOUND, NEG_FILM, NEG_SCENECUT, NEG_DRAMA = S("NEG-SOUND"), S("NEG-FILM"), S("NEG-SCENECUT"), S("NEG-DRAMA")
NEG_EQUIP = "no microphone in frame, no boom pole, no film equipment, no crew in frame"
NEG_MORPH = "no morphing, no warping, no melting, no merging, no splitting, no duplicate people, no background bending, no texture swimming, no flickering geometry"
SILENT = "The clip carries no dialogue and no voice at all: nobody speaks."
MULTI_HEAD = lambda n, start, still: (f"One scene covered in {n} shots within a single take, all on the same side of the action line, with the same light, look and wardrobe throughout. "
    f"Frame 1: {start}. " + ("Everyone stays in place, seated or standing; the only movement in each shot is its business and the performance." if still else
    "The action carries straight across every cut: each shot picks up the movement exactly where the last one left it — the same step, the same hand, the same direction — and everyone is where the last shot left them."))


def manifest(items):
    return ("INGREDIENTS. " + " ".join(f"{t} {c}" for t, c in items) +
            " These references set who, where and what things ARE; the prose below sets the shot and what HAPPENS, and nothing in them is a shot to cut to.")


FACE = lambda who, pos: f"is {who}: face and hair only, a close crop — {pos} clothes come from the outfit card, never from this picture."
CARD = lambda who, outfit: f"is an info card: {who}'s outfit on this day — {outfit}; follow it exactly, and its caption strip and any text on it never appear in the clip."
SHEET_LAD = "is the lad, the young garden-centre worker: face, age, hair, build and his green work uniform exactly as on this sheet; the sheet's grey backdrop and panels never appear in the clip."
VOICE = lambda name: f"is {name}'s voice, its timbre, pitch, accent and pace, for every line {name} speaks; it sets who they sound like, never how they feel in this shot."
PLACE = ("is the place: the open-air car park of a garden centre on a wet overcast day — the silver five-door hatchback with its boot open in the near bay on the left, "
         "the white panel van across the lane with its back doors toward the camera, the garden centre's glass-and-green-steel front with its racks of plants behind, the trolley shelter on the right; "
         "its tarmac, bay lines, cars and light side exactly as shown.")
state = lambda name, what, change="nothing": S("STATE-CARRY").replace("[NAME]", name).replace(
    "[STATE: eyes, face, hair, wardrobe state, what each hand holds, where they are]", what).replace(
    "[WHAT HAS VISIBLY CHANGED, and its cause, or nothing]", change)
focus = lambda plane, depth: f"FOCUS: {plane} is in sharp focus; {depth}. The blur is optical: soft and round, never smeared."
business = lambda name, act: (f"While the line is spoken, {name} keeps doing one thing with their hands: {act}. It is ordinary and unhurried, and the hands never stop to gesture.")
negs = lambda *x: "NEGATIVES: " + ", ".join(i for i in x if i) + "."

TONY_ID = ("a broad, heavy-shouldered builder of sixty-four with thick salt-and-pepper hair, a crooked nose and a short white scar through his left eyebrow")
SUE_ID = "a tall, lean, upright woman of fifty-two with a honey-blonde jaw-length bob and a long side-swept fringe"
LAD_ID = "a tall, lanky mixed-race lad of nineteen with short dark curls"
TONY_D1 = "a plain charcoal-grey crew-neck sweatshirt, faded navy work trousers down to his boots so both knees are covered, and worn tan leather work boots — exactly his outfit card"
SUE_D1 = "a navy quilted short jacket worn open over a plain white T-shirt, light-wash straight jeans and white trainers — exactly her outfit card"
LAD_D1 = "his plain bottle-green polo shirt, the dark-green zip fleece open over it, black work trousers and black trainers — exactly his sheet"
DAY = ("THE SCENE SO FAR, a wet Saturday midday at the garden centre, one continuous moment: flat grey overcast, about 6500K, the sky the single soft source from above and the left; "
       "the tarmac wet and dark, puddles holding the grey sky. Sue and Tony have come out with their plants to their silver hatchback; its boot is open. "
       "Nobody else is near them until the lad arrives.")
VAN = ("the plain white panel van across the lane, its back doors toward us, with no writing on it; its driver is never seen")
POT = "a black plastic garden-centre pot with a small leafy shrub in it"

L001, L002, L003, L004 = "Sue! SUE!", "You’re alright, you’re alright. I’ve got you.", "Is your dad alright? He looked like he was going to go over.", "He’s fine. Thanks, love."
VOICE_C1 = ("An Englishman of sixty-four from the south-east of England, Kent, a builder all his life: a low, rough, chesty voice with gravel in it, plain working vowels, dropped t's, unhurried. "
            "He says little and says it flat; when he is hurt he goes quieter, not louder. Never theatrical, never sing-song; statements fall at the end.")
VOICE_C2 = ("An Englishwoman of fifty-two from the south-east of England, Kent: a quick, clear, warm mid-range voice, light estuary vowels, crisp consonants; her anger is fear held down — "
            "clipped when frightened, soft when she lets go. Natural, never theatrical.")
VOICE_C4 = ("A young Londoner of nineteen from south London: a quick, light, friendly voice, London vowels, kind and easy, a little breathless when he has been running. Natural and unforced.")


def dialogue(who, line, voice, moment, playing, now, under):
    return (f"DIALOGUE ({who}, verbatim): \"{line}\" {voice} IN THIS MOMENT: {moment} PLAYING: {playing} VOICE NOW: {now} "
            f"UNDER THE LINE: {under} Played small and true, for a camera close enough to see a thought. Never theatrical, never pushed, never performed to the lens.")


GO = "chat: \"confirm and proceed\" (2026-10-02) — voices confirmed, on to the hook; ingredient cards OUT-C1-D1 / OUT-C2-D1 wait for the user's Confirm"
SHOTS = []

T1_START = ROWS["SC01-SH01"]["start_pos"]
T1_END = ROWS["SC01-SH04"]["end_pos"]
SHOTS.append(dict(beat="SC01-T1", kind="multi", covers=["SC01-SH01", "SC01-SH02", "SC01-SH03", "SC01-SH04"], duration=10, line=L001, subject_motion="in_place",
    start_pos=T1_START, end_pos=T1_END, files=["C2-FACE", "C1-FACE", "C4", "L-CARPARK", "OUT-C2-D1", "OUT-C1-D1"], audios=["C1"],
    title="Hook · SC01-T1 — the van backs at Sue; Tony shouts, his knee goes, the lad gets there (SH01–SH04)",
    prompt=" ".join([
        manifest([("@image1", FACE("Sue", "her")), ("@image2", FACE("Tony", "his")), ("@image3", SHEET_LAD), ("@image4", PLACE),
                  ("@image5", CARD("Sue", "the navy quilted jacket open over a white T-shirt, light jeans, white trainers")),
                  ("@image6", CARD("Tony", "the charcoal sweatshirt, navy work trousers to the boots, tan work boots")),
                  ("@audio1", VOICE("Tony"))]),
        SERIES, LOOK, INHERIT, DAY,
        f"Sue is {SUE_ID}, in {SUE_D1}. Tony is {TONY_ID}, in {TONY_D1}. The lad is {LAD_ID}, in {LAD_D1}.",
        MULTI_HEAD(4, T1_START, False),
        f"SHOT 1, [0s-2.5s]: WIDE from high above the car park, three-quarter on, the whole lane in frame; Camera on a tripod, locked: Sue lifts {POT} into the open boot of the silver hatchback, her back to the lane; "
        f"Tony stands about ten feet behind her on the wet tarmac, facing her, {POT} held in both hands at his waist; across the lane {VAN} — its reversing lights come on and it starts to roll back toward her at walking pace. "
        "SHOT 2, [2.5s-5s]: MEDIUM CLOSE-UP on Tony at eye height, three-quarter, the plant still in his hands: he sees the van and shouts her name, sudden and raw: \"" + L001 + "\" "
        "SHOT 3, [5s-7.5s]: FULL, low at knee height in clean profile: carrying straight on, he lets the pot fall — it cracks on the tarmac — and lunges one step toward her with his right foot; "
        "on that step his right knee gives and he goes down onto that knee on the wet tarmac, his right hand flat to the ground. "
        "SHOT 4, [7.5s-10s]: FULL at eye height, front-on to the boot: the lad runs in past Tony from behind him, four strides, takes Sue by both upper arms and pulls her two steps clear "
        "to the side of the hatchback's rear wheel as the van stops short with a jolt a metre from the open boot, its brake lights flaring. "
        "Each cut lands on a completed action. Nobody looks into the lens. Last frame: " + T1_END + ".",
        F2, PHYS,
        "The pot falls and lands at real speed — quick, ordinary, never in slow motion — and cracks into a few hard-edged pieces, the shrub's soil spilling; nothing bounces.",
        state("TONY", "in the outfit of his card, a potted shrub in both hands, standing ten feet behind Sue", "he has dropped the pot and is down on his right knee"),
        state("SUE", "in the outfit of her card, at the open boot, her back to the van", "the lad has pulled her clear and holds her by both arms"),
        focus("everything from the hatchback to the van", "everything from near to far stays sharp in the wides; Tony's eyes are sharp in his close-up, the car park soft behind him"),
        dialogue("Tony", L001, VOICE_C1, "he sees the van rolling at his wife and has one second. Calling to Sue across the tarmac, all alarm.",
                 "warns Sue. Opens on a sharp intake of breath; turns on the exact word 'SUE', where the second call breaks loud and ragged; exits already moving. Stress on 'SUE'.",
                 "a sudden full-chested shout from a man who rarely raises his voice, rough at the top, continuing from how Tony sounded on the previous line, and matching the face in this shot.",
                 "he knows before he moves that he will not get there, which leaks only through how his hands tighten on the pot."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, "no collision, no one hit by the van, no van touching the car, no blood, no slow motion, no shorts, no bare knees, no camel coat, no writing on the van, "
             "no logo on the uniform, no second van, no driver visible, no one else speaking, no lad's lines in this clip, no hand on any rail", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the van hits her or the car (the near miss reads as a crash)", "prevented_by": "it stops short a metre from the boot, collision negatives"},
           {"risk": "Tony's knee drop reads as a stumble or a dive", "prevented_by": "one step with the right foot, the right knee gives, down onto that knee, hand flat — SHOT 3 low profile"},
           {"risk": "the sheet clothes return (shorts, camel coat)", "prevented_by": "face crops + D1 outfit cards (HT26), shorts/coat negatives"},
           {"risk": "the shots restart the action", "prevented_by": "MULTI-FILM MOVE, start and end positions written"}]))

T2_START = ROWS["SC01-SH05"]["start_pos"]
T2_END = ROWS["SC01-SH07"]["end_pos"]
SHOTS.append(dict(beat="SC01-T2", kind="multi", covers=["SC01-SH05", "SC01-SH06a", "SC01-SH06b", "SC01-SH07"], duration=13, line=" ".join([L002, L003, L004]),
    subject_motion="still", start_pos=T2_START, end_pos=T2_END, files=["C4", "C2-FACE", "C1-FACE", "L-CARPARK", "OUT-C2-D1", "OUT-C1-D1"], audios=["C4", "C2"],
    title="Hook · SC01-T2 — \"I’ve got you.\" · \"Is your dad alright?\" · \"He’s fine. Thanks, love.\" (SH05–SH07)",
    prompt=" ".join([
        manifest([("@image1", SHEET_LAD), ("@image2", FACE("Sue", "her")), ("@image3", FACE("Tony", "his")), ("@image4", PLACE),
                  ("@image5", CARD("Sue", "the navy quilted jacket open over a white T-shirt, light jeans, white trainers")),
                  ("@image6", CARD("Tony", "the charcoal sweatshirt, navy work trousers to the boots, tan work boots")),
                  ("@audio1", VOICE("the lad")), ("@audio2", VOICE("Sue"))]),
        SERIES, LOOK, INHERIT, DAY.replace("Nobody else is near them until the lad arrives.",
            f"A moment ago {VAN.replace('across the lane, its back doors toward us', 'reversed toward her')} and stopped a metre short of the open boot; the lad pulled her clear. Tony went down on his right knee on the tarmac ten feet away, a cracked pot beside him."),
        f"Sue is {SUE_ID}, in {SUE_D1}. Tony is {TONY_ID}, in {TONY_D1}. The lad is {LAD_ID}, in {LAD_D1}.",
        MULTI_HEAD(4, T2_START, True),
        "THE EXCHANGE, word for word and in this order: " + L002 + " " + L003 + " " + L004 + " — the lad says the first two lines, Sue answers with the third; Tony says nothing. "
        "SHOT 1, [0s-3.5s]: MEDIUM CLOSE-UP over Sue's shoulder onto the lad, eye height, her shoulder soft in the near frame; Camera on a tripod, locked: breathless, holding her by both upper arms, he says gently: \"" + L002 + "\" "
        "SHOT 2, [3.5s-7s]: MEDIUM CLOSE-UP on the lad, three-quarter, eye height: still holding her arms, he glances past her toward Tony on the ground, kind and concerned, and asks her: \"" + L003 + "\" "
        "SHOT 3, [7s-10s]: WIDE from high past the lad's shoulder, his shoulder soft in the near frame: ten feet away, Tony is still down on his right knee on the wet tarmac beside the cracked pot, "
        "his right hand flat on the ground, getting ready to push himself up; the lad's question finishes over this shot. "
        "SHOT 4, [10s-13s]: CLOSE-UP on Sue, front-on, eye height: shaken, she glances toward Tony, a beat, then back to the lad, and says quietly: \"" + L004 + "\" "
        "The lines land on each other in the rhythm this scene needs: cutting in close, a beat held on Tony, a beat before Sue answers. Each cut lands on a completed line, action or reaction. "
        "The eyelines match across every reverse. Nobody looks into the lens. Last frame: " + T2_END + ".",
        F2, PHYS,
        business("the lad", "both hands holding Sue's upper arms, steadying her, at one even grip through the line, letting go only on the last frame"),
        state("SUE", "shaken, in the outfit of her card, held by both arms beside the hatchback's rear wheel", "the lad lets go of her arms at the end"),
        state("TONY", "in the outfit of his card, down on his right knee ten feet away, the cracked pot and spilled soil beside him", "nothing"),
        focus("the nearest eye of whoever is speaking", "the car park behind falls to a soft, recognisable shape; in the wide past the lad, Tony on the ground is sharp"),
        dialogue("the lad", L002 + " … " + L003, VOICE_C4, "he has just pulled a stranger out of a van's way and is still breathing hard. Speaking to Sue, close, steadying her.",
                 "reassures Sue. Opens breathless and quick; turns on the exact word 'dad', where his voice softens with concern as he looks past her; exits gentle, waiting for her answer. Stress on 'dad'.",
                 "light, quick and out of breath, settling as he goes, continuing from how the lad sounded on the previous line, and matching the face in this shot.",
                 "he assumes the man on the ground is her father and feels sorry for him, which leaks only through a glance away toward Tony."),
        dialogue("Sue", L004, VOICE_C2, "she has just nearly been hit and has watched her husband fall. Speaking to the lad, a stranger, who has just called her husband her dad.",
                 "covers for Tony. Opens with a small swallow; turns on the exact word 'fine', where her voice goes flat and closes the subject; exits polite, eyes down. Stress on 'fine'.",
                 "quiet, a little shaky, brisk to end it, continuing from how Sue sounded on the previous line, and matching the face in this shot.",
                 "she will not say 'husband' in front of the boy, which leaks only through a glance away from Tony before she speaks."),
        AUD,
        negs(NEG_EQUIP, NEG_MORPH, "no Tony speaking, no Tony standing up, no Sue saying 'husband', no lad saying Sue's line, no van moving, no shorts, no bare knees, no camel coat, "
             "no logo on the uniform, no crowd gathering", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "the voices swap or Tony speaks", "prevented_by": "Audio1 the lad, Audio2 Sue, every line named with its speaker, Tony-speaking negative"},
           {"risk": "Tony gets up or moves in the wide", "prevented_by": "STILL head, state-carry: still on his right knee, 'getting ready to push himself up'"},
           {"risk": "the sheet clothes return", "prevented_by": "face crops + D1 outfit cards (HT26)"}]))

T3_START = ROWS["SC01-SH08"]["start_pos"]
T3_END = "Tony still down on his right knee on the tarmac, the cracked pot beside his left hand, looking toward Sue and the lad by the hatchback, framed closer"
SHOTS.append(dict(beat="SC01-T3", kind="take", covers=["SC01-SH08"], duration=8, line="", vo="L005", subject_motion="still",
    start_pos=T3_START, end_pos=T3_END, files=["C1-FACE", "L-CARPARK", "OUT-C1-D1"], audios=[],
    title="Hook · SC01-T3 — Tony on one knee, watching them (SH08; his inner voice L005 laid in the edit)",
    prompt=" ".join([
        manifest([("@image1", FACE("Tony", "his")), ("@image2", PLACE),
                  ("@image3", CARD("Tony", "the charcoal sweatshirt, navy work trousers to the boots, tan work boots"))]),
        SERIES, LOOK, INHERIT, DAY.replace("Nobody else is near them until the lad arrives.",
            "A moment ago a white van reversed toward Sue and a young garden-centre worker pulled her clear; Tony went down on his right knee on the tarmac ten feet away, his dropped pot cracked beside him."),
        S("TAKE-FILM").split(" Frame 1:")[0].replace("[N]s", "8s") + f" Frame 1: {T3_START}. "
        f"Tony is {TONY_ID}, in {TONY_D1}. "
        "[0s-8s]: a CLOSE-UP from low, at the height of his knee, three-quarter on his face: he stays down on his right knee on the wet tarmac and watches them — Sue and the young man in green, soft and small "
        "by the silver hatchback in the background. His mouth stays closed. His face holds it: his jaw sets, his eyes stay on them, one slow breath; he does not get up. "
        f"Last frame: {T3_END}. The movement is continuous from the first frame to the last: nobody jumps position or appears somewhere new, and the car park behind him stays the same place.",
        F1(30), PHYS,
        state("TONY", "humiliated, in the outfit of his card, down on his right knee on the wet tarmac, his right hand on the ground, the cracked pot and spilled soil by his left hand", "nothing"),
        focus("the nearest eye of Tony", "Sue and the lad behind fall to a soft, recognisable shape"),
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, "no talking, no mouth moving, no tears, no standing up, no one coming to help him, no shorts, no bare knees, no knee support", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)]),
    risks=[{"risk": "Tony speaks or mouths the VO", "prevented_by": "silent call, mouth closed, talking negatives — the VO is laid in the edit"},
           {"risk": "the push-in turns into a travel", "prevented_by": "F1 at 30 cm, the subject still"},
           {"risk": "theatrical grief", "prevented_by": "jaw sets, one slow breath, NEG-DRAMA, no tears"}]))

FILES = {"C1-FACE": "voice/C1_face.jpg", "C2-FACE": "voice/C2_face.jpg", "C4": "cast/C4-LAD_v1.png", "L-CARPARK": "plates/L-CARPARK_v1.png",
         "OUT-C1-D1": "hooks/SC01/ingredients/OUT-C1-D1_v1.png", "OUT-C2-D1": "hooks/SC01/ingredients/OUT-C2-D1_v1.png"}
AUDIO = {"C1": "voice/C1_voice_master.mp3", "C2": "voice/C2_voice_master.mp3", "C4": "voice/C4_voice_master.mp3"}

if __name__ == "__main__":
    approved = "--approved" in sys.argv
    for s in SHOTS:
        call = {"beat": s["beat"], "build": "stryde-her-dad", "connector": "seedance", "model": "bytedance/seedance-2-5", "mode": 4, "kind": s["kind"], "prompt": s["prompt"],
                "take": s["beat"], "covers": s["covers"], "start_pos": s["start_pos"], "end_pos": s["end_pos"], "duration": s["duration"], "resolution": "720p",
                "aspect_ratio": "9:16", "start_image": None, "ingredients_approved": approved, "files": [FILES[f] for f in s["files"]],
                "audios": [AUDIO[a] for a in s["audios"]], "generate_audio": bool(s["line"]), "dialogue": s["line"] or None, "script_line": s["line"] or None,
                "pace": "unhurried", "subject_motion": s["subject_motion"], "prefer_multi_shots": "false", "generation": 1, "user_go": GO,
                "risks": s["risks"], "vo": s.get("vo"), "scene": 1, "title": s["title"],
                "taste": ["HT02", "HT17", "HT18", "HT22", "HT23", "HT26", "HT27"]}
        (H / f"{s['beat']}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{s['beat']}.prompt.txt").write_text(s["prompt"])
        print(s["beat"], s["duration"], "s", len(s["prompt"]), "chars")
