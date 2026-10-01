#!/usr/bin/env python3
"""Step-5 act map for down-forwards-again (E4, §27G, §30I–§30L), one row per beat, in cut order.
The doctor's talking head (HeyGen) runs under the whole VO in one segment per act (TH rows);
B-roll rows sit on top of it in the EDIT-DFA layouts (pip / split / cutout / full).
Writes work/angles_rows.json (angles.py), work/actmap.json (full rows) and work/actmap_tables.md."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
PH = {}  # phrase id -> verbatim line
for l in (HERE.parent / "BUILD_SHEET.md").read_text().split("\n"):
    if l.startswith("| HK") or l.startswith("| B-"):
        c = [x.strip() for x in l.split("|")]
        if len(c) > 3 and (c[1][:2] in ("HK", "B-")) and c[1] != "Beat": PH[c[1]] = c[2]

LOC = {
 "L-P-HALL":  dict(plate="P0-PROP-P", tier="TRAVERSED", src="front-door stained glass (east) + tall landing window"),
 "L-P-FRONT": dict(plate="P1-P-FRONTROOM", tier="PLATED", src="bay window, east wall, net curtains"),
 "L-P-KITCH": dict(plate="P2-P-KITCHEN", tier="PLATED", src="window over the sink, west wall"),
 "L-P-DOOR":  dict(plate="P0-PROP-P (exterior: the red-brick front, the step)", tier="INCIDENTAL", src="open sky over the street, east"),
 "L-D-CONS":  dict(plate="P3-D-CONSULT", tier="PLATED", src="consulting-room window, camera-left (north)"),
 "L-ORTHO":   dict(plate="—", tier="INCIDENTAL", src="clinic window, side light"),
 "L-TUBE":    dict(plate="—", tier="INCIDENTAL", src="the street entrance at the top of the stairs (daylight) + station strip lights"),
 "L-PHYSIO":  dict(plate="—", tier="INCIDENTAL", src="the gym's tall windows + ceiling panels"),
 "L-HOSP":    dict(plate="—", tier="INCIDENTAL", src="the bay window past the curtain + ward ceiling light"),
 "L-TOWPATH": dict(plate="—", tier="INCIDENTAL", src="open sky over the canal"),
 "L-PARK":    dict(plate="—", tier="INCIDENTAL", src="open sky over the park"),
 "L-LAB":     dict(plate="—", tier="INCIDENTAL", src="the gait lab's tall side windows + ceiling panels"),
 "L-SHOP":    dict(plate="—", tier="INCIDENTAL", src="the open front of a greengrocer's on a high street, morning sky"),
 "—":         dict(plate="—", tier="—", src="§12A render light"),
}
DAY = {  # story day -> (int, time, act light state, kelvin)
# P-D1 / P-D2 here are the LIGHT states (problem / after). Wardrobe v2 (2026-09-29) keys each body beat to its own story day in work/wardrobe.py.
 "P-D1": (1, "morning", "problem: grey overcast morning, flat and cool", 6500),
 "P-D2": (2, "morning", "after: sun in the house, warmer and open", 5600),
 "D-D1": (3, "morning", "the doctor's room: steady overcast north light", 6500),
 "X-D1": (4, "midday", "everyday: neutral daylight", 5600),
 "MECH": (None, "midday", "§12A anatomical register", 5600),
}
R = []
def row(beat, act, phrases, typ, subject, loc, day, action, pace, camera, staging, pin_end,
        h, side, scale, fg, why, dof, plane, key_side, key, product="absent", layout="cutout · EG04",
        model="NB2", ledger="—", face=False, eg="EG01"):
    R.append(dict(beat=beat, act=act, phrases=phrases, type=typ, subject=subject, loc=loc, day=day,
        action=action, pace=pace, camera=camera, staging=staging, pin_end=pin_end, height=h, side=side,
        scale=scale, fg=fg, why=why, dof=dof, plane=plane, key_side=key_side, key=key, product=product,
        layout=layout + " · " + eg, model=model, ledger=ledger, face=face))
def TH(beat, act, phrases, note):
    R.append(dict(beat=beat, act=act, phrases=phrases, type="TH", subject="D", loc="L-D-CONS", day="D-D1",
        action=note, pace="~155 wpm", camera="phone on a small tripod across the desk, locked off", staging="seated at his desk",
        pin_end="no", height="eye", side="front", scale="MCU", fg="clean", why="", dof="medium", plane="eyes",
        key_side="L", key="", product="absent", layout="spine (under every B-roll) · EG01", model="HeyGen Avatar V", ledger="—", face=True))
PIP, SPL, CUT, FULL = "pip · EG02", "split 60/40 · EG03", "cutout · EG04", "full · EG05"

# ---- HOOK 1 — VN01: result first, triple without (the reference's 0–8.4s) ----------------------------
TH("TH-HK1", "Hook 1", ["HK1-01", "HK1-02", "HK1-03"], "straight to lens, level; a small open hand on 'here is how'")
# §34 2026-09-29 (user: "I WANT A HOOK THAT WILL SELL I DONT WANT THIS NORMAL LOOKING HOOKS"): hook pictures redesigned as pattern interrupts (§31, §22E)
# §34 2026-09-29 board Fix notes: HK1-01a "SHOULD SHOW HER GOING DOWN THE STAIRS AT THE SUBWAY STATION RUNNING DOWN NOT JUST AT HOME";
# HK1-02 "DONT JUST SHOW 1 BROLL HERE SHOW ALL OF THOSE" → one B-roll per "without" (§30B triplet, escalating)
row("HK1-01a","Hook 1",["HK1-01"],"BR","P","L-TUBE","P-D2","runs lightly DOWN the entrance stairs of an Underground station, forwards, both hands free (never on the rail)","one stride, 2s",
    "locked-off sway","stairs descending (§27G: one stride, arms free, camera at the foot)","no","low","front","FULL","clean",
    "low = the stairs she now owns, out in the world","deep","deep","R","stairs",product="worn · CONCEALED under trousers (§9D)",layout=FULL,face=True)
row("HK1-02a","Hook 1",["HK1-02"],"BR","P","L-ORTHO","P-D1","over the surgeon's shoulder: he holds a knee replacement implant out to her across the desk; her worried face","held, 2s",
    "sway","seated (§27G: still, one small lean back)","no","eye","ots","MCU","through","ots = the surgeon's proposal, pressed on her",
    "medium","eyes","L","operation",layout=FULL,face=True)
row("HK1-02b","Hook 1",["HK1-02"],"BR","P","L-PHYSIO","P-D1","busy NHS physio class: she strains through a step-up between the parallel bars, the physio spotting her knee","one step-up, 3s",
    "sway","stepping up (§27G: one step, both hands on the bars)","no","ground","three-quarter","FULL","through","ground = the step that hurts; through the bars = trapped in it",
    "medium","eyes","L","physio",layout=FULL,face=True)
row("HK1-02c","Hook 1",["HK1-02"],"BR","P","L-P-KITCH","P-D1","the STRYDE strap lies apart on the table, sharp; behind, soft, she puts the old braces into a bin bag by hand (nothing flying)","one brace in, 2s",
    "sway","standing at the dresser (§27G: one action, the strap never moves)","no","low","front","CU","clean","low = the strap big in the foreground, the old braces going out behind it",
    "shallow","product","R","drawer",product="object on the table (§15A) · never in the drawer, never in the bag",layout=CUT,model="NBP",face=True)
# ---- HOOK 2 — against his own interest ------------------------------------------------------------------
TH("TH-HK2", "Hook 2", ["HK2-01", "HK2-02"], "leans in a touch on 'before you come and see me'; one flat hand down on the desk on 'not a prescription'")
# ADJUST 2026-09-29 (user: "hk2 02a should not need an end frame remove it"): pin_end no.
# §34 2026-09-29 board Fix: "THE TEN SECONDS IT MEANS TEN SECONDS TO PUT ON THE STRYDE STRAP" → seating beat (§9B), product's first appearance
row("HK2-02a","Hook 2",["HK2-02"],"BR","P","L-P-FRONT","P-D1","slides the closed strap up her LEFT shin and seats it under the kneecap (SEAT_LOCK)","one slide, 3s",
    "sway","seated on the chair edge (§27G: one action, both hands on the shell)","no","low","three-quarter","MEDIUM","clean","low = capable: ten seconds, done",
    "medium","product","R","ten",product="worn · VISIBLE (skirt, seated) · SEATING (§9B) · first appearance",layout=PIP,model="NBP")
# ---- HOOK 3 — the scan ------------------------------------------------------------------------------------
row("HK3-01a","Hook 3",["HK3-01"],"BR","D hand","L-D-CONS","D-D1","drops one more knee X-ray onto the heap of scans burying his desk","one drop, 2s",
    "sway","hands (§27G: one action, the film falls)","no","overhead","front","MEDIUM","clean",
    "overhead = routine: every week, another one","deep","deep","L","scan",layout=FULL)
TH("TH-HK3", "Hook 3", ["HK3-01", "HK3-02"], "lowers the X-ray to the desk; a small shake of the head on 'a different question'")

# ---- ACT 1 — the patient, the band (B-01–B-05) ------------------------------------------------------------
TH("TH-A1", "Act 1", ["B-01","B-02","B-03","B-04","B-05"], "measured; taps just under his own kneecap through the trousers on 'press'")
row("BR-01","Act 1",["B-01"],"BR","P","L-P-KITCH","P-D1","at the kitchen table, both hands round a mug, rubs her LEFT knee once","one rub, 3s",
    "sway","sitting","no","eye","three-quarter","MEDIUM","clean","","medium","eyes","R","patient",layout=CUT,face=True)
row("MECH-01","Act 1",["B-01"],"MECH","anatomy","—","MECH","ANAT: the LEFT knee joint worn bone on bone, the right knee behind it starting to redden","a slow turn, 3s",
    "RV render","none","no","eye","three-quarter","MCU","clean","","deep","deep","L","bone",layout=PIP,eg="EG07")
row("BR-02","Act 1",["B-02"],"BR","D hands","L-D-CONS","D-D1","clips her knee X-ray onto the window glass","one clip, 2s",
    "sway","hands","no","low","three-quarter","CU","clean","low = the scan looms over us","medium","foreground","back","scan",layout=PIP,
    )
# the user, 2026-09-29 (video Fix on MECH-03): "this should be cut into 4 brolls" → B-03 split: MECH-03a (where), BR-03b (how wide, her own thumb),
# MECH-03 (every step — keeps its confirmed image), MECH-03d (seventeen times)
row("MECH-03a","Act 1",["B-03"],"MECH","anatomy","—","MECH","ANAT-A front view: the kneecap, and a thumb's width below it one small spot on the tendon lights","one push in, 2s",
    "RV render","none","no","eye","front","CU","clean","front = where it is on your own knee","deep","deep","L","below",layout=PIP,eg="EG07")
row("BR-03b","Act 1",["B-03"],"BR","P hand","L-P-FRONT","P-D1","her thumb laid flat across the band under her LEFT kneecap, as wide as it","one lay-down, 2s",
    "sway","hands","no","eye","three-quarter","ECU","clean","eye + three-quarter = the band's width against her own thumb","medium","hands","L","thumb",layout=PIP)
row("MECH-03","Act 1",["B-03"],"MECH","anatomy","—","MECH","ANAT-A: the patellar tendon below the kneecap lights red as one band, one step lands on it","one step, 3s",
    "RV render","none","no","eye","profile","CU","clean","profile = the band's side view under the kneecap","deep","deep","L","tendon",layout=SPL,eg="EG07")
row("MECH-03d","Act 1",["B-03"],"MECH","anatomy","—","MECH","ANAT-A load: the body's whole weight pressed down the bent leg into the band, the band blazing near-white","one press of load, 2s",
    "RV render","none","no","low","three-quarter","MEDIUM","clean","low = the weight bearing down on it","deep","deep","L","Seventeen",layout=SPL,eg="EG07 · 17× card")
row("BR-04","Act 1",["B-04"],"BR","P hand","L-P-FRONT","P-D1","her forefinger presses into the soft spot just under her LEFT kneecap, the skirt hem lifted clear of the knee","one press, 2s",
    "sway","hands","no","high","front","ECU","clean","high = the viewer's own look down at their knee","medium","hands","L","press",layout=PIP,eg="EG06 red arrow")
# the user, 2026-09-29 (video Fix on BR-05a): "this should be 2 brolls" → BR-05 carries "Coming down is worse than going up."; BR-05a keeps its image for the rest
row("BR-05","Act 1",["B-05"],"BR","P","L-P-HALL","P-D1","at the top of the flight she stops and looks down it, both hands on the banister, and hesitates","one held breath, 2s",
    "sway","stairs at the top (§27G: no step taken, hands on the rail)","no","high","three-quarter-back","FULL","clean",
    "high + behind her = the drop she has to take","deep","deep","R","worse",layout=CUT)
row("BR-05a","Act 1",["B-05"],"BR","P","L-P-HALL","P-D1","climbs one stair away from camera, steady, hand on the banister","one step, 2s",
    "sway","stairs ascending (§27G: one step)","no","eye","behind","FULL","clean","behind = going up is the easy way, she leaves us","deep","deep","R","up",layout=CUT)
row("BR-05b","Act 1",["B-05"],"BR","P","L-P-HALL","P-D1","comes down one stair, both hands on the banister, the LEFT knee braced as it catches","one step, 2s",
    "locked-off sway","stairs descending (§27G: camera at the foot, hand on rail)","no","low","three-quarter","FULL","clean",
    "low = the stair looms; coming down is the hard way","deep","deep","R","Coming",layout=CUT,face=True)
# the user, 2026-09-29 (video Fix on MECH-05): "new image and mechanism here" → close on the knee as the foot lands on the step: the catch drives down through
# the kneecap into the band, which flares at the landing (was: the whole leg, the flash hard to read)
row("MECH-05","Act 1",["B-05"],"MECH","anatomy","—","MECH","ANAT-A step-down, close: the foot lands on the step, the knee bends to catch, the band under the kneecap flares at the landing","one catch, 3s",
    "RV render","none","no","low","three-quarter","CU","clean","low + close = the catch arriving on the band","deep","deep","L","catch",layout=SPL,eg="EG07")

# ---- ACT 2 — that is why ×3, the list, never / never / always (B-06–B-10) ------------------------------------
TH("TH-A2", "Act 2", ["B-06","B-07","B-08","B-09","B-10"], "quieter on the list; slower and lower on 'where the load was landing' (stress register)")
row("BR-06","Act 2",["B-06"],"BR","P","L-P-HALL","P-D1","comes down her stairs BACKWARDS, facing the steps, both hands on the banister","one step back, 3s",
    "locked-off sway","stairs descending backwards (§27G: one step, both hands on rail, camera at the foot)","no","eye","profile","FULL","clean",
    "profile = backwards only reads side-on; the flight above and below her","deep","deep","R","backwards",layout=CUT)
# the user, 2026-09-30 (image Fix on BR-06 v5): "fix this distorted image" → side-on from the hall, one plain straight flight, her mid-flight facing the steps
row("BR-07","Act 2",["B-07"],"BR","P","L-P-FRONT","P-D1","rocks forward in the low fireside armchair, hands on the wooden arms, to stand — the first try, sinks back","one rock, 3s",
    "sway","sit-to-stand (§27G: one action, hands on the arms)","no","eye","profile","MEDIUM","clean","profile = the effort side-on","medium","eyes","L","chair",layout=CUT,face=True)
row("BR-08","Act 2",["B-08"],"BR","P legs","L-P-HALL","P-D1","steps up onto the bottom stair RIGHT leg first, the left trailing","one step, 2s",
    "locked-off sway","stairs ascending (§27G: one step)","no","ground","three-quarter","CU","clean","ground = the leg she leads with","deep","deep","R","good",layout=CUT)
row("BR-09a","Act 2",["B-09"],"BR","object","L-P-HALL","P-D1","the brown walking boots on the newspaper by the door, laces dusty","still, 2s",
    "slow sway","none","no","low","front","CU","clean","low = the boots, left waiting","medium","foreground","L","walk",layout=PIP)
row("BR-09b","Act 2",["B-09"],"BR","P","L-P-KITCH","P-D1","at the sink, looks out at the overgrown garden, a mug in her hand","one look up, 2s",
    "sway","standing","no","eye","three-quarter-back","MEDIUM","through","three-quarter-back + through = the garden past her, out of reach","background","deep","back","garden",
    layout=CUT)
row("BR-09c","Act 2",["B-09"],"BR","family (one-offs FM-01 daughter, FM-02 grandson) + P","L-P-DOOR","P-D1","P opens her front door to her daughter and grandson on the step","the door opens, 2s",
    "sway","standing (§27G: no step)","no","eye","ots","MEDIUM","clean","OTS = from inside, the family comes to her","medium","eyes","L","family",layout=CUT,face=True)
row("BR-10","Act 2",["B-10"],"BR","P","L-P-FRONT","P-D1","seated in the armchair, pulls a blank physio band against her foot, carefully","one pull, 3s",
    "sway","sitting · hands","no","high","three-quarter","MEDIUM","clean","high = how hard she tried","medium","hands","L","tried",layout=CUT)
# the user, 2026-09-29 (video Fix on BR-10): "this should be 3 separate brolls" → B-10 split: BR-10 (how hard she tried — keeps its image),
# BR-10b (never a weak muscle — her hand on her thigh as the muscle tightens hard), BR-10c (where the load was landing — the knee as the foot lands a step down)
row("BR-10b","Act 2",["B-10"],"BR","P legs","L-P-FRONT","P-D1","her leg straight, the heel resting on a footstool, her hand flat on her thigh as the thigh muscle tightens hard under it","one squeeze, 2s",
    "sway","sitting · hands","no","low","profile","CU","clean","low + profile = the strong muscle's shape","medium","hands","L","muscle",layout=CUT)
# the user, 2026-09-30 (video Fix on BR-10c): "make this anatomy" → ANAT render: the load running down the leg and landing on the band as the foot lands
row("BR-10c","Act 2",["B-10"],"MECH","anatomy","—","MECH","ANAT-A: as the foot lands a step down, the load runs down the thigh and lands on the patellar tendon, which lights red","one landing, 2s",
    "RV render","none","no","low","three-quarter","CU","clean","low = where the weight lands, looking up the leg","deep","deep","L","landing",layout=CUT,eg="EG06 red arrow")

# ---- ACT 3 — the failed fixes, Stryde, placement (B-11–B-15) --------------------------------------------------
TH("TH-A3", "Act 3", ["B-11","B-12","B-13","B-14","B-15"], "counts the three on his fingers; lifts the strap from the desk into frame on 'This does'")
row("BR-11a","Act 3",["B-11"],"BR","object","L-P-KITCH","P-D2","a black stretchy knee sleeve squeezed flat in a hand (blank, no brand)","one squeeze, 2s",
    "sway","hands","no","eye","front","CU","clean","","medium","hands","R","sleeve",layout=PIP,eg="EG06 crossed-out list")
row("BR-11b","Act 3",["B-11"],"BR","object","L-P-KITCH","P-D2","a grey hinged knee brace flexes on the table — the hinge swings side to side (blank)","one tilt, 2s",
    "sway","hands","no","low","profile","CU","clean","low + profile = the hinge's sideways travel","medium","foreground","R","hinged",layout=PIP,eg="EG06 crossed-out list")
row("BR-11c","Act 3",["B-11"],"BR","P hand","L-P-KITCH","P-D2","rubs white gel from a plain unlabelled tube onto her knee skin","one rub, 2s",
    "sway","hands","no","high","three-quarter","CU","clean","high = sits on the skin, from above","medium","hands","R","gel",layout=PIP,eg="EG06 crossed-out list")
row("PR-12","Act 3",["B-12"],"PRODUCT","P hand","L-P-KITCH","P-D2","holds the strap up in the window light, pinched at the shell's bottom edge (HELD)","a quarter turn, 2s",
    "sway","hands","yes — product turns","eye","front","CU","clean","","medium","product","R","Stryde",product="held (HELD_GRIPS) · first appearance",layout=FULL,model="NBP")
row("BR-13","Act 3",["B-13"],"BR","P","L-P-FRONT","P-D2","sits on the armchair edge, LEFT leg straight, strap seated under the kneecap","still, one breath, 2s",
    "sway","sitting","no","eye","three-quarter","CU","clean","","medium","product","L","below",product="worn · VISIBLE (W-L-FRONT)",layout=SPL,model="NBP")
# MECH-14 — the user, 2026-09-29: "no need an anatomy here you can just show the inside  also this should not be 1 broll that script line is way too
# loing for 1 broll only" → MECH-14 keeps its id (version history) but becomes the product close-up of the pad's inside; BR-14b carries the second sentence.
row("MECH-14","Act 3",["B-14"],"PRODUCT","P hand","L-P-FRONT","P-D2","turns the strap over in her hand: the grey ridged silicone pad inside, its smooth central bar","a slow half turn, 2s",
    "sway","hands","yes — product turns","high","three-quarter","CU","clean","high = looking down into her palm at the pad","medium","product","L","pad",product="held, back of the shell (PAD_BACK_SHOT, the user's pad photo)",layout=SPL,model="NBP")
# the user, 2026-09-30 (video Fix on BR-14b): "use anatomy here" → ANAT render with the strap on: the load comes down, is caught by the pad and turned off
# the band into the shell before it reaches the joint
row("BR-14b","Act 3",["B-14"],"MECH","anatomy + strap","—","MECH","ANAT-A + product: the load comes down the leg, meets the pad over the tendon and is turned off into the shell; the joint below stays calm","one landing, 2s",
    "RV render","none","no","eye","three-quarter","CU","clean","three-quarter = the strap and the tendon under it both read","deep","deep","L","caught",
    product="worn · VISIBLE (on the anatomical model)",model="NBP")
# the user, 2026-09-29 (image Fix on BR-15): "generate a new image for this different concept" → her own knee, the strap on it, her fingertip resting on the
# notch where it meets the kneecap's lower edge: the placement checked on her, not on a desk model (was: the doctor's finger on a knee model)
row("BR-15","Act 3",["B-15"],"BR","P hand","L-P-FRONT","P-D2","her fingertip rests on the strap's notch where it meets the lower edge of her kneecap — right on the tendon, not a centimetre higher","one light touch, 2s",
    "sway","sitting · hands","no","high","three-quarter","ECU","clean","high = her own look down at the placement","medium","hands","L","placement",
    product="worn · VISIBLE",layout=PIP)

# ---- ACT 4 — proof, ten seconds, the doctor's word, the test, the scan (B-16–B-20) ------------------------------
TH("TH-A4", "Act 4", ["B-16","B-17","B-18","B-19","B-20"], "hands flat on the desk on 'I do not sell these'; eyebrows up on 'You will know in a minute'")
# the user, 2026-09-30 (video Fix on BR-16a): "this should be 2 brolls make an over all new ones" → BR-16a (measured: a gait lab) + BR-16a2 (the surgeons)
# the user, 2026-09-30 (video Fix on BR-16a v2): "show it in a like treadmill" → the volunteer walks on a lab treadmill, the load curve on the monitor
row("BR-16a","Act 4",["B-16"],"BR","volunteer (one-off LV-01)","L-LAB","X-D1","in a gait lab, a volunteer wearing the strap walks steadily on a treadmill, a load curve on the monitor beside him","walking on the spot, 3s",
    "locked-off sway","treadmill walk (§27G: he stays in place on the belt, camera side-on, never travels)","no","low","profile","MEDIUM","clean","low + profile = the measured step, side-on","medium","product","L","Measured",
    product="worn · VISIBLE",model="NBP",layout=PIP,eg="EG06 34% card")
row("BR-16a2","Act 4",["B-16"],"BR","surgeons (one-offs SG-01, SG-02, §19B approachable) + patient (one-off PT-01)","L-ORTHO","X-D1","an orthopaedic surgeon fits the strap below a patient's kneecap on the examination couch while a second surgeon watches","one slide up, 2s",
    "sway","hands · seating (SEAT_LOCK: only ever up)","yes — ends seated","eye","three-quarter","MEDIUM","clean","three-quarter = the two surgeons and the knee in one frame","medium","hands","R","orthopedic",
    product="seated · VISIBLE",model="NBP",layout=FULL,face=True)
# the user, 2026-09-30 (video Fix on BR-16b): "i need new image here" → a walking group coming towards us in a park, faces and knees, straps on several knees
row("BR-16b","Act 4",["B-16"],"BR","walkers (one-offs WK-01)","L-PARK","X-D1","a walking group of older people comes along a park path towards us, the slim strap on several knees","they walk towards us, 3s",
    "locked-off","walking at camera (§27G: camera never travels, they stop short of it)","no","low","front","WIDE","clean","low + front = the many, coming our way","deep","deep","L","Two",
    product="worn · VISIBLE",model="NBP",layout=CUT,eg="EG06 200,000 card")
row("BR-17a","Act 4",["B-17"],"BR","P","L-P-HALL","P-D2","sitting on the bottom stair, seats the strap on her LEFT knee in one slide up (SEAT_LOCK)","one slide up, 2s",
    "sway","seating (SEAT_LOCK: only ever up)","yes — ends seated","high","three-quarter","CU","clean","high = quick and easy","medium","product","R","Ten",
    product="seated · VISIBLE",model="NBP",layout=SPL,ledger="F6")
# the user, 2026-09-30 (video Fix on BR-17b): "new image productive broll but with the pants down not showing the strap" → out doing her shopping at the
# greengrocer's, the trouser legs down to her shoes, nothing showing at the knee
row("BR-17b","Act 4",["B-17"],"BR","P","L-SHOP","P-D2","out at the greengrocer's, choosing apples into a paper bag, the wide denim trouser legs down to her trainers, nothing showing at the knee","one reach, 2s",
    "sway","standing (§27G: one reach, no step)","no","eye","three-quarter","FULL","clean","three-quarter + full = out in the world, the whole leg line smooth","medium","subject","R","nobody",
    product="worn · CONCEALED under trousers (§9D)",model="NBP",layout=SPL,ledger="F6",face=True)
# the user, 2026-09-30 (video Fix on BR-19a): "should be going down the stairs no breathing and she should not touch the hand rail"
row("BR-19a","Act 4",["B-19"],"BR","P","L-P-HALL","P-D2","sets off down the stairs forwards from the top, strap on the LEFT knee, the right bare, hands free of the rail","two steps, 2s",
    "sway","stairs descending (§27G: camera below her on the flight, hands free, never on the rail)","no","high","front","MEDIUM","clean","high = the drop of the stairs below her","medium","product","R","One",
    product="worn · VISIBLE, one knee only",model="NBP",layout=CUT,ledger="F4")
row("BR-19b","Act 4",["B-19"],"BR","P","L-P-HALL","P-D2","comes down the stairs forwards, one step at a time, hand light on the banister","two steps, 3s",
    "locked-off sway","stairs descending (§27G: camera at the foot, hand on rail)","no","low","front","FULL","clean",
    "low = the mirror of BR-05b, now easy","deep","deep","R","forwards",product="worn · VISIBLE",model="NBP",layout=FULL,face=True,ledger="F4")
# the user, 2026-09-30 (video Fix on BR-20): "i want new images here this should be 3 brolls" → BR-20 (the arthritis still there), BR-20b (the two scans,
# identical), BR-20c (the load no longer landing on the band — anatomy with the strap)
row("BR-20","Act 4",["B-20"],"BR","D hand","L-D-CONS","D-D1","her knee X-ray held to the window, his fingertip tracing the narrowed joint gap on the inner side","one trace, 2s",
    "sway","hands","no","eye","front","CU","clean","front = read the scan straight on","medium","hands","back","arthritis",layout=SPL,ledger="F3")
row("BR-20b","Act 4",["B-20"],"BR","D hands","L-D-CONS","D-D1","the two knee X-rays laid side by side on his desk, March and now, identical; his hands square them up","one small push, 2s",
    "sway","hands","no","overhead","front","CU","clean","overhead = the two side by side, the same","medium","foreground","L","both",layout=CUT,ledger="F3")
row("BR-20c","Act 4",["B-20"],"MECH","anatomy + strap","—","MECH","ANAT-A + product: a step lands with the strap on, the tendon stays cool and unlit, the pad holding it","one landing, 2s",
    "RV render","none","no","low","profile","CU","clean","low + profile = the same view as the red band, now calm","deep","deep","L","band",
    product="worn · VISIBLE (on the anatomical model)",model="NBP",layout=FULL)

# ---- ACT 5 — the reframe, the offer, the close (B-21–B-23) ------------------------------------------------------
TH("TH-A5", "Act 5", ["B-21","B-22","B-23"], "slow and certain on 'move the load'; the last line straight to lens, a small nod")
row("PR-22a","Act 5",["B-22"],"PRODUCT","object","L-P-KITCH","P-D2","the open box on the kitchen table: two straps side by side in the insert (package_open)","still; a hand settles the lid, 2s",
    "sway","none","no","overhead","front","CU","clean","overhead = what's in the box","medium","product","R","Two",product="box open, two units (OFFER)",
    model="GPT Sunburst",layout=PIP)
# the user, 2026-09-29: "this should be 2 brolls the 2 strap is done but the 60 days need one too and the from stryde is th[e site]" → three B-rolls on B-22's first half
# the user, 2026-09-29 (Fix): "brolls of showing the results of using the strap" → the result, not the object: her, weeks on, going out again
row("BR-22a2","Act 5",["B-22"],"BR","P","L-P-DOOR","P-D2","weeks on, going out again: she steps down her front step onto the path, shopping bag on her arm, the strapped LEFT leg straight","one step down, 2s",
    "sway","front step descending (§27G: camera on the path, no rail, hands free)","no","hip","three-quarter","FULL","clean",
    "hip + three-quarter = the result: out of the house, the knee doing the step","medium","subject","L","Sixty",product="worn · VISIBLE",model="NBP",layout=PIP,face=True,eg="EG06 60-day seal")
row("BR-22a3","Act 5",["B-22"],"PRODUCT","P hand","L-P-KITCH","P-D2","her phone in her hand on the Stryde site: the strap's product photo on screen (real site screen added in the edit)","one thumb scroll, 2s",
    "sway","hands","no","high","three-quarter","CU","clean","high = over her shoulder onto the screen","medium","hands","R","site",product="on screen (the edit overlays the real site)",model="NBP",layout=PIP,eg="EG06 site URL")
# the user, 2026-09-29 (Fix): "show the cheap COPIES" → the copies themselves, stretched, on the kitchen table
row("BR-22b","Act 5",["B-22"],"PRODUCT","object (near-copies)","L-P-KITCH","P-D2","three cheap copy straps tipped out of a plastic bag on the kitchen table, their bands stretched long and limp","still; one limp band slides off the edge, 2s",
    "sway","none; blank near-copies (FAKE_BASE)","no","high","three-quarter","CU","clean","high = looking down on what she gave up on","medium","product","R","stretch",
    product="near-copy (FAKE_BASE)",model="NBP",layout=PIP,ledger="F7")
# the user, 2026-09-30 (video Fix on BR-23): "she should be going up normally she is not touching the hand rail" → she goes UP her stairs, hands free
row("BR-23","Act 5",["B-23"],"BR","P","L-P-HALL","P-D2","goes up her stairs at a normal pace, hands free and off the rail, a small smile, strap on the LEFT knee","two steps, 3s",
    "locked-off sway","stairs ascending (§27G: camera on the landing, she climbs towards it and stops short, hands free)","no","high","front","FULL","clean",
    "high + front = from the landing, she climbs towards us: she owns the stairs","deep","deep","R","stairs",product="worn · VISIBLE",model="NBP",layout=FULL,face=True)

def angles_row(r):
    d, t, arc, k = DAY[r["day"]]
    return dict(beat=r["beat"], group=r["act"], type=("SHOT" if r["type"] == "PRODUCT" else ("BR" if r["type"] == "MECH" else r["type"])),
        subject=r["subject"], height=r["height"], side=r["side"], scale=r["scale"], fg=r["fg"], why=r["why"], mode=1,
        product_beat=r["plane"] == "product", face=r["face"],
        focus=dict(plane=r["plane"], dof=r["dof"], rack=None, moving_subject="at camera" in r["staging"]),
        story_day=d, light=dict(source=LOC[r["loc"]]["src"], key_side=r["key_side"], time=t, arc=arc, kelvin=k,
            why="backlit by the window: the scan / the garden is the subject, the face is not speaking" if r["key_side"] == "back" else ""))
(HERE / "angles_rows.json").write_text(json.dumps([angles_row(r) for r in R], indent=1))
for r in R: r["line"] = " ".join(PH.get(p, "?") for p in r["phrases"])
# Where several B-rolls share one phrase, each card carries only the words it covers (the user, 2026-09-29: "fix the script line cause its not
# showing the script line for that broll only"). Verbatim spans, in order; together they rebuild the whole phrase (asserted below).
BLINE = {
 "BR-01": "A patient of mine. Nine years of knee pain.", "MECH-01": "Bone on bone on the left, the right one following it.",
 "MECH-03a": "Two centimetres below your kneecap", "BR-03b": "there is a band of tendon about as wide as your thumb.",
 "MECH-03": "Every step you take lands on it.", "MECH-03d": "Seventeen times your bodyweight.",
 "BR-05": "Coming down is worse than going up.", "BR-05a": "Going up, your muscles lift you.", "BR-05b": "Coming down, you are catching yourself,",
 "MECH-05": "and the catch lands on that band.",
 "BR-10": "It was never how hard she tried.", "BR-10b": "It was never a weak muscle.", "BR-10c": "It was where the load was landing.",
 "BR-09a": "And the list of things she said no to got longer every year. The long walk.", "BR-09b": "The garden.", "BR-09c": "Her family coming to her instead.",
 "BR-11a": "A sleeve squeezes the whole knee.", "BR-11b": "A hinged brace stops it going sideways, and her knee was never going sideways.",
 "BR-11c": "A gel sits on the skin. None of them move the load.",
 "BR-16a": "Thirty four percent less strain. Measured.", "BR-16a2": "Three years with orthopedic surgeons.", "BR-16b": "Two hundred thousand people wearing one.",
 "BR-17a": "Ten seconds to put on. No sores, no rolling down,", "BR-17b": "and nobody can see it.",
 "BR-19a": "You do not have to take my word for it. One knee only. Leave the other bare.", "BR-19b": "Go to your own stairs and come down forwards. You will know in a minute.",
 "PR-22a": "Two for one, so you do both knees, which is what she needed.", "BR-22a2": "Sixty days, and you keep the straps.", "BR-22a3": "From the Stryde site.",
 "MECH-14": "A silicone pad inside holds pressure on that one band instead of spreading it round the whole knee.",
 "BR-14b": "The weight gets caught and moved off the worn part before it reaches the joint.",
 "BR-22b": "The copies stretch, and a stretched strap stops holding the spot.",
 "BR-20": "Not because the arthritis has gone.",
 "BR-20b": "Her scan looks exactly the same as it did in March. I have both of them.", "BR-20c": "Because the load is not landing on that band any more.",
}
for r in R:
    if r["beat"] in BLINE:
        r["phrase_line"] = r["line"]; assert BLINE[r["beat"]] in r["line"], r["beat"]; r["line"] = BLINE[r["beat"]]
_groups = {}
for r in R:
    if r["beat"] in BLINE and r["type"] != "TH": _groups.setdefault(r["phrases"][0], []).append(r)
for ph, rs in _groups.items():
    assert " ".join(x["line"] for x in rs) == rs[0]["phrase_line"], ("spans do not rebuild", ph)
(HERE / "actmap.json").write_text(json.dumps(R, indent=1, ensure_ascii=False))
# markdown tables per act
cols = "| Beat | Phrase | Type | Subject | Location | Day | Action · pace | Camera · staging · pin | Angle (height · side · scale · fg) — why | Focus | Light key | Key word | Product | Layout · EG | Model | Ledger |"
md, cur = [], None
for r in R:
    if r["act"] != cur:
        cur = r["act"]; md += ["", f"#### {cur}", "", cols, "|" + "---|" * 16]
    ang = f'{r["height"]} · {r["side"]} · {r["scale"]} · {r["fg"]}' + (f' — {r["why"]}' if r["why"] else "")
    k = DAY[r["day"]][3]
    md.append(f'| {r["beat"]} | {", ".join(r["phrases"])} | {r["type"]} | {r["subject"]} | {r["loc"]} | {r["day"]} | {r["action"]} · {r["pace"]} | '
              f'{r["camera"]} · {r["staging"]} · {r["pin_end"]} | {ang} | {r["plane"]}, {r["dof"]} | {r["key_side"]} · {k}K | {r["key"]} | {r["product"]} | {r["layout"]} | {r["model"]} | {r["ledger"]} |')
(HERE / "actmap_tables.md").write_text("\n".join(md).strip() + "\n")
missing = [p for r in R for p in r["phrases"] if p not in PH]
print(len(R), "rows;", sum(r["type"] == "TH" for r in R), "TH;", sum(r["type"] == "MECH" for r in R), "MECH; missing phrases:", missing)
