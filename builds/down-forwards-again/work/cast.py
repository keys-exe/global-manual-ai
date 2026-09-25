from lib import *
CAST = {
 "DR": dict(sex="MAN", side="left",
  face=("A long narrow face with a high forehead, deep-set grey-green eyes under a low heavy brow, a long nose with an old break that kinks it slightly to his left at the bridge, thin lips, a small receding chin and hollow cheeks; the left eye sits a touch lower than the right. His one marker is that broken nose"),
  hair=("Short salt-and-pepper hair that is still mostly dark, cropped close at the sides, thinning at the crown with scalp showing through, a clean side parting on the left, the same tone and the same length in every panel"),
  body="Wiry and small, about five foot seven, narrow shoulders, slightly round-shouldered from years bent over an examination couch, sixty-one years old",
  wardrobe=("A creased white cotton doctor's coat, open, sleeves pushed a little up the forearms, over a pale blue open-neck shirt with a soft collar, charcoal wool trousers, scuffed brown leather lace-up shoes, a grey stethoscope hung round the neck with its chest-piece resting on the left of the coat"),
  wall="pale grey-green", floor="worn grey linoleum floor",
  age=("deep vertical lines between the brows, three horizontal forehead creases, crow's feet fanning from both eyes, deep nasolabial folds, a scatter of faint sun freckles across the cheekbones, a small broken capillary beside the left nostril, loose crepey skin at the throat")),
 "PT": dict(sex="WOMAN", side="left",
  face=("A broad round face with a heavy soft jaw, small hooded brown eyes, a short wide nose, full lips that turn down slightly at the corners at rest, full cheeks, and a small dark raised mole just beside her left nostril; her right eyebrow sits a little higher than her left. Her one marker is that mole"),
  hair=("Chin-length hair grown out from an old auburn dye, two inches of silver-white roots against faded copper ends, pushed behind the ears, a little flat at the crown, the same tone and the same length in every panel"),
  body=("Heavyset and short, about five foot two, broad hips, soft upper arms, a slight forward stoop, seventy-one years old; the left knee a little broader and knobblier than the right"),
  wardrobe=("A heather-grey wool cardigan buttoned over a cream cotton blouse, a plain navy jersey skirt ending a hand's width above the knee so both knees are bare, bare legs, flat brown leather slip-on shoes"),
  wall="magnolia", floor="beige carpet",
  age=("deep crow's feet, soft sagging jowls, marionette lines from the mouth corners, a loose double chin, crepey upper eyelids, age spots across the forehead and cheekbones, fine broken capillaries across both cheeks")),
}
def sheet(c):
    body = S("AVATAR-SHEET")
    first, rest = body.split(". ", 1)
    body = first + ". " + S("SHEET-GRID") + " " + rest
    body = (body.replace("[WOMAN/MAN]", c["sex"])
        .replace("[FACE — architecture in three or four plain sentences, the one marker, the asymmetries]", c["face"])
        .replace("[HAIR — colour, roots, how worn, the same tone and the same height in every panel]", c["hair"])
        .replace("[BODY — build, height impression]", c["body"])
        .replace("[WARDROBE — BASE, LOWER, FOOT]", c["wardrobe"])
        .replace("[SIDE]-hand", c["side"]+"-hand").replace("[SIDE]", c["side"])
        .replace("[WALL COLOUR]", c["wall"]).replace("[FLOOR]", c["floor"]))
    assert "[" not in body, body[body.index("["):][:80]
    skin = "In the face close-up panel: " + S("SKIN-T").replace("[AGE-FEATURES]", c["age"])
    negs = ", ".join([S("NEG-SHEET"), S("NEG-GRID"), S("NEG-FILE"), S("NEG-DEFAULT-FACE")])
    return " ".join([S("CAM-LOCK"), body, skin, S("CAP-SHARP"), S("CAP-FILE"), S("BODY-WHOLE"), "Avoid: " + negs + "."])
if __name__ == "__main__":
    for k,c in CAST.items():
        p = sheet(c); open(f"../beats/CAST-{k}.t2i.txt","w").write(p); print(k, len(p))
