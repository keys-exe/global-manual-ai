# Act map (§18 step 5, E4) — built after cast + plates rendered. B-roll durations pending-master (E4, V7.60.7).
import json
from pathlib import Path
B = Path(__file__).resolve().parents[1]
D1 = "D1 before: navy cotton shorts to just above the knee, a white vest under an oversized lilac cardigan, grey felt slippers"
D2 = "D2 after: faded teal crew-neck T-shirt, stone-coloured cotton shorts ending mid-thigh, scuffed white canvas plimsolls (sheet outfit)"
D3 = "D3 out and about: black straight-leg trousers, cream cable-knit jumper, black leather slip-on trainers"
rows = [
 # beat, act, phrase, type, subject, location/tier, story_day, product_state, visibility, valence, framing, note
 ("HK1-01","HOOK","Why this knee strap is a must for anyone who dreads the stairs.","BR","S1","HALL-STAIRS/TRAVERSED+PROP","D1","absent","NA","neg","WIDE","foot of stairs, looks up the flight, hand on the newel post and her right knee, braces to start"),
 ("HK2-01","HOOK","Why this strap is a must for bone on bone knees.","BR","S1","LIVING/PLATED","D1","absent","NA","neg","PROPPED","on sofa edge, both hands press around bare right knee, slow wince, starts to push up"),
 ("HK3-01","HOOK","Why this strap is a must if your knee hurts going downstairs.","BR","S1","HALL-STAIRS/TRAVERSED+PROP","D1","absent","NA","neg","WIDE","coming down the stairs step-to, gripping the handrail, filmed from the hall below"),
 ("B01","A1-PROBLEM","Because every step","BR","S1","HALL-STAIRS/TRAVERSED+PROP","D1","absent","NA","neg","OTS","close low angle: right foot lands on a tread, knee bends, hand grips rail"),
 ("B02","A1-PROBLEM","puts seventeen times your bodyweight","MECH","none","MECH field","-","absent","NA","neutral","MECH-C","anatomical knee on a step, load arriving down the femur onto the tendon (ANAT, walking cadence)"),
 ("B03","A1-PROBLEM","through one small spot below your kneecap.","MECH","none","MECH field","-","absent","NA","neutral","MECH-B","patellar tendon SITE glowing under load, just below the patella"),
 ("B04","A2-BUILT","These straps took three years to build with orthopaedic surgeons,","BR","S2","CLINIC/PLATED","SURG","held","VISIBLE","pos","PROPPED","surgeon at the desk turning the strap in his hands beside the knee model, pressing the notch against the model's kneecap"),
 ("B05","A2-BUILT","to sit right on that spot.","PRODUCT","S1","LIVING/PLATED","D2","seated","VISIBLE","pos","CLOSE","SEAT-LOCK: both hands slide the strap up the shin and seat it under the kneecap, fingers lifting"),
 ("B06","A2-BUILT","Unlike the cheap copies, which are too small to reach it.","DEMO","S1 hands","LIVING/PLATED","D2","held","VISIBLE","neutral","CLOSE","9C SIDE-BY-SIDE: STRYDE shell in one hand vs a small plain black generic tube strap in the other, the generic one visibly narrower than a kneecap"),
 ("B07","A3-MECH","Inside, a silicone pad","PRODUCT","S1 hands","LIVING/PLATED","D2","held","VISIBLE","neutral","CLOSE","strap turned in hand through window light, thumb pressing into the shell (9C PRESS), inner face toward camera only as matte black (pad not described: FLAG)"),
 ("B08","A3-MECH","catches the force and moves it off the worn part, before it hits the joint.","MECH","none","MECH field","-","worn (ANAT-PROD)","NA","neutral","MECH-B","anatomical: shell over tendon, load spreading off the SITE across the shell"),
 ("B09","A4-PROOF","Sports scientists measured it.","BR","S3 + S1","LAB/INCIDENTAL","LAB","worn","VISIBLE","pos","OTS","gait lab: S1 walking on a treadmill in the strap, S3 watching a laptop turned away, clipboard"),
 ("B10","A4-PROOF","Thirty-four percent less strain, every step.","BR","S1","STREET/TRAVERSED","D2","worn","VISIBLE","pos","CLOSE-WALK","tracking the right knee walking along a pavement, strap holding station each step"),
 ("B11","A4-CALLOUT","Built for bone on bone, arthritis,","BR","S1","LIVING/PLATED","D1","absent","NA","neg","PROPPED","rising from the sofa, hands pushing on both knees, stiff"),
 ("B12","A4-CALLOUT","worn cartilage and meniscus.","BR","S1","GARDEN/INCIDENTAL+PROP","D1","absent","NA","neg","WIDE","back garden, lowering herself to kneel at a border, hand on the right knee"),
 ("B13","A5-AFTER","So you walk further,","BR","S1","PARK/TRAVERSED","D2","worn","VISIBLE","pos","WIDE","walking briskly along a park path past a green bench, strap visible"),
 ("B14","A5-AFTER","and take the stairs without gripping the rail.","BR","S1","HALL-STAIRS/TRAVERSED+PROP","D2","worn","VISIBLE","pos","WIDE","STAIR-UP reciprocal gait, hands free, from the hall below"),
 ("B15","A5-AFTER","Not because the arthritis has gone.","BR","S1","HALL-STAIRS/TRAVERSED+PROP","D2","worn","VISIBLE","neutral","CLOSE","close on the right knee in the strap as it bends onto a tread, weight going through"),
 ("B16","A5-AFTER","Because the force isn't landing where it hurts.","MECH","none","MECH field","-","worn (ANAT-PROD)","NA","neutral","MECH-C","anatomical: step load landing on the shell, SITE calm"),
 ("B17","A6-FEATURES","Adjustable.","PRODUCT","S1 hands","LIVING/PLATED","D2","held","VISIBLE","neutral","CLOSE","band tail drawn through a chrome slide in hand, knit stretching and recovering (9C STRETCH)"),
 ("B18","A6-FEATURES","No slipping. No sores. No rolling down.","BR","S1","STREET/TRAVERSED","D2","worn","VISIBLE","pos","CLOSE-WALK","stepping up a kerb, strap holds station (12B anchoring)"),
 ("B19","A6-FEATURES","It sits flat under your trousers, light enough to wear all day.","BR","S1","HALL/TRAVERSED+PROP","D3","worn","CONCEALED","pos","WIDE","WEAR-CONCEAL: walking down the hall to the front door in trousers, no bulge"),
 ("B20","A7-SOCIAL","Recommended by orthopaedic surgeons,","BR","S2 + S1","CLINIC/PLATED","SURG","worn","VISIBLE","pos","OTS","S1 seated on the couch, surgeon crouched pointing at the strap seated under her kneecap, nodding"),
 ("B21","A7-SOCIAL","and worn by over two hundred thousand people.","BR","S4 one-off","HIGH-STREET/TRAVERSED","-","worn","VISIBLE","pos","WIDE","a British high street, an older man in shorts walking toward camera with the strap on his right knee among shoppers"),
 ("B22","A8-OFFER","And the best part? It's two for the price of one today.","PRODUCT","S1 hands","LIVING/PLATED","D2","held","VISIBLE","pos","CLOSE","two straps held in both hands, turned through the light (offer act in hand)"),
 ("B23","A8-OFFER","You get sixty days.","BR","S1","LIVING/PLATED","D2","worn","VISIBLE","pos","PROPPED","on the sofa, strap on, lifting the right leg and flexing the knee easily, small smile"),
 ("B24","A8-OFFER","If it doesn't change your stairs, you get your money back.","BR","S1","HALL-STAIRS/TRAVERSED+PROP","D2","worn","VISIBLE","pos","WIDE","STAIR-DOWN reciprocal gait, hands free"),
 ("B25","A9-CTA","Put one on,","PRODUCT","S1","LIVING/PLATED","D2","seated","VISIBLE","pos","CLOSE","SEAT-LOCK second angle, three-quarter from the right"),
 ("B26","A9-CTA","and your own stairs will tell you.","BR","S1","HALL-STAIRS/TRAVERSED+PROP","D2","worn","VISIBLE","pos","WIDE","foot of the stairs, starts to climb briskly, first two treads, from behind-right"),
]
keys = ["beat_id","act","phrase","type","subject","location","story_day","product_state","visibility","valence","framing","notes"]
am = [dict(zip(keys, r)) | {"duration": "pending-master", "side": "right"} for r in rows]
if __name__ == "__main__":
    (B/"act_map.json").write_text(json.dumps(am, indent=1))
    (B/"wardrobe_map.json").write_text(json.dumps({"S1": {"D1": D1, "D2": D2, "D3": D3}, "S2": {"SURG": "sheet outfit"}, "S3": {"LAB": "sheet outfit"}}, indent=1))
    print(len(am), "rows")
