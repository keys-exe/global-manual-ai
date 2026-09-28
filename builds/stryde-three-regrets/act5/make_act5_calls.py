"""Act 5 clip calls (§35 JSON on Kie kling-3.0-omni). The first Act 5 clip batch (8 beats) was built in the
previous session and its call files were lost with its container; this file rebuilds BR-043 (the one clip
that never landed) in the same shape as act4/make_act4_calls.py."""
import json, sys, os
sys.path.insert(0, "/home/user/global-manual-ai/products/stryde"); import stryde_product_sheet as ps
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../act4")
D = os.path.dirname(os.path.abspath(__file__)) + "/"
R1C = "Already drifting on frame one. Low breath sway throughout, vertical with slight roll. Brief focus hunt at entry. One late partial reframe. Camera lags the subject, never anticipates. Still drifting at the cut."
HOLD_C = "Everything in frame keeps the exact form, proportion and count it has in the start frame, first frame to last — nothing melts, merges, splits, grows or becomes something else. One small movement, completing inside the clip, subject fully in frame throughout, nothing leaving frame and returning."
HOLD_HC = "Same person, face and wardrobe every frame; five separate fingers on each hand, never fusing or passing through anything; limbs keep their length and bend only as real joints bend."
PHYS = "Mass and momentum in all movement: heavy starts and settles slow, nothing at uniform speed, nothing stops instantly — motions decelerate into a settle or small overshoot; actions travel through the body, weight transferring first, hands arriving last; hair, fabric and straps lag and keep moving after the body stops; objects drag with friction, never glide."
CAP = "Capture characteristics exactly as in the start frame — same tone-mapping, same noise, same colour temperature. No grading change across the clip."
NEGW = "no morphing, no warping, no melting, no shape shifting, no merging, no splitting, no parts detaching, no proportions changing, no duplicate objects, no background bending, no texture swimming, no smearing, no flickering geometry, no flickering light, no exposure pumping"
N = "no glancing at the lens, no talking, no slow motion, no music"

B = [dict(
    beat="BR-043", shot="act5_front_path",
    subject="THE SAME WOMAN as in the start frame, copper bob, white blouse, sage-green linen trousers to the ankle; unchanged in every respect.",
    framing="FULL as in the start frame: low, waist height in front of her on the path near the gate, looking up the path at her, from the front. FOCUS: deep; the path, her and the house stay sharp.",
    motion="CONTINUING: she is already mid-stride on her front path, right foot planted, left foot swinging through. COMPLETING: three easy steps towards the lens, about three seconds — each foot lands heel first and takes her weight, both knees bending freely, arms loose. UNRESOLVED: she slows near the gate, in frame head to shoes.",
    style="Unremarkable phone clip, warm midday sun on the front of the house, no grade.",
    negs="no strap, no knee support, no product, no limping, no running, no walking past the camera, no camera moving with her, " + N,
    risks=[{"risk": "the camera tracks with her and the walk turns to a glide", "prevented_by": "R1C sway only; no camera moving with her; feet land heel first and take her weight"},
           {"risk": "she walks out of frame or past the lens", "prevented_by": "three steps, slows near the gate, still in frame from head to shoes; no walking past the camera"},
           {"risk": "a strap reappears on the knee", "prevented_by": "start frame has none; no strap, no knee support, no product"}],
    sm="travels")]

# gen 2 clips from the Fix images (user: "MAKE CLIP FOR BR-046, BR-050, AND PR-045", 2026-09-28)
LOCK = "Locked off on a steady surface, only a faint breath of sway. The camera never pans or travels. Still at the cut."
B += [dict(
    beat="BR-046", shot="act5_towpath_walkers", cam=LOCK,
    subject="THE SAME THREE WALKERS, LEGS AND STRAPS as in the start frame; unchanged in every respect.",
    framing="MEDIUM as in the start frame: ground level on the towpath, the three walkers from the waist down. FOCUS: deep; legs and straps sharp.",
    motion="CONTINUING: the three walkers are already mid-stride towards the lens, one behind the other. COMPLETING: two easy steps each, about three seconds — each foot lands heel first and takes the weight, knees bending freely, the one strap on each near knee staying fixed below the kneecap. UNRESOLVED: still walking, slowing, all three in frame waist to shoes. " + ps.HOLD_PC,
    style="Unremarkable phone clip, warm late-morning sun on the towpath, no grade.",
    negs="no second strap on any walker, no strap appearing on a far knee, no strap sliding, no extra walkers, no faces, no running, no marching in step, no walking past the camera, no shell bending, no music",
    risks=[{"risk": "a second strap appears on a far knee", "prevented_by": "one strap each held by HOLD-PC and HOLD-C; no strap appearing on a far knee"},
           {"risk": "walkers walk out past the lens", "prevented_by": "two steps then slowing, all three in frame; no walking past the camera"},
           {"risk": "the camera tracks and the walk glides", "prevented_by": "locked-off camera; feet land heel first"}],
    sm="travels", hc=False, gen=2, fix="Image Fix: v1 frame had overlapping walkers (one read as wearing two straps) → new start frame, three separate walkers, one strap each; motion now towards the lens as the new frame faces them."),
 dict(
    beat="BR-050", shot="act5_landing_ease", cam=R1C,
    subject="THE SAME WOMAN as in the start frame, copper bob, white blouse, sage-green trousers, one strap on her right knee; unchanged in every respect.",
    framing="MEDIUM as in the start frame: from halfway up the stairs, her on the landing. FOCUS: both knees and the strap are sharp.",
    motion="CONTINUING: she stands at ease on the landing, arms loose at her sides, a soft half-smile. COMPLETING: one slow easy breath, about two seconds — her shoulders rise and settle, her half-smile warms a little. UNRESOLVED: she stands relaxed, both knees in view, hands away from the banister. " + ps.HOLD_PC,
    style="Unremarkable phone clip, warm midday light on the landing, no grade.",
    negs="no hand on the banister or rail, no stepping, no second strap, no strap on the left knee, no strap sliding, no big grin, no talking, no glancing at the lens, no shell bending, no music",
    risks=[{"risk": "her hand goes back to the banister", "prevented_by": "arms loose, hands away; no hand on the banister, no reaching for the rail"},
           {"risk": "she steps down", "prevented_by": "one breath only; no stepping"},
           {"risk": "the strap slides or a second appears", "prevented_by": "HOLD-PC; no strap sliding, no second strap"}],
    sm="in_place", hc=False, gen=2, fix="Image Fix: v2 frame had her hand on the banister and a stern face → new start frame at ease; motion reduced to one breath."),
 dict(
    beat="PR-045", shot="act5_surgeon_palm", cam=LOCK,
    subject="THE SAME SURGEON, OPEN HAND AND STRAP as in the start frame; unchanged in every respect.",
    framing="MEDIUM as in the start frame: eye height across the desk, the strap level on his open palm beside the knee model. FOCUS: the strap on his palm is sharp.",
    motion="CONTINUING: he holds the strap level on his open palm towards the lens, beside the knee model. COMPLETING: one small lift of the hand, about two seconds — the palm rises a little and settles, the strap staying level, front to the lens, never turning. UNRESOLVED: he holds it still, a slight warm smile. " + ps.HOLD_PC,
    style="Unremarkable phone clip, soft window daylight in the consulting room, no grade.",
    negs="no turning the strap, no strap sliding off, no fingers over the strap, no second strap, no talking, no music",
    risks=[{"risk": "the strap turns and its shape is redrawn", "prevented_by": "held level, never turning (pin_end not needed); HOLD-PC"},
           {"risk": "fingers close over the wordmark", "prevented_by": "no fingers closing over the strap"},
           {"risk": "the strap slides off", "prevented_by": "small lift and settle; no strap sliding off the palm"}],
    sm="in_place", gen=2, fix="Image Fix: v2 frame redrew the product tall and twisted → new start frame, the strap level on his palm as photographed; the turn (which needed a pinned end) replaced by one small lift so the product never changes angle."),
]

C = sys.argv[1] if len(sys.argv) > 1 else "/tmp/cards/"
ONLY = sys.argv[2].split(",") if len(sys.argv) > 2 else None
for b in B:
    if ONLY and b["beat"] not in ONLY: continue
    card = json.load(open(C + f"stryde-three-regrets__{b['beat']}.json"))
    prompt = json.dumps({"shot": b["shot"], "subject": b["subject"], "camera": {"movement": b.get("cam", R1C), "framing": b["framing"]},
                         "motion": b["motion"] + " " + HOLD_C + (" " + HOLD_HC if b.get("hc", True) else "") + " " + PHYS, "lighting": CAP,
                         "style": b["style"], "negatives": NEGW + ", " + b["negs"]}, ensure_ascii=False, separators=(",", ":"))
    call = {"beat": b["beat"], "connector": "kling", "mode": 1, "kind": "broll", "prompt": prompt,
            "duration": card["duration"], "resolution": "1080p", "aspect_ratio": "9:16",
            "start_image": card["imageUrl"], "start_approved": card["imageStatus"] == "confirmed",
            "pinned": False, "subject_motion": b["sm"], "prefer_multi_shots": "false", "generation": b.get("gen", 1), "risks": b["risks"]}
    if b.get("fix"): call["fix_note"] = b["fix"]
    json.dump(call, open(D + f"{b['beat']}.call.json", "w"), ensure_ascii=False, indent=1)
    open(D + f"{b['beat']}.kie_prompt.txt", "w").write(prompt)
    print(b["beat"], card["duration"], len(prompt))
