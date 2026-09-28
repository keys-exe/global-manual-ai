# Build Sheet — stryde-lost-moments

**STRYDE Precision Strap · "A - VID | Short VSL | TOF | Lost Moments | Iteration | Too Bad"** · Standards V7.64.2 · **RUN: MANUAL** · 2026-09-28

Steps 1–3 of §18. **Stopped at the avatar review (§18B, V7.62.0)**: steps 4–5 wait for the user's go.
Board: https://claude.ai/artifact/BahH1QuzHm4bQ9FAdxXfKj

---

## 0. Intake (§18B)

| Input | Found | Notes |
|---|---|---|
| Drive folder | `1UD92i5fATH3qiiez2jqI2WFQXYxxuPLc` | fetched with `fetch_drive.py` → `intake/` |
| Inspo | `MY INSPO VIDEO.mp4`: **the original STRYDE ad this script iterates** ("Too bad you have never worn these life-changing knee straps…", Meta Ad Library ID 1620934502990537) | 52.0s, 9:16, 720×1280, 30fps, audio |
| Script | `A VID Short VSL TOF Lost Moments Iteration Too Bad.dot`, a legacy Word (WPS) binary that `fetch_drive.py` could not sort. The text was read out of the file's UTF-16 stream → `intake/script.txt`, then normalised into `work/script_clean.txt` + one file per variant `work/script_<A–E>.txt` (labels only; no spoken word touched) | title line 1 ✓ · **5 hooks, each with its own body** · 1 build note + 5 visual notes ("Editor's call") |
| Product Sheet | `stryde_product_sheet_V7.49.32.py`: **newer than the repo's V7.49.31** (adds `WORDMARK_LOCK`, `NEG_WORDMARK`, `wordmark_check()`) | stored as `products/stryde/stryde_product_sheet.py`; `.md` regenerated |
| Product images | 10, identical to `products/stryde/stryde_refs/` (byte-compared) | layer 1 |
| Missing | `package_closed.jpg` (locked V7.49.27), anatomy samples | none blocks steps 1–3 |

**Message fields read:** `run manual` → **RUN: MANUAL**. `british` → **VOICE: British**, which matches the script's own note ("keep British Accent on Eleven Labs"). `MODE` blank → **Mode 1** (realistic reference, §18A). `HOOKS` blank → **in script: 5**, so **5 finished videos**. `CAP` blank → E0 Higgsfield default. No Loom.

**Script build note (whole build, VN01):** *"Different Voice (keep British Accent on Eleven Labs) Brolls and editing than the original. Include +\- 50% of Black People on the B-Rolls + Music."* Read as four instructions:
1. **a new narrator voice**, British: the original's male voice (median pitch 131 Hz) is replaced;
2. **new B-roll**: nothing re-used from the original ad and none of its shots re-staged;
3. **a new edit** that differs from the original's edit grammar (below);
4. **about half the people on screen are Black**, plus **a music bed**, which the original does not have (its tail is silent at −40 dB).

---

## 1. Absorption Sheet (§42)

### Part 1 — measured

| Instrument | Reading | Settles |
|---|---|---|
| Duration / aspect / res | 51.96s · 9:16 · 720×1280 · 30fps | 9:16 locked |
| Scene cuts | **33 shots, mean 1.57s**; cuts at 1.5 3.1 5.83 8.17 9.67 10.47 11.4 12.5 15.83 16.93 18.7 20.23 22.07 24.13 26.27 27.67 29.7 30.43 30.97 32.03 34.17 34.93 35.73 36.87 38.67 40.33 42.4 43.63 45.47 46.9 48.83 50.33 | a cut every ~1.6s |
| Silence (−30/−40 dB) | one, 50.32–51.85 (the tail), **silent at −40 dB** | wall-to-wall VO; **no music bed** |
| Volume | mean −16.7 dB, max 0.0 dB | hot VO |
| VO transcript (faster-whisper small) | 150 words / 50.2s = **179 wpm**, male, median pitch **131 Hz** | brisk; the voice we replace |
| TH / B-roll | **0 talking heads**, 100% B-roll | voice-only build |
| Shot frames + per-second sheets | `intake/frames/MY INSPO VIDEO/` | Edit Grammar below |

### Part 2 — structure map

| t | Job | What the original shows | Layout |
|---|---|---|---|
| 0.0–3.1 | hook ("Too bad you have never worn these…") | a clinician fits the strap on a seated woman's knee, X-rays on the wall; then she stands wearing it | full |
| 3.1–8.2 | proof (three years, surgeons) | old hands lift the strap out of a black box | full |
| 8.2–12.5 | "sleeves and braces never could" | CGI split card: **STRYDE PRECISION STRAP** (top) vs **BRACES** (bottom), glowing knees | split card + labels |
| 12.5–24.1 | conditions → 17× → redirect | glowing X-ray CGI knees, "MENISCUS" label, **17X** type with a red arrow, the strap on an X-ray knee | full CGI |
| 24.1–33.0 | result (walk, stairs, move) | people walking toward camera: park, stairs, garden, a warehouse worker with a box | full |
| 33.0–40.3 | features | strap worn in a garden, held in the palm, pressed on, clinic fit, trousers pulled down over it, living room | full |
| 40.3–46.9 | authority → offer | clinic group (patient, surgeon, nurse); a man walks a street; two straps on a table; black **BUY 1 GET 1 FREE** card with URL | full + offer card |
| 46.9–52.0 | guarantee → close | a man in an armchair puts it on; hands on the knee | full |

### Part 3 — Style Lock (copied, only what the brief keeps)

- **Kept:** one unseen narrator, brisk read (~175–180 wpm), plain declaratives; 100% B-roll, no talking head; product in almost every shot; a cut every ~1.5–2s; real older people in real places; iPhone register (§22).
- **Not copied, on the brief's instruction (VN01):** the voice, every B-roll shot, and the edit devices EG01–EG05 below.

### Part 3A — Edit Grammar (the original's, logged so we can do it differently)

| ID | Device (original) | Where | Our build |
|---|---|---|---|
| EG01 | **boxed captions**: every line in lowercase black text on a white box, centred at ~70% height | whole ad | **replaced** (EGN02) |
| EG02 | **CGI X-ray anatomy** (glowing blue/orange knees, labels, **17X** type, red arrow) across ~12s | 8.2–24.1 | **reduced and restyled** (EGN04) |
| EG03 | **comparison split card**: two stacked CGI panels with header labels ("STRYDE PRECISION STRAP" / "BRACES") | 8.2–12.5 | **not used** |
| EG04 | **offer card**: black background, two floating straps, italic "BUY 1 GET 1 FREE", URL | 43.6–46.9 | **replaced** (EGN05) |
| EG05 | hard cuts only, no music, no SFX, no punch-ins, no speed ramps | whole ad | **replaced** (EGN01, EGN03, EGN06) |

**`EDIT-STRYDE-LM`: our edit grammar (new, per VN01):**

| ID | Device | Rule |
|---|---|---|
| EGN01 | **Hook in two beats** | first line = the lost moment, live and full-frame (the thing they can't do now); hard cut on "Thanks to these life-changing knee straps" to the strap going on that same person's knee, then the moment done. |
| EGN02 | **Captions: key words only** | 1–3 word bold white captions with a thin black stroke, sentence case, centred at ~62% height, on the key words only (never every word); numbers as figures ("17×", "200,000+", "60 days"). No boxes. |
| EGN03 | **Punch-in on the payoff** | one 1.15× punch-in on each result line (e.g. "One foot per step.", "All eighteen.", "And you get back up on your own."). Otherwise hard cuts, ~1.8–2.2s runs. |
| EGN04 | **Anatomy: two beats, real-looking** | only the 17× line and the redirect/"takes the weight off" line; the Product Sheet's anatomy look (§12A register, `ANATOMY_LOOK`), not glowing X-ray; the 17× figure is a post overlay. |
| EGN05 | **Offer on a real table** | the open box with two straps (Product Sheet `PACKAGE`), hands lifting one out, then the offer text in the edit (BUY 1 GET 1 FREE · getstryde.co) over the live shot. No black card. |
| EGN06 | **Music bed** | one warm, light acoustic track under the VO (ducked ~−18 LU under speech, up 3 dB in the last 2s); a soft whoosh on the hook cut only. |
| EGN07 | **No watermark**, no split screens, no picture-in-picture | — |

### Part 4 — script absorption

**Copy formula (original → our five):** "Too bad…" identity/loss hook → build story with surgeons → comparative ("sleeves and braces never could") → conditions → 17× → mechanism ("redirects the load") → result → features → authority → offer → guarantee → close. **Each of our five variants swaps the generic hook for one lost moment and threads it through its own body** (the stairs, the walk, the dog, the golf round, the floor with the grandkids) and closes on a callback line ("Go to your own stairs.", "Get the lead.", "Book the tee time."…).

| Variant | Hook | Words (hook + body) | ≈ length at 175 wpm |
|---|---|---|---|
| A Forwards | "Too bad you can't go down the stairs forwards." | 19 + 137 = 156 | ≈ 53s |
| B Walk far | "Too bad you can't walk far without stopping anymore." | 19 + 140 = 159 | ≈ 55s |
| C Dog | "Too bad someone else walks your dog now." | 18 + 135 = 153 | ≈ 52s |
| D Golf | "Too bad your golf clubs are still in the garage." | 20 + 136 = 156 | ≈ 53s |
| E Floor | "Too bad you can't get down on the floor with the grandkids." | 25 + 133 = 158 | ≈ 54s |

**Seven lines are word-for-word in all five variants** (S-01…S-07 below). They get one set of B-roll, cut into each variant: the same product/authority/offer shots, re-used and never re-generated. That is ~40% of every body, and it keeps the five videos at roughly the cost of two.

### Part 5 — surfaced, not absorbed

| Original element | Disposition |
|---|---|
| Male narrator | replaced by a British woman (below), per VN01 |
| All B-roll (clinic fitting, box, CGI knees, walkers, clinic group) | not re-used, not re-staged (VN01) |
| Boxed captions, X-ray CGI, comparison card, black offer card | replaced by `EDIT-STRYDE-LM` |
| "BRACES" comparison card (a named category, glowing) | not used; the comparative line is voiced (F1) over our own shot of a sleeve and a brace pushed aside in a drawer |

### Part 6 — beat-it plan

| Original weakness | Our delta | Where |
|---|---|---|
| One generic hook for everyone | five specific lost moments → five videos, each with its own persona | Hooks A–E |
| The hook shows a fitting, not the loss | the loss first, live (EGN01), then the fix on the same person | every hook |
| 12s of CGI in a row, where the eye drifts | two anatomy beats only, surrounded by real people | EGN04 |
| No music; flat energy | a light bed and one punch-in per payoff (EGN03, EGN06) | every variant |
| All close with the same line | each variant closes on its own callback before the shared tag | A–E |

### Part 7 — confirmation

Conflicts with the rules are listed in **Flags**. **Confirm or correct the absorption along with the avatars.**

---

## 2. Script, product, claims, locks (step 2)

### Visual Instruction Ledger (§27F) — opened

| ID | Source | Instruction | Anchored | Carried by | Status |
|---|---|---|---|---|---|
| VN01 | script note | Different voice (British on ElevenLabs), different B-roll and editing from the original; ±50% Black people on the B-roll; music | whole build | new narrator (`VOICE-NARR`) · all-new B-roll · `EDIT-STRYDE-LM` · casting below · EGN06 | open → steps 4–8 |
| VN02 | script | Hook A: "Visual: Editor's call." | Hook A | EGN01, C1 Gloria on her stairs | open → step 5 |
| VN03 | script | Hook B: "Visual: Editor's call." | Hook B | EGN01, C2 Sheila on the high street | open → step 5 |
| VN04 | script | Hook C: "Visual: Editor's call." | Hook C | EGN01, C3 Winston and his dog | open → step 5 |
| VN05 | script | Hook D: "Visual: Editor's call." | Hook D | EGN01, C4 Graham and the garage | open → step 5 |
| VN06 | script | Hook E: "Visual: Editor's call." | Hook E | EGN01, C5 Clifton and the grandkids | open → step 5 |

### Phrase inventory (§27B) — dispositions are assigned at step 5

**Shared lines (identical in all five; one B-roll set, re-cut per variant):**

| ID | Phrase | Job | Claim | Subject / register |
|---|---|---|---|---|
| S-01 | Built over three years with orthopaedic surgeons, | proof | held | C6 surgeon, consulting room |
| S-02 | to do what sleeves and braces never could. | objection | **comparative, not in register (F1)** | a sleeve and a brace pushed aside in a drawer |
| S-03 | Perfect for bone on bone, arthritis, worn cartilage and meniscus pain. | conditions | held | C6 with a knee model / ANAT |
| S-04 | No slipping. No sores. No rolling down. | feature | — | worn in motion, three quick cuts |
| S-05 | Buy one, get one free today at getstryde.co. | offer | held (BOGOF) | open box, two straps (EGN05) |
| S-06 | Sixty-day money-back guarantee. | guarantee | held | box on a hall table / hands |
| S-07 | Nothing to lose but the pain. | close | — | the variant's protagonist, done |

**Near-shared lines** (same words in some variants; one B-roll set each):

| ID | Phrase | Variants | Claim | Subject |
|---|---|---|---|---|
| N-01 | This strap redirects the load away from the worn spot. | A C E | mechanism (**F2**) | ANAT-A (EGN04) |
| N-02 | And the pain just lifts. | A C D E | outcome (**F3**) | the variant's protagonist, relief |
| N-03 | Adjustable, breathable, with a silicone pad that locks the pressure right where you need it. | A C | held (pad) · "breathable" not in register (**F6**) | seating beat → pad back (`PAD_BACK_SHOT`) |
| N-04 | Adjustable, breathable, light enough you forget it's there. | B E | "breathable" (**F6**) | seating beat → worn, forgotten |
| N-05 | Recommended by orthopaedic surgeons for lasting relief. | A C E | held · "lasting relief" (**F3**) | C6 surgeon |
| N-06 | Sits flat under your trousers. | C D | — | §9D conceal/reveal, trousers (**F10**) |
| N-07 | Over two hundred thousand people wear one now. | B D | held | montage of wearers · 200,000+ overlay |
| N-08 | …seventeen times your bodyweight goes through one small spot below your kneecap. | all (lead-in differs) | held | ANAT-A, 17× overlay (EGN04) |

**Variant lines:**

| Variant | ID | Phrase | Subject |
|---|---|---|---|
| A | HK-A | Too bad you can't go down the stairs forwards. Thanks to these life-changing knee straps, not for much longer. | C1 Gloria: coming down sideways, gripping the rail → strap on |
| A | A-01 | On every step down, | C1 on the stairs (lead-in to N-08) |
| A | A-02 | That's why you turn sideways. | C1 sideways on the stairs |
| A | A-03 | That's why you grip the railing. | C1's hand white-knuckled on the rail |
| A | A-04 | So you come down facing forwards. | C1 facing forwards, strap on |
| A | A-05 | One foot per step. | C1's feet, one per step (EGN03 punch-in) |
| A | A-06 | Like a normal person again. | C1 at the bottom, into the hall |
| A | A-07 | Put one on. Go to your own stairs. | C1 seating the strap → looks up the stairs |
| B | HK-B | Too bad you can't walk far without stopping anymore. Thanks to these life-changing knee straps, that's about to change. | C2 Sheila stopped on a bench on the high street → strap on |
| B | B-01 | Every stride puts | C2 walking (lead-in to N-08) |
| B | B-02 | By the end of the road, that spot has had enough. So you stop. | C2 slowing, hand to knee, at a lamppost |
| B | B-03 | This strap catches the weight before it hits the knee. | ANAT-A |
| B | B-04 | The pain is pressure. Nothing more. Take the pressure off, and you keep going. | C2 seats the strap, sets off |
| B | B-05 | To the shops and back. | C2 with shopping bags |
| B | B-06 | Round the park, the long way. | C2 in a park (punch-in) |
| B | B-07 | Two miles, if you fancy it. | C2 on a long path (**F7**) |
| B | B-08 | Go the long way round. | C2 turns onto the longer path |
| C | HK-C | Too bad someone else walks your dog now. Thanks to these life-changing knee straps, not for much longer. | C3 Winston at the window watching a neighbour take his dog → strap on |
| C | C-01 | Here's why the walks got shorter. | C3 turning back at the gate |
| C | C-02 | Every stride, | lead-in to N-08 |
| C | C-03 | So you take the lead back. | C3 takes the lead from the neighbour |
| C | C-04 | Round the block first. Then the field. Then the long loop you both miss. | three places, rising (punch-in on the loop) |
| C | C-05 | Get the lead. | C3 lifts the lead off the hook |
| D | HK-D | Too bad your golf clubs are still in the garage. Thanks to these life-changing knee straps, not for much longer. | C4 Graham in the garage, clubs under a dust sheet → strap on |
| D | D-01 | A round is hours on your feet. Every stride, | C4 on the course (lead-in to N-08) |
| D | D-02 | By the back nine, that spot is finished. | C4 stopped on the fairway, hand on knee |
| D | D-03 | This strap sits two centimetres below the kneecap and takes the weight off it. | placement close-up (`PLACE-LOCK`, contact) → ANAT (**F5**) |
| D | D-04 | So you walk the course instead of watching it. | C4 walking past a buggy |
| D | D-05 | All eighteen. No buggy. | 18th flag / C4 walking off the green (punch-in) |
| D | D-06 | Sports doctors recommend it. | a sports-medicine doctor (one-off) (**F4**) |
| D | D-07 | One for each knee. | two straps worn, both knees (**F12**) |
| D | D-08 | Book the tee time. | C4 on the phone / at the pro shop counter |
| E | HK-E | Too bad you can't get down on the floor with the grandkids. Thanks to these life-changing knee straps, it doesn't have to stay that way. | C5 Clifton on the sofa, kids playing on the rug → strap on |
| E | E-01 | It's not getting down that stops you. It's getting back up. | C5 hand on the sofa arm, hesitating |
| E | E-02 | Seventeen times your bodyweight… | N-08 |
| E | E-03 | So you get down among the toys. | C5 kneeling on the rug with the kids |
| E | E-04 | And you get back up on your own. | C5 rising unaided (punch-in) |
| E | E-05 | No hand on the sofa. Nobody hauling you up. | his free hands; the sofa empty |
| E | E-06 | They won't be little for long. | the kids, backs to camera, with C5 |

Coverage: 5 hooks · 7 shared + 8 near-shared + 38 variant phrases · **uncovered 0 · blocked 0** (dispositions pending step 5).

### Claims (§43A)

Held in the Product Sheet register (user-confirmed V7.49.29): three years with orthopaedic surgeons · bone on bone / arthritis / worn cartilage / meniscus · 17× bodyweight · silicone pad · recommended by orthopaedic surgeons · 200,000+ wearers · Buy 1 Get 1 Free · 60-day money-back guarantee. Numbers are post overlays, never generated (§17). **Not in the register:** F1, F3, F4, F6, F7 (Flags).

### Mode & Model Lock (§18A)

| Beat class | Model · params | Why |
|---|---|---|
| Mode | **Mode 1 Realistic**, iPhone 17 Pro Max, 9:16 | realistic reference; no Mode 4/5 instruction |
| Avatar sheets | `gpt_image_2_5` · `variant: sunburst` · `quality: high` · `resolution: 2k` | §19 measured route (**used this delivery**) |
| Wordmark with hands or a body (held, worn, seating, hooks) | `nano_banana_pro` + `WORDMARK-LOCK` (Product Sheet V7.49.32) | rule 7; the name must read |
| Wordmark, no person (box, product) | `nano_banana_pro` | box lid wordmark |
| Volume B-roll with a person, no readable wordmark | `nano_banana_2` | volume |
| Anatomy (ANAT-A, EGN04) | `nano_banana_2` | §12A |
| Narrator voice-source image (§22U step 1) | `nano_banana_pro` | talking-head seed class |
| Video | Kling 3.0 (`kling-video-v3_0_omni`), start image required, `prefer_multi_shots: false` | §4, §27G |
| Voice | §22U: Kling source takes → ElevenLabs clone (user) → Eleven v3, five masters (hook + body per variant), house cut | §22U |

**Other locks:** format **voice-only, 100% B-roll** (reference style; say "talking heads" to change) · **side: right knee** (no knee named → `SIDE_RULE`), except D-07 both knees · mechanism claim: **protection** · edit: `EDIT-STRYDE-LM` · hooks: 5 in script → **5 videos, each hook with its own body** (§30H's identical-body rule does not apply: the script gives each hook its own body).

---

## 3. Cast (step 3) — generated, on the board for your check

**Casting to VN01 (±50% Black) and the Product Sheet (British, 55–80, balanced men/women):** six on-screen recurring people, **three Black British (C1, C3, C5) and three white British (C2, C4, C6)**, three women and three men. One protagonist per variant, plus the surgeon for the shared authority lines. One-offs (the neighbour in C, the sports doctor in D, extras) follow the same ±50%. The grandchildren (E) and the dog (C) come at step 4 as property/one-off sheets.

| Sheet | Job ID | File | Board |
|---|---|---|---|
| N-NARR | `b279a0c0-526e-455b-99f5-d8765ddfad37` | `cast/N-NARR_v1.png` | To check |
| C1-GLORIA | `ded1fa0c-1546-421d-adb5-94c1baee2800` | `cast/C1-GLORIA_v1.png` | To check |
| C2-SHEILA | `93f2ff6f-c34b-4e1f-af22-12eea57d8a87` | `cast/C2-SHEILA_v1.png` | To check |
| C3-WINSTON | `a6a36eec-ccb0-49a2-a70c-e29c191c9c4d` | `cast/C3-WINSTON_v1.png` | To check |
| C4-GRAHAM | `2bd591b1-d203-465c-aa46-7753d7f613e6` | `cast/C4-GRAHAM_v1.png` | To check |
| C5-CLIFTON | `578389bd-200a-401e-a6d9-c0ec3c5f32fe` | `cast/C5-CLIFTON_v1.png` | To check |
| C6-SURGEON | `4d32b455-fed9-47eb-a620-40a7cb1cbb1f` | `cast/C6-SURGEON_v1.png` | To check |

Manual run: the sheets are **not checked by me** (§18B step 3). They're on the board as To check; Confirm or Fix each one. Prompts: `cast/<ID>.prompt.txt`, built from Appendix A by ID in `cast/build_sheets.py` (`CAM-LOCK` → `AVATAR-SHEET` + `SHEET-GRID` → `SKIN-T` → `CAP-SHARP` → `CAP-FILE` → `NEG-SHEET` + `NEG-GRID` + `NEG-FILE` + `NEG-DEFAULT-FACE`; `APPROACH-PRO` on C6), 9,164–9,377 chars each. Spend: 7 Sunburst jobs, one render each.

### Identity strings — read off the renders (§7)

| ID | Identity string |
|---|---|
| N | Black British woman, 62, medium height, full-figured; round face, high full cheekbones, deep-set dark brown eyes, broad nose, full lips; a scatter of small dark raised spots on both cheekbones; short natural hair, black threaded with grey; mustard knitted cardigan over a cream top, dark straight jeans, tan loafers |
| C1 | Black British woman, 73, tall and slender, a little stooped; long narrow face, high forehead, wide-set heavy-lidded eyes, long straight nose, thin lips; short silver-white natural hair in small twists; lilac cardigan over a white blouse, navy-and-green floral skirt a hand above the knee, burgundy house slippers; bare knees |
| C2 | white British woman, 68, short and stocky; broad square face, heavy jaw, small pale-blue eyes, short upturned nose; flat brown mole on the chin, left of centre; short cropped grey pixie cut; teal rain jacket open over a grey T-shirt, khaki walking shorts above the knee, grey trainers |
| C3 | Black British man, 67, tall and broad, solid belly; broad heavy-jawed face, heavy-lidded dark eyes, wide flat nose; shaved head; short full grey beard, white at the chin; olive waxed jacket open over a red-and-navy check shirt, navy shorts above the knee, grey socks, brown walking boots |
| C4 | white British man, 64, tall and wiry; long lean face, sharp cheekbones, narrow pale eyes, crooked nose; sandy-grey hair in a side parting, clean-shaven, golfer's tan; navy golf polo, stone golf shorts above the knee, white ankle socks, white-and-tan golf shoes |
| C5 | Black British man, 70, short and heavyset, round belly; round full face, pouched eyes, broad nose, large ears; short grey-and-white hair receding at the temples, neat grey moustache; burgundy cardigan over a white T-shirt, grey jersey shorts above the knee, navy canvas slippers |
| C6 | white British woman, 56, medium height, upright; oval face, strong Roman nose, hazel eyes, relaxed brows, approachable; chin-length auburn bob gone grey at the roots; navy surgical scrubs, black clogs |

### §19A axis tables

| Axis | N | C1 | C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|---|---|---|
| Face | round, high cheekbones | long, narrow, high forehead | broad, square, heavy jaw | broad, heavy-jawed, low brow | long, lean, sharp cheekbones | round, full, heavy cheeks | oval, open (approachable, §19B) |
| Hair | cropped natural, black-grey | silver twists | grey pixie, thin at crown | shaved + full grey beard | sandy-grey side parting | cropped grey, receding + moustache | auburn-grey bob |
| Age position | 62 (young side) | 73 (far side) | 68 (mid) | 67 (mid) | 64 (young side) | 70 (far side) | 56 (below the band, a professional) |
| Build | medium, full-figured | tall, slender, stooped | short, stocky | tall, broad | tall, wiry | short, heavyset | medium, upright |
| Class / wardrobe | smart-casual | churchgoing, faded-smart | practical outdoors | country / dog-walker | club golfer | home, cardigan | clinical |
| Marker | dark raised spots on the cheekbones | scar through the left eyebrow | mole on the chin | mole by the left nostril | crooked nose | ears that stand out | Roman nose |
| Voice | South London (below) | non-speaking | non-speaking | non-speaking | non-speaking | non-speaking | non-speaking |
| Environment | kitchen table | terraced-house stairs | high street, park | back garden, field | garage, golf course | living room floor | consulting room |

**Clearance within the build (gate 5 of 8; the voice axis counts only for N):** every pair differs on ≥ 5 axes; the lowest are C3–C5 (5: both Black British men near 70 — they differ in face, hair, build, wardrobe, marker, environment) and C2–C4 (6). **Against the roster** (`stryde-identity` N, C1–C4): every new character differs on ≥ 6 axes from each entry. ✓
**Open face type (§19A scope note):** darker skin tones are still the unverified face type for §22S; C1, C3, C5 and N take the standard first-frame look on their first beat.

### Narrator — `VOICE-NARR` (§22D) and §20 constraint sheet

**`VOICE-NARR`** (compressed; goes verbatim into every §22U step-2 take, inside the Kling 2,500 limit)
```
A woman of sixty-two from South London, a warm mid-low voice with a soft grain, brisk and even. London vowels, relaxed and unforced; t's lightly dropped mid-word, clear at line ends. Statements fall gently at the end; a small smile audible on the payoff lines. Stress: slower and lower on the turn word, never louder.
```

| Field | N — narrator |
|---|---|
| Accent | South London, Black British, placed and unforced; never RP, never Cockney caricature, never American |
| Pacing | brisk, ~175 wpm (the original's 179, a touch warmer) |
| Posture / rest / gesture / ocular / rig | voice-source clip only (§22U step 1): seated at her kitchen table, forearms on it, Economical, eyeline on lens, R2 handheld: framed at steps 4–5 |
| Audio proximity | R2 |
| Wardrobe never-list | scrubs, white coat, anything clinical |
| Physical never-list | never on screen in the ad; never holds or wears the product |
| Voice spec | `VOICE-NARR` above |
| Stress register | slower, lower on "And the pain just lifts." / the variant's payoff; never bigger |
| Non-speech events | a soft breath-laugh before a payoff (once at most); a short in-breath before a number. Nothing else |
| Mouth asymmetry | read off the voice-source frame at step 4–5 |
| Voice name (§22U step 7) | `LostMoments-Narrator` (proposed) |

**Why a woman:** the brief asks for a different voice from the original's man; a Black British woman from South London is both different and in line with VN01's casting. Say if you want a man instead.

---

## Flags (decisions for the user — nothing below was changed silently)

| # | Where | Finding | Recommendation |
|---|---|---|---|
| **F1** | S-02 (all 5) | "to do what sleeves and braces never could": a comparative claim that isn't in the claim register | Voiced as written (§22U); shown with an ordinary sleeve and brace put away in a drawer, no brand. **Please confirm the advertiser holds it** |
| F2 | N-01 (A C E) | "redirects the load": load-path wording, but the Product Sheet's mechanism claim is **protection** | Voiced as written; pictured as protection (the pad takes the load off the worn spot), so nothing on screen contradicts the sheet |
| **F3** | N-02, N-05 | "the pain just lifts", "lasting relief": outcome claims not in the register | Voiced as written. Please confirm they're held |
| **F4** | D-06 | "Sports doctors recommend it": the register holds *orthopaedic surgeons* and *sports scientists*, not sports doctors | Voiced as written, shown with a sports-medicine doctor (one-off, §19B). **Please confirm the advertiser holds it** |
| F5 | D-03 | "sits two centimetres below the kneecap" | Voiced as written (matches the sheet's phrasing table); shown by contact (`PLACE-LOCK`: the kneecap seated in the notch), never a measured gap |
| F6 | N-03, N-04 | "breathable" is not in the register; "Adjustable" → `ADJUSTABLE_RULE` (seating beat, the band never shown adjusted) | Voiced as written; no visual claims breathability |
| F7 | B-07 | "Two miles, if you fancy it": an implied outcome | Voiced as written; no distance shown on screen |
| F8 | N-03 | "silicone pad" | Voiced verbatim; prompts say "the pad" (Product Sheet ruling) |
| **F9** | Format | Five hooks with **five different bodies** → five separate voice masters (hook + body each), not one shared body | As written. The seven shared lines re-use one B-roll set across all five |
| F10 | N-06 (C, D) | "Sits flat under your trousers": Winston and Graham wear shorts on their sheets | At step 5 the wardrobe map gives them a trousers day for that beat only (§9D conceal/reveal) |
| F11 | S-05/S-06 | `package_closed.jpg` is still missing from the folder | Open box only, unless you add it |
| F12 | D-07 | "One for each knee." | Graham wears one on each knee for that beat (the only two-knee beat) |
| F13 | VN01 | Read as: new narrator, all-new B-roll, a new edit (`EDIT-STRYDE-LM`), ±50% Black cast, add music | Say if the edit should stay closer to the original's |
| F14 | Script file | The script came as a legacy `.dot` Word template; `fetch_drive.py` couldn't sort it | Text read out of it word for word (`intake/script.txt`); a `.docx` next time avoids this |

## Next — on your go (§18B step 5)

Confirm or Fix each avatar on the board and answer F1, F3 and F4 (and anything else you want changed). Then steps 4–5 as one delivery: property and location sheets and plates (incl. the dog and the grandkids), act map + wardrobe map for all five variants with every VN row assigned and every B-roll row given its `EDIT-STRYDE-LM` layout, then the §22U voice route for the narrator.
