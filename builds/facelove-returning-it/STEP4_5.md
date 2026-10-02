# facelove-returning-it — Steps 4–5 (Manual)

Built against the **confirmed avatars** (user, 2026-10-02 "confirm and proceed"): N-BEFORE v2 · N-AFTER v1. The step 1–3 flags were not answered, so they are held on my defaults: **3 hooks** (F3), "Prime Sale" voiced as written (F7), offer as written (F8), the avatar's hair kept (F9).

**On the board as To check:** 5 location plates (16:9) and 2 side-cast sheets (C1 the counter saleswoman, C2 the friend who asks). The act map below is **planned**. No beat image is generated until the plates are confirmed, and every B-roll `duration` stays `pending-master` until the voice master exists (E6).

---

## Step 4 — Property, locations and light (§30C, §30G, §30K)

### Location Derivation Pass

| ID | Location | Owner | Beats | Tier | Plate |
|---|---|---|---|---|---|
| **L-VANITY** | her bedroom vanity — the talking-head set and every demo and offer beat (one sitting, today) | N | TH-01…TH-08 (+ hooks), B01–B03, B06–B08, B13–B16 | **PLATED** | L-VANITY |
| **L-HALL** | her front hall, the round brass mirror and the walnut door (property plate) | N | B11 | **PLATED** + property | P-HOME |
| **L-FRONT** | the front of her house, the path to the drive | N | B12 | **PLATED** | L-FRONT |
| **L-COUNTER** | a department-store makeup counter (flashback, weeks ago) | GENERIC | B04, B05 | **PLATED** | L-COUNTER |
| **L-CAFE** | a neighbourhood café table by the window (this week) | GENERIC | B09, B10 | **PLATED** | L-CAFE |

### Property Sheet (§30G, fields 1–4) — PROP-H, her house

| Field | PROP-H |
|---|---|
| 1 Type and era | 2000s single-storey cream stucco ranch-style house, terracotta tile roof, suburb of San Antonio, Texas |
| 2 Shell | warm off-white drywall, faint orange-peel texture · plain white baseboards · flat white casings · white two-panel shaker doors, brushed-nickel levers · flat white ceilings, brushed-nickel flush lights · **warm-beige porcelain tile in the hall → oatmeal carpet in the bedroom** · white ceiling vents · white decora switches |
| 3 Floor map | walnut front door → the hall (console, round brass mirror, key bowl on the left) → the main bedroom on the right: the vanity faces into the room, the window on its left-hand wall |
| 4 Orientation | front door faces **east** (morning sun); bedroom window faces **west** (late-afternoon light) |

### Light plans (§30K)

| Location | Source | Key (this build) | Kelvin |
|---|---|---|---|
| L-VANITY | west window, sheer curtains, camera-left | late afternoon, soft (REC) | 5000 |
| L-HALL | frosted panel beside the front door | morning (D2) | 5600 |
| L-FRONT | open sky, sun from the east | morning sun (D2) | 5600 |
| L-COUNTER | store ceiling downlights | afternoon, flat cool (D0) | 4000 |
| L-CAFE | big front window, camera-left | midday (D1) | 5600 |

**Light arc (Mode 1, daylight, never moody):** a flat cool store for the flashback, bright midday and morning for the after days, and soft warm late-afternoon window light for the recording.

### Plates (on the board, To check)

Higgsfield `gpt_image_2_5` · `sunburst` · `high` · `2k` · **16:9** (2688×1520) · empty, no people, no product, one render each, ODAQ B.V. Prompts in `plates/<ID>.prompt.txt` (`plates/build_plates.py`, Appendix A by ID).

| ID | Location | Job |
|---|---|---|
| P-HOME | front hall + mirror + walnut door | 3427141d |
| L-VANITY | bedroom from the vanity (talking-head set) | 195ccd70 |
| L-COUNTER | department-store makeup counter | 0a1ed1e5 |
| L-CAFE | café table by the window | 9e320cb2 |
| L-FRONT | front of the house, path, drive | 059ff154 |

### Side cast (§19) — people in more than one beat

| ID | Who | Beats | Job |
|---|---|---|---|
| C1-COUNTER | Korean American saleswoman, 29, sleek low bun, black work tunic | B04, B05 | 399b12ef |
| C2-FRIEND | white American friend, 44, copper-auburn bob, freckles, olive linen shirt | B09, B10 | 63089696 |

C3 and C4 (the two other friends in B09 only) are one-offs, each described in her own clause (L55): C3 a Black American woman in her 40s, short natural curls, a Breton top; C4 a South Asian American woman in her 50s, a long grey-streaked braid, a mustard cardigan.

---

## Step 5 — Act map, wardrobe, Visual Pitch, music

### Act map (`step5/act_map.json`, 24 rows: 16 B-roll + 8 talking heads; hooks at step 6)

Talking heads are one sitting at the vanity. The hooks are on her bare face (N-BEFORE); after the application B-roll, the body is on her finished face (N-AFTER). B-roll is one picture per phrase, full screen.

| Beat | Act | Line (phrase) | Type | Day | Location | Picture (action) | Angle | Face |
|---|---|---|---|---|---|---|---|---|
| B01 | Act 1 | And it is not because it goes on pure white | BR | REC | L-VANITY | the balm end's flat crest presses onto her bare right cheekbone and draws one short stroke toward the ear, leaving a clean white stripe | eye · three-quarter · ECU | N-BEFORE |
| B02 | Act 1 | and then turns into my exact shade | BR | REC | L-VANITY | the brush end sweeps through the white stripe in two small circles; behind the crown the white turns to her olive skin, ahead of it it stays white | eye · profile · ECU | N-BEFORE |
| B03 | Act 1 | and melts in like it was made for my skin. | BR | REC | L-VANITY | two fingertips pat the blended cheek twice and leave it; the cheek is one even tone, her crow's feet still there; her eyes go to the lens | low · three-quarter · CU | N-AFTER |
| B04 | Act 1 | Even the woman at the makeup counter | BR | D0 | L-COUNTER | she sits on the stool at the counter; the saleswoman behind the counter, back of her shoulder in frame, holds a foundation bottle up beside her jaw and tilts her head | eye · ots · MEDIUM | N-BEFORE |
| B05 | Act 1 | told me my redness was too tricky to match | BR | D0 | L-COUNTER | three short swatch stripes of different beige foundations on her jawline, none matching the redness around them; the saleswoman's hand with a sponge lowers out of frame | high · three-quarter · CU | N-BEFORE |
| TH-01 | Act 1 | and I should not bother. | TH | REC | L-VANITY | talking head to the lens (N-AFTER) | selfie, eye level | after |
| B06 | Act 2 | It is not because it covered the redness, | BR | REC | L-VANITY | her left cheek half done: the brush crown crosses from the blended even side into the red side and stops on the border | eye · front · ECU | mid |
| B07 | Act 2 | the hyperpigmentation, the old post-acne marks, | BR | REC | L-VANITY | the balm crest glides once along her jawline over the small brown marks, leaving a thin white line on them | low · three-quarter · ECU | N-BEFORE |
| B08 | Act 2 | and every tired line and dark circle | BR | REC | L-VANITY | the side of the brush crown pats under her right eye twice; the dark circle evens out, the crow's feet stay exactly where they were | high · three-quarter · ECU | mid |
| TH-02 | Act 2 | I have been hiding for years, in one swipe. | TH | REC | L-VANITY | talking head to the lens (N-AFTER) | selfie, eye level | after |
| B09 | Act 2 | And it is definitely not because three of my friends this week | BR | D1 | L-CAFE | the three friends round the café table lean in toward her at once, coffees in hand, looking at her face | eye · ots · MEDIUM | N-AFTER |
| B10 | Act 2 | asked what I am using, | BR | D1 | L-CAFE | the auburn friend touches her own cheek with two fingers and raises her brows, eyes on the creator just off the lens | eye · three-quarter · MCU | — |
| TH-03 | Act 2 | because my skin looks so even. | TH | REC | L-VANITY | talking head to the lens (N-AFTER) | selfie, eye level | after |
| TH-04 | Act 3 | It is not because I can finally skip a full face of makeup, | TH | REC | L-VANITY | talking head to the lens (N-AFTER) | selfie, eye level | after |
| B11 | Act 3 | throw this one stick on before the grocery store, | BR | D2 | L-HALL | keys hooked on one finger, she swipes the balm end once across her cheek in the round brass mirror and caps it | eye · three-quarter · MCU | N-AFTER |
| B12 | Act 3 | and feel completely confident walking out the door. | BR | D2 | L-FRONT | she pulls the walnut door shut behind her and walks two steps down the path toward the lens, tote on her shoulder, chin up | low · front · FULL | N-AFTER |
| TH-05 | Act 4 | No. I am returning this one, because after I bought it, I found out it is the last day of the Prime Sale. Sixty percent off. | TH | REC | L-VANITY | talking head to the lens (N-AFTER) | selfie, eye level | after |
| B13 | Act 4 | Two full Foundation Sticks for almost the price of one, | BR | REC | L-VANITY | her hand sets a second closed stick down upright beside the first on the white vanity top, both wordmarks to the lens | high · front · CU | — |
| B14 | Act 4 | plus a free primer, a mystery gift, | BR | REC | L-VANITY | her hand sets the primer and then the small mystery gift box beside the two sticks | eye · three-quarter · CU | — |
| TH-06 | Act 4 | free shipping, and a full thirty day money back guarantee. | TH | REC | L-VANITY | talking head to the lens (N-AFTER) | selfie, eye level | after |
| B15 | Act 4 | So I am sending back my one, | BR | REC | L-VANITY | her hands slide the one closed stick back into its carton and push the carton into a plain grey return mailer | overhead · front · CU | — |
| TH-07 | Act 4 | and buying the deal like I should have. | TH | REC | L-VANITY | talking head to the lens (N-AFTER) | selfie, eye level | after |
| TH-08 | Act 5 | So do not do what I did and pay for one. If you have not tried this yet, tap the link and grab the deal before midnight, because once the Prime Sale ends tonight, it is gone. | TH | REC | L-VANITY | talking head to the lens (N-AFTER) | selfie, eye level | after |
| B16 | Act 5 | It was never your skin. It was the formula. | BR | REC | L-VANITY | she lifts the closed stick up beside her even cheek, wordmark to the lens, and holds it; every line of her face still there | eye · three-quarter · MCU | N-AFTER |

`angles.py` **PASS** (9 setups, focus, light) · `wardrobe.py` **PASS** (4 story days) · `visual_plan.py` **PASS**.

### Wardrobe map — per story day and event (§21, V7.89)

One block per story day, in story order: the event, what makes it a day, each person's outfit, and the day's events with their beats. Never grouped by act (§21, V7.89.0).

### D0 — the makeup-counter visit, weeks before

*Why it is a day:* stated: 'Even the woman at the makeup counter told me'

| Who | Outfit |
|---|---|
| the creator | a camel wool-blend coat open over a cream ribbed sweater, dark straight jeans, bare face (N-BEFORE) |
| counter saleswoman | sheet outfit: black fitted short-sleeved work tunic, slim black trousers, black flats |

| Event | Place | Beats |
|---|---|---|
| D0-E1 | L-COUNTER · VISIBLE | B04, B05 |

### D1 — coffee with three friends, this week

*Why it is a day:* stated: 'three of my friends this week asked what I am using'

| Who | Outfit |
|---|---|
| the creator | a terracotta cotton knit top with three-quarter sleeves, small gold hoop earrings, white jeans, the stick on (N-AFTER) |
| auburn friend | sheet outfit: olive linen shirt, sleeves rolled, light-wash jeans |
| friend 2 | a navy-and-white Breton striped top (a Black American woman, 40s, short natural curls) |
| friend 3 | a mustard cardigan over a white T-shirt (a South Asian American woman, 50s, long grey-streaked braid) |

| Event | Place | Beats |
|---|---|---|
| D1-E1 | L-CAFE · VISIBLE | B09, B10 |

### D2 — the grocery-store morning, this week

*Why it is a day:* stated: 'throw this one stick on before the grocery store'

| Who | Outfit |
|---|---|
| the creator | a plain white crew-neck T-shirt, an olive cotton utility jacket, light-wash jeans, white leather sneakers, a tan canvas tote (N-AFTER) |

| Event | Place | Beats |
|---|---|---|
| D2-E1 | L-HALL · VISIBLE | B11 |
| D2-E2 | L-FRONT · VISIBLE | B12 |

### REC — today, the last day of the sale — filming at her vanity

*Why it is a day:* stated: 'it is the last day of the Prime Sale… ends tonight'

| Who | Outfit |
|---|---|
| the creator | sheet outfit: the cream-white sherpa robe over a white camisole |

| Event | Place | Beats |
|---|---|---|
| REC-E1 | L-VANITY · VISIBLE | B01, B02, B03, B06, B07, B08, B13, B14, B15, B16 |

### Talking heads — per recording day

| Recording day | Who | Outfit | Beats |
|---|---|---|---|
| REC | the creator | the cream-white sherpa robe over a white camisole (one sitting: bare face on the hooks, N-AFTER on the body) | TH-01, TH-02, TH-03, TH-04, TH-05, TH-06, TH-07, TH-08 |

### Visual Pitch (§30M) — `step5/visual_plan.md`

One hero per act: **B02** (white turns to her shade behind the brush) · **B06** (the half-done cheek) · **B12** (out of the door, chin up) · **B13** (the second stick set down) · **B16** (the stick beside her finished face). Swap any pick by its beat and letter.

### Music Register Map (§40A)

| Part | Lines | Register | Placement |
|---|---|---|---|
| Hooks + Act 1–2 (the first ~45 s) | L1–L3 | MUS-OPEN | — |
| Act 3 | L4 | MUS-AFTER | — |
| Act 4–5 (offer, CTA) | L5–L6 | MUS-OFFER | — |

**The inspo has no music (EG05), and the reference decides where music sits**, so this build carries **no music bed**: her voice and the room only. The map is recorded so a bed can be added on the team's call, in the registers above (`NEG-MUSIC`: nothing cute or upbeat under the fake-out).

### Ingredient / reference ledger

- Product: CLOSED, BALM END DEPLOYED, BRUSH END DEPLOYED (attachable); PACKAGING (B15); PRIMER, MYSTERY GIFT (B14); FACELOVE_REF_SHEET_01 is never attached.
- Faces: N-BEFORE v2 / N-AFTER v1 by row `face_state`; C1, C2 sheets; C3/C4 in words.

### Next — the voice (§22U), straight through in Manual
Voice frame N-VOICE-IMG (vanity, robe, N-AFTER; bare-face twin for the hooks) → two or more Kling voice-source takes → trim, ×1.2, join, loop ≥ 30 s → ElevenLabs IVC clone → Enhance → `eleven_v4` VO (hooks + body in one request) → HeyGen Avatar V talking heads → `trim.py`. Then placement (`assemble.py --lengths --sheet`), and the hooks at step 6.
