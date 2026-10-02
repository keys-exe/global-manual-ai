#!/usr/bin/env python3
"""§18 step 5 — act map (E4 rows) for stryde-her-dad, Mode 4 film on Seedance 2.5 (Kie). One row per shot in cut order;
`take` groups connected rows into one Seedance call (§24K part 5, V7.88.0). Lines are L-ids from work/lines.json."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
LINES = {l["id"]: l for l in json.load(open(HERE.parent / "work/lines.json"))}
ROWS = []
def L(src, key, time, arc, k, why=None):
    d = {"source": src, "key_side": key, "time": time, "arc": arc, "kelvin": k}
    if why: d["why"] = why
    return d
def dur(lines, extra=0.0):
    w = sum(LINES[x]["words"] for x in lines.split()) if lines else 0
    return round(max(2.0, w / 2.6 + 0.6 + extra), 1)
def R(beat, grp, typ, subj, h, side, scale, fg, why, shot, plane, dof, light, lines="", action="", rig="F2", cast=(), loc="", face=True,
      speaking=False, product=False, day=None, cue="", pace="", ing=(), mirror=None, moving=False, take=None, kind=None, start=None, end=None,
      split=None, music="", extra=0.0, voice=None):
    r = {"beat": beat, "group": grp, "scene": grp, "type": typ, "subject": subj, "height": h, "side": side, "scale": scale, "fg": fg,
         "why": why, "mode": 4, "shot": shot, "speaking": speaking, "product_beat": product,
         "focus": {"plane": plane, "dof": dof, "rack": None, "moving_subject": moving}, "story_day": day, "face": face,
         "light": light, "lines": lines, "voice": voice or ("VO" if lines and LINES[lines.split()[0]]["disp"] == "VO" else ("lip-sync" if speaking else ("off" if lines else ""))),
         "action": action, "pace": pace, "rig": rig, "cast": list(cast), "location": loc, "cut": cue, "ingredients": list(ing),
         "mirror_of": mirror, "take": take, "duration": dur(lines, extra), "music": music, "layout": "full"}
    if kind: r["take_kind"] = kind
    if start: r["start_pos"] = start
    if end: r["end_pos"] = end
    if split: r["split"] = split
    ROWS.append(r)

# ======================= SC01 — HOOK: THE VAN (D1, garden-centre car park, flat overcast) =======================
g, d, loc, m = "SC01", "D1", "L-CARPARK", "MUS-OPEN"
cp = L("the flat overcast sky over the car park", "L", "midday", "Hook — flat grey overcast, cold", 6500)
R("SC01-SH01", g, "SHOT", "C2", "high", "three-quarter", "WIDE", "clean", "high wide: Sue small at the open boot, the van's back doors already coming at her — the danger before anyone sees it", ["SH-WIDE", "SH-HIGH"], "deep", "deep", cp,
  "", "Sue lifts a potted plant into the open boot of the silver hatchback; two bays along, the white van's reversing lights come on and it starts to roll back toward her; Tony stands ten feet behind her holding a potted plant", "F2", ["C2", "C1"], loc, day=d, cue="as the van starts to roll", pace="the van creeps back at walking pace", ing=["C2", "C1", loc], take="SC01-T1", kind="multi",
  start="Sue at the open boot of the silver hatchback, back to the van, lifting a potted plant in; Tony ten feet behind her on the tarmac, facing her, a potted plant held in both hands at his waist; the white van two bays along, its back doors toward her", music=m, extra=1.5)
R("SC01-SH02", g, "SHOT", "C1", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow", cp,
  "L001", "Tony sees the van and shouts her name, the plant still in his hands", "F2", ["C1"], loc, speaking=True, day=d, cue="on 'SUE!'", pace="sudden", ing=["C1", loc, "VOICE-C1"], take="SC01-T1", music=m)
R("SC01-SH03", g, "SHOT", "C1", "low", "profile", "FULL", "clean", "low profile: the first step and the knee goes — the body betrays him at ground level", ["SH-PROFILE", "SH-LOW"], "deep", "deep", cp,
  "", "Tony drops the plant (the pot cracks on the tarmac) and lunges one step toward her; on that step his right knee buckles and he goes down onto that knee, one hand to the ground", "F2", ["C1"], loc, day=d, cue="as his knee hits the tarmac", pace="one step, then the drop, over two seconds", ing=["C1", loc], take="SC01-T1", music=m, extra=1.8)
R("SC01-SH04", g, "SHOT", "C4", "eye", "front", "FULL", "clean", "", ["SH-WIDE", "SH-EYE"] if False else ["SH-EYE"], "deep", "deep", cp,
  "", "the young garden-centre worker in the green fleece runs past Tony from behind him and pulls Sue clear by the arm, two steps to the side, as the van stops short a metre from the boot", "F5", ["C4", "C2", "C1"], loc, day=d, cue="as the van's brake lights flare", pace="the lad runs four strides; the pull is one move", ing=["C4", "C2", "C1", loc], moving=True, take="SC01-T1",
  end="the lad holding Sue by both upper arms beside the hatchback's rear wheel, both facing each other; the van stopped a metre short of the open boot; Tony down on his right knee ten feet away, the cracked pot beside him", music=m, extra=1.6)
R("SC01-SH05", g, "SHOT", "C4", "eye", "ots", "MCU", "through", "over Sue's shoulder onto the lad — the stranger who got there", ["SH-OTS"], "eyes", "shallow", cp,
  "L002", "the lad, holding Sue by both upper arms, breathless, reassuring her", "F2", ["C4", "C2"], loc, speaking=True, day=d, cue="on 'got you.'", pace="still, breathing hard", ing=["C4", "C2", loc, "VOICE-C4"], take="SC01-T2", kind="multi",
  start="the lad holding Sue by both upper arms beside the hatchback's rear wheel, facing each other; Tony down on his right knee ten feet away behind the lad", split="length", music=m)
R("SC01-SH06", g, "SHOT", "C4", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow", cp,
  "L003", "the lad glances past Sue toward Tony on the ground, kind and concerned, and asks her", "F2", ["C4"], loc, speaking=True, day=d, cue="on 'go over.'", pace="still", ing=["C4", loc, "VOICE-C4"], take="SC01-T2", music=m)
R("SC01-SH07", g, "SHOT", "C2", "eye", "front", "CU", "clean", "", ["SH-CU"], "eyes", "shallow", cp,
  "L004", "Sue, shaken, glances at Tony, then back to the lad, and doesn't correct him", "F2", ["C2"], loc, speaking=True, day=d, cue="on 'love.'", pace="a beat before she speaks", ing=["C2", loc, "VOICE-C2"], take="SC01-T2",
  end="Sue turned toward the lad, the lad letting go of her arms; Tony still on his right knee ten feet away", music=m, extra=0.8)
R("SC01-SH08", g, "SHOT", "C1", "low", "three-quarter", "CU", "clean", "low close on Tony on one knee: the ground he couldn't cross; his inner voice over his face", ["SH-CU", "SH-LOW"], "eyes", "shallow", cp,
  "L005", "Tony, still down on his right knee on the wet tarmac beside the cracked pot, watches them; mouth closed, his face holding it; the camera eases in", "F1", ["C1"], loc, day=d, cue="end of VO", pace="still; slow push-in", ing=["C1", loc], take="SC01-T3",
  start="Tony down on his right knee on the tarmac, the cracked pot beside his left hand, looking toward Sue and the lad by the hatchback", end="the same, closer", split="length", music=m)

# ======================= SC02 — THE CAR (D1, straight after, inside the hatchback) =======================
g, loc, m = "SC02", "L-CAR", "MUS-OPEN"
cr = L("the windscreen and side windows, overcast", "L", "midday", "Before — flat grey, close", 6500)
R("SC02-SH01", g, "SHOT", "C2", "eye", "profile", "MCU", "clean", "profile: she stares out of the windscreen, not starting the car — what she saw stays inside", ["SH-PROFILE"], "eyes", "shallow", cr,
  "L006", "Sue in the driver's seat, both hands on the wheel, the key not turned, staring ahead; mouth closed, her own thought over her face", "F2", ["C2"], loc, day=d, cue="end of VO", pace="still", ing=["C2", loc], take="SC02-T1", kind="multi",
  start="Sue in the driver's seat (right), hands on the wheel; Tony in the passenger seat (left), his trouser knee dirty from the tarmac, both facing the windscreen", music=m)
R("SC02-SH02", g, "SHOT", "C2", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow", cr,
  "L007", "Sue turns her head to him", "F2", ["C2"], loc, speaking=True, day=d, cue="on 'about it?'", pace="still", ing=["C2", loc, "VOICE-C2"], take="SC02-T1", music=m)
R("SC02-SH03", g, "SHOT", "C1", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow", cr,
  "L008", "Tony keeps looking out of the windscreen", "F2", ["C1"], loc, speaking=True, day=d, cue="on 'say?'", pace="still", ing=["C1", loc, "VOICE-C1"], take="SC02-T1", music=m)
R("SC02-SH04", g, "SHOT", "C2", "eye", "ots", "MCU", "through", "over his shoulder onto her — she is pressing, he won't look", ["SH-OTS"], "eyes", "shallow", cr,
  "L009", "Sue, at him, voice tight; she stops before the end of the sentence", "F2", ["C2", "C1"], loc, speaking=True, day=d, cue="on 'Tony…'", pace="still", ing=["C2", "C1", loc, "VOICE-C2"], take="SC02-T1",
  end="both in their seats, Sue turned toward Tony, Tony facing the windscreen", music=m)
R("SC02-SH05", g, "SHOT", "C1", "eye", "front", "CU", "clean", "", ["SH-CU"], "eyes", "shallow", cr,
  "L010", "Tony, quiet, still facing ahead", "F2", ["C1"], loc, speaking=True, day=d, cue="on 'you.'", pace="still", ing=["C1", loc, "VOICE-C1"], take="SC02-T2", kind="multi",
  start="Sue turned toward Tony, Tony facing the windscreen", split="length", music=m)
R("SC02-SH06", g, "SHOT", "C2", "eye", "three-quarter", "CU", "clean", "", ["SH-CU", "SH-34"], "eyes", "shallow", cr,
  "L011", "Sue, flat", "F2", ["C2"], loc, speaking=True, day=d, cue="on 'step.'", pace="still", ing=["C2", loc, "VOICE-C2"], take="SC02-T2", music=m)
R("SC02-SH07", g, "SHOT", "C2", "eye", "ots", "MCU", "through", "over him onto her: the fear under the anger", ["SH-OTS"], "eyes", "shallow", cr,
  "L012", "Sue, her eyes wet, holding it together", "F2", ["C2", "C1"], loc, speaking=True, day=d, cue="on 'chair.'", pace="still", ing=["C2", "C1", loc, "VOICE-C2"], take="SC02-T2", music=m)
R("SC02-SH08", g, "SHOT", "C1", "eye", "profile", "MCU", "clean", "profile: he answers the windscreen, not her", ["SH-PROFILE"], "eyes", "shallow", cr,
  "L013", "Tony, jaw set", "F2", ["C1"], loc, speaking=True, day=d, cue="on 'anywhere.'", pace="still", ing=["C1", loc, "VOICE-C1"], take="SC02-T2",
  end="Sue turned toward Tony, Tony facing the windscreen", music=m)
R("SC02-SH09", g, "SHOT", "C2", "eye", "front", "CU", "clean", "", ["SH-CU"], "eyes", "shallow", cr,
  "L014", "Sue, quietly — the line that lands", "F1", ["C2"], loc, speaking=True, day=d, cue="on 'dad?'", pace="still; slow push-in", ing=["C2", loc, "VOICE-C2"], take="SC02-T3", kind="multi",
  start="Sue turned toward Tony, Tony facing the windscreen", split="length", music=m)
R("SC02-SH10", g, "SHOT", "C1", "eye", "three-quarter", "CU", "clean", "", ["SH-CU", "SH-34"], "eyes", "shallow", cr,
  "L015", "Tony finally turns his head and looks at her", "F2", ["C1"], loc, speaking=True, day=d, cue="on 'like this.'", pace="a slow turn of the head, then still", ing=["C1", loc, "VOICE-C1"], take="SC02-T3", music=m)
R("SC02-SH11", g, "SHOT", "C1", "eye", "behind", "MEDIUM", "clean", "from the back seat: two heads, the windscreen and the garden centre — the silence after", ["SH-REAR"], "deep", "deep", cr,
  "", "the two of them sit side by side looking out at the garden centre; neither moves; Sue turns the key", "F2", ["C1", "C2"], loc, face=False, day=d, cue="as the engine starts", pace="still", ing=["C1", "C2", loc], take="SC02-T3",
  end="both facing the windscreen, Sue's hand on the key", music=m, extra=2.0)

# ======================= SC03 — ROCK BOTTOM (D2, a weekday: bedroom morning → stairs → the car park afternoon) =======================
g, d, m = "SC03", "D2", "MUS-EXPOSE"
bd = L("the sash window over the chest of drawers, cool morning", "L", "morning", "Problem — cool grey morning", 6500)
R("SC03-SH01", g, "SHOT", "C1", "high", "three-quarter", "MCU", "clean", "high on him at the drawer: the pile of things that never worked, pressing down", ["SH-HIGH", "SH-34"], "hands", "medium", bd,
  "L016", "Tony, dressed for work, shoves a beige knee sleeve back into the top drawer of the pine chest of drawers; the drawer is full of knee sleeves and supports and won't shut; he leans on it with his palm until it closes; mouth closed", "F2", ["C1"], "L-BEDROOM", day=d, cue="as the drawer bangs shut", pace="one push, then a second", ing=["C1", "L-BEDROOM", "P-HOUSE"], take="SC03-T1",
  start="Tony standing at the open top drawer of the pine chest of drawers under the window, a beige knee sleeve in his right hand", end="Tony's palm flat on the shut drawer", music=m, extra=0.5)
st = L("the frosted front-door glass at the foot of the stairs", "front", "morning", "Problem — cool grey morning", 6500, why="the only light in the stairwell comes up from the front door; he comes down into it")
R("SC03-SH02", g, "SHOT", "C1", "high", "behind", "FULL", "clean", "high from the landing behind him: going down his own stairs sideways like a man of 85 — the low point", ["SH-REAR", "SH-HIGH"], "deep", "deep", st,
  "L016", "Tony goes down the steep narrow stairs sideways, both hands on the white handrail, leading with his left foot, bringing the stiff right leg down beside it, one step at a time", "F2", ["C1"], "L-STAIRS", face=False, day=d, cue="on the third step", pace="one step every two seconds, foot then foot onto the same step", ing=["C1", "L-STAIRS", "P-HOUSE"], take="SC03-T2", kind="multi",
  start="Tony on the top step of the flight, side-on to the stairs facing the handrail, both hands on the white handrail", moving=True, music=m, extra=1.0)
R("SC03-SH03", g, "SHOT", "C1", "low", "front", "FULL", "clean", "low from the hall up the flight: his face tight on each step — the effort", ["SH-LOW", "SH-WIDE"] if False else ["SH-LOW"], "eyes", "medium", st,
  "", "halfway down, still sideways, Tony lowers the stiff right leg onto the next step, his face tight; mouth closed", "F2", ["C1"], "L-STAIRS", day=d, cue="as both feet land on the step", pace="one step every two seconds", ing=["C1", "L-STAIRS", "P-HOUSE"], take="SC03-T2",
  end="Tony halfway down the flight, side-on, both hands on the handrail", music=m, extra=2.5)
cpk = L("the flat overcast sky through the car windows", "L", "afternoon", "Problem — flat grey", 6500)
R("SC03-SH04", g, "SHOT", "C1", "eye", "profile", "MCU", "through", "profile through the passenger window: he waits in the car while, behind him through the back window, she lifts the shopping in", ["SH-PROFILE", "SH-BGFOC"] if False else ["SH-PROFILE"], "eyes", "medium", cpk,
  "L017", "Tony sits in the passenger seat of the parked hatchback, looking ahead; behind him, through the rear window, Sue lifts heavy shopping bags into the open boot on her own; mouth closed", "F2", ["C1", "C2"], "L-CAR", day=d, cue="as the boot slams", pace="still", ing=["C1", "C2", "L-CAR", "L-CARPARK"], take="SC03-T3",
  start="Tony in the passenger seat facing ahead; Sue at the open boot behind the car, lifting bags", end="the boot shut, Tony still facing ahead", music=m)

# ======================= SC04 — THE GP (D3, consulting room, cool) =======================
g, d, loc, m = "SC04", "D3", "L-GP", "MUS-EXPOSE"
gp = L("the window with vertical blinds and the ceiling panel", "R", "morning", "Problem — cool clinical white", 4500)
R("SC04-SH01", g, "SHOT", "C5", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow", gp,
  "L018", "the GP turns from her screen to Tony, brisk and kind", "F2", ["C5"], loc, speaking=True, day=d, cue="on 'nick.'", pace="still", ing=["C5", loc, "VOICE-C5"], take="SC04-T1", kind="multi",
  start="the GP in her office chair at the desk, turned to Tony; Tony in the patient chair at the desk's corner, hands on his knees", music=m)
R("SC04-SH02", g, "SHOT", "C1", "eye", "ots", "MCU", "through", "over the GP's shoulder onto Tony: he is the one under examination", ["SH-OTS"], "eyes", "shallow", gp,
  "L019", "Tony, flat, rubbing his right knee", "F2", ["C1", "C5"], loc, speaking=True, day=d, cue="on '85.'", pace="still", ing=["C1", "C5", loc, "VOICE-C1"], take="SC04-T1", music=m)
R("SC04-SH03", g, "SHOT", "C5", "low", "three-quarter", "MCU", "clean", "slightly low on the GP: the authority that says normal", ["SH-LOW", "SH-34"], "eyes", "shallow", gp,
  "L020", "the GP, reasonable, a small shrug", "F2", ["C5"], loc, speaking=True, day=d, cue="on 'normal.'", pace="still", ing=["C5", loc, "VOICE-C5"], take="SC04-T1", music=m)
R("SC04-SH04", g, "SHOT", "C1", "eye", "front", "CU", "clean", "", ["SH-CU"], "eyes", "shallow", gp,
  "L021", "Tony, quiet, not accepting it", "F2", ["C1"], loc, speaking=True, day=d, cue="on 'normal.'", pace="still", ing=["C1", loc, "VOICE-C1"], take="SC04-T1",
  end="the GP turned to Tony, Tony in the patient chair, hands on his knees", music=m)
R("SC04-SH05", g, "SHOT", "C5", "eye", "profile", "MEDIUM", "clean", "profile: she is already typing — the appointment is over", ["SH-PROFILE", "SH-MED"], "eyes", "medium", gp,
  "L022", "the GP turns back to the screen and types as she speaks", "F2", ["C5"], loc, speaking=True, day=d, cue="on 'people.'", pace="still, typing", ing=["C5", loc, "VOICE-C5"], take="SC04-T2", kind="multi",
  start="the GP turning back to her screen; Tony in the patient chair", split="length", music=m)
R("SC04-SH06", g, "SHOT", "C1", "high", "three-quarter", "WIDE", "clean", "high wide from the corner: Tony small in the patient chair, alone with it", ["SH-WIDE", "SH-HIGH"], "deep", "deep", gp,
  "", "Tony sits in the patient chair looking down at his right knee while the GP types", "F2", ["C1", "C5"], loc, day=d, cue="hold", pace="still", ing=["C1", "C5", loc], take="SC04-T2",
  end="Tony looking down at his knee, the GP typing", music=m, extra=2.0)

# ======================= SC05 — GARY AT THE BUILDERS' YARD (D4, bright overcast) =======================
g, d, loc = "SC05", "D4", "L-YARD"
yd = L("the bright overcast sky over the yard", "L", "morning", "Turn — bright, open overcast", 6500)
m = "MUS-EDU"
R("SC05-SH01", g, "SHOT", "C3", "low", "profile", "WIDE", "clean", "low wide, Gary's left side to us: a man of 70 carrying a slab alone — the question before it is asked", ["SH-WIDE", "SH-LOW"], "deep", "deep", yd,
  "", "Gary lifts one grey paving slab off the pallet on his own and carries it to the flatbed truck; Tony walks in through the yard gate behind him", "F2", ["C3", "C1"], loc, day=d, cue="as Gary sets the slab down", pace="Gary walks four steady steps with the slab", ing=["C3", "C1", loc], moving=False, take="SC05-T1", kind="multi",
  start="Gary at the pallet of grey slabs, his left side to the camera, lifting one slab; Tony entering at the yard gate in the background", music=m, extra=2.0)
R("SC05-SH02", g, "SHOT", "C1", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow", yd,
  "L023", "Tony, by the flatbed, shaking his head at him", "F2", ["C1"], loc, speaking=True, day=d, cue="on 'than me.'", pace="still", ing=["C1", loc, "VOICE-C1"], take="SC05-T1", music=m)
R("SC05-SH03", g, "SHOT", "C3", "eye", "front", "MCU", "clean", "", ["SH-EYE"], "eyes", "shallow", yd,
  "L024", "Gary, wiping his hands on a rag, amused", "F2", ["C3"], loc, speaking=True, day=d, cue="on 'answer?'", pace="still", ing=["C3", loc, "VOICE-C3"], take="SC05-T1", music=m)
R("SC05-SH04", g, "SHOT", "C1", "eye", "ots", "MCU", "through", "over Gary onto Tony: listing everything that failed", ["SH-OTS"], "eyes", "shallow", yd,
  "L025", "Tony, counting it off, fed up", "F2", ["C1", "C3"], loc, speaking=True, day=d, cue="on 'shifts it.'", pace="still", ing=["C1", "C3", loc, "VOICE-C1"], take="SC05-T1",
  end="Gary and Tony standing by the flatbed facing each other, a metre apart", music=m)
R("SC05-SH05", g, "SHOT", "C3", "eye", "three-quarter", "CU", "clean", "", ["SH-CU", "SH-34"], "eyes", "shallow", yd,
  "L026", "Gary, matter-of-fact", "F2", ["C3"], loc, speaking=True, day=d, cue="on 'backside.'", pace="still", ing=["C3", loc, "VOICE-C3"], take="SC05-T2", kind="multi",
  start="Gary and Tony standing by the flatbed facing each other", split="length", music=m)
R("SC05-SH06", g, "SHOT", "C1", "eye", "front", "MCU", "clean", "", ["SH-EYE"], "eyes", "shallow", yd,
  "L027", "Tony, half a laugh", "F2", ["C1"], loc, speaking=True, day=d, cue="on 'over.'", pace="still", ing=["C1", loc, "VOICE-C1"], take="SC05-T2", music=m)
R("SC05-SH07", g, "SHOT", "C3", "eye", "ots", "MCU", "through", "over Tony onto Gary: he means it", ["SH-OTS"], "eyes", "shallow", yd,
  "L028", "Gary, serious now", "F2", ["C3", "C1"], loc, speaking=True, day=d, cue="on 'now.'", pace="still", ing=["C3", "C1", loc, "VOICE-C3"], take="SC05-T2", music=m)
R("SC05-SH08", g, "SHOT", "C1", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow", yd,
  "L029", "Tony, leaning in", "F2", ["C1"], loc, speaking=True, day=d, cue="on 'changed?'", pace="still", ing=["C1", loc, "VOICE-C1"], take="SC05-T2",
  end="Gary and Tony by the flatbed facing each other", music=m)
R("SC05-SH09", g, "SHOT", "C3", "eye", "profile", "MEDIUM", "clean", "profile two-shot as they sit on the slab pallet: the lesson begins", ["SH-PROFILE", "SH-MED"], "eyes", "medium", yd,
  "L030", "Gary sits on the edge of the pallet of slabs and nods Tony down beside him; Tony sits; Gary asks", "F2", ["C3", "C1"], loc, speaking=True, day=d, cue="on 'one spot?'", pace="one sit-down each", ing=["C3", "C1", loc, "VOICE-C3"], take="SC05-T3", kind="multi",
  start="Gary and Tony by the flatbed facing each other", split="length", music=m, extra=1.0)
R("SC05-SH10", g, "SHOT", "C1", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow", yd,
  "L031", "Tony, seated on the pallet, shrugs", "F2", ["C1"], loc, speaking=True, day=d, cue="on 'know.'", pace="still", ing=["C1", loc, "VOICE-C1"], take="SC05-T3", music=m)
R("SC05-SH11", g, "SHOT", "C3", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "hands", "medium", yd,
  "L032", "Gary leans over and points two fingers just below Tony's right kneecap without touching it", "F2", ["C3", "C1"], loc, speaking=True, day=d, cue="on 'down.'", pace="still", ing=["C3", "C1", loc, "VOICE-C3"], take="SC05-T3", music=m)
R("SC05-SH12", g, "INSERT", "C1", "high", "front", "CU", "clean", "high, straight down onto the knee: the one spot, found by his own fingers", ["SH-HIGH", "SH-CU"], "hands", "shallow", yd,
  "L033", "Tony's two fingers press the soft spot just below his bare right kneecap; his leg flinches a little", "F2", ["C1"], loc, face=False, day=d, cue="on 'There.'", pace="one press", ing=["C1", loc, "VOICE-C1"], take="SC05-T3", voice="off",
  end="Gary and Tony seated side by side on the edge of the slab pallet, Tony's fingers on his knee", music=m)
R("SC05-SH13", g, "SHOT", "C3", "eye", "front", "CU", "clean", "", ["SH-CU"], "eyes", "shallow", yd,
  "L034", "Gary, seated, quiet and sure", "F1", ["C3"], loc, speaking=True, day=d, cue="on 'changes.'", pace="still; slow push-in", ing=["C3", loc, "VOICE-C3"], take="SC05-T4", kind="multi",
  start="Gary and Tony seated side by side on the edge of the slab pallet", split="length", music=m)
R("SC05-SH14", g, "SHOT", "C1", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow", yd,
  "", "Tony listening, looking at his knee; mouth closed", "F2", ["C1"], loc, day=d, cue="hold", pace="still", ing=["C1", loc], take="SC05-T4",
  end="Gary and Tony seated on the pallet", music=m)
R("SC05-SH15", g, "SHOT", "C3", "eye", "profile", "MCU", "clean", "profile: the teacher talking to the side of the student's head", ["SH-PROFILE"], "eyes", "shallow", yd,
  "L035", "Gary, seated, explaining, a hand making the size of a coin with finger and thumb", "F2", ["C3"], loc, speaking=True, day=d, cue="on 'Nothing more.'", pace="still", ing=["C3", loc, "VOICE-C3"], take="SC05-T5", kind="multi",
  start="Gary and Tony seated side by side on the pallet", split="length", music=m)
R("SC05-SH16", g, "SHOT", "C1", "low", "three-quarter", "CU", "clean", "slightly low on Tony: it lands", ["SH-CU", "SH-LOW"], "eyes", "shallow", yd,
  "", "Tony looks up from his knee at Gary; mouth closed", "F2", ["C1"], loc, day=d, cue="hold", pace="still", ing=["C1", loc], take="SC05-T5", end="seated on the pallet", music=m)
R("SC05-SH17", g, "SHOT", "C1", "eye", "front", "MCU", "clean", "", ["SH-EYE"], "eyes", "shallow", yd,
  "L036", "Tony asks", "F2", ["C1"], loc, speaking=True, day=d, cue="on 'fix it?'", pace="still", ing=["C1", loc, "VOICE-C1"], take="SC05-T6", kind="multi",
  start="Gary and Tony seated side by side on the pallet", split="length", music=m)
R("SC05-SH18", g, "SHOT", "C3", "eye", "ots", "MCU", "through", "over Tony onto Gary: the list of what doesn't work", ["SH-OTS"], "eyes", "shallow", yd,
  "L037", "Gary, counting the wrong answers on his fingers", "F2", ["C3", "C1"], loc, speaking=True, day=d, cue="on 'that spot.'", pace="still", ing=["C3", "C1", loc, "VOICE-C3"], take="SC05-T6", end="seated on the pallet", music=m)
R("SC05-SH19", g, "SHOT", "C3", "eye", "three-quarter", "CU", "clean", "", ["SH-CU", "SH-34"], "eyes", "shallow", yd,
  "L038", "Gary, warm, certain", "F1", ["C3"], loc, speaking=True, day=d, cue="on 'paracetamol.'", pace="still; slow push-in", ing=["C3", loc, "VOICE-C3"], take="SC05-T7", kind="multi",
  start="Gary and Tony seated side by side on the pallet", split="length", music=m)
R("SC05-SH20", g, "SHOT", "C1", "eye", "front", "MCU", "clean", "", ["SH-EYE"], "eyes", "shallow", yd,
  "L039", "Tony, quiet", "F2", ["C1"], loc, speaking=True, day=d, cue="on 'do?'", pace="still", ing=["C1", loc, "VOICE-C1"], take="SC05-T7", end="seated on the pallet", music=m)
m = "MUS-TURN"   # the product's first frame: the music changes here (§40A, product_at = SC05-SH21)
R("SC05-SH21", g, "SHOT", "C3", "low", "three-quarter", "MEDIUM", "clean", "low as he stands and puts his boot up: the reveal", ["SH-LOW", "SH-MED"], "eyes", "medium", yd,
  "L040", "Gary stands and puts his right boot up on the edge of the pallet, his bare right knee toward Tony", "F2", ["C3", "C1"], loc, speaking=True, product=False, day=d, cue="on 'strap.'", pace="one move", ing=["C3", "C1", loc, "VOICE-C3", "front.webp"], take="SC05-T8", kind="multi",
  start="Gary and Tony seated side by side on the pallet", split="length", music=m)
R("SC05-SH22", g, "INSERT", "C3", "eye", "front", "CU", "clean", "front-on at knee height: the strap where it sits — the hero insert", ["SH-CU"], "product", "shallow", yd,
  "L040", "Gary's bare right knee, front-on, the black strap on it, the notch cupping the bottom of his kneecap; his two fingers tap the shell once", "F2", ["C3"], loc, face=False, product=True, day=d, cue="on 'the knee.'", pace="one tap", ing=["C3", loc, "VOICE-C3", "front.webp", "INFO-PLACEMENT"], take="SC05-T8", voice="off", music=m)
R("SC05-SH23", g, "SHOT", "C3", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow", yd,
  "L040", "Gary, boot still up on the pallet, to Tony", "F2", ["C3"], loc, speaking=True, day=d, cue="on 'surgeons.'", pace="still", ing=["C3", loc, "VOICE-C3"], take="SC05-T8",
  end="Gary standing with his right boot up on the pallet edge, Tony seated beside it", music=m)
R("SC05-SH24", g, "SHOT", "C3", "eye", "front", "MCU", "clean", "", ["SH-EYE"], "eyes", "shallow", yd,
  "L041", "Gary, boot back down, wagging a finger", "F2", ["C3"], loc, speaking=True, day=d, cue="on 'doesn't work.'", pace="still", ing=["C3", loc, "VOICE-C3"], take="SC05-T9", kind="multi",
  start="Gary standing by the pallet, Tony seated on its edge", split="length", music=m)
R("SC05-SH25", g, "SHOT", "C1", "high", "three-quarter", "CU", "clean", "slightly high on Tony, seated: the sceptic looking up", ["SH-CU", "SH-HIGH"], "eyes", "shallow", yd,
  "L042", "Tony, half a laugh, shaking his head", "F2", ["C1"], loc, speaking=True, day=d, cue="on 'off it.'", pace="still", ing=["C1", loc, "VOICE-C1"], take="SC05-T9", end="Gary standing by the pallet, Tony seated", music=m)
R("SC05-SH26", g, "SHOT", "C3", "eye", "ots", "MCU", "through", "over Tony onto Gary, grinning: he's been here", ["SH-OTS"], "eyes", "shallow", yd,
  "L043", "Gary, grinning, then plain", "F2", ["C3", "C1"], loc, speaking=True, day=d, cue="on 'a minute.'", pace="still", ing=["C3", "C1", loc, "VOICE-C3"], take="SC05-T10", kind="multi",
  start="Gary standing by the pallet, Tony seated on its edge", split="length", music=m)
R("SC05-SH27", g, "SHOT", "C1", "high", "behind", "WIDE", "clean", "high wide: Gary back to work, Tony alone on the pallet with his knee", ["SH-WIDE", "SH-HIGH"], "deep", "deep", yd,
  "", "Gary picks up another slab and walks off with it; Tony stays sitting on the pallet, looking down at his right knee", "F2", ["C1", "C3"], loc, face=False, day=d, cue="hold", pace="Gary walks four steps", ing=["C1", "C3", loc], take="SC05-T10",
  end="Tony alone seated on the pallet; Gary at the flatbed", music=m, extra=2.0)

# ======================= SC06 — SUE FINDS THE STRAP (D5, kitchen at night) =======================
g, d, loc, m = "SC06", "D5", "L-KITCHEN", "MUS-TURN"
kt = L("the warm glass pendant over the table", "R", "night", "Turn — warm tungsten in the dark", 2800)
R("SC06-SH01", g, "SHOT", "C2", "eye", "three-quarter", "MEDIUM", "clean", "", ["SH-MED", "SH-34"], "product", "medium", kt,
  "L044", "Sue at the round table picks up a small black strap from beside the post, holding it flat in her palm front side up, and looks up at Tony in the doorway", "F2", ["C2"], loc, speaking=True, product=True, day=d, cue="on 'that?'", pace="one pick-up", ing=["C2", loc, "P-HOUSE", "VOICE-C2", "front.webp"], take="SC06-T1", kind="multi",
  start="Sue seated at the small round oak table under the pendant, the strap lying beside the stack of post; Tony in the kitchen doorway from the hall", music=m)
R("SC06-SH02", g, "SHOT", "C1", "eye", "ots", "MCU", "through", "over Sue onto Tony in the doorway: caught", ["SH-OTS"], "eyes", "shallow", kt,
  "L045", "Tony in the doorway, offhand", "F2", ["C1", "C2"], loc, speaking=True, day=d, cue="on 'on.'", pace="still", ing=["C1", "C2", loc, "P-HOUSE", "VOICE-C1"], take="SC06-T1", music=m)
R("SC06-SH03", g, "SHOT", "C2", "eye", "front", "CU", "clean", "", ["SH-CU"], "eyes", "shallow", kt,
  "L046", "Sue, tired of hoping", "F2", ["C2"], loc, speaking=True, day=d, cue="on 'before.'", pace="still", ing=["C2", loc, "VOICE-C2"], take="SC06-T1", music=m)
R("SC06-SH04", g, "SHOT", "C1", "low", "three-quarter", "CU", "clean", "slightly low: the first time he pushes back", ["SH-CU", "SH-LOW"], "eyes", "shallow", kt,
  "L047", "Tony, steady, holds out his hand for the strap", "F2", ["C1"], loc, speaking=True, day=d, cue="on 'watch.'", pace="still", ing=["C1", loc, "VOICE-C1"], take="SC06-T1",
  end="Sue seated holding the strap out; Tony a step into the kitchen, hand out for it", music=m)

# ======================= SC07 — THE CHANGE (D6: stairs forwards → the yard → the street) =======================
g, d, m = "SC07", "D6", "MUS-AFTER"
s7 = L("the front-door glass, warm morning sun", "front", "morning", "After — the light opens", 5600, why="the front door glass is the only light on the stairs; he comes down into it")
R("SC07-SH01", g, "SHOT", "C1", "high", "behind", "FULL", "clean", "the same high angle behind him as SC03: forwards this time, hands off the rail", ["SH-REAR", "SH-HIGH"], "deep", "deep", s7,
  "L048", "Tony walks down the steep narrow stairs facing forwards, hands free of the rail, one foot per step, at an easy pace", "F2", ["C1"], "L-STAIRS", face=False, day=d, cue="on 'forwards.'", pace="one step per second", ing=["C1", "L-STAIRS", "P-HOUSE", "front.webp"], mirror="SC03-SH02", take="SC07-T1", kind="multi",
  start="Tony at the top of the flight facing down the stairs, hands at his sides, the strap on his right knee", moving=True, music=m)
R("SC07-SH02", g, "SHOT", "C1", "low", "front", "FULL", "clean", "low from the hall: his face coming down into the light — and he says nothing", ["SH-LOW"], "eyes", "medium", s7,
  "L048", "Tony reaches the bottom steps facing forwards, the black strap visible on his bare right knee below the work shorts; a small private look; mouth closed", "F2", ["C1"], "L-STAIRS", product=True, day=d, cue="as he steps onto the hall floor", pace="one step per second", ing=["C1", "L-STAIRS", "P-HOUSE", "front.webp"], mirror="SC03-SH03", take="SC07-T1",
  end="Tony standing on the hall floor at the foot of the stairs", music=m)
yd6 = L("bright morning sun over the yard", "L", "midday", "After — sun on the yard", 5600)
R("SC07-SH03", g, "SHOT", "C1", "eye", "three-quarter", "MEDIUM", "clean", "", ["SH-MED", "SH-34"], "deep", "deep", yd6,
  "L049", "Tony carries a sandstone slab briskly across the yard to the flatbed; a young labourer loading bricks calls after him, grinning", "F2", ["C1", "X2"], "L-YARD", day=d, cue="on 'Tone.'", pace="brisk, one step per second", ing=["C1", "X2", "L-YARD", "VOICE-X2"], take="SC07-T2", voice="off",
  start="Tony walking across the yard with a slab, the labourer at the flatbed", end="Tony at the flatbed setting the slab down", moving=True, music=m)
sv = L("the low afternoon sun down the street", "R", "afternoon", "After — warm low sun", 5000)
R("SC07-SH04", g, "SHOT", "C1", "eye", "profile", "FULL", "clean", "profile track beside him: a man walking at full pace down his own street", ["SH-PROFILE"], "deep", "deep", sv,
  "L050", "Tony walks home briskly along the pavement past the terraced fronts; an older neighbour putting her bin out turns as he passes and calls after him", "F9", ["C1", "X3"], "L-STREET", day=d, cue="on 'back.'", pace="brisk, one step per second, five steps", ing=["C1", "X3", "L-STREET", "VOICE-X3"], take="SC07-T3", kind="multi", voice="off",
  start="Tony walking along the pavement past the terraced fronts, the neighbour at her gate with her bin ahead of him", moving=True, music=m)
R("SC07-SH05", g, "SHOT", "C1", "eye", "three-quarter", "CU", "clean", "", ["SH-CU", "SH-34"], "eyes", "shallow", sv,
  "L051", "Tony, still walking, a small smile he keeps to himself; mouth closed", "F2", ["C1"], "L-STREET", day=d, cue="end of VO", pace="walking", ing=["C1", "L-STREET"], take="SC07-T3",
  end="Tony walking on down the street", music=m, extra=0.5)

# ======================= SC08 — THE PATIO (D7, back garden, low sun) =======================
g, d, loc, m = "SC08", "D7", "L-GARDEN", "MUS-AFTER"
gd = L("the low west sun over the garden wall", "L", "evening", "After — honeyed low sun", 4300)
R("SC08-SH01", g, "SHOT", "C1", "high", "three-quarter-back", "FULL", "through", "high past Sue at the back door: him on his knees on the patio he is laying — the trade back", ["SH-HIGH", "SH-FGFOC"] if False else ["SH-HIGH"], "deep", "deep", gd,
  "L052", "Tony kneels on the half-laid sandstone patio, tapping a flag level with the rubber mallet; Sue steps into the back doorway and stops", "F2", ["C1", "C2"], loc, speaking=True, day=d, cue="on 'Tony…'", pace="two taps of the mallet", ing=["C1", "C2", loc, "P-HOUSE", "VOICE-C2"], take="SC08-T1", kind="multi", voice="lip-sync",
  start="Tony kneeling on the half-laid patio with the rubber mallet, his back three-quarter to the house; Sue stepping into the back doorway", music=m)
R("SC08-SH02", g, "SHOT", "C2", "eye", "front", "CU", "clean", "", ["SH-CU"], "eyes", "shallow", gd,
  "", "Sue in the back doorway, watching him; mouth closed, her eyes filling", "F2", ["C2"], loc, day=d, cue="hold", pace="still", ing=["C2", loc, "P-HOUSE"], take="SC08-T1", music=m)
R("SC08-SH03", g, "SHOT", "C1", "low", "front", "WIDE", "clean", "low wide from the end of the garden, pulling back: the man on his knees, the woman in the doorway, the whole patio", ["SH-WIDE", "SH-LOW"], "deep", "deep", gd,
  "L053", "Tony, still kneeling, sets the next flag and taps it; Sue leans in the doorway watching; the camera pulls slowly back down the garden", "F6", ["C1", "C2"], loc, day=d, cue="end of VO", pace="slow pull-back", ing=["C1", "C2", loc], take="SC08-T1",
  end="Tony kneeling on the patio, Sue leaning in the back doorway", music=m, extra=1.0)

# ======================= SC09 — THE SAME CAR PARK, WEEKS LATER (D8, warm late afternoon) =======================
g, d, m = "SC09", "D8", "MUS-AFTER"
cr9 = L("warm low sun through the windscreen", "R", "afternoon", "After — warm gold", 4800)
R("SC09-SH01", g, "SHOT", "C2", "eye", "three-quarter", "MCU", "clean", "", ["SH-34"], "eyes", "shallow", cr9,
  "L054", "Sue in the passenger seat this time, as the car turns into the garden-centre car park", "F2", ["C2"], "L-CAR", speaking=True, day=d, cue="on 'here?'", pace="still", ing=["C2", "L-CAR", "VOICE-C2"], take="SC09-T1", kind="multi",
  start="Tony driving (right seat), Sue in the passenger seat (left), the car pulling into a bay", music=m)
R("SC09-SH02", g, "SHOT", "C1", "eye", "profile", "MCU", "clean", "profile at the wheel: he is driving now", ["SH-PROFILE"], "eyes", "shallow", cr9,
  "L055", "Tony at the wheel, easy", "F2", ["C1"], "L-CAR", speaking=True, day=d, cue="on 'compost.'", pace="still", ing=["C1", "L-CAR", "VOICE-C1"], take="SC09-T1", end="the car parked, both in their seats", music=m)
cp9 = L("warm low late-afternoon sun across the car park", "R", "afternoon", "After — warm gold", 4800)
R("SC09-SH03", g, "SHOT", "C2", "high", "three-quarter", "WIDE", "clean", "the same high wide as the hook: Sue at the boot, a car backing out at her — the mirror", ["SH-WIDE", "SH-HIGH"], "deep", "deep", cp9,
  "", "Sue stands at the open boot of the silver hatchback; a car two bays along reverses out fast toward her; Tony is ten feet behind her", "F2", ["C2", "C1"], "L-CARPARK", day=d, cue="as the car starts back", pace="the car backs out quickly", ing=["C2", "C1", "L-CARPARK"], mirror="SC01-SH01", take="SC09-T2", kind="multi",
  start="Sue at the open boot of the silver hatchback, back to the row; Tony ten feet behind her facing her; a car two bays along starting to reverse", music=m)
R("SC09-SH04", g, "SHOT", "C1", "low", "profile", "FULL", "clean", "the same low profile as the hook: three strides, no fall", ["SH-PROFILE", "SH-LOW"], "deep", "deep", cp9,
  "", "Tony covers the ten feet to her in three long strides and steers her clear with an arm round her back as the car brakes and stops", "F5", ["C1", "C2"], "L-CARPARK", product=False, day=d, cue="as the car stops", pace="three strides in two seconds", ing=["C1", "C2", "L-CARPARK"], mirror="SC01-SH03", moving=True, take="SC09-T2", music=m)
R("SC09-SH05", g, "SHOT", "C4", "eye", "three-quarter", "MEDIUM", "clean", "", ["SH-MED", "SH-34"], "eyes", "medium", cp9,
  "L056", "the same garden-centre lad jogs up, stops a step away, to Tony", "F2", ["C4"], "L-CARPARK", speaking=True, day=d, cue="on 'sir?'", pace="three jogging steps, then still", ing=["C4", "L-CARPARK", "VOICE-C4"], take="SC09-T2", music=m)
R("SC09-SH06", g, "SHOT", "C1", "eye", "ots", "MCU", "through", "over the lad onto Tony, arm round Sue: the line given back", ["SH-OTS"], "eyes", "shallow", cp9,
  "L057", "Tony, his arm round Sue, easy", "F2", ["C1", "C2", "C4"], "L-CARPARK", speaking=True, day=d, cue="on 'love.'", pace="still", ing=["C1", "C2", "C4", "L-CARPARK", "VOICE-C1"], mirror="SC01-SH07", take="SC09-T2",
  end="Tony with his arm round Sue beside the open boot, the lad a step away", music=m)
R("SC09-SH07", g, "SHOT", "C1", "low", "three-quarter", "FULL", "clean", "low: the 25-kilo bag goes in without a thought", ["SH-LOW", "SH-34"], "deep", "deep", cp9,
  "", "Tony picks a 25-kilo bag of compost off the trolley with both hands and swings it into the boot in one move", "F2", ["C1"], "L-CARPARK", day=d, cue="as the bag lands", pace="one swing", ing=["C1", "L-CARPARK"], take="SC09-T3",
  start="Tony at the open boot beside a trolley with a plain bag of compost", end="the bag in the boot", split="length", music=m, extra=1.0)
R("SC09-SH08", g, "SHOT", "C2", "eye", "front", "MCU", "clean", "", ["SH-EYE"], "eyes", "shallow", cr9,
  "", "in the car, Sue leans across and kisses Tony on the cheek; he smiles at the windscreen", "F2", ["C2", "C1"], "L-CAR", day=d, cue="hold", pace="one lean", ing=["C2", "C1", "L-CAR"], take="SC09-T4",
  start="Tony at the wheel, Sue in the passenger seat", end="Sue's head on his shoulder", music=m, extra=2.0)

# ======================= SC10 — THE OFFER (narrator over the strap, the stairs, the patio and the pack) =======================
g, m = "SC10", "MUS-OFFER"
R("SC10-SH01", g, "INSERT", "C1", "low", "front", "CU", "clean", "front-on at knee height in the garden: the strap on the spot", ["SH-CU"], "product", "shallow", gd,
  "L058", "Tony's bare right knee as he kneels up on the patio, the black strap on it, the notch at the bottom of the kneecap; the low sun on the shell", "F1", ["C1"], "L-GARDEN", face=False, product=True, day="D7", cue="on 'not your age.'", pace="still; slow push-in", ing=["C1", "L-GARDEN", "front.webp", "INFO-PLACEMENT"], take="SC10-T1", music=m)
R("SC10-SH02", g, "SHOT", "C1", "eye", "behind", "FULL", "clean", "from behind as he walks up his street in jeans: nobody knows it's there", ["SH-REAR"], "deep", "deep", sv,
  "L060", "Tony in jeans walks briskly up the pavement of his street away from us, an ordinary man", "F2", ["C1"], "L-STREET", face=False, day="D9", cue="on 'there.'", pace="brisk, one step per second", ing=["C1", "L-STREET"], take="SC10-T2", moving=True, music=m,
  start="Tony walking away up the pavement", end="further up the street")
pk = L("the warm pendant over the kitchen table", "R", "evening", "Offer — warm", 3200)
R("SC10-SH03", g, "INSERT", "PACK", "high", "front", "CU", "clean", "high on the open box: two straps, one for each knee", ["SH-HIGH", "SH-CU"], "product", "medium", pk,
  "L061", "the open matte-black box on the oak kitchen table, two straps lying flat side by side inside it, shells up", "F1", [], "L-KITCHEN", face=False, product=True, day=None, cue="on 'grab it now.'", pace="still; slow push-in", ing=["L-KITCHEN", "package_open.jpg", "front.webp"], take="SC10-T3", music=m)

# ---- angles.py fixes (pass 1): focus depth spread, a second height in the car, keys off the lens axis ----
def _set(beat, **kw):
    r = next(x for x in ROWS if x["beat"] == beat)
    for k, v in kw.items():
        if k in ("plane", "dof"): r["focus"][k] = v
        else: r[k] = v
for b in ["SC02-SH02", "SC02-SH03", "SC02-SH07", "SC02-SH08", "SC05-SH02", "SC05-SH06", "SC05-SH08", "SC05-SH10", "SC05-SH14",
          "SC05-SH17", "SC05-SH20", "SC05-SH24", "SC06-SH02"]:
    _set(b, dof="medium")
_set("SC02-SH05", height="low", why="slightly low from the dashboard on Tony: the man digging in", shot=["SH-CU", "SH-LOW"])
_set("SC07-SH02", plane="product")
for b in ["SC03-SH03", "SC07-SH02"]:
    r = next(x for x in ROWS if x["beat"] == b); r["light"] = dict(r["light"], key_side="L")

# ---- pass 1b: long lines become coverage — the speaker, the listener (speaker off), the speaker again (inspo mean shot 3.4 s) ----
def _piece(src, suffix, share, **kw):
    r = json.loads(json.dumps(src)); r["beat"] = src["beat"] + suffix; r["duration"] = round(src["duration"] * share, 1)
    foc = kw.pop("focus", None)
    r.update(kw)
    if foc: r["focus"].update(foc)
    if r["subject"] != src["subject"] or kw.get("type") == "INSERT":
        r["speaking"] = False; r["voice"] = "off"
    return r
SPLITS = {
 "SC01-SH06": [dict(suffix="a", share=0.55),
               dict(suffix="b", share=0.45, subject="C1", height="high", side="three-quarter", scale="WIDE", fg="through", shot=["SH-WIDE", "SH-HIGH"],
                    why="high past the lad's shoulder: Tony still down on one knee ten feet away — what the lad is looking at",
                    action="past the lad's shoulder, Tony is still down on his right knee on the tarmac beside the cracked pot, getting a hand to the ground to push up",
                    cast=["C1", "C4"], focus={"plane": "deep", "dof": "deep"}, ing=None)],
 "SC05-SH09": [dict(suffix="a", share=0.5, speaking=False, voice="", lines="", action="Gary sits on the edge of the pallet of slabs and nods Tony down beside him; Tony sits"),
               dict(suffix="b", share=0.5, height="eye", side="front", scale="CU", shot=["SH-CU"], why="", action="Gary, seated, turns to Tony and asks",
                    focus={"plane": "eyes", "dof": "shallow"})],
 "SC05-SH13": [dict(suffix="a", share=0.36),
               dict(suffix="b", share=0.28, subject="C1", height="eye", side="ots", scale="MCU", fg="through", shot=["SH-OTS"], why="over Gary onto Tony, listening — it is his story being told",
                    action="Tony listening, looking at his knee, then at Gary; mouth closed", cast=["C1", "C3"]),
               dict(suffix="c", share=0.36, height="low", side="three-quarter", scale="MCU", shot=["SH-LOW", "SH-34"], why="slightly low on Gary: the man who got out", rig="F2", pace="still")],
 "SC05-SH15": [dict(suffix="a", share=0.38),
               dict(suffix="b", share=0.24, type="INSERT", subject="C1", height="high", side="front", scale="CU", shot=["SH-HIGH", "SH-CU"], face=False,
                    why="high on the knee again: the spot the size of a coin, under his finger", action="Tony's forefinger rests on the soft spot just below his bare right kneecap",
                    cast=["C1"], focus={"plane": "hands", "dof": "shallow"}),
               dict(suffix="c", share=0.38, height="eye", side="three-quarter", scale="CU", shot=["SH-CU", "SH-34"], why="", pace="still")],
 "SC05-SH18": [dict(suffix="a", share=0.5),
               dict(suffix="b", share=0.2, subject="C1", height="eye", side="three-quarter", scale="CU", fg="clean", shot=["SH-CU", "SH-34"], why="",
                    action="Tony, a slow nod — every one of them is in his drawer; mouth closed", cast=["C1"]),
               dict(suffix="c", share=0.3, height="eye", side="front", scale="MCU", fg="clean", shot=["SH-EYE"], why="", cast=["C3"])],
 "SC05-SH26": [dict(suffix="a", share=0.37),
               dict(suffix="b", share=0.22, subject="C1", height="eye", side="front", scale="CU", fg="clean", shot=["SH-CU"], why="",
                    action="Tony, despite himself, half a smile; mouth closed", cast=["C1"]),
               dict(suffix="c", share=0.41, height="low", side="three-quarter", scale="MCU", fg="clean", shot=["SH-LOW", "SH-34"], why="slightly low on Gary: the dare",
                    action="Gary, plain now, nodding at Tony's knee")],
}
_new = []
for r in ROWS:
    if r["beat"] in SPLITS:
        for spec in SPLITS[r["beat"]]:
            spec = dict(spec); sfx = spec.pop("suffix"); sh = spec.pop("share")
            if "ing" in spec:
                spec.pop("ing"); spec["ingredients"] = [x for x in r["ingredients"]]
            _new.append(_piece(r, sfx, sh, **spec))
    else:
        _new.append(r)
ROWS[:] = _new
for r in ROWS:   # listener pieces need the listener in the ingredients
    for c in r["cast"]:
        if c not in r["ingredients"]: r["ingredients"].insert(0, c)

# ---- pass 2: durations for lines split over several shots; takes grouped by rule (§24K part 5, L51) ----
for b, t in {"SC03-SH01": 3.5, "SC03-SH02": 4.0, "SC03-SH03": 4.0, "SC05-SH21": 3.0, "SC05-SH22": 5.0, "SC05-SH23": 3.0,
             "SC07-SH01": 3.5, "SC07-SH02": 3.0}.items():
    _set(b, duration=t)
DEFAULT_POS = {}
for r in ROWS:   # a scene's default staging = the first start position written in it
    if r.get("start_pos") and (r["scene"], r["location"], r["story_day"]) not in DEFAULT_POS:
        DEFAULT_POS[(r["scene"], r["location"], r["story_day"])] = r["start_pos"]
def _key(r): return (r["scene"], r["location"], r["story_day"])
own_start = {r["beat"]: r.pop("start_pos", None) for r in ROWS}
own_end = {r["beat"]: r.pop("end_pos", None) for r in ROWS}
for r in ROWS:
    for k in ("take", "take_kind", "split"): r.pop(k, None)
takes, cur = [], []
for r in ROWS:
    if cur and _key(cur[-1]) == _key(r) and len(cur) < 4 and sum(x["duration"] for x in cur) + r["duration"] <= 15.0 \
            and not r["product_beat"] == "pinned":
        cur.append(r)
    else:
        if cur: takes.append(cur)
        cur = [r]
takes.append(cur)
n = {}
for i, t in enumerate(takes):
    sc = t[0]["scene"]; n[sc] = n.get(sc, 0) + 1; tid = f"{sc}-T{n[sc]}"
    for r in t: r["take"] = tid
    if len(t) > 1:
        t[0]["take_kind"] = "one-take" if all(x["rig"] in ("F5", "F9") for x in t) and len(t) <= 3 else "multi"
    prev = takes[i - 1] if i else None
    if prev and _key(prev[-1]) == _key(t[0]):
        t[0]["split"] = "length"
    idx0 = ROWS.index(t[0]); idxN = ROWS.index(t[-1])
    t[0]["start_pos"] = own_start[t[0]["beat"]] or (own_end[ROWS[idx0 - 1]["beat"]] if idx0 and _key(ROWS[idx0 - 1]) == _key(t[0]) and own_end[ROWS[idx0 - 1]["beat"]] else None) \
        or DEFAULT_POS.get(_key(t[0])) or t[0]["action"]
    nxt = ROWS[idxN + 1] if idxN + 1 < len(ROWS) else None
    t[-1]["end_pos"] = own_end[t[-1]["beat"]] or (own_start[nxt["beat"]] if nxt and _key(nxt) == _key(t[-1]) and own_start[nxt["beat"]] else None) \
        or DEFAULT_POS.get(_key(t[-1])) or t[-1]["action"]

if __name__ == "__main__":
    json.dump(ROWS, open(HERE / "act_map.json", "w"), indent=1, ensure_ascii=False)
    print(len(ROWS), "rows;", len({r["take"] for r in ROWS}), "takes;", round(sum(r["duration"] for r in ROWS)), "s")
