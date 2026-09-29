# down-forwards-again — Steps 4–5 (Manual)

Built on the user's go (2026-09-28, "go ahead with steps 4–5"). **The avatars are still To check on the board** (D-DOC v2, P-PATIENT v1): plates carry no people, so nothing here depends on them yet; beat frames wait for your Confirm.

**Open flags carried with my recommendation (not yet answered):** **F8 → left knee** (the three left-knee worn references are generated below) · F9 → natural pace · F2/F4/F5/F6/F7 lines voiced as written, their beats marked in the Ledger column.

---

## Step 4 — Property and locations (§30C, §30G, §30K)

### Location Derivation Pass (C0 first)

| ID | Location | Channel | Owner | Beats | Tier | Plate |
|---|---|---|---|---|---|---|
| **PROP-P** | her house, a large Edwardian red-brick semi-detached | **C0**: hall/stairs, front room and kitchen are rooms of one dwelling | P | — | **Property Sheet + plate P0** | P0-PROP-P |
| L-P-HALL | hall and stairs | C1 (coming down vs going up, backwards, the test, the payoff) | P | HK1-01a, BR-05a, BR-05b, BR-06, BR-08, BR-09a, BR-17a, BR-17b, BR-19a, BR-19b, BR-23 | **TRAVERSED** + property plate · landmark: the dark turned banister on the right, the patterned runner with brass rods | P0 |
| L-P-FRONT | front room, the armchair | C1 ("the chair took three tries") | P | BR-04, BR-07, BR-10, BR-13 | **PLATED** | P1-P-FRONTROOM (P0 attached) |
| L-P-KITCH | kitchen, the dresser drawer, the garden window | C1 ("one more brace going in the drawer", "the garden") | P | HK1-02a, BR-01, BR-09b, BR-11a–c, PR-12, PR-22a, BR-22b | **PLATED** | P2-P-KITCHEN (P0 attached) |
| L-P-DOOR | her front step | C1 ("her family coming to her") | P | BR-09c | **INCIDENTAL** (the red-brick front, written with the beat) | — |
| L-D-CONS | the doctor's consulting room | C5 (the presenter, every TH) · C1 ("her scan") | D | TH-HK1…TH-A5, HK2-02a, HK3-01a, BR-02, BR-15, BR-20 | **PLATED** | P3-D-CONSULT |
| L-ORTHO | an orthopaedic clinic | C4 ("three years with orthopedic surgeons") | GENERIC | BR-16a | **INCIDENTAL** | — |
| L-TOWPATH | canal towpath | C4 (200,000 wearers) | GENERIC | BR-16b | **INCIDENTAL** | — |

**Set checks:** S1 tiers by beat count and movement ✓ · S2 every location daylight ✓ · S3 her house faces east at the front (door glass, bay window) and west at the back (kitchen, garden): the hall and front room take the morning, the kitchen stays flat and even ✓ · S4 consecutive acts don't open in the room the last one ended in: Act 1 ends MECH → Act 2 opens L-P-HALL; Act 2 ends L-P-FRONT → Act 3 opens L-P-KITCH; Act 3 ends L-D-CONS → Act 4 opens L-ORTHO; Act 4 ends L-D-CONS → Act 5 opens L-P-KITCH ✓. **The location set closes here.**

### Property Sheet — PROP-P (her house)

| # | Field | Content |
|---|---|---|
| 1 | Type and era | large, roomy Edwardian red-brick semi-detached (≈3 m ceilings), redecorated in the 1990s and kept since · **v2 (user Fix: "the house looks small and compressed")** — v1 was a narrow Victorian mid-terrace with a galley kitchen |
| 2 | Shell | magnolia above a dark-stained dado rail, cream anaglypta below · tall moulded skirting, white gloss gone yellow · white-gloss architraves · stripped pine four-panel doors, brass knobs · high white ceiling, plain cornice, frosted pendant · burgundy-and-cream patterned runner with brass rods over dark floorboards → red-and-black quarry tiles at the kitchen · white cast-iron column radiators · white switches, one brass dimmer |
| 3 | Floor map | front door → a wide hall (~2.5 m); a wide straight flight (>1 m) rises away from the door along the **left-hand** wall, banister on the open right; the front room through the doorway on the **right**; the large square kitchen-diner at the back of the hall |
| 4 | Orientation | front (door glass, bay window) faces **east**: morning light; back (kitchen, garden) faces **west** |
| 5 | Carried elements | the patterned runner and brass rods · the dark turned banister · the walking boots by the door · the telephone table · the harbour watercolour |
| 6 | Exterior | red-brick semi front, a low brick wall and privet hedge, the semis opposite across a wide tree-lined street |
| 7 | Standing negatives | none yet (first plate) |

### Light plans (§30K) — in room terms

| Location | Sources | Key by day | Kelvin (white balance) | Fill |
|---|---|---|---|---|
| L-P-HALL | front-door stained glass (east, behind a camera at the door) + tall landing window | P-D1 grey morning: pale wash down the runner · P-D2: sun through the door glass, a warm patch on the stairs | P-D1 6500K · P-D2 5600K | magnolia walls |
| L-P-FRONT | bay window, east wall, net curtains | P-D1 grey, even · P-D2 bright through the nets | 6500K · 5600K | magnolia walls |
| L-P-KITCH | window over the sink, west wall | P-D1 flat overcast across the room · P-D2 brighter, still indirect (morning, west window) | 6500K · 5600K | cream cupboards |
| L-D-CONS | the window camera-left (north), blinds open | D-D1 steady overcast, ~45° from camera-left on his face | 6500K | pale grey walls |
| L-ORTHO / L-TOWPATH | side window / open sky | X-D1 neutral daylight | 5600K | — |

**Light arc (Mode 1, daylight only):** hooks' problem shots and Acts 1–2 are the **problem** (P-D1: grey, flat, cooler). Act 3 onwards is the **after** (P-D2: sun in the house, warmer). The doctor's room never changes (D-D1). Never dark, never moody (§12).

### Plates and worn references — generated through the connector

Plates: Higgsfield `gpt_image_2_5` · `variant: sunburst` · `quality: high` · `resolution: 2k` · `9:16` · empty, no people, no product — `plates/build_plates.py` from Appendix A by ID (`CAM-LOCK`, `PLATE-PROP` / `PROP-REF` + `PROP-SHELL`, `VIEW-OUT`, `PHYS-FRAME-C`, `CAP-A`, `CAP-FILE`, `NEG-SCENE` / `NEG-PROP`, `NEG-M1`, `NEG-LIGHT`, `NEG-FILE`). Worn references: `worn_ref_prompts('left')` from the Product Sheet (never retyped), with the Product Sheet's scene text re-sided to the left leg (its scenes name the right leg), product photos attached.

| ID | Job | Attach | Chars | Model | Board |
|---|---|---|---|---|---|
| P0-PROP-P | 05091655-5fe3-468d-ad97-c6eec5bd7e0c | nothing | 6,143 | gpt_image_2_5 sunburst | To check |
| P1-P-FRONTROOM | fbf0668c-2650-411e-a540-fd991fecaaa8 | P0-PROP-P (approved) | 6,749 | gpt_image_2_5 sunburst | To check |
| P2-P-KITCHEN | 5534feb1-63c4-45fb-82ef-72cf39f32734 | P0-PROP-P (approved) | 6,776 | gpt_image_2_5 sunburst | To check |
| P3-D-CONSULT | 757817ea-6840-487c-879c-1b0310e137b2 | nothing | 4,965 | gpt_image_2_5 sunburst | To check |
| W-L-FRONT | 793ca329-e4b3-49fd-943c-5e97bae5366d | front.webp, product_tq_left.jpg | 4,650 | nano_banana_pro requested · Higgsfield reported nano_banana_2 | To check |
| W-L-REAR | c3e6103f-de8b-42e2-8929-281c4ea1e18d | back.webp, front.webp | 4,427 | nano_banana_pro requested · Higgsfield reported nano_banana_2 | To check |
| W-L-BENT | 2730a819-cf08-49a6-b5cd-01a086777dad | product_tq_left.jpg, front.webp | 5,264 | nano_banana_pro requested · Higgsfield reported nano_banana_2 | To check |

**Fix 2026-09-28 (user: "the house looks small and compressed"):** cause — the v1 prompts asked for a narrow terraced hall and a galley kitchen, framed tight through doorways with the door leaf in shot. Fixed at the source: a large Edwardian semi, wide hall and stairs, ~3 m ceilings, every room shot from standing inside it with nothing near the lens, plus a no-cramped-rooms negative on the house plates. P0 v2 `176c5c39`, then P1 v2 / P2 v2 against it; the three v1 plates are on the Old board. The layout the act map relies on (stairs on the left wall, banister right, front room right, kitchen at the back, east front / west back) is unchanged.

**Model note:** the three W-L references were sent as `nano_banana_pro`; Higgsfield's job record reports `nano_banana_2`. Recorded as reported — your check decides whether they stand. **Spend:** Higgsfield 17,933.25 (after the recast) → 17,894 after these 7 (the balance moved 39.25; per-job cost not itemised).

---

## Step 5 — Act map (E4) and wardrobe map (§21, §14A)

### Structure

| Act | Phrases | Job | Board group |
|---|---|---|---|
| Hook 1 / 2 / 3 | HK1 · HK2 · HK3 | three openings over the doctor (VN01: HK1 is the reference's construction — the result in a PiP box over him) | Hook 1, Hook 2, Hook 3 |
| Act 1 | B-01–B-05 | the patient, the scan, **the band**, the self-test, coming down vs going up | Act 1 |
| Act 2 | B-06–B-10 | "That is why" ×3, the list, never / never / always | Act 2 |
| Act 3 | B-11–B-15 | sleeve / brace / gel, **Stryde**, where it sits, the pad, placement | Act 3 |
| Act 4 | B-16–B-20 | proof, ten seconds, "I do not sell these", the stairs test, the two scans | Act 4 |
| Act 5 | B-21–B-23 | "move the load", the offer, the copies, "Go and do your stairs" | Act 5 |

**The doctor is the spine (EG spine):** one HeyGen talking-head segment per hook and act (TH rows) runs under the whole VO; every B-roll row sits on top of it in its `EDIT-DFA` layout — `pip` (anatomy, objects, his hands), `split 60/40` (mechanism, placement), `cutout` (her life full frame, him in the lower-left corner), `full` (only the product's first appearance PR-12 and the payoff stairs BR-19b, BR-23). **Product first appearance:** PR-12 ("This does. It is called Stryde."), ~1:50 into each video. HK1-01a shows her result with the strap **concealed** under trousers, so the product is first seen at PR-12. **Screen direction:** her stairs rise away from the front door along the left-hand wall (P0), so descents come towards camera. **Mirrors:** BR-19b mirrors BR-05b (the same step, now easy); BR-23 mirrors BR-06 (backwards from high → forwards from low). **Side:** the strap is on her **left** knee on every worn beat (F8); the right knee stays bare.

### Act map

Columns condensed from E4. `duration` = `pending-master` on every B-roll row (E6). Model: `NBP` = `nano_banana_pro` (wordmark with hands or a body), `NB2` = `nano_banana_2` (volume or mechanism), `GPT Sunburst` (product, no person). Motion per §27G: one action at a countable pace, the camera sways but never travels with a moving subject, safe staging on every stair, `pin_end` where the product turns or must end seated. Light key: the on-screen side derived from the room's plan, and the scene's white balance.

#### Hook 1

| Beat | Phrase | Type | Subject | Location | Day | Action · pace | Camera · staging · pin | Angle (height · side · scale · fg) — why | Focus | Light key | Key word | Product | Layout · EG | Model | Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TH-HK1 | HK1-01, HK1-02, HK1-03 | TH | D | L-D-CONS | D-D1 | straight to lens, level; a small open hand on 'here is how' · ~155 wpm | phone on a small tripod across the desk, locked off · seated at his desk · no | eye · front · MCU · clean | eyes, medium | L · 6500K |  | absent | spine (under every B-roll) · EG01 | HeyGen Avatar V | — |
| HK1-01a | HK1-01 | BR | P | L-TUBE | P-D2 | runs lightly DOWN the entrance stairs of an Underground station, forwards, both hands free (never on the rail) · one stride, 2s | locked-off sway · stairs descending (§27G: one stride, arms free, camera at the foot) · no | low · front · FULL · clean — low = the stairs she now owns, out in the world | deep, deep | R · 5600K | stairs | worn · CONCEALED under trousers (§9D) | full · EG05 · EG01 | NB2 | — |
| HK1-02a | HK1-02 | BR | P | L-HOSP | P-D1 | the surgeon holds a total knee replacement implant above her bare LEFT knee · one lowering, 2s | sway · hands (§27G: one action) · no | high · three-quarter · CU · clean — high = small on the bed, the knee replacement she nearly had | hands, medium | L · 6500K | operation | absent | full · EG05 · EG01 | NB2 | — |
| HK1-02b | HK1-02 | BR | P | L-PHYSIO | P-D1 | NHS physio class: a slow step-down on a low step, the physio watching her knee · one step-down, 3s | sway · stepping down (§27G: one step, hand on the bar) · no | eye · three-quarter · FULL · clean — eye/three-quarter = with her, one of a class | eyes, medium | L · 6500K | physio | absent | full · EG05 · EG01 | NB2 | — |
| HK1-02c | HK1-02 | BR | P hands | L-P-KITCH | P-D1 | holds the STRYDE strap up to the lens, the overflowing brace drawer soft behind · held still, a small turn, 2s | sway · hands (§27G: one action, HELD_GRIPS) · no | eye · front · CU · clean — eye/front = the answer held up against the pile | product, shallow | R · 6500K | drawer | held (HELD_GRIPS fingertips behind) · focus on the strap only | cutout · EG04 · EG01 | NBP | — |

#### Hook 2

| Beat | Phrase | Type | Subject | Location | Day | Action · pace | Camera · staging · pin | Angle (height · side · scale · fg) — why | Focus | Light key | Key word | Product | Layout · EG | Model | Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TH-HK2 | HK2-01, HK2-02 | TH | D | L-D-CONS | D-D1 | leans in a touch on 'before you come and see me'; one flat hand down on the desk on 'not a prescription' · ~155 wpm | phone on a small tripod across the desk, locked off · seated at his desk · no | eye · front · MCU · clean | eyes, medium | L · 6500K |  | absent | spine (under every B-roll) · EG01 | HeyGen Avatar V | — |
| HK2-02a | HK2-02 | BR | P | L-P-FRONT | P-D1 | slides the closed strap up her LEFT shin and seats it under the kneecap (SEAT_LOCK) · one slide, 3s | sway · seated on the chair edge (§27G: one action, both hands on the shell) · yes | low · three-quarter · MEDIUM · clean — low = capable: ten seconds, done | product, medium | R · 6500K | ten | worn · VISIBLE (skirt, seated) · SEATING (§9B) · first appearance | pip · EG02 · EG01 | NBP | — |

#### Hook 3

| Beat | Phrase | Type | Subject | Location | Day | Action · pace | Camera · staging · pin | Angle (height · side · scale · fg) — why | Focus | Light key | Key word | Product | Layout · EG | Model | Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HK3-01a | HK3-01 | BR | D hand | L-D-CONS | D-D1 | drops one more knee X-ray onto the heap of scans burying his desk · one drop, 2s | sway · hands (§27G: one action, the film falls) · no | overhead · front · MEDIUM · clean — overhead = routine: every week, another one | deep, deep | L · 6500K | scan | absent | full · EG05 · EG01 | NB2 | — |
| TH-HK3 | HK3-01, HK3-02 | TH | D | L-D-CONS | D-D1 | lowers the X-ray to the desk; a small shake of the head on 'a different question' · ~155 wpm | phone on a small tripod across the desk, locked off · seated at his desk · no | eye · front · MCU · clean | eyes, medium | L · 6500K |  | absent | spine (under every B-roll) · EG01 | HeyGen Avatar V | — |

#### Act 1

| Beat | Phrase | Type | Subject | Location | Day | Action · pace | Camera · staging · pin | Angle (height · side · scale · fg) — why | Focus | Light key | Key word | Product | Layout · EG | Model | Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TH-A1 | B-01, B-02, B-03, B-04, B-05 | TH | D | L-D-CONS | D-D1 | measured; taps just under his own kneecap through the trousers on 'press' · ~155 wpm | phone on a small tripod across the desk, locked off · seated at his desk · no | eye · front · MCU · clean | eyes, medium | L · 6500K |  | absent | spine (under every B-roll) · EG01 | HeyGen Avatar V | — |
| BR-01 | B-01 | BR | P | L-P-KITCH | P-D1 | at the kitchen table, both hands round a mug, rubs her LEFT knee once · one rub, 3s | sway · sitting · no | eye · three-quarter · MEDIUM · clean | eyes, medium | R · 6500K | patient | absent | cutout · EG04 · EG01 | NB2 | — |
| MECH-01 | B-01 | MECH | anatomy | — | MECH | ANAT: the LEFT knee joint worn bone on bone, the right knee behind it starting to redden · a slow turn, 3s | RV render · none · no | eye · three-quarter · MCU · clean | deep, deep | L · 5600K | bone | absent | pip · EG02 · EG07 | NB2 | — |
| BR-02 | B-02 | BR | D hands | L-D-CONS | D-D1 | clips her knee X-ray onto the window glass · one clip, 2s | sway · hands · no | low · three-quarter · CU · clean — low = the scan looms over us | foreground, medium | back · 6500K | scan | absent | pip · EG02 · EG01 | NB2 | — |
| MECH-03 | B-03 | MECH | anatomy | — | MECH | ANAT-A: the patellar tendon below the kneecap lights red as one band, one step lands on it · one step, 3s | RV render · none · no | eye · profile · CU · clean — profile = the band's side view under the kneecap | deep, deep | L · 5600K | tendon | absent | split 60/40 · EG03 · EG07 · 17× card | NB2 | — |
| BR-04 | B-04 | BR | P hand | L-P-FRONT | P-D1 | her forefinger presses into the soft spot just under her LEFT kneecap, the skirt hem lifted clear of the knee · one press, 2s | sway · hands · no | high · front · ECU · clean — high = the viewer's own look down at their knee | hands, medium | L · 6500K | press | absent | pip · EG02 · EG06 red arrow | NB2 | — |
| BR-05a | B-05 | BR | P | L-P-HALL | P-D1 | climbs one stair away from camera, steady, hand on the banister · one step, 2s | sway · stairs ascending (§27G: one step) · no | eye · behind · FULL · clean — behind = going up is the easy way, she leaves us | deep, deep | R · 6500K | up | absent | cutout · EG04 · EG01 | NB2 | — |
| BR-05b | B-05 | BR | P | L-P-HALL | P-D1 | comes down one stair, both hands on the banister, the LEFT knee braced as it catches · one step, 2s | locked-off sway · stairs descending (§27G: camera at the foot, hand on rail) · no | low · three-quarter · FULL · clean — low = the stair looms; coming down is the hard way | deep, deep | R · 6500K | Coming | absent | cutout · EG04 · EG01 | NB2 | — |
| MECH-05 | B-05 | MECH | anatomy | — | MECH | ANAT-A step-down: the thigh lengthens to catch, the catch lands on the band, a red flash · one catch, 3s | RV render · none · no | low · three-quarter · MCU · clean — low = the weight arriving | deep, deep | L · 5600K | catch | absent | split 60/40 · EG03 · EG07 | NB2 | — |

#### Act 2

| Beat | Phrase | Type | Subject | Location | Day | Action · pace | Camera · staging · pin | Angle (height · side · scale · fg) — why | Focus | Light key | Key word | Product | Layout · EG | Model | Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TH-A2 | B-06, B-07, B-08, B-09, B-10 | TH | D | L-D-CONS | D-D1 | quieter on the list; slower and lower on 'where the load was landing' (stress register) · ~155 wpm | phone on a small tripod across the desk, locked off · seated at his desk · no | eye · front · MCU · clean | eyes, medium | L · 6500K |  | absent | spine (under every B-roll) · EG01 | HeyGen Avatar V | — |
| BR-06 | B-06 | BR | P | L-P-HALL | P-D1 | comes down her stairs BACKWARDS, facing the steps, both hands on the banister · one step back, 3s | locked-off sway · stairs descending backwards (§27G: one step, both hands on rail, camera at the foot) · no | high · three-quarter-back · FULL · clean — high + three-quarter-back = small, careful, from the landing | deep, deep | R · 6500K | backwards | absent | cutout · EG04 · EG01 | NB2 | — |
| BR-07 | B-07 | BR | P | L-P-FRONT | P-D1 | rocks forward in the low fireside armchair, hands on the wooden arms, to stand — the first try, sinks back · one rock, 3s | sway · sit-to-stand (§27G: one action, hands on the arms) · no | eye · profile · MEDIUM · clean — profile = the effort side-on | eyes, medium | L · 6500K | chair | absent | cutout · EG04 · EG01 | NB2 | — |
| BR-08 | B-08 | BR | P legs | L-P-HALL | P-D1 | steps up onto the bottom stair RIGHT leg first, the left trailing · one step, 2s | locked-off sway · stairs ascending (§27G: one step) · no | ground · three-quarter · CU · clean — ground = the leg she leads with | deep, deep | R · 6500K | good | absent | cutout · EG04 · EG01 | NB2 | — |
| BR-09a | B-09 | BR | object | L-P-HALL | P-D1 | the brown walking boots on the newspaper by the door, laces dusty · still, 2s | slow sway · none · no | low · front · CU · clean — low = the boots, left waiting | foreground, medium | L · 6500K | walk | absent | pip · EG02 · EG01 | NB2 | — |
| BR-09b | B-09 | BR | P | L-P-KITCH | P-D1 | at the sink, looks out at the overgrown garden, a mug in her hand · one look up, 2s | sway · standing · no | eye · three-quarter-back · MEDIUM · through — three-quarter-back + through = the garden past her, out of reach | deep, background | back · 6500K | garden | absent | cutout · EG04 · EG01 | NB2 | — |
| BR-09c | B-09 | BR | family (one-offs FM-01 daughter, FM-02 grandson) + P | L-P-DOOR | P-D1 | P opens her front door to her daughter and grandson on the step · the door opens, 2s | sway · standing (§27G: no step) · no | eye · ots · MEDIUM · clean — OTS = from inside, the family comes to her | eyes, medium | L · 6500K | family | absent | cutout · EG04 · EG01 | NB2 | — |
| BR-10 | B-10 | BR | P | L-P-FRONT | P-D1 | seated in the armchair, pulls a blank physio band against her foot, carefully · one pull, 3s | sway · sitting · hands · no | high · three-quarter · MEDIUM · clean — high = how hard she tried | hands, medium | L · 6500K | tried | absent | cutout · EG04 · EG01 | NB2 | — |

#### Act 3

| Beat | Phrase | Type | Subject | Location | Day | Action · pace | Camera · staging · pin | Angle (height · side · scale · fg) — why | Focus | Light key | Key word | Product | Layout · EG | Model | Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TH-A3 | B-11, B-12, B-13, B-14, B-15 | TH | D | L-D-CONS | D-D1 | counts the three on his fingers; lifts the strap from the desk into frame on 'This does' · ~155 wpm | phone on a small tripod across the desk, locked off · seated at his desk · no | eye · front · MCU · clean | eyes, medium | L · 6500K |  | absent | spine (under every B-roll) · EG01 | HeyGen Avatar V | — |
| BR-11a | B-11 | BR | object | L-P-KITCH | P-D2 | a black stretchy knee sleeve squeezed flat in a hand (blank, no brand) · one squeeze, 2s | sway · hands · no | eye · front · CU · clean | hands, medium | R · 5600K | sleeve | absent | pip · EG02 · EG06 crossed-out list | NB2 | — |
| BR-11b | B-11 | BR | object | L-P-KITCH | P-D2 | a grey hinged knee brace flexes on the table — the hinge swings side to side (blank) · one tilt, 2s | sway · hands · no | low · profile · CU · clean — low + profile = the hinge's sideways travel | foreground, medium | R · 5600K | hinged | absent | pip · EG02 · EG06 crossed-out list | NB2 | — |
| BR-11c | B-11 | BR | P hand | L-P-KITCH | P-D2 | rubs white gel from a plain unlabelled tube onto her knee skin · one rub, 2s | sway · hands · no | high · three-quarter · CU · clean — high = sits on the skin, from above | hands, medium | R · 5600K | gel | absent | pip · EG02 · EG06 crossed-out list | NB2 | — |
| PR-12 | B-12 | PRODUCT | P hand | L-P-KITCH | P-D2 | holds the strap up in the window light, pinched at the shell's bottom edge (HELD) · a quarter turn, 2s | sway · hands · yes — product turns | eye · front · CU · clean | product, medium | R · 5600K | Stryde | held (HELD_GRIPS) · first appearance | full · EG05 · EG01 | NBP | — |
| BR-13 | B-13 | BR | P | L-P-FRONT | P-D2 | sits on the armchair edge, LEFT leg straight, strap seated under the kneecap · still, one breath, 2s | sway · sitting · no | eye · three-quarter · CU · clean | product, medium | L · 5600K | below | worn · VISIBLE (W-L-FRONT) | split 60/40 · EG03 · EG01 | NBP | — |
| MECH-14 | B-14 | MECH | anatomy | — | MECH | ANAT-A relief: the pad holds the one band, the red on the tendon cools to blue · one step, 3s | RV render · none · no | low · three-quarter · MCU · clean — low = the catch holds | deep, deep | L · 5600K | pad | absent | split 60/40 · EG03 · EG07 | NB2 | — |
| BR-15 | B-15 | BR | D hand | L-D-CONS | D-D1 | his fingertip sets on the tendon just under the kneecap of the desk knee model, then lifts a centimetre · one tap, 2s | sway · hands · no | high · three-quarter · ECU · clean — high = the placement from above | hands, medium | L · 6500K | placement | absent | pip · EG02 · EG01 | NB2 | — |

#### Act 4

| Beat | Phrase | Type | Subject | Location | Day | Action · pace | Camera · staging · pin | Angle (height · side · scale · fg) — why | Focus | Light key | Key word | Product | Layout · EG | Model | Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TH-A4 | B-16, B-17, B-18, B-19, B-20 | TH | D | L-D-CONS | D-D1 | hands flat on the desk on 'I do not sell these'; eyebrows up on 'You will know in a minute' · ~155 wpm | phone on a small tripod across the desk, locked off · seated at his desk · no | eye · front · MCU · clean | eyes, medium | L · 6500K |  | absent | spine (under every B-roll) · EG01 | HeyGen Avatar V | — |
| BR-16a | B-16 | BR | surgeon (one-off SG-01, §19B approachable) | L-ORTHO | X-D1 | turns the strap in his hand beside a knee model · one turn, 2s | sway · hands · yes — product turns | eye · three-quarter · MCU · clean | product, medium | R · 5600K | orthopedic | held | pip · EG02 · EG06 34% card | NBP | — |
| BR-16b | B-16 | BR | walkers (one-offs WK-01) | L-TOWPATH | X-D1 | a line of older walkers' legs passes on a towpath, a strap on each near knee · they cross frame, 3s | locked-off · walking across frame (§27G: camera never travels) · no | ground · profile · MEDIUM · clean — ground = the steps of many | deep, deep | L · 5600K | Two | worn · VISIBLE | cutout · EG04 · EG06 200,000 card | NBP | — |
| BR-17a | B-17 | BR | P | L-P-HALL | P-D2 | sitting on the bottom stair, seats the strap on her LEFT knee in one slide up (SEAT_LOCK) · one slide up, 2s | sway · seating (SEAT_LOCK: only ever up) · yes — ends seated | high · three-quarter · CU · clean — high = quick and easy | product, medium | R · 5600K | Ten | seated · VISIBLE | split 60/40 · EG03 · EG01 | NBP | F6 |
| BR-17b | B-17 | BR | P | L-P-HALL | P-D2 | stands and lets the rolled trouser leg fall; it lies flat over the strap · one drop, 2s | sway · standing · no | low · three-quarter · CU · clean — low = the flat line of the trouser | product, medium | R · 5600K | nobody | worn · REVEAL→CONCEALED (§9D) | split 60/40 · EG03 · EG01 | NBP | F6 |
| BR-19a | B-19 | BR | P | L-P-HALL | P-D2 | at the top of the stairs, trousers rolled above both knees: strap on the LEFT knee, the right bare · still, a breath, 2s | sway · standing on a landing (§27G: no step) · no | high · front · MEDIUM · clean — high = the drop of the stairs below her | product, medium | R · 5600K | One | worn · VISIBLE, one knee only | cutout · EG04 · EG01 | NBP | F4 |
| BR-19b | B-19 | BR | P | L-P-HALL | P-D2 | comes down the stairs forwards, one step at a time, hand light on the banister · two steps, 3s | locked-off sway · stairs descending (§27G: camera at the foot, hand on rail) · no | low · front · FULL · clean — low = the mirror of BR-05b, now easy | deep, deep | R · 5600K | forwards | worn · VISIBLE | full · EG05 · EG01 | NBP | F4 |
| BR-20 | B-20 | BR | D | L-D-CONS | D-D1 | holds two identical knee X-rays up side by side to the window · still, 2s | sway · standing at the window (§27G: no travel) · no | eye · three-quarter-back · MCU · through — three-quarter-back + through = we read both scans over his shoulder | background, medium | back · 6500K | both | absent | split 60/40 · EG03 · EG01 | NB2 | F3 |

#### Act 5

| Beat | Phrase | Type | Subject | Location | Day | Action · pace | Camera · staging · pin | Angle (height · side · scale · fg) — why | Focus | Light key | Key word | Product | Layout · EG | Model | Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TH-A5 | B-21, B-22, B-23 | TH | D | L-D-CONS | D-D1 | slow and certain on 'move the load'; the last line straight to lens, a small nod · ~155 wpm | phone on a small tripod across the desk, locked off · seated at his desk · no | eye · front · MCU · clean | eyes, medium | L · 6500K |  | absent | spine (under every B-roll) · EG01 | HeyGen Avatar V | — |
| PR-22a | B-22 | PRODUCT | object | L-P-KITCH | P-D2 | the open box on the kitchen table: two straps side by side in the insert (package_open) · still; a hand settles the lid, 2s | sway · none · no | overhead · front · CU · clean — overhead = what's in the box | product, medium | R · 5600K | Two | box open, two units (OFFER) | pip · EG02 · EG06 60-day seal | GPT Sunburst | — |
| BR-22b | B-22 | BR | copy (one-off CP-01 leg) | L-P-KITCH | P-D2 | a stretched grey near-copy strap sags down a shin · one slow sag, 2s | sway · none; blank near-copy (FAKE_BASE) · no | low · profile · CU · clean — low + profile = the sag | foreground, medium | R · 5600K | stretch | near-copy (FAKE_BASE) | pip · EG02 · EG01 | NBP | F7 |
| BR-23 | B-23 | BR | P | L-P-HALL | P-D2 | comes down her stairs forwards, hands free, a small smile, strap on the LEFT knee · two steps, 3s | locked-off sway · stairs descending (§27G: camera at the foot, hand near the rail) · no | low · three-quarter · FULL · clean — low = the mirror of BR-06's high angle: now she owns the stairs | deep, deep | R · 5600K | stairs | worn · VISIBLE | full · EG05 · EG01 | NBP | — |


**`angles.py` (§30I–§30K): PASS** on 44 rows (8 TH skipped as mount-locked). Setups: low/three-quarter ×6 · high/three-quarter ×5 · eye/three-quarter ×4 · low/front ×3 · high/front ×3 · eye/profile ×3 · eye/three-quarter-back ×2 · eye/front ×2 · low/profile ×2 · eye/behind · high/three-quarter-back · ground/three-quarter · eye/OTS · ground/profile · overhead/front. Rows: `work/angles_rows.json`; the map is generated by `work/actmap.py`.

### Visual Instruction Ledger — assigned (§27F)

| ID | Carried by | Status |
|---|---|---|
| VN01 "Result first, triple without — the reference's construction" | TH-HK1 + HK1-01a (her result in a PiP box, EG02) + HK1-02a (the drawer, EG04) | assigned, verified at your check |
| VN02 "his own interest" | D-DOC (a man) | verified |
| VN03 "The scan" | HK3-01a (he reads the X-ray at the window) | assigned |
| VN04 reference link | `EDIT-DFA` layouts on every row | assigned |
| EG06 overlays (§17) | 17× (MECH-03), red arrow (BR-04), crossed-out list (BR-11a–c), 34% + 200,000 (BR-16a/b), 60-day seal (PR-22a) | assigned (CapCut) |

### Wardrobe map (§21, §14A) — one outfit per story day

| Day | Subject | BASE | MID / OUTER | LOWER | FOOT | ACCENT | Colour family | Beats |
|---|---|---|---|---|---|---|---|---|
| D-D1 | D | pale blue button-down shirt, open collar, no tie | white knee-length doctor's coat, open; black stethoscope *(sheet: TH wardrobe lock)* | charcoal wool trousers | brown leather lace-ups | a plain steel watch | white / pale blue / charcoal | TH-HK1…TH-A5, HK2-02a, HK3-01a, BR-02, BR-15, BR-20 |
| P-D1 | P | cream fine-knit roll-neck | oatmeal cable-knit cardigan, buttoned once | knee-length plum wool skirt, bare legs | burgundy fleece-lined slippers | reading glasses on a cord round her neck | plum / oatmeal / cream | HK1-02a, BR-01, BR-04, BR-05a/b, BR-06–BR-10, BR-09c |
| P-D2 | P | white cotton shirt, sleeves turned back | coral lightweight cardigan, open | wide-leg navy linen trousers (rolled above both knees on the worn beats, down on HK1-01a and BR-17b) | tan leather flat loafers | small gold hoop earrings | navy / coral / white | HK1-01a, BR-11a–c, PR-12, BR-13, BR-17a/b, BR-19a/b, PR-22a, BR-23 |
| one-offs | SG-01 surgeon (§19B approachable, navy scrubs) · WK-01 walkers (outdoor shorts, bare knees) · FM-01 daughter (40s, rain jacket), FM-02 grandson (8, school jumper) · CP-01 copy leg | each its own single day (D5) | | | | | | BR-16a, BR-16b, BR-09c, BR-22b |

**Novelty (§14A):** no outfit repeats across days, and P never wears her sheet outfit (duck-egg jumper, check skirt). The strap is worn on bare skin on every worn beat.

## Next

1. **You:** Confirm or Fix the two avatars, the four plates and the three left-knee references on the board.
2. **Me, straight through (§22U, no stop):** the doctor's voice-source frame (`nano_banana_pro`, D in P3), two Kling 10s takes with `VOICE-DOC` → `voice_source.py` → clone by API → Enhance → `eleven_v4` VO for HK1–HK3 + body → house cut → HeyGen talking heads (TH rows) → E11 trim. This starts once D-DOC and P3 are confirmed (the voice frame is built from them).
3. Then the hooks one by one (step 6).
