"""User Fix round 6 (2026-09-28): A4-B1 new start frame — "instead of stairs it should be other activities" (§22X)."""
import json, copy
import broll
FX = {
 "A4-B1": ({"angle": {"height": "low", "side": "three-quarter", "scale": "MEDIUM", "fg": "clean", "why": "low: the strap earning its keep", "mirror_of": None}},
           "Away from the stairs, in the hall by the front door: he is crouched down in a deep knee bend to lace up his walking boots, getting ready to head out — his right knee deeply bent and carrying his weight, both hands on the laces of the boot on his right foot, the boots' other pair still on the mat beside him. The strap sits on his right knee two centimetres below the kneecap, on the tendon, its wordmark readable and facing the lens; the left knee is bare. Capable, easy, unbothered. The stairs are only a soft shape in the background.",
           "low in the hall, close to him, looking across at his bent right knee with the front door behind him"),
}
EXTRA_NEG = {"A4-B1": "no stairs in the foreground, no climbing, no laundry basket, no hand on the rail, no sitting on a step"}
if __name__ == "__main__":
    man = []
    for b, (ov, scene, campos) in FX.items():
        r = copy.deepcopy(broll.ROWS[b]); r.update(ov)
        p = broll.t2i(r, campos, scene) + ", " + EXTRA_NEG[b]
        (broll.PR / "frames" / f"{b}.fix6.txt").write_text(p)
        man.append({"beat": b, "model": "nano_banana_pro", "refs": broll.refs(r), "chars": len(p)})
    json.dump(man, open(broll.PR / "frames/manifest_fix6.json", "w"), indent=1)
    for m in man: print(m["beat"], m["chars"], m["refs"])
