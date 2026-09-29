# stryde-what-changed — Steps 4–5 (Manual)

Built against the **confirmed avatars** (user, 2026-09-29, "I'VE CONFIRM PROCEED"): H-HOST v3 · R1 Maureen v1 · R2 Desmond v1. The claim flags (F2, F3, F5, F6, F8, F9, F11) weren't answered, so the lines are **voiced as written** (§22U) and the flags stay open. **Side: right knee** on every worn beat (`SIDE_RULE`); B19a shows the script's own test, one strapped knee and one bare.

**On the board as To check:** 6 location plates (16:9), the one-off surgeon sheet (S1) and the host's talking-head frame (H-VOICE-IMG, §22U step 1). The act map below is **planned**: no beat image is generated until you confirm the plates. Every B-roll `duration` stays `pending-master` until the VO take exists (E6).

---

## Step 4 — Property, locations and light (§30C, §30G, §30K)

### Location Derivation Pass

| ID | Location | Owner | Beats | Tier | Plate |
|---|---|---|---|---|---|
| **L-STUDIO** | the podcast set: brick warehouse flat, chesterfield, mic on a boom arm, tripod lamp | H | every talking head, H-VOICE-IMG | **PLATED** | P0-STUDIO |
| **L-M-STAIRS** | Maureen's hall and stairs, 1930s semi, Kent (PROP-M) | R1 | HK1-a, B02, B07, B08a, B14a, B15, B17b, B18b, B19a, B19b, B23a, B23b | **PLATED** + property plate · landmark: the oak handrail and square newel | P1-PROP-M |
| **L-D-STAIRS** | Desmond's hall and stairs, late-Edwardian terrace, Croydon (PROP-D) | R2 | HK2-b, B01b, B04a, B04b, B08b, B08c, B16a, B17a, B17c, B18a, B21 | **PLATED** + property plate · landmark: the team photos up the stair wall | P2-PROP-D |
| L-STREET | residential pavement, 1930s semis | R1 / R2 | HK3-a, B16c | **PLATED** | P3-STREET |
| L-KITCHEN | kitchen, pale-oak table (the objects, the product, the offer) | hands | B10a–d, B13, B14b, B22a, B22c | **PLATED** | P4-KITCHEN |
| L-CONSULT | orthopaedic consulting room | S1 | B16b | **PLATED** | P5-CONSULT |
| ANAT | anatomical register (§12A, `ANATOMY_LOOK`) | — | HK1-b, HK2-a, HK3-b, B01a, B04c, B05, B06, B12, B14c, B20 | no plate | — |

**Set checks:** S1 tiers by beat count ✓ · S2 daylight only ✓ · S3 no two houses share finishes (duck-egg + oatmeal carpet + oak rail / warm grey + oak laminate + charcoal stair carpet) ✓ · S4 every variant moves through ≥ 3 locations ✓. **The location set closes here.**

### Property Sheets (§30G, fields 1–4)

| Field | PROP-M — Maureen | PROP-D — Desmond |
|---|---|---|
| 1 Type and era | 1930s pebble-dashed semi, Kent | late-Edwardian red-brick terrace, Croydon |
| 2 Shell | pale duck-egg blue walls, white ogee skirting, glazed oak doors with brass levers, oatmeal wool carpet → chequerboard vinyl at the kitchen | warm mid-grey walls, deep white gloss skirting, white four-panel doors with chrome knobs, oak laminate → charcoal stair carpet with white nosing stripes |
| 3 Floor map | front door → hall; stairs rise up the **right-hand wall**, open on the left with white spindles and an oak rail; kitchen doorway at the far end, left | front door → hall; stairs rise up the **left-hand wall**, open on the right with square white spindles; team photos up the stair wall; front room far end, right |
| 4 Orientation | front (door glass) faces **east**, half-landing window at the top of the flight | front faces **south-west**, small window at the top of the stairs |

### Light plans (§30K) — in room terms

| Location | Sources | Key by time (this build) | White balance |
|---|---|---|---|
| L-STUDIO | tall steel window, camera-left | overcast late morning, key from the left, one light state for every talking head | 6500K |
| L-M-STAIRS | leaded front-door glass (east), half-landing window | **morning (problem, M-D1): the landing window from above, grey** · **afternoon (after, M-D2): sun through the door glass down the hall** | 6500K → 5600K |
| L-D-STAIRS | frosted front-door glass (south-west), stair window | **morning (problem, D-D1): grey** · **afternoon (after, D-D2/D-D3): warm sun through the door glass** | 6500K → 5600K |
| L-STREET | open sky | morning overcast (HK3-a) · afternoon sun (B16c) | 6500K / 5600K |
| L-KITCHEN | window over the sink (camera-right in the plate) | cool overcast daylight (`LOC-KITCHEN-DAY`) | 6500K |
| L-CONSULT | half-lowered blind, left wall | afternoon, even | 5600K |

**Light arc by act (Mode 1, daylight, never moody):** the problem beats sit in grey morning light; from the product on (Act 3) the after-state beats move to afternoon sun. `angles.py` passes the LIGHT check for all three cut orders.

### Plates and sheets — generated through the connector (on the board, To check)

Higgsfield `gpt_image_2_5` · `variant: sunburst` · `quality: high` · `resolution: 2k` · **16:9** (V7.68.1) · empty, no people, no product, one render each. Prompts in `plates/<ID>.prompt.txt`, assembled by `plates/build_plates.py` from Appendix A by ID.

| ID | What | Job | Chars |
|---|---|---|---|
| P0-STUDIO | podcast set | `6dad3b2e-c422-4fa4-bb86-278fb522d79a` | 5,005 |
| P1-PROP-M | Maureen's hall and stairs (property plate) | `520de2e7-e577-4afe-b18c-b79dbed0acf0` | 5,431 |
| P2-PROP-D | Desmond's hall and stairs (property plate) | `68ddef76-e5b0-4947-966f-cda7e00335c2` | 5,208 |
| P3-STREET | pavement | `c19e14a9-5146-4444-8b83-e765dfdc3f8f` | 4,183 |
| P4-KITCHEN | kitchen table | `0bedfad5-bf20-4ebd-a862-fed90b55601a` | 4,503 |
| P5-CONSULT | consulting room | `833bfccb-a188-46d7-873a-ddc728f658fc` | 4,269 |
| S1-SURGEON | one-off surgeon, §19B sheet (`APPROACH-PRO`), British Pakistani man, 58, navy scrubs + grey gilet, scar through the right eyebrow | `7569a690-7398-49cb-ba09-4da6e7efd4ad` | 9,440 |
| **H-VOICE-IMG** | §22U step 1: the host on the chesterfield, thighs up, mic beside her chin, eyes on the lens — the Kling voice start image and the HeyGen avatar | `41e24534-5ee4-4e05-8a89-4b666259da10` (`nano_banana_pro` requested; Higgsfield logged `nano_banana_2`, the known §5 routing label) | 9,517 |

---

## Step 5 — Act map (E4) and wardrobe map (§21)

**One body, three hooks → three finished videos (§30H):** HK1 + BODY, HK2 + BODY, HK3 + BODY; the body's cuts are identical in each. **61 rows: 44 B-roll, 17 talking-head lines** (the host is on camera for ~45% of the running time; the reference's ~55%, less because our B-roll holds ~3s). Every hook opens with its first sentence as voice-over over full-screen B-roll and brings the host on camera for its last line (**VN01 → verified at step 5, carried by HK1–HK3**).

- **Layout (`EDIT-STRYDE-WC`, house rule V7.65.0):** B-roll full screen; `pip` (the host's cut-out bottom-left, EG02) on **3 of 44** (B06, B12, B20), never two in a row. Talking heads cut between the wide and a 1.25× punch-in (EG01). Captions EG04, red box on the numbers and turn words.
- **Motion (§27G):** one action per clip at a named pace, camera locked off on every B-roll (the subject moves, never both), stairs from the side waist-down or from behind with the hand on the rail, sit/stand beats start mid-movement and end on contact (3s max).
- **Angles, focus, light:** `angles.py` **PASS** on HK1, HK2 and HK3 cut orders (`work/angles_HK<n>.json`).
- Numbers are post overlays (17×, 70,000,000, 34%, 200,000+, 60 days, BUY 1 GET 1 FREE), never generated (§17).

| Beat | Act | Line | Subject · location · day | Framing / action | Angle · focus · light | Layout · EG | Product · model | Ledger |
|---|---|---|---|---|---|---|---|---|
| HK1-a | Hook 1 | Your knees have been taking seventeen times your bodyweight on every step | R1 · L-M-STAIRS · M-D1 | ECU her feet and bare right knee from the side, coming down one stair — one step down onto the next stair, weight onto the right leg (one step, about a second and a half) | ground profile CU through · foreground/medium · Maureen's landing window, grey morning L 6500K | full · EG03 full screen · EG04 caption red box 'seventeen times' | — · NB2 | VN01 |
| HK1-b | Hook 1 | for forty years, and you never felt a thing. | ANAT · — · — | ANAT-A: the knee in profile, a soft pulse of load arriving at the spot just below the kneecap with each step — one pulse per step (one pulse a second) | eye profile CU · deep/deep · anatomical register (§12A) L 5600K | full · EG05 anatomy | — · NB2 | VN01 |
| HK1-TH | Hook 1 | Here is what changed. | H · L-STUDIO · H-D1 | talking head (wide) | — | full · EG01 | — · HeyGen Avatar V | |
| HK2-a | Hook 2 | There is a band under your kneecap about as wide as your thumb, | ANAT · — · — | ANAT-A: the knee from the front, the patellar tendon under the kneecap lit, the rest of the joint quiet — the tendon's light swells once (one swell, about two seconds) | low front CU · deep/deep · anatomical register (§12A) R 5600K | full · EG03 · EG05 | — · NB2 | VN01 · F2 |
| HK2-b | Hook 2 | and for its size it is one of the strongest things in your body. | R2 · L-D-STAIRS · D-D1 | CU Desmond's bare right knee and shin as he plants his foot on the bottom stair and takes his weight — one step up onto the stair (one step, about a second) | low three-quarter CU · foreground/medium · Desmond's stair window, grey morning L 6500K | full | — · NB2 | VN01 · F2 |
| HK2-TH | Hook 2 | It is so good at its job that nobody ever thinks to check it. Not even the person who read your scan. | H · L-STUDIO · H-D1 | talking head (wide) | — | full · EG01 | — · HeyGen Avatar V | |
| HK3-a | Hook 3 | Five thousand steps a day. Forty years. | R1 · L-STREET · M-D1 | ground-level: Maureen's feet walking along the pavement towards the lens — three walking steps towards the lens (one step per second, normal walking speed) | ground front CU · deep/deep · open overcast sky, morning L 6500K | full · EG03 · captions '5,000 a day' '40 years' | — · NB2 | VN01 |
| HK3-b | Hook 3 | That is about seventy million times your full bodyweight has gone through one spot below your kneecap. | ANAT · — · — | ANAT-A: the knee from the side, the one spot below the kneecap glowing warmer as the pulses stack up — the spot warms with each pulse (one pulse a second) | high three-quarter CU · deep/deep · anatomical register (§12A) R 5600K | full · EG05 · '70,000,000' overlay (post) | — · NB2 | VN01 · F4 |
| HK3-TH | Hook 3 | Here is what happens when that spot stops being able to take it. | H · L-STUDIO · H-D1 | talking head (wide) | — | full · EG01 | — · HeyGen Avatar V | |
| B01a | Act 1 | That band is the patellar tendon. | ANAT · — · — | ANAT-A: the knee three-quarter front, the patellar tendon traced from the kneecap down to the shin — the tendon lights from top to bottom (one trace, about two seconds) | eye three-quarter CU · deep/deep · anatomical register (§12A) L 5600K | full · EG05 | — · NB2 |  |
| B01b | Act 1 | It sits two centimetres below your kneecap, on the front of the joint, and every step you take lands on it. | R2 · L-D-STAIRS · D-D1 | ECU from the side: Desmond's bare right knee bending as he steps down one stair — one step down (one step, about a second and a half) | eye profile ECU · foreground/medium · Desmond's stair window, grey morning L 6500K | full | — · NB2 |  |
| B01-TH | Act 1 | Put your finger there now and press. | H · L-STUDIO · H-D1 | talking head (1.25× punch-in) | — | full · EG01 | — · HeyGen Avatar V | |
| B02 | Act 1 | That is the one. | R1 · L-M-STAIRS · M-D1 | CU sitting on the bottom stair, her fingertip pressing just below her right kneecap — her fingertip presses in once and holds (one press, about a second) | high three-quarter CU · hands/shallow · Maureen's landing window, grey morning R 6500K | full | — · NB2 |  |
| B03-TH | Act 1 | It is not a big thing. It is about as wide as your thumb, and it has been quietly taking your whole bodyweight, multiplied, since you were a teenager. | H · L-STUDIO · H-D1 | talking head (wide) | — | full · EG01 | — · HeyGen Avatar V | |
| B04a | Act 1 | Going up the stairs, your muscles lift you. | R2 · L-D-STAIRS · D-D1 | from behind and below: Desmond climbs two stairs, thigh muscles working, hand on the rail — two steps up (one step a second) | low behind MEDIUM · deep/deep · Desmond's stair window, grey morning R 6500K | full | — · NB2 |  |
| B04b | Act 1 | Going down, nothing lifts you. You are catching yourself on every step, | R2 · L-D-STAIRS · D-D1 | from the side, waist-down: Desmond comes down one stair, the knee bending and taking the landing, hand on the rail — one step down, the knee absorbing it (one step, about a second and a half) | eye profile MEDIUM through · deep/deep · Desmond's stair window, grey morning L 6500K | full | — · NB2 |  |
| B04c | Act 1 | so coming down puts more through that band than going up does. | ANAT · — · — | ANAT-A: the knee on a down step, the tendon glowing stronger as the foot lands — one landing pulse, stronger than the last (one pulse, about a second) | high three-quarter CU · deep/deep · anatomical register (§12A) R 5600K | full · EG05 | — · NB2 | F5 |
| B05 | Act 1 | And inside the joint there is a layer of cartilage doing the absorbing. And over the years that layer thins. | ANAT · — · — | ANAT-A: the joint cut away, the pale cartilage layer between the bones slowly thinning — the cartilage thins by a fraction (one slow change over four seconds) | eye profile CU · deep/deep · anatomical register (§12A) L 5600K | full · EG05 | — · NB2 |  |
| B06-TH | Act 1 | That part is ordinary. It happens to everybody. But here is what nobody explains. The load does not thin with it. | H · L-STUDIO · H-D1 | talking head (wide) | — | full · EG01 | — · HeyGen Avatar V | |
| B06 | Act 1 | Seventeen times your bodyweight is still arriving, every step, in exactly the same place. | ANAT · — · — | ANAT-A: the thinner joint, the load pulses still arriving at the same spot below the kneecap — one pulse per second, unchanged (one pulse a second) | low three-quarter CU · deep/deep · anatomical register (§12A) L 5600K | pip · EG02 host cut-out bottom-left · EG04 red box 'Seventeen times' · 17× overlay | — · NB2 |  |
| B07-TH | Act 1 | The cushion gets thinner. The weight stays exactly the same. | H · L-STUDIO · H-D1 | talking head (1.25× punch-in) | — | full · EG01 | — · HeyGen Avatar V | |
| B07 | Act 1 | That is why it feels like it arrived overnight. | R1 · L-M-STAIRS · M-D1 | MCU at the top of her stairs, hand on the rail, she looks down the flight and stops — she draws one breath and doesn't step (one breath, about a second) | high three-quarter MCU · eyes/medium · Maureen's landing window, grey morning R 6500K | full | — · NB2 |  |
| B08-TH | Act 1 | Nothing about the way you walk changed, so you assume nothing changed. And here is the part that catches people out. You do not have to have done anything to your knees for this to happen. | H · L-STUDIO · H-D1 | talking head (wide) | — | full · EG01 | — · HeyGen Avatar V | |
| B08a | Act 1 | Some of the people it happens to have never run a mile in their life. | R1 · L-M-STAIRS · M-D1 | MEDIUM in her hall: Maureen picks her keys out of the bowl on the half-moon table — lifts the keys from the bowl (one lift, about a second) | eye three-quarter MEDIUM · eyes/medium · Maureen's landing window, grey morning L 6500K | full | — · NB2 |  |
| B08b | Act 1 | Others played sport for thirty years. | R2 · L-D-STAIRS · D-D1 | CU over Desmond's shoulder: his hand straightens one black-framed team photograph on the stair wall — his fingertips level the frame (one small nudge, about a second) | eye ots CU through · hands/shallow · Desmond's stair window, grey morning R 6500K | full | — · NB2 |  |
| B08-TH2 | Act 1 | It makes almost no difference, because the load is not coming from what you did. | H · L-STUDIO · H-D1 | talking head (1.25× punch-in) | — | full · EG01 | — · HeyGen Avatar V | |
| B08c | Act 1 | It is coming from standing up and walking. | R2 · L-D-STAIRS · D-D1 | MEDIUM: Desmond sitting on the bottom stair tying a trainer, already rising — ends standing — rises to standing (about a second and a half) | low three-quarter MEDIUM · eyes/deep · Desmond's stair window, grey morning L 6500K | full | — · NB2 |  |
| B09-TH | Act 2 | Which is why most of what gets sold for this cannot work. | H · L-STUDIO · H-D1 | talking head (1.25× punch-in) | — | full · EG01 | — · HeyGen Avatar V | |
| B10a | Act 2 | A sleeve squeezes the whole knee and leaves that band carrying everything. | hands · L-KITCHEN · K-D1 | overhead on the oak table: a plain grey knit knee sleeve; a hand slides it aside — one slide aside (one slide, about a second) | overhead front CU · hands/deep · kitchen window over the sink L 6500K | full | — · NB2 | F6 |
| B10b | Act 2 | A hinged brace stops the knee going sideways, and it was never going sideways. | hands · L-KITCHEN · K-D1 | CU a black hinged knee brace lying on the table; a hand flexes its hinge once sideways — one flex of the hinge (one flex, about a second) | high three-quarter CU · hands/medium · kitchen window over the sink L 6500K | full | — · NB2 | F6 |
| B10c | Act 2 | Gel sits on the skin. | hands · L-KITCHEN · K-D1 | CU a plain white tube; clear gel squeezed onto two fingertips — one squeeze (one squeeze, about a second) | eye profile CU · hands/shallow · kitchen window over the sink R 6500K | full | — · NB2 | F6 |
| B10d | Act 2 | A painkiller turns the alarm off and leaves the load exactly where it was. | hands · L-KITCHEN · K-D1 | CU a plain blister pack of white tablets beside a glass of water; a thumb pops one tablet out — one tablet popped (one press, about a second) | low three-quarter CU · hands/shallow · kitchen window over the sink L 6500K | full | — · NB2 | F6 |
| B11-TH | Act 2 | None of them are aimed at the spot. | H · L-STUDIO · H-D1 | talking head (1.25× punch-in) | — | full · EG01 | — · HeyGen Avatar V | |
| B12 | Act 2 | What that band actually needs is for less of your weight to land on it. | ANAT · — · — | ANAT-A: the knee in profile, the load pulse at the spot below the kneecap dimming to a soft glow — the pulse softens (one fade, about two seconds) | eye profile CU · deep/deep · anatomical register (§12A) L 5600K | pip · EG02 host cut-out bottom-left | — · NB2 |  |
| B13 | Act 3 | That is what this does. It is called Stryde. | hands · L-KITCHEN · K-D1 | CU two hands hold the strap up at chest height above the kitchen table, the front of the shell and the wordmark to the lens — the hands lift it a few centimetres into the light (one small lift, about a second) | eye front CU · product/medium · kitchen window over the sink R 6500K | full · EG04 red box 'Stryde' | VISIBLE · NBP |  |
| B14a | Act 3 | It sits two centimetres below the kneecap, on the tendon, and never crosses the joint. | R1 · L-M-STAIRS · M-D2 | CU sitting on the bottom stair, both hands slide the strap up her right shin and stop at contact under the kneecap — slides up the last few centimetres and stops at contact (one slide, about a second) | high three-quarter CU · product/medium · Maureen's front-door glass, afternoon sun R 5600K | full | VISIBLE · NBP |  |
| B14b | Act 3 | A silicone pad inside holds pressure on that one band instead of spreading it round the whole knee. | hands · L-KITCHEN · K-D1 | CU hands hold the strap and tip it so the inner pad faces the lens — one tilt of the strap toward the lens (one tilt, about a second) | eye three-quarter ECU · product/medium · kitchen window over the sink L 6500K | full | — · NBP |  |
| B14c | Act 3 | Your weight gets caught and moved off the worn part before it reaches the joint. | ANAT · — · — | ANAT-A: the strap seated below the kneecap, the pad pressing on the tendon, the glow at the worn spot calming — the red at the spot fades as the pad takes the load (one fade, about two seconds) | low three-quarter CU · deep/deep · anatomical register (§12A) R 5600K | full · EG05 | — · NB2 | F7 |
| B15-TH | Act 3 | The placement is the whole thing. | H · L-STUDIO · H-D1 | talking head (1.25× punch-in) | — | full · EG01 | — · HeyGen Avatar V | |
| B15 | Act 3 | A centimetre too high and it is a sleeve again. | R1 · L-M-STAIRS · M-D2 | ECU from the side: the strap seated on her right knee, the kneecap's lower edge sitting in the notch — her knee flexes a little and straightens (one flex, about a second) | eye profile ECU · product/medium · Maureen's front-door glass, afternoon sun L 5600K | full | VISIBLE · NBP |  |
| B16a | Act 3 | Thirty four percent less strain. Measured. | R2 · L-D-STAIRS · D-D2 | from the side, waist-down: Desmond comes down one stair easily, the strap on his right knee — one easy step down (one step, about a second) | eye profile MEDIUM · product/medium · Desmond's front-door glass, afternoon sun L 5600K | full · 34% overlay (post) | VISIBLE · NBP |  |
| B16b | Act 3 | Three years with orthopedic surgeons. | S1 · L-CONSULT · S1-D1 | MCU at his desk, the knee model beside him, he holds the strap still at chest height and looks up from it — lifts his eyes from the strap to the patient (one look up, about a second) | eye three-quarter MCU · eyes/medium · consulting-room blind window L 5600K | full | — · NBP |  |
| B16c | Act 3 | Two hundred thousand people wearing one. | R2 · L-STREET · D-D2 | knee-and-shin only, walking toward the lens on the pavement, the strap staying put — three walking steps toward the lens (one step per second, normal walking speed) | ground front CU · product/deep · open sky, afternoon sun L 5600K | full · 200,000+ overlay (post) | VISIBLE · NBP |  |
| B17a | Act 3 | Ten seconds to put on. | R2 · L-D-STAIRS · D-D3 | CU sitting on the bottom stair, his tracksuit leg rolled up, both hands slide the strap up to contact under the kneecap — slides up and stops at contact (one slide, about a second) | high three-quarter CU · product/medium · Desmond's front-door glass, afternoon sun R 5600K | full | VISIBLE · NBP | F8 |
| B17b | Act 3 | No sores, no rolling down, | R1 · L-M-STAIRS · M-D2 | CU seated, her fingertips run along the skin at the strap's lower edge — the skin smooth and unmarked — fingertips slide once along the edge (one slide, about a second) | low profile CU · product/medium · Maureen's front-door glass, afternoon sun L 5600K | full | VISIBLE · NBP | F8 |
| B17c | Act 3 | and nobody can see it. | R2 · L-D-STAIRS · D-D3 | CU from the side: he lets his tracksuit leg drop over the strap; the fabric lies flat — the trouser leg falls and settles (one drop, about a second) | eye profile CU · product/medium · Desmond's front-door glass, afternoon sun L 5600K | full | REVEAL · NBP | F8 |
| B18-TH | Act 4 | The thing people write to us about most is not the pain. | H · L-STUDIO · H-D1 | talking head (wide) | — | full · EG01 | — · HeyGen Avatar V | |
| B18a | Act 4 | It is that the knee stops feeling like a rusty hinge. | R2 · L-D-STAIRS · D-D2 | CU Desmond's strapped right knee bending smoothly as he sits down onto the bottom stair — already lowering, ends seated — sits down, ends on contact (about a second and a half) | eye three-quarter CU · product/medium · Desmond's front-door glass, afternoon sun R 5600K | full | VISIBLE · NBP | F9 |
| B18b | Act 4 | They stop planning the stairs before they get to them. | R1 · L-M-STAIRS · M-D2 | WIDE from the foot of the stairs: Maureen at the top starts straight down, facing forwards, hand light on the rail — one step down, facing forwards (one step, about a second and a half) | low front WIDE · deep/deep · Maureen's front-door glass, afternoon sun L 5600K | full | VISIBLE · NBP | F9 |
| B19-TH | Act 4 | And you do not have to take my word for any of it. | H · L-STUDIO · H-D1 | talking head (wide) | — | full · EG01 | — · HeyGen Avatar V | |
| B19a | Act 4 | Put one on one knee only. Leave the other bare. | R1 · L-M-STAIRS · M-D2 | CU seated on the bottom stair: both knees side by side, the strap on the right, the left bare — her hands rest on her thighs; she breathes out (one breath, about a second) | high front CU · product/medium · Maureen's front-door glass, afternoon sun R 5600K | full | VISIBLE · NBP |  |
| B19b | Act 4 | Go to your own stairs and come down forwards. | R1 · L-M-STAIRS · M-D2 | from the side, waist-down: Maureen comes down one stair facing forwards, hand light on the rail — one step down, facing forwards (one step, about a second and a half) | eye profile MEDIUM through · product/medium · Maureen's front-door glass, afternoon sun L 5600K | full | VISIBLE · NBP |  |
| B19-TH2 | Act 4 | You will know in a minute. Not because the arthritis has gone. It is still there, and nothing here changes that. | H · L-STUDIO · H-D1 | talking head (1.25× punch-in) | — | full · EG01 | — · HeyGen Avatar V | |
| B20 | Act 4 | Because the weight is not landing on that band any more. | ANAT · — · — | ANAT-A: the strap seated, the step pulse arriving and spreading off the tendon, the spot staying calm — one step pulse, the spot stays cool (one pulse, about a second) | high front CU · deep/deep · anatomical register (§12A) L 5600K | pip · EG02 host cut-out bottom-left | — · NB2 |  |
| B21-TH | Act 4 | So here is the choice. Keep aiming at the joint, which is where it hurts but not where the load is. | H · L-STUDIO · H-D1 | talking head (wide) | — | full · EG01 | — · HeyGen Avatar V | |
| B21 | Act 4 | Or move the load off the one spot that has been taking it since you were a teenager. | R2 · L-D-STAIRS · D-D2 | CU Desmond's strapped right knee as he steps down one stair, one of the old team photos on the wall behind — one step down (one step, about a second and a half) | low three-quarter CU · product/medium · Desmond's front-door glass, afternoon sun R 5600K | full | VISIBLE · NBP |  |
| B22a | Act 4 | Two for one, so you can do both knees. | hands · L-KITCHEN · K-D1 | overhead on the oak table: hands lift the lid off the box; two straps lie inside side by side — lifts the lid clear and out of frame (one lift, about a second) | overhead front CU · product/deep · kitchen window over the sink L 6500K | full · EG04 · 'BUY 1 GET 1 FREE' in the edit | — · NBP |  |
| B22-TH | Act 4 | Sixty days, and you keep the straps. From the Stryde site. | H · L-STUDIO · H-D1 | talking head (wide) | — | full · EG01 · '60 days' in the edit (F10) | — · HeyGen Avatar V | |
| B22c | Act 4 | The copies stretch, and a stretched strap stops holding the spot. | hands · L-KITCHEN · K-D1 | CU on the table: two hands pull a cheap copy's thin frayed band and it stretches slack — one pull, the band goes slack (one pull, about a second) | high profile CU · hands/medium · kitchen window over the sink R 6500K | full | — · NB2 | F11 |
| B23a | Act 4 | The next step is going to land in the same place either way. | R1 · L-M-STAIRS · M-D2 | ECU her foot, the strap just in frame above it, on the edge of the top stair — her foot settles on the edge (one small settle, about a second) | ground three-quarter ECU · foreground/medium · Maureen's front-door glass, afternoon sun R 5600K | full | VISIBLE · NBP |  |
| B23b | Act 4 | Go and do it forwards. | R1 · L-M-STAIRS · M-D2 | MEDIUM from below: Maureen comes down towards us facing forwards, a small smile — one step down, facing forwards (one step, about a second and a half) | low front MEDIUM · eyes/medium · Maureen's front-door glass, afternoon sun L 5600K | full | — · NB2 |  |


### Wardrobe map (§14, §21) — keyed to the story day

| Character | Story day | Outfit | Beats |
|---|---|---|---|
| H (host) | H-D1 | the sheet: oatmeal-cream chunky cable-knit, mid-blue jeans, dark brown Chelsea boots | every talking head |
| R1 Maureen | M-D1 (problem, grey morning) | the sheet: dusty-pink cardigan over the navy-and-white Breton top, navy A-line skirt above the knee, white plimsolls; knees bare | HK1-a, HK3-a, B02, B07, B08a |
| R1 Maureen | M-D2 (after, afternoon sun) | sage-green cardigan over a white T-shirt, mid-blue denim skirt just above the knee, the same white plimsolls; the strap on her right knee | B14a, B15, B17b, B18b, B19a, B19b, B23a, B23b |
| R2 Desmond | D-D1 (problem, grey morning) | the sheet: navy zip-neck over a white T-shirt, dark grey jogging shorts above the knee, white trainers with navy trim; knees bare | HK2-b, B01b, B04a, B04b, B08b, B08c |
| R2 Desmond | D-D2 (after, afternoon sun) | burgundy polo shirt, khaki cotton shorts above the knee, the same trainers; the strap on his right knee | B16a, B16c, B18a, B21 |
| R2 Desmond | D-D3 (after, the trouser day — §9D) | grey marl sweatshirt, navy tracksuit bottoms (rolled above the knee for B17a, dropped over the strap in B17c), the same trainers | B17a, B17c |
| S1 Surgeon | S1-D1 | the sheet: navy scrubs, grey fleece gilet, black clinic trainers | B16b |

Plain trainers on every beat (no visible logo) — the B-roll prompts ask for it.

---

## Next

Confirm or Fix the plates, the surgeon sheet and the host's talking-head frame. **The voice starts the moment H-VOICE-IMG is confirmed** (§22X: a Kling call needs its start frame approved): two Kling source takes (G1/G2, `VOICE-HOST`) → `voice_source.py` → ElevenLabs clone by API → Enhance → one Eleven v4 request (HK1 + HK2 + HK3 + BODY) → HeyGen Avatar V on the untrimmed take → cut per hook and trimmed at a natural pace (`trim.py`). Then Hook 1's images.
