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

Spend: 4 Sunburst jobs, 27 credits. **Scene Registry (§30C 7a):** these four job IDs are what every beat in their location attaches.

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

