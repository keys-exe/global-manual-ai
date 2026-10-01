"""User Fix round 5 (2026-09-28): new start frames for A4-B1, A4-P2, A4-P3 (§22X — the faults are in the frame)."""
import json, copy
import broll
P = broll.P
LOOP = "Each strap's black knit band is ONE CONTINUOUS CLOSED LOOP: it runs from the chrome slide at one end of the shell, round in an unbroken loop, and back into the chrome slide at the other end — never cut, never open, no loose or free band ends anywhere."
FX = {
 "A4-B1": ({"angle": {"height": "low", "side": "three-quarter", "scale": "MEDIUM", "fg": "clean", "why": "low: the strap earning its keep", "mirror_of": None}},
           "He is getting on with his day: carrying a full laundry basket up his own light oak stairs, the basket held on his RIGHT side, resting on his right hip under his right arm — on the side away from the banister — so the basket is well clear of the handrail. Caught mid-step with his right foot planted on the next tread and his weight going onto that knee, upright and easy, his left hand free and not touching the rail. The strap sits on his right knee two centimetres below the kneecap, on the tendon, its wordmark readable; the left knee is bare. Busy, capable, unbothered.",
           "low in the hall beside the bottom of the stairs, looking up across the flight at him, the banister on the far side of him"),
 "A4-P2": ({"subject": "product", "product_state": "object", "angle": {"height": "high", "side": "three-quarter", "scale": "CU", "fg": "clean", "why": "close, looking in: the pad", "mirror_of": None}, "focus": {"plane": "product", "dof": "deep"}},
           "On the scarred oak workbench in window light: ONE strap lies face-down so its BACK faces up to the lens, EXACTLY the product in the attached back-view reference photo, unchanged: the back of the shell has the same outline as the front — two rounded peaks either side of a gentle notch along the top edge, wide tapering wings — in smooth plain matte black silicone with no wordmark and no lettering, a brushed chrome slide at each end, and the black knit band forming one continuous closed loop behind it with its small keeper loop. No hands in the frame.",
           "standing at the workbench, looking down at the back of the strap at an angle"),
 "A4-P3": ({"subject": "product", "product_state": "object", "angle": {"height": "high", "side": "three-quarter", "scale": "CU", "fg": "clean", "why": "looking down: two ready to go", "mirror_of": None}, "focus": {"plane": "product", "dof": "deep"}},
           "On the scarred oak workbench in window light: two straps lie side by side, shell-up, a hand's width apart, each whole and exactly as in the attached product reference — the wide matte-black shell with two matching pointed peaks either side of a crisp concave notch along its top edge, a brushed chrome slide at each end, the grey stryde wordmark centred and readable on each. " + LOOP + " The loops lie flat and relaxed on the wood behind each shell. A pencil and a steel tape measure lie nearby. No hands in the frame.",
           "standing at the workbench, looking down at the two straps at an angle"),
}
REFS = {"A4-P2": ["WORK", "back"], "A4-P3": ["WORK", "front", "tq_left", "back"]}
EXTRA_NEG = {
 "A4-B1": "no basket on the banister side, no basket touching the handrail, no hand on the rail, no sitting",
 "A4-P2": "no rectangular pad, no watch-strap shape, no oval pad, no wordmark visible, no front of the shell, no lettering, no hands, no cut band, no open band ends",
 "A4-P3": "no cut band, no open band ends, no loose strap ends, no band lying straight out from the shell, no hands, no misshapen shell, no shell without peaks",
}
if __name__ == "__main__":
    man = []
    for b, (ov, scene, campos) in FX.items():
        r = copy.deepcopy(broll.ROWS[b]); r.update(ov)
        p = broll.t2i(r, campos, scene) + ", " + EXTRA_NEG[b]
        if b == "A4-P2":
            p = p.replace(" " + P.WORDMARK_LOCK, "")
            p = p.replace("and a lowercase grey stryde wordmark centred on the lower body directly beneath the notch, horizontal and readable, never to one side of the notch", "and a lowercase grey stryde wordmark on the FRONT of the shell only — the front faces down against the bench in this frame").replace("FOCUS: the strap and its wordmark is in sharp focus", "FOCUS: the back of the shell and its silicone pad are in sharp focus")
            for n in ["no blank shell, ", "no missing wordmark, ", "no wordmark fading, ", "no wordmark smearing, ", "no misspelled wordmark, ", "no extra letters, ", "no blown wordmark, ", "no product tipped on its side, "]: p = p.replace(n, "")
        refs = [broll.MID[k] for k in REFS[b]] if b in REFS else broll.refs(r)
        (broll.PR / "frames" / f"{b}.fix5.txt").write_text(p)
        man.append({"beat": b, "model": "nano_banana_pro", "refs": refs, "chars": len(p)})
    json.dump(man, open(broll.PR / "frames/manifest_fix5.json", "w"), indent=1)
    for m in man: print(m["beat"], m["chars"], m["refs"])
