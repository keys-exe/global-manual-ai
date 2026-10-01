#!/usr/bin/env python3
"""Step-6 hook prompts for stryde-not-your-cartilage, assembled from Appendix A and the Product Sheet by ID."""
import re, json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
sys.path.insert(0, str(ROOT / "products/stryde"))
import stryde_product_sheet as PS
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
SL = PS.SLOTS
def fill(s, **kw):
    for k, v in kw.items(): s = s.replace(f"[{k.replace('_',' ')}]", v)
    return s
MODULATION = ("no crossfade, no glow fading in place, no gradual onset, no delay before the modulation starts, no build-up, no ignition, "
              "no steady unchanging glow, no emission settling or resolving, ")
# v2 (Fix "MAKE MORE DETAILS"): v1's ANAT-B ghost limb is empty inside by design -> ANAT-A full stack + named joint detail
# ---- HK1-01: the worn joint, calm (ANAT-B ghost limb; no emission anywhere — the hook says the cartilage isn't what hurts)
HK1_IMG = "\n\n".join([
 fill(S("ANAT-BASE"), REGION=SL["REGION"], TARGET_JOINT=SL["TARGET_JOINT"]),
 fill(S("ANAT-A"), STACK=SL["STACK"], BONES=SL["BONES"]),
 "FINE DETAIL, rendered with the density of a high-end medical-atlas CGI: the patellar tendon a thick pearly band from the lower edge of the kneecap down to the shin, "
 "its fine lengthwise fibre sheen visible; the quadriceps tendon above the kneecap; the collateral ligaments on both sides of the joint as pale silvery straps; "
 "the crescent-shaped menisci as pale translucent wedges between the bones; the kneecap's rounded underside; the bone surfaces with fine grain, small pores and "
 "subtle ridges where the tendons attach; the translucent outer contour carrying a faint glassy sheen with soft reflections.",
 "THE JOINT: the smooth cartilage capping the end of the femur and the top of the tibia is visibly worn thin and patchy, rough-edged and uneven, "
 "the gap between the two bones narrowed on the inner side so bone sits close to bone. And yet the whole knee is calm: no glow, no red, no orange, "
 "no heat anywhere in the joint, the tendon or the bones — the muscles keep their natural healthy colour, the bones stay warm ivory-gold and the patellar tendon pearly white and quiet. "
 "A worn joint that is not hurting.",
 fill(S("ANAT-LIGHT"), TARGET=SL["TARGET"]),
 S("ANAT-FIELD"),
 "AVOID: " + S("ANAT-NEG").replace(MODULATION, "").replace("no individual muscle fibres, ", "") + ", no sparse empty interior, no low detail, no simplified shapes, no red glow, no orange glow, no hot spot, no emission anywhere, no glowing joint, no inflamed tissue, no strap, no product",
])
assert "[" not in HK1_IMG, HK1_IMG[HK1_IMG.index("["):][:80]
pathlib.Path("HK1-01.image.prompt.txt").write_text(HK1_IMG)
print("HK1-01 image", len(HK1_IMG))
