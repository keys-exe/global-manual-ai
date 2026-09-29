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
 "—":         dict(plate="—", tier="—", src="§12A render light"),
}
DAY = {  # story day -> (int, time, act light state, kelvin)
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
row("HK1-02c","Hook 1",["HK1-02"],"BR","P hand","L-P-KITCH","P-D1","from inside the drawer, past the old braces: her hand lifts the STRYDE strap out","one lift, 2s",
    "sway","hands (§27G: one action, HELD_GRIPS bottom-edge pinch)","no","ground","front","CU","through","ground/through = from among the old braces, the one that works",
    "shallow","product","R","drawer",product="held (HELD_GRIPS bottom-edge pinch) · focus on the strap only",layout=CUT,model="NBP")
# ---- HOOK 2 — against his own interest ------------------------------------------------------------------
TH("TH-HK2", "Hook 2", ["HK2-01", "HK2-02"], "leans in a touch on 'before you come and see me'; one flat hand down on the desk on 'not a prescription'")
# §34 2026-09-29 board Fix: "THE TEN SECONDS IT MEANS TEN SECONDS TO PUT ON THE STRYDE STRAP" → seating beat (§9B), product's first appearance
row("HK2-02a","Hook 2",["HK2-02"],"BR","P","L-P-FRONT","P-D1","slides the closed strap up her LEFT shin and seats it under the kneecap (SEAT_LOCK)","one slide, 3s",
    "sway","seated on the chair edge (§27G: one action, both hands on the shell)","yes","low","three-quarter","MEDIUM","clean","low = capable: ten seconds, done",
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
row("MECH-03","Act 1",["B-03"],"MECH","anatomy","—","MECH","ANAT-A: the patellar tendon below the kneecap lights red as one band, one step lands on it","one step, 3s",
    "RV render","none","no","eye","profile","CU","clean","profile = the band's side view under the kneecap","deep","deep","L","tendon",layout=SPL,eg="EG07 · 17× card")
row("BR-04","Act 1",["B-04"],"BR","P hand","L-P-FRONT","P-D1","her forefinger presses into the soft spot just under her LEFT kneecap, the skirt hem lifted clear of the knee","one press, 2s",
    "sway","hands","no","high","front","ECU","clean","high = the viewer's own look down at their knee","medium","hands","L","press",layout=PIP,eg="EG06 red arrow")
row("BR-05a","Act 1",["B-05"],"BR","P","L-P-HALL","P-D1","climbs one stair away from camera, steady, hand on the banister","one step, 2s",
    "sway","stairs ascending (§27G: one step)","no","eye","behind","FULL","clean","behind = going up is the easy way, she leaves us","deep","deep","R","up",layout=CUT)
row("BR-05b","Act 1",["B-05"],"BR","P","L-P-HALL","P-D1","comes down one stair, both hands on the banister, the LEFT knee braced as it catches","one step, 2s",
    "locked-off sway","stairs descending (§27G: camera at the foot, hand on rail)","no","low","three-quarter","FULL","clean",
    "low = the stair looms; coming down is the hard way","deep","deep","R","Coming",layout=CUT,face=True)
row("MECH-05","Act 1",["B-05"],"MECH","anatomy","—","MECH","ANAT-A step-down: the thigh lengthens to catch, the catch lands on the band, a red flash","one catch, 3s",
    "RV render","none","no","low","three-quarter","MCU","clean","low = the weight arriving","deep","deep","L","catch",layout=SPL,eg="EG07")

# ---- ACT 2 — that is why ×3, the list, never / never / always (B-06–B-10) ------------------------------------
TH("TH-A2", "Act 2", ["B-06","B-07","B-08","B-09","B-10"], "quieter on the list; slower and lower on 'where the load was landing' (stress register)")
row("BR-06","Act 2",["B-06"],"BR","P","L-P-HALL","P-D1","comes down her stairs BACKWARDS, facing the steps, both hands on the banister","one step back, 3s",
    "locked-off sway","stairs descending backwards (§27G: one step, both hands on rail, camera at the foot)","no","high","three-quarter-back","FULL","clean",
    "high + three-quarter-back = small, careful, from the landing","deep","deep","R","backwards",layout=CUT)
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
row("MECH-14","Act 3",["B-14"],"MECH","anatomy","—","MECH","ANAT-A relief: the pad holds the one band, the red on the tendon cools to blue","one step, 3s",
    "RV render","none","no","low","three-quarter","MCU","clean","low = the catch holds","deep","deep","L","pad",layout=SPL,eg="EG07")
row("BR-15","Act 3",["B-15"],"BR","D hand","L-D-CONS","D-D1","his fingertip sets on the tendon just under the kneecap of the desk knee model, then lifts a centimetre","one tap, 2s",
    "sway","hands","no","high","three-quarter","ECU","clean","high = the placement from above","medium","hands","L","placement",layout=PIP)

# ---- ACT 4 — proof, ten seconds, the doctor's word, the test, the scan (B-16–B-20) ------------------------------
TH("TH-A4", "Act 4", ["B-16","B-17","B-18","B-19","B-20"], "hands flat on the desk on 'I do not sell these'; eyebrows up on 'You will know in a minute'")
row("BR-16a","Act 4",["B-16"],"BR","surgeon (one-off SG-01, §19B approachable)","L-ORTHO","X-D1","turns the strap in his hand beside a knee model","one turn, 2s",
    "sway","hands","yes — product turns","eye","three-quarter","MCU","clean","","medium","product","R","orthopedic",product="held",model="NBP",layout=PIP,face=True,eg="EG06 34% card")
row("BR-16b","Act 4",["B-16"],"BR","walkers (one-offs WK-01)","L-TOWPATH","X-D1","a line of older walkers' legs passes on a towpath, a strap on each near knee","they cross frame, 3s",
    "locked-off","walking across frame (§27G: camera never travels)","no","ground","profile","MEDIUM","clean","ground = the steps of many","deep","deep","L","Two",
    product="worn · VISIBLE",model="NBP",layout=CUT,eg="EG06 200,000 card")
row("BR-17a","Act 4",["B-17"],"BR","P","L-P-HALL","P-D2","sitting on the bottom stair, seats the strap on her LEFT knee in one slide up (SEAT_LOCK)","one slide up, 2s",
    "sway","seating (SEAT_LOCK: only ever up)","yes — ends seated","high","three-quarter","CU","clean","high = quick and easy","medium","product","R","Ten",
    product="seated · VISIBLE",model="NBP",layout=SPL,ledger="F6")
row("BR-17b","Act 4",["B-17"],"BR","P","L-P-HALL","P-D2","stands and lets the rolled trouser leg fall; it lies flat over the strap","one drop, 2s",
    "sway","standing","no","low","three-quarter","CU","clean","low = the flat line of the trouser","medium","product","R","nobody",
    product="worn · REVEAL→CONCEALED (§9D)",model="NBP",layout=SPL,ledger="F6")
row("BR-19a","Act 4",["B-19"],"BR","P","L-P-HALL","P-D2","at the top of the stairs, trousers rolled above both knees: strap on the LEFT knee, the right bare","still, a breath, 2s",
    "sway","standing on a landing (§27G: no step)","no","high","front","MEDIUM","clean","high = the drop of the stairs below her","medium","product","R","One",
    product="worn · VISIBLE, one knee only",model="NBP",layout=CUT,ledger="F4")
row("BR-19b","Act 4",["B-19"],"BR","P","L-P-HALL","P-D2","comes down the stairs forwards, one step at a time, hand light on the banister","two steps, 3s",
    "locked-off sway","stairs descending (§27G: camera at the foot, hand on rail)","no","low","front","FULL","clean",
    "low = the mirror of BR-05b, now easy","deep","deep","R","forwards",product="worn · VISIBLE",model="NBP",layout=FULL,face=True,ledger="F4")
row("BR-20","Act 4",["B-20"],"BR","D","L-D-CONS","D-D1","holds two identical knee X-rays up side by side to the window","still, 2s",
    "sway","standing at the window (§27G: no travel)","no","eye","three-quarter-back","MCU","through","three-quarter-back + through = we read both scans over his shoulder",
    "medium","background","back","both",layout=SPL,ledger="F3",face=True)

# ---- ACT 5 — the reframe, the offer, the close (B-21–B-23) ------------------------------------------------------
TH("TH-A5", "Act 5", ["B-21","B-22","B-23"], "slow and certain on 'move the load'; the last line straight to lens, a small nod")
row("PR-22a","Act 5",["B-22"],"PRODUCT","object","L-P-KITCH","P-D2","the open box on the kitchen table: two straps side by side in the insert (package_open)","still; a hand settles the lid, 2s",
    "sway","none","no","overhead","front","CU","clean","overhead = what's in the box","medium","product","R","Two",product="box open, two units (OFFER)",
    model="GPT Sunburst",layout=PIP,eg="EG06 60-day seal")
row("BR-22b","Act 5",["B-22"],"BR","copy (one-off CP-01 leg)","L-P-KITCH","P-D2","a stretched grey near-copy strap sags down a shin","one slow sag, 2s",
    "sway","none; blank near-copy (FAKE_BASE)","no","low","profile","CU","clean","low + profile = the sag","medium","foreground","R","stretch",
    product="near-copy (FAKE_BASE)",model="NBP",layout=PIP,ledger="F7")
row("BR-23","Act 5",["B-23"],"BR","P","L-P-HALL","P-D2","comes down her stairs forwards, hands free, a small smile, strap on the LEFT knee","two steps, 3s",
    "locked-off sway","stairs descending (§27G: camera at the foot, hand near the rail)","no","low","three-quarter","FULL","clean",
    "low = the mirror of BR-06's high angle: now she owns the stairs","deep","deep","R","stairs",product="worn · VISIBLE",model="NBP",layout=FULL,face=True)

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
