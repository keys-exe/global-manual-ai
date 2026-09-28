# stryde-thirty-years — Steps 4–5 (Manual)

Built against the **confirmed avatars** (user, 2026-09-28): C1-MAKER `a866e6f7…` · S1-WEARER `7cc9a07d…`. Side: **right knee** on every worn beat.
Flags from steps 1–3 were not answered, so each runs on my recommendation until you say otherwise: **F1** hooks from inspo 1, body edited like inspo 2 · **F3** voiced as written, near-copies blank · **F4** still open: decide before the edit (dramatisation note or not).

**Plates:** four generated through Higgsfield and on the board **To check**. P1 and P3 were built against P0 and P2 before you checked those, so a Fix on P0 or P2 regenerates its dependant too. **Next:** the maker's talking-head image (§22U step 1), then two Kling voice-source takes. B-roll `duration` stays `pending-master` until his voice master exists (E6).

---

## Step 4 — Property and locations (§30C, §30G, §30K)

### Location Derivation Pass (C0 first)

| ID | Location | Channel | Owner | Beats | Tier | Plate |
|---|---|---|---|---|---|---|
| **L-WORKSHOP** | the maker's brace workshop, a Victorian brick unit in Walsall | C1 (VN01 workshop + rail, VN02 bench + vice, VN03 bench), C5 (his credential lives in the room) | C1 | HK1–HK3, every TH, BR-02, BR-05a/b, BR-07b, BR-10, BR-11, BR-14a/b, BR-15a/b, BR-18a/b | **PLATED**: two views of one room | **P2** bench (master) · **P3** rail aisle (P2 attached) |
| **PROP-S** | the wearer's 1970s semi-detached house | **C0**: hall/stairs + living room are rooms of one dwelling | S1 | — | **Property Sheet + plate P0** | P0 |
| L-S-STAIRS | her hall and stairs | C1 (script: "come down the stairs forwards", "go down your own stairs"), C6 (after-state) | S1 | BR-03a, BR-12, BR-13, BR-15c, BR-16 | **TRAVERSED** + property plate · landmark: the pine handrail and white spindles | P0 |
| L-S-LIVING | her living room | C1 ("out of a chair", "a drawer full of these") | S1 | BR-03b, BR-07a, BR-08 | **PLATED** | **P1** (P0 attached) |
| L-LANE | a village lane near her house | C1 ("the dog as far as you used to") | S1 | BR-03c | **TRAVERSED**: no plate · landmark: a five-bar gate and hedges | written with the beat at step 7 (`LOC-EXT-OVERCAST`) |

**Set checks:** **S1** tiers by beat count and movement ✓ · **S2** all daylight; the only change is the before-state afternoon (W-D0), flatter and cooler (§30K arc) ✓ · **S3** her hall (north, soft) and living room (south, sun) differ because they face opposite ways ✓ · **S4** acts open and close in different rooms: Act 1 opens mechanism, closes workshop TH · Act 2 opens workshop TH, closes workshop TH · Act 3 opens workshop TH, closes workshop bench · Act 4 opens workshop bench, closes workshop TH. **Talking-head builds return to one set by design** (inspo 2: the same stairs every time), so S4 is met by the B-roll between. **The location set closes here.**

### Property Sheet — PROP-S (the wearer's house)

| # | Field | Content |
|---|---|---|
| 1 | Type and era | 1970s brick semi-detached, decorated in the 1990s and kept since |
| 2 | Shell | warm cream plaster, scuffed along the stairs · plain square-edged pine skirting and architraves, varnished gone orange · flush pine-veneer doors, brushed-steel levers · flat white ceiling, round paper lampshades · pale fawn twist-pile carpet through hall, stairs and living room → beige vinyl at the kitchen · white double-panel radiators · white plastic switches |
| 3 | Floor map | front door → hall; straight flight of stairs rising on the **left**; living-room doorway halfway down on the **right**; closed door under the stairs at the end |
| 4 | Orientation | front (hall, door glass, landing window) faces **north**: no direct sun · living room at the back faces **south**: morning sun through the patio doors |
| 5 | Carried elements | the pine handrail and white spindles · the brass barometer · the green waxed jacket and red dog lead on the hooks · the green wing armchair · the oak sideboard |
| 6 | Exterior | back: small lawn, patio with bird table, larch-lap fence, neighbour's apple tree |
| 7 | Standing negatives | none yet |

### Light plans (§30K), in room terms

| Location | Sources | Sun path | Key by time (this build) | Fill |
|---|---|---|---|---|
| L-WORKSHOP | three tall east factory windows along the bench wall; green double doors at the far (south) end; fluorescent tubes **off** | low morning sun through the east windows across the bench | **morning** (every workshop beat, story day M-D1/W-D1): bench view → key screen-**left**; rail view (P3) → key screen-**right**; the maker's TH at the vice end → window beside the camera, key screen-**left**, 30–60° | pale whitewashed brick, concrete floor |
| L-S-STAIRS | frosted front-door panel (north); landing window at the top of the flight | none direct | **morning** (W-D2): soft cool-neutral; from the foot → key from the landing window, screen-**left** · from the landing/behind → key screen-**right** | cream walls |
| L-S-LIVING | south patio doors, far wall | mid-morning sun low through the patio doors | **morning** (W-D2, after): sun patch on the carpet, key from the patio doors · **afternoon** (W-D0, before): the sun gone round, flat grey sky, curtains half drawn, cooler | cream walls, fawn carpet |
| L-LANE | open sky | overcast | **morning** (W-D3): bright overcast | — |

### Plates — generated through the connector (Manual: on the board for your check)

Higgsfield `gpt_image_2_5` · `variant: sunburst` · `quality: high` · `resolution: 2k` · 9:16 · empty, no people, no product. Prompts in `plates/<ID>.prompt.txt` (assembled from Appendix A by ID in `plates/build_plates.py`, `NEG-LIGHT` added per §30K).

| ID | Location | Job | Attach | Chars | Board |
|---|---|---|---|---|---|
| **P0-PROP-S** | her hall and stairs (property plate) | `ed1a1f63-ad29-4ca4-8d10-87cccbbfb23a` | nothing | 6,026 | To check |
| P1-S-LIVING | her living room | `008afc51-e34e-4c1b-8018-e8b73d688a76` | P0 | 6,892 | To check |
| **P2-WORKSHOP-BENCH** | workshop, the bench (master) | `8e9aa897-2d5f-4b70-8a1b-221c82a956c4` | nothing | 5,372 | To check |
| P3-WORKSHOP-RAIL | workshop, the rail aisle | `efbbc61f-fd32-4de2-ae51-59f4e8081d5e` | P2 | 5,140 | To check |

Spend: 4 Sunburst jobs, 110.25 Higgsfield credits (19,908.25 → 19,798; about 27.6 each at 2k high — four times a cast sheet). **Scene Registry (§30C 7a):** these four job IDs are what every beat in their location attaches.

### COLOUR-KEY per capture event (§30L), from the plates and the outfit rows

| Event | COLOUR-KEY |
|---|---|
| Workshop (M-D1, W-D1) | pale east morning daylight, clean and slightly cool · whitewashed grey-white brick, grey concrete, dark oiled beech bench, a blue cast-iron vice, black neoprene · him: green-and-brown check, faded navy apron, grey trousers · her (W-D1): white, cornflower blue, bottle green · accent: the blue vice, the black strap · natural, slightly muted |
| Stairs (W-D2) | soft cool-neutral north light · cream walls, pale fawn carpet, orange pine handrail, white spindles · her: mustard yellow, navy cord, tan boots · accent: the mustard jumper, the black strap · natural |
| Living, after (W-D2) | warm mid-morning sun from the south · cream walls, fawn carpet, bottle-green velour armchair, dark oak · her: mustard, navy, tan · accent: the green armchair · natural, a touch warm |
| Living, before (W-D0) | flat grey afternoon, cooler, curtains half drawn · same room · her: dusty pink, heather grey, sheepskin · accent: the beige sleeve · muted |
| Lane (W-D3) | bright overcast morning · grey tarmac, green hedges, a grey five-bar gate · her: chambray blue, green waxed jacket, stone shorts, tan boots; a wheaten border terrier · natural |

---

## Step 5 — Act map (E4) and wardrobe map (§21, §14A)

### Structure

Hooks HK1–HK3 are the script's three openings, each butted onto the same body (§30H). The body is four acts, copying inspo 2's edit: the maker's talking head returns between B-roll runs.

| Act | Lines | Job | Opens · closes |
|---|---|---|---|
| Act 1: The spot | P-001–P-004 | mechanism + what it gives you | MECH · TH |
| Act 2: What fails | P-005–P-008 | the failed supports, the permission | TH · TH |
| Act 3: Three things | P-009–P-014 | placement, pad, band, 34%, copies | TH · BR |
| Act 4: The one I hand people | P-015–P-019 | product, test, honesty, offer, CTA | BR · TH |

### Act map

`dur` = `pending-master` on every B-roll row (E6); TH rows take E6 words→duration once the master exists. **Model** follows the Mode & Model Lock. Every B-roll row carries its `angle`, `why`, `focus`, `light` and the §27G motion fields. **`angles.py` PASS** (38 rows: 23 BR · 5 MECH · 10 TH; 14 distinct setups; eye-level frontal 5/28). Source: `work/actmap.json`.

| Beat | Act | Phrase | Type | Subject | Location | Day · event | Angle (height · side · scale · fg) · why | Focus | Light | Action · pace · camera · staging · pin_end | Key | Product · visibility | Layout · EG | Model | Ledger |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **HK1** | Hook 1 | HK1 | TH | C1 | L-WORKSHOP (P3 rail aisle) | M-D1 · E-HK1 | WALK (§22F): arm's length, walking slowly down the rail aisle, the braces racking past behind his shoulder | — | east factory windows over the bench · key R · morning | walks slowly towards the doors, talking · one slow step a second · travels with him (he walks, the phone is held by him: FRAME-WALK) · walking at camera → FRAME-WALK · pin no | — | absent · — | full · EG01 title cards (6s) · EG02 captions | HeyGen Avatar V (seed nano_banana_pro) · or Kling omni lip-sync if HeyGen can't walk (step 6) | VN01 |
| **HK2** | Hook 2 | HK2 | TH | C1 | L-WORKSHOP (P2 bench) | M-D1 · E-HK2 | SELFIE static, seated on the stool at the vice; a half-finished hinged brace clamped in the vice beside his face; he never touches it | — | east factory windows over the bench · key L · morning | — | — | absent (a generic unbranded hinged brace, half built) · — | full · EG02 captions · no title cards | HeyGen Avatar V (seed nano_banana_pro) | VN02 |
| **HK3-BR** | Hook 3 | HK3 "This is a knee sleeve I cut in half this morning." | BR | C1 hand | L-WORKSHOP (P2 bench) | M-D1 · E-HK3 | overhead · front · CU · clean — overhead = the thing on the bench, the object of the sentence | foreground · medium | east factory windows over the bench · key L · morning | two halves of a cut beige sleeve lie curled on the beech; his hand enters and lifts one half up towards the lens · one lift in 2s · sway · hands: whole, in the light · pin no | — | absent (generic sleeve, unbranded) · — | full · EG02 | nano_banana_2 | VN03 (part 1) |
| **HK3-BR2** | Hook 3 | HK3 "…this morning." | BR | C1 | L-WORKSHOP (P2 bench) | M-D1 · E-HK3 | eye · three-quarter · MCU · clean — the pull-back: from the sleeve half in his hand to him, sat angled to the bench | eyes · deep · tap sleeve half→his eyes on "the pull-back settles" | east factory windows over the bench · key L · morning | the phone eases back from the sleeve half held up in his hand to reveal his face and the bench · one slow pull over 3s · travels back (he is still) · none · pin no | morning | absent · — | full · EG02 | nano_banana_pro (start) · Kling omni | VN03 (part 2) |
| **HK3-TH** | Hook 3 | HK3 "I want to show you why the one in your drawer never helped you." | TH | C1 | L-WORKSHOP (P2 bench) | M-D1 · E-HK3 | SELFIE static at the bench, the sleeve half in his hand low in frame | — | east factory windows over the bench · key L · morning | — | — | absent · — | full · EG02 | HeyGen Avatar V | VN03 (part 3) |
| **MECH-01** | Act 1 | P-001 | MECH | anatomy | — | — · — | eye · profile · MEDIUM · clean — profile shows the load arriving down the leg | deep · deep | anatomy register (§12A), single glow at [SITE] · key front · midday | each step pulses a glow down into one spot below the kneecap · one pulse a second (walking cadence) · still · none · pin no | Seventeen | absent · — | full · EG06 · 17× overlay (CapCut) | nano_banana_2 (ANAT-A) | — |
| **BR-02** | Act 1 | P-002 "Two centimetres down, on the tendon." | BR | C1 finger + S1 knee | L-WORKSHOP (P2 bench) | W-D1 · E-FIT | high · three-quarter · CU · clean — high = looking down at the knee as he does at a fitting | hands · deep | east factory windows over the bench · key L · morning | his fingertip presses once into the tendon two centimetres below her right kneecap · one press, held 1s · sway · hands: fingertip whole, on the skin · pin no | centimetres | absent · bare knee | full · EG04 | nano_banana_2 | — |
| **MECH-02** | Act 1 | P-002 "Not the cartilage. Not the joint. That spot." | MECH | anatomy | — | — · — | eye · front · CU · clean — front shows the tendon as one bright point | deep · deep | anatomy register (§12A), single glow at [SITE] · key front · midday | the joint dims, the tendon spot stays lit · one change in 2s · still · none · pin no | cartilage | absent · — | full · EG06 | nano_banana_2 (ANAT-B) | — |
| **BR-03a** | Act 1 | P-003 "Take the load off it and you come down the stairs forwards." | BR | S1 | L-S-STAIRS | W-D2 · E-STAIRS | low · front · FULL · clean — low = the steps and her feet carry it; resolve | deep · deep | landing window + front-door glass (north) · key L · morning | she comes down three stairs forwards, hand only resting on the rail · one step a second · sway · stairs: descending, framed WIDE from the foot, low · pin no | stairs | worn · VISIBLE | full · EG04 | nano_banana_pro | — |
| **BR-03b** | Act 1 | P-003 "Out of a chair first try." | BR | S1 | L-S-LIVING | W-D2 · E-LIVING | eye · three-quarter · MEDIUM · clean | deep · deep | south patio doors · key R · morning | she stands up from the green wing armchair in one go, no hands on the arms · one rise in 2s · sway · sitting→standing: start mid-rise · pin no | chair | worn · VISIBLE | full · EG04 | nano_banana_pro | — |
| **BR-03c** | Act 1 | P-003 "The dog as far as you used to." | BR | S1 + her border terrier | L-LANE | W-D3 · E-DOG | eye · three-quarter-back · WIDE · clean — three-quarter-back = walking away down a long lane: distance, freedom | deep · deep | open overcast sky · key front · morning | she walks away down the lane with the dog on a lead · one step a second · sway · walking away from camera (safe) · pin no | dog | worn · VISIBLE | full · EG04 | nano_banana_pro | — |
| **TH-01** | Act 1 | P-004 | TH | C1 | L-WORKSHOP | M-D1 · E-TH | SELFIE, seated at the vice end of the bench (R2 static) | — | east factory windows over the bench · key L · morning | — | — | absent · — | full · EG03 · EG05 | HeyGen Avatar V (seed nano_banana_pro) | — |
| **TH-02** | Act 2 | P-005 "Here is what I have watched fail for thirty years." | TH | C1 | L-WORKSHOP | M-D1 · E-TH | SELFIE, seated at the vice end of the bench (R2 static) | — | east factory windows over the bench · key L · morning | — | — | absent · — | full · EG03 · EG05 | HeyGen Avatar V (seed nano_banana_pro) | — |
| **BR-05a** | Act 2 | P-005 "Sleeves. Hinged braces. Gels. Wraps." | BR | C1 hands | L-WORKSHOP (P2 bench) | M-D1 · E-BENCH | overhead · front · CU · clean — overhead = laying things out, routine, a list | hands · deep | east factory windows over the bench · key L · morning | his hands lay four supports in a row on the bench: a sleeve, a hinged brace, a gel-pad support, a wrap · one every second · still · hands: whole, in the light · pin no | Sleeves | absent (generic, unbranded) · — | full · EG04 | nano_banana_2 | — |
| **BR-05b** | Act 2 | P-005 "I have sold plenty of them, and they are better than nothing." | BR | C1 hand | L-WORKSHOP (P3 rail) | M-D1 · E-RAIL | eye · three-quarter · MEDIUM · through — through the hanging braces = a lifetime of stock | foreground · medium | east factory windows over the bench · key R · morning | his hand runs along the hangers on the rail, the braces swinging · one pass in 3s · sway · none · pin no | sold | absent (generic, unbranded) · — | full · EG04 | nano_banana_2 | — |
| **MECH-06** | Act 2 | P-006 | MECH | anatomy | — | — · — | eye · three-quarter · CU · clean | deep · deep | anatomy register (§12A), single glow at [SITE] · key front · midday | a sleeve outline squeezes the whole knee; the glow at the tendon spot stays · one squeeze in 2s · still · none · pin no | same spot | absent · — | full · EG06 | nano_banana_2 (ANAT-A) | — |
| **BR-07a** | Act 2 | P-007 "A sleeve squeezes the whole knee." | BR | S1 | L-S-LIVING | W-D0 · E-BEFORE | high · three-quarter · CU · clean — high = small, worn down: the before | hands · deep | south patio doors · key R · afternoon | sitting in the armchair, she tugs a beige sleeve up over her right knee · one tug in 2s · sway · hands: whole · pin no | sleeve | absent (generic sleeve) · bare knee under the sleeve | full · EG04 | nano_banana_2 | — |
| **BR-07b** | Act 2 | P-007 "A hinged brace stops your knee going sideways…" | BR | C1 hands | L-WORKSHOP (P2 bench) | M-D1 · E-BENCH | eye · front · CU · clean | hands · deep | east factory windows over the bench · key L · morning | his hands try to bend a hinged brace sideways; the steel side bars don't give · one push in 2s · still · hands: whole · pin no | sideways | absent (generic hinged brace) · — | full · EG04 | nano_banana_2 | — |
| **BR-08** | Act 2 | P-008 "So if you have a drawer full of these…" | BR | S1 | L-S-LIVING | W-D0 · E-BEFORE | high · ots · MEDIUM · clean — OTS = we look into her drawer with her | foreground · medium | south patio doors · key L · afternoon | she pulls the sideboard drawer open on a tangle of sleeves, braces and wraps · one pull in 2s · still · none · pin no | drawer | absent · — | full · EG04 | nano_banana_2 | — |
| **TH-03** | Act 2 | P-008 "…that was not you failing. You were wrapping the wrong part of your leg." | TH | C1 | L-WORKSHOP | M-D1 · E-TH | SELFIE, seated at the vice end of the bench (R2 static) | — | east factory windows over the bench · key L · morning | — | — | absent · — | full · EG03 · EG05 | HeyGen Avatar V (seed nano_banana_pro) | — |
| **TH-04** | Act 3 | P-009 | TH | C1 | L-WORKSHOP | M-D1 · E-TH | SELFIE, seated at the vice end of the bench (R2 static) | — | east factory windows over the bench · key L · morning | — | — | absent · — | full · EG03 · EG05 | HeyGen Avatar V (seed nano_banana_pro) | — |
| **BR-10** | Act 3 | P-010 | BR | C1 finger + S1 knee | L-WORKSHOP (P2 bench) | W-D1 · E-FIT | high · front · CU · clean — high = his view fitting it | product · deep | east factory windows over the bench · key L · morning | the strap is seated on her right knee; his fingertip traces the gap between kneecap and notch · one trace in 2s · still · hands: fingertip whole · pin no | placement | worn (PLACEMENT_REFERENCES) · VISIBLE | full · EG04 | nano_banana_pro | — |
| **BR-11** | Act 3 | P-011 "Two, the pad." | BR | C1 hands | L-WORKSHOP (P2 bench) | M-D1 · E-BENCH | eye · three-quarter · CU · clean | product · deep | east factory windows over the bench · key L · morning | his hands turn the strap over to show the pad side to the lens · one turn in 3s · still · held product: HELD_GRIPS · pin yes | pad | held (PAD_BACK_SHOT at the end) · — | full · EG04 · EG07 | nano_banana_pro | — |
| **MECH-11** | Act 3 | P-011 "…holding pressure on that one spot…" | MECH | anatomy | — | — · — | eye · front · CU · clean | deep · deep | anatomy register (§12A), single glow at [SITE] · key front · midday | pressure lands on one point on the tendon and the glow there eases · one ease in 2s · still · none · pin no | one spot | absent · — | full · EG06 | nano_banana_2 (ANAT-A) | — |
| **BR-12** | Act 3 | P-012 "Three, the band." | BR | S1 | L-S-STAIRS | W-D2 · E-STAIRS | ground · behind · CU · clean — ground, behind = the back of the knee where the band runs | product · deep | landing window + front-door glass (north) · key R · morning | she stands on the bottom stair, weight shifting onto her right leg; the band sits flat behind the knee · one shift in 2s · still · none · pin no | band | worn (worn_rear) · VISIBLE | full · EG04 | nano_banana_pro | — |
| **MECH-12** | Act 3 | P-012 "It catches your weight coming down…" | MECH | anatomy | — | — · — | eye · profile · MEDIUM · clean — profile shows weight coming down the leg | deep · deep | anatomy register (§12A), single glow at [SITE] · key front · midday | the load arrives, the pad catches it and the glow moves off the joint · one step in 2s · still · none · pin no | catches | absent · — | full · EG06 | nano_banana_2 (ANAT-A) | — |
| **BR-13** | Act 3 | P-013 | BR | S1 | L-S-STAIRS | W-D2 · E-STAIRS | eye · profile · MEDIUM · through — through the spindles, profile = the whole leg working on the step | deep · deep | landing window + front-door glass (north) · key L · morning | she steps down one stair forwards, the strapped right knee bending · one step in 2s · sway · stairs: descending, framed from the side through the spindles · pin no | Thirty | worn · VISIBLE | full · EG04 · 34% overlay (CapCut) | nano_banana_pro | — |
| **BR-14a** | Act 3 | P-014 "Most straps that look like this are copies." | BR | C1 hands | L-WORKSHOP (P2 bench) | M-D1 · E-BENCH | overhead · three-quarter · CU · clean — overhead = laid out for inspection | foreground · deep | east factory windows over the bench · key L · morning | his hand tips a paper bag and five blank near-copy straps slide out onto the bench · one tip in 2s · still · none · pin no | copies | absent (§10 near-copies, blank) · — | full · EG04 | nano_banana_2 | — |
| **BR-14b** | Act 3 | P-014 "Thin elastic, foam pad, no tension. They stretch…" | BR | C1 hands | L-WORKSHOP (P2 bench) | M-D1 · E-BENCH | eye · front · CU · clean | hands · deep | east factory windows over the bench · key L · morning | his hands pull a near-copy's thin band and it stretches long and stays slack · one pull in 2s · still · hands: whole · pin no | stretch | absent (§10 near-copy) · — | full · EG04 | nano_banana_2 | — |
| **BR-15a** | Act 4 | P-015 "The one I hand people is Stryde." | BR | C1 hand | L-WORKSHOP (P2 bench) | M-D1 · E-BENCH | eye · front · CU · clean | product · deep | east factory windows over the bench · key L · morning | he holds the strap up to the lens, wordmark to camera · one lift in 2s · sway · held product: HELD_GRIPS · pin yes | Stryde | held · — | full · EG07 | nano_banana_pro | — |
| **BR-15b** | Act 4 | P-015 "Three years with orthopedic surgeons. Two hundred thousand wearing one." | BR | C1 + S1 | L-WORKSHOP (P2 bench) | W-D1 · E-FIT | eye · ots · MEDIUM · clean — OTS from her side = being handed it | hands · medium | east factory windows over the bench · key L · morning | across the bench he hands her the strap and she takes it · one hand-over in 2s · sway · hand-over: both hands whole · pin no | hand | held · — | full · EG04 · 200,000 overlay (CapCut) | nano_banana_pro | — |
| **BR-15c** | Act 4 | P-015 "Ten seconds on, no sores, no rolling down." | BR | S1 | L-S-STAIRS | W-D2 · E-STAIRS | low · three-quarter · CU · clean — low = at her knee, seated on the step | product · deep | landing window + front-door glass (north) · key L · morning | sitting on the bottom stair she slides the closed strap up her shin and it seats below the kneecap · one slide in 3s · still · SEAT_LOCK (never adjusting) · pin yes | Ten | seated · VISIBLE | full · EG04 | nano_banana_pro | — |
| **TH-05** | Act 4 | P-016 "Do not take my word for it. One knee only. Leave the other bare." | TH | C1 | L-WORKSHOP | M-D1 · E-TH | SELFIE, seated at the vice end of the bench (R2 static) | — | east factory windows over the bench · key L · morning | — | — | absent · — | full · EG03 · EG05 | HeyGen Avatar V (seed nano_banana_pro) | — |
| **BR-16** | Act 4 | P-016 "Go down your own stairs. You will know in a minute." | BR | S1 | L-S-STAIRS | W-D2 · E-STAIRS | high · three-quarter-back · FULL · clean — high from the landing = the whole flight ahead of her | deep · deep | landing window + front-door glass (north) · key R · morning | from the landing she starts down the stairs forwards, one knee strapped, the other bare · one step a second · sway · stairs: descending away from camera (safe) · pin no | stairs | worn (one knee) · VISIBLE | full · EG04 | nano_banana_pro | — |
| **TH-06** | Act 4 | P-017 | TH | C1 | L-WORKSHOP | M-D1 · E-TH | SELFIE, seated at the vice end of the bench (R2 static) | — | east factory windows over the bench · key L · morning | — | — | absent · — | full · EG03 · EG05 | HeyGen Avatar V (seed nano_banana_pro) | — |
| **BR-18a** | Act 4 | P-018 "Two for one, so you can do both knees." | BR | C1 hands | L-WORKSHOP (P2 bench) | M-D1 · E-BENCH | eye · three-quarter · CU · clean | product · deep | east factory windows over the bench · key L · morning | he holds two straps up side by side to the lens · one lift in 2s · sway · held product: two units (§9 pair pack) · pin yes | Two | held ×2 · — | full · EG07 · offer card (CapCut) | nano_banana_pro | — |
| **BR-18b** | Act 4 | P-018 "Sixty days, and you keep the straps. From the Stryde site, not a marketplace." | BR | C1 hands | L-WORKSHOP (P2 bench) | M-D1 · E-BENCH | overhead · front · CU · clean — overhead = the open box, what you get | product · deep | east factory windows over the bench · key L · morning | his hands lift the lid off the box: two straps lying flat in the insert · one lift in 2s · still · none · pin yes | Sixty | box open, two units (package_open) · — | full · offer card (CapCut) | nano_banana_pro | — |
| **TH-07** | Act 4 | P-019 | TH | C1 | L-WORKSHOP | M-D1 · E-TH | SELFIE, seated at the vice end of the bench (R2 static) | — | east factory windows over the bench · key L · morning | — | — | absent · — | full · EG03 · EG05 | HeyGen Avatar V (seed nano_banana_pro) | — |
**Product first appearance:** TH-04 (P-009, held low in frame), named on screen at BR-15a. **Screen direction:** stairs hold a `GEO-LINE`: the flight rises on the **left** of frame from the hall (P0); descents come down right-to-left from the landing. **Talking-head set:** one setup for every body TH (seated at the vice end, selfie), so the face returns to the same place like inspo 2. **Numbers** (17×, 34%, 200,000, the offer) are CapCut overlays, never generated (§17).

**HK1 route (unverified):** HeyGen photo avatars don't walk. Plan: a Kling 3.0 walking-selfie clip from the approved HK1 seed (§27G: one action, one slow step a second), then HeyGen **lip-sync** (`create_lipsync`) with the HK1 VO. If HeyGen's lip-sync fails the §22W check, fallback: HK1 seated like HK2 with the rail in the background (say if you'd rather start there).

### Visual Instruction Ledger — assigned (§27F)

| ID | Carried by | Status |
|---|---|---|
| VN01 | **HK1**: walking selfie down the P3 rail aisle, braces racking past behind the shoulder. **EG01 title cards, verbatim, 0–6s, CapCut:** white box "Where knee pain actually comes from" / red box "From a man who has made knee braces for 30 years." | assigned · F4 open |
| VN02 | **HK2**: static selfie seated at the vice, a half-finished generic hinged brace clamped beside his face, never touched; **no title cards** | assigned |
| VN03 | **HK3-BR** (tight on the two curled halves; his hand lifts one to camera) → **HK3-BR2** (the phone pulls back to him, he is still) → **HK3-TH**. The script's one shot is split at the hand-lift because §27G never has the camera and the subject both move in one clip | assigned · nearest compliant execution |

### Wardrobe map (§21, §14A)

**A. Talking-head wardrobe:** C1 in the sheet outfit for every TH, all acts and all three hooks (**M-D1**). The hooks are alternate openings of **one recording** butted onto one body, so they share it (§14: alternate takes of one moment share wardrobe; different outfits would jump at the seam). F11.

**B. B-roll wardrobe — one outfit per story day**

| Day | Subject | BASE | MID | OUTER | LOWER | FOOT | ACCENT | Colour family | Events · visibility · beats |
|---|---|---|---|---|---|---|---|---|---|
| M-D1 | C1 | green-and-brown check flannel shirt, sleeves rolled | — | faded navy canvas work apron | grey work trousers | brown leather work boots *(signature)* | — | earth | E-HK1–3, E-TH, E-BENCH, E-RAIL, E-FIT · — · every TH, HK3-BR/BR2, BR-05a/b, BR-07b, BR-11, BR-14a/b, BR-15a, BR-18a/b (and his side of BR-02, BR-10, BR-15b) |
| W-D0 | S1 (before) | dusty-pink polo-neck jumper | — | — | heather-grey wool skirt, a hand above the knee | sheepskin slippers | — | red/pink | E-BEFORE · bare knee / sleeve · BR-07a, BR-08 |
| W-D1 | S1 (the fitting) | white cotton blouse | cornflower-blue cardigan | — | dark green corduroy skirt, a hand above the knee | tan leather ankle boots *(signature)* | — | blue | E-FIT · VISIBLE · BR-02, BR-10, BR-15b |
| W-D2 | S1 (after, at home) | mustard lambswool crew-neck jumper | — | — | navy corduroy A-line skirt, a hand above the knee | tan leather ankle boots *(signature)* | — | yellow | E-STAIRS, E-LIVING · VISIBLE · BR-03a, BR-03b, BR-12, BR-13, BR-15c, BR-16 |
| W-D3 | S1 (the dog walk) | chambray shirt | — | green waxed jacket (the one on her hall hook) | stone walking shorts to just above the knee | tan leather ankle boots *(signature)* | red dog lead | green | E-DOG · VISIBLE · BR-03c |

**Signature items:** C1 brown leather work boots · S1 tan leather ankle boots.

| # | Audit | Result |
|---|---|---|
| **W1** | No BASE class twice in an act; no exact garment twice except signatures | Act 1: blouse · jumper · shirt ✓ · Act 2: polo-neck ✓ · Act 3: blouse · jumper ✓ · Act 4: blouse · jumper ✓ · repeats: signatures and M-D1 (one recording) only ✓ |
| **W2** | Consecutive days differ on ≥2 layers incl. BASE | W-D0→W-D1 BASE, MID, LOWER, FOOT ✓ · W-D1→W-D2 BASE, MID, LOWER ✓ · W-D2→W-D3 BASE, OUTER, LOWER ✓ |
| **W3** | Colour families rotate; positive days carry colour | pink → blue → yellow → green ✓ · after-days blue, yellow, green ✓ |
| **W4** | Every event → one day → one outfit | 11 events → 5 days → 5 rows ✓ |

**Hem rule (§9D):** every VISIBLE row's LOWER ends above the knee ✓. The activity picked each garment; none was chosen to expose the product.

### Reconciliation (§27B)

Hooks HK1–HK3 → 5 rows (HK1 TH · HK2 TH · HK3 = 2 BR + 1 TH) · body P-001–P-019 → **33 rows** (BR 21 · MECH 5 · TH 7) · splits: P-002, P-003 (×3), P-005 (×3), P-007, P-008, P-011, P-012, P-014, P-015 (×3), P-016, P-018 · merges: none · **uncovered 0 · blocked 0** · plants: "Go down your own stairs" paid by BR-16 after BR-03a/BR-13 · open flags: F3, F4, F11.

### Subject Registry (§30E)

| ID | Sheet (confirmed) | Beats |
|---|---|---|
| C1 maker | `a866e6f7…` | HK1–HK3, TH-01–TH-07, HK3-BR/BR2, BR-02 (finger), BR-05a/b, BR-07b, BR-10 (finger), BR-11, BR-14a/b, BR-15a/b, BR-18a/b |
| S1 wearer | `7cc9a07d…` | BR-02, BR-03a/b/c, BR-07a, BR-08, BR-10, BR-12, BR-13, BR-15b/c, BR-16 |
| one-offs | — | her border terrier (BR-03c) |

### New flags

| # | Where | Finding | Recommendation |
|---|---|---|---|
| F11 | Wardrobe | §14 gives different openings different days; here the three hooks are alternate openings of one recording joined to one body | One outfit for the maker throughout. Say if you want each hook on its own day |
| F12 | HK1 | Talking while walking is outside HeyGen's photo avatar | Kling walking clip + HeyGen lip-sync (unverified); fallback seated |
| F13 | BR-02, BR-10, BR-15b | The maker fitting S1 in his workshop is added story (the script says "the one I hand people") | It shows the "hand people" line and the placement; say if you'd rather keep her only at home |
