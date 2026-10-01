# Build Sheet — stryde-71-stairs-pixar-song

**STRYDE Precision Strap · "A - VID | Pixar Song | TOF | Pure Mechanism | Iteration | 71 Stairs Black American Woman"** · Standards V7.75.1 · **RUN: MANUAL** · **Mode 2 — 3D Pixar** · 2026-10-01

Steps 1–3 of §18. **Stopped at the avatar review (§18B, V7.62.0)**: steps 4–5 wait for the user's go.
Boards: Current https://claude.ai/artifact/NPMPgJeXr6cgTvtuFGhkZc · Old https://claude.ai/artifact/3pEQz2pWLJwTNX5TuBdccV · Final https://claude.ai/artifact/FYK7PCvgLG4SLzj72YdBPn · Plan https://claude.ai/artifact/VEE8gmwPVbvhVMNSC5rBLY

---

## 0. Intake (§18B)

| Input | Found | Notes |
|---|---|---|
| Drive folder | `1VZ709_1L6_cNjSadgDKn-BIKDGy89a5C` (matches no existing build → new build) | fetched with `fetch_drive.py` → `intake/` |
| **The song** | `71 Stairs Afro American Woman.mp3` — **the Black American Woman script sung word for word (Suno custom mode)**; the file's own lyric tag carries the same lyrics | **228.0 s (3:48)** · vocal 0.0 → 222.7 s · 619 Whisper words · ~165 sung wpm · peak +2.4 dBFS / RMS −13.1 dBFS (hot) · tempo ≈ 74 bpm (**unverified** — autocorrelation estimate; confirm at step 5) |
| Inspo | `71_Stairs HOOK+BODY 1.mp4` — the original "71 Stairs" ad this script iterates (British woman, 71; Meta Ad Library 2158360988054964 — the doc's `Reference:` link) | 155.6 s · 9:16 · 1080×1920 · 30 fps · 82 shots — the same file `stryde-71-stairs` measured; re-measured this session (`intake/inspo_report.json`) |
| Script | native Google Doc, exported as `.docx` by the fetch → `intake/*.extracted.txt`; the lyrics as 108 lines → `work/lyrics.txt`, timed against the song → `work/lyrics.timed.json` | title line 1 ✓ · 3 direction lines (VN01–VN04) · **615 lyric words** (the Mode 1 build's 613 + "seventy-one / seventy-four…" spelt out) |
| Product Sheet | `stryde_product_sheet_V7.49.32.py` — older than the repo's V7.49.38 | repo sheet kept (`products/stryde/`); the Drive copy is the same V7.49.32 the Mode 1 build brought in |
| Product images | 11, byte-identical to `products/stryde/stryde_refs/` (`back_ref_v2.png` included) | layer 1 |
| Missing | `package_closed.jpg` (locked V7.49.27) · no `inner_face` photo in the folder (the repo has it) | none blocks steps 1–3 |

**Message fields:** "run manual, the song is inside" → **RUN: MANUAL**; the song = the build's voice. `MODE` → **Mode 2 — 3D Pixar** (the task title "Pixar Song" is the explicit instruction §2 asks for; the §24 hybrid recommendation is **F2**). `HOOKS` → **1, in the song** (the song is one fixed piece → **1 finished video**). `VOICE` → none to make: the song is the locked voice master. `CAP` → E0 Higgsfield default. No Loom. `BUILD` → `stryde-71-stairs-pixar-song`.

**What is different from every build before it:** the voice stage is already done. The song is the §22U voice master — used exactly as supplied, never re-voiced, trimmed, sped or cut inside a sung line (its words are the script, §22U verbatim). Everything downstream keys off the song's word timestamps (`work/lyrics.timed.json`): B-roll lengths (E6), placement (§30H) and the edit grid (§42 Part 3A) read the song, and cuts land on its beat.

---

## 1. Absorption Sheet (§42)

### Part 1 — measured

| Instrument | Reading | Settles |
|---|---|---|
| Inspo duration / aspect / res | 155.55 s · 9:16 · 1080×1920 · 30 fps | 9:16 locked |
| Inspo scene cuts | **82 shots, mean 1.9 s**; runs of 0.4–0.5 s in the anatomy stretch (92–95 s) | a cut every ~2 s — on our build the song's beat (≈0.81 s) sets the grid: cuts on 2, 3 or 4 beats |
| Inspo silence (−30/−40 dB) | none | wall-to-wall voice |
| Inspo VO | 597 words / 155.4 s = 231 wpm, one woman, British, selfie talking heads + B-roll ~1:2 | **replaced by the song** (below) |
| Inspo shot frames + per-second sheets | `intake/frames/71_Stairs HOOK+BODY 1/` (82 × in/mid, 6 sheets) | Edit Grammar (Part 3A) |
| **Song duration** | **228.02 s**; vocal 0.00 → 222.68 s; instrumental outro 222.7 → 228.0 s ("mmm" hum) | the finished video is **3:48** |
| Song instrumental breaks (> 1 s between sung lines) | 15.5→17.1 (1.6 s, after the hook) · 67.1→68.3 (1.2 s) · 84.5→86.3 (1.8 s, after "right under her kneecap" — **F4: is "Stryde." sung here?**) · 159.2→160.5 (1.2 s, before "Yesterday") · 213.8→214.8 (1.0 s) · 218.3→219.4 (1.1 s) | the only air in the piece — the act breaks (hook → problem, reveal, result, close) |
| Song pace | 615 lyric words over 222.7 s of vocal = **~165 wpm sung** (the original's VO: 231) | slower than the original by a third — more room per line, longer B-rolls |
| Song tempo | ≈ 74 bpm, beat ≈ 0.81 s (**unverified**: onset autocorrelation, no beat-tracker installed) | edit grid: 2 beats = 1.6 s · 3 beats = 2.4 s · 4 beats = 3.25 s (§30H holds ≥ 2.0 s → B-rolls on 3 or 4 beats) |
| Song loudness | peak +2.4 dBFS (clipped), RMS −13.1 dBFS | CapCut: normalise to −14 LUFS, true-peak −1 dB; the hot master is a CapCut note, not a regeneration |
| Song transcript vs lyrics (`faster-whisper small`, word timestamps) | 603 of 615 lyric words aligned (ratio 0.93); the 12 misses are Whisper mis-hearings of sung words ("knee"→"neat", "pressure"→"precious", "Stryde Patellar"→"Strap Attila") plus **"Stryde." (line 37) not heard at all** and two added "mmm" hums at 219 s and 222–227 s | the song is the script sung as written as far as a transcript can tell; **the listen-check is the user's (F4)** |

### Part 2 — structure map (the song's clock)

The original's eleven jobs, now at the song's times (the structure is the same, the clock is the song's):

| Song t | Job | Lines | Opens with | Instrumental break before it |
|---|---|---|---|---|
| 0.0–15.5 | **hook** | 1–5 | “I'm seventy-one, and I take the stairs” | — |
| 17.1–27.4 | **the low point** | 6–10 | “Six weeks ago, I was going down my stairs backwards.” | 1.6s |
| 27.4–44.0 | **what failed** | 11–18 | “That big knee brace I bought” | — |
| 44.0–64.4 | **the turn: the cousin** | 19–26 | “Then my grandbaby got married in June.” | — |
| 65.0–98.7 | **the reveal** | 27–43 | “Loretta came to stay the week after.” | — |
| 98.7–106.6 | **the payoff** | 44–49 | “I did.” | — |
| 106.6–134.2 | **mechanism (Loretta's words)** | 50–65 | “She said, "Everything else you tried” | — |
| 134.2–159.2 | **proof** | 66–77 | “Over two hundred thousand people wear one now.” | — |
| 160.5–178.1 | **the result, lived** | 78–87 | “Yesterday I walked to the store.” | 1.2s |
| 178.1–200.9 | **proof + name + authority + objection** | 88–99 | “That was six weeks of wearing the strap.” | — |
| 200.9–222.7 | **offer, guarantee, close** | 100–108 | “The link's right down below.” | — |

**The original, for the shots it used per job** (what the Mode 1 build absorbed, kept here as the picture bank the Pixar version re-stages): hook = her climbing station stairs past younger women → her own stairs, daughter behind → to camera · low point = backwards down the stairs gripping the rail, the empty landing · what failed = the brace slipping to the ankle, PT couch, pills + coffee, injection, a heap of braces · the turn = reception, the cousin dancing, CGI red knee · the reveal = cousin at the door, the table of remedies, the trouser leg lifted, the strap handed over in both palms · payoff = down the stairs forwards, hands free · mechanism = the "comfortable" list, the sleeve-vs-strap card, the finger on the spot, red → blue · proof = 0.4 s montage of wearers, a sports doctor, the husband's golf swing, the niece on court, trousers hiding it, strap by a mug · result = the street with a bag, passing younger women, the queue, bags to the door, the husband in his chair · close = strap on the knee, friends, CGI labelled knee, surgeon + patient, knock-offs reddening a leg, two straps to camera, the open box, the box being addressed.

### Part 3 — Style Lock (**copied where the song allows; the register is the brief's**)

- **Beats and order exactly as the original** (Part 2) — the song fixes them.
- **Register: Mode 2 — 3D Pixar throughout (the brief's call: "Pixar Song").** Same woman, same entourage, same US settings as the Mode 1 build (family-photo staircase, a reception with line dances, the kitchen table with pill bottles, a checkout line, church steps), re-staged as a storybook-cinematic animated world (§24): `PIX-SHAPE` cast, `PIX-LIGHT` three-source light, `PIX-EYES`, `PIX-MOTION` arcs, render rigs only (RV / R4 — never handheld, §24), `NEG-PIX`. **The product is the one real object in the frame — `PIX-SPLIT` on every beat it appears in**, the front photo attached first (FP01, FP12).
- **Narrated B-roll, variant A (§3A): the narrator is seen, never addressing the lens; no talking heads, no lip-sync** (F3 offers the sung-to-camera bookends). The song is the anchor; §30A's anchor slot passes to her own face beats (the shots where she is alone and the camera holds on her).
- **Edit rhythm: the song's.** Cuts on the beat, B-rolls on 3–4 beats (2.4–3.25 s), the six instrumental breaks are the act breaks, the fast montage (EG05) on single beats only where the original ran 0.4 s shots.
- **Pure Mechanism (the task's angle):** the mechanism act (106.6–134.2 s, 27.6 s of song) is the longest act after the reveal and carries the §12A anatomy register (NB Pro, red = pain, blue = relief, §11) — the one place Pixar stylization does explanatory work the original's CGI did.
- Copied from the original: hard cuts only, no transitions, no SFX; one caption style (EG01 as lyric captions).

### Part 3A — Edit Grammar

| ID | Device (original) | Where | Our build |
|---|---|---|---|
| EG01 | **boxed captions**: black text on white boxes, one or two short lines at ~72 % height, following the voice phrase by phrase | whole ad | **kept as lyric captions** (CapCut, from `work/lyrics.timed.json`) — the only on-screen type |
| EG02 | **selfie talking head** as the spine, never > 3 s at a time | whole ad | **not kept — a song has no talking head.** The anchor is her own face beats (§3A variant A); F3 offers two sung-to-camera bookends instead |
| EG03 | **comparison card**: two X-ray legs, sleeve vs strap, header labels | 76.0–77.9 | kept as a layout, in the §12A anatomy register (Pixar-world cutaway); labels in the edit (§17), wording per F1/F5 |
| EG04 | **CGI anatomy run**: red hotspot under the kneecap → blue relief when the strap goes on | 77.9–92.3, 132.8–135.6 | kept: `ANAT-*` + `PIX-SPLIT` strap, red = pain, blue = relief (§11, HT11) |
| EG05 | **rapid montage**: 5–6 shots of 0.4–0.5 s, different people putting the strap on | 92.3–94.5 | kept on single beats (0.8 s each) under "Over two hundred thousand people…" (134.2–136.7 s) |
| EG06 | **hold-to-camera**: two straps lifted to the lens | 143.1–145.5 | kept (FP09: two straps, at true size, FP02) |
| EG07 | hard cuts only; no music bed audible; no punch-ins, transitions or SFX | whole ad | hard cuts, **on the beat**; the song is the bed; no SFX |

**`EDIT-STRYDE-71-SONG` = EG01, EG03–EG07 as above, cuts on the song's beat.** B-roll full-screen by default; `split`/`pip` at most 1 in 5 and never two in a row (V7.65.0).

### Part 4 — script absorption

The script is the Mode 1 build's, sung. Line for line it is the original "71 Stairs" ad iterated into a Black American woman's voice ("I done tried everything", "Chile", "I'ma just say it", "She gon' walk…"), with the US substitutions the Mode 1 build logged (Mama, grandbaby, Loretta, physical therapy / pain pills / cortisone shots, pant leg, rail, track, the store, church steps, fake websites) and one new line ("Electric Slide, Cupid Shuffle, all of it."). Sung, the numbers are spelt out ("seventy-one", "seventy-four", "two hundred thousand", "twenty-two") — the lyric file is the verbatim source for captions. **615 lyric words, all sung in order** as far as the transcript shows (Part 1).

### Part 5 — surfaced, not absorbed

| Original element | Disposition |
|---|---|
| Selfie talking heads (⅓ of the shots) | not absorbed — a song has no spoken address (F3) |
| British woman, English home, station stairs | replaced: Black American, US home (VN04); the hook's stairs are her own family-photo staircase or a US public staircase — set at step 5 |
| Comparison-card labels generated inside the image | labels become CapCut text (§17) |
| Knock-off shot showing a red, sore leg | kept as §10 fake-product B-roll: cheap copies stretched in the hands on a plain table (FP08), no storefront, no marketplace UI (§10A) |
| "Amazon" sung | sung as supplied, never pictured (§10A) — **F6** |
| 231 wpm wall-to-wall VO | the song's ~165 wpm with six breaks — the edit breathes where the song does |

### Part 6 — beat-it plan

| Original weakness | Our delta | Where |
|---|---|---|
| Photoreal UGC that looks like every other knee-strap ad in the feed | a Pixar-world grandmother singing her own story — a pattern interrupt no photoreal ad matches (§24: the hook and the story act are exactly where Pixar earns its place) | whole build |
| Opening on a train station, not her life | open on **her own** family-photo staircase, the daughter one step behind — the same stairs the song returns to at the payoff and the close (HT05: stakes in the picture, not a normal shot) | hook |
| Mechanism as grey CGI | the "Pure Mechanism" act in the §12A register inside the Pixar world — the spot under the kneecap, the whole-knee treatments vs the one spot, red → blue — long enough (27.6 s) to show, not tell | 106.6–134.2 s |
| The proof act is a blur | every proof line gets its own picture on the beat (HT10): the montage, the doctor, the golf swing, the track, the hidden strap, the mug | 134.2–159.2 s |
| "Three friends walk into a room" | the church steps with three ladies watching her come down (VN08 in the Mode 1 build) | 181.5–186.8 s |

### Part 7 — confirmation

Conflicts are listed in **Flags**. **Confirm or correct the absorption along with the avatars.**

---

## 2. Script, product, claims, locks (step 2)

### Visual Instruction Ledger (§27F) — opened

| ID | Source | Instruction | Anchored | Carried by | Status |
|---|---|---|---|---|---|
| VN01 | doc line 3 | "The Black American Woman script, sung word for word." | whole build | the song is the voice master; captions from `work/lyrics.txt`; §22U verbatim satisfied by the song itself (F4: one word to listen for) | verified (transcript) |
| VN02 | doc line 3 | "Suno custom mode." | whole build | information — the song is supplied, nothing to generate | verified |
| VN03 | doc line 3 | "Visuals: editor's call" | whole build | the pictures are mine to derive: Part 2 structure map + Part 6 beat-it plan, Mode 2 lock | open → step 5 |
| VN04 | doc line 3 | "but same Afro American Black Woman and entourage" | whole build | read as the same **roles** (a Black American woman of 71, her cousin Loretta, her daughter) — the user asked for **new** faces on 2026-10-01 ("i want new ones"), so the v1 recast of the Mode 1 cast is retired and v2 are new people; US settings as in `stryde-71-stairs` (family-photo staircase, reception, kitchen table, checkout line, church steps) | open → steps 3–5 |
| VN05 | doc line 2 | `Reference:` the Meta Ad Library link = the original 71 Stairs ad (the mp4 in the folder) | whole build | Part 1–3 absorption | verified |

### Phrase inventory (§27B) — with the song's times; dispositions are assigned at step 5

| ID | Song t-in → t-out | Lines | Lyric (verbatim) | Job | Claim | Subject / register |
|---|---|---|---|---|---|---|
| HK-01 | 0.0s → 8.6s (8.6s) | 1–2 | I'm seventy-one, and I take the stairs faster than women half my age. | hook | — | N on stairs, passing younger women |
| HK-02 | 8.6s → 15.5s (6.9s) | 3–5 | Last Sunday, my daughter walked behind me the whole way up and said, "Mama, when did that happen?" | hook | — | N up her stairs, C2 behind |
| P-01 | 17.1s → 22.1s (5.0s) | 6–7 | Six weeks ago, I was going down my stairs backwards. One step at a time. | problem | — | N backwards down the stairs, both hands on the rail (HT02) |
| P-02 | 22.1s → 27.4s (5.2s) | 8–10 | I ain't gonna lie, some days I wasn't going down them at all. I'd just stay upstairs. | problem | — | the empty stairs from the landing; N upstairs |
| P-03 | 27.4s → 32.5s (5.1s) | 11–13 | That big knee brace I bought slid right down my leg. By evening, it was around my ankle. | failed fix | — | generic hinged brace sliding → at the ankle (§10) |
| P-04 | 33.3s → 40.6s (7.3s) | 14–16 | I done tried everything. Physical therapy. Pain pills. Cortisone shots. Every brace and sleeve they make. | failed fix | — | PT couch · pill bottles · injection · heap of braces (HT10: one picture each) |
| P-05 | 40.6s → 44.0s (3.4s) | 17–18 | Nothing worked. Nothing lasted. Nothing gave me my life back. | low | — | N at the table, still |
| T-01 | 44.0s → 48.0s (4.0s) | 19–20 | Then my grandbaby got married in June. My cousin Loretta was there. | turn | — | reception · C1 |
| T-02 | 48.0s → 55.1s (7.1s) | 21–23 | She's seventy-four, and she was out on that dance floor all night. Electric Slide, Cupid Shuffle, all of it. | turn | — | C1 in the line dance (VN05 in the Mode 1 build) |
| T-03 | 55.1s → 57.1s (2.1s) | 24–24 | Both her knees was bone on bone too. | turn | held (bone on bone) | ANAT red worn joint (§12A register, NB Pro) |
| T-04 | 57.1s → 64.4s (7.3s) | 25–26 | I always figured hers wasn't as bad as mine. I always figured mine was past fixing. | turn | — | N alone, watching |
| R-01 | 65.0s → 67.1s (2.0s) | 27–27 | Loretta came to stay the week after. | reveal | — | C1 at the front door with a bag |
| R-02 | 68.3s → 76.9s (8.6s) | 28–31 | She watched me at the kitchen table, going through my morning routine. Two anti-inflammatories, the gel, the brace, an ice pack on my right knee. | reveal | — | the table: tablets, gel, brace, ice pack on the RIGHT knee |
| R-03 | 76.9s → 81.4s (4.5s) | 32–34 | After a minute she said, "Baby, can I show you something?" She pulled up her pant leg. | reveal | — | C1 lifts her pant leg (§9D reveal) |
| R-04 | 81.4s → 84.5s (3.1s) | 35–37 | She had on a little black strap, right under her kneecap. Stryde. | product first appearance | — | C1's knee, strap worn (PLACE-LOCK, PIX-SPLIT) — ‘Stryde.’ see F4 |
| R-05 | 86.3s → 90.4s (4.1s) | 38–39 | She handed me one. It looked ridiculous. Too small. | reveal | — | the strap in N's palm (FP06, FP02 size) |
| R-06 | 90.4s → 98.7s (8.2s) | 40–43 | I said, "Loretta, you know good and well this ain't gonna work on knees like mine." She said, "Just put it on and walk down them stairs." | reveal | — | C1 and N at the table; seating beat |
| R-07 | 98.7s → 106.6s (7.9s) | 44–49 | I did. Chile, the first step, I didn't even have to hold the rail. Not the second. Not the third. All the way down. Both feet. Forwards. | payoff | — | N down her stairs forwards, hands off the rail (HT03/HT04) |
| M-01 | 106.6s → 112.9s (6.3s) | 50–52 | She said, "Everything else you tried was made to keep you comfortable while your knee got worse. | mechanism | comparative (F1) | PT / pills / shot callbacks |
| M-02 | 113.0s → 116.0s (3.0s) | 53–53 | This one fixes why it hurts." | mechanism | outcome (F1) | comparison card (EG03), labels in the edit |
| M-03 | 116.0s → 119.7s (3.7s) | 54–55 | She said, "There's one spot under the kneecap where every step lands. | mechanism | held (the spot) | ANAT: the point below the kneecap (HT11, HT14) |
| M-04 | 119.8s → 125.6s (5.8s) | 56–60 | Every brace, every shot, every pill you ever tried treated the whole knee. Not that spot. That's why ain't nothing worked. | mechanism | comparative (F1) | braces · injection · pills · ANAT whole-knee vs the spot |
| M-05 | 125.6s → 131.3s (5.7s) | 61–63 | The pain is pressure. That's all it is. This strap sits right on that spot and takes the weight off." | mechanism | protection ✓ | ANAT red → strap on → blue relief (EG04) |
| M-06 | 131.3s → 134.2s (2.9s) | 64–65 | First step. Pain gone. Just like that. | outcome | outcome (F1) | N's feet on the top step |
| PR-01 | 134.2s → 136.7s (2.5s) | 66–66 | Over two hundred thousand people wear one now. | proof | held (200,000) | EG05 montage of wearers |
| PR-02 | 136.7s → 140.7s (4.0s) | 67–68 | Sports doctors recommend it. Not the pharma companies. Sports doctors. | authority | not in register (F1) | a sports-medicine doctor (§19B, approachable) |
| PR-03 | 140.7s → 145.3s (4.6s) | 69–70 | Loretta's husband wears one. He's seventy-six, and he plays golf twice a week. | proof | — | Loretta's husband (one-off), golf swing |
| PR-04 | 145.3s → 148.1s (2.8s) | 71–72 | Her niece wears one when she runs track. She's twenty-two. | proof | — | the niece (one-off) on a track |
| PR-05 | 148.3s → 153.8s (5.5s) | 73–75 | I've worn mine every day for six weeks. Under my clothes. Don't nobody know it's there. | feature | — | §9D conceal — strap under trousers |
| PR-06 | 154.6s → 159.2s (4.6s) | 76–77 | No pills. No gel. No brace around my ankle by lunchtime. | feature | — | strap by a mug; the brace gone |
| L-01 | 160.5s → 166.7s (6.2s) | 78–80 | Yesterday I walked to the store. Two miles there. Two miles back. Passed three women half my age. | result | implied (F1) | N walking a street, passing younger women (HT01) |
| L-02 | 166.7s → 173.4s (6.7s) | 81–84 | Stood in that checkout line ten minutes without shifting my weight. Carried two bags home. Didn't nobody help me. | result | — | checkout line · two bags home (HT01) |
| L-03 | 173.4s → 178.1s (4.7s) | 85–87 | When I got home, my husband said, "You was gone a long time." I said, "I know." | result | — | husband (one-off) in his chair |
| C-01 | 178.1s → 181.5s (3.4s) | 88–89 | That was six weeks of wearing the strap. Nothing else. | result | — | strap on N's right knee |
| C-02 | 181.5s → 186.8s (5.4s) | 90–91 | Three ladies from church already ordered one after they watched me come down the church steps. | proof | — | church steps, three ladies (one-offs) |
| C-03 | 186.8s → 191.3s (4.5s) | 92–93 | So I'ma just say it right here. It's called Stryde Patellar Force Redirection. | name | name (F1) | ANAT strap on the knee (labels in the edit) |
| C-04 | 191.3s → 196.3s (4.9s) | 94–96 | They spent three years designing it with orthopedic surgeons. It's the real thing. | authority | held | surgeon + patient (one-offs, §19B) |
| C-05 | 196.3s → 200.9s (4.6s) | 97–99 | Not them cheap knock-offs they be selling on Amazon and them fake websites. | objection | Amazon named (F6) | fakes stretched in hands on a plain table (FP08, §10) |
| C-06 | 200.9s → 205.1s (4.2s) | 100–101 | The link's right down below. Two straps for the price of one right now. | offer | held (BOGOF) | two straps held up (FP09, EG06) |
| C-07 | 205.1s → 208.0s (2.9s) | 102–103 | Sixty days to send them back if they don't work. | guarantee | held | open box, two straps |
| C-08 | 208.0s → 213.8s (5.7s) | 104–105 | Eleven years of knee pain. Gone the first step I took with it on. | outcome | outcome (F1) | N on her top step |
| C-09 | 214.8s → 222.7s (7.9s) | 106–108 | I bought my sister a pair that same week. She coming Sunday. She gon' walk up my stairs on her own. | close | — | the sister (one-off) walks up N's stairs on her own; N watching |

Coverage: 2 hook + 40 body phrases, **615 words · uncovered 0 · blocked 0** (dispositions at step 5). Times from `work/lyrics.timed.json` (Whisper word timestamps, ±0.1 s); line 37 "Stryde." has no timestamp (F4).

### Claims (§43A)

Held in the Product Sheet register (user-confirmed V7.49.29): three years with orthopaedic surgeons · bone on bone · 200,000+ wearers · Buy 1 Get 1 Free · 60-day money-back guarantee · the spot below the kneecap. Numbers are post overlays, never generated (§17). **Not in the register (F1):** "made to keep you comfortable while your knee got worse", "This one fixes why it hurts", "treated the whole knee… that's why ain't nothing worked", "First step. Pain gone.", "Sports doctors recommend it. Not the pharma companies.", "Eleven years of knee pain. Gone the first step", "Two miles there. Two miles back." — all already sung in the supplied song; the pictures stay inside the held register (protection: the pad takes the weight off the spot).

### Mode & Model Lock (§18A)

| Beat class | Model · params | Why |
|---|---|---|
| Mode | **Mode 2 — 3D Pixar**, 9:16, the whole build (hybrid declined by the brief — F2) | the task title "Pixar Song"; §2 explicit instruction |
| **Format** | **Music Video (§3C, V7.76.0)** — no voices, no VO, no talking heads; one **sung** music master supplied by the team (the script's lines verbatim — the §22U verbatim rule on the lyrics); every clip silent, the track whole under the cut; board `kind: "music"`, Music stage, `MUS-BODY` card | V7.76.0 landed on the default branch during steps 4–5 and describes this build exactly; adopted the same turn (nothing generated against the act map yet) |
| Avatar sheets (step 3) | `nano_banana_pro` · 2k · 9:16 · one render each — **Higgsfield logged `nano_banana_2`** (the §5 routing fault seen on every build since stryde-identity; recorded on the cards) | §18A Mode 2 table (rule 6: Nano Banana only); F10 |
| Every beat image — hook, B-roll, worn, held, product, info cards | `nano_banana_pro` · 2k · **A/B pair** (two Pro renders, V7.70.0) · §6A short prompt · `PIX-SPLIT` + the front photo first on any product beat | §18A Mode 2 table |
| Anatomy / mechanism (EG03, EG04, M-03…M-05, C-03) | `nano_banana_pro` · A/B pair · §12A register inside the Pixar world | §18A |
| Location plates | `nano_banana_pro` · **16:9** · one render | §2 (V7.68.1) |
| Video (B-roll, hook) | Kling 3.0 (`kling-video-v3_0_omni`), start image, render rigs RV / R4 only, `PIX-MOTION`, `prefer_multi_shots: false`, §35A ≤ 1,000 chars | §4, §24, §27G |
| **Voice** | **the supplied song — locked as generated.** No §22U clone, no TTS, no `vo_trim.py`, no talking heads. Word timestamps `work/lyrics.timed.json` are the voice master's timeline (E6, §30H) | VN01 |
| Captions | CapCut, lyric lines verbatim (EG01) | §17 |
| Music (§40A, §3C) | **the song is the music master** (`music/MUS-BODY.cue.json`: the §40A register map as its sections, `sung: true`, `bpm: 73.8`); `music.py check` run (listening pass, thresholds unverified): loudness rises steadily hook → close, drum transients flag CLICK on a hot master, nothing to regenerate; the cut grid is the song's beat (`music/MUS-BODY.grid.json`, `music.py`'s `grid`) | §3C, §40A |
| Edit | `EDIT-STRYDE-71-SONG`; cuts on the song's beat; `assemble.py` plan from the song's word times; export native 9:16; audio normalised −14 LUFS | §30H, §42 Part 3A |

**Other locks:** format **Narrated B-roll, variant A** (the narrator seen, never addressing — §3A; F3); **side: right knee** ("an ice pack on my right knee" → `SIDE_RULE`); mechanism claim: **protection**; hooks: **1, in the song → 1 finished video (3:48)**; the §24 hybrid (Mode 1 proof/offer/close) **not applied** — the brief says Pixar (F2).

**Step 4–5 derived locks (for the go):** every beat image at ≤ 1,200 chars (§6A) with the §6A Part 2 first-render rules; `preflight.py "kind": "image"` PASS before any call; House Taste HT01–HT21 and `products/stryde/fix_patterns.md` FP01–FP13 read before every prompt (no Fix notes of this build's own yet — nothing to harvest, `fix_patterns.py` runs after the first Fix round).

---

## 3. Cast (step 3) — v2, generated, on the board for your check

**Fix round 1 (user, 2026-10-01: "i want new ones and loretta should not be too thin they should be the same size as the narrator").** Three new people (§19: with nothing attached every reroll is a new person — and new is what was asked), Loretta written at the narrator's build word for word ("THE SAME SIZE AS THE NARRATOR… never thin, never lean, never tall and willowy"). The v1 sheets (the Mode 1 cast recast) are on the Old board. Everyone with two or more beats gets a sheet: **N** the narrator (every act), **C1 Loretta** (reception, door, table, reveal, stairs coaching), **C2 the daughter** (the hook). One-offs are cast at step 5 per §13.

| Sheet | v | Job ID | File | Board asset | Board |
|---|---|---|---|---|---|
| N-NARR | v2 | `32b8bfc2-4538-4c28-b485-3fd28fc5d489` | `cast/N-NARR_v2.png` 1536×2752 | `21896d82f1800c80027bc2c76705c31c` | To check |
| C1-LORETTA | v2 | `fce3f6cb-9ef5-47b5-996b-f9c62e893bc8` | `cast/C1-LORETTA_v2.png` 1536×2752 | `f0d9e11e33a341d2260a173e49eff071` | To check |
| C2-DAUGHTER | v2 | `d7028142-0650-4c2e-9c6e-080e28f4edf4` | `cast/C2-DAUGHTER_v2.png` 1536×2752 | `fda069ae35950e7a573035855140337b` | To check |
| N-NARR | v1 | `499cdf95-5208-4713-8ac4-4be015410227` | `cast/N-NARR_v1.png` | Old `a86adc7f268e060772ffdc12da800900` | replaced |
| C1-LORETTA | v1 | `75275110-9d2e-4f4c-b540-88b68b13976a` | `cast/C1-LORETTA_v1.png` | Old `f0b774bc2cfc1e03f29b621f6b0a446b` | replaced |
| C2-DAUGHTER | v1 | `b00b3656-29e8-44f2-8608-82d9dbccfefe` | `cast/C2-DAUGHTER_v1.png` | Old `3128f425a117edf0f9ce9366c664fc2a` | replaced |

Manual run: the sheets are **not checked by me** (§18B step 3) — Confirm or Fix each on the board. Prompts: `cast/<ID>.v2.prompt.txt` (v1 in `cast/v1/`), built from Appendix A by ID in `cast/build_sheets.py` — the **Mode 2 sheet form (F10)**: a render opening in place of `CAM-LOCK` → `SHEET-GRID` verbatim → `AVATAR-SHEET`'s sameness / light / room clauses → `PIX-SHAPE` filled → `PIX-EYES` → `PIX-LIGHT` (the window as key) → `CAP-ANIM` → `NEG-SHEET` (minus its two anti-render clauses) + `NEG-GRID` + `NEG-PIX` + `NEG-DEFAULT-FACE`; v2 adds "NO WRITING ANYWHERE ON THE CANVAS" and a one-side-only marker clause (v1 drew panel titles and mirrored the marker); 9,983–10,326 chars. Spend: 6 jobs × 2 credits so far (Higgsfield 11,355.4 before the cast). Model requested `nano_banana_pro`; Higgsfield logs `nano_banana_2` on every job (§5 routing fault, recorded on the cards).

### Identity strings — read off the v2 renders (§7; descriptions, not verdicts)

| ID | Identity string (as rendered) |
|---|---|
| N | Pixar-stylized Black American woman, 71, deep brown skin, medium height, soft and full through the hips and middle, rounded shoulders; an oval face with full cheeks, wide-set dark eyes under straight level brows, a broad flat-bridged nose, full lower lip; one small dark mole beside the nose at the nostril crease (on the viewer's left in the close-up); short silver-grey twist-out with black at the nape; mustard short-sleeved top, mid-blue denim A-line skirt above the knee, white slip-on canvas shoes; warm-white room, beige carpet, window left; a faint closed-mouth smile in the close-up |
| C1 | Pixar-stylized Black American woman, 74, medium-brown skin, **the narrator's build** — medium height, soft and full through the hips and middle, rounded full shoulders, a soft double chin; a broad square face with soft full cheeks, hooded eyes under thick arched brows, a short wide nose, a wide mouth; one dark beauty mark beside the corner of her upper lip (on the viewer's right in the close-up); silver-grey chin-length pressed bob, centre-parted, tucked behind the ears; teal three-quarter-sleeve top, khaki shorts above the knee, white canvas slip-ons; butter-yellow wall, oak floor, window right |
| C2 | Pixar-stylized Black American woman, 46, medium-deep brown skin, medium height, athletic and broad-shouldered; a heart-shaped face with high cheekbones, almond eyes, softly arched brows, a slim straight nose, a small pointed chin; two small dark marks on one cheek below the eye (the prompt asked for one); dark-brown curly hair in one high round afro puff; olive crewneck sweatshirt, black denim shorts, white trainers; pale grey-white room, window left (the floor rendered as a pale hard floor, not the carpet asked for) |

### §19A axis tables (v2)

| Axis | N | C1 | C2 |
|---|---|---|---|
| Face | oval, full cheeks, straight brows (dominant: ROUND; accent: the straight brows) | broad square, soft cheeks, hooded eyes (SQUARE; accent: the round bob) | heart-shaped, pointed chin (TRIANGULAR; accent: the round puff) |
| Hair | short silver-grey twist-out | silver-grey chin-length pressed bob | dark-brown high afro puff |
| Age position | 71 | 74 | 46 |
| Build | medium, full; 5.5 heads, settled posture | **the same as N**: medium, full; 5.5 heads | medium, athletic; 6 heads |
| Class / wardrobe | home, mustard top and denim skirt | neat, going-visiting, teal and khaki | weekend casual, olive and black |
| Marker | mole beside the nose | beauty mark above the lip corner | mole under one eye |
| Voice | the song (sung) | none (quoted in the song) | none |
| Environment | stairs, landing, kitchen table | reception, front door, table | stairs (hook) |

**Clearance:** N–C1 differ on 6 axes (build now shared by design — the user's call), N–C2 on 7, C1–C2 on 7 ✓. Against the roster (every other build): no shared face architecture, hair, marker or wardrobe register with any locked sheet; v1 (the recast `stryde-71-stairs` faces) is retired to the Old board. **Sheets expose the placement site** (§19, §9D, FP13): above-the-knee skirt/shorts, bare knees, on all three.

### §20 constraint sheets (what the pictures may do)

| Field | N | C1 | C2 |
|---|---|---|---|
| Voice | the song — no dialogue generated; no mouth conform (§3A) | none | none |
| Posture / rest | settled, hands at her sides or on the table edge; never gripping the rail after the strap (HT03) | upright, hands free; a hand on her own knee on the reveal | one step behind her mother, a hand near the rail |
| Gesture register | Economical | Restrained | Restrained |
| Ocular default | off-lens, on what she is doing; to lens only in F3's bookends | on N | on N |
| Camera rig | RV / R4 render rigs only (§24); camera sways, never travels with a moving subject (§27G) | same | same |
| Wardrobe never-list | anything clinical; trousers over the strap on a worn beat (FP13) | trousers on the reveal beat (FP13) | — |
| Physical never-list | never both knees strapped; never brace and strap together; never hands on the rail in the after-state | — | — |
| Eyeline | off-lens | off-lens | off-lens |
| Mouth | closed between beats; no singing mouth unless F3 is chosen | closed | closed |

---

## Flags (decisions for the user — nothing below was changed silently)

| # | Where | Finding | Recommendation |
|---|---|---|---|
| **F1** | M-01, M-02, M-04, M-06, PR-02, L-01, C-03, C-08 | Comparative / outcome / authority claims not in the register (the same lines the Mode 1 build flagged as F1, F2, F4, F7) — **already sung in the supplied song, so nothing can be re-voiced** | Pictures stay inside the held register (protection; the spot); labels in the edit use the held wording. Please confirm the advertiser holds the sung claims |
| **F2** | Mode | §24's register warning: Pixar reads as content for families; on an adult-buyer product the standard recommends the **hybrid** (Pixar hook, story and mechanism; Mode 1 proof, offer and close) | **Locked as the brief says: full Mode 2** — the song's one voice and one world argue for one register. Say "hybrid" and acts PR/L/C re-lock to Mode 1 at step 5 (same cast recast realistic — new sheets) |
| **F3** | Format | A song has no talking head. §3A says bookend narrated B-roll with the two conversion beats on a face | **Default: variant A — she is seen, never sings to the lens.** Option: two **sung-to-camera** bookends (the hook 0–15.5 s and the close 200.9–222.7 s) lip-synced to the song (Kling omni with the song as audio, or HeyGen) — say "sing to camera" and they go on the act map |
| **F4** | Line 37 "Stryde." (84.5–86.3 s) | The transcript hears nothing in that gap — the word may be sung softly, or not at all | **Listen to 84–87 s.** If it isn't sung, the caption still carries "Stryde." on the product's first appearance (EG01); if it is, nothing changes |
| F5 | C-03, EG03 | "Stryde **Patellar Force Redirection**" is sung; the held claim is protection | Pictured as protection; card labels in the edit: "FULL SLEEVE: pressure everywhere" / "STRYDE STRAP: one spot" unless you want the original's words |
| **F6** | C-05 | "Amazon" sung (§10A) | Never pictured — knock-offs as plain stretched copies on a table (FP08) |
| F7 | Offer / guarantee / 200,000 | held claims | overlays in the edit (§17), numbers never generated |
| F8 | Side | "an ice pack on my **right** knee" | strap on the right knee throughout (`SIDE_RULE`) |
| F9 | `package_closed.jpg` | missing from the folder (as on every STRYDE build) | open box only |
| **F10** | Standards gap | §19 has a Mode 1 sheet and a Mode 5 sheet, **no Mode 2 sheet**. I built the Mode 2 form (section 3) and the sheets ran on it; Higgsfield also logged `nano_banana_2` for the `nano_banana_pro` request (§5 routing fault) | Say "amend" and the Mode 2 sheet form goes into §19 / Pending Amendments as a §34 correction. If you want the sheets on a true Nano Banana Pro route, Kie serves `nano-banana-pro` (`kie.py image nano-banana-pro`) — your call, 3 more renders |
| F11 | Length | The song is 3:48 — longer than a Short VSL's 2–4 min upper half; one finished video | Cut nothing from the song (its words are the script); the edit uses the six breaks |
| F12 | Edit | Tempo ≈ 74 bpm is an estimate | Confirm at step 5 with a beat grid laid over the song in CapCut, or say the BPM from Suno |
| F13 | Loudness | The song peaks at +2.4 dBFS (clipped master) | CapCut: normalise −14 LUFS, true-peak −1 dB; if Suno can re-export unclipped, drop the new file in the folder |

## Next — on your go (§18B step 5)

Confirm or Fix each avatar on the board; answer F2, F3, F4 (and anything else). Then steps 4–5 as one delivery: property sheet + 16:9 Pixar plates (her house — stairs, landing, kitchen; the reception; the store checkout; the church steps; the street), the act map on the song's clock (every phrase → beats on 3–4 beats of the song, E6 lengths from `lyrics.timed.json`, `angles.py` PASS), the wardrobe map, `EDIT-STRYDE-71-SONG`. **No voice stage** — then hooks at step 6 (one hook, 0–15.5 s) and the body acts.
