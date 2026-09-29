# Build Sheet — stryde-thirty-years

**STRYDE Precision Strap · "C - VID | Talking Head | TOF | Maker Concession | New | Thirty Years Making Braces"** · Standards V7.64.2 · **RUN: MANUAL** · 2026-09-28

Steps 1–3 of §18. **Stopped at the avatar review (§18B, V7.62.0)**: steps 4–5 wait for your go.
Board: https://claude.ai/artifact/EG999Jm7UoVdq5YAY7iafV

---

## 0. Intake (§18B)

| Input | Found | Notes |
|---|---|---|
| Drive folder | `1yO_Hjayp5pbXc2AfvbAXeXZTj_jdzcpi` | downloaded to `intake/` (gitignored). No OUTPUT subfolders in it |
| Inspo 1 (**primary**) | `inspo_hook.mp4`: the script's own `Reference:` link (instagram.com/p/DWLADFygI0W, "Video by trylymphoria") | 89.8s · 9:16 · 720×1280 · 30fps · audio |
| Inspo 2 (secondary, body edit) | `inspo_body.mp4`: STRYDE's own "go and do your stairs, love" grandmother ad | 267.3s · 9:16 · 1080×1920 · 30fps · audio |
| Script | `C.docx`: title on line 1 ✓ · 3 hooks + 19 body lines · 3 visual notes · 1 reference link | inferred as the script (only document) |
| Product Sheet | `stryde_product_sheet_V7.49.29.py` | **older than the repo's `products/stryde/` (V7.49.31)**. The only difference is the anatomy-look samples (V7.49.30–31), so the repo copy stays in use |
| Product images | 10: `front.webp`, `back.webp`, `product_tq_left/right`, `product_side`, `product_macro`, `worn_front/bent/rear`, `package_open` | identical set to `products/stryde/stryde_refs/` (layer 1) |
| Loom | none | optional: no question |
| Missing | `package_closed.jpg` (same as the last build) | does not block steps 1–3 |

**Message fields read:** `RUN MANUAL` → Manual. **`BRITISH`** → applied to the cast and the voice: every character is cast white British and the maker speaks with a placed British regional accent (it agrees with the Product Sheet's "British, roughly 55–80"). `MODE` blank → **Mode 1** (a realistic reference selects it, §22, §18A). `HOOKS` blank → **3, in the script** → 3 finished videos (§30H). `CAP` blank → E0 Higgsfield default. `VOICE` blank → derived (§22D), British.

---

## 1. Absorption Sheet (§42)

**Two inspos, two jobs.** The primary (`inspo_hook`) is the **script's skeleton**: our script is written slot for slot against it (below). It is one unbroken 90s selfie take with no B-roll. The secondary (`inspo_body`) is **STRYDE's own winning ad**, and it gives the body's edit: talking head to camera cut with B-roll every ~2.7s, CGI anatomy on the mechanism lines, the product in hand. Per the file names you chose, **the hooks copy inspo 1 and the body copies inspo 2's edit.** Inspo 1 alone would make the whole ad a single talking head with no B-roll; say so if you want that.

### Part 1: measured

| Instrument | Inspo 1 (primary, hook) | Inspo 2 (body edit) | Settles |
|---|---|---|---|
| Duration / aspect / res | 89.8s · 9:16 · 720×1280 · 30fps | 267.3s · 9:16 · 1080×1920 · 30fps | 9:16 locked |
| Scene cuts | **1 shot, 0 cuts** (one continuous take) | **90 shots, mean 2.97s, median 2.67s** (0.77–9.97s); first two shots 10.0s and 8.6s (the walking hook), then ~2–4s cuts to the end | hooks: one held selfie take; body: a cut every ~2.7s |
| Silence −30 dB / −40 dB | 10 gaps of 0.3–0.4s (sentence ends) / 3 | 5 gaps in the first 15s / **none** | wall-to-wall speech; no held beats |
| Volume | mean −18.0 dB, max −1.8 dB | mean −22.3 dB, max −3.6 dB | hot, compressed phone VO |
| Transcript (faster-whisper small) | 322 words / 89.7s = **215 wpm** | 811 words / 267.3s = **182 wpm** | pace: see voice |
| TH / B-roll | 100% TH | ~35% TH / ~65% B-roll (**read off the sheets, not measured**) | body density |
| Shot frames + per-second sheets | `intake/frames/inspo_hook/` (3 sheets) | `intake/frames/inspo_body/` (180 frames, 9 sheets) | Edit Grammar below |
| OCR | not run; overlays read off the frames | not run; read off the frames | **read, not measured** |

### Part 2: structure map

**Inspo 1:** one selfie take, walking slowly then standing, in her workplace (a lab), white coat.

| t | Job | Line (theirs) | Overlay |
|---|---|---|---|
| 0.0–~6 | **HOOK + authority permission** | "Here's how to drain your lymphatic system the right way, and if you don't believe me, I'm a pancreatic cancer researcher, so biology is my thing." | **two stacked title cards** (white box, black text: the topic; magenta box, white text: the credential), ~6s, then gone (EG01) |
| ~6–24 | benefits / agitate | puffy face, belly, cellulite… "all that goes away" | word captions (EG02) |
| ~24–35 | **what fails** | "hundreds of dollars on massages, gua sha, jade rollers, dry brushes. That's better than nothing, but the fluid always pools back" | captions |
| ~35–55 | **mechanism: three things** | "you have to drain it from the inside, and there are three herbs…" one, two, three | captions |
| ~55–65 | **copies objection** | "most supplements use weak doses… load up on fillers" | captions |
| ~65–85 | product + proof + offer + guarantee | "That's why I only take…", tested, 70% off, 60-day money-back | captions |
| ~85–90 | CTA | "Grab it while you can" | captions |

**Inspo 2:** hook walking on a lane (10s + 8.6s) → TH at the foot of her stairs, cut with B-roll: drawer of failed supports · consultant scene · CGI knee anatomy with the glowing spot on the tendon (mechanism) · product in hand (wave, "sits on the tendon") · stairs forwards (result) · copies on a table ("they stretch") · two straps held up (offer) · "go and do your stairs, love".

### Part 3: Style Lock (copied)

- **Delivery:** one expert speaking straight to the phone, first person, sure of himself, brisk (inspo 1: 215 wpm; inspo 2: 182 wpm). Ours: **~190 wpm**, between the two, a notch down for the older audience.
- **Hook:** selfie at arm's length in the speaker's own workplace, credential stated in the first sentence and repeated on a title card; no B-roll in the hook.
- **Body edit rhythm:** a cut every ~2.7s, talking head returning between B-roll runs; the mechanism is always shown (CGI anatomy); the product always in hand when it's named.
- **Visual grammar:** handheld phone, real rooms, daylight; hands and knees for proof; the speaker's workplace is the credibility (§19).
- **Retention:** credential-first hook ("if you don't believe me…"); "what fails" list; "three things" countdown; copies objection before the offer; "don't take my word for it" self-test close.
- **Capture axis (never yields):** iPhone 17 Pro Max register (§22).

### Part 3A: Edit Grammar → `EDIT-STRYDE-THIRTY-YEARS`

| ID | Device | Where | When used | Parameters |
|---|---|---|---|---|
| EG01 | **title cards**, two stacked | inspo 1 @ 0:00–~0:06 | hook: topic + credential | upper-middle (~28–33% height), full-width stacked boxes: box 1 white with black bold sentence case, box 2 coloured with white bold. **Our script sets the colours: white + red** (VN01); **HK1 only** (VN02 says none on HK2) |
| EG02 | **word captions**, one highlighted word | inspo 1, throughout | every spoken line (hooks) | centred at ~55–60% height, white bold caps with black outline, 2–5 words a line, the current word on a dark green box |
| EG03 | **line captions** | inspo 2, throughout | every spoken line (body) | centred at ~75% height, white bold lowercase with a thin black outline, one line of 3–7 words, no highlight |
| EG04 | **full** B-roll, hard cut | inspo 2, ~65% of shots | proof, product, result, list lines | full frame, hard cut, 1–4s runs |
| EG05 | TH selfie, static, returns between B-roll | inspo 2, ~35% of shots | turn lines, claims, CTA | chest-up handheld selfie, eyeline on lens, the same set every time |
| EG06 | **CGI anatomy** | inspo 2 S27–S40 | mechanism lines (the spot, 17×, 2 cm, 34%) | full-frame translucent leg on black, glowing spot on the tendon; our §12A anatomy register (`ANAT-A`/`ANAT-B`) |
| EG07 | hands-to-camera product | inspo 2 S62–S68 | product named / feature lines | hand holds the strap to the lens, wave to camera |
| — | not used by either inspo | — | — | no split-screen, no PiP, no punch-ins, no transitions other than the hard cut, no speed ramps, no SFX heard, no music heard |

**Light / focus / angles (read off the frames):** daylight from a side window, even and soft, never moody (inspo 2 has one lamp-lit night shot); phones deep, nothing shallow except the product close-ups; selfie eye-level for TH, B-roll spread across eye, high (drawer, table) and ground (stairs, feet).

### Part 4: script absorption

**Copy formula (reference):** credential hook ("if you don't believe me, I'm a…") → what it fixes → what fails and why ("better than nothing, but…") → the real mechanism in three parts → copies objection → "that's why I only…" + proof → offer + guarantee → CTA.

**Beat map: their `R-P` row → our line.** The script was supplied already rewritten slot for slot, so it is not edited (§42 Part 4 scope):

| R-P | Inspo 1 | Job | Our line |
|---|---|---|---|
| R-P-001 | "Here's how to drain your lymphatic system the right way, and if you don't believe me, I'm a … researcher, so biology is my thing." | hook + credential | **HK1** ("… Load is my job.") · HK2 and HK3 are new variants of the credential open |
| R-P-002 | puffy face, belly, cellulite | agitate / benefits | P-001–P-004 (17×, the spot, what taking the load off gives you, what leaving it costs) |
| R-P-003 | "massages, gua sha, jade rollers… better than nothing, but the fluid always pools back" | what fails | P-005–P-008 (sleeves, hinged braces, gels, wraps… "better than nothing… comes back to the same spot") |
| — | — | permission (added) | P-009 ("that was not you failing") |
| R-P-004 | "drain it from the inside, and there are three herbs you need" | mechanism, three things | P-010–P-013 (under the joint; placement, pad, band) |
| — | — | proof (added) | P-014 (34%, measured) |
| R-P-005 | "most supplements use weak doses… fillers" | copies objection | P-015 |
| R-P-006 | "That's why I only take…; third-party tested, made in the USA" | product + proof | P-016 ("The one I hand people is Stryde…") |
| — (inspo 2) | "don't take my word for it… put one on, go to your own stairs… you'll know in a minute" | self-test | P-017–P-018 |
| R-P-007 | "70% off, 60-day money-back guarantee" | offer + guarantee | P-019 |
| R-P-008 | "Grab it while you can" | CTA | P-020 ("Go and do your stairs.", inspo 2's close) |

**Voice fingerprint:** first person, plain, short declaratives and fragments ("Sleeves. Hinged braces. Gels. Wraps."), no contractions in the script ("I have", "do not"), numbers in words, the product named once, late ("The one I hand people is Stryde"). The no-contraction style is the script's and is voiced as written.

**Length:** hooks 29 / 18 / 25 words, body 349 words. At ~190 wpm each finished video is **≈ 1:56–2:00** (HK1 + body 1:59 · HK2 1:56 · HK3 1:58), longer than inspo 1 (90s) and shorter than inspo 2 (4:27).

### Part 5: surfaced, not absorbed

| Reference element | Disposition |
|---|---|
| Inspo 1's lab, white coat, health claims (lymphatic, toxins), "made in the USA", "70% off" | replaced: our maker, his workshop, our held claims, our offer (Buy 1 Get 1 Free) |
| Inspo 2 names Amazon and Facebook; shows a consultant with an X-ray | not used: our script says "not a marketplace", so no platform name or UI is generated (§10A) |
| Inspo 2's CGI anatomy | position-not-look → our `ANAT-A` / `ANAT-B` register (Product Sheet §17 anatomy looks) |
| Captions (EG02, EG03) | style copied; our words; added in CapCut, never generated (§17) |

### Part 6: beat-it plan

| Reference weakness | Our delta | Beats |
|---|---|---|
| Inspo 1 never shows the mechanism (no B-roll at all) | inspo 2's anatomy + product close-ups on every mechanism line | P-001–P-002, P-010–P-013 |
| Inspo 1's credential is a job title only | a maker whose workshop proves it: rail of finished braces, a brace in the vice, a sleeve cut in half on the bench (VN01–VN03) | HK1–HK3 |
| Inspo 1's "what fails" is a spoken list only | each failed support seen on the bench as it's named | P-005–P-007 |
| One hook | three hook variants on the same body | HK1–HK3 |

### Part 7: confirmation

Conflicts are in **Flags** at the end. **Confirm or correct the absorption with the avatars.**

---

## 2. Script, product, claims, locks (step 2)

### Visual Instruction Ledger (§27F), opened

| ID | Source | Instruction | Line | Carried by | Status |
|---|---|---|---|---|---|
| VN01 | script L4 | Selfie, arm's length, walking slowly through the workshop; a rail of finished braces racks past behind the shoulder. Two stacked title cards, six seconds only: white box "Where knee pain actually comes from", red box "From a man who has made knee braces for 30 years." | HK1 | TH walking selfie (§22F `FRAME-WALK`) · title cards EG01 in CapCut, verbatim | open → step 5 · **F5** |
| VN02 | script L6 | Static selfie, seated at the bench, a half-finished hinged brace clamped in the vice beside his face. He does not touch it. No title cards at all. | HK2 | TH static selfie; unbranded hinged brace, half-built | open → step 5 |
| VN03 | script L8 | Opens tight on two halves of a cut sleeve lying on the bench, still curled. Hand enters, lifts one half to camera, then pulls back to reveal him and the workshop. | HK3 | B-roll insert (maker's hand) → TH; unbranded sleeve | open → step 5 · F6 |

### Phrase inventory (§27B): dispositions assigned at step 5

| ID | Phrase | Job | Claim | Subject / register |
|---|---|---|---|---|
| HK1 | "Here is where your knee pain is actually coming from. And if you do not believe me, I have spent thirty years making knee braces. Load is my job." | hook | persona (F4) | C1 maker, walking selfie |
| HK2 | "I have made knee braces for thirty years. I am about to talk you out of buying one." | hook | persona (F4) | C1, seated at the vice |
| HK3 | "This is a knee sleeve I cut in half this morning. I want to show you why the one in your drawer never helped you." | hook | — | C1 hand + sleeve → C1 |
| P-001 | Seventeen times your bodyweight goes through one spot below your kneecap. Every step. | mechanism | 17× (held) | ANAT |
| P-002 | Two centimetres down, on the tendon. Not the cartilage. Not the joint. That spot. | mechanism | placement fact | ANAT · maker's finger on a knee |
| P-003 | Take the load off it and you come down the stairs forwards. Out of a chair first try. The dog as far as you used to. | result | — | **S1 wearer**: stairs · chair · dog |
| P-004 | Leave it there and the list of things you have stopped doing keeps growing. | agitate | — | TH |
| P-005 | Here is what I have watched fail for thirty years. Sleeves. Hinged braces. Gels. Wraps. I have sold plenty of them, and they are better than nothing. | what fails | persona (F4) | unbranded supports on the bench, one per word |
| P-006 | But the pain comes back to the same spot, because none of them move the load off it. | mechanism | comparative (F3) | ANAT |
| P-007 | A sleeve squeezes the whole knee. A hinged brace stops your knee going sideways, and your knee was never going sideways. | what fails | comparative (F3) | sleeve / hinged brace on a knee |
| P-008 | So if you have a drawer full of these, that was not you failing. You were wrapping the wrong part of your leg. | permission | — | drawer of supports · TH |
| P-009 | You do not wrap the joint. You go under it. Three things have to be right. | mechanism | — | TH, product in hand |
| P-010 | One, the placement. Two centimetres below the kneecap, on the tendon, never over the joint. | mechanism | placement fact | worn, front (`PLACEMENT_REFERENCES`) |
| P-011 | Two, the pad. Silicone, holding pressure on that one spot instead of spreading it round the whole knee. | mechanism | pad (held) · F2 | pad close-up (`PAD_BACK_SHOT`) · ANAT |
| P-012 | Three, the band. It catches your weight coming down and moves it off the worn part before it reaches the joint. | mechanism | protection | band close-up · ANAT |
| P-013 | Thirty four percent less strain. Measured. | proof | 34% (held) | S1 worn, stairs · 34% overlay |
| P-014 | Most straps that look like this are copies. Thin elastic, foam pad, no tension. They stretch, and a stretched strap stops holding that spot. | copies | comparative (F3) | blank near-copies on the bench (§10 archetypes) |
| P-015 | The one I hand people is Stryde. Three years with orthopedic surgeons. Two hundred thousand wearing one. Ten seconds on, no sores, no rolling down. | product + proof | held · "ten seconds on" F3 | maker hands the strap to camera · seating beat |
| P-016 | Do not take my word for it. One knee only. Leave the other bare. Go down your own stairs. You will know in a minute. | self-test | — | TH · S1 stairs, one knee strapped |
| P-017 | Not because the arthritis is gone. Because the force is not landing where it hurts. | honesty / mechanism | protection | TH · ANAT |
| P-018 | Two for one, so you can do both knees. Sixty days, and you keep the straps. From the Stryde site, not a marketplace. | offer | BOGOF, 60 days (held) · "keep the straps" F3 | two straps in hand / open box · offer card |
| P-019 | Go and do your stairs. | CTA | — | TH |

Hooks 3 · body 19 phrases · **uncovered 0 · blocked 0** (dispositions pending step 5).

### Claims (§43A)

**Held** (Product Sheet claim register, user-confirmed V7.49.29): 17× bodyweight · three years with orthopaedic surgeons · the silicone pad · 34% less strain, measured · protection mechanism · 200,000+ wearers · Buy 1 Get 1 Free · sixty-day money-back. Placement "2 cm below the kneecap, on the tendon" is the Product Sheet's own placement spec. Numbers are post overlays, never generated (§17). **Not in the register:** F3, F4.

### Mode & Model Lock (§18A)

| Beat class | Model · params | Why |
|---|---|---|
| Mode | **Mode 1 Realistic**, iPhone 17 Pro Max, 9:16 | realistic references (§22); no Mode 4/5 instruction |
| Avatar sheets | `gpt_image_2_5` · `variant: sunburst` · `quality: high` · `resolution: 2k` | measured route (§19). **Used this delivery** |
| Talking-head seeds (every TH look) | `nano_banana_pro` | §18A default; rule 7 (no GPT Image with a body) |
| Wordmark with hands or a body (strap in hand, worn, seating) | `nano_banana_pro` | the wordmark must read |
| Wordmark, no person (box, straps on the bench) | `nano_banana_pro` | |
| Volume B-roll with a person, no wordmark (failed supports, stairs wide, dog walk) | `nano_banana_2` | volume |
| Mechanism (`ANAT-A`, `ANAT-B`) | `nano_banana_2` | classifier threshold; never GPT Image |
| B-roll video | Kling 3.0 (`kling-video-v3_0_omni`), start image, `prefer_multi_shots: false` | §4, §27G |
| Voice | §22U: 2+ Kling voice-source takes → ElevenLabs clone (you, in the app) → `eleven_v3` TTS | §22U |
| Talking heads | **HeyGen Avatar V**, audio upload, 9:16, 1080p, motion prompt on every render | §22U step 13 |

**Other locks:** format **talking head + B-roll** (the title says Talking Head; the body edit copies inspo 2, EG04–EG05) · **side: right knee** (no knee named → `SIDE_RULE`) · mechanism claim: protection · edit: `EDIT-STRYDE-THIRTY-YEARS` · hooks: 3 in script → 3 finished videos · Voice name keyword (§22U step 7): `Thirty` (title "Thirty Years Making Braces").

---

## 3. Cast (step 3): generated, on the board for your check

Recurring subjects (≥ 2 beats): **C1 maker** (every hook, every TH, his hands on the bench beats) · **S1 wearer** (P-003 stairs/chair/dog, P-013, P-016). One-offs (not sheeted, §13): knees in the "what fails" beats.

| Sheet | Job ID | File | Board |
|---|---|---|---|
| C1-MAKER | `a866e6f7-c3d3-4f10-9902-02b1d62c0b41` | `cast/C1-MAKER_v1.png` (1520×2688) | To check |
| S1-WEARER | `7cc9a07d-c775-49ee-9e06-1d959a496260` | `cast/S1-WEARER_v1.png` (1520×2688) | To check |

**Not checked by me (Manual: the check is yours).** Prompts: `cast/<ID>.prompt.txt`, built from Appendix A by ID in `cast/build_sheets.py` (`CAM-LOCK` → `AVATAR-SHEET` + `SHEET-GRID` → `SKIN-T` → `CAP-SHARP` → `CAP-FILE` → `NEG-SHEET` + `NEG-GRID` + `NEG-FILE` + `NEG-DEFAULT-FACE`), 9,350 / 9,278 chars. Spend: 2 Sunburst jobs, 13.5 Higgsfield credits (19,921.75 → 19,908.25).

**Markers.** `NEG-SHEET` bans birthmarks and skin patches, so the markers are structural: the maker's broken, crooked nose; the wearer's prominent ears.

### Identity strings (read off the renders, §7; descriptions, not a verdict)

| ID | Identity string |
|---|---|
| C1 | white British man, 62, short and wiry; narrow hollow-cheeked face, long jaw, deep-set pale grey-blue eyes, deep forehead creases; long hooked nose; thick grey moustache; thin grey hair combed back, receding, scalp showing at the crown; green-and-brown check flannel shirt, sleeves rolled; faded navy canvas work apron, well worn; grey work trousers; brown leather work boots |
| S1 | white British woman, 69, tall and lean; long angular face, high cheekbones, wide-set pale blue eyes, strong straight nose, thin wide mouth; prominent ears; chin-length straight bob, dark brown grown out with a wide silver parting; mustard-yellow crew-neck jumper; navy corduroy mini-length A-line skirt (well above the knee), both knees bare; tan leather Chelsea boots |

### §19A axis tables: clearance against the roster

Roster (repo): `stryde-identity`: N (60, Tyneside narrator), C1 Maureen (74), C2 Dean (58, trades), C3 Pat (66), C4 surgeon (71). `intake-1` generated none.

| Axis | C1 maker | S1 wearer |
|---|---|---|
| Face | narrow, hollow-cheeked, long jaw, deep-set eyes | long, angular, high flat cheekbones, wide-set eyes |
| Hair | thin grey, combed back, scalp showing + grey moustache | chin-length bob, dark dye grown out, silver roots |
| Age position | 62 | 69 |
| Build | short, wiry | tall, lean, slight stoop |
| Class / wardrobe | trades (bracemaker's workshop apron) | country-casual (jumper, cord skirt, ankle boots) |
| Marker | broken, crooked hooked nose | prominent ears |
| Voice | Black Country (below) | non-speaking |
| Environment | brace workshop: bench, vice, rail of finished braces | home stairs, armchair, dog |

**Pairwise clearance (of 8; voice counts only between speakers):**

| vs | N | C1 Maureen | C2 Dean | C3 Pat | C4 surgeon |
|---|---|---|---|---|---|
| C1 maker | **7** (age close) | 7 | **6** (class: trades) | 7 | **6** (hair: thinning vs bald crown) |
| S1 wearer | 7 | 7 | 7 | **6** (age close) | 7 |

C1–S1: 7. **Every pair clears the gate of 5.**

### C1 maker: `VOICE-MAKER` (§22D) and §20 constraint sheet

**`VOICE-MAKER`** (compressed, to go verbatim into every §22U step-2 take; the clone inherits it)
```
A man of sixty-two from the Black Country, Walsall, a dry, flat, slightly nasal voice, level and unhurried but never slow. Statements fall and stop dead, no lift at the end; Black Country vowels, "I" close to "oi", dropped h's, glottal t's. A short dry sniff of a laugh before a put-down. Stress: slower and flatter on the turn, never louder.
```

| Field | C1 maker |
|---|---|
| Accent | Black Country (Walsall), placed and unforced; never Brummie caricature, never RP, never northern |
| Pacing | ~190 wpm in the hooks and lists, level; one notch slower on "that was not you failing" and "Not because the arthritis is gone" |
| Posture rules | a craftsman at ease in his own shop: shoulders loose, weight settled; never leans into the lens, never salesy |
| Rest position | forearms on the bench edge (seated) or free hand at the apron pocket (walking), inside the frame |
| Gesture register | **Economical** (§28B); Restrained on every held-product beat (§28D) |
| Ocular default | anchored on lens; breaks down-left to the bench on "what fails" lists, back on the turn |
| Camera rig | selfie, front camera (`CAM-FRONT`, §22F): R2 handheld walking (HK1), R2 static seated (HK2, body TH) |
| Audio proximity | R2 |
| Wardrobe never-list | white coat, scrubs, suit, tie, anything clinical, anything branded |
| Physical never-list | never wears the strap himself; never adjusts the band (`ADJUSTABLE_RULE`); never touches the brace in the vice on HK2 (VN02) |
| Eyeline | locked to lens in every act |
| Voice spec | `VOICE-MAKER` above |
| Stress register | quieter and flatter on the turn word; a dry pause before "Load is my job." |
| Non-speech events | one short dry sniff-laugh (at most once per act); a breath out through the nose before a number. Nothing else |
| Mouth asymmetry | read off the close-up: the moustache covers the corners. Recorded as **speech pulls right** (unverified until the first talking-head take) |
| Voice name (§22U step 7) | `Thirty` (to be cloned by you in the ElevenLabs app at §22U step 6) |

**Unverified:** `VOICE-MAKER`'s clearance against the generator's default male-60s voice is argued (accent, texture, rhythm, habit), not measured.

---

## Flags (decisions for you; nothing below was changed silently)

| # | Where | Finding | Recommendation |
|---|---|---|---|
| **F1** | Format | The primary inspo is one unbroken selfie take with no B-roll; the file you named `inspo_body` is cut with B-roll | Hooks copy inspo 1; the body copies inspo 2's edit (TH + B-roll). Say "all talking head" to follow inspo 1 alone |
| F2 | P-011 | "Silicone" pad | Voiced verbatim (held V7.49.29); prompts say "the pad" (the word renders the soft glossy fake, Product Sheet ruling) |
| **F3** | P-006, P-007, P-014, P-015, P-018 | Not in the claim register: "none of them move the load off it"; "a hinged brace stops your knee going sideways"; copies are "thin elastic, foam pad, no tension… they stretch" (our band is elastic too); "Ten seconds on"; "you keep the straps"; "not a marketplace" | Voiced as written (§22U). Please confirm the advertiser holds them. The copies are shown as blank §10 near-copies, never a real brand |
| **F4** | HK1, HK2, P-005 | The speaker is a generated character presented as a real maker with a 30-year career who has "sold plenty" of braces, and the title card states it ("From a man who has made knee braces for 30 years") | This is a testimonial-type persona claim. It is fine only if a real maker or the brand stands behind it; otherwise it needs a dramatisation note in the edit (§43, like the CCTV rule). Your call |
| F5 | VN01 | The title card says "30 years" in numerals while the voice says "thirty" | Kept as written: on-screen text is the script's, verbatim |
| F6 | VN03 / VN02 | "a knee sleeve", "a hinged brace" | Unbranded generic supports, no wordmark or logo (§10) |
| F7 | P-015 | "orthopedic" is US spelling in a British script | Spoken the same. The captions will use the script's spelling unless you want "orthopaedic" |
| F8 | P-013 | "Thirty four percent" (no hyphen) | Voiced verbatim; no effect on the voice |
| F9 | P-018 | `package_closed.jpg` is still missing from the Drive folder | Offer beat uses two straps in hand or the open box only |
| F10 | Product Sheet | Drive has V7.49.29; the repo has V7.49.31 (adds the anatomy looks you chose) | Using V7.49.31 |

## Next: on your go (§18B step 5)

Confirm or Fix the two sheets on the board, and answer F1, F3 and F4 → steps 4–5 as one delivery: the workshop and home location plates (generated through the connectors, on the board), the act map + wardrobe map with every VN row assigned and every B-roll row given its layout, then the §22U voice route for the maker (two Kling voice-source takes, then the clone, which you do in the ElevenLabs app).
