"""SC01 — HOOK A, THE IMPRESSION (D1, Sunday lunch in May, L-DINING): five Seedance takes (step5/act_map.json, takes.py PASS).
D1 outfits are every person's cast-sheet outfit (wardrobe map), so the sheets go in whole. Taste: HT22 (the room's geography fixed),
HT23 (one continuous moment), HT24 (the line's relationship in frame), HT27 (everyone in frame by a picture), HT25 (only the speaker's mouth moves)."""
import json, math, pathlib
from lib import *
GO = 'chat: "CONFIRMED ALL PROCEED" (2026-10-02) — cast, plates and the step-5 plan confirmed'
TASTE = ["HT22", "HT23", "HT24", "HT25", "HT27"]
OUT = {"N": "an oatmeal cable-knit cardigan buttoned over a navy round-neck top and a mid-grey wool skirt, exactly as on her sheet",
       "C1": "a navy quilted gilet over a pale blue Oxford shirt and tan chinos, exactly as on his sheet",
       "C2": "a grey marl sweatshirt, dark jeans and a thin gold chain, exactly as on her sheet",
       "C3": "a dark green half-zip jumper over a white T-shirt and charcoal chinos, exactly as on his sheet",
       "C4": "a red-and-navy striped long-sleeve T-shirt and navy shorts, exactly as on his sheet"}
WHO = {"N": "Hazel, sixty-seven", "C1": "Roy, seventy, her husband", "C2": "Emma, thirty-nine, their daughter", "C3": "Dan, forty-one, Emma's husband", "C4": "Oscar, four, Emma and Dan's son"}
NAME = {"N": "Hazel", "C1": "Roy", "C2": "Emma", "C3": "Dan", "C4": "Oscar"}
SHEETF = {"N": "cast/N-HAZEL_v1.png", "C1": "cast/C1-ROY_v1.png", "C2": "cast/C2-EMMA_v1.png", "C3": "cast/C3-DAN_v1.png", "C4": "cast/C4-OSCAR_v1.png"}
VM = {k: f"voice/{k}_voice_master.mp3" for k in NAME}
VOICES = {k: json.load(open(B / f"voice/VOICE-{k}.call.json"))["prompt"].split("Delivery: ")[1].split(" Level, even")[0] for k in NAME}
ROOM = ("THE ROOM, fixed in every shot, exactly as in the place reference (Image of the dining room) and the layout card (Image of the table from above): the front room of a Victorian stone terraced house used as the dining room, seen from its doorway — "
        "the long dark oak table runs straight AWAY from the doorway down the middle of the room under a cream cloth; the dark oak sideboard with a table lamp, a fruit bowl and framed photographs along the LEFT wall, a strip of carpet between it and the left-hand chair backs; "
        "the tiled Victorian fireplace with a wooden clock on its mantel and bookshelves in the corner on the RIGHT wall; the bay window with net curtains and green velvet curtains at the FAR end. "
        "THE TABLE, exactly as the layout card shows it, the same in every shot: the Sunday meal is over and cleared of food — one empty white plate with its knife and fork laid together at each of the five places, a clear water glass by each plate, one white china jug in the middle; "
        "no food anywhere, no serving dishes, nothing else on the cloth, and nothing on it changes from shot to shot. "
        "THE SEATS NEVER CHANGE, exactly as in the plate's six chairs: Hazel in the single chair at the FAR end, her back to the bay window; on the LEFT side (the sideboard side) Emma in the far chair next to Hazel and Oscar's chair nearest the doorway; "
        "on the RIGHT side (the fireplace side) Roy in the far chair next to Hazel and Dan in the chair nearest the doorway; the chair at the NEAR end, by the doorway, stays empty. "
        "WHAT IS BEHIND EACH PERSON in their own close shots, every time: behind Hazel the bay window and net curtains with the grey street beyond; behind Roy the fireplace wall, the clock on the mantel and the corner bookshelves; "
        "behind Dan the near end of the fireplace wall; behind Emma the oak sideboard, its lamp and framed photographs; behind Oscar the near end of the sideboard with the fruit bowl. "
        "THE LIGHT: overcast May afternoon daylight, about 6000K, through the bay window at the far end, soft and cool, with the warm cream pendant shade over the table lit; a soft shadow side on every face.")
WALK = ("Oscar does an impression of his nana's walk, earnest, not mocking: on every step his right leg swings stiff and hitches out to the side, his left shoulder dips, "
        "and a small hand reaches out and rests on each ladder-back chair back as he passes it, one chair back about every second. HIS ROUTE, the only route: along the strip of carpet between the LEFT-hand chair backs and the sideboard, never across the front of the table, never round the far end.")

def mf(ids):
    return [("@image" + str(i + 1), x) for i, x in enumerate(ids)]

CARD = "film/cards/INFO-TABLE-SC01_v1.png"
def files_for(cast):
    return [SHEETF[c] for c in cast] + ["plates/L-DINING_v1.png", CARD]

def pack(cast, speakers):
    imgs = [SHEET(WHO[c], OUT[c]) for c in cast] + [PLACE("the dining room of the house, the Sunday table"),
            "is the layout card: the same table from directly above — where the five empty plates, the glasses and the jug sit and which chair is empty; copy the table exactly as it shows, and never cut to this top view."]
    aud = [VOICE(NAME[s]) for s in speakers]
    items = [(f"@image{i+1}", x) for i, x in enumerate(imgs)] + [(f"@audio{i+1}", x) for i, x in enumerate(aud)]
    return manifest(items)

def dur(beats):
    return max(4, math.ceil(sum(ROWS[b]["duration"] for b in beats)))

CALLS = []
def make(beat, covers, cast, speakers, shots, rhythm, start, end, motion, state_txt, extra, focus, scene_neg, title, risks, dialogue_ids, rig_extra=""):
    d = dur(covers)
    dl = " ".join(LN[i] for i in dialogue_ids)
    d = max(d, master_fit(dl)) if dl else d
    assert d <= 15, (beat, d)
    SPK = {"EMMA": "Emma", "HAZEL": "Hazel", "ROY": "Roy", "DAN": "Dan", "OSCAR": "Oscar"}
    import json as _j
    who = [SPK[r["speaker"]] for r in _j.load(open(B / "work/lines.json"))["lines"] if r["id"] in dialogue_ids]
    ordn = ["first", "second", "third", "fourth", "fifth"]
    exch = ("THE EXCHANGE, word for word and in this order: " + dl + " — " + ", ".join(f"{w} says the {ordn[i]} line" for i, w in enumerate(who)) + ".") if len(dialogue_ids) > 1 else ""
    p = " ".join([pack(cast, speakers), SERIES, LOOK, INHERIT, ROOM,
                  multi(len(shots), start, motion != "still", shots, rhythm, end), exch, F2 + rig_extra, PHYS,
                  " ".join(state_txt), " ".join(extra), focus, ONLY_SPEAKER, AUD,
                  negs(NEG_EQUIP, NEG_MORPH, scene_neg, NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND)])
    # Kie caps a call's reference audio at 30 s: with three speakers each master goes in as its first ~10 s, cut at a pause (voice/<k>_voice_ref10.mp3);
    # the master itself stays untouched (§24I part 7)
    auds = [VM[s] for s in speakers] if len(speakers) < 3 else [f"voice/{s}_voice_ref10.mp3" for s in speakers]
    c = call(beat, 1, covers, d, title, files_for(cast), auds, p, start, end, dl, risks, motion, TASTE, GO,
             ingredients=[{"label": NAME[c] + " (cast sheet)", "role": f"@image{i+1}", "kind": "character", "ref": f"stryde-the-impression__{pathlib.Path(SHEETF[c]).stem.replace('_v1','')}"} for i, c in enumerate(cast)]
                        + [{"label": "L-DINING", "role": f"@image{len(cast)+1}", "kind": "location", "ref": "stryde-the-impression__L-DINING"},
                           {"label": "INFO-TABLE-SC01 — the cleared table from above", "role": f"@image{len(cast)+2}", "kind": "info", "note": "the meal over: five empty plates, glasses, one jug, no food; near-end chair empty", "ref": "stryde-the-impression__INFO-TABLE-SC01"}]
                        + [{"label": f"{NAME[s]}'s voice master", "role": f"@audio{i+1}", "kind": "voice", "ref": f"stryde-the-impression__VOICE-{s}"} for i, s in enumerate(speakers)])
    c["act"] = "Hook 1"; c["hook"] = 1; c["generation"] = GEN; c["fix_note"] = FIXN
    CALLS.append(c)

HZ = "Hazel, at the far end of the table, both hands flat on the cloth, still, her face her own age, 67, never aged"
GEN, FIXN = 2, ('chat (user, 2026-10-02): "make the hook consistent review the script guide" — v1 changed the table (food in T1/T4, cleared in T2), the seats (each wide put the family elsewhere), '
                 "Oscar's route (across the front in T1, the far side in T2) and Hazel's background (window, then bookshelves); the script: 'Sunday, the table cleared… crosses the room the way Nana does: the hitch, a hand on every chair back'. "
                 "→ a top-down layout card of the cleared table in every take, the seats fixed to the plate's six chairs, what is behind each person named, one route for Oscar along the sideboard")
make("SC01-T1", ["SC01-SH01", "SC01-SH02", "SC01-SH03", "SC01-SH04"], ["C4", "C3", "C2", "C1", "N"], ["C2", "N"],
     [(0, 4, "WIDE, from the doorway end past the near corner of the table, the cloth's edge soft in the near foreground: Oscar slides off his chair (the left side, nearest the doorway) and walks away from the camera along the strip of carpet between the left-hand chair backs and the sideboard, toward his nana at the far end. " + WALK + " Dan laughs first, a short surprised laugh; then Emma laughs."),
      (4, 5, "MCU, from above Roy's eye line on the right side of the table: Roy, the only one not laughing, looks down at his empty plate and turns his fork over once."),
      (5, 7, "MCU, three-quarter on Emma: her laugh stops in her throat; she turns toward Oscar and says, low and firm: \"Oscar. That’s enough.\""),
      (7, 10, "CU, low and straight on Hazel at the far end, the bay window soft behind her: very still, hands flat on the cloth, her eyes on the boy, she says, quietly: \"No. Let him. Do it again, Oscar.\"")],
     "cutting in quickly on the laugh, then a beat held on Roy, then Emma's line and Hazel's answer close on it",
     "the table cleared after Sunday lunch: Hazel seated at the far end by the bay window; Emma and Oscar on the left side by the sideboard, Roy and Dan on the right side by the fireplace; Oscar sliding off his chair nearest the doorway",
     "Oscar standing at the end of the room by the sideboard, everyone else seated; Hazel at the head of the table, hands flat on the cloth", "travels",
     [state("OSCAR", "his striped T-shirt, both hands free, walking his impression along the sideboard side"), state("THE TABLE", "the five empty plates, glasses and one jug exactly as the layout card shows; no food"), state("HAZEL", "seated at the far end, hands flat on the cloth, face still")],
     [delivery(VOICES["C2"], "she has been laughing at her son and catches her mother's face", "Oscar", "a mother stopping a game that has gone too far", "stops",
               "mid-laugh, shoulders still shaking", "enough", "the laugh is gone from her face", "firm and quiet", "enough", "low and firm, a little breath still in it from laughing",
               "embarrassment for her mother", "a glance at Hazel as she says it"),
      delivery(VOICES["N"], "she has just watched her grandson do her walk in front of everyone", "Emma and Oscar", "a mother overruling her daughter in her own house", "dares",
               "very still, hands flat on the cloth", "again", "her chin lifts a little", "steady, looking at the boy", "again", "quiet, level, a little dry",
               "she wants to see it, however much it hurts", "her thumb pressing once into the tablecloth"),
      listen("Roy", "the laughter", "he knows exactly whose walk it is; his eyes stay on his plate"),
      business("Roy", "the room laughs", "turning his fork over once on his empty plate", "one small turn")],
     "FOCUS: the nearest eye of whoever speaks is sharp; on the wide, Oscar and the table are sharp and the bay window soft. The blur is optical: soft and round, never smeared.",
     "no child running, no child falling, no exaggerated limp, no crutch, no stick, no food on the plates moving by itself, no extra chairs, no extra people, no pets, no lettering or logos",
     "Hook A · T1 — Oscar does Nana's walk; Dan laughs, then Emma; Roy looks at his plate; 'That's enough.' / 'No. Let him. Do it again, Oscar.' (SH01–SH04)",
     [{"risk": "the walk reads as a cruel parody or a fall", "prevented_by": "earnest impression, named body parts at a countable pace, no-fall/no-exaggerated-limp negatives"},
      {"risk": "people swap seats between shots (L24)", "prevented_by": "THE SEATS NEVER CHANGE block, left/right named, NEG-SCENECUT"},
      {"risk": "the wrong person speaks a line (HT25)", "prevented_by": "each line named to its speaker and shot, one voice master per speaker, ONLY_SPEAKER"}],
     ["L001", "L002"])

make("SC01-T2", ["SC01-SH05", "SC01-SH06", "SC01-SH07", "SC01-SH08"], ["C4", "C2", "C3", "N"], ["N", "C2"],
     [(0, 4, "FULL, in profile from across the table on the fireplace side, the sideboard behind him: Oscar does it again, slower, coming back from the far end toward his own chair along the same strip of carpet by the sideboard. " + WALK + " Nobody laughs; the room is silent."),
      (4, 6, "CU, straight on Hazel at the far end: she has watched him all the way; she asks it quietly: \"Is that what I look like?\""),
      (6, 9, "MCU, from slightly above Emma: she puts a hand on Oscar's back as he climbs back onto his chair and says, too quickly: \"He’s four, Mum. He doesn’t see it.\""),
      (9, 11, "MCU, over Emma's shoulder onto Hazel: Hazel turns her head from Emma to Dan and says only: \"Dan?\"")],
     "a silent walk held without a sound, then the question, a quick answer, and a held beat before 'Dan?'",
     "Oscar by the sideboard at the far end of the room, the family seated, silent",
     "everyone seated; Oscar back on his chair beside Emma; Hazel looking at Dan", "travels",
     [state("OSCAR", "doing the walk again, back toward his chair"), state("HAZEL", "seated at the far end, hands flat on the cloth, the same stillness as before")],
     [delivery(VOICES["N"], "she has seen her own walk from the outside for the first time", "the family", "the laughing has stopped", "asks",
               "very still", "look", "her eyes come up from the boy to the table", "plain and steady", "look", "quiet and level, no tremor",
               "she already knows the answer", "a slow breath in before the line"),
      delivery(VOICES["C2"], "she wants this to stop for her mother's sake", "Hazel", "a daughter protecting her mother from the truth", "smooths",
               "a hand on Oscar's back", "four", "her voice lifts brightly", "too brisk", "see", "bright and quick, covering",
               "she has seen it too", "her hand staying on the boy's back a beat too long"),
      listen("Dan", "Emma", "he looks down at his glass, then up when Hazel turns to him"),
      business("Emma", "listening", "steadying Oscar on his chair with one hand on his back", "one steady touch")],
     "FOCUS: the nearest eye of whoever speaks is sharp; on the profile, Oscar is sharp. The blur is optical: soft and round, never smeared.",
     "no laughing in this take, no child running, no exaggerated limp, no extra people, no lettering or logos",
     "Hook A · T2 — he does it again, nobody laughs; 'Is that what I look like?' / 'He's four, Mum…' / 'Dan?' (SH05–SH08)",
     [{"risk": "someone laughs again (the script: nobody laughs)", "prevented_by": "'Nobody laughs; the room is silent', no-laughing negative"},
      {"risk": "Oscar ends up in another seat", "prevented_by": "the fixed seats block, 'back onto his chair' named"},
      {"risk": "Hazel's question played as self-pity", "prevented_by": "DRAMA-DELIVERY: quiet and level, no tremor; NEG-DRAMA"}],
     ["L003", "L004", "L005"])

make("SC01-T3", ["SC01-SH09", "SC01-SH10", "SC01-SH11"], ["C3", "C4", "C2", "N"], ["C3", "C4", "C2"],
     [(0, 2, "MCU, from low on Dan across the table: he holds Hazel's look, puts his water glass down, and says it honestly: \"...A bit.\""),
      (2, 6, "MCU, at Oscar's eye level: Oscar, leaning on the table on his elbows, looks up the table at his nana and asks: \"Nana. Will you walk me to school? When I’m big.\""),
      (6, 12, "MCU, over Dan's shoulder onto Emma: Emma answers for her mother, bright: \"Nana’ll wait in the car, love. Nana’ll see you at the gate.\" Then she and Dan share a look across the table.")],
     "a pause before Dan's two words, the boy straight in, Emma quick and bright, then the silent look held",
     "everyone seated as before, Dan holding his water glass",
     "everyone seated; Emma and Dan holding a look across the table", "still",
     [state("THE FAMILY", "all seated in the same places, the cleared table between them, Hazel still at the far end")],
     [delivery(VOICES["C3"], "he has been asked straight and won't lie to her", "Hazel", "a son-in-law she trusts", "admits",
               "holding his glass", "bit", "he puts the glass down", "gentle and plain", "bit", "low and careful", "he wishes he'd been asked anything else", "the glass set down slowly"),
      delivery(VOICES["C4"], "he wants Nana to walk him to school", "Hazel", "a grandson who adores her", "asks", "leaning on his elbows", "big", "he sits up", "hopeful", "walk",
               "small and clear", "nothing — he means it simply", "his fingers drumming once on the table"),
      delivery(VOICES["C2"], "she is making the plan for everyone, kindly", "Oscar", "a mother managing a hard truth", "manages", "bright", "car", "her eyes go to Dan", "the look to Dan held",
               "gate", "light, brisk", "she thinks her mother can't do it", "the look to Dan"),
      business("Dan", "listening", "turning his water glass a quarter turn on the cloth", "one turn"),
      listen("Hazel", "Emma", "she sees the look pass between Emma and Dan")],
     "FOCUS: the nearest eye of whoever speaks is sharp, the rest of the table softly behind. The blur is optical: soft and round, never smeared.",
     "no laughing, no extra people, no lettering or logos",
     "Hook A · T3 — '…A bit.' / 'Nana. Will you walk me to school?' / 'Nana'll wait in the car…' + the look (SH09–SH11)",
     [{"risk": "Oscar's voice or face drifts from his sheet", "prevented_by": "his sheet + his own voice master, 'four' stated"},
      {"risk": "the look between Emma and Dan is lost", "prevented_by": "named as the shot's last beat, held, in the end position"},
      {"risk": "three voices blur into one", "prevented_by": "three voice masters, each line named to its speaker, ONLY_SPEAKER"}],
     ["L006", "L007", "L008"])

make("SC01-T4", ["SC01-SH12", "SC01-SH13", "SC01-SH14", "SC01-SH15"], ["N", "C2", "C1"], ["N", "C2", "C1"],
     [(0, 2, "CU, in profile on Hazel: she has seen the look; she says it to the table: \"I’ll walk him.\""),
      (2, 3, "MCU, straight on Emma: a warning: \"Mum.\""),
      (3, 5, "MCU, from low on Hazel, three-quarter: louder, in front of everyone: \"I said I’ll walk him.\""),
      (5, 7, "MCU, three-quarter on Roy: gently, not looking up from his plate: \"Hazel. It’s a hill.\"")],
     "quick, overlapping-close but never at once: claim, warning, insistence, then Roy's gentle fact",
     "everyone seated, Emma and Dan just breaking their look",
     "everyone seated, eyes on Hazel", "still",
     [state("HAZEL", "seated at the far end, hands flat on the cloth, the same stillness, now resolved")],
     [delivery(VOICES["N"], "she has decided, in front of everyone", "the family", "a grandmother being managed by her own children", "claims", "still", "walk", "her chin comes up",
               "louder the second time", "said", "level, then firmer and louder", "fear she can't", "her hands pressing flat"),
      business("Roy", "the others speak", "turning his fork over once on his empty plate", "one small turn, then still"),
      delivery(VOICES["C2"], "she doesn't want her mother to promise what she can't do", "Hazel", "daughter to mother", "warns", "sitting forward", "Mum", "nothing", "a single word", "Mum", "low, a warning", "worry", "her eyes going to Roy"),
      delivery(VOICES["C1"], "he loves her and knows the hill", "Hazel", "husband to wife", "warns", "eyes on his plate", "hill", "he looks up at the last word", "gentle", "hill", "soft, kind", "he has been driving her for three years", "the fork going still")],
     "FOCUS: the nearest eye of whoever speaks is sharp. The blur is optical: soft and round, never smeared.",
     "no laughing, no shouting, no standing up, no extra people, no lettering or logos",
     "Hook A · T4 — 'I'll walk him.' / 'Mum.' / 'I said I'll walk him.' / 'Hazel. It's a hill.' (SH12–SH15)",
     [{"risk": "Hazel shouts (played big)", "prevented_by": "'louder' only, DRAMA-DELIVERY firmer not shouting, no-shouting negative"},
      {"risk": "Roy looks at the lens", "prevented_by": "eyes on his plate, NEG-FILM no actor looking into the lens"},
      {"risk": "positions reset", "prevented_by": "the fixed seats block, STATE-CARRY"}],
     ["L009", "L010", "L011", "L012"])

make("SC01-T5", ["SC01-SH16"], ["N", "C1"], ["N"],
     [(0, 4, "CU, straight on Hazel at the far end, the bay window soft behind her: holding Roy's eye, she says it quietly: \"I know what it is.\" She holds his look after the line.")],
     "the line, then the look held to the end",
     "Hazel at the head of the table looking at Roy", "Hazel at the head of the table, still looking at Roy", "still",
     [state("HAZEL", "seated at the far end, hands flat on the cloth, resolved")],
     [delivery(VOICES["N"], "the decision is made", "Roy", "a wife telling her husband she knows exactly what she is taking on", "refuses", "holding his eye", "know",
               "nothing moves but her eyes", "the look held", "know", "quiet and level", "she is frightened of the hill", "a swallow after the line"),
      business("Hazel", "the line is spoken", "her hands resting flat on the tablecloth", "perfectly still")],
     "FOCUS: Hazel's nearest eye is sharp; the bay window falls to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
     "no tears, no smile, no extra people, no lettering or logos",
     "Hook A · T5 — 'I know what it is.' — the hook ends on her face (SH16)",
     [{"risk": "the push-in makes her slide (half-my-age HKB-SH05)", "prevented_by": "a slow push of a few centimetres on a still subject, 'never walks while the camera moves'"},
      {"risk": "she plays it tearful", "prevented_by": "no-tears negative, DRAMA-DELIVERY level"},
      {"risk": "a second voice", "prevented_by": "one voice master, ONLY_SPEAKER"}],
     ["L013"], rig_extra=" " + F1(15))

for c in CALLS:
    (H / "SC01").mkdir(exist_ok=True)
    (H / "SC01" / f"{c['beat']}.call.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
    (H / "SC01" / f"{c['beat']}.prompt.txt").write_text(c["prompt"])
    print(c["beat"], c["duration"], "s", len(c["prompt"]), "chars", len(c["files"]), "imgs", len(c["audios"]), "voices")
