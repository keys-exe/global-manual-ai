#!/usr/bin/env python3
"""stryde-71-stairs — Act 6 videos (life back: the walk, the store, the bags, the husband) + PR-01b video generation 2 (Fix 2026-09-30).
Same §35 shape as video_act3–5. Lengths: work/lengths_T2.json (E6; C-01a cut moved to "That" 2026-09-30 so L-03a fits 6s)."""
import json, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import video_act1 as V
from video_act2 import LOCKED, build
from video_act3 import RIGID, PNEG

S = "/tmp/claude-0/-home-user-global-manual-ai/8f10ea69-fe4e-5541-9214-2e22280bbf9c/scratchpad"
START = json.load(open(S + "/act6_cur.json"))
HID = ", no strap showing, no strap over the jeans, no product"
WALK = ", no stumbling, no limping, no walking stick, no looking at the camera"

FIX = {"PR-01b": ("v1 had her lunge and strain against the wheelbarrow (motion fault, user: 'just normal pushing the wagon she should not be struggling') → "
                  "she rises out of the lean into an easy upright stance and pushes the barrow lightly one relaxed step, no effort, no strain")}
G2 = {
 "PR-01b": dict(framing="MEDIUM as in the start frame, in the back garden, the woman with the wheelbarrow.", cam=LOCKED,
   motion="She straightens up easily from the lean into a relaxed, upright stance and pushes the loaded wheelbarrow forward lightly with ONE easy step in about a second — no effort, no strain, "
          "her arms relaxed, a calm smile, as if it weighs nothing. The soil stays in the barrow. Her trousers cover her knees.",
   extra=HID.replace("jeans", "trousers") + ", no straining, no struggling, no lunging, no leaning hard, no gritted teeth, no soil spilling, no wheelbarrow changing shape",
   pace="unhurried", smot="in_place",
   risks=[("she strains again","'no effort, no strain… as if it weighs nothing' + no straining / no lunging (user)"),("wheelbarrow warps","HOLD"),("strap shows","no strap showing (under the trousers)")]),
}
B6 = {
 "L-01a": dict(framing="MEDIUM as in the start frame, on her tree-lined street, seen from behind as she walks away along the sidewalk.", cam=LOCKED,
   motion="She walks away from the camera along the sidewalk at an easy, brisk pace, one step per second, the tote swinging a little on her shoulder, upright and steady; she is still well in frame, a little smaller, at the end.",
   extra=HID + WALK + ", no turning around", pace="brisk", smot="traveling",
   risks=[("legs blend while walking away","steady pace, locked camera, stays in frame (§27G)"),("tote morphs","HOLD"),("strap appears on the jeans","no strap showing")]),
 "L-01b": dict(framing="MEDIUM as in the start frame, on the sidewalk, her walking past the three younger women.", cam=LOCKED,
   motion="She walks on at a brisk, easy pace, one step per second, drawing level with the three younger women strolling slowly beside her and moving just ahead of them in two steps, a small smile; they keep chatting.",
   extra=HID + WALK + ", no faces changing, no people merging, no running", pace="brisk", smot="traveling",
   risks=[("people merge as she passes","'drawing level… moving just ahead' + no people merging"),("faces morph","same person clause + no faces changing"),("legs tangle","two steps only, locked camera")]),
 "L-02a": dict(framing="MEDIUM as in the start frame, in the grocery checkout line.", cam=LOCKED,
   motion="Standing square with her feet planted, she moves the shopping basket from one hand to the other in one easy movement over about a second, then stands waiting calmly, her weight steady.",
   extra=HID + ", no shifting her weight, no stepping, no groceries falling, no basket changing shape, no shoppers merging, no readable text", pace="unhurried", smot="in_place",
   risks=[("basket and hands fuse","finger clause + HOLD"),("groceries multiply","HOLD count clause"),("she shifts her weight","feet planted + no shifting her weight (the line)")]),
 "L-02b": dict(framing="MEDIUM as in the start frame, from behind on her front path, a grocery bag in each hand.", cam=LOCKED,
   motion="She walks up the front path toward the porch at an easy, steady pace, two steps, one per second, a paper grocery bag in each hand swinging a little, upright and unhurried.",
   extra=HID + WALK + ", no bags changing shape, no bags tearing, no dropping the bags, no climbing the porch steps", pace="unhurried", smot="traveling",
   risks=[("bags morph","HOLD"),("legs blend walking away","two steps, locked camera"),("she climbs the steps","no climbing the porch steps")]),
 "L-03a": dict(framing="MEDIUM as in the start frame, the living room, her husband in his recliner with the newspaper.", cam=LOCKED,
   motion="Her husband lowers the newspaper to his lap in one slow movement over about a second and looks up toward the front door with raised eyebrows, then holds the look.",
   extra=", no standing up, no paper tearing, no paper changing shape, no readable newspaper text, no glasses changing, no strap, no product", pace="unhurried", smot="in_place",
   risks=[("newspaper morphs","HOLD + no paper changing shape"),("face warps as he looks up","same person clause"),("hands fuse with the paper","finger clause")]),
}

def go(beat, cfg, gen=1, fix=None):
    cfg = dict(cfg)
    if cfg.pop("rigid", False): cfg["motion"] += " " + RIGID
    print(beat, V.LEN[beat], "s", build(beat, cfg, START[beat], gen=gen, fix=fix), "chars gen", gen)

if __name__ == "__main__":
    for bt, cfg in G2.items(): go(bt, cfg, gen=2, fix=FIX[bt])
    for bt, cfg in B6.items(): go(bt, cfg)
