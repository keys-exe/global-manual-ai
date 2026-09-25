# §35 Kling B-roll JSON per beat, minified, ≤2,500 chars (E1). Motion = §27A CONTINUING, COMPLETING, UNRESOLVED.
import json
from lib import A, PS, BUILD
from seeds import F
from lib import P
NEG_WARP_C = A("NEG-WARP-C"); M1_SEL = "no AI face, no plastic skin, no CGI look, no fake commercial gloss, no slow motion, no cut, no second shot"
NEG_PLACE_SEL = "no shell riding up over the kneecap, no product covering the kneecap face, no strap sliding down the shin, no product on the left knee, no second unit, no product rotating around the leg"
NEG_ORIENT_SEL = "no shell behind the leg, no wordmark changing letters, no band scalloped"
NOFACE = A("NEG-NOFACE")
def j(shot, subject, move, framing, motion, style, neg, lighting=None):
    d = {"shot": shot, "subject": subject, "camera": {"movement": move, "framing": framing}, "motion": motion,
         "lighting": lighting or A("INHERIT-CAP"), "style": style, "negatives": neg}
    return json.dumps(d, ensure_ascii=False, separators=(",", ":"))
IS = A("INHERIT-SUBJ"); HC = A("HOLD-C"); PM = A("PHYS-MOTION-C"); IF = A("IFACE-C")
DOC = "Documentation register, uncorrected phone file."
WORN = PS("PLACE-LOCK-C").split(" THAT FEATURE")[0]
B = {}
def add(bid, **k): B[bid] = j(**k)
add("HK1-01", shot="dreading_the_stairs", subject=IS, move=A("RIG-R1C"), framing="WIDE as in the start frame, stairs screen-left, front door behind camera.",
    motion="Already looking up the flight, her grip tightens on the rail and she shifts weight onto the left leg, then lifts the right foot onto the first tread and pauses there, knee bent, bracing, jaw tight, the second step not yet taken at the cut. " + HC + " " + PM,
    style=DOC, neg=NEG_WARP_C + ", " + M1_SEL)
add("HK2-01", shot="knee_wince_sofa", subject=IS, move=A("RIG-R1C"), framing="PROPPED as in the start frame, bay window camera-right.",
    motion="Already pressing both thumbs under the kneecap, she kneads slowly, winces harder and exhales through her nose, then shifts forward as if to stand and stops, hands still on the knee at the cut. " + HC + " " + PM,
    style=DOC, neg=NEG_WARP_C + ", " + M1_SEL)
add("HK3-01", shot="step_to_descent", subject=IS, move=A("RIG-R1C"), framing="WIDE low as in the start frame, looking up the stairs, handrail on her right.",
    motion="Already halfway down, she lowers her left foot onto the step beside her right, taking the weight gingerly on the rail, then leads with the right foot onto the next tread, knee bending slowly, weight held back, mid-step at the cut. " + HC + " " + PM,
    style=DOC, neg=NEG_WARP_C + ", " + M1_SEL)
add("B01", shot="foot_lands_tread", subject=IS, move=A("RIG-R1C"), framing="OTS low on the stairs as in the start frame, legs only, handrail top of frame.",
    motion="Already climbing, the right slipper lands on the tread and the bare knee bends and takes her weight slowly, the hand hauling on the rail, then the left foot starts to lift, still rising at the cut. " + HC + " " + PM,
    style=DOC, neg=NEG_WARP_C + ", " + M1_SEL + ", " + NOFACE)
add("B02", shot="load_arrives_knee", subject="The anatomical knee exactly as in the start frame: only the bones and the tendon, no muscle layer, the kneecap a smooth rounded bone.", move="Virtual camera already pushing in very slowly on frame one, no orbit, mechanically smooth. Still moving at the cut.", framing="Low three-quarter as in the start frame.",
    motion=F("Already moving on frame one: the thigh drives down into the bent knee at [LOAD-CADENCE], one arrival per second. ") + F(A("ANAT-LOAD").replace("[STACK] shortens and thickens as the load arrives, ", "")) + " Still loading at the cut. " + A("HOLD-AC"),
    style="Premium medical visualisation as in the start frame.", neg=A("NEG-EXTERNAL") + ", " + A("NEG-FLOW") + ", no muscle layer appearing, no red muscle, no ring, no disc, no new structures, no text", lighting="Exactly as in the start frame.")
add("B03", shot="site_throbs", subject="The knee exactly as in the start frame.", move=A("RIG-RVC"), framing="Low three-quarter as in the start frame.",
    motion=F(A("ANAT-SENSE-T")) + " " + A("HOLD-AC"),
    style="Premium medical visualisation as in the start frame.", neg=A("NEG-EXTERNAL") + ", " + A("NEG-FLOW") + ", no text", lighting="Exactly as in the start frame.")

HP = PS("HOLD-PC"); NWP = "no shell bending, no peaks rounding off, no notch filling in, no wordmark changing letters, no second product"
NSEAT = "no band being opened, no product being threaded, no twisted band, no additional hands, no product travelling past the kneecap, no shell riding up over the kneecap"
WN = NEG_WARP_C + ", " + NEG_PLACE_SEL + ", " + NEG_ORIENT_SEL + ", no slow motion, no cut"
def worn(bid, shot, framing, motion, move=None, noface=True, place=None):
    subj = IS + " " + (place or WORN).split(" --")[0].split(":")[0] + "."
    neg = WN + (", " + NOFACE if noface else "")
    add(bid, shot=shot, subject=subj, move=move or A("RIG-R1C"), framing=framing, motion=motion + " " + HP + " " + HC + " " + IF, style=DOC, neg=neg)
def held(bid, shot, framing, motion, noface=True):
    add(bid, shot=shot, subject=IS + " The strap is held in her hands, never worn.", move=A("RIG-R1C"), framing=framing,
        motion=motion + " " + HP + " " + HC + " " + PM, style=DOC, neg=NEG_WARP_C + ", " + NWP + (", " + NOFACE if noface else "") + ", no slow motion, no cut")
add("B04", shot="surgeon_fits_model", subject=IS, move=A("RIG-R1C"), framing="PROPPED as in the start frame, window behind him frame left.",
    motion="Already studying it, he presses the notched shell up under the model's kneecap, tilts the model a few degrees to check the fit, then nods slightly and starts to lift the strap away, still moving at the cut. " + HP + " " + HC,
    style=DOC, neg=NEG_WARP_C + ", " + NWP + ", " + M1_SEL)
add("B05", shot="seat_strap_up", subject=IS, move=A("RIG-R1C"), framing="CLOSE knee-down as in the start frame.",
    motion=PS("SEAT-LOCK").split(". ", 1)[1] + " " + HC,
    style=DOC, neg=NEG_WARP_C + ", " + NSEAT + ", " + NOFACE)
held("B06", "size_side_by_side", "CLOSE over the shoulder as in the start frame, hands in lap.",
    "Already holding both, she lifts the two straps a little toward the lens and brings them side by side, the thin generic one sagging over her fingers against the wide rigid shell, hands still turning at the cut.")
held("B07", "thumb_press_shell", "CLOSE as in the start frame, window light behind.",
    "Already pressing, her thumb pushes hard into the shell and it does not give, then she turns it a few degrees in the window light so the chrome slides catch, still turning at the cut.")
MOD6C = F(A("ANAT-MOD6-S")).replace(" The product's own cool tone brightens a fraction as each load is taken and settles between.", "")
PUSH = "Virtual camera already pushing in very slowly on frame one, no orbit, mechanically smooth. Still moving at the cut."
add("B08", shot="load_spread_off_site", subject="As in the start frame: the strap stays on the front of the knee every frame.", move=PUSH, framing="As in the start frame.",
    motion=MOD6C, style="As in the start frame.",
    neg=A("NEG-EXTERNAL") + ", " + A("NEG-FLOW"), lighting="As in the start frame.")
worn("B09", "gait_lab_watch", "OTS as in the start frame, Hannah's shoulder frame left, treadmill centre.",
    "Already walking steadily on the treadmill, Carol's strides roll on while Hannah ticks a line on her clipboard and glances back up at the knee, both still moving at the cut.", noface=False, place=WORN.split(" --")[0])
worn("B10", "walk_pavement_knee", "CLOSE as in the start frame.",
    "Already mid-stride, the right foot plants, the knee takes the weight, the strap stays put, the other leg swings past, still walking at the cut.")
add("B11", shot="push_up_off_sofa", subject=IS, move=A("RIG-R1C"), framing="PROPPED as in the start frame, bay window frame right.",
    motion="Already braced on both knees, she pushes and rises slowly off the sofa, face tight, a hand staying on the right knee as she straightens, not yet upright at the cut. " + HC + " " + PM, style=DOC, neg=NEG_WARP_C + ", " + M1_SEL)
add("B12", shot="kneel_garden", subject=IS, move=A("RIG-R1C"), framing="WIDE as in the start frame, garden behind.",
    motion="Already lowering, she leans on the fork and eases her left knee down onto the pad, the hand clamped on her right knee, wincing, still settling at the cut. " + HC + " " + PM, style=DOC, neg=NEG_WARP_C + ", " + M1_SEL)
worn("B13", "brisk_park_walk", "WIDE as in the start frame, park path toward camera.",
    "Already walking briskly toward the lens, arms swinging, she passes the bench and keeps coming, a small smile, still walking at the cut.", noface=False, place=WORN.split(" --")[0])
worn("B14", "climb_hands_free", "WIDE from the top landing as in the start frame, looking down the flight.",
    "Already climbing toward the lens, she takes the next tread with the right leg, the strapped knee bending and straightening under her weight, hands free at her sides, the left foot passing onto the next tread, still climbing at the cut.", noface=False, place=WORN.split(" --")[0])
worn("B15", "knee_loads_tread", "CLOSE as in the start frame.",
    "Already stepping, the strapped knee bends onto the tread and takes her full weight, the shell holding station as she rises, the other foot leaving the step at the cut.", place=PS("PLACE-BENT").split(" The shell's lower body")[0])
add("B16", shot="load_lands_on_shell", subject="As in the start frame: the strap stays on the front of the knee every frame.", move=PUSH, framing="As in the start frame.",
    motion=MOD6C, style="As in the start frame.",
    neg=A("NEG-EXTERNAL") + ", " + A("NEG-FLOW"), lighting="As in the start frame.")
held("B17", "draw_band_slide", "CLOSE as in the start frame, hands only.",
    "Already pinching the band tail, she draws it a couple of centimetres through the chrome slide, the coarse knit stretching and easing as it feeds, then gives it a small tug to snug it, still pulling at the cut.")
worn("B18", "kerb_step_holds", "CLOSE as in the start frame.",
    "Already stepping up, the right foot lands on the kerb, the strapped knee bends and drives her up, the strap holding station, the trailing foot lifting at the cut.", place=PS("PLACE-BENT").split(" The shell's lower body")[0])
add("B19", shot="hall_to_door_trousers", subject=IS, move=A("RIG-R1C"), framing="WIDE low from the stairs as in the start frame, front door ahead.",
    motion="Already walking briskly down the hall, her trousers swinging freely at the knee with nothing showing beneath, she reaches the door and takes hold of the latch, still opening it at the cut. " + HC + " " + PM, style=DOC,
    neg=NEG_WARP_C + ", " + P.NEG_CONCEAL + ", " + M1_SEL)
worn("B20", "surgeon_points_notch", "OTS from behind Carol's shoulder as in the start frame.",
    "Already crouched, he points to the notch under her kneecap, traces the shell's top edge with a fingertip without touching it, and nods, looking up at her, still nodding at the cut.", noface=False)
worn("B21", "high_street_walk", "WIDE as in the start frame, pavement toward camera, shoppers around.",
    "Already walking toward the lens through the shoppers, he strides on easily, the strapped knee flexing with each step, a woman with bags crossing behind him, still walking at the cut.", noface=False, place=WORN.split(" --")[0])
held("B22", "two_straps_offer", "CLOSE as in the start frame, window behind.",
    "Already holding one strap in each hand, she lifts both a little toward the lens and turns them together through the window light, chrome catching, band tails swinging with their weight, still turning at the cut.")
worn("B23", "flex_knee_easy", "PROPPED from the mantelpiece as in the start frame, bay window frame right.",
    "Already lifting the right leg, she straightens it out in front of her and bends it back easily, watching it, the small smile growing, lifting it again at the cut.", noface=False, place=PS("PLACE-BENT").split(" The shell's lower body")[0])
worn("B24", "descend_hands_free", "WIDE low from the hall as in the start frame, stairs coming toward camera.",
    "Already coming down, her right foot lands on the next tread, the strapped knee bending smoothly to take her weight, hands free, the left foot passing it to the tread below, still descending at the cut.", noface=False, place=PS("PLACE-BENT").split(" The shell's lower body")[0])
add("B25", shot="seat_strap_second_angle", subject=IS, move=A("RIG-R1C"), framing="CLOSE knee-down three-quarter from her right as in the start frame.",
    motion=PS("SEAT-LOCK").split(". ", 1)[1] + " " + HC, style=DOC, neg=NEG_WARP_C + ", " + NSEAT + ", " + NOFACE)
worn("B26", "starts_climb", "WIDE from the top landing as in the start frame, looking down to the foot of the stairs.",
    "Already on the first tread, she pushes up with the strapped knee and takes the second and third treads briskly, hands free, still climbing at the cut.", noface=False, place=PS("PLACE-BENT").split(" The shell's lower body")[0])

if __name__ == "__main__":
    for k, v in B.items():
        (BUILD / "beats" / f"{k}.i2v.json").write_text(v); print(k, len(v), "OK" if len(v) <= 2500 else "OVER")
