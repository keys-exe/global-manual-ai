from lib import *
PROP = dict(
 type="1930s semi-detached British suburban",
 wall="magnolia emulsion walls, slightly scuffed at hand height",
 skirt="tall white-gloss ogee skirting boards, the gloss yellowed and chipped",
 arch="plain white-gloss moulded architraves",
 door="four-panel internal doors painted white gloss with brass lever handles on round roses",
 ceiling="a white Artex ceiling with a swirl pattern and a plain brass pendant with a cream fabric shade",
 floor="beige wool-mix carpet running through the hall and up the stairs, changing to a brass threshold strip and oak-effect laminate at the kitchen door",
 rad="white single-panel steel radiators with chrome valves",
 sw="white plastic square switches and double sockets, slightly yellowed",
)
DAYLIGHT = ("Grey British daylight, overcast, mid-morning, entering only through the windows and door glass, cool and flat, "
            "the far end of each room falling a stop darker, the interior lights off.")
def shell():
    return (S("PROP-SHELL").replace("[WALL FINISH AND COLOUR]",PROP["wall"]).replace("[SKIRTING — profile, height, colour]",PROP["skirt"])
      .replace("[ARCHITRAVE]",PROP["arch"]).replace("[INTERNAL DOOR — style, colour, handle]",PROP["door"]).replace("[CEILING]",PROP["ceiling"])
      .replace("[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]",PROP["floor"]).replace("[RADIATOR TYPE]",PROP["rad"]).replace("[SWITCHES AND SOCKETS]",PROP["sw"]))
def prop_plate():
    b=(S("PLATE-PROP").replace("[TYPE AND ERA]",PROP["type"]).replace("[WALL FINISH AND COLOUR]",PROP["wall"]).replace("[SKIRTING]",PROP["skirt"])
      .replace("[ARCHITRAVE]",PROP["arch"]).replace("[INTERNAL DOOR AND HANDLE]",PROP["door"]).replace("[CEILING]",PROP["ceiling"])
      .replace("[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]",PROP["floor"]).replace("[RADIATOR]",PROP["rad"]).replace("[SWITCHES AND SOCKETS]",PROP["sw"]))
    b += (" The staircase rises on the left: a straight flight of thirteen carpeted steps with a dark varnished pine handrail and white spindles on the open side, "
          "a narrow wall on the right. A small framed print of a harbour hangs above the radiator; a coir doormat lies behind the camera's feet; "
          "a wooden telephone table with a cordless phone stands by the stairs. The open doorway on the right leads into the living room.")
    assert "[" not in b
    negs=", ".join([S("NEG-PROP"),S("NEG-M1")])
    return " ".join([S("CAM-LOCK"),b,DAYLIGHT,S("PHYS-FRAME-C"),S("CAP-A"),S("CAP-FILE"),"Avoid: "+negs+"."])
CLINIC = ("A single photograph of a small, lived-in NHS-style musculoskeletal consulting room in an older British health centre, "
  "taken from a phone on a tripod at seated chest height facing the doctor's chair, empty, nobody in frame. "
  "The doctor's black mesh office chair stands centre-frame in front of pale grey-green painted walls with scuffs at chair height. "
  "Behind the chair and to the left, a window with white vertical blinds half-open, daylight coming in from the left. "
  "Behind the chair to the right, a grey-blue vinyl examination couch with a roll of white paper, a wall-mounted wash basin with an elbow tap, "
  "a paper-towel dispenser. On a cluttered wooden shelf above the couch: a plastic anatomical knee joint model, a stack of worn orthopaedic textbooks, "
  "a box of blue gloves, a spider plant going brown at the tips. A cork noticeboard with curled leaflets and a hand-drawn diagram pinned to it. "
  "Grey-blue carpet tiles. Nothing tidied for the photograph, nothing arranged.")
def clinic_plate():
    negs=", ".join([S("NEG-M1")])
    return " ".join([S("CAM-LOCK"),CLINIC,"Grey British daylight through the blinds from the left, the right side of the room a stop under, the ceiling strip light off.",
                     S("PHYS-FRAME-C"),S("CAP-A"),S("CAP-FILE"),"Avoid: "+negs+", no text on the leaflets readable, no logos, no posters with words."])
if __name__=="__main__":
    for n,f in (("PLATE-PROP",prop_plate),("PLATE-CLINIC",clinic_plate)):
        p=f(); open(f"../beats/{n}.t2i.txt","w").write(p); print(n,len(p))
