# Build Sheet — stryde-regrets

**STRYDE Precision Strap · "C - VID | Listicle | TOF | Buyer Regrets | New | Three Regrets"** · Standards V7.64.2 · **RUN: MANUAL** · 2026-09-28

Steps 1–3 of §18. **Stopped at the avatar review (§18B, V7.62.0)** — steps 4–5 wait for the user's go.

Board: https://claude.ai/artifact/1PfmPCZQeuVTPn4ND1w86t

---

## 0. Intake (§18B)

| Input | Found | Notes |
|---|---|---|
| Drive folder | `1kvZgI49_u8VvW6rAS5YsElvJC0nH7wXF` | fetched with `fetch_drive.py` → `intake/` |
| Inspo | `inspo_regrets.mp4` (renamed from its Drive id) — "3 regrets" joint-supplement ad, Meta Ad Library ID 1317684553774108 (the script's `Reference:` line) | 169.95s, 9:16, 360×640, 30fps, audio |
| Script | `C_VID_Listicle_TOF_Buyer_Regrets_New_Three Regrets.docx` | title line 1 ✓ · "Door" = 3 hook options A/B/C · body 28 lines · 1 bracketed note |
| Product Sheet | `stryde_product_sheet_V7.49.29.py` | **older than the repo's `products/stryde/` (V7.49.31)** — the only differences are the V7.49.30–31 anatomy-look rulings the user made on stryde-identity. The repo copy stands |
| Product images | 10 — same set as stryde-identity (`front`, `back`, `product_tq_left/right`, `product_side`, `product_macro`, `worn_front/bent/rear`, `package_open`) | layer 1; already in `products/stryde/stryde_refs/` |
| Loom | none | optional — no question |
| Missing | `package_closed.jpg` | only the box beat needs it (F7) |

**Message fields read:** `run manual` → **Manual**. `mode 1` → **Mode 1 Realistic**. `british` → **cast British and the narrator's voice British** (read as on stryde-identity: every character white British, Product Sheet §8 "British, roughly 55–80" — F8). `HOOKS` blank → **in script: 3** (Door A/B/C) → 3 variant videos (§30H). `CAP` blank → E0 Higgsfield default. `VOICE` → derived (§22D), British. Build id `stryde-regrets` (from the script title).

---

## 1. Absorption Sheet (§42)

### Part 1 — measured

| Instrument | Reading | Settles |
|---|---|---|
| Duration / aspect / res | 169.95s · 9:16 · 360×640 · 30fps | Short VSL length (§31); ours 9:16 locked |
| Scene cuts | **49 shots, mean 3.47s**; 1.1–13.3s (plus two 1-frame flashes at 121.5 / 135.8s) | Slower than a UGC ad: 2–4s live-action cuts, long 9–13s holds on CGI anatomy |
| Silence (−30/−40 dB) | **none** | Wall-to-wall VO |
| VO transcript (faster-whisper) | 556 words / 170s = **196 wpm** | brisk read (`intake/inspo_transcript.txt`) |
| TH / B-roll | narrator on camera (a clinician, handheld at home, stairs behind) **7 times, ~15% of the runtime**; the rest B-roll | **talking heads in** (Style Lock) |
| Shot frames + per-second sheets | `intake/frames/inspo_regrets/` | Edit Grammar below |
| OCR | not run; overlays read off the frames | recorded as **read, not measured** |

### Part 2 — structure map

| Shot(s) | t | Job | What it shows | Overlay |
|---|---|---|---|---|
| S01–S02 | 0.0–5.0 | **HOOK** — number + promise | woman in bed clutching her hip, red pain glow; second woman head-down | headline (EG01) + caption |
| S03–S05 | 5.0–14.6 | Regret 1 named | woman struggling up from the bed; clinician with patient | "Regret No. 1" (EG03) |
| S06–S10 | 14.6–33.7 | symptoms → the ignored cause | a different woman per line (bed, walk, hands, phone); one 11.5s CGI knee run | captions |
| S11–S14 | 33.7–47.2 | the cost of waiting | CGI cartilage cracking; woman lowering into a chair | captions |
| S15–S22 | 47.2–76.6 | **Regret 2** | pills at a worktop; stomach/kidney CGI; narrator TH "trading one problem for three" | "Regret No. 2" |
| S23–S31 | 76.6–103.5 | **Regret 3** | shoulder/hip pain on a sofa; narrator TH; stairs descent gripping the rail; clinician | "Regret No. 3" |
| S32–S33 | 103.5–108.7 | **the turn** — "Here's what they wished someone had told them" | narrator TH | caption |
| S34–S43 | 108.7–139.5 | product + mechanism | bottle in hand; ingredient CGI; long CGI joint repair runs | captions |
| S44–S49 | 139.5–170.0 | close — "I can give it to you", guarantee, urgency | narrator TH; three different women holding the product to camera | captions |

### Part 3 — Style Lock (copied)

- **Delivery:** one narrator who has seen hundreds of cases, first person ("every woman I treated"), brisk (~196 wpm), plain, sombre — no pauses.
- **Structure:** listicle — number up front, "Regret No. 1/2/3" each named then evidenced, a turn ("here's what they wished…"), product, guarantee, urgency.
- **Visual grammar:** real people at home in the middle of the problem (a different face per line), CGI anatomy on every mechanism line, the narrator on camera at the structural joints (the turn, the close), product in hand only after the turn.
- **Density:** ~85% B-roll, ~15% narrator talking head; captions on every line.
- **Capture axis (never yields):** phone footage at home; ours runs the iPhone 17 Pro Max register (§22); anatomy in our §12A register.

### Part 3A — Edit Grammar → `EDIT-STRYDE-REGRETS`

| ID | Device | Where | When used | Parameters |
|---|---|---|---|---|
| EG01 | **headline** text overlay | S01–S02 @ 0:00–0:05 | the hook | two lines, top band (~3–6% height), small black bold sentence-case on a white highlight. Our words, never theirs |
| EG02 | **captions** | every shot | every spoken phrase | white rounded box, black bold sentence-case, 1–2 lines, centred; sits mid-frame to lower third (~55–80% height) off the subject's face |
| EG03 | **list label** | S06–S08, S15–S16, S27–S28 | the first line of each regret | "Regret No. N" in the same caption box, one line above the caption |
| EG04 | **full** B-roll, hard cut | all B-roll | throughout | hard cuts only; 1–5s on live action |
| EG05 | narrator **talking head**, full frame | S20, S29, S32, S39, S44, S45, S47 | the Regret 2 summary, "they knew", the turn, the product claim, the close | handheld selfie-height, waist-up, at home, stairs behind her |
| EG06 | **CGI anatomy runs** | S10, S11–S12, S16, S21–S22, S40–S43 | every mechanism / damage line | full frame, 5–13s holds, slow push-in inside the shot — our §12A ANAT-A/B |
| EG07 | pain glow on the body | S01 | the hook | red glow over the painful joint — ours: the ANAT-A hot spot, or a §17 motion-graphic in CapCut, never on live skin |
| EG08 | **product to camera** by different people | S44–S49 | the close | held up to the lens, face in frame, one line each |
| — | not used by the reference | — | — | no split screen, no PiP, no punch-ins, no transitions beyond hard cuts, no speed ramps; music bed not measured |

### Part 4 — script absorption

**Copy formula (reference):** "3 regrets every woman with X wishes she had known" → Regret 1 (ignored the signs) → Regret 2 (the painkiller) → Regret 3 (waited) → "here's what they wished someone had told them" → root cause → product + mechanism → "I can't go back… but I can give it to you" → guarantee → urgency.

**Beat map — their row → our line** (the script was supplied already rewritten slot for slot; not edited, §42 Part 4 scope):

| Reference (t) | Job | Our line |
|---|---|---|
| "Three regrets every woman… wishes she had known" (0–5) | hook | HK1 / HK2 / HK3 (Door A / B / C) |
| "Every woman that I treated…" (8–16) | authority / source | P-001 "I read the messages… Twenty five thousand of them now." |
| "Regret number one, they felt the stiffness and ignored it" (5–8) | Regret 1 | P-002 – P-008 (nobody told them where it comes from → the drawer of braces) |
| "Regret number two, they kept taking the painkiller" (42–76) | Regret 2 | P-009 – P-012 (the good knee protected the bad one) |
| "Regret number three, they waited" (77–103) | Regret 3 | P-013 – P-015 (they stopped saying yes) |
| "Here's what they wished someone had told them" (103–105) | the turn | P-016 |
| root cause + product + ingredients (105–145) | mechanism + product | P-017 – P-022 |
| — | proof (added) | P-023 – P-024 (34%, 3 years, 200,000; 10 seconds, no sores) |
| — | risk reversal as a test (added) | P-025 – P-026 (the one-knee stairs test) |
| "I can't go back… but I can give it to you… trade places" (145–157) | close | P-027 – P-028 |
| "90-day money-back… grab yours now" (158–169) | offer | P-029 – P-030 (two for one, sixty days, keep the straps, the copies stretch) · P-031 "Go and do your stairs." |

**Voice fingerprint (reference):** first person, one expert who has seen it all, second person for the viewer, anaphora ("They didn't know… They didn't know…"), numbers spoken. Ours matches: first person ("I read the messages"), anaphora ("No to the long walk. No to the day out. No to…"), numbers in words.

**Length:** hooks 27–28 words; body 580 words. At ~180 wpm (one notch below the reference's 196 for the older audience) each variant runs **≈ 9s hook + ≈ 3:13 body ≈ 3:22** — about 30s longer than the reference, still a Short VSL (§31).

### Part 5 — surfaced, not absorbed

| Reference element | Disposition |
|---|---|
| "estrogen drought", supplement ingredients, "the only thing that actually fixes the problem" | not ours — a different product and claim; our mechanism is the Product Sheet's (protection, §6) |
| Narrator as a treating clinician | **replaced** — ours is the person who reads the customers' messages (the script's "I read the messages"); no medical title, no white coat (§19B not triggered) |
| Stomach / kidney CGI, ingredient CGI | position-not-look → our §12A ANAT-A / ANAT-B on the tendon |
| "90-day money-back", "grab yours now… before it's too late" | replaced — ours is 60 days + Buy 1 Get 1 Free (Product Sheet); no false urgency |
| A different woman per line | kept as a *device* only on one-off lines; the regrets are carried by one recurring person each (below), so the story reads |

### Part 6 — beat-it plan

| Reference weakness | Our delta | Beats |
|---|---|---|
| The regrets are symptoms, not decisions — nobody to recognise yourself in | each regret is one person's decision (Graham's drawer, Lorraine's good leg, Ken's "no"), carried across its lines | Regret 1–3 |
| Mechanism is ingredient theatre | one visible, testable point: a finger under the kneecap, the strap seated on that band | P-006 – P-007, P-020 – P-022 |
| Guarantee is a line | the guarantee is a test the viewer can do tonight on their own stairs, one knee strapped, one bare | P-025 – P-026, P-031 |
| Women only | British, 55–80, men and women (Product Sheet §8) | cast |

### Part 7 — confirmation

Reference-vs-rule conflicts are flagged at the end of this sheet. **Confirm or correct the absorption with the avatars.**

---

## 2. Script, product, claims, locks (step 2)

### Script extraction (§22U step 8)

`script_lines.py` → `work/script.lines.txt`. **It kept two hook labels as spoken** ("A — Number plus refusal", "C — The regret named first" — "B — The source" was dropped as a heading) and kept the quote marks. Both removed by hand, nothing else touched: `work/HK1–HK3.lines.txt`, `work/BODY.lines.txt` (F1). Dropped, never voiced: title, `Reference:` link, "Door", "VO", "Body", "(the reference's construction)", the three hook labels.

### Visual Instruction Ledger (§27F) — opened

| ID | Source | Instruction | Line | Carried by | Status |
|---|---|---|---|---|---|
| VN01 | script | "(the reference's construction)" — build the Door hooks the way the reference opens | HK1–HK3 | EG01 headline + EG02 captions, number up front | open → step 5 |

### Phrase inventory (§27B) — dispositions are assigned at step 5

| ID | Phrase | Job | Claim | Subject / register |
|---|---|---|---|---|
| HK1 | "Three things people tell us they wish they had known about their knees. Not one of them is that they should have gone to the doctor sooner." | hook | — | the three regret people, one per phrase |
| HK2 | "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect." | hook | 25,000 (F2) | N at her messages → the three |
| HK3 | "The most common regret I read is not about surgery. It is not about painkillers. It is not about waiting too long. It is about two centimetres." | hook | 2 cm (F2) | N · ANAT-A on "two centimetres" |
| P-001 | I read the messages that come in when people buy one of these. Twenty five thousand of them now. | source | 25,000 (F2) | **N talking head** |
| P-002 | Regret number one. Nobody ever told them where it was actually coming from. | Regret 1 | — | C1 Graham · EG03 |
| P-003 | They bought the stretchy sleeve. Then the one with the metal sides. Then the wrap, then the gel, then the one their neighbour swore by. | agitate | — | C1 · five blank supports, one per phrase (§10, no brands) |
| P-004 | And why would they not. The joint is where it hurts, and the joint is what the scan shows. | agitate | — | C1 · ANAT-B |
| P-005 | But two centimetres below your kneecap there is a band of tendon about as wide as your thumb, and every step you take lands on it. Seventeen times your bodyweight. | mechanism | 2 cm, thumb-wide (F2) · 17× (held) | ANAT-A · 17× overlay |
| P-006 | Put your finger under your kneecap and press. That band is the one taking it. | demonstration | — | C1 bare knee, finger on the tendon |
| P-007 | A sleeve squeezes the whole knee and leaves that band carrying everything. A hinged brace stops the knee going sideways, and the knee was never going sideways. | objection | category comparatives (F2) | blank sleeve / hinged brace near-copies (§10) · ANAT-A |
| P-008 | So the drawer fills up, the years go by, and not one of them was ever aimed at the spot. | Regret 1 payoff | — | C1 · the drawer |
| P-009 | Regret number two. They protected the bad knee with the good one. | Regret 2 | — | C2 Lorraine · EG03 |
| P-010 | Nobody decides to do this. You lead with the good leg because it hurts less, and after a while you stop noticing. | agitate | — | C2 on stairs, leading with one leg |
| P-011 | But the good leg is now doing the work of two, and the band on that side is taking a load it was never meant to take. | mechanism | — | ANAT-A on the other knee |
| P-012 | That is why the second knee goes. It is the most common thing in the whole postbag, and nobody sees it coming. | Regret 2 payoff | "most common" (F2) | C2 · N TH |
| P-013 | Regret number three. They stopped saying yes, and they never said why. | Regret 3 | — | C3 Ken · EG03 |
| P-014 | No to the long walk. No to the day out. No to the house with the steps up to the front door. | agitate | — | C3, one beat per "No" |
| P-015 | Not a decision, just easier than explaining. And the people around them thought they had gone off it. | Regret 3 payoff | — | C3 with family |
| P-016 | Here is what they say they wish someone had told them. | **the turn** | — | **N talking head** |
| P-017 | Coming down is worse than going up. Going up, your muscles lift you. Coming down, you are catching yourself, and the catch lands on that band. | mechanism | biomechanics (F2) | stairs · ANAT-A |
| P-018 | So you do not wrap the joint. You go underneath it. | product turn | — | N TH or product in hand |
| P-019 | This one is called Stryde. It sits two centimetres below the kneecap, on the tendon, and never crosses the joint. | product | placement (F4) | worn, front |
| P-020 | A silicone pad inside holds pressure on that one band instead of spreading it round the whole knee. | mechanism | silicone pad (held) | `PAD_BACK_SHOT` → ANAT-A |
| P-021 | The weight gets caught and moved off the worn part before it reaches the joint. | mechanism | protection (held) | ANAT-A |
| P-022 | The placement is the whole thing. A centimetre too high and it is a sleeve again. | product | (F2) | worn, close front |
| P-023 | Thirty four percent less strain. Measured. Three years with orthopedic surgeons. Two hundred thousand people wearing one. | proof | 34%, 3 yrs, 200,000 (held) | overlays; montage |
| P-024 | Ten seconds to put on. No sores, no rolling down, and nobody can see it. | features | 10 s, no sores (F2) | **seating beat** (`SEAT_LOCK`) · §9D under trousers |
| P-025 | And you do not have to take my word for it. One knee only. Leave the other bare. Go to your own stairs and come down forwards. You will know in a minute. | test | — | N TH → C2 on stairs, one knee strapped |
| P-026 | Not because the arthritis has gone. It is still there. Because the weight is not landing on that band any more. | honesty | conditions (held) | ANAT-B → ANAT-A |
| P-027 | Most of those messages end the same way. I wish somebody had told me this four years ago. | close | — | N at her messages |
| P-028 | You are hearing it today. That is the only difference between you and them. | close | — | **N talking head** |
| P-029 | Two for one, so you do both knees, which after regret number two is the point. | offer | BOGOF (held) | box open, two straps |
| P-030 | Sixty days, and you keep the straps. From the Stryde site. The copies stretch, and a stretched strap stops holding it. | guarantee · objection | 60 days (held) · "keep the straps", "copies stretch" (F2) | near-copy, one archetype |
| P-031 | Go and do your stairs. | CTA | — | C2 / C3 on stairs |

Hooks 3 · body 31 phrases (the body's 28 script lines, three split at their sentence breaks) · **uncovered 0 · blocked 0** (dispositions pending step 5).

### Claims (§43A)

Advertiser-held (Product Sheet §9, user-confirmed V7.49.29): 17× bodyweight · three years with orthopaedic surgeons · silicone pad · 34% less strain (measured) · protection (weight moved off the worn part) · arthritis · 200,000+ wearers · Buy 1 Get 1 Free · 60-day money-back. Numbers are post overlays, never generated (§17). **Not in the register — voiced verbatim, flagged for the advertiser (F2):** 25,000 messages · "two centimetres below the kneecap" · "tendon about as wide as your thumb" · sleeve / hinged-brace statements · "the second knee goes… most common thing in the postbag" · "coming down is worse… the catch lands on that band" · "never crosses the joint" · "a centimetre too high and it is a sleeve again" · "ten seconds to put on" · "no sores, no rolling down, nobody can see it" · "you keep the straps" · "the copies stretch".

### Mode & Model Lock (§18A)

| Beat class | Model · params | Why |
|---|---|---|
| Mode | **Mode 1 Realistic**, iPhone 17 Pro Max, 9:16 | user: mode 1 |
| Avatar sheets | `gpt_image_2_5` · `variant: sunburst` · `quality: high` · `resolution: 2k` | measured route (§19) — **used this delivery** |
| Wordmark with hands or a body (held, worn, seating) | `nano_banana_pro` | rule 7: no GPT Image with a body in frame |
| Wordmark, no person (box, pack, product) | `nano_banana_pro` | the wordmark must read |
| Talking-head seeds (narrator), candid faces | `nano_banana_pro` | §18A default |
| Volume B-roll with a person, no readable wordmark | `nano_banana_2` | volume |
| Mechanism (ANAT-A point/protection, ANAT-B conditions) | `nano_banana_2` | classifier threshold; Product Sheet §17 looks |
| Video | Kling 3.0 (`kling-video-v3_0_omni`), start image, `prefer_multi_shots: false` | §4, §27G |
| Voice / talking head | §22U: 2+ Kling source takes → ElevenLabs clone → Eleven v3 TTS → HeyGen Avatar V with a motion prompt | talking heads in |

**Other locks:** format **Short VSL, narrator talking head + B-roll** (Style Lock: the reference's narrator is on camera ~15%) · **side: right knee** (no knee named → `SIDE_RULE`; "one knee only" is the viewer's, not a side) · mechanism claim: protection · edit: `EDIT-STRYDE-REGRETS` · hooks: 3 in script → 3 variants.

---

## 3. Cast (step 3) — generated, on the board for your check

Recurring subjects (≥ 2 beats on the inventory): **N narrator** (talking head P-001, P-016, P-025, P-028 + hooks) · **C1 Graham** (Regret 1, P-002 – P-008) · **C2 Lorraine** (Regret 2 P-009 – P-012, the stairs P-017, the test P-025, P-031) · **C3 Ken** (Regret 3, P-013 – P-015, hooks). One-offs (§13, not sheeted): hands/legs inserts, the P-023 montage.

| Sheet | Job ID | File | Board |
|---|---|---|---|
| N-NARR | `41353a06-41b3-4936-a150-6bebf8d478c0` | `cast/N-NARR_v1.jpg` | To check |
| C1-GRAHAM | `a30a316c-2969-498f-bd80-cc3ffbdcae42` | `cast/C1-GRAHAM_v1.jpg` | To check |
| C2-LORRAINE | `49113df5-b39f-4e1d-819c-eb352e6ceed6` | `cast/C2-LORRAINE_v1.jpg` | To check |
| C3-KEN | `dcd5df97-faac-4d82-a47e-118616c8c259` | `cast/C3-KEN_v1.jpg` | To check |

Manual: **you check them** (Confirm or Fix on the board); I regenerate only from a Fix note. Prompts: `cast/<ID>.prompt.txt`, built from Appendix A by ID in `cast/build_sheets.py` (`CAM-LOCK` → `AVATAR-SHEET` + `SHEET-GRID` → `SKIN-T` → `CAP-SHARP` → `CAP-FILE` → `NEG-SHEET` + `NEG-GRID` + `NEG-FILE` + `NEG-DEFAULT-FACE`), 9,133–9,294 chars. Spend: 4 Sunburst jobs, 11 Higgsfield credits (20,021.5 → 20,010.5).

### Identity strings — read off the renders (§7)

| ID | Identity string |
|---|---|
| N | white British woman, 62, slim and upright, average height; long narrow face, high flat cheekbones, deep-set grey-blue eyes, long straight nose, thin level mouth, a small dark mole below the left side of the mouth; chin-length blunt silver-grey bob with a straight fringe to the brows; moss-green knitted cardigan over a cream top; charcoal wool trousers; black leather loafers |
| C1 | white British man, 67, tall, lean and wiry; long lean face, hollow cheeks, heavy-lidded grey eyes, high hooked nose, deep brow lines, a small scar at the outer end of the left eyebrow; thinning grey hair combed back, balding at the crown; clipped grey moustache; burgundy polo shirt; khaki chino shorts above the knee; brown leather boat shoes |
| C2 | white British woman, 59, tall, broad-shouldered, solid; square face, strong jaw, pale green-grey eyes, short broad nose, deep forehead lines; chin-length dark auburn hair with a wide band of grey at the roots and parting, tucked behind the ears; teal zip-up fleece over a white T-shirt; dark denim shorts above the knee; white trainers |
| C3 | white British man, 72, short and round, big belly; round face, ruddy cheeks with broken veins, small pale-blue eyes, bulbous nose, large sticking-out ears; thick white hair side-parted; mustard V-neck jumper over a white collared shirt; beige shorts above the knee; grey socks; brown leather sandals |

*(Read off the renders, not the prompts. C1's scar came at the outer brow rather than cutting through it; C2's front-teeth gap can't show with the mouth closed; N's mole sits below the lip corner rather than above it.)*

### §19A axis tables — clearance against this build and the stryde-identity roster

| Axis | N | C1 | C2 | C3 |
|---|---|---|---|---|
| Face | long narrow, high flat cheekbones | long lean, hollow, hooked nose | square, strong jaw | round moon, ruddy |
| Hair | silver blunt bob + fringe | thinning grey, combed back + moustache | auburn, grey roots | thick white side parting |
| Age position | 62 (young side) | 67 (mid) | 59 (young edge) | 72 (far side) |
| Build | slim, upright | tall, wiry | tall, broad-shouldered | short, round |
| Class / wardrobe | quiet smart-casual (cardigan) | retired middle-class casual (polo, chinos) | practical-sporty (fleece) | old-school (jumper and shirt, sandals and socks) |
| Marker | mole by the lip | eyebrow scar | gap teeth (hidden when closed) | sticking-out ears |
| Voice | British (below) | non-speaking | non-speaking | non-speaking |
| Environment | her kitchen table with printed messages | bedroom, the drawer | semi-detached, stairs | living room, front step |

Pairwise within the build: every pair clears the gate of 5 (lowest **N–C2 5**: both women near 60). Against stryde-identity's roster: C1 vs Maureen/Pat (sex differs) and vs Dean (build, hair, age, wardrobe, marker) ≥ 5; C3 vs Maureen 5 (both short and heavy, 72/74 — sex, hair, face, wardrobe, marker differ); N vs Pat 6. ✓ *(counted, not measured by an instrument)*

### Narrator — `VOICE-NARR` (§22D) and §20 constraint sheet

**`VOICE-NARR`** *(proposed; goes verbatim into every §22U step-2 Kling take)*
```
A woman of sixty-two from West Yorkshire, a warm low alto with a little dryness at its edges, calm and measured. Statements land plainly and fall at the end; flat Yorkshire vowels, a clipped 'the'; she reads a number as if she has said it many times. Stress: slower and softer on the regret, never louder.
```

| Field | N — narrator |
|---|---|
| Accent | West Yorkshire, placed and unforced; never RP, never caricature (the stryde-identity narrator is Tyneside — kept apart) |
| Pacing | measured, ~180 wpm — one notch under the reference's 196 |
| Talking head | waist-up, handheld selfie-height, at her kitchen table with a stack of printed messages, window to her right (the sheet's side); HeyGen Avatar V with a motion prompt on every render (§22U step 13) |
| Wardrobe never-list | white coat, scrubs, anything clinical — she reads the messages, she isn't a clinician |
| Physical never-list | never wears the strap on camera; holds it only on P-018/P-019 |
| Stress register | slower, softer on "I wish somebody had told me this four years ago." — never bigger |
| Non-speech events | a small breath before "Regret number…"; nothing else |
| Voice name (§22U step 7) | `Regrets-Narrator` (proposed) |

---

## Flags (decisions for the user — nothing below was changed silently)

| # | Where | Finding | Recommendation |
|---|---|---|---|
| **F1** | script extraction | `script_lines.py` voiced two hook labels ("A — …", "C — …") and kept quote marks | Removed by hand; the spoken text is otherwise untouched. I'll fix the script's label rule in a separate standards change if you want it |
| **F2** | claims | 12 lines carry claims not in the Product Sheet register (list above: 25,000 messages, 2 cm, thumb-wide tendon, sleeve/brace, second knee, stairs biomechanics, 10 seconds, no sores/nobody can see it, keep the straps, copies stretch…) | Voiced as written (§22U). Please confirm the advertiser holds them |
| F3 | P-023 | "orthopedic" (US spelling) | Voiced as written; the on-screen caption follows the script unless you want "orthopaedic" |
| F4 | P-019, P-005 | "two centimetres below the kneecap" | The render follows the Product Sheet: the strap sits on the tendon directly below the kneecap (notch cups the lower border) — which is where 2 cm lands. No visible gap is ever drawn |
| F5 | format | The reference's narrator is on camera ~15% → talking heads are in (HeyGen) | Say "no talking head" to make it voice-only |
| F6 | narrator | The reference's narrator is a clinician; ours reads the customers' messages ("I read the messages") | Cast as a company person, not medical. Say if she should be a clinician (then §19B applies) |
| F7 | P-029 | `package_closed.jpg` (locked V7.49.27) is still not in the Drive folder | Add it before the box beat, or I'll use the open box only |
| F8 | casting | "british" read as white British cast + British narrator, as on stryde-identity | Say if you meant a different mix |
| F9 | length | ≈ 3:22 per variant (reference 2:50) | Script as written; no cuts suggested |
| F10 | EG01 | the reference's hook headline is theirs | Ours will be written from our hook line at step 8; one per variant |

## Next — on your go (§18B step 5)

Confirm the four sheets on the board (or Fix with a note), answer F2 (and F5/F6 if my reads are wrong) → steps 4–5 as one delivery: location maps and plates (N's kitchen, C1's bedroom, C2's stairs, C3's living room / front step), act map + wardrobe map with every beat's layout from `EDIT-STRYDE-REGRETS`, then the §22U voice route for the narrator.
