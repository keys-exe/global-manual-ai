"""Scene 3 — rock bottom, story day D2 (a weekday) — three Seedance 2.5 takes on Kie, ingredients only, no frames (act map takes SC03-T1..T3).
All three are silent: Tony's VO L016 runs over T1 + T2 and L017 over T3, laid in the edit (VO-T1-L016 / L017, confirmed).
Faces as face-and-hair crops + the D2 outfit cards (HT26); plates L-BEDROOM v1, L-STAIRS v5, L-CAR v1 (all confirmed).
Stairs: hands free at his sides, never on the rail (L56 / FP23 — the script does not put his hand on it)."""
import json, importlib.util
from pathlib import Path

H = Path(__file__).parent
B = H.parents[1]
_s = importlib.util.spec_from_file_location("sc01", B / "hooks/SC01/build_takes.py"); S1 = importlib.util.module_from_spec(_s); _s.loader.exec_module(S1)
S = S1.S
SERIES, LOOK, INHERIT, F1, F2, PHYS, SILENT = S1.SERIES, S1.LOOK, S1.INHERIT, S1.F1, S1.F2, S1.PHYS, S1.SILENT
NEG_EQUIP, NEG_MORPH, NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND = S1.NEG_EQUIP, S1.NEG_MORPH, S1.NEG_FILM, S1.NEG_SCENECUT, S1.NEG_DRAMA, S1.NEG_SOUND
manifest, FACE, CARD, state, focus, negs = S1.manifest, S1.FACE, S1.CARD, S1.state, S1.focus, S1.negs
TONY_ID, SUE_ID = S1.TONY_ID, S1.SUE_ID
ROWS = {r["beat"]: r for r in json.load(open(B / "step5/act_map.json"))}

TONY_D2 = "a plain olive-green crew-neck work sweatshirt, grey work trousers down to his boots so both knees are covered, and worn tan leather work boots — exactly his outfit card"
SUE_D2 = "a burgundy hip-length rain jacket zipped halfway over a grey T-shirt, black slim jeans and grey trainers — exactly her outfit card"
CARD_T = CARD("Tony", "the olive work sweatshirt, grey work trousers to the boots, tan work boots")
CARD_S = CARD("Sue", "the burgundy rain jacket, grey T-shirt, black jeans, grey trainers")
NEG_T = "no shorts, no bare knees, no knee sleeve worn, no charcoal sweatshirt, no navy sweatshirt, no navy trousers"
ONE = lambda n: S("TAKE-FILM").split(" Frame 1:")[0].replace("[N]s", f"{n}s")
CONT = ("The movement is continuous from the first frame to the last: nobody jumps position or appears somewhere new, every step lands on the step after the last, "
        "and the room behind them stays the same room.")
MOVE = ("The action carries straight across every cut: each shot picks up the movement exactly where the last one left it — the same step, the same hand, the same direction — "
        "and everyone is where the last shot left them.")
GO = "chat: \"confirm and proceed\" (2026-10-03) — SC02 confirmed, on to SC03; the D2 outfit cards wait for the user's Confirm"
DAY = ("THE DAY, a grey weekday, story day D2, some weeks after the car park: flat cool overcast light, about 6500K. Tony is dressed for work but there is no work today; "
       "he is alone with his knee.")
SHOTS = []

r = ROWS["SC03-SH01"]
SHOTS.append(dict(beat="SC03-T1", kind="take", covers=["SC03-SH01"], duration=5, subject_motion="in_place", start_pos=r["start_pos"], end_pos=r["end_pos"],
    files=["C1-FACE", "L-BEDROOM", "OUT-C1-D2"], vo="L016",
    title="Scene 3 · T1 — the drawer full of knee sleeves that won't shut (SH01; VO L016)",
    prompt=" ".join([
        manifest([("@image1", FACE("Tony", "his")), ("@image2", "is the place: their bedroom — the bed with the navy cover on the left, the pine chest of drawers under the sash window with its grey curtains, "
                   "the white fitted wardrobe on the right, grey carpet; its walls, window, furniture and light side exactly as shown."), ("@image3", CARD_T)]),
        SERIES, LOOK, INHERIT, DAY.replace("weeks after the car park:", "weeks after the car park, morning in the bedroom:") + " The window light comes from behind the chest of drawers.",
        ONE(5) + f" Frame 1: {r['start_pos']}. Tony is {TONY_ID}, in {TONY_D2}. "
        "[0s-5s]: a MEDIUM CLOSE-UP from a little above, three-quarter on him, at the chest of drawers: he pushes the beige knee sleeve into the top drawer, which is already packed full of knee sleeves, "
        "straps and supports; the drawer will not shut; he leans on it with the flat of his palm until it slides closed. His mouth stays closed. "
        f"Last frame: {r['end_pos']}. " + CONT,
        F2, PHYS,
        state("TONY", "tired, in the outfit of his card, standing at the chest of drawers, a beige knee sleeve in his right hand", "the drawer is shut under his palm"),
        focus("his hands and the packed drawer", "the window and the room behind fall to a soft, recognisable shape"),
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, NEG_T, "no brand or writing on the sleeves, no talking, no mouth moving, no drawer from another chest", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)])))

a, b = ROWS["SC03-SH02"], ROWS["SC03-SH03"]
SHOTS.append(dict(beat="SC03-T2", kind="multi", covers=["SC03-SH02", "SC03-SH03"], duration=8, subject_motion="travels", start_pos=a["start_pos"], end_pos=b["end_pos"],
    files=["C1-FACE", "L-STAIRS", "OUT-C1-D2"], vo="L016",
    title="Scene 3 · T2 — down his own stairs sideways (SH02–SH03; VO L016)",
    prompt=" ".join([
        manifest([("@image1", FACE("Tony", "his")), ("@image2", "is the place: the staircase of their house seen from the top — a steep straight flight of light-grey carpeted steps going down to the hall, "
                   "the oak handrail on white spindles down the LEFT side, the plain soft-white wall on the RIGHT, the light-oak hall floor and the white front door with its glass panel at the bottom; "
                   "its stairs, rail, walls and light side exactly as shown."), ("@image3", CARD_T)]),
        SERIES, LOOK, INHERIT, DAY.replace("he is alone with his knee.", "he is alone with his knee. The hall is lit by grey daylight through the front-door glass."),
        f"Tony is {TONY_ID}, in {TONY_D2}. He goes down his own stairs SIDEWAYS, the way a man does when one knee will not bend: his body side-on to the flight, facing the LEFT side of the stairs, "
        "his arms hanging loose at his sides — he does not touch the rail or the wall at any moment. Each step: his left foot goes down first, then he lowers the stiff right leg down beside it onto the same step, "
        "one step at a time, slowly.",
        f"One scene covered in 2 shots within a single take, all on the same side of the action line, with the same light, look and wardrobe throughout. Frame 1: {a['start_pos']}. " + MOVE + " "
        "SHOT 1, [0s-4s]: FULL, from high on the landing BEHIND him, looking down the flight exactly as in Image2: Tony, side-on, takes the first three steps down sideways, left foot first, the right leg brought down stiffly after it each time. "
        "SHOT 2, [4s-8s]: FULL, low from the hall at the foot of the stairs, looking up the flight: carrying straight on, halfway down, still side-on with his arms loose at his sides, "
        "he lowers the stiff right leg onto the next step; his face is tight with it. His mouth stays closed. "
        f"Each cut lands on a completed step. Nobody looks into the lens. Last frame: {b['end_pos']}.",
        F2, PHYS,
        state("TONY", "in the outfit of his card, going down sideways, arms loose at his sides", "he is halfway down the flight"),
        focus("Tony", "everything from near to far stays sharp"),
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, NEG_T, "no hand on the rail, no hand on the banister, no hand on the wall, no walking forwards down the stairs, no falling, no stumbling, no stairs bending, "
             "no steps changing count, no feet sliding, no talking, no mouth moving", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)])))

r = ROWS["SC03-SH04"]
SHOTS.append(dict(beat="SC03-T3", kind="take", covers=["SC03-SH04"], duration=9, subject_motion="still", start_pos=r["start_pos"], end_pos=r["end_pos"],
    files=["C1-FACE", "C2-FACE", "L-CAR", "OUT-C1-D2", "OUT-C2-D2"], vo="L017",
    title="Scene 3 · T3 — he waits in the car while she loads the boot (SH04; VO L017)",
    prompt=" ".join([
        manifest([("@image1", FACE("Tony", "his")), ("@image2", FACE("Sue", "her")),
                  ("@image3", "is the car: their silver right-hand-drive hatchback — the charcoal cloth front seats, the steering wheel on the RIGHT, the dashboard; its seats and windows exactly as shown."),
                  ("@image4", CARD_T), ("@image5", CARD_S)]),
        SERIES, LOOK, INHERIT,
        "THE DAY, a grey weekday, story day D2: flat overcast daylight, about 6500K, a supermarket car park outside. The car is parked; its boot is open behind. "
        "Tony sits in the PASSENGER seat on the LEFT; the driver's seat on the right is empty; Sue is outside at the open boot behind the car.",
        ONE(9) + f" Frame 1: {r['start_pos']}. Tony is {TONY_ID}, in {TONY_D2}. Sue is {SUE_ID}, in {SUE_D2}. "
        "[0s-9s]: a MEDIUM CLOSE-UP of Tony in clean profile, eye height, from the empty driver's seat: he sits looking straight ahead through the windscreen, still, his jaw set, his mouth closed. "
        "Behind him, small and soft through the rear window, Sue lifts two heavy shopping bags into the open boot on her own, one after the other, then reaches up and pulls the boot lid down; it shuts with a jolt that rocks the car slightly. "
        "Tony does not turn round. "
        f"Last frame: {r['end_pos']}. " + CONT.replace("every step lands on the step after the last, ", ""),
        F1(20), PHYS,
        state("TONY", "ashamed, in the outfit of his card, in the passenger seat facing ahead, hands in his lap", "nothing — the boot has shut behind him"),
        focus("the nearest eye of Tony", "Sue at the boot behind falls to a soft, recognisable shape"),
        SILENT,
        negs(NEG_EQUIP, NEG_MORPH, NEG_T, "no Tony turning round, no Tony getting out, no Sue in the car, no left-hand-drive car, no talking, no mouth moving, no burgundy on Tony", NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)])))

FMAP = {"C1-FACE": "voice/C1_face.jpg", "C2-FACE": "voice/C2_face.jpg", "L-BEDROOM": "plates/L-BEDROOM_v1.png", "L-STAIRS": "plates/L-STAIRS_v5.png", "L-CAR": "plates/L-CAR_v1.png",
        "OUT-C1-D2": "body/SC03/ingredients/OUT-C1-D2_v1.png", "OUT-C2-D2": "body/SC03/ingredients/OUT-C2-D2_v1.png"}

if __name__ == "__main__":
    import sys
    approved = "--approved" in sys.argv
    for s in SHOTS:
        call = {"beat": s["beat"], "build": "stryde-her-dad", "connector": "seedance", "model": "bytedance/seedance-2-5", "mode": 4, "kind": s["kind"], "prompt": s["prompt"],
                "take": s["beat"], "covers": s["covers"], "start_pos": s["start_pos"], "end_pos": s["end_pos"], "duration": s["duration"], "resolution": "720p", "aspect_ratio": "9:16",
                "start_image": None, "ingredients_approved": approved, "files": [FMAP[f] for f in s["files"]], "audios": [], "generate_audio": False, "dialogue": None, "script_line": None,
                "pace": "unhurried", "subject_motion": s["subject_motion"], "prefer_multi_shots": "false", "generation": 1, "user_go": GO, "vo": s["vo"], "scene": 3, "title": s["title"],
                "risks": [{"risk": "his hand goes to the rail (L56)", "prevented_by": "arms loose at his sides, rail negatives"},
                          {"risk": "the cast-sheet shorts return", "prevented_by": "face crop + D2 outfit card, shorts/bare-knee negatives (HT26)"},
                          {"risk": "Tony speaks or mouths the VO", "prevented_by": "silent call, mouth closed"}],
                "taste": ["HT02", "HT17", "HT18", "HT22", "HT23", "HT26", "HT27", "FP23"]}
        (H / f"{s['beat']}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{s['beat']}.prompt.txt").write_text(s["prompt"])
        print(s["beat"], s["duration"], "s", len(s["prompt"]), "chars")
