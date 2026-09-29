#!/usr/bin/env python3
"""Step 6 hook start images for stryde-too-bad (act map work/actmap.json, STEP4_5.md light plans and wardrobe).
Mode 1 §22T candid seed: CAM-LOCK → prose → scene (plate) → product → angle → focus → light → colour → CAP-FILE → negatives.
Product strings from the STRYDE product sheet module; placeholders from Appendix A by ID. Writes hooks/<BEAT>.t2i.txt + hooks.json."""
import json, re, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent; BUILD = HERE.parent; ROOT = BUILD.parents[1]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
sys.path.insert(0, str(ROOT / "products/stryde")); import stryde_product_sheet as P  # noqa: E402
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S); return m.group(1).strip()
ROWS = {r["beat"]: r for r in json.loads((BUILD / "work/actmap.json").read_text())["rows"]}
HEIGHT = {"overhead": "an overhead camera looking straight down", "high": "a high camera looking down", "eye": "an eye-level camera",
          "low": "a low camera close to the floor looking up", "ground": "a camera at ground level"}
SIDE = {"front": "the front", "three-quarter": "three-quarter", "profile": "the side, in profile", "three-quarter-back": "three-quarter behind",
        "behind": "directly behind", "ots": "over the shoulder"}
def angle(beat, subj, fg=""):
    r = ROWS[beat]
    return (S("ANGLE-LINE").replace("[HEIGHT CLAUSE from §30I]", HEIGHT[r["height"]]).replace("[SIDE]", SIDE[r["side"]]).replace("[SUBJECT]", subj)
            .replace("[, looking past FOREGROUND, soft in the near foreground | , seen in REFLECTION]", fg))
def focus(plane, deep=False):
    return (S("FOCUS-LINE").replace("[PLANE — the nearest eye of NAME / the hands and what they hold / the product and its wordmark / the foreground / everything]", plane)
            .replace("[DEPTH — the room behind falls to a soft, recognisable shape | everything from near to far stays sharp]",
                     "everything from near to far stays sharp" if deep else "the room behind falls to a soft, recognisable shape"))
def light(src, subj, side, q):   # no face in either hook: the face clause becomes the object's lit side
    return (S("LIGHT-SHOT").replace("[SOURCE from the light plan — the window on the room's WALL, or the named practical]", src)
            .replace("[SUBJECT]", subj).replace("[SCREEN SIDE]", side).replace("[TIME-OF-DAY QUALITY and the act's light state]", q)
            .replace("so the face has a lit side toward [SIDE] and a softer shadow side, with a small catchlight in the eyes",
                     f"so it has a lit side toward the {side} and a softer shadow side"))
def colour(lc, k, sc, who, wc, ac, sat):
    return (S("COLOUR-KEY").replace(", exactly as in the attached master frame", "").replace("[LIGHT COLOUR]", lc).replace("[KELVIN]", str(k))
            .replace("[SET COLOURS]", sc).replace("[WHO]", who).replace("[WARDROBE COLOURS]", wc).replace("[ACCENT]", "the accent is " + ac)
            .replace("[SATURATION AND CONTRAST IN CAMERA]", sat))
NEG_BASE = ("no readable text, no logos other than the stryde wordmark, no AI hands, no plastic skin, no extra fingers, no fused fingers, "
            "no polished render, no advertising image, no studio lighting, no vignette, no glowing skin, no light from nowhere, "
            "no shadows falling in two directions, no lens flare")
NEG_HANDS = "no wrong finger count, no malformed hands, no hands merging into objects"
def photo(parts, avoid):
    return "\n\n".join([S("CAM-LOCK")] + [p for p in parts if p] + [S("CAP-FILE"), "AVOID: " + avoid + ", " + NEG_BASE])
PROD = P.REF_PROD.replace("the attached reference image", "the attached product photos, front and back").rstrip(" —") + "."
RIGID = "It is a RIGID MOULDED shell with a hard edge, never fabric, never neoprene, never a padded pad."
OPEN_PALM = dict(P.HELD_GRIPS)["open palm"]
DENISE_HAND = ("Her hand is a sixty-four-year-old Black woman's hand, the same woman as the attached character sheet: dark brown skin with "
               "deeper creases over the knuckles, short unpainted nails, a paler palm, the rolled cuff of a mustard-yellow linen shirt at the wrist.")
ALAN_HAND = ("His hand is a seventy-two-year-old white man's hand, the same man as the attached character sheet: thin and wiry, knobbly "
             "knuckles, sun-mottled skin with age spots on the back, short nails, the cuff of a navy cardigan over a sage-green polo at the wrist.")
B = {}
# HK1-01 — "Too bad these knee straps look too small to work." (VN01: the strap small in a palm beside a big brace)
B["HK1-01"] = ("nano_banana_pro", ["front", "back", "R1-DENISE", "P2-D-LOUNGE"], photo([
    "A snapshot from a phone held high over the coffee table, looking down. Her right hand is held out, palm up, just above the low oak "
    "coffee table: " + OPEN_PALM + ". On the table right beside her hand lies a big grey knee brace, blank, no brand — a long "
    "neoprene sleeve with two steel hinged bars down its sides and three wide straps — three times the size of the strap in her palm. "
    "Only her hand, wrist and forearm come in from the right of the frame; her knees in olive cotton shorts are soft at the bottom edge. " + DENISE_HAND,
    "THE SAME LOUNGE exactly as in the attached location plate — the low oak coffee table with its stack of books and the bowl of clementines, "
    "the red-and-cream kilim rug below it, the teal velvet sofa with mustard cushions — seen from directly above the table, the table filling the frame.",
    PROD + " " + RIGID + " " + P.WORDMARK_LOCK + " " + P.SIZE_HELD,
    angle("HK1-01", "her hand and the brace"), focus("the strap in her palm and its wordmark"),
    light("the bay window on the lounge's south wall", "the table and her hand", "right", "bright morning daylight"),
    colour("bright morning daylight", 5600, "warm oak, the red-and-cream kilim, teal velvet at the edge", "she", "a mustard-yellow shirt cuff and olive shorts",
           "the black strap in her palm against the grey brace", "true to life")],
    P.NEG_HELD_P + ", " + P.NEG_WORDMARK + ", no stryde wordmark on the brace, no brand on the brace, no second strap, no strap worn, no face, " + NEG_HANDS))
# HK2-01 — "Too bad these knee straps look like another gimmick." (VN02: a drawer crammed with old supports)
B["HK2-01"] = ("nano_banana_2", ["R2-ALAN", "P0-A-KITCHEN"], photo([
    "A snapshot from a phone held straight above the kitchen units, looking down into a drawer. His right hand has just pulled the wide top "
    "drawer of the cream shaker unit open towards the camera: the drawer is crammed full of old knee supports that did not work, tangled "
    "together — a black stretchy knee sleeve, a grey hinged brace with steel bars, a blue gel wrap with hook-and-loop tails, a beige elastic "
    "bandage, a tube of knee gel — all blank, no brands, a little grubby, a strap hanging over the drawer's front edge. His fingers are hooked "
    "round the brushed steel bar handle. " + ALAN_HAND,
    "THE SAME KITCHEN exactly as in the attached location plate — the cream shaker units with brushed steel bar handles, the light oak-effect "
    "laminate worktop, the terracotta-effect floor — seen from directly above the open drawer, the drawer filling the frame.",
    angle("HK2-01", "the open drawer"), focus("the tangle of supports in the drawer"),
    light("the window over the sink on the kitchen's east wall", "the drawer and his hand", "left", "flat grey-white morning daylight"),
    colour("flat grey-white morning daylight", 5600, "cream units, light oak laminate, terracotta floor", "he", "a navy cardigan cuff",
           "the blue gel wrap", "muted, slightly cool")],
    "no stryde strap, no stryde wordmark, no black moulded shell with peaks, no brand names, no packaging text, no face, " + NEG_HANDS))
if __name__ == "__main__":
    out = {}
    for beat, (model, refs, prompt) in B.items():
        assert "[" not in prompt, (beat, prompt[prompt.index("["):][:80])
        (HERE / f"{beat}.t2i.txt").write_text(prompt + "\n")
        out[beat] = {"model": model, "refs": refs, "prompt": prompt, "line": ROWS[beat]["phrase"], "chars": len(prompt)}
        print(beat, model, len(prompt), refs)
    (HERE / "hooks.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
