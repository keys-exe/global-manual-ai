#!/usr/bin/env python3
"""stryde-71-stairs — step 5 act map (E4), one source of truth.

Writes:
  work/actmap_rows.json   every beat in cut order, E4 fields (+ §27G motion, §30I angle, §30J focus, §30K light)
  work/angles.json        the cut order for scripts/angles.py
  work/actmap.md          the act-map tables (pasted into STEP4_5.md)
Durations stay `pending-master` (E6) until the voice master exists.
"""
import json, pathlib
HERE = pathlib.Path(__file__).parent

ROWS = []
def R(beat, act, line, key, fn, subj, loc, day, framing, action, pace, staging, prod, vis, model,
      h, side, fg, scale, why, plane, dof, src, kelvin, time, arc, face, ledger="", layout="full", eg="",
      pin="no", camera="locked off", typ="BR", moving=False, speaking=False, mirror=None, ks=None):
    # on-screen key side from the camera side (§30K): the window stays where it is, so it swaps with the camera
    if vis in ("VISIBLE", "REVEAL", "REVEAL→CONCEALED") or prod.startswith(("worn (anatomical)", "held", "box")):
        plane = "product"
    ks = ks or {"front": "L", "three-quarter": "R", "profile": "L", "behind": "L", "three-quarter-back": "R", "ots": "R"}[side]
    ROWS.append(dict(beat=beat, act=act, type=typ, line=line, key=key, function=fn, subject=subj, location=loc,
        story_day=day, framing=framing, action=action, pace=pace, camera=camera, staging=staging, pin_end=pin, max=6,
        product=prod, visibility=vis, model=model, layout=layout, eg=eg, ledger=ledger, duration="pending-master",
        angle=dict(height=h, side=side, fg=fg, scale=scale, why=why), mirror_of=mirror,
        focus=dict(plane=plane, dof=dof, rack=None, moving_subject=moving),
        light=dict(source=src, key_side=ks, time=time, arc=arc, kelvin=kelvin), face=face, speaking=speaking))

def TH(beat, act, line, note=""):
    ROWS.append(dict(beat=beat, act=act, type="TH", line=line, key="", function="talking head (EG02)", subject="N",
        location="L-N-LANDING", story_day="N-TODAY", framing="propped phone at chest height, ~1.25 m, waist-up, standing at the top of her stairs — photo wall behind left, dark rail and newel right (no selfie — user 2026-09-28)",
        action=note or "speaks the line to the lens", pace="natural", camera="propped (R2), not held", staging="none", pin_end="no", max=6,
        product="absent", visibility="—", model="HeyGen Avatar V", layout="full", eg="EG02", ledger="", duration="pending-master",
        angle=dict(height="eye", side="front", fg="clean", scale="MCU", why="propped talking head"), mirror_of=None,
        focus=dict(plane="eyes", dof="deep", rack=None, moving_subject=False),
        light=dict(source="landing window, south wall", key_side="L", time="midday", arc="today", kelvin=5600), face=True, speaking=True))

E, TQ, PR, FR, BH, OT, TQB = "eye", "three-quarter", "profile", "front", "behind", "ots", "three-quarter-back"
# light sources
STAIR_AM = ("landing window at the top of the stairs, south wall", 6500)   # grey morning, problem days
STAIR_PM = ("front-door sidelights, west wall", 5600)                       # afternoon sun, after days
KIT = ("window over the sink, south wall", 5600)
REC = ("warm string lights and chandeliers", 3200)
STORE = ("overhead fluorescent panels", 4000)
SUN = ("open sky, afternoon sun", 5600)
CLIN = ("exam-room window, blind half open, west wall", 5600)
BED = ("bedroom window, east wall", 5600)
LIV = ("living-room window, front wall", 5600)
MALL = ("atrium skylight above the mall staircase", 5600)

# ---------------- Hook 1 (Last Sunday, N-D4)
A = "Hook 1"
R("HK-01a", A, "I'm 71, and I take the stairs faster than women half my age.", "stairs", "hook — the result", "N + C2", "L-N-STAIRS", "N-D4",
  "MEDIUM from the hall floor: N climbs her family-photo staircase briskly, hand only brushing the rail; C2 on the same flight two steps directly behind her, inside the rail, working to keep up (Fix 2026-09-28: C2 at the back of N)",
  "two steps up, N pulling ahead", "one step per second, brisk", "stairs: side-on, waist-up, camera still", "worn (under the dress)", "HIDDEN", "NB2",
  "low", TQB, "clean", "MEDIUM", "low = resolve; she's the strong one", "deep", "deep", *STAIR_PM, "afternoon", "after: Sunday sun", True, ledger="VN04")
R("HK-02a", A, "Last Sunday, my daughter walked behind me the whole way up", "daughter", "hook — the witness", "C2", "L-N-STAIRS", "N-D4",
  "MCU from the landing looking down the flight: C2 near the top, a hand on the rail, looking up after her mother, a little out of breath",
  "one last step up and a look up", "one step, about a second", "stairs: camera at the top, subject coming up, 1 step", "absent", "—", "NB2",
  "high", FR, "clean", "MCU", "high = from N's place at the top: she's arrived first", "eyes", "medium", *STAIR_PM, "afternoon", "after: Sunday sun", True)
TH("TH-01", A, "and said, \"Mama, when did that happen?\"")
# ---------------- Hook 2 — same lines, different visuals (user 2026-09-28: "2 versions same script different visual")
A = "Hook 2"
R("HK-01b", A, "I'm 71, and I take the stairs faster than women half my age.", "stairs", "hook — the result (version B, mall)", "N + one-offs", "L-MALL", "N-D4",
  "MEDIUM from the concourse: N climbs the mall's open staircase briskly, drawing level with two younger women standing still on the up escalator beside the stairs",
  "two brisk steps up, drawing level with the escalator riders", "one step per second, brisk", "stairs: camera at the bottom, subject 2 steps, camera still", "worn (under the dress)", "HIDDEN", "NB2",
  "low", TQ, "clean", "MEDIUM", "low = resolve; she beats the escalator", "deep", "deep", *MALL, "afternoon", "after: Sunday sun", True, ledger="VN04")
R("HK-02b", A, "Last Sunday, my daughter walked behind me the whole way up", "daughter", "hook — the witness (version B, mall)", "N + C2", "L-MALL", "N-D4",
  "MEDIUM side-on from the concourse: N mid-flight on the mall staircase, C2 one step directly behind her with shopping bags, looking up at her mother",
  "one step up each, the daughter a beat behind", "one step per second", "stairs: side, waist-up, camera still", "worn (under the dress)", "HIDDEN", "NB2",
  "eye", PR, "clean", "MEDIUM", "side-on = we watch the gap between them", "deep", "deep", *MALL, "afternoon", "after: Sunday sun", True)


# ---------------- Act 1 — the problem (six weeks ago, N-D1)
A = "Act 1"
R("P-01a", A, "Six weeks ago, I was going down my stairs backwards.", "backwards", "problem", "N", "L-N-STAIRS", "N-D1",
  "MEDIUM from the landing: N going down the stairs backwards, facing the steps, both hands gripping the rail",
  "one careful step down backwards", "one step, about two seconds", "stairs: camera at the top, subject below, slow single step", "absent", "—", "NB2",
  "high", BH, "clean", "MEDIUM", "high = small against the drop, overwhelmed", "deep", "deep", *STAIR_AM, "morning", "problem: grey", False, ledger="VN04")
R("P-01b", A, "One step at a time.", "step", "problem", "N", "L-N-STAIRS", "N-D1",
  "CU from the side at step height: her slipper lowers onto the next step down, the other foot joins it",
  "one foot down, the other joins", "about two seconds", "stairs: feet only, side", "absent", "—", "NB2",
  "ground", PR, "clean", "CU", "ground = the steps themselves", "foreground", "medium", *STAIR_AM, "morning", "problem: grey", False)
TH("TH-02", A, "I ain't gonna lie, some days I wasn't going down them at all.")
R("P-02a", A, "I'd just stay upstairs.", "upstairs", "problem", "—", "L-N-STAIRS", "N-D1",
  "WIDE from the top landing looking down the empty staircase to the closed front door, the hall below dim",
  "none — the light shifts faintly on the runner", "held, about two seconds", "none", "absent", "—", "NB2",
  "high", FR, "through", "WIDE", "high, through the banister = trapped up here", "deep", "deep", *STAIR_AM, "morning", "problem: grey", False)
R("P-03a", A, "That big knee brace I bought slid right down my leg.", "brace", "failed fix", "N", "L-N-KITCHEN", "N-D1",
  "CU seated at the kitchen table: a black hinged knee brace over her bare right knee, sagging below the kneecap, her hand hauling it up",
  "her hand pulls the brace up once and it slips back", "one pull, about two seconds", "hands: large in frame, one movement", "absent (generic brace, §10)", "—", "NB2",
  "high", TQ, "clean", "CU", "high = her own view of her knee", "hands", "medium", *KIT, "morning", "problem: grey", False)
R("P-03b", A, "By evening, it was around my ankle.", "ankle", "failed fix", "N", "L-N-KITCHEN", "N-D1",
  "CU at floor level: the brace bunched around her right ankle above her slipper",
  "she shifts her foot once", "one small shift, about a second", "feet only", "absent", "—", "NB2",
  "ground", TQ, "clean", "CU", "ground = where it ended up", "foreground", "medium", *KIT, "evening", "problem: grey", False)
TH("TH-03", A, "I done tried everything.")
R("P-04a", A, "Physical therapy.", "therapy", "failed fix", "N + one-off PT", "L-CLINIC", "N-D1b",
  "MEDIUM: N lying on a PT treatment table, a therapist's hands bending her right knee",
  "the therapist bends the knee a little further", "one slow bend, about two seconds", "hands: one movement, subject lying still", "absent", "—", "NB2",
  "high", TQ, "clean", "MEDIUM", "high = done to her, passive", "hands", "medium", *CLIN, "afternoon", "problem: clinical", False)
R("P-04b", A, "Pain pills.", "pills", "failed fix", "N hand", "L-N-KITCHEN", "N-D1c",
  "overhead on the table: orange pill bottles, a blister pack, a coffee mug; her hand taps two tablets into her palm",
  "two tablets tip into her palm", "one tip, about a second", "hands: large in frame", "absent", "—", "NB2",
  "overhead", FR, "clean", "CU", "overhead = routine", "hands", "deep", *KIT, "morning", "problem: grey", False, ledger="VN06")
R("P-04c", A, "Cortisone shots.", "shots", "failed fix", "N + one-off doctor", "L-CLINIC", "N-D1b",
  "CU: gloved hands hold a syringe to the side of her right knee, the skin swabbed",
  "the needle goes in slowly", "one slow push, about two seconds", "hands: large in frame, one movement", "absent", "—", "NB2",
  "eye", PR, "clean", "CU", "profile runs the needle across the frame", "hands", "shallow", *CLIN, "afternoon", "problem: clinical", False)
R("P-04d", A, "Every brace and sleeve they make.", "brace", "failed fix", "N hand", "L-N-KITCHEN", "N-D1c",
  "high CU: a heap of knee braces and sleeves on the table, her hand drops one more on the pile",
  "one brace dropped on the pile", "one drop, about a second", "hands: one movement", "absent (generic, §10)", "—", "NB2",
  "high", TQ, "clean", "CU", "high = the pile is beneath her, done with it", "hands", "deep", *KIT, "morning", "problem: grey", False)
TH("TH-04", A, "Nothing worked. Nothing lasted.")
R("P-05a", A, "Nothing gave me my life back.", "life", "low", "N", "L-N-KITCHEN", "N-D1c",
  "MEDIUM: N at the kitchen table among the bottles and braces, a cold coffee, looking at nothing",
  "she lets out one breath, shoulders drop", "one breath, about two seconds", "none", "absent", "—", "NB2",
  "eye", PR, "through", "MEDIUM", "profile through the doorway = watched, alone", "eyes", "deep", *KIT, "morning", "problem: grey", True)

# ---------------- Act 2 — the turn (the wedding, June, N-D2)
A = "Act 2"
R("T-01a", A, "Then my grandbaby got married in June.", "married", "turn", "one-off bride + guests", "L-RECEPTION", "N-D2",
  "MEDIUM: the bride in white laughing with guests at a reception table, string lights overhead",
  "the bride throws her head back laughing", "one laugh, about two seconds", "none", "absent", "—", "NB2",
  "eye", TQ, "clean", "MEDIUM", "", "eyes", "deep", *REC, "evening", "turn: warm party light", True, ledger="VN05")
R("T-01b", A, "My cousin Loretta was there.", "Loretta", "turn", "C1", "L-RECEPTION", "N-D2",
  "MCU: Loretta at the edge of the dance floor, clapping on the beat",
  "two claps on the beat", "about a second", "hands: one movement", "absent", "—", "NB2",
  "low", TQ, "clean", "MCU", "low = she's the one with the strength", "eyes", "deep", *REC, "evening", "turn: warm party light", True, ledger="VN05")
TH("TH-05", A, "She's 74,")
R("T-02a", A, "and she was out on that dance floor all night.", "floor", "turn", "C1 + one-off guests", "L-RECEPTION", "N-D2",
  "WIDE: a line of guests doing a line dance, Loretta in the middle of the line, stepping in time",
  "one side step with the line", "one step per beat, about a second", "dancing: wide, side step, camera still", "worn (under her dress, hidden)", "HIDDEN", "NB2",
  "eye", FR, "through", "WIDE", "through the guests = we're watching from our table", "deep", "deep", *REC, "evening", "turn: warm party light", False, ledger="VN05")
R("T-02b", A, "Electric Slide, Cupid Shuffle, all of it.", "Slide", "turn", "C1 feet + line", "L-RECEPTION", "N-D2",
  "CU at floor level: a row of dancing feet on the parquet, Loretta's white slip-ons among them, stepping together",
  "one step back in unison", "one step, about a second", "feet only, one step", "absent", "—", "NB2",
  "ground", FR, "clean", "CU", "ground = the steps", "foreground", "medium", *REC, "evening", "turn: warm party light", False, ledger="VN05")
R("T-03a", A, "Both her knees was bone on bone too.", "bone", "mechanism — the worn joint", "—", "—", "—",
  "ANAT-A: a knee in the anatomical register, the worn joint surface glowing red",
  "the red pulses once", "one pulse, about a second", "none", "absent", "—", "NB2",
  "eye", PR, "clean", "CU", "profile shows the joint gap", "deep", "deep", "anatomical register (§12A)", 5600, "—", "mechanism", False, eg="EG04")
TH("TH-06", A, "I always figured hers wasn't as bad as mine. I always figured mine was past fixing.")

# ---------------- Act 3 — the reveal (Loretta's visit, N-D3)
A = "Act 3"
R("R-01a", A, "Loretta came to stay the week after.", "stay", "reveal", "C1", "L-N-STAIRS", "N-D3a",
  "MEDIUM from inside the hall: Loretta stepping in through the open front door with a small overnight bag",
  "one step over the threshold", "one step, about a second", "walking toward camera: waist-up, 1 step", "absent", "—", "NB2",
  "eye", FR, "clean", "MEDIUM", "", "eyes", "deep", *STAIR_PM, "afternoon", "turn: daylight in the door", True)
TH("TH-07", A, "She watched me at the kitchen table, going through my morning routine.")
R("R-02a", A, "Two anti-inflammatories, the gel,", "gel", "reveal — the routine", "N hands", "L-N-KITCHEN", "N-D3",
  "overhead: her hands squeeze gel from a plain tube onto her fingers beside two tablets and a glass of water",
  "one squeeze", "about a second", "hands: large in frame", "absent", "—", "NB2",
  "overhead", FR, "clean", "CU", "overhead = routine", "hands", "deep", *KIT, "morning", "routine", False, ledger="VN06")
R("R-02b", A, "the brace, an ice pack on my right knee.", "ice", "reveal — the routine", "N", "L-N-KITCHEN", "N-D3",
  "CU seated: she presses a blue ice pack onto her right knee over the brace",
  "she presses the pack down once", "one press, about a second", "hands: one movement", "absent", "—", "NB2",
  "high", TQ, "clean", "CU", "high = her own view of her knee", "hands", "medium", *KIT, "morning", "routine", False)
TH("TH-08", A, "After a minute she said, \"Baby, can I show you something?\"")
R("R-03a", A, "She pulled up her pant leg.", "leg", "reveal (§9D)", "C1", "L-N-KITCHEN", "N-D3",
  "MEDIUM seated across the table: Loretta rolls her right khaki trouser leg up over the knee",
  "one roll up past the knee", "one roll, about two seconds", "hands: one movement, seated", "worn", "REVEAL", "NBP",
  "eye", TQ, "clean", "MEDIUM", "", "hands", "medium", *KIT, "morning", "turn", True)
R("R-04a", A, "She had on a little black strap, right under her kneecap. Stryde.", "strap", "product first appearance", "C1", "L-N-KITCHEN", "N-D3",
  "ECU her right knee: the strap seated just under the kneecap, her finger tapping it once",
  "one tap on the strap", "one tap, about a second", "hands: large in frame", "worn", "VISIBLE", "NBP",
  "low", TQ, "clean", "ECU", "low = the answer, resolve", "product", "medium", *KIT, "morning", "turn", False)
R("R-05a", A, "She handed me one. It looked ridiculous. Too small.", "small", "held product", "N hands", "L-N-KITCHEN", "N-D3",
  "CU: a strap resting across N's open palms, small against her hands",
  "she turns her hands a little to look at it", "one small tilt, about a second", "hands: product rigid", "held", "VISIBLE", "NBP",
  "high", FR, "clean", "CU", "high = her own view of it in her hands", "product", "medium", *KIT, "morning", "turn", False)
TH("TH-09", A, "I said, \"Loretta, you know good and well this ain't gonna work on knees like mine.\"")
R("R-06a", A, "She said, \"Just put it on and walk down them stairs.\"", "stairs", "SEAT", "N", "L-N-KITCHEN", "N-D3",
  "CU seated: both hands slide the strap up her right shin to seat it under the kneecap",
  "slides up the last few centimetres and stops at contact", "one slide, about a second", "hands: start mid-movement, end on contact", "seated", "VISIBLE", "NBP",
  "high", TQ, "clean", "CU", "high = her own view of her knee", "product", "medium", *KIT, "morning", "turn", False)
R("R-07a", A, "I did. Chile, the first step, I didn't even have to hold the rail.", "rail", "payoff", "N", "L-N-STAIRS", "N-D3",
  "MEDIUM from the hall floor: N at the top of the stairs takes the first step down facing forwards, hands at her sides",
  "one step down, facing forwards", "one step, about a second", "stairs: camera at the bottom, subject 1 step, hands free", "worn", "VISIBLE", "NBP",
  "low", FR, "clean", "MEDIUM", "low = resolve", "deep", "deep", *STAIR_PM, "afternoon", "after: sun through the sidelights", True, mirror="P-01a")
R("R-07b", A, "Not the second. Not the third.", "second", "payoff", "N feet", "L-N-STAIRS", "N-D3",
  "CU at step height from the side: her feet come down two steps, one foot per step, strap on the right knee at top of frame",
  "two steps down", "one step per second", "stairs: feet only, side", "worn", "VISIBLE", "NBP",
  "ground", PR, "clean", "CU", "ground = the steps", "product", "medium", *STAIR_PM, "afternoon", "after: sun", False, mirror="P-01b")
R("R-07c", A, "All the way down. Both feet. Forwards.", "Forwards", "payoff", "N", "L-N-STAIRS", "N-D3",
  "MEDIUM from the side through the spindles: she steps off the last step into the hall, facing forwards",
  "last step down onto the hall floor", "one step, about a second", "stairs: side, waist-up, camera still", "worn", "VISIBLE", "NBP",
  "eye", PR, "through", "MEDIUM", "through the spindles = Loretta's view, watching her do it", "deep", "deep", *STAIR_PM, "afternoon", "after: sun", True)

# ---------------- Act 4 — mechanism (Loretta's words)
A = "Act 4"
R("M-01a", A, "She said, \"Everything else you tried was made to keep you comfortable", "comfortable", "mechanism — comparative (F2)", "N", "L-CLINIC", "N-D1b",
  "MEDIUM: N lying back on the PT table with a heat pad on her knee, eyes closed",
  "she settles her head back", "one settle, about a second", "none", "absent", "—", "NB2",
  "overhead", FR, "clean", "MEDIUM", "overhead = passive, managed", "eyes", "deep", *CLIN, "afternoon", "problem: clinical", True, ledger="F2")
R("M-01b", A, "while your knee got worse.", "worse", "mechanism — comparative (F2)", "—", "—", "—",
  "ANAT-A: the worn knee joint, the red spreading a little further",
  "the red spreads slowly", "about two seconds", "none", "absent", "—", "NB2",
  "eye", TQ, "clean", "CU", "", "deep", "deep", "anatomical register (§12A)", 5600, "—", "mechanism", False, eg="EG04", ledger="F2")
R("M-02a", A, "This one fixes why it hurts.\"", "fixes", "mechanism — comparison card (EG03, F2/F3)", "—", "—", "—",
  "CARD: two knees side by side in the anatomical register — left, a full sleeve over the whole knee, pressure spread everywhere; right, the strap seated under the kneecap on one spot",
  "a slow soft glow settles on the right knee's spot", "about two seconds", "none", "worn (anatomical)", "—", "NB2",
  "eye", FR, "clean", "MEDIUM", "", "deep", "deep", "anatomical register (§12A)", 5600, "—", "mechanism", False, layout="card", eg="EG03 · labels in the edit", ledger="F3")
R("M-03a", A, "She said, \"There's one spot under the kneecap where every step lands.\"", "spot", "mechanism — the spot", "—", "—", "—",
  "ANAT-A: the knee, a red point on the patellar tendon just under the kneecap pulsing with each step",
  "the point pulses with a walking cadence", "one pulse per second", "none", "absent", "—", "NB2",
  "low", PR, "clean", "CU", "low = the spot made big and important", "deep", "deep", "anatomical register (§12A)", 5600, "—", "mechanism", False, eg="EG04")
R("M-04a", A, "\"Every brace, every shot, every pill you ever tried treated the whole knee.", "whole", "mechanism — comparative (F2)", "—", "L-N-KITCHEN", "N-D1c",
  "overhead: the heap of braces and sleeves beside the pill bottles on the table",
  "none — held", "about two seconds", "none", "absent", "—", "NB2",
  "overhead", FR, "clean", "MEDIUM", "overhead = the whole routine laid out", "deep", "deep", *KIT, "morning", "problem: grey", False, ledger="F2")
R("M-04b", A, "Not that spot. That's why ain't nothing worked.", "spot", "mechanism", "—", "—", "—",
  "ANAT-A: the knee with a generic sleeve drawn around it, the red point below the kneecap still glowing under it",
  "the red point keeps pulsing under the sleeve", "one pulse per second", "none", "absent", "—", "NB2",
  "eye", TQ, "clean", "CU", "", "deep", "deep", "anatomical register (§12A)", 5600, "—", "mechanism", False, eg="EG04", ledger="F2")
R("M-05a", A, "\"The pain is pressure. That's all it is.", "pressure", "mechanism", "—", "—", "—",
  "ANAT-A: pressure lines running down the thigh into the red point under the kneecap",
  "pressure pulses down the leg", "one pulse per second", "none", "absent", "—", "NB2",
  "eye", PR, "clean", "MEDIUM", "profile shows the load path down the leg", "deep", "deep", "anatomical register (§12A)", 5600, "—", "mechanism", False, eg="EG04")
R("M-05b", A, "This strap sits right on that spot and takes the weight off.\"", "weight", "mechanism — protection", "—", "—", "—",
  "ANAT-A: the strap seated under the kneecap, the pad on the spot, the red fading to calm blue",
  "the red fades to blue as the pad takes the load", "one fade, about two seconds", "none", "worn (anatomical)", "—", "NB2",
  "low", TQ, "clean", "CU", "low = the fix, resolve", "deep", "deep", "anatomical register (§12A)", 5600, "—", "mechanism", False, eg="EG04")
R("M-06a", A, "First step. Pain gone. Just like that.", "gone", "outcome (F4)", "N feet", "L-N-STAIRS", "N-D3",
  "CU from the step below: her foot settles on the top step, strap on the right knee above",
  "one foot lands on the step", "one step, about a second", "stairs: feet only, front", "worn", "VISIBLE", "NBP",
  "ground", FR, "clean", "CU", "ground = the first step", "product", "medium", *STAIR_PM, "afternoon", "after: sun", False, ledger="F4")

# ---------------- Act 5 — proof
A = "Act 5"
for i, (who, place, how, h, sd, src) in enumerate([
    ("one-off man, 60s", "L-MONT-1 porch", "sits on a porch step and seats the strap on his right knee", "high", TQ, SUN),
    ("one-off woman, 50s", "L-MONT-2 bedroom", "on the bed edge, slides the strap up her right shin", "eye", PR, BED),
    ("one-off man, 70s", "L-MONT-3 garage", "one foot on a stool, presses the strap flat under his kneecap", "low", TQ, SUN),
    ("one-off woman, 40s", "L-MONT-4 gym", "seated on a bench, seats the strap under her right kneecap", "high", FR, SUN)]):
    R(f"PR-01{'abcd'[i]}", A, "Over 200,000 people wear one now.", "people", "proof montage (EG05)", who, place, "G-%d" % (i+1),
      f"CU: {how}", "slides/presses the strap to contact", "one movement, about a second", "hands: start mid-movement, end on contact",
      "seated", "VISIBLE", "NBP", h, sd, "clean", "CU", {"high": "high = their own view of the knee", "low": "low = strong", "eye": "profile shows the strap from the side"}[h],
      "product", "medium", *src, "afternoon", "proof: daylight", False, eg="EG05 · 200,000+ overlay")
R("PR-02a", A, "Sports doctors recommend it.", "doctors", "authority (F1)", "one-off sports doctor", "L-CLINIC", "G-5",
  "MCU: a sports-medicine doctor in a polo shirt holds the strap up beside a knee model on his desk",
  "he turns the strap toward the patient", "one turn, about a second", "hands: product rigid", "held", "VISIBLE", "NBP",
  "eye", TQ, "clean", "MCU", "", "eyes", "medium", *CLIN, "afternoon", "authority: even daylight", True, ledger="F1", pin="yes")
TH("TH-10", A, "Not the pharma companies. Sports doctors.")
R("PR-03a", A, "Loretta's husband wears one. He's 76, and he plays golf twice a week.", "golf", "proof", "one-off, Loretta's husband", "L-GOLF", "G-6",
  "MEDIUM from the side: a Black man of 76 in a golf polo and khaki shorts mid-swing follow-through, the strap on his right knee",
  "finishes the follow-through and holds", "one follow-through, about a second", "one movement, feet planted", "worn", "VISIBLE", "NBP",
  "low", PR, "clean", "FULL", "low = strong at 76", "deep", "deep", *SUN, "afternoon", "proof: sun", True)
R("PR-04a", A, "Her niece wears one when she runs track. She's 22.", "track", "proof", "one-off, niece 22", "L-TRACK", "G-7",
  "MEDIUM: a young Black woman jogging on a red running track, the strap on her right knee",
  "three jogging strides past the lens", "about two strides per second", "running across frame: camera still, side-on", "worn", "VISIBLE", "NBP",
  "eye", PR, "clean", "FULL", "profile = she runs across our frame", "deep", "deep", *SUN, "afternoon", "proof: sun", True, moving=False)
R("PR-05a", A, "I've worn mine every day for six weeks.", "worn", "feature", "N", "L-N-BEDROOM", "N-D5",
  "CU on the bed edge in the morning: N seats the strap under her right kneecap",
  "slides the strap the last few centimetres", "one slide, about a second", "hands: start mid-movement, end on contact", "seated", "VISIBLE", "NBP",
  "high", TQ, "clean", "CU", "high = her own view of her knee", "product", "medium", *BED, "morning", "after: fresh daylight", False)
TH("TH-11", A, "Under my clothes. Don't nobody know it's there.")
R("PR-05b", A, "Under my clothes. Don't nobody know it's there.", "clothes", "feature — conceal (§9D)", "N", "L-N-BEDROOM", "N-D5",
  "CU from the side: her trouser leg drops over the strap and lies flat",
  "the trouser leg falls and settles", "one drop, about a second", "none", "worn", "REVEAL→CONCEALED", "NBP",
  "eye", PR, "clean", "CU", "profile shows the flat trouser line", "product", "medium", *BED, "morning", "after: fresh daylight", False)
R("PR-06a", A, "No pills. No gel. No brace around my ankle by lunchtime.", "pills", "feature", "—", "L-N-KITCHEN", "N-D5",
  "overhead: the kitchen table cleared — just a coffee mug and the strap lying beside it",
  "steam rises from the mug", "about two seconds", "none", "absent (strap on table)", "VISIBLE", "NBP",
  "overhead", FR, "clean", "CU", "overhead = the same table, the routine gone", "product", "deep", *KIT, "morning", "after: sun", False, mirror="P-04b")

# ---------------- Act 6 — the result, lived (yesterday, N-D6)
A = "Act 6"
R("L-01a", A, "Yesterday I walked to the store. Two miles there. Two miles back.", "store", "result (F7)", "N", "L-STREET", "N-D6",
  "MEDIUM from behind: N walking away along the sidewalk of her tree-lined street, a tote bag on her shoulder",
  "three steps away from the lens", "one step per second", "walking away: waist-up, 3 steps, camera still", "worn (under trousers)", "HIDDEN", "NB2",
  "eye", BH, "clean", "MEDIUM", "behind = we let her go, she doesn't need us", "deep", "deep", *SUN, "afternoon", "after: sun", False, ledger="F7")
R("L-01b", A, "Passed three women half my age.", "passed", "result", "N + one-offs", "L-STREET", "N-D6",
  "MEDIUM three-quarter: N overtakes three younger women strolling slowly on the sidewalk",
  "two steps as she draws level and passes", "one step per second", "walking across frame: camera still", "worn (under trousers)", "HIDDEN", "NB2",
  "low", TQ, "clean", "MEDIUM", "low = she's the strong one", "deep", "deep", *SUN, "afternoon", "after: sun", True)
R("L-02a", A, "Stood in that checkout line ten minutes without shifting my weight.", "checkout", "result", "N + one-offs", "L-STORE", "N-D6",
  "MEDIUM: N standing square in a grocery checkout line with a full basket, shoppers ahead of her",
  "she moves the basket to her other hand, feet planted", "one movement, about a second", "none", "worn (under trousers)", "HIDDEN", "NB2",
  "eye", TQ, "clean", "MEDIUM", "", "eyes", "deep", *STORE, "afternoon", "after: store light", True, ledger="VN07")
R("L-02b", A, "Carried two bags home. Didn't nobody help me.", "bags", "result", "N", "L-STREET", "N-D6",
  "MEDIUM from behind: N walking up her front path to the porch, a grocery bag in each hand",
  "two steps up the path", "one step per second", "walking away: waist-up, 2 steps", "worn (under trousers)", "HIDDEN", "NB2",
  "low", TQB, "clean", "MEDIUM", "low = resolve; she made it", "deep", "deep", *SUN, "afternoon", "after: sun", False)
R("L-03a", A, "When I got home, my husband said, \"You was gone a long time.\"", "husband", "result", "one-off, N's husband", "L-N-LIVING", "N-D6",
  "MEDIUM: her husband in his recliner lowers the newspaper and looks up toward the door",
  "lowers the paper and looks up", "one movement, about a second", "none", "absent", "—", "NB2",
  "eye", TQ, "clean", "MEDIUM", "", "eyes", "deep", *LIV, "afternoon", "after: sun", True)
TH("TH-12", A, "I said, \"I know.\"")

# ---------------- Act 7 — close
A = "Act 7"
R("C-01a", A, "That was six weeks of wearing the strap. Nothing else.", "strap", "result", "N", "L-N-BEDROOM", "N-D5",
  "CU: the strap on N's right knee as she sits on the bed edge, her hand resting beside it",
  "her hand pats her knee once", "one pat, about a second", "hands: one movement", "worn", "VISIBLE", "NBP",
  "eye", TQ, "clean", "CU", "", "product", "medium", *BED, "morning", "after: fresh daylight", False)
R("C-02a", A, "Three ladies from church already ordered one after they watched me come down the church steps.", "church", "proof", "N + 3 one-offs", "L-CHURCH", "N-D4",
  "MEDIUM from the sidewalk: N comes down the brick church steps facing forwards, three ladies in Sunday hats watching from the side",
  "one step down, facing forwards", "one step, about a second", "stairs: camera at the bottom, subject 1 step, hands free", "worn (under the dress)", "HIDDEN", "NB2",
  "low", TQ, "clean", "MEDIUM", "low = resolve; she's the proof", "deep", "deep", *SUN, "afternoon", "after: Sunday sun", True, ledger="VN08")
TH("TH-13", A, "So I'ma just say it right here.")
R("C-03a", A, "It's called Stryde Patellar Force Redirection.", "Stryde", "name (F3)", "—", "—", "—",
  "ANAT-A: the strap seated on the knee in the anatomical register, calm blue at the spot (labels in the edit)",
  "a slow soft glow at the pad", "about two seconds", "none", "worn (anatomical)", "—", "NB2",
  "eye", TQ, "clean", "CU", "", "deep", "deep", "anatomical register (§12A)", 5600, "—", "mechanism", False, eg="EG04 · labels in the edit", ledger="F3")
R("C-04a", A, "They spent three years designing it with orthopedic surgeons.", "surgeons", "authority", "one-off surgeon + patient", "L-CLINIC", "G-8",
  "MEDIUM: an orthopedic surgeon in scrubs fits the strap on a seated patient's right knee",
  "presses the strap flat under the kneecap", "one press, about a second", "hands: one movement", "seated", "VISIBLE", "NBP",
  "eye", OT, "clean", "MEDIUM", "over the shoulder = we're the patient", "hands", "medium", *CLIN, "afternoon", "authority: even daylight", True)
TH("TH-14", A, "It's the real thing.")
R("C-05a", A, "Not them cheap knock-offs they be selling on Amazon and them fake websites.", "knock-offs", "objection (F5, §10)", "—", "L-N-KITCHEN", "N-D5",
  "CU on a table: two cheap generic knee straps, frayed, a velcro tab curling up (no brand, no packaging, no screen)",
  "a finger flicks the curled tab", "one flick, about a second", "hands: one movement", "absent (fakes, §10)", "—", "NB2",
  "high", TQ, "clean", "CU", "high = looked down on", "foreground", "medium", *KIT, "morning", "objection", False, ledger="F5")
R("C-06a", A, "The link's right down below. Two straps for the price of one right now.", "Two", "offer (EG06)", "N", "L-N-LANDING", "N-TODAY",
  "MCU on the landing, phone propped as in the talking heads: N holds up two straps toward the lens, one in each hand",
  "lifts both straps a little higher", "one lift, about a second", "hands: product rigid in both hands", "held, two units", "VISIBLE", "NBP",
  "eye", FR, "clean", "MCU", "", "product", "medium", "landing window, south wall", 5600, "midday", "offer: bright daylight", True, eg="EG06 · offer overlay")
R("C-07a", A, "Sixty days to send them back if they don't work.", "Sixty", "guarantee", "—", "L-N-KITCHEN", "N-D5",
  "overhead on the kitchen table: the open box with two straps side by side",
  "her hand sets the lid beside the box", "one movement, about a second", "hands: straps do not move", "box open, two units", "VISIBLE", "NBP",
  "overhead", FR, "clean", "CU", "overhead = the table, the reveal", "product", "deep", *KIT, "morning", "offer: bright daylight", False, eg="60-day overlay")
TH("TH-15", A, "Eleven years of knee pain. Gone the first step I took with it on.")
R("C-09a", A, "I bought my sister a pair that same week.", "sister", "close", "N hands", "L-N-KITCHEN", "N-D5",
  "CU: she writes her sister's name on a card and lays it on the closed box",
  "a few pen strokes", "about two seconds", "hands: large in frame", "box closed", "—", "NBP",
  "high", TQ, "clean", "CU", "high = her own view", "hands", "medium", *KIT, "morning", "after", False)
TH("TH-16", A, "She coming Sunday. She gon' walk up my stairs on her own.")

if __name__ == "__main__":
    json.dump(ROWS, open(HERE / "actmap_rows.json", "w"), indent=1)
    ang = []
    for r in ROWS:
        a = dict(beat=r["beat"], group=r["act"], type=r["type"], subject=r["subject"], **r["angle"], mirror_of=r["mirror_of"],
                 mode=1, speaking=r["speaking"], product_beat=not r["product"].startswith("absent") and r["visibility"] != "HIDDEN",
                 focus=r["focus"], story_day=r["story_day"], face=r["face"], light=r["light"])
        ang.append(a)
    json.dump(ang, open(HERE / "angles.json", "w"), indent=1)
    cols = ["Beat", "Act", "Line (verbatim)", "Key", "Function", "Subject", "Location", "Day", "Framing", "Action · pace", "Staging (§27G)",
            "Pin end", "Angle (§30I)", "Focus (§30J)", "Light (§30K)", "Product · visibility", "Layout · EG", "Model", "Ledger"]
    md, cur = [], None
    for r in ROWS:
        if r["act"] != cur:
            cur = r["act"]; md += ["", f"### {cur}", "", "| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
        a, f, l = r["angle"], r["focus"], r["light"]
        md.append("| " + " | ".join(str(x).replace("|", "/") for x in [
            r["beat"], r["act"], r["line"], r["key"], r["function"], r["subject"], r["location"], r["story_day"], r["framing"],
            f'{r["action"]} · {r["pace"]}', r["staging"], r["pin_end"],
            f'{a["height"]} · {a["side"]} · {a["fg"]} · {a["scale"]}' + (f' — {a["why"]}' if a["why"] and r["type"] != "TH" else ""),
            f'{f["plane"]} · {f["dof"]}', f'{l["source"]} · key {l["key_side"]} · {l["time"]} · {l["arc"]} · {l["kelvin"]}K',
            f'{r["product"]} · {r["visibility"]}', r["layout"] + (f' · {r["eg"]}' if r["eg"] else ""), r["model"], r["ledger"] or "—"]) + " |")
    (HERE / "actmap.md").write_text("\n".join(md).strip() + "\n")
    print(len(ROWS), "rows ·", sum(r["type"] == "BR" for r in ROWS), "B-roll ·", sum(r["type"] == "TH" for r in ROWS), "TH")
