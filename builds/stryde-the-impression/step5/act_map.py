#!/usr/bin/env python3
"""§18 step 5 — act map (E4 rows) for stryde-the-impression: Mode 4 film on Seedance 2.5, one take per connected run (§24K part 5).
Writes act_map.json — the input for angles.py, takes.py and wardrobe.py. Cut order = story order: SC01 (the hook) … SC16 (the close).
Lines are L-ids from work/lines.json; durations are estimated at the inspo's 165 wpm (E6, no voice master over dialogue)."""
import json, math, pathlib
HERE = pathlib.Path(__file__).parent
LINES = {r["id"]: r for r in json.load(open(HERE.parent / "work/lines.json"))["lines"]}
ROWS = []
NAMES = {"N": "Hazel", "C1": "Roy", "C2": "Emma", "C3": "Dan", "C4": "Oscar", "C5": "Wendy", "X1": "the assistant", "X2": "the mum", "X3": "the lollipop lady", "X4": "Wendy's grandchildren"}

def L(src, key, time, arc, k, why=None):
    d = {"source": src, "key_side": key, "time": time, "arc": arc, "kelvin": k}
    if why: d["why"] = why
    return d

def dur(lines, extra=0.0, say=None):
    w = len(say.split()) if say else (sum(len(LINES[i]["text"].split()) for i in lines.split()) if lines else 0)
    return round(max(1.2, w / 2.75 + (0.3 if w else 0) + extra), 1)

CUR = {}
def scene(g, day, loc, light, music, spine, state):
    CUR.update(g=g, day=day, loc=loc, light=light, music=music, spine=spine, state=state)

def R(beat, typ, subj, h, side, scale, fg, why, shot, plane, dof, lines, action, take, rig="F2", cast=(), speaking=None, product=False,
      cue="", pace="", ing=(), mirror=None, moving=False, face=True, extra=0.0, kind=None, start=None, end=None, split=None, playing="",
      loc=None, light=None, day=None, pinned=False, say=None):
    d = dur(lines, extra, say)
    if say: assert say in LINES[lines]["text"], (beat, say)
    row = {"beat": f'{CUR["g"]}-{beat}', "group": CUR["g"], "scene": CUR["g"], "type": typ, "subject": subj, "height": h, "side": side,
           "scale": scale, "fg": fg, "why": why, "mode": 4, "shot": shot,
           "speaking": bool(lines) if speaking is None else speaking, "product_beat": product,
           "focus": {"plane": plane, "dof": dof, "rack": None, "moving_subject": moving}, "story_day": day or CUR["day"], "face": face,
           "light": light or CUR["light"], "lines": lines, "line_text": (f'{NAMES.get(LINES[lines]["speaker"][:2], LINES[lines]["speaker"].title())}: …{say}…' if say else " / ".join(f'{NAMES.get(LINES[i]["speaker"][:2], LINES[i]["speaker"].title())}: {LINES[i]["text"]}' for i in lines.split())) if lines else "",
           "action": action, "business": action, "pace": pace, "rig": rig, "camera": rig, "cast": list(cast), "location": loc or CUR["loc"], "cut": cue, "cut_cue": cue,
           "ingredients": list(ing), "mirror_of": mirror, "duration": d, "music": CUR["music"], "spine": CUR["spine"], "state": CUR["state"],
           "playing": playing, "say": say, "take": f'{CUR["g"]}-{take}', "layout": "full"}
    if pinned: row["pinned"] = True
    if kind: row["take_kind"] = kind
    if start: row["start_pos"] = start
    if end: row["end_pos"] = end
    if split: row["split"] = split
    ROWS.append(row)

HAZ_BEFORE = "Hazel: the walk of a woman of 80 — a hitch on the right knee, a hand on every chair back and wall, the left shoulder dipping; face her own age, 67, never aged"
HAZ_AFTER = "Hazel: the same woman, an ordinary even walk, hands free; the strap unseen under her trousers"

# ======== SC01 — HOOK: THE IMPRESSION (D1 Sunday lunch, L-DINING) ========
scene("SC01", "D1", "L-DINING", L("the bay window, overcast May afternoon", "L", "afternoon", "Before — cool overcast daylight, one warm pendant", 6000),
      "MUS-OPEN", "plant: the impression; want: walk Oscar to school", HAZ_BEFORE)
R("SH01", "SHOT", "C4", "eye", "three-quarter", "WIDE", "through", "past the end of the table: the whole family and the child crossing behind their chairs — everyone sees it at once", ["SH-WIDE", "SH-FGFOC"], "deep", "deep",
  "", "Oscar slides off his chair and crosses the room behind the chairs the way Nana does: a hitch on his right leg, a small hand on every chair back, his left shoulder dipping; Dan laughs first, then Emma", "T1", "F2", ["C4", "C3", "C2", "C1", "N"],
  cue="as Emma's laugh starts", pace="one chair back per second, five chairs", extra=4.0, moving=True, kind="multi",
  start="the table cleared after Sunday lunch: Hazel seated at the far end by the bay window, Roy on her left, Emma and Dan on the near side, Oscar sliding off his chair beside Emma", ing=["C4", "C3", "C2", "C1", "N", "L-DINING", "P-HOUSE"])
R("SH02", "SHOT", "C1", "high", "three-quarter", "MCU", "clean", "high on Roy: a man looking down and away — he has seen this walk for three years", ["SH-34", "SH-HIGH"], "eyes", "shallow",
  "", "Roy, the only one not laughing, looks down at his plate and moves a pea with his fork", "T1", cast=["C1"], cue="on his eyes dropping", pace="still, one small fork move", extra=1.0, playing="hides")
R("SH03", "SHOT", "C2", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow",
  "L001", "Emma's laugh stops in her throat; she turns to Oscar", "T1", cast=["C2"], cue="on 'enough.'", pace="still", playing="stops")
R("SH04", "SHOT", "N", "low", "front", "CU", "clean", "low on Hazel: she takes charge of her own humiliation", ["SH-CU", "SH-LOW"], "eyes", "shallow",
  "L002", "Hazel, very still at the head of the table, hands flat on the cloth, eyes on the boy", "T1", cast=["N"], cue="on 'Oscar.'", pace="still", playing="dares",
  end="Oscar standing at the end of the room by the sideboard, everyone else seated; Hazel at the head of the table, hands flat on the cloth")
R("SH05", "SHOT", "C4", "eye", "profile", "FULL", "clean", "profile: the walk itself, end to end, now with no laughter over it", ["SH-PROFILE"], "deep", "deep",
  "", "Oscar does it again, slower, behind the chairs back to his seat — the hitch, the hand on every chair back, the shoulder dip; nobody laughs", "T2", cast=["C4"], cue="as he reaches his chair",
  pace="one chair back per second", extra=4.0, moving=True, kind="multi", split="length", start="Oscar by the sideboard at the far end of the room, the family seated, silent")
R("SH06", "SHOT", "N", "eye", "front", "CU", "clean", "", ["SH-CU", "SH-EYE"], "eyes", "shallow",
  "L003", "Hazel watches him all the way, then asks it quietly", "T2", rig="F1", cast=["N"], cue="on 'like?'", pace="a slow push-in over the line", playing="asks")
R("SH07", "SHOT", "C2", "high", "three-quarter", "MCU", "clean", "high on Emma: smaller, caught", ["SH-34", "SH-HIGH"], "eyes", "shallow",
  "L004", "Emma, a hand on Oscar's back as he climbs onto his chair, too quick", "T2", cast=["C2", "C4"], cue="on 'see it.'", pace="still", playing="smooths")
R("SH08", "SHOT", "N", "eye", "ots", "MCU", "through", "over Emma's shoulder: Hazel turns from her daughter to the one who will tell the truth", ["SH-OTS"], "eyes", "medium",
  "L005", "Hazel turns her head from Emma to Dan", "T2", cast=["N", "C2"], cue="on 'Dan?'", pace="one head turn", playing="tests",
  end="everyone seated; Oscar back on his chair beside Emma; Hazel looking at Dan")
R("SH09", "SHOT", "C3", "low", "three-quarter", "MCU", "clean", "low on Dan: the honest one, cornered", ["SH-34", "SH-LOW"], "eyes", "shallow",
  "L006", "Dan holds Hazel's look, puts his glass down", "T3", cast=["C3"], cue="on 'bit.'", pace="a pause, then the glass down", extra=1.0, playing="admits", kind="multi", split="length",
  start="everyone seated as before, Dan holding his water glass")
R("SH10", "SHOT", "C4", "eye", "three-quarter", "MCU", "clean", "", ["SH-34", "SH-EYE"], "eyes", "shallow",
  "L007", "Oscar, leaning on the table on his elbows, looks up at Nana", "T3", cast=["C4"], cue="on 'big.'", pace="still", playing="asks")
R("SH11", "SHOT", "C2", "eye", "ots", "MCU", "through", "over Dan's shoulder: Emma answering for her mother", ["SH-OTS"], "eyes", "shallow",
  "L008", "Emma answers for her mother, bright; then she and Dan share a look across the table", "T3", cast=["C2", "C3"], cue="on the look", pace="still", extra=1.0, playing="manages",
  end="everyone seated; Emma and Dan holding a look across the table")
R("SH12", "SHOT", "N", "eye", "profile", "CU", "clean", "profile: she sees the look and answers it", ["SH-PROFILE", "SH-CU"], "eyes", "shallow",
  "L009", "Hazel, who saw the look, says it to the table", "T4", cast=["N"], cue="on 'him.'", pace="still", playing="claims", kind="multi", split="length",
  start="everyone seated, Emma and Dan just breaking their look")
R("SH13", "SHOT", "C2", "eye", "front", "MCU", "clean", "", ["SH-EYE"], "eyes", "shallow",
  "L010", "Emma, a warning", "T4", cast=["C2"], cue="on 'Mum.'", pace="still", playing="warns")
R("SH14", "SHOT", "N", "low", "three-quarter", "MCU", "clean", "low: she raises her voice once and owns it", ["SH-34", "SH-LOW"], "eyes", "shallow",
  "L011", "Hazel, louder, in front of everyone", "T4", cast=["N"], cue="on 'him.'", pace="still", playing="insists")
R("SH15", "SHOT", "C1", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow",
  "L012", "Roy, gently, not looking up", "T4", cast=["C1"], cue="on 'hill.'", pace="still", playing="warns", end="everyone seated, eyes on Hazel")
R("SH16", "SHOT", "N", "eye", "front", "CU", "clean", "", ["SH-CU", "SH-EYE"], "eyes", "shallow",
  "L013", "Hazel, holding Roy's eye; the hook ends on her face", "T5", rig="F1", cast=["N"], cue="end of line, hold", pace="a slow push-in", extra=1.0, playing="refuses",
  split="length", start="Hazel at the head of the table looking at Roy", end="Hazel at the head of the table, still looking at Roy")

# ======== SC02 — THE FILM (D1 night, the hall, P-HOUSE) ========
scene("SC02", "D1", "P-HOUSE", L("the hall pendant and the kitchen light behind", "R", "night", "Before — tungsten night", 3000),
      "MUS-OPEN", "obstacle: she sees herself", HAZ_BEFORE)
R("SH01", "SHOT", "N", "eye", "three-quarter", "MEDIUM", "clean", "", ["SH-MED", "SH-34"], "eyes", "medium",
  "L014", "Hazel, coat off, holds her phone out to Emma at the foot of the stairs", "T1", cast=["N", "C2"], cue="on 'door.'", pace="one reach", playing="asks",
  kind="multi", start="night, the hall lit by the pendant; Hazel and Emma by the front door, Emma in her coat about to leave, Hazel holding out her phone")
R("SH02", "SHOT", "C2", "eye", "ots", "MCU", "through", "over Hazel's shoulder: Emma doesn't want this", ["SH-OTS"], "eyes", "shallow",
  "L015", "Emma takes the phone, not wanting to", "T1", cast=["C2", "N"], cue="on 'Why?'", pace="still", playing="resists")
R("SH03", "SHOT", "N", "high", "front", "CU", "clean", "high on Hazel: small and plain about it", ["SH-CU", "SH-HIGH"], "eyes", "shallow",
  "L016", "Hazel, already turning to walk to the kitchen door", "T1", cast=["N"], cue="on 'seen it.'", pace="still, then turning", playing="decides")
R("SH03b", "SHOT", "C2", "eye", "profile", "MCU", "clean", "profile: she raises it like a weight", ["SH-PROFILE"], "eyes", "shallow",
  "", "Emma lifts the phone to frame the hall, reluctant, as her mother walks away to the kitchen door", "T1", cast=["C2"], cue="as the phone comes up", pace="one slow lift", extra=1.5, speaking=False,
  end="Hazel at the kitchen door at the far end of the hall; Emma by the front door with the phone up")
R("SH04", "SHOT", "N", "eye", "front", "FULL", "clean", "the phone's view, from the front door down the hall — the same frame both films use", ["SH-POV", "SH-EYE"], "deep", "deep",
  "", "Hazel walks from the kitchen door to the front door toward the camera: the hitch on the right knee, a hand on the wall, the radiator, the newel post, the left shoulder dipping", "T2",
  rig="F2", cast=["N"], cue="as she reaches the door", pace="one step per second, eight steps", extra=7.0, moving=True, face=True, speaking=False, split="length",
  start="Hazel at the open kitchen door at the far end of the hall, facing down the hall toward the camera at the front door", end="Hazel at the front door, a hand on the newel post")
R("SH05", "SHOT", "N", "eye", "three-quarter", "CU", "clean", "", ["SH-CU", "SH-34"], "eyes", "shallow",
  "", "Hazel watches the clip once on the phone in her hand, the screen's light on her face, the screen unseen", "T3", rig="F1", cast=["N"], cue="as the clip ends", pace="still, a slow push-in", extra=3.0, speaking=False, playing="takes it in",
  kind="multi", split="length", start="Hazel by the front door holding the phone, Emma beside her")
R("SH06", "SHOT", "C2", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow",
  "L017", "Emma, too quickly", "T3", cast=["C2"], cue="on 'bad.'", pace="still", playing="soothes")
R("SH07", "SHOT", "N", "low", "three-quarter", "CU", "clean", "low: the line that matters", ["SH-CU", "SH-LOW"], "eyes", "shallow",
  "L018", "Hazel, eyes still on the phone", "T3", cast=["N"], cue="on 'hand.'", pace="still", playing="admits")
R("SH08", "SHOT", "C2", "eye", "ots", "MCU", "through", "over Hazel's shoulder", ["SH-OTS"], "eyes", "shallow",
  "L019", "Emma puts a hand on her mother's arm", "T3", cast=["C2", "N"], cue="on 'Mum.'", pace="one touch", playing="reassures", end="the two of them at the front door, Emma's hand on Hazel's arm")
R("SH09", "SHOT", "N", "eye", "front", "CU", "clean", "", ["SH-CU", "SH-EYE"], "eyes", "shallow",
  "L020", "Hazel looks up from the phone at her daughter", "T4", cast=["N"], cue="on 'Am I.'", pace="still", playing="asks", kind="multi", split="length",
  start="the two of them at the front door, Emma's hand on Hazel's arm")
R("SH10", "SHOT", "N", "eye", "profile", "MCU", "clean", "profile: she says it to the hall, not to Emma", ["SH-PROFILE"], "eyes", "shallow",
  "L021", "Hazel looks back down the hall she just walked", "T4", cast=["N"], cue="on 'walk.'", pace="still", playing="names it", end="Hazel by the front door looking down the hall")

# ======== SC03 — THE CHEMIST (D2, L-CHEMIST) ========
scene("SC03", "D2", "L-CHEMIST", L("the shop window and ceiling panels", "R", "morning", "Problem — cool white shop light", 5000),
      "MUS-EXPOSE", "failed fix: the stick, the sleeve", HAZ_BEFORE)
R("SH01", "SHOT", "N", "eye", "three-quarter-back", "FULL", "through", "past the rack: her at the hooks, the assistant coming", ["SH-REAR", "SH-FGFOC"], "deep", "deep",
  "L022", "Hazel at the rack of hooks, a hand on the shelf edge for balance; the young assistant comes over from the counter", "T1", cast=["N", "X1"], cue="on 'all?'", pace="the assistant's three steps",
  kind="multi", start="Hazel at the hook rack on the left wall, the assistant behind the white counter")
R("SH02", "SHOT", "N", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow",
  "L023", "Hazel, plain and specific", "T1", cast=["N"], cue="on 'four-year-old.'", pace="still", playing="specifies")
R("SH03", "SHOT", "X1", "eye", "ots", "MCU", "through", "over Hazel's shoulder onto the assistant's kind sales face", ["SH-OTS"], "eyes", "shallow",
  "L024", "the assistant, helpful, glancing at the stand of walking sticks", "T1", cast=["X1", "N"], cue="on 'run.'", pace="one glance", playing="suggests",
  end="the two of them at the hook rack, the assistant nodding at the stick stand by the counter")
R("SH04", "SHOT", "N", "high", "three-quarter", "CU", "clean", "high: the word lands on her", ["SH-CU", "SH-HIGH"], "eyes", "shallow",
  "L025", "Hazel looks at the sticks", "T2", cast=["N"], cue="on 'stick.'", pace="still", playing="weighs", kind="multi", split="length",
  start="the two of them at the hook rack")
R("SH05", "SHOT", "X1", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow",
  "L026", "the assistant starts her line", "T2", cast=["X1"], cue="cut off on 'find...'", pace="still", playing="sells")
R("SH06", "SHOT", "N", "eye", "front", "MCU", "clean", "", ["SH-EYE"], "eyes", "shallow",
  "L027", "Hazel, cutting her off, kindly", "T2", cast=["N"], cue="on 'well.'", pace="still", playing="refuses")
R("SH07", "INSERT", "N", "eye", "profile", "CU", "clean", "her hand and the hook: the habit", ["SH-CU", "SH-PROFILE"], "hands", "shallow",
  "", "Hazel's hand takes a beige elastic knee sleeve in its clear packet off the hook", "T2", cast=["N"], cue="as it comes off the hook", pace="one move", face=False, extra=1.5, speaking=False,
  end="Hazel holding the boxed beige sleeve, the assistant beside her")
R("SH08", "SHOT", "X1", "low", "three-quarter", "MCU", "clean", "low on the assistant behind the counter: the sale", ["SH-34", "SH-LOW"], "eyes", "shallow",
  "L028", "the assistant at the till, eyes on the packet", "T3", cast=["X1"], cue="on 'large.'", pace="still", playing="helps", kind="multi", split="length",
  start="Hazel at the counter putting the beige sleeve down, the assistant at the till")
R("SH09", "SHOT", "N", "eye", "three-quarter", "CU", "clean", "", ["SH-CU", "SH-34"], "eyes", "shallow",
  "L029", "Hazel, flat, paying", "T3", cast=["N"], cue="on 'them.'", pace="still", playing="confesses", end="Hazel at the counter, paying")

# ======== SC04 — THE DRAWER (D3, L-BEDROOM) ========
scene("SC04", "D3", "L-BEDROOM", L("the sash window", "L", "afternoon", "Problem — flat grey afternoon", 6000),
      "MUS-EXPOSE", "failed fixes counted", HAZ_BEFORE)
R("SH01", "INSERT", "C2", "overhead", "front", "CU", "clean", "overhead into the drawer: the count is the picture", ["SH-OVER", "SH-CU"], "foreground", "shallow",
  "L030", "Emma pulls open the stuck second drawer: it is packed with beige elastic knee sleeves, many still in their packets", "T1", cast=["C2"], cue="on 'this?'", pace="one pull", face=False,
  kind="multi", start="Emma kneeling at the oak chest of drawers looking for something, Hazel coming in at the bedroom door")
R("SH02", "SHOT", "N", "eye", "three-quarter", "MEDIUM", "through", "through the door: she arrives, too late", ["SH-MED", "SH-OCCL"], "eyes", "medium",
  "L031", "Hazel in the doorway, one hand on the door frame", "T1", cast=["N"], cue="on 'it.'", pace="still", playing="blocks")
R("SH03", "SHOT", "C2", "high", "three-quarter-back", "MCU", "clean", "high over Emma at the drawer, sleeves in her hands", ["SH-REAR", "SH-HIGH"], "eyes", "medium",
  "L032", "Emma lifts a handful of the sleeves", "T1", cast=["C2"], cue="on 'here.'", pace="one lift", playing="counts")
R("SH04", "SHOT", "N", "eye", "front", "MCU", "clean", "", ["SH-EYE"], "eyes", "shallow",
  "L033", "Hazel, exact", "T1", cast=["N"], cue="on 'Tuesday.'", pace="still", playing="corrects", end="Emma kneeling at the open drawer with sleeves in her hands; Hazel in the doorway")
R("SH05", "SHOT", "C2", "low", "three-quarter", "MCU", "clean", "low on Emma looking up at her mother", ["SH-34", "SH-LOW"], "eyes", "shallow",
  "L034", "Emma looks up from the drawer", "T2", cast=["C2"], cue="on 'them?'", pace="still", playing="questions", kind="multi", split="length",
  start="Emma kneeling at the open drawer, Hazel in the doorway")
R("SH06", "SHOT", "N", "eye", "three-quarter", "CU", "clean", "", ["SH-CU", "SH-34"], "eyes", "shallow",
  "L035", "Hazel comes in and sits on the edge of the bed", "T2", cast=["N"], cue="on 'one.'", pace="one slow sit", playing="admits")
R("SH07", "SHOT", "C2", "eye", "ots", "MCU", "through", "over Hazel's shoulder", ["SH-OTS"], "eyes", "shallow",
  "L036", "Emma", "T2", cast=["C2", "N"], cue="on 'Why?'", pace="still", playing="presses", end="Hazel on the bed edge; Emma kneeling at the drawer")
R("SH08", "SHOT", "N", "eye", "profile", "MCU", "clean", "profile: she says it to the window", ["SH-PROFILE"], "eyes", "shallow",
  "L037", "Hazel on the bed edge, looking at the window, a sleeve turning in her hands", "T3", cast=["N"], cue="on 'that.'", pace="the sleeve turned once", playing="explains",
  say="Because the girl in the shop said it was supportive. They all say that.", kind="multi", split="length", start="Hazel on the bed edge with a sleeve in her hands; Emma kneeling at the open drawer")
R("SH09", "INSERT", "N", "high", "three-quarter", "CU", "clean", "high on her hands: the sleeve stretched round her fist — round and round", ["SH-CU", "SH-HIGH"], "hands", "shallow",
  "L037", "Hazel pulls the beige sleeve over her fist and lets it go slack", "T3", cast=["N"], cue="on 'hill.'", pace="one pull", face=False, playing="shows it",
  say="They all go round. And I still stop halfway up that hill.", end="Hazel on the bed edge with a sleeve in her hands; Emma kneeling at the drawer")

# ======== SC05 — THE HILL, JULY (D4, L-HILL) ========
scene("SC05", "D4", "L-HILL", L("the open overcast sky", "back", "morning", "Problem — flat overcast morning", 6500, "the open sky behind her as she climbs"),
      "MUS-EXPOSE", "the obstacle: halfway, the postbox", HAZ_BEFORE + "; number twenty-four under her trousers")
R("SH01", "SHOT", "N", "low", "three-quarter-back", "WIDE", "clean", "low from the bottom of the hill: the whole climb above her", ["SH-WIDE", "SH-LOW"], "deep", "deep",
  "", "Hazel climbs the steep pavement alone at 8:40, her right hand trailing along the top of the stone wall, the hitch, stopping every few steps", "T1", rig="F2", cast=["N"], cue="as she nears the postbox",
  pace="slow, a stop every four steps", extra=6.0, moving=True, face=False, speaking=False, kind="multi",
  start="Hazel on the pavement at the bottom of the hill by the stone wall, facing uphill, her back to the camera; the mum with a buggy at the top of the pavement coming down")
R("SH02", "SHOT", "N", "eye", "profile", "MEDIUM", "clean", "profile at the postbox: the line she can't pass", ["SH-PROFILE", "SH-MED"], "eyes", "medium",
  "L038", "Hazel stops at the pillar box, a hand flat on the wall, breathing; the mum with the buggy coming down the hill pauses beside her", "T1", cast=["N", "X2"], cue="on 'love?'", pace="breathing")
R("SH03", "SHOT", "N", "eye", "ots", "CU", "through", "over the mum's shoulder onto Hazel's polite face", ["SH-OTS", "SH-CU"], "eyes", "shallow",
  "L039", "Hazel, a polite smile", "T1", cast=["N", "X2"], cue="on 'knee.'", pace="still", playing="deflects")
R("SH04", "SHOT", "N", "high", "behind", "FULL", "clean", "high behind her: she turns back down — the hill wins", ["SH-REAR", "SH-HIGH"], "deep", "deep",
  "", "Hazel turns round and walks back down the hill, a hand on the wall, the mum and buggy going on ahead", "T1", cast=["N", "X2"], cue="as she turns", pace="slow, one step at a time", extra=3.0, moving=True, face=False,
  speaking=False, end="Hazel walking back down the hill below the postbox")

# ======== SC06 — THE CAR (D5, L-KITCHEN) ========
scene("SC06", "D5", "L-KITCHEN", L("the back window over the sink", "R", "afternoon", "Problem — warm afternoon, a soft room", 5600),
      "MUS-EXPOSE", "failed fix: the car", HAZ_BEFORE)
R("SH01", "SHOT", "C1", "eye", "three-quarter", "MEDIUM", "clean", "", ["SH-MED", "SH-34"], "eyes", "medium",
  "L040", "Roy, making two mugs of tea at the worktop, says it with his back half turned — the plan already made", "T1", cast=["C1", "N"], cue="on 'yards.'", pace="stirring", playing="arranges",
  kind="multi", start="Roy at the worktop by the sink making tea, Hazel sitting at the square pine table")
R("SH02", "SHOT", "N", "eye", "front", "MCU", "clean", "", ["SH-EYE"], "eyes", "shallow",
  "L041", "Hazel at the table, repeating it", "T1", cast=["N"], cue="on 'yards.'", pace="still", playing="weighs")
R("SH03", "SHOT", "C1", "low", "three-quarter", "MCU", "clean", "low on Roy: kind, certain, wrong", ["SH-34", "SH-LOW"], "eyes", "shallow",
  "L042", "Roy puts her mug down in front of her", "T1", cast=["C1"], cue="on 'love.'", pace="one move", playing="reassures")
R("SH04", "SHOT", "N", "high", "three-quarter", "CU", "clean", "high on her at the table: she knows it isn't", ["SH-CU", "SH-HIGH"], "eyes", "shallow",
  "L043", "Hazel, not touching the tea", "T1", cast=["N"], cue="on 'thing.'", pace="still", playing="refuses", end="Hazel at the table with the mug, Roy standing by her")
R("SH05", "SHOT", "C1", "eye", "ots", "MCU", "through", "over Hazel's shoulder: his last word on it", ["SH-OTS"], "eyes", "shallow",
  "L044", "Roy, gently, a hand on the back of her chair", "T2", cast=["C1", "N"], cue="on 'do.'", pace="still", playing="pleads", extra=1.0, split="length",
  start="Hazel at the table, Roy standing behind her chair", end="Roy's hand on the back of her chair")

# ======== SC07 — SIDEWAYS (D5 evening, the hall from the kitchen door, P-HOUSE / L-STAIRS) ========
scene("SC07", "D5", "L-STAIRS", L("the hall pendant", "L", "evening", "Problem — tungsten evening", 3000),
      "MUS-EXPOSE", "plant: Roy's sideways stairs", "Roy: comes down sideways, one step at a time, a hand on the banister; Hazel watching unseen")
R("SH01", "SHOT", "C1", "eye", "three-quarter-back", "FULL", "through", "from the kitchen doorway down the hall: we see him as she does, unseen", ["SH-REAR", "SH-OCCL"], "deep", "deep",
  "", "Roy comes down the stairs for his glasses sideways, one step at a time, his body turned to the banister, both feet on each step before the next", "T1", cast=["C1"], cue="as he reaches the bottom step",
  pace="one step every two seconds", extra=6.0, moving=True, face=False, speaking=False, kind="multi",
  start="Roy at the top of the stairs turning sideways to the banister; Hazel out of sight in the kitchen doorway at the end of the hall")
R("SH02", "SHOT", "N", "eye", "profile", "CU", "clean", "profile in the kitchen doorway: she sees, and says nothing", ["SH-PROFILE", "SH-CU"], "eyes", "shallow",
  "", "Hazel in the kitchen doorway, a tea towel in her hands, watching him without a word", "T1", cast=["N"], cue="hold", pace="still", extra=2.5, speaking=False,
  loc="L-STAIRS", end="Roy at the bottom of the stairs picking his glasses off the hall table; Hazel in the kitchen doorway")

# ======== SC08 — THE GATE (D6, last week of term, L-CAR) ========
scene("SC08", "D6", "L-CAR", L("the windscreen, late-afternoon sun", "L", "afternoon", "Turn — late gold afternoon", 4800),
      "MUS-EXPOSE", "turn: she sees Wendy", HAZ_BEFORE)
R("SH01", "SHOT", "N", "eye", "three-quarter", "MCU", "through", "through the windscreen glass: she's on the inside, watching life", ["SH-34", "SH-OCCL"], "eyes", "shallow",
  "", "Hazel in the passenger seat of Emma's car at pick-up, looking up the hill through the windscreen", "T1", cast=["N"], cue="as her eyes catch something", pace="still", extra=2.0, speaking=False,
  kind="multi", start="Hazel in the passenger seat, Emma out of the car at the school gate, children coming out")
R("SH02", "SHOT", "C5", "eye", "front", "WIDE", "through", "her view through the passenger window: Wendy coming down the hill", ["SH-WIDE", "SH-FGFOC"], "deep", "deep",
  "", "through the passenger window: a woman Hazel's age comes down the steep pavement with two children and a book bag in each hand — no wall, no stick, no hitch", "T1", cast=["C5", "X4"], cue="as she passes the gate",
  pace="brisk, one step per second", extra=4.0, moving=True, speaking=False, end="Wendy at the crossing by the school gate with the two children")
R("SH03", "SHOT", "N", "eye", "front", "MCU", "clean", "", ["SH-EYE"], "eyes", "shallow",
  "L045", "Hazel winds the window down; the lollipop lady is right beside the car at the crossing", "T2", cast=["N", "X3"], cue="on 'that?'", pace="still", playing="asks", kind="multi", split="length",
  start="Hazel at the open passenger window, the lollipop lady standing at the kerb beside the car with her sign lowered")
R("SH04", "SHOT", "X3", "high", "three-quarter", "MCU", "clean", "high: she leans down to the window — a conspirator", ["SH-34", "SH-HIGH"], "eyes", "shallow",
  "L046", "the lollipop lady leans to the window, sign tucked under her arm", "T2", cast=["X3"], cue="on 'shine.'", pace="one lean", playing="gossips")
R("SH05", "SHOT", "N", "eye", "ots", "CU", "through", "over the lollipop lady's shoulder", ["SH-OTS", "SH-CU"], "eyes", "shallow",
  "L047", "Hazel", "T2", cast=["N", "X3"], cue="on 'she?'", pace="still", playing="probes")
R("SH06", "SHOT", "X3", "low", "three-quarter", "MCU", "clean", "low on her with a wink", ["SH-34", "SH-LOW"], "eyes", "shallow",
  "L048", "the lollipop lady, lowering her voice", "T2", cast=["X3"], cue="on 'you.'", pace="still", playing="confides", end="the lollipop lady stepping back to her crossing")

# ======== SC09 — WENDY (D6, L-GATE) ========
scene("SC09", "D6", "L-GATE", L("the low sun", "L", "afternoon", "Turn — late gold afternoon", 4800),
      "MUS-EDU", "turn: the mechanism", HAZ_BEFORE)
R("SH01", "SHOT", "N", "eye", "three-quarter", "FULL", "clean", "", ["SH-34", "SH-EYE"], "deep", "deep",
  "", "Hazel gets out of the car and crosses the pavement to Wendy by the bench at the gate, a hand on the car, then on the railings", "T1", cast=["N", "C5"], cue="as she reaches Wendy",
  pace="slow, the hitch, six steps", extra=4.0, moving=True, speaking=False, kind="multi",
  start="Hazel opening the passenger door of the parked car; Wendy by the bench at the open green gate with the two children and the book bags")
R("SH02", "SHOT", "N", "eye", "ots", "MCU", "through", "over Wendy's shoulder", ["SH-OTS"], "eyes", "shallow",
  "L049", "Hazel, embarrassed but asking", "T1", cast=["N", "C5"], cue="on 'hill?'", pace="still", playing="asks")
R("SH03", "SHOT", "C5", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow",
  "L050", "Wendy, amused", "T1", cast=["C5"], cue="on 'bit?'", pace="still", playing="teases")
R("SH04", "SHOT", "N", "high", "three-quarter", "CU", "clean", "high: the confession", ["SH-CU", "SH-HIGH"], "eyes", "shallow",
  "L051", "Hazel", "T1", cast=["N"], cue="on 'postbox.'", pace="still", playing="confesses", end="the two women face to face by the bench at the gate, the children on the bench")
R("SH05", "SHOT", "C5", "low", "three-quarter", "MCU", "clean", "low on Wendy: she knows", ["SH-34", "SH-LOW"], "eyes", "shallow",
  "L052", "Wendy glances down at Hazel's knee", "T2", cast=["C5"], cue="on 'it?'", pace="one glance", playing="diagnoses", kind="multi", split="length",
  start="the two women face to face by the bench at the gate")
R("SH06", "SHOT", "N", "eye", "front", "MCU", "clean", "", ["SH-EYE"], "eyes", "shallow",
  "L053", "Hazel", "T2", cast=["N"], cue="on 'sleeve.'", pace="still", playing="admits")
R("SH07", "SHOT", "C5", "eye", "ots", "MCU", "through", "over Hazel's shoulder: the long one, held", ["SH-OTS"], "eyes", "shallow",
  "L054", "Wendy, matter-of-fact, sits down on the bench", "T2", cast=["C5", "N"], cue="on 'lands.'", pace="one sit", playing="explains", end="Wendy sitting on the bench, Hazel standing")
R("SH08", "SHOT", "N", "high", "front", "CU", "clean", "high on Hazel looking down at her", ["SH-CU", "SH-HIGH"], "eyes", "shallow",
  "L055", "Hazel sits down beside her", "T3", cast=["N"], cue="on 'land?'", pace="one slow sit", playing="asks", kind="multi", split="length", start="Wendy sitting on the bench, Hazel standing beside it")
R("SH09", "SHOT", "C5", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow",
  "L056", "Wendy touches two fingers to the spot just under her own kneecap through her dress", "T3", cast=["C5"], cue="on 'it.'", pace="one touch", playing="shows")
R("SH10", "SHOT", "N", "eye", "profile", "CU", "clean", "", ["SH-PROFILE", "SH-CU"], "eyes", "shallow",
  "L057", "Hazel", "T3", cast=["N"], cue="on 'times.'", pace="still", playing="absorbs", end="the two women side by side on the bench")
R("SH11", "SHOT", "C5", "low", "three-quarter", "MCU", "clean", "low on Wendy: the diagnosis, kind and blunt", ["SH-34", "SH-LOW"], "eyes", "shallow",
  "L058", "Wendy nods at the car", "T4", cast=["C5"], cue="on 'Badly.'", pace="one nod", playing="names it", kind="multi", split="length", start="the two women side by side on the bench")
R("SH12", "SHOT", "N", "eye", "front", "CU", "clean", "", ["SH-CU", "SH-EYE"], "eyes", "shallow",
  "L059", "Hazel, quietly", "T4", cast=["N"], cue="on 'that.'", pace="still", playing="takes it", end="the two women on the bench, Hazel looking at Wendy")
R("SH13", "INSERT", "C5", "eye", "front", "CU", "clean", "the reveal: the strap is the picture", ["SH-CU", "SH-EYE"], "product", "shallow",
  "L060", "Wendy lifts the hem of her dress above her right knee: a thin black strap with a rigid shell sits just under her kneecap on bare skin", "T5", cast=["C5"], cue="on 'walk.'", pace="one lift",
  product=True, face=False, playing="shows", split="insert", start="Wendy sitting on the bench, her hand at the hem of her dress over her right knee",
  end="Wendy's hem lifted above the right knee, the strap just under the kneecap", ing=["C5", "L-GATE", "PRODUCT", "INFO-WORN-WENDY"])
R("SH14", "SHOT", "N", "high", "three-quarter", "MCU", "clean", "high: she looks down at it", ["SH-34", "SH-HIGH"], "eyes", "shallow",
  "L061", "Hazel looks down at Wendy's knee", "T6", cast=["N"], cue="on 'thing?'", pace="still", playing="doubts", kind="multi", split="insert",
  start="the two women on the bench, Wendy's hem back down")
R("SH15", "SHOT", "C5", "eye", "ots", "MCU", "through", "over Hazel's shoulder", ["SH-OTS"], "eyes", "shallow",
  "L062", "Wendy, dry", "T6", cast=["C5", "N"], cue="on 'thing.'", pace="still", playing="corrects")
R("SH16", "SHOT", "N", "eye", "three-quarter", "CU", "clean", "", ["SH-CU", "SH-34"], "eyes", "shallow",
  "L063", "Hazel", "T6", cast=["N"], cue="on 'one.'", pace="still", playing="objects", end="the two women on the bench")
R("SH17", "SHOT", "C5", "low", "front", "MCU", "clean", "low on Wendy: certain", ["SH-LOW", "SH-MED"], "eyes", "shallow",
  "L064", "Wendy, shaking her head", "T7", cast=["C5"], cue="on 'well.'", pace="one shake", playing="dismisses", kind="multi", split="length", start="the two women on the bench",
  say="The Facebook copies slide. Those go round as well.")
R("SH17b", "SHOT", "C5", "eye", "ots", "CU", "through", "over Hazel's shoulder: the claim, close", ["SH-OTS", "SH-CU"], "eyes", "shallow",
  "L064", "Wendy pats her own right knee through her dress", "T7", cast=["C5", "N"], cue="on 'woman.'", pace="one pat", playing="insists",
  say="This has a pad. It stays on the spot. And I’m not a small woman.")
R("SH18", "SHOT", "N", "eye", "front", "MCU", "clean", "", ["SH-EYE"], "eyes", "shallow",
  "L065", "Hazel", "T7", cast=["N"], cue="on 'home.'", pace="still", playing="argues", end="the two women on the bench, Wendy turning to her")
R("SH19", "SHOT", "C5", "eye", "three-quarter", "CU", "clean", "", ["SH-CU", "SH-34"], "eyes", "shallow",
  "L066", "Wendy, gentle, final", "T8", rig="F1", cast=["C5"], cue="on 'nothing.'", pace="a slow push-in", playing="ends it", split="length", kind="multi",
  start="the two women on the bench")
R("SH20", "SHOT", "N", "high", "three-quarter-back", "WIDE", "clean", "high wide: Wendy goes off down the hill with the children; Hazel left on the bench", ["SH-WIDE", "SH-HIGH"], "deep", "deep",
  "", "Wendy stands, takes the two children's hands and the book bags and walks off down the steep hill; Hazel stays on the bench watching her go", "T8", cast=["C5", "X4", "N"], cue="as Wendy passes out of frame",
  pace="brisk, one step per second", extra=3.0, moving=True, speaking=False, end="Hazel alone on the bench at the gate")

# ======== SC10 — THE PRICE (D6 night, L-KITCHEN) ========
scene("SC10", "D6", "L-KITCHEN", L("the cooker-hood light and the phone screen", "R", "night", "Turn — a warm lamp at night", 2800),
      "MUS-TURN", "decision: get the two", HAZ_BEFORE)
R("SH01", "SHOT", "N", "high", "three-quarter", "MEDIUM", "clean", "high: alone at the table at night with the phone — the decision", ["SH-MED", "SH-HIGH"], "hands", "medium",
  "", "Hazel at the pine table at night, reading glasses on, scrolling on her phone, the screen unseen; Roy comes down the hall sideways and into the doorway behind her", "T1", cast=["N", "C1"], cue="as Roy speaks",
  pace="still, one scroll", extra=3.0, speaking=False, kind="multi", start="night: Hazel alone at the pine table with her phone; Roy out of sight in the hall")
R("SH02", "SHOT", "C1", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow",
  "L067", "Roy in the kitchen doorway in his jumper", "T1", cast=["C1"], cue="on 'that?'", pace="still", playing="asks")
R("SH03", "SHOT", "N", "eye", "front", "CU", "clean", "", ["SH-CU", "SH-EYE"], "eyes", "shallow",
  "L068 L069 L070", "Hazel, not looking up; Roy off-screen asks; she answers", "T1", cast=["N", "C1"], cue="on 'hill.'", pace="still", playing="decides",
  end="Hazel at the table with the phone, Roy in the doorway")
R("SH04", "SHOT", "C1", "low", "ots", "MCU", "through", "low over Hazel's shoulder onto Roy: his worry", ["SH-OTS", "SH-LOW"], "eyes", "shallow",
  "L071", "Roy comes to the table", "T2", cast=["C1", "N"], cue="on 'car.'", pace="three steps", playing="resists", kind="multi", split="length", start="Roy in the doorway, Hazel at the table")
R("SH05", "SHOT", "N", "eye", "profile", "CU", "clean", "profile: the real reason", ["SH-PROFILE", "SH-CU"], "eyes", "shallow",
  "L072", "Hazel takes her glasses off", "T2", cast=["N"], cue="on 'nothing.'", pace="one move", playing="confesses")
R("SH06", "SHOT", "C1", "eye", "front", "MCU", "clean", "", ["SH-EYE"], "eyes", "shallow",
  "L073", "Roy, sitting down opposite", "T2", cast=["C1"], cue="on 'doesn't?'", pace="one sit", playing="tests")
R("SH07", "SHOT", "N", "eye", "three-quarter", "CU", "clean", "", ["SH-CU", "SH-34"], "eyes", "shallow",
  "L074", "Hazel", "T2", cast=["N"], cue="on 'back.'", pace="still", playing="answers", end="the two of them across the table")
R("SH08", "SHOT", "C1", "eye", "three-quarter", "CU", "clean", "", ["SH-CU", "SH-34"], "eyes", "shallow",
  "L075", "Roy, after a beat, pushes the phone back to her", "T3", rig="F1", cast=["C1"], cue="on 'two.'", pace="a beat, then one push", extra=1.0, playing="gives in", split="length",
  start="the two of them across the table", end="the phone back in front of Hazel")

# ======== SC11 — THE STAIRS (D7 morning, L-BEDROOM → L-STAIRS) ========
scene("SC11", "D7", "L-BEDROOM", L("the sash window, early sun", "L", "morning", "Turn — first clear morning sun", 5600),
      "MUS-TURN", "the test", "Hazel: before → after inside the scene; the strap goes on")
R("SH01", "INSERT", "N", "eye", "front", "CU", "clean", "front-on to the knee: the placement is the point", ["SH-CU", "SH-EYE"], "product", "shallow",
  "", "Hazel, sitting on the edge of the bed in her nightdress, slides the closed strap up her bare right shin with both hands flat on the shell until it seats just under the kneecap", "T1", cast=["N"],
  cue="as it seats", pace="one slow slide up", product=True, face=False, extra=3.5, speaking=False, split="insert",
  start="Hazel sitting on the bed edge in her nightdress, the closed strap at mid-shin on her bare right leg", end="the strap seated just under her right kneecap",
  ing=["N", "OUT-N-D7", "L-BEDROOM", "PRODUCT", "INFO-SEAT"])
S7 = L("the landing window and the front door glass", "L", "morning", "Turn — first clear morning sun", 5600)
R("SH02", "SHOT", "N", "high", "three-quarter", "FULL", "clean", "high from the landing: the flight below her — the old fear", ["SH-HIGH", "SH-34"], "deep", "deep",
  "L076", "Hazel, dressed, at the top of the stairs, her right hand on the banister", "T2", cast=["N"], cue="on 'Hazel.'", pace="still, one breath", speaking=False, kind="multi",
  loc="L-STAIRS", light=S7, start="Hazel dressed, standing on the landing at the top of the fourteen steps, right hand on the banister", playing="steels herself")
R("SH03", "SHOT", "N", "low", "front", "FULL", "clean", "low from the hall: she comes down to us — step by step", ["SH-LOW", "SH-EYE"], "deep", "deep",
  "L077", "Hazel comes down: first step with her hand on the banister, second step, and on the third her hand lifts off the rail on its own; she goes on down with her hands free at her sides", "T2",
  cast=["N"], cue="on 'own.'", pace="one step per second, foot by foot", extra=2.0, moving=True, speaking=False, loc="L-STAIRS", light=S7,
  end="Hazel at the bottom of the stairs on the hall tiles, hands free")
R("SH04", "SHOT", "N", "eye", "profile", "FULL", "clean", "profile on the stairs: the A/B test, side by side in one place", ["SH-PROFILE"], "deep", "deep",
  "", "back on the landing with the strap taken off off-screen in the bedroom, she comes down again: the hitch is back, the hand is back on the banister", "T3", cast=["N"],
  cue="as her hand grips the rail", pace="slow, the hitch", extra=7.0, moving=True, speaking=False, loc="L-STAIRS", light=S7, kind="multi", split="length",
  start="Hazel on the landing at the top of the stairs, the strap off (taken off off-screen)")
R("SH05", "SHOT", "N", "low", "three-quarter", "FULL", "clean", "low from the hall: the second descent, nothing in her hand — the proof", ["SH-LOW", "SH-34"], "deep", "deep",
  "", "on the landing again, the strap back on off-screen, she comes down a third time: even steps, nothing in her hand", "T3", cast=["N"], cue="as she reaches the bottom",
  pace="one step per second", extra=5.0, moving=True, speaking=False, loc="L-STAIRS", light=S7, mirror="SC11-SH03")
R("SH06", "SHOT", "C1", "eye", "three-quarter", "MCU", "clean", "Roy in the kitchen doorway: he saw — and says nothing", ["SH-34"], "eyes", "shallow",
  "", "Roy in the kitchen doorway in his dressing gown, a mug in his hand, watching; he says nothing", "T3", cast=["C1"], cue="hold", pace="still", extra=2.5, speaking=False,
  loc="L-STAIRS", light=S7, end="Hazel at the bottom of the stairs; Roy in the kitchen doorway")

# ======== SC12 — THE HILL, AUGUST (D8, L-HILL) ========
scene("SC12", "D8", "L-HILL", L("the morning sun from the left", "L", "morning", "After — clear summer morning", 5600),
      "MUS-AFTER", "payoff: past the postbox", HAZ_AFTER)
R("SH01", "SHOT", "N", "eye", "profile", "FULL", "clean", "profile beside her, the same hill: the postbox goes by", ["SH-PROFILE"], "deep", "deep",
  "", "Hazel walks up the hill at an even pace, hands free, and passes the red pillar box without slowing", "T1", rig="F9", cast=["N"], cue="as the postbox passes behind her", pace="brisk, one step per second",
  extra=4.0, moving=True, speaking=False, kind="multi", mirror="SC05-SH02",
  start="Hazel on the pavement below the pillar box, walking up, hands free; the mum with the buggy coming down from above")
R("SH02", "SHOT", "X2", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow",
  "L078", "the mum with the buggy stops, surprised", "T1", cast=["X2"], cue="on 'postbox.'", pace="still", playing="notices")
R("SH03", "SHOT", "N", "low", "front", "MCU", "clean", "low: she owns the hill", ["SH-LOW", "SH-MED"], "eyes", "shallow",
  "L079", "Hazel, a small smile", "T1", cast=["N"], cue="on 'did.'", pace="still", playing="owns it")
R("SH04", "SHOT", "X2", "eye", "ots", "MCU", "through", "over Hazel's shoulder", ["SH-OTS"], "eyes", "shallow",
  "L080", "the mum", "T1", cast=["X2", "N"], cue="on 'done?'", pace="still", playing="asks", end="the two of them stopped just above the pillar box")
R("SH05", "SHOT", "N", "eye", "three-quarter", "CU", "clean", "", ["SH-CU", "SH-34"], "eyes", "shallow",
  "L081", "Hazel taps her right trouser leg once", "T2", cast=["N"], cue="on 'trousers.'", pace="one tap", playing="tells", kind="multi", split="length", start="the two of them just above the pillar box")
R("SH06", "SHOT", "X2", "high", "three-quarter", "MCU", "clean", "high on the mum looking at the leg", ["SH-34", "SH-HIGH"], "eyes", "shallow",
  "L082", "the mum", "T2", cast=["X2"], cue="on 'when?'", pace="still", playing="asks")
R("SH07", "SHOT", "N", "eye", "three-quarter-back", "FULL", "clean", "", ["SH-REAR"], "deep", "deep",
  "L083", "Hazel answers over her shoulder and walks on up the hill", "T2", cast=["N"], cue="on 'mornings.'", pace="brisk", moving=True, playing="moves on", end="Hazel walking on up the hill")

# ======== SC13 — THE SECOND FILM (D9, end of August, the hall, P-HOUSE) ========
scene("SC13", "D9", "P-HOUSE", L("the front door glass, afternoon", "back", "afternoon", "After — bright soft daylight", 5600, "the door glass behind the camera's subject line"),
      "MUS-AFTER", "payoff: the second film", HAZ_AFTER)
R("SH01", "SHOT", "N", "eye", "front", "FULL", "clean", "the phone's view again, the same frame as the first film", ["SH-POV", "SH-EYE"], "deep", "deep",
  "", "Hazel walks from the kitchen door to the front door toward the camera: even steps, hands free, past the radiator and the newel post without touching them", "T1", cast=["N"],
  cue="as she reaches the door", pace="one step per second, eight steps", extra=6.0, moving=True, speaking=False, mirror="SC02-SH04",
  start="Hazel at the open kitchen door at the far end of the hall, facing the camera at the front door", end="Hazel at the front door")
R("SH02", "SHOT", "C2", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow",
  "L084", "Emma lowers the phone, the two clips side by side on its screen, unseen", "T2", cast=["C2"], cue="on 'that?'", pace="still", playing="asks", kind="multi", split="length",
  start="Emma at the front door holding the phone, Hazel arriving beside her")
R("SH03", "SHOT", "N", "eye", "front", "MCU", "clean", "", ["SH-EYE"], "eyes", "shallow",
  "L085", "Hazel", "T2", cast=["N"], cue="on 'ago.'", pace="still", playing="states")
R("SH04", "SHOT", "C2", "high", "three-quarter", "MCU", "clean", "high on Emma: caught out", ["SH-34", "SH-HIGH"], "eyes", "shallow",
  "L086", "Emma", "T2", cast=["C2"], cue="on 'said.'", pace="still", playing="accuses")
R("SH05", "SHOT", "N", "low", "three-quarter", "CU", "clean", "low: the line that turns it back", ["SH-CU", "SH-LOW"], "eyes", "shallow",
  "L087", "Hazel, gently", "T2", cast=["N"], cue="on 'right.'", pace="still", playing="returns it", end="the two of them at the front door")
R("SH06", "SHOT", "C2", "eye", "ots", "CU", "through", "over Hazel's shoulder", ["SH-OTS", "SH-CU"], "eyes", "shallow",
  "L088 L089 L090", "Emma looks at her mother properly; Hazel asks; Emma can't say", "T3", cast=["C2", "N"], cue="on 'know.'", pace="still", playing="sees her", kind="multi", split="length",
  start="the two of them at the front door")
R("SH07", "SHOT", "N", "eye", "profile", "CU", "clean", "profile: she looks down the hall she just walked", ["SH-PROFILE", "SH-CU"], "eyes", "shallow",
  "L091", "Hazel", "T3", rig="F1", cast=["N"], cue="on 'I.'", pace="a slow push-in", playing="agrees", mirror="SC02-SH10", end="Hazel by the front door looking down the hall")

# ======== SC14 — ROY (D10, early September evening, the hall, P-HOUSE) ========
scene("SC14", "D10", "P-HOUSE", L("the hall pendant", "R", "evening", "After — warm tungsten evening", 3000),
      "MUS-AFTER", "payoff: Roy knew the day; plant paid: sideways", HAZ_AFTER)
R("SH01", "SHOT", "C1", "eye", "three-quarter", "MEDIUM", "clean", "", ["SH-MED", "SH-34"], "eyes", "medium",
  "L092", "Roy in the hall with the car keys in his hand", "T1", cast=["C1", "N"], cue="on 'eight.'", pace="still", playing="arranges", kind="multi",
  start="Roy by the hall table with the car keys; Hazel at the kitchen door at the end of the hall")
R("SH02", "SHOT", "N", "eye", "front", "MCU", "clean", "", ["SH-EYE"], "eyes", "shallow",
  "L093 L094 L095", "Hazel; Roy, a warning; Hazel", "T1", cast=["N", "C1"], cue="on 'me.'", pace="still", playing="challenges")
R("SH03", "SHOT", "N", "eye", "front", "FULL", "clean", "the hall-film frame a third time: now he is the witness", ["SH-EYE", "SH-WIDE"], "deep", "deep",
  "", "Hazel walks to the front door and back, even, hands free, past him", "T1", cast=["N", "C1"], cue="as she turns at the door", pace="one step per second", extra=6.0, moving=True, speaking=False,
  mirror="SC02-SH04", end="Hazel back by Roy in the hall")
R("SH04", "SHOT", "C1", "low", "three-quarter", "MCU", "clean", "low on Roy: the man who drove is moved", ["SH-34", "SH-LOW"], "eyes", "shallow",
  "L096", "Roy, quiet", "T1", cast=["C1"], cue="on 'years.'", pace="still", playing="admits", end="the two of them in the hall")
R("SH05", "SHOT", "N", "eye", "ots", "CU", "through", "over Roy's shoulder", ["SH-OTS", "SH-CU"], "eyes", "shallow",
  "L097", "Hazel", "T2", cast=["N", "C1"], cue="on 'again.'", pace="still", playing="asks", kind="multi", split="length", start="the two of them in the hall by the hall table")
R("SH06", "SHOT", "C1", "eye", "front", "CU", "clean", "", ["SH-CU", "SH-EYE"], "eyes", "shallow",
  "L098", "Roy", "T2", cast=["C1"], cue="on 'years.'", pace="still", playing="gives it")
R("SH07", "SHOT", "N", "high", "three-quarter", "CU", "clean", "high: the question she has never asked", ["SH-CU", "SH-HIGH"], "eyes", "shallow",
  "L099", "Hazel", "T2", cast=["N"], cue="on 'Roy?'", pace="still", playing="asks")
R("SH08", "SHOT", "C1", "eye", "profile", "CU", "clean", "profile: he remembers it, not to her", ["SH-PROFILE", "SH-CU"], "eyes", "shallow",
  "L100", "Roy, looking at the front door", "T2", rig="F1", cast=["C1"], cue="on 'it.'", pace="a slow push-in", playing="remembers", end="Roy looking at the front door")
R("SH09", "SHOT", "N", "eye", "three-quarter", "CU", "clean", "", ["SH-CU", "SH-34"], "eyes", "shallow",
  "L101", "Hazel", "T4", cast=["N"], cue="on 'day.'", pace="still", playing="sees him", kind="multi", split="length", start="the two of them in the hall")
R("SH10", "SHOT", "C1", "low", "three-quarter", "CU", "clean", "low: his confession", ["SH-CU", "SH-LOW"], "eyes", "shallow",
  "L102", "Roy", "T4", cast=["C1"], cue="on 'car.'", pace="still", playing="confesses")
R("SH11", "SHOT", "N", "eye", "ots", "MCU", "through", "over Roy's shoulder", ["SH-OTS"], "eyes", "shallow",
  "L103", "Hazel takes his hand", "T4", cast=["N", "C1"], cue="on 'well.'", pace="one move", playing="forgives", end="Hazel holding Roy's hand in the hall")
R("SH12", "SHOT", "N", "eye", "front", "MCU", "clean", "", ["SH-EYE"], "eyes", "shallow",
  "L104 L105", "Hazel; Roy", "T5", cast=["N", "C1"], cue="on 'for?'", pace="still", playing="teases", kind="multi", split="length", start="Hazel holding Roy's hand in the hall")
R("SH13", "SHOT", "N", "eye", "three-quarter", "CU", "clean", "", ["SH-CU", "SH-34"], "eyes", "shallow",
  "L106", "Hazel", "T5", cast=["N"], cue="on 'Roy.'", pace="still", playing="reveals")
R("SH14", "SHOT", "C1", "high", "three-quarter", "CU", "clean", "high on Roy: found out, and glad", ["SH-CU", "SH-HIGH"], "eyes", "shallow",
  "L107", "Roy", "T5", cast=["C1"], cue="on 'seen.'", pace="still", playing="admits")
R("SH15", "SHOT", "N", "eye", "profile", "CU", "clean", "", ["SH-PROFILE", "SH-CU"], "eyes", "shallow",
  "L108", "Hazel", "T5", rig="F1", cast=["N"], cue="on 'round.'", pace="a slow push-in", playing="gives it him", end="Hazel looking at Roy")

# ======== SC15 — THE FIRST DAY (D11, September 8:40, L-HILL → L-GATE) ========
scene("SC15", "D11", "L-HILL", L("the morning sun from the left", "L", "morning", "After — clear September morning", 5600),
      "MUS-AFTER", "payoff: 'That's just walking, Nana.'", HAZ_AFTER)
R("SH01", "SHOT", "N", "eye", "profile", "FULL", "clean", "beside them in profile: his pace, past the postbox", ["SH-PROFILE"], "deep", "deep",
  "", "Hazel and Oscar walk up the hill hand in hand at his pace, past the red pillar box; Emma's car creeps behind them up the road", "T1", rig="F9", cast=["N", "C4"],
  cue="as the postbox passes", pace="a four-year-old's steps", extra=5.0, moving=True, speaking=False, kind="one-take", mirror="SC12-SH01",
  start="Hazel and Oscar hand in hand on the pavement below the pillar box, walking up; Emma's car behind them on the road", end="the two of them above the pillar box, still walking")
G15 = L("the morning sun, low behind the school", "L", "morning", "After — clear September morning", 5600)
R("SH02", "SHOT", "C2", "eye", "three-quarter", "MCU", "through", "through the windscreen: the witnesses", ["SH-34", "SH-OCCL"], "eyes", "shallow",
  "", "Emma and Dan in the parked car behind, watching through the windscreen; Emma raises her phone", "T2", cast=["C2", "C3"], cue="as the phone comes up", pace="still", extra=2.5, speaking=False,
  loc="L-GATE", light=G15, kind="multi", split="length", start="Hazel and Oscar at the school gate; Emma and Dan in the car parked behind")
R("SH03", "SHOT", "N", "low", "three-quarter", "MEDIUM", "clean", "low at the gate: she asks it now from strength", ["SH-LOW", "SH-MED"], "eyes", "medium",
  "L109", "Hazel lets go of his hand at the gate", "T2", cast=["N", "C4"], cue="on 'walk.'", pace="still", loc="L-GATE", light=G15, playing="invites")
R("SH04", "SHOT", "C4", "eye", "profile", "FULL", "clean", "profile: the same child, the same walk — straight", ["SH-PROFILE"], "deep", "deep",
  "", "Oscar looks at her, walks a few steps along the railings — straight, an ordinary four-year-old walk — and turns round", "T2", cast=["C4"], cue="as he turns", pace="six small steps",
  extra=3.0, moving=True, speaking=False, loc="L-GATE", light=G15, mirror="SC01-SH05")
R("SH05", "SHOT", "C4", "eye", "front", "MCU", "clean", "", ["SH-EYE"], "eyes", "shallow",
  "L110", "Oscar, puzzled", "T2", cast=["C4"], cue="on 'walk?'", pace="still", loc="L-GATE", light=G15, playing="asks", end="Oscar facing Hazel by the railings")
R("SH06", "SHOT", "N", "eye", "front", "CU", "clean", "", ["SH-CU", "SH-EYE"], "eyes", "shallow",
  "L111", "Hazel", "T3", rig="F1", cast=["N"], cue="on 'like?'", pace="a slow push-in", loc="L-GATE", light=G15, mirror="SC01-SH06", playing="asks", kind="multi", split="length",
  start="Hazel and Oscar facing each other at the gate")
R("SH07", "SHOT", "C4", "high", "three-quarter", "MCU", "clean", "high on him: small, certain", ["SH-34", "SH-HIGH"], "eyes", "shallow",
  "L112", "Oscar, as if it's obvious; he runs in through the gate", "T3", cast=["C4"], cue="on 'Nana.'", pace="then a run", loc="L-GATE", light=G15, playing="tells her")
R("SH08", "SHOT", "N", "eye", "three-quarter-back", "WIDE", "clean", "a pull-back: her at the gate with nothing in her hands", ["SH-WIDE", "SH-REAR"], "deep", "deep",
  "", "Hazel stands at the gate with nothing in her hands as Oscar runs into the playground", "T3", rig="F6", cast=["N", "C4"], cue="hold", pace="a slow pull-back", extra=3.0, speaking=False,
  loc="L-GATE", light=G15, end="Hazel alone at the open gate, hands empty")

# ======== SC16 — THE CLOSE (D11, to camera at the gate, L-GATE) ========
scene("SC16", "D11", "L-GATE", L("the morning sun, low behind the school, open shade at the gate", "L", "morning", "Offer — clear September morning", 5600),
      "MUS-OFFER", "close: the offer", HAZ_AFTER)
R("SH01", "SHOT", "N", "eye", "front", "MCU", "clean", "", ['SH-EYE', 'SH-MED'], "eyes", "shallow",
  "L113", "Hazel to the lens at the school gate, plain and direct", "T1", cast=["N"], cue="end of phrase", pace="still, one small gesture", playing="tells us", say="Twenty-four of them in a drawer. Every one went round my knee.", kind="multi", start="Hazel standing at the open green school gate, the playground behind her, facing the lens")
R("SH02", "SHOT", "N", "eye", "three-quarter", "CU", "clean", "", ['SH-CU', 'SH-34'], "eyes", "shallow",
  "L113", "Hazel to the lens at the school gate, plain and direct", "T1", cast=["N"], cue="end of phrase", pace="still, one small gesture", playing="tells us", say="Not one of them took the weight off it. It goes round, it moves nothing.")
R("SH03", "SHOT", "N", "low", "front", "MCU", "clean", "low: she says the hard part with her chin up", ['SH-LOW', 'SH-MED'], "eyes", "shallow",
  "L113", "Hazel to the lens at the school gate, plain and direct", "T1", cast=["N"], cue="end of phrase", pace="still, one small gesture", playing="tells us", say="The walk my grandson copied wasn’t my knee.", end="Hazel at the gate, facing the lens")
R("SH04", "SHOT", "N", "eye", "front", "CU", "clean", "", ['SH-CU', 'SH-EYE'], "eyes", "shallow",
  "L113", "Hazel to the lens at the school gate, plain and direct", "T2", cast=["N"], cue="end of phrase", pace="still, one small gesture", playing="tells us", say="It was my body carrying seventeen times my weight onto one spot, and doing it badly.", kind="multi", start="Hazel standing at the open green school gate, the playground behind her, facing the lens", split="length")
R("SH05", "SHOT", "N", "high", "three-quarter", "MCU", "clean", "high, a touch: the plain fact, unforced", ['SH-34', 'SH-HIGH'], "eyes", "shallow",
  "L113", "Hazel to the lens at the school gate, plain and direct", "T2", cast=["N"], cue="end of phrase", pace="still, one small gesture", playing="tells us", say="This takes the weight before it lands.")
R("SH06", "SHOT", "N", "eye", "three-quarter", "MCU", "clean", "", ['SH-34', 'SH-MED'], "eyes", "shallow",
  "L114", "Hazel to the lens at the school gate, plain and direct", "T2", cast=["N"], cue="end of phrase", pace="still, one small gesture", playing="tells us", say="I put it on at half seven this morning and I’ve not thought about it since.", end="Hazel at the gate, facing the lens")
R("SH07", "SHOT", "N", "low", "three-quarter", "CU", "clean", "low: three refusals", ['SH-CU', 'SH-LOW'], "eyes", "shallow",
  "L114", "Hazel to the lens at the school gate, plain and direct", "T3", cast=["N"], cue="end of phrase", pace="still, one small gesture", playing="tells us", say="No wall. No stick. No car.", kind="multi", start="Hazel standing at the open green school gate, the playground behind her, facing the lens", split="length")
R("SH08", "SHOT", "N", "eye", "profile", "MCU", "clean", "profile: she looks down the hill they climbed, then back to us", ['SH-PROFILE', 'SH-MED'], "eyes", "shallow",
  "L114", "Hazel to the lens at the school gate, plain and direct", "T3", cast=["N"], cue="end of phrase", pace="still, one small gesture", playing="tells us", say="He walked up that hill holding my hand and there was nothing to copy.")
R("SH09", "SHOT", "N", "eye", "front", "CU", "clean", "", ['SH-CU', 'SH-EYE'], "eyes", "shallow",
  "L114", "Hazel to the lens at the school gate, plain and direct", "T3", cast=["N"], cue="end of phrase", pace="still, one small gesture", playing="tells us", say="He’s not why I’m telling you this. I’d stopped looking at myself walk.", end="Hazel at the gate, facing the lens")
R("SH10", "SHOT", "N", "low", "front", "MCU", "clean", "low: the offer with authority", ['SH-LOW', 'SH-MED'], "eyes", "shallow",
  "L115", "Hazel to the lens at the school gate, plain and direct", "T4", cast=["N"], cue="end of phrase", pace="still, one small gesture", playing="tells us", say="Two straps, under thirty pounds, today at getstryde.co.", kind="multi", start="Hazel standing at the open green school gate, the playground behind her, facing the lens", split="length")
R("SH11", "SHOT", "N", "eye", "three-quarter", "CU", "clean", "", ['SH-CU', 'SH-34'], "eyes", "shallow",
  "L115", "Hazel to the lens at the school gate, plain and direct", "T4", cast=["N"], cue="end of phrase", pace="still, one small gesture", playing="tells us", say="Sixty days to send them back. No awkward questions.")
R("SH12", "SHOT", "N", "eye", "front", "MCU", "clean", "", ['SH-EYE', 'SH-MED'], "eyes", "shallow",
  "L115", "Hazel to the lens at the school gate, plain and direct", "T4", cast=["N"], cue="end of phrase", pace="still, one small gesture", playing="tells us", say="Keep one. Give the other to whoever’s been driving you.", end="Hazel at the gate, facing the lens")
R("SH13", "SHOT", "N", "low", "three-quarter", "MCU", "clean", "low: the dare", ['SH-34', 'SH-LOW'], "eyes", "shallow",
  "L115", "Hazel to the lens at the school gate, plain and direct", "T5", cast=["N"], cue="end of phrase", pace="still, one small gesture", playing="tells us", say="Then put it on, walk to your own front gate, and ask the little one to do your walk.", kind="multi", start="Hazel standing at the open green school gate, the playground behind her, facing the lens", split="length")
R("SH14", "SHOT", "N", "low", "front", "CU", "clean", "low and close: the last word is hers", ['SH-CU', 'SH-LOW'], "eyes", "shallow",
  "L115", "Hazel to the lens at the school gate, plain and direct", "T5", cast=["N"], cue="end of phrase", pace="still, one small gesture", playing="tells us", say="Your turn.", end="Hazel at the gate, facing the lens")

FIX = {  # angles.py pass: a speaking face is never on a rear shot; every non-default angle states its reason
 "SC03-SH01": dict(subject="X1", side="three-quarter", shot=["SH-34", "SH-FGFOC"], why="past the rack edge: the assistant comes to her"),
 "SC04-SH03": dict(side="three-quarter", shot=["SH-34", "SH-HIGH"]),
 "SC12-SH07": dict(side="three-quarter", shot=["SH-34"], why="three-quarter as she turns away up the hill — already moving on"),
 "SC09-SH10": dict(why="profile: she takes the number in, looking at the hill"),
 "SC14-SH15": dict(why="profile: she says it to his face at close quarters, not to the room"),
}
FALLBACK = {"three-quarter": "SH-34", "profile": "SH-PROFILE", "ots": "SH-OTS", "behind": "SH-REAR", "three-quarter-back": "SH-REAR"}

def tidy(r):
    """Library shots agree with the setup fields; MCU and wider sit at medium depth so no scene is all shallow (§30J)."""
    r.update(FIX.get(r["beat"], {}))
    sh = [x for x in r["shot"] if not ((x == "SH-MED" and r["scale"] != "MEDIUM") or (x == "SH-WIDE" and r["scale"] != "WIDE")
          or (x == "SH-EYE" and r["height"] != "eye") or (x == "SH-CU" and r["scale"] not in ("CU",)))]
    if not sh:
        sh = [FALLBACK.get(r["side"]) or {"eye": "SH-EYE", "low": "SH-LOW", "high": "SH-HIGH"}.get(r["height"], "SH-EYE")]
    r["shot"] = sh
    if r["scale"] in ("MCU", "MEDIUM") and r["focus"]["dof"] == "shallow":
        r["focus"]["dof"] = "medium"

ACTS = {"SC01": "Hook 1", "SC02": "Act 1", **{f"SC{n:02d}": "Act 2" for n in range(3, 8)}, **{f"SC{n:02d}": "Act 3" for n in range(8, 12)},
        **{f"SC{n:02d}": "Act 4" for n in range(12, 16)}, "SC16": "Act 5"}
PRODUCT_AT = "SC09-SH13"   # the product's first frame: the music changes here (§40A, V7.78.0)

if __name__ == "__main__":
    turn = False
    for r in ROWS:
        tidy(r)
        r["act"] = ACTS[r["scene"]]
        turn = turn or r["beat"] == PRODUCT_AT
        if r["scene"] == "SC09" and turn: r["music"] = "MUS-TURN"
        if not r["ingredients"]:
            r["ingredients"] = [c for c in r["cast"]] + [r["location"]] + (["P-HOUSE"] if r["location"] in ("L-DINING", "L-STAIRS", "L-KITCHEN", "L-BEDROOM") else [])
    json.dump({"build": "stryde-the-impression", "rows": ROWS}, open(HERE / "act_map.json", "w"), indent=1, ensure_ascii=False)
    tot = sum(r["duration"] for r in ROWS)
    print(len(ROWS), "rows ·", len({r["take"] for r in ROWS}), "takes ·", round(tot), "s ≈", f"{int(tot//60)}:{int(tot%60):02d}")
    used = {i for r in ROWS for i in r["lines"].split()}
    print("lines missing:", sorted(set(LINES) - used - {"L076"}) or "none")
