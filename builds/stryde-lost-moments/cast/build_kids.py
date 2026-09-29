#!/usr/bin/env python3
"""§19 sheets for the two grandchildren in variant E (recurring: HK-E, E-04, E-08). Children: no SKIN-T
(its adult age-wear clauses do not apply) and no NEG-DEFAULT-FACE (its retiree clauses do not apply)."""
import re, pathlib, json
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
KIDS = {
 "GK1-AMARA": dict(sex="GIRL", side="right", wall="warm beige", floor="honey oak laminate",
   face="A round face with full cheeks, big bright dark-brown eyes, a small button nose and a wide mouth. A gap where one front tooth is missing shows only if she speaks, and a small healed graze on her left knee — her one marker. The right dimple is deeper than the left",
   hair="Black natural hair in two puffs high on the head held with yellow bobbles, the same height and the same bobbles in every panel",
   body="A Black British girl of Caribbean heritage. Small and slight, six years old",
   ward="A yellow long-sleeve T-shirt with no print, blue denim dungaree shorts and white trainers with pink laces"),
 "GK2-TOBI": dict(sex="BOY", side="right", wall="warm beige", floor="honey oak laminate",
   face="A round chubby face with soft cheeks, wide dark-brown eyes with long lashes, a flat little nose and a small mouth. A small pale crescent scar on his chin from a fall — his one marker. The left ear sits slightly higher than the right",
   hair="Very short black natural hair cut close, the same in every panel",
   body="A Black British boy of Caribbean heritage. Sturdy and small, four years old",
   ward="A red-and-navy striped T-shirt, navy jogging shorts and blue velcro trainers"),
}
def build(k, c):
    sheet = S("AVATAR-SHEET")
    first, rest = sheet.split(". ", 1)
    sheet = first + ". " + S("SHEET-GRID") + " " + rest
    for a, b in [("[WOMAN/MAN]", c["sex"]), ("[FACE — architecture in three or four plain sentences, the one marker, the asymmetries]", c["face"]),
                 ("[HAIR — colour, roots, how worn, the same tone and the same height in every panel]", c["hair"]),
                 ("[BODY — build, height impression]", c["body"]), ("[WARDROBE — BASE, LOWER, FOOT]", c["ward"]),
                 ("[SIDE]", c["side"]), ("[WALL COLOUR]", c["wall"]), ("[FLOOR]", c["floor"])]:
        sheet = sheet.replace(a, b)
    assert "[" not in sheet, k
    skin = "IN THE FACE CLOSE-UP: a child's skin as a phone renders it in window light — soft but not airbrushed, fine vellus hair catching the light on the cheek, a little dryness at the corners of the lips, a faint shine on the forehead and the tip of the nose, natural uneven tone around the eyes."
    neg = ", ".join([S("NEG-SHEET"), S("NEG-GRID"), S("NEG-FILE")]) + ", no adult, no older face, no makeup, no posed smile, no stock-photo child, no catalogue child model"
    return "\n\n".join([S("CAM-LOCK"), sheet, skin, S("CAP-SHARP"), S("CAP-FILE"), "AVOID: " + neg + "."])
for k, c in KIDS.items():
    p = build(k, c); pathlib.Path(f"{k}.prompt.txt").write_text(p); print(k, len(p))
