from lib import A, ncount, BUILD
PROP = {
 "TYPE AND ERA": "1930s pebble-dashed semi-detached",
 "WALL FINISH AND COLOUR": "magnolia emulsion walls with a faint roller texture, scuffed grey at hand height",
 "SKIRTING": "tall white-gloss ogee skirting boards, the gloss yellowed and chipped along the top edge",
 "ARCHITRAVE": "plain moulded white-gloss architraves",
 "INTERNAL DOOR AND HANDLE": "white-painted four-panel internal doors with brushed brass lever handles",
 "CEILING": "a white Artex swirl ceiling with a plain white pendant lampshade",
 "FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD": "oatmeal twist carpet running up the stairs, meeting a brass threshold strip at the front door mat",
 "RADIATOR": "a white single-panel steel radiator with chrome valves",
 "SWITCHES AND SOCKETS": "white plastic switches and sockets gone faintly yellow",
}
CARRIED = "magnolia walls, yellowed white-gloss ogee skirting, white four-panel doors with brass levers, Artex ceiling, oatmeal twist carpet"
STAIRS = ("The staircase is a straight flight rising along the LEFT wall as seen from the front door, oatmeal carpet on every tread, "
          "a dark-stained wooden handrail on white-painted square spindles on its open right side, a framed seaside print on the wall above the third step; "
          "the open doorway on the RIGHT leads into the front living room.")
DAY = ("Soft late-morning daylight through the frosted glass of the front door behind the camera and through the living-room doorway on the right, "
       "falling off down the hall to a dimmer back end, the brightest patch of carpet just inside the door blowing out a little, shadows open with detail held, "
       "no sensor noise in the bright areas. Ambient palette warm magnolia and oatmeal, slightly flat the way a phone renders an overcast British morning.")
def pp():
    s = A("PLATE-PROP")
    for k, v in PROP.items(): s = s.replace("[%s]" % k, v)
    p = " ".join([A("CAM-LOCK"), s, STAIRS, DAY, A("PHYS-FRAME-C"), A("CAP-A"), A("CAP-FILE")])
    n = ", ".join([A("NEG-PROP"), A("NEG-SCENE"), A("NEG-M1"), "no people, no product, no text, no house numbers"])
    return p + "\n\nNegative: " + n
def shell():
    s = A("PROP-SHELL")
    s = s.replace("[WALL FINISH AND COLOUR]", PROP["WALL FINISH AND COLOUR"]).replace("[SKIRTING — profile, height, colour]", PROP["SKIRTING"])
    s = s.replace("[ARCHITRAVE]", PROP["ARCHITRAVE"]).replace("[INTERNAL DOOR — style, colour, handle]", PROP["INTERNAL DOOR AND HANDLE"])
    s = s.replace("[CEILING]", PROP["CEILING"]).replace("[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]", "oatmeal twist carpet through the hall, stairs and living room")
    s = s.replace("[RADIATOR TYPE]", PROP["RADIATOR"]).replace("[SWITCHES AND SOCKETS]", PROP["SWITCHES AND SOCKETS"])
    return s
def propref():
    return A("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", CARRIED)
LIVING_ANCHORS = ("the front living room: a bay window with white net curtains on the far wall, a worn brown leather two-seater sofa against the left wall "
    "with a crocheted granny-square blanket over its arm, a dark wooden nest of tables beside it with a mug on top, a gas fire with a cream stone surround "
    "and a carriage clock on the mantel on the right wall, a brass standard lamp in the corner by the bay")
LIVING_LIGHT = ("Broad overcast daylight through the bay window on the far wall, filling the room evenly, shadows open and soft, the net curtains and window glowing and "
    "blowing out, a faint warm bounce off the oatmeal carpet. No sensor noise. Palette natural and slightly cool from the window, warmed by the beige sofa and the wooden side table.")
VIEW_LIVING = A("VIEW-OUT").replace("[WHAT THE PROPERTY'S EXTERIOR SHOWS FROM THIS ROOM'S SIDE, NAMED]",
    "the small front garden's low privet hedge and the pebble-dashed semis across a quiet residential street")
def living_plate():
    p = " ".join([A("CAM-LOCK"), propref(), shell(),
        "A single photograph of " + LIVING_ANCHORS + ", taken from the doorway from the hall, looking across the room toward the bay window.",
        VIEW_LIVING, LIVING_LIGHT, "Empty — nobody in frame, no product, nothing staged, nothing tidied for the photograph.",
        A("PHYS-FRAME-C"), A("CAP-A"), A("CAP-FILE")])
    n = ", ".join([A("NEG-SCENE"), A("NEG-PROP"), A("NEG-M1"), "no people, no product, no text"])
    return p + "\n\nNegative: " + n
CLINIC_ANCHORS = ("a British NHS-style orthopaedic consulting room: a grey padded examination couch with a roll of white paper along the right wall, "
    "a light box with no film on it above the couch, a pale wooden desk under the window on the left wall with a computer monitor turned away and a plastic anatomical knee-joint model, "
    "a blue plastic visitor chair, a hand-washing sink with a steel mixer tap in the far corner, a blue privacy curtain on a ceiling rail half drawn")
CLINIC_LIGHT = ("Cool overcast daylight from the window on the left mixing with flat overhead fluorescent panels, shadows shallow, the window blowing out white, the paper on the couch clipping. "
    "No sensor noise. Palette cool clinical greys and pale blues, the wooden desk the only warm element.")
def clinic_plate():
    p = " ".join([A("CAM-LOCK"), "A single photograph of " + CLINIC_ANCHORS + ", taken from just inside the door, looking across the room toward the window wall.",
        CLINIC_LIGHT, "Empty — nobody in frame, no product, nothing staged, a lived-in working room with a few papers and a box of gloves out.",
        A("PHYS-FRAME-C"), A("CAP-A"), A("CAP-FILE")])
    n = ", ".join([A("NEG-SCENE"), A("NEG-M1"), "no people, no product, no readable text, no posters with writing, no screens showing data, no hospital logos"])
    return p + "\n\nNegative: " + n
if __name__ == "__main__":
    for k, f in [("PLATE-PROPERTY", pp), ("PLATE-LIVING", living_plate), ("PLATE-CLINIC", clinic_plate)]:
        s = f(); assert "[" not in s, (k, s[s.index("["):][:80]); (BUILD/"beats"/f"{k}.t2i.txt").write_text(s); print(k, ncount(s))
