# Build Sheet — down-forwards-again

**STRYDE Precision Strap · "C - VID | Doctor VSL | TOF | Doctor Authority | New | Down Forwards Again"** · Standards V7.64.4 · **RUN: MANUAL** · 2026-09-28

Steps 1–3 of §18. **Stopped at the avatar review (§18B, V7.62.0)**: steps 4–5 wait for the user's go.
Boards: Current https://claude.ai/artifact/UqVKJB21YyfBZTjxh5dNNT · Old https://claude.ai/artifact/8eXUW9NwJq49zRfPHtgC5Y · Final https://claude.ai/artifact/W11NPXayafpTXoY4FqMccb · Plan https://claude.ai/artifact/5Wzyk63o5viz5t4wLVZUu7

---

## 0. Intake (§18B)

| Input | Found | Notes |
|---|---|---|
| Drive folder | `1m1H8YO6MEVQBnoD2gkWPfn-y__PW0Bbk` (brand folder STRYDE `1MG81pjTPpj6qSJsJzKVQzcNcuyik8Nkc`) | fetched with `fetch_drive.py` → `intake/`; matches no existing build → new build |
| Inspo | one MP4 (renamed `intake/inspo.mp4`): a **doctor-authority VSL for a menopause supplement** ("She Again", Moringa) — the script's "Reference: facebook.com/ads/library/?id=1011702238236696" | 142.1s · 9:16 · **360×640** (low-res download) · 29.97fps · audio |
| Script | native Google Doc, exported as `.docx` → `intake/script.txt`; spoken lines `work/script.lines.txt`, split `work/HK1–HK3.lines.txt` + `work/BODY.lines.txt` | title line 1 ✓ · **3 hooks (A, B, C)** + body · **576 spoken words** (hooks 37 / 33 / 26, body 480) |
| Product Sheet | `stryde_product_sheet_V7.49.32.py` — newer than this branch's V7.49.31 | stored as `products/stryde/stryde_product_sheet.py` + `.md`; self-test fails only on the already-known missing files (`package_closed.jpg`, ANAT samples, `HELD_EXAMPLE`) |
| Product images | 10, byte-identical to `products/stryde/stryde_refs/` | layer 1 |
| Loom | none | no question (§18C) |
| Missing | `package_closed.jpg` (locked V7.49.27) | doesn't block steps 1–3 |

**Message fields:** `RUN MANUAL` → **RUN: MANUAL**. Everything else blank: `MODE` → **Mode 1** (realistic doctor reference, §18A); `FORMAT` → **Short VSL, doctor talking head + B-roll** (the reference's); `HOOKS` → **in script: 3** → **3 finished videos** (HK1/HK2/HK3 + the same body); `VOICE` → derived (§22D, below: the script calls the doctor "his"); `CAP` → E0 Higgsfield default; `BUILD` → `down-forwards-again`.

---

## 1. Absorption Sheet (§42)

### Part 1 — measured

| Instrument | Reading | Settles |
|---|---|---|
| Duration / aspect / res | 142.1s · 9:16 · 360×640 · 29.97fps | 9:16 locked; the download is low-res — reading layout, not texture |
| Scene cuts | **40 shots, mean 3.6s**; but the talking head holds long (S01 11.4s, S34 13.2s) while overlays change **every ~1–2s** on top of it (per-second sheets) | the edit moves by overlay, not by cut |
| Silence (−30/−40 dB) | none | wall-to-wall voice |
| VO transcript (faster-whisper small, `intake/inspo_transcript.txt`) | 494 words / 142s = **209 wpm**, one woman (the doctor), US | brisk; ours is a man at a natural pace (F9) |
| Talking head / B-roll | the doctor **seated, locked-off phone on a mount, chest-up, eye level**, white coat + stethoscope, a bright clinic behind (soft-focus); on screen ~60% of the time, under or beside the B-roll the rest | seated doctor TH is the spine |
| Shot frames + per-second sheets | `intake/frames/inspo/` | Edit Grammar below |

### Part 2 — structure map (the reference's jobs → our script)

| t (ref) | Job | Reference | Ours |
|---|---|---|---|
| 0.0–8.4 | **hook: result first, triple "without", "here's how you can do that too"** | "In four weeks, this woman lost her menopause belly without eating less, without walking more, without cutting a single carb." — before/after photos in a PiP box | **HK1**, built on the same construction (the script says so: *"the reference's construction, exactly"*) |
| — | alt hooks | — | **HK2** (the doctor against his own interest), **HK3** (the scan) — new openings, same body |
| 8.5–46.5 | the hidden cause, named by the doctor | "menopause belly is an estrogen problem… cortisol… dumps it in one place" — CGI anatomy PiPs, gauges | "Here is what her scan does not show you… a band of tendon… Seventeen times your bodyweight… Put your finger under your kneecap and press." |
| 35.9–46.5 | **"That is why…" ×3** | "That is why your belly keeps growing / the scale barely moves / you wake up bloated" — lifestyle B-roll with the doctor in a corner cut-out | "That is why she came down backwards / the chair took three tries / the good knee started going the same way" |
| 46.8–62.3 | it gets worse / what life shrinks to | "the belly gets harder… one day you stop recognizing the body" | "the list of things she said no to got longer… The long walk. The garden. Her family coming to her instead." |
| 62.5–66.7 | **"It was never X. It was never Y. It was always Z."** | "never their discipline… never their diet… always the estrogen" | "It was never how hard she tried. It was never a weak muscle. It was where the load was landing." |
| 67.1–111.2 | why the usual answers fail → the product, named | Moringa · "most on the shelf is too weak" · "93%" · She Again, bottle | "A sleeve squeezes… A hinged brace… A gel… None of them move the load. This does. It is called Stryde." + how it sits, placement, proof numbers |
| 111.6–116.0 | proof | "most people who took She Again got rid of the belly in four weeks" — review cards | "Thirty four percent less strain. Measured. Three years with orthopedic surgeons. Two hundred thousand people" |
| 116.3–134.5 | root cause vs symptoms; "you cannot out-X a Y problem" | "Cutting calories… will never outrun an estrogen problem" — a crossed-out list card | "I do not sell these…", the stairs test, "Her scan looks exactly the same", "You cannot strengthen your way out of a load problem." |
| 134.8–142.1 | offer + guarantee + "nothing to lose except…" | "I am attaching She Again… 60 day money back guarantee… nothing to lose except the belly" | "Two for one… Sixty days… From the Stryde site… Nothing to lose but the pain. Go and do your stairs." |

### Part 3 — Style Lock

- One speaker: **the doctor, seated, on a locked-off phone at eye level, chest-up**, white coat open over a shirt, stethoscope round the neck, a bright consulting room soft behind him. He speaks straight to the lens.
- The talking head is the spine; the B-roll comes **on top of him** far more often than instead of him (Part 3A). Mode 1 iPhone register throughout; real older people in real UK homes for the patient's story.
- **Changed from the reference:** a man (the script's "his"), British (physio, centimetres), a knee story instead of a belly story; the patient is one recurring woman (the reference used a different woman per shot).

### Part 3A — Edit Grammar

| ID | Device (reference) | Where | Our build |
|---|---|---|---|
| EG01 | **one-word captions**: black text on a small white box, one word at a time, position moving with the layout (top when the lower half is busy, mid-chest otherwise) | whole ad | **kept** (CapCut) |
| EG02 | **PiP box**: a B-roll clip in a box (~45% of frame width) in the lower right over the doctor's chest, thin white border, drop shadow | 0–8s (before/after), 14–24s, 30–35s | **kept** for anatomy and object inserts (`layout: pip`, lower right) |
| EG03 | **split band**: B-roll fills the lower ~40% edge to edge, the doctor above | 10.5–13s, 20–24s (CGI anatomy) | **kept** for mechanism beats (`layout: split`, 60/40) |
| EG04 | **corner cut-out**: the B-roll goes full frame and the doctor shrinks to a cut-out in the lower-left corner (~30% height) still talking | 29–35s, 36–45s, 55–59s, 67–73s, 100–111s, 128–133s | **kept** for the patient's story (`layout: cutout`, lower left) |
| EG05 | **full-frame B-roll, no doctor** | 58s, 91–93s, 96–99s, 100–102s | **kept**, sparingly (the payoff stairs shot) |
| EG06 | **overlay graphics**: gauges (ESTROGEN / CORTISOL low–normal–high), a green title bar ("93% MORINGA EXTRACT"), a red arrow pointing at a PiP, a handwritten crossed-out list, review cards, a gold 60-day seal | 30s, 50s, 73s, 78s, 96s, 112s, 121s, 136s | **kept as edit graphics (§17)**: red arrow onto the band, a crossed-out list (sleeve / hinged brace / gel), number cards for 17× / 34% / 200,000 / 60 days. Never generated |
| EG07 | **CGI anatomy** PiPs — glossy medical-render look (red/pink tissue, yellow fat, green glow for the fix) | 10–24s, 69–78s, 98–100s | **kept** in the Product Sheet's `ANATOMY_LOOK` (§12A): red = load/pain, blue = relief (§11) |
| EG08 | hard cuts, no transitions, no punch-ins, no audible music bed | whole ad | **kept** |

**`EDIT-DFA` = EG01–EG08.** Every B-roll row gets its `layout` at step 5 by this rule: anatomy/objects → `pip` or `split`; the patient's life → `cutout`; the payoff → `full`.

### Part 4 — script absorption

The body follows the reference's skeleton move for move (hidden cause → "that is why" ×3 → life shrinking → "never / never / always" → why the usual fixes fail → the product → proof → "you cannot out-X a Y problem" → offer → "nothing to lose but…"), rewritten for knees. **New content:** a physical self-test ("Put your finger under your kneecap and press"), a named mechanism (coming down vs going up), the doctor's disinterest ("I do not sell these"), and the stairs test ("One knee only… come down forwards"). HK1 copies the reference's hook construction exactly; HK2 and HK3 are new doctor-voice openers.

### Part 5 — surfaced, not absorbed

| Reference element | Disposition |
|---|---|
| A different random woman in every lifestyle shot | one recurring patient (P) — the story is hers |
| Before/after body photos with weights on them | not used (no weights, no before/after bodies); HK1 shows her on her stairs instead |
| On-screen product name/number bars generated in the image | CapCut text only (§17) |
| Review cards | not used (none supplied; would be fabricated, §43) |
| Female US doctor | male UK doctor (the script's "his"; "physio", "centimetres") |

### Part 6 — beat-it plan

| Reference weakness | Our delta | Where |
|---|---|---|
| Lifestyle shots are stock-feeling strangers | one patient, one house, one staircase — the whole ad returns to her stairs | body |
| Mechanism is asserted, never felt | the viewer presses their own kneecap on the doctor's cue — a hands-on beat on screen (the doctor does it too) | "Put your finger…" |
| 209 wpm, no air | natural doctor's pace and the house cut — clearer for a 60+ viewer | voice (F9) |
| The close is "nothing to lose except the belly" | the close is an action: "Go and do your stairs." — she walks down forwards | final beat |

### Part 7 — confirmation

Conflicts are in **Flags**. **Confirm or correct the absorption along with the avatars.**

---

## 2. Script, product, claims, locks (step 2)

### Visual Instruction Ledger (§27F) — opened

`script_lines.py --visual` found **no visual notes** in the script. The authoring notes on the hooks are logged:

| ID | Source | Instruction | Anchored | Carried by | Status |
|---|---|---|---|---|---|
| VN01 | hook label A | "Result first, triple without — *the reference's construction, exactly*" | HK1 | HK1 structure = the reference's 0–8.4s (EG02 PiP result shot + TH) | open → step 6 |
| VN02 | hook label B | "Instruction against **his** own interest" | HK2, whole build | the doctor is a man (D-DOC) | verified (cast) |
| VN03 | hook label C | "The scan" | HK3 | a knee scan in the doctor's hand / on the lightbox at step 6 (no numerals, no readouts §43) | open → step 6 |
| VN04 | script header | "Reference: facebook.com/ads/library/?id=1011702238236696" | whole build | the inspo in the folder; `EDIT-DFA` | verified |

### Phrase inventory (§27B) — dispositions are assigned at step 5

| ID | Phrase | Job | Claim | Subject / register |
|---|---|---|---|---|
| HK1-01 | In six weeks, this woman stopped coming down her own stairs backwards. | hook — result | implied outcome (F4) | P coming down her stairs forwards (PiP, EG02) · TH |
| HK1-02 | Without an operation. Without another course of physio. Without one more brace going in the drawer. | hook — triple without | — | TH · brace dropped into a drawer of braces |
| HK1-03 | And here is how you can do that too. | hook | — | TH |
| HK2-01 | I am a doctor, and I am going to tell you to do something before you come and see me about your knee. | hook — against interest | — | TH (§19B) |
| HK2-02 | It takes ten seconds and it is not a prescription. | hook | "ten seconds" (F6) | TH · the strap seated in one move |
| HK3-01 | Every week somebody brings me a scan of a knee and asks what can be done about the cartilage. | hook — the scan | — | D holding a knee X-ray up to the window light (no numerals) |
| HK3-02 | I have started answering a different question. | hook | — | TH |
| B-01 | A patient of mine. Nine years of knee pain. Bone on bone on the left, the right one following it. | problem | held (bone on bone) | P at her kitchen table · ANAT worn joint |
| B-02 | Here is what her scan does not show you. | turn | — | TH · scan |
| B-03 | Two centimetres below your kneecap there is a band of tendon about as wide as your thumb. Every step you take lands on it. Seventeen times your bodyweight. | mechanism | held (17×, post overlay) | ANAT — the patellar tendon lit red (split, EG03) |
| B-04 | Put your finger under your kneecap and press. That band is the one taking it. | mechanism — self-test | — | D's finger pressing below his own kneecap / a hand on a bare knee (hands beat) |
| B-05 | Coming down is worse than going up. Going up, your muscles lift you. Coming down, you are catching yourself, and the catch lands on that band. | mechanism | load wording (F3) | P going up (easy) vs coming down (catching) · ANAT red flash on the band |
| B-06 | That is why she came down backwards. Backwards takes the catch out. | problem | — | P coming down her stairs backwards, both hands on the rail (cutout, EG04) |
| B-07 | That is why the chair took three tries. | problem | — | P rocking to stand from an armchair |
| B-08 | That is why the good knee started going the same way. She had been leading with it for years. | problem | — | P leading with the right leg on a step |
| B-09 | And the list of things she said no to got longer every year. The long walk. The garden. Her family coming to her instead. | cost | — | walking boots by the door · the overgrown garden from the window · family arriving at her door (one-offs) |
| B-10 | It was never how hard she tried. It was never a weak muscle. It was where the load was landing. | reframe | — | P doing her physio band exercises · TH |
| B-11 | A sleeve squeezes the whole knee. A hinged brace stops it going sideways, and her knee was never going sideways. A gel sits on the skin. None of them move the load. | failed fixes | comparative (F2) | generic sleeve / hinged brace / gel tube (§10, no brand) · crossed-out list (EG06) |
| B-12 | This does. It is called Stryde. | product first appearance | name | the strap, held (`HELD_GRIPS`) — **product's first appearance** |
| B-13 | It sits two centimetres below the kneecap, on the tendon. It never crosses the joint. | product | placement | worn, `PLACE-LOCK` on P's knee |
| B-14 | A silicone pad inside holds pressure on that one band instead of spreading it round the whole knee. The weight gets caught and moved off the worn part before it reaches the joint. | mechanism | held (pad) · load-path wording (F3) | ANAT: strap on the tendon, red → blue |
| B-15 | The placement is the whole thing. A centimetre too high and it is a sleeve again. | product | — | D pointing to the spot on a knee model |
| B-16 | Thirty four percent less strain. Measured. Three years with orthopedic surgeons. Two hundred thousand people wearing one. | proof | held ×3 (post overlays) | number cards (EG06) · surgeon one-off (§19B) |
| B-17 | Ten seconds to put on. No sores, no rolling down, and nobody can see it. | feature | **F6** (ten seconds, no sores) | P seats it in one move (`SEAT_LOCK`) · under a skirt/trousers (§9D conceal) |
| B-18 | I do not sell these and I make nothing from saying this. I say it before we talk about anything else, because it is the cheapest thing on the list and the only one aimed at the band. | authority | **F5** (disinterest, "cheapest", "only one") | TH |
| B-19 | You do not have to take my word for it. One knee only. Leave the other bare. Go to your own stairs and come down forwards. You will know in a minute. | test / CTA | implied outcome (F4) | P's feet at the top of her stairs, one knee strapped |
| B-20 | Not because the arthritis has gone. Her scan looks exactly the same as it did in March. I have both of them. Because the load is not landing on that band any more. | proof | F3 | D holding two X-rays side by side (identical, no numerals) |
| B-21 | You cannot strengthen your way out of a load problem. You have to move the load. | reframe | — | TH |
| B-22 | Two for one, so you do both knees, which is what she needed. Sixty days, and you keep the straps. From the Stryde site. The copies stretch, and a stretched strap stops holding the spot. | offer / objection | held (BOGOF, 60 days) · **F7** ("keep the straps", copies stretch) | open box, two straps · a stretched generic copy (§10) |
| B-23 | Nothing to lose but the pain. Go and do your stairs. | close | — | TH · **P coming down her stairs forwards, hands free** (full, EG05) |

Coverage: 7 hook + 23 body phrases · **uncovered 0 · blocked 0** (dispositions at step 5).

### Claims (§43A)

Held in the Product Sheet register (user-confirmed V7.49.29): 17× bodyweight through the spot · the pad · 34% less strain (sports scientists, measured) · three years with orthopaedic surgeons · bone on bone · 200,000+ wearers · Buy 1 Get 1 Free · 60-day money-back guarantee. Numbers are post overlays, never generated (§17). **Not in the register:** F2, F4, F5, F6, F7 — voiced verbatim (§22U), listed in Flags.

### Mode & Model Lock (§18A)

| Beat class | Model · params | Why |
|---|---|---|
| Mode | **Mode 1 Realistic**, iPhone 17 Pro Max, 9:16 | realistic reference |
| Avatar sheets | `gpt_image_2_5` · `variant: sunburst` · `quality: high` · `resolution: 2k` | §19 measured route (**used this delivery**) |
| Talking-head seed (D seated in his consulting room) | `nano_banana_pro` | talking-head seed class |
| Wordmark with hands or a body (held, worn, seating) | `nano_banana_pro` + `WORDMARK-LOCK` | rule 7 |
| Wordmark, no person (open box) | `nano_banana_pro` | wordmark |
| Volume B-roll with a person, no readable wordmark | `nano_banana_2` | volume |
| Anatomy (EG07) | `nano_banana_2` | §12A |
| Video (B-roll) | Kling 3.0 (`kling-video-v3_0_omni`), start image, `prefer_multi_shots: false` | §4, §27G |
| Voice | §22U: Kling source takes (2+) → ElevenLabs clone (API) → Enhance → `eleven_v4` → house cut | §22U |
| Talking heads | HeyGen Avatar V driven by the VO, motion prompt on every render | §22U step 13 |

**Other locks:** format **seated doctor TH + B-roll in `pip` / `split` / `cutout` / `full` layouts** (`EDIT-DFA`); **side: left knee — proposed (F8)**; mechanism claim: **protection**; hooks: **3, in script → 3 finished videos**.

---

## 3. Cast (step 3) — generated, on the board for your check

Everyone with two or more beats gets a sheet. **Two:** **D-DOC** the doctor (narrator, on camera in every talking head) and **P-PATIENT** his patient (every story beat). One-offs (her family at the door, the surgeon on B-16, the hand-model wearers) are cast at step 5 per §13.

| Sheet | Job ID | File | Board |
|---|---|---|---|
| D-DOC | v2 `71b20c5a-f8ef-48d8-8645-f5685a4a92b6` (v1 `4623967d…` → Old board) | `cast/D-DOC_v2.png` (1520×2688) | To check |
| P-PATIENT | `02333782-0c9a-4696-b3f1-fcc7480fe8db` | `cast/P-PATIENT_v1.png` (1520×2688) | To check |

Manual run: the sheets are **not checked by me** (§18B step 3) — Confirm or Fix each on the board. Prompts: `cast/<ID>.prompt.txt`, built from Appendix A by ID in `cast/build_sheets.py` (`CAM-LOCK` → `AVATAR-SHEET` + `SHEET-GRID` → face fill (+ `APPROACH-PRO` for D, §19B) → `SKIN-T` → `CAP-SHARP` → `CAP-FILE` → `NEG-SHEET` + `NEG-GRID` + `NEG-FILE` + `NEG-DEFAULT-FACE` (D: last two clauses dropped, §19B)), 9,983 (v2) / 9,466 chars. Spend: 3 Sunburst jobs (D-DOC v1 + v2, P), one render each (Higgsfield 17,998.5 before).

### Identity strings — read off the renders (§7)

| ID | Identity string |
|---|---|
| D | white British man, 54, medium height, stocky and broad through the chest; broad square face, light blue-grey eyes, short nose, fair ruddy freckled skin; short sandy-red hair greying at the sides, side parting, clean-shaven; white knee-length coat open over a pale blue shirt (open collar, no tie), black stethoscope round the neck, charcoal trousers, brown leather lace-ups |
| P | white British woman, 69, short and petite, slight stoop; small fine-boned oval face, pale grey-blue eyes, small straight nose, thin upper lip, a small mole above the right corner of the upper lip; chin-length layered hair dyed chestnut brown with silver roots at the parting, tucked behind the ears; duck-egg blue crew-neck jumper, knee-length navy-and-cream check wool skirt, flesh tights, dark brown suede ankle boots |

### §19A axis tables

| Axis | D | P |
|---|---|---|
| Face | broad square, wide-set blue-grey eyes, snub nose | small, fine-boned oval, pointed chin |
| Hair | sandy-red greying, short, side parting; clean-shaven | chestnut dye, silver roots, chin-length layers |
| Age position | 54 | 69 |
| Build | medium height, stocky, broad chest | short, petite, stooped |
| Class / wardrobe | clinician: white coat, shirt, stethoscope | home: knit jumper, check skirt, tights |
| Marker | flat brown mole high on the right cheekbone | mole above the right upper lip |
| Voice | British, measured GP (below) | none (no lines) |
| Environment | consulting room | her house — stairs, kitchen, armchair |

**Clearance:** D–P differ on 8 axes ✓. Against the roster (stryde-identity, stryde-lost-moments, stryde-regrets, stryde-three-regrets, stryde-71-stairs): the white British men on file (identity N 60 long oval face, wavy dark-grey hair and beard; identity C2 58 round face, shaved head; regrets C1 67 long lean face; regrets C3 72 round, white hair) share no face architecture, hair or build with D (square face, sandy-red hair, clean-shaven, stocky); P's nearest is regrets N (white British woman, 62, slim) — different face (long narrow vs small oval), hair (silver bob vs chestnut dye with roots), build (tall upright vs petite stooped), wardrobe, marker ✓. D is §19B approachable (`APPROACH-PRO`, the sheet's no-smile kept).

### Doctor — `VOICE-DOC` (§22D) and §20 constraint sheet

**`VOICE-DOC`** (goes verbatim into every §22U step-2 take, inside Kling's 2,500 limit)
```
A white British man in his mid-fifties, a family doctor from the north of England: a warm, clear, mid-low voice with a light Yorkshire accent and no put-on polish. Speaks the way he talks to one patient across his desk — unhurried, plain, certain, a little dry; short sentences land and stop. Statements fall at the end, never up. Stress comes by slowing down and dropping lower, never by getting louder. Never a newsreader, never a salesman.
```

| Field | D — the doctor |
|---|---|
| Accent | light Yorkshire English; never RP newsreader, never a broad comedy accent |
| Pacing | measured, ~150–160 wpm before the house cut (the reference runs 209) |
| Posture / rest / gesture / ocular / rig | **seated** at his consulting-room desk, phone on a small tripod across the desk at eye level, chest-up (EG spine); hands resting on the desk edge, free for one Economical gesture a line; eyeline on the lens; framed at steps 4–5 |
| Audio proximity | R1 (phone ~1 m across a desk) |
| Wardrobe never-list | no tie, no scrubs, no name badge with a readable name (§19B: generic role, not a real clinician) |
| Physical never-list | never wears the strap himself on camera; hands only on a knee model or his own knee through the trousers on B-04 |
| Voice spec | `VOICE-DOC` above |
| Stress register | slower and lower on "Seventeen times your bodyweight." / "It was where the load was landing." / "Go and do your stairs." |
| Non-speech events | one short breath before "Here is what her scan does not show you." Nothing else |
| Mouth asymmetry | read off the voice-source frame at the voice stage |
| Voice name (§22U step 7) | `DownForwards-Doctor` (proposed) |

---

**Recast 2026-09-28 (user: "USE BRITISH ETNICITY"):** D-DOC v1 (British South Asian) → v2 white British man, 54; v1 kept on the Old board. P was already white British. §34: `VOICE-DOC` and the identity string updated; nothing else built on D yet.

## Flags (decisions for the user — nothing below was changed silently)

| # | Where | Finding | Recommendation |
|---|---|---|---|
| F1 | Inspo | The folder's video is the **menopause/Moringa doctor ad**, not a knee ad; it's the "Reference" link in the script | Used as the **format and edit** reference (Parts 2–3A); nothing product-specific carried over |
| **F2** | B-11 | "A sleeve squeezes the whole knee… A hinged brace… A gel sits on the skin. None of them move the load." — comparative against other product types, not in the register | Voiced as written; shown as generic unbranded items (§10). Please confirm |
| F3 | B-05, B-14, B-20, B-21 | "the weight gets caught and moved off", "move the load" — load-path wording; the Product Sheet's one claim is **protection** (load-path retired) | Voiced verbatim; **pictured as protection** — the pad holding the spot, red → blue relief, no arrows carrying force elsewhere |
| **F4** | HK1-01, B-19 | "In six weeks, this woman stopped coming down her own stairs backwards" / "You will know in a minute" — implied outcome claims | Voiced as written. Please confirm |
| **F5** | B-18 | "I do not sell these and I make nothing from saying this… the cheapest thing on the list and the only one aimed at the band" — a disinterest statement by a generated doctor + "cheapest" / "only one" comparatives | Voiced as written; the doctor stays a generic role, no name, no clinic name (§19B). **Please confirm the advertiser holds it** |
| F6 | HK2-02, B-17 | "ten seconds", "No sores, no rolling down" — not in the register | Voiced; please confirm |
| F7 | B-22 | "you keep the straps" (guarantee terms) and "The copies stretch" — not in the register | Voiced; the copy shown as a generic stretched strap (§10); terms in the edit only as you supply them |
| **F8** | Side | Script: "Bone on bone on the **left**, the right one following it" — the left is her bad knee; the sheet's `side_from_script()` finds no "left knee" phrase and defaults right | **Left knee** (the one the story is about). Cost: the 3 left-knee worn references (`worn_ref_prompts('left')`) at step 4 before any worn beat — a right frame is never mirrored (wordmark). Say "right" to keep the locked references instead |
| F9 | Length | 576 words. At a natural doctor's pace and the house cut each video lands around **3:25–3:45** (hook ~12–15s + body ~3:15), vs the reference's 2:22 at 209 wpm | Keep the natural pace (my recommendation for a 60+ audience); or say "match the reference's speed" |
| F10 | Hooks | HK1 is the reference's construction; HK2, HK3 new | 3 finished videos, one per hook |
| F11 | `package_closed.jpg` | still missing | open box only |

## Next — on your go (§18B step 5)

Confirm or Fix each avatar on the board and answer F2, F4, F5, F8 (and anything else). Then steps 4–5 as one delivery: the consulting room (doctor TH plate) and her house (stairs, kitchen, living-room armchair, garden window) + the left-knee worn references if F8 stands; act map + wardrobe map with every phrase assigned an `EDIT-DFA` layout; `angles.py` pass. Then the voice stage straight through (§22U: Kling source takes → clone → VO for HK1–3 + body → HeyGen talking heads → trim).
