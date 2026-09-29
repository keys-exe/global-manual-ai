"""User Fix round 4 (2026-09-28): new start frames for A4-M1, A4-P1, A4-P3, A5-B2, A5-B3 (§22X — fault at its source)."""
import json, copy
import broll
P = broll.P
FX = {
 "A4-P1": ({"angle": {"height": "eye", "side": "front", "scale": "CU", "fg": "clean", "why": "level and square: the product reads whole", "mirror_of": None}},
           "Inside the open side door of his van: ONE weathered right hand, coming in from the bottom of the frame, holds one strap up facing the lens, pinching it between thumb and forefinger at the LOWER EDGE of the shell only. Nothing touches the top of the shell: the two matching pointed peaks and the crisp concave notch along its top edge are completely clear, with no hand, finger or thumb anywhere above or on them. The wide matte-black shell as wide as his hand, a brushed chrome slide at each end, the grey stryde wordmark centred on the lower body beneath the notch, exactly as in the attached product reference. The black knit band hangs down free in a loop below from both chrome slides. Only one hand in the frame.",
           "standing just outside the open side door, level with his hand, looking straight at the front of the strap"),
 "A4-P3": ({"subject": "product", "product_state": "object", "angle": {"height": "high", "side": "three-quarter", "scale": "CU", "fg": "clean", "why": "looking down: two ready to go", "mirror_of": None}, "focus": {"plane": "product", "dof": "deep"}},
           "On the scarred oak workbench in window light: two straps lie side by side, shell-up, a hand's width apart, each whole and exactly as in the attached product reference — the wide matte-black shell with two matching pointed peaks either side of a crisp concave notch along its top edge, a brushed chrome slide at each end, the grey stryde wordmark centred and readable on each — their black knit bands curled loosely on the wood beside them, still attached at both slides. A pencil and a steel tape measure lie nearby. No hands in the frame.",
           "standing at the workbench, looking down at the two straps at an angle"),
 "A5-B2": ({"angle": {"height": "eye", "side": "front", "scale": "FULL", "fg": "clean", "why": "level: a happy man coming down", "mirror_of": None}},
           "Seen from the hall at the foot of the stairs: he is coming quickly and happily down his light oak stairs, caught mid-step halfway down, smiling, on the WALL side of the flight — a full arm's length away from the banister and its pine handrail, which runs down the other side. His right hand, on the banister side, holds his car keys; his left arm swings loose by the wall. Neither hand is near the handrail. The strap on his right knee, the left knee bare. The landing window behind him, his face lit softly by the front-door glass behind the camera.",
           "in the hall at the foot of the stairs, looking up the flight at him"),
 "A5-B3": ({"angle": {"height": "low", "side": "front", "scale": "FULL", "fg": "clean", "why": "low from the hall: the whole man coming down, face and knees", "mirror_of": None}},
           "From the hall at the foot of the stairs: he is coming DOWN his light oak stairs briskly, caught mid-stride halfway down, his whole body in frame from his head to his feet, his face clearly visible and relaxed, walking down the WALL side of the flight — a full arm's length away from the banister and its pine handrail on the other side. His right hand, on the banister side, holds his car keys; his left arm swings loose by the wall. Neither hand is near the handrail. His right foot with the strap on the knee lands on the next tread; the left knee is bare. His face is lit softly by the front-door glass behind the camera, never a dark silhouette.",
           "standing back in the hall a few steps from the bottom stair, the phone at chest height tilted up the flight, so his head and his feet both fit in the frame"),
}
ANATFX = {
 "A4-M1": "Side view with the strap on the knee, the strap clearly PROTECTING the tendon: the strap's shell sits over the patellar tendon just below the kneecap, and a soft cool BLUE protective glow spreads from its pad over the tendon like a shield, wrapping it; a warm orange pulse of load travelling down the thigh reaches the top of the blue shield and is stopped there, fading into the blue, while the tendon inside the shield stays calm, pale and untouched. The strap, the blue shield and the calm tendon fill the middle of the frame.",
}
REFS = {"A4-P1": ["N_sheet", "VAN", "front", "tq_left"], "A4-P3": ["WORK", "front", "tq_left"]}
EXTRA_NEG = {
 "A4-P1": "no second hand, no hand at the top of the shell, no fingers on the peaks or the notch, no thumb over the top edge, no hand holding the band, no rounded rectangle shell, no clip-shaped shell",
 "A4-P3": "no hands, no fingers, no band stripped off the shell, no band stretched, no misshapen shell, no rounded rectangle shell, no shell without peaks",
 "A5-B2": "no hand on the handrail, no hand near the handrail, no hand touching the banister, no walking beside the banister, no sad face",
 "A5-B3": "no hand on the handrail, no hand near the handrail, no hand touching the banister, no walking beside the banister, no face cut off by the frame, no silhouette",
 "A4-M1": "no orange glow below the strap, no orange on the tendon, no wave passing the strap, no glow inside the joint, no second leg",
}
if __name__ == "__main__":
    man = []
    for b, (ov, scene, campos) in FX.items():
        r = copy.deepcopy(broll.ROWS[b]); r.update(ov)
        p = broll.t2i(r, campos, scene) + ", " + EXTRA_NEG[b]
        refs = [broll.MID[k] for k in REFS[b]] if b in REFS else broll.refs(r)
        (broll.PR / "frames" / f"{b}.fix4.txt").write_text(p)
        man.append({"beat": b, "model": "nano_banana_pro", "refs": refs, "chars": len(p)})
    for b, scene in ANATFX.items():
        r = broll.ROWS[b]; p = broll.t2i(r, "", scene) + ", " + EXTRA_NEG[b]
        p = p.replace("viewed from a low three-quarter angle, foreshortened, the knee joint sitting slightly off-centre", "viewed in strict side profile at eye level, the knee joint sitting slightly off-centre")
        (broll.PR / "frames" / f"{b}.fix4.txt").write_text(p)
        man.append({"beat": b, "model": "nano_banana_pro", "refs": broll.refs(r), "chars": len(p)})
    json.dump(man, open(broll.PR / "frames/manifest_fix4.json", "w"), indent=1)
    for m in man: print(m["beat"], m["chars"], m["refs"])
