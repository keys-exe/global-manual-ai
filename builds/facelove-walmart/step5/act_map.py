#!/usr/bin/env python3
"""Step-5 act map (E4) for facelove-walmart — Mode 5 Pixar Film, Seedance 2.5 takes (§24K part 5: one scene one take up to 30 s,
a new shot every 2–5 s inside it), §24P drama coverage + set marks, §24N F1–F24 moves.
Checked by takes.py, blocking.py (--sets sets.json), angles.py, wardrobe.py, visual_plan.py."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
LIGHT = {
 "STORE": dict(source="the long rows of overhead store light panels", time="midday", arc="the present — bright, clean, unbothered", kelvin=4500),
 "LIVING": dict(source="the pleated table lamp beside the armchair, dusk through the window", time="evening", arc="the wound — amber dying to blue", kelvin=2700),
 "MIRROR": dict(source="the vanity bulbs over the oval mirror", time="night", arc="the undoing — flat, unflattering", kelvin=3500),
 "VANITY_AM": dict(source="cool morning daylight through the sheer curtains", time="morning", arc="nothing worked — cool, flat", kelvin=6000),
 "HALL": dict(source="the globe pendant light in the hall", time="night", arc="the turn — warm light in the dark house", kelvin=2900),
 "VANITY_GOLD": dict(source="golden morning sun through the sheer curtains", time="morning", arc="the change — warm, new", kelvin=4300),
 "PATIO_AM": dict(source="the low morning sun over the garden wall", time="morning", arc="the after — open, golden", kelvin=4300),
 "DOORS": dict(source="the low golden sun through the open sliding doors", time="afternoon", arc="the after — walking into the light", kelvin=3800),
 "PATIO_GOLD": dict(source="the low late sun over the garden wall", time="afternoon", arc="the after — at peace", kelvin=3800),
}
rows = []
def F(plane, dof, rack=None, moving=False): return {"plane": plane, "dof": dof, "rack": rack, "moving_subject": moving}
def R(beat, scene, take, lt, key, **k):
    L = dict(LIGHT[lt], key_side=key)
    if "lwhy" in k: L["why"] = k.pop("lwhy")
    r = {"beat": beat, "group": scene, "scene": scene, "take": take, "type": k.pop("type", "SHOT"), "mode": 5, "light": L,
         "fg": "clean", "speaking": False, "face": True, "product_beat": False, "mirror_of": None}
    r.update(k); rows.append(r)

# ============ SC01 — COLD-OPEN HOOK · the aisle, the carts hit (L-AISLE · P1) — one take, 30 s ============
AX1 = "the line between Michelle (frame left) and Peter with the woman (frame right) across the two carts"
R("SC01-SH01", "SC01", "SC01-T1", "STORE", "L", take_kind="multi", subject="N", cast=["N", "C1", "C2"], location="L-AISLE", story_day="P1",
  height="eye", side="three-quarter", scale="WIDE", shot=["SH-WIDE", "SH-34"], focus=F("deep", "deep"), coverage="establish", rig="F13",
  why="the aisle and both carts in one frame: we see the corner before she does", axis=AX1, axis_side="A", dir="away",
  vo="At sixty three, I ran into my ex-husband in Walmart.", hold_s=0, duration=3,
  action="Michelle pushes her cart briskly up the aisle toward the walkway, the camera backing away in front of her; Peter's cart swings round the end-cap into her path",
  motion="her cart rolls forward three strides, his cart noses round the end-cap", pace="three brisk strides, one swing",
  marks={"N": "mid-aisle, beside the paper shelves, pushing Michelle's cart (a full-size store shopping cart, waist-high, holding a few household things)", "C1": "at the end-cap, rounding it from the walkway", "C2": "at the end-cap, half a step behind Peter"},
  start_pos="Michelle mid-aisle by the paper shelves pushing her cart toward the walkway, facing camera; Peter and the woman unseen beyond the end-cap on the walkway, about to turn in",
  music="MUS-OPEN", lines="L001")
R("SC01-SH02", "SC01", "SC01-T1", "STORE", "L", type="INSERT", subject="carts", cast=["N", "C1"], location="L-AISLE", story_day="P1", face=False,
  height="low", side="profile", scale="MEDIUM", shot=["SH-MED", "SH-LOW"], focus=F("foreground", "medium"), coverage="insert", rig="F19",
  why="low on the two carts as they hit: the impact is the hook — fast, physical (brief VN02)", axis_side="neutral",
  vo="He was with her.", duration=2,
  action="the two carts collide nose to nose with a jolt, both carts rocking back; both pairs of hands lurch on the handles",
  motion="the two carts slam together and rock back a hand's width; both pairs of hands jerk on the handles", pace="one hit",
  marks={"N": "mid-aisle at the end-cap corner, hands on Michelle's cart", "C1": "at the end-cap, hands on his cart"}, music="MUS-OPEN", lines="L001")
R("SC01-SH03", "SC01", "SC01-T1", "STORE", "R", subject="C1", cast=["C1", "C2"], location="L-AISLE", story_day="P1",
  height="eye", side="three-quarter", scale="MCU", shot=["SH-34"], focus=F("eyes", "shallow", rack={"from": "Peter", "to": "the woman", "cue": "the woman, 41", "kind": "pull"}),
  coverage="single", rig="F12", why="Peter looks up annoyed — then his face changes: the stare is the story", axis_side="A",
  vo="The woman he left me for. She is forty one.", duration=4,
  action="Peter looks up annoyed, then his face changes completely — eyes widening, scanning her head to toe; behind him the woman stiffens",
  motion="his brows drop then lift, his eyes travel down and up; the woman's shoulders rise", pace="one look down, one look up",
  marks={"C1": "at the end-cap, behind his cart", "C2": "at the end-cap, at Peter's shoulder"}, music="MUS-OPEN", lines="L001")
R("SC01-SH04", "SC01", "SC01-T1", "STORE", "R", subject="C1", cast=["C1"], location="L-AISLE", story_day="P1",
  height="low", side="three-quarter", scale="CU", shot=["SH-LOCU"], focus=F("eyes", "shallow"), coverage="close", rig="F1", speaking=True,
  why="low close on Peter: the man who left her, now the one looking up", axis_side="A",
  dialogue="Michelle? Is that you? My God, what happened, did you get work done? You look so much more beautiful.", duration=6,
  action="Peter, staring, says it in one breath, his hand loose on the cart handle",
  motion="the slow push-in closes on his face as his mouth falls open between questions", pace="the line in one breath",
  marks={"C1": "at the end-cap, behind his cart"}, music="MUS-OPEN", lines="L002")
R("SC01-SH05", "SC01", "SC01-T1", "STORE", "L", subject="N", cast=["N"], location="L-AISLE", story_day="P1",
  height="eye", side="three-quarter", scale="CU", shot=["SH-CU", "SH-34"], focus=F("eyes", "shallow"), coverage="close", rig="F2", speaking=True,
  turn=True, beat_before=1.0, why="the turn: she is calm — a beat, then three words", axis_side="A",
  dialogue="It is just me.", duration=3,
  action="Michelle holds his look for a beat, calm, cool, unbothered, and says it with one corner of her mouth lifting",
  motion="a beat of stillness, then her lips move and the smile settles; her eyes stay on him", pace="a beat, then four words",
  marks={"N": "mid-aisle at the end-cap corner, hands on Michelle's cart"}, music="MUS-OPEN", lines="L003")
R("SC01-SH06", "SC01", "SC01-T1", "STORE", "L", subject="N", cast=["N", "C1", "C2"], location="L-AISLE", story_day="P1",
  height="eye", side="three-quarter-back", scale="FULL", shot=["SH-REAR"], focus=F("deep", "medium", moving=True), coverage="master", rig="F14",
  why="following her as she steers round him and glides off down the walkway: she leaves, he stays", axis_side="A", dir="L>R",
  vo="The only reason I did not fall apart standing there", duration=4,
  action="Michelle steers her cart around his and walks off along the walkway, unhurried, the camera following behind her",
  motion="her cart swings round his and she walks five easy strides away", pace="five unhurried strides",
  marks={"N": "at the end-cap, steering out onto the walkway", "C1": "at the end-cap, behind his cart", "C2": "at the end-cap, at Peter's shoulder"}, music="MUS-OPEN", lines="L004")
R("SC01-SH07", "SC01", "SC01-T1", "STORE", "R", type="SHOT", subject="C1", cast=["C1", "C2"], location="L-AISLE", story_day="P1",
  height="high", side="front", scale="MEDIUM", shot=["SH-HIGH", "SH-MED"], focus=F("eyes", "medium"), coverage="reaction", rig="F6",
  why="high, pulling back: Peter frozen and smaller, the woman watching him watch her", axis_side="A",
  vo="is because of what my sister handed me a few weeks ago.", duration=5,
  action="Peter stands frozen staring after her; the woman beside him turns from Michelle to Peter, stiffening",
  motion="the camera pulls back and rises a little; the woman's head turns slowly from her to him", pace="one slow turn of the head",
  marks={"C1": "at the end-cap, behind his cart", "C2": "at the end-cap, at Peter's shoulder"},
  end_marks={"C1": "at the end-cap, behind his cart", "C2": "at the end-cap, at Peter's shoulder", "N": "walking away along the walkway, out of frame"},
  end_pos="Peter frozen at the end-cap behind his cart, staring frame right; the woman at his shoulder looking at him; Michelle gone along the walkway",
  music="MUS-OPEN", lines="L004", transition="the image cools and dissolves back four years (VN05)")

# ============ SC02 — THE DIVORCE (L-LIVING · F1, four years earlier) — one take, 24 s ============
AX2 = "the line between Michelle in the armchair (frame left) and Peter by the coffee table (frame right)"
R("SC02-SH01", "SC02", "SC02-T1", "LIVING", "L", take_kind="multi", subject="N", cast=["N", "C1"], location="L-LIVING", story_day="F1",
  height="eye", side="three-quarter", scale="WIDE", shot=["SH-WIDE", "SH-34"], focus=F("deep", "deep"), coverage="establish", rig="F18",
  why="the room of thirty years: lamp-lit, her in the armchair, him standing", axis=AX2, axis_side="A",
  duration=4, hold_s=4,
  action="Peter, in his coat, stands by the coffee table and sets a plain manila envelope (a little larger than a sheet of paper) on it; Michelle sits in the armchair, very still",
  motion="his hand lowers the envelope to the table and withdraws; the slow creep moves in a few centimetres", pace="one slow placing",
  marks={"N": "in the armchair, by the lamp", "C1": "beside the coffee table, the archway behind him"},
  start_pos="Michelle sitting very still in the dusty-rose armchair by the lamp, facing the coffee table; Peter standing beside the coffee table in his coat, the envelope in his hand, the archway behind him",
  music="MUS-OPEN", lines="—")
R("SC02-SH02", "SC02", "SC02-T1", "LIVING", "L", type="INSERT", subject="envelope", cast=["C1"], location="L-LIVING", story_day="F1", face=False,
  height="high", side="front", scale="CU", shot=["SH-HICU"], focus=F("hands", "shallow"), coverage="insert", rig="F12",
  why="high on the envelope on the walnut: the end of thirty-one years, in paper", axis_side="neutral", duration=2, hold_s=2,
  action="the plain manila envelope (a little larger than a sheet of paper) lies on the coffee table; Peter's fingers slide off it",
  motion="his fingers slide off the envelope; the camera tilts down onto it", pace="one slide", marks={"C1": "beside the coffee table"}, music="MUS-OPEN", lines="—")
R("SC02-SH03", "SC02", "SC02-T1", "LIVING", "R", subject="C1", cast=["C1"], location="L-LIVING", story_day="F1",
  height="eye", side="three-quarter", scale="MCU", shot=["SH-34"], focus=F("eyes", "shallow"), coverage="single", rig="F11", speaking=True,
  why="Peter will not meet her eyes: his gaze on the floor, the pan follows his turn away", axis_side="A",
  dialogue="I am sorry, Michelle. After thirty one years. I just... I need something different.", duration=6,
  action="Peter says it to the floor, never meeting her eyes, then half turns toward the archway",
  motion="his eyes stay down; he half turns away and the camera pans with him", pace="the line, then one half turn",
  marks={"C1": "beside the coffee table"}, music="MUS-OPEN", lines="L005")
R("SC02-SH04", "SC02", "SC02-T1", "LIVING", "L", subject="N", cast=["N"], location="L-LIVING", story_day="F1",
  height="eye", side="three-quarter", scale="CU", shot=["SH-CU", "SH-EYE"], focus=F("eyes", "shallow"), coverage="close", rig="F1", speaking=True,
  turn=True, beat_before=1.5, why="the turn: the floor falls out from under her — a whisper", axis_side="A",
  dialogue="Thirty one years.", duration=4,
  action="Michelle, very still in the armchair, eyes on the envelope, whispers it barely aloud",
  motion="a long held breath, then her lips barely move; the camera pushes in slowly", pace="a held beat, then three words",
  marks={"N": "in the armchair, by the lamp"}, music="MUS-OPEN", lines="L006")
R("SC02-SH05", "SC02", "SC02-T1", "LIVING", "R", subject="C1", cast=["N", "C1"], location="L-LIVING", story_day="F1",
  height="eye", side="ots", scale="FULL", shot=["SH-OTS"], fg="through", focus=F("background", "medium"), coverage="ots", rig="F2",
  why="over her shoulder: he walks out through the archway and the house swallows him", axis_side="A", dir="away",
  duration=4, hold_s=4,
  action="over Michelle's shoulder, Peter walks away through the archway and out of sight; the front door closes beyond",
  motion="Peter walks four steps through the archway and is gone; the door's light flickers shut", pace="four steps",
  marks={"N": "in the armchair, by the lamp", "C1": "walking from the coffee table out through the archway"}, music="MUS-OPEN", lines="—")
R("SC02-SH06", "SC02", "SC02-T1", "LIVING", "L", type="SHOT", subject="N", cast=["N"], location="L-LIVING", story_day="F1",
  height="high", side="three-quarter", scale="WIDE", shot=["SH-WIDE", "SH-HIGH"], focus=F("deep", "deep"), coverage="reaction", rig="F16",
  why="high and wide: the house suddenly enormous and silent, the lamp's pool shrinking around her", axis_side="A",
  duration=4, hold_s=4, lwhy="the light dies — the lamp's pool holds while the window goes dark",
  action="Michelle alone in the armchair as the light dies, the envelope on the table in front of her",
  motion="her shoulders drop with one long breath out as the window behind goes from blue to dark", pace="one slow descent",
  marks={"N": "in the armchair, by the lamp"}, end_marks={"N": "in the armchair, by the lamp"},
  end_pos="Michelle alone, small in the armchair by the lamp, the envelope on the coffee table, the room dark around her", music="MUS-OPEN", lines="—")

# ============ SC03 — THE UNDOING (L-VANITY · F2) — one take, 22 s ============
R("SC03-SH01", "SC03", "SC03-T1", "MIRROR", "R", take_kind="multi", subject="N", cast=["N"], location="L-VANITY", story_day="F2",
  height="eye", side="behind", scale="MEDIUM", shot=["SH-REAR", "SH-MED"], fg="reflection", focus=F("background", "medium"), coverage="establish", rig="F18",
  why="behind her at the vanity, her face only in the mirror: she is talking to a stranger", duration=4, hold_s=4,
  action="Michelle sits on the stool at the vanity in her robe, looking at her reflection in the oval mirror",
  motion="she leans an inch toward the mirror; the camera creeps in behind her", pace="one lean",
  marks={"N": "on the stool, at the vanity"}, start_pos="Michelle seated on the stool at the vanity, back to camera, her face in the oval mirror, the bulbs on above it",
  music="MUS-OPEN", lines="L007")
R("SC03-SH02", "SC03", "SC03-T1", "MIRROR", "R", subject="N", cast=["N"], location="L-VANITY", story_day="F2",
  height="eye", side="three-quarter", scale="CU", shot=["SH-CU", "SH-34"], focus=F("eyes", "shallow"), coverage="close", rig="F1", speaking=True,
  turn=True, beat_before=1.0, why="close on her own face as she asks it: the question she has avoided",
  dialogue="When did I start looking like this? Tired. Worn out. Older than I am. No wonder he stopped looking at me.", duration=8,
  action="Michelle, hollow, says it to her reflection, touching the shadow under one eye with a fingertip",
  motion="her fingertip touches under her eye and drops; the camera pushes in", pace="the line, one touch",
  marks={"N": "on the stool, at the vanity"}, music="MUS-OPEN", lines="L007")
R("SC03-SH03", "SC03", "SC03-T1", "MIRROR", "R", type="INSERT", subject="photo", cast=["N"], location="L-VANITY", story_day="F2", face=False,
  height="high", side="three-quarter", scale="CU", shot=["SH-HICU"], focus=F("hands", "shallow"), coverage="insert", rig="F12",
  why="her hand turns a photograph of herself face down: she stops being in photos",
  vo="I stopped looking in mirrors. I stopped being in photos.", duration=4,
  action="her hand lays a small framed photograph (the size of a paperback) face down on the vanity",
  motion="her hand turns the frame over and lays it flat; the camera tilts with it", pace="one tip", marks={"N": "on the stool, at the vanity"}, music="MUS-OPEN", lines="L008")
R("SC03-SH04", "SC03", "SC03-T1", "MIRROR", "L", subject="N", cast=["N"], location="L-VANITY", story_day="F2",
  height="low", side="profile", scale="MCU", shot=["SH-PROFILE", "SH-LOW"], focus=F("eyes", "shallow"), coverage="single", rig="F15",
  why="the slow orbit as she works heavy foundation into her face — burying it",
  vo="And I buried my face under more and more makeup that only made it worse.", duration=5,
  action="in profile, Michelle pats thick beige foundation from an unlabelled bottle over her cheeks with her fingers, layer on layer",
  motion="her fingers press the foundation on three times; the camera orbits slowly round to her front", pace="three pats",
  marks={"N": "on the stool, at the vanity"}, music="MUS-OPEN", lines="L008")
R("SC03-SH05", "SC03", "SC03-T1", "MIRROR", "R", subject="N", cast=["N"], location="L-VANITY", story_day="F2",
  height="eye", side="ots", scale="MEDIUM", shot=["SH-OTS"], fg="through", focus=F("background", "medium"), coverage="cutaway", rig="F23",
  why="over her shoulder into the mirror: the caked mask looking back", duration=3, hold_s=3,
  action="over her shoulder, the mirror shows her face caked and grey; she looks away from it",
  motion="her eyes drop away from the mirror; the camera breathes", pace="one look away",
  marks={"N": "on the stool, at the vanity"}, end_marks={"N": "on the stool, at the vanity"},
  end_pos="Michelle on the stool at the vanity, face heavy with foundation, looking down away from the mirror", music="MUS-OPEN", lines="L008")

# ============ SC04 — NOTHING WORKED (L-VANITY · F3) — one take, 18 s ============
R("SC04-SH01", "SC04", "SC04-T1", "VANITY_AM", "R", take_kind="multi", type="INSERT", subject="bottles", cast=["N"], location="L-VANITY", story_day="F3", face=False,
  height="overhead", side="front", scale="MEDIUM", shot=["SH-OVER"], focus=F("hands", "medium"), coverage="establish", rig="F21",
  why="from above: the vanity crowded with a dozen unlabelled creams, serums and foundations — the failed fixes in one look",
  dialogue="Every cream. Every serum. Every foundation on the shelf.", speaking=False, duration=4, hold_s=0,
  action="her hand moves across the crowded vanity top, touching one bottle after another",
  motion="her hand moves across the bottles, touching three; the camera tracks overhead with it", pace="three touches",
  marks={"N": "on the stool, at the vanity"}, start_pos="Michelle on the stool at the vanity in the morning, her hand over a crowd of a dozen unlabelled bottles and jars",
  music="MUS-OPEN", lines="L009")
R("SC04-SH02", "SC04", "SC04-T1", "VANITY_AM", "R", subject="N", cast=["N"], location="L-VANITY", story_day="F3",
  height="eye", side="three-quarter", scale="MCU", shot=["SH-34"], focus=F("eyes", "shallow"), coverage="single", rig="F1", speaking=True,
  turn=True, beat_before=1.0, why="defeated, to the mirror: the brands she trusted",
  dialogue="The Estée Lauder, the L'Oréal. And I look older in all of them.", duration=5,
  action="Michelle, defeated, says it to the mirror, a jar in her hand",
  motion="she lowers the jar to the vanity as she speaks; the camera pushes in", pace="the line, one lowering",
  marks={"N": "on the stool, at the vanity"}, music="MUS-OPEN", lines="L009", note="the Every cream… line opens over SH01 off-screen, the brands on screen here (F8: no brand on any bottle)")
R("SC04-SH03", "SC04", "SC04-T1", "VANITY_AM", "L", subject="N", cast=["N"], location="L-VANITY", story_day="F3",
  height="high", side="three-quarter-back", scale="FULL", shot=["SH-HIGH", "SH-REAR"], focus=F("deep", "deep"), coverage="cutaway", rig="F6",
  why="high and pulling away: she sweeps the bottles into a drawer and makes her peace with disappearing",
  vo="I decided this was just what sixty looked like, and I made my peace with disappearing.", duration=6,
  action="Michelle sweeps the bottles into the vanity drawer, shuts it, and sits back on the stool, small in the cool room",
  motion="one sweep of the arm, the drawer slides shut; the camera pulls back and up", pace="one sweep, one push of the drawer",
  marks={"N": "on the stool, at the vanity"}, end_marks={"N": "on the stool, at the vanity"},
  end_pos="Michelle sitting back on the stool, the vanity bare, the drawer shut, the room cool and quiet", music="MUS-OPEN", lines="L010")

# ============ SC05 — THE SISTER (L-HALL · F4, night) — two takes (conversation over 30 s, split at a line end, nobody moving) ============
AX5 = "the line between Rosa (frame left, by the front door) and Michelle (frame right, by the archway)"
R("SC05-SH01", "SC05", "SC05-T1", "HALL", "L", take_kind="multi", subject="C3", cast=["N", "C3"], location="L-HALL", story_day="F4",
  height="eye", side="three-quarter-back", scale="WIDE", shot=["SH-WIDE", "SH-REAR"], focus=F("deep", "deep"), coverage="establish", rig="F14",
  why="following Michelle down the dark hall toward the knocking door", axis=AX5, axis_side="A", dir="away", speaking=False,
  dialogue="Michelle, open the door. I brought wine and I am not leaving.", duration=4,
  action="Michelle shuffles down the hall to the front door as Rosa's voice calls through it; she opens the door",
  motion="Michelle walks four steps to the door and pulls it open", pace="four slow steps, one pull",
  marks={"N": "walking from the archway to the front door", "C3": "outside the front door"},
  start_pos="Michelle at the archway in an old grey sweatshirt walking toward the front door, back to camera; Rosa unseen outside the front door, calling through it",
  music="MUS-OPEN", lines="L011", note="Rosa heard through the door (off), then on screen")
R("SC05-SH02", "SC05", "SC05-T1", "HALL", "L", subject="C3", cast=["C3", "N"], location="L-HALL", story_day="F4",
  height="eye", side="ots", scale="MEDIUM", shot=["SH-OTS", "SH-MED"], fg="through", focus=F("eyes", "shallow"), coverage="ots", rig="F17", speaking=True,
  why="past Michelle's shoulder onto Rosa in the doorway: wine up, then the look", axis_side="A",
  dialogue="...Oh, honey. Look at you. Come here.", duration=4,
  action="Rosa in the doorway holds up the bottle of red wine (held by its neck), sees Michelle's face, and her grin softens",
  motion="the wine comes up, then lowers as her face softens; the camera pushes through past Michelle's shoulder", pace="one lift, one lowering",
  marks={"N": "at the front door, holding it open", "C3": "in the front door, on the mat"}, music="MUS-OPEN", lines="L011")
R("SC05-SH03", "SC05", "SC05-T1", "HALL", "L", subject="N", cast=["N", "C3"], location="L-HALL", story_day="F4",
  height="eye", side="three-quarter", scale="MCU", shot=["SH-34"], focus=F("eyes", "shallow"), coverage="single", rig="F11",
  why="Rosa's hand takes Michelle's chin and tilts her tired face up to the pendant's light", axis_side="A",
  duration=3, hold_s=3,
  action="Rosa steps in and takes Michelle's chin in her hand, tilting her tired face up to the hall light",
  motion="Rosa's hand lifts her chin; the pan follows the tilt up", pace="one tilt",
  marks={"N": "under the pendant", "C3": "under the pendant, facing Michelle"}, music="MUS-OPEN", lines="—")
R("SC05-SH04", "SC05", "SC05-T1", "HALL", "R", subject="N", cast=["N"], location="L-HALL", story_day="F4",
  height="low", side="three-quarter", scale="CU", shot=["SH-LOCU"], focus=F("eyes", "shallow"), coverage="close", rig="F18", speaking=True,
  why="close on Michelle: the brave words, then the truth", axis_side="A",
  dialogue="I am fine, Rosa. I am. I just... I do not know who that woman in the mirror is anymore.", duration=6,
  action="Michelle says it, eyes sliding away from Rosa's, toward the round mirror on the wall",
  motion="her eyes slide away toward the mirror; the camera creeps in", pace="the line, one glance",
  marks={"N": "under the pendant"}, music="MUS-OPEN", lines="L012")
R("SC05-SH05", "SC05", "SC05-T1", "HALL", "L", subject="N", cast=["N", "C3"], location="L-HALL", story_day="F4",
  height="eye", side="profile", scale="MEDIUM", shot=["SH-PROFILE", "SH-MED"], fg="reflection", focus=F("foreground", "medium"), coverage="single", rig="F7",
  why="her and her reflection in the round mirror: the stranger she means", axis_side="A", speaking=True,
  dialogue="He looked at me like a stranger the day he left, and lately so do I.", duration=5,
  action="Michelle turns to the round mirror over the console and looks at herself as she says it; Rosa behind her",
  motion="she turns her head to the mirror; the camera arcs a little round her", pace="one turn",
  marks={"N": "by the mirror, at the console", "C3": "under the pendant, behind Michelle"}, music="MUS-OPEN", lines="L012")
R("SC05-SH06", "SC05", "SC05-T1", "HALL", "L", subject="C3", cast=["C3"], location="L-HALL", story_day="F4",
  height="eye", side="three-quarter", scale="MCU", shot=["SH-34"], focus=F("eyes", "shallow"), coverage="reaction", rig="F2",
  why="Rosa listening: she has been here herself", axis_side="A", duration=3, hold_s=3,
  action="Rosa listens, her eyes wet, nodding once, and sets the wine on the console",
  motion="one slow nod, the bottle set down on the console", pace="one nod",
  marks={"C3": "under the pendant, behind Michelle"}, end_marks={"N": "by the mirror, at the console", "C3": "under the pendant, behind Michelle"},
  end_pos="Michelle at the round mirror over the console, Rosa just behind her under the pendant, the wine on the console", music="MUS-OPEN", lines="—")
R("SC05-SH07", "SC05", "SC05-T2", "HALL", "L", split="length", take_kind="multi", subject="C3", cast=["C3", "N"], location="L-HALL", story_day="F4",
  height="eye", side="ots", scale="MEDIUM", shot=["SH-OTS", "SH-MED"], fg="through", focus=F("eyes", "shallow"), coverage="ots", rig="F2", speaking=True,
  why="past Michelle onto Rosa: the secret she learned the hard way", axis_side="A",
  dialogue="Can I tell you something? Two years ago, I felt exactly like that. Same mirror, same thoughts.", duration=6,
  action="Rosa turns Michelle gently by the shoulders to face her and speaks low",
  motion="Rosa's hands turn Michelle round by the shoulders", pace="one turn",
  marks={"N": "by the mirror, at the console", "C3": "under the pendant, behind Michelle"},
  start_pos="Michelle at the round mirror over the console, Rosa just behind her under the pendant, the wine on the console", music="MUS-OPEN", lines="L013")
R("SC05-SH08", "SC05", "SC05-T2", "HALL", "R", subject="N", cast=["N"], location="L-HALL", story_day="F4",
  height="high", side="three-quarter", scale="CU", shot=["SH-HICU"], focus=F("eyes", "shallow"), coverage="reaction", rig="F18",
  why="from a little above: Michelle's face taking it in, small and listening", axis_side="A", duration=3, hold_s=3,
  action="Michelle listens, her eyes lifting to Rosa's",
  motion="her eyes rise from the floor to Rosa's face; the camera creeps in", pace="one look up",
  marks={"N": "by the mirror, at the console"}, music="MUS-OPEN", lines="—")
R("SC05-SH09", "SC05", "SC05-T2", "HALL", "L", subject="C3", cast=["C3"], location="L-HALL", story_day="F4",
  height="low", side="three-quarter", scale="CU", shot=["SH-LOCU"], focus=F("eyes", "shallow"), coverage="close", rig="F1", speaking=True,
  turn=True, beat_before=1.0, why="low on Rosa for the reframe: it was never your age", axis_side="A",
  dialogue="And I will tell you what I had to learn the hard way. It was never your age, Michelle. It was the foundation.", duration=7,
  action="Rosa says it slowly, certain, holding Michelle's eyes",
  motion="her brows lift on 'never'; the camera pushes in", pace="the line, one lift of the brows",
  marks={"C3": "under the pendant, facing Michelle"}, music="MUS-OPEN", lines="L013")
R("SC05-SH10", "SC05", "SC05-T2", "HALL", "L", subject="C3", cast=["C3", "N"], location="L-HALL", story_day="F4",
  height="eye", side="profile", scale="MEDIUM", shot=["SH-PROFILE", "SH-MED"], focus=F("eyes", "medium"), coverage="master", rig="F9",
  why="the two sisters in profile under the light: the old foundation sits on top and ages us", axis_side="A", speaking=True,
  dialogue="Made for young skin, so on ours it just sits on top and ages us.", duration=5,
  action="Rosa taps her own cheek with two fingers as she says it; Michelle touches her own",
  motion="two taps on Rosa's cheek, Michelle's hand rises to hers; the camera tracks a little sideways", pace="two taps",
  marks={"C3": "under the pendant, facing Michelle", "N": "under the pendant, facing Rosa"},
  end_marks={"C3": "under the pendant, facing Michelle", "N": "under the pendant, facing Rosa"},
  end_pos="Rosa and Michelle face to face under the pendant in profile, Rosa's bag on her shoulder", music="MUS-OPEN", lines="L013")

# ============ SC06 — THE REVEAL (L-HALL · F4, the same night) — two takes: the stick, then the colour-change oner ============
AX6 = AX5
R("SC06-SH01", "SC06", "SC06-T1", "HALL", "L", take_kind="multi", subject="C3", cast=["C3", "N"], location="L-HALL", story_day="F4",
  height="eye", side="three-quarter", scale="MEDIUM", shot=["SH-MED", "SH-34"], focus=F("product", "medium"), coverage="master", rig="F4",
  why="Rosa goes into her bag: the turn of the film is an object", axis=AX6, axis_side="A", speaking=True, product_beat=True,
  dialogue="This is the one that changed it for me.", duration=4,
  action="Rosa reaches into her big woven shoulder bag and draws out the FACELOVE stick (a little longer than her hand is wide)",
  motion="her hand goes into the bag and comes out with the stick; the slider moves a little sideways", pace="one reach",
  marks={"C3": "under the pendant, facing Michelle", "N": "under the pendant, facing Rosa"},
  start_pos="Rosa and Michelle face to face under the pendant, Rosa's bag on her shoulder", music="MUS-TURN", lines="L014", product_at=0.0)
R("SC06-SH02", "SC06", "SC06-T1", "HALL", "L", type="INSERT", subject="product", cast=["C3"], location="L-HALL", story_day="F4", face=False,
  height="eye", side="front", scale="CU", shot=["SH-CU", "SH-EYE"], focus=F("product", "shallow"), coverage="insert", rig="F20", product_beat=True,
  why="the hero insert: the violet stick in Rosa's hand, the wordmark clear (VN12)", axis_side="neutral",
  dialogue="Here, let me just show you.", duration=3,
  action="Rosa's hand holds the closed violet FACELOVE stick (a little longer than her hand is wide) upright in the warm light, wordmark to the lens",
  motion="the camera pulls out from the wordmark to the whole stick in her hand; the light slides down the barrel", pace="one pull-out",
  marks={"C3": "under the pendant, facing Michelle"}, music="MUS-TURN", lines="L014")
R("SC06-SH03", "SC06", "SC06-T1", "HALL", "R", subject="N", cast=["N", "C3"], location="L-HALL", story_day="F4",
  height="eye", side="ots", scale="MCU", shot=["SH-OTS"], fg="through", focus=F("product", "shallow"), coverage="ots", rig="F18", speaking=True, product_beat=True,
  why="past Rosa onto Michelle as the white stripe goes on her cheek", axis_side="A",
  dialogue="It comes out pure white.", duration=4,
  action="Rosa uncaps the balm end and draws one short stripe of white balm across Michelle's cheekbone",
  motion="one stroke of the balm across the cheek; Michelle's eyes flick to it", pace="one stroke",
  marks={"N": "under the pendant, facing Rosa", "C3": "under the pendant, facing Michelle"}, music="MUS-TURN", lines="L014")
R("SC06-SH04", "SC06", "SC06-T1", "HALL", "L", subject="C3", cast=["C3"], location="L-HALL", story_day="F4",
  height="eye", side="three-quarter", scale="MCU", shot=["SH-34"], focus=F("eyes", "shallow"), coverage="single", rig="F11", speaking=True,
  why="Rosa, smiling, explaining as she turns the stick to its brush end", axis_side="A",
  dialogue="Then it reads the warmth of your own skin and turns into your exact shade, and it melts right in.", duration=6,
  action="Rosa turns the stick to its brush end as she speaks, her eyes crinkling at the corners",
  motion="the stick turns in her fingers; the pan follows it up to her face", pace="one turn of the stick",
  marks={"C3": "under the pendant, facing Michelle"}, end_marks={"C3": "under the pendant, facing Michelle", "N": "under the pendant, facing Rosa"},
  end_pos="Rosa and Michelle face to face under the pendant, the white stripe on Michelle's cheek, the brush end of the stick in Rosa's hand", music="MUS-TURN", lines="L014")
R("SC06-SH05", "SC06", "SC06-T2", "HALL", "L", split="user", take_kind="one-take", oner=True, type="INSERT", subject="N", cast=["N", "C3"], location="L-HALL", story_day="F4",
  height="eye", side="profile", scale="ECU", shot=["SH-MACRO"], focus=F("product", "shallow"), coverage="insert", rig="F2", product_beat=True,
  why="THE REVEAL hero macro — one continuous unbroken shot, no cut during the colour change (brief, non-negotiable): white warming into her shade behind the brush",
  dialogue="It has jojoba, shea, vitamin E, so it feels like nothing and never cakes. It covers the lines, the tired, the circles, and it still looks like your own skin.", duration=12,
  action="the brush end works the white stripe on Michelle's cheekbone in small circles; behind the brush the white warms into her own olive shade, ahead of it still white; every line stays",
  motion="the brush moves in slow circles across the cheek and the colour front travels behind it, white to her shade in real time", pace="small slow circles, left to right",
  marks={"N": "under the pendant, facing Rosa", "C3": "under the pendant, facing Michelle"},
  start_pos="extreme close on Michelle's cheekbone in profile, a short stripe of white balm on it, the brush end of the stick just touching its left end",
  end_marks={"N": "under the pendant, facing Rosa", "C3": "under the pendant, facing Michelle"},
  end_pos="the stripe blended into her own shade, the brush lifting away, every line of her face still there", music="MUS-TURN", lines="L015", note="Rosa heard off; oner by the brief (VN13)")
R("SC06-SH06", "SC06", "SC06-T3", "HALL", "L", split="user", take_kind="multi", subject="N", cast=["N", "C3"], location="L-HALL", story_day="F4",
  height="eye", side="three-quarter", scale="MCU", shot=["SH-34"], fg="reflection", focus=F("foreground", "medium"), coverage="reaction", rig="F15",
  why="Michelle sees herself in the round mirror — the orbit lands on her reflection", axis_side="A", speaking=True,
  dialogue="Not a mask. You.", duration=4,
  action="Rosa steps aside; Michelle turns to the round mirror and sees her even, warm face, every line still there",
  motion="Michelle turns to the mirror and her lips part; the camera orbits round to her reflection", pace="one turn",
  marks={"N": "under the pendant, facing Rosa", "C3": "under the pendant, facing Michelle"},
  start_pos="Michelle turning from Rosa to the round mirror over the console, Rosa stepping back under the pendant", music="MUS-TURN", lines="L015")
R("SC06-SH07", "SC06", "SC06-T3", "HALL", "R", subject="N", cast=["N"], location="L-HALL", story_day="F4",
  height="low", side="front", scale="CU", shot=["SH-LOCU"], fg="reflection", focus=F("eyes", "shallow"), coverage="close", rig="F1",
  turn=True, beat_before=1.0, why="her reflection, close: for the first time she does not look away", axis_side="A", duration=3, hold_s=3,
  action="in the mirror Michelle's eyes fill and the corners of her mouth lift a little at herself",
  motion="her eyes fill, the corner of her mouth lifts; a slow push", pace="one breath",
  marks={"N": "by the mirror, at the console"}, end_marks={"N": "by the mirror, at the console", "C3": "under the pendant, behind Michelle"},
  end_pos="Michelle at the round mirror, almost smiling at herself; Rosa behind her under the pendant", music="MUS-TURN", lines="—")

# ============ SC07 — THE CHANGE (L-VANITY · A1, the first morning) — one take, 13 s ============
R("SC07-SH01", "SC07", "SC07-T1", "VANITY_GOLD", "R", take_kind="multi", subject="N", cast=["N"], location="L-VANITY", story_day="A1",
  height="eye", side="three-quarter-back", scale="FULL", shot=["SH-REAR"], focus=F("deep", "deep"), coverage="establish", rig="F14",
  why="following her to the vanity in the golden morning: the same mirror, a new day", dir="away",
  vo="I ordered my own before Rosa even left. And the first morning I tried it,", duration=4,
  action="Michelle walks to the vanity in her robe and sits on the stool, her own violet stick (a little longer than her hand is wide) on the vanity",
  motion="three steps to the vanity and she sits; the camera follows behind", pace="three steps, one sit",
  marks={"N": "walking from the door to the vanity"}, start_pos="Michelle at the bedroom door in a cream robe walking toward the vanity, back to camera, golden sun through the curtains",
  music="MUS-AFTER", lines="L016")
R("SC07-SH02", "SC07", "SC07-T1", "VANITY_GOLD", "R", type="INSERT", subject="product", cast=["N"], location="L-VANITY", story_day="A1", face=False,
  height="high", side="three-quarter", scale="CU", shot=["SH-HICU"], focus=F("product", "shallow"), coverage="insert", rig="F18", product_beat=True,
  why="her own hand, her own stick: the swipe she does herself", vo="the tired just lifted.", duration=3,
  action="her hand draws the stick (a little longer than her hand is wide) across her cheek, white going on",
  motion="her hand slides the balm once across her cheekbone", pace="one swipe", marks={"N": "on the stool, at the vanity"}, music="MUS-AFTER", lines="L016")
R("SC07-SH03", "SC07", "SC07-T1", "VANITY_GOLD", "R", subject="N", cast=["N"], location="L-VANITY", story_day="A1",
  height="eye", side="front", scale="MCU", shot=["SH-EYE"], fg="reflection", focus=F("eyes", "shallow"), coverage="close", rig="F1",
  turn=True, beat_before=1.0, why="the mirror's face, straight on: she does not look away",
  vo="For the first time in years, I did not look away from my own reflection.", duration=6,
  action="in the mirror Michelle meets her own eyes and holds them, her chin lifting a little",
  motion="her eyes rise to the mirror and hold; the smile comes; a slow push-in", pace="one long held look",
  marks={"N": "on the stool, at the vanity"}, end_marks={"N": "on the stool, at the vanity"},
  end_pos="Michelle on the stool at the vanity, smiling at her reflection, the stick in her hand", music="MUS-AFTER", lines="L016")

# ============ SC08 — BACK IN THE PHOTOS (L-PATIO · A2, the weeks after) — one take, 12 s ============
AX8 = "the line between Michelle (frame left) and Rosa (frame right) at the table"
R("SC08-SH01", "SC08", "SC08-T1", "PATIO_AM", "L", take_kind="multi", subject="N", cast=["N", "C3"], location="L-PATIO", story_day="A2",
  height="low", side="front", scale="FULL", shot=["SH-LOW"], focus=F("eyes", "medium"), coverage="establish", rig="F16",
  why="low as she stands up from the table: she stood taller", axis=AX8, axis_side="A",
  vo="And it was more than my face. I stood taller.", duration=4,
  action="Michelle rises from the patio table and straightens, shoulders back; Rosa beside her laughing",
  motion="she stands up and straightens, shoulders back; the jib comes down to her eye line", pace="one rise",
  marks={"N": "at the table, by the lemon tree", "C3": "at the table, by the bougainvillea"},
  start_pos="Michelle and Rosa seated at the round patio table in the morning sun, Michelle by the lemon tree, Rosa by the bougainvillea", music="MUS-AFTER", lines="L017")
R("SC08-SH02", "SC08", "SC08-T1", "PATIO_AM", "L", subject="N", cast=["N", "C3"], location="L-PATIO", story_day="A2",
  height="high", side="front", scale="MCU", shot=["SH-SELFIE"], focus=F("eyes", "medium"), coverage="reaction", rig="F23",
  why="the sisters' selfie — she is back in the photos (the one signature shot of the scene)", axis_side="A",
  vo="I got back in the photos. I stopped hiding.", duration=4,
  action="Rosa holds her phone (a little smaller than her hand) up at arm's length; the sisters press cheek to cheek and laugh for the picture",
  motion="the two lean in and laugh; the handheld breathes", pace="one lean, one laugh",
  marks={"N": "at the table, by the lemon tree", "C3": "at the table, by the bougainvillea"}, music="MUS-AFTER", lines="L017")
R("SC08-SH03", "SC08", "SC08-T1", "PATIO_AM", "L", subject="N", cast=["N"], location="L-PATIO", story_day="A2",
  height="eye", side="three-quarter", scale="CU", shot=["SH-CU", "SH-34"], focus=F("eyes", "shallow"), coverage="close", rig="F18", turn=True, beat_before=1.0,
  why="close on her, sure of herself: not afraid of anyone",
  vo="So by the time that cart hit mine in Walmart, I was not afraid of anyone.", duration=5,
  action="Michelle lowers her face from the laugh, calm and sure, looking off past the lens",
  motion="the laugh settles into a calm, level look; the camera creeps in", pace="one settling",
  marks={"N": "at the table, by the lemon tree"}, end_marks={"N": "at the table, by the lemon tree", "C3": "at the table, by the bougainvillea"},
  end_pos="Michelle standing at the patio table, calm and sure, Rosa beside her", music="MUS-AFTER", lines="L017")

# ============ SC09 — THE PAYOFF (L-AISLE · P1, back to the cold open) — one take, 20 s ============
AX9 = "the line between Michelle (frame left) and Peter with the woman (frame right) across the carts"
R("SC09-SH01", "SC09", "SC09-T1", "STORE", "R", take_kind="multi", subject="C2", cast=["C1", "C2"], location="L-AISLE", story_day="P1",
  height="eye", side="profile", scale="MEDIUM", shot=["SH-MED", "SH-PROFILE"], focus=F("eyes", "medium"), coverage="master", rig="F11", speaking=True,
  why="back to the same aisle, the same frozen man: the woman turns on him", axis=AX9, axis_side="A", time_cut=False,
  dialogue="Wait. That is your ex-wife?", duration=3,
  action="the woman, unsettled, turns to Peter and asks; Peter still staring after Michelle",
  motion="the woman's head snaps round to Peter; the pan settles on the two of them", pace="one snap of the head",
  marks={"C1": "at the end-cap, behind his cart", "C2": "at the end-cap, at Peter's shoulder"},
  start_pos="Peter frozen at the end-cap behind his cart staring frame right; the woman at his shoulder looking at him; Michelle beyond them on the walkway, walking away",
  music="MUS-AFTER", lines="L018")
R("SC09-SH02", "SC09", "SC09-T1", "STORE", "R", subject="C2", cast=["C2", "N"], location="L-AISLE", story_day="P1",
  height="eye", side="three-quarter", scale="FULL", shot=["SH-34"], focus=F("eyes", "medium", moving=True), coverage="single", rig="F13", speaking=True,
  why="leading her as she hurries after Michelle, all guardedness gone", axis_side="A", dir="L>R",
  dialogue="I am sorry, I just have to ask. What do you use on your skin? You look amazing.", duration=6,
  action="the woman hurries along the walkway after Michelle, catching up to her cart, the camera backing away in front of her",
  motion="the woman strides five quick steps and draws level with Michelle's cart", pace="five quick strides",
  marks={"C2": "walking from the end-cap along the walkway", "N": "on the walkway beyond the end-cap"}, music="MUS-AFTER", lines="L019")
R("SC09-SH03", "SC09", "SC09-T1", "STORE", "L", subject="N", cast=["N"], location="L-AISLE", story_day="P1",
  height="low", side="three-quarter", scale="CU", shot=["SH-LOCU"], focus=F("eyes", "shallow"), coverage="close", rig="F2",
  turn=True, beat_before=1.5, why="the turn: she says nothing — a warm, serene smile (VN17)", axis_side="A", duration=4, hold_s=4,
  action="Michelle turns her head to the woman, her lips closed, the corners of her mouth curving up warm and serene, saying nothing",
  motion="her head turns, the smile grows slowly; she does not speak", pace="one turn, one slow smile",
  marks={"N": "on the walkway beyond the end-cap"}, music="MUS-AFTER", lines="—")
R("SC09-SH04", "SC09", "SC09-T1", "STORE", "L", subject="N", cast=["N", "C2"], location="L-AISLE", story_day="P1",
  height="eye", side="three-quarter-back", scale="FULL", shot=["SH-REAR"], focus=F("deep", "medium", moving=True), coverage="master", rig="F14",
  why="following as she turns her cart and glides away, the woman left standing", axis_side="A", dir="L>R", duration=4, hold_s=4,
  action="Michelle turns her cart and walks away down the walkway, unhurried; the woman stops, left behind",
  motion="the cart turns and she walks five easy strides away; the camera follows behind", pace="five unhurried strides",
  marks={"N": "walking away along the walkway", "C2": "on the walkway beyond the end-cap"}, music="MUS-AFTER", lines="—")
R("SC09-SH05", "SC09", "SC09-T1", "STORE", "R", subject="C1", cast=["C1"], location="L-AISLE", story_day="P1",
  height="high", side="front", scale="WIDE", shot=["SH-WIDE", "SH-HIGH"], focus=F("deep", "deep"), coverage="reaction", rig="F6",
  why="high and pulling back: Peter small and forgotten at the end-cap", axis_side="A", duration=3, hold_s=3,
  action="Peter stands alone at the end-cap behind his cart, small in the bright aisle, his hand slipping off the handle",
  motion="his hand slips off the handle; the camera pulls back and up", pace="one slip of the hand",
  marks={"C1": "at the end-cap, behind his cart"}, end_marks={"C1": "at the end-cap, behind his cart"},
  end_pos="Peter alone at the end-cap behind his cart, small; Michelle gone", music="MUS-AFTER", lines="—")

# ============ SC10 — THE EPILOGUE: the doors (L-STORE-DOORS · P1) — one take, 6 s ============
R("SC10-SH01", "SC10", "SC10-T1", "DOORS", "back", take_kind="multi", subject="N", cast=["N"], location="L-STORE-DOORS", story_day="P1",
  height="eye", side="behind", scale="WIDE", shot=["SH-WIDE", "SH-REAR"], focus=F("deep", "deep", moving=True), coverage="establish", rig="F2",
  why="behind her as she pushes her cart out through the open sliding doors into the golden light", dir="away",
  lwhy="she walks into the sun — a silhouette edged in gold, by design", face=False,
  vo="I did not need to say a thing.", duration=3,
  action="Michelle walks her cart (a full-size store shopping cart, waist-high, holding a few household things) out through the open sliding doors into golden light",
  motion="she walks four strides away through the doors into the sun", pace="four easy strides",
  marks={"N": "on the mat, walking to the sliding doors"}, start_pos="Michelle on the blue mat pushing her cart toward the open sliding doors, back to camera, the golden parking lot beyond",
  music="MUS-AFTER", lines="L020")
R("SC10-SH02", "SC10", "SC10-T1", "DOORS", "back", subject="N", cast=["N"], location="L-STORE-DOORS", story_day="P1",
  height="low", side="three-quarter-back", scale="FULL", shot=["SH-LOW", "SH-REAR"], focus=F("background", "medium", moving=True), coverage="cutaway", rig="F12",
  why="low, tilting up as she passes into the sun: she does not look back", lwhy="backlit through the doors — the after in gold", face=False,
  vo="I did not look back either.", duration=3,
  action="Michelle passes through the outer doors into the sunlit parking lot without looking back",
  motion="she walks out of the doors; the camera tilts up into the sun", pace="three strides",
  marks={"N": "at the sliding doors, walking out"}, end_marks={"N": "out in the parking lot"}, end_pos="Michelle out in the golden parking lot, small, walking away", music="MUS-AFTER", lines="L020")

# ============ SC11 — THE EPILOGUE: the text (L-PATIO · P2, two weeks later) — one take, 10 s ============
R("SC11-SH01", "SC11", "SC11-T1", "PATIO_GOLD", "L", take_kind="multi", subject="N", cast=["N"], location="L-PATIO", story_day="P2",
  height="eye", side="three-quarter", scale="MEDIUM", shot=["SH-MED", "SH-34"], focus=F("eyes", "medium"), coverage="establish", rig="F7",
  why="her patio, her peace: the arc finds her at the table as the phone lights up",
  vo="Two weeks later, Peter texted me. First time in four years.", duration=4,
  action="Michelle sits at the patio table with a cup of coffee; her phone (a little smaller than her hand) lights up on the table",
  motion="the phone's screen glows; she glances down; the camera arcs a little round the table", pace="one glance",
  marks={"N": "at the table, by the lemon tree"}, start_pos="Michelle seated at the round patio table by the lemon tree in a lilac shirt, coffee cup in hand, her phone face up on the table",
  music="MUS-AFTER", lines="L020")
R("SC11-SH02", "SC11", "SC11-T1", "PATIO_GOLD", "L", type="INSERT", subject="phone", cast=["N"], location="L-PATIO", story_day="P2", face=False,
  height="overhead", side="front", scale="CU", shot=["SH-OVER"], focus=F("hands", "shallow"), coverage="insert", rig="F12",
  why="overhead on the phone: the text arrives (the words set in post, F11)", vo="I read it, I smiled,", duration=3,
  action="the phone (a little smaller than her hand) on the mosaic table lights up with a message; her hand picks it up",
  motion="the screen lights, her hand lifts the phone; the camera tilts with it", pace="one lift",
  marks={"N": "at the table, by the lemon tree"}, music="MUS-AFTER", lines="L020")
R("SC11-SH03", "SC11", "SC11-T1", "PATIO_GOLD", "L", subject="N", cast=["N"], location="L-PATIO", story_day="P2",
  height="low", side="three-quarter", scale="CU", shot=["SH-LOCU"], focus=F("eyes", "shallow"), coverage="close", rig="F18",
  turn=True, beat_before=1.0, why="close as she smiles and sets it face down: at peace", vo="and I put my phone away.", duration=4,
  action="Michelle's mouth curves up at one corner as she sets the phone (a little smaller than her hand) face down on the table, then lifts her coffee",
  motion="the smile, the phone turned face down, the cup raised; the camera creeps in", pace="one smile, one turn of the phone",
  marks={"N": "at the table, by the lemon tree"}, end_marks={"N": "at the table, by the lemon tree"},
  end_pos="Michelle at the patio table, the phone face down, coffee raised, at peace", music="MUS-AFTER", lines="L020")

# ============ SC12 — CTA (L-PATIO · P2, later that afternoon) — one take + the pinned product turn ============
R("SC12-SH01", "SC12", "SC12-T1", "PATIO_GOLD", "L", take_kind="multi", subject="N", cast=["N"], location="L-PATIO", story_day="P2",
  height="eye", side="three-quarter", scale="MCU", shot=["SH-34"], focus=F("eyes", "shallow"), coverage="establish", rig="F1", speaking=True,
  why="she turns to us — the one look into the lens in the film (the narrator, §24J)", time_cut=True,
  dialogue="So if someone ever looked at you and made you feel like you had faded, please hear me. It was never you.", duration=7,
  action="Michelle, at the patio table in the late sun, turns from the garden to the lens and speaks to it, warm and direct",
  motion="her head turns from the garden to the lens; the camera pushes in slowly", pace="one turn, the line",
  marks={"N": "at the table, by the lemon tree"}, start_pos="Michelle seated at the patio table by the lemon tree in the late sun, looking at the garden wall, her violet stick on the table",
  music="MUS-OFFER", lines="L021", to_lens=True)
R("SC12-SH02", "SC12", "SC12-T1", "PATIO_GOLD", "L", subject="N", cast=["N"], location="L-PATIO", story_day="P2",
  height="low", side="front", scale="MEDIUM", shot=["SH-MED", "SH-LOW"], focus=F("product", "medium"), coverage="single", rig="F11", speaking=True, product_beat=True,
  why="she lifts the stick into the light as she names it",
  dialogue="The thing she wanted to know, I will tell you instead. It is called FACELOVE, and I have linked it below.", duration=7,
  action="Michelle picks up the violet stick (a little longer than her hand is wide) and holds it up beside her face, wordmark to the lens",
  motion="her hand lifts the stick up beside her cheek; the pan follows it", pace="one lift",
  marks={"N": "at the table, by the lemon tree"}, music="MUS-OFFER", lines="L021", to_lens=True)
R("SC12-SH03", "SC12", "SC12-T1", "PATIO_GOLD", "L", subject="N", cast=["N"], location="L-PATIO", story_day="P2",
  height="low", side="three-quarter", scale="CU", shot=["SH-LOCU"], focus=F("eyes", "shallow"), coverage="close", rig="F18",
  why="close, warm, whole: the face the film was about, every line still there", turn=True, beat_before=1.0,
  vo="Right now you get two Foundation Sticks for almost the price of one, plus a free primer, a mystery gift, and free shipping and a full thirty day money back guarantee.", duration=8,
  action="Michelle lowers the stick and looks out at the garden, her face easy and open, the late sun on her cheek",
  motion="the stick lowers, the smile widens, a breeze moves her hair; the camera creeps in", pace="one breath",
  marks={"N": "at the table, by the lemon tree"}, end_marks={"N": "at the table, by the lemon tree"},
  end_pos="Michelle at the patio table smiling in the late sun, the stick lowered in her hand", music="MUS-OFFER", lines="L021")
R("SC12-SH04", "SC12", "SC12-T2", "PATIO_GOLD", "L", split="pinned", pinned=True, take_kind="one-take", type="INSERT", subject="product", cast=[], location="L-PATIO", story_day="P2", face=False,
  height="eye", side="front", scale="CU", shot=["SH-CU", "SH-EYE"], focus=F("product", "shallow"), coverage="insert", rig="F2", product_beat=True,
  why="the clean hero: the violet stick turning slowly on the mosaic table, no badge (VN19) — pinned both ends",
  vo="Go be too busy glowing to look backward.", duration=5,
  action="the FACELOVE stick (a little longer than her hand is wide) stands upright on the mosaic table in the late sun and turns slowly a quarter turn to bring the wordmark to the lens",
  motion="the stick turns a slow quarter turn on its base", pace="one quarter turn over the shot",
  start_pos="the stick upright on the mosaic table, wordmark turned a quarter away from the lens", end_pos="the stick upright, wordmark square to the lens",
  marks={}, music="MUS-OFFER", lines="L021")


def SPLIT(beat, parts):
    """Replace one row by 2+ shots (a new size or angle each, §24K part 5 V7.99.0): parts = [overrides, ...]."""
    i = next(n for n, r in enumerate(rows) if r["beat"] == beat); base = rows.pop(i)
    for j, o in enumerate(parts):
        r = dict(base); r["beat"] = beat + "abcdefg"[j]
        if j > 0:
            for k in ("take_kind", "start_pos", "split", "axis", "time_cut"): r.pop(k, None)
        if j < len(parts) - 1:
            for k in ("end_marks", "end_pos"): r.pop(k, None)
        for k in ("turn", "beat_before"):
            if k not in o: r.pop(k, None)
        r.update(o); rows.insert(i + j, r)

SPLIT("SC01-SH04", [dict(dialogue="Michelle? Is that you? My God, what happened,", duration=3),
                    dict(dialogue="did you get work done? You look so much more beautiful.", duration=3, scale="MCU", height="eye", shot=["SH-34", "SH-EYE"], rig="F11",
                         coverage="single", why="Peter's double-take, wider: the woman's shoulder at the edge of frame", motion="he leans over the cart, his hand lifting off the handle; the pan follows")])
SPLIT("SC02-SH03", [dict(dialogue="I am sorry, Michelle. After thirty one years.", duration=3),
                    dict(dialogue="I just... I need something different.", duration=3, scale="MEDIUM", side="profile", shot=["SH-PROFILE", "SH-MED"], rig="F22",
                         why="in profile as he turns from her: the counter-move holds him in frame as he leaves her", motion="he turns away toward the archway, one step; the camera moves against him")])
SPLIT("SC03-SH02", [dict(dialogue="When did I start looking like this? Tired. Worn out.", duration=4, turn=True, beat_before=1.0),
                    dict(dialogue="Older than I am. No wonder he stopped looking at me.", duration=4, scale="MCU", side="front", fg="reflection", shot=["SH-EYE"], rig="F12", coverage="single",
                         why="the mirror's face straight on: the stranger she sees", motion="her hand drops from her face to the vanity; the camera tilts with it")])
SPLIT("SC04-SH03", [dict(vo="I decided this was just what sixty looked like,", duration=3),
                    dict(vo="and I made my peace with disappearing.", duration=3, scale="WIDE", shot=["SH-WIDE", "SH-HIGH"], rig="F8",
                         why="the crane rises away: small in the cool room", motion="she sits back on the stool and lowers her head; the crane rises")])
SPLIT("SC05-SH04", [dict(dialogue="I am fine, Rosa. I am.", duration=2),
                    dict(dialogue="I just... I do not know who that woman in the mirror is anymore.", duration=4, scale="MCU", side="profile", height="eye", shot=["SH-PROFILE"], rig="F12",
                         why="in profile, her eyes going to the mirror on the wall", motion="her eyes slide to the mirror and her chin lowers; the camera tilts with it")])
SPLIT("SC05-SH07", [dict(dialogue="Can I tell you something?", duration=2),
                    dict(dialogue="Two years ago, I felt exactly like that. Same mirror, same thoughts.", duration=4, scale="MCU", side="three-quarter", fg="clean", shot=["SH-34"], rig="F11", coverage="single",
                         why="Rosa, closer: her own two years ago", motion="Rosa's hand lifts to her own cheek and lowers; the pan follows")])
SPLIT("SC05-SH09", [dict(dialogue="And I will tell you what I had to learn the hard way.", duration=3, scale="MCU", height="eye", shot=["SH-34", "SH-EYE"], rig="F18", coverage="single",
                         why="Rosa leaning in to the secret", motion="Rosa leans in one step closer; the camera creeps in"),
                    dict(dialogue="It was never your age, Michelle. It was the foundation.", duration=4, turn=True, beat_before=1.0)])
SPLIT("SC06-SH04", [dict(dialogue="Then it reads the warmth of your own skin", duration=3),
                    dict(dialogue="and turns into your exact shade, and it melts right in.", duration=3, scale="CU", side="ots", fg="through", shot=["SH-OTS", "SH-CU"], rig="F18", coverage="ots",
                         why="past Rosa's shoulder onto the white stripe on Michelle's cheek", motion="Rosa lifts the brush end toward the stripe; the camera creeps in")])
SPLIT("SC07-SH03", [dict(vo="For the first time in years,", duration=3, turn=True, beat_before=1.0),
                    dict(vo="I did not look away from my own reflection.", duration=3, scale="MEDIUM", side="ots", fg="through", shot=["SH-OTS", "SH-MED"], rig="F7", coverage="single",
                         why="over her shoulder: her and the mirror, eye to eye", motion="she lowers the stick and smiles at the mirror; the camera arcs a little")])
SPLIT("SC09-SH02", [dict(dialogue="I am sorry, I just have to ask.", duration=3),
                    dict(dialogue="What do you use on your skin? You look amazing.", duration=3, scale="MCU", side="ots", fg="through", shot=["SH-OTS"], rig="F2", coverage="ots",
                         why="past Michelle's shoulder onto the woman, eager, close", motion="the woman leans toward Michelle, hand out; Michelle's shoulder turns in the foreground")])
SPLIT("SC12-SH01", [dict(dialogue="So if someone ever looked at you and made you feel like you had faded,", duration=4),
                    dict(dialogue="please hear me. It was never you.", duration=3, turn=True, beat_before=1.0, scale="CU", side="front", height="eye", shot=["SH-CU", "SH-EYE"], rig="F18", coverage="single",
                         why="straight into the lens, close: to the viewer", motion="she leans an inch toward the lens and nods once; the camera creeps in")])
SPLIT("SC12-SH02", [dict(dialogue="The thing she wanted to know, I will tell you instead.", duration=4),
                    dict(dialogue="It is called FACELOVE, and I have linked it below.", duration=3, scale="MCU", side="three-quarter", shot=["SH-34"], rig="F4", coverage="single",
                         why="the stick beside her face, the slider gliding across", motion="she turns the stick so the wordmark faces the lens; the slider glides sideways")])
SPLIT("SC12-SH03", [dict(vo="Right now you get two Foundation Sticks for almost the price of one, plus a free primer, a mystery gift,", duration=4, turn=False),
                    dict(vo="and free shipping and a full thirty day money back guarantee.", duration=4, scale="MEDIUM", side="three-quarter-back", height="eye", shot=["SH-MED", "SH-REAR"], rig="F13",
                         coverage="cutaway", why="she rises and walks to the bougainvillea in the late sun: whole", motion="she stands up and walks three steps to the bougainvillea; the camera leads her",
                         marks={"N": "walking from the table to the bougainvillea"}, end_marks={"N": "by the bougainvillea"},
                         end_pos="Michelle standing by the bougainvillea in the late sun, the stick in her hand", turn=False)])

# --- derived fields ---
from collections import defaultdict
G = defaultdict(list)
for r in rows: G[r["group"]].append(r)
for g, rs in G.items():          # §30J: shallow on at most two thirds of a scene — the plainer singles go to medium depth
    for r in rs:
        if sum(1 for x in rs if x["focus"]["dof"] == "shallow") * 3 <= len(rs) * 2: break
        if r["focus"]["dof"] == "shallow" and r["scale"] in ("MCU", "MEDIUM") and not r.get("turn") and not r.get("product_beat") and not r["focus"].get("rack"):
            r["focus"]["dof"] = "medium"
    for r in rs:
        if sum(1 for x in rs if x["focus"]["dof"] == "shallow") * 3 <= len(rs) * 2: break
        if r["focus"]["dof"] == "shallow" and not r.get("turn") and not r.get("product_beat") and not r["focus"].get("rack"):
            r["focus"]["dof"] = "medium"
for r in rows:
    r.setdefault("pace", "")
    r.setdefault("ingredients", sorted(set(r.get("cast", []) + [r["location"]])))
order = list(dict.fromkeys(r["take"] for r in rows))
json.dump({"build": "facelove-walmart", "rows": rows}, open(HERE / "act_map.json", "w"), indent=1, ensure_ascii=False)
print(len(rows), "rows,", len(order), "takes,", sum(r["duration"] for r in rows), "s")
