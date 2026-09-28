# Build Sheet — stryde-cascade

**STRYDE Precision Strap · "C - VID | Picture In Picture | TOF | The Cascade | New | Four Hundred Houses"** · Standards V7.64.2 · **RUN: AUTOMATION** · 2026-09-28

Board: https://claude.ai/artifact/QK6FwiCxWuZqoWWVoEx2Yd · Drive task folder `1nOldjHSuTw6koTHeChJ5BDvZ1MtNBfld` (OUTPUT tree in `drive.json`).

---

## 0. Intake (§18B)

| Input | Found | Notes |
|---|---|---|
| Drive folder | `1nOldjHSuTw6koTHeChJ5BDvZ1MtNBfld` | `fetch_drive.py` → `intake/` |
| Inspo | `intake/inspo.mp4` (Drive name was a hash; renamed) — Meta Ad Library 1665142644551220 per the script | 142.1s · 9:16 · 360×640 · 29.97 fps · audio |
| Script | native Google Doc, exported `.docx` → `script.txt`; title on line 1 ✓ | 3 hooks ("Doors" A/B/C) + 22 body lines, a VO table, one writer's note |
| Product Sheet | `stryde_product_sheet_V7.49.32.py` | newer than the repo's V7.49.31 → `products/stryde/stryde_product_sheet.py` updated (adds `WORDMARK_LOCK`, `NEG_WORDMARK`, `wordmark_check()`) |
| Product images | 10 — byte-identical to `products/stryde/stryde_refs/` | layer 1 |
| Loom | none | no question, no flag (§18C) |
| Missing | `package_closed.jpg`, anatomy samples, `product_held.jpg` (Product Sheet self-test) | none blocks the build |

**Message fields read:** `run automation` → **RUN: AUTOMATION** (E0 trigger, explicit). No `BUILD` → `stryde-cascade` (the task title "The Cascade"). **No `MODE` → Mode 1**: the reference is realistic phone footage, and a realistic reference selects Mode 1 automatically (§44 default 31). No `HOOKS` → **in script: 3** → 3 variant videos (§30H). No `CAP` → E0 Mode 1–3 defaults: **Higgsfield 600 · Kling 3,000 · Kie 2,000**. No `VOICE` → derived (§22D), below. No `ADJUST`, no `DIRECTIONS`.

**Balances at start (2026-09-28 08:27 UTC):** Higgsfield 20,185.5 · Kling 4,087 · Kie 249,842.8. ElevenLabs clone check PASS (522 free slots).

---

## 1. Absorption Sheet (§42)

### Part 1 — measured

| Instrument | Reading | Settles |
|---|---|---|
| Duration / aspect / res | 142.1s · 9:16 · 360×640 · 29.97 fps | a long-form 9:16 talking-head ad; ours 9:16 locked |
| Scene cuts | **61 shots, mean 2.33s** (ffmpeg scene detect) | a cut every ~2.3s from start to finish, including cuts between talking-head takes |
| Silence (−30/−40 dB) | **none** | wall-to-wall voice, butt-joined |
| VO transcript (faster-whisper base.en) | 488 words / 142s = **206 wpm** | brisk, jump-cut delivery |
| TH / B-roll | ~55% talking head (seated expert), ~45% B-roll in three layouts | talking-head build → §22U steps 1–13, HeyGen |
| Shot frames + per-second sheets | `intake/frames/inspo/` (5 sheets) | Edit Grammar below |

### Part 2 — structure map (read off the sheets and the transcript)

| t | Job | What shows | Layout |
|---|---|---|---|
| 0–7 | **HOOK** — "X is not a Y problem" reframe + "I have treated thousands" authority + "take this seriously" | expert TH, two quick lifestyle cuts (people with the pain) | TH + full B-roll; red banner "TAKE THIS SERIOUSLY." |
| 7–42 | **mechanism of the problem** — what fails, the cascade of symptoms | TH ↔ full-screen 3D anatomy, lower-half split B-roll (pain moments), small PIP cards (body map, knee, lower back) | full / split / pip |
| 42–75 | **"you've been told…"** — why the usual fixes fail (physio, pills, cortisone) | TH with PIP cards of each fix (pill bottles), split B-roll of physio | pip / split |
| 75–113 | **the real fix → product** — the one thing that stops it, then the product and why the concentration matters | anatomy full-screen, product hero on a table, lifestyle | full |
| 113–128 | **proof** — "not me promoting", 3,000 patients, 97% relief | TH, split UGC testimonial | split |
| 128–142 | **close** — "share this with someone", "link below" | TH, PIP of a person with the pain, product still | pip / full |

### Part 3 — Style Lock (copied)

- **Presenter:** one older expert, seated, square to a propped phone, chest-up, centred; plain dark lived-in room, one window to camera-left; dark plain clothes. Same framing every talking-head cut, with occasional punch-ins (tighter scale on emphasis).
- **Delivery:** calm, grave, first person, short declaratives; authority from lived practice ("in my years of practice"); the pain framed as a sequence the viewer is already in.
- **Edit rhythm:** a cut every ~2.3s; talking-head takes jump-cut; B-roll arrives on the noun it names.
- **Density:** about half talking head, half B-roll; B-roll never runs more than ~4s.
- **Capture axis (never yields):** phone footage; ours runs the iPhone 17 Pro Max register (§22).

### Part 3A — Edit Grammar → `EDIT-STRYDE-CASCADE`

| ID | Device | Where (inspo) | When used | Parameters |
|---|---|---|---|---|
| EG01 | **pip** card | 0:34–0:40 (knee, lower back, body map), 1:10–1:13 (pill bottles), 2:10 | a noun the presenter names (a body part, a product, a remedy) | the TH stays full frame; a card **inside, lower-centre**, ~55% frame width, bottom edge ~12% up, square-ish, hard-cut in and out |
| EG02 | **split** | 0:07, 0:25, 0:30, 1:00, 1:12, 2:05–2:13 | a lived moment under the presenter's words | **top = TH, bottom = B-roll, seam at 50%** (TH band cropped to face and shoulders) |
| EG03 | **full** B-roll | throughout | anatomy, lifestyle, product hero | hard cut, 1–4s |
| EG04 | **punch-in** on the TH | 0:52, 1:35, 1:52 | emphatic lines | ~1.2× on the face, hard cut |
| EG05 | **captions** | every frame | always | one to three words at a time, white rounded box, black bold sans, lower-middle (~65% height); keyword in a red box |
| EG06 | **red banner** | 0:08 "TAKE THIS SERIOUSLY." | the hook's command | white bold caps on a red bar, top ~12%, over the TH |
| EG07 | **number overlay** | 1:20 "95%", 2:03 "97%" | a number in the VO | large bold white numerals with a dark stroke, centred on B-roll |
| — | not used | — | — | no transitions other than hard cuts, no speed ramps, no music bed audible over the VO, no SFX heard |

Captions, the banner and number overlays are CapCut lines (§17); `assemble.py` renders `full`, `split`, `pip` and punch-ins.

### Part 4 — script absorption

**Copy formula (reference):** reframe hook ("not a X problem") → authority by numbers ("thousands of patients") → "take this seriously" → the hidden mechanism → "you've been told it's…" → why each usual fix fails → the one thing that fixes it → product → proof → share → CTA.

| R-P | Reference | Job | Our line |
|---|---|---|---|
| R-P-001 | "Gluteal tendinopathy is not a hip problem…" | reframe hook | HK1 L1 "A bad knee is not a knee problem…" |
| R-P-002 | "I have treated over … thousand women" | authority | HK1 L2 "four hundred houses" (tradesman, not clinician) |
| R-P-003 | "I need you to take this seriously" | command | HK1 L3 (verbatim match) |
| R-P-004 | the cascade — hip → knee → back | mechanism of the problem | B01–B04 the stair sequence |
| R-P-005 | "tendons are mostly collagen… repair slows" | mechanism | B05–B08 the band, 17×, coming down |
| R-P-006 | "you've been told… sometimes part of it, never the full story" | objection | B09 (near-verbatim structure) |
| R-P-007 | physio / ibuprofen / cortisone never fix it | failed fixes | B10–B11 physio, gel, pills, sleeve |
| R-P-008 | "the only way…" → product | mechanism → product | B11–B14 |
| R-P-009 | 95% extract / "anything less will not work" | spec as proof | B14–B15 "the placement is the whole thing", 34% |
| R-P-010 | "not me promoting a solution" / 3,000 women, 97% | proof | B16–B18 "not paid by them", three houses |
| R-P-011 | "if you know someone… share this" | share | B21 |
| R-P-012 | "link below" | CTA | B20 offer |

**Voice fingerprint (ours):** first person, plain British tradesman ("favour", "centimetres", "physio"), short declaratives, numbers spoken in words, no exclamation. **Length:** hooks 49 / 49 / 42 words, body 511 words — each variant ≈ 3:10 at ~175 wpm after the house cut, longer than the inspo's 2:22; the cut rhythm carries it (≈ 80 cuts per variant).

### Part 5 — surfaced, not absorbed

| Reference element | Disposition |
|---|---|
| Clinician authority, "thousands of patients", 97% relief | not inherited; ours is a tradesman's observation, numbers are the advertiser's (claim register) |
| Third-party UGC testimonial clips, competitor bottle | not copied; our proof is the narrator + product demonstration |
| Moringa/estrogen CGI | position-not-look → our §12A anatomy register (patellar tendon below the kneecap) |

### Part 6 — beat-it plan

| Reference weakness | Our delta | Beats |
|---|---|---|
| Mechanism asserted, product never shown working on the body | real §12A beats on the band (load lands → pad catches → moved off) and worn-strap placement beats | B05–B08, B13–B14 |
| No self-test | "go to your own stairs and come down forwards" shown as a worn demonstration | B19 |
| Stock pain clips | one recurring subject whose house goes through the whole cascade (rail at the top → full length → bed downstairs) | B01–B04 |

---

## 2. Script, product, claims, locks (step 2)

### Hooks and body (verbatim, `script.lines.txt`)

- **HK1 (Door A)** — lines 1–3 · **HK2 (Door B)** — lines 4–6 · **HK3 (Door C)** — lines 7–8 · **BODY** — lines 10–31 (22 lines).
- **Dropped from the voice (not script speech):** the title, the reference link, the table headers `Door` / `VO`, the door letters, and the writer's note *"All three hand off to the same first body line. C is the strongest and the bleakest, and you should decide whether you want to run it…"* (line 9). `script_lines.py` kept that note as a spoken line; it is a note to the advertiser, so it is removed from `voice.lines.txt` and logged here — no spoken word changed.
- **Hook C decision (Automatic, the agent decides):** all three doors run — the script supplies three and the note recommends testing C. Listed in *Flags*.

### Visual Instruction Ledger (§27F)

`script_lines.py --visual` found **no visual notes** — the script carries none (a VO-only table). The ledger has one build-wide row: the format name in the title, **"Picture In Picture"** → the TH with pip/split B-roll (EG01–EG02). Status: carried by the act map (`layout` column) → verified at assembly.

### Claims pass (§43A) — against the Product Sheet claim register

| Line | Claim | Status |
|---|---|---|
| B06 | "Seventeen times your bodyweight" | advertiser-held (V7.49.29) — post overlay only |
| B13 | "a silicone pad inside" | advertiser-held; prompts say "the pad", never "silicone" (Product Sheet ruling) |
| B15 | "Thirty four percent less strain. Measured." | advertiser-held — post overlay |
| B15 | "Three years with orthopedic surgeons" | advertiser-held |
| B15 | "Two hundred thousand people wearing one" | advertiser-held — post overlay |
| B20 | "Two for one… Sixty days" | advertiser-held (Buy 1 Get 1 Free, 60-day guarantee) |
| B20 | "The copies stretch, and a stretched strap does not hold the spot" | **comparative, not in the register → flag F3** |
| B16 | "I am not paid by them" | **disclosure risk → flag F1**: the speaker is a paid, AI-generated presenter in a paid ad |
| B17 | "Three houses this year have not called me back" | anecdotal result from a fictional character, hedged in-line ("not a study") → **flag F2** |
| HK1 | "four hundred houses", a working rail fitter | a fictional persona's biography → covered by F1 |

### Mode & Model Lock (§18A)

| Class | Mode | Image model | Video |
|---|---|---|---|
| Avatar sheets | 1 | `gpt_image_2_5` Sunburst, high, 2k | — |
| Talking-head frame, every beat with a person | 1 | `nano_banana_pro` 2k (sheet attached) | HeyGen Avatar V (TH); Kling `kling-video-v3_0_omni` (B-roll, voice source) |
| Product / object beats, no person | 1 | `gpt_image_2_5` Sunburst | Kling omni |
| Mechanism (§12A anatomy) | §12A register | `nano_banana_pro` | Kling omni |
| Pinned end frame beats | 1 | as the class | `kling-video-v3_0` first + last frame |

### Voice (§22D) — `VOICE-N`

Derived (no `VOICE` line): see `voice/VOICE.md` once written at stage 6.

---

## 3. Cast (§19) — sheets on the board

| ID | Who | Role | Speaks |
|---|---|---|---|
| N | rail fitter, 61, white British, stocky, broken nose, scar through the right eyebrow; navy work fleece | narrator on camera (TH) + his own hands fitting rails in B-roll | yes |
| C1 | woman, 74, white British, small, white curls, mole on left cheekbone; lilac cardigan, navy skirt to the knee, slippers | the cascade: her stairs, her rails, her bed downstairs | no |
| C2 | man, 68, white British, heavyset, white moustache; olive polo, khaki shorts | wears the strap: placement, stairs demonstration, "come down forwards" | no |

Fills in `work/cast.py`; prompts in `renders/<ID>_sheet.prompt.txt`.

## Flags (running)

- **F1 — "I am not paid by them."** The presenter is a generated character in a paid ad; a first-person "not paid" statement may be a deceptive endorsement (FTC Endorsement Guides / ASA CAP Code 3.45). Voiced verbatim (§22U); the advertiser's counsel decides.
- **F2 — "Three houses this year have not called me back."** A result anecdote from a fictional person. Hedged in the line; flagged.
- **F3 — "The copies stretch…"** comparative claim not in the Product Sheet register.
- **F4 — Hook C** run as written (the script's note asks the advertiser to decide).
- **F5 — MODE not given** → Mode 1 from the realistic inspo (§44-31).
- **F6 — Model logging.** Every `nano_banana_pro` render is logged by Higgsfield as `nano_banana_2` (platform label); the request named `nano_banana_pro`.
- **F7 — Kling B-roll audio off.** B-roll clips were generated with `enable_audio: false` (their sound is replaced by the VO); only the voice-source takes carried audio.
- **F8 — Kling spend over cap.** The connector reports 8 credits/s (and 120 for a 10s voice take) but the account is charged about 2.8× that; the cap check before the last batch used the reported cost, so Kling closed at 3,496 spent against the 3,000 cap (+496).
- **F9 — HeyGen engine.** `avatar_v` rejected the motion prompt (no digital twin) → Avatar IV with expressiveness high + the motion prompt (E7 fallback).
- **F10 — VO pace.** The eleven_v3 master runs fast (~270 wpm body). Verbatim PASS; no speed change applied (house cut forbids it).
- **F11 — BODY master tail** ends at −44.8 dB, borderline to the −45 dB take gate; T4 was the only take below it and was kept.
- **F12 — "stretched"** in the last body line not verified word-for-word by the ASR (word present in the TTS text, verbatim PASS on the input).
- **F13 — Best-of-retries picks:** A2-M2 frame (side-on after two tries, row asked front); A3-B2 frame (third try, over-the-shoulder CU); A2-M1/M3/M4 clips (second generation after a diagnosed glow-placement fault; M3/M4 still light the front of the knee rather than a thin tendon strip); A4-M1 frame (front view, row asked profile).
- **F14 — Kept clean part:** A2-B3 used to 2.1s (he crouches oddly after); A1-B2 camera follows the legs slightly (1.7s on screen).
- **F15 — Continuity:** the Act 3 front-room beats in Day 2 wardrobe show the divan bed in the room (the bed "comes downstairs" in Act 1's list; the room plate carries it throughout).
- **F16 — Act 1 list cut on "Then".** A1-B4…A1-B7 cut on each "Then" (not the row key word) so no shot falls under 0.8s; lead 3 frames.
- **F17 — Kie balance** fell 10,010 during the run although this run only used Kie for free file uploads (no generation) — not attributable to this build; check the shared account.
- **F18 — Variant set check.** `variants.py` reported `body_identical_across_variants: false`; compared in whole frames (cut, layout, in-point, speed) the body is identical in all three. The difference was 0.01s rounding of exact half-frame times (e.g. 5.125s). All three variants PASS individually.
- **F19 — Delivery.** The finished videos (101 MB each) could not go to Drive (the connector takes inline content only) or onto the board (its 1 GB file store is full after 40 beats with all versions). They are at full quality on a separate private finals page, https://claude.ai/artifact/3uDVLnVKanAFsfna7pxvSb; the board's FINAL-HK1..3 cards and Drive `OUTPUT.md` link it. Talking-head tracks were padded by a held last frame (10–20 ms) and the hook tracks cut to their audio's frame count, so the body lip-sync and the last word stay intact.
