# Build Sheet — stryde-half-my-age

**STRYDE Precision Strap · "A - VID | AI Drama VSL | TOF | Discovery Story | Iteration | HalfMyAge Drama"** · Standards V7.74.2 · **RUN: MANUAL · MODE 4 Realistic Film · AI Drama VSL** · 2026-09-30

Steps 1–3 of §18. **Stopped at the avatar review (§18B, V7.62.0)**: steps 4–5 wait for the user's go.
Boards: Current https://claude.ai/artifact/RrQR9jKnsbqT6v8uJMbqR2 · Old https://claude.ai/artifact/SXWuEkNiYcdetxvhetCFaZ · Final https://claude.ai/artifact/FH22SWdaLRACaGTyS92KpH · Plan https://claude.ai/artifact/UK75G7UMCa1sSmvwJQFWJo

---

## 0. Intake (§18B)

| Input | Found | Notes |
|---|---|---|
| Drive folder | `1R1jJrUhMjPzbIsbM3fmXdJUpxnu48iOT` — matches no existing build → new build | fetched with `fetch_drive.py` → `intake/` |
| Inspo (primary) | `inspo_halfmyage_drama.mp4` — an AI Drama VSL (British divorcee, 55, lipstick offer; the script's first Ad Library link) | 322.3s · 9:16 · 360×640 · 30 fps · audio |
| Inspo (secondary) | `71_Stairs HOOK+BODY 1.mp4` — the original "71 Stairs" UGC ad this script iterates | 155.6s · 9:16 · 1080×1920 · position-not-look (story beats only) |
| Script | `.docx`, title line 1 ✓ → `work/lines.json` (screenplay parse: `work/parse_script.py`) | **4 hooks (A, B, C, E) + 12 scenes · 74 spoken lines · 739 words (body 611) · 25 parenthetical visual notes** · 11 speakers |
| Product Sheet | `stryde_product_sheet_V7.49.32.py` — **older** than the repo's V7.49.38 | the repo's V7.49.38 is kept (`products/stryde/`) |
| Product images | 12; 11 byte-identical to `products/stryde/stryde_refs/`; **new: `back_ref_v2.png`** (clean studio back view of the grey grooved pad) | added to `stryde_refs/` (layer 1) |
| Loom | none | — |

**Message fields:** `RUN MANUAL` → **RUN: MANUAL**; `MODE 4` → **Mode 4 Realistic Film** (the §2 explicit instruction); FORMAT → **AI Drama VSL** (the script's title, §3B); `HOOKS` → **in script: 4 (A, B, C, E)** → **4 finished films**; `VOICE` → derived (§22D, below); `CAP` → E0 default; `DIRECTIONS` none; "use the updated branches" → checkout on the default branch at V7.74.2 (no newer standards on any branch). `BUILD` → `stryde-half-my-age`.

---

## 1. Absorption Sheet (§42)

### Part 1 — measured (`work/inspo_measure.json`, `work/inspo_transcript.json`)

| Instrument | Drama inspo (primary) | 71 Stairs (secondary) | Settles |
|---|---|---|---|
| Duration / aspect | 322.3s · 9:16 | 155.6s · 9:16 | 9:16 locked; a 5–6 min film is the format |
| Scene cuts | **72 shots, mean 4.5s**; dialogue beats 1–3s, held establishing / reaction shots 10–15s | 82 shots, mean 1.9s | our film cuts at the drama's rhythm, never the UGC's |
| Silence (−40 dB) | none; −30 dB only at dialogue gaps | none | continuous sound bed; pauses live inside scenes |
| Words / pace | 666 words / 322s = **124 wpm** (narration + dialogue) | 231 wpm | our 739 words at ~124 wpm ≈ **5:05–5:40 per film** (hook + body) |
| Speech mix | narrator VO over scenes (~50%), on-screen dialogue lip-synced (~40%), narrator **to the lens** only in the close (last ~20s, holding the product) | one speaker | §3B: narrator looks at the lens only in Offer & Close |
| Captions (OCR read off the frames) | word-by-word, **bold lowercase white, the spoken word highlighted yellow**, centred at ~77% height, 2–4 words on screen | boxed captions | EG01 |
| Shot frames + per-second sheets | `intake/frames/inspo_halfmyage_drama/` (11 sheets) | `intake/frames/71_Stairs HOOK+BODY 1/` | Edit Grammar below |

### Part 2 — structure map (drama inspo → our script)

| t | §3B act | Inspo shows | Our slot |
|---|---|---|---|
| 0.0–9.6 | **Hook — cold open** | kitchen at dusk, husband in his coat by the door (the crisis), then a flash-forward: her in business class, champagne — VO sets the before/after in two lines | HK A/B/C/E: the result shown (stairs beaten, witnessed by the daughter) + "When did that happen?" + VO "I'm 71…" |
| 9.6–29 | Before (the wound, dialogue) | OTS/CU two-hander in the kitchen: "I'm leaving." "What?" — cool blue night, warm pendant practical | SC02 Rock bottom: landing ↔ hallway, husband "I'll bring it up", "Sleep alright?" "Fine, love." |
| 29–82 | Problem | daughter on the phone (single CUs, cross-cut), book club overheard through a doorway, driving alone at night | SC03 tried everything + drawer + sister on the phone (cross-cut CUs) |
| 82–149 | Turn — the friend brings it | café two-shot / OTS singles; the friend explains the mechanism in dialogue; buy-one-get-one planted by the friend | SC04 wedding (Barbara seen) → SC05–SC08 Barbara at the table, the strap, the test on the stairs, the mechanism in her words |
| 149–182 | Turn — the first test | bathroom mirror, macro insert of the product on the lips, tissue test | SC07 the test: first step down forwards, hands free |
| 182–261 | After — mirrored scenes | "six weeks later" card in VO; airport, rooftop dinner with strangers — warm golden light; the ex's claim answered | SC09–SC12: proof, town, the queue, the husband, the café friends |
| 261–303 | After — the loop paid | daughter sees the photos: "You look incredible" | SC13 the sister on the stairs |
| 303–322 | Offer & Close | narrator in her bright living room **to the lens**, product held at chest height, macro insert, offer and guarantee spoken | L068–L071 over the story (our script keeps the offer inside the story — "planted") |

### Part 3 — Style Lock (copied)

- **Format:** AI Drama VSL — scenes with lip-synced dialogue, the protagonist narrating over them, no presenter until the close.
- **Visual grammar:** restrained prestige-drama coverage in 9:16 — establishing wides held long, OTS pairs, clean singles tightening to CU on the turn, inserts for props; faces off-lens; shallow depth from MCU in.
- **Light and colour arc:** Before/Problem at dusk and night, cool blue ambience with one warm tungsten practical (pendant, lamp); Turn in soft daylight; After in warm golden daylight and sunset. Read off the frames — this is the §30K light arc.
- **Rhythm:** mean shot 4.5s; dialogue lines 1–3s per shot, reactions held; a new scene every ~20–40s (§3B).
- **Tone of voice:** plain British, understated, dry humour, lines left hanging.

### Part 3A — Edit Grammar → `EDIT-HALFMYAGE`

| ID | Device (inspo) | Where | Our build |
|---|---|---|---|
| EG01 | **word-by-word captions**: bold lowercase white, the spoken word in yellow, 2–4 words, centred at ~77% height, no box | whole film | **kept** (CapCut) |
| EG02 | **full-frame shots only** — no split, no picture-in-picture, no cutouts | whole film | **kept** (every row `full`) |
| EG03 | **hard cuts** only; no transitions, no speed ramps, no punch-ins beyond a reframe | whole film | kept; time jumps carried by the VO, not by cards (VN23: "the VO line announces the jump, no card") |
| EG04 | **insert macro** of the product in use (lipstick on the lips) at the first test | 151–167 | kept as the strap's reveal / first-step insert (`HERO-FILM`, §24G) |
| EG05 | **narrator to the lens with the product** for the offer | 303–322 | **not copied as a separate scene** — our script plants the offer in the story (SC13 heading); the narrator stays off-lens. Say if you want a to-lens close (F12) |
| EG06 | low music bed under the whole film, dipping under dialogue | whole film | music added in the edit (§24M, never generated in a clip) |
| Light | cool night + warm practical → daylight → golden hour | by act | §30K light arc (Look Sheet field 3) |
| Focus | shallow from MCU in, deep on wides; no rack focus seen | — | §30J |
| Angles | eye-level singles and OTS, a few high wides (the empty hallway), low reverse on the ex at the door | — | range copied at step 5 (`angles.py`) |

### Part 4 — script absorption

The script is **the 71 Stairs story (secondary inspo) rewritten as a drama in the primary inspo's form**: the same beats (station stairs, backwards down her stairs, brace round the ankle, the wedding, the cousin, the strap, "walk down the stairs", the mechanism, proof, the town walk, the queue, the husband, the three friends, the offer, the sister) now staged as scenes with dialogue, British register ("love", "Mum", "tannoy", "garden centre", "physiotherapy"). New: four cold-open hooks (A station stairs, B lift queue, C dead escalator, E the floor), the husband as a character, the sister's "one level" Sundays planted in SC03 and paid in SC13, the café reveal. Voice fingerprint: short declaratives, fragments in threes ("Physiotherapy. Painkillers. Cortisone injections."; "Nothing worked. Nothing lasted. Nothing gave me my life back."), understatement ("I know."). Spoken verbatim (§22U).

### Part 5 — surfaced, not absorbed

| Inspo element | Disposition |
|---|---|
| Lipstick product, beauty macro on lips | replaced by the strap (§9), its reveal an insert inside a scene (§24G) |
| Narrator to the lens for the offer | not in our script (EG05, F12) |
| 71 Stairs CGI knee / comparison card | not in our script — the mechanism is Barbara's dialogue (SC08). A §24G **MODEL/SCREEN** route is available if you want the knee shown (F11) |
| "Amazon", "Shopify" | voiced verbatim (§22U), never pictured (§10A) — F5 |

### Part 6 — beat-it plan

| Inspo weakness | Our delta | Where |
|---|---|---|
| 360×640 source, soft, TV-flat in the kitchen scenes | prestige-series package, `PROD-DEPTH` layers, motivated low-key light (§24N) | every shot |
| The friend explains, the viewer never sees it work | SC07 shows it: first step down **forwards**, hands off the banister — the mirror of SC02's backwards descent | SC02 ↔ SC07 |
| One hook | four cold opens, each a different story day, one body | HK A/B/C/E |
| Offer as a pitch to camera | offer planted in the story; the loop paid by the sister on the stairs (SC03 plant → SC13 payoff) | SC13 |

### Part 7 — confirmation

Conflicts are listed in **Flags**. **Confirm or correct the absorption along with the avatars.**

---

## 1b. Film Look Sheet (§24G) — written by the agent, shown for information

| # | Field | Value |
|---|---|---|
| 1 | Genre and reference | British family drama shot like a prestige streaming series (§24N house base) — ordinary semi-detached house, a railway station, a wedding, a high-street café; warm and restrained |
| 2 | Camera and glass | **ARRI Alexa Mini LF, large format · ARRI Signature Prime (spherical) · ARRI colour science** · 24 fps, 180° shutter. Focal by scale: WIDE 24–32 · FULL 32–40 · MED 40–50 · MCU 50–65 · CU 75–85 · INSERT 100 macro; stop T4–T5.6 wides → T1.8–T2 CU. Shallow from MCU in; one focus pull per clip at most, on a named cue (§30J) |
| 3 | Light | Motivated, soft key from windows and practicals, **4:1 on faces in the Before/Problem, 2:1–3:1 in the After**; practicals in frame. Arc: BF/PB dusk and night — cool 6500K window ambience + one 2800K tungsten lamp; TN overcast daylight 6500K; AF warm low sun 4300–5600K; OC late-afternoon sun |
| 4 | Palette | sage, navy, oatmeal, brick, cool blue-grey (Before) → honey, cream, soft green, warm white (After); HER's wardrobe moves from greys/greens to warmer colours by act (§14A at step 5) |
| 5 | Grade (the edit only) | slight warm lift (+0.02), gentle S (1.10), sat 0.94, teal-blue shadow tint (205°, 0.04), amber highlight tint (38°, 0.03), black lift 0.025, white point 0.97, skin protect 0.75 → `edit/grade.json` → **`edit/LUT-HALFMYAGE.cube` — `lut.py check` PASS** (skin hue ≤ 3.9°, sat −3…+9%) |
| 6 | Optical texture | soft highlight roll-off, faint warm halation around bulbs and bright windows, clean glass with gentle edge fall-off; no haze, no flare |
| 7 | Motion | Seedance move library (§24N): F2 locked for dialogue, F1 slow push-in on the turn lines, F6 pull-back reveal for the hooks' payoff, F9 lateral track on the town walk; one move per shot; mean shot ~4.5s (inspo) |
| 8 | Performance | Restrained (§28B); understatement; the husband's "too quickly", HER's "Fine, love" played as covering; Barbara bright and certain |
| 9 | Sound and post | dialogue only in every clip (`NEG-SOUND`, no BGM, V7.73.3); room tone per location; SFX list (doorbell, tannoy, drawer, carriage doors); **music theme**: sparse piano and cello, 70–84 bpm, a four-note rising motif; sparse in the Problem, the theme at the Turn (SC07), full in the After; grain in the edit (Mode 4) |

**`LOOK-HALFMYAGE`** (verbatim on every Mode 4 frame — `cast/LOOK.txt`):
```
THE LOOK OF THIS FILM: A British family drama shot like a prestige streaming series — an ordinary semi-detached house, a railway station, a wedding and a high-street café, watched with warmth and restraint. Lived-in domestic colour: cool blue-grey dusk and night in the rooms of the Before, lit by warm tungsten lamps; muted sage, navy, oatmeal and brick; warming to honeyed daylight, soft greens and cream in the After. Highlights roll off softly with a faint warm halation around bulbs and bright windows; clean modern glass with a gentle fall-off toward the frame edges. Captured with natural, neutral colour and a gentle contrast, ungraded — the grade is added later in the edit. Every frame of this film shares exactly this look.
```

---

## 2. Script, product, claims, locks (step 2)

### Visual Instruction Ledger (§27F) — opened (every row → a beat at step 5)

| ID | Anchored to | Instruction (verbatim) | Status |
|---|---|---|---|
| VN01 | L001 Daughter | at the top of the steps, reaching for the rail | open → step 5 |
| VN02 | L002 Her | already three steps down, shopping bag in hand | open |
| VN03 | L003 Daughter | in the carriage, catching her breath, staring at her | open |
| VN04 | L005 Daughter | loaded with shopping bags, nodding at the lift | open |
| VN05 | L006 Her | already three steps up, a full bag in each hand | open |
| VN06 | L007 Daughter | reaching the top, out of breath | open |
| VN07 | L009 Tannoy | off | open (SFX/voice off-screen) |
| VN08 | L010 Commuter | 20s, groaning at his phone | open (one-off cast) |
| VN09 | L011 Her | passing him, first onto the steps | open |
| VN10 | L012 Daughter | at the bottom | open |
| VN11 | L014 Daughter | entering, reflex | open — **F8** (Hook E's action is unwritten) |
| VN12 | L016 VO | variant | open (Hook E's own VO line) |
| VN13 | L017 Her | calling down from the landing | open |
| VN14 | L018 Husband | off, too quickly | open |
| VN15 | L024 VO | on the drawer closing | open |
| VN16 | L025 Husband | from the doorway, soft, watching her drop the brace in | open |
| VN17 | L027 Sister | voice on the phone | open |
| VN18 | L031 Her | low, not taking her eyes off Barbara | open |
| VN19 | L038 Barbara | laying a second, boxed strap on the table | open (package_open.jpg) |
| VN20 | L047 Barbara | two fingers below her own kneecap | open (FP03 placement) |
| VN21 | L055 Cashier | reaching for the bags | open (one-off cast) |
| VN22 | L065 Her | pulling the trouser leg up an inch | open — **F10** (FP13) |
| VN23 | L071 VO | cut to the front door ON the doorbell; the VO line announces the jump, no card | open (SFX doorbell, no time card) |
| VN24 | L072 Sister | at the door, eyes going past her to the staircase | open |
| VN25 | L074 VO | as the sister puts her hand on the rail and takes the first step | open |
| VN26 | HOOK B heading | "(up, with the shopping)" | open |

### Phrase inventory (§27B) — dispositions `SH` (acted in a shot) / `VO` (narration over shots) / `off` (voice off-screen); beats assigned at step 5

