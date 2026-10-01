# Build Sheet — stryde-failed-alternatives

**STRYDE Precision Strap · "A - VID | Short VSL | TOF | Failed Alternatives | Iteration | Too Bad"** · Standards V7.68.2 · **RUN: MANUAL** · 2026-09-29

Steps 1–3 of §18. **Stopped at the avatar review (§18B, V7.62.0)**: steps 4–5 wait for the user's go.
Boards: Current https://claude.ai/artifact/CXmyrmezBb25rcyXJYk1fF · Old https://claude.ai/artifact/1LogbiXVkVQ3EU8rBiza2A · Final https://claude.ai/artifact/BDpgxcW4UDgKZCpRMExQkL · Plan https://claude.ai/artifact/JdfqS1zzWJY4k27eV7wjt2

---

## 0. Intake (§18B)

| Input | Found | Notes |
|---|---|---|
| Drive folder | `1GbYzHIQKw39DKonyeNI1owY3yE6hlcRn` | fetched with `fetch_drive.py` → `intake/`; matches no existing build → new build |
| Inspo | `INSPO VIDEO` (no extension, an MP4) → `intake/inspo.mp4`: the STRYDE "Too bad you have never worn these" ad (Meta Ad Library 1620934502990537, per the script) | 51.96s · 9:16 · 720×1280 · 30fps · audio. **The same reference as `stryde-too-bad`** (same duration, same 33 cuts, same transcript word for word, re-measured here) |
| Script | `Untitled document.docx` (the only document, so inferred as the script) → `intake/script.docx` | title line 1 ✓ · **3 hooks (A Sleeves, B NoneWorked, C Injections), each with its own body** |
| Product Sheet | `stryde_product_sheet_V7.49.29.py`: **older than the repo's V7.49.38** | the repo's V7.49.38 is used (`products/stryde/`) |
| Product images | 10 (front, back, side, ¾ left/right, macro, package open, worn front/rear/bent) | layer 1 |
| Missing | `package_closed.jpg`, `inner_face.jpg` in the folder (the repo has `inner_face.jpg`) | none blocks steps 1–3 |

**Message fields read:** `RUN MANUAL` → **RUN: MANUAL**. `BRITISH` → **VOICE: British** (the narrator). `MODE` blank → **Mode 1** (realistic reference, §2). `HOOKS` blank → **3 in the script → 3 finished videos** (HK1 + BODY1, HK2 + BODY2, HK3 + BODY3). `CAP` blank → E0 Higgsfield default. `BUILD` blank → `stryde-failed-alternatives`, from the title. No Loom.

**Script header note, applied as `ADJUST` lines (layer 5):** "Different Voice (keep British Accent on Eleven Labs) Brolls and editing than the original. Include +\- 50% of Black People on the B-Rolls + Music."
- **A different voice**: the reference narrator is a man; ours is a **British woman** (N, below), a new voice (not `stryde-too-bad`'s), cloned by §22U, voiced in Eleven v4. (F2)
- **Different B-roll and editing**: new cast, new locations, new shots; `EDIT-STRYDE-FA` keeps the reference's type of edit, never its shots.
- **About half the B-roll people Black**: recurring cast 2 of 4 Black (R1, R3); one-offs cast to hold ~50% across each finished video (checked at step 5 on the act map).
- **Music**: a music bed in the CapCut block (VN-H1).

---

## 1. Absorption Sheet (§42)

### Part 1 — measured

| Instrument | Reading | Settles |
|---|---|---|
| Duration / aspect / res | 51.96s · 9:16 · 720×1280 · 30fps | 9:16 locked |
| Scene cuts | **33 shots, mean 1.57s** (`fetch_inspo.py`; frames in `intake/frames/inspo/`) | a cut every ~1.6s |
| Silence (−30/−40 dB) | only the tail, 50.3–51.9s (black end frames) | wall-to-wall voice |
| Transcript (faster-whisper small) | 150 words over 50.5s of voice = **~180 wpm**, one male voice (`work/inspo_transcript.txt`) | brisk, even |
| On camera | **no talking heads**: narration over B-roll the whole way | voice-only build |
| Frames + per-second sheets | `intake/frames/inspo/sheet_01.jpg`, `sheet_02.jpg` | Edit Grammar below |

### Part 2 — structure map

| t | Job | What the reference shows | Layout |
|---|---|---|---|
| 0.0–3.1 | **hook**: "Too bad you have never worn these life-changing knee straps." | a clinician's hands seating the strap on a woman's knee; a woman standing in it in a clinic | full |
| 3.2–8.0 | credibility: three years with orthopaedic surgeons, "what sleeves and braces never could" | older hands opening the box; **split card**: STRYDE (glowing X-ray, strap) over BRACES (red-hot knee in a brace) | full → split |
| 8.2–12.3 | conditions: bone on bone, arthritis, worn cartilage, meniscus | X-ray knee glowing red; "MENISCUS" anatomy | full (CGI) |
| 12.6–16.7 | mechanism: 17× bodyweight through one small spot below the kneecap | "17X" overlay, red arrow down the tendon; red glow at the spot | full (CGI) |
| 17.0–21.8 | the strap redirects the load, the pain lifts | X-ray knee, strap glows blue; man in a garden, strap on | full |
| 22.1–29.5 | outcomes: walk further, stairs without the rail, move like you used to | woman walking in a park; man on stairs; woman in a garden; warehouse worker | full |
| 29.5–40.2 | features: adjustable, breathable, pad, no slipping / sores / rolling, under trousers, light | worn close-ups, in hand, seating, trousers pulled over it, clinic, living room | full |
| 40.4–43.3 | recommended by orthopaedic surgeons | man with a surgeon and a nurse in a clinic; man walking a street | full |
| 43.7–48.5 | offer: BOGOF, getstryde.co, 60-day guarantee | two straps on a table; dark end card "BUY 1 GET 1 FREE" + URL; man seating it in an armchair | full + card |
| 48.9–50.5 | close: "Nothing to lose but the pain." | hands at the knee, strap on | full |

### Part 3 — Style Lock (what we keep)

- **Voice-only**, one narrator, brisk and even; no one speaks on camera.
- **Realistic iPhone-register B-roll** (§22) of 55–80s wearing the strap in ordinary British places: home, stairs, garden, park, street, clinic.
- **Anatomy as glowing 3D X-ray renders** on every "why" line: red/orange on the pain, electric blue when the strap works (§11, §12A) — the Product Sheet's ANAT-A / ANAT-B looks.
- **One comparison card** early (the strap vs a brace), and **a dark offer card** with two straps at the end.
- Captions all the way through; hard cuts only.

### Part 3A — Edit Grammar (`EDIT-STRYDE-FA`)

| ID | Device (reference) | Where | Our build |
|---|---|---|---|
| EG01 | **Captions**: 2–5 words at a time, black text in a white rounded box, centred at ~66% height | whole ad | kept (CapCut line) |
| EG02 | **Full-screen B-roll**, no talking head, no PiP | whole ad | kept (house default) |
| EG03 | **Split card**: top half STRYDE (label bar "STRYDE PRECISION STRAP"), bottom half BRACES | "to do what sleeves and braces never could" (5.6–8.0s) | kept as our one `split` B-roll per video (≤ 1 in 5 boxed ✓): the strap vs a sleeve/brace (BODY1, BODY3), the strap vs the pile of old supports (BODY2) |
| EG04 | **Text overlays**: "17X" in heavy white italic with a red down-arrow; "BUY 1 GET 1 FREE" headline and the URL on a dark end card with two straps | 12.6s, 44–46s | kept (CapCut lines; numbers never generated, §17); plus "94%" on BODY2 |
| EG05 | **CGI anatomy**, X-ray blue with red pain glow; strap glowing blue on relief | 5–21s | kept, in the Product Sheet's looks (ANAT-A on the spot and the load; ANAT-B on the conditions) |
| EG06 | **Cut rhythm**: a hard cut every ~1.6s, no transitions, no speed ramps | whole ad | hard cuts kept; **rhythm overridden by the house hold (V7.65.0): every B-roll holds ~3.0s, never under 2.0s** (F14) |
| EG07 | Music bed | not measurable under the voice | **added**: the script asks for it (VN-H1); a light bed under the VO, ducked, in CapCut |
| EG08 | SFX | none heard | one: the drawer / cabinet slam in HK1 and HK2 (the script's "slammed shut", VN01/VN02) |

### Part 4 — script absorption

**Copy formula (reference → ours):** the reference's "too bad you have never worn these" hook becomes **"too bad about what you already tried"**: sleeves and braces (HK1), everything (HK2), injections (HK3). Each hook turns on "Thanks to these life-changing knee straps…" and each body explains why the old fix failed (it doesn't touch the one small spot), then runs the reference's own spine: surgeons → 17× through one small spot → strap moves the load → pain lifts → conditions → outcomes → features → proof → offer → close.

| Part | Words | ≈ at 175 wpm |
|---|---|---|
| HK1 — Sleeves | 21 | 7.2s |
| BODY1 | 137 | 47.0s |
| HK2 — NoneWorked | 20 | 6.9s |
| BODY2 | 135 | 46.3s |
| HK3 — Injections | 22 | 7.5s |
| BODY3 | 142 | 48.7s |
| **Each finished video** | 158 / 155 / 164 | **≈ 54s / 53s / 56s** (reference 52s) |

Pace gate: ≤ 210 wpm (§22U); target ~175 wpm (the reference's 180, a touch slower for a 55–80 audience).

### Part 5 — surfaced, not absorbed

| Reference element | Disposition |
|---|---|
| The reference's people, rooms and shots | not copied (the script asks for different B-roll); new cast §19A, new locations at step 4 |
| The male voice | replaced by a British woman (the script asks for a different voice) |
| Clinician's gloved hands seating the strap | the script asks for "the existing clinic strap-on shot" on the bridge line: **F4** |

### Part 6 — beat-it plan

| Reference weakness | Our delta | Where |
|---|---|---|
| Cuts every 1.6s: shots flash past before the eye finds the strap | ~3s holds, the strap readable in every worn shot | whole body |
| The hook shows a clinic, not the viewer's own history | each hook shows what the viewer already tried: the drawer of braces slammed (HK1), the cabinet slammed (HK2), the injection plaster peeled off (HK3) | HK1–HK3 |
| "one small spot" is said but only shown in CGI | a real finger pressing the spot below the kneecap, then the strap seated exactly there | BODY1–3 |
| A sleeve and the strap never seen side by side | a sleeve on one knee vs the strap on the spot, the split card on the brace line | BODY1, BODY3 |
| Mostly one register of person | cast balanced by the script's instruction: ~half Black, men and women, 57–78 | whole build |

### Part 7 — confirmation

Conflicts with the rules are listed in **Flags**. **Confirm or correct the absorption along with the avatars.**

---

## 2. Script, product, claims, locks (step 2)

Spoken lines, verbatim: `work/script_lines.txt` and per part `work/script_{HK1,BODY1,HK2,BODY2,HK3,BODY3}.txt`. `script_lines.py` read the header note, the hook names ("Sleeves", "NoneWorked", "Injections") and the "Body:" prefix as spoken; they were removed by hand (labels and quotation marks only — no spoken word touched).

### Visual Instruction Ledger (§27F), opened

| ID | Source | Instruction | Anchored | Carried by | Status |
|---|---|---|---|---|---|
| VN-H1 | script header | "Different Voice (keep British Accent on Eleven Labs) Brolls and editing than the original. Include +\- 50% of Black People on the B-Rolls + Music" | whole build | voice: N (British woman) · B-roll: new cast/locations, ~50% Black · edit: `EDIT-STRYDE-FA` · music: CapCut bed | open → steps 4–8 |
| VN01 | script L7 | "A drawer full of braces and sleeves, slammed shut. On the bridge line, cut to the existing clinic strap-on shot (the HOOK+BODY 2 opening), then the existing footage re-cut to the body below." | HK1 ("Too bad about all those sleeves and braces…" → bridge "Thanks to these life-changing knee straps…") | drawer: R1 Patricia's hall drawer, slammed (+ SFX) · bridge: **F4** | open → step 5 |
| VN02 | script L11 | "A cabinet full of braces and sleeves, slammed shut. On the bridge line, cut to the existing clinic strap-on shot (the HOOK+BODY 2 opening), then the existing footage re-cut to the body below." | HK2 ("Too bad nothing you've tried…" → bridge) | cabinet: R2 Gordon's bathroom cabinet, slammed (+ SFX) · bridge: **F4** | open → step 5 |
| VN03 | script L15 | "Visual: Editor's call." | HK3 | our pick (Part 6): R4 Sian peels a small round plaster off the side of her knee, stands, and the knee catches; bridge: the clinic strap-on shot as HK1/HK2 | open → step 5 |

### Phrase inventory (§27B): dispositions assigned at step 5

Variant n = HKn + BODYn. Shared lines are planned once and reused where the words match (B1-01 = B3-01; the conditions line, the "No slipping" line, the surgeons line, the offer and the close recur).

| ID | Phrase (short) | Job | Claim | Subject / register |
|---|---|---|---|---|
| HK1 | "Too bad about all those sleeves and braces you bought. Thanks to these life-changing knee straps, you won't need another one." | hook | life-changing (F10) | drawer of supports slammed → clinic strap-on (F4) |
| B1-01 | Built over three years with orthopaedic surgeons, to do what sleeves and braces never could. | credibility | 3 yrs ✓ · **F7** | box opened → **split card** (EG03) |
| B1-02 | A sleeve goes round the whole knee. The pain comes from one small spot. | answer | **F7** | a sleeve on a knee → finger presses below the kneecap |
| B1-03 | Seventeen times your bodyweight goes through it, just below your kneecap. | mechanism | 17× ✓ · just below ✓ | ANAT-A, 17X overlay |
| B1-04 | Squeezing the joint doesn't move that load. A cover is not a fix. | comparison | **F7** | ANAT-A, sleeve ghosted round the joint, the spot still red |
| B1-05 | This strap sits on the spot and redirects the load away from it. And the pain just lifts. | mechanism → relief | **F8** | strap seated (`SEAT_LOCK`) → ANAT-A blue → wearer's face easing |
| B1-06 | Perfect for bone on bone, arthritis, worn cartilage and meniscus pain. | conditions | ✓ | ANAT-B ghost limb |
| B1-07 | Take the stairs without gripping the railing. | outcome | **F9** | R1 down her hall stairs, hand off the rail |
| B1-08 | It doesn't stretch, so it doesn't give up by lunchtime. | feature | **F5** | the strap still in place late in the day (R3 at the bowls club) |
| B1-09 | No slipping. No sores. No rolling down. | features | **F9** | R2 walking, strap on |
| B1-10 | Recommended by orthopaedic surgeons for lasting relief. | proof | ✓ | surgeon one-off (§19B) with a wearer |
| B1-11 | Buy one, get one free today at getstryde.co. Sixty-day money-back guarantee. | offer | ✓ | box, two straps → dark offer card |
| B1-12 | Make this the last one you buy. Nothing to lose but the pain. | close | — | the drawer again, the strap on top, closed gently → R1 walking off |
| HK2 | "Too bad nothing you've tried for your knees has worked. Thanks to these life-changing knee straps, that's about to change." | hook | life-changing (F10) | cabinet of supports slammed → clinic strap-on (F4) |
| B2-01 | Built over three years with orthopaedic surgeons, for people who've tried the lot. | credibility | 3 yrs ✓ | the pile of old supports → **split card** vs the strap |
| B2-02 | Perfect for bone on bone, arthritis, worn cartilage and meniscus pain. | conditions | ✓ | as B1-06 (reused) |
| B2-03 | It's not you. And it's not your knees. | reassurance | — | R2 on the edge of the bed, rubbing his knee |
| B2-04 | Everything you've tried was made to keep you comfortable. None of it touched why it hurts. | comparison | **F7** | gel pack, sleeve, cream tube on a side table (unbranded) |
| B2-05 | Seventeen times your bodyweight goes through one small spot below your kneecap. | mechanism | 17× ✓ | ANAT-A, 17X overlay |
| B2-06 | This strap redirects the load away from that spot. And the pain just lifts. | mechanism → relief | **F8** | ANAT-A blue → wearer easing |
| B2-07 | Ninety-four percent feel the difference in the first few days. | proof | **F6** | 94% overlay over worn montage |
| B2-08 | So you can walk further without stopping. | outcome | — | R3 walking a park path |
| B2-09 | Adjustable, breathable, light enough you forget it's there. | features | **F9** · F11 | the fit (`SEAT_LOCK`), never adjusting → R4 on a hill path |
| B2-10 | No slipping. No sores. No rolling down. | features | **F9** | as B1-09 |
| B2-11 | Buy one, get one free today at getstryde.co. | offer | ✓ | as B1-11 |
| B2-12 | And if it's one more thing that doesn't work, send it back. Sixty-day money-back guarantee. Nothing to lose but the pain. | offer → close | ✓ | the box → R2 walking off |
| HK3 | "Too bad the injections wore off. Thanks to these life-changing knee straps, it doesn't have to go back to how it was." | hook | life-changing (F10) | plaster peeled off the knee, the knee catches → clinic strap-on (F4) |
| B3-01 | Built over three years with orthopaedic surgeons, to do what sleeves and braces never could. | credibility | as B1-01 | as B1-01 (reused) |
| B3-02 | Perfect for bone on bone, arthritis, worn cartilage and meniscus pain. | conditions | ✓ | as B1-06 (reused) |
| B3-03 | An injection quietens the knee. It doesn't change where the load goes. | comparison | **F7** | ANAT-A: the knee calm, then the spot glowing again |
| B3-04 | Seventeen times your bodyweight still goes through one small spot below your kneecap. | mechanism | 17× ✓ | ANAT-A, 17X overlay |
| B3-05 | So when it fades, the pain is right where you left it. | comparison | **F7** | R4 stops on her stairs, hand to the knee |
| B3-06 | This strap is mechanical. There's nothing to wear off. | answer | — | strap close front hold, wordmark |
| B3-07 | It redirects the load away from the worn spot, every step you take in it. And the pain just lifts. | mechanism → relief | **F8** | ANAT-A blue → R4 steps easily |
| B3-08 | No needle. No waiting room. No counting the weeks. | contrast | — | a calendar with crossed-off weeks → the strap on the kitchen table |
| B3-09 | So you can walk further without stopping. | outcome | — | as B2-08 (reused) |
| B3-10 | Adjustable and breathable. No slipping. No sores. No rolling down. | features | **F9** · F11 | seating → as B1-09 |
| B3-11 | Recommended by orthopaedic surgeons for lasting relief. | proof | ✓ | as B1-10 (reused) |
| B3-12 | Buy one, get one free today at getstryde.co. Sixty-day money-back guarantee. Nothing to lose but the pain. | offer → close | ✓ | as B1-11 → R4 walking off |

Coverage: 3 hooks + 36 body phrases · **uncovered 0 · blocked 0** (dispositions at step 5).

### Claims (§43A)

Held in the Product Sheet register (V7.49.38): 17× bodyweight · just below the kneecap · three years with orthopaedic surgeons · bone on bone / arthritis / worn cartilage / meniscus · recommended by orthopaedic surgeons · Buy 1 Get 1 Free · 60-day money-back guarantee. Numbers are post overlays, never generated (§17). **Not in the register:** F5–F9 (Flags). Voiced verbatim in every case (§22U): **a line is flagged, never rewritten.**

### Mode & Model Lock (§18A)

| Beat class | Model · params | Why |
|---|---|---|
| Mode | **Mode 1 Realistic**, iPhone 17 Pro Max, 9:16 (plates 16:9) | realistic reference; no Mode 4/5 instruction |
| Avatar sheets | `gpt_image_2_5` · `variant: sunburst` · `quality: high` · `resolution: 2k` | §19 measured route (**used this delivery**) |
| Wordmark with hands or a body (worn, seating, held) | `nano_banana_pro` + `WORDMARK-LOCK` | the name must read |
| Wordmark, no person (box, product hero, offer card) | `gpt_image_2_5` Sunburst, product refs under `image_references` | §4 routing |
| Volume B-roll with a person, no readable wordmark | `nano_banana_2` | volume |
| Anatomy (EG05) | `nano_banana_2`, ANAT-A / ANAT-B | §12A, Product Sheet §17 |
| Video | Kling 3.0 (`kling-video-v3_0_omni`), start image required, `prefer_multi_shots: false`; Kie `kling-3.0` when Kling is short | §4, §5, §27G |
| Voice | §22U: two Kling source takes of N → ElevenLabs clone by API → Enhance → Eleven v4, **all three hooks and all three bodies in one request**, split at the silences; VO trimmed in the house cut (`vo_trim.py`) | §22U, E11A |
| Talking heads | **none** (voice-only, as the reference) | Style Lock |
| Hooks | Kling (never Seedance: not called for, V7.68.2) | §4 |

**Other locks:** format **Short VSL, narrated B-roll, voice-only** · **side: right knee** (no knee named → `SIDE_RULE`) · mechanism claim: **protection** (Product Sheet §6) · edit: `EDIT-STRYDE-FA` · hooks: 3 → **3 videos, each hook with its own body** (§30H; `variants.py` builds each pair).

---

## 3. Cast (step 3): generated, on the board for your check

**Casting to the Product Sheet (British, 55–80, balanced men/women) and the script's instruction (about half Black):** four recurring wearers carry the B-roll across the three videos, two Black (R1 Bernadette, R3 Delroy — recast at your Fix) and two white, two women and two men. **N, the narrator, is never on screen**: her sheet exists only to make the two Kling clips her voice is cloned from (§22U). One-offs (the clinician on the bridge shot, the surgeon on the surgeons line, hands, extras) come at steps 4–5, balanced to keep about half Black. All five are new faces (§19A: reuse only on request).

| Sheet | Who | Job ID | File | Board |
|---|---|---|---|---|
| N-NARR | the narrator (voice only) | `994041a5-3e6f-47fb-947f-91a4c450237c` | `cast/N-NARR_v1.jpg` | **Confirmed** (user, 2026-09-29) |
| R1-BERNADETTE | wearer · the drawer (HK1), her hall stairs | `83478915-af9c-4d15-a24c-127f41ef944c` | `cast/R1-BERNADETTE_v1.jpg` | To check (replaced R1-PATRICIA, "change this avatar"; Patricia on the Old board) |
| R2-GORDON | wearer · the cabinet (HK2), walking | `4e0242ec-2b22-44cd-af29-4582ecb3bacb` | `cast/R2-GORDON_v1.jpg` | **Confirmed** (user, 2026-09-29) |
| R3-DELROY | wearer · bowls club, park path | `69175fd1-c1c8-4ae9-b3da-3b8ac3a797f2` | `cast/R3-DELROY_v1.jpg` | To check (replaced R3-EMMANUEL, "change this avatar"; Emmanuel on the Old board) |
| R4-SIAN | wearer · the injection plaster (HK3), her stairs, a hill path | `df90c511-adee-4c35-8bd8-e2ea0c9f53b5` | `cast/R4-SIAN_v1.jpg` | **Confirmed** (user, 2026-09-29) |

Manual run: **I don't check the sheets** (§18B step 3). Confirm or Fix each on the board. Prompts: `cast/<ID>.prompt.txt`, assembled from Appendix A by ID in `cast/build_sheets.py` (`CAM-LOCK` → `AVATAR-SHEET` + `SHEET-GRID` → `SKIN-T` → `CAP-SHARP` → `CAP-FILE` → `NEG-SHEET` + `NEG-GRID` + `NEG-FILE` + `NEG-DEFAULT-FACE`), 9,168–9,286 chars each. Spend: 5 Sunburst jobs, one render each, + 2 for the Fix recasts. Higgsfield 17,448 credits before the cast.

### Identity strings (from the prompts; read off the renders once you confirm them, §7)

| ID | Identity string |
|---|---|
| N | white British woman, 61, short and heavyset; broad round face, full soft cheeks, heavy-lidded pale blue eyes, short snub nose, wide mouth with a fuller lower lip; small round pitted chickenpox scar mid-forehead; short white spiky crop; bottle-green cardigan over a navy-and-white Breton top, dark jeans, navy canvas slip-ons |
| R1 | Black British woman (Nigerian heritage), 69, small and slight, narrow shoulders; wide face, broad flat forehead, round full cheeks, small deep-set dark eyes, short broad nose, small neat mouth; three small dark moles in a row along the left jawline; grey-and-black short locs to the jaw; rust-orange roll-neck under an olive quilted gilet, charcoal jersey skirt above the knee, burgundy suede trainers |
| R2 | white British man, 63, medium height, pot belly, heavy shoulders, thin legs; broad flat face, heavy jowls, small dark eyes, one thick dark eyebrow unbroken across the nose, short wide nose, thin mouth; thick salt-and-pepper hair brushed forward; navy Harrington jacket over a grey marl T-shirt, black football shorts above the knee, scuffed white trainers |
| R3 | Black British man (Jamaican heritage), 60, tall and heavy, broad chest, big belly; long rectangular face, heavy brow ridge, deep-set dark eyes, wide nose, broad mouth, clean-shaven; thick raised scar down the outside of the right forearm; salt-and-pepper flat-top, sides faded; royal-blue tracksuit top over a white T-shirt, grey jersey shorts above the knee, black-and-white trainers |
| R4 | white British woman (Welsh heritage), 57, tall and very thin; angular face, narrow grey eyes, long straight nose, slight overbite, sharp narrow chin; pale burn scar across the back of the left hand; long grey-blonde hair in a single plait; purple waterproof jacket over a black base layer, black running shorts above the knee, grey trail shoes |

### §19A axis tables

| Axis | N | R1 | R2 | R3 | R4 |
|---|---|---|---|---|---|
| Face | broad round, soft cheeks, snub nose | wide, flat forehead, round cheeks | broad flat, jowly | long rectangular, heavy brow | angular, narrow chin, overbite |
| Hair | white spiky crop | grey-black short locs | salt-and-pepper, forward fringe | salt-and-pepper flat-top | long grey-blonde plait |
| Age | 61 | 69 | 63 | 60 (young side) | 57 (young edge) |
| Build | short, heavyset | small, slight | medium, pot belly | tall, heavy, big belly | tall, very thin |
| Wardrobe | green cardigan + Breton | rust roll-neck + olive gilet + skirt | Harrington + football shorts | blue tracksuit top + jersey shorts | purple waterproof + running shorts |
| Marker | forehead pock scar | three moles along the jaw | unbroken single brow | forearm scar | burn scar, left hand |
| Voice | British, West Country (below) | non-speaking | non-speaking | non-speaking | non-speaking |
| Environment | — (voice only) | her hall, drawer, stairs | bathroom cabinet, streets | bowls club, park | stairs, hill path with a dog |

**Clearance within the build:** every pair differs on ≥ 6 axes. **Against the roster** (every Build Sheet's §19A table, incl. `stryde-too-bad` N, Denise, Alan, Clive, Fiona): every new face differs on ≥ 5 axes; the replaced R1 Patricia and R3 Emmanuel are cleared too (R1: face, hair, age, build, wardrobe, marker, environment; R3: face, hair, age, build, wardrobe, marker: ≥ 6); the closest roster entry is N vs the 72-year-old short round man (hair, age, sex, marker, wardrobe, voice, environment: 7). No marker repeats a roster marker. ✓

### Narrator: `VOICE-NARR` (§22D) and §20 constraint sheet

**`VOICE-NARR`** (goes verbatim into both §22U step-2 takes)
```
A British woman of sixty-one from Bristol, a warm mid-low voice with a soft West Country burr worn smooth by years of talking to the public, plain and kind, as if telling a neighbour over the fence what finally worked. Rounded vowels and a light rhotic r, never RP, never a caricature, never American. Sympathetic on the "too bad" lines, brisk and sure on the facts, the numbers slightly slower, never louder. Even, about one hundred and seventy-five words a minute.
```

| Field | N — narrator |
|---|---|
| Accent | Bristol / West Country worn smooth, light rhotic r; never RP, never American |
| Pacing | ~175 wpm (reference 180) |
| On camera | never (voice-only build); the sheet is only for the two Kling source clips |
| Audio proximity | close, dry, studio-quiet |
| Stress register | the "Too bad…" openers sympathetic, a touch rueful; "A cover is not a fix.", "It's not you.", "There's nothing to wear off." slower and lower, never bigger |
| Non-speech events | one short in-breath before a number; nothing else |
| Voice name (§22U step 7) | **`Alternatives`** — voice ID `uh69ybRPQgahYncj0lYN` (cloned 2026-09-29 from three Kling takes) |

---

## Flags (decisions for the user: nothing below was changed silently)

| # | Where | Finding | Recommendation |
|---|---|---|---|
| F1 | Product Sheet | The Drive copy is V7.49.29; the repo has V7.49.38 | Using V7.49.38 |
| **F2** | Voice | "Different Voice": the reference is a man; I cast a **British woman** narrator (West Country), new to this build | Say "male narrator" if you meant a different man's voice |
| F3 | Format | Three hooks, **each with its own body** | 3 finished videos; all hooks and bodies voiced in one TTS request so the voice matches |
| **F4** | VN01, VN02 (HK1–HK3 bridge) | "cut to the **existing** clinic strap-on shot (the HOOK+BODY 2 opening), then the **existing footage** re-cut to the body": that footage is not in the Drive folder, and the header asks for **different B-roll than the original** | **Recommended:** I generate our own clinic strap-on shot (a clinician seating the strap on the hook's wearer, new cast) and all-new body footage. If you meant your existing footage, put it in the Drive folder and I'll cut it in instead |
| **F5** | B1-08 | "It doesn't stretch, so it doesn't give up by lunchtime": the Product Sheet says the band is **black elastic** — this contradicts the product spec (layer 2) | Voiced as written (verbatim rule); never shown stretching or not. **Please confirm with the advertiser** — the line may need rewording by them |
| **F6** | B2-07 | "Ninety-four percent feel the difference in the first few days": not in the register | Voiced as written; 94% as a post overlay only. Please confirm the advertiser holds it |
| **F7** | B1-01/02/04, B2-04, B3-03/05 | Comparative claims — "what sleeves and braces never could", "A cover is not a fix", "None of it touched why it hurts", **"An injection quietens the knee. It doesn't change where the load goes… when it fades, the pain is right where you left it"** (a claim about a medical treatment) | Voiced as written; sleeves/braces shown unbranded, no needle or syringe ever shown. Please confirm the advertiser holds them, the injection lines above all |
| F8 | B1-05, B2-06, B3-07 | "redirects the load away from…": load-path wording; the Product Sheet's claim is **protection** | Voiced as written; pictured as protection (the strap takes the load off the spot) |
| **F9** | B1-07/09, B2-09/10, B3-10 | "Take the stairs without gripping the railing", "No slipping. No sores. No rolling down.", "light enough you forget it's there", "Adjustable, breathable": not in the register | Voiced as written; shown as wearers moving. Please confirm |
| F10 | HK1–HK3 | "life-changing" | Puffery, voiced as written; nothing shown for it |
| F11 | B2-09, B3-10 | "Adjustable" (Product Sheet §12) | Shown as the fit (the seating beat), never adjusting; the word never enters a prompt |
| F12 | B1-10, B3-11 | "Recommended by orthopaedic surgeons" | A surgeon one-off per §19B at steps 4–5 |
| F13 | Casting | "Include +\- 50% of Black People on the B-Rolls" | Applied: recurring cast 2 of 4 Black; one-offs balanced; checked per video on the act map |
| F14 | EG06 | The reference cuts every ~1.6s; the house rule (V7.65.0) holds every B-roll ~3.0s, never under 2.0s | House rule wins: ~16–18 B-rolls per video instead of 33 |
| F15 | Script file | Named "Untitled document"; header note and hook names read as spoken | Handled (see step 2) |

## Next — on your go (§18B step 5)

Confirm or Fix each avatar on the board and answer the bold flags (F2, F4, F5, F6, F7, F9). Then steps 4–5 as one delivery: locations as 16:9 plates (R1's hall with the drawer and stairs, R2's bathroom and a street, R3's bowls club and a park, R4's stairs, kitchen and a hill path, the clinic), the act map and wardrobe map for all three videos with every row's angle, focus, light and layout (`angles.py` passing); then the voice straight through (two Kling source clips of N → clone → VO takes on the board → house-cut trim).
