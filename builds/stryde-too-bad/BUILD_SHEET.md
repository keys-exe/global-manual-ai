# Build Sheet — stryde-too-bad

**STRYDE Precision Strap · "A - VID | Short VSL | TOF | Objection First | Iteration | Too Bad"** · Standards V7.68.2 · **RUN: MANUAL** · 2026-09-29

Steps 1–3 of §18. **Stopped at the avatar review (§18B, V7.62.0)**: steps 4–5 wait for the user's go.
Boards: Current https://claude.ai/artifact/DW6GGWmvHtVhDJrWaxT1JZ · Old https://claude.ai/artifact/GFL3d6zEr8E4bPENfKkyTq · Final https://claude.ai/artifact/3phx9ujBsxcHiEcsgm3xPN · Plan https://claude.ai/artifact/D5erRJZXiEc2YeMYMyo829

---

## 0. Intake (§18B)

| Input | Found | Notes |
|---|---|---|
| Drive folder | `1sRxZ8thrNmqmo1hVO3MJxY_-dCHGlsxE` | fetched with `fetch_drive.py` → `intake/`; matches no existing build → new build |
| Inspo | `INSPO VIDEO` (no extension, an MP4) → `intake/inspo.mp4`: the STRYDE "Too bad you have never worn these" ad (Meta Ad Library 1620934502990537, per the script) | 51.96s · 9:16 · 720×1280 · 30fps · audio |
| Script | `Untitled document.docx` (the only document, so inferred as the script) → `intake/script.docx` | title line 1 ✓ · **2 hooks (A TooSmall, B Gimmick), each with its own body** |
| Product Sheet | `stryde_product_sheet_V7.49.29.py`: **older than the repo's V7.49.37** | the repo's V7.49.37 is used (`products/stryde/`) |
| Product images | 10 (front, back, side, ¾ left/right, macro, package open, worn front/rear/bent) | layer 1 |
| Missing | `package_closed.jpg`, `inner_face.jpg` in the folder (the repo has `inner_face.jpg`) | none blocks steps 1–3 |

**Message fields read:** `RUN MANUAL` → **RUN: MANUAL**. `BRITISH` → **VOICE: British** (the narrator). `MODE` blank → **Mode 1** (realistic reference, §2). `HOOKS` blank → **2 in the script → 2 finished videos** (HK1 + BODY1, HK2 + BODY2). `CAP` blank → E0 Higgsfield default. `BUILD` blank → `stryde-too-bad`, from the title. No Loom.

**Script header note, applied as `ADJUST` lines (layer 5):** "Different Voice (keep British Accent on Eleven Labs) Brolls and editing than the original. Include +/- 50% of Black People on the B-Rolls + Music."
- **A different voice**: the reference narrator is a man (median pitch 132 Hz); ours is a **British woman** (N, below), cloned by §22U, voiced in Eleven v4. (F2)
- **Different B-roll and editing**: new cast, new locations, new shots; `EDIT-STRYDE-TB` below keeps the reference's type of edit, never its shots.
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
| Transcript (faster-whisper small) | 150 words over 50.2s of voice = **~180 wpm**, one male voice (median pitch 132 Hz) (`work/inspo_transcript.txt`) | brisk, even |
| On camera | **no talking heads**: narration over B-roll the whole way | voice-only build |
| Frames + per-second sheets | `intake/frames/inspo/sheet_01.jpg`, `sheet_02.jpg` | Edit Grammar below |

### Part 2 — structure map

| t | Job | What the reference shows | Layout |
|---|---|---|---|
| 0.0–2.7 | **hook**: "Too bad you have never worn these life-changing knee straps." | a clinician's hands seating the strap on a woman's knee; a woman standing in it in a clinic | full |
| 3.2–8.0 | credibility: three years with orthopaedic surgeons, "what sleeves and braces never could" | older hands opening the box; **split card**: STRYDE (glowing X-ray, strap) over BRACES (red-hot knee in a brace) | full → split |
| 8.2–12.3 | conditions: bone on bone, arthritis, worn cartilage, meniscus | X-ray knee glowing red; "MENISCUS" anatomy | full (CGI) |
| 12.6–16.7 | mechanism: 17× bodyweight through one small spot below the kneecap | "17X" overlay, red arrow down the tendon; red glow at the spot | full (CGI) |
| 17.0–21.8 | the strap redirects the load, the pain lifts | X-ray knee, strap glows blue; man in a garden, strap on | full |
| 22.1–29.5 | outcomes: walk further, stairs without the rail, move like you used to | Black woman walking in a park; man on stairs; woman in a garden; warehouse worker | full |
| 29.5–40.2 | features: adjustable, breathable, pad, no slipping / sores / rolling, under trousers, light | worn close-ups, in hand, seating, trousers pulled over it, clinic, living room | full |
| 40.4–43.3 | recommended by orthopaedic surgeons | Black man with a surgeon and a nurse in a clinic; Black man walking a street | full |
| 43.7–48.5 | offer: BOGOF, getstryde.co, 60-day guarantee | two straps on a table; dark end card "BUY 1 GET 1 FREE" + URL; man seating it in an armchair | full + card |
| 48.9–50.2 | close: "Nothing to lose but the pain." | hands at the knee, strap on | full |

### Part 3 — Style Lock (what we keep)

- **Voice-only**, one narrator, brisk and even; no one speaks on camera.
- **Realistic iPhone-register B-roll** (§22) of 55–80s wearing the strap in ordinary British places: home, stairs, garden, park, street, clinic, a workplace.
- **Anatomy as glowing 3D X-ray renders** on every "why" line: red/orange on the pain, electric blue when the strap works (§11, §12A) — the Product Sheet's ANAT-A / ANAT-B looks.
- **One comparison card** early (the strap vs a brace), and **a dark offer card** with two straps at the end.
- Captions all the way through; hard cuts only.

### Part 3A — Edit Grammar (`EDIT-STRYDE-TB`)

| ID | Device (reference) | Where | Our build |
|---|---|---|---|
| EG01 | **Captions**: 2–5 words at a time, black text in a white rounded box, centred at ~66% height | whole ad | kept (CapCut line) |
| EG02 | **Full-screen B-roll**, no talking head, no PiP | whole ad | kept (house default) |
| EG03 | **Split card**: top half STRYDE (label bar "STRYDE PRECISION STRAP"), bottom half BRACES, one line of each | "to do what sleeves and braces never could" (5.6–8.0s) | kept as our one `split` B-roll per video (≤ 1 in 5 boxed ✓): our strap vs a big brace, on the brace/sleeve line |
| EG04 | **Text overlays**: "17X" in heavy white italic with a red down-arrow on the 17× line; "BUY 1 GET 1 FREE" headline and the URL on a dark end card with two straps | 12.6s, 44–46s | kept (CapCut lines; numbers never generated, §17) |
| EG05 | **CGI anatomy**, X-ray blue with red pain glow; strap glowing blue on relief | 5–21s | kept, in the Product Sheet's looks (ANAT-A full stack on the spot and the load; ANAT-B ghost limb on the conditions) |
| EG06 | **Cut rhythm**: a hard cut every ~1.6s, no transitions, no speed ramps | whole ad | hard cuts kept; **rhythm overridden by the house hold (V7.65.0): every B-roll holds ~3.0s, never under 2.0s** (F14) |
| EG07 | Music bed | not measurable under the voice | **added** — the script asks for it (VN-H1); a light bed under the VO, ducked, in CapCut |
| EG08 | SFX | none heard | none |

### Part 4 — script absorption

**Copy formula (reference → ours):** "too bad you have never…" hook → surgeon credibility → what sleeves and braces can't → the one small spot + 17× → strap moves the load → pain lifts → conditions → outcomes → features → proof → offer → risk reversal → close. **Ours turns the hook into an objection** ("look too small to work" / "look like another gimmick") and each body answers that objection, then lands on the same offer and close.

| Part | Words | ≈ at 175 wpm |
|---|---|---|
| HK1 — TooSmall | 10 | 3.4s |
| BODY1 | 147 | 50.4s |
| HK2 — Gimmick | 9 | 3.1s |
| BODY2 | 148 | 50.7s |
| **Each finished video** | 157 / 157 | **≈ 54s** (reference 52s) |

Pace gate: ≤ 210 wpm (§22U); target ~175 wpm (the reference's 180, a touch slower for a 55–80 audience).

### Part 5 — surfaced, not absorbed

| Reference element | Disposition |
|---|---|
| The reference's people, rooms and shots | not copied (the script asks for different B-roll); new cast §19A, new locations at step 4 |
| The male voice | replaced by a British woman (the script asks for a different voice) |
| "life-changing" | not in our script |
| Clinician's gloved hands seating the strap | not copied; seating shown by the wearer (`SEAT_LOCK`), a clinician appears only on the surgeon line (§19B) |

### Part 6 — beat-it plan

| Reference weakness | Our delta | Where |
|---|---|---|
| Cuts every 1.6s: shots flash past before the eye finds the strap | ~3s holds, the strap readable in every worn shot | whole body |
| The hook shows a clinic, not the objection | each hook shows the objection itself: the strap small in a palm next to a big brace (HK1); a drawer of old supports (HK2) | HK1, HK2 |
| "one small spot" is said but only shown in CGI | a real finger pressing the spot below the kneecap, then the strap seated exactly there | BODY1, BODY2 |
| Mostly one register of person | cast balanced by the script's instruction: ~half Black, men and women, 55–80 | whole build |

### Part 7 — confirmation

Conflicts with the rules are listed in **Flags**. **Confirm or correct the absorption along with the avatars.**

---

## 2. Script, product, claims, locks (step 2)

Spoken lines, verbatim: `work/script_lines.txt` and per part `work/script_{HK1,BODY1,HK2,BODY2}.txt`. `script_lines.py` read the header note, the hook names ("TooSmall", "Gimmick") and the "Body:" prefix as spoken; they were removed by hand (labels and quotation marks only — no spoken word touched).

### Visual Instruction Ledger (§27F), opened

| ID | Source | Instruction | Anchored | Carried by | Status |
|---|---|---|---|---|---|
| VN-H1 | script header | "Different Voice (keep British Accent on Eleven Labs) Brolls and editing than the original. Include +/- 50% of Black People on the B-Rolls + Music" | whole build | voice: N (British woman) · B-roll: new cast/locations, ~50% Black · edit: `EDIT-STRYDE-TB` · music: CapCut bed | open → steps 4–8 |
| VN01 | script L4 | "Visual: Editor's call." | HK1 | our pick (Part 6): the strap small in a palm beside a big hinged brace | open → step 5 |
| VN02 | script L8 | "Visual: Editor's call." | HK2 | our pick (Part 6): a drawer of old supports, then the strap | open → step 5 |

### Phrase inventory (§27B): dispositions assigned at step 5

Variant 1 = HK1 + BODY1 · Variant 2 = HK2 + BODY2. Shared lines are planned once and reused where the words match.

| ID | Phrase (short) | Job | Claim | Subject / register |
|---|---|---|---|---|
| HK1 | "Too bad these knee straps look too small to work." | hook (objection) | — | strap in a palm beside a big brace |
| B1-01 | Built over three years with orthopaedic surgeons, to do what sleeves and braces never could. | credibility | 3 yrs ✓ · **F4** | box opened / surgeon hands → **split card** (EG03) |
| B1-02 | They're small on purpose. Because the pain comes from one small spot. | answer | **F4** | finger presses below the kneecap |
| B1-03 | Seventeen times your bodyweight goes through it, two centimetres below your kneecap. | mechanism | 17× ✓ · **F5** | ANAT-A, 17X overlay |
| B1-04 | A big brace wraps the whole knee and misses it. This sits right on it. | comparison | **F4** | brace on a knee → strap seated (`SEAT_LOCK`) |
| B1-05 | It redirects the load away from the worn spot. And the pain just lifts. | mechanism → relief | **F6** | ANAT-A red → blue; wearer's face easing |
| B1-06 | A scalpel, not a sledgehammer. | line | **F4** | strap close front hold, wordmark |
| B1-07 | Perfect for bone on bone, arthritis, worn cartilage and meniscus pain. | conditions | ✓ | ANAT-B ghost limb |
| B1-08 | So you can walk further without stopping. | outcome | — | R1 walking a park path |
| B1-09 | Small enough to sit flat under your trousers. Light enough you forget it's there. | features | **F7** | trousers over the strap (§9D); R2 in his garden |
| B1-10 | No slipping. No sores. No rolling down. | features | **F7** | R3 at work, strap on |
| B1-11 | Over two hundred thousand people wear one now. | proof | 200k ✓ | quick worn montage, 200,000 overlay |
| B1-12 | Buy one, get one free today at getstryde.co. Sixty-day money-back guarantee. | offer | ✓ | box, two straps → dark offer card |
| B1-13 | Too small to work? Try it on your own stairs. Nothing to lose but the pain. | close | — | R4 down her stairs, easy |
| HK2 | "Too bad these knee straps look like another gimmick." | hook (objection) | — | drawer of old supports → the strap |
| B2-01 | Built over three years with orthopaedic surgeons, to do what sleeves and braces never could. | credibility | as B1-01 | as B1-01 (reused) |
| B2-02 | You've been stung before. Fair enough. So here's what a gimmick never has. A mechanism. | answer | — | wearer shrugs off an old sleeve → ANAT |
| B2-03 | Seventeen times your bodyweight goes through one small spot below your kneecap. | mechanism | 17× ✓ | ANAT-A, 17X overlay |
| B2-04 | This strap redirects the load away from that spot. | mechanism | **F6** | ANAT-A blue |
| B2-05 | In a sports medicine study, the strain was cut by thirty-four percent. And the pain just lifts. | proof → relief | **F8** | 34% overlay; wearer easing |
| B2-06 | Perfect for bone on bone, arthritis, worn cartilage and meniscus pain. | conditions | ✓ | as B1-07 (reused) |
| B2-07 | Over two hundred thousand people wear one now. | proof | ✓ | as B1-11 |
| B2-08 | Adjustable, breathable, with a silicone pad that locks the pressure right where you need it. | features | pad ✓ · **F10, F11** | seating beat (`SEAT_LOCK`) → `PAD_BACK_SHOT` |
| B2-09 | No slipping. No sores. No rolling down. | features | **F7** | as B1-10 |
| B2-10 | Recommended by orthopaedic surgeons for lasting relief. | proof | ✓ | surgeon one-off (§19B) with a wearer |
| B2-11 | Only at getstryde.co. Not the knock-offs on Amazon. | offer | **F9** | a cheap copy (`FAKE-BASE` + one archetype) on a real table → the real strap |
| B2-12 | Buy one, get one free today. And a gimmick doesn't give you sixty days to send it back. Nothing to lose but the pain. | offer → close | ✓ | two straps in the box → R4 walking off |

Coverage: 2 hooks + 25 body phrases · **uncovered 0 · blocked 0** (dispositions at step 5).

### Claims (§43A)

Held in the Product Sheet register (V7.49.37): 17× bodyweight · three years with orthopaedic surgeons · silicone pad (prompts say "the pad") · 34% less strain (sports scientists) · bone on bone / arthritis / worn cartilage / meniscus · recommended by orthopaedic surgeons · 200,000+ wearers · Buy 1 Get 1 Free · 60-day money-back guarantee. Numbers are post overlays, never generated (§17). **Not in the register:** F4–F9 (Flags). Voiced verbatim in every case (§22U): **a line is flagged, never rewritten.**

### Mode & Model Lock (§18A)

| Beat class | Model · params | Why |
|---|---|---|
| Mode | **Mode 1 Realistic**, iPhone 17 Pro Max, 9:16 (plates 16:9) | realistic reference; no Mode 4/5 instruction |
| Avatar sheets | `gpt_image_2_5` · `variant: sunburst` · `quality: high` · `resolution: 2k` | §19 measured route (**used this delivery**) |
| Wordmark with hands or a body (worn, seating, held) | `nano_banana_pro` + `WORDMARK-LOCK` | the name must read |
| Wordmark, no person (box, product hero, offer card) | `nano_banana_pro` | — |
| Volume B-roll with a person, no readable wordmark | `nano_banana_2` | volume |
| Anatomy (EG05) | `nano_banana_2`, ANAT-A / ANAT-B | §12A, Product Sheet §17 |
| Video | Kling 3.0 (`kling-video-v3_0_omni`), start image required, `prefer_multi_shots: false`; Kie `kling-3.0` when Kling is short | §4, §5, §27G |
| Voice | §22U: two Kling source takes of N → ElevenLabs clone by API → Enhance → Eleven v4, **both hooks and both bodies in one request**, split at the silences; VO trimmed in the house cut (`vo_trim.py`) | §22U, E11A |
| Talking heads | **none** (voice-only, as the reference) | Style Lock |

**Other locks:** format **Short VSL, narrated B-roll, voice-only** · **side: right knee** (no knee named → `SIDE_RULE`) · mechanism claim: **protection** (Product Sheet §6) · edit: `EDIT-STRYDE-TB` · hooks: 2 → **2 videos, each hook with its own body** (§30H; `variants.py` builds each pair).

---

## 3. Cast (step 3): generated, on the board for your check

**Casting to the Product Sheet (British, 55–80, balanced men/women) and the script's instruction (about half Black):** four recurring wearers carry the B-roll across both videos, two Black and two white, two women and two men. **N, the narrator, is never on screen**: her sheet exists only to make the two Kling clips her voice is cloned from (§22U). One-offs (the surgeon on B2-10, hands, extras) come at steps 4–5, balanced to keep about half Black.

| Sheet | Who | Job ID | File | Board |
|---|---|---|---|---|
| N-NARR | the narrator (voice only) | `208200f7-8adc-4cc8-99fa-4e3a60772df4` | `cast/N-NARR_v1.png` | To check |
| R1-GRACE | wearer · walks, stairs | `d74aa805-e134-4a6c-b8ed-65d690299805` | `cast/R1-GRACE_v1.png` | To check |
| R2-ALAN | wearer · garden, trousers over it | `29295252-0141-4402-af1f-28ce67a2dcf2` | `cast/R2-ALAN_v1.png` | To check |
| R3-KOFI | wearer · still working, on his feet | `6411f6af-38fd-440f-8849-a99023f8cfc3` | `cast/R3-KOFI_v1.png` | To check |
| R4-FIONA | wearer · her stairs, the close | `6757bb36-e953-4b36-84c3-23bf20d39d9f` | `cast/R4-FIONA_v1.png` | To check |

Manual run: **I don't check the sheets** (§18B step 3). Confirm or Fix each on the board. Prompts: `cast/<ID>.prompt.txt`, assembled from Appendix A by ID in `cast/build_sheets.py` (`CAM-LOCK` → `AVATAR-SHEET` + `SHEET-GRID` → `SKIN-T` → `CAP-SHARP` → `CAP-FILE` → `NEG-SHEET` + `NEG-GRID` + `NEG-FILE` + `NEG-DEFAULT-FACE`), 9,145–9,255 chars each. Spend: 5 Sunburst jobs, one render each. Higgsfield 17,527 credits before the cast.

### Identity strings (from the prompts; read off the renders once you confirm them, §7)

| ID | Identity string |
|---|---|
| N | white British woman, 57, tall and narrow, slightly stooped; long narrow face, high flat cheekbones, hooded grey-green eyes, slightly hooked nose, thin mouth turned down at the corners; small white scar breaking the outer end of the right eyebrow; silver-ash blunt chin-length bob with a straight fringe; charcoal merino V-neck over a white T-shirt, black trousers, black loafers |
| R1 | Black British woman (Nigerian heritage), 62, tall and full-figured; round face, wide cheekbones, large dark brown eyes, broad short nose, full lips; gap between her front teeth; short coiled hair, mostly grey; mustard chunky cardigan over a black top, stone shorts above the knee, white leather trainers |
| R2 | white British man, 72, short and wiry, slight bow legs; long thin face, sunken cheeks, close-set pale blue eyes, large nose crooked to the left, large ears; bald with a white fringe; faded red-and-green checked flannel shirt, khaki shorts above the knee, brown walking shoes, grey socks |
| R3 | Black British man (Ghanaian heritage), 58, stocky, barrel-chested; broad square face, heavy brow, deep-set eyes, wide flat nose; notch through the left eyebrow; shaved head, short grey goatee; heather-grey zip hoodie over navy T-shirt, navy work shorts above the knee, black work boots |
| R4 | white British woman (Scottish heritage), 66, tall, strong-shouldered; wide oval face, strong jaw, light hazel eyes, freckles; small pale scar on the point of the chin; shoulder-length curly faded copper-red hair going grey at the temples; teal fleece zip-neck over white T-shirt, navy shorts above the knee, grey trail trainers |

### §19A axis tables

| Axis | N | R1 | R2 | R3 | R4 |
|---|---|---|---|---|---|
| Face | long, narrow, flat cheekbones | round, full | long, thin, sunken | broad, square, heavy brow | wide oval, strong jaw |
| Hair | silver bob + fringe | short grey coils | bald, white fringe | shaved + grey goatee | curly copper-grey |
| Age | 57 | 62 | 72 | 58 | 66 |
| Build | tall, narrow | tall, full-figured | short, wiry | medium, stocky | tall, strong |
| Wardrobe | charcoal knit | mustard cardigan | checked flannel | grey hoodie, workwear | teal fleece |
| Marker | eyebrow scar | tooth gap | crooked nose | eyebrow notch | chin scar |
| Voice | British (below) | non-speaking | non-speaking | non-speaking | non-speaking |
| Environment | — (voice only) | park, her hall and stairs | his garden, home | his workplace | her stairs, a coastal path |

**Clearance within the build:** every pair differs on ≥ 7 axes. **Against the roster** (`stryde-what-changed` H, R1 Maureen, R2 Desmond; `stryde-three-regrets` N, Gail, Ken, Joan; `stryde-lost-moments`): every new face differs on ≥ 6 axes; no marker repeats (R2 Desmond's nose scar ≠ R2 Alan's crooked nose). ✓

### Narrator: `VOICE-NARR` (§22D) and §20 constraint sheet

**`VOICE-NARR`** (goes verbatim into both §22U step-2 takes)
```
A British woman of fifty-seven from the north of England, now living in the south, a low-mid, slightly dry voice with a steady warmth, plain and matter-of-fact, as if setting a friend straight over a cup of tea. Soft northern vowels worn smooth, never RP, never a caricature, never American. Short sentences land flat and sure; the numbers slightly slower, never louder. Brisk and even, about one hundred and seventy-five words a minute.
```

| Field | N — narrator |
|---|---|
| Accent | northern English worn smooth; never RP, never American |
| Pacing | ~175 wpm (reference 180) |
| On camera | never (voice-only build); the sheet is only for the two Kling source clips |
| Audio proximity | close, dry, studio-quiet |
| Stress register | the objection lines ("Too small to work?", "Fair enough.") dry, almost amused; "A mechanism." and "A scalpel, not a sledgehammer." slower and lower, never bigger |
| Non-speech events | one short in-breath before a number; nothing else |
| Voice name (§22U step 7) | `TooBad-Narrator` (proposed) |

---

## Flags (decisions for the user: nothing below was changed silently)

| # | Where | Finding | Recommendation |
|---|---|---|---|
| F1 | Product Sheet | The Drive copy is V7.49.29; the repo has V7.49.37 | Using V7.49.37 |
| **F2** | Voice | "Different Voice": the reference is a man; I cast a **British woman** narrator | Say "male narrator" if you meant a different man's voice |
| F3 | Format | Two hooks, **each with its own body** (not one shared body) | 2 finished videos; both hooks and both bodies voiced in one TTS request so the voice matches |
| **F4** | B1-01/02/04/06, B2-01 | "They're small on purpose", "A big brace wraps the whole knee and misses it", "A scalpel, not a sledgehammer", "what sleeves and braces never could": comparative claims, not in the register | Voiced as written; the brace/sleeve shown unbranded, never a named brand. Please confirm the advertiser holds them |
| **F5** | B1-03 | "two centimetres below your kneecap": a placement figure (Tier 3; the register says "just below") | Voiced as written; never shown as a measurement on screen. Please confirm |
| F6 | B1-05, B2-04 | "redirects the load away from the worn spot": load-path wording; the Product Sheet's claim is **protection** | Voiced as written; pictured as protection (the strap takes the load off the spot) |
| **F7** | B1-09/10, B2-09 | "sit flat under your trousers", "light enough you forget it's there", "No slipping. No sores. No rolling down.": not in the register | Voiced as written; shown as trousers over the strap (§9D) and wearers moving. Please confirm |
| **F8** | B2-05 | "In a sports medicine study, the strain was cut by thirty-four percent": the register holds "sports scientists measured 34% less strain" — "a study" is a stronger wording | Voiced as written; 34% as a post overlay. Please confirm a study backs it |
| **F9** | B2-11 | "Not the knock-offs on Amazon": a named marketplace (§10A) | Voiced as written (verbatim rule); **never shown** — no listing, logo or screenshot; the copy shown per Product Sheet §7. §10A asks for a generic alternative ("the knock-offs online"); it's the advertiser's call. Please confirm |
| F10 | B2-08 | "Adjustable" (Product Sheet §12) | Shown as the fit (the seating beat), never adjusting; the word never enters a prompt |
| F11 | B2-08 | "silicone pad" | Prompts say "the pad" (it renders the soft fake otherwise); shown by `PAD_BACK_SHOT` |
| F12 | B2-10 | "Recommended by orthopaedic surgeons" | A surgeon one-off per §19B at step 4–5 |
| F13 | Casting | "Include +/- 50% of Black People on the B-Rolls" | Applied: recurring cast 2 of 4 Black; one-offs balanced; checked per video on the act map |
| F14 | EG06 | The reference cuts every ~1.6s; the house rule (V7.65.0) holds every B-roll ~3.0s, never under 2.0s | House rule wins: ~16–18 B-rolls per video instead of 33 |
| F15 | Script file | Named "Untitled document"; header note and hook names read as spoken | Handled (see step 2) |

## Next — on your go (§18B step 5)

Confirm or Fix each avatar on the board and answer the bold flags (F2, F4, F5, F7, F8, F9). Then steps 4–5 as one delivery: locations (R1's park and hall stairs, R2's garden, R3's workplace, R4's stairs and a coastal path, a clinic for the surgeon) as 16:9 plates, the act map and wardrobe map for both videos with every row's angle, focus, light and layout (`angles.py` passing); then the voice straight through (two Kling source clips of N → clone → VO takes on the board → house-cut trim).
