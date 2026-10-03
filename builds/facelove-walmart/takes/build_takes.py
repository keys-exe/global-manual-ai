#!/usr/bin/env python3
"""SD-PROMPT takes for facelove-walmart (V7.97.0 format, V7.99.0 coverage, V7.100.0 moves, V7.101.0 sound on).
One Seedance 2.5 call per take of step5/act_rows.json. Writes takes/<TAKE>.call.json; SC01-T1 is build_sc01.py."""
import json, pathlib, re, sys
from collections import OrderedDict
H = pathlib.Path(__file__).parent
B = H.parent
rows = json.load(open(B / "step5/act_rows.json"))
LINES = {l["id"]: l for l in json.load(open(B / "work/lines.json"))["lines"]}
W = {d["day"]: d["outfits"] for d in json.load(open(B / "step5/wardrobe.json"))["days"]}
NAME = {"N": "Michelle", "C1": "Peter", "C2": "the woman", "C3": "Rosa"}
SPK = {"MICHELLE": "N", "PETER": "C1", "YOUNGER WOMAN": "C2", "ROSA": "C3"}
AGE = {"N": "63", "C1": "65", "C2": "41", "C3": "67"}
SHEET = {"C1": "cd1173f1-ffef-4258-90f0-4c5143ea351b", "C2": "260a0f37-7ab1-4b16-b87a-ccc9c4bba621", "C3": "702ccb5a-64ac-4585-af45-b7b8443efba6"}
SHEET_N = {"before": "e41bb60b-dd24-4808-8b8e-5956cbe2dda6", "after": "7ee60be8-ae88-458d-8d13-d5ebfc2ff6a7"}
AUDIO = {"N": ("voice/N_voice_master.mp3", "18b2c0a4-b1d2-40f0-8321-dbd8fba7c8f1", 16.8), "C1": ("voice/C1_voice_master.mp3", "57c4e338-a41d-4931-a5ac-9ecbd7e26975", 13.1),
         "C2": ("voice/C2_voice_master.mp3", "a9360508-157a-46c4-b14b-ba13c1b3221f", 8.7), "C3": ("voice/C3_voice_ref_cut.mp3", "83341657-baea-4764-a0a8-ecd793cb5472", 10.8)}
PLATE = {"L-AISLE": ("61b35cd5-43a2-4e4d-a243-be5ace889248", "the store aisle: copy it — paper shelves left, detergent shelves right, the blue end-cap at the far right corner, the walkway across the far end"),
         "L-LIVING": ("fa121b5f-769e-4246-8b2d-98784c2a4e93", "the living room: copy it — the dusty-rose armchair and lamp front left, the walnut coffee table in the middle, the oatmeal sofa on the right wall, the archway back centre"),
         "L-VANITY": ("07f8970a-fd26-4dcd-8e73-83e1fcefd259", "the bedroom: copy it — the white vanity and oval mirror right of centre, the lilac stool, the curtained window on the right, the cream bed on the left"),
         "L-HALL": ("95d48c48-199d-40c1-a0d7-b0c6f5422a28", "the entry hall: copy it — the white front door at the end, the round brass mirror over the console on the left wall, the archway on the right, the globe pendant in the middle"),
         "L-PATIO": ("2555f8cb-3c99-4448-97d5-3eccb9044369", "the patio: copy it — the round mosaic table in the middle, the lemon tree left, the magenta bougainvillea right, the sand garden wall behind"),
         "L-STORE-DOORS": ("d1621fb9-266e-4c1a-bf04-c731988564aa", "the store front: copy it — the open sliding doors ahead, nested carts on the right, the blue mat, the golden parking lot and palms beyond")}
PROD = [("47b23ddf-c6c4-4ffa-89c2-77a4ddc312f1", "the FACELOVE stick, closed: copy it exactly — the violet satin barrel with its one wordmark; it is a little longer than a hand is wide"),
        ("ab69219d-f5c7-448d-92e5-056867ad5ad7", "the stick's balm end, uncapped: the white balm, copied exactly"),
        ("aa71f71b-7076-495c-a7d6-8c68af08fce9", "the stick's brush end: copied exactly"),
        ("89f64a0f-9603-4986-b15f-5369389f9f7f", "info card: the stick's true size in a hand. Copy only that size")]
COLOUR = ("cddd3282-90c4-40d2-bdcd-def14ab1e0d2", "info card: the colour front — white ahead of the brush, her own shade behind, every line of the skin kept. Copy only that; its caption never appears")
SIZE = {"WIDE": "wide", "FULL": "full shot", "MEDIUM": "medium", "MCU": "medium close-up", "CU": "close-up", "ECU": "extreme close-up"}
GROUP = {"wide": "wide", "full shot": "wide", "medium": "medium", "medium close-up": "close", "close-up": "close", "extreme close-up": "xclose", "insert": "xclose"}
MOVE = {"F1": "slow push-in", "F2": "locked", "F4": "slider moving sideways", "F5": "follows", "F6": "the camera pulls back", "F7": "the camera arcs",
        "F8": "crane up", "F9": "tracks alongside", "F11": "slow pan", "F12": "slow tilt", "F13": "leading her, backing away in front", "F14": "follows from behind",
        "F15": "the camera orbits", "F16": "jib down", "F17": "pushes through", "F18": "slow creep in", "F19": "crash zoom", "F20": "pull-out from the macro",
        "F21": "overhead track", "F22": "counter-move", "F23": "handheld, breathing"}
ROOM = {"L-AISLE": "the store's soft air-conditioning hum", "L-LIVING": "a quiet house at night, a clock ticking", "L-VANITY": "a still bedroom",
        "L-HALL": "the quiet hall at night", "L-PATIO": "birdsong and a light breeze in the garden", "L-STORE-DOORS": "the doors' hum and the car park outside"}
SHOT = {"SC02": "A quiet, aching animated family drama: in the lamplit living room Peter, in his coat, leaves an envelope and thirty-one years; Michelle stays in the armchair as the room goes dark",
        "SC03": "A quiet animated drama: at night at her vanity Michelle stops recognising the woman in the mirror and buries her under layer after layer of foundation",
        "SC04": "A quiet animated drama: one morning at the vanity Michelle goes through every bottle she owns, gives up, and sweeps them away",
        "SC05": "A warm animated family drama: Rosa bangs on the front door with wine, Michelle opens it in an old sweatshirt, and in the hall her sister holds her face up to the light",
        "SC06": "A warm animated family drama with a quiet wonder: in the hall Rosa draws the violet stick from her bag and shows Michelle how it turns from white into her own shade",
        "SC07": "A warm animated drama: the first morning Michelle does it herself at her vanity, and for once she does not look away",
        "SC08": "A sunny animated family drama: on the patio Michelle and Rosa take photos together again, and Michelle stands taller",
        "SC09": "An animated comedy-drama payoff: back in the store aisle the younger woman turns on Peter, then runs after Michelle to ask what she uses",
        "SC10": "A bright animated payoff: Michelle pushes her cart out through the sliding doors into the golden light, never looking back",
        "SC11": "A calm animated epilogue: two weeks later on the patio Peter's text arrives; Michelle reads it, smiles and turns the phone face down",
        "SC12": "A warm animated close: on the patio in the late sun Michelle turns to us, holds up the violet stick and tells us it was never us"}
SOUND = {"SC02": "the envelope set down on the wood, his shoes on the rug, the front door closing off-screen, the lamp's click",
         "SC03": "jars and bottles touched down on the vanity, a sponge patting skin, her slow breath",
         "SC04": "glass bottles clinking, the drawer sliding shut, her sigh",
         "SC05": "knocking on the front door, the latch and the door opening, the wine bottle set on the console",
         "SC06": "the bag's zip, the cap coming off the stick, the soft brush on skin",
         "SC07": "her slippers on the floor, the stool, the cap of the stick",
         "SC08": "the phone camera's shutter click, chairs scraping on stone, their laughter",
         "SC09": "the cart wheels, trainers hurrying on the shiny floor",
         "SC10": "the sliding doors, the cart wheels on the mat",
         "SC11": "the phone's buzz on the mosaic table, the cup set down, the phone turned over",
         "SC12": "the chair pushed back, her sandals on the stone, the stick set down on the table"}
SHOT_T = {"SC05-T2": "A warm animated family drama: in the hall Rosa turns her sister round from the mirror and tells her it was never her age, it was the foundation",
          "SC06-T2": "A warm animated drama in one unbroken close shot: the brush works the white stripe on Michelle's cheek and the white turns into her own shade as it goes",
          "SC06-T3": "A warm animated family drama: Michelle turns from her sister to the hall mirror and almost smiles at herself"}
SOUND_T = {"SC05-T2": "Rosa's bracelets, their slippers and sandals on the hall floor, a breath",
           "SC06-T2": "the soft brush on skin, a breath",
           "SC06-T3": "her slippers turning on the hall floor, a breath"}
LOOKBASE = "A theatrical 3D animated feature, stylised adults with large expressive eyes, soft skin, sculpted hair, fabric with weight; natural, ungraded colour"

def take_rows():
    t = OrderedDict()
    for r in rows:
        t.setdefault(r["take"], []).append(r)
    return t

def speaker(r):
    return SPK[LINES[r["lines"]]["speaker"]] if r.get("dialogue") else None

def build(take, rs):
    g = rs[0]["group"]; day = rs[0]["story_day"]; loc = rs[0]["location"]
    after = day[0] in "AP"
    cast = []
    for r in rs:
        for c in r["cast"]:
            if c not in cast and c in NAME: cast.append(c)
    prod = any(r.get("product_beat") for r in rs) or any("stick" in (r.get("action") or "") for r in rs)
    files, media, refs = [], [], []
    for c in cast:
        mid = SHEET_N["after" if after else "before"] if c == "N" else SHEET[c]
        files.append(f"cast/{c}"); media.append(mid)
        refs.append(f"{NAME[c].capitalize()}, {AGE[c]}: face, hair and build only")
    files.append(f"plates/{loc}"); media.append(PLATE[loc][0]); refs.append(PLATE[loc][1])
    if prod:
        for m, d in PROD:
            files.append("product/" + m[:8]); media.append(m); refs.append(d)
        if g == "SC06":
            files.append("cards/COLOUR-FRONT-CARD"); media.append(COLOUR[0]); refs.append(COLOUR[1])
    spk = []
    for r in rs:
        s = speaker(r)
        if s and s not in spk: spk.append(s)
    audios = [AUDIO[s] for s in spk]
    assert sum(a[2] for a in audios) <= 30, (take, spk)
    REF = "REFERENCES\n" + "\n".join(f"@image{i} — {t}." for i, t in enumerate(refs, 1))
    if spk:
        REF += "\n" + "\n".join(f"@audio{i} — {NAME[s].capitalize()}'s voice." for i, s in enumerate(spk, 1))
    dur = sum(r["duration"] for r in rs)
    if take == "SC06-T2": rs[0] = dict(rs[0], duration=16); dur = 16  # §28H: 30 words need 16 s (2·d − 2), the oner kept whole
    oner = len(rs) == 1 and dur > 5
    SH = f"SHOT: {SHOT_T.get(take, SHOT[g])}; " + (f"one continuous shot, 9:16, {dur} s." if len(rs) == 1 else f"one take of {len(rs)} shots, 9:16, {dur} s.")
    # sizes: never three in a row in one group
    sizes = [("insert" if r["type"] == "INSERT" and r["scale"] in ("CU", "ECU") else SIZE[r["scale"]]) for r in rs]
    for i in range(2, len(sizes)):
        if GROUP[sizes[i]] == GROUP[sizes[i - 1]] == GROUP[sizes[i - 2]]:
            sizes[i - 1] = {"close": "medium", "medium": "medium close-up", "wide": "medium", "xclose": "close-up"}[GROUP[sizes[i]]]
    need = 1 if len(sizes) < 3 else (2 if len(sizes) < 5 else 3)
    if len({GROUP[x] for x in sizes}) < need and "wide" not in {GROUP[x] for x in sizes}:
        j = max(i for i, x in enumerate(sizes) if GROUP[x] == "medium")
        sizes[j] = "full shot"
    t = 0; tl = []; dialog_first = None; marks = rs[0]["marks"]
    for i, (r, sz) in enumerate(zip(rs, sizes)):
        a, b = t, t + r["duration"]; t = b
        mv = MOVE[r["rig"]]
        s = f"[{a}–{b}s] Shot {i + 1} · {sz}, {mv}: "
        if i == 0:
            s += f"Frame 1: {r['start_pos']} — "
        s += r["motion"].rstrip(".") + "."
        if r.get("beat_before"):
            s += " A beat of stillness first."
        sp = speaker(r)
        if sp:
            s += f' {NAME[sp].capitalize()} says: "{r["dialogue"]}"'
            if dialog_first is None: dialog_first = r["dialogue"]
        if i == len(rs) - 1:
            s += f" Last frame: {rs[-1]['end_pos']}."
        tl.append(s)
    TL = "TIMELINE\n" + "\n".join(tl)
    outfits = "; ".join(f"{NAME[c].capitalize()}: {W[day][c].split(' (')[0]}" for c in cast if c in W.get(day, {}))
    lt = rs[0]["light"]
    LOOK = f"LOOK: {LOOKBASE}; light from {lt['source']}, a shadow side on every face. {outfits}."
    if spk:
        who = ", ".join(f"{NAME[s].capitalize()}'s voice from @audio{i}" for i, s in enumerate(spk, 1))
        SND = f"SOUND: Dialogue in natural American English — {who}; only the person written as speaking speaks, and on every other shot nobody speaks. No music. The actions' own sounds: {SOUND_T.get(take, SOUND[g])}; {ROOM[loc]} under it."
    else:
        SND = "SOUND: No dialogue — nobody speaks. No music."  # pre-V7.101 build (PRE_SOUND): a no-dialogue clip is generated silent
    keep = ["same faces, hair and clothes in every frame", f"just {' and '.join(NAME[c] for c in cast)} in the scene" if cast else "the room as in @image1"]
    if prod:
        keep.append("exactly one violet stick at its true size, its wordmark the only text")
    else:
        keep.append("text, logos and captions nowhere")
    keep += ["five fingers on each hand", "real weight and timing"]
    if g != "SC12":
        keep.append("eyes off the lens")
    if g == "SC06":
        keep.append("every line of her skin stays exactly as deep; only the colour evens out")
    KEEP = "KEEP: " + "; ".join(keep)
    P = "\n\n".join([REF, SH, TL, LOOK, SND, KEEP])
    call = {"beat": take, "take": take, "build": "facelove-walmart", "connector": "seedance", "model": "seedance_2_5", "mode": 5,
            "kind": "take" if len(rs) == 1 else "multi", "prompt": P, "duration": dur, "resolution": "720p", "aspect_ratio": "9:16",
            "start_image": None, "ingredients_approved": True, "files": files, "media": media,
            "audios": [a[0] for a in audios], "audio_media": [a[1] for a in audios], "generate_audio": bool(spk), "pre_sound": True,
            "covers": [r["beat"] for r in rs], "start_pos": rs[0]["start_pos"], "end_pos": rs[-1]["end_pos"], "marks": {}, "motion": rs[0]["motion"].rstrip("."),
            "subject_motion": "travels" if any(r["rig"] in ("F13", "F14", "F5", "F9", "F21") for r in rs) else "in_place",
            "pace": rs[0].get("pace") or "unhurried", "prefer_multi_shots": "false", "generation": 1, "user_go": None, "rack": None,
            "risks": [{"risk": "faces or clothes drift between shots", "prevented_by": "faces from the confirmed sheets, the day's outfit written in LOOK, KEEP holds them"},
                      {"risk": "the room changes or flips between shots", "prevented_by": "the plate as a reference with its landmarks and sides written out; start and end positions word for word"},
                      {"risk": "music or a wrong voice in the clip", "prevented_by": "SOUND says no music and names whose voice comes from which audio ref; unmusic.py on landing"}],
            "taste": ["no real brand or logo in frame", "faces from sheets, clothes in words"]}
    # marks: the start position carries everyone's place against the set (§24P), written word for word
    call["marks"] = {c: rs[0]["start_pos"] for c in cast} if cast else {"set": rs[0]["start_pos"]}
    if dialog_first:
        call["dialogue"] = dialog_first; call["script_line"] = dialog_first
    if oner:
        call["oner"] = True
    if g == "SC12" and take == "SC12-T2":
        return None
    return call

if __name__ == "__main__":
    want = sys.argv[1:]
    for take, rs in take_rows().items():
        if take == "SC01-T1" or (want and take not in want): continue
        c = build(take, rs)
        if not c: continue
        (H / f"{take}.call.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
        print(take, c["duration"], len(c["prompt"]))
