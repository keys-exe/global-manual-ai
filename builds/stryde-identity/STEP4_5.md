# stryde-identity — Steps 4–5 (Manual)

Built against the **locked avatars** (user, 2026-09-26): N-NARR v2 · C1 Maureen · C2 Dean · C3 Pat v2 · C4 Surgeon v2. **F2 settled:** Pat in shorts on HK3 (her knee must show). **F1 as read:** HK1 top = C4, bottom = C1. Side: **right knee**, every worn beat.

**Order to run:** generate the six plates (§4, below) → send them back for my check (§22V) → I write the hook seeds (step 6). The narrator's voice route comes in the next delivery. Every B-roll `duration` stays `pending-master` until his voice master exists (E6).

---

## Step 4 — Property and locations (§30C, §30G)

### Location Derivation Pass (C0 first)

| ID | Location | Channel | Owner | Beats | Tier | Profile |
|---|---|---|---|---|---|---|
| **PROP-M** | Maureen's house — 1930s end-of-terrace | **C0**: hall/stairs + kitchen are rooms of one dwelling | C1 | — | **Property Sheet + plate P0** | east-facing front, morning |
| L-M-STAIRS | hall and stairs | C1 (VN01 "carpeted staircase at home"), C6 (stairs after-state) | C1 | HK1-B, BR-13, BR-14, BR-18, BR-25, BR-26a, BR-26b | **TRAVERSED** + property plate · landmark: the mahogany-stained handrail | P0 daylight |
| L-M-KITCHEN | galley kitchen | C3 (the box and its straps need a real table) | C1 | BR-22, BR-23, BR-24 | **PLATED** — plate P1 | `LOC-KITCHEN-MORN`, west, indirect |
| L-CONSULT | consulting room, private clinic | C1 (VN01 lightbox), C5 (surgeon) | C4 | HK1-T, BR-03, BR-04, BR-06, BR-20 | **PLATED** — plate P2 | cool window + lightbox |
| L-WAREHOUSE | warehouse aisle | C1 (VN02 shelving) | C2 | HK2-T, BR-17, BR-19 | **PLATED** — plate P3 | high-bay LED + open shutter |
| L-YARD | loading yard, the van | C1 (VN02 van) | C2 | HK2-B, BR-16 | **PLATED** — plate P4 (the van spot) | `LOC-EXT-OVERCAST` |
| L-LAB | gait lab | C2 (sports scientists measured it) | GENERIC | BR-08, BR-09 | **PLATED** — plate P5 | fluorescent + high window |
| L-PARK | park path | C1 (VN03), C7 (positive act) | C3 / GENERIC | HK3-B, BR-12, BR-21 | **TRAVERSED** · landmark: the green-painted park railings | `LOC-EXT-SUN` |
| L-P-HALL | Pat's hallway | C1 (VN03 "scooter leaning on the wall") | C3 | HK3-T | **INCIDENTAL** (one room of her house, no second room → no property sheet) | written with the beat at step 6 |
| L-G-TABLE | a kitchen table, anonymous | C4 (the comparison is GENERIC, so it can't use Maureen's rooms) | GENERIC | BR-05 | **INCIDENTAL** | written with the beat at step 7 |

**Set checks:** **S1** tiers above by beat count and movement ✓ · **S2** every location daylight, no evening ✓ · **S3** Maureen's hall (east, door glass) and kitchen (west, indirect) differ because they face opposite ways ✓ · **S4** no two consecutive acts share a room — A mechanism · B ends L-LAB · C opens mechanism · C ends mechanism · D opens L-YARD · D ends L-WAREHOUSE · E opens L-CONSULT ✓. **The location set closes here.**

### Property Sheet — PROP-M (Maureen's house)

| # | Field | Content |
|---|---|---|
| 1 | Type and era | 1930s red-brick end-of-terrace, decorated in the late 1980s and kept since |
| 2 | Shell | faded magnolia painted plaster · deep ogee skirting, ~20 cm, yellowed white gloss · matching moulded architraves · white four-panel doors, round brass knobs worn dull · white ceiling, faint Artex swirl, simple pendant · worn beige carpet on hall and stairs with brass stair rods → brown-and-cream patterned vinyl at the kitchen, brass carpet strip · white single-panel steel radiators · yellowed white plastic switches and sockets |
| 3 | Floor map | front door → hall; stairs rise on the **left** from just inside the door; kitchen straight ahead at the end of the hall on the **right**; landing at the top turns right |
| 4 | Orientation | front (hall, door glass) faces **east** — morning sun through the door glass · kitchen at the back faces **west** — indirect morning light |
| 5 | Carried elements | the beige carpet with brass stair rods · the mahogany-stained handrail · the harbour print above the half-moon hall table · the navy raincoat on the hook |
| 6 | Exterior | front: a small paved yard and low brick wall to the street; back: a narrow lawn, wooden fence, backs of the terrace opposite |
| 7 | Standing negatives | none yet (first plate) |

### Plates — copy-ready

Every plate: **empty, no people, no product**. Generate on Higgsfield `gpt_image_2_5`, `variant: sunburst`, `quality: high`, `resolution: 2k`, `aspect_ratio: 9:16`, one generation each. Send each one back for my check before anything is built against it.

The prompts are in `plates/<ID>.prompt.txt`, assembled by `plates/build_plates.py` from the Appendix A strings by ID:

| ID | Location | Attach | Chars | Gate |
|---|---|---|---|---|
| **P0-PROP-M** | Maureen's hall and stairs (property plate) | nothing | 5,370 | **first** — every shell element readable, one age of building, no show home |
| P1-M-KITCHEN | Maureen's kitchen | **P0 approved** | 6,670 | after P0 |
| P2-CONSULT | consulting room | nothing | 4,658 | anchors: lightbox with two knee X-rays, knee model, bookshelf, blue couch |
| P3-WAREHOUSE | warehouse aisle | nothing | 4,416 | anchors: orange-and-blue racking, yellow lines, open shutter, red pallet truck, workbench |
| P4-YARD | loading yard | nothing | 4,389 | anchors: white van with open rear doors and step, corrugated wall, pallets, yellow bollard |
| P5-LAB | gait lab | nothing | 4,400 | anchors: treadmill, pressure walkway, two knee-height cameras, blank whiteboard — **no readable screen or numbers** (§43) |

---

## Step 5 — Act map (E4) and wardrobe map (§21, §14A)

### Hook variants (§14)

**Different openings on different days**, so each hook is its own capture event with its own story day, and its wardrobe is different at class level. All three hooks use **EG01 split 50/50**: two clips per hook, each generated full 9:16 and **framed for the crop**, so the action sits in the middle half of the frame.

### Act map

Columns are E4's, condensed. `dur` = `pending-master` on every row (E6). **Model** follows the Mode & Model Lock: `NBP` = `nano_banana_pro` (wordmark with hands or a body), `NB2` = `nano_banana_2` (volume or mechanism).

| Beat | Act | Phrase | Type · function | Subject | Location · tier | Day · event | Framing · energy · valence | Product · visibility | Layout · EG | Model | Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **HK1-T** | Hook | HK1 | BR · product presentation | **C4** hands, face cropped at chin | L-CONSULT · P | S-D1 · E-H1a | CU hands to lens, lightbox behind · lift · neutral | **held** — turns it to show the pad (`HELD_GRIPS` + `PAD_BACK_SHOT`) | split top · EG01 | NBP | VN01 top |
| **HK1-B** | Hook | HK1 | BR · problem-to-relief | **C1** knee | L-M-STAIRS · T | M-D1 · E-H1b | ECU right knee stepping down a stair, eases back to her hand resting on the rail · calm · pos | **worn** · VISIBLE | split bottom · EG01 | NBP | VN01 bottom |
| **HK2-T** | Hook | HK2 | BR · product presentation | **C2** gloved hands | L-WAREHOUSE · P | D-D1 · E-H2a | CU gloved hands to lens, shelving blurred · lift · neutral | **held** — turns to the pad | split top · EG01 | NBP | VN02 top |
| **HK2-B** | Hook | HK2 | BR · capability | **C2** knee | L-YARD · P | D-D1 · E-H2b | ECU right knee stepping down off the van's rear step, walks off with a box on his shoulder · stab · pos | **worn** · VISIBLE | split bottom · EG01 | NBP | VN02 bottom |
| **HK3-T** | Hook | HK3 | BR · product presentation | **C3** hands (rings, cardigan cuff) | L-P-HALL · I | P-D1 · E-H3a | CU hands to lens, child's scooter against the wall · lift · pos | **held** | split top · EG01 | NBP | VN03 top |
| **HK3-B** | Hook | HK3 | BR · after-state | **C3** knee | L-PARK · T | P-D1 · E-H3b | ECU right knee walking fast on the path, eases back to a toddler on a scooter just ahead, her keeping up · lift · pos | **worn** · VISIBLE (shorts, F2) | split bottom · EG01 | NBP | VN03 bottom |
| MECH-01 | A | P-001 | MECH · load arriving | — | — | — | ANAT-A, walking cadence · stab · neg | absent | full · EG02 · **17× overlay** | NB2 | — |
| MECH-02 | A | P-002 | MECH · the point | — | — | — | ANAT-A + `ANAT_A_POINT_TIGHT` at `[SITE]` · stab · neg | absent | full | NB2 | — |
| BR-03 | B | P-003 | BR · authority/proof | **C4** | L-CONSULT · P | S-D2 · E-B1 | MCU at the desk, turns the strap in the light beside the knee model · calm · neutral | **held** | full | NBP | — |
| BR-04 | B | P-004 | BR · placement demo | one-off patient G-01 (knee only) + C4 hand | L-CONSULT · P | G-01 / S-D2 · E-B1 | ECU patient's right knee on the couch, strap seated, kneecap in the notch; C4's fingertip rests beside the notch · calm · neutral | **worn** · VISIBLE (`worn_front`) | full | NBP | — |
| BR-05 | B | P-005 | BR · SIDE-BY-SIDE demo | one-off hands G-02 | L-G-TABLE · I | G-02 · E-B2 | CU both straps side by side on a kitchen table, the near-copy (`FAKE_BASE` + **too small**) visibly smaller · stab · neg | hero + copy (§9C) | full | NBP | F4 |
| BR-06 | B | P-006 | BR · the pad | **C4** hands | L-CONSULT · P | S-D2 · E-B3 | CU hands turn the strap to show the inner pad (`PAD_BACK_SHOT`) · calm · neutral | **held** · the pad | full | NBP | — |
| MECH-07 | B | P-007 | MECH · protection | — | — | — | ANAT-A: force spreads across the pad, off the joint · lift · pos | absent | full | NB2 | — |
| BR-08 | B | P-008 | BR · proof | **C3** walking (legs) + one-off scientist G-04 | L-LAB · P | P-D0 + G-04 · E-B4 | MW treadmill, scientist beside it, legs in the frame · calm · neutral | **worn** · VISIBLE | full | NBP | — |
| BR-09 | B | P-009 | BR · proof | **C3** knee | L-LAB · P | P-D0 · E-B4 | ECU right knee on the treadmill, walking cadence · lift · pos | **worn** · VISIBLE | full · **34% overlay** | NBP | — |
| MECH-10 | C | P-010 | MECH · conditions | — | — | — | ANAT-B ghost limb: bone on bone, arthritis · calm · neg | absent | full | NB2 | — |
| MECH-11 | C | P-011 | MECH · conditions | — | — | — | ANAT-B: worn cartilage, meniscus · calm · neg | absent | full | NB2 | — |
| BR-12 | C | P-012 | BR · after-state | **C3** | L-PARK · T | P-D2 · E-C1 | MW walking past the green railings, strides long · lift · pos | **worn** · VISIBLE | full | NBP | — |
| BR-13 | C | P-013 | BR · after-state (ascent) | **C1** | L-M-STAIRS · T | M-D3 · E-C2 | MW from the hall, climbing, her hand off the rail · lift · pos | **worn** · VISIBLE | full | NBP | — |
| BR-14 | C | P-014 | BR · honesty beat | **C1** | L-M-STAIRS · T | M-D3 · E-C2 | MCU on the landing, pausing, palm resting above the kneecap · calm · neutral | **worn** · VISIBLE | full | NBP | — |
| MECH-15 | C | P-015 | MECH · protection | — | — | — | ANAT-A: the site calm, the force carried by the pad · calm · pos | absent | full | NB2 | — |
| BR-16 | D | P-016 | BR · **SEAT** (fit, never adjusting) | **C2** | L-YARD · P | D-D2 · E-D1 | MCU sitting on the van step, both hands slide the closed strap **up** the shin to seat (`SEAT_LOCK`) · calm · neutral | **seated** · VISIBLE | full | NBP | F6 |
| BR-17 | D | P-017 | BR · capability (FLEX) | **C2** | L-WAREHOUSE · P | D-D2 · E-D2 | MW squat-lift of a box, knee flexed, strap holding (`PLACE_BENT`) · stab · pos | **worn** · VISIBLE | full | NBP | — |
| BR-18 | D | P-018 | BR · **REVEAL→CONCEALED** (§9D) | **C1** | L-M-STAIRS · T | M-D4 · E-D3 | CU trouser leg lowered over the strap, the fabric lies flat · calm · neutral | **worn** · REVEAL | full | NBP | — |
| BR-19 | D | P-019 | BR · end of shift | **C2** | L-WAREHOUSE · P | D-D2 · E-D4 | MW leaning on the workbench, mug of tea, strap still in place · calm · pos | **worn** · VISIBLE | full | NBP | — |
| BR-20 | E | P-020 | BR · recommendation | **C4** + one-off patient hands G-05 | L-CONSULT · P | S-D3 / G-05 · E-E1 | CU across the desk, C4 hands the strap to the patient · calm · pos | **held** | full | NBP | — |
| BR-21 | E | P-021 | BR · social proof | one-off walking group G-06 | L-PARK · T | G-06 · E-E2 | MW group of older walkers passing the railings, a strap on the nearest knee · lift · pos | **worn** · VISIBLE | full · **200,000 overlay** | NBP | — |
| BR-22 | E | P-022 | BR · re-hook | **C1** hands | L-M-KITCHEN · P | M-D5 · E-E3 | CU closed box on the checked cloth, hands begin lifting the lid · lift · pos | box **closed** — needs `package_closed.jpg` (F7) | full · **EG04 offer card starts** | NBP | F7 |
| BR-23 | E | P-023 | BR · offer | **C1** hands | L-M-KITCHEN · P | M-D5 · E-E3 | CU lid off, **two** straps lying flat in the insert (`package_open`) · lift · pos | box **open**, two units | full · EG04 | NBP | — |
| BR-24 | E | P-024 | BR · guarantee | **C1** | L-M-KITCHEN · P | M-D5 · E-E3 | MCU lifts one strap out, turns it in the window light · calm · pos | **held** | full · EG04 | NBP | — |
| BR-25 | E | P-025 | BR · stairs payoff | **C1** | L-M-STAIRS · T | M-D5 · E-E4 | MW at the foot of the stairs looking up, first step · calm · pos | **worn** · VISIBLE | full · EG04 | NBP | — |
| BR-26a | E | P-026 "Put one on," | BR · **SEAT** | **C1** | L-M-STAIRS · T | M-D5 · E-E4 | MCU seated on the bottom stair, slides it up the shin to seat (`SEAT_LOCK`) · calm · neutral | **seated** · VISIBLE | full · EG04 | NBP | — |
| BR-26b | E | P-026 "and your own stairs will tell you." | BR · after-state (ascent) | **C1** | L-M-STAIRS · T | M-D5 · E-E4 | MW from the landing looking down, she climbs towards the camera, hand off the rail · lift · pos | **worn** · VISIBLE | full · EG04 | NBP | — |

**Product first appearance:** hooks — HK1-T/HK2-T/HK3-T, in hand at 0:00 in every variant. **Screen direction:** stairs sequences hold a `GEO-LINE` — the stairs rise **left** of frame from the hall (per P0); ascent beats move left-to-right-up, descents the reverse. **Offer card (EG04)** runs BR-22 → BR-26b, like the reference's close. **No talking head anywhere** (Style Lock).

### Visual Instruction Ledger — assigned (§27F)

| ID | Carried by | Status |
|---|---|---|
| VN01 | HK1-T (C4, lightbox, turns to the pad) + HK1-B (C1 stairs, eases back to her hand on the rail) | assigned — verified at the §22V/§22W check |
| VN02 | HK2-T (gloved hands, shelving) + HK2-B (van step, box on shoulder) | assigned |
| VN03 | HK3-T (rings, cardigan cuff, scooter) + HK3-B (park path, toddler on scooter) — **shorts, not cropped trousers (F2, user)** | assigned — **flagged-and-settled** |
| LM01–LM07 | whole build (identity call-out, reference formula) + HK1–HK3 | assigned |

### Wardrobe Ledger (§14A) — one outfit per story day

Story-day pass: **D2** one day per act per subject · **D5** each GENERIC subject has its own single day · hooks are different days (§14 hook table). **Timeline order** (hook first, then the shared body):

| Day | Subject | BASE | MID | OUTER | LOWER | FOOT | ACCENT | Colour family | Events · visibility · beats |
|---|---|---|---|---|---|---|---|---|---|
| S-D1 | C4 | blue-and-white fine-check button-down shirt | navy v-neck jumper | — | grey chinos | brown lace-ups *(signature)* | steel watch | navy/denim | E-H1a · — · HK1-T |
| M-D1 | C1 | mustard-and-teal paisley blouse | — | — | teal A-line skirt, a hand above the knee | tartan slippers | — | pattern-led | E-H1b · VISIBLE · HK1-B |
| D-D1 | C2 | navy crew-neck T-shirt | — | orange hi-vis waistcoat | black multi-pocket work shorts | black steel-toe boots *(signature)* | work gloves (top band only) | navy/denim + hi-vis | E-H2a, E-H2b · VISIBLE · HK2-T, HK2-B |
| P-D1 | C3 | white polo shirt | moss-green buttoned cardigan | — | navy cotton shorts to just above the knee | white canvas trainers *(signature)* | two rings, cross-body bag strap | green | E-H3a, E-H3b · VISIBLE · HK3-T, HK3-B |
| S-D2 | C4 | white button-down shirt | charcoal knitted waistcoat | — | charcoal trousers | brown lace-ups *(signature)* | clinic lanyard, card blank | monochrome | E-B1, E-B3 · — · BR-03, BR-04, BR-06 |
| G-01 | patient | navy T-shirt (out of frame) | — | — | grey running shorts | grey trainers | — | cool neutral | E-B1 · VISIBLE · BR-04 |
| G-02 | hands | oatmeal long-sleeve tee (cuffs) | — | — | — | — | — | warm neutral | E-B2 · — · BR-05 |
| P-D0 | C3 | coral technical polo | — | — | black running shorts to just above the knee | grey running trainers | fitness watch | red | E-B4 · VISIBLE · BR-08, BR-09 |
| G-04 | scientist | blue gingham check shirt | — | — | navy chinos | black trainers | lanyard, card blank | navy/denim | E-B4 · — · BR-08 |
| P-D2 | C3 | navy-and-cream Breton long-sleeve top | rust quilted gilet | — | khaki shorts to just above the knee | white canvas trainers *(signature)* | — | earth | E-C1 · VISIBLE · BR-12 |
| M-D3 | C1 | burgundy long-sleeve jersey tunic | — | — | denim skirt, a hand above the knee | sheepskin slippers | — | red | E-C2 · VISIBLE · BR-13, BR-14 |
| D-D2 | C2 | green-and-black check flannel shirt, sleeves rolled | — | — | khaki cargo shorts | black steel-toe boots *(signature)* | watch | green | E-D1, E-D2, E-D4 · VISIBLE · BR-16, BR-17, BR-19 |
| M-D4 | C1 | cream roll-neck | camel open draped cardigan | — | wide-leg navy trousers | brown loafers | — | warm neutral | E-D3 · REVEAL · BR-18 |
| S-D3 | C4 | pale pink button-down shirt | — | — | navy trousers | brown lace-ups *(signature)* | steel watch | red | E-E1 · — · BR-20 |
| G-05 | patient hands | grey long-sleeve tee (cuffs) | — | — | — | — | — | cool neutral | E-E1 · — · BR-20 |
| G-06 | walking group (nearest walker) | sage-green T-shirt | — | — | navy walking shorts | walking boots | cap | green | E-E2 · VISIBLE · BR-21 |
| M-D5 | C1 | cornflower-blue cotton dress, a hand above the knee *(replaces BASE + LOWER)* | — | — | *(dress)* | navy slip-ons *(signature)* | — | navy/denim | E-E3, E-E4 · VISIBLE · BR-22–BR-26b |

**Signature items (declared):** C1 navy slip-ons · C2 black steel-toe boots · C3 white canvas trainers · C4 brown lace-ups.

**Audits:**

| # | Audit | Result |
|---|---|---|
| **W1** | No BASE class twice in an act · no exact garment twice except the signatures | Hooks: button-down · blouse · T-shirt · polo ✓ · B: button-down · T-shirt · long-sleeve · polo · check ✓ · C: long-sleeve · tunic ✓ · D: check · roll-neck ✓ · E: button-down · long-sleeve · T-shirt · dress ✓ · exact repeats: signatures only ✓ |
| **W2** | Consecutive days differ on ≥2 layers incl. BASE | 17/17 consecutive pairs ✓ (every pair changes BASE and LOWER or MID) |
| **W3** | Colour families rotate; positive days not all neutral | no two consecutive days share a family (HK1: navy → pattern → monochrome; HK2: navy → monochrome; HK3: green → monochrome; body: mono → cool → warm → red → navy → earth → red → green → warm → red → cool → green → navy) ✓ · positive days carry colour (coral, green, rust, cornflower) ✓ |
| **W4** | Every event resolves to one day, every day to one outfit | 25 events → 17 days → 17 outfit rows ✓ |

**Hem rule (§9D):** every VISIBLE row's LOWER ends clearly above the knee ✓. **Wardrobe is never changed to expose the product** — the activity picked the garment. BR-18 is the one trousers beat, and its job is the concealment.

### Reconciliation (§27B)

Hooks HK1–HK3 → 6 split clips · body P-001–P-026 → **31 beats** (BR 25 · MECH 6), P-026 split into BR-26a/b on its comma · merges: none · TH-carried: none · **uncovered 0 · blocked 0** · plants: HK1 stairs → paid BR-13, BR-25, BR-26b · open flags: F4 (comparative claim), F7 (`package_closed.jpg`).

### Subject Registry (§30E)

| ID | Sheet (locked) | Beats |
|---|---|---|
| C1 Maureen | `fb41402a…` | HK1-B, BR-13, BR-14, BR-18, BR-22–BR-26b |
| C2 Dean | `f81be8b9…` | HK2-T, HK2-B, BR-16, BR-17, BR-19 |
| C3 Pat | `c10469d4…` (v2) | HK3-T, HK3-B, BR-08, BR-09, BR-12 |
| C4 Surgeon | `1ba54d8d…` (v2) | HK1-T, BR-03, BR-04, BR-06, BR-20 |
| N Narrator | `366296a0…` (v2) | voice only |
