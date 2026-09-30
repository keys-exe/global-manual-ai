#!/usr/bin/env python3
"""Wardrobe map v2 (§21, §14A) — the user, 2026-09-29: "the wardrobe map is just the same wardrobe all over even though its a different day/event".
v1 dressed every problem beat in P-D1 and every after beat in P-D2. v2: one outfit per story day, a story day per event (§14A D1–D4: the problem
beats are separate moments across nine years; the after beats are separate days across six weeks). Rules held: ≥2 layers change between
consecutive days, BASE always one of them · no BASE class twice in an act · no exact garment twice in the build · colour family rotates ·
signature item (declared): her reading glasses on a beaded cord · never the sheet outfit (duck-egg jumper, check skirt) · problem days muted
and cool-season indoors, after days carry colour (§30F), late spring · the LOWER layer decides visibility (§9D), never modified to expose
the product. Hooks keep P-D1 / P-D2 (confirmed renders, untouched). The doctor keeps D-D1 (one consulting-room session, TH-locked).
Builders import DAY / WEAR; this file is the source for STEP4_5.md's wardrobe table and docs/wardrobe."""
SIG = "reading glasses on a thin beaded cord round her neck"
# day: (act, [beats], BASE, MID/OUTER, LOWER, FOOT, ACCENT, colour family, visibility, the "She wears …" sentence)
DAYS = {
 "P-B1": ("Act 1", ["BR-01"], "pale blue cotton button-down shirt, collar out", "grey marl crew-neck jumper", "knee-length charcoal wool A-line skirt, bare legs", "sheepskin moccasin slippers", SIG, "cool neutral", "absent",
          "She wears a pale blue cotton button-down shirt with its collar out over a grey marl crew-neck jumper, a knee-length charcoal wool A-line skirt with bare legs, sheepskin moccasin slippers, and " + SIG + "."),
 "P-B2": ("Act 1", ["BR-03b", "BR-04"], "rust long-sleeve jersey top", "—", "knee-length camel corduroy skirt, bare legs", "bare feet", "a plain gold wedding band", "earth", "absent",
          "She wears a rust-coloured long-sleeve jersey top, a knee-length camel corduroy skirt with bare legs, and bare feet."),
 "P-B3": ("Act 1", ["BR-05", "BR-05a", "BR-05b"], "cream blouse with a small dusky-rose floral print", "bottle-green buttoned cardigan", "dark grey slim ankle trousers", "navy felt slippers", SIG, "pattern-led", "absent",
          "She wears a cream blouse with a small dusky-rose floral print under a bottle-green buttoned cardigan, dark grey slim ankle-length trousers, navy felt slippers, and " + SIG + "."),
 "P-B4": ("Act 2", ["BR-06"], "lilac long-sleeve cotton tee", "navy quilted gilet", "navy elasticated-waist trousers", "grey knitted slipper boots", "—", "navy/denim", "absent",
          "She wears a lilac long-sleeve cotton tee under a navy quilted gilet, navy elasticated-waist trousers and grey knitted slipper boots."),
 "P-B5": ("Act 2", ["BR-07"], "teal jersey tunic", "—", "black leggings", "black suede slippers", "a soft grey-and-teal patterned scarf", "green family", "absent",
          "She wears a long teal jersey tunic over black leggings, black suede slippers, and a soft grey-and-teal patterned scarf loosely round her neck."),
 "P-B6": ("Act 2", ["BR-08"], "blue-and-white check flannel shirt", "—", "knee-length faded denim skirt, bare legs", "red tartan slippers", "—", "navy/denim", "absent",
          "She wears a blue-and-white check flannel shirt, a knee-length faded denim skirt with bare legs, and red tartan slippers."),
 "P-B7": ("Act 2", ["BR-09b"], "dusky-pink blouse with a rounded collar", "heather-grey v-neck jumper", "charcoal straight trousers", "brown suede slippers", SIG, "red family", "absent",
          "She wears a dusky-pink blouse with a rounded collar under a heather-grey v-neck jumper, charcoal straight trousers, brown suede slippers, and " + SIG + "."),
 "P-B8": ("Act 2", ["BR-09c"], "bottle-green fine roll-neck", "long charcoal open draped cardigan", "black straight trousers", "black flat shoes", "—", "green family", "absent",
          "She wears a bottle-green fine roll-neck under a long charcoal open draped cardigan, black straight trousers and black flat shoes."),
 "P-B9": ("Act 2", ["BR-10", "BR-10b", "BR-10c"], "raspberry polo shirt", "grey zip fleece, open", "grey jogging bottoms", "white trainers", "—", "red family", "absent",
          "She wears a raspberry-red polo shirt under an open grey zip fleece, grey jogging bottoms and white trainers."),
 "P-A1": ("Act 3", ["BR-11a", "BR-11b", "BR-11c", "PR-12"], "cornflower-blue linen button-down shirt, sleeves rolled to the forearm", "—", "wide-leg cream cotton trousers", "tan leather sandals", SIG, "navy/denim", "VISIBLE on BR-11c (trouser leg rolled for the gel), absent otherwise",
          "She wears a cornflower-blue linen button-down shirt with the sleeves rolled to the forearm, wide-leg cream cotton trousers, tan leather sandals, and " + SIG + "."),
 "P-A2": ("Act 3", ["BR-13", "MECH-14", "BR-14b", "BR-15"], "jade-green short-sleeved blouse", "—", "knee-length stone cotton skirt, bare legs", "white canvas plimsolls", "small pearl stud earrings", "green family", "VISIBLE (the skirt sits above the knee as she sits)",
          "She wears a jade-green short-sleeved blouse, a knee-length stone-coloured cotton skirt with bare legs, white canvas plimsolls and small pearl stud earrings."),
 "P-A3": ("Act 4", ["BR-17a", "BR-17b"], "raspberry-and-white Breton striped long-sleeve top", "—", "wide-leg mid-blue denim trousers", "white leather trainers", "a navy cross-body bag strap", "red family", "REVEAL (BR-17a, the left leg rolled to put it on) → CONCEALED (BR-17b, out at the shops, the trouser legs down)",
          "She wears a raspberry-and-white Breton striped long-sleeve top, wide-leg mid-blue denim trousers, white leather trainers, and a navy cross-body bag."),
 "P-A4": ("Act 4", ["BR-19a", "BR-19b"], "white cotton crew-neck t-shirt", "light denim overshirt, open", "knee-length mustard-yellow A-line skirt, bare legs", "navy canvas plimsolls", SIG, "earth (mustard)", "VISIBLE, one knee only",
          "She wears a white cotton crew-neck t-shirt under an open light denim overshirt, a knee-length mustard-yellow A-line skirt with bare legs, navy canvas plimsolls, and " + SIG + "."),
 "P-A5": ("Act 5", ["PR-22a", "BR-22a3"], "lilac cotton button-down shirt", "—", "(out of frame)", "(out of frame)", "a plain gold wedding band", "cool (lilac)", "absent (box)",
          "She wears a lilac cotton button-down shirt."),
 # the user, 2026-09-29 (BR-22a2 Fix): "brolls of showing the results of using the strap" → BR-22a2 becomes her, weeks on, going out again: its own day
 "P-A5b": ("Act 5", ["BR-22a2"], "coral linen short-sleeved top", "—", "knee-length navy cotton skirt, bare legs", "navy leather loafers", SIG, "warm (coral)", "VISIBLE",
          "She wears a coral linen short-sleeved top, a knee-length navy cotton skirt with bare legs, navy leather loafers, and reading glasses on a thin beaded cord round her neck."),
 "P-A6": ("Act 5", ["BR-23"], "cornflower-and-white floral knee-length tea dress, short sleeves (replaces BASE + LOWER)", "pale-yellow open cardigan", "(the dress), bare legs", "tan leather sandals", "small gold studs", "pattern-led", "VISIBLE",
          "She wears a cornflower-and-white floral knee-length tea dress with short sleeves under an open pale-yellow cardigan, bare legs, tan leather sandals and small gold stud earrings."),
}
DAY = {b: d for d, v in DAYS.items() for b in v[1]}
WEAR = {b: DAYS[d][-1] for b, d in DAY.items()}
def wear(beat, lead="She wears "):
    s = WEAR[beat]; return s if lead == "She wears " else s.replace("She wears ", lead, 1)
if __name__ == "__main__":
    # §14A audits: BASE class not repeated within an act, consecutive days change BASE, colour family rotates
    order = list(DAYS); prev = None
    for d in order:
        a, beats, base, *_ = DAYS[d]; fam = DAYS[d][7]
        if prev: assert DAYS[prev][7] != fam or DAYS[prev][0] != a, ("colour repeats", prev, d)
        prev = d
    for act in {v[0] for v in DAYS.values()}:
        bases = [v[2] for v in DAYS.values() if v[0] == act]; assert len(bases) == len(set(bases)), act
    print("wardrobe v2:", len(DAYS), "story days ·", len(DAY), "beats · audits PASS")
