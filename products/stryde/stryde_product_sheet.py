#!/usr/bin/env python3
"""
STRYDE PRECISION STRAP — PRODUCT SHEET, SINGLE FILE.  V7.49.31

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
    one size fits all ........... FIT_SNUG, worn_ref_prompts() (V7.49.15)
    the size lock ............... SIZE_LOCK, SIZE_WORN, SIZE_HELD, SIZE_OBJECT (V7.49.21)
    how it is worn .............. WEAR_GUIDE (V7.49.21)
    which images to attach ...... REFS_USE, refs_for(shot) (V7.49.23)
    held beats .................. HELD_GRIPS, NEG_HELD_P (V7.49.23)
    observed failures ........... NEG_OBSERVED (V7.49.23)
    which knee .................. SIDE_RULE, side_from_script() (V7.49.24)
    the box and the offer ....... PACKAGE, OFFER, package_prompts() (V7.49.24)
    the cheap copy .............. FAKE_BASE, FAKE_ARCHETYPES, NEG_FAKE_HERO (V7.49.28)
    the back of the pad ......... PAD_BACK_SHOT (V7.49.28)
    the V7.49.4 pattern fills ... HOLD_PC, HOLD_PROD, NEG_WARP_P, WEAR_*,
                                  REAR_VIEW_SPEC, DEMONSTRATION_TABLE, ...
                                  (content moved OUT of the Standards)

USE

    python3 stryde_product_sheet.py              self-test, counts, ratios
    python3 stryde_product_sheet.py --md         write the prose sheet out
    python3 stryde_product_sheet.py --check f... score frames against RATIOS
    python3 stryde_product_sheet.py --refs       score the supplied product photos
    python3 stryde_product_sheet.py --worn-refs  print the three worn-reference T2I prompts
    python3 stryde_product_sheet.py --product-set print the five product-set T2I prompts

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

VERSION = "7.49.31"

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
    "SIDE":     None,   # from the script, per build -- SIDE_RULE (V7.49.24)
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
"leg, the black coarse-knit elastic band running from the slides around behind the knee. Wordmark horizontal and "
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
"the leg silhouette standing proud of the outline as a small bright bar. The band presses in: flesh swells slightly "
"above and below it, the band's own edges stay straight while its line follows the curve of the leg, a few "
"degrees off horizontal, never a drawn line. The shell is entirely hidden by the leg and no shell, wordmark or fastening appears anywhere on "
"the rear.")

ORIENT_C = (
"The rigid shell stays on the front of the knee throughout, never rotating around the leg. Only the "
"black coarse-knit elastic band crosses the back of the leg, below the hollow behind the knee and across the top of "
"the calf with the knee bare above it, its outer face carrying the two black keeper loops side by side at the rear, "
"with the chrome slides standing proud at the outer sides as small bright bars. The band "
"presses in: flesh swells above and below it and its line follows the curve of the leg. No shell, "
"wordmark or fastening appears at the rear.")

# Bent-knee placement. The standing spec guards against the shell riding UP
# onto the kneecap; with the knee flexed the opposite failure appears -- a gap
# opening between the kneecap and the notch, so the shell reads disengaged
# from the thing it acts on. Stated positively as contact, per PLACE-LOCK.
PLACE_BENT = (
"With the knee bent the kneecap stands out as a distinct bulge and the shell sits HIGH, pushed well up the "
"leg and tight against it: the shell's top edge sits level with the kneecap's lower pole, the concave notch "
"pressed firmly up into the underside of the kneecap along its whole curve, the flesh of the kneecap filling "
"it with no gap of bare skin anywhere between them, and the two matching peaks rising either side to flank "
"the lower half of the kneecap's sides -- up to but never past its middle and never covering any of its face. "
"The kneecap's own face stays completely uncovered above the shell, its outline reading in full. The shell's "
"lower body reaches only just onto the top of the shin, never down the shin. A brushed "
"chrome slide sits at each outer margin of the leg with the black coarse-knit band running back from it. The shell "
"never rotates with the joint -- the notch stays under the kneecap through every angle of flexion.")

# The shell wraps far enough round that a side or three-quarter view still
# reads most of its face and the whole wordmark. Without this a profile beat
# renders a flat panel stuck on the front of a leg.
PLACE_PROFILE = (
"Seen from the side or three-quarter with the knee bent, the shell wraps far enough around the leg that most "
"of its face still reads: the nearer pointed peak curls up and over toward the front of the knee, the notch "
"dips between the peaks under the kneecap, and the wordmark runs horizontally along the shell's lower body, "
"readable rather than edge-on. At the rear edge of the shell a brushed chrome slide stands proud with the "
"black coarse-knit band folding through it and running on around the leg. The shell's own curve follows the leg -- "
"it is a wrapped plate, never a flat panel stuck on the front.")

NEG_BENT = (
"no shell above the kneecap, no shell covering the kneecap, no shell sitting low on the shin, no shell top edge "
"below the kneecap's lower pole, no gap of bare skin between the kneecap and the "
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
"no band tracing a perfect straight line across the leg, no band floating off "
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
"concave notch that occupies only the middle three fifths of its width, waisted off-centre, a "
"black elastic band in a coarse knit with a visible textured weave carrying two black keeper loops on its outer "
"face, a brushed chrome slide inset flush into each end of the shell carrying three engraved dotted chevrons, and a lowercase grey stryde wordmark "
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
SEAT_REFERENCES = ("front.webp", "back.webp", "front")   # V7.49.23: originals + PLACEMENT_REFERENCES["front"]; the composite was never in the repo

# --- one size fits all (V7.49.15, user) --------------------------------
# One unit, no sizes. The shell is a fixed size; the elastic band takes up
# the leg. A worn frame shows it fitting THIS leg exactly: snug, flat, no
# slack, the shell scaled to the knee. Positive wording only -- this string
# goes into T2I, which has no negative channel.
FIT_SNUG = (
"One size fits all, and it fits this leg exactly: the elastic band runs snug and flat all the way round the "
"leg, pressing in lightly so the skin dips a touch at its edges, the band's tail folded back through each "
"chrome slide and lying flat against the band, every part of it in contact with the skin. The shell is "
"scaled to this knee: its notch is one kneecap wide and the shell spans the whole front of the joint, a "
"chrome slide at each side of the leg.")

# --- the size lock (V7.49.21, user: "we need a perfect sizing so we always get
# the same size") ------------------------------------------------------------
# One unit, one size. Proportions are MEASURED on the canonical front photo
# (front.webp, layer 1, straight-on): shell 688 px slide-to-slide x 275 px
# peak-to-lowest-edge = 2.50; product_front.jpg (eb1e16e1) 2.32; band 147 px
# = 0.53 of the shell's height. Absolute sizes are a RENDERING size derived
# from those proportions and Tier-3 adult anatomy (thumb ~2 cm wide, kneecap
# ~5 cm tall, knee ~10-11 cm across the front) -- not advertiser-held. Replace
# with supplied dimensions the moment they exist.
SIZE_LOCK = {
    "shell_width_cm":   12.0,   # slide to slide, along the curve
    "shell_height_cm":  5.0,    # peak tips to the lowest point of the bottom edge
    "band_width_cm":    2.5,    # band height, edge to edge
    "shell_aspect":     (2.3, 2.6),   # width / height, measured straight-on
    "band_over_shell_h": (0.45, 0.60),  # edge-to-edge by eye, confirmed on back.webp V7.49.22
                                        # (band ~175 px vs shell ~310 px head-on). The --check
                                        # distance transform reads the same band as 0.351 on
                                        # front.webp: its dark threshold drops the knit's light
                                        # fibres, so it UNDER-reads bands. RATIOS keeps its own gates.
    "notch_rise_over_w": (0.15, 0.21),  # front.webp 0.18
    "peak_span_over_w":  (0.55, 0.66),  # front.webp 0.60
    "worn_band_over_leg": (0.20, 0.28), # band height / leg width at the calf, from behind
    "held_shell_in_thumbs": (5.0, 6.0), # shell width / the holder's thumb width
    "source": "front.webp measured V7.49.21; anatomy Tier 3; NOT advertiser-held",
}

# The same size said three ways -- one per context. Positive wording (T2I).
SIZE_OBJECT = (
"Its size never changes: a rigid shell about 12 cm across from slide to slide and about 5 cm tall at the "
"peaks, so it is roughly two and a half times as wide as it is tall, with a band about 2.5 cm wide -- the band "
"about half as tall as the shell.")
SIZE_WORN = (
"Its size never changes: the shell spans the leg's whole front width at the patellar tendon with a chrome "
"slide at each side of the leg, it stands about as tall as the kneecap itself, and the band is about a "
"quarter of the leg's width at the top of the calf.")
SIZE_HELD = (
"Its size never changes: the shell is about five to six of the holder's thumb-widths across, overhanging the "
"pinching hand at both ends, and about as tall as the thumb is long from its tip to its base knuckle; the "
"band is a little wider than the thumb.")

# --- which knee (V7.49.24, user: "depends on the script") -----------------------
# The side is read from the script, never chosen for looks. Declared once at the
# act map and held on every beat of the build (Standards §9: continuity).
SIDE_RULE = (
    "1. The script names a knee (left or right, including 'my left knee', 'the right one') -> that knee.",
    "2. The script names no knee -> right, which matches every locked worn reference.",
    "3. Declared once at the act map, held on every beat; never both knees; never switched mid-build.",
    "4. A left-knee build needs left-knee worn references first -- a right-knee frame is never "
    "mirrored, because a mirror reverses the wordmark. Generate them from worn_ref_prompts('left').",
)


def side_from_script(text):
    """Apply SIDE_RULE to a script. Returns ('left'|'right', reason). A script that
    names both knees is returned as ('right', ...) with a flag for the human."""
    import re as _re
    t = text.lower()
    left = bool(_re.search(r"\bleft\s+(knee|leg)\b", t))
    right = bool(_re.search(r"\bright\s+(knee|leg)\b", t))
    if left and right:
        return "right", "FLAG: script names both knees -- confirm the side with the user"
    if left:
        return "left", "script names the left knee"
    if right:
        return "right", "script names the right knee"
    return "right", "script names no knee -- default right (matches the locked worn references)"


# --- the box and the offer (V7.49.24, user) ----------------------------------
# Our own box. The offer is ALWAYS Buy 1 Get 1 Free, so there are ALWAYS two
# straps in it. Rendering spec written V7.49.24 -- the physical box does not
# exist yet; update this when it does.
OFFER = "Buy 1 Get 1 Free -- always (user-confirmed V7.49.24)"
PACKAGE = {
    "box":      ("a rigid two-piece box, a lid over a base, matte black all over, about 28 cm wide, "
                 "16 cm deep and 8 cm tall -- sized to hold two straps side by side"),
    "logo":     ("the lowercase grey stryde wordmark centred on the lid, in the same bold rounded lettering "
                 "and the same grey as the wordmark on the shell; nothing else printed anywhere on the box"),
    "inside":   ("a matte-black insert with two shaped wells side by side; in each well one strap lying FLAT "
                 "(V7.49.26, user: 'it's a strap, not rock solid') -- shell face up at the front, wordmark "
                 "readable, the soft band a flattened loop behind it, joined at both slides; never apart "
                 "(V7.49.25)"),
    "contents": "always exactly two straps -- never one, never three, no other items",
    "text":     ("no offer text, price, badge or sticker on the box in any prompt -- 'Buy 1 Get 1 Free' is "
                 "added in the edit (Standards §17)"),
}
PACKAGE_LOCK = (
"A rigid two-piece gift box, a lid over a base, matte black all over, about 28 cm wide, 16 cm deep and 8 cm "
"tall. The only thing printed on it is the lowercase grey stryde wordmark centred on the lid, in the same bold "
"rounded lettering and grey as the wordmark on the strap's shell. Inside, a matte-black insert with two shaped "
"wells side by side holds exactly two identical straps, one in each well. Each strap is ONE piece lying FLAT "
"in its well, because the band is soft elastic, not rigid: the shell lies face up at the front of the well, "
"its peaks and notch pointing toward the back of the box, its grey wordmark horizontal and readable from the "
"front; the soft knit band leaves the chrome slide at each end of the shell and lies flat and relaxed behind "
"it as a flattened closed loop, joined to the shell at both slides.")
NEG_PACKAGE = (
"no text on the box except the stryde wordmark, no offer text, no price, no badge, no sticker, no barcode, no "
"white box, no coloured box, no glossy box, no window in the lid, no third strap, no single strap in the box, "
"no loose strap outside the insert, no extra items in the box, no shell separate from its band, no shell "
"resting on top of a loop of band, no strap standing upright as a stiff ring, no strap turned on its side")

PACKAGE_SCENES = {
    "closed": ("Product photograph, vertical 9:16, on a plain seamless white background with soft even light "
               "and a soft grey shadow below, the closed box seen three-quarter from the front and a little "
               "above so the lid and the wordmark on it read clearly."),
    "open":   ("Product photograph, vertical 9:16, on a plain seamless white background with soft even light "
               "and a soft shadow, the box open with its lid leaning against the back of the base, seen from "
               "the front and above so both straps in the insert read clearly."),
}
PACKAGE_ATTACH = ("front.webp", "back.webp")

# Generated V7.49.24, agent verdict USE (§22V); awaiting the user's lock.
# Model passed nano_banana_pro, logged nano_banana_2 (routing fault).
PACKAGE_REFS_STATUS = ("LOCKED V7.49.27 by the user -- closed e8c4df4b, open a9409405. "
                       "Replaced only on a user instruction.")
PACKAGE_REFS = {
    "closed": {"file": "stryde_refs/package_closed.jpg", "job_id": "e8c4df4b-ceb4-404f-ac1d-989f2e8b9154",
               "attempt": "1 of 1", "flags": ""},
    "open":   {"file": "stryde_refs/package_open.jpg", "job_id": "a9409405-2d78-4802-bdf0-01c7266b18a1",
               "attempt": ("flat layout (V7.49.26), 3 of 3 -- 950a39d7 and c4aec9e7 REGENERATE Q2: wrong "
                           "product, a small buckle shell with horn peaks (user: 'wrong product'); c4aec9e7 was "
                           "anchored on 950a39d7 and copied its wrong shell. 3 = only correct references "
                           "attached (front.webp, tq_left 0cdf393f, closed box e8c4df4b), layout in words. "
                           "Upright-ring layout (bea8b220, 5448322e, 3f1b84a8) superseded by the user."),
               "flags": "band loop folded flat under each shell -- only its ends show at the slides"},
}


def package_prompts():
    """The two box reference T2I prompts (V7.49.24). Nano Banana Pro, 9:16, 2k."""
    strap = REF_PROD.replace("The product exactly as in the attached reference image",
                             "Each strap exactly as in the attached product photos")
    out = {}
    for k, scene in PACKAGE_SCENES.items():
        parts = [scene, PACKAGE_LOCK]
        if k == "open":
            parts += [strap + " two identical straps.", SIZE_OBJECT]
        else:
            parts += ["The box is closed; the straps inside are not visible."]
        out[k] = " ".join(parts)
    return out


# --- the cheap copy (V7.49.28, user: "looks alike STRYDE but looks cheap and
# easy to get damaged") --------------------------------------------------------
# Standards §10: a near-copy of the hero silhouette, visibly cheaper, no wordmark,
# in a real home (never on white). FAKE_BASE is on EVERY copy; one archetype from
# FAKE_ARCHETYPES is added per build and never reused in that build. A knock-off
# may be damaged or break (Standards §27E / §9C SIDE-BY-SIDE); the hero never does.
FAKE_BASE = (
"A cheap copy of the strap: at a glance the same shape -- a shell with two peaks and a notch, a band, a "
"fastening at each end -- but everything about it is cheaper and already worn. The shell is thin shiny "
"black plastic with no wordmark, its peaks rounded and soft, scuffed and scratched across the face, a small "
"crack running in from one edge; the band is a thin flat shiny nylon strap with frayed edges and loose "
"threads; the fastenings are thin black plastic buckles instead of chrome, one of them chipped. It looks "
"like it came in a plastic bag and has been worn a few times too many.")
FAKE_ARCHETYPES = (
    ("too small", "the whole copy visibly undersized -- a narrow shell that covers only a small patch below "
     "the kneecap and never reaches the sides of the knee (the script line 'too small to reach it')"),
    ("soft silicone", "the shell is soft floppy glossy silicone that sags and folds instead of holding its shape"),
    ("wide webbing", "a wide stiff flat nylon webbing band with a velcro tab, fraying at the cut end"),
    ("thick and proud", "a bulky thick shell that sits proud of the leg with a gap at its edges"),
    ("blue gel", "a blue gel pad showing at the inside edge of the shell (cheap-silicone archetype only)"),
    ("breaking", "the copy failing on camera: the band's stitching splitting or the shell snapping at the "
     "crack when it is flexed -- SIDE-BY-SIDE only, the hero next to it never gives"),
)
NEG_FAKE_HERO = (
"no wordmark on the copy, no chrome on the copy, no copy with a different silhouette, no copy on a white "
"background, no copy in a shop, no damage on the hero strap, no crack in the hero shell, no fraying on the "
"hero band")

# --- the back of the pad (V7.49.28, user: "inside a silicone pad -- it should be
# the back of the silicone pad") ------------------------------------------------
# The script line about the pad is covered by the BACK of the shell -- the inner
# pad turned to the lens -- never by the front. Then the mechanism shot.
PAD_BACK_SHOT = (
"The strap turned round so the back of the shell faces the camera: the inside of the shell, the pad that "
"sits against the skin, fills the frame -- a plain, smooth, matte-black pad following the shell's curve, "
"with no markings, no texture pattern and no second colour -- the two peaks rising along its top edge, a "
"chrome slide at each end, the band running away from the slides behind it. No wordmark is visible from "
"this side.")

# --- anatomy look samples (V7.49.30) -----------------------------------------
# One sample per Standards density (Appendix A ANAT-A..D) on this knee, all in the
# ANAT-HOT state with the glow placed at [SITE]. For choosing a look -- NOT locked,
# never attached as a reference (anatomy beats carry no product photo).
ANATOMY_SAMPLES = {
    "ANAT-A": {"file": "stryde_refs/anatomy_samples/anat_A.jpg", "job_id": "e2f2335f-d480-4998-a3e9-2f3eb25fba82",
               "reads": "full stack; glow broad, spilling onto the tibia -- the point reads least sharply"},
    "ANAT-B": {"file": "stryde_refs/anatomy_samples/anat_B.jpg", "job_id": "5dd74ef4-c1ad-4e88-a5cc-68eb16358abb",
               "reads": "ghost limb; a tight bright spot exactly on the tendon below the patella -- the clearest point"},
    "ANAT-C": {"file": "stryde_refs/anatomy_samples/anat_C.jpg", "job_id": "a85ccc9c-fe8a-4420-a80c-c6c062e49973",
               "reads": "silhouette; the whole tendon lit below the patella, moody, instant read"},
    "ANAT-D": {"file": "stryde_refs/anatomy_samples/anat_D.jpg", "job_id": "55f4ea05-5303-4cb8-8064-70223cbddc23",
               "reads": "physical model on a kitchen worktop, thumb on the tendon below the patella; phone capture"},
}
# V7.49.31 (user): A and B the other way round from the agent's suggestion.
ANATOMY_LOOK = {
    "point":      "ANAT-A",   # the spot below the kneecap, the load arriving (e.g. '17x', 'one small spot')
    "protection": "ANAT-A",   # the pad catching the force, the spot staying calm
    "conditions": "ANAT-B",   # bone on bone, worn cartilage, meniscus
}
# ANAT-A's sample spread its glow onto the tibia; every ANAT-A beat carries this.
ANAT_A_POINT_TIGHT = (
"The glow is one tight, bright spot on the patellar tendon just below the kneecap, sharp-edged and small, "
"never spreading down onto the shin bone or across the joint; the bones and muscles around it stay calm.")

# --- the inner pad (V7.49.23) -----------------------------------------------
# Read off back.webp. Used on held beats and any view of the inside of the shell.
# Never the word "silicone" (it renders the soft glossy fake, §10).
INNER_PAD = (
"The inside of the shell is a plain, smooth, matte-black pad following the shell's curve, with no markings, "
"no texture pattern and no second colour.")

# --- held beats (V7.49.23, user: "there are so many ways to hold it") -------
# NOT a locked pose. Any of these grips, chosen per beat and varied across a
# build; every one keeps the three fixed rules: the hand is on the pad or the
# shell's edge, never on the band or the slides, never across the wordmark.
HELD_GRIPS = (
    ("bottom-edge pinch",
     "thumb in front on the shell's bottom edge below the wordmark, fingers behind on the pad, band slack "
     "round the wrist (HELD_EXAMPLE shows this one)"),
    ("open palm",
     "the strap resting across an open upturned palm, the pad on the palm and the front face up to the lens, "
     "fingers loosely curled at the shell's lower edge, the band draped over the hand"),
    ("fingertips behind",
     "held up by the fingertips pressed flat on the pad behind the shell, the thumb at one lower corner of the "
     "shell, the front face square to the lens, the band hanging below"),
    ("turned through the light",
     "the bottom-edge pinch, the wrist slowly turning the shell a little either way so the chrome slides catch "
     "the light -- video only, one slow turn"),
    ("two-hand presentation",
     "both hands, each with fingers on the pad near one end of the shell and thumbs on the bottom edge, "
     "holding it out square to the lens -- briefly, on a presentation landing only (§9A)"),
)
HELD_RULES = ("the hand is on the pad or the shell's edge", "never on the band", "never on the chrome slides",
              "never across the wordmark", "the peaks and notch stay visible")

# I2V negatives for held beats (product tail; merges with the Standards' NEG-HELD).
# "no second strap" is dropped on a pair-pack (Buy 1 Get 1 Free) beat, where two
# units side by side are required (Standards §9 pair-pack carve-out).
NEG_HELD_P = (
"no hand gripping the band, no fingers on the chrome slides, no fingers across the wordmark, no fingers over "
"the peaks or the notch, no flat palm pressed on the front face, no strap swinging by its band alone, no band "
"being stretched, no band being threaded, no product changing hands, no second strap, no strap worn while held")

# Standing negatives accumulated from observed failures (Appendix B item 11),
# dated. I2V only -- T2I has no negative channel.
NEG_OBSERVED = (
"no V-shaped notch, no crown-shaped peaks, no tall horn peaks, no deep U-shaped shell, no slot-shaped notch, "
"no flat rectangular shell, no slab shell without peaks, no chrome slide mounted on the front face, no slide "
"on the band instead of the shell's end, no moulded frame around the slide, no sideways chevrons, no band "
"leaving the bottom edge of the shell, no product tipped on its side, no watch-strap band, no keeper loop "
"shaped like a buckle, no shell drawn apart from its band, no strap turned on its side with the wordmark "
"vertical")
NEG_OBSERVED_LOG = (
    ("V7.49.15", "worn bent", "shell tall and narrow, U-shaped with horn peaks"),
    ("V7.49.18", "three-quarter right", "V notch, crown peaks, slide on the face, watch-strap band"),
    ("V7.49.18", "profile", "slot notch, slab shell, slide on the face"),
    ("V7.49.18", "macro", "invented moulded slide frame, sideways chevrons"),
    ("V7.49.18", "held", "flat rectangular shell with no peaks"),
    ("V7.49.19", "side", "slide on the band's face, shell reduced to a thin inner shape"),
    ("V7.49.19", "side", "product tipped, band leaving the shell's bottom edge"),
    ("V7.49.20", "held", "fingers curled over the top edge hiding the notch and peaks"),
    ("V7.49.21", "product front", "camera above, notch deep and narrow, peaks 12% unequal"),
    ("V7.49.24", "package open", "each strap drawn as two pieces -- a flat band loop with the shell sitting on top"),
    ("V7.49.25", "package open", "one-piece rings turned 90 degrees in the box, peaks sideways, wordmark vertical"),
    ("V7.49.26", "package open", "flat layout: shell redesigned as a small buckle with horn peaks, thin lettering"),
)

# --- how the strap is worn (V7.49.21, user: "it needs to be clarified") ------
# The one reference answer for every worn, seating and bent beat. Every line
# is already enforced by a locked string; this is the plain-words version.
WEAR_GUIDE = (
    ("ONE UNIT, ONE KNEE",
     "One strap on one knee -- the side declared at the act map, held all build. Never both knees, never "
     "two units on one person. The same unit fits left or right; it is not handed."),
    ("SHELL ON THE FRONT, NOTCH UP",
     "The rigid shell sits on the front of the leg, the notch at the top pointing up at the kneecap, the "
     "wordmark upright and readable to someone facing the wearer. Never upside down, never turned to the "
     "side or the back (PLACE_LOCK, ORIENT_LOCK)."),
    ("HEIGHT -- ON THE PATELLAR TENDON",
     "Directly below the kneecap, on the tendon. The notch cups the kneecap's lower border with no gap; "
     "straight leg -- peaks no higher than the base of the kneecap's sides; bent leg -- the shell sits "
     "high, top edge level with the kneecap's lower pole, peaks to the lower half of its sides. The "
     "kneecap's face is always fully uncovered (PLACE_LOCK, PLACE_BENT)."),
    ("BAND ROUND THE BACK, BELOW THE HOLLOW",
     "From the slides the band runs level round the back of the leg, below the hollow behind the knee, "
     "across the top of the calf, the two keeper loops together at the centre back. Only the band is at "
     "the back -- no shell, no wordmark, no fastening (ORIENT_LOCK)."),
    ("FIT -- ONE SIZE, SNUG",
     "One size fits all: the elastic band takes up the leg. Snug and flat all the way round, pressing in "
     "lightly, no slack, no loose tail, no gap between band and skin (FIT_SNUG, SIZE_LOCK)."),
    ("ON BARE SKIN",
     "Worn directly on the skin. Under trousers it is hidden (CONCEALED); it is never worn over "
     "clothing (§9D, CONCEALING / EXPOSING)."),
    ("PUTTING IT ON",
     "The band stays closed. The strap goes over the foot like a sock cuff, sits at mid-shin on a straight "
     "leg, and both hands, flat on the shell's sides, slide it UP the front of the shin until the kneecap "
     "stops it on the tendon. Never opened, threaded, fastened or tightened on camera (SEAT_LOCK, "
     "ADJUSTABLE_RULE)."),
    ("WHILE WORN",
     "Hands off it (Standards §9). It holds its place through walking, stairs, sitting and standing; the "
     "shell never rotates with the joint and never slides down the shin."),
    ("HELD, NOT WORN",
     "In the hand it is pinched at the shell's bottom edge -- thumb in front below the wordmark, fingers "
     "behind on the pad, band slack round the wrist (RULINGS['held_on_pad']). Held and worn never in the "
     "same beat."),
    ("NEVER SHOWN",
     "Taking it off, the band open, the band being adjusted, two units worn, the shell on the thigh, "
     "calf or kneecap."),
)

# Leg-skin clause for worn frames with no face in them (SKIN-A is written
# for faces). Buyer age band, not an identity.
LEG_SKIN = (
"Real unretouched skin on an adult leg of about sixty: fine hairs on the shin and thigh catching the light, "
"visible pores, faint veins at the side of the knee, soft creases and slight redness over the kneecap, a "
"mildly uneven tone between thigh, knee and shin. Every crease and hair casts its own small shadow.")

# CAP-A and BODY-WHOLE, copied verbatim from the Standards (Appendix A) so the
# prompts below are complete. The Standards own them: re-copy on any change.
CAP_A = (
"Capture must look like a phone camera file, not a lit scene: Smart HDR 5 tone-mapping lifting the shadows so "
"they read flat rather than deep, highlight clipping at the brightest edge of frame, natural warm-neutral "
"colour temperature straight out of the phone, subtle lens distortion and softening at the frame edges "
"consistent with a 24mm phone lens. No colour grading, no retouched skin, no shaped or lit light on the subject.")
BODY_WHOLE = (
"EVERY PERSON IN FRAME IS ANATOMICALLY WHOLE. Each person has exactly one head attached to one neck, two arms "
"and two legs, each joined to the body at the right place and bending only at real joints. Every visible hand "
"has one thumb and four fingers, separate, correctly sized, gripping or resting the way a real hand does. Any "
"part of a body that is not visible is out of view for a reason you can see — cut by the frame edge or hidden "
"behind a named object — never simply missing inside the frame.")

WORN_REF_SCENES = {
    "front": ("Vertical 9:16 phone photo, taken at knee height from straight in front of the right leg of a "
              "standing adult in dark grey shorts ending mid-thigh, weight on the right leg, knee straight, the "
              "frame running from mid-thigh to mid-shin with the knee in the centre, a plain living room behind "
              "out of focus, daylight from a window to one side."),
    "rear":  ("Vertical 9:16 phone photo, taken at knee height from directly behind the right leg of a "
              "standing adult in dark grey shorts ending mid-thigh, knee straight, the frame running from "
              "mid-thigh to mid-calf with the back of the knee in the centre, a plain living room wall behind, "
              "daylight from a window to one side."),
    "bent":  ("Vertical 9:16 phone photo, taken from about forty-five degrees to the right of straight in front "
              "of the knee, so both peaks, the notch between them and the centred wordmark read, of an "
              "adult in dark grey shorts ending mid-thigh, seated on the edge of a sofa with the right knee bent to about a right "
              "angle and the foot flat on the floor, the frame running from mid-thigh to the ankle with the knee "
              "in the upper centre, daylight from a window across the knee."),
}

# Bent-frame shape guard (V7.49.15, after bent attempt 2 drew a tall narrow
# U-shell with horn peaks). Aspect since settled: SIZE_LOCK (V7.49.21).
WORN_REF_SHAPE = (
"The shell keeps the exact proportions of the front product photo: far wider than it is tall, a broad low "
"plate wrapping the front of the knee, the two peaks broad and low, the notch a wide rounded curve between "
"them. The wordmark is the bold rounded grey lowercase lettering of the product photos. Each chrome slide is a "
"slim bar with three small fine dotted chevrons.")

# Attach these with each prompt (products/stryde_refs/). The product photos
# carry the object; the prompt carries the placement.
WORN_REF_ATTACH = {
    "front": ("front.webp", "three_quarter_b.jpg"),
    "rear":  ("back.webp", "front.webp"),
    "bent":  ("three_quarter_b.jpg", "front.webp"),
}


# --- product set (V7.49.18) ---------------------------------------------
# Fills the gaps in PRODUCT_PHOTOS: a matched three-quarter pair, a side
# profile, the product held in one hand (§9A), and a hardware close-up.
# front.webp and back.webp stay the product's identity and are never
# regenerated. Studio frames match the supplied photos' register; the held
# frame is Mode 1 phone capture (§9A: a product in a hand is never a catalogue photo).
PRODUCT_SET_STUDIO = (
"Product photograph, vertical 9:16, on a plain seamless white background with soft even light from above "
"and the front, the product floating with a soft grey shadow on the ground below it, exactly the lighting and "
"background of the attached product photos, sharp focus across the whole object, no props and no added text "
"or graphics.")

PRODUCT_SET_RING = (
"The band is closed in a loop behind the shell exactly as in the product photos, standing open as a round "
"ring as if around an invisible leg, the band's tail folded back through each chrome slide and lying flat.")

PRODUCT_SET_VIEWS = {
    "tq_left": ("Seen three-quarter from the front left, about forty-five degrees: the shell's front face, both "
                "peaks, the notch and the wordmark read, the left chrome slide nearest the camera, the band "
                "curving away behind to the right, the far slide just visible at the far end of the shell."),
    "tq_right": ("Seen three-quarter from the front right, about forty-five degrees: the shell's front face, both "
                 "peaks, the notch and the wordmark read, the right chrome slide nearest the camera, the band "
                 "curving away behind to the left, the far slide just visible at the far end of the shell."),
    "profile": ("Seen exactly from the side, edge-on to the shell: the shell reads as a rigid curved plate bending "
                "around the ring, the near peak rising at its top edge, the near chrome slide facing the camera "
                "with its three dotted chevrons, the band continuing round behind as a ring with the two keeper "
                "loops on its outer face at the back."),
    "front_view": ("Seen exactly straight-on from the front, level with the product, no turn and no tilt, as "
                   "flat to the camera as the attached front product photo: both peaks equal, the notch dead "
                   "centre, the wordmark centred beneath it, a chrome slide at each end, the band's two sides "
                   "just visible leaving each slide."),
    "back_view": ("Seen exactly straight-on from the back, level with the product, no turn and no tilt, as in "
                  "the attached back product photo: the band crossing the front of the frame with its two black "
                  "keeper loops side by side at the centre, the shell's plain inner face behind it with both peaks "
                  "rising above the band, a chrome slide at each end, no wordmark visible."),
    "side_view": ("Seen exactly from the side at ninety degrees, level with the product, looking straight at "
                  "one end: that end's chrome slide faces the camera flat with its three dotted chevrons and the "
                  "band threading through it, the shell curving away to one side as a rigid wrapped plate with "
                  "the silhouette of its peaks along the top edge, the band ring running away to the other side "
                  "with the keeper loops on its outer face at the back."),
    "macro": ("Close-up filling the frame with one end of the strap: the matte-black end of the shell, the brushed "
              "chrome slide inset flush into it with its three engraved dotted chevrons crisp, and the black "
              "coarse-knit elastic band threading through the slide and folding back on itself, the textured "
              "weave resolved stitch by stitch, the band's edges straight."),
}

PRODUCT_SET_HELD = (
"Vertical 9:16 phone photo, close, of an adult casually showing the strap to the camera at chest height in a "
"lived-in living room, the room soft and out of focus behind, daylight from a window to one side, the forearm "
"coming in from the bottom corner of the frame. One hand holds it by the pad the way a real person holds a "
"strap: a relaxed natural pinch at the shell's bottom edge, the thumb in front resting on the bottom edge just "
"below the wordmark, the four fingers behind the shell on its inner pad with their tips hidden behind it, the "
"wrist loose and turned slightly toward the lens. Nothing rises above the shell's top edge: both peaks and the "
"notch stand completely clear against the room. Never on the band, never on the chrome slides, nothing across "
"the wordmark. The shell's front face is toward the lens, the wordmark horizontal and readable, both chrome "
"slides catching hard specular highlights. Because the hand is inside the ring, the closed band falls loosely "
"down behind the hand and hangs slack around the wrist under its own weight, the way a real strap does, its "
"tail visible. Real unretouched skin on "
"the hand of an adult of about sixty: visible pores and fine lines across the knuckles, faint veins on the "
"back of the hand, short clean nails.")

# T2I geometry guard for the set (HOLD_PROD is written for I2V).
PRODUCT_SET_GEOM = (
"The shell is rigid and keeps the exact geometry of the product photos: same silhouette, same two matching "
"peaks of equal height, same notch depth and width, same band width, same slide and wordmark positions, the "
"wordmark spelled stryde, never bent, flexed or stretched from any angle.")

# Generated product set, V7.49.18. Agent verdicts per §22V; awaiting the
# user's lock. Model passed nano_banana_pro, logged nano_banana_2 (routing fault).
PRODUCT_SET_STATUS = ("V7.49.23: the images in REFS_USE are LOCKED by the user; product_front, "
                      "product_back and product_profile retired; the held example is not locked")
PRODUCT_SET_REFS = {
    "tq_left":  {"file": "stryde_refs/product_tq_left.jpg", "job_id": "0cdf393f-6525-4f0e-a52b-728fda2410dd",
                 "attempt": "1 of 1", "flags": ""},
    "tq_right": {"file": "stryde_refs/product_tq_right.jpg", "job_id": "1794fcb5-9307-4d17-9138-a73481604fd2",
                 "attempt": ("3 of 3 -- a783c579 and 9e92a908 REGENERATE Q2 (V notch, crown peaks, face-mounted "
                             "slide); 3 = tq_left mirrored (media 182f9710) and re-rendered with the wordmark "
                             "reading correctly"),
                 "flags": "wordmark reads slightly left of the notch at this yaw"},
    "profile":  {"file": "stryde_refs/retired/product_profile.jpg", "job_id": "0b58a185-987e-4f71-97f6-0493ce15f17e",
                 "attempt": ("3 of 3 -- 3e404d2e and fcb96952 REGENERATE Q2 (slot notch / slab shell, "
                             "face-mounted slide); 3 = tq_left turned to about seventy degrees"),
                 "flags": "near peak reads low from the side"},
    "macro":    {"file": "stryde_refs/product_macro.jpg", "job_id": "8a9b0c5d-d3d7-496a-a557-0437c94c9579",
                 "attempt": "2 of 3 -- 42629d4f REGENERATE Q2 (invented moulded frame, sideways chevrons)",
                 "flags": "strap tilted on the diagonal"},
    "held":     {"file": "stryde_refs/product_held.jpg", "job_id": "c8339084-5ec3-4884-a558-e92681654e64",
                 "attempt": ("V7.49.20 realistic pinch, 2 of 3 -- 1f6ebf58 REGENERATE (fingers over the top "
                             "edge hiding the notch and peaks). Superseded: 972e16d9 (flat palm, not a real "
                             "hold), 930e3245 (grip not on the pad), 86093b25 (flat rectangular shell)"),
                 "flags": "one fingertip shows through the notch from behind the shell"},
    "front_view": {"file": "stryde_refs/retired/product_front.jpg", "job_id": "81f0fb23-9472-414d-bdc8-79926db9b2af",
                   "attempt": ("3 of 3 (V7.49.22) -- eb1e16e1 failed --check (rise 0.272, span 0.442, peaks 12% "
                               "unequal); 314cab43 camera above the product (ring top visible); 3 = re-render of "
                               "front.webp at level camera height. --check: all shape gates pass, peaks 2%"),
                   "flags": "band reads 0.387 on --check (front.webp 0.351): ~10% thicker, inside SIZE_LOCK tolerance"},
    "back_view":  {"file": "stryde_refs/retired/product_back.jpg", "job_id": "7921dfdf-9bda-4599-a861-9234a30b961f",
                   "attempt": "1 of 1", "flags": ""},
    "side_view":  {"file": "stryde_refs/product_side.jpg", "job_id": "a18b4a42-a306-41d8-8d09-2306c85393fb",
                   "attempt": ("3 of 3 -- 18c09090 REGENERATE Q2 (slide on the band face, shell reduced); "
                               "64d17655 REGENERATE Q2 (object tipped, band leaving the shell's bottom edge); "
                               "3 = anchored on front_view + back_view, camera moved round an invisible "
                               "upright leg"),
                   "flags": ""},
}
# --- which images to attach (V7.49.23, user) --------------------------------
# The whole answer to "which product images do I use". Paths are relative to
# this file. LOCKED by the user V7.49.23, except the held example, which is
# deliberately NOT locked: there are many right ways to hold it (HELD_GRIPS).
REFS_USE = {
    "base":     ("stryde_refs/front.webp", "stryde_refs/back.webp"),   # every product-facing call
    "tq_left":  ("stryde_refs/product_tq_left.jpg",),
    "tq_right": ("stryde_refs/product_tq_right.jpg",),
    "side":     ("stryde_refs/product_side.jpg",),
    "macro":    ("stryde_refs/product_macro.jpg",),
    "worn_front": ("stryde_refs/worn_front.jpg",),
    "worn_bent":  ("stryde_refs/worn_bent.jpg",),
    "worn_rear":  ("stryde_refs/worn_rear.jpg",),
    "package_closed": ("stryde_refs/package_closed.jpg",),   # V7.49.27, locked
    "package_open":   ("stryde_refs/package_open.jpg",),
}
REFS_USE_STATUS = "LOCKED V7.49.23 by the user"
HELD_EXAMPLE = "stryde_refs/product_held.jpg"   # an example of grip 1 only -- never locked, optional
REFS_RETIRED = (
    "stryde_refs/retired/product_front.jpg -- duplicate of front.webp; the original wins",
    "stryde_refs/retired/product_back.jpg -- duplicate of back.webp",
    "stryde_refs/retired/product_profile.jpg -- replaced by product_side + the three-quarter pair",
    "stryde_refs/retired/three_quarter_b.jpg -- replaced by the three-quarter pair",
    "stryde_refs/retired/three_quarter_a.jpg -- wordmark on the wrong side of the notch",
)
_SHOT_EXTRA = {
    "front": (), "back": (), "tq_left": ("tq_left",), "tq_right": ("tq_right",),
    "side": ("side",), "macro": ("macro",), "held": (),
    "worn_front": ("worn_front",), "worn_bent": ("worn_bent",), "worn_rear": ("worn_rear",),
    "seating": ("worn_front",),
    "package_closed": ("package_closed",), "package_open": ("package_open",),
}


def refs_for(shot):
    """The files to attach for one shot type: the two originals plus at most one extra."""
    if shot not in _SHOT_EXTRA:
        raise ValueError("unknown shot type %r; one of %s" % (shot, sorted(_SHOT_EXTRA)))
    out = list(REFS_USE["base"])
    for k in _SHOT_EXTRA[shot]:
        out += REFS_USE[k]
    return tuple(out)


# Retired V7.49.18: three_quarter_a.jpg -- its wordmark contradicts front.webp.
# Replaced by PRODUCT_SET_REFS['tq_left'] / ['tq_right'].

# Re-roll anchor (V7.49.18): the first product-set pass drew invented shells on
# every view except tq_left (0cdf393f, USE). Every re-roll attaches that frame
# FIRST and opens with this sentence.
PRODUCT_SET_ANCHOR_JOB = "0cdf393f-6525-4f0e-a52b-728fda2410dd"
PRODUCT_SET_ANCHOR = (
"The strap is the exact same object as the first attached image -- the same broad low shell with two matching "
"peaks and a rounded notch between them, the same slim brushed chrome slides inset into the shell's two ends, "
"the same wordmark, the same black coarse-knit band -- and only the view changes. Nothing about the object is "
"redesigned.")

PRODUCT_SET_ATTACH = {
    "tq_left":  ("front.webp", "back.webp", "three_quarter_b.jpg"),
    "tq_right": ("front.webp", "back.webp", "three_quarter_b.jpg"),
    "profile":  ("front.webp", "back.webp", "three_quarter_b.jpg"),
    "held":     ("front.webp", "back.webp"),
    "front_view": ("front.webp", "back.webp"),
    "back_view":  ("back.webp", "front.webp"),
    "side_view":  ("front.webp", "back.webp"),
    "macro":    ("front.webp", "back.webp"),
}


def product_set_prompts(anchor=False):
    """The five product-set T2I prompts (V7.49.18). Nano Banana Pro, 9:16, 2k.
    anchor=True: re-roll form -- PRODUCT_SET_ANCHOR first, attach PRODUCT_SET_ANCHOR_JOB first."""
    lead = REF_PROD.replace("the attached reference image", "the attached product photos")
    if anchor:
        lead = PRODUCT_SET_ANCHOR + " " + lead
    out = {}
    for k, view in PRODUCT_SET_VIEWS.items():
        out[k] = " ".join((PRODUCT_SET_STUDIO, lead + " a single unit.", PRODUCT_SET_RING, view, PRODUCT_SET_GEOM,
                           SIZE_OBJECT))
    out["held"] = " ".join((PRODUCT_SET_HELD, lead + " a single unit.", PRODUCT_SET_RING.replace(
        "standing open as a round ring as if around an invisible leg", "hanging as a closed loop"),
        PRODUCT_SET_GEOM, SIZE_HELD, INNER_PAD, CAP_A, BODY_WHOLE))
    return out


def worn_ref_prompts(side="right"):
    """The three worn-placement reference T2I prompts (V7.49.15), built from
    the locked strings so nothing is retyped. Nano Banana Pro, 9:16, 2k."""
    lead = REF_PROD.replace("the attached reference image", "the attached product photos")
    worn = " worn on the %s leg of a real person, fitted exactly." % side
    body = {
        "front": fill(PLACE_LOCK, side=side),
        "rear":  fill(ORIENT_LOCK, side=side),
        "bent":  fill(PLACE_BENT, side=side) + " " + fill(PLACE_PROFILE, side=side),
    }
    out = {}
    for k, scene in WORN_REF_SCENES.items():
        extra = (WORN_REF_SHAPE,) if k == "bent" else ()
        out[k] = " ".join((scene, lead + worn, body[k]) + extra + (FIT_SNUG, SIZE_WORN, LEG_SKIN, CAP_A, BODY_WHOLE))
    return out


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
"and below it, its line following the leg (V7.49.15: the band's own edges stay straight, per the "
"supplied photos), the whole thing a few degrees off horizontal. Band height / leg width at the contact point is its own ratio "
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
# V7.49.15: all three frames are to be REPLACED by the worn_ref_prompts()
# frames (one size fits all, fitted exactly, supplied product photos as the
# object reference). The frames below stay attached until the new ones are
# accepted by the user; then swap file/job ids here and log it.
PLACEMENT_REFERENCES_STATUS = ("LOCKED V7.49.17 by the user -- front (f5263ed7), bent (8a8979ac, raised) and "
                               "rear (81992d6c, band narrowed V7.49.22 on user instruction; was a38bc276). "
                               "Layer 1 for placement. Replaced only on a user instruction.")
PLACEMENT_REFERENCES = {
    "front": {
        "file": "stryde_refs/worn_front.jpg",
        "job_id": "f5263ed7-0667-4ebd-977e-9bfd835d5036",
        "higgsfield_media": "use the job_id as the medias value",
        "model_passed": "nano_banana_pro", "model_logged": "nano_banana_2",   # routing fault, logged
        "attempt": "1 of 1",
        "reads": ("right knee, standing, straight-on; the notch cups the kneecap's lower border with the "
                  "flesh filling it, the peaks no higher than the base of the kneecap's sides, the kneecap "
                  "bare above; the shell spans the whole front of the joint with a chrome slide at each side "
                  "of the leg; wordmark centred beneath the notch; snug, one-size fit."),
    },
    "bent": {
        "file": "stryde_refs/worn_bent.jpg",
        "job_id": "8a8979ac-9eb1-4398-b41b-eea793a99a26",
        "higgsfield_media": "use the job_id as the medias value",
        "model_passed": "nano_banana_pro", "model_logged": "nano_banana_2",
        "attempt": ("3 of 3 -- attempt 1 (b0a3f260) REGENERATE Q2: too side-on, one peak, notch lost; "
                    "attempt 2 (970785f4) REGENERATE Q2: tall narrow U-shell, horn peaks, wrong type; "
                    "attempt 3 (d2d0124c) USE with flags; V7.49.16 user correction 'higher' -> "
                    "edit of d2d0124c (8a8979ac), strap raised only, USE"),
        "flags": ("near peak reads low at this yaw; band at the near slide reads smoother than the knit; "
                  "wordmark shifted toward the far peak by yaw"),
        "reads": ("right knee bent about a right angle, seated, three-quarter from the front right; the shell "
                  "sits HIGH -- top edge level with the kneecap's lower pole, the notch pressed up into its "
                  "underside, the far peak flanking the lower half of its side, the face bare above, the "
                  "lower body only just onto the top of the shin; broad low shell wrapping the leg, slim chrome slide with three dotted chevrons "
                  "at the near margin, band running back round the calf. Attached on every bent-knee worn beat."),
    },
    "rear": {
        "file": "stryde_refs/worn_rear.jpg",
        "job_id": "81992d6c-dbf2-406d-95eb-cf5a941d5ed9",
        "edit_of": ("a38bc276 (locked V7.49.17) -- V7.49.22 user-ordered band fix: band/leg 0.33 -> "
                    "about 0.27, everything else unchanged"),
        "higgsfield_media": "use the job_id as the medias value",
        "model_passed": "nano_banana_pro", "model_logged": "nano_banana_2",
        "attempt": "1 of 1",
        "reads": ("right knee from behind, standing; the band crosses BELOW the hollow, across the top of the "
                  "calf, the knee's bulge bare above; two black keeper loops side by side at the centre rear "
                  "exactly as back.webp; straight band edges; a chrome slide as a bright bar at each side; "
                  "no shell, wordmark or fastening at the rear; band about a quarter of the leg's width "
                  "(0.27, V7.49.22)."),
    },
}

# The V7.49.8-13 worn frames, retired V7.49.15. Never attached again.
RETIRED_PLACEMENT_REFERENCES = (
    "hf_20260819_134414_dab787bf (worn_front_ref.png)",
    "hf_20260915_182228_5e75f3c8 (worn_bent.png)",
    "hf_20260922_120414_6e07d1c8 (rear, accepted V7.49.13)",
    "hf_20260819_134410_6a573801 (worn_back_ref.png, retired V7.49.13)",
)

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
     "(V7.49.10). Width-to-height settled V7.49.21 (ASPECT_RATIO, SIZE_LOCK)."),
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
    # V7.49.23
    "NEG-HELD-P": NEG_HELD_P, "NEG-OBSERVED": NEG_OBSERVED,
    "FAKE-BASE": FAKE_BASE, "NEG-FAKE-HERO": NEG_FAKE_HERO, "PAD-BACK-SHOT": PAD_BACK_SHOT,
    "PACKAGE-LOCK": PACKAGE_LOCK, "NEG-PACKAGE": NEG_PACKAGE,
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
    # V7.49.21: target (0.20, 0.28) = SIZE_LOCK['worn_band_over_leg'] (2.5 cm band on a
    # 10-11 cm calf). The old 0.28-0.36 came off an upscaled V7.48 frame and
    # rendered the band ~3.5 cm (worn_rear.jpg reads 0.33 -- flagged, locked by user).
    "BAND_HEIGHT_TO_LIMB_WIDTH": (0.20, 0.28),
    # V7.49.12. Shell width (slide to slide) / greatest height, read off the
    # supplied straight-on front.png: height measured (565 px of 2048), width
    # by eye at the slides' outer edges. Informational, never gated.
    "SHELL_ASPECT_EST": (2.3, 2.6),
}

# Shell width-to-height, SETTLED V7.49.21: measured on two straight-on,
# no-yaw frames -- front.webp (layer 1) 2.50 and product_front.jpg 2.32. The
# 1.23-1.72 read off the V7.48 three-quarter renders was yaw, as predicted.
ASPECT_RATIO = (2.3, 2.6)

RULINGS = {
    "seating_joint_state":
        "LOCKED V7.49.8. Seating (putting-on) beats run on a STRAIGHT leg, the ring "
        "starting at mid-shin and seating on the patellar tendon. The bent-knee state "
        "is a WORN beat only (PLACEMENT_REFERENCES['bent']); a bent-knee seating beat "
        "was tested and dropped. Placement wording is per joint state: straight -- peaks "
        "no higher than the base of the kneecap's sides; bent -- peaks flanking the lower "
        "half of its sides, up to but never past its middle (V7.49.16).",
    "bent_height":
        "LOCKED V7.49.16 (user: 'the bent one should be higher'). On a bent knee the shell sits "
        "HIGH: top edge level with the kneecap's lower pole, notch pressed up into its underside, "
        "the lower body only just onto the top of the shin. Applies to every bent-knee worn "
        "beat (PLACE_BENT, NEG_BENT) and to PLACEMENT_REFERENCES['bent'].",
    "size_lock":
        "LOCKED V7.49.21 (user: always the same size). SIZE_LOCK is the product's one size. Every "
        "worn prompt carries SIZE_WORN, every product-only prompt SIZE_OBJECT, every held prompt "
        "SIZE_HELD. A frame whose shell or band reads more than ~20 percent off its anchor is "
        "REGENERATE Q2.",
    "side_from_script":
        "LOCKED V7.49.24 (user): the knee that wears the strap comes from the script (SIDE_RULE, "
        "side_from_script). No knee named -> right. Left needs left-knee worn references first; a "
        "right-knee frame is never mirrored.",
    "package_always_two":
        "LOCKED V7.49.24 (user): our own box -- matte black, the stryde wordmark on the lid, nothing "
        "else printed -- and ALWAYS two straps inside, because the offer is always Buy 1 Get 1 Free. "
        "PACKAGE, PACKAGE_LOCK, NEG_PACKAGE.",
    "band_is_soft":
        "LOCKED V7.49.26 (user: 'they are not rock solid'). The band is soft elastic. Off the leg and "
        "not held up, the strap lies flat -- in the box, on a surface -- the band relaxed in a "
        "flattened loop. Only the studio product views (after the supplied photos) show the ring "
        "standing open.",
    "fake_cheap_and_damaged":
        "LOCKED V7.49.28 (user): the cheap copy looks like STRYDE at a glance but cheap and easily "
        "damaged -- FAKE_BASE on every copy (thin shiny plastic, scuffs, a crack, frayed thin nylon, "
        "plastic buckles, no wordmark), plus one FAKE_ARCHETYPES entry per build, never reused.",
    "pad_line_shows_back":
        "LOCKED V7.49.28 (user): a line about the pad inside ('Inside, a silicone pad...') is covered "
        "by the BACK of the shell turned to the lens (PAD_BACK_SHOT), then the mechanism.",
    "claims_confirmed":
        "V7.49.29 (user): every claim in the Identity Callout script is confirmed and advertiser-held -- "
        "17x bodyweight, three years with orthopaedic surgeons, the silicone pad, 34% less strain, "
        "bone on bone / arthritis / cartilage / meniscus, recommended by surgeons, 200,000 wearers, "
        "sixty-day money-back guarantee, Buy 1 Get 1 Free. Numbers and terms are still post overlays "
        "(§17); 'silicone' still never enters a prompt.",
    "anatomy_look":
        "LOCKED V7.49.31 (user): ANAT-A full stack for the point and protection beats, ANAT-B ghost "
        "limb for the condition beats. Every ANAT-A beat adds ANAT_A_POINT_TIGHT.",
    "held_not_locked":
        "LOCKED V7.49.23 (user): the held pose is NOT locked -- there are many right ways to hold it. "
        "Pick from HELD_GRIPS per beat and vary them across a build; product_held.jpg is one example "
        "(grip 1), optional, never required. The fixed rules are HELD_RULES.",
    "held_on_pad":
        "LOCKED V7.49.19, made realistic V7.49.20 (user). Whenever the product is held, the grip is "
        "on the pad, the way a person really holds a strap: a relaxed pinch at the bottom edge -- "
        "thumb in front on the edge below the wordmark, four fingers behind on the inner pad with "
        "their tips hidden, wrist loose. Nothing above the shell's top edge (peaks and notch clear). "
        "The hand is inside the ring, so the band falls slack around the wrist -- physically right, "
        "never prompted away. Never a flat "
        "palm, never by the band, never by the slides, never across the wordmark. Prompts say 'the pad' / 'inner pad', "
        "never 'silicone' (UNSETTLED['inner_face_script'] -- advertiser-stated, and the word renders "
        "the soft glossy fake).",
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
    "inner_face_script_RESOLVED_7_49_23":
        "RESOLVED V7.49.23 for rendering by back.webp: the inside of the shell is a plain, smooth, "
        "matte-black pad with no markings (INNER_PAD). The user calls it the silicone pad; the "
        "material stays advertiser-stated (Six Weeks Ago script), so prompts say 'the pad' and never "
        "'silicone'. Was: OPEN V7.49.12, unphotographed.",
    "band_faces_RESOLVED_7_49_11":
        "RESOLVED by the supplied product images (CANONICAL_REFERENCES). The OUTER "
        "face carries TWO black moulded keeper loops side by side at the rear; the "
        "band is a coarse knit with a visible textured weave and STRAIGHT edges. "
        "The V7.49.8 plain-face / scalloped-edge reading, taken off a worn "
        "generation, is retired -- a worn frame is a placement reference, never a "
        "product-geometry source. The inner face remains undescribed.",
    "band_keepers":
        "RESOLVED V7.49.15 by PRODUCT_PHOTOS['back.webp']: two black moulded keeper loops side by "
        "side at the centre rear of the band's outer face. Was: SETTLED FOR RENDERING, OPEN AS A FACT. Small black moulded keeper "
        "loops sit on the band, consistent across 63, 64, 68 and every "
        "V7.48.2 reference panel. They are a secondary component the "
        "eight-field spec did not carry, and they now render on every "
        "object beat. UNBLOCKED AS A FACT BY: a photograph of the band.",
    "band_weave":
        "RESOLVED V7.49.15 by PRODUCT_PHOTOS: a coarse knit with a visible textured weave and "
        "straight edges (BAND_MATERIAL). History follows. Was: SETTLED FOR RENDERING, OPEN AS A FACT. At V7.48.1 the native-"
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
        "RETIRED V7.49.15: the photos show the keeper loops on the OUTER face and a plain inner "
        "face. Nothing is ever written about inner-face lugs. History follows. The outer-face keeper loops are neither confirmed nor killed by the "
        "V7.48 rear reference. The band's lower edge does undulate against "
        "the calf, but plain compression explains that equally, and the lugs "
        "sit against the skin where the camera cannot see them. They stay as "
        "written and stay unverified. RESOLVED AS A FACT BY: a close still of the "
        "band's inner face, or a rear beat generated with and without the "
        "inner-face clause.",
    "shell_elevation_aspect_RESOLVED_7_49_21":
        "RESOLVED V7.49.21: 2.3-2.6 measured on front.webp (2.50) and product_front.jpg (2.32), "
        "both straight-on -- ASPECT_RATIO, SIZE_LOCK. History: True shell width-to-height is unknown. Every canonical render is "
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
# V7.49.23: RETIRED. STRYDE_reference_v7_49_11.png was never stored in the repo, so
# nothing may name it. Its job is done by front.webp + back.webp (REFS_USE).

# --- the supplied product photos, stored in the repo (V7.49.15) ----------
# Layer 1 (Order of Authority). Stored beside this sheet so every session
# has them. Read by eye V7.49.15.
PRODUCT_PHOTOS_DIR = "stryde_refs"   # three_quarter_a/_b moved to stryde_refs/retired/ V7.49.23
PRODUCT_PHOTOS = {
    "front.webp": ("straight-on front elevation: two matching peaks, notch centred, grey lowercase "
                   "stryde wordmark centred beneath the notch, chrome slide inset at each end with three "
                   "engraved dotted chevrons, coarse-knit band with straight edges each side"),
    "back.webp": ("rear view: the band doubled through the slides and running round the back, two "
                  "black moulded keeper loops side by side at the centre of the band's outer face, the "
                  "shell's inner face plain matte black, the peaks rising behind"),
    "three_quarter_a.jpg": "three-quarter, floating: wordmark reads left of the notch in this view (yaw)",
    "three_quarter_b.jpg": "three-quarter, floating: the wrap reads, slide and band tail at the near end",
}

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
    "any file in REFS_RETIRED (V7.49.23)",
    "STRYDE_reference_v7_49_11.png -- never stored in the repo; retired V7.49.23",
    "stryde_refs/retired/three_quarter_a.jpg -- wordmark on the wrong side of the notch against front.webp; retired V7.49.18",
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
    "the band's outer face carries two moulded keeper loops side by side at "
    "the centre rear, visible on rear and turning beats",
    "one size fits all: band snug and flat all the way round, tail folded "
    "back flat through each slide, no slack, shell scaled to the knee",
    "rear and turning beats: only the woven band crosses the back of the "
    "knee, and no fastening is visible there",
    "rear beats: the band sits BELOW the hollow, across the top of the calf, "
    "with the knee's own bulge bare above it -- never in the hollow",
    "rear beats: the band presses in, flesh swelling above and below it, its "
    "line following the leg's curve while its own edges stay straight",
    "rear beats: a chrome slide reads as a bright bar standing proud of the "
    "leg silhouette at each outer edge",
    "bent-knee beats: the kneecap's flesh presses INTO the notch curve and "
    "fills it -- no gap between kneecap and notch",
    "bent-knee beats: the shell sits HIGH -- top edge level with the kneecap's "
    "lower pole, only just onto the top of the shin -- and has not rotated with the joint",
    "side and three-quarter beats: the shell reads as a WRAPPED plate "
    "following the leg's curve, wordmark still horizontal and readable, "
    "never a flat panel on the front",
    "seating beats: the closed strap starts at mid-shin and moves UP the "
    "front of the shin only -- never down, never from above the kneecap",
    "seating beats: hands flat on the shell's sides, never on the band "
    "ends or the slides; nothing pulled, tightened or threaded",
    "seating beats: end position matches the front worn-placement reference",
    "size (SIZE_LOCK): shell about two and a half times as wide as tall; band about half "
    "the shell's height; worn -- shell spans the leg's front width and stands about as tall "
    "as the kneecap, band about a quarter of the calf's width; held -- shell five to six "
    "thumb-widths across",
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
     "a phrasing this sheet retires. RESOLVED V7.49.11/V7.49.15: the "
     "supplied front photo centres it beneath the notch, and every string "
     "now says so. See OVERRIDES."),
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
    ps = product_set_prompts()
    if set(ps) != set(PRODUCT_SET_ATTACH):
        fails.append("product set prompts and attachments disagree")
    for k, v in ps.items():
        if "[" in v:
            fails.append("product set %s left a slot unfilled" % k)
        for bad in RETIRED_PHRASINGS:
            if bad in v.lower() and bad not in NEG_ONLY:
                fails.append("product set %s carries retired phrasing: %r" % (k, bad))
        for f in PRODUCT_SET_ATTACH[k]:
            if f not in PRODUCT_PHOTOS:
                fails.append("product set %s attaches an unregistered photo: %s" % (k, f))
    if "holds it by the pad" not in PRODUCT_SET_HELD or "never on the band" not in PRODUCT_SET_HELD.lower() \
            or "natural pinch" not in PRODUCT_SET_HELD or "Nothing rises above the shell's top edge" not in PRODUCT_SET_HELD:
        fails.append("held frame lost the V7.49.19 grip-on-the-pad rule")
    if "silicone" in PRODUCT_SET_HELD.lower():
        fails.append("held prompt names silicone -- renders the shell as the soft fake")
    if "One hand" not in PRODUCT_SET_HELD:
        fails.append("held frame lost the §9A grip rules")
    for k, v in PRODUCT_SET_REFS.items():
        if k not in PRODUCT_SET_ATTACH or not v.get("job_id"):
            fails.append("product set ref %s unregistered" % k)
    if any("three_quarter_a.jpg" in files for files in PRODUCT_SET_ATTACH.values()):
        fails.append("retired three_quarter_a.jpg is still attached")
    if not PLACEMENT_REFERENCES_STATUS.startswith("LOCKED"):
        fails.append("worn placement references are not locked")
    if [PLACEMENT_REFERENCES[k]["job_id"][:8] for k in ("front", "bent", "rear")] != \
            ["f5263ed7", "8a8979ac", "81992d6c"]:
        fails.append("a locked worn reference was swapped without a user instruction")
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
    if not all(k in PRODUCT_PHOTOS or k in PLACEMENT_REFERENCES for k in SEAT_REFERENCES):
        fails.append("SEAT_REFERENCES names an unregistered reference")

    # 8c one size fits all; worn-reference prompts build and stay positive (V7.49.15)
    for frag in ("One size fits all", "snug and flat", "scaled to this knee"):
        if frag not in FIT_SNUG:
            fails.append("FIT_SNUG missing: %s" % frag)
    wr = worn_ref_prompts("right")
    if set(wr) != {"front", "rear", "bent"} or set(WORN_REF_ATTACH) != set(wr):
        fails.append("worn reference prompts must be exactly front, rear, bent, each with attachments")
    for k, v in wr.items():
        if "[" in v:
            fails.append("worn ref %s left a slot unfilled" % k)
        for bad in RETIRED_PHRASINGS:
            if bad in v.lower() and bad not in NEG_ONLY:
                fails.append("worn ref %s carries retired phrasing: %r" % (k, bad))
    for k, files in WORN_REF_ATTACH.items():
        for f in files:
            if f not in PRODUCT_PHOTOS:
                fails.append("worn ref %s attaches an unregistered photo: %s" % (k, f))
    for name in ("PLACE-LOCK", "ORIENT-C", "REF-PROD"):
        if "webbing" in S[name] or "flat matte-black black" in S[name]:
            fails.append("%s still describes the band as flat webbing" % name)

    # 8d size lock and wear guide (V7.49.21)
    if ASPECT_RATIO != SIZE_LOCK["shell_aspect"]:
        fails.append("ASPECT_RATIO and SIZE_LOCK disagree")
    if INFO_RATIOS["BAND_HEIGHT_TO_LIMB_WIDTH"] != SIZE_LOCK["worn_band_over_leg"]:
        fails.append("INFO_RATIOS band/limb and SIZE_LOCK disagree")
    for k, v in worn_ref_prompts("right").items():
        if SIZE_WORN not in v:
            fails.append("worn ref %s missing SIZE_WORN" % k)
    for k, v in product_set_prompts().items():
        want = SIZE_HELD if k == "held" else SIZE_OBJECT
        if want not in v:
            fails.append("product set %s missing its size string" % k)
    heads = [h for h, _ in WEAR_GUIDE]
    for must in ("ONE UNIT, ONE KNEE", "SHELL ON THE FRONT, NOTCH UP", "HEIGHT -- ON THE PATELLAR TENDON",
                 "BAND ROUND THE BACK, BELOW THE HOLLOW", "FIT -- ONE SIZE, SNUG", "PUTTING IT ON"):
        if must not in heads:
            fails.append("WEAR_GUIDE missing: %s" % must)
    for name in ("SIZE_OBJECT", "SIZE_WORN", "SIZE_HELD"):
        v = globals()[name]
        if "never changes" not in v:
            fails.append("%s lost its fixed-size clause" % name)
        for bad in RETIRED_PHRASINGS:
            if bad in v.lower() and bad not in NEG_ONLY:
                fails.append("%s carries retired phrasing: %r" % (name, bad))

    # 8e image use map, held grips, observed negatives (V7.49.23)
    here = os.path.dirname(os.path.abspath(__file__))
    for k, files in REFS_USE.items():
        for f in files:
            if not os.path.exists(os.path.join(here, f)):
                fails.append("REFS_USE[%s] names a file that is not in the repo: %s" % (k, f))
    if ANATOMY_LOOK.get("point") != "ANAT-A" or ANATOMY_LOOK.get("conditions") != "ANAT-B":
        fails.append("ANATOMY_LOOK lost the user's choice (A point/protection, B conditions)")
    for k, v in ANATOMY_SAMPLES.items():
        if not os.path.exists(os.path.join(here, v["file"])):
            fails.append("anatomy sample %s missing" % k)
    if not os.path.exists(os.path.join(here, HELD_EXAMPLE)):
        fails.append("HELD_EXAMPLE missing")
    used = {f for files in REFS_USE.values() for f in files}
    for r in REFS_RETIRED:
        if r.split(" -- ")[0] in used:
            fails.append("a retired image is still in REFS_USE: %s" % r)
    for shot in _SHOT_EXTRA:
        if len(refs_for(shot)) > 3:
            fails.append("refs_for(%s) attaches more than the two originals plus one" % shot)
    if HELD_EXAMPLE in used:
        fails.append("the held example must not be in the locked set")
    if len(HELD_GRIPS) < 3:
        fails.append("HELD_GRIPS must offer several grips")
    for name, how in HELD_GRIPS:
        low = how.lower()
        if "band" in low and ("gripping the band" in low or "by the band" in low):
            fails.append("held grip %s holds the band" % name)
        if "silicone" in low:
            fails.append("held grip %s names silicone" % name)
    for clause in ("no hand gripping the band", "no fingers on the chrome slides", "no fingers across the wordmark"):
        if clause not in NEG_HELD_P:
            fails.append("NEG_HELD_P missing: %s" % clause)
    if len(NEG_OBSERVED_LOG) < 9 or "no V-shaped notch" not in NEG_OBSERVED:
        fails.append("NEG_OBSERVED lost its logged failures")
    if "silicone" in INNER_PAD.lower():
        fails.append("INNER_PAD names silicone")
    if "composite" in SEAT_REFERENCES:
        fails.append("SEAT_REFERENCES names the missing composite")

    # 8f side from the script; the box always holds two (V7.49.24)
    for txt, want in (("my left knee has been killing me", "left"), ("the right knee on the stairs", "right"),
                      ("my knee hurts on the stairs", "right")):
        if side_from_script(txt)[0] != want:
            fails.append("side_from_script(%r) != %s" % (txt, want))
    if "FLAG" not in side_from_script("left knee and right knee")[1]:
        fails.append("side_from_script does not flag a script naming both knees")
    if "lying FLAT" not in PACKAGE_LOCK or "soft elastic" not in PACKAGE_LOCK:
        fails.append("PACKAGE lost the lying-flat rule (V7.49.26)")
    if "ONE piece" not in PACKAGE_LOCK or "no shell separate from its band" not in NEG_PACKAGE:
        fails.append("PACKAGE lost the one-piece rule (V7.49.25)")
    if "exactly two" not in PACKAGE_LOCK or "two" not in PACKAGE["contents"]:
        fails.append("PACKAGE_LOCK lost the always-two rule")
    if "Buy 1 Get 1 Free" in PACKAGE_LOCK or "Buy 1 Get 1 Free" in "".join(package_prompts().values()):
        fails.append("offer text must never be generated on the box (§17)")
    if not PACKAGE_REFS_STATUS.startswith("LOCKED") or \
            [PACKAGE_REFS[k]["job_id"][:8] for k in ("closed", "open")] != ["e8c4df4b", "a9409405"]:
        fails.append("the locked box references were changed without a user instruction")
    for k, v in PACKAGE_REFS.items():
        if v["file"] and not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), v["file"])):
            fails.append("package ref %s file missing" % k)
    if "matte black" not in PACKAGE_LOCK or "stryde wordmark" not in PACKAGE_LOCK:
        fails.append("PACKAGE_LOCK lost the black box or the logo")
    for k, v in package_prompts().items():
        if "[" in v:
            fails.append("package prompt %s left a slot unfilled" % k)

    # 8g the cheap copy and the pad-back shot (V7.49.28)
    for frag in ("no wordmark", "scuffed", "frayed", "plastic buckles", "crack"):
        if frag not in FAKE_BASE:
            fails.append("FAKE_BASE missing: %s" % frag)
    if "chrome" in FAKE_BASE.split("instead of")[0].split("fastenings")[-1]:
        fails.append("FAKE_BASE gives the copy chrome")
    if not any(n == "too small" for n, _ in FAKE_ARCHETYPES):
        fails.append("FAKE_ARCHETYPES lost the undersized copy the script needs")
    if "back of the shell" not in PAD_BACK_SHOT or "silicone" in PAD_BACK_SHOT.lower():
        fails.append("PAD_BACK_SHOT must show the back and never say silicone")
    for clause in ("no damage on the hero strap", "no wordmark on the copy"):
        if clause not in NEG_FAKE_HERO:
            fails.append("NEG_FAKE_HERO missing: %s" % clause)

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

**V7.49.23.** This is the prose half of `stryde_product_sheet.py`, embedded in it and emitted with `--md`. It carries the spec, the phrasing table, the claim register and the reference registry; the module around it carries the slots, the locked strings, the measured ratios and the assertions. **Never retype a string into a prompt — import it.**

The geometry ratios were measured off the five V7.48 canonical renders (63, 64, 65, 66, 68) with a roll correction applied. **Since V7.49.11 the supplied product photos (`stryde_refs/`) are the product** (layer 1) and outrank those renders wherever they disagree. Where a figure is external it is marked Tier 3 and is not advertiser-held.

---

## 1. Product name and category

Stryde Precision Strap — a patellar tendon strap. A rigid moulded anterior shell on a closed elastic knit band, **one size fits all**, worn on one knee, sitting under the kneecap and over the upper patellar tendon.

**Market note.** Multiple marketplace sellers list a "Stryde Precision Strap" built around a soft silicone lock-point pad. Our hero is rigid matte polymer with brushed chrome hardware, which is the opposite construction. Two consequences: the cheap-silicone villain archetype (§10) is the literal market reality and the anti-knock-off angle is stronger than it looked; and the name question is the advertiser's counsel's, not this sheet's.

---

## 2. The eight spec fields (§8)

**1 — Primary form.** A rigid moulded polymer shell spanning the whole front of the knee from one side of the leg to the other, its top edge waving up into two matching pointed peaks of equal height either side of a crisp concave notch, waisted off-centre, closed behind the leg by a flat matte-black woven elastic band.

**2 — Material and finish.** Shell: matte polymer, satin not gloss, holding a soft broad highlight along the crown of each peak and down the waist. Band: black elastic band in a coarse knit with a visible textured weave and straight edges (supplied photos). Hardware: brushed chrome slides carrying three engraved dotted chevrons, the only specular element on the object. Keeper loops: moulded matte black, on the band's outer face.

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

**5 — Secondary components.** Band: black coarse-knit elastic, threading through each slide and folding back on itself, so the fold-back sits at the sides of the leg and never at the rear. The band is never shown being adjusted (§12 below). **Keeper loops — outer face:** two black moulded rounded rectangles side by side at the centre rear of the band, a little narrower than the band, standing proud of the knit. The inner face is plain and never described. Hardware: brushed chrome rectangular slides inset flush into each shell end, carrying three engraved dotted chevrons — captured by the shell, not floating on the band.

**6 — Interface mechanism.** Band threads through the chrome slides and folds back. There is no visible velcro tab, buckle or fastening in any canonical render, and none at the rear in any beat.

**7 — Placement lock.** `[SITE]` is the patellar tendon immediately below the patella; `[LANDMARK]` is the kneecap. Height is set by **contact** — the kneecap's lower pole seats into the concave notch, its flesh filling the curve, no gap anywhere between skin and shell — never by a measured offset. Coverage is guarded separately: the kneecap's face stays completely uncovered, its outline reading in full. Side is declared at the act map and held; the product is **not handed**. Strings: `PLACE-LOCK`, `PLACE-LOCK-C`, `ORIENT-LOCK`, `ORIENT-C`, `SEAT-LOCK`, `NEG-PLACE`, `NEG-ORIENT`, `NEG-SEAT`.

**8 — Standing negatives.** `NEG-PLACE` and `NEG-ORIENT` in the `.py`, accumulated from observed failures. Clauses added at V7.47: `no undersized shell`, `no peaks filling the whole width of the shell`, `no band without its two keeper loops` (outer face — the V7.47 "inner face" wording is retired).

---

## 3. Phrasing table

| Intent | Phrasing that failed, and what it produced | Phrasing that works |
|---|---|---|
| Set the height | "2 cm below the kneecap" / "one to two fingers below" | The kneecap's lower pole seats deep into the notch, its flesh filling the curve, no gap between skin and shell |
| Keep the kneecap clear | "a clear gap of bare skin between the kneecap and the strap" — rendered the strap low on the shin and visibly disengaged from what it acts on | The kneecap's face stays completely uncovered above the strap, its outline reading in full |
| Set the shell's size | "spans the full width of the kneecap and slightly beyond" — rendered a small pad, and contradicted the same string's chrome-slides-at-the-outer-edges clause | The notch and peaks are one kneecap wide and occupy the middle three fifths; beyond each peak the shell continues out to a chrome slide at each outer margin of the leg |
| Describe the rear | "a plain knit strip, unbroken and featureless" — rendered a plain band with no keepers | A coarse-knit band with straight edges, two black moulded keeper loops side by side at the centre rear of its outer face |
| Place the wordmark | "offset to one side of the notch" — contradicted by the supplied front photo (V7.49.11) | Horizontal and readable on the broad lower body, centred directly beneath the notch |
| Show that it fits | "adjustable" — renders the act of adjusting (V7.49.14) | The seating move up the shin, then the product itself (§12); on a worn frame, `FIT_SNUG` |
| Any new angle of the product | Describing the view from scratch — the model redesigns the object: V notch, crown peaks, slide on the face (V7.49.18) | Attach a frame that already reads right FIRST and open with "the exact same object as the first attached image … only the view changes" (`PRODUCT_SET_ANCHOR`) |
| Opposite three-quarter | "Seen from the front right" — failed twice | Mirror the good left view and ask for a re-render with the wordmark reading correctly (V7.49.18) |
| True side view | "Exactly from the side, edge-on" — tipped the object, band out of the bottom edge (V7.49.19) | Anchor on the front and back views; "the camera moves round to the outside of an invisible upright leg; the band stays horizontal" |
| Straight front | "Straight-on" alone — camera drifted above, ring top showing, notch read deep (V7.49.21) | "Camera level with the middle of the shell, not from above and not from below; the ring behind hidden" |
| Held | "Held from underneath" / "fingers flat behind" — flat stop-sign palm, then fingers over the top edge (V7.49.19–20) | Pick a grip from `HELD_GRIPS` and add "nothing rises above the shell's top edge"; the band falls slack round the wrist — never prompt it away |
| Same size every time | Adjectives ("broad", "the size of a hand") — band drifted 2–3.5 cm (V7.49.21) | `SIZE_OBJECT` / `SIZE_WORN` / `SIZE_HELD` — the size said against the body in each context |
| Layout from an earlier frame | Attaching a frame whose layout is right but whose product is wrong — the product flaw is copied too (package open, V7.49.26) | Attach ONLY frames whose product is correct; carry the layout in words |
| Change one thing on a good frame | A fresh generation — loses what was right | An edit: attach the frame first, "keep everything exactly the same and change one thing only" (bent height, rear band, V7.49.16/22) |
| Bound the scale | "no wider than X" — biased the object small | State what it spans positively; put the upper bound in the negatives |
| Stop the rear shell | `no shell at the back` alone — a generator does not classify a flat printed patch as a shell | State the rear positively and at length, then negate |

---

## 4. Reference image registry

**Which images to attach (V7.49.23, locked by the user) — `REFS_USE`, `refs_for(shot)`:**

| Shot | Attach |
|---|---|
| Every product-facing call | `front.webp` + `back.webp` (your originals) |
| Three-quarter | + `product_tq_left.jpg` or `product_tq_right.jpg`, matching the angle |
| Side | + `product_side.jpg` |
| Close-up of slide or band | + `product_macro.jpg` |
| Worn — straight, bent, rear | + `worn_front.jpg`, `worn_bent.jpg` or `worn_rear.jpg` |
| Putting it on | + `worn_front.jpg` (the end position) |
| Box — closed / open | + `package_closed.jpg` or `package_open.jpg` (locked V7.49.27) |
| Held | the two originals only; `product_held.jpg` is an optional example of one grip, **not locked** — pick a grip from `HELD_GRIPS` |

Never more than the two originals plus one. **Retired:** `product_front.jpg`, `product_back.jpg`, `product_profile.jpg`, `three_quarter_a.jpg`, `three_quarter_b.jpg`, and the never-stored composite `STRYDE_reference_v7_49_11.png`. Image plus names is the pair; either alone leaks.

**Never attach as reference:** any image carrying baked-in headline type, any multi-instance shot, any marketplace listing image of a silicone-pad product sold under the same name.

**Per-batch first-frame check:** the `CHECKLIST` in the `.py` (the self-test prints its count). The measurable half runs as `stryde_product_sheet.py --check <frames>`. The rest stays an eyeball: matte finish, woven band, wordmark legibility, declared side, placement on the body, shell on the front, keeper loops on rear and turning beats.

---

## 5. Mechanism type and slots

Register: anatomical (§12A-1). Slots: `[REGION]` knee · `[STACK]` quadriceps, hamstrings and calf · `[BONES]` femur, patella and tibia · `[TARGET]` the patellar tendon · `[TARGET_JOINT]` the knee joint · `[SITE]` the patellar tendon immediately below the patella.

**`[SITE]` is not the anatomical insertion.** The tibial tuberosity is the textbook-obvious spot and it is the wrong one — the product acts above it. Name the tuberosity in the negatives on every modulation beat.

**Standards slots this product fills:** `[BAND-MATERIAL]` black elastic band in a coarse knit with a visible textured weave and straight edges · `[HARDWARE]` brushed chrome slides · `[BAND-INNER]` two black moulded keeper loops side by side on the band's outer face at the rear (the slot name is historical; the inner face is never described).

---

## 6. Mechanism claim

**Protection.** One per build. Load-path is retired for this product and stays in the library for a build pitched on the other claim.

---

## 7. Competitor archetypes (§10)

**V7.49.28 (user): the copy looks like STRYDE at a glance but cheap and easily damaged.** Every copy carries `FAKE-BASE` — thin shiny plastic shell, no wordmark, soft rounded peaks, scuffs and a crack, a thin frayed nylon band, cheap plastic buckles instead of chrome. On top, **one** archetype per build from `FAKE_ARCHETYPES` (too small · soft silicone · wide webbing · thick and proud · blue gel · breaking), never reused in that build. Always in a real home, never on white. The hero is never damaged (`NEG-FAKE-HERO`).

Degraded near-copies of the same silhouette, never different products. One signifier per archetype, never repeated across a build (symmetric peaks are no longer a fake signifier -- the hero's are symmetric): · rounded mushy peaks · shallow vague notch · soft glossy silicone · wide flat nylon webbing · black plastic hardware · thicker and sitting proud. Blank shells, no wordmarks ever. Blue gel pad on the cheap-silicone archetype only.

---

## 8. Buyer age band and cast profile

British, roughly 55–80. Cast to the buyer, balanced across men and women, with a minority outside the band.

---

## 9. Claim register (§43A)

| Claim | Tier | Status |
|---|---|---|
| **One size fits all** | Advertiser (user-stated V7.49.15) | Rendered as `FIT_SNUG` on worn frames and covered per §12 on fit lines. No size chart, size label or S/M/L is ever shown. The V7.49.13 competitor sizing figures (25–44 cm, 15–46 cm) are retired — this product has no sizes |
| Rendering size: shell ~12 cm × ~5 cm, band ~2.5 cm (`SIZE_LOCK`) | Derived | Proportions measured on `front.webp` (V7.49.21); absolute size from Tier-3 anatomy. Not advertiser-held — replace with supplied dimensions. Never stated on screen. (The V7.49.13 "band about 2 inches" category figure is retired.) |
| Adult patella about 4–5 cm wide; tendon 4–5 cm from inferior pole to tibial tuberosity | 3 | Anatomical anchor, used for scale reasoning only, never as a claim |
| Clinical placement "just below the kneecap"; one manufacturer specifies about 2 inches below | 3 | Third-party guidance. Compatible with the contact phrasing — the top edge touches the pole while the body covers the upper tendon |
| Every step puts **17× bodyweight** through the spot below the kneecap | **User-confirmed V7.49.29** | Advertiser-held. The number is a post overlay, never generated (§17) |
| **Three years to build with orthopaedic surgeons** | **User-confirmed V7.49.29** | Advertiser-held. Surgeon cast per §19B |
| Inside, a **silicone pad** catches the force | **User-confirmed V7.49.29** | The material is now advertiser-held. Rendering rule unchanged: prompts say "the pad", never "silicone", because the word renders the soft glossy fake (§10, `RULINGS['held_on_pad']`) |
| **Sports scientists measured 34% less strain** every step | **User-confirmed V7.49.29** | Advertiser-held. 34% is a post overlay; no screen with numerals is generated (§10) |
| Built for bone on bone, arthritis, worn cartilage, meniscus | **User-confirmed V7.49.29** | Advertiser-held |
| **Recommended by orthopaedic surgeons** | **User-confirmed V7.49.29** | Advertiser-held. Surgeon cast per §19B |
| **Worn by over 200,000 people** | **User-confirmed V7.49.29** | Advertiser-held. The number is a post overlay |
| **Buy 1 Get 1 Free — always** | User-confirmed V7.49.24 | Every offer, box and "what's included" beat shows two units (Standards §9 pair-pack carve-out). The offer text is added in the edit, never generated (§17) |
| **Sixty-day money-back guarantee** | **User-confirmed V7.49.29** | Advertiser-held. Terms shown in the edit, never generated |

---

## 10. Standing open item

**Peak equality and the wordmark are settled** by the supplied front photo (V7.49.10–11). **Still open: the true shell width-to-height.** `front.webp` gives an estimate (2.3–2.6, `INFO_RATIOS`); it becomes a figure only when measured edge to edge on a flat, no-yaw, no-roll elevation. Until then no aspect figure enters this sheet.

**Worn references (V7.49.15):** new front, rear and bent frames are prompted by `--worn-refs` (one size fits all, fitted exactly). They replace `PLACEMENT_REFERENCES` once accepted.

---

## 11. Content moved from the Standards at V7.49.4

The global Standards are product-agnostic from V7.49.4. Everything below used to be written into the global document about this product and now lives only here, imported from the `.py`:

| Standards § | Pattern there | Fill here |
|---|---|---|
| 9A-P | Rear path `[REAR-PATH]`, `[BAND-HEIGHT-RATIO]` | `SLOTS`, `REAR_VIEW_SPEC` — the band crosses **below** the hollow, across the top of the calf, knee bare above it; slides as bright bars at each outer edge; band presses in |
| 9A-P / A | `PLACE-BENT`, `PLACE-PROFILE`, `NEG-BENT` | `PLACE_BENT`, `PLACE_PROFILE`, `NEG_BENT` |
| 27D / A | `HOLD-PC`, `HOLD-PROD`, `NEG-WARP-P` | `HOLD_PC`, `HOLD_PROD`, `NEG_WARP_P` — matching peaks, notch, band width |
| 9D / A | `WEAR-CONCEAL`, `WEAR-REVEAL`, `NEG-CONCEAL`, garment list, reveal block | `WEAR_*`, `NEG_CONCEAL`, `CONCEALING`, `EXPOSING`, `HEM_RULE`, `REVEAL_STATUS` (OPEN since V7.49.8) |
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

## 13. Size — always the same *(V7.49.21 — user ruling)*

**One unit, one size, every frame.** Proportions measured straight-on on `front.webp`: the shell is **about 2.5× as wide as it is tall** (2.50; `product_front.jpg` 2.32), the band is **about half the shell's height**, the notch rises 0.18 of the width, the peaks span 0.60 of it. Rendering size: **shell ~12 cm across × ~5 cm tall, band ~2.5 cm** — derived, not advertiser-held.

| Context | Size anchor (string) |
|---|---|
| Product only | ~12 × 5 cm shell, band half the shell's height (`SIZE_OBJECT`) |
| Worn | shell spans the leg's whole front width, about as tall as the kneecap; band about a quarter of the calf's width (`SIZE_WORN`) |
| Held | shell five to six thumb-widths across, as tall as the thumb is long; band a little wider than the thumb (`SIZE_HELD`) |

A frame more than ~20% off its anchor is REGENERATE Q2. Drift found V7.49.21 and fixed V7.49.22: `worn_rear.jpg` band 0.33 of the leg → re-rolled to ~0.27 (edit, everything else unchanged); `product_front.jpg` failed three `--check` shape gates → re-rolled level and now passes them all. The `--check` gates stay in their own units: its band reading under-reads the knit (0.351 on `front.webp` for a band that is about half the shell's height edge to edge, confirmed on `back.webp`).

---

## 14. How it is worn *(V7.49.21 — user ruling)*

`WEAR_GUIDE` in the `.py` is the plain-words answer; every line points at the locked string that enforces it.

1. **One unit, one knee.** The side declared at the act map, held all build. Not handed.
2. **Shell on the front, notch up.** Wordmark upright and readable to someone facing the wearer. Never upside down, never on the side or back.
3. **On the patellar tendon.** Directly below the kneecap; the notch cups its lower border, no gap. Straight leg: peaks no higher than the base of the kneecap's sides. Bent leg: sits high, top edge level with the kneecap's lower pole. Kneecap face always uncovered.
4. **Band round the back, below the hollow.** Level, across the top of the calf, the two keeper loops together at the centre back. Only the band at the back.
5. **One size, snug.** Flat all the way round, no slack, no loose tail.
6. **On bare skin.** Hidden under trousers; never worn over clothing.
7. **Putting it on.** Closed band over the foot, to mid-shin on a straight leg, both hands flat on the shell slide it **up** until the kneecap stops it. Never opened, threaded or tightened on camera.
8. **While worn.** Hands off; it holds its place through walking, stairs, sitting.
9. **Held.** Pinched at the shell's bottom edge — thumb in front, fingers behind on the pad, band slack round the wrist. Never held and worn in one beat.
10. **Never shown.** Taking it off, the band open or adjusted, two units worn, the shell on the thigh, calf or kneecap.

---

## 15. Held beats, the inner pad and the standing negatives *(V7.49.23)*

**Held is not locked** (user): there are many right ways to hold it. Choose from `HELD_GRIPS` per beat — bottom-edge pinch, open palm, fingertips behind, turned through the light, two-hand presentation — and vary them across a build. Fixed rules: on the pad or the shell's edge; never on the band, never on the slides, never across the wordmark; peaks and notch visible. I2V negatives: `NEG-HELD-P`.

**The inner pad** (the user's "silicone pad"): plain, smooth, matte black, no markings (`INNER_PAD`, read off `back.webp`). Prompts say "the pad", never "silicone".

**Standing negatives from observed failures** (`NEG-OBSERVED`, dated in `NEG_OBSERVED_LOG`): V-shaped notch · crown or horn peaks · deep U or slab shell · slide on the face or on the band · invented slide frame · sideways chevrons · band out of the shell's bottom edge · product tipped · watch-strap band · buckle-shaped keeper. I2V only.

---

## 16. Which knee, the box and the offer *(V7.49.24 — user rulings)*

**Which knee — from the script** (`SIDE_RULE`, `side_from_script()`): a knee named in the script decides it; no knee named → right, matching the locked worn references. Declared once at the act map and held all build. **A left-knee build needs left-knee worn references first** — a right-knee frame is never mirrored, because the mirror reverses the wordmark.

**The offer — always Buy 1 Get 1 Free** (`OFFER`). So every box, offer and "what's included" beat shows **two** straps side by side (Standards §9 pair-pack carve-out). The offer text is added in the edit, never generated (§17).

**Our box** (`PACKAGE`, `PACKAGE-LOCK`, `NEG-PACKAGE`): a rigid two-piece box, matte black all over, about 28 × 16 × 8 cm. The only print is the lowercase grey stryde wordmark centred on the lid, in the same lettering and grey as the shell. Inside, a matte-black insert holds **exactly two straps** side by side, bands closed, shells up, wordmarks readable. No other items, no text, no stickers. The size is a rendering spec until the real box exists.

**Box references** (`PACKAGE_REFS`, **locked V7.49.27**): `package_closed.jpg` (e8c4df4b) and `package_open.jpg` (a9409405): straps **lie flat** (the band is soft), shell face up, one piece, band folded under (V7.49.26). For box beats attach the box reference plus `front.webp` + `back.webp`.

---

## 17. Anatomy looks *(V7.49.30–31 — user ruling)*

The mechanism beats use the Standards' anatomical register (§12A-1): knee · quadriceps, hamstrings and calf · femur, patella and tibia · target the patellar tendon · **site the patellar tendon immediately below the kneecap** (never the tibial tuberosity) · claim: protection.

| Beats | Look |
|---|---|
| The point, the load arriving, the pad catching the force (protection) | **ANAT-A full stack**, plus `ANAT_A_POINT_TIGHT` — one tight spot on the tendon, never spreading onto the shin |
| The conditions — bone on bone, worn cartilage, meniscus | **ANAT-B ghost limb** |

Samples of all four looks on this knee (A full stack, B ghost limb, C silhouette, D physical model) are in `stryde_refs/anatomy_samples/` (`ANATOMY_SAMPLES`) — for choosing only, never attached as references.
'''


# ==================================================================
# GEOMETRY CHECKER  (was stryde_frame_check.py)
# ==================================================================
# Thresholds come from RATIOS above — nothing below hardcodes a number.
# numpy and cv2 are imported inside the functions that need them, so the
# sheet still imports for prompt work without them installed.

import sys, os, glob

REFS = os.path.join(os.path.dirname(os.path.abspath(__file__)), PRODUCT_PHOTOS_DIR, "*")


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

    if a[0] == "--worn-refs":
        side = a[1] if len(a) > 1 else "right"
        for k, v in worn_ref_prompts(side).items():
            print("=== WORN-REF-%s · nano_banana_pro · 9:16 · 2k · %d chars · attach: %s"
                  % (k.upper(), len(v), ", ".join(WORN_REF_ATTACH[k])))
            print(v)
            print()
        sys.exit(0)

    if a[0] == "--product-set":
        for k, v in product_set_prompts().items():
            print("=== PRODUCT-%s · nano_banana_pro · 9:16 · 2k · %d chars · attach: %s"
                  % (k.upper(), len(v), ", ".join(PRODUCT_SET_ATTACH[k])))
            print(v)
            print()
        sys.exit(0)

    if a[0] in ("--check", "--refs"):
        paths = sorted(glob.glob(REFS)) if a[0] == "--refs" else a[1:]
        if not paths:
            sys.exit("no frames given")
        print("  thresholds from this sheet; ruling: %s" % list(RULINGS)[0])
        sys.exit(run(paths))

    sys.exit("unknown option %r — try no args, --md, --check, --refs" % a[0])
