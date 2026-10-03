"""Scene 5 — the builders' yard, Gary, story day D4 (a working morning) — eleven Seedance 2.5 takes on Kie, ingredients only, no frames
(act map takes SC05-T1..T11; this build keeps its pre-V7.96 format and its own takes, PRE_DRAMA — the blocks pasted from Appendix A by ID).
Tony and Gary go in as face-and-hair crops + their D4 outfit cards (HT26); Gary's card carries the strap on his bare right knee all day.
The product shot (T9, SH22) adds the supplied photos: front.webp (the strap) and INFO-PLACEMENT (worn_front.jpg, where it sits).
Every take writes out the same marks on the yard plate, so nobody moves between takes (the lesson of SC01-T2/T3 and SC04-T2):
standing — Gary on the LEFT by the pallets of grey slabs, Tony on the RIGHT facing him; seated (from SC05-SH09a) — side by side on the
edge of the near pallet of grey slabs, Gary on the left, Tony on the right. Lengths: each take's row seconds, raised to the §28H word budget
(unhurried, 2 × s − 2 words). Never trimmed (§24L). Lines that run over several rows are split at sentence ends by the rows' seconds."""
import json, math, re, importlib.util, sys
from pathlib import Path

H = Path(__file__).parent
B = H.parents[1]
_s = importlib.util.spec_from_file_location("sc01", B / "hooks/SC01/build_takes.py"); S1 = importlib.util.module_from_spec(_s); _s.loader.exec_module(S1)
SERIES, LOOK, INHERIT, F2, F1, PHYS, AUD = S1.SERIES, S1.LOOK, S1.INHERIT, S1.F2, S1.F1, S1.PHYS, S1.AUD
NEG_EQUIP, NEG_MORPH, NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND = S1.NEG_EQUIP, S1.NEG_MORPH, S1.NEG_FILM, S1.NEG_SCENECUT, S1.NEG_DRAMA, S1.NEG_SOUND
manifest, FACE, CARD, VOICE, state, focus, negs, dialogue, MULTI_HEAD, SILENT, business = (S1.manifest, S1.FACE, S1.CARD, S1.VOICE, S1.state, S1.focus, S1.negs,
    S1.dialogue, S1.MULTI_HEAD, S1.SILENT, S1.business)
TONY_ID, VOICE_C1 = S1.TONY_ID, S1.VOICE_C1
ROWS = [r for r in json.load(open(B / "step5/act_map.json")) if r["beat"].startswith("SC05")]
L = {x["id"]: x["line"] for x in json.load(open(B / "work/lines.json")) if str(x.get("id", "")).startswith("L0")}

GARY_ID = ("a tall, lean, wiry man of seventy with a shaved, tanned bald head, a strong hooked nose, small bright pale-blue eyes under bushy white brows "
           "and a short neat white beard, straight-backed and springy on his feet")
TONY_D4 = ("a plain grey marl hoodie with the sleeves pushed to the forearm, khaki canvas work shorts above the knee so both knees are bare, grey work socks "
           "and worn tan work boots — exactly his outfit card")
GARY_D4 = ("a sand-coloured canvas work jacket open over a faded black T-shirt, navy work shorts above the knee, rolled grey socks and scuffed brown rigger boots, "
           "and the black knee strap on his bare RIGHT knee only — exactly his outfit card")
VOICE_C3 = ("An Englishman of seventy from Essex: a dry, amused, certain voice, a little hoarse, a builder's directness, broad Essex vowels; "
            "he enjoys being right and isn't arguing. Unhurried, never theatrical.")
PLACE = ("is the place: a builders' merchant's yard on a wet overcast morning — the pallets of grey concrete paving slabs and stacked kerbs in the near LEFT foreground, "
         "the steel racking of plain bagged sand on the left, the open-sided steel shed with the parked yellow forklift at the back, the white flatbed truck loaded with bricks "
         "at the back right, the portable cabin office and the steel yard gate on the right; its wet concrete, puddles and light exactly as shown.")
STRAP = ("is the product — the Stryde knee strap: a rigid black moulded shell with two rounded peaks and a crisp concave notch between them, a small chrome slide at each end "
         "and a flat black woven band; this exact object, nothing redesigned.")
INFO_PLACE = ("is an info card: where the strap sits — across the front of the knee just below the kneecap, the bottom of the kneecap seated into the notch with no gap, "
              "the kneecap's face uncovered; its leg and shorts never appear in the clip.")
STAND = ("THE PLACE OF EVERYONE, fixed for the whole scene: Gary standing on the LEFT beside the near pallet of grey paving slabs, Tony standing on the RIGHT facing him, "
         "an arm's length apart, the white flatbed truck behind them at the back right, the shed with the forklift at the back; the camera stays on this side of them in every shot.")
SEAT = ("THE PLACE OF EVERYONE, fixed for the whole scene: Gary and Tony sitting side by side on the edge of the near pallet of grey paving slabs, Gary on the LEFT, Tony on the RIGHT, "
        "an arm's length apart and turned a little toward each other, their boots on the wet concrete; the white flatbed truck behind them at the back right, the shed with the forklift "
        "at the back; the camera stays on this side of them in every shot.")
DAY = ("THE SCENE SO FAR, a working weekday morning at the builders' yard, story day D4, one continuous moment: bright soft overcast, about 6500K, the sky the single soft source "
       "from above and the left; the concrete wet, puddles holding the grey sky. Gary, seventy, still works the yard; Tony has come in to see him. Nobody else is in the yard.")
NEG_T = ("no long trousers on either man, no knee support or sleeve on Tony, no strap on Tony, no strap on Gary's left knee, no buffalo-check shirt, no third person, "
         "no customers, no forklift moving, no truck moving")
SHOTS_TXT = {"SH-WIDE": "WIDE", "SH-MED": "MEDIUM", "SH-MCU": "MEDIUM CLOSE-UP", "SH-CU": "CLOSE-UP", "SH-OTS": "MEDIUM CLOSE-UP over the other man's shoulder",
             "SH-34": "three-quarter", "SH-EYE": "front-on", "SH-PROFILE": "in clean profile", "SH-LOW": "from low", "SH-HIGH": "from a little high"}
SCALE = {"WIDE": "WIDE", "MEDIUM": "MEDIUM", "MCU": "MEDIUM CLOSE-UP", "CU": "CLOSE-UP"}
WHO = {"C1": "Tony", "C3": "Gary"}
SPK = {"L023": "C1", "L024": "C3", "L025": "C1", "L026": "C3", "L027": "C1", "L028": "C3", "L029": "C1", "L030": "C3", "L031": "C1", "L032": "C3", "L033": "C1",
       "L034": "C3", "L035": "C3", "L036": "C1", "L037": "C3", "L038": "C3", "L039": "C1", "L040": "C3", "L041": "C3", "L042": "C1", "L043": "C3"}
PLAY = {  # the line's job and turn (§24N part 4), one per line
 "L023": ("he has come to ask the one thing he can't work out. Speaking to Gary, half-joking, half not.", "asks it straight. Opens flat; turns on the exact word 'How?', where it becomes a real question; exits on 'than me', a little sore. Stress on 'older'."),
 "L024": ("he has been waiting for someone to ask. Speaking to Tony, wiping his hands.", "teases. One dry question, amused; turns on 'real'. Stress on 'real'."),
 "L025": ("he has tried everything and is fed up. Counting it off to Gary.", "lists it. Opens flat; turns on 'drawer full', a sour little laugh in it; exits on 'Nothing shifts it', final. Stress on 'Nothing'."),
 "L026": ("he has been where Tony is. Matter-of-fact, to Tony.", "levels with him. Opens blunt on 'It won't'; turns on 'worse than you'; exits dry on 'backside'. Stress on 'worse'."),
 "L027": ("he doesn't believe it. To Gary, half a laugh.", "scoffs. Two words, a breath of a laugh. Stress on 'over'."),
 "L028": ("he means it now. To Tony, the joke gone.", "insists. Opens firm on 'I'm serious'; exits plain. Stress on 'everything'."),
 "L029": ("he is hooked. Leaning in to Gary.", "asks. One quiet question. Stress on 'changed'."),
 "L030": ("he wants Tony to find it himself. Seated, turning to him.", "tests him. Opens slow on 'Let me ask you'; turns on 'one spot?', the real question. Stress on 'one'."),
 "L031": ("he has never thought about it. A shrug.", "admits it. Flat, a little lost. Stress on 'round'."),
 "L032": ("he is showing him exactly. Pointing, never touching.", "directs. Short and exact; turns on 'Two fingers'. Stress on 'under'."),
 "L033": ("he has found it and it hurts. Off, under his breath.", "a single word, surprised. Stress on 'There'."),
 "L034": ("he has said this to himself many times. Quiet and sure, to Tony.", "explains. Opens on 'Exactly', certain; turns on 'blame our age', rueful; exits quiet. Stress on 'nobody'."),
 "L035": ("he is giving Tony the thing nobody gave him. Explaining, plain.", "lays it out. Opens on 'not your knee giving up'; turns on 'seventeen times'; exits on 'Nothing more', simple. Stress on 'pressure'."),
 "L036": ("he wants the answer now. To Gary, plain.", "asks straight. Stress on 'fix'."),
 "L037": ("he is counting the things Tony has tried. Counting on his fingers.", "dismisses them one by one; turns on 'None of them'. Stress on 'spot'."),
 "L038": ("he is fond of Tony and sure. Warm, certain.", "reassures and corrects him. Opens warm on 'You're not old, Tony'; turns on 'overloaded'; exits on 'paracetamol', a small smile in it. Stress on 'overloaded'."),
 "L039": ("he is ready to listen. Quiet, to Gary.", "asks. Stress on 'do'."),
 "L040": ("he is showing him the answer on his own knee. Plain, proud of it.", "shows and tells. Opens on 'I took the weight off it'; turns on 'It's a strap', a shrug in it; exits on 'surgeons', matter-of-fact. Stress on 'spot'."),
 "L041": ("he is warning a friend. Wagging a finger, half a smile.", "warns. Opens on 'Don't buy'; turns on 'They stretch'. Stress on 'stretches'."),
 "L042": ("he can't help scoffing. Half a laugh, shaking his head.", "scoffs. Stress on 'strap'."),
 "L043": ("he was the same once and isn't arguing. Grinning, then plain.", "owns it and dares him. Opens grinning on 'I know'; turns on 'That's what changed', plain; exits on 'in a minute', certain. Stress on 'minute'."),
}


def words(t):
    return len(re.findall(r"[A-Za-z0-9’']+", t))


def budget(d):
    return int(2 * d - 2)


def sentences(t):
    return [s.strip() for s in re.findall(r"[^.?!]+[.?!]+", t)]


# each line's sentences go to the rows that carry it, in order, by the rows' seconds
SPLIT = {}
for lid in {r["lines"] for r in ROWS if r.get("lines")}:
    rs = [r for r in ROWS if r.get("lines") == lid]
    sn = sentences(L[lid])
    if len(rs) == 1:
        SPLIT[rs[0]["beat"]] = L[lid]
        continue
    tot = sum(r["duration"] for r in rs); tw = sum(words(s) for s in sn)
    out = {r["beat"]: [] for r in rs}; acc = 0; cum = 0; i = 0
    bounds = []
    for r in rs:
        cum += r["duration"]; bounds.append(cum / tot * tw)
    for s in sn:
        mid = acc + words(s) / 2
        while i < len(rs) - 1 and mid > bounds[i]:
            i += 1
        out[rs[i]["beat"]].append(s); acc += words(s)
    for b, ss in out.items():
        SPLIT[b] = " ".join(ss)

TAKES = []
for t in sorted({r["take"] for r in ROWS}, key=lambda x: int(x.split("T")[-1])):
    rs = [r for r in ROWS if r["take"] == t]
    TAKES.append((t, rs))

STARTS = {}
ENDS = {
 "SC05-T1": "Gary standing on the left by the near pallet of grey slabs, wiping his hands on a rag; Tony standing on the right facing him, an arm's length away",
 "SC05-T2": "Gary and Tony standing face to face by the near pallet of grey slabs as before, Gary on the left, Tony on the right",
 "SC05-T3": "Gary and Tony sitting side by side on the edge of the near pallet of grey slabs, Gary on the left, Tony on the right",
 "SC05-T4": "Gary and Tony sitting side by side on the edge of the pallet as before, Tony's two fingers pressing just below his bare right kneecap",
 "SC05-T5": "Gary and Tony sitting side by side on the pallet as before, Tony looking at his own right knee",
 "SC05-T6": "Gary and Tony sitting side by side on the pallet as before, Tony's forefinger resting just below his right kneecap",
 "SC05-T7": "Gary and Tony sitting side by side on the pallet as before, Gary counting on his fingers",
 "SC05-T8": "Gary and Tony sitting side by side on the pallet as before, Tony quiet",
 "SC05-T9": "Gary standing on the left with his right boot up on the edge of the pallet, his strapped right knee toward Tony, who sits on the pallet on the right",
 "SC05-T10": "Gary sitting back down on the left of the pallet beside Tony, both boots on the concrete, Tony on the right shaking his head",
 "SC05-T11": "Tony sitting alone on the edge of the pallet on the right, looking down at his bare right knee; Gary walking away toward the white flatbed with a slab",
}
prev = ROWS[0]["start_pos"]
for t, rs in TAKES:
    STARTS[t] = prev; prev = ENDS[t]

FILES = {"C1-FACE": "voice/C1_face.jpg", "OUT-C1-D4": "body/SC05/ingredients/OUT-C1-D4_v1.png", "C3-FACE": "voice/C3_face.jpg",
         "OUT-C3-D4": "body/SC05/ingredients/OUT-C3-D4_v1.png", "L-YARD": "plates/L-YARD_v1.png",
         "STRAP": "../../products/stryde/stryde_refs/front.webp", "INFO-PLACEMENT": "../../products/stryde/stryde_refs/worn_front.jpg"}
# Kie caps reference audio at 30 s in total: Gary's master (18.1 s) is cut at its 12.8 s pause (voice/C3_voice_ref13.mp3) so both fit (28.0 s).
AUDIO = {"C1": "voice/C1_voice_master.mp3", "C3": "voice/C3_voice_ref13.mp3"}
GO = "chat: \"confirm and proceed\" (2026-10-03) — SC04 confirmed, on to SC05; the D4 outfit cards and INFO-PLACEMENT wait for the user's Confirm"


def shot_line(n, a, b, r):
    who = WHO[r["subject"]]
    other = "Tony" if who == "Gary" else "Gary"
    lens = SCALE.get(r["scale"], r["scale"])
    view = []
    if r["side"] == "ots":
        lens = f"{lens} over {other}'s shoulder onto {who}, {other}'s shoulder soft in the near frame"
    else:
        lens = f"{lens} on {who}"
        view.append({"three-quarter": "three-quarter", "front": "front-on", "profile": "in clean profile", "behind": "from behind"}.get(r["side"], r["side"]))
    view.append({"eye": "eye height", "low": "from a little low", "high": "from a little high"}.get(r["height"], r["height"]))
    if r["type"] == "INSERT":
        lens = f"CLOSE-UP INSERT"
        view = [{"eye": "eye height", "high": "from a little high", "low": "from low"}.get(r["height"], r["height"])]
    txt = f"SHOT {n}, [{a}s-{b}s]: {lens}, {', '.join(view)}: {r['action']}"
    if "push-in" in (r.get("pace") or ""):
        txt += ", the camera easing in slowly"
    line = SPLIT.get(r["beat"])
    if line and r.get("voice") == "lip-sync":
        txt += f"; {who} says: \"{line}\""
    elif line and r.get("voice") == "off":
        sp = WHO[SPK[r['lines']]]
        txt += f"; {sp}'s line carries on over this shot, spoken off-screen: \"{line}\"" if sp != who or r["type"] == "INSERT" else f"; {who} says, under his breath: \"{line}\""
    elif not line:
        txt += "; nobody speaks"
    return txt + (" " if txt.endswith('"') else ". ")


SHOTS = []
for t, rs in TAKES:
    raw = sum(r["duration"] for r in rs)
    lines = [lid for lid in dict.fromkeys(r["lines"] for r in rs if r.get("lines"))]
    CH = {l: " ".join(SPLIT[r["beat"]] for r in rs if r.get("lines") == l and SPLIT.get(r["beat"])) for l in lines}   # this take's part of each line
    spoken = " ".join(CH[l] for l in lines)
    d = math.ceil(raw)
    while budget(d) < words(spoken):
        d += 1
    # timecodes: each row's share of the take, whole and half seconds, continuous
    marks = [0.0]; acc = 0
    for r in rs:
        acc += r["duration"]; marks.append(round(acc / raw * d * 2) / 2)
    marks[-1] = float(d)
    fmt = lambda x: (str(int(x)) if x == int(x) else str(x))
    seated = int(t.split("T")[-1]) >= 4 or t == "SC05-T3" and False
    layout = SEAT if int(t.split("T")[-1]) >= 4 else STAND
    if t == "SC05-T3":
        layout = STAND + " At the end of this take, on Gary's nod, both sit down side by side on the edge of the near pallet of grey slabs, Gary on the left, Tony on the right, and stay there."
    if t == "SC05-T1":
        layout = ("THE PLACE OF EVERYONE: Gary works between the near pallet of grey paving slabs on the LEFT and the white flatbed truck at the back right; Tony comes in through the steel yard gate "
                  "on the right and stops on the RIGHT facing Gary, an arm's length away; from then on Gary stands on the LEFT by the pallet and Tony on the RIGHT; the camera stays on this side of them.")
    if t == "SC05-T11":
        layout = SEAT + " At the end Gary stands, picks up one slab and walks off toward the white flatbed truck; Tony stays sitting on the right."
    if t in ("SC05-T9", "SC05-T10"):
        layout = SEAT + " Gary stands up from his place on the LEFT to put his right boot up on the edge of the pallet, his strapped right knee toward Tony, and sits back down in the same place on the left after."
    if int(t.split("T")[-1]) < 9:   # STEP4_5: the strap is first seen at SH21 (T9) — before that Gary's knees stay out of every shot
        layout += (" The strap on Gary's right knee is not seen before the later take that shows it: every shot of Gary frames him from the waist up, and in any wider "
                   "shot his knees are hidden — behind the slab he carries, the pallet's edge or Tony.")
    shots = " ".join(shot_line(i + 1, fmt(marks[i]), fmt(marks[i + 1]), r) for i, r in enumerate(rs))
    cast = sorted({c for r in rs for c in r["cast"]}, key=lambda c: ["C3", "C1"].index(c))
    voices = sorted({SPK[l] for l in lines}, key=lambda c: ["C3", "C1"].index(c))
    product = any("front.webp" in r["ingredients"] for r in rs)
    items, files, n = [], [], 1
    for c in ["C3", "C1"]:
        nm = WHO[c]
        items += [(f"@image{n}", FACE(nm, "his")), (f"@image{n+1}", CARD(nm, TONY_D4.split(' — ')[0] if c == "C1" else GARY_D4.split(' — ')[0]))]
        files += [f"{c}-FACE", f"OUT-{c}-D4"]; n += 2
    items.append((f"@image{n}", PLACE)); files.append("L-YARD"); n += 1
    if product:
        items += [(f"@image{n}", STRAP), (f"@image{n+1}", INFO_PLACE)]; files += ["STRAP", "INFO-PLACEMENT"]; n += 2
    for k, c in enumerate(voices):
        items.append((f"@audio{k+1}", VOICE(WHO[c])))
    exchange = ""
    if lines:
        exchange = ("THE EXCHANGE, word for word and in this order: " + spoken + " — " +
                    "; then ".join(f"{WHO[SPK[l]]} says \"{CH[l]}\"" for l in lines) + "; each line spoken only by the man named. ")
    dlg = [dialogue(WHO[SPK[l]], CH[l], VOICE_C3 if SPK[l] == "C3" else VOICE_C1, PLAY[l][0], PLAY[l][1],
                    f"{'dry, a little hoarse, unhurried' if SPK[l] == 'C3' else 'low, rough and flat'}, continuing from how he sounded on his last line, matching the face in this shot.",
                    "what he really thinks leaks only through his eyes, never his voice.") for l in lines]
    prompt = " ".join([
        manifest(items), SERIES, LOOK, INHERIT, DAY,
        f"Gary is {GARY_ID}, in {GARY_D4}. Tony is {TONY_ID}, in {TONY_D4}.",
        layout,
        MULTI_HEAD(len(rs), STARTS[t], not any(k in (rs[0].get("pace") or "") for k in ("walks", "sit-down", "move"))),
        exchange + shots +
        "Each cut lands on a completed line, action or reaction. The eyelines match across every reverse: Gary looks right to Tony, Tony looks left to Gary. Nobody looks into the lens. "
        f"Last frame: {ENDS[t]}.",
        F2, PHYS,
        business("whichever man is listening", "resting them still on his knees, or at his sides when standing, until his own line or action comes"),
        state("GARY", "easy and certain, in the outfit of his card" + (", the strap on his bare right knee" if int(t.split("T")[-1]) >= 9 else ", framed from the waist up"), "nothing"),
        state("TONY", "tired and doubtful, in the outfit of his card, both knees bare", "nothing"),
        focus("the nearest eye of whoever is speaking", "the yard behind falls to a soft, recognisable shape"),
        *dlg, AUD if lines else SILENT,
        negs(NEG_EQUIP, NEG_MORPH, NEG_T, "no man saying the other's line, no one standing or sitting but as written, no one swapping sides, no new places",
             NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)])
    SHOTS.append(dict(beat=t, covers=[r["beat"] for r in rs], duration=d, raw=round(raw, 1), line=spoken,
                      files=files, audios=voices, prompt=prompt, start=STARTS[t], end=ENDS[t],
                      title=f"Scene 5 · {t.split('-')[1]} — " + (" · ".join(f"\"{CH[l][:28]}…\"" for l in lines) or rs[0]["action"][:50]) + f" ({rs[0]['beat'].split('-')[1]}–{rs[-1]['beat'].split('-')[1]})",
                      risks=[{"risk": "the voices swap or the wrong man speaks a line", "prevented_by": "Audio refs named, every line named with its speaker, swap negatives"},
                             {"risk": "the men change places between shots or takes", "prevented_by": "the marks written out in every take (Gary left, Tony right), STILL head, place negatives"},
                             {"risk": "the sheet clothes return or the strap moves knee", "prevented_by": "face crops + D4 outfit cards, strap-on-right-knee-only negatives (HT26)"}]))

if __name__ == "__main__":
    approved = "--approved" in sys.argv
    for s in SHOTS:
        call = {"beat": s["beat"], "build": "stryde-her-dad", "connector": "seedance", "model": "bytedance/seedance-2-5", "mode": 4, "kind": "multi", "prompt": s["prompt"],
                "take": s["beat"], "covers": s["covers"], "start_pos": s["start"], "end_pos": s["end"], "duration": s["duration"], "resolution": "720p",
                "aspect_ratio": "9:16", "start_image": None, "ingredients_approved": approved, "files": [FILES[f] for f in s["files"]],
                "audios": [AUDIO[a] for a in s["audios"]], "generate_audio": bool(s["line"]), "dialogue": s["line"] or None, "script_line": s["line"] or None,
                "pace": "unhurried", "subject_motion": "still", "prefer_multi_shots": "false", "generation": 1, "user_go": GO, "legacy_build": True,
                "risks": s["risks"], "scene": 5, "title": s["title"], "taste": ["HT02", "HT17", "HT18", "HT22", "HT23", "HT26", "HT27"]}
        (H / f"{s['beat']}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{s['beat']}.prompt.txt").write_text(s["prompt"])
        print(s["beat"], s["duration"], "s (rows", s["raw"], ")", len(s["prompt"]), "chars", s["files"], s["audios"])
