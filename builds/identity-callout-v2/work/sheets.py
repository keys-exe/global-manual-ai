from lib import A, ncount, BUILD
import json
open_sentence, rest = A("AVATAR-SHEET").split("the same face as the front panel, closer. ",1)
CAST = {
 "S1-CAROL": dict(sex="WOMAN", side="left",
  face="A broad, heavy-jawed face with a low brow and small deep-set blue-grey eyes; a short, slightly bumpy nose; thin lips that turn down a little at the corners. Her one marker: the left upper eyelid droops noticeably lower than the right, in every panel. The face is not symmetrical — the right cheek is fuller and the jaw sits slightly to the left.",
  hair="Grown-out home-dyed auburn hair, shoulder length, with two inches of flat grey roots at the parting, tucked behind both ears, the same tone and the same length in every panel",
  body="A stocky, broad-hipped White British woman of sixty-four, about five foot three, soft round shoulders, thick calves, a real middle-aged belly",
  ward="A faded teal cotton crew-neck T-shirt, stone-coloured cotton shorts ending mid-thigh so both knees are fully bare, and scuffed white canvas plimsolls with no socks showing",
  wall="magnolia", floor="worn oatmeal carpet",
  age="deep crow's feet at both eyes, two heavy horizontal creases across the low forehead, deep nasolabial folds, marionette lines at the mouth corners, slack crepe under the eyes, broken capillaries across both cheeks and the nose, faded sun freckling on the cheekbones"),
 "S2-HARGREAVES": dict(sex="MAN", side="right",
  face="A long, narrow face with a high forehead, a prominent hooked nose and hooded grey eyes set close together; a small receding chin under the beard. His one marker: a thickened cauliflower left ear from years of rugby, in every panel. The face is uneven — the left eye sits a touch lower, and the nose bends very slightly to the right.",
  hair="Salt-and-pepper hair, still mostly dark, cut short at the sides and thinning on top with scalp showing through, and a short trimmed full beard of the same tone, the same in every panel",
  body="A tall, slightly stooped, rangy White British man of fifty-eight, long arms, narrow shoulders rolled forward from years bent over an operating table",
  ward="A pale blue cotton shirt with the sleeves rolled to the forearms, no tie, navy chino trousers, dark brown leather brogues",
  wall="pale grey", floor="grey vinyl flooring",
  age="deep vertical frown lines between the brows, crow's feet, sagging upper eyelids, deep creases from nose to beard, weathered ruddy cheeks, a few broken capillaries on the nose"),
 "S3-HANNAH": dict(sex="WOMAN", side="left",
  face="A small, sharp, freckled face with high flat cheekbones, pale green eyes slightly prominent, a thin straight mouth and a pointed chin. Her one marker: a nose broken once and set crooked, bending visibly to the left below the bridge, in every panel. The brows are uneven — the right one sits higher.",
  hair="Very short cropped bleached-blonde hair with a quarter inch of dark roots showing, the same tone in every panel",
  body="A wiry, small White British woman of thirty-four, about five foot two, lean runner's build, sinewy forearms",
  ward="A plain charcoal zip-neck sports top, black running tights to the ankle, grey trail running shoes",
  wall="white", floor="grey rubber gym flooring",
  age="dense ginger freckles across the nose and cheeks, faint lines at the eye corners from squinting outdoors, one or two fine forehead lines, slightly weathered sun-dry skin on the cheekbones"),
}
def sheet(c):
    body = (open_sentence + "the same face as the front panel, closer. ").replace("[WOMAN/MAN]", c["sex"])
    r = rest.replace("[FACE — architecture in three or four plain sentences, the one marker, the asymmetries]", c["face"])
    r = r.replace("[HAIR — colour, roots, how worn, the same tone and the same height in every panel]", c["hair"])
    r = r.replace("[BODY — build, height impression]", c["body"])
    r = r.replace("[WARDROBE — BASE, LOWER, FOOT]", c["ward"])
    r = r.replace("[SIDE]", c["side"]).replace("[WALL COLOUR]", c["wall"]).replace("[FLOOR]", c["floor"])
    # SHEET-GRID pasted verbatim directly after the opening sheet sentence
    first, after = body.split(". ", 1)
    p = " ".join([A("CAM-LOCK"), first + ".", A("SHEET-GRID"), after + r,
                  A("SKIN-T").replace("[AGE-FEATURES]", c["age"]), A("CAP-SHARP"), A("CAP-FILE")])
    neg = ", ".join([A("NEG-SHEET"), A("NEG-GRID"), A("NEG-FILE"), A("NEG-DEFAULT-FACE")])
    return (p + "\n\nNegative: " + neg).replace(".. ", ". ")
out = {}
for k, c in CAST.items():
    s = sheet(c); assert "[" not in s, (k, s[s.index("["):s.index("[")+60])
    (BUILD/"beats"/f"{k}.sheet.t2i.txt").write_text(s); out[k] = ncount(s)
print(out)
