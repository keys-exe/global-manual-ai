from lib import *
from plates import PROP, DAYLIGHT, shell
def propref():
    return S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]",
      "magnolia walls, white-gloss ogee skirting and architraves, white four-panel doors with brass levers, Artex ceiling, beige wool-mix carpet, single-panel radiators")
LOCS = {
 "STAIRS": ("THE STAIRS, seen from the landing at the top looking straight down the straight flight of thirteen carpeted steps to the hall below: "
   "the dark varnished pine handrail and white spindles on the left, the magnolia wall on the right with a second small framed print, "
   "the front door with its patterned glass at the bottom of the flight glowing with daylight, the telephone table just visible at the foot. "
   "The carpet on the treads is worn paler in the middle of each step. Empty, nobody in frame."),
 "LIVING": ("THE LIVING ROOM, off the hall, seen from the doorway: a high-backed wing armchair in faded green velour with wooden arms and a crocheted "
   "antimacassar sits angled toward a small television, a side table beside it with a mug and a pair of reading glasses, a brown three-seater sofa "
   "under the bay window on the left wall, net curtains in the bay, a gas fire with a wooden surround, family photographs in frames on the mantelpiece, "
   "a walking stick leaning on the armchair. Empty, nobody in frame."),
 "GARDEN": ("THE BACK GARDEN of the same house, seen from the back door step: a narrow lawn slightly overgrown, a concrete path down the left, "
   "raised timber vegetable beds gone to weed, a greenhouse with a cracked pane at the far end, a wooden fence with a neighbour's sycamore beyond, "
   "the brick back wall of the semi-detached house at the right edge with a white UPVC window. A garden fork left standing in one bed. Empty, nobody in frame."),
}
DL = {"STAIRS":DAYLIGHT, "LIVING":"Grey British daylight through the net curtains of the bay window on the left, soft and cool, the right side of the room a stop under, the lamps off.",
      "GARDEN":"Overcast British morning daylight, flat and cool, the grass damp, no sun."}
def loc_plate(k):
    head = propref()+" "+shell() if k!="GARDEN" else "The back garden of THE SAME HOUSE as the attached property reference image, a 1930s semi-detached British suburban house."
    negs=S("NEG-PROP")+", no warped background, no CGI look, no fake commercial gloss, no over-saturated colors, no film grain, no vignette, no darkened corners, no moody dark grade"
    return " ".join([S("CAM-LOCK"),head,LOCS[k],DL[k],S("PHYS-FRAME-C"),S("CAP-A"),S("CAP-FILE"),"Avoid: "+negs+"."])
DR_AGE=("deep vertical lines between the brows, three horizontal forehead creases, crow's feet fanning from both eyes, deep nasolabial folds, a scatter of faint sun freckles across the cheekbones, a small broken capillary beside the left nostril, loose crepey skin at the throat")
def th_seed():
    subj=("THE SAME MAN exactly as in the attached character reference sheet -- sixty-one, wiry and small, a long narrow face with deep-set grey-green eyes under a low heavy brow, "
      "a long nose with an old break kinking it slightly to his left, short salt-and-pepper hair thinning at the crown -- unchanged in face, age and build, "
      "in the same creased open white doctor's coat over a pale blue open-neck shirt, a grey stethoscope round his neck. He sits in the black mesh chair of the attached consulting room, "
      "square to the phone, forearms resting on his thighs, hands loosely together in his lap below the frame's lower third, looking straight into the lens, about to speak, "
      "eyebrows level, a flat serious mouth.")
    scene=S("SCENE-REF").split(" — but seen")[0].replace("[LOCATION]","CONSULTING ROOM").replace("[the location's named anchors, stated in one clause]",
      "the half-open white vertical blinds on the window to the left, the grey-blue examination couch and wash basin to the right, the wooden shelf with the knee model and textbooks") + \
      " -- seen from the same tripod position as the reference, at his seated eye height."
    frame=("A talking-head video frame: phone on a tripod at his eye height about a metre and a half away, vertical 9:16, the man centred, framed from just above the top of his head to mid-chest, "
      "his head in the upper third, the room behind him readable and a little soft. ")+S("FRAME-SCALE").replace("[SCALE]","head and shoulders, about half")
    skin=S("SKIN-A").replace("[AGE-FEATURES]",DR_AGE)
    negs=", ".join([S("NEG-M1"),S("NEG-SKIN"),S("NEG-BODY")])
    return " ".join([S("CAM-LOCK").replace("handheld","on a small tripod"),frame,subj,scene,"Grey British daylight through the blinds from the left, raking across the left side of his face, the right side in open shadow lifted by the pale walls.",
       skin,S("TEETH-A"),S("BODY-WHOLE"),S("CAP-A"),S("CAP-FILE"),"Avoid: "+negs+"."])
if __name__=="__main__":
    for k in LOCS:
        p=loc_plate(k); open(f"../beats/PLATE-{k}.t2i.txt","w").write(p); print(k,len(p))
    p=th_seed(); open("../beats/TH-DR-SEED.t2i.txt","w").write(p); print("TH",len(p))
