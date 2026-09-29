# Build Sheet — stryde-what-changed

**STRYDE Precision Strap · "C - VID | Podcast | TOF | Why Now | New | What Changed"** · Standards V7.68.2 · **RUN: MANUAL** · 2026-09-29

Steps 1–3 of §18. **Stopped at the avatar review (§18B, V7.62.0)**: steps 4–5 wait for the user's go.
Boards: Current https://claude.ai/artifact/3uy6935ZTAivEZgysENYvq · Old https://claude.ai/artifact/T3RZo3ak1QfC2ue6yaV9LD · Final https://claude.ai/artifact/6aiYxibqFq5F9R8tMiqp2z · Plan https://claude.ai/artifact/SGxFerhs4WKGiy3uV5bh8R

---

## 0. Intake (§18B)

| Input | Found | Notes |
|---|---|---|
| Drive folder | `1zFGMzZ-olam9tpD63hM5MvHlUMkUVHKW` | fetched with `fetch_drive.py` → `intake/`; matches no existing build → new build |
| Inspo | `inspo video - Podcast why now what changed.mp4`: a UK podcast-style ad (female host on a sofa with a podcast mic; hip pain / menopause / collagen product) | 195.5s, 9:16, 720×1280, 29.97fps, audio |
| Script | `Script - C - VID \| Podcast \| TOF \| Why Now \| New \| What Changed` (Word 2007+ file with no extension; `fetch_drive.py` couldn't sort it) → copied to `intake/script.docx`, text in `intake/script.txt` | title line 1 ✓ · Meta Ad Library ref ID 1964659840908449 · **3 hooks (A, B, C) + one shared body** |
| Product Sheet | `stryde_product_sheet_V7.49.29.py`: **older than the repo's V7.49.37** | the repo's V7.49.37 is used (`products/stryde/`); the Drive copy isn't imported |
| Product images | 10 (front, back, side, ¾ left/right, macro, package open, worn front/rear/bent) | layer 1 |
| Missing | `package_closed.jpg`, `inner_face.jpg` in the folder (the repo has `inner_face.jpg`) | none blocks steps 1–3 |

**Message fields read:** `RUN MANUAL` → **RUN: MANUAL**. `BRITISH` → **VOICE: British** (the host's voice, below). `MODE` blank → **Mode 1** (the reference is realistic, §18A). `HOOKS` blank → **3 in the script → 3 finished videos** (HK1 + BODY, HK2 + BODY, HK3 + BODY; one body, §30H). `CAP` blank → E0 Higgsfield default. No Loom.

---

## 1. Absorption Sheet (§42)

### Part 1 — measured

| Instrument | Reading | Settles |
|---|---|---|
| Duration / aspect / res | 195.5s · 9:16 · 720×1280 · 29.97fps | 9:16 locked |
| Scene cuts | **115 shots, mean 1.70s** (`work/inspo_measure.json`) | a cut every ~1.7s |
| Silence (−30/−40 dB) | none except the tail (195.1–195.4s) | wall-to-wall voice |
| Volume | mean −18.0 dB, max 0.0 dB | — |
| Transcript (faster-whisper small) | 573 words / 195.5s = **176 wpm**, one female British voice, the host (`work/inspo_transcript.txt`) | brisk, conversational |
| On camera | one host throughout; **about 55% of the shots are her on camera**, the rest B-roll, most of it with her cut-out in the corner (EG02) | talking-head build |
| Frames + per-second sheets | `intake/frames/inspo video - Podcast why now what changed/` | Edit Grammar below |

### Part 2 — structure map

| t | Job | What the reference shows | Layout |
|---|---|---|---|
| 0.0–3.1 | **hook, line 1 in voice-over** ("Your hips have been preparing for pregnancy for 30 years.") | full-screen B-roll: hips with a glowing highlight, a woman's hip on a gym bench | full, no host |
| 3.1–6.1 | hook, line 2 **on camera** ("Here's what happens when menopause suddenly shuts it all down.") | host on the sofa, first appearance | talking head |
| 6.1–66.5 | mechanism: what the body did for 30 years, then what stopped | host ↔ CGI anatomy (bones, muscles), CGI abstracts (bubbles, cells, DNA), lifestyle shots | TH + cut-out B-roll |
| 67–94 | "catches people out": it happens whether or not you had children; not gradual | host, B-roll of people | TH + cut-out |
| 95–106 | **the costly mistake**: painkillers, injections, surgery don't address it | IV drip, syringe, operating theatre | cut-out |
| 106–128 | what the body needs → product ("That's exactly why we formulated…") | product in hands, kitchen, pouring | full + cut-out |
| 128–158 | result + testimonial ("rusty hinges", a customer from Bristol) | host; a woman on a sofa; clinic | TH + cut-out |
| 158–171 | **the choice**: keep masking, or support the cause | host, clinic, product | TH + cut-out |
| 171–188 | guarantee → CTA | host, product, drinking | TH + cut-out |
| 188–195 | close (callback to the opening) | host | TH |

### Part 3 — Style Lock (what we keep)

- **One presenter on a podcast set**, seated, speaking to the lens as if to a guest: sofa, podcast mic on a boom arm in the foreground, brick wall, window, a floor lamp. Two framings (wide seated, medium close-up), alternated as punch-ins.
- Plain, confiding register; a "why now / what changed" explanation, then the mistake, then the fix, then the choice.
- A cut every ~1.7s; talking head roughly half the running time.
- Hook = one line of voice-over over B-roll, then the host on camera for the second line (this is **VN01**, "the reference's construction").
- Realistic, iPhone register for the B-roll (§22); anatomy as clean 3D renders (§12A register).

### Part 3A — Edit Grammar (`EDIT-STRYDE-WC`)

| ID | Device (reference) | Where | Our build |
|---|---|---|---|
| EG01 | **Two talking-head framings**: wide seated (sofa, knees, mic) and a medium close-up, cut between as punch-ins every 2–4s | whole ad | kept: talking heads cut between two framings of the one HeyGen take (a 1.25× punch-in in the edit for the MCU, never a second generation) |
| EG02 | **Cut-out PiP**: the host's head and shoulders, cut out, pinned bottom-left (~⅓ width) over full-screen B-roll | most B-roll, ~60 shots | **limited by the house rule (V7.65.0): B-roll full screen by default; `pip` on at most 1 B-roll in 5, never two in a row, on lines where her face adds something** (flag F12) |
| EG03 | **Full-screen B-roll, no host** | the hook (0–3s) and a few product shots | default for our B-roll |
| EG04 | **Captions**: 1–3 words at a time, black text in a white rounded box, centred at ~57% height; a key word in white on a **red** box ("for 30 years", "it all down", "COSTLY mistake") | whole ad | kept (CapCut line; red box on the numbers and turn words: "seventeen times", "seventy million", "cannot work", "Stryde", "34%") |
| EG05 | **CGI anatomy + abstract CGI** (bones, muscles, cells, DNA, bubbles) | mechanism section | anatomy kept, in the Product Sheet's anatomy look (`ANATOMY_LOOK`, §12A); abstract CGI (DNA, bubbles) **not used**: nothing in our script is chemical |
| EG06 | Hard cuts only; no transitions, no speed ramps | whole ad | kept |
| EG07 | Music bed | — | not measurable (no gap in the voice long enough); **unverified**. Default: none, as the reference plays |

### Part 4 — script absorption

**Copy formula (reference → ours):** hidden number / "what changed" hook → what the body has quietly done for decades → why it shows up "overnight" → it isn't what you did → the costly mistake (what gets sold doesn't aim at the cause) → what it actually needs → product → proof → test it yourself → the honest caveat → the choice → offer → callback close. **Our script follows the reference's construction line for line**, with the patellar tendon and load in place of hips and hormones.

| Part | Words | ≈ at 170 wpm |
|---|---|---|
| HK1 — the hidden number | 25 | 9s |
| HK2 — the flattering fact | 49 | 17s |
| HK3 — the arithmetic | 37 | 13s |
| BODY (shared) | 623 | 3:40 |
| **Each finished video** | 648 / 672 / 660 | **≈ 3:49 / 3:57 / 3:53** |

Pace gate: ≤ 210 wpm (§22U); target ~170 wpm (the reference's 176, a touch slower for a 55–80 audience).

### Part 5 — surfaced, not absorbed

| Reference element | Disposition |
|---|---|
| The host's look (auburn curls, burgundy roll-neck) | not copied; our host is cast new (§19A) |
| Hormones, collagen, DNA/bubble CGI | not relevant to this product |
| Named customer testimonial ("a customer from Bristol") | not in our script; nothing invented |
| Operating theatre / syringe / IV shots | our script's "costly mistake" is products (sleeve, brace, gel, painkiller), shown as ordinary unbranded objects at home, never a clinic |

### Part 6 — beat-it plan

| Reference weakness | Our delta | Where |
|---|---|---|
| Cut-out PiP on almost every B-roll, which crowds the frame | full-screen B-roll by default, PiP only where her face adds something (≤ 1 in 5) | EG02 |
| Abstract CGI that shows nothing specific | every CGI shot shows the one spot (the tendon under the kneecap) | EG05 |
| The product arrives with no demonstration | the self-test on your own stairs is shown (one knee strapped, one bare, coming down forwards) | body |
| Three hooks that share nothing on screen | each hook opens on its own number or fact, voice-over over B-roll (VN01), then the host | HK1–HK3 |

### Part 7 — confirmation

Conflicts with the rules are listed in **Flags**. **Confirm or correct the absorption along with the avatars.**

---

## 2. Script, product, claims, locks (step 2)

Spoken lines, verbatim: `work/script_lines.txt` (34 lines, 742 words) and, per part, `work/script_HK1.txt`, `script_HK2.txt`, `script_HK3.txt`, `script_BODY.txt`. The labels "A — The hidden number" and "B — The flattering fact" were read as spoken lines by `script_lines.py` (their em dash). They were removed by hand (labels only, no spoken word touched), and so were the quotation marks around each hook.

### Visual Instruction Ledger (§27F), opened

| ID | Source | Instruction | Anchored | Carried by | Status |
|---|---|---|---|---|---|
| VN01 | script L3–5 | "Door · VO · (the reference's construction)" | HK1–HK3 | each hook's first sentence is voice-over over full-screen B-roll (EG03); the host comes on camera for the hook's last line, as the reference does at 3.1s | open → step 5 |

No other visual notes in the script. B-roll is planned from the lines at step 5.

### Phrase inventory (§27B): dispositions assigned at step 5

| ID | Phrase (short) | Job | Claim | Subject / register |
|---|---|---|---|---|
| HK1 | "Your knees have been taking seventeen times your bodyweight… Here is what changed." | hook | 17× held | VO over B-roll: R1 on her stairs → host |
| HK2 | "There is a band under your kneecap about as wide as your thumb… Not even the person who read your scan." | hook | **F2, F3** | VO over anatomy (ANAT, the tendon) → host |
| HK3 | "Five thousand steps a day. Forty years… Here is what happens when that spot stops being able to take it." | hook | F4 | VO over feet on a pavement / stairs → host |
| B01 | That band is the patellar tendon. It sits two centimetres below your kneecap… | anatomy | phrasing table ✓ | ANAT (tendon lit) |
| B02 | Put your finger there now and press. That is the one. | participation | — | R1's finger pressing below her kneecap |
| B03 | It is not a big thing… since you were a teenager. | anatomy | F2 | host / ANAT |
| B04 | Going up the stairs, your muscles lift you. Going down, nothing lifts you… | mechanism | **F5** | R2 on stairs, up then down |
| B05 | …a layer of cartilage… that layer thins… It happens to everybody. | anatomy | ordinary | ANAT (cartilage) |
| B06 | The load does not thin with it… The cushion gets thinner. The weight stays exactly the same. | mechanism | 17× held | ANAT, 17× overlay |
| B07 | That is why it feels like it arrived overnight… | explanation | — | host / R1 |
| B08 | You do not have to have done anything… Some… never run a mile… Others played sport for thirty years… | "not what you did" | — | R1 (never ran) / R2 (old football photos) |
| B09 | Which is why most of what gets sold for this cannot work. | turn | **F6** | host |
| B10 | A sleeve… A hinged brace… Gel… A painkiller… | the costly mistake | **F6** | four unbranded objects at home |
| B11 | None of them are aimed at the spot. | turn | — | host |
| B12 | What that band actually needs is for less of your weight to land on it. | need | — | ANAT |
| B13 | That is what this does. It is called Stryde. | reveal | — | product hero (wordmark) |
| B14 | It sits two centimetres below the kneecap… A silicone pad inside… Your weight gets caught and moved off the worn part… | product mechanism | pad held · **F7** (load-path wording) | seating beat → `PAD_BACK_SHOT` → ANAT |
| B15 | The placement is the whole thing. A centimetre too high and it is a sleeve again. | placement | — | `PLACE-LOCK` close-up |
| B16 | Thirty four percent less strain. Measured. Three years with orthopedic surgeons. Two hundred thousand people wearing one. | proof | all held | overlays (34%, 200,000); surgeon one-off (§19B) |
| B17 | Ten seconds to put on. No sores, no rolling down, and nobody can see it. | features | **F8** | R1 seats it; trousers over it (§9D) |
| B18 | The thing people write to us about most… rusty hinge… stop planning the stairs… | outcome | **F9** | R2 / R1 on stairs, easy |
| B19 | …Put one on one knee only. Leave the other bare. Go to your own stairs and come down forwards… | self-test | — | R1: one knee strapped, one bare, down forwards |
| B20 | Not because the arthritis has gone… Because the weight is not landing on that band any more. | honest caveat | arthritis held | host |
| B21 | So here is the choice… | choice | — | host |
| B22 | Two for one… Sixty days, and you keep the straps. From the Stryde site. The copies stretch… | offer | BOGOF ✓ · 60 days ✓ · **F10, F11** | open box, two straps; a copy (`FAKE-BASE` + one archetype) |
| B23 | The next step is going to land in the same place either way. Go and do it forwards. | close | — | host → R1 at the top of her stairs |

Coverage: 3 hooks + 23 body phrases · **uncovered 0 · blocked 0** (dispositions at step 5).

### Claims (§43A)

Held in the Product Sheet register (V7.49.37): 17× bodyweight · three years with orthopaedic surgeons · silicone pad (prompts say "the pad") · 34% less strain (sports scientists) · arthritis · 200,000+ wearers · Buy 1 Get 1 Free · 60-day money-back guarantee. Numbers are post overlays, never generated (§17). **Not in the register:** F2–F11 (Flags). Voiced verbatim in every case (§22U): **a line is flagged, never rewritten.**

### Mode & Model Lock (§18A)

| Beat class | Model · params | Why |
|---|---|---|
| Mode | **Mode 1 Realistic**, iPhone 17 Pro Max, 9:16 (plates 16:9) | realistic reference; no Mode 4/5 instruction |
| Avatar sheets | `gpt_image_2_5` · `variant: sunburst` · `quality: high` · `resolution: 2k` | §19 measured route (**used this delivery**) |
| Talking-head seed (host on the podcast set) | `nano_banana_pro` | talking-head seed class |
| Wordmark with hands or a body (worn, seating, held) | `nano_banana_pro` + `WORDMARK-LOCK` | rule 7; the name must read |
| Wordmark, no person (box, product hero) | `nano_banana_pro` | — |
| Volume B-roll with a person, no readable wordmark | `nano_banana_2` | volume |
| Volume B-roll, no person (sleeve, brace, gel, painkillers) | `nano_banana_2` | — |
| Anatomy (EG05) | `nano_banana_2` | §12A |
| Video | Kling 3.0 (`kling-video-v3_0_omni`), start image required, `prefer_multi_shots: false`; Kie `kling-3.0` when Kling is short | §4, §5, §27G |
| Voice | §22U: two Kling source takes of the host → ElevenLabs clone by API → Enhance → Eleven v4, all three hooks + body in one request, split at the silences | §22U |
| Talking heads | HeyGen **Avatar V**, the whole untrimmed take in one go with a motion prompt, then cut into HK1/HK2/HK3/BODY and trimmed with `trim.py` (natural pace) | §22U steps 11–14 |

**Other locks:** format **Short VSL, podcast talking head** (~55% host on camera, as the reference) · **side: right knee** (no knee named → `SIDE_RULE`); B19 shows one strapped knee and one bare (the script's own test, never both strapped) · mechanism claim: **protection** (Product Sheet §6) · edit: `EDIT-STRYDE-WC` · hooks: 3 → **3 videos, one shared body** (§30H).

---

## 3. Cast (step 3): generated, on the board for your check

**Casting to the Product Sheet (British, 55–80, balanced men/women) and the script:** the host speaks on camera; two recurring wearers carry the B-roll story the body tells: **R1 Maureen, "never run a mile in her life"**, and **R2 Desmond, "played sport for thirty years"**. The host sits just under the buyer band on purpose: she explains, she isn't the patient. One-offs (the surgeon on B16, hands, extras) come at step 4–5.

| Sheet | Job ID | File | Board |
|---|---|---|---|
| H-HOST | v1 `79f9d508…`, v2 `b9242d45…` (both on the Old board) · **v3 `e6a49b97-3b9d-4651-a870-a64f52b5183c`** | `cast/H-HOST_v3.png` | To check (v3) |
| R1-MAUREEN | `fd75b478-6a1b-4a8f-ba80-d20f272f65b0` | `cast/R1-MAUREEN_v1.png` | To check |
| R2-DESMOND | `9f0903d2-b148-4273-93b6-e4227a87d9f6` | `cast/R2-DESMOND_v1.png` | To check |

Manual run: **I don't check the sheets** (§18B step 3). Confirm or Fix each on the board. Prompts: `cast/<ID>.prompt.txt`, assembled from Appendix A by ID in `cast/build_sheets.py` (`CAM-LOCK` → `AVATAR-SHEET` + `SHEET-GRID` → `SKIN-T` → `CAP-SHARP` → `CAP-FILE` → `NEG-SHEET` + `NEG-GRID` + `NEG-FILE` + `NEG-DEFAULT-FACE`), 9,256–9,322 chars each. Spend: 3 Sunburst jobs, one render each (R2's first call hit a Higgsfield 503 before it started and was sent again once).

### Identity strings: read off the renders (§7)

| ID | Identity string |
|---|---|
| H | white British woman, 41, medium height, softly athletic, relaxed open posture; soft heart-shaped face, round apple cheeks, hazel-green eyes that crinkle at the corners, small slightly upturned nose, wide full mouth; freckles across the nose and cheeks and a small dark beauty mark high on the left cheekbone; shoulder-length honey-blonde waves with darker roots, tucked behind the right ear; oatmeal-cream chunky cable-knit jumper, mid-blue straight jeans, dark brown leather Chelsea boots *(v3: a new person, from your second Fix)* |
| R1 | white British woman, 69, short and slight, a little rounded at the upper back; heart-shaped face, round light-blue eyes, short straight nose, thin lips; a small dark mole at the left corner of her mouth; short layered white crop lifted at the crown; dusty-pink cardigan over a navy-and-white Breton top, navy A-line skirt above the knee, white canvas plimsolls; bare knees |
| R2 | Black British man, 66, tall, broad-shouldered, thickened middle, strong legs; long square-jawed face, deep-set dark eyes, broad straight nose; close-cropped grey-white hair and a short grey-white beard; navy half-zip sports top over a white T-shirt, dark grey jogging shorts above the knee, white trainers with navy trim |

### §19A axis tables

| Axis | H | R1 | R2 |
|---|---|---|---|
| Face | heart-shaped, apple cheeks | heart-shaped, pointed chin | long, square jaw |
| Hair | shoulder-length honey-blonde waves | short white layered crop | cropped grey-white + beard |
| Age position | 41 (below the band: the presenter) | 69 (mid) | 66 (mid) |
| Build | medium, softly athletic | short, slight | tall, broad, athletic gone soft |
| Class / wardrobe | smart-casual presenter | neat retired, Breton stripes | sporty, zip-neck |
| Marker | beauty mark on the left cheekbone + freckles | mole at the mouth | scar across the nose |
| Voice | British (below) | non-speaking | non-speaking |
| Environment | podcast set | her terraced-house stairs, hall | his house, stairs, old team photos |

**Clearance within the build:** every pair differs on ≥ 7 axes. **Against the roster** (`stryde-lost-moments` N, C1–C6; `stryde-identity`): every new face differs on ≥ 6 axes; H v3 differs from R1 (the nearest: both white British women) on 7 of 8 axes. ✓

### Host: `VOICE-HOST` (§22D) and §20 constraint sheet

**`VOICE-HOST`** (goes verbatim into every §22U step-2 take)
```
A British woman of forty-one from the south-east of England, a clear mid-range voice with a little warmth underneath, plain and confiding, as if explaining something to a friend across a table. Soft modern southern English vowels, never RP, never estuary caricature, never American. Statements fall at the end; the turn lines slower and lower, never louder. Brisk and even, about one hundred and seventy words a minute.
```

| Field | H — host |
|---|---|
| Accent | south-east English, modern and unforced; never RP, never American |
| Pacing | ~170 wpm (reference 176) |
| Posture / rest / gesture / rig | seated on a leather sofa, one knee over the other, hands loose in the lap, podcast mic on a boom arm in the foreground; Economical gestures on the turn lines; eyeline just off the lens toward an unseen guest in the wide, on the lens in the MCU; locked-off tripod (the reference's) |
| Audio proximity | close podcast mic |
| Wardrobe never-list | scrubs, white coat, anything clinical (she is not a clinician; the script never says she is) |
| Physical never-list | never wears the product on camera (she presents it; the wearers wear it) |
| Voice spec | `VOICE-HOST` above |
| Stress register | slower and lower on "Here is what changed.", "None of them are aimed at the spot.", "It is called Stryde."; never bigger |
| Non-speech events | one short in-breath before a number; nothing else |
| Voice name (§22U step 7) | `WhatChanged-Host` (proposed) |

---

## Flags (decisions for the user: nothing below was changed silently)

| # | Where | Finding | Recommendation |
|---|---|---|---|
| F1 | Product Sheet | The Drive copy is V7.49.29; the repo has V7.49.37 (wordmark lock, inner pad redrawn, back-of-strap ruling) | Using V7.49.37 |
| **F2** | HK2, B03 | "about as wide as your thumb", "one of the strongest things in your body": anatomy statements, not advertiser-held (Tier 3) | Voiced as written; no size shown against a thumb on screen. Please confirm |
| **F3** | HK2 | "Not even the person who read your scan": implies clinicians miss it | Voiced as written; no clinician shown on that line (host on camera). Please confirm the advertiser is happy with it |
| F4 | HK3 | "about seventy million times your full bodyweight": the script's arithmetic (5,000 × 365 × 40 = 73m), built on the held 17× figure | Voiced as written; "70 million" as a post overlay |
| **F5** | B04 | "coming down puts more through that band than going up does": a biomechanics claim, not in the register | Voiced as written. Please confirm it's held |
| **F6** | B09–B10 | "most of what gets sold for this cannot work" + sleeve / hinged brace / gel / painkiller: comparative claims, not in the register | Voiced as written; shown as ordinary unbranded objects, never a named brand, never a clinic. **Please confirm the advertiser holds it** |
| F7 | B14 | "Your weight gets caught and moved off the worn part": load-path wording; the Product Sheet's claim is **protection** | Voiced as written; pictured as protection (the pad takes the load off the spot) |
| **F8** | B17 | "Ten seconds to put on. No sores, no rolling down, and nobody can see it.": not in the register | Voiced as written; shown as a seating beat and trousers over the strap (§9D). Please confirm |
| **F9** | B18 | "the knee stops feeling like a rusty hinge. They stop planning the stairs": outcome / testimonial claim | Voiced as written. Please confirm it's held |
| F10 | B22 | "you keep the straps" (on a refund): not in the register (the guarantee is held, its terms aren't) | Voiced as written; terms in the edit only |
| **F11** | B22 | "The copies stretch, and a stretched strap stops holding the spot": an anti-copy claim | Voiced as written; the copy shown per Product Sheet §7 (`FAKE-BASE` + one archetype, unbranded). Please confirm |
| F12 | EG02 | The reference puts its host's cut-out over most B-roll; the house rule (V7.65.0) caps boxed B-roll at 1 in 5 | House rule wins: B-roll full screen, `pip` ≤ 1 in 5 |
| F13 | Script | "orthopedic" (US spelling) in a British script | Spelling only; it's voiced the same. Captions will use "orthopaedic" unless you say otherwise |
| F14 | Length | ≈ 3:50 per finished video (the reference is 3:15) | As written; the body isn't cut |
| F15 | Script file | No file extension and two hook labels read as spoken | Handled (see step 2); a `.docx` extension next time |

## Next — on your go (§18B step 5)

Confirm or Fix each avatar on the board and answer the bold flags (F2, F3, F5, F6, F8, F9, F11). Then steps 4–5 as one delivery: the podcast set (16:9 plate + the host's talking-head seed), R1's stairs and hall, R2's house, act map + wardrobe map for the three variants with every B-roll row given its `EDIT-STRYDE-WC` layout; then the voice straight through (Kling source takes → clone → VO → HeyGen talking heads, trimmed at a natural pace).
