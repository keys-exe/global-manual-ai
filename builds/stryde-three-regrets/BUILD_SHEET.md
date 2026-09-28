# Build Sheet — stryde-three-regrets

**STRYDE Precision Strap · "C - VID | Listicle | TOF | Buyer Regrets | New | Three Regrets"** · Standards V7.64.2 · **RUN: MANUAL** · 2026-09-28

Steps 1–3 of §18. **Stopped at the avatar review (§18B, V7.62.0).** Steps 4–5 wait for your go.

**Board:** https://claude.ai/artifact/HMjMnUVMQwBX4WsVjkUbcK

---

## 0. Intake (§18B)

| Input | Found | Notes |
|---|---|---|
| Drive folder | `1kvZgI49_u8VvW6rAS5YsElvJC0nH7wXF` | fetched with `fetch_drive.py` → `intake/`. It matches no existing build, so this is a new build |
| Inspo | `inspo.mp4`: a joint-supplement "3 regrets" listicle, clinician narrator (Meta Ad Library 1317684553774108, per the script) | 169.95s · 9:16 · 360×640 · 30fps · audio |
| Script | `C_VID_Listicle_TOF_Buyer_Regrets_New_Three Regrets.docx` | title on line 1 ✓ · "Door" = 3 hook options A/B/C · body 28 lines · 1 bracketed note |
| Product Sheet | `stryde_product_sheet_V7.49.29.py` | **older** than `products/stryde/` (V7.49.31, a superset). The repo copy is used; nothing in V7.49.29 is missing from it |
| Product images | 10, byte-identical to `products/stryde/stryde_refs/` | layer 1 |
| Loom | none | no question (§18C) |
| Missing | `package_closed.jpg`, as on the last STRYDE build | not needed for steps 1–3 |

**Message fields read:** `run manual` → **RUN: MANUAL**. `british` → **VOICE: British** (the narrator's `VOICE-NARR`), and applied as a casting instruction too: every character is cast white British (this agrees with Product Sheet §8, "British, roughly 55–80"). `MODE` blank → **Mode 1**, because a realistic reference selects Mode 1 automatically (§2). `HOOKS` blank → **in script: 3** (Door A, B, C), so 3 variant videos (§30H). `CAP` blank → the E0 Higgsfield default. `BUILD` blank → `stryde-three-regrets`, named after the script title.

**Tool finding:** `script_lines.py` kept two hook labels as spoken lines ("A — Number plus refusal", "C — The regret named first") but dropped "B — The source" as a heading. It also left the typographic quotes in. The verbatim file used from here on is `work/script.lines.txt`, with those two labels and the quote marks removed and every word unchanged. The fix belongs in `script_lines.py`: a line `^[A-Z] — ` under a heading is a label. Not changed in this commit.

---

## 1. Absorption Sheet (§42)

### Part 1 — measured

| Instrument | Reading | Settles |
|---|---|---|
| Duration / aspect / res | 169.95s · 9:16 · 360×640 · 30fps | Short VSL length band (2–4 min) |
| Scene cuts (detector) | 49 shots, mean 3.47s, range 0.03–13.32s | **The detector under-counts.** The per-second sheets show a new shot every ~1.5–3s in most stretches (e.g. 22–34s holds 5 shots the detector read as one). Pace is **read off the sheets, not measured**: a cut every ~2–3s, TH shots held 3–6s |
| Silence (−30/−40 dB) | none | **Wall-to-wall VO**, no held beats |
| VO transcript (faster-whisper small) | 556 words / 169.2s = **197 wpm** | brisk, even read → `work/inspo_transcript.txt` |
| TH / B-roll | the narrator on camera ≈ 8 shots, ≈ 12% of runtime (read off the sheets) | **talking head + B-roll**, B-roll-led |
| Shot frames + per-second sheets | `intake/frames/inspo/` (sheets 01–06) | Edit Grammar below |

### Part 2 — structure map

| t | Section | What it shows | Overlay |
|---|---|---|---|
| 0.0–5.0 | **HOOK**: "Three regrets every woman with severe joint damage wishes she had known…" | sufferer in bed with a red pain glow; sufferer bent over | **top headline banner** (EG01) + captions (EG02) |
| 5.1–42.0 | **REGRET 1**: felt the stiffness, ignored it | card "Regret No. 1" over a sufferer; clinician with patient; a new anonymous sufferer per symptom line; CGI knee cartilage drying/cracking | captions + "Regret No. 1" (EG03) |
| 42.2–76.5 | **REGRET 2**: the painkiller | pills in the kitchen; CGI stomach, blood vessel, kidneys; **narrator TH** 63–65s | captions + "Regret No. 2" |
| 76.7–103.3 | **REGRET 3**: waited until irreversible | "Regret No. 3" card; narrator TH; stairs; CGI cracking | captions + "Regret No. 3" |
| 103.5–121.5 | **TURN + PRODUCT**: "Here's what they wished someone had told them" | narrator TH → CGI → product in hand → product-and-ingredients CGI | captions |
| 121.7–145.6 | **MECHANISM**: six ingredients | stylised 3D ingredient and joint CGI (lab glassware, glowing) | captions |
| 145.8–169.2 | **CLOSE / OFFER**: "I can't go back…, but I can give it to you"; 90-day guarantee; stock urgency | narrator TH holding the product; three UGC selfie holders; pack on a counter | captions |

### Part 3 — Style Lock (copied)

- **Delivery:** one narrator, first person, a professional who has "seen" the regrets; brisk (~197 wpm), plain declaratives, even level, no pauses.
- **Edit rhythm:** a hard cut every ~2–3s; the narrator's TH shots are the only holds (3–6s).
- **Visual grammar:** a different anonymous sufferer per symptom line, in real homes (bed, stairs, sofa, kitchen); CGI anatomy on every "why" line; the narrator TH at the section turns; product only after the turn; UGC holders on the close.
- **Density:** B-roll-led, TH ≈ 12%.
- **Retention:** numbered listicle ("Regret No. 1/2/3" cards), each regret closing on a consequence; "Here's what they wished someone had told them" as the turn; a guarantee plus scarcity on the close.
- **Capture axis (never yields):** the reference mixes phone footage with glossy CGI. Ours runs iPhone 17 Pro Max (§22), with mechanism beats in the §12A anatomical register (`ANATOMY_LOOK`), never the reference's glowing lab-CGI look.

### Part 3A — Edit Grammar → `EDIT-STRYDE-THREE-REGRETS`

| ID | Device | Where | When used | Parameters |
|---|---|---|---|---|
| EG01 | **headline banner** text overlay | S01–S02 @ 0:00–0:05 | the hook only | two lines of bold white text with a thin black stroke, centred at the top ~6–10% of height. Our words, never theirs (written at step 5 from the hook line) |
| EG02 | **captions**, every line | 0:00–end | the whole VO | short phrase groups (4–8 words), black bold sans on a white rounded box, centred at ~55–60% height (upper-lower third), one group at a time |
| EG03 | **section card** "Regret No. N" | @ 5.1s, 42.2s, 76.7s | each regret opener | the caption box with "Regret No. N" set **above** the line's own caption, the same style, held for the first 2–3 caption groups of the regret |
| EG04 | **full** B-roll, hard cut | throughout | every body line | hard cuts only, 1.5–3s runs; one 13s mechanism run |
| EG05 | narrator **TH**, full frame | ~8 shots | the turns (regret 2's consequence, regret 3's opener, the turn, the close) | handheld phone, mid-shot, chest up, at home by the stairs, eyeline on lens, gesturing |
| EG06 | CGI anatomy, full frame | on every "why" line | mechanism | our §12A anatomical register (`ANATOMY_LOOK`), not their glowing-lab look |
| EG07 | product in hand, full frame | after the turn | product intro | hand holding the pack or product close to lens, plain counter |
| EG08 | UGC **selfie holders** | close | proof / offer | three different people, selfie framing, product held to camera, smiling |
| EG09 | **whip / motion-blur** transition | @ ~166s | into the last shot | one fast blur into the final holder. CapCut line |
| — | not used by the reference | — | — | no split, no PiP, no punch-ins, no speed ramps; music/SFX **not measured** (VO dominates the mix) |

### Part 4 — script absorption

**Copy formula (reference):** number-plus-audience hook → Regret 1 (a symptom ignored) → Regret 2 (the wrong fix) → Regret 3 (left too late) → "Here's what they wished someone had told them" → root cause → product and mechanism → "I can't go back… but I can give it to you" → guarantee → scarcity.

**Beat map: their structure → our script.** The script was supplied rewritten slot for slot and is not edited (§42 Part 4 scope):

| Reference (t) | Job | Our lines |
|---|---|---|
| "Three regrets every woman… wishes she had known" (0–5) | hook | HK1 (A: number plus refusal) · HK2 (B: the source) · HK3 (C: the regret named first) |
| "Every woman that I treated…" (8–16) | narrator authority | P-001–P-002 "I read the messages… Twenty five thousand" |
| Regret 1: symptom ignored, CGI why (5–42) | regret 1 | P-003–P-016 wrong supports; the band below the kneecap; 17× |
| Regret 2: painkiller harm (42–76) | regret 2 | P-017–P-023 the good leg takes the load; the second knee goes |
| Regret 3: left too late (77–103) | regret 3 | P-024–P-030 stopped saying yes |
| "Here's what they wished someone had told them" (103–105) | turn | P-031 |
| root cause + product + ingredients (105–145) | mechanism / product | P-032–P-042 coming down; underneath the joint; Stryde; the pad; placement |
| — | proof (added) | P-043–P-048 34%, 3 years, 200,000, 10s, no sores |
| — | self-test (added) | P-049–P-056 one knee, your own stairs; honesty line |
| "I can't go back… I can give it to you" (145–156) | emotional close | P-057–P-060 "I wish somebody had told me… You are hearing it today" |
| 90-day guarantee; stock urgency (158–169) | offer | P-061–P-065 two for one · sixty days · the copies stretch · "Go and do your stairs" |

**Voice fingerprint (reference):** first person, a professional witness ("every woman I treated"), numbered lists, short declaratives, no contractions on the turns. Ours matches: a first-person witness ("I read the messages"), numbered regrets, and **no contractions anywhere** ("It is not", "you do not"), a deliberate plain register the voice must keep (§22U: verbatim, never contracted).

**Length:** hooks 27 / 28 / 27 words; body 580 words. At ~185 wpm each variant runs **≈ 9s hook + ≈ 3:08 body ≈ 3:17**, about 27s longer than the reference, inside the Short VSL band.

### Part 5 — surfaced, not absorbed

| Reference element | Disposition |
|---|---|
| "Every woman that I treated" (a clinician's authority) | **replaced** by the script's witness, a Stryde person reading customer messages. Not a clinician, so no medical-professional claim |
| Oestrogen-drought, ibuprofen-harm and "irreversible" claims | not inherited; our claims are the advertiser's (claims table) |
| Competitor supplement pack on screen (EG07/EG08) | **replaced** by our product; never another brand (§10) |
| "If you see it still in stock… before it's too late" (scarcity) | **not used**; the script's close has no scarcity |
| Glowing lab-CGI ingredient renders | position, not look → our §12A anatomical register |
| Women-only casting ("every woman") | not inherited; the script is gender-neutral, so the cast mixes (3 women, 1 man) |

### Part 6 — beat-it plan

| Reference weakness | Our delta | Beats |
|---|---|---|
| A new stranger on every line, so no one to follow | **one recurring person per regret** (Gail, Ken, Joan), each carried from regret to payoff | R1 / R2 / R3 rows |
| The "why" is asserted in CGI, never felt | a viewer self-test on screen: finger under the kneecap (P-012), one knee on your own stairs (P-050–P-053) | P-012, P-052 |
| Mechanism is a list of ingredients | one mechanism: the band, the catch, the pad, **anatomical beats paired with the worn product** | P-010–P-015, P-032–P-042 |
| Scarcity close | risk reversal (sixty days, keep the straps) plus a call to act on the stairs | P-061–P-065 |

### Part 7 — confirmation

Reference-vs-rule conflicts are in the Flags. **Confirm or correct the absorption along with the avatars.**

---

## 2. Script, product, claims, locks (step 2)

### Visual Instruction Ledger (§27F) — opened

| ID | Source | Instruction | Line | Carried by | Status |
|---|---|---|---|---|---|
| VN01 | script, under "Door / VO" | "(the reference's construction)": the hooks follow the reference's hook construction | HK1–HK3 | the hook beats copy the reference's opener: headline banner (EG01), captions (EG02), a sufferer image on the number line | open → step 5 |
| — | script heading "VO" | the Door is voice-over | HK1–HK3 | hooks are **VO over B-roll** (no TH on the hook); the narrator first appears in the body. Recorded as read | open → step 5 |

### Phrase inventory (§27B) — dispositions are assigned at step 5

Hooks (verbatim, `work/hooks_body.txt`):

| ID | Hook | Words |
|---|---|---|
| HK1 (A — number plus refusal) | Three things people tell us they wish they had known about their knees. Not one of them is that they should have gone to the doctor sooner. | 27 |
| HK2 (B — the source) | Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect. | 28 |
| HK3 (C — the regret named first) | The most common regret I read is not about surgery. It is not about painkillers. It is not about waiting too long. It is about two centimetres. | 27 |

Body, 65 phrases:

| ID | Phrase | Job | Claim | Subject / register |
|---|---|---|---|---|
| P-001 | I read the messages that come in when people buy one of these. | witness | — | **N TH** |
| P-002 | Twenty five thousand of them now. | proof | 25,000 messages (**not in register**, F3) | N / postbag |
| P-003 | Regret number one. | section | — | EG03 card · R1 |
| P-004 | Nobody ever told them where it was actually coming from. | agitate | — | R1 |
| P-005 | They bought the stretchy sleeve. | wrong fix | — | R1 · near-copy sleeve (blank) |
| P-006 | Then the one with the metal sides. | wrong fix | — | R1 · hinged brace (blank) |
| P-007 | Then the wrap, then the gel, then the one their neighbour swore by. | wrong fix | — | R1 · wrap / gel / strap (blank) |
| P-008 | And why would they not. | empathy | — | R1 |
| P-009 | The joint is where it hurts, and the joint is what the scan shows. | why | — | knee X-ray / scan (no readable numerals) |
| P-010 | But two centimetres below your kneecap there is a band of tendon about as wide as your thumb, and every step you take lands on it. | mechanism | 2 cm (F4) · thumb-width (tier 3) | ANAT-A · `[SITE]` |
| P-011 | Seventeen times your bodyweight. | mechanism | 17× (held) | ANAT-A load · overlay |
| P-012 | Put your finger under your kneecap and press. | self-test | — | R1 finger under kneecap (right knee) |
| P-013 | That band is the one taking it. | mechanism | — | ANAT-A point tight |
| P-014 | A sleeve squeezes the whole knee and leaves that band carrying everything. | mechanism | — | ANAT-A (sleeve pressure spread) |
| P-015 | A hinged brace stops the knee going sideways, and the knee was never going sideways. | mechanism | — | hinged brace on a knee |
| P-016 | So the drawer fills up, the years go by, and not one of them was ever aimed at the spot. | consequence | — | R1's drawer of supports |
| P-017 | Regret number two. | section | — | EG03 card · R2 |
| P-018 | They protected the bad knee with the good one. | agitate | — | R2 |
| P-019 | Nobody decides to do this. | empathy | — | R2 |
| P-020 | You lead with the good leg because it hurts less, and after a while you stop noticing. | behaviour | — | R2 leading with the left leg, kerb / bus step |
| P-021 | But the good leg is now doing the work of two, and the band on that side is taking a load it was never meant to take. | mechanism | — | ANAT-A, left knee |
| P-022 | That is why the second knee goes. | consequence | prevalence (**not in register**, F3) | R2 |
| P-023 | It is the most common thing in the whole postbag, and nobody sees it coming. | proof | prevalence (F3) | N TH / postbag |
| P-024 | Regret number three. | section | — | EG03 card · R3 |
| P-025 | They stopped saying yes, and they never said why. | agitate | — | R3 |
| P-026 | No to the long walk. | behaviour | — | R3 |
| P-027 | No to the day out. | behaviour | — | R3 |
| P-028 | No to the house with the steps up to the front door. | behaviour | — | R3 at the foot of front steps |
| P-029 | Not a decision, just easier than explaining. | empathy | — | R3 |
| P-030 | And the people around them thought they had gone off it. | consequence | — | R3 + family (one-offs) |
| P-031 | Here is what they say they wish someone had told them. | turn | — | **N TH** |
| P-032 | Coming down is worse than going up. | mechanism | — | stairs, descending |
| P-033 | Going up, your muscles lift you. | mechanism | — | stairs, ascending |
| P-034 | Coming down, you are catching yourself, and the catch lands on that band. | mechanism | — | ANAT-A load on the step down |
| P-035 | So you do not wrap the joint. | product logic | — | sleeve over the joint (blank) |
| P-036 | You go underneath it. | product logic | — | worn, front |
| P-037 | This one is called Stryde. | product | — | hero / held (`nano_banana_pro`) |
| P-038 | It sits two centimetres below the kneecap, on the tendon, and never crosses the joint. | product | 2 cm (F4) | worn front, straight leg (`PLACE-LOCK`) |
| P-039 | A silicone pad inside holds pressure on that one band instead of spreading it round the whole knee. | mechanism | pad material (held) | `PAD_BACK_SHOT` → ANAT-A |
| P-040 | The weight gets caught and moved off the worn part before it reaches the joint. | mechanism | protection | ANAT-A (relief) |
| P-041 | The placement is the whole thing. | product | — | seating beat (`SEAT_LOCK`) |
| P-042 | A centimetre too high and it is a sleeve again. | product | — | **wrong-height demo**: never shown worn wrong (§9 placement lock). Shown as the seating beat stopping at the right height, F6 |
| P-043 | Thirty four percent less strain. | proof | 34% (held) | worn, walking · overlay |
| P-044 | Measured. | proof | held | — |
| P-045 | Three years with orthopedic surgeons. | proof | held | surgeon (one-off, §19B approachable) |
| P-046 | Two hundred thousand people wearing one. | social proof | 200,000 (held) | montage · overlay |
| P-047 | Ten seconds to put on. | feature | **not in register** (F3) | seating beat |
| P-048 | No sores, no rolling down, and nobody can see it. | feature | — | §9D conceal: trousers over it |
| P-049 | And you do not have to take my word for it. | self-test | — | **N TH** |
| P-050 | One knee only. | self-test | — | R1 puts one on (right knee) |
| P-051 | Leave the other bare. | self-test | — | R1, left knee bare |
| P-052 | Go to your own stairs and come down forwards. | self-test | — | R1 on her stairs, facing down |
| P-053 | You will know in a minute. | self-test | — | R1 at the foot of the stairs |
| P-054 | Not because the arthritis has gone. | honesty | — | N TH |
| P-055 | It is still there. | honesty | — | N TH |
| P-056 | Because the weight is not landing on that band any more. | mechanism | protection | ANAT-A relief |
| P-057 | Most of those messages end the same way. | witness | — | N / postbag |
| P-058 | I wish somebody had told me this four years ago. | testimony | — | a printed message in hand (no readable text generated, §17) |
| P-059 | You are hearing it today. | close | — | **N TH** |
| P-060 | That is the only difference between you and them. | close | — | N TH |
| P-061 | Two for one, so you do both knees, which after regret number two is the point. | offer | BOGOF (held) | R2 wearing two, one per knee · box open, two straps |
| P-062 | Sixty days, and you keep the straps. | guarantee | 60 days (held) · "keep the straps" (**not in register**, F3) | two straps |
| P-063 | From the Stryde site. | CTA | — | end card (edit, §17) |
| P-064 | The copies stretch, and a stretched strap stops holding it. | objection | comparative (**unverified**, F5) | near-copy, `rounded mushy peaks` or `wide flat nylon webbing` archetype |
| P-065 | Go and do your stairs. | close | — | R3 coming down her daughter's front steps (the payoff of P-028) |

Hooks 3 · body 65 phrases · **uncovered 0 · blocked 0** (dispositions pending step 5).

### Claims (§43A)

Advertiser-held (Product Sheet claim register, user-confirmed V7.49.29): 17× bodyweight · three years with orthopaedic surgeons · silicone pad · 34% less strain, measured · 200,000+ wearers · Buy 1 Get 1 Free · sixty-day money-back. Numbers are post overlays, never generated (§17).

**Not in the register (voiced verbatim per §22U, flagged F3–F5):** 25,000 messages · "the most common thing in the whole postbag" (the second knee) · "two centimetres below the kneecap" · "ten seconds to put on" · "you keep the straps" · "the copies stretch".

### Mode & Model Lock (§18A)

| Beat class | Model · params | Why |
|---|---|---|
| Mode | **Mode 1 Realistic**, iPhone 17 Pro Max, 9:16 | realistic reference (§2); no Mode 4/5 instruction |
| Avatar sheets | `gpt_image_2_5` · `variant: sunburst` · `quality: high` · `resolution: 2k` | §19 measured route. **Used this delivery** |
| Narrator TH seeds + §22U voice-source image | `nano_banana_pro` | face class, talking-head seed |
| Wordmark with hands or a body (held, worn, seating) | `nano_banana_pro` | no GPT Image with a body in frame (§44 default 19) |
| Wordmark, no person (box, pack, two straps) | `gpt_image_2_5` sunburst | pack-shot class, no person |
| Volume B-roll with a person, no readable wordmark | `nano_banana_2` | volume |
| Mechanism (ANAT-A / ANAT-B) | `nano_banana_2` | §12A; no GPT Image |
| Video | Kling 3.0 `kling-video-v3_0_omni`, start image required, `prefer_multi_shots: false` | §4, §27G |
| Voice | §22U: 2+ Kling takes of N → ElevenLabs clone (you clone in the app) → Eleven v3 TTS → `vo_trim.py` house cut | §22U, E11A |
| Talking heads | HeyGen Avatar V, driven by the master, motion prompt on every render | §22U step 13, §44 default 84 |

**Other locks:** format **talking head + B-roll**. The reference has a narrator on camera (Style Lock), which agrees with §44 default 11, so this is recorded rather than asked. **Side: the right knee is the bad knee** (no knee named → `SIDE_RULE`); R2's good leg is the left, so P-021 shows the left knee · mechanism claim: protection · edit: `EDIT-STRYDE-THREE-REGRETS` · hooks: 3 in the script → 3 variants.

---

## 3. Cast (step 3) — generated, on the board for your check

Recurring subjects (≥ 2 beats): **N narrator** (TH P-001, P-031, P-049, P-054–P-060 · speaking) · **R1 Gail** (P-003–P-016, P-050–P-053) · **R2 Ken** (P-017–P-022, P-061) · **R3 Joan** (P-024–P-030, P-065). One-offs, not sheeted (§13): the surgeon (P-045), the family on P-030, the hook sufferers.

| Sheet | Job ID | File | Board |
|---|---|---|---|
| N-NARR | `4bb1467d-f843-4329-affe-b50470add366` | `cast/N-NARR_v1.png` | **Confirmed** (user, 2026-09-28) |
| R1-GAIL | `39306d36-3fbe-43ab-a8a8-43fc3d63b61c` | `cast/R1-GAIL_v1.png` | **Confirmed** (user, 2026-09-28) |
| R2-KEN | `4fe46b58-adec-4baf-bbf8-61f70a909fca` | `cast/R2-KEN_v1.png` | **Confirmed** (user, 2026-09-28) |
| R3-JOAN | `5684782d-e205-428b-a5f1-00a73d31f126` (v2) | `cast/R3-JOAN_v2.png` | To check. *v1 `f885e719…` sent to Fix: "make it look friendly and natural". v2 adds a FRIENDLY AND NATURAL register after her face fill (warm eyes, relaxed lids, mouth corners very slightly up, loose jaw, easy stance, not a posed smile) and drops `NEG-DEFAULT-FACE`'s last two clauses, as §19B does for clinicians. Face, hair, marker and wardrobe unchanged. Prompt `cast/R3-JOAN.v2.prompt.txt` (9,656 chars)* |

All are 1520×2688, one render per call, 6.25 credits each (31.25 total with the Joan Fix). Prompts: `cast/<ID>.prompt.txt`, built from Appendix A by ID in `cast/build_sheets.py` (`CAM-LOCK` → `AVATAR-SHEET` with `SHEET-GRID` → `SKIN-T` → `CAP-SHARP` → `CAP-FILE` → `NEG-SHEET` + `NEG-GRID` + `NEG-FILE` + `NEG-DEFAULT-FACE`), 9,211–9,302 chars each. R1's first marker (a port-wine mark) was swapped for bunions before sending, because `NEG-SHEET` bans birthmarks.

### Identity strings — read off the renders (§7), descriptive only (the check is yours)

| ID | Identity string |
|---|---|
| N | white British woman, 57, tall and wiry, narrow shoulders; long narrow face, high cheekbones, deep-set grey-green eyes, long nose, thin wide mouth; grey-brown hair with grey through the front, pulled back in a low knot; rust-orange needlecord overshirt open over a cream T-shirt; dark indigo jeans; tan leather lace-ups. *Gap tooth not visible on the sheet (mouth closed)* |
| R1 | white British woman, 62, tall and heavy through the hips; broad square face, full cheeks, pale-blue eyes, short nose; coppery auburn chin-length bob with a side parting; olive zip fleece over a navy-and-white check shirt; stone shorts a hand above the knee; grey socks; brown walking sandals. *Bunions not legible at sheet scale* |
| R2 | white British man, 72, small and wiry, straight-backed; long thin face, hollow cheeks, heavy dark-grey brows, long nose; sparse white hair combed back, scalp showing; pale-blue short-sleeved check shirt tucked into navy shorts just above the knee; brown belt; navy socks; brown leather shoes |
| R3 | white British woman, 79, small and slight; round soft face, hazel eyes, small nose; thick white pixie crop; a small scar through her right eyebrow; mustard cable-knit cardigan over a teal-and-cream floral dress just above the knee; bare legs; navy canvas slip-ons |

### §19A axis tables — clearance against the roster (stryde-identity N, C1–C4) and within this build

| Axis | N | R1 Gail | R2 Ken | R3 Joan |
|---|---|---|---|---|
| Face | long narrow, hooked nose | broad square, heavy jaw | thin long, hollow, broken nose | small round soft |
| Hair | grown-out dark dye, low knot | thin copper bob, scalp at the part | sparse white combed back | thick white pixie crop |
| Age position | 57 (young edge) | 62 | 72 | 79 (far edge) |
| Build | tall, wiry | tall, big-boned | small, wiry, straight-backed | small, slight, stooping |
| Class / wardrobe | customer-care / workroom casual | walker / allotment | ex-services, pressed | chapel Sunday-best (cardigan, floral dress) |
| Marker | gap between the front teeth | bunions | broken nose | scar through the brow |
| Voice | West Yorkshire (below) | non-speaking | non-speaking | non-speaking |
| Environment | workroom with the postbag | semi-detached house, stairs; allotment | high street, bus stop, club | ground-floor flat; daughter's house with front steps; chapel hall |

**Clearance (gate 5 of 8):** N vs roster N 6, C1 7, C2 7, C3 7, C4 8 · R1 vs C1 5, C2 6, C3 5, C4 7 · R2 vs C4 5 (hair and age close), N 7, C1 6, C2 6, C3 6 · R3 vs C1 6 (both white-haired at the band's far edge, both non-speaking), C3 6, C4 6. **Within the build** every pair clears 6–8. Lowest: R1–C1, R1–C3 and R2–C4 at 5 ✓.

### Narrator — `VOICE-NARR` (§22D) and §20 constraint sheet

**`VOICE-NARR`** (goes verbatim into every §22U step-2 take; the clone inherits it)
```
A woman of fifty-seven from West Yorkshire, a low dry alto, level and unhurried but brisk. Flat Yorkshire vowels, short "u", t's clipped; statements land and stop, no lift. A small breath before a number. Stress: slower and quieter on the turn word, never louder.
```

| Field | N — narrator |
|---|---|
| Accent | West Yorkshire (Leeds / Bradford), placed and unforced; never RP, never northern caricature |
| Pacing | ~185 wpm, the reference's 197 one notch down for the older audience |
| Posture / gesture / rig | TH at her workroom table or standing by the shelf of parcels; Economical gesture, one hand; eyeline on lens; R3 compressed (VSL) — framed at step 5 |
| Wardrobe never-list | white coat, scrubs, anything clinical (she is not a clinician), a suit |
| Physical never-list | never wears the product; may hold it or a printed message |
| Voice spec | `VOICE-NARR` above |
| Stress register | slower and quieter on "Not because the arthritis has gone." and "You are hearing it today." |
| Non-speech events | a small breath before a number; one dry half-laugh at most. Nothing else |
| Mouth | the gap tooth shows when her lips part. `TEETH-A` on every TH seed |
| Voice name (§22U step 7) | `Regrets` (keyword from the title). Check the account for a clash before cloning |

**Unverified:** `GEN-DEFAULT-female-50s` is not in the roster yet, so `VOICE-NARR`'s clearance against the generator default is argued (texture, rhythm, melody, habit), not measured.

---

## Flags (decisions for you; nothing below was changed silently)

| # | Where | Finding | Recommendation |
|---|---|---|---|
| **F1** | Format | The script heads the Door "VO", and the reference has the narrator on camera ~12% of the time | Hooks as VO over B-roll; narrator TH in the body at the turns (P-001, P-031, P-049, P-054–P-060). Say "voice-only" to drop the TH |
| **F2** | Narrator | Who "I" is: the reference narrator is a clinician; our script's narrator reads customer messages | Cast as a Stryde customer-care person, not a clinician, so no medical-authority claim is implied |
| **F3** | P-002, P-022–P-023, P-047, P-062 | 25,000 messages · second knee "most common in the postbag" · ten seconds to put on · keep the straps: not in the claim register | Voiced as written (§22U). Please confirm the advertiser holds them |
| F4 | P-010, P-038 | "two centimetres below the kneecap": the Product Sheet sets the height by contact (the kneecap's lower pole in the notch), never by a measured offset | Voiced as written; the picture follows the Product Sheet (`PLACE-LOCK`), and the 2 cm is never drawn as a measured gap |
| **F5** | P-064 | "The copies stretch": a comparative, unverified | Voiced as written; shown with a blank near-copy archetype. Please confirm |
| F6 | P-042 | "A centimetre too high and it is a sleeve again": the product is never shown worn wrong (§9 placement lock) | Show the seating beat stopping at the right height |
| F7 | P-039 | "silicone pad" | Voiced verbatim; prompts say "the pad" (Product Sheet ruling) |
| F8 | P-050 vs P-061 | "One knee only… leave the other bare" (the test) vs "Two for one, so you do both knees" | Not a conflict: the test is one knee and the offer is two. Noted only |
| F9 | Tooling | `script_lines.py` read two hook labels as spoken (Intake, tool finding) | Worked around here; I can fix the script if you want |
| F10 | Standards | `AVATAR-SHEET` says the back panel is "from the waist up", while `SHEET-GRID` and §19 say full length (carried from the last build's F8) | Proposed §34 amendment, still open |

## Next — on your go (§18B step 5)

Check the four avatars on the board (Confirm or Fix) and answer F1–F3 and F5 → steps 4–5 as one delivery: property and location maps with plates generated, the act map and wardrobe map with every row's angle, focus, light and `EDIT` layout (`angles.py` passing), then the §22U voice route for the narrator.
