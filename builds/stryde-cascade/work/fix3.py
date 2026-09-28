"""User Fix round 3 (2026-09-28): new start frames for A2-B2, A4-P1, A4-P2 — the faults are in the frame (§22X)."""
import json, copy
import broll
P = broll.P
FX = {
 "A2-B2": ({"angle": {"height": "high", "side": "front", "scale": "CU", "fg": "clean", "why": "looking down: exactly where the tendon is", "mirror_of": None}, "focus": {"plane": "hands", "dof": "deep"}},
           "Looking straight down at his bare right knee as he sits on the bottom light oak stair: the round kneecap in the middle of the frame, and his right index fingertip pressed onto the FRONT of the leg exactly on the midline, just below the bottom tip of the kneecap — on the soft narrow patellar tendon between the kneecap and the bump at the top of the shin bone — the skin dimpling under the fingertip. The finger comes straight in from the front, never from the side of the knee; his other hand rests flat on his thigh. The kneecap is fully visible above the fingertip, untouched.",
           "standing over him in the hall, the phone held high looking straight down at his right knee"),
 "A4-P1": ({"angle": {"height": "eye", "side": "front", "scale": "CU", "fg": "clean", "why": "level and square: the product reads whole", "mirror_of": None}},
           "Inside the open side door of his van: his weathered right hand has just lifted one strap up out of a clear organiser box on the steel shelf and holds it up facing the lens, pinching it between thumb and forefinger at the LOWER EDGE of the shell only, so the whole shell reads clearly and nothing covers it: the wide matte-black shell as wide as his hand, its top edge rising into two matching pointed peaks either side of a crisp concave notch, a brushed chrome slide at each end, the grey stryde wordmark centred on the lower body beneath the notch, exactly as in the attached product reference. The black knit band hangs down free in a loop below from both chrome slides. His fingers never touch the band.",
           "standing just outside the open side door, level with his hand, looking straight at the front of the strap"),
 "A4-P2": ({"subject": "N-hands", "product_state": "held", "camera": "sway"},
           "On a scarred oak workbench in window light: his two weathered hands hold one strap turned over so its BACK faces the lens, exactly as in the attached back-view reference — the inside of the shell one smooth, continuous, unbroken surface of plain matte black silicone pad, with no holes, no openings, no perforations and no dimples anywhere in it; the brushed chrome slides at each end seen from behind; the soft woven black band looping round behind with its two small keeper loops. His right thumb rests lightly on the smooth pad without pressing in. The front of the shell and its wordmark face away from the camera and are not visible.",
           "close over the workbench, looking at the back of the strap in his hands"),
}
REFS = {"A4-P1": ["N_sheet", "VAN", "front", "tq_left"], "A4-P2": ["N_sheet", "WORK", "back"]}
EXTRA_NEG = {
 "A2-B2": "no finger at the side of the knee, no hands clasping the sides of the knee, no finger on the kneecap, no finger on the shin, no strap",
 "A4-P1": "no rounded rectangle shell, no clip-shaped shell, no shell without peaks, no hand covering the shell, no fingers across the peaks or the notch, no hand holding the band, no fingers on the elastic",
 "A4-P2": "no holes in the pad, no openings, no perforations, no vents, no dimples, no recesses, no thumb pressing in, no wordmark visible, no front of the shell, no lettering on the shell",
}
if __name__ == "__main__":
    man = []
    for b, (ov, scene, campos) in FX.items():
        r = copy.deepcopy(broll.ROWS[b]); r.update(ov)
        if b == "A2-B2": r["product_state"] = "absent"
        p = broll.t2i(r, campos, scene) + ", " + EXTRA_NEG[b]
        if b == "A4-P2":
            p = p.replace(" " + P.WORDMARK_LOCK, "")
            p = p.replace("and a lowercase grey stryde wordmark centred on the lower body directly beneath the notch, horizontal and readable, never to one side of the notch", "and a lowercase grey stryde wordmark on the FRONT of the shell only — the front faces away from the camera in this frame").replace("FOCUS: the strap and its wordmark is in sharp focus", "FOCUS: the inside of the shell and the silicone pad are in sharp focus")
            for n in ["no blank shell, ", "no missing wordmark, ", "no wordmark fading, ", "no wordmark smearing, ", "no misspelled wordmark, ", "no extra letters, ", "no fingers across the wordmark, ", "no blown wordmark, "]: p = p.replace(n, "")
        refs = [broll.MID[k] for k in REFS[b]] if b in REFS else broll.refs(r)
        (broll.PR / "frames" / f"{b}.fix3.txt").write_text(p)
        man.append({"beat": b, "model": "nano_banana_pro", "refs": refs, "chars": len(p)})
    json.dump(man, open(broll.PR / "frames/manifest_fix3.json", "w"), indent=1)
    for m in man: print(m["beat"], m["chars"], m["refs"])
