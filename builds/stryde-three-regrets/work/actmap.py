#!/usr/bin/env python3
"""Step-5 act map for stryde-three-regrets (E4, §27G, §30I–§30K), one row per beat.

Writes work/angles_rows.json (for angles.py), work/actmap.json (full rows) and ACTMAP.md.
Fields per row, condensed from E4:
  beat act phrases type subject loc day event action pace camera staging pin_end
  h side scale fg why focus(dof, plane) key product layout model ledger face
"""
import json, re, pathlib
HERE = pathlib.Path(__file__).resolve().parent
LINES = {}
body = (HERE / "hooks_body.txt").read_text().split("BODY:\n")[1].strip().split("\n")
i = 0
for l in body:
    for s in re.split(r"(?<=[.?!])\s+", l):
        i += 1; LINES[f"P-{i:03d}"] = s
for l in (HERE / "hooks_body.txt").read_text().split("BODY:")[0].strip().split("\n"):
    k, v = l.split(": ", 1); LINES[k] = v

# ---- locations: light plan in room terms (§30K) ---------------------------------------------
LOC = {
 "L-G-BED":   dict(plate="P1-G-BEDROOM", tier="PLATED", src="bedroom window, south wall"),
 "L-G-HALL":  dict(plate="P0-PROP-G", tier="TRAVERSED", src="front-door glass (south) + landing window"),
 "L-G-OUT":   dict(plate="P0-PROP-G (exterior: the pebble-dash front)", tier="INCIDENTAL", src="midday sun, south"),
 "L-N-WORK":  dict(plate="P2-N-WORKROOM", tier="PLATED", src="sash window, east wall"),
 "L-K-STOP":  dict(plate="P3-K-BUSSTOP", tier="PLATED", src="overcast sky, brighter to the south"),
 "L-J-LOUNGE":dict(plate="P4-J-LOUNGE", tier="PLATED", src="lounge window, west wall, net curtains"),
 "L-J-STEPS": dict(plate="P5-J-STEPS", tier="PLATED", src="open sky over the street"),
 "L-CONSULT": dict(plate="P6-CONSULT", tier="PLATED", src="consulting-room window, right-hand wall"),
 "L-TOWPATH":dict(plate="—", tier="INCIDENTAL", src="afternoon sun over the canal"),
 "L-TABLE":   dict(plate="—", tier="INCIDENTAL", src="kitchen window, side light"),
 "—":         dict(plate="—", tier="—", src="§12A render light"),
}
# story days: int for angles.py, time and act light state
DAY = {
 "G-D1": (1, "morning", "problem: grey late-morning light, flat and cool"),
 "G-D2": (2, "midday", "after: sun in the room, warmer and open"),
 "K-D1": (3, "morning", "problem: overcast, cool"),
 "K-D2": (4, "afternoon", "after: bright broken cloud, warmer"),
 "J-D1": (5, "afternoon", "problem: grey afternoon through net curtains"),
 "J-D2": (6, "afternoon", "after: low warm sun on the street"),
 "N-D1": (7, "morning", "everyday: soft east morning light"),
 "X-D1": (8, "midday", "everyday: neutral daylight"),
 "MECH": (None, "midday", "§12A anatomical register"),
}

R = []
def row(beat, act, phrases, typ, subject, loc, day, event, action, pace, camera, staging, pin_end,
        h, side, scale, fg, why, dof, plane, key_side, key, product="absent", layout="full · EG02",
        model="NB2", ledger="—", face=False, eg=""):
    R.append(dict(beat=beat, act=act, phrases=phrases, type=typ, subject=subject, loc=loc, day=day, event=event,
                  action=action, pace=pace, camera=camera, staging=staging, pin_end=pin_end,
                  height=h, side=side, scale=scale, fg=fg, why=why, dof=dof, plane=plane, key_side=key_side,
                  key=key, product=product, layout=layout, model=model, ledger=ledger, face=face))

TH = lambda beat, act, phrases, note: R.append(dict(beat=beat, act=act, phrases=phrases, type="TH", subject="N",
    loc="L-N-WORK", day="N-D1", event="E-N1", action=note, pace="~185 wpm", camera="R3 compressed, propped",
    staging="none", pin_end="no", height="eye", side="three-quarter", scale="MCU", fg="clean", why="",
    dof="medium", plane="eyes", key_side="L", key="", product="absent", layout="full · EG05 · EG02", model="HeyGen Avatar V",
    ledger="—", face=True))

# ---- HOOKS (VO over B-roll, VN01: the reference's construction — EG01 banner + EG02 captions) ----
H = "full · EG01 banner · EG02"
row("HK1-01","Hook 1",["HK1"],"BR","R1 Gail","L-G-BED","G-D1","E-G1","sits on the bed edge, both hands cupping her right knee, a slow rock forward","one rock, 3s","sway","sitting (§27G: already seated)","no",
    "eye","three-quarter","MEDIUM","clean","","medium","hands","R","knees",layout=H,face=True)
row("HK1-02","Hook 1",["HK1"],"BR","R2 Ken","L-K-STOP","K-D1","E-K1","steps down off the high kerb, left leg first, right hand on the lamp post","one step, 2s","locked-off sway","kerb step-down (§27G steps: one step, hand on support)","no",
    "ground","three-quarter","FULL","clean","ground = steps and feet: the leg he leads with","deep","deep","L","one",layout=H)
row("HK1-03","Hook 1",["HK1"],"BR","object","L-CONSULT","X-D1","E-C1","the knee X-ray glowing on the viewing screen, the hinged brace on the desk in the foreground","still; the screen's glow only","slow sway","none","no",
    "low","three-quarter","CU","through","through = the doctor's room, seen past the brace","medium","background","R","doctor",layout=H)
row("HK2-01","Hook 2",["HK2"],"BR","N hands","L-N-WORK","N-D1","E-N2","her hands lift a stack of printed letters out of a grey post tray","one lift, 2s","sway","none","no",
    "overhead","front","CU","clean","overhead = routine, the daily postbag","deep","hands","L","written",layout=H)
row("HK2-02","Hook 2",["HK2"],"BR","N","L-N-WORK","N-D1","E-N2","pins one more card onto the full pinboard","one push of a pin, 2s","sway","none","no",
    "eye","three-quarter-back","MEDIUM","clean","three-quarter-back = we read over her shoulder, the board is the subject","medium","background","L","Three",layout=H)
row("HK2-03","Hook 2",["HK2"],"BR","object","L-G-BED","G-D1","E-G1","Gail's overfilled top drawer of knee supports, a strap sliding off the edge","one small slide, 2s","sway","none","no",
    "high","front","CU","clean","high = looking down into the pile","medium","foreground","R","none",layout=H)
row("HK3-01","Hook 3",["HK3"],"BR","object","L-CONSULT","X-D1","E-C1","the knee X-ray on the viewing screen, the couch paper roll in the foreground","still; the screen's glow only","slow sway","none","no",
    "eye","profile","CU","through","profile + through = the clinic at arm's length","medium","background","R","surgery",layout=H)
row("HK3-02","Hook 3",["HK3"],"BR","R2 Ken hands","L-K-STOP","K-D1","E-K1","presses one tablet out of a blank blister strip into his palm, on the perch bench","one press, 2s","sway","hands (§27G: hands whole, one action)","no",
    "high","three-quarter","CU","clean","high = small daily habit","medium","hands","L","painkillers",layout=H)
row("HK3-03","Hook 3",["HK3"],"BR","R3 Joan","L-J-LOUNGE","J-D1","E-J1","in the armchair, looks up from her lap to the carriage clock on the mantel","one look, 2s","sway","sitting","no",
    "eye","three-quarter","MCU","clean","","medium","eyes","L","waiting",layout=H,face=True)
row("HK3-04","Hook 3",["HK3"],"BR","R1 Gail","L-G-BED","G-D1","E-G1","her forefinger presses into the soft spot just under her right kneecap","one press, 2s","sway","hands","no",
    "high","front","ECU","clean","high = her own view down at her knee","medium","hands","R","two",layout=H)

# ---- ACT 1: the witness + Regret 1 (P-001–P-016) --------------------------------------------
TH("TH-01","Act 1",["P-001","P-002"],"at her desk by the post trays, a printed letter in one hand; Economical gesture")
row("BR-003","Act 1",["P-003"],"BR","R1 Gail","L-G-BED","G-D1","E-G2","pulls the top drawer of the chest open; it sticks, then gives","one pull, 2s","sway","none","no",
    "eye","three-quarter-back","MEDIUM","clean","three-quarter-back = over her shoulder into the drawer","medium","hands","R","Regret",layout="full · EG03 'Regret No. 1' · EG02")
row("BR-004","Act 1",["P-004"],"BR","R1 Gail","L-G-BED","G-D1","E-G2","sits on the bed edge rubbing the outside of her right knee, frowning at it","slow rubs, 3s","sway","sitting","no",
    "high","three-quarter","MCU","clean","high = small against the problem","medium","eyes","R","coming",face=True)
row("BR-005","Act 1",["P-005"],"BR","R1 Gail","L-G-BED","G-D1","E-G2","both hands pull a black stretchy sleeve up over her right knee","one pull, 3s","sway","hands; the sleeve is a blank near-copy, never our product","no",
    "eye","profile","CU","clean","profile = the sleeve's shape over the joint","medium","hands","R","sleeve")
row("BR-006","Act 1",["P-006"],"BR","R1 Gail","L-G-BED","G-D1","E-G2","fastens the strap of a grey hinged brace with metal side bars","one fasten, 2s","sway","hands; blank brace","no",
    "low","three-quarter","CU","clean","low = the bars, big and heavy","medium","hands","R","metal")
row("BR-007","Act 1",["P-007"],"BR","R1 Gail hands","L-G-BED","G-D1","E-G2","drops a beige wrap and a blue gel pad onto the pile in the drawer","one drop, 2s","sway","none","no",
    "overhead","front","CU","clean","overhead = the pile growing","medium","foreground","R","wrap")
row("BR-008","Act 1",["P-008"],"BR","R1 Gail","L-G-BED","G-D1","E-G2","looks at the drawer, a small tired shrug","one shrug, 2s","sway","none","no",
    "eye","three-quarter","MCU","clean","","medium","eyes","R","",face=True)
row("BR-009","Act 1",["P-009"],"BR","clinician hand (one-off CL-01)","L-CONSULT","X-D1","E-C2","a fingertip traces the joint line on the knee X-ray","one trace, 2s","sway","hands","no",
    "eye","front","CU","clean","","medium","background","R","scan")
row("MECH-010","Act 1",["P-010"],"MECH","anatomy","—","MECH","—","ANAT-A: the patellar tendon below the kneecap lights as the band, one walking step lands on it","one step, 3s","RV render","none","no",
    "eye","profile","CU","clean","profile = the band's side view under the kneecap","deep","deep","L","band")
row("MECH-011","Act 1",["P-011"],"MECH","anatomy","—","MECH","—","ANAT-A load: heel strike, the load arrives at the one point","one strike, 2s","RV-FAST","none","no",
    "low","three-quarter","MCU","clean","low = the force, heavy","deep","deep","L","Seventeen",layout="full · EG02 · 17× overlay")
row("BR-012","Act 1",["P-012"],"BR","R1 Gail","L-G-BED","G-D1","E-G2","presses her forefinger under her right kneecap and winces slightly","one press, 2s","sway","hands","no",
    "high","three-quarter","ECU","clean","high = the viewer's own look down at their knee","medium","hands","R","finger")
row("MECH-013","Act 1",["P-013"],"MECH","anatomy","—","MECH","—","ANAT-A + ANAT_A_POINT_TIGHT: one tight spot on the tendon","a pulse, 2s","RV render","none","no",
    "eye","front","ECU","clean","","deep","deep","L","band")
row("MECH-014","Act 1",["P-014"],"MECH","anatomy","—","MECH","—","ANAT-A: a sleeve's squeeze spreads round the whole joint; the band under the kneecap stays loaded","one squeeze, 3s","RV-DRIFT","none","no",
    "high","three-quarter","MCU","clean","high = the whole knee wrapped, seen from above","deep","deep","L","sleeve")
row("BR-015","Act 1",["P-015"],"BR","clinician hand (one-off CL-01)","L-CONSULT","X-D1","E-C2","tilts the hinged brace on the desk from side to side","one tilt, 2s","sway","hands; blank brace","no",
    "low","profile","CU","clean","low + profile = the hinge's sideways travel","medium","hands","R","hinged")
row("BR-016","Act 1",["P-016"],"BR","R1 Gail","L-G-BED","G-D1","E-G2","pushes the overfilled drawer; it will not shut","one push, 2s","sway","none","no",
    "eye","behind","MEDIUM","clean","behind = alone with it","medium","hands","R","drawer")

# ---- ACT 2: Regret 2 (P-017–P-023) -----------------------------------------------------------
row("BR-017","Act 2",["P-017"],"BR","R2 Ken","L-K-STOP","K-D1","E-K2","stands at the bus shelter, weight shifts onto his left leg","one shift, 2s","sway","standing","no",
    "eye","three-quarter","FULL","clean","","deep","deep","L","Regret",layout="full · EG03 'Regret No. 2' · EG02",face=True)
row("BR-018","Act 2",["P-018"],"BR","R2 Ken","L-K-STOP","K-D1","E-K2","his knees: the left straight and loaded, the right slightly bent and off the ground-weight","held stance, a small sway, 2s","sway","standing","no",
    "low","front","CU","clean","low = the legs, the load on one side","medium","foreground","L","bad")
row("BR-019","Act 2",["P-019"],"BR","R2 Ken","L-K-STOP","K-D1","E-K2","glances down the road for the bus, unaware of how he is standing","one glance, 2s","sway","standing","no",
    "eye","profile","MCU","clean","profile = distance, he does not notice","medium","eyes","L","",face=True)
row("BR-020","Act 2",["P-020"],"BR","R2 Ken","L-K-STOP","K-D1","E-K3","steps down off the high kerb onto the zebra crossing, left leg first","one step, 2s","locked-off sway","kerb step-down (§27G steps)","no",
    "ground","front","FULL","clean","ground = the step and the leading foot","deep","deep","L","good")
row("MECH-021","Act 2",["P-021"],"MECH","anatomy","—","MECH","—","ANAT-A both legs, the LEFT knee's band taking a doubled load, the right faint","one step, 3s","RV render","none","no",
    "eye","three-quarter","MCU","clean","","deep","deep","L","work")
row("BR-022","Act 2",["P-022"],"BR","R2 Ken","L-K-STOP","K-D1","E-K3","sits on the red perch bench and rubs his LEFT knee now","one rub, 3s","sway","sitting","no",
    "high","three-quarter","MCU","clean","high = worn down","medium","hands","L","second",face=True)
TH("TH-02","Act 2",["P-023"],"a small shake of the head; one hand turns palm up")

# ---- ACT 3: Regret 3 (P-024–P-030) -----------------------------------------------------------
row("BR-024","Act 3",["P-024"],"BR","R3 Joan","L-J-LOUNGE","J-D1","E-J2","in the pink armchair; the cream phone on the side table rings, she looks at it","one look, 2s","sway","sitting","no",
    "eye","three-quarter","MEDIUM","clean","","medium","eyes","L","Regret",layout="full · EG03 'Regret No. 3' · EG02",face=True)
row("BR-025","Act 3",["P-025"],"BR","R3 Joan","L-J-LOUNGE","J-D1","E-J2","on the phone, a gentle shake of the head, a polite smile","one shake, 3s","sway","sitting","no",
    "eye","profile","MCU","clean","profile = she keeps it to herself","medium","eyes","L","yes",face=True)
row("BR-026","Act 3",["P-026"],"BR","R3 Joan + walkers (one-off WK-01)","L-J-LOUNGE","J-D1","E-J2","through the net curtain, a walking group passes on the path; she watches from the chair","the group crosses frame, 3s","locked-off sway","none","no",
    "eye","three-quarter-back","MEDIUM","through","through = watching life from behind the curtain","deep","background","back","long",face=False)
row("BR-027","Act 3",["P-027"],"BR","R3 Joan hands","L-J-LOUNGE","J-D1","E-J2","puts the phone back on its cradle","one set-down, 2s","sway","hands","no",
    "high","three-quarter","CU","clean","high = the small act of saying no","medium","hands","L","day")
row("BR-028","Act 3",["P-028"],"BR","R3 Joan","L-J-STEPS","J-D1","E-J3","stands at the foot of the seven steps, one hand on the railing, looking up; does not climb","still, one breath, 3s","sway","standing at the foot of steps (§27G: no climb)","no",
    "high","front","FULL","clean","high = small against the steps","deep","deep","L","steps",face=True)
row("BR-029","Act 3",["P-029"],"BR","R3 Joan","L-J-STEPS","J-D1","E-J3","a small covering smile, eyes down","one small smile, 2s","sway","standing","no",
    "eye","three-quarter","CU","clean","","shallow","eyes","L","",face=True)
row("BR-030","Act 3",["P-030"],"BR","daughter + grandson (one-offs DT-01, GS-01) + R3 Joan","L-J-STEPS","J-D1","E-J3","from the top step, the daughter waves; Joan turns away down the pavement","one turn, 3s","sway","walking away (§27G: 3–4 steps)","no",
    "high","ots","MEDIUM","clean","OTS = from the family's side, she leaves","deep","deep","L","people")

# ---- ACT 4: the turn, the mechanism, the product (P-031–P-042) --------------------------------
TH("TH-03","Act 4",["P-031"],"leans in slightly; the turn")
row("BR-032","Act 4",["P-032"],"BR","R1 Gail","L-G-HALL","G-D1","E-G3","comes down one stair, hand on the rail, the right knee braced","one step, 2s","locked-off sway","stairs descending (§27G: one step, hand on rail, camera at the foot)","no",
    "low","front","FULL","clean","low = the stair looms; coming down is the hard way","deep","deep","R","Coming",face=True)
row("BR-033","Act 4",["P-033"],"BR","R1 Gail","L-G-HALL","G-D1","E-G3","climbs one stair away from camera, steady","one step, 2s","sway","stairs ascending (§27G: one step)","no",
    "eye","behind","FULL","clean","behind = going up is easy, she leaves us","deep","deep","L","Going")
row("MECH-034","Act 4",["P-034"],"MECH","anatomy","—","MECH","—","ANAT-A step-down: the front thigh lengthens to catch, the catch lands on the band","one catch, 3s","RV render","none","no",
    "eye","profile","MCU","clean","profile = the step-down's side view","deep","deep","L","catch")
row("BR-035","Act 4",["P-035"],"BR","R1 Gail","L-G-BED","G-D1","E-G4","peels the black sleeve down off her knee","one peel, 2s","sway","hands","no",
    "eye","three-quarter","CU","clean","","medium","hands","R","wrap")
row("MECH-036","Act 4",["P-036"],"MECH","anatomy","—","MECH","—","ANAT-A: attention drops from the joint line to the band below the kneecap","one drift down, 2s","RV-DRIFT","none","no",
    "low","front","CU","clean","low = underneath","deep","deep","L","underneath")
row("PR-037","Act 4",["P-037"],"PRODUCT","R1 Gail hand","L-G-BED","G-D2","E-G5","holds the strap up by the window, pinched at the shell's bottom edge (HELD)","a quarter turn, 2s","sway","hands","yes — product turns",
    "eye","front","CU","clean","","medium","product","R","Stryde",product="held (HELD_GRIPS) · first appearance",model="NBP")
row("BR-038","Act 4",["P-038"],"BR","R1 Gail","L-G-BED","G-D2","E-G5","sits on the bed edge, right leg straight, strap seated under the kneecap","still, one breath, 2s","sway","sitting","no",
    "eye","three-quarter","CU","clean","","medium","product","R","below",product="worn · VISIBLE (worn_front)",model="NBP")
row("BR-039","Act 4",["P-039"],"BR","R1 Gail hands","L-G-BED","G-D2","E-G5","turns the strap over to show the pad inside (PAD_BACK_SHOT)","one turn, 2s","sway","hands","yes — product turns",
    "high","front","CU","clean","high = looking into it","medium","product","R","pad",product="held · the pad",model="NBP")
row("MECH-040","Act 4",["P-040"],"MECH","anatomy","—","MECH","—","ANAT-A relief: the pad catches the force and moves it off the worn part","one catch, 3s","RV render","none","no",
    "low","three-quarter","MCU","clean","low = the catch holds","deep","deep","L","caught")
row("BR-041","Act 4",["P-041"],"BR","R1 Gail","L-G-BED","G-D2","E-G5","both hands slide the closed strap up her shin until it seats (SEAT_LOCK)","one slide up, 3s","sway","seating (Product Sheet SEAT_LOCK: only ever up)","yes — ends seated",
    "eye","profile","CU","clean","profile = the height, the notch meets the kneecap","medium","product","R","placement",product="seated · VISIBLE",model="NBP",ledger="F6")
row("BR-042","Act 4",["P-042"],"BR","R1 Gail","L-G-BED","G-D2","E-G5","a fingertip taps the top edge of the shell where the kneecap sits in the notch","one tap, 2s","sway","hands","no",
    "high","three-quarter","ECU","clean","high = the placement from above","medium","product","R","centimetre",product="worn · VISIBLE",model="NBP",ledger="F6")

# ---- ACT 5: proof + the self-test (P-043–P-056) ----------------------------------------------
row("BR-043","Act 5",["P-043","P-044"],"BR","R1 Gail","L-G-OUT","G-D2","E-G6","walks down her front path towards the gate, trousers rolled, strap on the right knee","3–4 steps, 3s","sway","walking at camera (§27G: 3–4 steps, waist-height phone)","no",
    "low","front","FULL","clean","low = strength in the stride","deep","deep","L","Thirty",product="worn · VISIBLE",model="NBP",layout="full · EG02 · 34% overlay")
row("PR-045","Act 5",["P-045"],"PRODUCT","surgeon (one-off SG-01, §19B approachable)","L-CONSULT","X-D1","E-C3","turns the strap in his hand beside the knee model","one turn, 2s","sway","hands","yes — product turns",
    "eye","three-quarter","MCU","clean","","medium","product","R","orthopedic",product="held",model="NBP",face=True)
row("BR-046","Act 5",["P-046"],"BR","walkers (one-offs WK-02)","L-TOWPATH","X-D1","E-X1","a line of older walkers' legs passes on a towpath, a strap on each near knee","they cross frame, 3s","locked-off","walking across frame","no",
    "ground","profile","MEDIUM","clean","ground = the steps of many","deep","deep","L","Two",product="worn · VISIBLE",model="NBP",layout="full · EG02 · 200,000 overlay")
row("BR-047","Act 5",["P-047"],"BR","R1 Gail","L-G-HALL","G-D2","E-G7","sitting on the bottom stair, seats the strap in one move","one slide up, 2s","sway","seating (SEAT_LOCK)","yes — ends seated",
    "high","three-quarter","CU","clean","high = quick and easy","medium","product","R","Ten",product="seated · VISIBLE",model="NBP",ledger="F3")
row("BR-048","Act 5",["P-048"],"BR","R1 Gail","L-G-HALL","G-D2","E-G7","stands and lets the rolled trouser leg fall; it lies flat over the strap","one drop, 2s","sway","standing","no",
    "low","three-quarter","CU","clean","low = the flat line of the trouser","medium","product","R","nobody",product="worn · REVEAL→CONCEALED (§9D)",model="NBP")
TH("TH-04","Act 5",["P-049"],"eyebrows up, a small open hand toward the lens")
row("BR-050","Act 5",["P-050","P-051"],"BR","R1 Gail","L-G-HALL","G-D2","E-G8","at the top of the stairs, trousers rolled on both legs: strap on the right knee, the left bare","still, a breath, 2s","sway","standing on a landing (§27G: no step)","no",
    "high","front","MEDIUM","clean","high = the drop of the stairs below her","medium","product","R","One",product="worn · VISIBLE, one knee only",model="NBP")
row("BR-052","Act 5",["P-052"],"BR","R1 Gail","L-G-HALL","G-D2","E-G8","comes down the stairs forwards, one step at a time, hand light on the rail","two steps, 3s","locked-off sway","stairs descending (§27G: camera at the foot, hand on rail)","no",
    "low","three-quarter","FULL","clean","low = the mirror of BR-032, now easy","deep","deep","L","come",product="worn · VISIBLE",model="NBP",face=True)
row("BR-053","Act 5",["P-053"],"BR","R1 Gail","L-G-HALL","G-D2","E-G8","at the foot of the stairs she stops and looks back up, a small surprised breath","one look back, 2s","sway","standing","no",
    "eye","three-quarter","MCU","clean","","medium","eyes","R","know",face=True)
TH("TH-05","Act 5",["P-054","P-055"],"quieter and slower (stress register); hands still")
row("MECH-056","Act 5",["P-056"],"MECH","anatomy","—","MECH","—","ANAT-A relief: the site calm, the load carried by the pad","a steady step, 3s","RV render","none","no",
    "eye","profile","MCU","clean","profile = the same side view as MECH-010, now calm","deep","deep","L","weight")

# ---- ACT 6: the close + offer (P-057–P-065) --------------------------------------------------
row("BR-057","Act 6",["P-057"],"BR","N hands","L-N-WORK","N-D1","E-N3","unfolds a printed message on the desk","one unfold, 2s","sway","hands","no",
    "overhead","front","CU","clean","overhead = one of thousands","medium","hands","L","messages")
row("BR-058","Act 6",["P-058"],"BR","N hand","L-N-WORK","N-D1","E-N3","her finger rests under one handwritten line on a card on the pinboard (no readable text)","still, 2s","sway","hands","no",
    "eye","three-quarter","ECU","clean","","shallow","foreground","L","wish")
TH("TH-06","Act 6",["P-059","P-060"],"straight to lens, level; the last TH")
row("PR-061a","Act 6",["P-061"],"PRODUCT","object","L-TABLE","X-D1","E-X2","the open box: two straps side by side in the insert (package_open)","still; a hand settles the lid, 2s","sway","none","no",
    "overhead","front","CU","clean","overhead = what's in the box","medium","product","L","Two",product="box open, two units (OFFER)",model="GPT Sunburst",layout="full · EG02 · offer text in the edit")
row("BR-061b","Act 6",["P-061"],"BR","R2 Ken","L-K-STOP","K-D2","E-K4","stands up briskly from the perch bench, a strap on each knee","one stand, 2s","sway","sit-to-stand (§27G: one action, hands on knees)","no",
    "low","three-quarter","FULL","clean","low = strong again, both legs","deep","deep","L","both",product="worn · two, one per knee",model="NBP",face=True)
row("PR-062","Act 6",["P-062"],"PRODUCT","R2 Ken hands","L-K-STOP","K-D2","E-K4","both straps in his open palm","still, 2s","sway","hands","no",
    "eye","front","CU","clean","","medium","product","L","keep",product="held · two",model="NBP",ledger="F3")
R.append(dict(beat="CARD-063", act="Act 6", phrases=["P-063"], type="CARD", subject="—", loc="—", day="—", event="—",
              action="end card: the Stryde site, made in the edit (§17)", pace="—", camera="—", staging="—", pin_end="—",
              height="—", side="—", scale="—", fg="—", why="", dof="—", plane="—", key_side="—", key="From",
              product="wordmark in the edit", layout="card · EG02", model="CapCut", ledger="—", face=False))
row("BR-064","Act 6",["P-064"],"BR","copy hands (one-off CP-01)","L-TABLE","X-D1","E-X2","a stretched grey near-copy strap sags down a shin","one slow sag, 2s","sway","none; blank near-copy (wide flat nylon webbing archetype)","no",
    "low","profile","CU","clean","low + profile = the sag","medium","foreground","L","stretch",product="near-copy (FAKE_BASE + webbing)",model="NBP",ledger="F5")
row("BR-065","Act 6",["P-065"],"BR","R3 Joan","L-J-STEPS","J-D2","E-J4","comes down her daughter's steps forwards, hand on the railing, a strap on her right knee, smiling","two steps, 3s","locked-off sway","steps descending (§27G: camera at the foot)","no",
    "low","front","FULL","clean","low = the mirror of BR-028's high angle: now she owns the steps","deep","deep","L","stairs",product="worn · VISIBLE",model="NBP",face=True)

R = [r for r in R if r]
# ---- outputs ------------------------------------------------------------------------------------
def angles_row(r):
    d, t, arc = DAY.get(r["day"], (None, "midday", "—"))
    return dict(beat=r["beat"], group=r["act"], type=("SHOT" if r["type"] == "PRODUCT" else ("BR" if r["type"] == "MECH" else r["type"])),
        subject=r["subject"], height=r["height"], side=r["side"], scale=r["scale"], fg=r["fg"], why=r["why"],
        mode=1, product_beat=r["plane"] == "product", face=r["face"],
        focus=dict(plane=r["plane"], dof=r["dof"], rack=None, moving_subject="at camera" in r["staging"]),
        story_day=d, light=dict(source=LOC[r["loc"]]["src"], key_side=r["key_side"], time=t, arc=arc,
            why="backlit through the net curtain: she watches from inside" if r["key_side"] == "back" else ""))
rows = [angles_row(r) for r in R if r["type"] not in ("CARD",)]
(HERE / "angles_rows.json").write_text(json.dumps(rows, indent=1))
for r in R: r["line"] = " ".join(LINES[p] for p in r["phrases"])
(HERE / "actmap.json").write_text(json.dumps(R, indent=1, ensure_ascii=False))
print(len(R), "rows;", sum(r["type"] == "TH" for r in R), "TH;", sum(r["type"] == "MECH" for r in R), "MECH")
