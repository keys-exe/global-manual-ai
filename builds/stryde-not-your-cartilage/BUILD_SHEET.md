# Build Sheet — stryde-not-your-cartilage

**STRYDE Precision Strap · "A - VID | Short VSL | TOF | Rediagnosis | New | Not Your Cartilage"** · Standards V7.69.1 · **RUN: MANUAL** · 2026-09-29

Steps 1–3 of §18. **Stopped at the avatar review (§18B, V7.62.0)**: steps 4–5 wait for the user's go.
Boards: Current https://claude.ai/artifact/DUsxw9aB6Q4PE7uTa9FFLE · Old https://claude.ai/artifact/7qQDVB81c5s5JtejBqJZw1 · Final https://claude.ai/artifact/7bejwknnCQGFtV6AUN3Nxc · Plan https://claude.ai/artifact/7ntxnK1H2VmA62SndFADqW

---

## 0. Intake (§18B)

| Input | Found | Notes |
|---|---|---|
| Drive folder | `13oUXl866Cxjts6mSxCZJAGcCsxeoxein` | fetched with `fetch_drive.py` → `intake/`; matches no existing build → new build |
| Inspo | `MY INSPO VIDEO.mp4` → `intake/inspo.mp4`; the same file is in `facebook-ad-creatives.zip` (byte-identical) with its Ad Library record (Meta 1620934502990537, "Buy 1 Get 1 FREE", getstryde.co) | 51.96s · 9:16 · 720×1280 · 30fps · audio. **The same STRYDE "Too bad you have never worn these" ad `stryde-too-bad` used** |
| Script | `Untitled document.docx` (the only document) → `intake/script.docx` | title line 1 ✓ · **3 hooks (A, B, C), one shared body** ("BODY: same for all three") |
| Product Sheet | `stryde_product_sheet_V7.49.32.py`: **older than the repo's V7.49.38** | the repo's V7.49.38 is used (`products/stryde/`) |
| Product images | 10 (front, back, side, ¾ left/right, macro, package open, worn front/rear/bent) | layer 1 |
| Missing | nothing required | — |

**Message fields read:** `Run manual` → **RUN: MANUAL**. `British` → **VOICE: British** (the narrator). `MODE` blank → **Mode 1** (realistic reference, §2). `HOOKS` blank → **3 in the script → 3 finished videos** (HK1/HK2/HK3 + the same BODY). `CAP` blank → E0 Higgsfield default. `BUILD` blank → `stryde-not-your-cartilage`, from the title. No Loom.

**Script header note, applied as `ADJUST` lines (layer 5):** "Different Voice (keep British Accent on Eleven Labs) Brolls and editing than the original. Include +\- 50% of Black People on the B-Rolls + Music."
- **A different voice**: the reference narrator is a man (median pitch 132 Hz); ours is a **British woman** (N, below), cloned by §22U, voiced in Eleven v4. (F2)
- **Different B-roll and editing**: new cast, new locations, new shots; `EDIT-STRYDE-NYC` keeps the reference's type of edit, never its shots.
- **About half the B-roll people Black**: recurring cast 2 of 4 Black (R1, R3); one-offs cast to hold ~50% (checked at step 5 on the act map).
- **Music**: a music bed in the CapCut block (VN-H1).

---

## 1. Absorption Sheet (§42)

### Part 1 — measured

| Instrument | Reading | Settles |
|---|---|---|
| Duration / aspect / res | 51.96s · 9:16 · 720×1280 · 30fps | 9:16 locked |
| Scene cuts | **33 shots, mean 1.57s** (`fetch_inspo.py`; frames in `intake/frames/MY INSPO VIDEO/`) | a cut every ~1.6s |
| Silence (−30/−40 dB) | only the tail, 50.3–51.9s (black end frames) | wall-to-wall voice |
| Transcript (faster-whisper small) | 150 words over 50.2s of voice = **~180 wpm**, one male voice (median pitch 132 Hz) (`work/inspo_transcript.txt`) | brisk, even |
| On camera | **no talking heads**: narration over B-roll the whole way | voice-only build |
| Frames + per-second sheets | `intake/frames/MY INSPO VIDEO/sheet_01.jpg`, `sheet_02.jpg` | Edit Grammar below |

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
- **Realistic iPhone-register B-roll** (§22) of 60–75s wearing the strap in ordinary British places: home, stairs, a chair, a long walk, a street, a clinic.
- **Anatomy as glowing 3D X-ray renders** on every "why" line: red/orange on the pain, electric blue when the strap works (§11, §12A) — the Product Sheet's ANAT-A / ANAT-B looks.
- **One comparison card** early (the strap vs a brace), and **a dark offer card** with two straps at the end.
- Captions all the way through; hard cuts only.

### Part 3A — Edit Grammar (`EDIT-STRYDE-NYC`)

| ID | Device (reference) | Where | Our build |
|---|---|---|---|
| EG01 | **Captions**: 2–5 words at a time, black text in a white rounded box, centred at ~66% height | whole ad | kept (CapCut line) |
| EG02 | **Full-screen B-roll**, no talking head, no PiP | whole ad | kept (house default) |
| EG03 | **Split card**: top half STRYDE (label bar), bottom half BRACES | "to do what sleeves and braces never could" (5.6–8.0s) | kept as our one `split` B-roll per video (≤ 1 in 5 boxed ✓), on the same line in our body (B-01) |
| EG04 | **Text overlays**: "17X" + red arrow; "BUY 1 GET 1 FREE" + URL on a dark end card with two straps | 12.6s, 44–46s | "17X" not used (our script has no number there); the offer card kept (CapCut lines; text never generated, §17) |
| EG05 | **CGI anatomy**, X-ray blue with red pain glow; strap glowing blue on relief | 5–21s | kept, in the Product Sheet's looks (ANAT-B ghost limb on cartilage / bone on bone; ANAT-A full stack on the tendon and the strain coming off it) |
| EG06 | **Cut rhythm**: a hard cut every ~1.6s, no transitions, no speed ramps | whole ad | hard cuts kept; **rhythm overridden by the house hold (V7.65.0): every B-roll holds ~3.0s, never under 2.0s** (F14) |
| EG07 | Music bed | not measurable under the voice | **added** — the script asks for it (VN-H1); a light bed under the VO, ducked, in CapCut |
| EG08 | SFX | none heard | none |

### Part 4 — script absorption

**Copy formula (reference → ours):** "too bad…" hook → surgeon credibility → sleeves and braces → conditions → 17× through one spot → strap moves the load → outcomes → features → proof → offer → close. **Ours is a rediagnosis**: the hook says the pain isn't decided by the cartilage; the body names the reader's situation (bone on bone, a new knee on the table), the three daily moments that hurt, says plainly the strap doesn't repair cartilage, then gives the real cause (strain on the tendon below the kneecap) and the relief, then features, proof, offer, close.

| Part | Words | ≈ at 175 wpm |
|---|---|---|
| HK1 (A) | 11 | 3.8s |
| HK2 (B) | 11 | 3.8s |
| HK3 (C) | 13 | 4.5s |
| BODY (shared) | 150 | 51.4s |
| **Each finished video** | 161 / 161 / 163 | **≈ 55–56s** (reference 52s) |

Pace gate: ≤ 210 wpm (§22U); target ~175 wpm (the reference's 180, a touch slower for a 60–75 audience).

### Part 5 — surfaced, not absorbed

| Reference element | Disposition |
|---|---|
| The reference's people, rooms and shots | not copied (the script asks for different B-roll); new cast §19A, new locations at step 4 |
| The male voice | replaced by a British woman (the script asks for a different voice) |
| The `stryde-too-bad` cast and narrator (same inspo) | not reused: new faces, new narrator voice, so the two ads never look like one |
| "17X" overlay, "life-changing" | not in our script |
| Clinician's gloved hands seating the strap | not copied; seating shown by the wearer (`SEAT_LOCK`), a clinician appears only on the surgeon line (§19B) |

### Part 6 — beat-it plan

| Reference weakness | Our delta | Where |
|---|---|---|
| Cuts every 1.6s: shots flash past before the eye finds the strap | ~3s holds, the strap readable in every worn shot | whole body |
| The hook shows a clinic, not an idea | each hook shows the rediagnosis: the worn cartilage in the X-ray look, then the same knee on a good day, strap on (step 6 proposes each) | HK1–HK3 |
| "Every time, the pain" lists three moments the reference never shows | three short real moments: the long walk (R2), the flight of stairs (R3), getting up from a chair (R1), each a wince | B-03 |
| Pain and relief only in CGI | the same three people doing the same three things again with the strap on, easy (payoff mirrors the problem) | B-07 |
| Mostly one register of person | cast balanced by the script's instruction: ~half Black, men and women, 60–75 | whole build |

### Part 7 — confirmation

Conflicts with the rules are listed in **Flags**. **Confirm or correct the absorption along with the avatars.**

---

## 2. Script, product, claims, locks (step 2)

Spoken lines, verbatim: `work/script_lines.txt` and per part `work/script_{HK1,HK2,HK3,BODY}.txt`. `script_lines.py` read the header note, "same for all three" and the quotation marks as spoken; they were removed by hand (labels, notes and quotation marks only — no spoken word touched).

### Visual Instruction Ledger (§27F), opened

| ID | Source | Instruction | Anchored | Carried by | Status |
|---|---|---|---|---|---|
| VN-H1 | script header | "Different Voice (keep British Accent on Eleven Labs) Brolls and editing than the original. Include +\- 50% of Black People on the B-Rolls + Music" | whole build | voice: N (British woman) · B-roll: new cast/locations, ~50% Black · edit: `EDIT-STRYDE-NYC` · music: CapCut bed | open → steps 4–8 |
| VN-H2 | script L12 | "BODY: same for all three" | BODY | one body voiced once, reused identically in every variant (`variants.py`) | open → step 8 |

No per-line visual notes in the script: every shot is the editor's call (Part 6).

### Phrase inventory (§27B): dispositions assigned at step 5

Variant n = HKn + BODY. The body is planned once and reused.

| ID | Phrase (short) | Job | Claim | Subject / register |
|---|---|---|---|---|
| HK1 | "It's not your cartilage that decides if your knee hurts today." | hook (rediagnosis) | **F5** | ANAT-B worn cartilage → the same knee on a good day, strap on |
| HK2 | "Your cartilage doesn't decide whether today is a bad knee day." | hook | **F5** | wearer at the bottom of the stairs, a bad day vs a good day |
| HK3 | "How much cartilage you've got left doesn't decide how much it hurts today." | hook | **F5** | ANAT-B thin cartilage → wearer walking easy |
| B-01 | Built over three years with orthopaedic surgeons, to do what sleeves and braces never could. | credibility | 3 yrs ✓ · **F4** | box opened by older hands → **split card** (EG03) |
| B-02 | Bone on bone, advanced arthritis, and they're already talking about a new knee. | conditions | ✓ · **F9** | ANAT-B ghost limb → a wearer across a desk from a consultant, X-ray lightbox (no numerals) |
| B-03 | A long walk. A flight of stairs. Getting up out of a chair. Every time, the pain. | problem | — | R2 on a path, R3 on stairs, R1 rising from a chair — each a wince |
| B-04 | This strap doesn't repair your cartilage. | honesty | ✓ | strap close hold, wordmark; ANAT-B cartilage stays worn |
| B-05 | It takes the strain off the tendon below your kneecap. | mechanism | protection ✓ | ANAT-A red on the tendon → strap seated, glow turns blue |
| B-06 | And that's why it works even on knees they've written off. | claim | **F6** | wearer's face easing as they straighten the leg |
| B-07 | You walk again. You come down your own stairs again. | outcome | — | R2 walking on, R1 coming down her stairs, strap on |
| B-08 | Surgery is no longer the only thing you've got left. | claim | **F6** | R3 at home, easy, putting the kettle on — never a hospital |
| B-09 | Adjustable, breathable, with a silicone pad that locks the pressure right where you need it. | features | pad ✓ · **F10, F11** | seating beat (`SEAT_LOCK`) → `PAD_BACK_SHOT` |
| B-10 | No slipping. No sores. No rolling down. | features | **F7** | R4 moving, strap stays put |
| B-11 | It stays put under your trousers. Light enough you forget it's there. | features | **F7** | trousers over the strap (§9D); R4 going about her day |
| B-12 | Recommended by orthopaedic surgeons for lasting relief. | proof | ✓ · **F8** | surgeon one-off (§19B) with a wearer |
| B-13 | Buy one, get one free today at getstryde.co. Sixty-day money-back guarantee. | offer | ✓ | two straps in the box → dark offer card |
| B-14 | Nothing to lose but the pain. | close | — | a wearer walking off, strap on |

Coverage: 3 hooks + 14 body phrases · **uncovered 0 · blocked 0** (dispositions at step 5).

### Claims (§43A)

Held in the Product Sheet register (V7.49.38): three years with orthopaedic surgeons · silicone pad (prompts say "the pad") · bone on bone / arthritis / worn cartilage · recommended by orthopaedic surgeons · Buy 1 Get 1 Free · 60-day money-back guarantee. The mechanism line ("takes the strain off the tendon below your kneecap") matches the build's claim, **protection**. **Not in the register:** F4–F9 (Flags). Voiced verbatim in every case (§22U): **a line is flagged, never rewritten.**

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
| Voice | §22U: two Kling source takes of N → ElevenLabs clone by API → Enhance → Eleven v4, **all three hooks and the body in one request**, split at the silences; VO trimmed in the house cut (`vo_trim.py`) | §22U, E11A |
| Talking heads | **none** (voice-only, as the reference) | Style Lock |

**Other locks:** format **Short VSL, narrated B-roll, voice-only** · **side: right knee** (no knee named → `SIDE_RULE`) · mechanism claim: **protection** (Product Sheet §6) · edit: `EDIT-STRYDE-NYC` · hooks: 3 → **3 videos, each hook + the same body** (§30H; `variants.py`).

---

## 3. Cast (step 3): generated, on the board for your check

**Casting to the Product Sheet (British, 55–80, balanced men/women) and the script's instruction (about half Black):** four recurring wearers carry the B-roll across all three videos, two Black (R1 Folake, R3 Hassan) and two white, two women and two men — each one of the script's moments: R1 getting up out of a chair, R2 the long walk, R3 the flight of stairs, R4 the features (trousers, moving about). **N, the narrator, is never on screen**: her sheet exists only to make the two Kling clips her voice is cloned from (§22U). One-offs (the consultant on B-02, the surgeon on B-12, hands) come at steps 4–5, balanced to keep about half Black.

| Sheet | Who | Job ID | File | Board |
|---|---|---|---|---|
| N-NARR | the narrator (voice only) | `95fe41b6-c20a-430e-8473-f955985b51b1` | `cast/N-NARR_v1.jpg` | To check |
| R1-FOLAKE | wearer · the chair, her stairs | `f8fb4e3a-229b-4815-9612-755cebed357b` | `cast/R1-FOLAKE_v1.jpg` | To check |
| R2-DEREK | wearer · the long walk | `8759c885-5260-48b6-9510-9c47e39e0e31` | `cast/R2-DEREK_v1.jpg` | To check |
| R3-HASSAN | wearer · the flight of stairs, surgery line | `776436a1-344a-4c8a-b4f6-b4db75f8d516` | `cast/R3-HASSAN_v1.jpg` | To check |
| R4-ELAINE | wearer · features, under trousers | `88e67893-8e4f-4f02-9ec2-da328257aece` | `cast/R4-ELAINE_v1.jpg` | To check |

Manual run: **I don't check the sheets** (§18B step 3). Confirm or Fix each on the board. Prompts: `cast/<ID>.prompt.txt`, assembled from Appendix A by ID in `cast/build_sheets.py` (`CAM-LOCK` → `AVATAR-SHEET` + `SHEET-GRID` → `SKIN-T` → `CAP-SHARP` → `CAP-FILE` → `NEG-SHEET` + `NEG-GRID` + `NEG-FILE` + `NEG-DEFAULT-FACE`), 9,253–9,397 chars each. Spend: 7 Sunburst jobs, one render each (Higgsfield 17,384 credits before the cast). Full renders are on the board (1520×2688 PNG); the repo keeps JPEG copies.

**Withdrawn before your review (my catch, §19A):** the first R1 (Patrice, Jamaican heritage, long oval face, tall and full-figured) and R3 (Kwame, Ghanaian heritage, round face, stocky) were too close to R1 Patricia and R3 Emmanuel in `stryde-failed-alternatives` (same heritage, face shape and build). Both were recast (R1 Folake, R3 Hassan, one render each); the first renders sit on the Old board (`cast/withdrawn/`). R2 was renamed Derek (the render is unchanged) so no slot name repeats that build's R2 Gordon.

### Identity strings (from the prompts; read off the renders once you confirm them, §7)

| ID | Identity string |
|---|---|
| N | white British woman from the West Midlands, 61, short and solid; round soft face, full cheeks dropping at the jaw, deep-set dark brown eyes under low heavy brows, short upturned nose, small full mouth; short pale scar across the tip of her nose; dark brown hair threaded with grey in a low loose bun; mustard cardigan over a navy-and-white Breton top, indigo jeans, brown suede ankle boots |
| R1 | Black British woman of Nigerian heritage, 66, medium height, slim and wiry, long neck; wide face, very high prominent cheekbones tapering to a narrow pointed chin, narrow deep-set dark eyes, broad flat nose, wide mouth with a full lower lip; small keloid bump on the top rim of her right ear; long thin grey-and-black box braids in a low ponytail; plum long-sleeved top, grey knitted waistcoat, mid-grey shorts above the knee, black slip-on shoes |
| R2 | white British man from the north-east, 74, big-framed, heavy chest, round belly; broad square face, heavy-lidded pale grey eyes, bushy white brows, wide flattened nose, short clipped white beard; top joint of his left index finger missing; thick wavy white hair combed back; bottle-green quilted gilet over grey marl sweatshirt, stone shorts above the knee, black trail shoes, grey socks |
| R3 | Black British man of Sudanese heritage, very dark skin, 72, very tall and thin, slight stoop; long face, heavy square jaw, hollow cheeks, prominent forehead, deep-set eyes under a heavy brow ridge, long nose broad at the tip, thin lips, clean-shaven with grey stubble; thin pale scar along his right jawline; short rounded grey afro, thinning at the crown; sky-blue short-sleeved shirt tucked into navy chino shorts above the knee, brown lace-ups, dark socks |
| R4 | white British woman of Welsh heritage, 63, petite and slim; narrow heart-shaped face, pointed chin, wide-set bright blue eyes, long thin nose with a slight bump, thin lips; cluster of three small pale moles under her left eye; ash-grey blonde pixie cut; rust-orange zip jacket over cream T-shirt, black shorts above the knee, white-and-grey running trainers |

### §19A axis tables

| Axis | N | R1 | R2 | R3 | R4 |
|---|---|---|---|---|---|
| Face | round, soft, full cheeks | wide, high cheekbones, narrow chin | broad square | long, heavy square jaw, hollow cheeks | narrow heart, pointed chin |
| Hair | dark-grey low bun | grey-black box braids, low ponytail | thick wavy white, combed back + white beard | short grey afro, clean-shaven | ash-blonde pixie |
| Age | 61 | 66 | 74 | 72 | 63 |
| Build | short, solid | medium, slim and wiry | big-framed, heavy | very tall, thin, stooped | petite, slim |
| Wardrobe | mustard cardigan, Breton | plum top, grey waistcoat | green gilet, grey marl | sky-blue shirt | rust-orange jacket |
| Marker | scar on nose tip | keloid on right ear rim | missing fingertip (left index) | jawline scar | three moles under left eye |
| Voice | British (below) | non-speaking | non-speaking | non-speaking | non-speaking |
| Environment | — (voice only) | her armchair, her stairs | a long walk (path, park) | his stairs, his kitchen | her day, trousers over it |

**Clearance within the build:** every pair differs on ≥ 6 axes. **Against the roster** (`stryde-too-bad` N, Denise, Alan, Clive, Fiona; `stryde-what-changed`; `stryde-three-regrets`; `stryde-lost-moments`; `stryde-failed-alternatives`): every new face differs on ≥ 6 axes; no marker repeats; no slot name repeats (the roster's markers were checked: no nose-tip scar, ear keloid, missing fingertip, jawline scar or mole cluster in use). ✓

### Narrator: `VOICE-NARR` (§22D) and §20 constraint sheet

**`VOICE-NARR`** (goes verbatim into both §22U step-2 takes)
```
A British woman of sixty-one from the West Midlands, now living in the south, a warm mid-low voice with a little gravel in it, unhurried, kind but no-nonsense, as if telling a neighbour over the garden fence what finally worked. Midlands vowels softened by the years, never RP, never a caricature, never American. Short sentences land plainly; the lists even and steady, never salesy. About one hundred and seventy-five words a minute.
```

| Field | N — narrator |
|---|---|
| Accent | West Midlands softened; never RP, never American |
| Pacing | ~175 wpm (reference 180) |
| On camera | never (voice-only build); the sheet is only for the two Kling source clips |
| Audio proximity | close, dry, studio-quiet |
| Stress register | the hooks level and certain, a quiet correction, never a shout; "This strap doesn't repair your cartilage." plain and honest; "Every time, the pain." slower and lower |
| Non-speech events | one short in-breath before the three-moment list; nothing else |
| Voice name (§22U step 7) | `NotYourCartilage-Narrator` (proposed) |

---

## Flags (decisions for the user: nothing below was changed silently)

| # | Where | Finding | Recommendation |
|---|---|---|---|
| F1 | Product Sheet | The Drive copy is V7.49.32; the repo has V7.49.38 | Using V7.49.38 |
| **F2** | Voice | "Different Voice": the reference is a man; I cast a **British woman** narrator, a different woman from `stryde-too-bad`'s | Say "male narrator" if you meant a different man's voice |
| F3 | Format | Three hooks, **one shared body** | 3 finished videos; all hooks and the body voiced in one TTS request so the voice matches |
| F4 | B-01 | "to do what sleeves and braces never could": a comparative claim, not in the register | Voiced as written; the brace/sleeve shown unbranded. Please confirm the advertiser holds it |
| **F5** | HK1–HK3 | "It's not your cartilage that decides if your knee hurts today" (and B, C): a statement about what causes knee pain, not in the register | Voiced as written; shown as the rediagnosis, never as a medical chart. Please confirm |
| **F6** | B-06, B-08 | "it works even on knees they've written off" / "Surgery is no longer the only thing you've got left": a strong efficacy claim that sets the strap against knee replacement; not in the register, and the kind of health claim ad platforms review closely | Voiced as written; pictured as everyday relief at home, never a hospital, an operation avoided or a scar. **Please confirm the advertiser holds these** |
| **F7** | B-10, B-11 | "No slipping. No sores. No rolling down. It stays put under your trousers. Light enough you forget it's there.": not in the register | Voiced as written; shown as trousers over the strap (§9D) and wearers moving. Please confirm |
| F8 | B-12 | "for lasting relief": the register holds "recommended by orthopaedic surgeons", not "lasting relief" | Voiced as written. Please confirm |
| F9 | B-02 | "advanced arthritis": the register says "arthritis" | Voiced as written; shown with the ANAT-B look, no grade or stage on screen |
| F10 | B-09 | "Adjustable" (Product Sheet: one size fits all, §12) | Shown as the fit (the seating beat), never adjusting; the word never enters a prompt |
| F11 | B-09 | "silicone pad" | Prompts say "the pad" (it renders the soft fake otherwise); shown by `PAD_BACK_SHOT` |
| F12 | B-02, B-12 | "they're already talking about a new knee", "Recommended by orthopaedic surgeons" | A consultant and a surgeon one-off per §19B at steps 4–5, one of them Black to hold the ~50% |
| F13 | Casting | "Include +\- 50% of Black People on the B-Rolls" | Applied: recurring cast 2 of 4 Black; one-offs balanced; checked per video on the act map |
| F14 | EG06 | The reference cuts every ~1.6s; the house rule (V7.65.0) holds every B-roll ~3.0s, never under 2.0s | House rule wins: ~17–19 B-rolls per video instead of 33 |
| F15 | Script file | Named "Untitled document"; the header note and "same for all three" read as spoken | Handled (see step 2) |

## Next — on your go (§18B step 5)

Confirm or Fix each avatar on the board and answer the bold flags (F2, F5, F6, F7). Then steps 4–5 as one delivery: locations (R1's living room + stairs, R2's walk, R3's stairs + kitchen, R4's day, a consulting room for the consultant/surgeon) as 16:9 plates, the act map and wardrobe map for all three videos with every row's angle, focus, light and layout (`angles.py` passing); then the voice straight through (two Kling source clips of N → clone → VO takes on the board → house-cut trim).
