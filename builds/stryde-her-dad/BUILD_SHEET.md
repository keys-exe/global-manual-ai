# Build Sheet — stryde-her-dad

**STRYDE Precision Strap · "A - VID | AI Drama VSL | TOF | Discovery Story | New | Her Dad"** · Standards V7.91.3 · **RUN: MANUAL · MODE 4 Realistic Film · AI Drama VSL** · 2026-10-02

Steps 1–3 of §18. **Stopped at the avatar review (§18B, V7.62.0)**: steps 4–5 wait for your go.
Boards: Current https://claude.ai/artifact/Ki6d6eeXAgujWT1vAKTu8B · Old https://claude.ai/artifact/KnhxtqiFtKW7x4AJXdDtmQ · Final https://claude.ai/artifact/FTaYbfPdGNzgvtW7H5D3V9 · Plan https://claude.ai/artifact/GGfqqXJgZNEKzVmicQv5Ps

---

## 0. Intake (§18B)

| Input | Found | Notes |
|---|---|---|
| Drive folder | `1HiQYsCmreGmcdUU2a-HF0hmxW68gFfz8` — matches no existing build → new build | fetched with `fetch_drive.py` → `intake/` |
| Inspo | `inspo video` (no extension; MP4) → `intake/inspo.mp4` — the **Lymphoria AI drama** this script ports (the script's Ad Library link) | 407.4s · 9:16 · 360×640 · 30 fps · audio |
| Script | `Untitled document.docx`, title line 1 ✓ → `work/lines.json` (screenplay parse: `work/parse_script.py`) | **1 hook + 9 scenes · 61 spoken lines · 702 words (hook 43, body 659)** · 8 speakers · staging in THE STORY / CASTING |
| Product Sheet | `stryde_product_sheet_V7.49.32.py` — **older** than the repo's V7.49.38 | the repo's V7.49.38 is kept (`products/stryde/`) |
| Product images | 12; 11 byte-identical to `products/stryde/stryde_refs/`; **new: `831541848…_n.png`** — studio back view of the closed strap (grey grooved pad, chrome slides, band with two keepers) | kept in this build's `intake/` (adding it to `stryde_refs/` is an owner change — see BUILD_NOTES, For the owner) |
| Loom | none | — |
| Connectors (§5, step 0) | `work/connectors.md` | every job on its default route; talking heads (HeyGen API) and SFX via the ElevenLabs API are rung 2 — not used by a film except SFX; Drive via the public link |
| Higgsfield | one private workspace, Max plan, 5,869.65 credits before this delivery | the ODAQ B.V. workspace rule is for another account — not applied |

**Message fields:** `run manual` → **RUN: MANUAL**. No `MODE` line: the script declares the format — "An AI Drama VSL, **photoreal, like a short film**" — read as the §2 explicit instruction for **Mode 4 Realistic Film** (F0). `HOOKS` → **in script: 1** → **1 finished film** (F1). `VOICE` → derived per §22D (below). `CAP` → E0 default. `DIRECTIONS` → the script's own: British accents throughout, no narrator until the offer. `BUILD` → `stryde-her-dad`.

---

## 1. Absorption Sheet (§42)

### Part 1 — measured (`work/inspo_measure.json`, `work/inspo_transcript.json`)

| Instrument | Inspo (Lymphoria drama) | Settles |
|---|---|---|
| Duration / aspect | 407.4s · 9:16 | 9:16 locked; a ~7-minute film is the format |
| Scene cuts | **121 shots, mean 3.4s**; dialogue singles 1.5–4s, held reaction / establishing shots up to 13s | our film cuts at this rhythm |
| Silence (−40 dB) | 20 short gaps (0.3–1.6s), all inside dialogue | continuous sound bed; pauses live inside scenes |
| Words / pace | 711 words / 407s = **105 wpm** (dialogue + inner VO) | our 702 words at ~105 wpm ≈ **6:40**, plus the silent action beats (the van, the stairs, the three strides, the compost) → **~7:00–7:30** (F8) |
| Speech mix | dialogue lip-synced on screen (~80%); the hero's inner VO over his own close-ups (~15%); the wife's inner VO once; an off-screen narrator only for the offer (last ~30s) | §3B narrator rule — kept exactly (VN19) |
| Captions (read off the frames) | word-by-word, **bold lowercase white, the spoken word highlighted yellow**, centred at ~72% height, 2–4 words on screen, no box | EG01 |
| Shot frames + per-second sheets | `intake/frames/inspo/` (14 sheets, 121 shot frames) | Edit Grammar below |

### Part 2 — structure map (inspo → our script — a line-for-line port)

| t (inspo) | §3B act | Inspo shows | Our scene |
|---|---|---|---|
| 0–26 | **HK — cold open** | night street: a man smacks the wife; the husband doubled over out of breath; "How am I supposed to feel safe with you?" — his inner VO "I'm too fat to protect the woman I love" | **SC01 the van** — the car park, the van reversing, the lad pulls Sue clear, "Is your dad alright?", Tony's inner VO |
| 26–51 | BF | her inner VO, then the truck cab two-hander: "Are we gonna talk about it?"… "I'm gonna fix it." | **SC02 the car** — the same exchange, line for line |
| 58–70 | PB | bathroom mirror, shirtless; inner VO "I used to be the guy…" | **SC03 rock bottom** — down his own stairs sideways, the drawer of braces, waiting in the car while she loads the boot |
| 72–92 | PB | doctor's room, OTS pair: "everything's in range… very normal" / "That's not normal" | **SC04 the GP** — the same beats |
| 108–248 | TN | gym locker room, the mentor (same age, was bigger): the soft-or-hard question, the mechanism, the product named, "don't grab whatever pops up online", "I said the same" | **SC05 Gary at the builders' yard** — "all round or one spot?", "press there", 17× bodyweight, the strap named, "don't buy the cheap ones off Amazon" |
| 257–265 | TN | kitchen: "What is that?" / "You've said that before." / "Then don't watch." | **SC06 Sue finds the strap** |
| 265–320 | AF | the change noticed by others ("Looking good lately?"), "That was the first time I felt it", the wife finds him — "the man looking back at me was someone I used to know" | **SC07** stairs forwards, labourer, neighbour · **SC08** the garden, the new patio |
| 323–378 | AF — the mirror | the same gas station at night: the same lads; this time he steps in and protects her; walking off hand in hand | **SC09 the same car park** — the car pulls out, three strides, "You alright, sir?" "She's fine. Thanks, love.", 25 kg of compost, the kiss |
| 378–407 | OC | narrator over product macro, ingredients, product on the counter with the man behind; offer + guarantee + "if the link's still there" | **SC10** narrator over the strap, the stairs, the patio and the pack |

### Part 3 — Style Lock (copied)

- **Format:** AI Drama VSL — fully acted dialogue scenes; the hero's inner thought as VO over his own face; no presenter; an unseen narrator only in the offer.
- **Visual grammar:** prestige-drama coverage in 9:16 — tight singles and CUs on faces (most of the film), dirty OTS pairs in the two-handers, a few wides to place a scene, inserts for props; faces off-lens; shallow from MCU in.
- **Light and colour arc (read off the frames):** the hook and the car at night, cool with sodium/neon practicals; the doctor and the mentor scene in cool overcast/fluorescent; the After warming to golden sunlight; the mirror scene back at night but now protective. Ours moves the hook to **daytime** (the script's garden centre, F12) and keeps the arc by light quality: grey overcast → cool evening tungsten at home → honeyed low sun in the After → the mirror car park in warm late-afternoon sun.
- **Rhythm:** mean shot 3.4s; dialogue lines 1.5–4s per shot; reactions held on the turn; a new scene every 20–60s.
- **Tone of voice:** plain and blunt, short lines, lines left hanging ("I'm her husband."); British in ours (VN19).

### Part 3A — Edit Grammar → `EDIT-HERDAD`

| ID | Device (inspo) | Where | Our build |
|---|---|---|---|
| EG01 | **word-by-word captions**: bold lowercase white, the spoken word in yellow, 2–4 words, centred at ~72% height, no box | whole film | **kept** (CapCut) |
| EG02 | **full-frame shots only** — no split, no picture-in-picture | whole film | **kept** (every row `full`) |
| EG03 | **hard cuts** only; no transitions, no speed ramps | whole film | kept (§24L: no trimming, no speed change in Mode 4) |
| EG04 | **tears and tight CUs on the turn** — the camera goes to the hero's face for his inner VO | HK, PB | kept: Tony's inner-VO lines play over his own CU (SC01, SC03) |
| EG05 | **product hero macros** in the offer (bottle, dropper), the product on the counter with the hero soft behind | OC | kept as the strap's hero insert and the pack (two straps, BOGOF) with Tony soft behind (§24G `HERO-FILM`) |
| EG06 | **mirror scene** — same location, same lads, same framing, opposite outcome | AF | kept: the same car park, the same lad, the same axis (VN04, VN05, §3B) |
| EG07 | low music bed under scenes — **not measured** (no stem); the offer has a warmer bed | whole film | music added in the edit only (§24M / §40A register map at step 5; never generated in a clip, V7.73.3) |
| Light | night/overcast cool → golden After → warm mirror | by act | §30K arc (Look Sheet field 3) |
| Focus | shallow from MCU in, deep on wides; no rack focus seen | — | §30J |
| Angles | eye-level singles and OTS, low angle on the men in the hook, a high wide on the doubled-over husband | — | range copied at step 5 (`angles.py`) |

### Part 4 — script absorption

The script is **the Lymphoria drama rewritten line for line for STRYDE and Britain**: the safety failure in front of a younger man → the car talk → the mirror and the doctor → the mentor and the one-question diagnosis → the doubt ("You've said that before." "Then don't watch.") → the change noticed by others → the mirror scene → the narrator's offer. New against the inspo: the "your dad" humiliation (stronger than the inspo's, and the title), a physical failure (the knee gives out on the first step), the trade (thirty years laying patios) paid off by him laying their own patio, the strap's spot found by touch ("Press there… Two fingers down."). Voice fingerprint: short declaratives, threes ("The physio. The tablets. … a drawer full of braces."), understatement, British register ("Give over", "decent nick", "Come off it", "Tone", "love"). Spoken verbatim (§22U).

**Story spine (§24I part 9):** want — to be her husband, not her dad · stakes — her safety, his place beside her · obstacle — the knee · failed fixes — physio, tablets, braces, the GP's "very normal" · turn — Gary's one spot · payoff — the same car park, three strides; plants — the lad (SC01 → SC09), the car park (SC01 → SC09), "Thanks, love" (Sue SC01 → Tony SC09), the patios (SC03 → SC08), "I'll sort it" (SC02 → SC07).

### Part 5 — surfaced, not absorbed

| Inspo element | Disposition |
|---|---|
| A man smacks the wife (assault in the hook) | replaced by the script's van (an accident, no assailant) |
| Shirtless mirror body-shame scene | not in our script — SC03 is the stairs, the drawer and the car |
| Herbal dropper, ingredient macros, "third party tested" | replaced by the strap (§9), its reveal inside SC05 and the hero insert in SC10 |
| On-screen product label / brand name on the pack | our pack shows only the lowercase stryde wordmark on the lid (PACKAGE-LOCK); offer text added in the edit (§17) |
| US gas station, US pick-up | British garden-centre car park, a plain van and a plain hatchback, no badges, no readable plates (§10A) |

### Part 6 — beat-it plan

| Inspo weakness | Our delta | Where |
|---|---|---|
| 360×640 source, soft, heavy-handed tears | prestige-series package, `PROD-DEPTH` layers, restrained acting (§24I) | every shot |
| The mentor only explains | Tony **finds the spot himself** under Gary's two fingers — the viewer feels it | SC05 |
| The change told by others only | **shown**: forwards down his own stairs (the mirror of SC03's sideways descent), then on his knees laying the patio | SC03 ↔ SC07, SC08 |
| One hook | one hook as written (F1) — two more cold opens can be written on request at step 6 | SC01 |

### Part 7 — confirmation

Conflicts are listed in **Flags**. **Confirm or correct the absorption along with the avatars.**

---

## 1b. Film Look Sheet (§24G) — written by the agent, shown for information

| # | Field | Value |
|---|---|---|
| 1 | Genre and reference | British working-class family drama shot like a prestige streaming series (§24N house base) — a garden-centre car park, a terraced house with a steep narrow staircase, a GP's room, a builders' yard, a back garden; warm and restrained |
| 2 | Camera and glass | **ARRI Alexa Mini LF, large format · ARRI Signature Prime (spherical) · ARRI colour science** · 24 fps, 180° shutter. Focal by scale: WIDE 24–32 · FULL 32–40 · MED 40–50 · MCU 50–65 · CU 75–85 · INSERT 100 macro; stop T4–T5.6 wides → T1.8–T2 CU. Shallow from MCU in; one focus pull per clip at most, on a named cue (§30J) |
| 3 | Light | Motivated, soft key from sky, windows and practicals. **HK/BF: flat grey overcast 6500K**, shadows soft, the car interior lit by the grey sky through the windscreen · **PB: cool evening at home** — 6500K window dusk + one 2800K tungsten lamp, 4:1 on faces; the GP room cool 4000K overhead + window · **TN: the yard under bright overcast 6500K**, the kitchen at night under a warm pendant · **AF: low honeyed sun 4300–5000K**, 2:1–3:1 on faces · **SC09 mirror: warm late-afternoon sun**, the same car park and axis as SC01 |
| 4 | Palette | slate grey, wet tarmac, red brick, navy and khaki workwear, plant-centre greens (Before) → honey, sandstone, fresh green, warm white (After); Tony's wardrobe moves from navy/grey to warmer colours by story day (§14A at step 5) |
| 5 | Grade (the edit only) | warmth +0.01, contrast 1.12, sat 0.90, teal shadow tint (200°, 0.05), amber highlight tint (40°, 0.025), black lift 0.02, white point 0.97, skin protect 0.75 → `edit/grade.json` → **`edit/LUT-HERDAD.cube` — `lut.py check` PASS** (skin hue ≤ 4.2°, sat −7…+8%) |
| 6 | Optical texture | soft highlight roll-off, faint warm halation around bulbs and bright windows, clean glass with gentle edge fall-off; no haze, no flare |
| 7 | Motion | Seedance move library (§24N): F2 locked for dialogue, F1 slow push-in on the turn lines (Tony's inner VO), F5 follow for the lad's sprint and Tony's three strides, F6 pull-back reveal on the patio, F9 lateral track on the street walk; one move per shot; takes for connected action (§24K part 5) |
| 8 | Performance | Restrained (§28B): Tony covers with gruffness, Sue's anger is fear, Gary amused and certain, the lad kind and quick; no generated-acting tells (`NEG-DRAMA`) |
| 9 | Sound and post | dialogue only in every clip (`NEG-SOUND`, no BGM, V7.73.3); room tone per location; SFX list (van reversing beeper, pot smashing, car door, slabs, compost bag); **music** by the §40A register map at step 5 — investigation before the strap's first frame (never sad), the change on it; grain in the edit (Mode 4) |

**`LOOK-HERDAD`** (verbatim on every Mode 4 frame — `cast/LOOK.txt`):
```
THE LOOK OF THIS FILM: A British working-class family drama shot like a prestige streaming series — a garden-centre car park, a terraced house with a steep narrow staircase, a GP's consulting room, a builders' yard and a back garden, watched with warmth and restraint. Overcast English daylight and lived-in colour: slate-grey skies, wet tarmac, red brick, khaki and navy workwear and the greens of garden-centre plants; the evenings at home cool blue-grey lit by warm tungsten lamps; warming to low honeyed sun, fresh greens and pale sandstone paving in the After. Highlights roll off softly with a faint warm halation around bulbs and bright windows; clean modern glass with a gentle fall-off toward the frame edges. Captured with natural, neutral colour and a gentle contrast, ungraded — the grade is added later in the edit. Every frame of this film shares exactly this look.
```

---

## 2. Script, product, claims, locks (step 2)

### Visual Instruction Ledger (§27F) — opened (every row → a beat at step 5)

The script's VISUALS line is "Editor's call. The script below is dialogue only; the story above is the staging." — so THE STORY and CASTING sections are its visual instructions.

| ID | Anchored to | Instruction (verbatim or closest) | Status |
|---|---|---|---|
| VN01 | whole build · Tony | "TONY, 64: his face looks his age (salt and pepper, strong builder's hands, broad shoulders), but he moves like a man of 85. Do NOT age his face." | applied at step 3 (C1); movement at step 5 |
| VN02 | whole build · Sue | "SUE, 52, looks 45 to 48: active, well kept, quick." | applied (C2) |
| VN03 | whole build · Gary | "GARY, 70, fit, lifts slabs on his own." | applied (C3); SC05 action at step 5 |
| VN04 | SC01 ↔ SC09 | "The same LAD in the hook and the payoff." | applied (C4) |
| VN05 | SC01 ↔ SC09 | "The same car park in the hook and the payoff." | open → one location plate, step 4 |
| VN06 | L001–L002 | "Sue is loading the boot when a van starts reversing towards her. Tony sees it from ten feet away and shouts, drops the potted plant he's holding, and his knee gives out on the first step. A young lad from the garden centre sprints past him and pulls Sue clear." | open → step 5 (F12) |
| VN07 | L003–L004 | "Then he asks her: 'Is your dad alright?' Sue doesn't correct him." | open |
| VN08 | SC02 | "Sue is shaken." · "She doesn't finish." · "Tony promises he'll sort it." | open |
| VN09 | SC03 · L016–L017 | "now he comes down his own stairs sideways" · "A drawer full of braces that never worked." | open |
| VN10 | SC05 · L023 | "At the builders' yard, Gary, 70, is lifting slabs on his own." | open |
| VN11 | L032–L033 | "He makes Tony press one spot under the kneecap: that's where it hurts." | open (FP03, FP21 placement) |
| VN12 | L044 | "Sue finds the strap" | open (one strap, FP19) |
| VN13 | L048–L050 | "He comes down the stairs forwards for the first time in two years, and doesn't tell her. A labourer and a neighbour notice." | open |
| VN14 | L052–L053 | "Sue finds him on his knees in the garden, laying their new patio." | open |
| VN15 | L054–L056 | "Same car park, weeks later. A car pulls out fast towards Sue, and this time Tony gets to her in three strides. The same lad saw it." | open (F12) |
| VN16 | after L057 | "He swings a 25 kilo bag of compost into the boot." | open (plain bag, no print) |
| VN17 | end SC09 | "In the car, she kisses him." | open |
| VN18 | L058–L061 | "A narrator closes over the strap, the stairs, the patio and the pack" | open (pack = two straps, BOGOF) |
| VN19 | whole build | "Fully acted in dialogue, no narrator until the offer. The only voice-over is Tony's inner thought, plus Sue's once. British accents throughout." | applied (dispositions below, voices §22D) |
| VN20 | whole build | "Editor's call." (VISUALS) | the staging above + §30M Visual Pitch at step 5 |

### Phrase inventory (§27B) — dispositions `SH` (acted in a shot) / `VO` (inner thought or narration over shots); beats assigned at step 5

| ID | Act · scene | Speaker | Line (verbatim) | Disp. | Claim | Visual note |
|---|---|---|---|---|---|---|
| L001 | HK · SC01 | TONY | Sue! SUE! | SH | — | VN06 |
| L002 | HK · SC01 | LAD | You’re alright, you’re alright. I’ve got you. | SH | — | VN06 |
| L003 | HK · SC01 | LAD | Is your dad alright? He looked like he was going to go over. | SH | — | VN07 |
| L004 | HK · SC01 | SUE | He’s fine. Thanks, love. | SH | — | VN07 |
| L005 | HK · SC01 | TONY (VO, inner) | She didn’t correct him. I’m her husband. And I couldn’t get ten feet to my own wife. | VO | — |  |
| L006 | BF · SC02 | SUE (VO, inner) | He has no idea what I saw from behind that van. | VO | — | VN08 |
| L007 | BF · SC02 | SUE | Are we going to talk about it? | SH | — |  |
| L008 | BF · SC02 | TONY | What do you want me to say? | SH | — |  |
| L009 | BF · SC02 | SUE | I want you to say you’re going to do something. Because if that lad hadn’t been there, Tony… | SH | — |  |
| L010 | BF · SC02 | TONY | I’d have got to you. | SH | — |  |
| L011 | BF · SC02 | SUE | You didn’t make it one step. | SH | — |  |
| L012 | BF · SC02 | SUE | I’m 52. I’m not ready to push you round in a chair. | SH | — |  |
| L013 | BF · SC02 | TONY | Nobody’s pushing me anywhere. | SH | — |  |
| L014 | BF · SC02 | SUE | Then why did he think you were my dad? | SH | — |  |
| L015 | BF · SC02 | TONY | I’ll sort it. I’m not living like this. | SH | — |  |
| L016 | PB · SC03 | TONY (VO) | Sixty-four. Thirty years laying patios. I’ve knelt on every drive in this street. Now I can’t get across a car park to my own wife. | VO | — | VN09 |
| L017 | PB · SC03 | TONY (VO) | I used to carry her bags in from the car. Now I wait in the car while she loads the boot. | VO | — | VN09 |
| L018 | PB · SC04 | GP | Your bloods are fine. Blood pressure’s fine. For 64 you’re in decent nick. | SH | — |  |
| L019 | PB · SC04 | TONY | I’m 64 and I walk like I’m 85. | SH | — |  |
| L020 | PB · SC04 | GP | Thirty years on your knees, Tony. It’s wear and tear. It’s very normal. | SH | — |  |
| L021 | PB · SC04 | TONY | It’s not normal. | SH | — |  |
| L022 | PB · SC04 | GP | Keep moving, lose a few pounds, paracetamol when it’s bad. That works for most people. | SH | — |  |
| L023 | TN · SC05 | TONY | Gary. I’ve got to ask. How? You’re six years older than me. | SH | — | VN10 |
| L024 | TN · SC05 | GARY | You want the real answer? | SH | — |  |
| L025 | TN · SC05 | TONY | I’ve done the physio. The tablets. I’ve got a drawer full of braces. Nothing shifts it. | SH | — | VN09 |
| L026 | TN · SC05 | GARY | It won’t. Two years ago I was worse than you. I went down my stairs on my backside. | SH | — |  |
| L027 | TN · SC05 | TONY | Give over. | SH | — |  |
| L028 | TN · SC05 | GARY | I’m serious. And I’d tried everything you’re trying now. | SH | — |  |
| L029 | TN · SC05 | TONY | So what changed? | SH | — |  |
| L030 | TN · SC05 | GARY | Let me ask you something first. Where does it hurt? All round the knee, or one spot? | SH | — |  |
| L031 | TN · SC05 | TONY | All round. I don’t know. | SH | — |  |
| L032 | TN · SC05 | GARY | Press there. Just under the kneecap. Two fingers down. | SH | — | VN11 |
| L033 | TN · SC05 | TONY | There. | SH | — | VN11 |
| L034 | TN · SC05 | GARY | Exactly. That’s what nobody tells us. Every bloke our age thinks his knee’s worn out. So we rest it, strap it, take the tablets, and blame our age when nothing changes. | SH | — |  |
| L035 | TN · SC05 | GARY | But that’s not your knee giving up. It’s that one spot. Every step down the stairs, seventeen times your bodyweight goes through it. A spot the size of a coin. The pain is pressure. Nothing more. | SH | held (17×) · **F3** (size of a coin) · **F4** (pressure, nothing more) |  |
| L036 | TN · SC05 | TONY | So how do you fix it? | SH | — |  |
| L037 | TN · SC05 | GARY | You can’t rest it off. A brace goes round the joint. A sleeve squeezes it. A tablet hides it. None of them take the weight off that spot. | SH | **F4** comparative |  |
| L038 | TN · SC05 | GARY | You’re not old, Tony. You’re overloaded. That’s why nothing’s worked. You’ve been fighting a pressure problem with paracetamol. | SH | **F4** comparative |  |
| L039 | TN · SC05 | TONY | So what did you do? | SH | — |  |
| L040 | TN · SC05 | GARY | I took the weight off it. Stryde. It’s a strap. Sits right on that spot, two centimetres under the kneecap. Catches the force before it hits the knee. Three years they spent on it with orthopaedic surgeons. | SH | protection ✓ · held (3 yrs, orthopaedic surgeons) · **F3** (two centimetres) |  |
| L041 | TN · SC05 | GARY | Don’t buy the cheap ones off Amazon. They stretch. Anything that stretches doesn’t work. | SH | **F5** Amazon · **F4** (stretches → doesn't work) |  |
| L042 | TN · SC05 | TONY | A strap? Come off it. | SH | — |  |
| L043 | TN · SC05 | GARY | I know. I said the same. Laughed at my wife when she ordered it. And that’s it. That’s what changed. Put it on and go down your own stairs. You’ll know in a minute. | SH | **F4** outcome ("you'll know in a minute") |  |
| L044 | TN · SC06 | SUE | What’s that? | SH | — | VN12 |
| L045 | TN · SC06 | TONY | Something Gary put me on. | SH | — |  |
| L046 | TN · SC06 | SUE | You’ve said that before. | SH | — |  |
| L047 | TN · SC06 | TONY | Then don’t watch. | SH | — |  |
| L048 | AF · SC07 | TONY (VO) | First time in two years, I came down my own stairs forwards. I didn’t tell her. | VO | — | VN13 |
| L049 | AF · SC07 | LABOURER | You’re quick today, Tone. | SH | — | VN13 |
| L050 | AF · SC07 | NEIGHBOUR | Didn’t recognise you from the back. | SH | — | VN13 |
| L051 | AF · SC07 | TONY (VO) | That was the first time I felt it. | VO | — |  |
| L052 | AF · SC08 | SUE | Tony… | SH | — | VN14 |
| L053 | AF · SC08 | TONY (VO) | The man on his knees in that garden was someone I used to know. | VO | — | VN14 |
| L054 | AF · SC09 | SUE | Why are we stopping here? | SH | — | VN15 |
| L055 | AF · SC09 | TONY | Need compost. | SH | — |  |
| L056 | AF · SC09 | LAD | You alright, sir? | SH | — | VN15 |
| L057 | AF · SC09 | TONY | She’s fine. Thanks, love. | SH | — | VN16 · VN17 |
| L058 | OC · SC10 | VO | If your knees won’t come right no matter what you do. If the physio didn’t work and the doctor said it’s your age. It’s not your age. | VO | **F4** ("It's not your age") | VN18 |
| L059 | OC · SC10 | VO | It’s one spot, taking seventeen times your bodyweight, every step. You’re not old. You’re overloaded. | VO | held (17×) |  |
| L060 | OC · SC10 | VO | It’s called Stryde. It goes on under your trousers and nobody knows it’s there. | VO | name · hidden under trousers ✓ (wear guide 6) |  |
| L061 | OC · SC10 | VO | Buy one, get one free right now. One for each knee. Sixty days to send it back. Not the knock-offs on Amazon. If the link’s still there, grab it now. | VO | held (BOGOF, 60 days) · **F5** knock-offs on Amazon | VN18 |

Coverage: 1 hook (5 lines) + body 56 lines · **uncovered 0 · blocked 0** (beats at step 5).

### Claims (§43A)

Held in the Product Sheet register (V7.49.29): **17× bodyweight** through the spot below the kneecap · **three years with orthopaedic surgeons** · protection mechanism ("catches the force before it hits the knee") · hidden under trousers (wear guide 6) · **Buy 1 Get 1 Free** · **60-day money-back guarantee**. Numbers are edit overlays, never generated (§17). **Not in the register: F3, F4, F5** — voiced verbatim (§22U), listed in Flags. The GP gives ordinary advice and never recommends or disparages a product (§19B) — fine as written.

### Mode & Model Lock (§18A)

| Beat class | Model · params | Why |
|---|---|---|
| Mode | **Mode 4 Realistic Film**, 9:16, `LOOK-HERDAD` | the script: "AI Drama VSL, photoreal, like a short film" (F0) |
| Avatar sheets | `gpt_image_2_5` · `sunburst` · `high` · `2k` · 9:16 | §19 / V7.72.0 (**used this delivery**) |
| Location & property plates | Sunburst, **16:9** | V7.68.1 |
| Info cards (the spot under the kneecap, the drawer of braces, the strap in Sue's hand, the pack…) | Sunburst | V7.72.0 |
| Anatomy / mechanism (only if added — the script has none; Gary explains in words, F11) | `nano_banana_pro` | V7.72.0 |
| Video — every scene, the hook included | **Seedance 2.5 on Kie AI** (`kie.py seedance`), 720p, 9:16, **ingredients only, no frames** (V7.68.0) — sheets (face-and-hair crops on day outfits, HT26), plates, info cards, the speaker's voice master on spoken shots; **one take for connected action** (§24K part 5, `takes.py`); silent when no dialogue; `SERIES-LOOK`, `NEG-SOUND`, THE SCENE SO FAR per take (HT23) | §4, §24N, V7.88.0 |
| Voice | **§24I film voice master per speaking character** (Seedance, untrimmed); Tony's and Sue's inner VO and the offer narrator voiced to match (§3B, §22D bookend) | §18B voice route for Mode 4 / AI Drama |
| Music / tone / SFX | ElevenLabs `eleven_music_v2` / sound generation by API, `music.py` (§40A register map), `mix_scene.py` | §24M, §40A |
| Edit | CapCut desktop; `LUT-HERDAD.cube` + grain; **no trimming** (§24L) | §40 |

**Other locks:** side — **not named in the script** → the **right knee** (`SIDE_RULE`, F6); mechanism claim **protection**; edit `EDIT-HERDAD`; hooks **1 → 1 film** (F1); `kind: film`, no talking heads, no VO trim.

---

## 3. Cast (step 3) — generated, on the board for your check

Everyone with two or more beats gets a sheet. **Five:** Tony (hero, every scene), Sue (wife), Gary (mentor), the Lad (hook + payoff, VN04), the GP (one scene, five lines across several shots). One-offs cast at step 5 (§13): the van driver, the car driver (SC09), the labourer, the neighbour, garden-centre shoppers.

| Sheet | Job | File | Board |
|---|---|---|---|
| C1-TONY | `6e014a08-ef90-4fdf-ad91-6922c6faee59` | `cast/C1-TONY_v1.png` | To check |
| C2-SUE | `eea15f20-f918-45a8-bea6-06749429e7cc` | `cast/C2-SUE_v1.png` | To check |
| C3-GARY | `94bdab0e-7d42-4c7f-b260-99a7504d5621` | `cast/C3-GARY_v1.png` | To check |
| C4-LAD | `80c2158b-4f43-42db-a43b-2b4cc771c5c9` | `cast/C4-LAD_v1.png` | To check |
| C5-GP | `36504e3c-bad4-476c-934b-ed7e2939c330` | `cast/C5-GP_v1.png` | To check |

Manual run: **not checked by me** (§18B step 3) — Confirm or Fix each on the board. Prompts `cast/<ID>.prompt.txt` (9,287–10,167 chars), built from Appendix A by ID in `cast/build_sheets.py`: `CAM-FILM` (Alexa Mini LF + Signature Prime 50mm T4, tripod) → `AVATAR-SHEET` + `SHEET-GRID` → `SKIN-T` (Tony, Gary, GP) / `SKIN-A` (Sue — the script's "looks 45 to 48"; the Lad, 19) → `LOOK-HERDAD` → `CAP-FILM` → `NEG-SHEET` + `NEG-GRID` + `NEG-FILM` (lens clause dropped — the close-up looks at the lens) + `NEG-DEFAULT-FACE`. The two men who wear the strap (Tony, Gary) wear work shorts on the sheet so the knee shows (§19, §9D). Spend: 5 Sunburst jobs, one render each — **13.75 Higgsfield credits** (5,869.65 → 5,855.90).

### Identity strings — read off the renders (§7)

| ID | Identity string |
|---|---|
| C1 | white English man, 64, broad-shouldered, solid; broad weathered square face, heavy brow, grey-blue eyes, a broad nose, thin-lipped wide mouth, grey stubble, deep forehead and eye creases; short salt-and-pepper hair, side-parted, greyer at the temples; navy crew-neck sweatshirt (sleeves down) over a grey T-shirt, faded olive cargo work shorts above the knee, grey socks, tan leather work boots |
| C2 | white English woman, 52 reading mid-to-late 40s, slim, medium height; heart-shaped face, green-hazel eyes, straight nose, full mouth; a small dark mole on the cheek below the eye (her left — the prompt said right); chestnut-brown shoulder-length layered hair with caramel lights; **dark olive** quilted jacket (prompt: sage green) over a cream jumper, dark indigo straight jeans, white trainers |
| C3 | white English man, 70, tall, lean, wiry; long lean face, strong nose, pale blue eyes, bushy white brows, short white beard; shaved bald head; red-and-black buffalo-check overshirt, sleeves rolled, over a charcoal T-shirt, navy cargo work shorts, grey socks, brown leather work boots (the ear notch doesn't read at this size) |
| C4 | mixed-race British young man, 19, tall and lanky; narrow oval face, brown eyes, thick dark brows, broad nose, full lips, a light moustache; short dark tight curls, faded sides; a small dark mole on the left side of his neck; dark-green zip fleece over a bottle-green polo, black cargo work trousers, black trainers |
| C5 | British Indian woman, 48, slim, medium height; oval face, dark brown eyes, straight brows, long straight nose; a small dark mole on the jaw below the mouth (her right — the prompt said left); black hair with grey threads in a low bun, centre parting; navy cardigan over a pale-blue collared blouse, charcoal trousers, black loafers |

### §19A axis tables

| Axis | C1 Tony | C2 Sue | C3 Gary | C4 Lad | C5 GP |
|---|---|---|---|---|---|
| Face | broad weathered square | heart-shaped | long lean, hooked nose | narrow oval | oval, long nose |
| Hair | salt-and-pepper, side part | chestnut, caramel lights | shaved bald | short tight curls | black low bun |
| Age | 64 | 52 (looks ~46) | 70 | 19 | 48 |
| Build | broad, solid | slim, toned | tall, wiry | tall, lanky | slim |
| Wardrobe key | navy / olive | olive / cream / indigo | red check / navy | bottle green / black | navy / pale blue |
| Marker | scar through left eyebrow | mole on cheekbone | notch in right ear | mole on left neck | mole on jaw |
| Voice | south-east English, gruff (below) | south-east English, quick | Essex, dry, amused | south London, quick, kind | Midlands, calm, measured |

**Clearance:** every pair differs on ≥ 6 axes. ✓ Against the STRYDE roster (identity, 71-stairs, three-regrets, half-my-age, failed-alternatives, what-changed…): no repeat of a face architecture; the nearest is failed-alternatives' 63-year-old salt-and-pepper man (round face, pot belly, unibrow, fringe) — different face, build, hair cut and marker. The salt-and-pepper is the script's own casting (VN01).

### Voices (§22D) — for the §24I film voice masters, built after the maps (§18)

**`VOICE-TONY`** (Tony's dialogue and his inner VO)
```
An Englishman of sixty-four from the south-east of England, Kent, a builder all his life: a low, rough, chesty voice with gravel in it, plain working vowels, dropped t's, unhurried. He says little and says it flat; when he is hurt he goes quieter, not louder. Never theatrical, never sing-song; statements fall at the end.
```

| Character | `VOICE-[CHAR]` (short form; full string at the voice stage) |
|---|---|
| Sue | Englishwoman of 52, south-east, quick, clear and warm; her anger is fear held down — clipped when frightened, soft when she lets go |
| Gary | Englishman of 70, Essex, dry, amused and certain, a builder's directness; enjoys being right and isn't arguing |
| Lad | Londoner of 19, south London, quick and kind, a little breathless after the sprint |
| GP | Englishwoman of 48, Midlands (British Indian), calm, measured, kind and brisk — a ten-minute appointment |
| Narrator (offer, SC10) | **F2** — recommended: an English man in his 60s, warm, plain, unhurried, not Tony |
| One-offs (step 5) | Labourer: 30s, south-east, cheeky ("Tone") · Neighbour: older woman, friendly, surprised |

---

## Flags (decisions for you — nothing below was changed silently)

| # | Where | Finding | Recommendation |
|---|---|---|---|
| **F0** | mode | no `MODE` line; the script says "AI Drama VSL, photoreal, like a short film" | **Mode 4 Realistic Film** (Seedance, 720p). Say if you want Mode 5 (Pixar film) instead |
| **F1** | hooks | the script has **one** hook (THE VAN) and no `HOOKS` line | **1 finished film**. I can write two more cold opens at step 6 (agent-written, voiced only after your approval) — say if you want them |
| **F2** | SC10 | "A narrator closes" — the narrator's voice isn't specified | a separate English male narrator, 60s, warm and plain (not Tony). Say if you'd rather it be Tony's own voice |
| **F3** | L035, L040 | "A spot the size of a coin" and "two centimetres under the kneecap" — the register holds "just below the kneecap" (third-party guidance says about 2 inches), not 2 cm or coin size | voiced as written; pictured per FP03 (the notch on the kneecap's lower edge); please confirm the advertiser holds them |
| **F4** | L035, L037, L038, L041, L043, L058 | comparative / outcome lines: "The pain is pressure. Nothing more.", "None of them take the weight off that spot", "That's why nothing's worked", "Anything that stretches doesn't work", "You'll know in a minute", "It's not your age" | voiced as written; please confirm |
| **F5** | L041, L061 | "Amazon" named twice (§10A) | voiced verbatim; never pictured; no copy strap is shown (the script doesn't call for one) |
| F6 | side | the script never says which knee | **right knee** throughout (`SIDE_RULE`) — the knee that gives out in SC01 and wears the strap |
| F7 | L060 | "It goes on under your trousers and nobody knows it's there" vs FP13 (worn on screen: bare knee) | Tony and Gary are builders — work shorts on their strap days show it bare (FP13); the L060 picture is Tony in trousers, the strap hidden (nothing to show) |
| F8 | length | 702 words at the inspo's 105 wpm + the silent action beats → **~7:00–7:30** (inspo 6:47) | film pace, no trimming (§24L) |
| F9 | cast | read off the renders: Sue's jacket came out dark olive (prompt sage green) and her mole on the other cheek; the GP's mole on the other side; Gary's ear notch doesn't read; Tony's sleeves are down | on the board for your check — Confirm keeps them (the identity strings above follow the renders); Fix regenerates |
| F10 | SC05 | the mentor scene runs 21 lines (~2:20) in one place — §3B caps a scene at ~45s | staged as three beats in the yard: the slabs and "How?" → the spot (Gary sits Tony on a pallet of slabs, "Press there") → the strap named; each its own takes (§24K part 5) |
| F11 | mechanism | the script has no picture for "seventeen times your bodyweight… a spot the size of a coin" — Gary says it | kept in the scene (Tony's two fingers on the spot); a §12A-1 anatomy insert (the tendon, the glow on the spot) can be added on request |
| F12 | SC01, SC09 | the van and the car moving at Sue are risky for the video model (vehicles + a person pulled clear) | staged safely at step 5: the van reverses slowly and stops short, the lad's pull is one move across the frame, never contact; the car "pulls out fast" is shown by the car's nose in frame and Tony's three strides — no near miss in one shot |
| F13 | Drive | no Google Drive connector in this session → no `OUTPUT/` tree | every render is on the board; the tree is made when a Drive connector is available |
| F14 | product images | one new image (studio back of the strap) | kept in `intake/`; adding it to `stryde_refs/` is an owner change (BUILD_NOTES → For the owner). The back is never shown unless you ask (FP20) |

## Next — on your go (§18B step 5)

Confirm or Fix each avatar on the board and answer F0–F5 (and anything else). Then steps 4–5 as one delivery: the Property Sheet (Tony and Sue's terraced house — the steep narrow staircase, the bedroom drawer, the kitchen, the back garden) and plates (16:9), the garden-centre car park (one plate for SC01 and SC09), the car interior, the GP's room, the builders' yard, the street; the scene list with Scene Bibles, act map (with takes, `takes.py`) + wardrobe map per story day (`wardrobe.py`), the Visual Pitch (`visual_plan.py`), the music register map, ingredient lists per take, `angles.py` pass. Then the §24I voice masters, then the hook on Seedance.
