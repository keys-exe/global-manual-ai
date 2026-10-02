#!/usr/bin/env python3
"""Step 5 for facelove-returning-it: act map (E4 rows, one picture per phrase §27), wardrobe map per story day (§21/§14A),
Visual Pitch (§30M). Hook rows are written at step 6 (L1 is Hook 1). Writes act_map.json, wardrobe.json, visual_plan.json."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
REC = dict(source="bedroom window, west wall", key_side="L", time="afternoon", arc="soft late-afternoon window light", kelvin=5000)
CNT = dict(source="store ceiling downlights", key_side="R", time="afternoon", arc="flat cool store light", kelvin=4000)
CAF = dict(source="café front window", key_side="L", time="midday", arc="bright midday window", kelvin=5600)
HAL = dict(source="frosted panel beside the front door", key_side="R", time="morning", arc="soft morning daylight", kelvin=5600)
SUN = dict(source="morning sun, east", key_side="L", time="morning", arc="clear morning sun", kelvin=5600)
SUN2 = dict(source="morning sun, east", key_side="R", time="morning", arc="clear morning sun, the delivery", kelvin=5600)
def F(plane, dof): return {"plane": plane, "dof": dof, "rack": None, "moving_subject": False}
def BR(beat, act, line, day, loc, cast, h, s, sc, why, focus, light, face, prod, action, pace, camera, plate, fg="clean", staging="", pin_end=False, state=None, **kw):
    r = dict(beat=beat, group=act, act=act, type="BR", line=line, story_day=day, location=loc, cast=cast, subject=cast[0] if cast else "PRODUCT",
             height=h, side=s, scale=sc, fg=fg, why=why, mode=1, focus=focus, light=light, face=face, product_beat=prod,
             action=action, pace=pace, camera=camera, staging=staging, pin_end=pin_end, plate=plate, face_state=state, layout="full",
             duration="pending-master", max=None)
    r.update(kw); return r
def TH(beat, act, line, state="N-AFTER"):
    return dict(beat=beat, group=act, act=act, type="TH", line=line, story_day="REC", location="L-VANITY", cast=["N"], subject="N",
                mode=1, face=True, face_state=state, seed="N-VOICE-IMG", layout="full")

R = [
 # ---- Act 1 · Scene 2 · The fake-out begins (L2) ----
 BR("B01", "Act 1", "And it is not because it goes on pure white", "REC", "L-VANITY", ["N"], "eye", "three-quarter", "ECU",
    "close and level — we are at her cheek as the white goes on", F("product", "shallow"), REC, True, True,
    "the balm end's flat crest presses onto her bare right cheekbone and draws one short stroke toward the ear, leaving a clean white stripe", "one slow stroke, about 2 s",
    "handheld selfie distance, the phone sways slightly, no travel", "P: her face from her left side, the stick in her right hand", state="N-BEFORE"),
 BR("B02", "Act 1", "and then turns into my exact shade", "REC", "L-VANITY", ["N"], "eye", "profile", "ECU",
    "true side-on so the white-to-skin front reads across the frame", F("product", "shallow"), REC, True, True,
    "the brush end sweeps through the white stripe in two small circles; behind the crown the white turns to her olive skin, ahead of it it stays white", "two slow circles, about 3 s",
    "phone held still, slight sway", "profile of her right cheek, window behind the phone", state="N-BEFORE"),
 BR("B03", "Act 1", "and melts in like it was made for my skin.", "REC", "L-VANITY", ["N"], "low", "three-quarter", "CU",
    "a little low — the reveal of the finished cheek, quietly pleased", F("eyes", "medium"), REC, True, False,
    "two fingertips pat the blended cheek twice and leave it; the cheek is one even tone, her crow's feet still there; her eyes go to the lens", "two light pats, then still",
    "handheld, slight sway", "her face three-quarter from below the chin", state="N-AFTER"),
 TH("TH-01", "Act 1", "Even the woman at the makeup counter", state="N-AFTER"),
 BR("B05", "Act 1", "told me my redness was too tricky to match and I should not bother.", "D0", "L-COUNTER", ["N", "C1"], "high", "ots", "MEDIUM",
    "over the saleswoman's shoulder, a little above — she is being looked down on", F("eyes", "medium"), CNT, True, False,
    "at the counter, the saleswoman, her back shoulder in frame, holds a beige foundation bottle beside the creator's red jaw, where three swatch stripes match nothing, and slowly shakes her head", "one slow head shake, about 2 s",
    "phone held by a friend at counter height, steady", "L-COUNTER from behind the counter", fg="through", state="N-BEFORE"),
 # ---- Act 2 · Scene 3 · The reasons pile up (L3) ----
 BR("B06", "Act 2", "It is not because it covered the redness,", "REC", "L-VANITY", ["N"], "eye", "front", "ECU",
    "square on the cheek — before and after in one frame", F("product", "shallow"), REC, True, True,
    "her left cheek half done: the brush crown crosses from the blended even side into the red side and stops on the border", "one slow sweep, about 2 s",
    "phone held still", "front of her left cheek", state="mid"),
 BR("B07", "Act 2", "the hyperpigmentation, the old post-acne marks,", "REC", "L-VANITY", ["N"], "low", "three-quarter", "ECU",
    "from under the jaw — where the marks hide", F("product", "shallow"), REC, True, True,
    "the balm crest glides once along her jawline over the small brown marks, leaving a thin white line on them", "one slow glide, about 2 s",
    "phone held still, slight sway", "her right jaw from below", state="N-BEFORE"),
 BR("B08", "Act 2", "and every tired line and dark circle", "REC", "L-VANITY", ["N"], "high", "three-quarter", "ECU",
    "slightly above the eye — the tired look, honestly lit", F("product", "shallow"), REC, True, True,
    "the side of the brush crown pats under her right eye twice; the dark circle evens out, the crow's feet stay exactly where they were", "two light pats",
    "phone held still", "her right eye from above, three-quarter", state="mid"),
 BR("B08b", "Act 2", "I have been hiding for years, in one swipe.", "REC", "L-VANITY", ["N"], "eye", "front", "MCU",
    "square to her finished face — one swipe, the whole result", F("eyes", "medium"), REC, True, False,
    "she draws the brush end once across her cheekbone and lowers it; her whole face is one even tone, every line still there; her eyes come to the lens", "one swipe, about 2 s",
    "handheld selfie distance, slight sway", "her face square, window left", state="N-AFTER"),
 BR("B09", "Act 2", "And it is definitely not because three of my friends this week", "D1", "L-CAFE", ["N", "C2", "C3", "C4"], "eye", "ots", "MEDIUM",
    "over her shoulder into the three faces turned on her — the attention is the point", F("eyes", "deep"), CAF, True, False,
    "the three friends round the café table lean in toward her at once, coffees in hand, looking at her face", "one lean in, about 1 s",
    "phone propped on the table, still", "L-CAFE from her chair", fg="through", state="N-AFTER"),
 BR("B10", "Act 2", "asked what I am using,", "D1", "L-CAFE", ["C2"], "eye", "three-quarter", "MCU",
    "on the friend asking — the question lands on her face", F("eyes", "medium"), CAF, True, False,
    "the auburn friend touches her own cheek with two fingers and raises her brows, eyes on the creator just off the lens", "one touch, held",
    "phone handheld across the table, slight sway", "C2 across the table, window on the left", state=None),
 # ---- Act 3 · Scene 4 · The last reason (L4) ----
 TH("TH-04", "Act 3", "It is not because I can finally skip a full face of makeup,"),
 BR("B11", "Act 3", "throw this one stick on before the grocery store,", "D2", "L-HALL", ["N"], "eye", "three-quarter", "MCU",
    "at the hall mirror — the quick check on the way out", F("product", "medium"), HAL, True, True,
    "keys hooked on one finger, she swipes the balm end once across her cheek in the round brass mirror and caps it", "one swipe and cap, about 3 s",
    "phone handheld beside the mirror, slight sway", "P-HOME, at the console and mirror", state="N-AFTER"),
 BR("B12", "Act 3", "and feel completely confident walking out the door.", "D2", "L-FRONT", ["N"], "low", "front", "FULL",
    "from low on the path — she owns the step out", F("deep", "deep"), SUN, True, False,
    "she pulls the walnut door shut behind her and walks two steps down the path toward the lens, tote on her shoulder, chin up", "two brisk steps",
    "phone held low on the path, still; she walks, the camera does not", "L-FRONT from the path", staging="flat path, no steps", pin_end=True, state="N-AFTER"),
 # ---- Act 4 · Scene 5 · The real twist (L5) ----
 TH("TH-05", "Act 4", "No. I am returning this one, because after I bought it, I found out it is the last day of the Prime Sale. Sixty percent off."),
 BR("B13", "Act 4", "Two full Foundation Sticks for almost the price of one,", "REC", "L-VANITY", ["N"], "high", "front", "CU",
    "from above the vanity — the deal laid out", F("product", "medium"), REC, False, True,
    "her hand sets a second closed stick down upright beside the first on the white vanity top, both wordmarks to the lens", "one set-down, about 1 s",
    "phone held above, still", "vanity top", pin_end=True, state=None),
 BR("B14", "Act 4", "plus a free primer, a mystery gift, free shipping,", "REC", "L-VANITY", ["N"], "eye", "three-quarter", "CU",
    "level with the vanity — the bundle grows", F("product", "medium"), REC, False, True,
    "her hand sets the primer and then the small mystery gift box beside the two sticks", "two set-downs, about 2 s",
    "phone held still", "vanity top, low and level", pin_end=True, state=None),
 BR("B14b", "Act 4", "and a full thirty day money back guarantee.", "REC", "L-VANITY", ["N"], "low", "front", "CU",
    "low and level with the vanity top — the whole deal, safe", F("product", "medium"), REC, False, True,
    "her hand slides the full bundle — two closed sticks, the primer and the gift box — a hand's width toward the lens and lets go", "one slow slide, about 1 s",
    "phone held still", "vanity top, low", pin_end=True, state=None),
 TH("TH-06", "Act 4", "So I am sending back my one,"),
 BR("B15b", "Act 4", "and buying the deal like I should have.", "D3", "L-FRONT", ["N"], "high", "three-quarter", "MEDIUM",
    "from above on the step — the deal arrives", F("product", "medium"), SUN2, True, True,
    "on her front step she bends and picks up a plain brown delivery box, tucking it under her arm with a small grin", "one pick-up, about 2 s",
    "phone held still from the doorway", "L-FRONT, the step by the rosemary pot", state="N-AFTER"),
 # ---- Act 5 · Scene 6 · CTA (L6) ----
 TH("TH-08", "Act 5", "So do not do what I did and pay for one. If you have not tried this yet, tap the link and grab the deal before midnight, because once the Prime Sale ends tonight, it is gone."),
 BR("B16", "Act 5", "It was never your skin. It was the formula.", "REC", "L-VANITY", ["N"], "eye", "three-quarter", "MCU",
    "her finished face and the stick side by side — the line in one picture", F("product", "medium"), REC, True, True,
    "she lifts the closed stick up beside her even cheek, wordmark to the lens, and holds it; every line of her face still there", "one lift, then still",
    "handheld selfie distance, slight sway", "her face three-quarter, window left", state="N-AFTER", whole="the two short sentences make one picture (each under 2 s)"),
]
json.dump(R, open(HERE / "act_map.json", "w"), indent=1, ensure_ascii=False)

W = {"names": {"N": "the creator", "C1": "counter saleswoman", "C2": "auburn friend", "C3": "friend 2", "C4": "friend 3"},
 "days": [
  {"day": "D0", "event": "the makeup-counter visit, weeks before", "source": "stated: 'Even the woman at the makeup counter told me'",
   "outfits": {"N": "a camel wool-blend coat open over a cream ribbed sweater, dark straight jeans, bare face (N-BEFORE)",
               "C1": "sheet outfit: black fitted short-sleeved work tunic, slim black trousers, black flats"},
   "events": [{"id": "D0-E1", "location": "L-COUNTER", "visibility": "VISIBLE", "beats": ["B05"]}]},
  {"day": "D1", "event": "coffee with three friends, this week", "source": "stated: 'three of my friends this week asked what I am using'",
   "outfits": {"N": "a terracotta cotton knit top with three-quarter sleeves, small gold hoop earrings, white jeans, the stick on (N-AFTER)",
               "C2": "sheet outfit: olive linen shirt, sleeves rolled, light-wash jeans",
               "C3": "a navy-and-white Breton striped top (a Black American woman, 40s, short natural curls)",
               "C4": "a mustard cardigan over a white T-shirt (a South Asian American woman, 50s, long grey-streaked braid)"},
   "events": [{"id": "D1-E1", "location": "L-CAFE", "visibility": "VISIBLE", "beats": ["B09", "B10"]}]},
  {"day": "D2", "event": "the grocery-store morning, this week", "source": "stated: 'throw this one stick on before the grocery store'",
   "outfits": {"N": "a plain white crew-neck T-shirt, an olive cotton utility jacket, light-wash jeans, white leather sneakers, a tan canvas tote (N-AFTER)"},
   "events": [{"id": "D2-E1", "location": "L-HALL", "visibility": "VISIBLE", "beats": ["B11"]},
              {"id": "D2-E2", "location": "L-FRONT", "visibility": "VISIBLE", "beats": ["B12"]}]},
  {"day": "D3", "event": "the deal arrives on her doorstep, days later", "source": "stated: 'and buying the deal like I should have' — the bought bundle arriving",
   "outfits": {"N": "a soft heather-grey crewneck sweatshirt, black leggings, white leather sneakers, hair in a loose low bun (N-AFTER)"},
   "events": [{"id": "D3-E1", "location": "L-FRONT", "visibility": "VISIBLE", "beats": ["B15b"]}]},
  {"day": "REC", "event": "today, the last day of the sale — filming at her vanity", "source": "stated: 'it is the last day of the Prime Sale… ends tonight'",
   "outfits": {"N": "sheet outfit: the cream-white sherpa robe over a white camisole"},
   "events": [{"id": "REC-E1", "location": "L-VANITY", "visibility": "VISIBLE", "beats": ["B01", "B02", "B03", "B06", "B07", "B08", "B08b", "B13", "B14", "B14b", "B16"]}]}],
 "talking_heads": [{"day": "REC", "subject": "N", "outfit": "the cream-white sherpa robe over a white camisole (one sitting: bare face on the hooks, N-AFTER on the body)",
                    "beats": [r["beat"] for r in R if r["type"] == "TH"]}]}
json.dump(W, open(HERE / "wardrobe.json", "w"), indent=1, ensure_ascii=False)
print(len(R), "rows,", sum(r["type"] == "BR" for r in R), "B-roll,", sum(r["type"] == "TH" for r in R), "TH")
