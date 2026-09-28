from lib import s
import json
AV = s("AVATAR-SHEET")
CAST = {
 "N": dict(sex="MAN", side="left", wall="warm off-white", floor="worn grey vinyl floor",
  face="Sixty-one, white British, a long face with a heavy brow ridge and deep-set grey-blue eyes set slightly close together. The nose was broken once and bends a little to his left at the bridge; a wide thin-lipped mouth with a deep crease from each nostril to the mouth corners; a squared, slightly uneven jaw, the left side fuller. The one marker: a short pale scar cutting through the outer end of his right eyebrow, leaving a gap in the brow hairs. Weathered, ruddy outdoor skin across the cheeks and nose, deep crow's feet, three horizontal forehead creases, grey stubble two days old",
  hair="Close-cropped grey hair, darker pepper-grey at the sides, receding into two deep bays at the temples, cut short with clippers, the same tone and length in every panel",
  body="Stocky and broad-shouldered, a slight belly, thick forearms and square workman's hands, about five foot ten, standing easy with his weight a little on the left leg",
  ward="A faded navy half-zip work fleece with no logo over a grey crew-neck T-shirt, dark charcoal work trousers with a hammer loop and slim knee-pad pockets, scuffed tan leather work boots",
  age="the deep nasolabial creases, the crow's feet and the weathered ruddy cheeks"),
 "C1": dict(sex="WOMAN", side="right", wall="pale sage green", floor="beige carpet",
  face="Seventy-four, white British, a small round face with full soft cheeks that have dropped into jowls along the jaw, hooded pale brown eyes under thin arched brows, a short broad nose with a rounded tip, thin lips that turn down very slightly at one corner. The one marker: a flat brown mole on her left cheekbone the size of a lentil. Fine pale papery skin, freckled across the forehead and backs of the hands, a vertical crease between the brows, fine lines over the top lip",
  hair="Fine white hair cut short and set in soft loose curls close to the head, a little flat at the back, the same white in every panel",
  body="Small and soft-bodied, round-shouldered, about five foot one, standing with a slight forward stoop",
  ward="A lilac lambswool cardigan buttoned over a cream blouse, a navy pleated skirt ending just above the knee so both knees and the shins below them are bare, flat navy fleece-lined slippers",
  age="the jowls, the freckling and the fine lines above the lip"),
 "C2": dict(sex="MAN", side="left", wall="plain magnolia", floor="light oak laminate floor",
  face="Sixty-eight, white British, a wide square face with high flat cheekbones and small bright blue eyes under bushy salt-and-pepper brows, a fleshy bulbous nose with visible red capillaries, a full lower lip, a heavy double chin. The one marker: a white trimmed moustache, the rest of the face clean-shaven. Pink sun-reddened skin across the nose and the tops of the cheeks, deep pouches under the eyes, a crosshatch of lines across the forehead",
  hair="Thin white hair combed straight back over a pink scalp, thinning on the crown, the same tone in every panel",
  body="Heavyset, a big round belly and broad hips, thick legs, about five foot nine, standing solid with his feet apart",
  ward="A washed-out olive short-sleeved polo shirt, khaki cotton shorts ending just above the knee so both knees are bare, white sports socks and grey trainers",
  age="the pouches under the eyes, the red capillaries across the nose and the forehead crosshatch"),
}
def sheet(k):
    c = CAST[k]
    p = AV
    p = p.replace("[WOMAN/MAN]", c["sex"]).replace("[FACE — architecture in three or four plain sentences, the one marker, the asymmetries]", c["face"])
    p = p.replace("[HAIR — colour, roots, how worn, the same tone and the same height in every panel]", c["hair"]).replace("[BODY — build, height impression]", c["body"])
    p = p.replace("[WARDROBE — BASE, LOWER, FOOT]", c["ward"]).replace("[SIDE]", c["side"]).replace("[WALL COLOUR]", c["wall"]).replace("[FLOOR]", c["floor"])
    assert "[" not in p, p[p.index("["):p.index("[")+60]
    first, rest = p.split(". ", 1)
    skin = s("SKIN-T").replace("[AGE-FEATURES]", c["age"])
    pos = " ".join([s("CAM-LOCK"), first + ". " + s("SHEET-GRID"), rest, "In the face close-up panel: " + skin, s("CAP-SHARP"), s("CAP-FILE")])
    neg = ", ".join([s("NEG-SHEET"), s("NEG-GRID"), s("NEG-FILE"), s("NEG-DEFAULT-FACE")])
    return pos + "\n\nNegative: " + neg
if __name__ == "__main__":
    import sys
    for k in CAST:
        t = sheet(k); open(f"../renders/{k}_sheet.prompt.txt","w").write(t); print(k, len(t))
