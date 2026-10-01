#!/usr/bin/env python3
"""§18 step 5 — act map (E4 rows) for stryde-half-my-age, Mode 4 film on Seedance. Writes act_map.json (angles.py input + our fields).
One row per shot, cut order: hooks HKA, HKB, HKC, HKE, then the body SC02…SC13. Lines are L-ids from work/lines.json."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
ROWS = []
FOC = {"eyes": "nearest eye", "hands": "the hands", "product": "the strap", "deep": "deep", "foreground": "foreground", "background": "background"}
def L(src, key, time, arc, k, why=None):
    d = {"source": src, "key_side": key, "time": time, "arc": arc, "kelvin": k}
    if why: d["why"] = why
    return d
def R(beat, grp, typ, subj, h, side, scale, fg, why, shot, plane, dof, light, lines="", action="", rig="F2", cast=(), loc="", face=True,
      speaking=False, product=False, day=None, cue="", pace="", ing=(), mirror=None, moving=False):
    ROWS.append({"beat": beat, "group": grp, "type": typ, "subject": subj, "height": h, "side": side, "scale": scale, "fg": fg,
                 "why": why, "mode": 4, "shot": shot, "speaking": speaking, "product_beat": product,
                 "focus": {"plane": plane, "dof": dof, "rack": None, "moving_subject": moving}, "story_day": day, "face": face,
                 "light": light, "lines": lines, "action": action, "pace": pace, "rig": rig, "cast": list(cast), "location": loc,
                 "cut": cue, "ingredients": list(ing), "mirror_of": mirror})

# ---------- HOOK A — THE STATION STAIRS (story day HA, After, overcast late morning) ----------
g, d = "HKA", "HA"; st = L("overcast sky through the glass canopy", "L", "midday", "After — cool overcast, open", 6500)
R("HKA-SH01", g, "SHOT", "C2", "high", "behind", "WIDE", "clean", "high over the daughter's shoulder: the drop of the stairs and Mum already below — the gap between them is the joke", ["SH-WIDE", "SH-HIGH"], "deep", "deep", st,
  "L001", "the daughter at the top of the station steps reaches for the rail; below, HER is already three steps down, bag in hand", "F2", ["C2", "N"], "L-STATION", day=d, cue="on 'we can…'", pace="HER steps down one step per second", ing=["C2", "N", "L-STATION", "VOICE-C2"])
R("HKA-SH02", g, "SHOT", "N", "low", "three-quarter", "MEDIUM", "clean", "low from below on the steps: she owns the stairs — resolve", ["SH-MED", "SH-LOW"], "eyes", "medium", st,
  "L002", "HER, three steps down, turns her head back up to her daughter without stopping, bag in her right hand, left hand free of the rail", "F2", ["N"], "L-STATION", speaking=True, day=d, cue="on 'love.'", pace="one step per second", ing=["N", "L-STATION", "VOICE-N"])
R("HKA-SH03", g, "SHOT", "N", "eye", "profile", "FULL", "clean", "profile as she steps down the last stairs and onto the train — distance growing from the daughter", ["SH-PROFILE"], "deep", "deep", st,
  "", "HER walks down the last steps and steps through the open train doors, brisk and even", "F2", ["N"], "L-STATION", day=d, cue="as she steps inside", pace="brisk, one step per second", ing=["N", "L-STATION"], moving=True)
ct = L("carriage windows", "L", "midday", "After — cool overcast, open", 6500)
R("HKA-SH04", g, "SHOT", "C2", "eye", "three-quarter", "MCU", "clean", "three-quarter on the daughter, breathless, staring across the table — the witness", ["SH-34"], "eyes", "shallow", ct,
  "L003", "the daughter drops into the seat opposite, catching her breath, staring at her mother", "F1", ["C2"], "L-CARRIAGE", speaking=True, day=d, cue="on 'happen?'", pace="still, chest rising", ing=["C2", "L-CARRIAGE", "VOICE-C2"])
R("HKA-SH05", g, "SHOT", "N", "eye", "ots", "CU", "through", "over the daughter's shoulder onto HER, calm, looking out of the window — the answer is her face", ["SH-OTS", "SH-CU"], "eyes", "shallow", ct,
  "L004", "HER sits settled by the window, bag on her lap, a small private smile, looking out as the town slides past", "F1", ["N", "C2"], "L-CARRIAGE", day=d, cue="end of VO", pace="still", ing=["N", "C2", "L-CARRIAGE"])

# ---------- HOOK B — THE LIFT QUEUE (story day HB, After, daylight) ----------
g, d = "HKB", "HB"; sc = L("the atrium skylight", "R", "afternoon", "After — soft top daylight", 5600)
R("HKB-SH01", g, "SHOT", "C2", "eye", "front", "MEDIUM", "clean", "", ["SH-MED", "SH-EYE"], "eyes", "medium", sc,
  "L005", "the daughter, loaded with shopping bags on both arms, nods at the glass lift where a small queue waits", "F2", ["C2"], "L-SHOPCENTRE", speaking=True, day=d, cue="on 'there.'", pace="still", ing=["C2", "L-SHOPCENTRE", "VOICE-C2"])
R("HKB-SH02", g, "SHOT", "N", "low", "three-quarter-back", "FULL", "clean", "low behind her as she climbs: the flight ahead, her pace against it", ["SH-REAR", "SH-LOW"], "deep", "deep", sc,
  "L006", "HER is already three steps up the wide staircase, a full bag in each hand, climbing at an even pace, glancing back over her shoulder", "F2", ["N"], "L-SHOPCENTRE", day=d, cue="on 'stairs.'", pace="one step per second", ing=["N", "L-SHOPCENTRE", "VOICE-N"], moving=True)
R("HKB-SH03", g, "SHOT", "N", "high", "three-quarter", "MCU", "clean", "from the top of the stairs looking down on her face as she speaks up", ["SH-34", "SH-HIGH"], "eyes", "shallow", sc,
  "L006", "HER, mid-climb, says it over her shoulder without breaking stride", "F2", ["N"], "L-SHOPCENTRE", speaking=True, day=d, cue="on 'stairs.'", pace="one step per second", ing=["N", "L-SHOPCENTRE", "VOICE-N"])
R("HKB-SH04", g, "SHOT", "C2", "eye", "profile", "MCU", "clean", "profile of the daughter arriving at the top, out of breath — her effort against Mum's ease", ["SH-PROFILE"], "eyes", "shallow", sc,
  "L007", "the daughter reaches the top step, puffing, bags sagging, and looks at her mother", "F2", ["C2"], "L-SHOPCENTRE", speaking=True, day=d, cue="on 'happen?'", pace="breathing hard", ing=["C2", "L-SHOPCENTRE", "VOICE-C2"])
R("HKB-SH05", g, "SHOT", "N", "eye", "ots", "CU", "through", "over the daughter onto HER, unbothered at the top", ["SH-OTS", "SH-CU"], "eyes", "shallow", sc,
  "L008", "HER waits at the top rail, bags down by her feet, breathing easily, eyebrows up", "F1", ["N", "C2"], "L-SHOPCENTRE", day=d, cue="end of VO", pace="still", ing=["N", "C2", "L-SHOPCENTRE"])

# ---------- HOOK C — THE DEAD ESCALATOR (story day HC, After, morning rush) ----------
g, d = "HKC", "HC"; es = L("the concourse glass roof", "R", "morning", "After — cool station daylight", 6000)
R("HKC-SH01", g, "SHOT", "X2", "eye", "front", "MCU", "clean", "", ["SH-MED", "SH-EYE"] if False else ["SH-EYE"], "eyes", "shallow", es,
  "L009 L010", "the tannoy (off) announces the escalator is out of service; a commuter in his 20s looks up from his phone and groans", "F2", ["X2"], "L-ESCALATOR", speaking=True, day=d, cue="on 'joking.'", pace="still", ing=["L-ESCALATOR", "VOICE-X1", "VOICE-X2"])
R("HKC-SH02", g, "SHOT", "N", "low", "three-quarter", "FULL", "through", "low past the commuter's legs: she walks past him and takes the first step — first to go", ["SH-LOW", "SH-34"], "deep", "deep", es,
  "L011", "HER walks past the groaning commuter and puts her foot on the first step of the fixed stairs, handbag on her shoulder, hands free", "F2", ["N", "X2"], "L-ESCALATOR", speaking=True, day=d, cue="on 'love.'", pace="brisk, one step per second", ing=["N", "L-ESCALATOR", "VOICE-N"], moving=True)
R("HKC-SH03", g, "SHOT", "N", "high", "behind", "WIDE", "clean", "high wide from the top: one small figure climbing ahead of the crowd", ["SH-WIDE", "SH-HIGH"], "deep", "deep", es,
  "", "HER climbs the long fixed staircase at an even pace while commuters behind her bunch up at the foot", "F2", ["N"], "L-ESCALATOR", face=False, day=d, cue="halfway up", pace="one step per second", ing=["N", "L-ESCALATOR"], moving=True)
R("HKC-SH04", g, "SHOT", "C2", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow", es,
  "L012", "the daughter at the bottom of the stairs, coffee in hand, stares up after her mother", "F1", ["C2"], "L-ESCALATOR", speaking=True, day=d, cue="on 'happen?'", pace="still", ing=["C2", "L-ESCALATOR", "VOICE-C2"])
R("HKC-SH05", g, "SHOT", "N", "high", "front", "CU", "clean", "high at the top of the stairs looking down on her arriving — she turns to look back down", ["SH-CU", "SH-HIGH"], "eyes", "shallow", es,
  "L013", "HER reaches the top and turns back to look down at her daughter, not out of breath", "F1", ["N"], "L-ESCALATOR", day=d, cue="end of VO", pace="still", ing=["N", "L-ESCALATOR"])

# ---------- HOOK E — THE FLOOR (story day HE, After, afternoon, living room) ----------
g, d = "HKE", "HE"; lv = L("the bay window", "L", "afternoon", "After — soft daylight", 5600)
R("HKE-SH01", g, "SHOT", "N", "high", "three-quarter", "FULL", "clean", "high on her kneeling on the floor — small, low down, the old danger", ["SH-HIGH", "SH-34"], "deep", "deep", lv,
  "", "HER kneels on the living-room carpet picking up a grandchild's spilled jigsaw pieces into the box", "F2", ["N"], "L-LIVING", day=d, cue="as the door opens", pace="slow, piece by piece", ing=["N", "L-LIVING", "P-HOUSE"])
R("HKE-SH02", g, "SHOT", "C2", "eye", "three-quarter", "MEDIUM", "through", "through the doorway: the daughter comes in already reaching", ["SH-MED", "SH-OCCL"], "eyes", "medium", lv,
  "L014", "the daughter comes through the doorway and reflexively reaches a hand down toward her mother", "F2", ["C2"], "L-LIVING", speaking=True, day=d, cue="on 'a…'", pace="quick, two steps", ing=["C2", "L-LIVING", "P-HOUSE", "VOICE-C2"])
R("HKE-SH03", g, "SHOT", "N", "low", "profile", "FULL", "clean", "low profile: she rises from kneeling to standing in one move, no hands on the furniture — the proof", ["SH-PROFILE", "SH-LOW"], "deep", "deep", lv,
  "", "HER puts one foot flat and stands up from kneeling in one smooth move, the jigsaw box in her hands, before the offered hand arrives", "F2", ["N", "C2"], "L-LIVING", day=d, cue="as she reaches full height", pace="one smooth rise over two seconds", ing=["N", "C2", "L-LIVING", "P-HOUSE"])
R("HKE-SH04", g, "SHOT", "C2", "eye", "ots", "CU", "through", "over Mum's shoulder onto the daughter's face, hand still out", ["SH-OTS", "SH-CU"], "eyes", "shallow", lv,
  "L015", "the daughter, hand still outstretched in the air, stares", "F1", ["C2", "N"], "L-LIVING", speaking=True, day=d, cue="on 'happen?'", pace="still", ing=["C2", "N", "L-LIVING", "VOICE-C2"])
R("HKE-SH05", g, "SHOT", "N", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow", lv,
  "L016", "HER puts the jigsaw box on the mantel and gives her daughter a small look", "F1", ["N"], "L-LIVING", day=d, cue="end of VO", pace="still", ing=["N", "L-LIVING", "P-HOUSE"])

# ---------- SC02 — ROCK BOTTOM (story day B1 evening → B2 morning) ----------
g = "SC02"; ev = L("the hall pendant lamp below and the landing lamp", "R", "evening", "Before — cool dusk, one warm lamp", 2800)
R("SC02-SH01", g, "SHOT", "N", "low", "three-quarter", "FULL", "clean", "from the hall looking up at her on the landing — she is stranded up there", ["SH-LOW", "SH-34"], "deep", "deep", ev,
  "L017", "HER stands at the top of the stairs holding the newel post, calling down", "F2", ["N"], "L-STAIRS", speaking=True, day="B1", cue="on 'later.'", pace="still", ing=["N", "L-STAIRS", "P-HOUSE", "VOICE-N"])
R("SC02-SH02", g, "SHOT", "C3", "high", "front", "MEDIUM", "clean", "down the stairs onto the husband too quickly lifting the bags — what he doesn't say", ["SH-HIGH", "SH-MED"], "eyes", "medium", ev,
  "L018", "the husband in the hall snatches up the two shopping bags by the bottom step, a little too fast", "F2", ["C3"], "L-STAIRS", speaking=True, day="B1", cue="on 'up.'", pace="quick lift", ing=["C3", "L-STAIRS", "P-HOUSE", "VOICE-C3"])
mo = L("the frosted landing window", "L", "morning", "Before — cold grey morning", 6500)
R("SC02-SH03", g, "SHOT", "N", "high", "behind", "FULL", "clean", "high behind her from the landing: going down backwards, both hands on the banister — the low point", ["SH-REAR", "SH-HIGH"], "deep", "deep", mo,
  "L019", "next morning, HER goes down the stairs backwards, facing the steps, both hands gripping the banister, one foot then the other onto each step", "F2", ["N"], "L-STAIRS", face=False, day="B2", cue="on 'at a time.'", pace="slow, one step every three seconds", ing=["N", "L-STAIRS", "P-HOUSE"])
R("SC02-SH04", g, "SHOT", "N", "eye", "profile", "MCU", "clean", "profile on her face, jaw set, mid-step", ["SH-PROFILE"], "eyes", "shallow", mo,
  "L019", "HER, mid-stairs, backwards, lowers her weight onto the next step and breathes out", "F2", ["N"], "L-STAIRS", day="B2", cue="breath out", pace="slow", ing=["N", "L-STAIRS", "P-HOUSE"])
R("SC02-SH05", g, "SHOT", "C3", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow", mo,
  "L020", "the husband at the foot of the stairs with a mug of tea, not quite looking at how she's coming down", "F2", ["C3"], "L-STAIRS", speaking=True, day="B2", cue="on 'alright?'", pace="still", ing=["C3", "L-STAIRS", "P-HOUSE", "VOICE-C3"])
R("SC02-SH06", g, "SHOT", "N", "eye", "ots", "CU", "through", "over his shoulder onto her covering it", ["SH-OTS", "SH-CU"], "eyes", "shallow", mo,
  "L021", "HER, on the bottom step, takes the tea and gives a small tight smile", "F1", ["N", "C3"], "L-STAIRS", speaking=True, day="B2", cue="on 'love.'", pace="still", ing=["N", "C3", "L-STAIRS", "VOICE-N"])
bd = L("the bedroom window through net curtains", "L", "afternoon", "Before — flat grey afternoon", 6500)
R("SC02-SH07", g, "SHOT", "N", "eye", "three-quarter-back", "WIDE", "through", "through the half-open door: her alone on the bed edge, the world outside the window", ["SH-WIDE", "SH-OCCL"], "deep", "deep", bd,
  "L022", "HER sits on the edge of the bed upstairs, hands in her lap, looking out of the window", "F2", ["N"], "L-BEDROOM", day="B2", cue="end of VO", pace="still", ing=["N", "L-BEDROOM", "P-HOUSE"])

# ---------- SC03 — TRIED EVERYTHING + THE SUNDAY PLANT (story day B3) ----------
g = "SC03"; ld = L("the landing lamp", "R", "evening", "Before — cool dusk, one warm lamp", 2800)
R("SC03-SH01", g, "INSERT", "N", "low", "front", "ECU", "clean", "low on the knee: the brace sliding down — the failure at eye level with it", ["SH-MACRO", "SH-LOW"], "foreground", "shallow", ld,
  "L023", "a bulky hinged knee brace slides slowly down her shin as she stands on the landing", "F2", ["N"], "L-STAIRS", face=False, day="B3", cue="on 'down my leg.'", pace="slow slide over three seconds", ing=["N", "L-STAIRS", "INFO-BRACE"])
R("SC03-SH02", g, "INSERT", "N", "ground", "profile", "ECU", "clean", "ground level: the brace round her ankle by evening", ["SH-GROUND", "SH-MACRO"], "foreground", "shallow", ld,
  "L023", "the hinged brace sits bunched round her ankle above her slipper", "F2", ["N"], "L-STAIRS", face=False, day="B3", cue="on 'ankle.'", pace="still", ing=["N", "L-STAIRS", "INFO-BRACE"])
ph = L("the clinic window blinds", "L", "morning", "Before — clinical cool", 5600)
R("SC03-SH03", g, "SHOT", "N", "high", "three-quarter", "MEDIUM", "clean", "high on her on the physio couch — small, being handled", ["SH-HIGH", "SH-MED"], "eyes", "medium", ph,
  "L023", "HER lies on a physiotherapy couch while a physio's hands bend her right knee", "F2", ["N"], "L-PHYSIO", day="B3p", cue="on 'Physiotherapy.'", pace="slow bend", ing=["N", "INFO-PHYSIO"])
kt = L("the kitchen window", "L", "morning", "Before — cold grey morning", 6500)
R("SC03-SH04", g, "INSERT", "N", "overhead", "front", "ECU", "clean", "overhead on the table: the pills as routine", ["SH-OVER", "SH-MACRO"], "hands", "shallow", kt,
  "L023", "her hand pushes two painkillers out of a blister strip beside a mug on the pine table", "F2", ["N"], "L-KITCHEN", face=False, day="B3q", cue="on 'Painkillers.'", pace="one pill, then the next", ing=["N", "L-KITCHEN"])
R("SC03-SH05", g, "INSERT", "N", "eye", "profile", "ECU", "clean", "profile on the knee: the needle side, clinical", ["SH-MACRO", "SH-PROFILE"], "hands", "shallow", ph,
  "L023", "a gloved hand swabs the side of her right knee before an injection, the syringe held out of focus", "F2", ["N"], "L-PHYSIO", face=False, day="B3p", cue="on 'injections.'", pace="one swab", ing=["N", "INFO-PHYSIO"])
bd3 = L("the bedside lamp", "R", "evening", "Before — cool dusk, one warm lamp", 2800)
R("SC03-SH06", g, "SHOT", "N", "high", "three-quarter-back", "MEDIUM", "clean", "high over her shoulder into the drawer: every failed brace", ["SH-HIGH", "SH-REAR"], "hands", "medium", bd3,
  "L023 L024", "HER drops the hinged brace into the bottom drawer, already crammed with braces, sleeves and supports, and pushes it shut with her foot", "F2", ["N"], "L-BEDROOM", face=False, day="B3d", cue="on the drawer closing", pace="drop, then one push", ing=["N", "L-BEDROOM", "INFO-DRAWER"])
R("SC03-SH07", g, "SHOT", "C3", "eye", "three-quarter", "MCU", "through", "through the doorway: he watches, soft", ["SH-34", "SH-OCCL"], "eyes", "medium", bd3,
  "L025", "the husband in the bedroom doorway, a hand on the frame, watching her", "F2", ["C3"], "L-BEDROOM", speaking=True, day="B3d", cue="on 'soon.'", pace="still", ing=["C3", "L-BEDROOM", "VOICE-C3"])
R("SC03-SH08", g, "SHOT", "N", "eye", "profile", "CU", "clean", "profile on her not turning round", ["SH-PROFILE", "SH-CU"], "eyes", "shallow", bd3,
  "L026", "HER, still facing the drawer, answers without turning", "F1", ["N"], "L-BEDROOM", speaking=True, day="B3d", cue="on 'shuts.'", pace="still", ing=["N", "L-BEDROOM", "VOICE-N"])
R("SC03-SH09", g, "SHOT", "N", "eye", "front", "MCU", "clean", "", ["SH-EYE"], "eyes", "medium", bd3,
  "L027 L028", "HER sits on the bed edge with the phone to her ear; the sister's voice comes through the phone", "F1", ["N"], "L-BEDROOM", speaking=True, day="B3d", cue="on 'Easier.'", pace="still", ing=["N", "L-BEDROOM", "VOICE-N", "VOICE-C4"])
R("SC03-SH10", g, "SHOT", "N", "high", "three-quarter", "WIDE", "clean", "high wide: phone down in her lap, the room around her — a life on one level", ["SH-WIDE", "SH-HIGH"], "deep", "deep", bd3,
  "L029", "HER lowers the phone to her lap and sits still", "F6", ["N"], "L-BEDROOM", day="B3d", cue="end of VO", pace="slow pull-back over the line", ing=["N", "L-BEDROOM", "P-HOUSE"])

# ---------- SC04 — THE WEDDING (story day B4, June evening) ----------
g = "SC04"; wd = L("fairy lights and candle jars", "L", "evening", "Turn — warm party light", 2700)
R("SC04-SH01", g, "SHOT", "C1", "eye", "front", "WIDE", "through", "past the tables onto the floor: Barbara in the middle of it", ["SH-WIDE", "SH-FGFOC"], "deep", "deep", wd,
  "L030", "the reception in full swing: Barbara dances in the middle of the parquet floor among the guests, the bride in white near her", "F2", ["C1"], "L-WEDDING", day="B4", cue="on 'all night.'", pace="dancing on the beat", ing=["C1", "L-WEDDING", "INFO-WEDDING"])
R("SC04-SH02", g, "SHOT", "C1", "low", "three-quarter", "MEDIUM", "clean", "low on Barbara dancing — strength", ["SH-LOW", "SH-MED"], "eyes", "medium", wd,
  "L030", "Barbara bends her knees and turns on the beat, laughing", "F2", ["C1"], "L-WEDDING", day="B4", cue="on '74.'", pace="on the beat", ing=["C1", "L-WEDDING"])
R("SC04-SH03", g, "SHOT", "N", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow", wd,
  "L031", "HER seated at a round table, not taking her eyes off Barbara, says it low to her husband", "F1", ["N", "C3"], "L-WEDDING", speaking=True, day="B4", cue="on 'Bone on bone.'", pace="still", ing=["N", "L-WEDDING", "VOICE-N"])
R("SC04-SH04", g, "SHOT", "C3", "eye", "ots", "MCU", "through", "over her shoulder onto him, half-listening", ["SH-OTS"], "eyes", "shallow", wd,
  "L032", "the husband beside her leans in with his pint", "F2", ["C3", "N"], "L-WEDDING", speaking=True, day="B4", cue="on 'Whose?'", pace="still", ing=["C3", "N", "L-WEDDING", "VOICE-C3"])
R("SC04-SH05", g, "SHOT", "N", "eye", "profile", "CU", "clean", "profile: she answers without looking at him", ["SH-PROFILE", "SH-CU"], "eyes", "shallow", wd,
  "L033 L034", "HER keeps watching the dance floor, the light of it on her face", "F1", ["N"], "L-WEDDING", speaking=True, day="B4", cue="end of VO", pace="slow push-in", ing=["N", "L-WEDDING", "VOICE-N"])

# ---------- SC05 — BARBARA COMES TO STAY (story day B5, morning, kitchen) ----------
g = "SC05"; k5 = L("the kitchen window", "L", "morning", "Turn — soft morning daylight", 5600)
R("SC05-SH01", g, "SHOT", "N", "eye", "three-quarter", "WIDE", "through", "past the doorframe: the two of them at the table, the routine laid out", ["SH-WIDE", "SH-OCCL"], "deep", "deep", k5,
  "L035", "morning: HER at the pine table with pills, a tube of gel, the brace and an ice pack on her right knee; Barbara sits opposite with a mug, watching", "F2", ["N", "C1"], "L-KITCHEN", day="B5", cue="on 'routine.'", pace="still", ing=["N", "C1", "L-KITCHEN", "P-HOUSE"])
R("SC05-SH02", g, "INSERT", "N", "overhead", "front", "ECU", "clean", "overhead: the routine, piece by piece", ["SH-OVER", "SH-MACRO"], "hands", "shallow", k5,
  "L035", "on the table: two pills, the gel tube, the brace, the ice pack on the right knee", "F2", ["N"], "L-KITCHEN", face=False, day="B5", cue="on 'routine.'", pace="still", ing=["N", "L-KITCHEN"])
R("SC05-SH03", g, "SHOT", "C1", "eye", "ots", "MCU", "through", "over HER shoulder onto Barbara deciding", ["SH-OTS"], "eyes", "medium", k5,
  "L036", "Barbara puts her mug down", "F1", ["C1", "N"], "L-KITCHEN", speaking=True, day="B5", cue="on 'something?'", pace="still", ing=["C1", "N", "L-KITCHEN", "VOICE-C1"])
R("SC05-SH04", g, "INSERT", "C1", "low", "front", "ECU", "clean", "low on the knee: the reveal", ["SH-MACRO", "SH-LOW"], "product", "shallow", k5,
  "L037", "Barbara, seated, turns her bare right knee toward the camera: a small black strap sits just below her kneecap on the tendon", "F2", ["C1"], "L-KITCHEN", face=False, product=True, day="B5", cue="on 'kneecap.'", pace="still", ing=["C1", "L-KITCHEN", "PROD-FRONT", "INFO-PLACEMENT"])
R("SC05-SH05", g, "SHOT", "N", "eye", "three-quarter", "CU", "clean", "", ["SH-34", "SH-CU"], "eyes", "medium", k5,
  "L037", "HER looks at it, unimpressed", "F1", ["N"], "L-KITCHEN", day="B5", cue="on the look", pace="still", ing=["N", "L-KITCHEN"])
R("SC05-SH06", g, "INSERT", "C1", "high", "three-quarter", "ECU", "clean", "high on the table: the boxed spare arrives", ["SH-HIGH", "SH-MACRO"], "product", "shallow", k5,
  "L038", "Barbara's hand lays a small open box with a second strap inside on the table next to the pills", "F2", ["C1"], "L-KITCHEN", face=False, product=True, day="B5", cue="on 'spare.'", pace="one move", ing=["C1", "L-KITCHEN", "PROD-BOX"])
R("SC05-SH07", g, "SHOT", "C1", "eye", "profile", "MCU", "clean", "profile on Barbara, easy", ["SH-PROFILE"], "eyes", "medium", k5,
  "L038", "Barbara sits back, matter-of-fact", "F2", ["C1"], "L-KITCHEN", speaking=True, day="B5", cue="on 'spare.'", pace="still", ing=["C1", "L-KITCHEN", "VOICE-C1"])

# ---------- SC06 — THE SCEPTIC (continuous) ----------
g = "SC06"
R("SC06-SH01", g, "INSERT", "N", "overhead", "front", "ECU", "clean", "overhead: the strap in her palm, small", ["SH-OVER", "SH-MACRO"], "product", "shallow", k5,
  "L039", "the strap rests across HER open palm; she turns it once", "F2", ["N"], "L-KITCHEN", face=False, product=True, day="B5", cue="on 'Too small.'", pace="one turn", ing=["N", "L-KITCHEN", "PROD-FRONT"])
R("SC06-SH02", g, "SHOT", "N", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "medium", k5,
  "L040", "HER holds the strap up, sceptical", "F1", ["N"], "L-KITCHEN", speaking=True, day="B5", cue="on 'mine.'", pace="still", ing=["N", "L-KITCHEN", "PROD-FRONT", "VOICE-N"])
R("SC06-SH03", g, "SHOT", "C1", "low", "three-quarter", "CU", "clean", "low on Barbara: certainty", ["SH-LOW", "SH-CU"], "eyes", "shallow", k5,
  "L041", "Barbara leans in across the table", "F1", ["C1"], "L-KITCHEN", speaking=True, day="B5", cue="on 'stairs.'", pace="slow push-in", ing=["C1", "L-KITCHEN", "VOICE-C1"])

# ---------- SC07 — THE TEST (continuous, the stairs) — mirror of SC02-SH03 ----------
g = "SC07"; t7 = L("the frosted landing window", "L", "morning", "Turn — the light opens", 5600)
R("SC07-SH01", g, "INSERT", "N", "low", "front", "ECU", "clean", "low on the knee: the strap slides up into place", ["SH-MACRO", "SH-LOW"], "product", "shallow", t7,
  "", "on the landing, HER slides the strap up her bare right shin in one move until it seats just below the kneecap", "F2", ["N"], "L-STAIRS", face=False, product=True, day="B5", cue="as it seats", pace="one move", ing=["N", "L-STAIRS", "PROD-FRONT", "INFO-PLACEMENT"])
R("SC07-SH02", g, "SHOT", "N", "high", "behind", "FULL", "clean", "the mirror of SC02-SH03: same high angle behind her, now facing forwards", ["SH-REAR", "SH-HIGH"], "deep", "deep", t7,
  "L042", "HER stands at the top of the stairs facing forwards, hand hovering over the banister, and takes the first step down without touching it", "F2", ["N"], "L-STAIRS", face=False, day="B5", cue="on 'banister.'", pace="one step, then a beat", ing=["N", "L-STAIRS", "P-HOUSE"], mirror="SC02-SH03")
R("SC07-SH03", g, "SHOT", "N", "low", "front", "MEDIUM", "clean", "from below: she comes toward us, step by step, hands free", ["SH-LOW", "SH-MED"], "eyes", "medium", t7,
  "L043", "HER comes down the second and third steps facing forwards, hands at her sides, eyes on the steps", "F2", ["N"], "L-STAIRS", day="B5", cue="on 'third.'", pace="one step per second", ing=["N", "L-STAIRS", "P-HOUSE"], moving=True)
R("SC07-SH04", g, "SHOT", "C1", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow", t7,
  "", "Barbara watches from the hall below, arms folded, a small smile", "F2", ["C1"], "L-STAIRS", day="B5", cue="reaction", pace="still", ing=["C1", "L-STAIRS", "P-HOUSE"])
R("SC07-SH05", g, "SHOT", "N", "ground", "profile", "FULL", "clean", "ground level at the foot: both feet, forwards, down the last steps", ["SH-GROUND", "SH-PROFILE"], "deep", "deep", t7,
  "L044", "HER walks down the last steps forwards and steps onto the hall carpet", "F2", ["N"], "L-STAIRS", face=False, day="B5", cue="on 'Forwards.'", pace="one step per second", ing=["N", "L-STAIRS", "P-HOUSE"], moving=True)
R("SC07-SH06", g, "SHOT", "N", "eye", "front", "CU", "clean", "", ["SH-CU", "SH-EYE"], "eyes", "shallow", t7,
  "L045", "HER stands at the foot of the stairs and looks back up the flight, breath caught", "F1", ["N"], "L-STAIRS", day="B5", cue="on 'switch.'", pace="slow push-in", ing=["N", "L-STAIRS", "P-HOUSE"])

# ---------- SC08 — THE MECHANISM, FROM BARBARA (kitchen, same morning) ----------
g = "SC08"
R("SC08-SH01", g, "SHOT", "C1", "eye", "three-quarter", "MEDIUM", "clean", "", ["SH-34", "SH-MED"], "eyes", "medium", k5,
  "L046", "back at the table, Barbara talks while HER sits down across from her", "F2", ["C1", "N"], "L-KITCHEN", speaking=True, day="B5", cue="on 'hurts.'", pace="still", ing=["C1", "N", "L-KITCHEN", "VOICE-C1"])
R("SC08-SH02", g, "INSERT", "C1", "low", "three-quarter", "ECU", "clean", "low on her own knee: the spot", ["SH-MACRO", "SH-LOW"], "hands", "shallow", k5,
  "L047", "Barbara presses two fingers on her own bare knee just below the kneecap", "F2", ["C1"], "L-KITCHEN", face=False, day="B5", cue="on 'lands.'", pace="one press", ing=["C1", "L-KITCHEN", "INFO-PLACEMENT"])
R("SC08-SH03", g, "SHOT", "C1", "eye", "ots", "MCU", "through", "over HER shoulder: the explanation lands on her", ["SH-OTS"], "eyes", "medium", k5,
  "L047", "Barbara, leaning in, counts it off", "F2", ["C1", "N"], "L-KITCHEN", speaking=True, day="B5", cue="on 'that spot.'", pace="still", ing=["C1", "N", "L-KITCHEN", "VOICE-C1"])
R("SC08-SH04", g, "SHOT", "N", "eye", "profile", "CU", "clean", "profile on HER taking it in", ["SH-PROFILE", "SH-CU"], "eyes", "shallow", k5,
  "L048", "HER listens, looking down at her own knee", "F1", ["N"], "L-KITCHEN", day="B5", cue="on 'Nothing more.'", pace="still", ing=["N", "L-KITCHEN"])
R("SC08-SH05", g, "SHOT", "C1", "low", "three-quarter", "CU", "clean", "low on Barbara's last line — she is sure", ["SH-LOW", "SH-CU"], "eyes", "shallow", k5,
  "L049", "Barbara taps the table once beside the box", "F1", ["C1"], "L-KITCHEN", speaking=True, day="B5", cue="on 'off.'", pace="slow push-in", ing=["C1", "L-KITCHEN", "VOICE-C1"])

# ---------- SC09 — PROOF IN THE FAMILY (VO montage, one-offs) ----------
g = "SC09"
R("SC09-SH01", g, "SHOT", "X4", "eye", "three-quarter", "MEDIUM", "clean", "", ["SH-34", "SH-MED"], "product", "medium", L("clinic window", "L", "midday", "After — clear daylight", 5600),
  "L050", "a sports-medicine doctor fits the strap below a patient's kneecap in a bright clinic", "F2", ["X4"], "L-CLINIC", product=True, day="A1", cue="on 'Sports doctors.'", pace="one move", ing=["L-CLINIC", "PROD-FRONT", "INFO-PLACEMENT"])
R("SC09-SH02", g, "SHOT", "X5", "low", "profile", "FULL", "clean", "low profile on a full swing — 76 and strong", ["SH-LOW", "SH-PROFILE"], "product", "deep", L("the sun", "R", "morning", "After — clear daylight", 5600),
  "L051", "Barbara's husband, 76, takes a full golf swing on a green fairway, the strap on his knee under his shorts", "F2", ["X5"], "L-GOLF", product=True, day="A1g", cue="on 'twice a week.'", pace="one swing", ing=["L-GOLF", "PROD-FRONT"])
R("SC09-SH03", g, "SHOT", "X6", "eye", "front", "WIDE", "clean", "", ["SH-WIDE", "SH-EYE"], "product", "deep", L("the sun", "L", "afternoon", "After — clear daylight", 5600),
  "L051", "Barbara's niece, 22, runs across a tennis court for a forehand, the strap on her knee", "F2", ["X6"], "L-TENNIS", product=True, day="A1t", cue="on '22.'", pace="one shot", ing=["L-TENNIS", "PROD-FRONT"], moving=True)

# ---------- SC10 — SIX WEEKS (story day A2) ----------
g = "SC10"; b10 = L("the bedroom window", "L", "morning", "After — warm morning sun", 5000)
R("SC10-SH01", g, "INSERT", "N", "low", "front", "ECU", "clean", "low on the knee: the strap going on, then hidden", ["SH-MACRO", "SH-LOW"], "product", "shallow", b10,
  "L052", "six weeks later: on the bed edge, HER slides the strap up to just below her right kneecap, then pulls her trouser leg down over it", "F2", ["N"], "L-BEDROOM", face=False, product=True, day="A2", cue="on 'there.'", pace="two moves", ing=["N", "L-BEDROOM", "PROD-FRONT", "INFO-PLACEMENT"])
R("SC10-SH02", g, "INSERT", "N", "overhead", "front", "ECU", "clean", "overhead: the same table, empty now — the mirror of the pills", ["SH-OVER", "SH-MACRO"], "deep", "medium", L("the kitchen window", "L", "morning", "After — warm morning sun", 5000),
  "L052", "the pine table with just a mug of tea on it — no pills, no gel", "F2", [], "L-KITCHEN", face=False, day="A2", cue="on 'lunchtime.'", pace="still", ing=["L-KITCHEN"], mirror="SC03-SH04")
hs = L("the late-morning sun", "R", "midday", "After — warm open daylight", 5600)
R("SC10-SH03", g, "SHOT", "N", "eye", "profile", "FULL", "clean", "lateral track beside her walk — pace made visible", ["SH-PROFILE"], "deep", "deep", hs,
  "L053", "HER walks briskly along the high street past shopfronts, overtaking three younger women", "F9", ["N"], "L-HIGHST", day="A2", cue="on 'half my age.'", pace="brisk, two steps per second", ing=["N", "INFO-HIGHST"], moving=True)
R("SC10-SH04", g, "SHOT", "N", "low", "three-quarter", "MEDIUM", "clean", "low: she stands square, rooted — strength", ["SH-LOW", "SH-34"], "eyes", "medium", L("the shop's glass front", "L", "midday", "After — warm open daylight", 4500),
  "L054", "HER stands square in the checkout queue, a full basket in her hand, weight even on both feet, completely still", "F2", ["N"], "L-SHOP", day="A2", cue="on 'weight.'", pace="still", ing=["N", "L-SHOP"])
R("SC10-SH05", g, "SHOT", "X3", "eye", "ots", "MCU", "through", "over HER shoulder onto the cashier", ["SH-OTS"], "eyes", "shallow", L("the shop's glass front", "L", "midday", "After — warm open daylight", 4500),
  "L055", "the young cashier reaches across for the two full bags", "F2", ["X3", "N"], "L-SHOP", speaking=True, day="A2", cue="on 'love?'", pace="one reach", ing=["N", "L-SHOP", "VOICE-X3"])
R("SC10-SH06", g, "SHOT", "N", "eye", "three-quarter", "CU", "clean", "", ["SH-34", "SH-CU"], "eyes", "shallow", L("the shop's glass front", "L", "midday", "After — warm open daylight", 4500),
  "L056", "HER lifts both bags herself with a small smile", "F1", ["N"], "L-SHOP", speaking=True, day="A2", cue="on 'actually.'", pace="one lift", ing=["N", "L-SHOP", "VOICE-N"])
R("SC10-SH07", g, "SHOT", "N", "eye", "behind", "WIDE", "clean", "behind her, walking away up her own street with the bags", ["SH-WIDE", "SH-REAR"], "deep", "deep", L("the afternoon sun", "back", "afternoon", "After — warm open daylight", 5000, "the sun ahead of her down the street: she walks into it"),
  "L057", "HER walks up her street toward her front door, a full bag in each hand", "F2", ["N"], "L-HIGHST", face=False, day="A2", cue="on 'helped me.'", pace="brisk", ing=["N", "P-HOUSE-EXT"], moving=True)

# ---------- SC11 — THE HUSBAND (A2 afternoon, living room) ----------
g = "SC11"; l11 = L("the bay window", "L", "afternoon", "After — warm afternoon", 5000)
R("SC11-SH01", g, "SHOT", "C3", "eye", "three-quarter", "MEDIUM", "through", "through the doorway: him in his chair, as always", ["SH-MED", "SH-OCCL"], "eyes", "medium", l11,
  "L058", "the husband in his leather armchair by the fire looks up from his newspaper", "F2", ["C3"], "L-LIVING", speaking=True, day="A2", cue="on 'time.'", pace="still", ing=["C3", "L-LIVING", "P-HOUSE", "VOICE-C3"])
R("SC11-SH02", g, "SHOT", "N", "low", "front", "MCU", "clean", "low on her in the doorway, bags down — she has won", ["SH-LOW"], "eyes", "shallow", l11,
  "L059", "HER stands in the living-room doorway, bags at her feet, cheeks flushed from the walk", "F1", ["N"], "L-LIVING", speaking=True, day="A2", cue="on 'I know.'", pace="still", ing=["N", "L-LIVING", "P-HOUSE", "VOICE-N"])

# ---------- SC12 — THE CAFÉ + REVEAL (story day A3) ----------
g = "SC12"; cf = L("the café front window", "L", "midday", "After — honeyed daylight", 4800)
R("SC12-SH01", g, "SHOT", "N", "eye", "three-quarter", "WIDE", "through", "past the friends at the table: she crosses the room — nobody waits for her", ["SH-WIDE", "SH-FGFOC"], "deep", "deep", cf,
  "L060 L061", "HER walks across the café floor straight to the window table where her two friends sit, easy and quick", "F2", ["N", "C5", "C6"], "L-CAFE", day="A3", cue="on 'anymore.'", pace="brisk", ing=["N", "C5", "C6", "L-CAFE"], moving=True)
R("SC12-SH02", g, "SHOT", "C5", "eye", "ots", "MCU", "through", "over HER shoulder onto Friend 1", ["SH-OTS"], "eyes", "medium", cf,
  "L062", "Friend 1 looks her up and down as she sits", "F2", ["C5", "N"], "L-CAFE", speaking=True, day="A3", cue="on 'haircut.'", pace="still", ing=["C5", "N", "L-CAFE", "VOICE-C5"])
R("SC12-SH03", g, "SHOT", "N", "eye", "three-quarter", "CU", "clean", "", ["SH-34", "SH-CU"], "eyes", "shallow", cf,
  "L063", "HER, settled in her chair, meets her eye", "F1", ["N"], "L-CAFE", speaking=True, day="A3", cue="on 'like that.'", pace="still", ing=["N", "L-CAFE", "VOICE-N"])
R("SC12-SH04", g, "SHOT", "C6", "low", "profile", "MCU", "clean", "low profile: Friend 2 leans in, curious", ["SH-PROFILE", "SH-LOW"], "eyes", "medium", cf,
  "L064", "Friend 2 leans forward over her coffee", "F2", ["C6"], "L-CAFE", speaking=True, day="A3", cue="on 'it?'", pace="still", ing=["C6", "L-CAFE", "VOICE-C6"])
R("SC12-SH05", g, "INSERT", "N", "low", "three-quarter", "ECU", "clean", "under the table: the reveal, an inch", ["SH-MACRO", "SH-LOW"], "product", "shallow", cf,
  "L065", "under the table HER lifts her trouser leg an inch and the strap shows just below her right kneecap", "F2", ["N"], "L-CAFE", face=False, product=True, day="A3", cue="on 'strap.'", pace="one lift", ing=["N", "L-CAFE", "PROD-FRONT", "INFO-PLACEMENT"])
R("SC12-SH06", g, "SHOT", "C5", "eye", "front", "CU", "clean", "", ["SH-CU", "SH-EYE"], "eyes", "shallow", cf,
  "L066", "Friend 1 peers down, unconvinced", "F1", ["C5"], "L-CAFE", speaking=True, day="A3", cue="on 'thing?'", pace="still", ing=["C5", "L-CAFE", "VOICE-C5"])
R("SC12-SH07", g, "SHOT", "N", "high", "three-quarter", "MCU", "clean", "slightly high on her sitting back — at ease, nothing to prove", ["SH-34", "SH-HIGH"], "eyes", "medium", cf,
  "L067", "HER sits back and picks up her cup", "F2", ["N"], "L-CAFE", speaking=True, day="A3", cue="on 'said.'", pace="still", ing=["N", "L-CAFE", "VOICE-N"])
R("SC12-SH08", g, "INSERT", "N", "eye", "three-quarter", "ECU", "clean", "the name, on the table between the cups", ["SH-MACRO", "SH-34"], "product", "shallow", cf,
  "L068", "the strap lies on the café table between the cups, its wordmark reading", "F2", [], "L-CAFE", face=False, product=True, day="A3", cue="on 'real thing.'", pace="slow push-in", ing=["L-CAFE", "PROD-FRONT"])
R("SC12-SH09", g, "SHOT", "N", "eye", "ots", "MEDIUM", "through", "over Friend 2's shoulder onto the table: the three of them together", ["SH-OTS", "SH-MED"], "eyes", "medium", cf,
  "L068", "the three women laughing together at the window table", "F2", ["N", "C5", "C6"], "L-CAFE", day="A3", cue="on 'sites.'", pace="still", ing=["N", "C5", "C6", "L-CAFE"])

# ---------- SC13 — THE OFFER, PLANTED IN THE STORY (A4 Sunday) ----------
g = "SC13"; k13 = L("the kitchen window", "L", "afternoon", "After — warm afternoon", 5000)
R("SC13-SH01", g, "INSERT", "N", "high", "three-quarter", "ECU", "clean", "high on the table: two straps, the offer", ["SH-MACRO", "SH-HIGH"], "product", "shallow", k13,
  "L069", "HER hands lift the lid of a small box on the kitchen table: two straps side by side inside", "F2", ["N"], "L-KITCHEN", face=False, product=True, day="A4", cue="on 'work.'", pace="one lift", ing=["N", "L-KITCHEN", "PROD-BOX"])
R("SC13-SH02", g, "SHOT", "N", "eye", "three-quarter", "CU", "clean", "", ["SH-34", "SH-CU"], "eyes", "shallow", k13,
  "L070 L071", "HER looks at the box, quiet, then out of the window", "F1", ["N"], "L-KITCHEN", day="A4", cue="on the doorbell", pace="slow push-in", ing=["N", "L-KITCHEN"])
hl = L("the front door glass", "back", "afternoon", "After — warm afternoon", 5000, "the sister framed against the open door's daylight: the arrival")
R("SC13-SH03", g, "SHOT", "C4", "eye", "ots", "MEDIUM", "through", "over HER shoulder: the door opens on the sister", ["SH-OTS", "SH-MED"], "eyes", "medium", L("the front door glass", "L", "afternoon", "After — warm afternoon", 5000),
  "L072", "HER opens the front door; her sister on the step, eyes going past her to the staircase", "F2", ["C4", "N"], "P-HOUSE", speaking=True, day="A4", cue="on 'up?'", pace="still", ing=["C4", "N", "P-HOUSE", "VOICE-C4"])
R("SC13-SH04", g, "SHOT", "N", "low", "three-quarter", "MCU", "clean", "low on her in the doorway: the host of her own house again", ["SH-LOW", "SH-34"], "eyes", "shallow", L("the front door glass", "R", "afternoon", "After — warm afternoon", 5000),
  "L073", "HER, holding the door, nods", "F1", ["N"], "P-HOUSE", speaking=True, day="A4", cue="on 'up.'", pace="still", ing=["N", "P-HOUSE", "VOICE-N"])
R("SC13-SH05", g, "SHOT", "C4", "high", "behind", "FULL", "clean", "high from the landing: the sister's first step, hand on the rail — the loop paid", ["SH-HIGH", "SH-REAR"], "deep", "deep", L("the frosted landing window", "L", "afternoon", "After — warm afternoon", 5000),
  "L074", "the sister puts her hand on the banister and takes the first step up, HER one step behind her", "F2", ["C4", "N"], "L-STAIRS", face=False, day="A4", cue="end", pace="one step, then the next", ing=["C4", "N", "L-STAIRS", "P-HOUSE"])

json.dump(ROWS, open(HERE / "act_map.json", "w"), indent=1, ensure_ascii=False)
print(len(ROWS), "rows")
