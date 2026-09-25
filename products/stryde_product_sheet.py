#!/usr/bin/env python3
"""
STRYDE PRECISION STRAP — PRODUCT SHEET, SINGLE FILE.  V7.49.14

One artefact for §18 step 2. Attach this file alone when absorbing the
product; it carries everything that step needs.

    the prose spec .............. SHEET_MD, printable with --md
    the slots ................... SLOTS, fill()
    the locked strings .......... PLACE_LOCK, ORIENT_LOCK, SEAT_LOCK, ...
    the measured ratios ......... RATIOS, INFO_RATIOS, RULINGS, UNSETTLED
    the per-batch checklist ..... CHECKLIST
    the assertions .............. verify()
    the geometry checker ........ check(), was stryde_frame_check.py
    the fit / "adjustable" rule . ADJUSTABLE_RULE, NEG_ADJUST (V7.49.14)
    the V7.49.4 pattern fills ... HOLD_PC, HOLD_PROD, NEG_WARP_P, WEAR_*,
                                  REAR_VIEW_SPEC, DEMONSTRATION_TABLE, ...
                                  (content moved OUT of the Standards)

USE

    python3 stryde_product_sheet.py              self-test, counts, ratios
    python3 stryde_product_sheet.py --md         write the prose sheet out
    python3 stryde_product_sheet.py --check f... score frames against RATIOS
    python3 stryde_product_sheet.py --refs       score the canonical five

    from stryde_product_sheet import PLACE_LOCK, fill
    fill(PLACE_LOCK, side="right")

NEVER RETYPE A STRING FROM THIS FILE INTO A PROMPT — import it. A retyped
string drifts from the one the assertions test, and the drift is silent.

V7.49.4: the Standards became fully product-agnostic. Everything that had
been written into the global document about THIS product now lives here,
under "MOVED FROM THE STANDARDS AT V7.49.4" below, and the Standards carry
only the slotted PATTERN for each of those strings. Import the fill from
here; never retype it from a pattern.

V7.48.3 PROJECT EXECUTION NOTE: this Product Sheet cannot create a routine
B-roll BLOCKED state. Unknown geometry, missing evidence, claim sourcing, or a
failed first frame route to reference-guided generation, POST-ASSIST, or REISSUE.
They never remove the script phrase from coverage. Media generation itself is
external in the project profile; this module supplies prompt locks and QA.

The prose half is embedded rather than shipped beside it. That is a change
from the Appendix B pair rule and it is recorded in Pending Amendments: the
pair existed so the prose stayed readable and the machine half stayed
importable, and a single module that emits its own markdown satisfies both.

The geometry checker needs numpy and cv2. They are imported lazily, so this
file imports cleanly for prompt work on a machine that has neither.

WHAT THE CHECKER CANNOT SEE, and these stay human checks:
  matte versus glossy · knit versus webbing · wordmark legibility · the
  declared side · placement on a body · whether the shell is on the front ·
  the band's outer-face keeper loops in a rear or turning beat.
It measures proportion only. A frame that passes here can still be wrong.
"""

VERSION = "7.49.14"

# --------------------------------------------------------------- slots

SLOTS = {
    "SITE":     "the patellar tendon immediately below the patella",
    "LANDMARK": "the kneecap",
    "REGION":   "knee",
    "STACK":    "quadriceps, hamstrings and calf",
    "BONES":    "femur, patella and tibia",
    "TARGET":   "the patellar tendon",
    "TARGET_JOINT": "the knee joint",
    # standards-side slots this product fills (see apply_v7_47.py)
    "BAND_MATERIAL": "black elastic band in a coarse knit with a visible textured weave and straight edges",
    "HARDWARE":      "brushed chrome slides",
    "BAND_INNER":    ("two small black moulded keeper loops side by side on the band's OUTER face, "
                      "rounded rectangles a little narrower than the band, standing proud of the "
                      "knit, sitting together at the rear of the loop. The band's edges run straight, "
                      "never scalloped. The INNER face lies against the skin and is not described."),
    # V7.49.4 pattern slots (Standards §8, §9A-P, §9D, §12A, Appendix A, E5)
    "RIGID":            "shell",
    "LIMB":             "leg",
    "JOINT":            "the knee",
    "SEGMENT_BEYOND":   "the upper shin",
    "FEATURE":          "the notch and its peaks",
    "FRACTION":         "three fifths",
    "NAMED_ASYMMETRIES": ("same two matching pointed peaks of equal height, same crisp centred notch, "
                          "same off-centre waist"),
    "REAR_PATH":        ("BELOW the hollow behind the knee, running horizontally across the top "
                         "of the calf with the knee's own bulge bare above it and unbroken calf below"),
    "BAND_HEIGHT_RATIO": "a third",
    "LOAD_CADENCE":     "walking cadence",
    # declared at the act map, held across every beat
    "SIDE":     None,
}

MECHANISM_CLAIM = "protection"          # one per build; load-path is retired
MECHANISM_REGISTER = "anatomical"       # 12A-1


def fill(s, side=None):
    """Substitute slots. Raises if the build's side has not been declared."""
    side = side or SLOTS["SIDE"]
    if side is None:
        raise ValueError("declare SIDE at the act map before filling any string")
    out = s
    for k, v in SLOTS.items():
        if v is None:
            continue
        out = out.replace("[%s]" % k, v)
        out = out.replace("[%s]" % k.replace("_", "-"), v)   # Standards write hyphens
    out = out.replace("[SIDE]", side)
    out = out.replace("[OTHER_SIDE]", "left" if side == "right" else "right")
    return out


# ------------------------------------------------------ locked strings
#
# Height is set by CONTACT, never by a measurement. Coverage is guarded
# separately. Scale is stated as FEATURE versus SHELL, because stating only
# one of the two is what produced an undersized shell.

PLACE_LOCK = (
"The strap is worn on the [SIDE] leg ON THE PATELLAR TENDON, directly BELOW the kneecap, already fully and "
"correctly in place: the shell sits on the tendon and the raised wave along its top edge catches the underside "
"of the kneecap. At the centre of that top edge a crisp concave notch curves upward and cups the kneecap's "
"lower border, the flesh of the lower border resting into and filling the curve with no gap anywhere between skin and "
"shell, and two matching pointed peaks of equal height rise either side of the notch, their tips reaching no higher than the "
"base of the kneecap's sides -- the shell never climbs the kneecap and never covers any of its face. THAT NOTCH "
"AND PEAK FEATURE IS ONE KNEECAP WIDE AND OCCUPIES "
"ONLY THE MIDDLE THREE FIFTHS OF THE SHELL: beyond each peak the shell continues outward and tapers down "
"across the front of the knee, ending in a brushed chrome slide inset flush at each outer margin of the leg, "
"so the shell spans the whole front of the joint rather than the kneecap alone. Slim and flush against the "
"leg, the flat black woven band running from the slides around behind the knee. Wordmark horizontal and "
"readable on the broad lower body of the shell, centred directly beneath the notch, never off to one side. "
"The band runs level around the leg at the height of the shell's middle. The kneecap's "
"face stays completely uncovered above the strap, its outline reading in full.")

PLACE_LOCK_C = (
"The strap is worn on the [SIDE] leg on the patellar tendon, directly below the kneecap, already fully and "
"correctly in place: the shell sits on the tendon and the raised wave along its top edge catches the underside "
"of the kneecap -- a crisp concave notch cupping the kneecap's lower border, its flesh filling the curve with no gap between skin and shell, "
"two matching pointed peaks of equal height either side reaching no higher than the base of the kneecap's sides, the shell never "
"climbing the kneecap. THAT FEATURE IS "
"ONE KNEECAP WIDE AND SITS INSIDE THE MIDDLE THREE FIFTHS OF THE SHELL, which continues outward past each "
"peak and tapers down to a chrome slide at each outer margin of the leg, spanning the whole front of the "
"joint. Slim and flush, wordmark horizontal and readable on the lower body, centred directly beneath the notch, "
"the band level at the shell's middle. "
"The kneecap's face stays completely uncovered above it, its outline reading in full.")

ORIENT_LOCK = (
"The rigid shell always faces forward, on the front of the knee only. The band is the only part that crosses "
"the back of the leg: a black elastic band in a coarse knit with a visible textured weave, running horizontally "
"around behind the knee, carrying no shell and no wordmark. Its OUTER FACE carries two small black moulded "
"keeper loops side by side at the rear, rounded rectangles a little narrower than the band, standing proud of "
"the knit. Its edges run straight. Its INNER FACE lies against the skin and is not described. "
"The only metal is a brushed chrome slide at each outer side of the leg, inset flush into the end of the "
"shell, where the band threads through and folds back on itself. From behind, the band crosses BELOW the "
"hollow behind the knee, running horizontally across the top of the calf with the knee's own bulge bare above "
"it and unbroken calf below, its height roughly a third of the leg's width at that point, the two keeper loops "
"standing proud together at the centre of the rear, and the outermost edge of one chrome slide at each side of "
"the leg silhouette standing proud of the outline as a small bright bar. The band presses in: flesh swells slightly above and below it, its edges undulate rather "
"than running as straight lines, and it sits a few degrees off horizontal, following the leg instead of a "
"drawn line. The shell is entirely hidden by the leg and no shell, wordmark or fastening appears anywhere on "
"the rear.")

ORIENT_C = (
"The rigid shell stays on the front of the knee throughout, never rotating around the leg. Only the flat "
"black woven webbing band crosses the back of the leg, below the hollow behind the knee and across the top of "
"the calf with the knee bare above it, its outer face carrying the two black keeper loops side by side at the rear, "
"with the chrome slides standing proud at the outer sides as small bright bars. The band "
"presses in: flesh swells above and below it and its edges undulate rather than running straight. No shell, "
"wordmark or fastening appears at the rear.")

# Bent-knee placement. The standing spec guards against the shell riding UP
# onto the kneecap; with the knee flexed the opposite failure appears -- a gap
# opening between the kneecap and the notch, so the shell reads disengaged
# from the thing it acts on. Stated positively as contact, per PLACE-LOCK.
PLACE_BENT = (
"With the knee bent the kneecap stands out as a distinct bulge and the shell sits directly beneath it: the "
"concave notch cradles the underside of the kneecap along its whole curve, the flesh of the kneecap pressing "
"into the notch and filling it with no gap of bare skin anywhere between them, and the two matching peaks "
"rising either side to flank the lower part of the kneecap's sides -- never past its middle and never covering "
"any of its face. The kneecap's own face stays completely uncovered above the "
"shell, its outline reading in full. The shell's lower body carries on down onto the upper shin. A polished "
"chrome slide sits at each outer margin of the leg with the flat black band running back from it. The shell "
"never rotates with the joint -- the notch stays under the kneecap through every angle of flexion.")

# The shell wraps far enough round that a side or three-quarter view still
# reads most of its face and the whole wordmark. Without this a profile beat
# renders a flat panel stuck on the front of a leg.
PLACE_PROFILE = (
"Seen from the side or three-quarter with the knee bent, the shell wraps far enough around the leg that most "
"of its face still reads: the nearer pointed peak curls up and over toward the front of the knee, the notch "
"dips between the peaks under the kneecap, and the wordmark runs horizontally along the shell's lower body, "
"readable rather than edge-on. At the rear edge of the shell a polished chrome slide stands proud with the "
"flat black band folding through it and running on around the leg. The shell's own curve follows the leg -- "
"it is a wrapped plate, never a flat panel stuck on the front.")

NEG_BENT = (
"no shell above the kneecap, no shell covering the kneecap, no gap of bare skin between the kneecap and the "
"notch, no kneecap sitting clear of the notch, no shell rotating with the joint, no shell sliding down the "
"shin, no wordmark upside down, no wordmark rotated, no flat panel sitting proud of the leg, no shell edge "
"lifting away from the skin, no second slide at the centre front")

# SEAT-LOCK states height as contact, exactly as PLACE-LOCK does, so a
# seating beat and a worn beat describe one position rather than two.
SEAT_LOCK = (
"The strap is already fully formed and closed — correct geometry, band closed, wordmark readable — but "
"sitting clearly off-position at mid-shin, well below the knee, on a straight leg. Both hands hold the shell by "
"its two sides, palms and fingertips flat on the matte shell, and slide the whole strap UPWARD in a single "
"unhurried movement, travelling up the front of the shin as one piece, and seat it: it comes to rest ON THE "
"PATELLAR TENDON, at the exact point where the raised wave on the shell's top edge meets the underside of the "
"kneecap -- the concave notch cupping the kneecap's lower border, its flesh filling the curve with no gap "
"anywhere between skin and shell, the two matching peaks either side reaching no higher than the base of the "
"kneecap's sides, the shell's outer ends carrying the chrome slides to the outer margins of the leg, exactly as "
"in the attached worn-placement reference. It is stopped there by the kneecap itself and travels no further, "
"never climbing onto it. The kneecap's face stays completely uncovered and clearly visible above it, its "
"outline reading in full. The band stays closed and correctly formed throughout — moved up the leg only, "
"never threaded, never fastened, never adjusted, never tightened, never removed. Fingers are just beginning "
"to lift away at the cut, still in contact, the movement unfinished.")

NEG_PLACE = (
"no shell riding up over the kneecap, no shell climbing the kneecap, no peaks climbing the sides of the kneecap, no peaks reaching the middle of the kneecap, no shell higher than the base of the kneecap, no gap of bare skin between the kneecap and the top edge of the strap, no strap sitting low on the shin, no "
"strap disengaged from the joint, no peaks level with or below the kneecap's lower pole, no flat straight top "
"edge, no shallow vague notch, no one peak taller than the other, no uneven peaks, no rounded mushy peaks, no "
"undersized shell, no shell no wider than the kneecap, no shell stopping short of the sides of the leg, no "
"peaks filling the whole width of the shell, no product covering the kneecap face, no product sitting on top "
"of the kneecap, no product above the kneecap, no product sitting too high, no product sitting too low, no "
"product upside down, no notch facing downward, no product on the [OTHER_SIDE] knee, no product on both "
"knees, no second unit, no full sleeve, no wrap, no brace covering the joint, no product rotated out of "
"alignment, no product gapping away from the leg")

NEG_ORIENT = (
"no shell at the back of the knee, no shell behind the leg, no wordmark visible from behind, no rigid moulded "
"shell on the rear of the leg, no hardware at the back of the knee, no second shell, no shell rotating around "
"the limb, no band crossing the front of the knee instead of the shell, no shell on the side of the knee, no "
"shell facing away from camera, no branded panel on the calf, no branded panel on the hamstring, no rear pad "
"behind the knee, no fastening visible at the back of the knee, no velcro tab at the rear, no buckle at the "
"rear, no band without its two keeper loops, no keeper loops on the inner face, no scalloped band edges, no wavy band edges, no smooth flat webbing band, no fine even weave, "
"no band sitting in the hollow behind the knee, no band above the knee, no band on the thigh, "
"no straight undented band edges, no band tracing a perfect straight line across the leg, no band floating off "
"the skin, no hardware at the centre of the back, no strap orientation changing between beats")

NEG_SEAT = (
"no product being threaded, no product being fastened, no band being opened, no band being closed, no velcro "
"being pulled, no buckle being worked, no product being removed, no product half-on, no twisted band, no open "
"band, no deformed shell, no stretched shell, no product changing shape, no product changing size, no hands "
"passing through the product, no hands passing through the body, no additional hands, no second person, no "
"two separate actions in one clip, no product travelling past the kneecap, no product climbing onto the kneecap, no shell riding up over the kneecap, no product coming to rest low on "
"the shin, no product moving downward, no product coming down from above the kneecap, no band being pulled "
"tight, no band ends being tugged, no fingers pulling the band through the slides, no hands gripping the band")

REF_PROD = (
"The product exactly as in the attached reference image — a matte-black polymer shell spanning "
"the whole front of the knee, its top edge waving up into two matching pointed peaks of equal height either side of a crisp "
"concave notch that occupies only the middle three fifths of its width, waisted off-centre, a flat matte-black "
"black elastic band in a coarse knit with a visible textured weave carrying two black keeper loops on its outer "
"face, a brushed chrome slide inset flush into each end of the shell, and a lowercase grey stryde wordmark "
"centred on the lower body directly beneath the notch, horizontal and readable, never to one side "
"of the notch —")

# --- fit lines and the word "adjustable" (V7.49.14) --------------------
# A generator reads "adjustable" as the act of adjusting: the band pulled
# tighter, the tail tugged, fingers working at the slides. That is not how
# this product is shown. A line about fit is covered by the FIT -- the closed
# strap slid up the shin and seated -- and by the product itself.
ADJUSTABLE_RULE = (
"A script line about fit or adjustability -- 'adjustable', 'fits any knee', 'one size fits all', 'easy to "
"put on', 'no fiddly straps', 'slips on in seconds' -- is covered by showing the fit, never the adjustment. "
"First beat: SEAT_LOCK -- the closed strap slid UP from mid-shin along the front of the shin and seated on "
"the patellar tendon, ending exactly on PLACEMENT_REFERENCES['front']. Second beat, when the line is long "
"enough for two (§27): the product itself -- in hand, turned through the light (DEMONSTRATION_TABLE "
"'Quality / materials'), or worn and already seated in a close front hold. Never shown: the band pulled "
"tighter, the band tail tugged, the band threaded or re-threaded through a slide, fingers working at the "
"slides, the strap opened, wrapped round the leg or closed. The word never enters a prompt. NEG_ADJUST on "
"every in-hand beat; NEG_SEAT on every seating beat.")

NEG_ADJUST = (
"no band being pulled tight, no band ends being tugged, no band tail being pulled, no fingers pulling the "
"band through the slides, no band being threaded through a slide, no band being unthreaded, no hands working "
"the chrome slides, no tightening motion, no loosening motion, no strap being opened, no strap being "
"wrapped around the leg, no strap being closed, no velcro, no buckle, no band tail hanging loose")

# Seating beats attach the canonical product image AND the front worn frame
# (the end position). The shin start is written, never shown by reference.
SEAT_REFERENCES = ("composite", "front")

# ==================================================================
# MOVED FROM THE STANDARDS AT V7.49.4
#
# Every string and passage below used to sit in the global document
# with this product's geometry written into it. The Standards now carry
# a slotted PATTERN for each; this is the fill. Section numbers refer to
# the Standards V7.49.4.
# ==================================================================

# --- §9A-P rear-view spec (was "The band sits below the hollow") --------
REAR_VIEW_SPEC = (
"A live-action reference at V7.48 contradicted the earlier locked spec and won under the "
"order of authority (Standards §7, layer 1). THE BAND CROSSES BELOW THE HOLLOW BEHIND THE "
"KNEE, across the top of the calf, with the knee's own bulge bare above it. The prior "
"wording -- the band crossing the hollow itself -- is retired: it renders the band tucked "
"up behind the knee and silently contradicts the front geometry, because a notch seated "
"under the kneecap cannot put the band behind the joint. Two further readings from the "
"same reference: the chrome slides read from behind as small bright bars standing proud "
"of the leg silhouette at each outer edge, and the band presses in -- flesh swelling above "
"and below it, its edges undulating rather than running straight, the whole thing a few "
"degrees off horizontal. Band height / leg width at the contact point is its own ratio "
"(INFO_RATIOS['BAND_HEIGHT_TO_LIMB_WIDTH']), not the band-thickness figure measured "
"against the shell's height.")

# --- §27D structural-integrity fills (patterns HOLD-PC, HOLD-PROD, NEG-WARP-P)
HOLD_PC = (
"The product keeps the start frame's exact geometry every frame: same silhouette, same "
"two matching peaks of equal height, same notch, same band width, same hardware and "
"wordmark position. The rigid shell never bends, flexes or stretches from any angle.")

HOLD_PROD = (
"The product keeps the exact geometry of the start frame on every frame: same silhouette, "
"same shell shape, same two matching peaks of equal height, same notch depth and width, "
"same band width, same hardware position, same wordmark position and spelling. The rigid "
"shell never bends, flexes, stretches, tapers or changes proportion under any movement or "
"from any camera angle. Only the band's own elastic stretch is permitted, and it returns to "
"its resting form.")

NEG_WARP_P = (
"no product changing shape, no shell bending, no shell flexing, no shell stretching, no "
"one peak growing taller than the other, no peaks becoming uneven, no peaks rounding off, no notch filling in, no notch widening, "
"no band changing width, no hardware moving, no wordmark moving, no wordmark changing "
"letters, no second product, no product parts detaching, no product changing size relative "
"to the leg")

# --- §9D worn-visibility fills (patterns WEAR-CONCEAL, WEAR-REVEAL, NEG-CONCEAL)
WEAR_CONCEAL = (
"The leg is covered by [GARMENT], which hangs and creases at the knee the way that fabric "
"actually does over a bent joint, breaking softly across the front of the knee and falling "
"straight below it. It reads as an ordinary covered leg: the fabric's own drape and weight "
"are all that show, with no shape beneath it and nothing interrupting its surface anywhere.")

WEAR_REVEAL = (
"Already seated with the leg drawn up, one hand takes the hem of [GARMENT] and draws it "
"clear of the knee in a single unhurried movement, the fabric gathering above the joint and "
"staying there. The product is already fully and correctly in place beneath it and comes "
"into view unchanged as the fabric clears. Neither hand touches the product, adjusts it, or "
"arrives at it. Fingers stay on the fabric at the cut.")

NEG_CONCEAL = (
"no strap visible through the fabric, no product outline printing through the trouser leg, "
"no bulge at the knee, no rolled trouser leg, no hitched hem, no lifted cuff, no hem held "
"up, no strap edge showing above a sock or below a hem, no fabric moulded to a shape "
"underneath")

# §9D reveal status. Standards: REVEAL beats are BLOCKED on any product with
# no attachable worn-placement reference; the block is recorded on the sheet.
REVEAL_STATUS = {
    "state": "OPEN",
    "reason": ("two worn-placement references accepted by the user at V7.49.8 -- "
               "PLACEMENT_REFERENCES below -- one front, one rear, both single-unit, "
               "right knee. They are generations, not photographs, so they are "
               "rendering references (RULINGS['worn_placement']), not measurement."),
    "unblocked_at": "7.49.8",
}

# --- worn-placement references, accepted V7.49.8 ----------------------
# Attached on every worn beat: the FRONT frame on straight-leg front and
# three-quarter beats, the BENT frame on any beat with the knee flexed
# (seated, stairs, kneeling, rising), the REAR frame on rear, turning and
# orbiting beats, and two of them on any beat where the leg turns or flexes
# through the clip. Seating beats attach the composite + the FRONT frame as
# the end position (SEAT_REFERENCES, V7.49.14). Image + names: the beat still
# carries PLACE_LOCK / ORIENT_LOCK in prose. The person in these frames is
# not the beat's subject -- the reference carries placement, never identity.
PLACEMENT_REFERENCES = {
    "front": {
        "file": "hf_20260819_134414_dab787bf-2285-4662-8597-1f60d7076347.png",
        "upload": "worn_front_ref.png",   # V7.49.12, Six Weeks Ago absorption
        "reads": ("right knee, weight on it, kneecap prominent; the notch cradles the "
                  "kneecap's lower border with the flesh filling the curve; the peaks "
                  "reach the lower half of the kneecap's side margins; the shell spans "
                  "almost the full width of the knee with a chrome slide just inside each "
                  "outer margin; the shell's lower edge sits at the top of the shin; "
                  "the wordmark on the lower body, horizontal, centred under the "
                  "side of the leg; the band level with the shell's middle; kneecap face "
                  "bare above. Shell height roughly half its width (estimated by eye)."),
    },
    "bent": {
        "file": "hf_20260915_182228_5e75f3c8-33ae-47eb-9e5e-f1bf32172d52.png",
        "upload": "worn_bent.png",
        "reads": ("right knee bent to about a right angle, seated, three-quarter from the right; "
                  "the shell on the patellar tendon with the notch cupping the underside of the "
                  "jutting kneecap, no gap; the near peak rising to flank the lower third of the "
                  "kneecap's side, the face bare above; the shell wrapped round the leg so the "
                  "wordmark reads horizontally from three-quarter, never edge-on; the chrome slide "
                  "standing proud at the outer margin with the band folding through it and running "
                  "back across the top of the calf; light band across the knee, matte black holding "
                  "its edges in the sun. Attached on every bent-knee worn beat."),
    },
    "rear": {
        "file": "hf_20260922_120414_6e07d1c8-e539-458d-9f87-86e017bf7808.png",
        "job_id": "6e07d1c8-e539-458d-9f87-86e017bf7808",
        "higgsfield_media": "use the job_id as the medias value",
        "supersedes": ("worn_back_ref.png (hf_20260819_134410_6a573801) -- scalloped band, "
                       "no keepers. Retired V7.49.13, never attached again."),
        "accepted": "V7.49.13, user-accepted. Edit of the original frame: band corrected to back.png, "
                    "straight-edged knit, two keeper loops at the centre rear holding the doubled band. "
                    "Logged model nano_banana_2 (connector routing fault).",
        "reads": ("right knee from behind, standing; the band crosses BELOW the hollow, "
                  "across the top of the calf, the hollow and the knee's bulge bare above "
                  "it; BAND DETAIL IN THIS FRAME IS SUPERSEDED by CANONICAL_REFERENCES['rear'] -- "
                  "in a regular soft wave; a small bright chrome bar standing proud at each "
                  "outer edge of the leg; the band roughly a third of the leg's width there "
                  "(estimated 0.33 by eye), a few degrees off horizontal, pressing in; no "
                  "shell, wordmark or fastening at the rear."),
    },
}

# --- §30B demonstration table, this product's fills ------------------
DEMONSTRATION_TABLE = (
    ("Rigid / solid / not cheap silicone",
     "9C FLEX or PRESS -- force applied to the shell, it resists and returns"),
    ("The band recovers / never stretches out",
     "9C STRETCH -- the coarse knit pulling open along its axis, snapping back"),
    ("It stays put / never slides",
     "worn in motion -- the strap visibly holds station through the step (12B ANCHORING)"),
    ("It takes the load",
     "worn under a real step -- shell settling into the tissue under the kneecap, "
     "band tensioning and easing (12B tension cycle, 8A)"),
    ("How it fits / where it sits / adjustable / fits any knee",
     "9B seating beat (SEAT_LOCK) -- the closed strap rises from mid-shin up the front of the "
     "shin in one move and seats on the patellar tendon with the kneecap's pole in the notch, "
     "ending on PLACEMENT_REFERENCES['front'], fingers lifting at the cut; then the product "
     "itself if the line runs long. Never adjusted or tightened on camera (ADJUSTABLE_RULE)"),
    ("Fake vs real",
     "9C SIDE-BY-SIDE -- same force on both, the silicone fake folds"),
    ("Quality / materials (offer act)",
     "in hand, turned through the light -- chrome slides catching specular, band tail "
     "swinging with weight -- never lying on a surface"),
)

# --- §12B form constraint, this product ------------------------------
MECHANISM_FORM_NOTE = (
"A rigid shell over the patellar tendon can only do what a rigid shell can do: press, take "
"load, hold position. It cannot pull, radiate or reach. The load arrives at footstep rate, "
"so LOAD_CADENCE is walking cadence and the throb in a pain beat is the footstep rate.")

# --- §30D after-state, this product ----------------------------------
AFTER_STATE_NOTE = (
"The visible difference between a painful knee and a recovered one on stairs is the gait. "
"Before-states may show a hand pressed on the thigh or knee; after-states never do, and "
"never hover near a rail. Reciprocal gait after; step-to gait before.")

# --- §16A widget examples that named this build's assets --------------
WIDGET_EXAMPLES = {
    "six_slot_row": "MECHANISM · the fifth tread, a shadow · propped candid · stab · Hall",
    "attachments":  ("hall plate", "Denise sheet", "product ref"),
}

# --- Standards Open Decision 15, now a product-level open item --------
OPEN_ITEMS = (
    ("orthographic front elevation",
     "One straight-on frame settles two geometry questions: where the wordmark sits "
     "against the notch, and the true width-to-height. Peak equality is settled "
     "(V7.49.10). See UNSETTLED['shell_elevation_aspect'] and RULINGS."),
    ("worn-placement reference", "See REVEAL_STATUS."),
)

# The Standards' generic NEG-ORIENT plus this product's own rear clauses.
NEG_ORIENT_PRODUCT_TAIL = (
"no velcro tab at the rear, no buckle at the rear, no coarse open knit, no visible loop "
"structure on the band, no band without its two keeper loops, no scalloped band edges, no band sitting in the hollow "
"behind the knee, no band on the thigh, no branded panel on the calf, no branded panel on "
"the hamstring")


S = {
    "PLACE-LOCK": PLACE_LOCK, "PLACE-LOCK-C": PLACE_LOCK_C,
    "ORIENT-LOCK": ORIENT_LOCK, "ORIENT-C": ORIENT_C,
    "SEAT-LOCK": SEAT_LOCK, "NEG-PLACE": NEG_PLACE,
    "NEG-ORIENT": NEG_ORIENT, "NEG-SEAT": NEG_SEAT, "REF-PROD": REF_PROD,
    "PLACE-BENT": PLACE_BENT, "PLACE-PROFILE": PLACE_PROFILE, "NEG-BENT": NEG_BENT,
    # V7.49.4 pattern fills
    "HOLD-PC": HOLD_PC, "HOLD-PROD": HOLD_PROD, "NEG-WARP-P": NEG_WARP_P,
    "WEAR-CONCEAL": WEAR_CONCEAL, "WEAR-REVEAL": WEAR_REVEAL, "NEG-CONCEAL": NEG_CONCEAL,
    # V7.49.14 fit lines
    "NEG-ADJUST": NEG_ADJUST,
}

# ------------------------------------------- measured geometry ratios
# Every figure below is measured off the five canonical renders with a
# roll correction applied. Perspective caveats are recorded beside each.

RATIOS = {
    # Each band is the observed range across the five renders PLUS a margin.
    # Raw min/max would put the references themselves on the boundary, which
    # fails a correct frame on a rounding difference.
    #
    # peak-to-notch rise / shell width. Observed 0.154-0.228, mean 0.196.
    # Yaw inflates this, so a true elevation reads at or below the low end.
    "RISE_RATIO": (0.14, 0.25),
    # distance between the peaks / shell width. Observed 0.548-0.687 across
    # the four usable renders; 65 reads 0.254 at 34 degrees of yaw, which is
    # why the checker gates this on roll rather than trusting it.
    "PEAK_SPAN_RATIO": (0.50, 0.73),
    # shell width / band width. Observed 5.61-6.66.
    "SHELL_OVER_BAND": (5.2, 7.2),
    # band width / shell greatest height. Observed 0.206-0.304, and the
    # highest reading comes from the most frontal render, so the top of the
    # range is the honest one.
    "BAND_OVER_SHELL_H": (0.19, 0.37),   # V7.49.12: canonical front.png reads 0.351; layer 1 wins
    # wordmark centroid / shell width. Observed 0.392-0.581.
    "WORDMARK_POSITION": (0.35, 0.62),
}

# Measured, reported, and deliberately NOT gated. Notch position ranges
# 0.362-0.647 across the five renders because yaw moves it further than the
# real offset does. It is informational until the elevation lands: near
# frontal views put it at 0.45-0.53, so write the waist offset as subtle.
INFO_RATIOS = {
    "NOTCH_POSITION": (0.42, 0.58),
    # Band height divided by LIMB WIDTH at the contact point, read off the
    # V7.48 live-action rear reference. This is NOT the band-thickness figure
    # in RATIOS, which is measured against the shell's height: different
    # denominators, and conflating them puts a wrong ratio on every frame.
    # Single sample, upscaled video, so it is informational not gated.
    "BAND_HEIGHT_TO_LIMB_WIDTH": (0.28, 0.36),
    # V7.49.12. Shell width (slide to slide) / greatest height, read off the
    # supplied straight-on front.png: height measured (565 px of 2048), width
    # by eye at the slides' outer edges. Informational, never gated.
    "SHELL_ASPECT_EST": (2.3, 2.6),
}

# Deliberately absent: shell width-to-height. Measured 1.23-1.72 across the
# five renders, but yaw compresses width and the wrap tilts the bounding
# box, so every one of those is an UNDER-estimate of the true elevation.
# No aspect figure enters this sheet until the elevation render exists.
ASPECT_RATIO = None

RULINGS = {
    "seating_joint_state":
        "LOCKED V7.49.8. Seating (putting-on) beats run on a STRAIGHT leg, the ring "
        "starting at mid-shin and seating on the patellar tendon. The bent-knee state "
        "is a WORN beat only (PLACEMENT_REFERENCES['bent']); a bent-knee seating beat "
        "was tested and dropped. Placement wording is per joint state: straight -- peaks "
        "no higher than the base of the kneecap's sides; bent -- peaks flanking the lower "
        "part of its sides, never past its middle.",
    "fit_not_adjustment":
        "LOCKED V7.49.14 (user). A fit or 'adjustable' line is covered by the seating move -- "
        "closed strap, mid-shin, slid UP the front of the shin, seated on the patellar tendon "
        "matching PLACEMENT_REFERENCES['front'] -- and by the product itself. Never by the band "
        "being pulled, tightened, threaded or worked at the slides. See ADJUSTABLE_RULE.",
    "peak_asymmetry_RETIRED_7_49_10":
        "RETIRED. The peaks are EQUAL in height and width -- two matching pointed "
        "peaks either side of a crisp centred notch. The 'taller narrower peak on "
        "the wordmark's side' ruling was a rendering drift promoted to spec: the "
        "V7.48.2 close-front panel, cropped through the left peak, taught every "
        "generation that one peak stands tall. That panel is withdrawn from the "
        "reference set. Peak height difference over 10 percent is now a FAIL.",
}

UNSETTLED = {
    "rear_ref_band_drift_RESOLVED_7_49_13":
        "RESOLVED V7.49.13 by the accepted edit 6e07d1c8. Was: OPEN V7.49.12. worn_back_ref.png (PLACEMENT_REFERENCES['rear']) renders the band "
        "with a scalloped outline and no keeper loops. CANONICAL_REFERENCE (layer 1) shows "
        "straight edges and two keeper loops at the centre rear. The frame stays attached "
        "for PLACEMENT ONLY on rear and turning beats, with ORIENT_LOCK + NEG_ORIENT_PRODUCT_TAIL "
        "stated in full. RESOLVED BY: one regenerated rear worn frame, right knee, straight-edged "
        "knit band with both keeper loops, accepted by the user.",
    "inner_face_script":
        "OPEN V7.49.12. The Six Weeks Ago script states a silicone pad on the inside of the "
        "shell. Advertiser-stated, unphotographed. Never rendered: no beat shows the inner face.",
    "band_faces_RESOLVED_7_49_11":
        "RESOLVED by the supplied product images (CANONICAL_REFERENCES). The OUTER "
        "face carries TWO black moulded keeper loops side by side at the rear; the "
        "band is a coarse knit with a visible textured weave and STRAIGHT edges. "
        "The V7.49.8 plain-face / scalloped-edge reading, taken off a worn "
        "generation, is retired -- a worn frame is a placement reference, never a "
        "product-geometry source. The inner face remains undescribed.",
    "band_keepers":
        "SETTLED FOR RENDERING, OPEN AS A FACT. Small black moulded keeper "
        "loops sit on the band, consistent across 63, 64, 68 and every "
        "V7.48.2 reference panel. They are a secondary component the "
        "eight-field spec did not carry, and they now render on every "
        "object beat. UNBLOCKED AS A FACT BY: a photograph of the band.",
    "band_weave":
        "SETTLED FOR RENDERING, OPEN AS A FACT. At V7.48.1 the native-"
        "resolution rear crop shows a tight, regular, fine woven grain with "
        "no loop structure at all, at a scale where loops would resolve. "
        "CORRECTED AT V7.48.2: every V7.48.2 panel and the macro frame show a COARSE OPEN KNIT WITH VISIBLE LOOP STRUCTURE, not a fine even weave. BAND_MATERIAL therefore describes what must RENDER: flat matte-"
        "black woven elastic webbing. It does NOT assert how the band is "
        "manufactured -- the plates are our own generated renders, and a "
        "render cannot know whether the band is the loop half of a "
        "hook-and-loop pair. If the physical product is loop-knit, the "
        "prompts are still correct, because they target the accepted "
        "appearance. RESOLVED AS A FACT BY: a photograph of the physical band, or an "
        "advertiser statement of the closure type.",
    "band_inner_lugs":
        "The outer-face keeper loops are neither confirmed nor killed by the "
        "V7.48 rear reference. The band's lower edge does undulate against "
        "the calf, but plain compression explains that equally, and the lugs "
        "sit against the skin where the camera cannot see them. They stay as "
        "written and stay unverified. RESOLVED AS A FACT BY: a close still of the "
        "band's inner face, or a rear beat generated with and without the "
        "inner-face clause.",
    "shell_elevation_aspect":
        "True shell width-to-height is unknown. Every canonical render is "
        "three-quarter, and yaw makes the measured 1.23-1.72 an "
        "under-estimate. V7.49.12: the supplied straight-on front.png gives an ESTIMATE "
        "of 2.3-2.6 (INFO_RATIOS['SHELL_ASPECT_EST']); still informational until measured "
        "edge-to-edge. DOES NOT BLOCK GENERATION: no exact shell width-to-height "
        "figure may be stated until the elevation exists; use REF-PROD plus the known "
        "feature/span locks and reissue any frame that fails visual QA. RESOLVED BY: one "
        "orthographic front elevation, shell flat to camera, no yaw, no roll.",
}

# ------------------------------------------ per-batch first-frame checks
# ==================================================================
# REFERENCE REGISTRY  (V7.48.2)
#
# PROVENANCE, stated once and never softened: every image of this
# product in the corpus is model output. There is no photograph. The
# reference sheet is a RENDERING CONSISTENCY DEVICE -- it makes every
# beat draw the same object. It is not evidence and nothing measured
# off it may enter RATIOS as a fact.
# ==================================================================

# --- canonical reference set, supplied V7.49.11 -------------------------
# These four are THE PRODUCT (Order of Authority layer 1). They outrank every
# prior render, the V7.48.2 sheet, and the band detail in any worn frame.
CANONICAL_REFERENCE = {
    "file": "STRYDE_reference_v7_49_11.png",
    "built_from": "front.png (top, full width), 2.png (bottom left), back.png (bottom right) -- the supplied product images composited on a plain white ground, no text",
    "reads": ("ONE image, attached on every product-facing generation call, alongside REF_PROD in prose. "
              "Front elevation: two peaks of equal height, notch centred, wordmark centred directly beneath "
              "the notch, chrome slides inset at each end with engraved dashed detail, coarse-knit band with "
              "straight edges. Three-quarter: the wrap reads, keeper loops visible on the band. Rear: two "
              "black moulded keeper loops side by side at the centre of the band, the shell's silhouette "
              "rising behind with equal peaks, a slide at each side."),
    "excluded": "3.png -- its wordmark sits on the opposite side of the notch from 2.png; a composite must not contradict itself",
}
CANONICAL_REFERENCES = {"composite": CANONICAL_REFERENCE}  # single-image rule, V7.49.11

REFERENCE_SHEET = {
    "version": "7.48.2",
    "file": "STRYDE_reference_sheet_v7.48.2.png",
    "built_from": "the canonical five (63, 64, 68 attached as references)",
    "panels": {
        "front_elevation": "21f95c16-b18d-44ae-81cc-dc96bc79bae6",
        "three_quarter_a": "e50eeb40-f7c2-4159-a403-1d4f155a2a47",
        "three_quarter_b": "fbf62c52-5a03-4187-ab00-e953ea3676a6",
        "rear":            "bf419254-5290-49e6-8b88-6cb77ac20a40",
        "close_front":     "411ef306-fd8d-43fd-ba4c-2ed9eae015be",
    },
    "model_passed": "nano_banana_pro",
    "model_logged": "nano_banana_2",   # routing fault, 8/8 this session
    "gaps": (
        "both three-quarters recede the same way -- no true mirror pair",
        "inner face excluded deliberately, unevidenced",
    ),
}

# --- §9D garment list -------------------------------------------------
# Which garments conceal this shell and which leave it visible. Product
# Sheet content, not standards content.

CONCEALING = (
    "full-length trousers of any weight",
    "jeans",
    "tracksuit bottoms",
    "a long skirt or dress falling below the knee",
    "leggings",
)

EXPOSING = (
    "shorts ending above the knee",
    "a skirt or dress ending above the knee",
    "bare legs, indoors or in warm weather",
    "a trouser leg already drawn up while seated -- a REVEAL, not a default",
)

# The shell sits under the kneecap and carries onto the upper shin, so a
# hem must clear the kneecap by a good margin to leave it visible. A hem
# AT the knee is the worst case: it half-covers the shell and reads as a
# wardrobe accident rather than a choice. Beats are written to a hem
# clearly above or clearly below.
HEM_RULE = ("no hem resting at the knee itself -- clearly above the "
            "kneecap or clearly below the calf, never level with the shell")

VISIBILITY_STATES = ("CONCEALED", "VISIBLE", "REVEAL")

# Attach the sheet to every product-facing generation. Never attach a
# multi-instance frame: it teaches the generator to draw two units.
PHRASING_V7482 = (
    ("rear view of the object",
     "ORIENT-LOCK's 'outermost edge of a slide standing proud at each "
     "outer silhouette edge' -- worn-beat wording. On a free-floating "
     "object it renders the chrome as large plates out at the band's "
     "extremities with the shell a featureless slab behind.",
     "State the slides as INSET FLUSH INTO THE SHELL'S OWN ENDS, no wider "
     "than the end, and restate the shell's full wavy silhouette seen "
     "from behind."),
)

NEVER_ATTACH = (
    "STRYDE_reference_sheet_v7.48.2.png -- SUPERSEDED V7.49.11 by CANONICAL_REFERENCES; its close-front panel taught the tall-peak error",
    "any frame showing more than one unit",
    "any worn frame other than PLACEMENT_REFERENCES on a beat where placement is the claim",
    "any reference image showing ring marks on a table or worktop",
)

# Accepted against a measurement that failed. Recorded, not hidden.
OVERRIDES = {
    "front_elevation_symmetry": (
        "RESOLVED V7.49.10: the 0.0 percent peak asymmetry the V7.48.2 front "
        "elevation measures IS the spec. The 26-38 percent the other renders "
        "carried was drift. What that frame still gets wrong is the wordmark, "
        "centred at 0.500 -- which the supplied front elevation (V7.49.11) now "
        "confirms as the spec."
    ),
}

CHECKLIST = [
    "the two peaks equal in height and width, pointed, not mushy",
    "notch crisp and concave, not shallow or vague",
    "waist off-centre, but subtly — not dramatically",
    "shell matte, not glossy",
    "chrome slides catching hard specular, inset flush into the shell ends",
    "band a coarse knit with a visible textured weave, two black keeper loops on its outer face -- and narrower than a fake's wide thick strap",
    "wordmark readable, on the lower body, centred beneath the notch",
    "correct declared side",
    "product at the site, not on the landmark",
    "no second unit unless a sanctioned pair-pack beat",
    "notch valley under the kneecap's centre, not off to one side",
    "kneecap flesh visibly filling the notch curve, zero gap",
    "peaks rising past the pole and flanking its lower side margins",
    "kneecap face uncovered, outline reading in full above the shell",
    "peak-to-notch rise divided by shell width sits near 0.15-0.24",
    "notch and peaks span one kneecap and sit inside the middle three "
    "fifths; the shell continues out to a chrome slide at each outer "
    "margin of the leg",
    "the band's outer face carries spaced moulded keeper loops, visible on "
    "rear and turning beats",
    "rear and turning beats: only the woven band crosses the back of the "
    "knee, and no fastening is visible there",
    "rear beats: the band sits BELOW the hollow, across the top of the calf, "
    "with the knee's own bulge bare above it -- never in the hollow",
    "rear beats: the band presses in, flesh swelling above and below it, its "
    "edges undulating rather than running as straight lines",
    "rear beats: a chrome slide reads as a bright bar standing proud of the "
    "leg silhouette at each outer edge",
    "bent-knee beats: the kneecap's flesh presses INTO the notch curve and "
    "fills it -- no gap between kneecap and notch",
    "bent-knee beats: the shell's lower body carries on down onto the upper "
    "shin, and the shell has not rotated with the joint",
    "side and three-quarter beats: the shell reads as a WRAPPED plate "
    "following the leg's curve, wordmark still horizontal and readable, "
    "never a flat panel on the front",
    "seating beats: the closed strap starts at mid-shin and moves UP the "
    "front of the shin only -- never down, never from above the kneecap",
    "seating beats: hands flat on the shell's sides, never on the band "
    "ends or the slides; nothing pulled, tightened or threaded",
    "seating beats: end position matches the front worn-placement reference",
]

# back-compat for callers that imported the bare name
RISE_RATIO = RATIOS["RISE_RATIO"]

# ------------------------------------------------- retired / never write
REVERSALS_V7482 = (
    ("band weave", "V7.48 retired the loop-knit phrasings on the strength "
     "of one rear crop reading as a fine even weave. Every V7.48.2 "
     "reference panel and the macro frame show a coarse open knit with "
     "loops clearly resolving. The retirement is REVERSED."),
    ("band fixture face", "The spec placed moulded lugs on the band's "
     "INNER face and NEG-ORIENT banned them from the outer face. The "
     "corpus shows moulded keeper loops on the OUTER face. The faces were "
     "inverted; the inner face is unevidenced and is described nowhere."),
    ("wordmark position", "PLACE-LOCK-C and REF-PROD require the wordmark "
     "offset to one side of the notch, matching the canonical five. The "
     "accepted V7.48.2 front elevation shows it centred beneath the notch, "
     "a phrasing this sheet retires. Prompts keep the offset wording; the "
     "front elevation panel is NOT attached on beats where wordmark "
     "position matters. See OVERRIDES."),
)

RETIRED_PHRASINGS = [
    # V7.49.8 -- these rendered the shell ON the kneecap. The shell sits on
    # the patellar tendon; the top-edge wave catches the underside of the
    # kneecap; the peaks reach no higher than the base of its sides.
    "riding up under the kneecap",
    "rides up onto the kneecap",
    "climbing past the pole",
    "lower third of its side margins",
    "clear gap of bare skin",
    "2 cm below",
    "two centimetres below",
    "two centimeters below",
    "one to two fingers below",
    "fingers below the kneecap",
    "no wider than",
    "right knee only",
    "<<<",                                  # element tokens
    "full width of the kneecap and slightly beyond",
    "spans the kneecap and slightly beyond",
    "plain coarse black knit strip, unbroken and featureless",   # pre-lug band
    "centred on the broad lower body of the shell directly beneath the notch",
    "load-path",
    # V7.48 -- the band sits below the hollow, not in it
    "crossing the hollow just below the crease",
    "band crossing the hollow",
    # V7.48 -- resolution is 2k on every beat type
    "4k for mechanism",
    "4k only for mechanism",
    # V7.48 -- the flow grammar is retired from the mechanism register
    "standing column",
    "river of load",
    "molten amber load",
    "plumes descending",
    # V7.49.14 -- a generator renders the word as the act of adjusting
    "adjustable",
    "adjust the strap",
    "tighten the strap",
    "pull the strap tight",
]

# clauses that are legal ONLY inside a named negatives string
NEG_ONLY = {
    "clear gap of bare skin": ("NEG-PLACE",),
    "no wider than": ("NEG-PLACE",),
}


# --------------------------------------------------------------- checks
# ==================================================================
# SURFACE STANDARD  (§15A, V7.48.2)
#
# Ring marks are a standing exclusion. Overrepresented in stock
# cosy-kitchen photography — the register §15 exists to keep out — so a
# generator handed "named wear" reaches for them every time. Also
# inaccurate: most real domestic tables are laminate, melamine, oilcloth,
# painted or covered, and do not ring at all.
# ==================================================================

RING_TERMS = (
    "ring mark", "ring marks", "cup ring", "cup rings",
    "water ring", "water rings", "circular stain", "circular stains",
    "coffee ring", "coffee rings", "mug ring", "mug rings",
)

# I2V negatives ONLY. Never written into T2I — T2I has no negative
# channel, so naming the ring in order to exclude it renders it (§5).
NEG_RING = ("no ring marks, no cup rings, no water rings, "
            "no circular stains on the surface")

SURFACE_WEAR_MENU = (
    "scorch and heat marks where a hot pan lands",
    "knife scoring across the working area",
    "ink transfer at one corner",
    "finish worn through where forearms rest",
    "wax build-up settled into the grain",
    "a chipped and bruised edge",
    "sun-bleaching down the window side",
    "a lifted veneer edge",
)

# Bare oiled or waxed wood is one option among several, not the reach.
DEFAULT_SURFACES = (
    "worn laminate with a lifting edge",
    "melamine, dulled where it is wiped most",
    "oilcloth creased from being folded",
    "painted wood chipped back at a corner",
    "scrubbed pine, dry and pale",
)

NEVER_ATTACH_SURFACE = (
    "any reference image showing ring marks on a table or worktop",
)


def rotate_wear(beat_index, count=2):
    """Deterministic rotation — consecutive object beats never share a
    feature. Deterministic rather than random so the no-repeat property is
    provable by assertion rather than hoped for."""
    n = len(SURFACE_WEAR_MENU)
    start = (beat_index * count) % n
    return tuple(SURFACE_WEAR_MENU[(start + k) % n] for k in range(count))


def check_surface_clause(t2i, i2v_negatives=""):
    """Score one object-beat surface clause. [] == pass."""
    fails = []
    low = t2i.lower()
    for term in RING_TERMS:
        if term in low:
            fails.append("RING NAMED IN T2I: %r — T2I has no negative "
                         "channel, so naming it renders it. Block "
                         "positively instead." % term)
            break
    hits = [w for w in SURFACE_WEAR_MENU
            if w.split(",")[0].lower()[:18] in low]
    if len(hits) < 2:
        fails.append("WEAR THIN: %d menu features present, 2 minimum. A "
                     "surface with no history renders clean and new "
                     "(§15A)." % len(hits))
    if i2v_negatives and "no ring marks" not in i2v_negatives.lower():
        fails.append("NEG_RING missing from I2V negatives.")
    return fails


def _verify_registry():
    fails = []
    if set(VISIBILITY_STATES) != {"CONCEALED", "VISIBLE", "REVEAL"}:
        fails.append("§9D visibility states wrong")
    if not CONCEALING or not EXPOSING:
        fails.append("§9D garment list incomplete")
    if "at the knee itself" not in HEM_RULE:
        fails.append("§9D hem rule missing its worst case")
    if REFERENCE_SHEET["model_logged"] == REFERENCE_SHEET["model_passed"]:
        fails.append("routing fault record lost -- passed and logged now agree")
    if len(REFERENCE_SHEET["panels"]) != 5:
        fails.append("reference sheet must carry five panels")
    if "front_elevation_symmetry" not in OVERRIDES:
        fails.append("front elevation override record missing")
    if not any("more than one unit" in x for x in NEVER_ATTACH):
        fails.append("multi-instance never-attach rule missing")
    if not PHRASING_V7482 or len(PHRASING_V7482[0]) != 3:
        fails.append("phrasing row must be intent/failed/works")
    return fails


def _verify_surface():
    fails = []
    if not NEG_RING.startswith("no ring marks"):
        fails.append("NEG_RING head clause missing")
    if len(SURFACE_WEAR_MENU) < 8:
        fails.append("wear menu too short to rotate 2-per-beat")
    if len(set(SURFACE_WEAR_MENU)) != len(SURFACE_WEAR_MENU):
        fails.append("duplicate wear entry")
    for i in range(len(SURFACE_WEAR_MENU)):
        if set(rotate_wear(i)) & set(rotate_wear(i + 1)):
            fails.append("wear rotation repeats at beat %d" % i)
    if not check_surface_clause("resting on a clean oak table"):
        fails.append("checker passed a surface with no wear")
    if not check_surface_clause("scrubbed pine, knife scoring across the "
                                "working area, no ring marks"):
        fails.append("checker passed a ring named in T2I")
    good = ("worn laminate with a lifting edge, scorch and heat marks "
            "where a hot pan lands, knife scoring across the working area")
    if not check_surface_clause(good, "no white background"):
        fails.append("checker passed a beat missing NEG_RING")
    if check_surface_clause(good, NEG_RING):
        fails.append("checker failed a valid clause")
    return fails


def _verify_v7490():
    """The V7.49.4 pattern fills: every slot the Standards now expect is
    filled here, and every moved string is present and product-specific."""
    fails = []
    for k in ("RIGID", "LIMB", "JOINT", "SEGMENT_BEYOND", "FEATURE", "FRACTION",
              "NAMED_ASYMMETRIES", "REAR_PATH", "BAND_HEIGHT_RATIO", "LOAD_CADENCE"):
        if not SLOTS.get(k):
            fails.append("V7.49.4 slot unfilled: %s" % k)
    if "BELOW the hollow" not in SLOTS["REAR_PATH"]:
        fails.append("REAR_PATH lost the V7.48 correction (band below the hollow)")
    for name, must in (("HOLD-PC", "matching"), ("HOLD-PROD", "matching"),
                       ("NEG-WARP-P", "no peaks becoming uneven"),
                       ("WEAR-CONCEAL", "[GARMENT]"), ("WEAR-REVEAL", "[GARMENT]"),
                       ("NEG-CONCEAL", "no rolled trouser leg")):
        if must not in S[name]:
            fails.append("%s missing: %s" % (name, must))
    if REVEAL_STATUS["state"] != "BLOCKED" and not PLACEMENT_REFERENCES:
        fails.append("REVEAL_STATUS changed without a worn reference being registered")
    for k in ("front", "bent", "rear"):
        if k not in PLACEMENT_REFERENCES or "file" not in PLACEMENT_REFERENCES[k]:
            fails.append("PLACEMENT_REFERENCES missing the %s frame" % k)
    if len(DEMONSTRATION_TABLE) != 7:
        fails.append("DEMONSTRATION_TABLE must carry the seven §30B rows")
    # fill() must resolve both slot spellings the Standards use
    probe = fill("[BAND-MATERIAL] / [BAND_MATERIAL] / [REAR-PATH] / [LOAD-CADENCE]", side="right")
    if "[" in probe:
        fails.append("fill() left a slot unresolved: %s" % probe)
    return fails


def _n(s):
    return len(s.replace("\n", ""))


def verify(verbose=False):
    """Self-test. Raises AssertionError on any drift."""
    fails = []

    # 1 no locked string carries a retired phrasing outside its carve-out
    for name, s in S.items():
        low = s.lower()
        for bad in RETIRED_PHRASINGS:
            if bad in low and name not in NEG_ONLY.get(bad, ()):
                fails.append("%s carries retired phrasing: %r" % (name, bad))

    # 2 height is stated as contact in every string that sets height
    for name in ("PLACE-LOCK", "PLACE-LOCK-C", "SEAT-LOCK"):
        if "filling the" not in S[name]:
            fails.append("%s does not state height as contact" % name)
        if "uncovered" not in S[name]:
            fails.append("%s does not guard coverage separately" % name)

    # 3 scale states the feature and the shell separately
    for name in ("PLACE-LOCK", "PLACE-LOCK-C"):
        low = S[name].lower()
        if "middle three fifths" not in low:
            fails.append("%s does not scope the notch feature to the middle "
                         "three fifths" % name)
        if "outer margin" not in low and "outer margins" not in low:
            fails.append("%s does not carry the shell out to the leg's outer "
                         "margins" % name)

    # 4 the wordmark is stated as offset, never centred under the notch
    for name in ("PLACE-LOCK", "PLACE-LOCK-C"):
        if "centred directly beneath the notch" not in S[name]:
            fails.append("%s does not state the wordmark centred beneath the notch" % name)

    # 5 orientation strings keep the shell off the rear AND carry the lugs
    for name in ("ORIENT-LOCK", "ORIENT-C"):
        if "front of the knee" not in S[name]:
            fails.append("%s does not pin the shell to the front" % name)
        if "keeper loops" not in S[name]:
            fails.append("%s does not carry the band's two outer-face keeper loops" % name)
        if "scallop" in S[name]:
            fails.append("%s still carries the scalloped-edge reading (retired V7.49.11)" % name)
    if "OUTER" not in ORIENT_LOCK or "INNER" not in ORIENT_LOCK:
        fails.append("ORIENT-LOCK does not separate the band's outer and inner faces")

    # 6 the negatives exclude the landmark explicitly
    for clause in ("no product covering the kneecap face",
                   "no product sitting on top of the kneecap",
                   "no product above the kneecap"):
        if clause not in NEG_PLACE:
            fails.append("NEG-PLACE missing: %s" % clause)

    # 7 the negatives defend the corrected scale and the lugs
    for clause in ("no undersized shell", "no shell no wider than the kneecap",
                   "no peaks filling the whole width of the shell"):
        if clause not in NEG_PLACE:
            fails.append("NEG-PLACE missing scale clause: %s" % clause)
    for clause in ("no band without its two keeper loops",
                   "no scalloped band edges",
                   "no fastening visible at the back of the knee"):
        if clause not in NEG_ORIENT:
            fails.append("NEG-ORIENT missing rear clause: %s" % clause)

    # 8 seating stays a reposition, never an assembly
    for clause in ("never threaded", "never fastened", "never removed"):
        if clause not in SEAT_LOCK:
            fails.append("SEAT-LOCK missing: %s" % clause)

    # 8b seating rises from the shin and never adjusts (V7.49.14)
    for frag in ("mid-shin", "UPWARD", "never tightened", "worn-placement reference"):
        if frag not in SEAT_LOCK:
            fails.append("SEAT-LOCK missing: %s" % frag)
    for clause in ("no product moving downward", "no band being pulled tight"):
        if clause not in NEG_SEAT:
            fails.append("NEG-SEAT missing: %s" % clause)
    for clause in ("no band being pulled tight", "no fingers pulling the band through the slides",
                   "no tightening motion"):
        if clause not in NEG_ADJUST:
            fails.append("NEG-ADJUST missing: %s" % clause)
    for frag in ("SEAT_LOCK", "NEG_ADJUST", "PLACEMENT_REFERENCES['front']", "never the adjustment"):
        if frag not in ADJUSTABLE_RULE:
            fails.append("ADJUSTABLE_RULE missing: %s" % frag)
    if not all(k in {**CANONICAL_REFERENCES, **PLACEMENT_REFERENCES} for k in SEAT_REFERENCES):
        fails.append("SEAT_REFERENCES names an unregistered reference")

    # 9 one mechanism claim, and it is not the retired one
    if MECHANISM_CLAIM != "protection":
        fails.append("mechanism claim is not the locked one")

    # 10 no aspect figure may be published before the elevation exists
    if ASPECT_RATIO is not None and "shell_elevation_aspect" in UNSETTLED:
        fails.append("ASPECT_RATIO published while the elevation is unsettled")

    # 11 the measured ratios are ordered pairs
    for k, (lo, hi) in RATIOS.items():
        if not (0 < lo < hi):
            fails.append("RATIOS[%s] is not an ordered positive pair" % k)

    # 12 the checklist carries the three V7.47 items
    joined = " ".join(CHECKLIST)
    for frag in ("middle three fifths", "equal in height and width",
                 "keeper loops", "centred beneath the notch"):
        if frag not in joined:
            fails.append("CHECKLIST missing V7.47 item: %s" % frag)

    fails += _verify_surface()
    fails += _verify_registry()
    fails += _verify_v7490()

    if fails:
        raise AssertionError("product sheet self-test failed:\n  " + "\n  ".join(fails))
    if verbose:
        print("self-test passed: %d strings, %d checklist items, %d ratios"
              % (len(S), len(CHECKLIST), len(RATIOS)))
    return True


def counts():
    return {k: _n(v) for k, v in sorted(S.items())}

# ==================================================================
# PROSE SHEET  (was stryde_product_sheet.md — emit with --md)
# ==================================================================
SHEET_MD = r'''# Product Sheet — Stryde Precision Strap

**V7.49.14.** This is the prose half of `stryde_product_sheet.py`, embedded in it and emitted with `--md`. It carries the spec, the phrasing table, the claim register and the reference registry; the module around it carries the slots, the locked strings, the measured ratios and the assertions. **Never retype a string into a prompt — import it.**

Every geometry figure below was measured off the five canonical renders (63, 64, 65, 66, 68) with a roll correction applied, not read off the prose. Where a figure is external it is marked Tier 3 and is not advertiser-held.

---

## 1. Product name and category

Stryde Precision Strap — a patellar tendon strap. A rigid moulded anterior shell on a closed knit band, worn on one knee, sitting under the kneecap and over the upper patellar tendon.

**Market note.** Multiple marketplace sellers list a "Stryde Precision Strap" built around a soft silicone lock-point pad. Our hero is rigid matte polymer with brushed chrome hardware, which is the opposite construction. Two consequences: the cheap-silicone villain archetype (§10) is the literal market reality and the anti-knock-off angle is stronger than it looked; and the name question is the advertiser's counsel's, not this sheet's.

---

## 2. The eight spec fields (§8)

**1 — Primary form.** A rigid moulded polymer shell spanning the whole front of the knee from one side of the leg to the other, its top edge waving up into two matching pointed peaks of equal height either side of a crisp concave notch, waisted off-centre, closed behind the leg by a flat matte-black woven elastic band.

**2 — Material and finish.** Shell: matte polymer, satin not gloss, holding a soft broad highlight along the crown of each peak and down the waist. Band: black elastic band in a coarse open knit with visible loop structure, no visible loop structure — read off the native-resolution rear crop at V7.48.1. This describes what must **render**; see `UNSETTLED["band_weave"]` for why it is not a manufacturing claim. Hardware: polished brushed chrome, the only specular element on the object. Inner-face lugs: soft matte black, lower sheen than the shell.

**3 — Distinguishing asymmetries.** *The most important field, and every item here is normalised out if unstated.*

- The two peaks are **equal** in height and in width — two matching pointed peaks. A height difference over 10% is a fail (V7.49.10: the earlier 'uneven' reading was rendering drift promoted to spec by a cropped close-front panel).
- The waist is **off-centre**, but subtly. Near-frontal renders put the notch at 0.45–0.53 of shell width; write it as a shift, never as dramatic.
- The notch is **crisp and concave**, not a shallow dip.
- The peaks are **pointed**, not rounded.
- The wordmark is **centred directly beneath the notch** (V7.49.11, read off the supplied front elevation; the two supplied three-quarter renders disagree with each other on this and are not the authority).

**4 — Scale reference.** *Two dimensions, stated separately — this is the correction that mattered most.*

- The **notch-and-peaks feature** is one kneecap wide and occupies the **middle three fifths** of the shell. Measured peak span 0.55–0.69 of shell width.
- The **shell** spans the whole front of the joint, ending in a chrome slide at each outer margin of the leg. Measured shell width 5.6–6.7 band-widths.
- Peak-to-notch rise is 0.15–0.24 of shell width, mean 0.196.
- Band width is roughly a quarter to a third of the shell's greatest height.
- **No width-to-height figure exists yet.** See §7 below.

**5 — Secondary components.** Band: flat matte-black woven elastic webbing, threading through each slide and folding back on itself, so the fold-back sits at the sides of the leg and never at the rear. The band is never shown being adjusted (§12 below). **Inner-face keeper loops:** spaced soft matte-black moulded rounded rectangles, a little narrower than the band, standing slightly proud of the webbing, at least two visible per side. Hardware: polished chrome rectangular bars inset flush into each shell end, carrying fine engraved dashed detail on the face — captured by the shell, not floating on the band.

**6 — Interface mechanism.** Band threads through the chrome slides and folds back. There is no visible velcro tab, buckle or fastening in any canonical render, and none at the rear in any beat.

**7 — Placement lock.** `[SITE]` is the patellar tendon immediately below the patella; `[LANDMARK]` is the kneecap. Height is set by **contact** — the kneecap's lower pole seats into the concave notch, its flesh filling the curve, no gap anywhere between skin and shell — never by a measured offset. Coverage is guarded separately: the kneecap's face stays completely uncovered, its outline reading in full. Side is declared at the act map and held; the product is **not handed**. Strings: `PLACE-LOCK`, `PLACE-LOCK-C`, `ORIENT-LOCK`, `ORIENT-C`, `SEAT-LOCK`, `NEG-PLACE`, `NEG-ORIENT`, `NEG-SEAT`.

**8 — Standing negatives.** `NEG-PLACE` and `NEG-ORIENT` in the `.py`, accumulated from observed failures. Three clauses were added at V7.47: `no undersized shell`, `no peaks filling the whole width of the shell`, `no band without keeper loops on its inner face`.

---

## 3. Phrasing table

| Intent | Phrasing that failed, and what it produced | Phrasing that works |
|---|---|---|
| Set the height | "2 cm below the kneecap" / "one to two fingers below" | The kneecap's lower pole seats deep into the notch, its flesh filling the curve, no gap between skin and shell |
| Keep the kneecap clear | "a clear gap of bare skin between the kneecap and the strap" — rendered the strap low on the shin and visibly disengaged from what it acts on | The kneecap's face stays completely uncovered above the strap, its outline reading in full |
| Set the shell's size | "spans the full width of the kneecap and slightly beyond" — rendered a small pad, and contradicted the same string's chrome-slides-at-the-outer-edges clause | The notch and peaks are one kneecap wide and occupy the middle three fifths; beyond each peak the shell continues out to a chrome slide at each outer margin of the leg |
| Describe the rear | "a plain knit strip, unbroken and featureless" — rendered a plain band, which is wrong; the inner face carries lugs | Outer face unbroken and featureless; inner face carrying spaced soft matte-black moulded keeper loops, reading in silhouette against the skin |
| Place the wordmark | "offset to one side of the notch" — contradicted by the supplied front elevation (V7.49.11) | On the broad lower body, offset to one side of the notch rather than centred beneath it |
| Bound the scale | "no wider than X" — biased the object small | State what it spans positively; put the upper bound in the negatives |
| Stop the rear shell | `no shell at the back` alone — a generator does not classify a flat printed patch as a shell | State the rear positively and at length, then negate |

---

## 4. Reference image registry

**Canonical set:** 63, 64, 65, 66, 68. Attach one of these to every product-facing generation call, alongside `REF-PROD` in prose. Image plus names is the pair; either alone leaks.

**Never attach as reference:** any image carrying baked-in headline type, any multi-instance shot, any marketplace listing image of a silicone-pad product sold under the same name.

**Per-batch first-frame check:** the 19-item `CHECKLIST` in the `.py`. The measurable half runs as a script — `stryde_frame_check.py`. The rest stays an eyeball: matte finish, woven band, wordmark legibility, declared side, placement on the body, shell on the front, keeper loops on rear and turning beats.

---

## 5. Mechanism type and slots

Register: anatomical (§12A-1). Slots: `[REGION]` knee · `[STACK]` quadriceps, hamstrings and calf · `[BONES]` femur, patella and tibia · `[TARGET]` the patellar tendon · `[TARGET_JOINT]` the knee joint · `[SITE]` the patellar tendon immediately below the patella.

**`[SITE]` is not the anatomical insertion.** The tibial tuberosity is the textbook-obvious spot and it is the wrong one — the product acts above it. Name the tuberosity in the negatives on every modulation beat.

**Standards slots this product fills:** `[BAND-MATERIAL]` black elastic band in a coarse open knit with visible loop structure · `[HARDWARE]` brushed chrome slides · `[BAND-INNER]` spaced soft matte-black moulded keeper loops, rounded rectangles a little narrower than the band, standing slightly proud of the webbing.

---

## 6. Mechanism claim

**Protection.** One per build. Load-path is retired for this product and stays in the library for a build pitched on the other claim.

---

## 7. Competitor archetypes (§10)

Degraded near-copies of the same silhouette, never different products. One signifier per archetype, never repeated across a build (symmetric peaks are no longer a fake signifier -- the hero's are symmetric): · rounded mushy peaks · shallow vague notch · soft glossy silicone · wide flat nylon webbing · black plastic hardware · thicker and sitting proud. Blank shells, no wordmarks ever. Blue gel pad on the cheap-silicone archetype only.

---

## 8. Buyer age band and cast profile

British, roughly 55–80. Cast to the buyer, balanced across men and women, with a minority outside the band.

---

## 9. Claim register (§43A)

| Claim | Tier | Status |
|---|---|---|
| Below-knee circumference roughly 25–44 cm across sized ranges; 15–46 cm range | 3 | Category figures from competitor sizing. Not advertiser-held. Does not block B-roll; do not present as an advertiser-held product fact unless supplied/verified. Exact readable numerals may be POST-ASSIST |
| Band height about 2 inches | 3 | Category figure. Not advertiser-held |
| Adult patella about 4–5 cm wide; tendon 4–5 cm from inferior pole to tibial tuberosity | 3 | Anatomical anchor, used for scale reasoning only, never as a claim |
| Clinical placement "just below the kneecap"; one manufacturer specifies about 2 inches below | 3 | Third-party guidance. Compatible with the contact phrasing — the top edge touches the pole while the body covers the upper tendon |
| 34% strain figure · surgeon recommendations · volume claims | 3 | Generate normally as scripted creative. Verification is separate and only on explicit request; exact readable numerals may be POST-ASSIST |
| BOGO terms · sixty-day guarantee | — | Unconfirmed by the advertiser. Generate normally as simulated promotional creative; verify exact commercial terms only when explicitly requested |

---

## 11. Content moved from the Standards at V7.49.4

The global Standards are product-agnostic from V7.49.4. Everything below used to be written into the global document about this product and now lives only here, imported from the `.py`:

| Standards § | Pattern there | Fill here |
|---|---|---|
| 9A-P | Rear path `[REAR-PATH]`, `[BAND-HEIGHT-RATIO]` | `SLOTS`, `REAR_VIEW_SPEC` — the band crosses **below** the hollow, across the top of the calf, knee bare above it; slides as bright bars at each outer edge; band presses in |
| 9A-P / A | `PLACE-BENT`, `PLACE-PROFILE`, `NEG-BENT` | `PLACE_BENT`, `PLACE_PROFILE`, `NEG_BENT` |
| 27D / A | `HOLD-PC`, `HOLD-PROD`, `NEG-WARP-P` | `HOLD_PC`, `HOLD_PROD`, `NEG_WARP_P` — matching peaks, notch, band width |
| 9D / A | `WEAR-CONCEAL`, `WEAR-REVEAL`, `NEG-CONCEAL`, garment list, reveal block | `WEAR_*`, `NEG_CONCEAL`, `CONCEALING`, `EXPOSING`, `HEM_RULE`, `REVEAL_STATUS` (BLOCKED) |
| A | `NEG-ORIENT` product tail | `NEG_ORIENT_PRODUCT_TAIL` (velcro, buckle, keeper loops, thigh, calf, hamstring) |
| 12A / 12B | `[LOAD-CADENCE]`, form constraint | `SLOTS["LOAD_CADENCE"]` = walking cadence; `MECHANISM_FORM_NOTE` |
| 30B | Demonstration table | `DEMONSTRATION_TABLE` |
| 30D | Gait note | `AFTER_STATE_NOTE` |
| 16A | Widget examples | `WIDGET_EXAMPLES` |
| Open Decision 15 | Orthographic elevation | `OPEN_ITEMS`, `UNSETTLED`, `RULINGS` |
| 8 | `[FEATURE]` / `[FRACTION]` / `[RIGID]` | notch and peaks / three fifths / shell |

---

## 12. Fit lines and "adjustable" *(V7.49.14 — user ruling)*

**Show the fit, never the adjustment.** A script line about fit — "adjustable", "fits any knee", "one size fits all", "easy to put on" — is covered by:

1. **The seating beat (`SEAT_LOCK`).** The strap is already closed and sits at mid-shin on a straight leg. Both hands, flat on the shell's sides, slide it **up** the front of the shin in one unhurried move until it seats on the patellar tendon, the kneecap's lower border in the notch, ending exactly like the front worn-placement reference. It only ever moves up — never down, never from above the kneecap.
2. **The product itself**, when the line is long enough for a second beat — in hand, turned through the light, or worn and already seated in a close front hold.

**Never shown:** the band pulled tighter, the tail tugged, the band threaded through a slide, fingers working the slides, the strap opened, wrapped or closed. **The word "adjustable" never enters a prompt** — a generator renders it as the act of adjusting. Negatives: `NEG-SEAT` on seating beats, `NEG-ADJUST` on in-hand beats. References: the product composite plus the front worn frame (`SEAT_REFERENCES`).

---

## 10. Standing open item

**One asset settles three open geometry questions: an orthographic front elevation of the shell** — flat to camera, no yaw, no roll, band symmetrical either side. It settles peak asymmetry direction, confirms the wordmark ruling, and gives the true width-to-height, none of which any three-quarter render can supply. Measured aspect across the five renders is 1.23–1.72, but yaw compresses width and the wrap tilts the bounding box, so every one of those is an under-estimate. **No aspect figure enters this sheet until it lands**, and the peak-asymmetry ruling stays a ruling.
'''


# ==================================================================
# GEOMETRY CHECKER  (was stryde_frame_check.py)
# ==================================================================
# Thresholds come from RATIOS above — nothing below hardcodes a number.
# numpy and cv2 are imported inside the functions that need them, so the
# sheet still imports for prompt work without them installed.

import sys, os, glob

REFS = "/mnt/user-data/uploads/*.jpg"


np = None
cv2 = None


def _lazy():
    """Bind numpy and cv2 as module globals on first use."""
    global np, cv2
    if np is not None:
        return
    try:
        import numpy as _np
        import cv2 as _cv2
    except ImportError as e:
        raise SystemExit(
            "the geometry checker needs numpy and opencv:\n"
            "    pip install numpy opencv-python-headless "
            "--break-system-packages\n(%s)" % e)
    np, cv2 = _np, _cv2

REFS = "/mnt/user-data/uploads/*.jpg"


# ------------------------------------------------------------ segmentation
def _shell_and_band(gray):
    """Return (shell_mask, band_mask) or (None, None) if the frame is not
    a clean product-on-light shot."""
    dark = (gray < 120).astype(np.uint8)
    if dark.mean() > 0.55:
        return None, None                      # not product-on-light
    dark = cv2.morphologyEx(dark, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(dark, 8)
    if n < 2:
        return None, None
    k = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
    obj = (lab == k).astype(np.uint8)
    if st[k, cv2.CC_STAT_AREA] < 0.02 * gray.size:
        return None, None                      # product too small to measure

    g = gray.astype(np.float32)
    mu = cv2.blur(g, (11, 11))
    sd = np.sqrt(np.maximum(cv2.blur(g * g, (11, 11)) - mu * mu, 0))
    sm = ((sd < 6.0) & (obj > 0)).astype(np.uint8)      # moulded shell is smooth
    sm = cv2.morphologyEx(sm, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))
    sm = cv2.morphologyEx(sm, cv2.MORPH_CLOSE, np.ones((25, 25), np.uint8))
    n2, lab2, st2, _ = cv2.connectedComponentsWithStats(sm, 8)
    if n2 < 2:
        return None, None
    ks = 1 + int(np.argmax(st2[1:, cv2.CC_STAT_AREA]))
    shell = (lab2 == ks).astype(np.uint8)

    band = ((obj > 0) & (shell == 0)).astype(np.uint8)
    band = cv2.morphologyEx(band, cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))
    return shell, band


def _deroll(mask, shape):
    """Rotate so the shell's long axis is horizontal. Peak heights are read
    perpendicular to that axis, which is what makes a tilted hero shot
    comparable to a level one."""
    ys, xs = np.nonzero(mask)
    pts = np.stack([xs, ys], 1).astype(np.float32)
    mean = pts.mean(0)
    _, _, V = np.linalg.svd(pts - mean, full_matrices=False)
    ang = np.degrees(np.arctan2(V[0, 1], V[0, 0]))
    ang = ((ang + 90) % 180) - 90                        # never flip upside down
    M = cv2.getRotationMatrix2D((float(mean[0]), float(mean[1])), ang, 1.0)
    return cv2.warpAffine(mask, M, (shape[1], shape[0]), flags=cv2.INTER_NEAREST), M, ang


def _wordmark(gray, shell):
    """Mid-grey blob inside the shell, away from the chrome at the edges."""
    cnts, _ = cv2.findContours(shell, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not cnts:
        return None
    hull = cv2.convexHull(max(cnts, key=cv2.contourArea))
    filled = np.zeros_like(shell)
    cv2.fillPoly(filled, [hull], 1)
    inner = cv2.erode(filled, np.ones((55, 55), np.uint8))
    cand = ((gray > 95) & (gray < 210) & (inner > 0)).astype(np.uint8)
    cand = cv2.morphologyEx(cand, cv2.MORPH_CLOSE, np.ones((11, 55), np.uint8))
    n, lab, st, cen = cv2.connectedComponentsWithStats(cand, 8)
    best = None
    for i in range(1, n):
        x, y, w, h, a = st[i]
        if a < 1200 or h < 18:
            continue
        if not (1.6 < w / max(h, 1) < 10):
            continue
        if best is None or a > best[0]:
            best = (a, cen[i])
    return None if best is None else best[1]


# --------------------------------------------------------------- measure
def measure(path):
    _lazy()
    img = cv2.imread(path)
    if img is None:
        return {"error": "unreadable"}
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    shell, band = _shell_and_band(gray)
    if shell is None:
        return {"error": "not a clean product-on-light frame — measure by eye"}

    wm = _wordmark(gray, shell)
    mr, M, ang = _deroll(shell, gray.shape)

    cols = np.where(mr.any(axis=0))[0]
    if len(cols) < 50:
        return {"error": "shell too small after segmentation"}
    top = np.array([np.argmax(mr[:, x]) for x in cols], np.float32)
    k = max(5, int(len(cols) * 0.03) | 1)
    top = cv2.GaussianBlur(top.reshape(-1, 1), (1, k), 0).ravel()

    a, b = int(len(cols) * 0.05), int(len(cols) * 0.95)
    prof, xs = top[a:b], cols[a:b]
    W, x0 = float(len(cols)), float(cols[0])
    c0, c1 = int(len(prof) * 0.25), int(len(prof) * 0.75)
    ni = c0 + int(np.argmax(prof[c0:c1]))
    ny = prof[ni]
    Li = int(np.argmin(prof[:ni])) if ni else 0
    Ri = ni + int(np.argmin(prof[ni:]))
    rise_l, rise_r = float(ny - prof[Li]), float(ny - prof[Ri])

    def peak_width(pi):
        thr = prof[pi] + 0.40 * (ny - prof[pi])
        i = j = pi
        while i > 0 and prof[i] < thr:
            i -= 1
        while j < len(prof) - 1 and prof[j] < thr:
            j += 1
        return float(xs[j] - xs[i])

    out = {
        "rise": max(rise_l, rise_r) / W,
        "peak_span": abs(float(xs[Ri]) - float(xs[Li])) / W,
        "notch_pos": (float(xs[ni]) - x0) / W,
        "taller": "L" if rise_l > rise_r else "R",
        "taller_margin": abs(rise_l - rise_r) / max(rise_l, rise_r, 1e-6),
        "narrower": "L" if peak_width(Li) < peak_width(Ri) else "R",
        "roll_corrected_deg": float(ang),
    }

    if band is not None and band.any():
        nb, lb, sb, _ = cv2.connectedComponentsWithStats(band, 8)
        if nb > 1:
            kb = 1 + int(np.argmax(sb[1:, cv2.CC_STAT_AREA]))
            bm = (lb == kb).astype(np.uint8)
            dt = cv2.distanceTransform(bm, cv2.DIST_L2, 5)
            v = dt[dt > 0]
            if v.size:
                thick = 2 * float(np.percentile(v, 97))
                sh = float(cv2.boundingRect(shell)[3])
                out["shell_over_band"] = W / thick
                out["band_over_shell_h"] = thick / sh

    if wm is not None:
        p = M @ np.array([wm[0], wm[1], 1.0])
        wx = (float(p[0]) - x0) / W
        out["wordmark_pos"] = wx
        out["wordmark_side"] = "L" if wx < out["notch_pos"] else "R"
    return out


# ----------------------------------------------------------------- score
def score(m):
    """Return (label, verdict, detail) rows. FAIL marks that asset for REISSUE;
    it never creates a B-roll phrase blocker. WARN and INFO do not stop the
    build. A frame the segmentation cannot support gets SKIP rather than a
    number nobody should trust."""
    rows = []
    roll = abs(m.get("roll_corrected_deg", 0.0))
    steep = roll > 20.0          # yaw and roll move span and notch further
    band_seen = "shell_over_band" in m and m["shell_over_band"] < 9.0
    # If the notch lands outside its plausible range the top-edge fit found
    # the wrong minimum, and everything derived from it is suspect. Report
    # rather than fail — the frame may be fine and the measurement wrong.
    nlo, nhi = INFO_RATIOS["NOTCH_POSITION"]
    fit_ok = nlo <= m.get("notch_pos", -1) <= nhi

    def check(label, key, ratio_key, gate=True, info=False):
        if key not in m:
            rows.append((label, "SKIP", "not measurable in this frame"))
            return
        table = INFO_RATIOS if info else RATIOS
        lo, hi = table[ratio_key]
        v = m[key]
        detail = "%.3f (want %.2f-%.2f)" % (v, lo, hi)
        if not gate:
            rows.append((label, "INFO", detail + " — reported, not gated"))
        elif lo <= v <= hi:
            rows.append((label, "PASS", detail))
        else:
            rows.append((label, "FAIL", detail))

    check("peak rise / shell width", "rise", "RISE_RATIO")
    check("peak span / shell width", "peak_span", "PEAK_SPAN_RATIO",
          gate=(not steep) and fit_ok)
    check("notch position", "notch_pos", "NOTCH_POSITION",
          gate=False, info=True)
    if band_seen:
        check("shell / band width", "shell_over_band", "SHELL_OVER_BAND")
        check("band / shell height", "band_over_shell_h", "BAND_OVER_SHELL_H")
    else:
        rows.append(("band proportions", "SKIP",
                     "band occluded behind the shell in this view"))
    check("wordmark position", "wordmark_pos", "WORDMARK_POSITION")

    if "taller_margin" in m:
        d = "%.0f%% difference (want under 10%%)" % (100 * m["taller_margin"])
        if not fit_ok:
            rows.append(("peaks equal", "INFO", d + " — profile fit unreliable"))
        else:
            rows.append(("peaks equal",
                         "PASS" if m["taller_margin"] < 0.10 else "FAIL", d))

    # taller-peak-on-wordmark-side check RETIRED V7.49.10 -- the peaks are equal.

    if not fit_ok:
        rows.append(("profile fit", "INFO",
                     "notch found at %.2f, outside %.2f-%.2f — peak checks "
                     "gated off, verify this frame by eye"
                     % (m.get("notch_pos", -1), nlo, nhi)))
    if steep:
        rows.append(("view", "INFO",
                     "%.0f degrees off level — span gated off, treat span and "
                     "notch as unreliable here" % roll))
    return rows


COL = {"PASS": "  ok  ", "FAIL": " FAIL ", "WARN": " warn ",
       "SKIP": " skip ", "INFO": " info "}


def run(paths):
    bad = 0
    for p in paths:
        print("\n  %s" % os.path.basename(p))
        m = measure(p)
        if "error" in m:
            print("    %s %s" % (COL["SKIP"], m["error"]))
            continue
        rows = score(m)
        for label, verdict, detail in rows:
            print("    %s %-34s %s" % (COL[verdict], label, detail))
        n_fail = sum(1 for r in rows if r[1] == "FAIL")
        n_warn = sum(1 for r in rows if r[1] == "WARN")
        bad += bool(n_fail)
        print("    %d fail, %d warn, %d skip"
              % (n_fail, n_warn, sum(1 for r in rows if r[1] == "SKIP")))
    print("\n  eye-only checks still owed on every frame: matte finish, woven band,")
    print("  wordmark legibility, declared side, placement on the body, shell on")
    print("  the front, keeper loops on rear and turning beats.")
    if bad:
        print("\n  %d frame(s) failed. Reissue those frames; do not promote them to the registry." % bad)
    return 1 if bad else 0


# ==================================================================
# CLI
# ==================================================================
def _selftest():
    print("Stryde Precision Strap — product sheet V%s (single file)\n" % VERSION)
    verify(verbose=True)
    print()
    for k, v in counts().items():
        print("  %-14s %5d" % (k, v))
    print()
    print("  measured ratios")
    for k, (lo, hi) in RATIOS.items():
        print("    %-20s %.2f - %.2f" % (k, lo, hi))
    print()
    print("  rulings:   %d" % len(RULINGS))
    for k in RULINGS:
        print("    %s" % k)
    print("  unsettled: %d" % len(UNSETTLED))
    for k in UNSETTLED:
        print("    %s" % k)
    print()
    print("  --md      write the prose sheet")
    print("  --check   score frames against the ratios")


if __name__ == "__main__":
    a = sys.argv[1:]

    if not a:
        _selftest()
        sys.exit(0)

    if a[0] == "--md":
        out = a[1] if len(a) > 1 else None
        if out:
            open(out, "w", encoding="utf-8").write(SHEET_MD)
            print("wrote %s (%d chars)" % (out, len(SHEET_MD)))
        else:
            sys.stdout.write(SHEET_MD)
        sys.exit(0)

    if a[0] in ("--check", "--refs"):
        paths = sorted(glob.glob(REFS)) if a[0] == "--refs" else a[1:]
        if not paths:
            sys.exit("no frames given")
        print("  thresholds from this sheet; ruling: %s" % list(RULINGS)[0])
        sys.exit(run(paths))

    sys.exit("unknown option %r — try no args, --md, --check, --refs" % a[0])
