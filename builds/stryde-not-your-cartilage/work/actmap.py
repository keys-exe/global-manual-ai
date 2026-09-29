#!/usr/bin/env python3
"""Step-5 act map for stryde-not-your-cartilage (E4, §30I–§30K, §27G). One row per unique beat; the three videos share the body.
Writes actmap.json, angles_V1/V2/V3.json (cut order per finished video) and actmap_tables.md."""
import json, pathlib
H = pathlib.Path(__file__).parent

# light plans (§30K): location -> (source, time, kelvin, arc)
LP = {
 "L-F-LOUNGE": ("east window of Folake's lounge, net curtains", "morning", 5600, "problem → after: bright morning through the nets"),
 "L-F-HALL":   ("front-door glass behind the camera + the landing window", "morning", 5600, "after: soft bright wash down the hall"),
 "L-D-TOWPATH":("open sky, high thin cloud, sun high on the left", "midday", 6500, "problem (D1): flat bright overcast · after (D2): the cloud broken, sun"),
 "L-H-HALL":   ("front-door coloured glass + half-landing window", "morning", 5600, "problem (H1) → after (H2): warm wash on the stairs"),
 "L-H-KITCHEN":("window over the sink, east wall", "morning", 5600, "after: bright sun along the worktop"),
 "L-E-BEDROOM":("sash window, south wall", "morning", 5600, "after: bright morning across the bed"),
 "L-E-MARKET": ("open sky over a street market, sun behind the camera's right", "midday", 5600, "after: bright, busy"),
 "L-CONSULT":  ("consulting-room window, left-hand wall", "morning", 6500, "everyday: overcast morning daylight (a morning clinic)"),
 "MECH":       ("rendered: the ANAT look's own light", "midday", 6500, "mechanism: X-ray blue, red on pain"),
 "CARD":       ("rendered: dark card, soft top light", "midday", 6500, "offer card"),
}

# beat: act, phrase, type, subject, loc, day, action·pace, camera·staging·pin, height, side, scale, fg, why, fplane, dof, kside, key, product, layout, model, ledger
R = [
 # ---- Hooks ----
 ("HK1-01","Hook 1","HK1","MECH","anatomy — worn cartilage, calm","MECH","MECH","ANAT-B ghost limb of a right knee: the cartilage worn thin, bone close to bone — and the joint cool blue, no red anywhere · a slow orbit of the view, 3s","render · none · no","eye","three-quarter","CU","clean","the worn joint shown calm: the rediagnosis in one picture","deep","deep","front","cartilage","absent","full · EG01","NB2","F5"),
 ("HK2-01","Hook 2","HK2","BR","R1 Folake","L-F-LOUNGE","F-D1","sitting in her burgundy armchair with a mug of tea, she rubs her right knee once and looks out of the window · one rub, 3s","sway · sitting · no","eye","three-quarter","MEDIUM","clean","eye level, beside her: an ordinary morning deciding the day","eyes","medium","L","day","absent","full · EG01","NB2","F5"),
 ("HK3-01","Hook 3","HK3","BR","consultant CS-01 hand (one-off, §19B)","L-CONSULT","X-D1","a knee X-ray film clipped on the lit light box; the consultant's forefinger traces the narrow gap between the bones · one trace, 3s","sway · hands · no","eye","ots","CU","through","through the consultant's shoulder = the reading being given","foreground","medium","L","cartilage","absent","full · EG01","NB2","F5"),
 # ---- Body (Act 1: the problem; Act 2: the answer) ----
 ("B-01a","Act 1","B-01","PRODUCT","R2 Derek hands","L-D-TOWPATH","D-D2","sitting on the towpath bench, his hands lift the lid off the matte-black box on his knees: two straps side by side in the insert · one lift, 3s","sway · hands · no","high","three-quarter","CU","clean","high = his view down into the box","product","medium","L","Built","box open, two units (OFFER)","full","NBP","F4"),
 ("MECH-S1","Act 1","B-01","MECH","anatomy — the strap","MECH","MECH","ANAT-A full stack of a right knee in X-ray blue; the strap seated on the patellar tendon glows electric blue · a slow glow, 2s","render · none · no","eye","front","MCU","clean","","deep","deep","front","sleeves","worn (rendered, blue)","split · top · EG03 'STRYDE PRECISION STRAP'","NB2","F4"),
 ("MECH-S2","Act 1","B-01","MECH","anatomy — the brace","MECH","MECH","ANAT-A knee in a big wraparound brace, the joint glowing hot red-orange under it · a slow pulse of the red, 2s","render · none · no","eye","three-quarter","MCU","clean","","deep","deep","front","braces","absent (blank brace, rendered)","split · bottom · EG03 'BRACES'","NB2","F4"),
 ("MECH-01","Act 1","B-02","MECH","anatomy — bone on bone","MECH","MECH","ANAT-B ghost limb: bone on bone, the worn joint surfaces glowing hot red · a slow pulse of the red, 3s","render · none · no","low","profile","CU","clean","low + profile = the gap closed, bone meeting bone","deep","deep","front","Bone","absent","full","NB2","F9"),
 ("B-02b","Act 1","B-02","BR","R3 Hassan + consultant CS-01","L-CONSULT","H-D1","sitting across the desk from the consultant, he listens as she turns the knee model towards him; he looks down at it · one look down, 3s","sway · sitting · no","eye","ots","MEDIUM","through","OTS over the consultant = the news landing on him","eyes","medium","L","knee","absent","full","NB2","F12"),
 ("B-03a","Act 1","B-03","BR","R2 Derek","L-D-TOWPATH","D-D1","walking the towpath, he stops, leans a hand onto his right knee, a wince · one stop, 2s","locked-off sway · walking then stopping (§27G: 2 steps, stop) · no","eye","profile","FULL","clean","profile = the long path ahead of him","deep","deep","L","walk","absent","full","NB2","—"),
 ("B-03b","Act 1","B-03","BR","R3 Hassan","L-H-HALL","H-D1","standing halfway up his stairs, gripping the handrail, he pauses on one step and breathes out, a wince · still, one breath, 2s","sway · standing on a step (§27G: no step taken) · no","low","three-quarter","FULL","clean","low = the flight looms over him","eyes","medium","R","stairs","absent","full","NB2","—"),
 ("B-03c","Act 1","B-03","BR","R1 Folake","L-F-LOUNGE","F-D1","both hands on the armchair's arms, she pushes herself up out of the chair, a wince on the way up · one stand, 3s","sway · sit-to-stand (§27G: one action) · no","high","front","MEDIUM","clean","high = the chair holding her down","eyes","medium","L","pain","absent","full","NB2","—"),
 ("B-04","Act 2","B-04","PRODUCT","R2 Derek hand","L-D-TOWPATH","D-D2","holds the strap up in his palm by the canal, the wordmark facing the phone, a small tilt into the light · one tilt, 2s","sway · hands · yes — product turns","eye","front","CU","clean","","product","shallow","L","repair","held (open palm, HELD_GRIPS) · wordmark","full","NBP","—"),
 ("MECH-02","Act 2","B-05","MECH","anatomy — the strain off","MECH","MECH","ANAT-A + ANAT_A_POINT_TIGHT: one tight red point on the tendon below the kneecap; the strap seats on it and the red cools to blue · one seat, 3s","render · none · no","eye","three-quarter","MCU","clean","","deep","deep","front","tendon","worn (rendered, blue)","full","NB2","—"),
 ("B-06","Act 2","B-06","BR","R3 Hassan","L-H-HALL","H-D2","sitting on his bottom stair, strap on his right knee, he straightens the leg slowly, his face easing · one straighten, 3s","sway · sitting · no","ground","three-quarter","MCU","clean","ground = at the knee: the leg straightening","eyes","medium","R","written","worn · VISIBLE","full","NBP","F6"),
 ("B-07","Act 2","B-07","BR","R1 Folake","L-F-HALL","F-D2","comes down her stairs forwards, one foot per step, a hand light on the rail, strap on her right knee · two steps, 3s","locked-off sway · stairs descending (§27G, §30D: camera at the foot) · no","low","front","FULL","clean","low = the stairs no longer loom","deep","deep","R","stairs","worn · VISIBLE","full","NBP","—"),
 ("B-08","Act 2","B-08","BR","R3 Hassan","L-H-KITCHEN","H-D2","at the sink he fills the kettle, easy on his feet, strap on his right knee · one fill, 3s","sway · standing · no","eye","profile","MEDIUM","clean","profile = an ordinary morning back","eyes","medium","L","Surgery","worn · VISIBLE","full","NBP","F6"),
 ("B-09a","Act 2","B-09","BR","R4 Elaine","L-E-BEDROOM","E-D1","sitting on the edge of her bed, both hands flat on the closed strap slide it up her shin until the kneecap stops it (SEAT_LOCK) · one slide up, 3s","sway · seating (only ever up) · yes — ends seated","eye","profile","CU","clean","profile = the height: the notch meets the kneecap","product","medium","R","Adjustable","seated · VISIBLE","full","NBP","F10"),
 ("B-09b","Act 2","B-09","PRODUCT","R4 Elaine hands","L-E-BEDROOM","E-D1","turns the second strap over in both hands to show the grey pad inside (PAD_BACK_SHOT) · one turn, 2s","sway · hands · yes — product turns","high","three-quarter","CU","clean","high = looking into it","product","medium","R","pad","held · the pad","full","NBP","F11"),
 ("B-10","Act 2","B-10","BR","R3 Hassan","L-H-KITCHEN","H-D2","crouches to the bottom cupboard for a pan and stands back up, easy, strap on his right knee staying put · one stand, 3s","sway · crouch-to-stand (§27G: one action) · no","low","three-quarter","FULL","clean","low = the full bend and straightening","deep","deep","L","slipping","worn · VISIBLE","full","NBP","F7"),
 ("B-11a","Act 2","B-11","BR","R4 Elaine","L-E-BEDROOM","E-D1","standing by the bed she lets her rolled trouser leg drop; it falls flat over the strap · one drop, 2s","sway · standing · no","low","three-quarter","CU","clean","low = the flat line of the trouser","product","medium","R","trousers","worn · REVEAL→CONCEALED (§9D)","full","NBP","F7"),
 ("B-11b","Act 2","B-11","BR","R4 Elaine","L-E-MARKET","E-D1","at a street-market fruit stall she picks up apples into a paper bag, weight easy on both legs, not thinking about her knee · one reach, 3s","sway · standing · no","eye","three-quarter","MEDIUM","through","through the stall's fruit = caught in her day","eyes","medium","R","forget","worn · CONCEALED","full","NB2","F7"),
 ("B-12","Act 2","B-12","BR","surgeon SG-01 (one-off, §19B) + R2 Derek","L-CONSULT","D-D3","Derek sits on the couch edge, strap on his right knee; the surgeon crouches, taps the shell's top edge and nods · one tap, 2s","sway · sitting · no","eye","ots","MEDIUM","clean","OTS over the surgeon's shoulder = his approval","product","medium","L","Recommended","worn · VISIBLE","full","NBP","F8"),
 ("B-13a","Act 2","B-13","PRODUCT","object","L-F-LOUNGE","F-D2","the open matte-black box on the glass coffee table, two straps side by side in the insert; a hand settles the lid beside it · one settle, 2s","sway · hands · no","overhead","front","CU","clean","overhead = what's in the box","product","medium","L","free","box open, two units (OFFER)","full · offer text in the edit","NBP","—"),
 ("CARD-13b","Act 2","B-13","CARD","two straps on dark","CARD","CARD","two straps floating side by side on a dark navy-black background, soft top light (a still, moved in the edit) · still","render · none · no","eye","front","MEDIUM","clean","","product","deep","front","getstryde","two units, wordmarks","card · EG04 'BUY 1 GET 1 FREE' + URL","GPT Sunburst","—"),
 ("B-14","Act 2","B-14","BR","R2 Derek","L-D-TOWPATH","D-D2","walks the towpath towards camera, strap on his right knee, the bridge behind him · 3–4 steps, 3s","locked-off sway · walking at camera (§27G: 3–4 steps, waist-height phone) · no","low","front","FULL","clean","low = strong, the after","deep","deep","L","pain","worn · VISIBLE","full","NBP","—"),
]
KEYS = "beat act phrase type subject loc day action camera height side scale fg why fplane dof kside key product layout model ledger".split()
rows = [dict(zip(KEYS, r)) for r in R]
by = {r["beat"]: r for r in rows}
BODY = ["B-01a","MECH-S1","MECH-01","B-02b","B-03a","B-03b","B-03c","B-04","MECH-02","B-06","B-07","B-08","B-09a","B-09b","B-10","B-11a","B-11b","B-12","B-13a","CARD-13b","B-14"]
VIDS = {"V1": ["HK1-01"] + BODY, "V2": ["HK2-01"] + BODY, "V3": ["HK3-01"] + BODY}
DAYN = {d: i+1 for i, d in enumerate(sorted({r["day"] for r in rows}))}

def arow(b, group):
    r = by[b]; src, t, k, arc = LP[r["loc"]]
    face = r["type"] == "BR" and "hand" not in r["subject"] and r["subject"].startswith(("R", "surgeon", "consultant")) and r["scale"] in ("MCU", "MEDIUM", "CU")
    return {"beat": b, "group": group, "type": "BR" if r["type"] in ("PRODUCT", "MECH", "CARD") else r["type"], "subject": r["subject"].split(" —")[0].split(" +")[0],
            "height": r["height"], "side": r["side"], "scale": r["scale"], "fg": r["fg"], "why": r["why"], "mode": 1,
            "product_beat": r["type"] in ("PRODUCT", "CARD"), "face": face,
            "focus": {"plane": r["fplane"], "dof": r["dof"], "rack": None, "moving_subject": "walk" in r["action"] or "comes down" in r["action"]},
            "story_day": DAYN[r["day"]],
            "light": {"source": src, "key_side": r["kside"], "time": t, "arc": arc, "why": "", "kelvin": k}}

for name, order in VIDS.items():
    json.dump([arow(b, by[b]["act"] if b.startswith("HK") else "Body") for b in order], open(H / f"angles_{name}.json", "w"), indent=1)
json.dump({"rows": rows, **VIDS}, open(H / "actmap.json", "w"), indent=1)

hdr = "| Beat | Act | Phrase | Type | Subject | Location | Day | Action · pace | Camera · staging · pin | Angle (height · side · scale · fg) — why | Focus | Light key | Key word | Product | Layout · EG | Model | Ledger |\n|" + "---|" * 17
out = []
for act in ["Hook 1", "Hook 2", "Hook 3", "Act 1", "Act 2"]:
    out.append(f"#### {act}\n\n{hdr}")
    for r in rows:
        if r["act"] != act: continue
        ang = f"{r['height']} · {r['side']} · {r['scale']} · {r['fg']}" + (f" — {r['why']}" if r["why"] else "")
        out.append(f"| {r['beat']} | {r['act']} | {r['phrase']} | {r['type']} | {r['subject']} | {r['loc']} | {r['day']} | {r['action']} | {r['camera']} | {ang} | {r['fplane']}, {r['dof']} | {r['kside']} | {r['key']} | {r['product']} | {r['layout']} | {r['model']} | {r['ledger']} |")
    out.append("")
(H / "actmap_tables.md").write_text("\n".join(out))
print(len(rows), "beats ·", {k: len(v) for k, v in VIDS.items()})
