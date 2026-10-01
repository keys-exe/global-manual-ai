#!/usr/bin/env python3
"""E6 lengths plans for stryde-too-bad: one assemble.py plan per finished video (hook + body T8 VO parts joined),
each B-roll row on its phrase with its anchor. Writes edit/plan_V1.json, edit/plan_V2.json. Audio: pass the joined masters."""
import json, sys, pathlib
H = pathlib.Path(__file__).resolve().parent
A1, A2 = sys.argv[1], sys.argv[2]
V1 = [("HK1-01","Too bad these knee straps look too small to work.",None),
 ("B1-01a","Built over three years with orthopaedic surgeons",None),
 ("MECH-S1","to do what sleeves and braces never could.","sleeves"),
 ("B1-02a","They're small on purpose.","small"),
 ("B1-02","Because the pain comes from one small spot.","one"),
 ("B1-03a","Seventeen times your bodyweight goes through it,",None),
 ("MECH-02","two centimetres below your kneecap.",None),
 ("MECH-03","A big brace wraps the whole knee and misses it.",None),
 ("B1-04b","This sits right on it.",None),
 ("MECH-04","It redirects the load away from the worn spot.",None),
 ("B1-05b","And the pain just lifts.",None),
 ("B1-06","A scalpel, not a sledgehammer.",None),
 ("B1-07a","Perfect for bone on bone, arthritis,",None),
 ("MECH-05","worn cartilage and meniscus pain.",None),
 ("B1-08","So you can walk further without stopping.",None),
 ("B1-09a","Small enough to sit flat under your trousers.",None),
 ("B1-09b","Light enough you forget it's there.",None),
 ("B1-10","No slipping. No sores. No rolling down.",None),
 ("B1-11","Over two hundred thousand people wear one now.",None),
 ("B1-12a","Buy one, get one free today at getstryde.co.",None),
 ("CARD-12b","Sixty-day money-back guarantee.",None),
 ("B1-13a","Too small to work? Try it on your own stairs.",None),
 ("B1-13b","Nothing to lose but the pain.",None)]
V2 = [("HK2-01","Too bad these knee straps look like another gimmick.",None),
 ("B1-01a","Built over three years with orthopaedic surgeons",None),
 ("MECH-S1","to do what sleeves and braces never could.","sleeves"),
 ("B2-02","You've been stung before. Fair enough.",None),
 ("MECH-06","So here's what a gimmick never has. A mechanism.",None),
 ("MECH-02","Seventeen times your bodyweight goes through",None),
 ("B1-02","one small spot below your kneecap.",None),
 ("MECH-04","This strap redirects the load away from that spot.",None),
 ("B2-06a","In a sports medicine study, the strain was cut by thirty-four percent.",None),
 ("B1-05b","And the pain just lifts.",None),
 ("MECH-05","Perfect for bone on bone, arthritis, worn cartilage and meniscus pain.",None),
 ("B1-11","Over two hundred thousand people wear one now.",None),
 ("B1-04b","Adjustable, breathable,",None),
 ("B2-09b","with a silicone pad that locks the pressure right where you need it.",None),
 ("B1-10","No slipping. No sores. No rolling down.",None),
 ("B2-11","Recommended by orthopaedic surgeons for lasting relief.",None),
 ("B2-12","Only at getstryde.co, not the knock-offs on Amazon.",None),
 ("B1-12a","Buy one, get one free today.",None),
 ("B2-14","And a gimmick doesn't give you sixty days to send it back.",None),
 ("B1-13b","Nothing to lose but the pain.",None)]
for name, rows, audio, lines in (("V1", V1, A1, "vo/V1.lines.txt"), ("V2", V2, A2, "vo/V2.lines.txt")):
    plan = {"audio": audio, "script": str(H.parent / lines), "base": None,
            "broll": [dict(beat=b, clip=None, phrase=p, **({"key": k} if k else {})) for b, p, k in rows]}
    (H / f"plan_{name}.json").write_text(json.dumps(plan, indent=1, ensure_ascii=False))
print("ok")
