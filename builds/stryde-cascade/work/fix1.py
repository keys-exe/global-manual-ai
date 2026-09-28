"""User Fix round 1 (2026-09-28): new start frames for beats whose fault is in the frame (§22X)."""
import json, copy
import broll
from scenes import ANAT
MID = broll.MID
# beat -> (row overrides, scene, campos)
FX = {
 "A2-B1": ({}, "A tight low close shot of ONLY his right knee and shin in khaki shorts and ONE light oak stair tread with its white riser: his right foot has just landed flat on the tread below, the knee bending and taking his weight, the skin just below the kneecap tensed. Only one tread and one riser are in the frame, no flight of stairs, no stairs rising behind him.",
           "on the stairs, close to his knee, looking across the leg at a single tread"),
 "A2-B2": ({}, "Looking down at his bare right knee as he sits on the bottom light oak stair of his own hall, the white riser and the pine handrail's newel post beside him: he presses one fingertip into the patellar tendon, the soft narrow band of tendon just BELOW the bottom tip of the kneecap and above the bump at the top of the shin bone, the skin dimpling under his fingertip. The kneecap itself is fully visible above his finger, untouched.",
           "standing over him in the hall, looking down at his right knee"),
 "A3-B2": ({}, "A clean close-up of her bare right knee as she sits in the armchair, the leg bent at a natural right angle with the hem of her grey skirt resting just above the knee: the fingertips of her right hand spread a small blob of clear gel over the front of the kneecap, the gel shining wet on the skin. One normal knee with one round kneecap, smooth natural contours, the shin running straight down below it. Exactly one hand, entering from the right edge; her other hand, her face and her hair are out of frame.",
           "sitting close beside her armchair, looking straight across at her right knee"),
 "A4-B1": ({"focus": {"plane": "product", "dof": "deep"}}, "A product close-up: the strap on his right knee fills the middle of the frame as he sits on his bottom stair in shorts, the matte-black shell sitting on the tendon just below the kneecap with its wordmark crisp and readable, the band wrapping snugly round the back of the leg, the chrome slide at the side catching the window light. His knee and upper shin only, the shell the clear hero of the frame.",
           "low beside the bottom stair, close to his right knee, the strap facing the lens"),
 "A4-B2": ({"focus": {"plane": "product", "dof": "deep"}}, "A product close-up looking down at his right knee as he sits on his bottom stair: the round face of the kneecap bare above, and directly below it the strap on the tendon filling the lower middle of the frame, its notch cupping the kneecap's lower edge, the wordmark crisp and readable; his index finger points at the notch, touching the top edge of the shell, marking the spot. The strap is lower than the kneecap, never on the thigh.",
           "standing over him, looking down at the strap on his right knee"),
 "A4-P2": ({"subject": "N-hands", "product_state": "held", "camera": "sway"}, "On a scarred oak workbench in window light: his two weathered hands hold one strap turned on its back so the inside of the shell faces the lens, and his right thumb presses into the plain matte black silicone pad, the soft pad visibly dimpling under his thumb; the band hangs loose over his left wrist, sawdust and a pencil on the bench.",
           "close over the workbench, looking at the inside of the strap in his hands"),
 "A4-P3": ({"subject": "N-hands", "product_state": "held", "camera": "sway"}, "On the scarred oak workbench in window light: one strap already lies shell-up with its wordmark readable, and his weathered hand is setting a second strap down beside it, the shell just touching the wood, the band still trailing from his fingers; a pencil and a tape measure nearby.",
           "close over the workbench, looking down at the two straps"),
 "A5-B1": ({"product_state": "worn", "subject": "N", "camera": "sway"}, "Inside the open back of his van: he is lifting a heavy steel toolbox off the van floor with both hands, knees bent and back straight, the strap on his right knee below the kneecap, caught mid-lift with the weight just coming off the floor. He wears grey work shorts ending just above the knee so both knees are bare; handrail lengths strapped to the van wall behind him.",
           "standing outside the open back doors of the van, looking in at him from the side"),
 "A5-B2": ({}, "Seen from the hall: he is walking down his stairs wearing the strap on his right knee, caught mid-step, steady and upright, BOTH arms hanging loose at his sides, both hands well away from the pine handrail, not touching it. The landing window behind him.",
           "in the hall at the foot of the stairs, looking up the flight at him"),
 "A5-B3": ({}, "From the hall below, framed from the waist down: he is coming DOWN his stairs briskly, caught mid-stride, his right foot with the strap on the knee landing on the next tread while his left foot is already swinging past toward the tread below, arms loose, hands off the rail. Both knees in view, the strap on the right, the left knee bare.",
           "at the foot of the stairs, low, looking up the flight at his legs"),
 "A5-B4": ({}, "Facing him on the stairs: he is coming down forwards at a brisk, confident pace, caught mid-step halfway down the flight, one foot in the air above the next tread, arms loose and swinging slightly, not holding the rail, the strap on his right knee. The landing window behind him.",
           "in the hall at the foot of the stairs, looking up the flight at him"),
 "A5-B5": ({}, "Seen from behind her at the foot of the straight flight: she is climbing, one hand on the banister and one on the wall rail, paused on the second tread with one foot up on the third. The thirteen treads rise straight and evenly, each tread the same depth and each riser the same height, the brass stair rods parallel, the banister and the wall rail running straight and parallel up the flight.",
           "at the foot of the stairs, behind her, looking straight up the flight"),
 "A5-F1": ({"product_state": "fake", "subject": "C1"}, "Close on her hands as she sits in the armchair: she holds a cheap copy strap in her lap, NOT wearing it, and pulls its band apart between both hands; the thin band stretches out long and slack, already baggy and out of shape. Her knees in the grey skirt below, the strap nowhere near her leg.",
           "sitting close in front of her armchair, looking down at her hands"),
}
ANATFX = {
 "A4-M1": "Side view with the strap on the knee, the mechanism large and clear: the strap's shell sits on the patellar tendon just below the kneecap, its pad pressing into the tendon; a bright pulse of load travels down the thigh muscle as a glowing wave and is caught at the pad, where it splits and spreads away sideways across the shell in soft rings, while the tendon beneath stays calm and pale. The pad, the tendon and the spreading wave fill the middle of the frame.",
}
if __name__ == "__main__":
    man = []
    for b, (ov, scene, campos) in FX.items():
        r = copy.deepcopy(broll.ROWS[b]); r.update(ov)
        p = broll.t2i(r, campos, scene)
        if b == "A5-B1":
            p = p.replace(broll.WARD["N"], "Wearing a grey crew-neck T-shirt, a faded navy half-zip work fleece with no logo, grey cotton work shorts ending just above the knee with both knees bare, grey work socks, scuffed tan leather work boots, in navy and grey.")
        refs = broll.refs(r)
        model = "nano_banana_pro"
        (broll.PR / "frames" / f"{b}.v2.txt").write_text(p)
        man.append({"beat": b, "model": model, "refs": refs, "chars": len(p)})
    for b, scene in ANATFX.items():
        r = broll.ROWS[b]; p = broll.t2i(r, "", scene)
        (broll.PR / "frames" / f"{b}.v2.txt").write_text(p)
        man.append({"beat": b, "model": "nano_banana_pro", "refs": broll.refs(r), "chars": len(p)})
    json.dump(man, open(broll.PR / "frames/manifest_fix1.json", "w"), indent=1)
    for m in man: print(m["beat"], m["chars"], len(m["refs"]))
