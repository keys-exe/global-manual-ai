#!/usr/bin/env python3
"""Step-5 act map for stryde-failed-alternatives (E4, §30I–§30K, §27G). One row per unique beat; each video's cut order reuses beats.
Writes actmap.json, angles_V1/V2/V3.json (cut order per finished video) and actmap_tables.md."""
import json, pathlib
H = pathlib.Path(__file__).parent

# light plans (§30K): location -> (source, time, kelvin, arc)
LP = {
 "L-B-HALL":    ("stained-glass front-door panel, east, plus the landing window", "morning", 5600, "problem → after: bright morning wash down the hall"),
 "L-G-KITCHEN": ("kitchen window over the sink, far wall", "morning", 6500, "problem → turn: flat grey overcast morning"),
 "L-G-STREET":  ("open sky, the sun high behind the camera's right", "midday", 5600, "after: bright, sun on the brick"),
 "L-D-BOWLS":   ("open sky, midday sun high to the left", "midday", 5600, "after: bright midday sun"),
 "L-D-PARK":    ("open sky, broken cloud, sun behind the camera's left", "morning", 5600, "after: bright, sun and cloud"),
 "L-S-KITCHEN": ("small kitchen window over the sink, far wall", "morning", 6500, "problem: soft overcast morning"),
 "L-S-HALL":    ("the window at the top of the stairs, plus the front-door pane", "late morning", 5600, "turn → after: sun down the treads"),
 "L-S-HILL":    ("open sky over the hillside, sun high to the left", "midday", 5600, "after: bright, clean hill light"),
 "L-CLINIC":    ("consulting-room window, left-hand wall", "midday", 6500, "everyday: bright overcast daylight"),
 "MECH":        ("rendered: the ANAT look's own light", "midday", 6500, "mechanism: X-ray blue, red on pain"),
 "CARD":        ("rendered: dark card, soft top light", "midday", 6500, "offer card"),
}

# beat: act, phrase, type, subject, loc, day, action·pace, camera·staging·pin, height, side, scale, fg, why, focus plane, dof, key side, key word, product, layout, model, ledger
R = [
 # ---- Hooks ----
 ("HK1-01","Hook 1","HK1","BR","R1 Bernadette","L-B-HALL","B-D1","the top drawer of her hall dresser is open and crammed with old knee supports — black sleeves, a hinged brace, a beige wrap, a blue gel wrap, all blank; her hand pushes it shut hard · one push, 1.5s","sway · hands · no","high","three-quarter","CU","clean","high = looking down into the drawer: all that money","foreground","medium","L","sleeves","absent","full · EG01 · EG08 slam","NB2","VN01"),
 ("HK2-01","Hook 2","HK2","BR","R2 Gordon","L-G-KITCHEN","G-D1","the tall larder cabinet stands open, its shelves crammed with old knee supports — sleeves, hinged braces, gel wraps, magnetic bands, all blank; he swings the door shut hard with a flat hand · one swing, 1.5s","sway · none · no","eye","three-quarter","MEDIUM","clean","","foreground","medium","R","tried","absent","full · EG01 · EG08 slam","NB2","VN02"),
 ("HK3-01","Hook 3","HK3","BR","R4 Sian","L-S-KITCHEN","S-D1","sitting at her kitchen table, right leg out, she peels a small round plaster off the inner side of her right knee and looks at the spot · one peel, 2s","sway · sitting · no","high","three-quarter","CU","clean","high = her own look down at the knee: it wore off","hands","medium","L","injections","absent","full · EG01","NB2","VN03"),
 ("HK-BR","Hook 1","HK1/HK2/HK3 bridge","PRODUCT","SG-01 hands + R3 Delroy","L-CLINIC","D-D3","Delroy sits on the couch edge, right leg out; the surgeon's hands slide the closed strap up his shin until the kneecap stops it (SEAT_LOCK) · one slide up, 2.5s","sway · seating (only ever up) · yes — ends seated","eye","profile","CU","clean","profile = the height: the notch meets the kneecap","product","medium","L","straps","seated · VISIBLE","full · EG01","NBP","VN01, VN02, VN03 · F4"),
 # ---- Act 1 (Body 1; shared lines reused) ----
 ("B1-01a","Act 1","B1-01","PRODUCT","SG-01","L-CLINIC","X-D1","at her desk the surgeon seats the strap on the plastic knee model, just below the model's kneecap, and lets go · one small press, 2.5s","sway · hands · yes — product placed","eye","three-quarter","MCU","clean","","product","medium","L","surgeons","held against a knee model","full","NBP","—"),
 ("MECH-S1","Act 1","B1-01","MECH","anatomy — the strap","MECH","MECH","ANAT-A full stack of a right knee in X-ray blue; the strap seated on the patellar tendon glows electric blue · a slow glow, 2.5s","render · none · no","eye","front","MCU","clean","","deep","deep","front","never","worn (rendered, blue)","split · top · EG03 'STRYDE PRECISION STRAP'","NB2","F7"),
 ("MECH-S2","Act 1","B1-01","MECH","anatomy — the sleeve","MECH","MECH","ANAT-A knee in a black stretch sleeve pulled over the whole joint, the spot below the kneecap glowing hot red-orange under it · a slow pulse of the red, 2.5s","render · none · no","eye","three-quarter","MCU","clean","","deep","deep","front","sleeves","absent (blank sleeve, rendered)","split · bottom · EG03 'SLEEVES & BRACES'","NB2","F7"),
 ("B1-02a","Act 1","B1-02","BR","R4 Sian","L-S-KITCHEN","S-D1","sitting at her kitchen table, she pulls a black stretch sleeve up over her right knee with both hands until it covers the whole joint · one pull up, 2.5s","sway · sitting, hands · no","eye","profile","MCU","clean","profile = the whole knee swallowed by the sleeve","hands","medium","L","whole","absent (blank sleeve)","full","NB2","F7"),
 ("B1-02b","Act 1","B1-02","BR","R1 Bernadette","L-B-HALL","B-D1","sitting on her bottom stair, right leg straight, she presses her forefinger into the soft spot just under her right kneecap · one press, 2s","sway · sitting · no","high","front","ECU","clean","high = her own view down at her knee","hands","medium","R","spot","absent","full","NB2","—"),
 ("MECH-02","Act 1","B1-03","MECH","anatomy — the load","MECH","MECH","ANAT-A + ANAT_A_POINT_TIGHT: heel strike, the load arrives down the thigh and lands on one tight red point on the tendon just below the kneecap, never spreading onto the shin · one strike, 3s","render · none · no","low","three-quarter","MCU","clean","low = the force, heavy","deep","deep","front","Seventeen","absent","full · EG04 '17X' + arrow","NB2","—"),
 ("MECH-03","Act 1","B1-04","MECH","anatomy — the squeeze","MECH","MECH","ANAT-A: a sleeve squeezes the whole joint tight; the red point below the kneecap stays lit under it, the load line unchanged · one slow squeeze, 3s","render · none · no","high","three-quarter","MCU","clean","high = the whole knee wrapped, seen from above","deep","deep","front","cover","absent","full","NB2","F7"),
 ("B1-05a","Act 1","B1-05","BR","R1 Bernadette","L-B-HALL","B-D1","sitting on her bottom stair, both hands flat on the closed strap slide it up her shin until the kneecap stops it (SEAT_LOCK) · one slide up, 2.5s","sway · seating (only ever up) · yes — ends seated","low","three-quarter","CU","clean","low = the strap meeting the spot, from below","product","medium","R","sits","seated · VISIBLE","full","NBP","F11"),
 ("MECH-04","Act 1","B1-05","MECH","anatomy — relief","MECH","MECH","ANAT-A relief: the strap glows blue, the red point cools to blue as the load is taken off the spot · one step, 3s","render · none · no","eye","profile","MCU","clean","profile = the tendon's side view, now calm","deep","deep","front","redirects","worn (rendered, blue)","full","NB2","F8"),
 ("MECH-05","Act 1","B1-06","MECH","anatomy — the conditions","MECH","MECH","ANAT-B ghost limb: the joint surfaces worn thin, bone near bone, a torn meniscus edge glowing red · a slow orbit of the glow, 3s","render · none · no","eye","three-quarter","CU","clean","","deep","deep","front","bone","absent","full","NB2","—"),
 ("B1-08","Act 1","B1-08","BR","R3 Delroy","L-D-BOWLS","D-D1","on the bowls green he steps forward, bends low and rolls a bowl along the rink, strap on his right knee · one delivery, 3s","sway · one bend and roll (§27G) · no","ground","three-quarter","FULL","clean","ground = the bent knee, the strap still in place","deep","deep","L","lunchtime","worn · VISIBLE","full","NBP","F5"),
 ("B1-09","Act 1","B1-09","BR","R2 Gordon","L-G-STREET","G-D2","walks a terraced street towards camera past a red postbox, strap on his right knee · 3–4 steps, 3s","locked-off sway · walking at camera (§27G: 3–4 steps, waist-height phone) · no","low","front","FULL","clean","low = strength in the stride","deep","deep","R","slipping","worn · VISIBLE","full","NBP","F9"),
 ("B1-10","Act 1","B1-10","BR","SG-01 + R3 Delroy","L-CLINIC","D-D3","Delroy sits on the couch edge, strap on his right knee; the surgeon, crouched, taps the shell's top edge and nods · one tap, 2.5s","sway · sitting · no","eye","ots","MEDIUM","clean","OTS = over the surgeon's shoulder: her approval","product","medium","L","Recommended","worn · VISIBLE","full","NBP","—"),
 ("B1-11a","Act 1","B1-11","PRODUCT","object","L-B-HALL","B-D1","the open matte-black box on the hall telephone table, two straps side by side in the insert; a hand settles the lid beside it · one settle, 2.5s","sway · hands · no","overhead","front","CU","clean","overhead = what's in the box","product","medium","R","free","box open, two units (OFFER)","full · offer text in the edit","NBP","—"),
 ("CARD-11b","Act 1","B1-11","CARD","two straps on dark","CARD","CARD","two straps floating side by side on a dark navy-black background, soft top light (a still, moved in the edit) · still","render · none · no","eye","front","MEDIUM","clean","","product","deep","front","guarantee","two units, wordmarks","card · EG04 'BUY 1 GET 1 FREE' + URL + '60-DAY MONEY-BACK GUARANTEE'","GPT Sunburst","—"),
 ("B1-12a","Act 1","B1-12","BR","R1 Bernadette","L-B-HALL","B-D1","the dresser drawer is open again, the old supports gone; she lays the strap's empty box in it and slides it shut gently · one slide, 2.5s","sway · hands · no","high","three-quarter","CU","clean","high = the same drawer as the hook, now calm","foreground","medium","L","last","box (closed, wordmark)","full","NBP","VN01"),
 ("B1-12b","Act 1","B1-12","BR","R1 Bernadette","L-B-HALL","B-D1","walks down her hall away from camera to the front door, coat over her arm, strap on her right knee · 3–4 steps, 3s","locked-off · walking away (§27G) · no","eye","behind","FULL","clean","behind = she's off out, the day ahead","deep","deep","L","pain","worn · VISIBLE","full","NBP","—"),
 # ---- Act 2 (Body 2: new beats) ----
 ("B2-01b","Act 2","B2-01","PRODUCT","object — the old supports","L-G-KITCHEN","G-D1","on Gordon's kitchen table, a heap of old knee supports — sleeves, a hinged brace, a gel wrap, a magnetic band, all blank; nobody touches them · still, a tiny drift of the camera, 2.5s","sway · none · no","overhead","front","MEDIUM","clean","overhead = the whole pile at once: the lot","deep","deep","R","lot","absent (blank supports)","split · bottom · EG03 'EVERYTHING ELSE'","NB2","—"),
 ("B2-03","Act 2","B2-03","BR","R1 Bernadette","L-B-HALL","B-D1","sitting on her bottom stair she rubs her right knee slowly with one hand, then looks up, tired · one rub, 2.5s","sway · sitting · no","eye","three-quarter","MCU","clean","","eyes","medium","R","you","absent","full","NB2","—"),
 ("B2-04","Act 2","B2-04","BR","R1 Bernadette hand","L-B-HALL","B-D1","on the hall telephone table a blue gel pack, a rolled black sleeve and a plain tube of cream; her hand sweeps them to one side · one sweep, 2.5s","sway · hands · no","overhead","front","CU","clean","overhead = the routine, laid out","hands","medium","R","comfortable","absent (blank)","full","NB2","F7"),
 ("B2-06","Act 2","B2-06","BR","R2 Gordon","L-G-KITCHEN","G-D1","gets up from the kitchen chair in one easy move, strap on his right knee, a small surprised breath out · one stand, 2.5s","sway · sit-to-stand (§27G: one action, hands on knees then free) · no","low","three-quarter","MEDIUM","clean","low = strength as he rises","eyes","medium","R","lifts","worn · VISIBLE","full","NBP","—"),
 ("B2-08","Act 2","B2-08","BR","R3 Delroy","L-D-PARK","D-D2","walks a tarmac park path beside a boating lake, across frame, strap on his right knee · 3–4 steps, 3s","locked-off sway · walking across frame (§27G) · no","eye","profile","FULL","clean","profile = he keeps going, no stopping","deep","deep","L","further","worn · VISIBLE","full","NBP","—"),
 ("B2-12a","Act 2","B2-12","BR","R2 Gordon","L-G-KITCHEN","G-D1","the larder cabinet stands open, empty now but for the strap's box on the middle shelf; he closes the door gently · one close, 2.5s","sway · none · no","eye","three-quarter","MEDIUM","clean","","foreground","medium","R","back","box (closed, wordmark)","full","NBP","VN02"),
 ("B2-12b","Act 2","B2-12","BR","R2 Gordon","L-G-STREET","G-D2","walks away up the terraced street, strap on his right knee, hands in his jacket pockets · 3–4 steps, 3s","locked-off · walking away (§27G) · no","eye","three-quarter-back","FULL","clean","three-quarter-back = off up the street, the knee in view","deep","deep","R","pain","worn · VISIBLE","full","NBP","—"),
 # ---- Act 3 (Body 3: new beats) ----
 ("MECH-07","Act 3","B3-03","MECH","anatomy — the injection fades","MECH","MECH","ANAT-A: the joint's glow cools to blue for a moment, but the tight red point on the tendon below the kneecap stays lit, and the red creeps back over the joint · one slow fade and return, 3s","render · none · no","eye","three-quarter","MCU","clean","","deep","deep","front","load","absent · no needle ever","full","NB2","F7"),
 ("B3-05","Act 3","B3-05","BR","R4 Sian","L-S-HALL","S-D1","halfway down her stairs she stops, one hand on the wall rail, the other to her right knee, and waits · stops, one breath, 2.5s","sway · standing on a stair (§27G: no step) · no","low","three-quarter","MEDIUM","clean","low = the stairs loom over her","eyes","medium","R","fades","absent","full","NB2","F7"),
 ("B3-06","Act 3","B3-06","PRODUCT","R1 Bernadette hands","L-B-HALL","B-D1","holds the strap up in the light from the front door, pinched at the shell's bottom edge, turning it a quarter turn · a quarter turn, 2.5s","sway · hands · yes — product turns","eye","front","CU","clean","","product","shallow","R","mechanical","held (bottom-edge pinch) · wordmark","full","NBP","—"),
 ("B3-07","Act 3","B3-07","BR","R4 Sian","L-S-HALL","S-D1","comes down her stairs forwards, one foot per step, hand off the rail, strap on her right knee · two steps, 3s","locked-off sway · stairs descending (§27G, §30D: camera at the foot) · no","low","front","FULL","clean","low = the stairs no longer loom","deep","deep","L","lifts","worn · VISIBLE","full","NBP","F9"),
 ("B3-08","Act 3","B3-08","BR","object — the calendar","L-S-KITCHEN","S-D1","the wall calendar by the back door, weeks crossed off in pen, no readable writing; a hand lifts it off its hook · one lift, 2.5s","sway · hands · no","eye","front","CU","clean","","foreground","medium","L","weeks","absent","full","NB2","—"),
 ("B3-12","Act 3","B3-12","BR","R4 Sian","L-S-HILL","S-D2","walks a hill path beside a dry-stone wall with her black-and-white collie, away from camera, strap on her right knee · 3–4 steps, 3s","locked-off · walking away (§27G) · no","eye","three-quarter-back","FULL","clean","three-quarter-back = up the hill, the knee in view","deep","deep","L","pain","worn · VISIBLE","full","NBP","—"),
]
KEYS = "beat act phrase type subject loc day action camera height side scale fg why fplane dof kside key product layout model ledger".split()
rows = [dict(zip(KEYS, r)) for r in R]
by = {r["beat"]: r for r in rows}
assert len(by) == len(rows)

# cut order per finished video (split = MECH-S1 over the bottom half, one shot)
V1 = ["HK1-01","HK-BR","B1-01a","MECH-S1","B1-02a","B1-02b","MECH-02","MECH-03","B1-05a","MECH-04","B2-06","MECH-05","B3-07","B1-08","B1-09","B1-10","B1-11a","CARD-11b","B1-12a","B1-12b"]
V2 = ["HK2-01","HK-BR","B1-01a","MECH-S1","MECH-05","B2-03","B2-04","MECH-02","MECH-04","B2-06","B1-08","B2-08","B1-05a","B1-12b","B1-09","B1-11a","B2-12a","CARD-11b","B2-12b"]
V3 = ["HK3-01","HK-BR","B1-01a","MECH-S1","MECH-05","MECH-07","MECH-02","B3-05","B3-06","MECH-04","B3-07","B3-08","B2-08","B1-05a","B1-08","B1-10","B1-11a","CARD-11b","B3-12"]
SPLIT_BOTTOM = {"V1": "MECH-S2", "V2": "B2-01b", "V3": "MECH-S2"}
for v in (V1, V2, V3):
    for b in v: assert b in by, b
DAYN = {d: i+1 for i, d in enumerate(sorted({r["day"] for r in rows}))}

def arow(b, group):
    r = by[b]; src, t, k, arc = LP[r["loc"]]
    face = r["type"] == "BR" and "hand" not in r["subject"] and r["subject"].startswith(("R", "SG")) and r["scale"] in ("MCU", "MEDIUM", "CU")
    return {"beat": b, "group": group, "type": "BR" if r["type"] in ("PRODUCT", "MECH", "CARD") else r["type"], "subject": r["subject"].split(" —")[0],
            "height": r["height"], "side": r["side"], "scale": r["scale"], "fg": r["fg"], "why": r["why"], "mode": 1,
            "product_beat": r["type"] in ("PRODUCT", "CARD"), "face": face,
            "focus": {"plane": r["fplane"], "dof": r["dof"], "rack": None, "moving_subject": "walk" in r["action"] or "comes down" in r["action"]},
            "story_day": DAYN[r["day"]],
            "light": {"source": src, "key_side": r["kside"], "time": t, "arc": arc, "why": "", "kelvin": k}}

for name, order in (("V1", V1), ("V2", V2), ("V3", V3)):
    json.dump([arow(b, by[b]["act"] if b.startswith("HK") else ("Video " + name[1])) for b in order], open(H / f"angles_{name}.json", "w"), indent=1)
json.dump({"rows": rows, "V1": V1, "V2": V2, "V3": V3, "split_bottom": SPLIT_BOTTOM}, open(H / "actmap.json", "w"), indent=1)

# casting balance per video (people on screen, by recurring/one-off identity)
BLACK = {"R1", "R3"}; WHITE = {"R2", "R4", "SG"}
def people(b):
    s = by[b]["subject"]; out = []
    for t in ("R1", "R2", "R3", "R4", "SG"):
        if t in s: out.append(t)
    return out
for name, order in (("V1", V1), ("V2", V2), ("V3", V3)):
    ppl = [p for b in order for p in people(b)]
    nb = sum(p in BLACK for p in ppl); nw = sum(p[:2] in WHITE or p == "SG" for p in ppl)
    print(f"{name}: {len(order)} shots · people on screen {len(ppl)} · Black {nb} · white {nw} · {100*nb/max(1,len(ppl)):.0f}% Black")

hdr = "| Beat | Act | Phrase | Type | Subject | Location | Day | Action · pace | Camera · staging · pin | Angle (height · side · scale · fg) — why | Focus | Light key | Key word | Product | Layout · EG | Model | Ledger |\n|" + "---|" * 17
out = []
for act in ["Hook 1", "Hook 2", "Hook 3", "Act 1", "Act 2", "Act 3"]:
    out.append(f"#### {act}\n\n{hdr}")
    for r in rows:
        if r["act"] != act: continue
        ang = f"{r['height']} · {r['side']} · {r['scale']} · {r['fg']}" + (f" — {r['why']}" if r["why"] else "")
        out.append(f"| {r['beat']} | {r['act']} | {r['phrase']} | {r['type']} | {r['subject']} | {r['loc']} | {r['day']} | {r['action']} | {r['camera']} | {ang} | {r['fplane']}, {r['dof']} | {r['kside']} | {r['key']} | {r['product']} | {r['layout']} | {r['model']} | {r['ledger']} |")
    out.append("")
(H / "actmap_tables.md").write_text("\n".join(out))
print(len(rows), "beats ·", len(V1), "/", len(V2), "/", len(V3), "shots")
