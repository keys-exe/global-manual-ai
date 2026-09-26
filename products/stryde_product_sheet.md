# Product Sheet — Stryde Precision Strap

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

---

## 18. The name on the product *(V7.49.32 — user: "sometimes the product shows no name")*

A STRYDE with no wordmark reads as the cheap copy, which is defined by having none. So:

1. **Prompts ask for it.** Every shot that shows the shell's front carries `WORDMARK-LOCK` (the grey lowercase stryde wordmark on the lower body, centred beneath the notch, always there, never a blank shell); every video adds `NEG-WORDMARK`. Back, side and rear shots never ask for it.
2. **Every render is checked:** `python3 stryde_product_sheet.py --wordmark <frames>` — `--no-name` for back, side and rear. A front view with no name is **REGENERATE Q2**; a name on a back view is too. For video, run it on the contact-sheet frames (§22W).
3. **How it checks:** a letter-shape detector (grey letters on smooth dark shell) and a match against the real wordmark cut from `front.webp`. Measured V7.49.32: all 11 reference frames with the name found, all 10 without it clear, and both frames with the name painted out failed as they should. The self-test re-runs six of these every time.
