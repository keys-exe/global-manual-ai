from lib import s
LIVING = s("LOC-LIVING-DAY")
P1 = dict(
 type="1930s red-brick semi-detached",
 wall="woodchip wallpaper painted pale magnolia, a little yellowed", skirt="tall ogee-profile skirting painted white gloss, chipped at the corners",
 arch="moulded white-gloss architrave", door="four-panel oak-veneer internal doors with brass lever handles", ceiling="white textured Artex ceiling with a plain pendant bulb shade",
 floor="a worn brown-and-cream patterned hall carpet running up the stairs, changing to a beige carpet with a brass threshold strip at the front-room doorway",
 rad="a white steel panel radiator under a small window", sw="cream plastic switches and sockets, one with a hairline crack")
def shell(p):
    t = s("PROP-SHELL")
    for a,b in [("[WALL FINISH AND COLOUR]",p["wall"]),("[SKIRTING — profile, height, colour]",p["skirt"]),("[ARCHITRAVE]",p["arch"]),("[INTERNAL DOOR — style, colour, handle]",p["door"]),("[CEILING]",p["ceiling"]),("[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]",p["floor"]),("[RADIATOR TYPE]",p["rad"]),("[SWITCHES AND SOCKETS]",p["sw"])]:
        t = t.replace(a,b)
    assert "[" not in t; return t
def plateprop(p):
    t = s("PLATE-PROP")
    for a,b in [("[TYPE AND ERA]",p["type"]),("[WALL FINISH AND COLOUR]",p["wall"]),("[SKIRTING]",p["skirt"]),("[ARCHITRAVE]",p["arch"]),("[INTERNAL DOOR AND HANDLE]",p["door"]),("[CEILING]",p["ceiling"]),("[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]",p["floor"]),("[RADIATOR]",p["rad"]),("[SWITCHES AND SOCKETS]",p["sw"])]:
        t = t.replace(a,b)
    assert "[" not in t; return t
NEG = lambda *k: ", ".join(s(x) for x in k)
PROPREF = s("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", "the pale magnolia woodchip walls, the white ogee skirting, the oak-veneer panel doors with brass levers and the worn brown-and-cream patterned carpet")
PLATES = {}
PLATES["P1-PROP"] = " ".join([s("CAM-LOCK"), plateprop(P1),
 "The staircase rises on the left: a straight flight of thirteen steps with the patterned carpet held by brass stair rods, a plain white-painted spindle banister with a dark varnished handrail on the open side, and bare wall on the other side with NO rail fixed to it. On the right, the open door into the front room shows a slice of beige carpet and the corner of a floral armchair. A wooden coat hook board by the door with two coats on it, a small telephone table with a cordless phone.",
 "Daylight through the front door's frosted glass panel behind the camera and through the front-room doorway, the hall a stop darker toward the back, highlights clipping on the gloss skirting, no sensor noise — bright capture is clean.",
 s("PHYS-FRAME-C"), s("CAP-A"), s("CAP-FILE"),
 "\n\nNegative: " + NEG("NEG-PROP","NEG-M1") + ", no people, no product, no stairlift, no grab rails on the wall side"])
PLATES["P1-FRONT"] = " ".join([s("CAM-LOCK"), PROPREF, shell(P1),
 "THE FRONT ROOM of this house, seen from its doorway: a square room with a bay window on the far wall looking onto the street, net curtains and heavy green velvet curtains tied back. ANCHORS: the floral chintz armchair by the bay with a crocheted blanket over its arm, the tiled 1930s fireplace with a gas fire and a carriage clock on the mantel, the dark wood display cabinet of china against the left wall, a brass standard lamp. The room has been rearranged for living downstairs: a single divan bed with a pale blue candlewick bedspread pushed against the right-hand wall where a sofa used to be, its dents still in the carpet, a bedside cabinet holding a glass of water, a pill organiser and reading glasses.",
 s("VIEW-OUT").replace("[WHAT THE PROPERTY'S EXTERIOR SHOWS FROM THIS ROOM'S SIDE, NAMED]", "the privet hedge, the low brick front wall and the red-brick semis across the street"),
 LIVING.replace("camera-left", "from the bay on the far wall"), s("PHYS-FRAME-C"), s("CAP-A"), s("CAP-FILE"),
 "\n\nNegative: " + NEG("NEG-PROP","NEG-M1") + ", no people, no product, no hospital bed, no staged room"])
PLATES["WORK"] = " ".join([s("CAM-LOCK"),
 "An empty single-car garage converted into a joiner's workshop, seen chest-high from about a metre and a half away, as a phone propped on a bench would see it: the back wall is a pegboard of hand tools hanging on hooks — tenon saws, a spirit level, squares, a claw hammer, chisels in a canvas roll — above a long scarred workbench. ANCHORS: offcut lengths of varnished oak and pale pine handrail standing on end in the corner to the right, a row of brass and chrome handrail brackets in a plastic tray on the bench, a battered yellow cordless drill on its charger, a fluorescent tube light switched off. A plain wooden stool stands in the middle of the frame in front of the bench, empty, where a person would sit. Sawdust in the corners of the grey painted concrete floor.",
 "THE LIGHT: one small side window to camera-left at about forty-five degrees, low afternoon daylight coming in across the stool and the bench, the right side of the garage falling a stop under into warm brown shadow, the window edge blowing to white, no overhead light on. Ambient palette warm brown timber and grey, the only cool note the daylight on the pegboard.",
 s("PHYS-FRAME-C"), s("CAP-A"), s("CAP-FILE"),
 "\n\nNegative: " + NEG("NEG-M1") + ", no people, no product, no logos, no brand names on tools, no text, no posters, no clean showroom workshop"])
PLATES["VAN"] = " ".join([s("CAM-LOCK"),
 "The inside of a white panel van's load area seen from its open sliding side door, a working tradesman's van: plywood-lined walls, a steel shelving unit bolted along one side holding clear plastic organiser boxes of screws, brackets and wall plugs, lengths of wooden handrail strapped along the other wall with a ratchet strap, a battered black tool bag on the floor, a spirit level, a tape measure and a folded dust sheet. ANCHORS: the steel shelving with the organiser boxes, the strapped handrail lengths, the black tool bag. Daylight from the open side door behind the camera falling into the van and fading to shadow at the bulkhead.",
 s("LOC-EXT-OVERCAST"), s("PHYS-FRAME-C"), s("CAP-A"), s("CAP-FILE"),
 "\n\nNegative: " + NEG("NEG-M1") + ", no people, no product, no logos, no brand names, no text, no signwriting"])
PLATES["C2-HALL"] = " ".join([s("CAM-LOCK"),
 "The hall and staircase of a 1990s brick detached house seen from the front door: a straight flight of fourteen stairs rising away with light oak-effect laminate treads and white risers, a white-painted square-spindle banister with a pale pine handrail on the open side, plain magnolia walls, white skirting. ANCHORS: a framed print of a harbour at sunset on the stair wall halfway up, a pair of walking boots on a rubber mat by the bottom step, a tall green plant in a white pot at the foot of the stairs, a radiator with a shelf and a dish of keys. Light oak laminate floor in the hall.",
 "Daylight from a tall landing window at the top of the stairs and the glass panel of the front door behind the camera, the stairs bright, the hall under the stairs a stop darker, highlights clipping on the white risers, no sensor noise — bright capture is clean.",
 s("PHYS-FRAME-C"), s("CAP-A"), s("CAP-FILE"),
 "\n\nNegative: " + NEG("NEG-M1") + ", no people, no product, no stairlift, no text"])
if __name__ == "__main__":
    for k,v in PLATES.items():
        open(f"../renders/{k}_plate.prompt.txt","w").write(v); print(k, len(v))
