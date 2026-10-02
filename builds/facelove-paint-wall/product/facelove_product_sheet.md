# Product Sheet — FACELOVE Changing Foundation Stick

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
