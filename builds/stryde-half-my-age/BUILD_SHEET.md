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

| ID | Act · scene | Speaker | Line (verbatim) | Disp. | Claim | Visual note |
|---|---|---|---|---|---|---|
| L001 | HKA · HKA | DAUGHTER | Mum… the next one’s in ten minutes, we can… | SH | — | VN01 |
| L002 | HKA · HKA | HER | Not waiting ten minutes, love. | SH | — | VN02 |
| L003 | HKA · HKA | DAUGHTER | When did that happen? | SH | — | VN03 |
| L004 | HKA · HKA | VO | I’m 71 and I take the stairs faster than women half my age. Six weeks ago, I couldn’t. | VO | — |  |
| L005 | HKB · HKB | DAUGHTER | Mum, the lift’s just there. | SH | — | VN04 |
| L006 | HKB · HKB | HER | So are the stairs. | SH | — | VN05 |
| L007 | HKB · HKB | DAUGHTER | When did that happen? | SH | — | VN06 |
| L008 | HKB · HKB | VO | I’m 71 and I take the stairs faster than women half my age. Six weeks ago, I couldn’t. | VO | — |  |
| L009 | HKC · HKC | TANNOY | ...the escalator is out of service. Please use the stairs. | off | — | VN07 |
| L010 | HKC · HKC | COMMUTER | You’re joking. | SH | — | VN08 |
| L011 | HKC · HKC | HER | It’s only stairs, love. | SH | — | VN09 |
| L012 | HKC · HKC | DAUGHTER | When did that happen? | SH | — | VN10 |
| L013 | HKC · HKC | VO | I’m 71 and I take the stairs faster than women half my age. Six weeks ago, I couldn’t. | VO | — |  |
| L014 | HKE · HKE | DAUGHTER | Mum, wait, I’ll give you a… | SH | — | VN11 |
| L015 | HKE · HKE | DAUGHTER | ...When did that happen? | SH | — |  |
| L016 | HKE · HKE | VO | I’m 71. Six weeks ago I couldn’t get up off my own floor. | VO | — | VN12 |
| L017 | BF · SC02 | HER | Just leave it by the stairs, love. I’ll get it later. | SH | — | VN13 |
| L018 | BF · SC02 | HUSBAND | I’ll bring it up. | off | — | VN14 |
| L019 | BF · SC02 | VO | Six weeks ago, I was going down my stairs backwards. One step at a time. | VO | — |  |
| L020 | BF · SC02 | HUSBAND | Sleep alright? | SH | — |  |
| L021 | BF · SC02 | HER | Fine, love. | SH | — |  |
| L022 | BF · SC02 | VO | If I’m being honest, some days I wasn’t going down them at all. I’d just stay upstairs. | VO | — |  |
| L023 | PB · SC03 | VO | The full knee brace I bought slipped down my leg. By evening, it was around my ankle. I tried everything. Physiotherapy. Painkillers. Cortisone injections. Every brace and sleeve on the market. | VO | — |  |
| L024 | PB · SC03 | VO | Nothing worked. Nothing lasted. Nothing gave me my life back. | VO | — | VN15 |
| L025 | PB · SC03 | HUSBAND | That drawer won’t shut soon. | SH | — | VN16 |
| L026 | PB · SC03 | HER | It shuts. | SH | — |  |
| L027 | PB · SC03 | SISTER | Sunday… shall we just do the garden centre? It’s all one level. | off | — | VN17 |
| L028 | PB · SC03 | HER | Course, love. Easier. | SH | — |  |
| L029 | PB · SC03 | VO | My sister’s knees are worse than mine. We planned our Sundays around one level. | VO | — |  |
| L030 | TN · SC04 | VO | Then my granddaughter got married in June. My cousin Barbara was there. She’s 74. And she was on the dance floor all night. | VO | — |  |
| L031 | TN · SC04 | HER | Her knees were worse than mine. Both of them. Bone on bone. | SH | held (bone on bone) | VN18 |
| L032 | TN · SC04 | HUSBAND | Whose? | SH | — |  |
| L033 | TN · SC04 | HER | Barbara’s. | SH | — |  |
| L034 | TN · SC04 | VO | I always assumed hers weren’t as bad as mine. I always assumed mine were past the point of fixing. | VO | — |  |
| L035 | TN · SC05 | VO | Barbara came to stay the week after. She watched me work through my morning routine. | VO | — |  |
| L036 | TN · SC05 | BARBARA | Can I show you something? | SH | — |  |
| L037 | TN · SC05 | VO | A small black strap. Just below her kneecap. | VO | — |  |
| L038 | TN · SC05 | BARBARA | They come in twos. I never used the spare. | SH | — | VN19 |
| L039 | TN · SC06 | VO | It looked absurd. Too small. | VO | — |  |
| L040 | TN · SC06 | HER | Barbara. This can’t possibly work on knees like mine. | SH | — |  |
| L041 | TN · SC06 | BARBARA | Just put it on and walk down the stairs. | SH | — |  |
| L042 | TN · SC07 | VO | The first step, I didn’t have to hold the banister. | VO | — |  |
| L043 | TN · SC07 | VO | Not the second. Not the third. | VO | — |  |
| L044 | TN · SC07 | VO | All the way down. Both feet. Forwards. | VO | — |  |
| L045 | TN · SC07 | VO | First step. Pain gone. Like a switch. | VO | **outcome (F4)** |  |
| L046 | TN · SC08 | BARBARA | Everything you’ve tried was designed to make you comfortable while your knee got worse. This one fixes why it hurts. | SH | **comparative / outcome (F2)** |  |
| L047 | TN · SC08 | BARBARA | There’s one spot below the kneecap where every step lands. Every brace, every injection, every pill you’ve ever taken treated the whole knee. Not that spot. | SH | held (the spot) · **comparative (F2)** | VN20 |
| L048 | TN · SC08 | BARBARA | That’s why nothing worked. The pain is pressure. Nothing more. | SH | **comparative (F2)** |  |
| L049 | TN · SC08 | BARBARA | This sits on that spot and lifts the weight off. | SH | protection ✓ |  |
| L050 | AF · SC09 | VO | Over 200,000 people wear one now. Sports doctors recommend it. Not the pharma companies. Sports doctors. | VO | held (200,000) · **sports doctors / pharma (F1)** |  |
| L051 | AF · SC09 | VO | Barbara’s husband wears one. He’s 76. He plays golf twice a week. Her niece wears one for tennis. She’s 22. | VO | — |  |
| L052 | AF · SC10 | VO | I’ve worn mine every day for six weeks. Under my clothes. Nobody knows it’s there. No pills. No gel. No brace around my ankle by lunchtime. | VO | — |  |
| L053 | AF · SC10 | VO | Yesterday I walked into town. Two miles there. Two miles back. I outwalked three women half my age. | VO | implied (F7) |  |
| L054 | AF · SC10 | VO | I stood in line for ten minutes without shifting my weight. | VO | — |  |
| L055 | AF · SC10 | CASHIER | You alright carrying those, love? | SH | — | VN21 |
| L056 | AF · SC10 | HER | I am, actually. | SH | — |  |
| L057 | AF · SC10 | VO | I carried two bags home. Nobody helped me. | VO | — |  |
| L058 | AF · SC11 | HUSBAND | You were gone a long time. | SH | — |  |
| L059 | AF · SC11 | HER | I know. | SH | — |  |
| L060 | AF · SC12 | VO | That was six weeks of wearing the strap. Nothing else. | VO | — |  |
| L061 | AF · SC12 | VO | I’m not the one everyone waits for anymore. | VO | — |  |
| L062 | AF · SC12 | FRIEND 1 | Right. What’s changed? And don’t say a haircut. | SH | — |  |
| L063 | AF · SC12 | HER | Three weeks ago I couldn’t have crossed this room like that. | SH | **timeline (F9)** |  |
| L064 | AF · SC12 | FRIEND 2 | So what is it? | SH | — |  |
| L065 | AF · SC12 | HER | It’s a strap. | SH | — | VN22 |
| L066 | AF · SC12 | FRIEND 1 | That little thing? | SH | — |  |
| L067 | AF · SC12 | HER | That’s what I said. | SH | — |  |
| L068 | AF · SC12 | VO | So I’m just going to say it here. It’s called Stryde. Patellar Force Redirection. It’s been designed for three years with orthopaedic surgeons. It’s the real thing. Not the cheap knockoffs they sell on Amazon and fake Shopify sites. | VO | name (F3) · held (3 yrs, surgeons) · **Amazon, Shopify (F5)** |  |
| L069 | OC · SC13 | VO | The link’s below. Two straps for the price of one right now. 60 days to send them back if they don’t work. | VO | held (BOGOF, 60 days) |  |
| L070 | OC · SC13 | VO | Eleven years of knee pain. Gone the first step I took with it on. | VO | **outcome (F4)** |  |
| L071 | OC · SC13 | VO | I bought a second pair for my sister the same week. She’s coming Sunday. | VO | — | VN23 |
| L072 | OC · SC13 | SISTER | All the way up? | SH | — | VN24 |
| L073 | OC · SC13 | HER | All the way up. | SH | — |  |
| L074 | OC · SC13 | VO | She’ll walk up my stairs on her own. | VO | — | VN25 |

Coverage: 4 hooks (20 lines) + body 54 lines · **uncovered 0 · blocked 0** (beats at step 5).

### Claims (§43A)

Held in the Product Sheet register (V7.49.29): bone on bone · the spot below the kneecap · 200,000+ wearers · three years with orthopaedic surgeons · Buy 1 Get 1 Free · 60-day money-back guarantee · protection mechanism. Numbers are edit overlays, never generated (§17). **Not in the register: F1, F2, F4, F7** — voiced verbatim (§22U), listed in Flags. Nothing blocked (same lines the 71 Stairs builds ran with).

### Mode & Model Lock (§18A)

| Beat class | Model · params | Why |
|---|---|---|
| Mode | **Mode 4 Realistic Film**, 9:16, `LOOK-HALFMYAGE` | user MODE 4; AI Drama VSL (§3B) |
| Avatar sheets | `gpt_image_2_5` · `sunburst` · `high` · `2k` · 9:16 | §19 / V7.72.0 (**used this delivery**) |
| Location & property plates | Sunburst, **16:9** | V7.68.1 |
| Info cards (the strap under the kneecap, the boxed spare, the drawer of braces…) | Sunburst | V7.72.0 |
| Anatomy / mechanism (only if F11 adds a MODEL/SCREEN beat) | `nano_banana_pro` | V7.72.0 |
| Video — every shot, hooks included | **Seedance 2.5 on Kie AI** (`kie.py seedance`), 720p, 9:16, ingredients mode — sheets, voice masters, plates, product photos, info cards; **no master/start frames** (V7.68.0); `SERIES-LOOK`, `NEG-SOUND`, silent when no dialogue | §4, §24N, V7.73.3 |
| Voice | **§24I film voice master per speaking character** (Seedance, untrimmed); the narration (VO) cast to HER's master (§3B, §22D bookend) | §18B voice route for Mode 4 / AI Drama |
| Music / tone / SFX | ElevenLabs `eleven_music_v2` / `eleven_text_to_sound_v2`, `music.py`, `mix_scene.py` | §24M |
| Edit | CapCut desktop; `LUT-HALFMYAGE.cube` + grain; **no trimming** (§24L) | §40 |

**Other locks:** side — **not stated in the script** → the **right knee** by default (the house `SIDE_RULE`; F6); mechanism claim **protection**; edit `EDIT-HALFMYAGE`; hooks **4 → 4 films** (HK A/B/C/E + the identical body); `kind: film`, no talking heads, no VO trim.

---

## 3. Cast (step 3) — generated, on the board for your check

Everyone with two or more beats gets a sheet. **Seven:** HER (narrator/protagonist), Barbara, the daughter (all four hooks), the husband, the sister (phone + door), Friend 1 and Friend 2 (the café, several shots each). One-offs cast at step 5 (§13): the commuter, the tannoy voice, the cashier, the granddaughter (bride) and wedding guests, Barbara's husband (golf), her niece (tennis), the three women she outwalks.

| Sheet | Job | File | Board |
|---|---|---|---|
| N-HER | `30fd2bc8-17e3-4e27-b2cf-8225e00b088c` | `cast/N-HER_v1.png` | To check |
| C1-BARBARA | `715eb066-8dce-4343-98b0-c38d0dcd6600` | `cast/C1-BARBARA_v1.png` | To check |
| C2-DAUGHTER | `c936500d-9947-44da-9950-cc6e16fe056a` | `cast/C2-DAUGHTER_v1.png` | To check |
| C3-HUSBAND | `98c11aee-5f7f-4244-a68e-d649856acf2d` | `cast/C3-HUSBAND_v1.png` | To check |
| C4-SISTER | `582d3d80-d3cb-4894-a867-a281436ed90a` | `cast/C4-SISTER_v1.png` | To check |
| C5-FRIEND1 | v1 `eaae20f9-0e81-40c7-986f-7f483d82db83` (Old) · **v2 `18040ee9-baea-4511-a622-6554decdb9e9`** | `cast/C5-FRIEND1_v2.png` | To check (v2) |
| C6-FRIEND2 | `f310a25a-423f-401b-9a45-21a8173a3127` | `cast/C6-FRIEND2_v1.png` | To check |

Manual run: **not checked by me** (§18B step 3) — Confirm or Fix each on the board. Prompts `cast/<ID>.prompt.txt` (9,375–9,636 chars), built from Appendix A by ID in `cast/build_sheets.py`: `CAM-FILM` (Alexa Mini LF + Signature Prime 50mm T4, tripod) → `AVATAR-SHEET` + `SHEET-GRID` → `SKIN-T` → `LOOK-HALFMYAGE` → `CAP-FILM` → `NEG-SHEET` + `NEG-GRID` + `NEG-FILM` (lens clause dropped — the close-up looks at the lens) + `NEG-DEFAULT-FACE`. Spend: 7 Sunburst jobs, one render each (Higgsfield 12,735.65 before).

### Identity strings — read off the renders (§7)

| ID | Identity string |
|---|---|
| N | white English woman, 71, small and slight, narrow-shouldered; long oval face, high-bridged nose, pale blue-grey eyes under hooded lids, wide thin mouth, deep lines from nose to mouth, loose neck; steel-grey blunt chin-length bob with a heavy straight fringe; heather-green crew-neck jumper, charcoal A-line skirt above the knee, black low-heeled shoes |
| C1 | white English woman, 74, tall, big-boned, broad shoulders, sturdy legs; broad square face, dark brown eyes, strong straight brows, wide mouth; short white hair cropped at the sides, tousled on top; cobalt-blue quilted gilet over a white long-sleeve top, **navy knee-length shorts** (rendered as shorts, not culottes), white leather trainers |
| C2 | white English woman, mid-40s, medium height, sturdy; oval face, straight nose, grey-blue eyes, straight mouth; dark brown hair in a loose low bun with strands at the temples; small dark mole left of the upper lip; olive hooded parka open over a cream cable-knit jumper, dark indigo jeans, tan ankle boots |
| C3 | white English man, mid-70s, medium height, round-shouldered, soft paunch; broad heavy face, jowls, pale blue eyes under thick grey-white brows, large nose; grey hair swept back, **thinning and receding** (fuller in the prompt), short grey-white beard; brown V-neck cardigan over a blue-and-white checked shirt, grey trousers, brown slippers |
| C4 | white English woman, late 60s, short and heavy, wide waist; round soft face, rosy cheeks, hazel eyes, short upturned nose, double chin, a mole on the left cheek; short strawberry-blonde permed curls; lilac zip fleece over a navy floral blouse, navy trousers, beige walking shoes |
| C5 | **v2 (Fix: "I WANT A NEW ONE HERE")** white Irish woman, 69, tall, lean, wiry; long narrow angular face, sharp cheekbones, pale green eyes, freckles; hennaed copper-red short layered hair; navy pea coat over a red-and-cream Breton top, charcoal trousers, tan brogues — identity string to be re-read off the render once confirmed. (v1, British Indian woman with a silver plait, moved to Old) |
| C6 | Black British woman (Jamaican heritage), 72, short and full-figured; round full face, dark brown eyes, broad nose, full mouth, small raised dark mole under the left eye; short salt-and-pepper rounded afro; mustard corduroy jacket over a black polo-neck, dark green wide-leg trousers, burgundy loafers |

### §19A axis tables

| Axis | N | C1 Barbara | C2 Daughter | C3 Husband | C4 Sister | C5 Friend 1 | C6 Friend 2 |
|---|---|---|---|---|---|---|---|
| Face | long oval, beaked nose | broad square | oval, mother's nose | broad, jowled | round, rosy | long oval, arched brows | round, full cheeks |
| Hair | steel-grey bob + fringe | white crop, spiky top | dark brown bun | grey swept back, beard | strawberry-blonde perm | silver plait | salt-and-pepper afro |
| Age | 71 | 74 | ~46 | ~74 | ~68 | 70 | 72 |
| Build | small, slight | tall, big-boned | medium, sturdy | medium, paunch | short, heavy | tall, slim | short, full |
| Wardrobe key | green / charcoal | cobalt / navy | olive / cream | brown / check | lilac / navy | rust / teal | mustard / black |
| Marker | mole on right jaw | scar across the nose bridge | mole above the lip | scar on the chin | mole on left cheekbone | mole by right eye | mole under left eye |
| Voice | Northern English (below) | bright, certain | quick, warm | gruff, soft | soft, Midlands | crisp, dry | warm, London |

**Clearance:** every pair differs on ≥ 6 axes. ✓ Against the STRYDE roster (identity, lost-moments, 71-stairs, three-regrets, what-changed…): no repeat of a face architecture; the nearest are three-regrets' white British women in their 70s — different face, hair (none with a fringe bob), wardrobe and marker. N is deliberately far from the inspo's long silver-haired lead (`NEG-DEFAULT-FACE`).

### Voices (§22D) — for the §24I film voice masters, built after the maps (§18)

**`VOICE-HER`** (the narrator and HER's dialogue — VO cast to her master)
```
An English woman of seventy-one from the north of England, Lancashire, a light, dry, slightly reedy voice with a little gravel at the bottom of her range. Plain northern vowels, flat "a", unhurried and understated — she says the big things quietly and lets a line land without pushing it. A dry humour just under the surface. Statements fall at the end; never sing-song, never theatrical.
```

| Character | `VOICE-[CHAR]` (short form; full string at the voice stage) |
|---|---|
| Barbara | Englishwoman of 74, Midlands warmth with a bright, certain, slightly husky voice; quick, practical, amused — she has seen it work and isn't arguing |
| Daughter | Englishwoman of 46, northern, quick and warm, a little breathless in the hooks, concern hidden under teasing |
| Husband | Englishman of 74, northern, gruff and soft, few words, says kind things too quickly |
| Sister | Englishwoman of 68, northern, soft and careful, used to making the easier plan |
| Friend 1 | British Indian woman of 70, crisp southern English, dry and direct, a teasing edge |
| Friend 2 | Black British woman of 72, London with a Jamaican lilt, warm, curious, unhurried |
| One-offs (step 5) | Tannoy: flat station announcer · Commuter: 20s, southern, fed-up · Cashier: young, friendly, northern |

---

## Flags (decisions for the user — nothing below was changed silently)

| # | Where | Finding | Recommendation |
|---|---|---|---|
| **F1** | L050 | "Sports doctors recommend it. Not the pharma companies." — the register holds orthopaedic surgeons and sports scientists, not sports doctors; "not the pharma companies" is comparative | voiced as written; **please confirm the advertiser holds it** |
| **F2** | L046–L048 | "designed to make you comfortable while your knee got worse", "This one fixes why it hurts", "treated the whole knee… That's why nothing worked" — comparative / outcome, not in the register | voiced as written (the 71 Stairs lines); please confirm |
| F3 | L068 | Name "Stryde **Patellar Force Redirection**" — load-path wording; the locked claim is **protection** | voiced as written; pictured as protection |
| **F4** | L045, L070 | "First step. Pain gone. Like a switch." / "Gone the first step I took with it on." — outcome claims | voiced as written; please confirm |
| **F5** | L068 | "Amazon" and "Shopify" named (§10A) | voiced verbatim; never pictured; the knock-offs, if shown, are plain straps on a table (§10) |
| F6 | side | the script never says which knee | **right knee** throughout (`SIDE_RULE`) unless you say otherwise |
| F7 | L053 | "Two miles there. Two miles back." — implied outcome | voiced; no distance on screen |
| **F8** | Hook E | "The Floor" has only the daughter's two lines and the VO; **what HER does isn't written** | my read: HER is kneeling on the living-room floor (grandchild's toys / a dropped jigsaw), the daughter comes in reaching to help, and HER stands up unaided before the hand arrives — the mirror of "couldn't get up off my own floor". Confirm or give the action |
| **F9** | L063 | "**Three** weeks ago I couldn't have crossed this room like that." — the film's timeline is **six** weeks | voiced as written (§22U never changes a word); say if you want "Six" |
| **F10** | VN22 | "pulling the trouser leg up an inch" vs STRYDE fix pattern **FP13** (worn on screen: bare knee — shorts or a skirt, never trousers pushed up round the strap) | keep the script's gesture (trousers, lifted an inch — it's the "nobody knows it's there" reveal) and show the strap itself in the next insert on a bare knee from an earlier day (SC07). Or make her café outfit a skirt. Your call |
| F11 | mechanism | the script has no picture for SC08's mechanism (Barbara talks, two fingers under her kneecap) | kept in the scene (VN20); a §24G **MODEL** insert (the knee, the spot, the load lifting) can be added on request |
| F12 | close | the inspo closes with the narrator to the lens holding the product; our script plants the offer in the story | kept as written (no to-lens shot); say if you want the inspo's close |
| F13 | Hooks | A, B, C, **E** — there is no Hook D | 4 hooks → 4 films |
| F14 | length | 739 words at the inspo's 124 wpm + visual beats → **~5:05–5:40 per film** (inspo 5:22) | film pace, no trimming (§24L) |
| F15 | cast | C1 Barbara's culottes rendered as shorts; C3's hair rendered thinning | they're on the board for your check — Confirm keeps them; Fix regenerates |
| F16 | Drive | no Google Drive connector in this session → no `OUTPUT/` tree yet | every render is on the board; the tree is made when a Drive connector is available |

## Next — on your go (§18B step 5)

Confirm or Fix each avatar on the board and answer F1, F2, F4, F8, F9, F10 (and anything else). Then steps 4–5 as one delivery: the Property Sheet (her house — hallway and stairs, landing, kitchen, living room, front door) and plates (16:9), the station stairs + carriage, the shopping-centre lift + stairs, the escalator, Barbara's wedding venue, the high street + queue, the café, the garden-centre/phone locations; the scene list with Scene Bibles, act map + wardrobe map (story days), ingredient lists per shot, `angles.py` pass. Then the §24I voice masters, then the hooks one by one on Seedance.
