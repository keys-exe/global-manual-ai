#!/usr/bin/env python3
"""
FACELOVE CHANGING FOUNDATION STICK — PRODUCT SHEET, SINGLE FILE.  V7.47

One artefact for §18 step 2. Attach this file alone when absorbing the
product; it carries everything that step needs.

    the prose spec .............. SHEET_MD, printable with --md
    the slots ................... SLOTS, fill()
    the locked strings .......... CONTACT_LOCK, ORIENT_LOCK, HOLD_LOCK, ...
    the measured ratios ......... RATIOS, INFO_RATIOS, RULINGS, UNSETTLED
    the per-batch checklist ..... CHECKLIST
    the assertions .............. verify()
    the geometry checker ........ check(), measure(), score()

USE

    python3 facelove_product_sheet.py             self-test, counts, ratios
    python3 facelove_product_sheet.py --md        write the prose sheet out
    python3 facelove_product_sheet.py --check f.. score frames against RATIOS
    python3 facelove_product_sheet.py --refs      score the canonical four

    from facelove_product_sheet import CONTACT_LOCK, fill
    fill(CONTACT_LOCK, end="balm")

NEVER RETYPE A STRING FROM THIS FILE INTO A PROMPT — import it. A retyped
string drifts from the one the assertions test, and the drift is silent.

TWO THINGS DIFFER FROM THE STRYDE SHEET AND BOTH ARE DELIBERATE.

1. The product is HELD AND APPLIED, never worn. §9's three product states
   resolve to held (§9A), demonstration (§9C) and an uncapping beat that is
   the §9B reposition carve-out with the cap as the moving part. There is no
   PLACE-LOCK, no ORIENT band, no IFACE contact-with-a-limb block. What
   replaces PLACE-LOCK is CONTACT_LOCK: where the tip meets skin and where
   the brush meets the laid band. Pasting a Stryde placement string into a
   FACELOVE beat describes a different object on a different body part.

2. NO LOCKED STRING MAY CONTAIN A NUMBER. Every absolute dimension and
   every ratio on this product is Tier 3 craft input (§43A) and the
   compiler's check_scale() refuses numeric figures in prompt text. The
   ratios below exist for the frame checker and for reasoning, and they
   never travel into a prompt. verify() enforces this as an assertion, so
   the rule cannot rot.

WHAT THE CHECKER CANNOT SEE, and these stay human checks:
  satin versus gloss on the barrel · fibre quality in the brush crown ·
  wordmark legibility · the terrain-constant rule · whether the colour
  front sits behind the brush crown · the four dated surface failures.
It measures proportion and two colour axes only. A frame that passes here
can still be wrong.
"""

VERSION = "7.49.5"
PRODUCT = "FACELOVE Changing Foundation Stick"

# WHAT CHANGED AT V7.49.5 — the advertiser's own retail carton and the
# delivery packaging were photographed and read. This is the first TIER 1
# physical evidence on the sheet and it settles two things the whole V7.49.4
# research pass could only guess at.
#
#   SETTLED  fill weight. The carton states it. Both third-party figures
#            are withdrawn — see RULINGS['fill_weight_settled'].
#   SETTLED  the product's name on the pack, which is not the name on the
#            website — see RULINGS['pack_name_differs'].
#   ADDED    PACK      the carton, the mailer and the pouch, specified
#   ADDED    PACK_LOCK / PACK_LOCK_C / NEG_PACK, for unboxing, offer and
#            guarantee beats, which had no strings at all until now
#   ADDED    SIBLINGS  the four other products in the same drop, because a
#            bundle or what's-included beat will otherwise invent them
#
# THE THING TO KNOW BEFORE WRITING A PACK BEAT: THE BOX IS WHITE AND THE
# STICK IS VIOLET. Every generator handed "FACELOVE packaging" will reach
# for the barrel's lilac and put it on the carton. It is wrong, and it is
# wrong in the one beat class where the pack is the hero.

# WHAT CHANGED AT V7.49.4 — a full source pass over the advertiser's own
# pages, the EU sister store, the marketplace listings and the category's
# social, plus a fresh measurement pass over the four canonical renders.
#
#   ADDED   DIMS      absolute dimensions, tiered, anchored to the carton
#   ADDED   INCI      the published ingredient list, verbatim
#   ADDED   CLAIMS    every advertiser claim found, §43A-tiered
#   ADDED   NEVER     claims belonging to other brands in the category
#   ADDED   REF_WANTED the two views the canonical set does not carry
#   CHANGED RATIOS    CLOSED_ASPECT and DEPLOYED_ASPECT re-banded; the
#                     balm's own exposed aspect added; BALM_B_STAR split
#                     out of CREAM_B_STAR
#   CHANGED RULINGS   five new, including the twist-up mechanism and two
#                     source conflicts that are logged, never corrected
#   CHANGED UNSETTLED brush_end_deployment resolved; two gates stand
#
# THE SINGLE MOST IMPORTANT FINDING IS IN CLAIMS, NOT IN GEOMETRY. The
# advertiser's own page claims that fine lines are softened and appear
# smoother with each application. The render standard forbids showing any
# such thing (TERRAIN_LOCK). That is an Order-of-Authority collision, it
# is surfaced and not resolved here, and it blocks every beat that carries
# those lines until the advertiser rules.

# --------------------------------------------------------------- slots
#
# The mechanism register is the locked §12A-4 Surface Layer register, an
# anatomical-family register at skin-surface scale: no bone, no muscle, a
# volumetric skin body read through the material rather than via a cut
# section. The slot names are the standards' slot names, filled at that
# scale, so the §12A blocks substitute without rewording.

SLOTS = {
    "REGION":       "a band of mature facial skin running from crest to crease",
    "STACK":        "the dry surface plates and the band of skin between them",
    "BONES":        "the warm body zone below the surface, read through the material as depth",
    "TARGET":       "the film of product lying across crest and crease",
    "TARGET_JOINT": "the shear front travelling behind the brush crown",
    "SITE":         "the crease floor and the dry plate gaps immediately either side of it",
    "LANDMARK":     "the crease itself",
    # the object's own parts, named once and reused
    "BARREL":       "a slim satin pale violet-mauve metal barrel",
    "TIP_BALM":     ("a solid warm-neutral white balm, its top cut back into two straight "
                     "shoulders that rise to a short flat crest"),
    "TIP_BRUSH":    ("a dense white synthetic brush crown, domed and slightly splayed, "
                     "standing proud of its collar"),
    "COLLAR":       ("a stepped collar that flares outward to the barrel, a fine machined slot "
                     "set into its sloped face just below the rim"),
    "WORDMARK":     "a single pale letterspaced FACELOVE wordmark running along the barrel",
    # declared per beat at the act map, held across the beat
    "END":          None,
}

# Slots the standards define that this product does NOT fill. Named so that
# nobody quietly borrows a string that needs them.
NOT_APPLICABLE = {
    "BAND_MATERIAL": "no band — the product is not worn",
    "HARDWARE":      "no exposed hardware — the collar slot is the only cut detail",
    "BAND_INNER":    "no band, therefore no inner face",
    "OFFSET":        "no placement offset — contact is stated, never measured",
}

MECHANISM_CLAIM    = "adaptation"        # one per build; coverage is the retired alternative
MECHANISM_REGISTER = "surface-layer"     # §12A-4
ENDS = ("balm", "brush")


def fill(s, end=None):
    """Substitute slots. Raises if the beat's working end is undeclared."""
    end = end or SLOTS["END"]
    if end not in ENDS:
        raise ValueError("declare END as one of %s before filling any string" % (ENDS,))
    out = s
    for k, v in SLOTS.items():
        if v is None:
            continue
        out = out.replace("[%s]" % k, v)
    out = out.replace("[END]", end)
    out = out.replace("[OTHER_END]", "brush" if end == "balm" else "balm")
    return out


# ------------------------------------------------------ locked strings
#
# Scale is stated RELATIONALLY and never as a figure — see the module
# docstring. Contact is stated as contact, exactly as the Stryde height
# clause is, because a generator can draw a relationship between two shapes
# and cannot resolve a measurement.

REF_PROD = (
"The product exactly as in the attached reference image — a slim satin pale violet-mauve metal barrel, "
"cool-toned and softly reflective rather than glossy, closed at the far end, carrying a single pale "
"letterspaced FACELOVE wordmark set along the barrel on its front centreline, and at the working end "
"either a solid warm-neutral white balm cut back into two straight shoulders rising to a short flat crest, "
"or a dense white synthetic brush crown standing domed and slightly splayed above a stepped collar with a "
"fine machined slot in its sloped face —")

# ---- the applied-contact lock. This is what PLACE-LOCK is for a worn
# product: it states what touches what, and what must stay visible.
CONTACT_LOCK = (
"The [END] end is the working end and it is already in contact with the skin, the cap already off and out of "
"frame. THE BALM MEETS THE SKIN ON ITS FLAT CREST AND THE LEADING SHOULDER, never on the barrel rim: the crest "
"lies flat against the surface and the skin gives very slightly under it, a shallow dimple with a tight contact "
"shadow along the whole line of the crest and no daylight anywhere between white and skin. THE BRUSH MEETS THE "
"SKIN ON THE SIDE OF ITS CROWN, not on its tip: the fibres bend back against the surface, the crown flattening "
"a little where it presses and springing clear behind, the collar itself never touching the face. Product is "
"laid as a band and worked from the band outward. The barrel stays clear of the skin at all times. THE TERRAIN "
"IS CONSTANT: every crease, pore and fold sits exactly as deep after the product as before it, unchanged in "
"depth, length and shape — the product evens colour across the terrain and never fills, softens or erases it.")

CONTACT_LOCK_C = (
"The [END] end is already in contact with the skin, cap already off and out of frame. The balm meets the skin on "
"its flat crest and leading shoulder, the skin giving very slightly under it with a tight contact shadow along "
"the crest and no gap between white and skin; the brush meets it on the side of its crown, fibres bending back "
"and springing clear behind, the collar never touching the face. The barrel stays clear of the skin. THE TERRAIN "
"IS CONSTANT: every crease, pore and fold sits exactly as deep after the product as before it, unchanged in "
"depth and shape.")

# ---- the terrain-constant rule as its own block, because it is the one
# clause the whole product argument rests on and it is never trimmed.
TERRAIN_LOCK = (
"THE TERRAIN IS CONSTANT THROUGHOUT. The crease is exactly as deep in the final frame as in the first: same "
"depth, same length, same shape, same shadow geometry inside it. Pores stay open and individually resolved, fine "
"lines stay legible, the surface keeps its relief. What changes is colour and colour only — the film evens tone "
"across crest and crease alike while every feature of the terrain stays exactly where it was.")

# ---- orientation. The stick has two ends and one wordmark, and both facts
# fail in ways a still cannot show.
ORIENT_LOCK = (
"The [END] end is uppermost and deployed; the [OTHER_END] end is at the bottom of the barrel, capped, closed and "
"unremarkable, and it is never open in the same frame. THE WORDMARK APPEARS ONCE AND ONCE ONLY: a single pale "
"letterspaced FACELOVE set along the barrel on its front centreline, running with the length of the barrel "
"rather than across it, upright to the balm end so that it reads upward from the base when the balm is uppermost "
"and downward from the top when the brush is uppermost. It sits on the barrel section immediately below the "
"working end, never on the closed end, never across the barrel, never twice in one frame and never on both "
"sections. The barrel's satin surface carries one soft broad highlight running the length of the lit side and a "
"gradual fall to a cool shadow edge on the other; the finish is satin, holding that highlight broad and diffuse "
"rather than as a hard mirror line.")

ORIENT_C = (
"The [END] end stays uppermost and deployed throughout, the [OTHER_END] end capped and closed at the bottom of "
"the barrel and never opened. One wordmark only, set along the barrel on its front centreline below the working "
"end, upright to the balm end, never across the barrel and never twice in frame. Satin barrel, one soft broad "
"highlight down the lit side.")

# ---- §9A held beats. The barrel is slim, so the grip is the whole risk.
HOLD_LOCK = (
"Held in one hand, low on the barrel and well below the wordmark, fingers wrapped around the closed end with the "
"working end standing clear and upward. Fingers never cross the wordmark, never touch the balm crest or the "
"brush crown, and never cover the collar. The barrel is held near upright with a slight tilt toward the lens so "
"the wordmark stays square to camera and legible along its length. Nothing is unscrewed, twisted, wound up, "
"clicked or adjusted; the product is complete and at rest in the hand on the first frame.")

# ---- the §9B reposition carve-out, with the cap as the moving part. The
# object's state never changes: only the cap's position does.
UNCAP_LOCK = (
"The stick is already fully formed and complete — barrel closed, working end fully formed, wordmark readable — "
"with the cap still seated on the working end. One hand holds the barrel low and the other draws the cap "
"STRAIGHT OFF ALONG THE BARREL'S OWN AXIS in a single unhurried movement, without twisting, and the working end "
"comes clear exactly as it already was: the balm crest and shoulders intact, or the brush crown standing proud "
"of its collar, unchanged in shape at every frame. Nothing screws, winds, clicks or extends. The cap is still in "
"the second hand and still travelling at the cut, the movement unfinished.")

NEG_CONTACT = (
"no product filling the crease, no crease shallower after the product than before, no crease erased, no line "
"softened away, no terrain smoothed out, no pores closed over, no surface flattened into an even sheet, no skin "
"rendered poreless, no gap between the balm crest and the skin, no floating balm, no product hovering above the "
"surface, no barrel rim touching the skin, no collar touching the skin, no brush tip stabbing the surface, no "
"colour resolving ahead of the brush, no colour arriving before the brush touches it, no fully matched patch "
"with no brush present")

NEG_ORIENT = (
"no second wordmark, no wordmark on both barrel sections, no wordmark across the barrel, no horizontal wordmark "
"on an upright barrel, no wordmark on the capped end, no mirrored or reversed lettering, no wordmark on the "
"brush collar, no both ends open at once, no cap missing from the closed end, no second cap in frame, no second "
"unit, no gloss mirror finish on the barrel, no chrome barrel, no hard specular line down the barrel, no seam "
"where the barrel has none")

NEG_UNCAP = (
"no twisting, no unscrewing, no winding, no clicking, no product extending or retracting, no mechanism turning, "
"no balm rising out of the barrel, no brush emerging from inside the barrel, no cap being replaced, no product "
"changing shape, no product changing size, no crest deforming, no crown compressing, no hands passing through "
"the product, no additional hands, no second person, no two separate actions in one clip, no cap coming to rest "
"in frame")

# ---- the four dated observed failures, 2026-08-14. Permanently never
# trimmed from any surface-layer beat and from any macro cream beat.
NEG_SURFACE_FAILURES = (
"no bubbles on the cream, no domes on the cream surface, no blistered surface, no foamed layer, no granular bead "
"layer, no bed of separate beads, no polystyrene foam texture, no rounded bodies sitting at the base of the "
"film, no globules, no droplets suspended in the layer, no cool blue-white cream, no blue cast in the white, no "
"grey-white cream, no cream cooler in tone than the ground it sits on")

# ---- vocabulary the register does not use, in either channel
NEG_LOOK = (
"no glowing skin, no radiant skin, no luminous finish, no flawless finish, no beauty-filter smoothing, no "
"airbrushed skin, no poreless skin, no plastic sheen, no wet gloss on the finished film, no makeup-advertisement "
"gloss, no even mask of colour, no opaque coverage hiding the surface")

# ---- packaging. New at V7.49.5. Until now the sheet had no string for the
# retail carton at all, so every offer, guarantee, unboxing and
# what's-included beat was being written freehand — the exact drift path §8
# exists to close, on the one beat class where the pack is the hero.

PACK_LOCK = (
"The retail carton is a tall slim rectangular box in soft matte off-white, several times taller than it is wide "
"and only a little deeper than it is wide, its long faces flat and its edges crisp and square. The board is "
"uncoated and matte: no gloss, no varnish, no foil, no metallic, no embossing anywhere on it. Printing is pale "
"grey-silver, low in contrast against the white and small throughout — a letterspaced FACELOVE set along one long "
"face and reading upward along its length, and beneath it a single fine line-drawn flourish curving across the "
"face, drawn in one continuous hairline. THE BOX IS WHITE AND THE STICK IS VIOLET: the carton carries none of the "
"barrel's colour and nothing on it is tinted. The small block of product type low on the face is left blank in "
"generation and set afterwards.")

PACK_LOCK_C = (
"A tall slim rectangular carton in soft matte off-white, several times taller than wide, flat faced with crisp "
"square edges, uncoated board with no gloss, foil, metallic or embossing. Pale grey-silver print, low contrast "
"and small: a letterspaced FACELOVE reading upward along one long face, one fine line-drawn flourish beneath it. "
"THE BOX IS WHITE AND THE STICK IS VIOLET. The product type block low on the face is left blank in generation.")

UNBOX_LOCK = (
"The outer mailer is a white bubble-lined poly envelope, soft and padded, its bubble grid clearly readable through "
"the face, sealed along a welded top edge with a fine sawtooth texture; one large letterspaced FACELOVE runs "
"across its upper face in pale lilac-mauve, and this is the only place in the whole delivery where the brand's "
"lilac appears on packaging. Inside it a flat frosted zip pouch, slide-sealed with a small black slider, "
"translucent enough that the cartons inside read as soft shapes through it, its own tone a pale cool lilac-white "
"cooler and bluer than the barrel and never a match for it, with FACELOVE in black across its face.")

NEG_PACK = (
"no lilac carton, no violet box, no coloured box, no tinted board, no printed pattern on the box, no gloss finish "
"on the board, no varnish, no foil, no metallic print, no gold, no embossing, no spot gloss, no ribbon, no bow, "
"no window cut into the box, no barcode, no small print, no ingredient list, no paragraph of text, no numerals, "
"no price, no sticker, no seal, no duplicate wordmark on one face, no wordmark across the short face, no mirrored "
"or reversed lettering, no box being torn open, no box being crushed, no second carton unless the beat is a "
"sanctioned pair-pack")

S = {
    "REF-PROD": REF_PROD,
    "CONTACT-LOCK": CONTACT_LOCK, "CONTACT-LOCK-C": CONTACT_LOCK_C,
    "TERRAIN-LOCK": TERRAIN_LOCK,
    "ORIENT-LOCK": ORIENT_LOCK, "ORIENT-C": ORIENT_C,
    "HOLD-LOCK": HOLD_LOCK, "UNCAP-LOCK": UNCAP_LOCK,
    "PACK-LOCK": PACK_LOCK, "PACK-LOCK-C": PACK_LOCK_C,
    "UNBOX-LOCK": UNBOX_LOCK, "NEG-PACK": NEG_PACK,
    "NEG-CONTACT": NEG_CONTACT, "NEG-ORIENT": NEG_ORIENT,
    "NEG-UNCAP": NEG_UNCAP, "NEG-SURFACE-FAILURES": NEG_SURFACE_FAILURES,
    "NEG-LOOK": NEG_LOOK,
}

# ------------------------------------------- measured geometry ratios
#
# Every figure below is measured off the canonical renders by segmenting
# each row against its own background, splitting the white tip from the
# violet barrel on the blue-minus-green channel, and normalising to the
# barrel width adjacent to the feature. Bands are the observed range plus a
# margin: raw min and max would put the references themselves on the
# boundary and fail a correct frame on a rounding difference.
#
# NONE OF THESE EVER ENTERS A PROMPT. Tier 3, craft input only (§43A).

RATIOS = {
    # balm tip width / the sleeve it stands on. Observed 0.86 on the one
    # deployed balm render.
    "BALM_OVER_SLEEVE":     (0.78, 0.94),
    # chamfer rise / balm tip width. Observed 0.25. This is the number that
    # keeps the crest a low broad chisel rather than a cone or a dome.
    "CHAMFER_RISE":         (0.19, 0.33),
    # flat crest width / balm tip width. Observed 0.08 — a short flat, not
    # a point and not a dome.
    "CREST_FLAT":           (0.03, 0.15),
    # brush crown width / barrel width. Observed 0.76.
    "CROWN_OVER_BARREL":    (0.68, 0.85),
    # crown height above the collar rim / crown width. Observed 0.65: the
    # crown is broader than it is tall.
    "CROWN_ASPECT":         (0.54, 0.78),
    # balm exposed height above the sleeve / balm width. Observed 0.297 on
    # the one deployed balm render, re-measured 2026-09-14. This is what
    # keeps the deployed bullet a LOW BROAD CHISEL rather than a tall
    # bullet: it is roughly a third as tall as it is wide, and a generator
    # handed "foundation stick" returns something twice that.
    "BALM_EXPOSED_ASPECT":  (0.22, 0.40),
    # closed stick height / greatest barrel width. Observed 4.75-4.82 in
    # the V7.47 pass and 5.03 in the V7.49.4 re-measure of the same render.
    # Both figures are kept and the band covers both — see RULINGS
    # ["remeasure_2026_09"]. The difference is where each pass took the
    # barrel width, not a change in the object.
    "CLOSED_ASPECT":        (4.45, 5.35),
    # wordmark block length / barrel width. Observed 1.19-1.25 across all
    # three single-unit renders — the most stable figure on the sheet.
    "WORDMARK_LENGTH":      (1.08, 1.36),
    # wordmark cap height / barrel width. Observed 0.175-0.18.
    "WORDMARK_CAP_HEIGHT":  (0.14, 0.22),
    # |wordmark centre - barrel centre| / barrel width. Observed 0.01: the
    # wordmark sits on the front centreline, not offset.
    "WORDMARK_CENTRING":    (0.00, 0.06),
    # colour, and these two are the point. The barrel is the only cool
    # element on the object; the cream is warm-neutral and must never drift
    # cool. b* below zero on the cream is the dated 2026-08-14 failure.
    "CREAM_B_STAR":         (0.5, 14.0),
    "BARREL_B_STAR":        (-16.0, -3.0),
    "BARREL_A_STAR":        (4.0, 18.0),
    # The SOLID balm in the barrel is a much tighter target than a laid
    # film on skin. Measured across the three single-unit renders at
    # L 95.1-95.4, a* +0.8 to +1.0, b* +2.0 to +2.4 — a warm-neutral white
    # that is very nearly neutral and never negative. CREAM_B_STAR stays
    # wide because a laid film picks up the ground it sits on.
    "BALM_B_STAR":          (0.5, 6.0),
    "BALM_L_STAR":          (90.0, 99.0),
    # Brush fibre. Measured L 90.2-91.2, a* +1.4 to +1.7, b* +2.0 to +2.4:
    # the same warm-neutral white as the balm, read a little darker because
    # fibre shadows itself. A crown rendered BRIGHTER than the balm is the
    # tell that the generator has given it a plastic or nylon sheen.
    "FIBRE_L_STAR":         (85.0, 94.0),
}

# Measured, reported, and deliberately NOT gated.
INFO_RATIOS = {
    # deployed height / barrel width. Observed 4.94 balm-out and 5.05
    # brush-out in the V7.47 pass; 5.27 balm-out, 5.56 brush-out and
    # 5.68/5.72 in the two-unit render in the V7.49.4 re-measure. Both
    # passes are kept. How far the working end stands proud is a STATE on
    # a twist-up mechanism, not a property, so it is reported and never
    # failed — which is exactly why the spread does not matter.
    "DEPLOYED_ASPECT":      (4.60, 6.00),
    # brush-out reads TALLER than balm-out in every render that shows both.
    # Reported so that a frame putting them the other way round is visible.
    "BRUSH_OVER_BALM_H":    (1.02, 1.12),
    # closed-body section split, top to bottom, as fractions of body
    # height: 0.39 cap over the balm end, 0.36 wordmark barrel, 0.24 base
    # over the brush end. Perspective moves these more than the object does.
    "CAP_SECTION":          (0.34, 0.45),
    "BASE_SECTION":         (0.19, 0.30),
    # collar slot width / collar width. Observed 0.39 on the one render
    # that shows it.
    "COLLAR_SLOT":          (0.28, 0.50),
}

# ---------------------------------------------------- absolute dimensions
#
# NONE OF THESE EVER ENTERS A PROMPT — check_scale() refuses numerals in
# prompt text and verify() enforces it. They exist for three jobs: to size
# a hand and a face correctly in a beat the writer is imagining, to sanity
# -check a render against the real object, and to give the ratios above an
# anchor in millimetres so a wrong-scale frame is arguable rather than
# merely felt.
#
# TIERING (§43A). Nothing here comes from the advertiser. Every figure is
# a third-party marketplace listing or is derived from one, so the whole
# block is TIER 2 AT BEST and the derived rows are Tier 3. The advertiser
# publishes no dimension and no fill weight on either store.

DIMS = {
    # (value_mm_or_g, tier, source)
    "carton_height":   (148.0, 2, "Amazon package dims 5.83-5.91 in, two listings"),
    "carton_width":    (26.5,  2, "Amazon package dims 1.02-1.06 in"),
    "carton_depth":    (24.9,  2, "Amazon package dims 0.98 in, two listings"),
    "gross_weight_g":  (41.1,  2, "Amazon 1.45 oz, two listings — product plus carton"),
    "stick_height":    (127.0, 2, "Amazon 'Product Dimensions 1 x 1 x 5 inches'"),
    "barrel_diameter": (25.2,  3, "derived: stick_height / CLOSED_ASPECT observed 5.03"),
    "upper_sleeve_d":  (20.4,  3, "derived: 0.81 of barrel, measured off the balm render"),
    "collar_diameter": (21.7,  3, "derived: 0.86 of barrel, measured off the brush render"),
    "balm_width":      (17.5,  3, "derived: BALM_OVER_SLEEVE 0.857 of upper sleeve"),
    "balm_exposed_h":  (5.2,   3, "derived: BALM_EXPOSED_ASPECT 0.297 of balm width"),
    "crown_width":     (19.4,  3, "derived: CROWN_OVER_BARREL 0.77 of barrel"),
    "crown_height":    (12.0,  3, "derived: CROWN_ASPECT 0.62 of crown width"),
    "wordmark_length": (30.5,  3, "derived: WORDMARK_LENGTH 1.21 of barrel"),
    "wordmark_cap_h":  (4.4,   3, "derived: WORDMARK_CAP_HEIGHT 0.177 of barrel"),
}

# Fill weight is SETTLED at V7.49.5 by the advertiser's own carton, which
# states it on the front face. Tier 1. The two third-party figures carried
# at V7.49.4 are WITHDRAWN and kept only as a record of what was wrong, so
# that nobody re-derives them from a marketplace listing later.
FILL = {
    "net_weight_g": (13.0, 1, "printed on the retail carton front face"),
    "net_volume":   ("0.45 fl oz", 1, "printed on the retail carton front face"),
    "withdrawn": {
        "7 g":     "eBay listing. Wrong — half the true fill.",
        "0.35 oz": "several Amazon titles, 9.9 g. Wrong — the mould's "
                   "commonest fill, carried over by resellers who never "
                   "read this carton.",
    },
    "note": "Thirteen grams is a substantial charge for a stick this size, "
            "and it is a fact worth having in the offer act: it is nearly "
            "a third more product than the figure every marketplace "
            "reseller prints. It is Tier 1 and it is the advertiser's own.",
}

# --------------------------------------------------------------- packaging
#
# Read off photographs of a delivered order, 2026-09-14. TIER 1 — this is
# the advertiser's own packaging, photographed, not described by anyone.
#
# THE ONE THING THAT MATTERS MOST: THE CARTON IS WHITE AND THE STICK IS
# VIOLET. Nothing in the retail packaging carries the barrel's colour, and
# a generator handed "FACELOVE packaging" will put it there every time.

PACK = {
    "carton": {
        "form":    "a tall slim rectangular box, several times taller than "
                   "it is wide and only a little deeper than wide, flat "
                   "faced with crisp edges",
        "colour":  "soft matte off-white, very slightly warm — measured "
                   "L 98, a* -1.7, b* +3.7. Not bright paper white, not "
                   "cream, and emphatically not lilac",
        "finish":  "uncoated matte board. No gloss, no varnish, no foil, "
                   "no emboss, no spot UV",
        "print":   "pale grey-silver, low contrast against the white, all "
                   "of it small. A letterspaced FACELOVE set along the long "
                   "face reading upward; one fine line-drawn flourish "
                   "curving across the face beneath it; a small block of "
                   "product type low on the same face",
        "type_block": "the product name, a one-line descriptor, and the net "
                      "weight — all of it §17 territory. BLANK IT IN "
                      "GENERATION AND SET IT IN POST. It garbles every time "
                      "and it is the part a viewer reads",
    },
    "mailer": {
        "form":   "a white bubble-lined poly mailer, soft and padded, the "
                  "bubble grid clearly readable through the face, sealed "
                  "along a welded top edge with a fine sawtooth texture",
        "print":  "one large letterspaced FACELOVE across the upper face in "
                  "pale lilac-mauve — the only place in the whole delivery "
                  "where the barrel's colour family appears on packaging",
    },
    "pouch": {
        "form":   "a flat frosted zip pouch, slide-seal with a black "
                  "slider, translucent enough to read the cartons through "
                  "it as soft shapes",
        "colour": "pale cool lilac-white — measured L 93, a* -0.2, "
                  "b* -7.2. Cooler and bluer than the barrel, not a match",
        "print":  "FACELOVE in black, larger than anything on the cartons, "
                  "with a short tagline line set beneath it",
    },
}

# The other products that arrive in the same pouch. Named so that a bundle,
# an unboxing or a what's-included beat has a real set to show instead of
# an invented one, and so that a sibling carton is never mistaken for this
# product's carton — they are the same board, the same white and the same
# print style, and they differ only in the small type block.
SIBLINGS = {
    "foundation brush": "its own carton, same white, same slim box",
    "everlove mascara": "a care mascara, in the same carton family",
    "eyeshadow stick":  "two of them in the photographed drop, same carton "
                        "family, a noticeably shorter box",
}

# What the stick reads as in a hand, for the writer rather than the model.
# A barrel a shade over an inch tall short of a ruler's five inches, about
# as thick as a thumb, and light — it sits in the hand like a fat marker
# pen, not like a lipstick. That sentence is the useful form of the block
# above and it is the only form that should ever reach a prompt.

# ---------------------------------------------------------------- INCI
#
# Published on the EU sister store (faccelove.com), not on the US store.
# Verbatim, in the published order. TIER 1 as an ingredient disclosure;
# see CLAIMS for what may and may not be said about it.

INCI = (
    "Squalane, Diisostearyl Malate, CI 77891, Limnanthes Alba (Meadowfoam) "
    "Seed Oil, Simmondsia Chinensis (Jojoba) Seed Oil, Butyrospermum Parkii "
    "(Shea) Butter, Euphorbia Cerifera (Candelilla) Wax, Copernicia Cerifera "
    "(Carnauba) Wax, Tocopheryl Acetate, Phytosteryl Oleate, Madecassoside, "
    "Ceramide NP, CI 77492, CI 77491, CI 77499."
)

# The INCI is the mechanism's evidence and it is worth reading as one.
#
#   CI 77891            titanium dioxide — the white, and the hiding power
#   CI 77492/77491/77499 yellow, red and black iron oxide — the TONE
#   Diisostearyl Malate  the ester the pigment is dispersed in
#   Candelilla/Carnauba  the waxes that make it a stick rather than a cream
#   Squalane, jojoba, meadowfoam, shea   the emollient load
#   Tocopheryl Acetate   vitamin E
#   Madecassoside        the centella actives
#   Ceramide NP          barrier lipid
#
# THE COLOUR IS ALREADY IN THE STICK. It is not made on the skin and
# nothing reacts with anything. Three iron oxides sit at low load in a
# matrix the titanium dioxide renders opaque white; thinning the film under
# shear drops the white's hiding power and the oxides read through. That is
# exactly the ADAPT behaviour the register already renders — colour
# resolving from inside the cream's own thickness at the shear front — and
# it means the render is a description of the material rather than a
# metaphor for it. Say it that way, never as a reaction.

MECHANISM_PHYSICAL = (
    "Three iron oxides dispersed at low load in an ester-and-wax base that "
    "titanium dioxide renders opaque white. Thinning the film under the "
    "brush drops the white's hiding power and the oxides read through, so "
    "the tone resolves from inside the film's own thickness at the shear "
    "front. Nothing reacts, nothing is triggered, and the colour was in the "
    "stick before it touched anyone."
)

# --------------------------------------------------------------- claims
#
# §43A, assigned per claim, from the advertiser's own two stores. Tier 1 is
# stated as fact. Tier 2 is stated and the qualification goes in the editor
# note; the line is NOT altered. Tier 3 BLOCKS its beat until the advertiser
# rules; the line is NOT rewritten and NOT cut (§27B — CUT is withdrawn).

CLAIMS = {
    # ---- tier 1: the advertiser's own commercial terms, on their page
    "price_39_from_59":        (1, "US store, live"),
    "guarantee_30_day":        (1, "US store, stated twice"),
    "free_shipping_us":        (1, "US store"),
    "dual_ended_with_brush":   (1, "the object; visible in every render"),
    "goes_on_white":           (1, "the object; CI 77891 on the INCI"),
    "one_shade":               (1, "single 'Default Title' variant on both stores"),
    "ingredients_as_inci":     (1, "EU store, verbatim in INCI above"),
    "net_weight":              (1, "printed on the retail carton front face; "
                                   "see FILL. This supersedes every "
                                   "marketplace figure"),
    "pack_name":               (1, "printed on the retail carton — the pack "
                                   "name differs from the website name; see "
                                   "RULINGS['pack_name_differs']"),
    "matches_your_natural_skintone": (1, "printed on the retail carton as the "
                                         "product's own descriptor line. Tier 1 "
                                         "as a quotation of the advertiser's own "
                                         "pack; the underlying performance claim "
                                         "is still the Tier 2 adapts_to_skin_tone "
                                         "row below"),

    # ---- tier 2: real but qualified. State the line, flag in the editor note
    "adapts_to_skin_tone":     (2, "true of the material (see MECHANISM_PHYSICAL) "
                                   "but 'perfectly' and 'always the perfect tone' "
                                   "overstate a single-shade product; the honest "
                                   "form is that it meets a wide middle band"),
    "no_orange_grey_yellow":   (2, "a formulation intention, not a measured result"),
    "does_not_settle_in_lines": (2, "renderable and consistent with TERRAIN_LOCK — "
                                    "this is the claim to lean on, because the film "
                                    "not plugging the crease is a thing the camera "
                                    "can actually show"),
    "cruelty_free":            (2, "asserted on a badge; no certifier named"),
    "suitable_sensitive_skin": (2, "asserted; no panel test cited"),
    "buildable_coverage":      (2, "ordinary of the format"),
    "reviews_4624":            (2, "site widget. SEE RULINGS['review_count_conflict'] "
                                   "— the brand's own Shop listing showed 2 ratings"),

    # ---- tier 3: BLOCKED. No source held. Do not build against these.
    "50000_women_over_40":     (3, "no source anywhere on either store"),
    "lasts_up_to_12_hours":    (3, "EU store, 'tested on mature skin' — no study"),
    "no_oxidation_by_midday":  (3, "EU store; a durability claim with no test"),
    "thousands_of_tones_analysed": (3, "EU store development story, unsourced"),
    "softens_fine_lines":      (3, "US and EU stores, twice each. COLLIDES WITH "
                                   "TERRAIN_LOCK — see RULINGS['terrain_vs_copy']"),
    "lines_smoother_each_use": (3, "US and EU stores. Same collision, and it is "
                                   "additionally a cumulative-efficacy claim"),
    "anti_aging":              (3, "US and EU section headings"),
    "covers_dark_spots":       (3, "testimonial copy; a coverage performance claim"),
    "hyaluronic_acid":         (3, "US store ingredient panel — NOT ON THE INCI"),
    "niacinamide":             (3, "US store ingredient panel — NOT ON THE INCI"),
    "aloe_vera":               (3, "EU store ingredient panel and FAQ — NOT ON THE INCI"),
    "beeswax":                 (3, "EU store ingredient panel — NOT ON THE INCI"),
}

# Claims that belong to OTHER brands in the same Korean dual-ended mould and
# that marketplace copy repeatedly attaches to this one. None of them is a
# FACELOVE claim and none may enter a script, a caption or a prompt.
NEVER_CLAIM = {
    "SPF 50+":     "ELROEL and others in the category. FACELOVE publishes no SPF "
                   "and the INCI carries no filter.",
    "Volufiline":  "ELROEL's actives story.",
    "collagen":    "ELROEL and several marketplace resellers. Not on the INCI.",
    "collagen capsules": "a reseller's invented mechanism. The colour is pigment, "
                         "not capsules — see MECHANISM_PHYSICAL.",
    "waterproof":  "marketplace titles only; never claimed by the advertiser.",
    "sweat-proof": "marketplace titles only.",
    "full coverage": "marketplace titles. The advertiser says buildable and "
                     "lightweight, which is the opposite end of the same axis.",
    "Korean":      "true of the mould and the category, never said by the "
                   "advertiser about this product. Adding it is a sourcing "
                   "claim nobody has authorised.",
}

# -------------------------------------------------- reference set wanted
#
# The canonical set is the advertiser's own four renders and it STAYS the
# canonical set (§5: competing reference sets are a drift source, and every
# beat already built is built against these). Nothing here replaces them.
# These are the two views the set does not carry, generated to ADD to it.

REF_WANTED = {
    "REF-REAR-01":
        "The closed stick, single unit, rotated a half turn from the "
        "canonical front elevation, same ground and same light. ATTACHABLE. "
        "Closes UNSETTLED['rear_and_rotated_elevation'] and unblocks every "
        "beat in which the stick turns, rolls in the hand, or the camera "
        "orbits it.",
    "REF-SHEET-01":
        "BUILT 2026-09-14 and no longer wanted as a generation. It exists "
        "as FACELOVE_REF_SHEET_01.png, COMPOSITED FROM THE ADVERTISER'S OWN "
        "THREE RENDERS rather than generated from a prompt — the three "
        "units matted out, scaled to a common barrel width so their "
        "proportions read against each other, laid on one ground with four "
        "detail crops taken at scale from the same files, and captioned in "
        "post (§17: type is post, and drawn type does not garble). "
        "Compositing beats generating here and it is worth saying why: a "
        "generated sheet is a model's idea of the object and drifts from "
        "it, and a reference that drifts is worse than no reference at all. "
        "Every pixel of this one is the advertiser's. NEVER ATTACHABLE — it "
        "is a multi-instance frame (§5) and attaching it is the fastest "
        "route to two sticks in a frame that should hold one. Read it by "
        "eye against CHECKLIST; do not point --check at it.",
}

RULINGS = {
    "fill_weight_settled":
        "SETTLED, TIER 1, off the advertiser's own carton: the front face "
        "states the net weight and the net volume. The `fill_weight` gate "
        "is CLOSED and both third-party figures carried at V7.49.4 are "
        "WITHDRAWN — the eBay figure was half the true fill and the Amazon "
        "figure was the mould's commonest charge, carried over by resellers "
        "who never read this box. Withdrawn rather than deleted, so that "
        "nobody re-derives either from a marketplace listing in six months "
        "(§34: errors are logged, not silently corrected). The useful "
        "consequence is commercial, not technical: the true fill is "
        "meaningfully larger than the number the marketplaces print, and "
        "that is a Tier 1 fact available to the offer act.",
    "pack_name_differs":
        "THE PACK AND THE WEBSITE DO NOT CALL THIS PRODUCT THE SAME THING. "
        "The carton reads COLOR CHANGING FOUNDATION STICK with a one-line "
        "descriptor about matching the wearer's own tone; the US store "
        "sells it as the Changing Foundation Stick. Neither is wrong and "
        "the difference is small, but it is a continuity decision and not a "
        "typo: a beat that shows the carton and a caption that uses the "
        "website name will read as two products to anyone looking closely, "
        "and the offer act is exactly where people look closely. DECLARE "
        "WHICH NAME THE BUILD USES AT THE ACT MAP and hold it. Where the "
        "carton is legible in frame, the pack name wins, because the viewer "
        "can read it.",
    "pack_is_white":
        "THE CARTON IS WHITE AND THE STICK IS VIOLET, and nothing in the "
        "retail packaging carries the barrel's colour. Measured off the "
        "photographed carton at L 98, a* -1.7, b* +3.7: a soft matte "
        "off-white, very slightly warm, not bright paper white and not "
        "cream. A generator handed 'FACELOVE packaging' reaches for the "
        "lilac every time, because the lilac is what every other image of "
        "this brand is full of, and it puts it on the box. It is wrong, and "
        "it is wrong in the one beat class where the pack is the hero. "
        "Stated positively in PACK_LOCK and negated in NEG_PACK, because "
        "neither alone holds. The one place the brand's lilac does appear "
        "on packaging is the outer mailer, and the inner pouch is a "
        "different lilac again — cooler and bluer than the barrel, and "
        "never a match for it.",
    "pack_type_is_post":
        "Everything printed on the carton is small, low-contrast and "
        "§17 territory: the product name block, the descriptor line, the "
        "net weight. It garbles in generation without exception and it is "
        "the part of the box a viewer actually reads. BLANK IT IN "
        "GENERATION AND SET IT IN POST. What is generated is the box, the "
        "board, the wordmark along the long face and the one line-drawn "
        "flourish; what is added afterwards is the type block. The "
        "flourish is worth naming separately because it is the carton's "
        "only ornament and a generator drops it as noise.",
    "sibling_cartons_are_identical":
        "The four other products in the same drop — the foundation brush, "
        "the mascara, and two eyeshadow sticks — arrive in the SAME carton "
        "family: same board, same white, same print style, same flourish, "
        "differing only in the small type block and in height. That is "
        "useful and dangerous in the same breath. Useful, because a bundle "
        "or what's-included beat has a real set to show and does not have "
        "to invent one. Dangerous, because a sibling carton in frame is "
        "indistinguishable from this product's carton at any distance where "
        "the type does not resolve, so a beat that means to show THIS "
        "product's box and shows a row of them has shown nothing. On any "
        "single-product pack beat, ONE CARTON IN FRAME.",
    "printed_copy_is_not_our_copy":
        "The brush carton's printed descriptor uses a word that is on this "
        "project's banned-vocabulary list in both channels. It is the "
        "advertiser's printed copy on a physical object and it is none of "
        "our business to change it — but it must never be transcribed into "
        "a script, a caption, a VO line or a prompt, and it is one more "
        "reason the carton type block is set in post rather than generated: "
        "generated type invents its own words, and a garbled version of "
        "that particular line is worse than a blank face.",
    "terrain_vs_copy":
        "THE ADVERTISER'S OWN COPY AND THE RENDER STANDARD DISAGREE, AND "
        "THE DISAGREEMENT IS NOT RESOLVED HERE. Both stores claim that the "
        "product instantly softens fine lines and that lines appear "
        "smoother with each application. TERRAIN_LOCK forbids rendering any "
        "such thing: the crease is exactly as deep in the final frame as in "
        "the first, and only colour changes. Under the Order of Authority a "
        "visual standard outranks the script, so the RENDER follows "
        "TERRAIN_LOCK and the LINE IS FLAGGED AND NOT REWRITTEN. Both "
        "claims are additionally Tier 3 in CLAIMS, so every beat carrying "
        "them is BLOCKED on that ground as well. What the build can show "
        "instead, honestly and on a Tier 2 claim, is the film NOT PLUGGING "
        "the crease — no opaque line of product sitting in the groove, the "
        "terrain reading as terrain and not as a filled trench. That is "
        "'does not settle into lines', it is the claim the product page "
        "makes second, and it is the one the camera can actually prove.",
    "twist_up_and_detachable_brush":
        "The balm end is a TWIST-UP mechanism and the brush is DETACHABLE. "
        "Both are stated repeatedly in marketplace copy for this exact "
        "product and for the mould it is made in ('Portable Twist-Up Tube', "
        "'Dual-Ended with Detachable Brush'). This settles what the object "
        "does; it changes nothing about what a beat may show. NEG_UNCAP's "
        "ban on twisting, winding, extending and clicking stands in full, "
        "because a travelling mechanism is among the least reliable things "
        "in the pipeline to generate and a half-extended balm is a product "
        "in a state the reference set has never seen. THE BALM IS ALWAYS "
        "ALREADY DEPLOYED AT THE STAND-OUT THE REFERENCE SHOWS. The one "
        "consequence that does bite: deployed height is a state on a "
        "twist-up, so DEPLOYED_ASPECT stays informational and ungated.",
    "colour_is_pigment_not_reaction":
        "The tone is three iron oxides already dispersed in the stick, "
        "masked by titanium dioxide, read through as the film thins under "
        "shear — see MECHANISM_PHYSICAL and the INCI. It is NOT a reaction, "
        "NOT a pH change, NOT capsules bursting, and NOT anything "
        "triggered by the skin. Reseller copy says capsules and says "
        "collagen; both are wrong about this product. The register already "
        "renders the correct behaviour, so this ruling changes no string — "
        "it makes the existing render defensible rather than decorative.",
    "ingredient_disclosure_conflict":
        "THE TWO STORES AND THE INCI DO NOT AGREE, AND THE INCI WINS. The "
        "US store's ingredient panel names hyaluronic acid and niacinamide; "
        "the EU store's names aloe vera and beeswax. NONE OF THE FOUR "
        "APPEARS ON THE PUBLISHED INCI. What the INCI does support is "
        "squalane, vitamin E as tocopheryl acetate, centella as "
        "madecassoside, ceramide NP and a heavy plant-oil and butter "
        "emollient load — all four of which are on one panel or the other "
        "and are therefore safe to name. Every one of the four unsupported "
        "actives is Tier 3 in CLAIMS and blocks its beat. Logged as a "
        "conflict, never silently corrected (§34), and it is the "
        "advertiser's to resolve — it may be a panel error, a reformulation "
        "or a stale INCI, and guessing which is not this sheet's job.",
    "review_count_conflict":
        "The US store's homepage shows a four-thousand-plus review count "
        "for this product while the brand's own Shop listing for the same "
        "product showed two ratings. Both are the advertiser's surfaces. "
        "Recorded as a discrepancy, not resolved; any beat or caption "
        "carrying a review count is BLOCKED until the advertiser states "
        "which number it stands behind. This is the CL-14 class of failure "
        "and it is cheap here and expensive at beat seventy.",
    "remeasure_2026_09":
        "The four canonical renders were re-measured on 2026-09-14 with a "
        "different segmentation — object separated from the warm ground on "
        "the b* channel rather than by RGB distance — and CLOSED_ASPECT "
        "came back 5.03 against the V7.47 pass's 4.75-4.82, with "
        "DEPLOYED_ASPECT likewise higher. The object did not change; where "
        "each pass took the barrel width did. BOTH FIGURES ARE KEPT and the "
        "bands cover both. What the new pass CONFIRMED unchanged, and these "
        "are the load-bearing ones: BALM_OVER_SLEEVE at 0.857 against a "
        "recorded 0.86, and CHAMFER_RISE at 0.252 against a recorded 0.25. "
        "The chisel geometry is the most stable thing on the object.",
    "single_wordmark":
        "There is ONE wordmark on the object, not one per end. The three "
        "single-unit renders place it at consistent distance from the same "
        "seam once the stick is flipped end for end, and its reading "
        "direction inverts between the balm-up and brush-up renders, which "
        "is what a single print on a flipped object does and what two "
        "prints would not do. Carried on the checklist as a ruling. "
        "Confirmed by: any render showing both barrel sections uncapped.",
    "wordmark_upright_to_balm":
        "The wordmark is upright to the BALM end: it reads upward from the "
        "base with the balm uppermost, and downward from the top with the "
        "brush uppermost. Settled by OCR on all three single-unit renders, "
        "which read correctly under opposite rotations for the two states.",
    "balm_crest_centred":
        "The balm's flat crest is CENTRED on the tip, its centre within a "
        "couple of pixels of the tip's own centre, and the two shoulders "
        "are of equal pitch. This is the one place on the object where the "
        "§8 expectation of a named asymmetry is NOT met, and saying so is "
        "load-bearing: an off-centre crest written into a prompt invents a "
        "feature the object does not have. One deployed render only.",
    "crown_apex_centred":
        "The brush crown's apex sits on the barrel's centreline in both "
        "renders that show it, within a couple of pixels. The apparent "
        "lopsidedness in the two-unit render is fibre splay and lighting, "
        "not a shaped tuft. This bears directly on open gate G9 and is "
        "offered as evidence toward it, NOT as its closure — the gate is "
        "the user's to close, and documentation errors are logged rather "
        "than silently corrected.",
    "highlight_side_is_lighting":
        "The soft broad highlight falls on the camera-left side of the "
        "barrel in every canonical render because every canonical render "
        "was lit from camera-left. THIS IS A PROPERTY OF THE REFERENCE "
        "SET, NOT OF THE OBJECT. Never write a highlight side into a "
        "prompt; the beat's Location Profile decides it (§22A).",
}

UNSETTLED = {
    "rear_and_rotated_elevation":
        "Nothing is known about the back of the barrel. All four canonical "
        "renders are frontal or near-frontal and all four show the same "
        "face. BLOCKS: any beat in which the stick turns, rolls in the "
        "hand, or the camera orbits it, because the generator will either "
        "wrap the wordmark round or invent a second one. UNBLOCKED BY: one "
        "render of the closed stick rotated a half turn, same lighting.",
    "cap_seating_geometry":
        "How the cap seats — friction push-fit, magnet, or click — is not "
        "visible in any render, and the closed stick shows two fine seams "
        "whose ownership is inferred rather than seen. BLOCKS: any beat "
        "showing the cap going back ON. UNCAPPING is safe because it only "
        "requires the cap to leave along the axis. UNBLOCKED BY: a render "
        "of the cap held clear of the barrel, both parts in frame.",
    "carton_rear_and_base":
        "Only the carton's front face has been photographed. What is "
        "printed on the back, the sides and the base — the INCI, a batch "
        "code, a barcode, an origin line, a period-after-opening mark — is "
        "unknown. BLOCKS: any beat that turns the carton, any beat that "
        "shows its back or base, and any hand-held pack beat where the box "
        "rotates. UNBLOCKED BY: photographs of the remaining faces. Until "
        "then, pack beats hold the front face square to camera and the box "
        "does not turn. This is the carton's version of the barrel's "
        "rear-elevation gate and it fails the same way — the generator will "
        "invent a printed back rather than leave one blank.",
    "actives_panel":
        "Four actives are claimed on the stores and absent from the INCI — "
        "see RULINGS['ingredient_disclosure_conflict']. BLOCKS: every "
        "ingredient beat and every VO line naming hyaluronic acid, "
        "niacinamide, aloe vera or beeswax. UNBLOCKED BY: a current INCI "
        "from the advertiser, or a decision to build the ingredient act on "
        "squalane, vitamin E, centella and ceramide only — which the "
        "published INCI already supports and which needs no new asset.",
    "line_softening_copy":
        "See RULINGS['terrain_vs_copy']. BLOCKS: every beat carrying the "
        "line-softening or lines-smoother-each-use claims. UNBLOCKED BY: "
        "the advertiser either supplying a source and accepting that the "
        "render will still not show a crease getting shallower, or "
        "replacing the line with the does-not-settle claim, which the "
        "register can prove.",
}

# brush_end_deployment was an open gate at V7.47 and is CLOSED at V7.49.4
# by RULINGS['twist_up_and_detachable_brush']: the brush is detachable and
# the balm end twists. The generation rule it produced is unchanged — the
# working end is always already deployed and never moves relative to its
# collar or sleeve on camera.
RESOLVED = {
    "brush_end_deployment": "closed 2026-09-14, see RULINGS["
                            "'twist_up_and_detachable_brush']",
    "fill_weight":          "closed 2026-09-14 by the retail carton, "
                            "see RULINGS['fill_weight_settled'] and FILL",
}

# ------------------------------------------ per-batch first-frame checks
CHECKLIST = [
    "barrel satin pale violet-mauve, not glossy, not chrome, not pink",
    "one soft broad highlight down the lit side, no hard mirror line",
    "balm warm-neutral white, never cooler in tone than the ground it sits on",
    "balm top cut back into two straight shoulders rising to a short flat "
    "crest — a low broad chisel, not a dome, not a cone, not a flat cylinder",
    "the crest centred on the tip, shoulders of equal pitch",
    "brush crown domed, broader than it is tall, standing proud of the collar",
    "brush crown apex on the barrel's centreline",
    "collar stepped and flaring, the fine machined slot present in its "
    "sloped face just below the rim",
    "ONE wordmark, on the front centreline, running along the barrel, "
    "upright to the balm end, never twice in frame",
    "the closed end capped and closed — never both ends open",
    "no second unit unless a sanctioned pair-pack beat",
    "TERRAIN CONSTANT: the crease exactly as deep after as before, pores "
    "open and individually resolved, relief intact",
    "colour resolves only behind the brush crown — white ahead of it, "
    "matched behind, nothing matched where the brush has not been",
    "the four dated surface failures absent: no bubbles or domes on the "
    "cream, no granular bead layer, no rounded bodies at the base of the "
    "film, no cool blue-white drift in the white",
    "no banned vocabulary rendered as a look: nothing glowing, radiant, "
    "luminous or flawless",
    "wordmark legible if it is in frame at all — otherwise blanked in "
    "generation and set in post",
    "ON PACK BEATS ONLY — the carton soft matte off-white, never lilac, "
    "never tinted, never glossy, never foiled",
    "ON PACK BEATS ONLY — the carton's fine line-drawn flourish present "
    "beneath the wordmark, and the product type block left blank",
    "ON PACK BEATS ONLY — one carton in frame unless the beat is a "
    "sanctioned pair-pack, and the front face square to camera",
]

# ------------------------------------------------- retired / never write
RETIRED_PHRASINGS = [
    # banned vocabulary, project-wide, in prompts and in negatives alike
    "glowing", "radiant", "luminous", "flawless",
    # scale figures of every kind: check_scale() refuses these outright
    "cm", "mm", "inch", "millimetre", "millimeter", "centimetre", "centimeter",
    "percent", "per cent", "fifths", "thirds", "quarters",
    "no wider than", "no taller than",
    # geometry retired by the V7.47 measurement pass
    "off-centre crest", "asymmetric crest", "crest offset",
    "wordmark on each end", "wordmark on both sections", "second wordmark",
    "highlight on the left of the barrel", "highlight camera-left",
    # mechanism wording retired with the claim
    "fills the lines", "fills in wrinkles", "plumps the crease",
    "smooths away lines", "erases wrinkles",
    # element tokens
    "<<<",
]

# clauses that are legal ONLY inside a named negatives string
NEG_ONLY = {
    "glowing":       ("NEG-LOOK",),
    "radiant":       ("NEG-LOOK",),
    "luminous":      ("NEG-LOOK",),
    "flawless":      ("NEG-LOOK",),
    "second wordmark": ("NEG-ORIENT",),
}

# tokens that make a string carry a scale figure. Digits are checked
# separately. This is check_scale() at sheet level.
SCALE_TOKENS = ("cm", "mm", "inch", "millimet", "centimet", "percent",
                "per cent", "fifths", "thirds", "quarters", "ratio")

# Short tokens must match as WORDS, or "immediately" reads as a millimetre
# and "machined" as an inch. Everything longer matches as a substring,
# which is what catches "wordmark on both sections" inside a sentence.
import re as _re


def _carries(low, needle):
    if len(needle) <= 6 or needle in SCALE_TOKENS:
        return _re.search(r"\b%s\b" % _re.escape(needle), low) is not None
    return needle in low


# --------------------------------------------------------------- checks
def _n(s):
    return len(s.replace("\n", ""))


def verify(verbose=False):
    """Self-test. Raises AssertionError on any drift."""
    fails = []

    # 1 no locked string carries a retired phrasing outside its carve-out
    for name, s in S.items():
        low = s.lower()
        for bad in RETIRED_PHRASINGS:
            if _carries(low, bad) and name not in NEG_ONLY.get(bad, ()):
                fails.append("%s carries retired phrasing: %r" % (name, bad))

    # 2 check_scale: no locked string carries a numeral or a scale token
    for name, s in S.items():
        low = s.lower()
        if any(ch.isdigit() for ch in s):
            fails.append("%s carries a digit — check_scale refuses it" % name)
        for tok in SCALE_TOKENS:
            if _carries(low, tok):
                fails.append("%s carries a scale token: %r" % (name, tok))

    # 3 contact is stated as contact, and coverage of the terrain guarded
    for name in ("CONTACT-LOCK", "CONTACT-LOCK-C"):
        low = S[name].lower()
        if "no daylight" not in low and "no gap" not in low:
            fails.append("%s does not state contact without a gap" % name)
        if "terrain is constant" not in low:
            fails.append("%s does not carry the terrain-constant rule" % name)

    # 4 the terrain rule survives independently of the contact block
    for frag in ("exactly as deep", "pores stay open", "colour and colour only"):
        if frag not in TERRAIN_LOCK.lower():
            fails.append("TERRAIN-LOCK missing: %s" % frag)

    # 5 orientation carries the single-wordmark ruling and the end state
    for name in ("ORIENT-LOCK", "ORIENT-C"):
        low = S[name].lower()
        if "once" not in low and "one wordmark only" not in low:
            fails.append("%s does not lock the wordmark to a single instance" % name)
        if "capped" not in low:
            fails.append("%s does not state the closed end is capped" % name)
    if "upright to the balm end" not in ORIENT_LOCK.lower():
        fails.append("ORIENT-LOCK does not fix the wordmark's reading direction")
    if "satin" not in ORIENT_LOCK.lower():
        fails.append("ORIENT-LOCK does not hold the finish against gloss drift")

    # 6 the negatives defend the terrain rule and the moving front
    for clause in ("no product filling the crease",
                   "no crease shallower after the product than before",
                   "no colour resolving ahead of the brush"):
        if clause not in NEG_CONTACT:
            fails.append("NEG-CONTACT missing: %s" % clause)

    # 7 the negatives defend the single wordmark and the capped end
    for clause in ("no second wordmark", "no both ends open at once",
                   "no gloss mirror finish on the barrel"):
        if clause not in NEG_ORIENT:
            fails.append("NEG-ORIENT missing: %s" % clause)

    # 8 the four dated failures are all present, none trimmed
    for clause in ("no bubbles on the cream", "no granular bead layer",
                   "no rounded bodies sitting at the base of the film",
                   "no cool blue-white cream"):
        if clause not in NEG_SURFACE_FAILURES:
            fails.append("NEG-SURFACE-FAILURES dropped a dated failure: %s" % clause)

    # 9 uncapping stays a reposition, never an assembly
    for clause in ("straight off along the barrel's own axis".upper(),
                   "no twisting", "no unscrewing"):
        pool = UNCAP_LOCK + " " + NEG_UNCAP
        if clause not in pool:
            fails.append("UNCAP missing: %s" % clause)

    # 10 held beats keep the hands off the working end
    for frag in ("never touch the balm crest", "never cross the wordmark"):
        if frag not in HOLD_LOCK:
            fails.append("HOLD-LOCK missing: %s" % frag)

    # 11 one mechanism claim, and it is the locked one
    if MECHANISM_CLAIM != "adaptation":
        fails.append("mechanism claim is not the locked one")
    if MECHANISM_REGISTER != "surface-layer":
        fails.append("mechanism register is not the locked one")

    # 12 the ratios are ordered pairs; the two colour axes may be signed
    for k, (lo, hi) in list(RATIOS.items()) + list(INFO_RATIOS.items()):
        if not lo < hi:
            fails.append("%s is not an ordered pair" % k)
    if RATIOS["BARREL_B_STAR"][1] >= 0:
        fails.append("BARREL_B_STAR must stay negative — the barrel is the cool element")
    if RATIOS["CREAM_B_STAR"][0] <= 0:
        fails.append("CREAM_B_STAR must stay positive — the cream never drifts cool")

    # 13 the checklist carries the load-bearing items
    joined = " ".join(CHECKLIST).lower()
    for frag in ("terrain constant", "one wordmark", "behind the brush crown",
                 "four dated surface failures"):
        if frag not in joined:
            fails.append("CHECKLIST missing: %s" % frag)

    # 14 nothing borrows a slot this product does not fill
    for name, s in S.items():
        for slot in NOT_APPLICABLE:
            if "[%s]" % slot in s:
                fails.append("%s uses inapplicable slot [%s]" % (name, slot))

    # 15 every claim carries a legal tier and a source
    for k, (t, src) in CLAIMS.items():
        if t not in (1, 2, 3):
            fails.append("CLAIMS[%s] has no legal tier" % k)
        if not src.strip():
            fails.append("CLAIMS[%s] has no source" % k)

    # 16 nothing another brand owns has leaked into a locked string
    for name, s in S.items():
        low = s.lower()
        for tok in NEVER_CLAIM:
            if _carries(low, tok.lower()):
                fails.append("%s carries another brand's claim: %r" % (name, tok))

    # 17 the absolute dimensions stay OUT of the prompt channel entirely.
    # They are numerals by definition, so the guard is that no locked
    # string contains one — already asserted at check 2 — plus that every
    # row is tiered and sourced, so nobody quotes one as a fact.
    for k, v in DIMS.items():
        if len(v) != 3 or v[1] not in (2, 3) or not str(v[2]).strip():
            fails.append("DIMS[%s] is not a tiered, sourced triple" % k)

    # 18 the INCI is present and carries the pigments the mechanism rests on
    for ci in ("CI 77891", "CI 77492", "CI 77491", "CI 77499"):
        if ci not in INCI:
            fails.append("INCI is missing %s — the mechanism loses its evidence" % ci)
    for frag in ("Nothing reacts", "was in the stick"):
        if frag not in MECHANISM_PHYSICAL:
            fails.append("MECHANISM_PHYSICAL missing: %s" % frag)

    # 19 the three blocking gates opened at V7.49.4 are still declared
    for g in ("actives_panel", "line_softening_copy"):
        if g not in UNSETTLED:
            fails.append("UNSETTLED lost a blocking gate: %s" % g)
    if "terrain_vs_copy" not in RULINGS:
        fails.append("the terrain-versus-copy collision has been dropped")

    # 20 the packaging strings hold the one thing that fails every time
    for name in ("PACK-LOCK", "PACK-LOCK-C"):
        if "the box is white and the stick is violet" not in S[name].lower():
            fails.append("%s does not hold the white-carton rule" % name)
    for clause in ("no lilac carton", "no violet box", "no numerals"):
        if clause not in NEG_PACK:
            fails.append("NEG-PACK missing: %s" % clause)
    for g in ("carton_rear_and_base",):
        if g not in UNSETTLED:
            fails.append("UNSETTLED lost the carton gate: %s" % g)
    if "fill_weight" in UNSETTLED or "fill_weight" not in RESOLVED:
        fails.append("the fill-weight gate is not recorded as closed")
    if FILL["net_weight_g"][1] != 1:
        fails.append("the fill weight must be Tier 1 — it is on the carton")

    if fails:
        raise AssertionError("product sheet self-test failed:\n  " + "\n  ".join(fails))
    if verbose:
        print("self-test passed: %d strings, %d checklist items, %d gated ratios"
              % (len(S), len(CHECKLIST), len(RATIOS)))
    return True


def counts():
    return {k: _n(v) for k, v in sorted(S.items())}


# ==================================================================
# PROSE SHEET  (emit with --md)
# ==================================================================
SHEET_MD = r'''# Product Sheet — FACELOVE Changing Foundation Stick

**V7.49.4.** This is the prose half of `facelove_product_sheet.py`, embedded in it and emitted with `--md`. It carries the spec, the phrasing table, the claim register and the reference registry; the module around it carries the slots, the locked strings, the measured ratios and the assertions. **Never retype a string into a prompt — import it.**

> **Read sections 10 and 11 first.** The V7.49.4 source pass found more in the advertiser's copy than in the object's geometry, and two of the findings block beats. The advertiser's own page claims that fine lines are softened and that they look smoother with every application; the render standard forbids showing a crease get shallower. And four of the actives named on the two stores' ingredient panels do not appear on the published INCI. Neither is resolved here. Both are surfaced, tiered and blocked, which is what §43A asks for and what costs nothing now and costs a corpus at beat seventy.

Every geometry figure below was measured off the canonical renders, not read off the prose: each row segmented against its own background, the white tip split from the violet barrel on the blue-minus-green channel, features normalised to the adjacent barrel width, and the wordmark's reading direction settled by OCR under both rotations. **Every figure is Tier 3 craft input and none of them enters a prompt** — the compiler's `check_scale()` refuses numeric figures in prompt text, and `verify()` enforces the same rule over the locked strings.

---

## 1. Product name and category

FACELOVE Changing Foundation Stick — a dual-ended cosmetic stick. One end is a solid white cream foundation balm; the other is an integrated blending brush. The balm goes on white and resolves to the wearer's own tone as the brush works it.

**Register note.** The buyer is a mature woman with established skin terrain — deep creases, visible pores, age features. That makes the terrain-constant rule (below) commercially load-bearing rather than merely honest: an ad that shows the lines disappearing is selling a different product, and the viewer knows it.

---

## 2. The eight spec fields (§8)

**1 — Primary form.** A slim straight cylinder, several times taller than it is wide, closed at both ends by caps and carrying one wordmark along its length. Uncapped at one end it presents a solid white balm cut back to a short flat crest; uncapped at the other, a domed brush crown standing proud of a stepped collar.

**2 — Material and finish.** Barrel: pale violet-mauve metal with a **satin** anodised look — softly reflective, holding one broad diffuse highlight down the lit side and falling gradually to a cool shadow edge. Never gloss, never chrome, never a hard mirror line. Balm: solid, matte-waxy, **warm-neutral white**. Brush: dense white synthetic fibre, very slightly warmer than the balm, matte, no sheen. Collar: same satin finish as the barrel, with one fine machined slot as its only cut detail.

**3 — Distinguishing asymmetries.** *The most important field — and on this object the most important entry is a place where there is no asymmetry.*

- The balm's top is **cut back into two straight shoulders rising to a short flat crest** — a low broad chisel in silhouette. Measured chamfer rise about a quarter of the tip's width; measured flat crest under a tenth of it. Not a dome, not a cone, not a flat cylinder, and a generator will return all three.
- **The crest is centred and the shoulders are of equal pitch.** Measured, and stated deliberately: writing an off-centre crest invents a feature the object does not have.
- **The brush crown's apex is on the centreline** in both renders that show it. The lopsidedness visible in the two-unit render is fibre splay and lighting.
- **One wordmark, not two.** Set along the barrel on its front centreline, upright to the balm end, on the section immediately below the working end.
- **The collar slot** — a fine machined horizontal slot in the collar's sloped face just below the rim, about two fifths of the collar's width. It is the only hard-edged cut on an otherwise smooth object and it is normalised away every time unless named.
- **The highlight side is not a property of the object.** It falls camera-left in every canonical render because every canonical render was lit camera-left. The beat's Location Profile decides it (§22A).

**4 — Scale reference.** *Stated relationally in every string, because every figure here is Tier 3 and `check_scale()` refuses numerals in prompt text.*

- Closed, the stick is several times taller than it is wide — measured between four and a half and five barrel widths.
- The balm tip is a little narrower than the sleeve it stands on; the brush crown a little narrower than the barrel and **broader than it is tall**.
- The wordmark block runs a little longer than the barrel is wide, at a cap height around a sixth of the barrel's width.
- Deployed height is a **state, not a property** — how far the working end stands proud is reported and never gated.

**5 — Secondary components.** Two caps, one per end; the non-working end is capped in every beat. A stepped collar at the brush end, flaring outward to the barrel. A raised sleeve at the balm end. No hardware, no closures, no straps.

**6 — Interface mechanism.** *Corrected at V7.49.4 — what the object does is now known, and what a beat may show is unchanged.*

The cap draws **straight off along the barrel's axis**. The balm end is a **twist-up** and the brush is **detachable**; both are stated repeatedly in marketplace copy for this product and for the mould it is made in. That settles the object. It does not open the mechanism to camera: `NEG_UNCAP`'s ban on twisting, winding, extending and clicking **stands in full**, because a travelling mechanism is among the least reliable things in the pipeline to generate and a half-extended balm is a state the reference set has never seen. **The working end is always already deployed, at the stand-out the reference shows, and it never moves relative to its sleeve or collar on camera.** Product state never changes; only the cap's position does (§9B logic, with the cap as the moving part).

The one consequence that bites: on a twist-up, **how far the balm stands proud is a state, not a property**. `DEPLOYED_ASPECT` therefore stays informational and ungated, and the spread between the two measurement passes is not a defect.

**7 — Placement lock — replaced by a contact lock.** This product is **held and applied**, never worn, so §9A-P's placement parts do not apply and `PLACE-LOCK`, `ORIENT` band clauses and `IFACE` blocks must never be borrowed from a worn-product sheet. What replaces them is `CONTACT_LOCK`: the balm meets the skin on its **flat crest and leading shoulder** with the skin giving slightly under it and no gap anywhere; the brush meets it on the **side of its crown**, fibres bending back and springing clear; the barrel and collar never touch the face. Contact is stated as contact, never as a measured offset — the same rule that governs a worn product's height.

**8 — Standing negatives.** `NEG-CONTACT`, `NEG-ORIENT`, `NEG-UNCAP`, `NEG-SURFACE-FAILURES`, `NEG-LOOK` in the `.py`. `NEG-SURFACE-FAILURES` carries the four dated observed failures of 2026-08-14 and is **never trimmed from any beat showing the cream at scale**.

---

## 3. Phrasing table

| Intent | Phrasing that failed, and what it produced | Phrasing that works |
|---|---|---|
| Shape the balm top | "a rounded balm tip" / "a bullet tip" | Cut back into two straight shoulders rising to a short flat crest — a low broad chisel |
| Show the benefit | "smooths away the lines" / "fills the creases" | The film evens colour across crest and crease alike while every feature of the terrain stays exactly where it was |
| Show absorption | "the cream soaks in" — rendered a granular bead layer reading as polystyrene foam | The dry band drinks the emollient, the plates lie flat, the milky scatter clears to translucency |
| Keep the cream white | left unstated — drifted cool blue-white against a warm ground | Warm-neutral white, never cooler in tone than the ground it sits on |
| Time the colour change | "the colour matches her skin" — rendered a fully matched patch with no brush in it | Colour resolves from inside the cream's thickness at the shear front, white ahead of the brush crown and matched behind |
| Describe the finish | "glowing" / "radiant" / "luminous" | Banned outright, both channels. Describe the surface, not the effect |
| State the size | any figure at all | Relational only — "a little narrower than", "broader than it is tall". `check_scale()` refuses the rest |
| Place the wordmark | "the FACELOVE wordmark on the barrel" — rendered twice, once per section | One wordmark and once only, on the front centreline below the working end |

---

## 4. Reference image registry

**Canonical set — attachable:** the closed stick on white; the balm end deployed on beige; the brush end deployed on beige. Attach one to every product-facing generation call alongside `REF-PROD` in prose. Image plus names is the pair; either alone leaks.

**The canonical set is not replaced, ever, by anything generated.** These are the advertiser's own renders, they are internally consistent, and every beat already delivered was built against them. Generating a prettier set and swapping it in invalidates the corpus (§5: competing reference sets are a drift source). New reference images **add views the set does not carry**; they never stand in for views it does.

**There is no single attachable image that carries everything, and asking for one runs into the sheet's own rules.** `ORIENT_LOCK` forbids both ends open in one frame, so no single-unit frame can show the balm and the brush deployed together; and §5 forbids attaching a multi-instance frame, so a composite that shows both is documentation rather than a reference. The honest form of "one image for everything" is therefore **one composite sheet that a human and the checker read, and a small attachable set that the models read.** Both are specified in `REF_WANTED`.

**Wanted, and why:**

| Asset | Attachable | Closes |
|---|---|---|
| `REF-REAR-01` — the closed stick rotated a half turn, same ground, same light | **Yes** | `rear_and_rotated_elevation`. Unblocks every beat where the stick turns, rolls in the hand, or the camera orbits it — today the generator either wraps the wordmark round the barrel or invents a second one, and no negative reliably stops either |
| `REF-SHEET-01` — five views on one neutral ground: closed front, closed rear, balm deployed, brush deployed, both working ends from directly above | **No — never attach** | Nothing on its own. It is the human and `--check` artefact: the one picture that carries the whole object, the crest geometry from above, the crown splay from above, and the rear elevation, in a form a person can hold against a frame |
| `REF-CAP-01` — the cap held clear of the barrel, both parts in frame | **Yes** | `cap_seating_geometry`. Low priority: uncapping already generates, because the cap only has to leave along the axis. Capping stays banned with or without it |

**Never attach as reference:** the two-unit render showing both ends deployed side by side. It is a multi-instance shot (§5) and attaching it is the fastest route to two sticks in a frame that should hold one. It stays a cut-in for the edit.

**Model routing (§4, §44 default 19).** Any beat carrying a readable wordmark routes to the Pro model; volume beats carrying no critical type route to the fast sibling. **Read the logged model on every completed job** (§5, §44 default 47) — the string passed is not evidence of the model run. Where the wordmark would render small, blank it in generation and set it in post (§17).

**Per-batch first-frame check:** the sixteen-item `CHECKLIST`. The measurable half runs as a script — `--check`. The rest stays an eyeball: satin versus gloss, fibre quality, wordmark legibility, the terrain-constant rule, and the colour front sitting behind the brush crown.

---

## 5. Mechanism register and slots

**Register: the locked surface-layer register (§12A-4)** — an anatomical-family register at skin-surface scale. A volumetric skin body on a warm blush-beige ground, translucent depth read **through** the material rather than via a cut section, brand violet as the cool channel. No bone, no muscle, no section plane.

Slots, filled at that scale so the §12A blocks substitute without rewording: `[REGION]` a band of mature facial skin from crest to crease · `[STACK]` the dry surface plates and the band between them · `[BONES]` the warm body zone below, read through as depth · `[TARGET]` the film lying across crest and crease · `[TARGET_JOINT]` the shear front travelling behind the brush crown · `[SITE]` the crease floor and the plate gaps either side of it.

**`[SITE]` is not the crest.** The crest is the obvious place for a generator to put the event, and it is the wrong one: the argument is that the film lies at equal thickness in the crease *and* on the crest, so the beat that only lights the crest is not making the claim. Name the crest as the exclusion in the negatives on every modulation beat.

**Material behaviour, locked.** The villain material is **non-wetting**: it stands proud on the crests, collects as an opaque plug in the creases, dries and cracks. The hero **wets**: it spreads, thins, and is drawn into the plate gaps by capillary action. Absorption is rendered as **scatter to transmission** — dry plate edges scatter light and read milky; the emollient fills the gaps, the plates lie flat, the band clears from milky to translucent, and warm light from the body zone passes through.

**Slots this product does not fill:** `[BAND-MATERIAL]`, `[HARDWARE]`, `[BAND-INNER]`, `[OFFSET]`. Named so nobody borrows a string that needs them.

---

## 6. Mechanism claim

**Adaptation.** One per build. Coverage is the competing explanation of the same object and it stays in the library for a build pitched on the other claim. The two must not run together: a build that argues both shows the viewer two mechanisms and weakens each.

**The colour change travels behind the brush crown as a moving front.** Nothing resolves until the brush touches it — white ahead, matched behind. This is the single most reissued failure on the product and it is in the negatives as well as the positives.

---

## 7. Competitor archetypes (§10)

Degraded near-copies of the same silhouette, never different products. One signifier per archetype, never repeated across a build: a domed or bullet tip where the hero has a chisel crest · glossy plastic where the hero is satin · a loose sparse brush where the hero is dense · a visible seam or moulding line · a thicker, dumpier barrel · a screw mechanism where the hero has none. Blank barrels, **no wordmark ever**, and no real third-party brand wordmark in any generated frame regardless of what the voiceover says.

Villain product beats sit on a real domestic surface per §15A — never seamless, never a storefront (§10A).

---

## 8. Buyer age band and cast profile

Mature women with established skin terrain. Cast to the buyer, not the aspirational version of her: deep creases, visible pores, age features named per character in `[AGE-FEATURES]` (§19, §22S). The §22S realism stack is mandatory on every beat with a face — and on this product it is the proof, not the polish.

---

## 9. Claim register (§43A)

| Claim | Tier | Status |
|---|---|---|
| The balm goes on white and resolves to the wearer's tone | 1 | Observable and demonstrable on camera. The build's core claim |
| The film lies at equal thickness in crease and on crest | 1 | Demonstrable in the mechanism register |
| Every absolute dimension and ratio on this sheet | 3 | Craft input only. Never spoken, never captioned, never in prompt text |
| The three surgery-line voiceover claims (gate D32) | 3 | **Blocked** pending an advertiser or counsel decision. Carried verbatim into prompts and flagged, never silently rewritten |
| Social proof figure (gate CL-14) | 3 | **Blocked** — the figure differs between sources. Two builds held |
| Offer construction: BOGO, free primer, mystery gift | — | **Unconfirmed.** None verified on the product page. Dependent beats blocked |

**Standing to raise this is part of the role.** A Tier-3 claim in a finished corpus costs the corpus; caught at the act map it costs nothing.

---

## 10. Standing open items

**One asset unblocks the turning beats: a render of the closed stick rotated a half turn**, same lighting, so the back of the barrel is known. Until it lands, any beat in which the stick turns, rolls in the hand, or the camera orbits it will either wrap the wordmark around the barrel or invent a second one, and no negative reliably prevents either.

**A second asset unblocks the cap: the cap held clear of the barrel, both parts in frame.** Uncapping is safe without it — the cap only has to leave along the axis — but capping is not, and no beat may show the cap going back on.

**Gate G9 (tuft asymmetry) is not closed here.** The measurement pass contributes evidence toward it — the crown apex is centred within a couple of pixels in both renders that show it, and the apparent lopsidedness is splay and lighting — and that evidence is recorded as a ruling. Closing the gate, and deciding whether delivered beats are reissued for it, remains the user's call.

---

## 9. Absolute dimensions *(new at V7.49.4 — and none of it enters a prompt)*

The advertiser publishes no dimension and no fill weight on either store. Everything below is a third-party marketplace listing or is derived from one, so the block is **Tier 2 at best** and the derived rows are Tier 3. It is in the sheet for three jobs and no others: to let a writer size a hand and a face correctly in a beat they are imagining, to let a person argue that a render is the wrong scale instead of merely feeling it, and to give the ratios an anchor in millimetres. `check_scale()` refuses numerals in prompt text and `verify()` enforces it over every locked string.

| | Figure | Tier | Source |
|---|---|---|---|
| Retail carton | ~148 × 26.5 × 25 mm | 2 | two Amazon listings, 5.83–5.91 × 1.02–1.06 × 0.98 in |
| Gross weight, product plus carton | ~41 g | 2 | Amazon, 1.45 oz |
| Closed stick | ~127 mm tall | 2 | Amazon, "Product Dimensions 1 × 1 × 5 inches" |
| Barrel | ~25 mm across | 3 | derived: stick height ÷ `CLOSED_ASPECT` |
| Upper sleeve, balm end | ~20 mm | 3 | derived, 0.81 of the barrel |
| Collar, brush end | ~22 mm | 3 | derived, 0.86 of the barrel |
| Balm, exposed | ~17.5 mm wide × ~5 mm proud | 3 | derived from `BALM_OVER_SLEEVE` and `BALM_EXPOSED_ASPECT` |
| Brush crown | ~19 mm wide × ~12 mm tall | 3 | derived from `CROWN_OVER_BARREL` and `CROWN_ASPECT` |
| Wordmark block | ~30 mm long, cap height ~4.4 mm | 3 | derived from the wordmark ratios |

**Fill weight is settled at V7.49.5 and it is Tier 1.** The advertiser's own retail carton states the net weight and the net volume on its front face. Both figures carried at V7.49.4 are **withdrawn**: the eBay listing's was about half the true fill, and the Amazon titles' was the mould's commonest charge, carried over by resellers who never read the box. They are withdrawn rather than deleted so nobody re-derives them from a marketplace listing in six months (§34: errors are logged, not silently corrected).

**The consequence is commercial rather than technical.** The true fill is meaningfully larger than the number every marketplace prints, and it is the advertiser's own Tier 1 fact. That belongs in the offer act.

**The only form of this block that should ever reach a prompt is the sentence, not the number:** it sits in the hand like a fat marker pen — a shade over five inches closed, about as thick as a thumb, and light. The deployed balm stands proud by about the width of a pencil lead's worth of height and is nearly as wide as the sleeve under it. That is the bit that keeps a generator from rendering a lipstick.

---

## 10. Claim register *(§43A — the most important section on this sheet)*

Every claim found on the advertiser's two stores, tiered. Tier 1 is stated as fact. Tier 2 is stated **and the qualification goes in the editor note — the line is not altered.** Tier 3 **blocks its beat** until the advertiser rules; the line is not rewritten and not cut (§27B: `CUT` is withdrawn, `BLOCKED` replaces it).

**Tier 1 — sourced, stated as fact.** Thirty-nine dollars from fifty-nine · thirty-day money-back guarantee · free US shipping · dual-ended with an integrated brush · it goes on white · one shade, single variant on both stores · the ingredients as published on the EU store's INCI.

**Tier 2 — real but qualified. Flag in the editor note; do not alter the line.**

| Claim | The qualification |
|---|---|
| Adapts to your skin tone | True of the material — see section 11 — but *perfectly* and *always the perfect tone* overstate a single-shade product. The honest form is that it meets a wide middle band |
| No orange, grey or yellow tint | A formulation intention, not a measured result |
| **Does not settle into wrinkles or pores** | **Renderable, consistent with `TERRAIN_LOCK`, and the claim to build on.** The film not plugging the crease is a thing the camera can actually show |
| Cruelty-free | A badge with no certifier named |
| Suitable for sensitive skin | Asserted; no panel test cited |
| Buildable coverage | Ordinary of the format |
| Four-thousand-plus reviews | The site widget. See the review-count conflict below |

**Tier 3 — `BLOCKED`. No source held. Do not build against these.**

Fifty thousand women over forty · lasts up to twelve hours, tested on mature skin · no colour change by midday · thousands of mature skin tones analysed in development · **instantly softens fine lines** · **fine lines appear smoother with each application** · anti-aging · covers dark spots · **hyaluronic acid · niacinamide · aloe vera · beeswax**.

### 10a. The collision, stated once and not resolved

**The advertiser's own copy and the render standard disagree.** Both stores claim the product softens fine lines and that lines look smoother with every application. `TERRAIN_LOCK` forbids rendering any such thing: the crease is exactly as deep in the final frame as in the first, and **only colour changes**.

Under the Order of Authority a locked visual standard outranks the script, so **the render follows `TERRAIN_LOCK` and the line is flagged, not rewritten.** Both claims are additionally Tier 3, so every beat carrying them is blocked on that ground as well.

This is not pedantry and it is not squeamishness. The buyer is a woman with established terrain who has been sold disappearing wrinkles before and did not get them. An ad that shows the lines going is selling a product she will not receive, and she knows it on sight — which is why the terrain rule was commercially load-bearing before it was ever a compliance question. **What the build can show instead, honestly, on a Tier 2 claim the page itself makes second, is the film not plugging the crease**: no opaque line of product sitting in the groove, the terrain reading as terrain rather than as a filled trench. That is provable on camera and it is the stronger beat.

### 10b. The two source conflicts, logged and not corrected

**The ingredient panels and the INCI do not agree, and the INCI wins.** The US store's panel names hyaluronic acid and niacinamide; the EU store's names aloe vera and beeswax. **None of the four appears on the published INCI.** What the INCI does support — and all of it appears on one panel or the other, so all of it is safe to name — is squalane, vitamin E as tocopheryl acetate, centella as madecassoside, ceramide NP, and a heavy plant-oil and butter emollient load. It may be a panel error, a reformulation, or a stale INCI; guessing which is not this sheet's job. **An ingredient act built on squalane, vitamin E, centella and ceramide needs no new asset and is defensible today.**

**The review counts disagree between two of the advertiser's own surfaces.** The US homepage shows a four-thousand-plus count for this product; the brand's own Shop listing for the same product showed two ratings. Both are theirs. Any beat or caption carrying a review count is `BLOCKED` until the advertiser says which number it stands behind.

### 10c. Claims that belong to other brands and must never enter a script

Marketplace copy for this exact product repeatedly attaches claims from the Korean mould's other tenants. None is a FACELOVE claim: **SPF 50+** (no filter on the INCI) · **Volufiline** · **collagen** · **colour-changing capsules** — a reseller's invented mechanism, and section 11 is what actually happens · **waterproof** · **sweat-proof** · **full coverage** — the advertiser says buildable and lightweight, which is the other end of the same axis · **Korean** — true of the mould and the category, never said by the advertiser about this product, and adding it is a sourcing claim nobody authorised.

---

## 11. What the colour change actually is *(new at V7.49.4)*

The published INCI, verbatim and in order:

> Squalane, Diisostearyl Malate, CI 77891, Limnanthes Alba (Meadowfoam) Seed Oil, Simmondsia Chinensis (Jojoba) Seed Oil, Butyrospermum Parkii (Shea) Butter, Euphorbia Cerifera (Candelilla) Wax, Copernicia Cerifera (Carnauba) Wax, Tocopheryl Acetate, Phytosteryl Oleate, Madecassoside, Ceramide NP, CI 77492, CI 77491, CI 77499.

Read as a mechanism: **CI 77891** is titanium dioxide — the white, and the hiding power. **CI 77492, 77491 and 77499** are yellow, red and black iron oxide — the tone. **Diisostearyl malate** is the ester the pigment is dispersed in; **candelilla and carnauba** are what make it a stick rather than a cream; squalane, jojoba, meadowfoam and shea are the emollient load.

**The colour is already in the stick.** It is not made on the skin, nothing reacts, nothing is triggered and there are no capsules. Three iron oxides sit at low load in a matrix the titanium dioxide renders opaque white; thinning the film under the brush drops the white's hiding power and the oxides read through. **The tone resolves from inside the film's own thickness at the shear front** — white ahead of the brush crown, matched behind.

That is precisely what the surface-layer register already renders, which is the point of putting it here: **the render stops being a metaphor and becomes a description of the material.** It also draws the line on how to say it. *Adapts, meets your tone, matches as you blend* — fine. *Reacts, activates, triggers, capsules burst, senses your skin* — never, in copy or in a prompt, because none of it is true and the INCI is public.

---

## 12. Buyer and cast

Core band: **women from the late forties to the seventies**, with the centre of gravity in the fifties and sixties. The advertiser's own testimonial cast runs 38, 42, 52 and 67, and the page's whole pitch — *made for mature skin*, *over 40* — sits there. Cast to that band and to established terrain, not to the aspirational edge of it. The product's single shade, and the single-shade claim's Tier 2 qualification, argue for showing it on **more than one skin tone across the build** rather than on one: a single-shade product shown on a single face is making the narrower claim look like the wider one.

---

## 14. Packaging *(new at V7.49.5 — the first Tier 1 physical evidence on this sheet)*

Read off photographs of a delivered order. Not described by a reseller, not inferred from a render: photographed.

### 14a. The one rule

> **The carton is white and the stick is violet.**

Nothing in the retail packaging carries the barrel's colour. Measured off the photographed carton at **L 98, a\* −1.7, b\* +3.7** — a soft matte off-white, very slightly warm, not bright paper white and not cream. A generator handed "FACELOVE packaging" reaches for the lilac every time, because the lilac is what every other image of this brand is full of, and it puts it on the box. It is wrong, and it is wrong in **the one beat class where the pack is the hero**. `PACK_LOCK` states it positively and `NEG_PACK` negates it, because neither alone holds.

The one place the brand's lilac *does* appear on packaging is the **outer mailer**. The **inner pouch** is a different lilac again — cooler and bluer than the barrel, measured L 93, a\* −0.2, b\* −7.2, and never a match for it.

### 14b. The three layers

| | What it is |
|---|---|
| **Mailer** | A white bubble-lined poly envelope, soft and padded, the bubble grid clearly readable through the face, welded along a top edge with a fine sawtooth texture. One large letterspaced FACELOVE across the upper face in pale lilac-mauve |
| **Pouch** | A flat frosted zip pouch, slide-sealed with a small black slider, translucent enough that the cartons read through it as soft shapes. FACELOVE in black across the face, larger than anything on the cartons, with a short tagline beneath it |
| **Carton** | A tall slim rectangular box in soft matte off-white, several times taller than wide and only a little deeper than wide, flat faced with crisp square edges. Uncoated matte board — no gloss, no varnish, no foil, no metallic, no emboss. Pale grey-silver print, low contrast and small throughout: a letterspaced FACELOVE reading upward along one long face, and beneath it one fine line-drawn flourish in a single continuous hairline |

### 14c. The type block is post, and the flourish is not

Everything printed on the carton is small, low-contrast and **§17 territory**: the product name block, the descriptor line, the net weight. It garbles in generation without exception and it is the part of the box a viewer actually reads. **Blank it in generation and set it in post.**

What *is* generated is the box, the board, the wordmark along the long face, and **the flourish** — which is worth naming separately because it is the carton's only ornament and a generator drops it as noise.

### 14d. The pack name is not the website name

The carton reads **COLOR CHANGING FOUNDATION STICK**, with a one-line descriptor about matching the wearer's own tone. The US store sells it as the **Changing Foundation Stick**. Neither is wrong and the difference is small, but it is a continuity decision rather than a typo: a beat that shows the carton under a caption using the website name reads as two products to anyone looking closely, and the offer act is exactly where people look closely.

**Declare which name the build uses at the act map and hold it.** Where the carton is legible in frame, the pack name wins — the viewer can read it.

### 14e. The siblings are the same box

The four other products in the same drop — the foundation brush, the mascara and two eyeshadow sticks — arrive in the **same carton family**: same board, same white, same print style, same flourish, differing only in the small type block and in height.

Useful, because a bundle or what's-included beat has a real set to show instead of an invented one. Dangerous, because a sibling carton is indistinguishable from this product's carton at any distance where the type does not resolve — so a beat that means to show *this* product's box and shows a row of them has shown nothing. **On any single-product pack beat: one carton in frame, front face square to camera.**

### 14f. What is still unknown

**Only the front face has been photographed.** What is printed on the back, the sides and the base — the INCI, a batch code, a barcode, an origin line, a period-after-opening mark — is unknown, and `carton_rear_and_base` is open. **Pack beats hold the front face square to camera and the box does not turn.** It is the carton's version of the barrel's rear-elevation gate and it fails the same way: the generator invents a printed back rather than leaving one blank.

One more note, and it is about copy rather than geometry. **A word printed on a sibling carton is on this project's banned-vocabulary list in both channels.** It is the advertiser's printed copy on a physical object and it is not ours to change — but it must never be transcribed into a script, a caption, a VO line or a prompt. It is one more reason the type block is set in post: generated type invents its own words, and a garbled version of that particular line is worse than a blank face.

---

## 15. Strings added at V7.49.5

`PACK-LOCK` and `PACK-LOCK-C` — the retail carton, full and compressed. `UNBOX-LOCK` — the mailer and the pouch, for unboxing beats. `NEG-PACK` — merges into the negatives of every pack beat.

Until now the sheet had **no string for the carton at all**, so every offer, guarantee, unboxing and what's-included beat was being written freehand. That is the exact drift path §8 exists to close, and it was open on the beat class where the pack is the hero.

---

## 16. Standing session state

**Open gates, blocking:** `rear_and_rotated_elevation` · `cap_seating_geometry` · `carton_rear_and_base` · `actives_panel` · `line_softening_copy`.

**Closed:** `brush_end_deployment` at V7.49.4, by the twist-up and detachable-brush ruling. `fill_weight` at V7.49.5, by the retail carton.

**Rulings at V7.49.4:** the terrain-versus-copy collision · the twist-up and detachable brush · colour is pigment, not a reaction · the ingredient disclosure conflict · the review count conflict · the September re-measurement, which kept both passes' figures and confirmed the chisel geometry unchanged.

**Rulings at V7.49.5:** the fill weight settled and both marketplace figures withdrawn · the pack name differing from the website name · the carton being white while the stick is violet · the carton type block being post and the flourish not · the sibling cartons being identical at any distance the type does not resolve · printed pack copy never being transcribed into ours.
'''


# ==================================================================
# GEOMETRY AND COLOUR CHECKER
# ==================================================================
# Thresholds come from RATIOS above — nothing below hardcodes a number
# that governs a verdict. numpy and cv2 are imported lazily, so the sheet
# imports cleanly for prompt work on a machine that has neither.

import sys, os, glob

REFS = "/mnt/project/*.jp*g"

# Never scored and never attached: the two-unit render. It is a
# multi-instance shot (§5) and the one-wordmark gate would read its two
# wordmarks as a duplicated print on one object, which is a true verdict
# about a frame that should never have been in the batch.
EXCLUDE_REFS = ("BRUSH_AND_FOUNDATION",)

np = None
cv2 = None


def _lazy():
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


def _rowmask(im):
    """Per-row background subtraction. The product is a narrow vertical
    object on a plain ground, so each row carries its own background sample
    in its outer margins — which survives a gradient ground that a single
    global background model does not."""
    lab = cv2.cvtColor(im, cv2.COLOR_BGR2LAB).astype(np.float32)
    H, W, _ = im.shape
    m = np.zeros((H, W), np.uint8)
    pad = max(40, W // 14)
    for y in range(H):
        bg = np.concatenate([lab[y, pad:pad * 3], lab[y, W - pad * 3:W - pad]], 0).mean(0)
        m[y] = (np.linalg.norm(lab[y] - bg, axis=1) > 12)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    n, lab2, st, _ = cv2.connectedComponentsWithStats(m, 8)
    if n < 2:
        return None, 0
    areas = st[1:, cv2.CC_STAT_AREA]
    k = 1 + int(np.argmax(areas))
    big = float(areas.max())
    if big < 0.01 * H * W:
        return None, 0
    # §9 one instance per beat. Keeping only the largest component would
    # measure one of two sticks and report a clean pass on a frame holding
    # two, so the count is carried out of here rather than thrown away.
    units = int((areas > 0.35 * big).sum())
    return (lab2 == k).astype(np.uint8), units


def _spans(mask):
    out = {}
    for y in range(mask.shape[0]):
        x = np.nonzero(mask[y])[0]
        if len(x):
            out[y] = (int(x.min()), int(x.max()))
    return out


def _labstats(im, ys, xs):
    lab = cv2.cvtColor(im, cv2.COLOR_BGR2LAB).astype(np.float32)
    p = lab[ys, xs]
    return float(p[:, 0].mean()), float(p[:, 1].mean() - 128), float(p[:, 2].mean() - 128)


def measure(path):
    """Return a dict of scale-free measurements, or {'error': ...}."""
    _lazy()
    im = cv2.imread(path)
    if im is None:
        return {"error": "unreadable"}
    mask, units = _rowmask(im)
    if mask is None:
        return {"error": "not a clean product-on-plain-ground frame — measure by eye"}
    sp = _spans(mask)
    if len(sp) < 100:
        return {"error": "product too small to measure"}

    b = im[:, :, 0].astype(np.int16)
    g = im[:, :, 1].astype(np.int16)
    ys = sorted(sp)
    ytop, ybot = ys[0], ys[-1]

    # violet rows: the barrel reads clearly blue-over-green; the white tip
    # and the cast reflection do not.
    violet = []
    for y in ys:
        a, z = sp[y]
        xs = np.arange(a, z + 1)
        sel = mask[y, a:z + 1] > 0
        if sel.sum() < 10:
            continue
        cool = (b[y, xs][sel] - g[y, xs][sel])
        violet.append((y, float((cool > 12).mean()), z - a + 1))
    if not violet:
        return {"error": "no violet barrel found"}

    barrel_rows = [v for v in violet if v[1] > 0.55]
    if len(barrel_rows) < 60:
        return {"error": "barrel not separable from the ground in this frame"}
    y_bar0 = barrel_rows[0][0]
    # the body ends where the reflection begins: a sudden width blow-out
    widths = np.array([v[2] for v in barrel_rows], np.float32)
    med = float(np.median(widths))
    keep = [v for v in barrel_rows if v[2] < med * 1.35]
    y_bar1 = keep[-1][0] if keep else barrel_rows[-1][0]
    barrel_w = float(np.percentile([v[2] for v in keep], 90))

    out = {"unit_count": units,
           "barrel_w": barrel_w,
           "body_h": float(y_bar1 - ytop),
           "deployed_aspect": float(y_bar1 - ytop) / barrel_w}

    # ---- white working end, if one is deployed
    white = [y for y in ys if y < y_bar0 - 2]
    tip_state = None
    if len(white) > 20:
        w_top = white[0]
        w_bot = white[-1]
        wid = {y: sp[y][1] - sp[y][0] + 1 for y in white}
        tip_w = float(np.percentile(list(wid.values()), 92))
        # rise: from the apex row to the first row at full tip width
        full = [y for y in white if wid[y] >= 0.95 * tip_w]
        rise = float((full[0] - w_top)) if full else float(w_bot - w_top)
        crest = float(np.percentile([wid[y] for y in white[:4]], 50))
        sleeve = float(sp[y_bar0 + 3][1] - sp[y_bar0 + 3][0] + 1) if (y_bar0 + 3) in sp else barrel_w

        # A chisel crest rises fast and lands on a short flat; a dome does
        # not. The rise ratio separates them, so it decides which end this is.
        out["tip_w_over_sleeve"] = tip_w / sleeve
        out["tip_w_over_barrel"] = tip_w / barrel_w
        out["tip_rise"] = rise / tip_w
        out["tip_crest_flat"] = crest / tip_w
        out["tip_aspect"] = float(w_bot - w_top) / tip_w
        lo, hi = RATIOS["CHAMFER_RISE"]
        tip_state = "balm" if lo <= out["tip_rise"] <= hi and out["tip_crest_flat"] < 0.20 else "brush"
        out["tip_state"] = tip_state

        yy, xx = np.nonzero(mask[w_top:w_bot + 1, :])
        L, A, B = _labstats(im, yy + w_top, xx)
        out["cream_L"], out["cream_a"], out["cream_b"] = L * 100.0 / 255.0, A, B
        # apex centring
        apex_c = (sp[w_top][0] + sp[w_top][1]) / 2.0
        tip_c = (min(sp[y][0] for y in white) + max(sp[y][1] for y in white)) / 2.0
        out["tip_apex_offset"] = abs(apex_c - tip_c) / tip_w
    else:
        out["tip_state"] = "capped"
        out["closed_aspect"] = out["deployed_aspect"]

    # ---- barrel colour, sampled off the highlight and off the shadow edge
    mid = (y_bar0 + y_bar1) // 2
    a, z = sp[mid]
    q0, q1 = a + int((z - a) * 0.55), a + int((z - a) * 0.85)
    yy = np.arange(mid - 30, mid + 30)
    xx = np.arange(q0, q1)
    YY, XX = np.meshgrid(yy, xx, indexing="ij")
    L, A, B = _labstats(im, YY.ravel(), XX.ravel())
    out["barrel_L"], out["barrel_a"], out["barrel_b"] = L * 100.0 / 255.0, A, B

    # ---- wordmark: a tall narrow HIGH-FREQUENCY block inside the barrel.
    # Thresholding on brightness alone finds the satin highlight instead and
    # then bridges the two into one blob, which is how a single wordmark
    # reads as none. Letter strokes are thin and the highlight is smooth, so
    # the discriminator is the residual against a blurred copy, not the level.
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY).astype(np.float32)
    resid = gray - cv2.GaussianBlur(gray, (0, 0), 9)
    inside = np.zeros(gray.shape, np.uint8)
    for y in range(y_bar0, y_bar1):
        if y not in sp:
            continue
        a, z = sp[y]
        w = z - a
        if w < 30:
            continue
        inside[y, a + int(w * 0.15): z - int(w * 0.15)] = 1
    bright = ((resid > 7) & (inside > 0)).astype(np.uint8)
    bright = cv2.morphologyEx(bright, cv2.MORPH_CLOSE, np.ones((21, 5), np.uint8))
    bright = cv2.morphologyEx(bright, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    n, lb, st, cen = cv2.connectedComponentsWithStats(bright, 8)
    blobs = []
    for i in range(1, n):
        x, y, w, h, ar = st[i]
        if (ar > 0.08 * barrel_w * barrel_w and h > 3 * w
                and h < barrel_w * 2.2 and w < barrel_w * 0.45
                and y_bar0 <= cen[i][1] <= y_bar1):
            blobs.append((ar, x, y, w, h, cen[i]))
    out["wordmark_count"] = len(blobs)
    if blobs:
        ar, x, y, w, h, c = max(blobs)
        out["wordmark_length"] = h / barrel_w
        out["wordmark_cap_h"] = w / barrel_w
        a0, z0 = sp[int(c[1])]
        out["wordmark_centring"] = abs(c[0] - (a0 + z0) / 2.0) / barrel_w
    return out


# ----------------------------------------------------------------- score
def score(m):
    """Return (label, verdict, detail) rows. FAIL blocks a batch; WARN and
    INFO do not. Anything the segmentation cannot support gets SKIP rather
    than a number nobody should trust."""
    rows = []
    tip = m.get("tip_state")
    u = m.get("unit_count", 1)
    rows.append(("one unit in frame", "PASS" if u == 1 else "FAIL",
                 "%d product-sized object(s) found" % u))

    def chk(label, key, rkey, info=False, gate=True):
        if key not in m:
            rows.append((label, "SKIP", "not measurable in this frame"))
            return
        table = INFO_RATIOS if info else RATIOS
        lo, hi = table[rkey]
        v = m[key]
        d = "%.3f (want %.2f-%.2f)" % (v, lo, hi)
        if not gate:
            rows.append((label, "INFO", d + " — reported, not gated"))
        elif lo <= v <= hi:
            rows.append((label, "PASS", d))
        else:
            rows.append((label, "FAIL", d))

    if tip == "balm":
        chk("balm tip / sleeve width", "tip_w_over_sleeve", "BALM_OVER_SLEEVE")
        chk("chamfer rise / tip width", "tip_rise", "CHAMFER_RISE")
        chk("flat crest / tip width", "tip_crest_flat", "CREST_FLAT")
        if "tip_apex_offset" in m:
            ok = m["tip_apex_offset"] <= 0.06
            rows.append(("crest centred on the tip", "PASS" if ok else "FAIL",
                         "%.3f off centre (want under 0.06)" % m["tip_apex_offset"]))
    elif tip == "brush":
        chk("crown / barrel width", "tip_w_over_barrel", "CROWN_OVER_BARREL")
        chk("crown height / crown width", "tip_aspect", "CROWN_ASPECT")
        if "tip_apex_offset" in m:
            ok = m["tip_apex_offset"] <= 0.08
            rows.append(("crown apex on the centreline", "PASS" if ok else "WARN",
                         "%.3f off centre — working ruling, not a fact"
                         % m["tip_apex_offset"]))
    else:
        rows.append(("working end", "INFO", "capped in this frame — tip checks skipped"))
        chk("closed height / barrel width", "closed_aspect", "CLOSED_ASPECT")

    chk("deployed height / barrel width", "deployed_aspect", "DEPLOYED_ASPECT",
        info=True, gate=False)

    # colour — the two axes that carry the dated failure
    for label, key, rkey in (("cream warmth b*", "cream_b", "CREAM_B_STAR"),
                             ("barrel coolness b*", "barrel_b", "BARREL_B_STAR"),
                             ("barrel violet a*", "barrel_a", "BARREL_A_STAR")):
        if key not in m:
            rows.append((label, "SKIP", "not present in this frame"))
            continue
        lo, hi = RATIOS[rkey]
        v = m[key]
        d = "%+.1f (want %+.1f to %+.1f)" % (v, lo, hi)
        rows.append((label, "PASS" if lo <= v <= hi else "FAIL", d))

    # wordmark
    c = m.get("wordmark_count", 0)
    if c == 0:
        rows.append(("wordmark present", "SKIP", "none located — check by eye"))
    elif c == 1:
        rows.append(("one wordmark only", "PASS", "one block found"))
        chk("wordmark length / barrel width", "wordmark_length", "WORDMARK_LENGTH")
        chk("wordmark cap height / barrel", "wordmark_cap_h", "WORDMARK_CAP_HEIGHT")
        chk("wordmark on the centreline", "wordmark_centring", "WORDMARK_CENTRING")
    else:
        rows.append(("one wordmark only", "FAIL",
                     "%d bright blocks found — check for a duplicated wordmark" % c))
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
        nf = sum(1 for r in rows if r[1] == "FAIL")
        bad += bool(nf)
        print("    %d fail, %d warn, %d skip"
              % (nf, sum(1 for r in rows if r[1] == "WARN"),
                 sum(1 for r in rows if r[1] == "SKIP")))
    print("\n  eye-only checks still owed on every frame: satin not gloss, fibre")
    print("  quality, wordmark legibility, the terrain-constant rule, the colour")
    print("  front sitting behind the brush crown, and the four dated failures.")
    if bad:
        print("\n  %d frame(s) failed. Do not proceed with the batch." % bad)
    return 1 if bad else 0


check = run


# ==================================================================
# CLI
# ==================================================================
def _selftest():
    print("%s — product sheet V%s (single file)\n" % (PRODUCT, VERSION))
    verify(verbose=True)
    print()
    for k, v in counts().items():
        print("  %-22s %5d" % (k, v))
    print()
    print("  gated ratios")
    for k, (lo, hi) in RATIOS.items():
        print("    %-22s %8.2f - %8.2f" % (k, lo, hi))
    print("  informational")
    for k, (lo, hi) in INFO_RATIOS.items():
        print("    %-22s %8.2f - %8.2f" % (k, lo, hi))
    print()
    print("  mechanism: %s register, %s claim" % (MECHANISM_REGISTER, MECHANISM_CLAIM))
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
        if a[0] == "--refs":
            paths = []
            for q in sorted(glob.glob(REFS)):
                if any(t in os.path.basename(q) for t in EXCLUDE_REFS):
                    print("  excluded (multi-instance, never attachable): %s"
                          % os.path.basename(q))
                    continue
                paths.append(q)
        else:
            paths = a[1:]
        if not paths:
            sys.exit("no frames given")
        print("  thresholds from this sheet; ruling: %s" % list(RULINGS)[0])
        sys.exit(run(paths))

    sys.exit("unknown option %r — try no args, --md, --check, --refs" % a[0])
