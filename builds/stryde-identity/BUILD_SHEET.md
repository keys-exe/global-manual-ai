# Build Sheet — stryde-identity

**STRYDE Precision Strap · "C - VID | AI VO | TOF | Identity Callout | New | A Must For"** · Standards V7.63.0 · **RUN: MANUAL** · 2026-09-26

Steps 1–3 of §18. **Stopped at the avatar review (§18B, V7.62.0)** — steps 4–5 wait for the user's go.

---

## 0. Intake (§18B, §18C)

| Input | Found | Notes |
|---|---|---|
| Drive folder | `1tKlZFjNApDMf5U_q3qFPcRyGZLQsVcwE` | fetched with `fetch_drive.py` → `intake/` |
| Inspo | `inspo_vogany.mp4` — Vogany shoe ad, Meta Ad Library ID 824173110747310 | 46.3s, 9:16, 360×640, audio |
| Script | `IDENTITY CALLOUT - A MUST FOR.docx` | title line 1 ✓ · 3 hooks + 12 body lines · 3 visual notes |
| Product Sheet | `stryde_product_sheet_V7.49.31.py` | stored as `products/stryde/` (Appendix B pair) |
| Product images | 10 — `front.webp`, `back.webp`, `product_tq_left/right`, `product_side`, `product_macro`, `worn_front/bent/rear`, `package_open` | layer 1; copied to `products/stryde/stryde_refs/` |
| Brief video | ClickUp clip "Shoe Ad Identity Strategy" (the `LOOM` role, §18C) | `fetch_loom.py` on the link returned a 9.5s 172×96 silent preview (the page's loading animation). The real file (47.4s, 1080p, audio) was found through the page's player and transcribed → `intake/loom/loom.md` |
| Missing | `package_closed.jpg`, anatomy samples, `product_held.jpg` | see `products/stryde/stryde_product_sheet.md` → Intake note. None blocks steps 1–3 |

**Message fields read:** `RUN: MANUAL`. **`BRITISH ETNICITY` → applied as a casting instruction: every character is cast white British** (it agrees with Product Sheet §8, "British, roughly 55–80"). `MODE` blank → **Mode 1**, because a realistic reference selects Mode 1 automatically (§22, §18A). `HOOKS` blank → **in script: 3**, so 3 variant videos (§30H). `CAP` blank → E0 Higgsfield default. `VOICE` blank → derived (§22D), British.

---

## 1. Absorption Sheet (§42)

### Part 1 — measured

| Instrument | Reading | Settles |
|---|---|---|
| Duration / aspect / res | 46.3s · 9:16 · 360×640 · 30fps | Short 9:16 ad; our build 9:16 locked |
| Scene cuts | **22 shots, mean 2.1s**; range 0.97–6.13s; cuts at 3.33 5.50 6.47 8.00 11.80 13.03 15.50 18.13 19.53 21.20 23.10 24.37 26.10 27.60 28.63 29.60 31.27 33.77 39.90 43.50 45.10 | Pacing: a cut every ~2s all the way through, no breathing section |
| Silence (−30/−40 dB) | one silence only, 45.93–46.33 (the tail) | **Wall-to-wall VO**, no held beats |
| Volume | mean −24.9 dB, max −3.4 dB | normal hot VO, no whisper register |
| VO transcript (faster-whisper) | 147 words / 46.2s = **191 wpm** | brisk read — see voice fingerprint |
| TH / B-roll | **0 talking heads**, 100% B-roll | voice-only build (§30H rule 4: no uncovered frame) |
| Shot frames + per-second sheets | `intake/frames/inspo_vogany/` | Edit Grammar below |
| Luminance timeline, OCR | not run by the instruments; overlays read off the frames | recorded as **read, not measured** |

### Part 2 — structure map

| Shot(s) | t | Type | What it shows | Layout | Overlay |
|---|---|---|---|---|---|
| S01 | 0.0–3.3 | **HOOK** | top: a man's hand presents the shoe to camera, face cropped at the chin · bottom: extreme close-up of the shoe worn, foot moving | **split 50/50** (EG01) | none |
| S02–S03 | 3.3–6.5 | proof (build story) | worn, walking on tile | full | none |
| S04 | 6.5–8.0 | authority | clinician in white coat, X-rays on the wall, holds the shoe open to the insole | full | none |
| S05–S07 | 8.0–13.0 | product | insole in hand; branded insole; cheap insole (comparison) | full | none |
| S08–S13 | 13.0–23.1 | lifestyle / mechanism | worn walking, product on table, insole flexed, foot-bone CGI, craftsman at bench | full | none |
| S14–S18 | 23.1–33.8 | demonstration | waterproof splash, lacing, water glass test, sofa, grass POV, shop shelf | full | none |
| S19 | 33.8–39.9 | authority + lifestyle run | white-coat clinician twists the shoe; pairs on a car bonnet; walking | full | none |
| S20–S22 | 39.9–46.3 | **OFFER / CLOSE** | CGI: foot heat-map, knee skeleton, red pain ring | full | **offer card** (EG04) |

### Part 3 — Style Lock (copied)

- **Delivery:** one unseen narrator, brisk (~191 wpm), plain declaratives, no pauses; hot, even level.
- **Edit rhythm:** hard cut every ~2s from the first second to the last; no act slows down.
- **Visual grammar:** hands and legs, faces almost never; product in every shot; handheld phone footage in real places; a clinician for authority; CGI anatomy only on the close.
- **Density:** 100% B-roll, zero talking head.
- **Retention:** identity call-out hook (who it is for) in a split screen that shows the product and the result at once; "unlike cheaper alternatives" at ~10s; "here's the best part" re-hook before the offer.
- **Capture axis (never yields):** the reference is phone footage; ours runs the iPhone 17 Pro Max register (§22).

### Part 3A — Edit Grammar → `EDIT-STRYDE-IDENTITY`

| ID | Device | Where | When used | Parameters |
|---|---|---|---|---|
| EG01 | **split** | S01 @ 0:00–0:03.3 | the hook line | two bands, **50/50, seam at mid-height**; top = the product presented to camera by hands (face cropped at the chin); bottom = extreme close-up of the product worn, in motion |
| EG02 | **full** B-roll, hard cut | S02–S22 | every body line | hard cuts only, 1–4s runs, one 6.1s run (S19) |
| EG03 | CGI anatomy under the close | S20–S22 @ 0:39.9–0:46.3 | offer / close | full-frame anatomy renders — the §12A register in our build |
| EG04 | **offer card** text overlay | S20–S22 @ ~0:42–0:46 | "best part" → offer | three centred lines in the lower third (~65–80% height): bullet + italic bold offer line with black stroke · white bold caps urgency line · URL in an outlined box. Our words, never theirs |
| EG05 | brand watermark | many B-roll shots | throughout | faint lowercase URL, top-centre. **Position-not-look; recommend omit** (§17) — flag, the user decides |
| — | not used by the reference | — | — | no captions, no punch-ins, no zoom/whip/flash transitions, no speed ramps, no SFX heard |

### Part 4 — script absorption

**Copy formula (reference):** identity call-out hook → build story ("three years to perfect") → orthopaedic credibility → "unlike cheaper alternatives" → features and comfort → doctors recommend → "here's the best part" → offer + urgency.

**Beat map — their `R-P` row → our script (the script was supplied already rewritten slot-for-slot; not edited, §42 Part 4 scope):**

| R-P | Reference (t) | Job | Our line |
|---|---|---|---|
| R-P-001 | "Why these shoes are a must for wide feet travelers?" (0.0–3.3) | hook | HK1 / HK2 / HK3 |
| — | — | agitate (added) | P-001–P-002 "seventeen times your bodyweight…" |
| R-P-002 | "took us three years to perfect" (3.3–5.5) | proof | P-003 |
| R-P-003 | "real orthopedic insoles that truly support" (5.5–9.3) | mechanism | P-004, P-006–P-007 |
| R-P-004 | "unlike cheaper alternatives that just pretend to" (9.3–11.8) | objection | P-005 |
| — | — | proof (added) | P-008–P-009 "Thirty-four percent less strain" |
| R-P-006 | "arch support … relieving pain" (15.5–23.0) | mechanism / result | P-010–P-015 |
| R-P-007/008 | materials; lightweight, hours without fatigue (23.0–35.7) | features | P-016–P-019 |
| R-P-009 | "Recommended by doctors" (35.7–38.2) | authority | P-020–P-021 |
| R-P-011 | "here's the best part. 60% off today, free delivery until midnight" (42.0–46.2) | offer | P-022–P-023 |
| — | — | risk reversal + close (added) | P-024–P-026 |

**Voice fingerprint (reference):** second person, short declaratives, fragments allowed, numbers spoken in words, product named "these shoes". Ours matches: "these knee straps", fragments ("No slipping. No sores."), numbers in words.

**Length:** hooks 15–16 words; body 176 words. At the reference's 191 wpm each variant runs **≈ 5s hook + ≈ 55s body ≈ 60s** — about 14s longer than the reference, carried by the same 2s cut rhythm (≈ 30 B-roll shots per variant).

### Part 5 — surfaced, not absorbed

| Reference element | Disposition |
|---|---|
| "60% off", "free delivery until midnight", "Limited stock!" | **replaced** — our offer is Buy 1 Get 1 Free (Product Sheet `OFFER`); urgency words only as the advertiser holds them |
| "Recommended by doctors", "real orthopedic" | their substantiation not inherited; ours are advertiser-held (claims table below) |
| Competitor insole (another brand's branded insole visible, S06) | **replaced** by our blank near-copy (§10, `FAKE_BASE` + one archetype) — never a real brand |
| CGI foot heat-map / pain ring | position-not-look → our §12A anatomical register (ANAT-A / ANAT-B, `ANATOMY_LOOK`) |
| Brand watermark (EG05) | recommend omit |

### Part 6 — beat-it plan

| Reference weakness | Our delta | Beats |
|---|---|---|
| One persona only ("wide feet travelers") | three identity call-outs → three variants, same body | HK1–HK3 |
| Mechanism named, never shown (foot CGI is decoration under the offer) | real §12A mechanism beats on the lines that argue it (load → pad catches → off the worn part) | P-001–P-002, P-006–P-007, P-015 |
| No numbers | 17× and 34% as post overlays (§17) | P-001, P-009 |
| No risk reversal | 60-day guarantee + "your own stairs will tell you" close, payoff on the stairs set up in HK1 | P-024–P-026 |

### Part 7 — confirmation

Reference-vs-rule conflicts are flagged at the end of this sheet (Flags). **Confirm or correct the absorption with the avatars.**

---

## 2. Script, product, claims, locks (step 2)

### Brief video (§18C) → ledger rows

`intake/loom/loom.md` — 7 spoken segments, 47.4s. Frames show the Meta Ad Library entry for the Vogany ad (the inspo). All instructions are whole-build:

| ID | Source | Instruction | Anchored |
|---|---|---|---|
| LM01–LM02 | @ 0:01–0:15 | "an identity call-out … same brand … replicate [this reference], let's do one of our own" | whole build — copy the reference's formula (§42) |
| LM03–LM07 | @ 0:16–0:44 | "Why these [shoes] are a must for …" — call out the specific personas: bone on bone · on your feet all day for work · can't keep up with your grandchildren | HK1, HK2, HK3 — **the script's three hooks already do exactly this; no conflict** ("shoes" is the reference's wording; the script says "knee straps" and the voice follows the script, §22U) |

### Visual Instruction Ledger (§27F) — opened

| ID | Source | Instruction | Line | Carried by | Status |
|---|---|---|---|---|---|
| VN01 | script | Top: an older man's hands, face cropped at the chin, hold the strap out and turn it to show the pad; knee X-ray on a lightbox behind him. Bottom: extreme close-up of a 70-year-old knee wearing the strap, stepping down a carpeted staircase at home; camera eases back to her hand resting on the rail | HK1 | split EG01 · top **C4 surgeon** · bottom **C1 Maureen** | open → step 5 · **flag F1** |
| VN02 | script | Top: work-gloved hands hold the strap out and turn it to the pad, warehouse shelving blurred. Bottom: extreme close-up of a 58-year-old's knee in work shorts wearing the strap, stepping off the back of a van, walking off with a box on his shoulder | HK2 | split EG01 · both bands **C2 Dean** | open → step 5 |
| VN03 | script | Top: a grandmother's hands (rings, cardigan cuff) hold the strap out, a child's scooter against the wall behind. Bottom: extreme close-up of her knee wearing the strap (cropped trousers), walking fast on a park path; camera eases back to a toddler on a scooter just ahead and her keeping up | HK3 | split EG01 · both bands **C3 Pat** | open → step 5 · **flag F2** |
| LM01–07 | brief | above | whole build / HK1–3 | the hooks as written | open → step 5 |

### Phrase inventory (§27B) — dispositions are assigned at step 5

| ID | Phrase | Job | Claim | Subject / register |
|---|---|---|---|---|
| HK1 | "Why these knee straps are a must if you've been told you're bone on bone." | hook | — | C4 + C1 (split) |
| HK2 | "Why these knee straps are a must if you're on your feet all day for work." | hook | — | C2 (split) |
| HK3 | "Why these knee straps are a must if you can't keep up with your grandchildren anymore." | hook | — | C3 (split) |
| P-001 | Because every step puts seventeen times your bodyweight | agitate | 17× (held) | mechanism — load |
| P-002 | through one small spot below your kneecap. | mechanism | — | mechanism — `[SITE]`, ANAT-A |
| P-003 | These straps took three years to build with orthopaedic surgeons, | proof | 3 yrs w/ surgeons (held) | C4 surgeon |
| P-004 | to sit right on that spot. | product | — | worn, front |
| P-005 | Unlike the cheap copies, which are too small to reach it. | objection | comparative (**unverified**, F4) | near-copy, `too small` archetype |
| P-006 | Inside, a silicone pad catches the force | mechanism | pad material (held) | `PAD_BACK_SHOT` then mechanism |
| P-007 | and moves it off the worn part, before it hits the joint. | mechanism | protection | ANAT-A |
| P-008 | Sports scientists measured it. | proof | — | one-off subject (sports scientist) |
| P-009 | Thirty-four percent less strain, every step. | proof | 34% (held) | worn, walking · 34% overlay |
| P-010 | Built for bone on bone, arthritis, | conditions | conditions (held) | ANAT-B |
| P-011 | worn cartilage and meniscus. | conditions | conditions (held) | ANAT-B |
| P-012 | So you walk further, | result | — | C3 Pat |
| P-013 | and take the stairs without gripping the rail. | result | — | C1 Maureen, stairs |
| P-014 | Not because the arthritis has gone. | honesty | — | C1 |
| P-015 | Because the force isn't landing where it hurts. | mechanism | protection | ANAT-A |
| P-016 | Adjustable. | feature | one size (held) | **seating beat** — never adjusting (`ADJUSTABLE_RULE`) |
| P-017 | No slipping. No sores. No rolling down. | feature | — | worn in motion |
| P-018 | It sits flat under your trousers, | feature | — | §9D conceal / reveal |
| P-019 | light enough to wear all day. | feature | — | C2 Dean at work |
| P-020 | Recommended by orthopaedic surgeons, | authority | held | C4 surgeon |
| P-021 | and worn by over two hundred thousand people. | social proof | 200,000 (held) | montage · overlay |
| P-022 | And the best part? | re-hook | — | box closed (needs `package_closed.jpg`, F7) |
| P-023 | It's two for the price of one today. | offer | BOGOF (held) | box open, two straps · offer card EG04 |
| P-024 | You get sixty days. | guarantee | 60 days (held) | — |
| P-025 | If it doesn't change your stairs, you get your money back. | guarantee | held | C1 stairs |
| P-026 | Put one on, and your own stairs will tell you. | close | — | seating beat → stairs |

Hooks 3 · body 26 phrases · **uncovered 0 · blocked 0** (dispositions pending step 5).

### Claims (§43A)

Every figure is **advertiser-held (user-confirmed V7.49.29)** per the Product Sheet claim register: 17× bodyweight · three years with orthopaedic surgeons · silicone pad · 34% less strain (sports scientists) · bone on bone / arthritis / worn cartilage / meniscus · recommended by orthopaedic surgeons · 200,000+ wearers · Buy 1 Get 1 Free · 60-day money-back. Numbers are post overlays, never generated (§17). **One line is not in the register:** P-005, "cheap copies … too small to reach it" (F4).

### Mode & Model Lock (§18A)

| Beat class | Model · params | Why |
|---|---|---|
| Mode | **Mode 1 Realistic**, iPhone 17 Pro Max, 9:16 | realistic reference (§22); no Mode 4/5 instruction |
| Avatar sheets | `gpt_image_2_5` · `variant: sunburst` · `quality: high` · `resolution: 2k` | measured route (§19) — **used this delivery** |
| Wordmark with hands or a body (held, worn, seating, split hooks) | `nano_banana_pro` | rule 7: no GPT Image with a body in frame |
| Wordmark, no person (box, pack, product) | `nano_banana_pro` | box lid wordmark must read |
| Volume B-roll with a person, no readable wordmark | `nano_banana_2` | volume |
| Mechanism A–C (ANAT-A, ANAT-B) | `nano_banana_2` | classifier threshold; no GPT Image |
| Narrator voice-source image (§22U step 1) | `nano_banana_pro` | talking-head seed class |
| Video | Kling 3.0 (`kling-video-v3_0_omni`), start image required; voice source per §22U | §4 |

**Other locks:** format **voice-only, 100% B-roll** (Style Lock: reference has zero talking heads — a style axis, it wins over §3A's talking-head default; say so to override) · **side: right knee** (no knee named in the script → `SIDE_RULE`) · mechanism claim: protection · edit: `EDIT-STRYDE-IDENTITY` · hooks: 3 in script → 3 variants.

---

## 3. Cast (step 3) — generated, checked, awaiting your decision

Recurring subjects (≥ 2 beats on the inventory): **C1 Maureen** (HK1 bottom, P-013/014, P-025/026) · **C2 Dean** (HK2 both bands, P-019) · **C3 Pat** (HK3 both bands, P-012) · **C4 surgeon** (HK1 top, P-003, P-020). Narrator **N** — unseen, but §22U needs his image for the voice source. One-off: the sports scientist (P-008), not sheeted (§13).

| Sheet | Job ID | File | Verdict (§19 panel check + §22V) |
|---|---|---|---|
| N-NARR | `366296a0-6fe1-4113-a189-b61eee326a0c` (v2) | `cast/N-NARR_v2.jpg` | **USE** — recast on the user's call: warm, open face, wavy dark-grey hair, salt-and-pepper beard, navy jumper; identity holds, window left. Chin cleft hidden by the beard. *v1 `75dd0c42…` replaced* |
| C1-MAUREEN | `fb41402a-b678-4282-921b-05bdd2ce71ef` | `cast/C1-MAUREEN_v1.jpg` | **USE** — identity holds, both knees bare, white curls in all five. **Crooked little finger not legible** (hands curled) |
| C2-DEAN | `f81be8b9-02ea-4513-bcb9-e26525e6fea6` | `cast/C2-DEAN_v1.jpg` | **USE** — identity holds, knees bare, work boots. Cauliflower ear rendered mild, on his **right** ear (prompted left) |
| C3-PAT | `c10469d4-79c1-4e97-9afb-a1a92eb7df06` (v2) | `cast/C3-PAT_v2.jpg` | **USE** — recast on the user's call: freckled, warm grandmother, sandy-grey ponytail at one height in all five, both knees bare; window right. *v1 `f07388cb…` replaced* |
| C4-SURGEON | `1ba54d8d-73b3-4f34-9ea3-55e4ba056236` (v2) | `cast/C4-SURGEON_v2.jpg` | **USE** — approachable per the §19B correction: relaxed open brow, soft eyes with laugh lines, mouth resting slightly up, no posed smile; identity holds, window left. *v1 `ee5a7185…` invalidated — read stern (correction 2026-09-26)* |

All five: the bottom row came **~43/57 instead of 50/50** (a `NEG-GRID` miss, not a panel-check failure — no effect on the sheet as a reference). Back views came full length on all five. Prompts: `cast/<ID>.prompt.txt`, built from Appendix A by ID in `cast/build_sheets.py` (`CAM-LOCK` → `AVATAR-SHEET` with `SHEET-GRID` → `SKIN-T` → `CAP-SHARP` → `CAP-FILE` → `NEG-SHEET` + `NEG-GRID` + `NEG-FILE` + `NEG-DEFAULT-FACE`), 9,148–9,286 chars each. Spend: 8 Sunburst jobs — 5 sheets, 1 surgeon regeneration (approachable correction), 2 recasts on the user's call (narrator, Pat).

### Identity strings — read off the renders (§7)

| ID | Identity string |
|---|---|
| N | white British man, 60, medium height, solid, a little soft at the middle; long oval face, warm hazel eyes crinkled at the corners, strong straight nose; thick wavy dark-grey hair worn over the collar; short salt-and-pepper beard; navy crew-neck jumper over a blue gingham shirt collar; dark jeans; brown suede desert boots |
| C1 | white British woman, 74, short and heavyset; broad heavy face, soft jowls, hooded brown eyes, wide nose, age spots across the forehead; short tight pure-white curls; cerise-and-orange leaf-print blouse; plum skirt a hand above the knee; navy slip-ons; heavy bare knees and calves |
| C2 | white British man, 58, barrel-chested and heavy; round broad face, small pale-blue eyes, wide nose, ruddy cheeks, heavy forehead creases; shaved head with grey stubble, grey stubble on the jaw; right ear thickened; charcoal T-shirt; navy cargo work shorts to just above the knee; grey socks; black work boots |
| C3 | white British woman, 66, sturdy and compact; wide heart-shaped face, apple cheeks, warm brown eyes, heavy freckles across nose, cheeks and neck; sandy hair gone mostly grey in a loose low ponytail, strands at the temples; navy quilted gilet over a navy-and-white Breton top; stone shorts to just above the knee; white canvas trainers |
| C4 | white British man, 71, tall, slightly stooped; broad open square face with full cheeks, soft grey-blue eyes with laugh lines, thick dark-grey brows relaxed and high, mouth resting slightly up — warm, kind, attentive; bald crown, close white sides; pale blue shirt, cuffs turned back; navy trousers, black belt; dark brown lace-ups |

### §19A axis tables — within-build clearance (no roster entries exist yet in this repo; `intake-1` generated none)

| Axis | N | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|
| Face | long oval, warm, crinkled eyes | broad, jowled, hooded | round, broad, small eyes | wide heart-shaped, apple cheeks | broad, open, full-cheeked, soft eyes (approachable, §19B) |
| Hair | wavy dark-grey, long over the collar + salt-and-pepper beard | cropped white curls | shaved, stubble | sandy-grey low ponytail | bald crown, white sides |
| Age position | 60 (young side) | 74 (far edge) | 58 (young edge) | 66 (mid) | 71 (far side) |
| Build | medium, solid, soft middle | short, heavyset | barrel-chested | sturdy, compact | tall, stooped |
| Class / wardrobe | smart-casual (jumper and jeans) | faded-flamboyant | trades | coastal-casual (gilet, Breton top) | professional |
| Marker | cleft chin (under the beard) | crooked little finger (not legible) | thickened ear | heavy freckles | thick dark brows, set high and relaxed |
| Voice | Tyneside (below) | non-speaking | non-speaking | non-speaking | non-speaking |
| Environment | kitchen table at home | terraced house, stairs | warehouse, van | park, grandchild | consulting room, lightbox |

**Correction 2026-09-26 (user, §34):** medical professionals are always approachable — written into §19B and Appendix A `APPROACH-PRO`; only C4 affected, clearance unchanged.

**Pairwise clearance (of 8; the voice axis counts only for N):** every pair clears the gate of 5 — lowest **N–C2 5** (age and build close) and C1–C3 6 (both solid builds); every other pair 6–7. ✓ *(re-counted after the N and C3 recast, 2026-09-26)*

### Narrator — `VOICE-NARR` (§22D) and §20 constraint sheet

**`VOICE-NARR`** *(locked 2026-09-26 in this compressed form — it goes verbatim into every §22U step-2 take and fits the Kling 2,500 ceiling; the clone inherits it. Narrator recast to 60 at v2)*
```
A man of sixty from Tyneside, a low dry chest voice with gravel at its edges, brisk and stop-start. Statements land flat and fall at the end; Geordie vowels, glottal t's; a short breath out through the nose before a number. Stress: quieter and slower on the turn word, never louder.
```

Full derivation, kept for reference (not sent):
```
A man of sixty from Tyneside, a low dry chest voice with gravel at its edges, brisk and stop-start. Placement in the chest, little nasal colour; texture dry with a faint rasp on held vowels; tempo brisk, about 185 words a minute, in short bursts; melody flat, statements falling at the end, questions barely lifting; articulation: Geordie vowels kept, final t's glottal, every other consonant clear; habit: a short breath out through the nose before a number. Age wear: breath shortening at long line ends, a thin top to the range. Stress: quieter and slower on the turn word, never louder.
```

| Field | N — narrator |
|---|---|
| Accent | Tyneside (Geordie), placed and unforced; never RP, never Scottish, never caricature |
| Pacing | brisk, ~185 wpm — the reference's 191 wpm, one notch down for the older audience |
| Posture / rest / gesture / ocular / rig | voice-source clip only (§22U step 1): seated at his kitchen table, forearms on it, Economical, eyeline on lens, R2 handheld — framed at step 4–5 |
| Audio proximity | R2 |
| Wardrobe never-list | suit, tie, white coat, anything clinical |
| Physical never-list | never on screen in the ad itself; never holds or wears the product |
| Voice spec | `VOICE-NARR` above |
| Stress register | quieter, slower on "Not because the arthritis has gone." — never bigger |
| Non-speech events | one short nasal exhale before a number; a dry half-laugh (once at most). Nothing else |
| Mouth asymmetry | level at rest (read off the v2 close-up); speech pulls right |
| Voice name (§22U step 7) | `Identity` — from the title "Identity Callout" (confirm no clash on the account at step 6) |

**Unverified:** the `GEN-DEFAULT-male-60s` roster entry does not exist yet, so `VOICE-NARR`'s clearance against the generator default is argued (four axes: accent, texture, rhythm, habit), not measured.

---

## Flags (decisions for the user — nothing below was changed silently)

| # | Where | Finding | Recommendation |
|---|---|---|---|
| **F1** | VN01 / HK1 | Top band says "an older **man**'s hands … behind **him**", bottom band says "a 70-year-old knee … **her** hand" — two people | Read as written: top = **C4 surgeon** (the X-ray lightbox makes him the clinician), bottom = **C1 Maureen**. Say if you meant one person |
| **F2** | VN03 / HK3 | "(cropped trousers)" — cropped trousers cover the knee, so the worn strap would not be visible (§9D; the Product Sheet says it's worn on bare skin) | Put Pat in walking shorts to just above the knee (as on her sheet) for the bottom band. **Waiting on your call for this line only** |
| F3 | VN02 / HK2 | Work gloves on the top band only | Dean in gloves at the shelving (top), bare hands at the van (bottom) — as written |
| **F4** | P-005 | "Unlike the cheap copies, which are too small to reach it" — a comparative claim that is not in the claim register | Voiced as written (§22U); shown with the blank `too small` near-copy archetype. Please confirm the advertiser holds it |
| F5 | P-006 | "silicone pad" | Voiced verbatim; prompts say "the pad" (the word renders the soft glossy fake — Product Sheet ruling) |
| F6 | P-016 | "Adjustable." | Covered by the seating beat; the band is never shown adjusted (`ADJUSTABLE_RULE`) |
| F7 | P-022 | `package_closed.jpg` (locked V7.49.27) is not in the Drive folder | Add it to the folder before the box beats, or I'll use the open box only |
| F8 | Standards | `AVATAR-SHEET` says the back panel is "from the waist up"; `SHEET-GRID` and §19 say full length. The five renders came full length | Doc inconsistency in the master — propose a §34 amendment to `AVATAR-SHEET` (say the word and I'll draft it) |
| F9 | Format | The reference has no talking head, so the build is voice-only (Style Lock) | Say "talking heads" to change it |
| F10 | EG05 | Brand watermark on the reference's B-roll | Recommend omitting it |

## Next — on your go (§18B step 5)

Approve the avatars (or name a swap / change), answer F2 (and F1 if the read is wrong) → steps 4–5 as one delivery of copy-ready prompts: property and location maps, act map + wardrobe map with every VN/LM row assigned and every B-roll row given its `EDIT` layout, then the §22U voice route for the narrator.
