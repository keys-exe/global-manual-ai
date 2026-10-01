# Build Sheet — stryde-71-stairs

**STRYDE Precision Strap · "A - VID | AI UGC | TOF | Pure Mechanism | Iteration | 71 Stairs Black American Woman"** · Standards V7.64.4 · **RUN: MANUAL** · 2026-09-28

Steps 1–3 of §18. **Stopped at the avatar review (§18B, V7.62.0)**: steps 4–5 wait for the user's go.
Boards: Current https://claude.ai/artifact/Ev166tkWbX9QaE1P7VLjti · Old https://claude.ai/artifact/E3hbWw3ea9nS8vTgzGLLmd · Final https://claude.ai/artifact/QVBQW1v5WHJ7cJN4PGxcbY · Plan https://claude.ai/artifact/KZ6FRJSii34aQcCTp6XmNy

---

## 0. Intake (§18B)

| Input | Found | Notes |
|---|---|---|
| Drive folder | `1B2H-Kx8-NpEKsMoL0IvMqbvy8uAQIL5T` (brand folder STRYDE `1MG81pjTPpj6qSJsJzKVQzcNcuyik8Nkc`) | fetched with `fetch_drive.py` → `intake/` |
| Inspo | `71_Stairs HOOK+BODY 1.mp4` — **the original "71 Stairs" ad this script iterates** (British woman, 71; Meta Ad Library 2158360988054964) | 155.6s · 9:16 · 1080×1920 · 30fps · audio |
| Script | native Google Doc, exported as `.docx` by the fetch (inferred: the only document) → `intake/script.txt`; spoken lines `work/script.lines.txt` | title line 1 ✓ · **1 hook** · 1 direction note (VN01) · **613 spoken words** |
| Product Sheet | `stryde_product_sheet_V7.49.32.py` — newer than `main`'s V7.49.31, identical to the one `stryde-lost-moments` brought in | stored as `products/stryde/stryde_product_sheet.py` + `.md` |
| Product images | 10, byte-identical to `products/stryde/stryde_refs/` | layer 1 |
| Missing | `package_closed.jpg` (locked V7.49.27) | none blocks steps 1–3 |

**Message fields:** `RUN MANUAL` → **RUN: MANUAL**. Everything else blank: `MODE` → **Mode 1** (realistic reference, §18A; the task is "AI UGC"); `HOOKS` → **in script: 1** ("same hook as 71 Stairs") → **1 finished video**; `VOICE` → derived from the script's note (below); `CAP` → E0 Higgsfield default; no Loom; `BUILD` → `stryde-71-stairs`.

---

## 1. Absorption Sheet (§42)

### Part 1 — measured

| Instrument | Reading | Settles |
|---|---|---|
| Duration / aspect / res | 155.55s · 9:16 · 1080×1920 · 30fps | 9:16 locked |
| Scene cuts | **82 shots, mean 1.9s**; runs of 0.4–0.5s in the anatomy stretch (92.3–94.5s) | a cut every ~2s |
| Silence (−30/−40 dB) | none | wall-to-wall voice; no designed pauses |
| VO transcript (faster-whisper small) | 597 words / 155.4s = **231 wpm**, one woman, British | very brisk — the edit's pace; ours will be slower (F12) |
| Talking head / B-roll | the speaker **on camera in selfie** (front camera, arm's length, chest-up, on her upstairs landing, banister and family photos behind) in ~⅓ of the shots; the rest B-roll | UGC selfie + B-roll |
| Shot frames + per-second sheets | `intake/frames/71_Stairs HOOK+BODY 1/` | Edit Grammar below |

### Part 2 — structure map

| t | Job | Script (ours) | What the original shows | Layout |
|---|---|---|---|---|
| 0.0–7.6 | **hook** — the result, then the witness | "I'm 71… faster than women half my age." / "Last Sunday, my daughter walked behind me… 'Mama, when did that happen?'" | her climbing busy station stairs past younger women → climbing her own stairs, daughter behind → selfie TH | full |
| 7.6–15.2 | the low point | "Six weeks ago… backwards… I'd just stay upstairs." | from behind, going down her stairs sideways gripping the rail · the empty landing | full |
| 15.2–28.8 | what failed | "That big knee brace… around my ankle… I done tried everything… Nothing gave me my life back." | hinged brace slipping on the knee, then round the ankle · physio couch · pill packs + coffee · cortisone injection · a heap of braces and sleeves · her at the table, deflated | full |
| 28.8–40.9 | the turn: the cousin | "my grandbaby got married… Loretta… dance floor all night… bone on bone… past fixing." | wedding marquee · the cousin dancing · **CGI knee, red worn joint** · TH | full |
| 40.9–63.7 | the reveal | "Loretta came to stay… morning routine… 'Baby, can I show you something?'… little black strap… Stryde… too small… 'walk down them stairs.'" | cousin at the front door · the table: tub, gel, brace, ice pack · cousin lifts her trouser leg, strap under the kneecap · strap handed over, held in both palms · the two of them at the table | full |
| 63.7–70.3 | **the payoff** | "the first step, I didn't even have to hold the rail… Forwards." | her walking down her stairs facing forwards, hands free | full |
| 70.3–92.3 | mechanism (Loretta's words) | "Everything else you tried… This one fixes why it hurts… one spot under the kneecap… takes the weight off. First step. Pain gone." | physio, pills, injection (the "comfortable" list) · **comparison card: sleeve vs strap on two X-ray legs, header labels** · CGI knee model with a gloved finger on the spot · glowing X-ray knees, red hotspot · strap on the knee, red glow → blue relief lines | full CGI + card |
| 92.3–112.1 | proof | "Over 200,000… Sports doctors… Loretta's husband… golf… niece… track… every day for six weeks… no brace around my ankle" | quick cuts of different people putting the strap on (0.4–0.5s each) · a sports doctor with the strap · the husband's golf swing · the niece on court · her legs in trousers (hidden) · strap by a mug on the table | full, fast |
| 112.1–125.9 | the result, lived | "Yesterday I walked to the store… Two miles… checkout line… two bags home… 'You was gone a long time.' 'I know.'" | walking a suburban street with a bag · passing younger women on a high street · standing in a shop queue with a basket · carrying bags to her door · husband in his armchair | full |
| 125.9–143.1 | proof + name + authority + objection | "six weeks… Three ladies from church… Stryde Patellar Force Redirection… three years… orthopedic surgeons… Not them cheap knock-offs…" | strap on her knee on the bed edge · walking into a room of friends · **CGI strap on a labelled anatomy knee** · surgeon + patient in clinic · generic knock-off straps, one reddening a leg | full CGI + live |
| 143.1–155.6 | offer, guarantee, close | "The link's right down below. Two straps for the price of one… Sixty days… Eleven years… my sister… She gon' walk up my stairs on her own." | her holding two straps up to camera · open box with two straps · TH · box + card being addressed · TH to the end | full |

### Part 3 — Style Lock (**copied — the brief says "same ad, same beats"**)

- One speaker, on camera in **selfie talking heads** (§22F creator framing, front camera, arm's length, chest-up, her own upstairs landing — banister and family photos behind), cut with B-roll roughly 1:2.
- iPhone register throughout (§22), real older people in real homes; the product in every result shot.
- Beats and order exactly as the original (Part 2); hard cuts at ~1.9s; the anatomy stretch cut fast.
- **Changed by the brief (VN01):** the woman (Black American, 71, light Southern accent), her family and cousin, and **US settings**: family-photo staircase, a wedding reception with line dances (Electric Slide, Cupid Shuffle), the kitchen table with pill bottles, a checkout line, church steps.

### Part 3A — Edit Grammar

| ID | Device (original) | Where | Our build |
|---|---|---|---|
| EG01 | **boxed captions**: lowercase-ish black text on white boxes, one or two short lines, centred at ~72% height; follows the voice phrase by phrase | whole ad | **kept** (CapCut) |
| EG02 | **selfie talking head** as the spine: she returns to camera between B-roll runs, never more than ~3s at a time | whole ad | **kept as the spine, but propped, not selfie** (user 2026-09-28 — §34 correction: TH-01…TH-16, C-06a, N-VOICE-IMG) |
| EG03 | **comparison card**: two X-ray legs side by side, "FULL NEOPRENE SLEEVE: uniform diffuse pressure" vs "STRYDE STRAP: precise redirection point", header labels | 76.0–77.9 | **kept as a layout, restyled**: the Product Sheet's anatomy look (§12A), sleeve vs strap; labels added in the edit, never generated (§17). Label wording flagged (F3) |
| EG04 | **CGI anatomy run**: glowing X-ray knees, red hotspot on the spot below the kneecap, then blue relief lines when the strap goes on | 77.9–92.3, 132.8–135.6 | **kept**, red = pain, blue = relief (§11), `ANATOMY_LOOK` |
| EG05 | **rapid montage**: 5–6 shots of 0.4–0.5s, different people putting the strap on | 92.3–94.5 ("Over 200,000…") | **kept** (all distinct one-offs, mixed ages) |
| EG06 | **hold-to-camera**: she lifts two straps up to the lens | 143.1–145.5 (offer) | **kept** |
| EG07 | hard cuts only; no music bed audible; no punch-ins, no transitions, no SFX | whole ad | **kept** |

**`EDIT-STRYDE-71` = EG01–EG07 as above** (the original's grammar, because the brief asks for the same ad).

### Part 4 — script absorption

**Iteration, line for line.** Every one of the original's sentences has its counterpart in our script, in the same order, re-voiced in a light Southern Black American register ("I done tried everything", "Chile", "I'ma just say it", "She gon' walk…"), with US substitutions: *mum → Mama*, *granddaughter → grandbaby*, *Barbara → Loretta*, *physiotherapy/painkillers/injections → physical therapy/pain pills/cortisone shots*, *trousers → pant leg*, *banister → rail*, *tennis → track*, *walked into town → walked to the store*, *three friends … walk into a room → three ladies from church … come down the church steps*, *Shopify sites → fake websites*. **New content:** "Electric Slide, Cupid Shuffle, all of it." (VN01's line dances). Spoken words: **613** (the original 597).

### Part 5 — surfaced, not absorbed

| Original element | Disposition |
|---|---|
| British woman, English home, station stairs | replaced per VN01 (Black American, US home; hook stairs → her own family-photo staircase and a US setting for the opener, step 4) |
| Comparison-card labels generated inside the image | labels become CapCut text (§17); the card itself is generated clean |
| Knock-off shot showing a red, sore leg (135.6–141.5) | kept as §10 fake-product B-roll on a real surface — no storefront, no marketplace UI, no logo (§10A) |
| "Amazon", "Shopify" | our line names **Amazon** only; voiced verbatim (§22U), never pictured (§10A) — **F5** |

### Part 6 — beat-it plan

| Original weakness | Our delta | Where |
|---|---|---|
| 231 wpm read, no air | the house cut at a natural pace (E11A) — clearer for a 65+ viewer; the video runs longer (F12) | voice |
| Opening shows stairs in a train station, not her home | open on **her own** family-photo staircase, the daughter one step behind — the same place the whole story returns to | hook |
| Wedding shot is a generic marquee | a Black American reception with a line dance going (Electric Slide), Loretta in the middle of the line | 28.8–36.7 |
| "Three friends… walk into a room" is abstract | **church steps** with three ladies watching her come down — a concrete, recognisable proof moment | close |

### Part 7 — confirmation

Conflicts are listed in **Flags**. **Confirm or correct the absorption along with the avatars.**

---

## 2. Script, product, claims, locks (step 2)

### Visual Instruction Ledger (§27F) — opened

| ID | Source | Instruction | Anchored | Carried by | Status |
|---|---|---|---|---|---|
| VN01 | script note | "Same ad, same beats, same hook as 71 Stairs." | whole build | Part 2 structure map, `EDIT-STRYDE-71`, 1 hook | open → step 5 |
| VN02 | script note | "Black American woman, 71, light Southern accent." | whole build | N-NARR sheet · `VOICE-NARR` | open → voice stage |
| VN03 | script note | "The dialect is written light on purpose: the actress adjusts any line to her own voice." | whole build | **F11** — TTS voices the words as written (§22U) | flagged |
| VN04 | script note | US environment: **family-photo staircase** | hook, "down my stairs backwards", payoff, close | P-HOUSE stairs plate | open → step 4 |
| VN05 | script note | US environment: **wedding reception with line dances** | "grandbaby got married… Electric Slide, Cupid Shuffle" | reception plate, C1 Loretta dancing | open → step 4 |
| VN06 | script note | US environment: **kitchen table with pill bottles** | "kitchen table… morning routine", "Pain pills", "No pills" | kitchen plate | open → step 4 |
| VN07 | script note | US environment: **checkout line** | "Stood in that checkout line ten minutes" | store plate | open → step 4 |
| VN08 | script note | US environment: **church steps** | "Three ladies from church… come down the church steps" | church plate | open → step 4 |

### Phrase inventory (§27B) — dispositions are assigned at step 5

| ID | Phrase | Job | Claim | Subject / register |
|---|---|---|---|---|
| HK-01 | I'm 71, and I take the stairs faster than women half my age. | hook | — | N climbing, passing younger women |
| HK-02 | Last Sunday, my daughter walked behind me the whole way up and said, "Mama, when did that happen?" | hook | — | N up her stairs, C2 daughter behind · TH |
| P-01 | Six weeks ago, I was going down my stairs backwards. One step at a time. | problem | — | N from above, backwards, both hands on the rail |
| P-02 | I ain't gonna lie, some days I wasn't going down them at all. I'd just stay upstairs. | problem | — | TH · the empty stairs from the landing |
| P-03 | That big knee brace I bought slid right down my leg. By evening, it was around my ankle. | failed fix | — | hinged brace sliding → at the ankle (§10 generic, no brand) |
| P-04 | I done tried everything. Physical therapy. Pain pills. Cortisone shots. Every brace and sleeve they make. | failed fix | — | TH · PT couch · pill bottles · injection · heap of braces |
| P-05 | Nothing worked. Nothing lasted. Nothing gave me my life back. | low | — | TH · N at the table, still |
| T-01 | Then my grandbaby got married in June. My cousin Loretta was there. | turn | — | reception · C1 |
| T-02 | She's 74, and she was out on that dance floor all night. Electric Slide, Cupid Shuffle, all of it. | turn | — | C1 in the line dance (VN05) |
| T-03 | Both her knees was bone on bone too. | turn | held (bone on bone) | ANAT-A red worn joint |
| T-04 | I always figured hers wasn't as bad as mine. I always figured mine was past fixing. | turn | — | TH |
| R-01 | Loretta came to stay the week after. | reveal | — | C1 at the front door with a bag |
| R-02 | She watched me at the kitchen table, going through my morning routine. Two anti-inflammatories, the gel, the brace, an ice pack on my right knee. | reveal | — | TH · the table (VN06): tablets, gel, brace, ice pack on the **right** knee |
| R-03 | After a minute she said, "Baby, can I show you something?" She pulled up her pant leg. | reveal | — | TH · C1 lifting her khaki leg (§9D reveal) |
| R-04 | She had on a little black strap, right under her kneecap. Stryde. | product first appearance | — | C1's knee, strap worn (`PLACE-LOCK`) — **product's first appearance** |
| R-05 | She handed me one. It looked ridiculous. Too small. | reveal | — | held strap in N's palms (`HELD_GRIPS`) |
| R-06 | I said, "Loretta, you know good and well this ain't gonna work on knees like mine." She said, "Just put it on and walk down them stairs." | reveal | — | TH · C1 and N at the table · seating beat (`SEAT_LOCK`) |
| R-07 | I did. Chile, the first step, I didn't even have to hold the rail. Not the second. Not the third. All the way down. Both feet. Forwards. | **payoff** | — | N down her stairs facing forwards, hands free |
| M-01 | She said, "Everything else you tried was made to keep you comfortable while your knee got worse. | mechanism | **comparative (F2)** | PT / pills / shot callbacks |
| M-02 | This one fixes why it hurts." | mechanism | **outcome (F2)** | comparison card (EG03) |
| M-03 | She said, "There's one spot under the kneecap where every step lands." | mechanism | held (the spot; 17× not voiced) | ANAT-A, red point below the kneecap |
| M-04 | "Every brace, every shot, every pill you ever tried treated the whole knee. Not that spot. That's why ain't nothing worked." | mechanism | comparative (F2) | braces heap · injection X-ray · pills · ANAT |
| M-05 | "The pain is pressure. That's all it is. This strap sits right on that spot and takes the weight off." | mechanism | protection ✓ | ANAT red → strap on → blue relief (EG04) |
| M-06 | First step. Pain gone. Just like that. | outcome | **outcome (F4)** | N's feet on the top step |
| PR-01 | Over 200,000 people wear one now. | proof | held | EG05 montage |
| PR-02 | Sports doctors recommend it. Not the pharma companies. Sports doctors. | authority | **not in register (F1)** | sports doctor (one-off, §19B) · TH |
| PR-03 | Loretta's husband wears one. He's 76, and he plays golf twice a week. | proof | — | husband (one-off) golf swing |
| PR-04 | Her niece wears one when she runs track. She's 22. | proof | — | niece (one-off) on a track |
| PR-05 | I've worn mine every day for six weeks. Under my clothes. Don't nobody know it's there. | feature | — | TH · §9D conceal, trousers |
| PR-06 | No pills. No gel. No brace around my ankle by lunchtime. | feature | — | strap by a coffee mug on the table |
| L-01 | Yesterday I walked to the store. Two miles there. Two miles back. Passed three women half my age. | result | implied (F7) | N walking a US suburban street, passing younger women |
| L-02 | Stood in that checkout line ten minutes without shifting my weight. Carried two bags home. Didn't nobody help me. | result | — | checkout line (VN07) · bags to the door |
| L-03 | When I got home, my husband said, "You was gone a long time." I said, "I know." | result | — | husband (one-off) in his chair · TH |
| C-01 | That was six weeks of wearing the strap. Nothing else. | result | — | strap on N's right knee |
| C-02 | Three ladies from church already ordered one after they watched me come down the church steps. | proof | — | church steps (VN08), three ladies (one-offs) |
| C-03 | So I'ma just say it right here. It's called Stryde Patellar Force Redirection. | name | name (F3) | TH · ANAT strap on labelled knee (labels in edit) |
| C-04 | They spent three years designing it with orthopedic surgeons. It's the real thing. | authority | held | surgeon + patient (one-offs, §19B) |
| C-05 | Not them cheap knock-offs they be selling on Amazon and them fake websites. | objection | **marketplace named (F5)** | §10 fake straps on a real surface |
| C-06 | The link's right down below. Two straps for the price of one right now. | offer | held (BOGOF) | N holding two straps to camera (EG06) |
| C-07 | Sixty days to send them back if they don't work. | guarantee | held | open box, two straps |
| C-08 | Eleven years of knee pain. Gone the first step I took with it on. | outcome | **outcome (F4)** | TH |
| C-09 | I bought my sister a pair that same week. She coming Sunday. She gon' walk up my stairs on her own. | close | — | box being addressed · TH to end |

Coverage: 2 hook + 41 body phrases · **uncovered 0 · blocked 0** (dispositions at step 5).

### Claims (§43A)

Held in the Product Sheet register (user-confirmed V7.49.29): three years with orthopaedic surgeons · bone on bone · 200,000+ wearers · Buy 1 Get 1 Free · 60-day money-back guarantee · the spot below the kneecap. Numbers are post overlays, never generated (§17). **Not in the register:** F1, F2, F4, F7 — voiced verbatim (§22U), listed in Flags.

### Mode & Model Lock (§18A)

| Beat class | Model · params | Why |
|---|---|---|
| Mode | **Mode 1 Realistic**, iPhone 17 Pro Max, 9:16 | realistic reference; UGC |
| Avatar sheets | `gpt_image_2_5` · `variant: sunburst` · `quality: high` · `resolution: 2k` | §19 measured route (**used this delivery**) |
| Talking-head seed (N on the landing, propped — never selfie) | `nano_banana_pro` | talking-head seed class |
| Wordmark with hands or a body (held, worn, seating, offer hold-up) | `nano_banana_pro` + `WORDMARK-LOCK` | rule 7 |
| Wordmark, no person (strap by the mug, box) | `nano_banana_pro` | wordmark |
| Volume B-roll with a person, no readable wordmark | `nano_banana_2` | volume |
| Anatomy (EG03, EG04) | `nano_banana_2` | §12A |
| Video (B-roll) | Kling 3.0 (`kling-video-v3_0_omni`), start image, `prefer_multi_shots: false` | §4, §27G |
| Voice | §22U: Kling source takes (2+) → ElevenLabs clone (API) → Enhance → `eleven_v4` → house cut | §22U |
| Talking heads | HeyGen Avatar V driven by the VO, motion prompt on every render | §22U step 13 |

**Other locks:** format **propped talking heads + B-roll** (the original's selfie TH changed to propped by the user, 2026-09-28); **side: right knee** ("an ice pack on my right knee" → `SIDE_RULE`); mechanism claim: **protection**; edit: `EDIT-STRYDE-71`; hooks: **1, in script → 1 finished video**.

---

## 3. Cast (step 3) — generated, on the board for your check

Everyone with two or more beats gets a sheet. **Three:** the narrator (on camera and in most B-roll), **C1 Loretta** (reception, door, table, reveal, stairs coaching) and **C2 the daughter** (both hook shots — sheeted so the hook's faces hold). One-offs (grandbaby bride, Loretta's husband, the niece, the sports doctor, the surgeon, the narrator's husband, the church ladies, the montage wearers, the younger women she passes) are cast at step 5 per §13.

| Sheet | Job ID | File | Board |
|---|---|---|---|
| N-NARR | `5d4f7598-14d9-4e53-8173-bb48b516e54a` | `cast/N-NARR_v1.png` | To check |
| C1-LORETTA | `cf777e26-5d0f-4fae-9063-116f20e27ffd` | `cast/C1-LORETTA_v1.png` | To check |
| C2-DAUGHTER | `61ff6760-6aba-4054-aaf5-31b7a67c6cd9` | `cast/C2-DAUGHTER_v1.png` | To check |

Manual run: the sheets are **not checked by me** (§18B step 3) — Confirm or Fix each on the board. Prompts: `cast/<ID>.prompt.txt`, built from Appendix A by ID in `cast/build_sheets.py` (`CAM-LOCK` → `AVATAR-SHEET` + `SHEET-GRID` → `SKIN-T` → `CAP-SHARP` → `CAP-FILE` → `NEG-SHEET` + `NEG-GRID` + `NEG-FILE` + `NEG-DEFAULT-FACE`), 9,040–9,521 chars. Spend: 3 Sunburst jobs, one render each (Higgsfield 18,072.75 before).

### Identity strings — read off the renders (§7)

| ID | Identity string |
|---|---|
| N | Black American woman, 71, medium height, soft and full through the hips; wide face, heavy-lidded dark eyes, broad nose, full lips; a cluster of small dark raised spots high on the left cheek; short grey natural hair in tight curls, fuller on top; cream open cardigan with ¾ sleeves over a coral top, navy slim trousers, black flat slip-ons |
| C1 | Black American woman, 74, tall and lean, straight-backed; long face, high cheekbones, sharp jaw, deep-set eyes; short silver-grey coiled crop; plum button-front blouse with rolled sleeves, khaki straight trousers, white canvas slip-ons |
| C2 | Black American woman, mid-40s, medium height, sturdy; round face, full cheeks, straight brows, broad nose, full lips; long dark box braids pulled back in a low ponytail; heather-grey crewneck sweatshirt, mid-blue jeans, white trainers |

### §19A axis tables

| Axis | N | C1 | C2 |
|---|---|---|---|
| Face | wide, heavy-lidded, soft jaw | long, high cheekbones, sharp jaw | round, full cheeks |
| Hair | short grey tight curls | silver coiled crop | long dark box braids, ponytail |
| Age position | 71 | 74 (older) | ~46 (daughter's generation) |
| Build | medium, full | tall, lean, upright | medium, sturdy |
| Class / wardrobe | home, soft cardigan | neat, going-visiting | weekend casual |
| Marker | dark spots high on left cheek | scar through the right eyebrow | crescent scar on the chin |
| Voice | light Southern (below) | none (quoted by N) | none (quoted by N) |
| Environment | stairs, landing, kitchen table | reception, front door, table | stairs (hook) |

**Clearance:** N–C1 differ on 7 axes, N–C2 on 7, C1–C2 on 8. ✓ Against the roster (stryde-identity, stryde-lost-moments): no shared face architecture with any sheet (closest: lost-moments N, a Black British woman of 62 — different face, hair, age, wardrobe, marker, voice). **Open face type (§19A scope note):** darker skin tones remain the unverified §22S face type; all three take the standard first-frame look on their first beat.

### Narrator — `VOICE-NARR` (§22D) and §20 constraint sheet

**`VOICE-NARR`** (goes verbatim into every §22U step-2 take, inside Kling's 2,500 limit)
```
A Black American woman of seventy-one from the South, a warm, low, slightly husky voice with a soft rasp at the ends of phrases. A light Southern lilt — drawn-out vowels, dropped g's, relaxed rhythm — never a caricature, never a drawl for effect. Talks like she's telling it to her sister across the table: easy, sure of herself, a smile in the voice on the good parts. Statements fall at the end; stress is slower and lower, never louder.
```

| Field | N — narrator |
|---|---|
| Accent | light Southern Black American (e.g. Georgia / the Carolinas), placed and unforced; never General American newsreader, never a stage drawl |
| Pacing | conversational, ~165–175 wpm before the house cut (the original is 231 wpm) |
| Posture / rest / gesture / ocular / rig | standing at the top of her stairs (EG02), phone **propped** at chest height ~1.25 m, waist-up — never selfie (user 2026-09-28); hands resting at the waist, Economical gestures; eyeline on the lens |
| Audio proximity | R2 (propped phone) |
| Wardrobe never-list | anything clinical; nothing that hides the right knee on a worn beat |
| Physical never-list | never both knees strapped; never the brace and the strap together |
| Voice spec | `VOICE-NARR` above |
| Stress register | slower and lower on "Forwards." / "I know." / "on her own." |
| Non-speech events | a soft laugh before "Chile" (once); a short breath before a number. Nothing else |
| Mouth asymmetry | read off the voice-source frame at the voice stage |
| Voice name (§22U step 7) | `Stairs-Narrator` (proposed) |

---

## Flags (decisions for the user — nothing below was changed silently)

| # | Where | Finding | Recommendation |
|---|---|---|---|
| **F1** | PR-02 | "Sports doctors recommend it. Not the pharma companies." — the register holds *orthopaedic surgeons* and *sports scientists*, not sports doctors; "not the pharma companies" is a comparative | Voiced as written, shown with a sports-medicine doctor (one-off, §19B). **Please confirm the advertiser holds it** |
| **F2** | M-01, M-02, M-04 | "made to keep you comfortable while your knee got worse", "This one fixes why it hurts", "treated the whole knee… That's why ain't nothing worked" — comparative/outcome claims not in the register | Voiced as written (they're the original's lines too). Please confirm |
| F3 | C-03, EG03 | Product name "Stryde **Patellar Force Redirection**" and the card's "precise redirection point": load-path wording; the Product Sheet claim is **protection** | Name voiced as written; pictured as protection (the pad takes the weight off the spot), card labels written in the edit as "FULL SLEEVE: pressure everywhere" / "STRYDE STRAP: one spot" unless you want the original's words |
| **F4** | M-06, C-08 | "First step. Pain gone." / "Eleven years of knee pain. Gone the first step" — outcome claims | Voiced as written. Please confirm |
| **F5** | C-05 | "Amazon" named (§10A) | Voiced verbatim (§22U locks the words); never pictured — knock-offs shown as plain straps on a table (§10). A generic take ("the big websites") can be voiced as a spare on request |
| F6 | Offer | "Two straps for the price of one" = Buy 1 Get 1 Free (held); "Sixty days" (held); "200,000" (held) | ✓ overlays in the edit |
| F7 | L-01 | "Two miles there. Two miles back." — implied outcome | Voiced; no distance shown on screen |
| F8 | Side | "an ice pack on my **right** knee" | Strap on the right knee throughout (`SIDE_RULE`) |
| F9 | Hooks | "same hook as 71 Stairs" → **1 hook, 1 finished video** | Say if you want 2 more hooks written (3 videos) |
| F10 | `package_closed.jpg` | still missing from the folder | open box only |
| **F11** | VN03 | "the actress adjusts any line to her own voice" — there's no actress: the voice is a TTS clone and §22U voices every word verbatim | Voiced exactly as written ("I ain't gonna lie", "Chile", "I'ma", "She gon'"). The Enhance pass adds delivery only. Say if you want any line softened |
| **F12** | Length | 613 words. At a natural pace and the house cut the video lands around **2:45–3:10**, vs the original's 2:36 at 231 wpm | Keep the natural pace (my recommendation — clearer for 65+ viewers); or say "match the original's speed" and the cut tightens |
| F13 | Talking heads | The original's selfie TH is on her landing; ours: her own US family-photo staircase landing (VN04) | set at step 4 |

## Next — on your go (§18B step 5)

Confirm or Fix each avatar on the board and answer F1, F2, F4 (and anything else). Then steps 4–5 as one delivery: property sheet + plates (her house — stairs, landing, kitchen), reception, store/checkout, church steps, street; act map + wardrobe map with every VN row assigned and `EDIT-STRYDE-71` layouts; `angles.py` pass. Then the voice stage straight through (§22U: Kling source takes → clone → VO → HeyGen talking heads → trim).


## 5c. Music Register Map (§40A, added 2026-10-01 on the user's ask: "use the new bgm update")

### The family

One music family for the whole video: felt piano, low cello and bowed strings, a soft heartbeat pulse, a warm string pad from the turn on. Instrumental, slow (60 BPM measured). Both hooks share the same track (both hooks are 10.95 s; the body is identical).

### The map

| Part | Lines | What the script is doing | Register | Cue in plain words | In – out (finished video) |
|---|---|---|---|---|---|
| Hook — the callout | “I'm 71…” → “Mama, when did that happen?” | opens a loop — the callout, the question | `MUS-OPEN` | investigative documentary suspense, low sustained drone, slow felt pulse, sparse felt piano notes, soft ticking, minor, unresolved | 0.0–10.9 s |
| Act 1 — the stairs backwards, the failed fixes | “Six weeks ago…” → “Nothing gave me my life back.” | the problem, the failed fixes, the years lost | `MUS-EXPOSE` | darker and lower, long low cello drone, dissonant interval, present slow heartbeat pulse, minor, no warmth | 10.9–39.0 s |
| Act 2 — Loretta on the dance floor | “Then my grandbaby got married…” → “mine was past fixing.” | opens a loop — the callout, the question | `MUS-OPEN` | curiosity, the drone continues, a single questioning piano figure, soft pulse, modal, unresolved | 39.0–57.6 s |
| Act 3 — the kitchen table, the little strap, the doubt | “Loretta came to stay…” → “walk down them stairs.” | curiosity — leaning in, how it works | `MUS-EDU` | inquisitive, repeating soft piano arpeggio, light pulse, leaning in, minor, building slowly | 57.6–88.8 s |
| Act 3 — I did. The first step | “I did.” → “Both feet. Forwards.” | the turn — it works | `MUS-TURN` | release, the drone lifts, first warm major chord, pulse opens into movement, strings enter softly | 88.8–100.1 s |
| Act 4 — why it works | “Everything else you tried…” → “Pain gone. Just like that.” | curiosity — leaning in, how it works | `MUS-EDU` | inquisitive and forward, clean repeating piano arpeggio, steady light pulse, warm undertone kept, lifting at the end | 100.1–128.2 s |
| Acts 5–6 — the proof, the walk, the husband | “Over 200,000 people…” → “I said, ‘I know.’” | proof and the life back | `MUS-AFTER` | warm hopeful theme, major, strings pads and piano with movement, dignified lift, the opening figure now warm | 128.2–171.8 s |
| Act 7 — the name, the offer, her sister | “That was six weeks…” → “on her own.” | the name, the real thing vs copies, the offer | `MUS-OFFER` | confident steady pulse, a little brighter, the theme held calm, ends on a held resolved chord, no flourish | 171.8–210.6 s |

### Reference vs script

The reference ad has no music bed (EG07). §40A: the reference decides placement, never register — the user asked for the new music rule on this build ("use the new bgm update", 2026-10-01), so a quiet bed runs under the voice: about 18 dB under in pauses, about 26 dB under while she speaks. It dips 4 dB more under the link, the price and the guarantee.

### Check

ElevenLabs Music, one track (MUS-FINAL v1). music.py check on the bed after shaping: LENGTH, ENERGY order, DROPOUT, VOCALS (none), TEMPO pass. The CLICK flags are musical onsets, located and listened for: the first note at 0.4 s, piano attacks around 12 dB, the soft heartbeat ticks over the final held chord (209–212 s). The composer resolved at ~201 s and faded by 208.5 s; the held final chord was extended with a 1.5 s crossfade to cover her last line. Section levels set in the mix (low −4 dB, mid 0, high +2.5 dB, 1 s ramps).
