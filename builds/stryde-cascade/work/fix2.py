"""User Fix round 2 (2026-09-28): new start frames — every fault in this round sits in the frame (§22X)."""
import json, copy
import broll
FX = {
 "A1-B3": ({}, "She sits on the second stair of her own hall and rubs her right knee with her right hand, her left hand resting on her left knee, head bowed. Behind her the straight flight of carpeted stairs rises cleanly along the left wall to a proper landing at the top, the landing window lighting it; every tread leads on to the next, the banister runs the full length of the flight on the open side and ends at a newel post on the landing, and the top step meets the landing floor — the stairs never run into a wall.",
           "standing in the hall in front of the stairs, the phone held high, looking down at her with the whole flight and its landing visible behind her"),
 "A4-B1": ({"angle": {"height": "low", "side": "three-quarter", "scale": "MEDIUM", "fg": "clean", "why": "low: the strap earning its keep", "mirror_of": None}},
           "He is getting on with his day: carrying a full laundry basket in both arms up his own light oak stairs, caught mid-step with his right foot planted on the next tread and his weight going onto that knee, upright and easy, not holding the rail. The strap sits on his right knee two centimetres below the kneecap, on the tendon, its wordmark readable; the left knee is bare. Busy, capable, unbothered.",
           "low in the hall beside the bottom of the stairs, looking up across the flight at his legs and the basket, his strapped right knee nearest the lens"),
 "A4-P1": ({}, "Inside the open side door of his van: his weathered right hand lifts one strap up out of a clear organiser box on the steel shelf, holding it ONLY by its rigid matte-black shell — thumb on the front of the shell beside the wordmark, fingers behind the shell — so the wordmark faces the lens, and the soft black elastic band hangs down free from both ends of the shell, swinging loose below his hand. His fingers never touch the band.",
           "standing just outside the open side door, close to the shelf, looking at his hand and the strap"),
 "A4-P2": ({"subject": "N-hands", "product_state": "held", "camera": "sway"},
           "On a scarred oak workbench in window light: his two weathered hands hold one strap turned over so its BACK faces the lens — the inside of the shell, which is plain smooth matte black with NO wordmark and no lettering, lined with the soft black silicone pad, the brushed chrome slides at each end seen from behind and the soft woven black band looping round behind with its two small keeper loops, exactly as in the attached back-view reference. His right thumb presses into the silicone pad, the pad dimpling under it. The front of the shell and its wordmark face away from the camera and are not visible.",
           "close over the workbench, looking at the back of the strap in his hands"),
 "A5-B3": ({"angle": {"height": "low", "side": "front", "scale": "FULL", "fg": "clean", "why": "low from the hall: the whole man coming down, face and knees", "mirror_of": None}},
           "From the hall at the foot of the stairs: he is coming DOWN his light oak stairs briskly, caught mid-stride halfway down, his whole body in frame from his head to his feet — his face clearly visible, looking down at the steps ahead with a relaxed, confident expression — his right foot with the strap on the knee landing on the next tread while his left foot swings past toward the tread below, arms loose, hands off the rail. The strap on the right knee, the left knee bare. His face is lit softly by the front-door glass behind the camera, never a dark silhouette against the landing window.",
           "standing back in the hall a few steps from the bottom stair, the phone at chest height tilted up the flight, so his head and his feet both fit in the frame"),
 "A5-F1": ({"camera": "sway"},
           "Close on her hands as she sits in the armchair: she holds a cheap knock-off copy of the strap in her lap — NOT wearing it — and pulls it apart between both hands. The copy is shaped like the real strap in the attached reference (the same curved two-peak shell with a notch, a band, a fastening at each end) but cheaper: a thin shiny unbranded black plastic shell with no wordmark, and a thin shiny flat elastic band that stretches out long and slack between her hands, already baggy and out of shape. Her knees in the grey skirt below, the copy nowhere near her leg.",
           "sitting close in front of her armchair, looking down at her hands"),
}
ANATFX = {
 "A2-M4": "Strict side view, profile, of ONE single leg — exactly one thigh, one knee, one kneecap and one shin, one continuous outline — on a descending step: the thigh muscle lengthening as it brakes, and the load snapping down onto the patellar tendon just below the kneecap, which flares red. No second leg anywhere in the frame, no overlapping or ghosted copy of the limb, no double outline.",
}
REFS = {"A4-P2": ["N_sheet", "WORK", "back", "macro"], "A5-F1": ["C1_sheet", "P1_PROP", "P1_FRONT", "front"]}
EXTRA_NEG = {
 "A1-B3": "no stairs running into a wall, no flight ending at a blank wall, no staircase that goes nowhere",
 "A4-P1": "no hand holding the band, no fingers on the elastic, no band held taut",
 "A4-P2": "no wordmark visible, no front of the shell, no lettering on the shell",
 "A5-B3": "no face cut off by the frame, no cropped head, no silhouette, no face in shadow",
 "A5-F1": "no strap worn on the leg, no webbing strap with side-release buckles, no luggage strap, no STRYDE wordmark on the copy",
 "A2-M4": "no second leg, no overlapping legs, no duplicate limb, no double outline, no ghosted copy of the knee",
 "A4-B1": "no sitting, no resting, no hand on the rail",
}
if __name__ == "__main__":
    man = []
    for b, (ov, scene, campos) in FX.items():
        r = copy.deepcopy(broll.ROWS[b]); r.update(ov)
        if b == "A5-F1": r["product_state"] = "held_fake"
        if r["product_state"] == "held_fake":
            r2 = dict(r); r2["product_state"] = "absent"; p = broll.t2i(r2, campos, scene)
            p = p.replace("no knee strap, no knee brace, no product", broll.P.NEG_FAKE_HERO)
        else:
            p = broll.t2i(r, campos, scene)
        p += ", " + EXTRA_NEG[b]
        refs = [broll.MID[k] for k in REFS[b]] if b in REFS else broll.refs(r if r["product_state"] != "held_fake" else dict(r, product_state="absent"))
        (broll.PR / "frames" / f"{b}.fix2.txt").write_text(p)
        man.append({"beat": b, "model": "nano_banana_pro", "refs": refs, "chars": len(p)})
    for b, scene in ANATFX.items():
        r = broll.ROWS[b]; p = broll.t2i(r, "", scene) + ", " + EXTRA_NEG[b]
        (broll.PR / "frames" / f"{b}.fix2.txt").write_text(p)
        man.append({"beat": b, "model": "nano_banana_pro", "refs": broll.refs(r), "chars": len(p)})
    # post-edits (applied after generation of the text): A4-P2 back view drops the front wordmark lock; A2-M4 strict profile
    P = broll.P; f = broll.PR / "frames" / "A4-P2.fix2.txt"; t = f.read_text().replace(" " + P.WORDMARK_LOCK, "")
    t = t.replace("and a lowercase grey stryde wordmark centred on the lower body directly beneath the notch, horizontal and readable, never to one side of the notch", "and a lowercase grey stryde wordmark on the FRONT of the shell only — the front faces away from the camera in this frame").replace("FOCUS: the strap and its wordmark is in sharp focus", "FOCUS: the inside of the shell and the silicone pad are in sharp focus")
    for n in ["no blank shell, ", "no missing wordmark, ", "no wordmark fading, ", "no wordmark smearing, ", "no misspelled wordmark, ", "no extra letters, ", "no fingers across the wordmark, ", "no blown wordmark, "]: t = t.replace(n, "")
    f.write_text(t)
    f = broll.PR / "frames" / "A2-M4.fix2.txt"; f.write_text(f.read_text().replace("viewed from a low three-quarter angle, foreshortened, the knee joint sitting slightly off-centre", "viewed in strict side profile at eye level, the knee joint sitting slightly off-centre"))
    json.dump(man, open(broll.PR / "frames/manifest_fix2.json", "w"), indent=1)
    for m in man: print(m["beat"], m["chars"], len(m["refs"]))
