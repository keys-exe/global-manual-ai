#!/usr/bin/env python3
"""§19 avatar-sheet prompts for stryde-identity, assembled from Appendix A by ID (never retyped)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

CAST = {
 "N-NARR": dict(sex="MAN", side="left", wall="pale grey", floor="bare grey-painted concrete floor",
   face="A long, narrow face with deep-set pale grey eyes under a low brow, hollow cheeks and a long upper lip. The nose was broken long ago and bends visibly to the left at the bridge — his one marker. The left eye sits a fraction lower than the right and the mouth pulls slightly to the right",
   hair="Short grey hair, thinning at the crown, and a full close-trimmed beard of grey shot through with faded ginger at the chin, the same tone and the same trim in every panel",
   body="A white British man. Tall and wiry, long arms, big knuckled hands, a slight forward set to the shoulders, sixty-three years old",
   ward="A faded olive-green work shirt with the sleeves rolled to the elbow, worn brown cord trousers and scuffed brown leather work boots",
   age="deep crow's feet fanning from both eyes, two long vertical creases between the brows, weathered wind-reddened skin across the cheekbones, a scatter of sun spots on the temples"),
 "C1-MAUREEN": dict(sex="WOMAN", side="right", wall="warm magnolia", floor="a worn beige carpet",
   face="A broad, heavy face with soft jowls under a wide jaw, hooded brown eyes, a wide flat-bridged nose and thin lips. The little finger of her right hand is crooked at the top joint and never straightened — her one marker, visible in every full-length panel. The right side of the mouth sits a little lower than the left",
   hair="Short, tightly cropped pure white curls close to the head, a little flattened on one side, the same white and the same height in every panel",
   body="A white British woman. Short and heavyset, a broad soft middle, thick calves, seventy-four years old",
   ward="A loose cerise-and-orange patterned blouse, a plum-coloured cotton skirt ending a hand's width above the knee so both knees are bare, and flat navy slip-on shoes",
   age="deep folds from the nose to the corners of the mouth, a crosshatch of fine lines on the upper lip, heavy crepe under the eyes, age spots across the forehead and the backs of the hands, soft loose skin at the knees"),
 "C2-DEAN": dict(sex="MAN", side="left", wall="scuffed white", floor="grey vinyl flooring",
   face="A round, broad face with small narrow blue eyes, a wide flattened nose, a thick neck and a heavy brow ridge. His left ear is a cauliflower ear, thickened and lumpy from years of rugby — his one marker. The left side of the face is fuller than the right",
   hair="A shaved head with dark grey stubble over the whole scalp and a few days of dark grey stubble on the jaw, the same length and tone in every panel",
   body="A white British man. Barrel-chested and heavyset, thick forearms, a solid belly, sturdy legs, fifty-eight years old",
   ward="A plain charcoal work T-shirt, navy work shorts ending just above the knee so both knees are bare, grey work socks and black steel-toe work boots",
   age="deep horizontal forehead creases, weathered outdoor skin reddened across the nose and cheeks, fine broken capillaries on the nose, squint lines at the outer eyes"),
 "C3-PAT": dict(sex="WOMAN", side="right", wall="sage green", floor="light oak floorboards",
   face="A narrow, sharp face with high prominent cheekbones, a small pointed chin, a thin pointed nose and quick bright hazel eyes. Her ears stick out noticeably from the head — her one marker. The left eyebrow sits slightly higher than the right",
   hair="A short pixie crop of grown-out chestnut dye with about three centimetres of iron-grey roots at the parting and temples, the same tone and the same grow-out line in every panel",
   body="A white British woman. Small and wiry, narrow shoulders, lean muscular calves of someone who walks everywhere, sixty-two years old",
   ward="A fitted oatmeal knit cardigan buttoned over a white T-shirt, khaki cotton walking shorts ending just above the knee so both knees are bare, and grey running trainers",
   age="fine lines fanning from the corners of both eyes, light vertical lines above the upper lip, faint freckling across the nose and cheekbones, slight crepe under the eyes"),
 "C4-SURGEON": dict(pro=True, sex="MAN", side="left", wall="pale blue-grey", floor="grey hard-wearing clinic flooring",
   face="A broad, open, square face with full cheeks and warm grey-blue eyes that crease easily at the corners, a short straight nose and a wide mouth. His eyebrows are thick and still dark against the white hair, sitting high and relaxed — his one marker. The jaw is a little heavier on the right",
   hair="Bald across the crown and top, close-cropped white hair at the sides and back, no beard, clean-shaven, the same in every panel",
   body="A white British man. Tall and a little stooped at the shoulders, long-boned, broad hands with long fingers, seventy-one years old",
   ward="A pale blue cotton shirt with the cuffs turned back once, dark navy wool trousers and polished dark brown leather lace-up shoes",
   age="deep lines across the forehead, heavy folds from the nose to the mouth, loose skin under the jaw, age spots on the scalp and the backs of the hands"),
}

def build(k, c):
    sheet = S("AVATAR-SHEET")
    if c.get("pro"):                          # §19B face register (correction 2026-09-26)
        c = dict(c, face=c["face"] + ". " + S("APPROACH-PRO").rstrip("."))
    first, rest = sheet.split(". ", 1)          # SHEET-GRID pasted after the opening sheet sentence
    sheet = first + ". " + S("SHEET-GRID") + " " + rest
    for a, b in [("[WOMAN/MAN]", c["sex"]), ("[FACE — architecture in three or four plain sentences, the one marker, the asymmetries]", c["face"]),
                 ("[HAIR — colour, roots, how worn, the same tone and the same height in every panel]", c["hair"]),
                 ("[BODY — build, height impression]", c["body"]), ("[WARDROBE — BASE, LOWER, FOOT]", c["ward"]),
                 ("[SIDE]", c["side"]), ("[WALL COLOUR]", c["wall"]), ("[FLOOR]", c["floor"])]:
        sheet = sheet.replace(a, b)
    assert "[" not in sheet, k
    skin = "IN THE FACE CLOSE-UP: " + S("SKIN-T").replace("[AGE-FEATURES]", c["age"])
    ndf = S("NEG-DEFAULT-FACE")
    if c.get("pro"):                          # §19B: drop the last two clauses
        ndf = ndf.replace(", no soft agreeable features throughout, not a face that could advertise anything", "")
    neg = ", ".join([S("NEG-SHEET"), S("NEG-GRID"), S("NEG-FILE"), ndf])
    return "\n\n".join([S("CAM-LOCK"), sheet, skin, S("CAP-SHARP"), S("CAP-FILE"), "AVOID: " + neg + "."])

out = {}
for k, c in CAST.items():
    p = build(k, c); out[k] = p
    pathlib.Path(f"{k}.prompt.txt").write_text(p)
    print(k, len(p))
json.dump(out, open("prompts.json", "w"), indent=1)
