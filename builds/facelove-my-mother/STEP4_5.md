# Steps 4–5 — facelove-my-mother (Mode 4 film, Manual)

Built 2026-10-02 on the user's "go". **Board state (user, 2026-10-02):** all 8 cast sheets and 7 plates **confirmed**; L-VANITY-REV **retired** on the user's Fix ("dont use this") — SC05-SH01/SH02 restaged on L-VANITY. Flags from steps 1–3 run on my recommendations until you say otherwise (one hook so far — F3; claims voiced as written — F4–F9; the stick violet, unlabelled to the viewer until the hero — F10).

## 4. Property and location maps (§30G, §30C)

### Story geography (read from the script)

- **The party yard is the hosts' house, not Susan's.** "The same yard I'd been hiding from for months. I almost turned the car around" (L021) only works if she drives to it; SC02 ends with "the porch door clicks shut behind her" and SC03 has her back against that door inside — the hosts' back hall. The hosts are the group's usual party house (not named in the script). **F16** — confirm, or say if it's Susan and Greg's own yard.
- **SC04's mirror and SC05–SC06's mirror are the same mirror** — her bedroom dressing table: "every morning the mirror agreed with them" → Beth pulls out "the vanity stool" → "The mirror, her enemy all film, gives her back" (VN20). One location, two story days.

### Property Sheet — P-HOUSE (Susan's house)

| # | Field | Value |
|---|---|---|
| 1 | Type and era | two-storey 1990s American suburban family house; the same couple thirty years |
| 2 | Shell | warm greige eggshell on smooth drywall · white colonial baseboards and casings · white six-panel doors, brushed-nickel knobs · flat white ceilings, recessed cans · honey oak downstairs → beige carpet on the stairs and bedrooms · white floor vents · white decora switches |
| 3 | Floor map | front door → hall; stairs up the left wall, white banister on the right; kitchen through the wide doorway on the right (white shaker cabinets, beige granite, island with stools); main bedroom upstairs at the front |
| 4 | Orientation | front (main bedroom window, hall door glass) faces the street — soft daylight; kitchen window to the back yard |
| 5 | Carried elements | the white dressing table and its large mirror · the dusty-blue quilt · the kitchen island · the stair-wall photographs |
| 6 | Exterior | not shown in this film |
| 7 | Standing negatives | none yet |

### Location Sheets

| ID | Tier | Shots | Owner | Anchors (restated in every shot) | Light profile | Plate |
|---|---|---|---|---|---|---|
| P-HOUSE (hall + kitchen) | PLATED (property plate) | SC04-SH01 (the invite on the island) | Susan | stairs up the left wall, white banister, photos up the wall, wide doorway to the kitchen, granite island | overcast morning through the kitchen window, 6500K | v1 confirmed |
| L-VANITY | PLATED | SC04 (mirror), SC05, SC06 — 16 shots (SC05's entrance from the plate's own doorway view) | Susan | white dressing table + large rectangular mirror under the right-hand window, upholstered stool, queen bed with the dusty-blue quilt, sheer curtains | window over the dressing table: cool morning 6500K (SC04) · soft warm afternoon 5000K (SC05–06) | v1 confirmed |
| L-YARD | PLATED | SC01, SC02, SC07, SC08, SC09 — 24 shots | the hosts | the long white-clothed table down the lawn, the uncut white sheet cake mid-table, the bulb swags on posts, the deck steps + glass-paned back door, the drinks table left of the steps | sun low behind the house + 2700K bulbs; white balance 3800K (D1), 4300K (D5) | v1 confirmed |
| L-YARD-REV | PLATED (reverse, L24) | SC09-SH02; reference for SC07-SH03 | the hosts | the table running away down the lawn, the drinks table at near right, the hedge and trees at the far end | backlit by the low sun in the trees | v1 confirmed |
| L-PORCH-IN | PLATED | SC03 (2 shots) | the hosts | the white back door with its glass upper pane, the party glow through it, coat hooks and bench on the left | only the party glow through the glass, 8:1; white balance 4300K | v1 confirmed |
| L-HOSTS-FRONT | PLATED | SC07-SH01–02 | the hosts | pale grey clapboard house, red door, white balloons on the mailbox, cars at the curb, the side gate | low sun behind the camera, 4300K | v1 confirmed |
| L-GATHERING | PLATED | SC04-SH02 | the daughter | grey sectional under the big window, coffee table with the plain white birthday cake, pastel balloons, bookshelf left | big window, afternoon 5600K | v1 confirmed |
| PRODUCT | INCIDENTAL | SC09-SH03 | — | pale stone surface, soft window light | 5000K | hero card at SC09 |

**Set checks:** S1 tiers above · S2 golden hour (D1, D5), dusk (SC03), morning (D2), afternoon (D3, D4) · S3 the yard's sun stays behind the house (frame left from the lawn, backlight from the deck) · S4 consecutive scenes change place except SC01→SC02 (one continuous moment) and SC05→SC06 (one continuous moment). **The set closes here.**

## 5. Act map, takes, wardrobe, music

### Story spine (§24I part 9)

want — to stop being counted out · stakes — the group that saw the low point · obstacle — the face the mirror agrees with · failed fix — the old foundation caking into the lines · turn — Beth: "Watch this." (SC05) · payoff — Paula: "what are you doing?" / "Go enjoy the party, Greg." · plants → payoffs: the cake (SC01-SH09 → SC07-SH07), the yard (SC01 → SC07), the high wide (SC01-SH08 → SC08-SH04), the mirror (SC04 → SC06), "ask her what she does" (L005 → L023).

### Act map (E4) — 48 shots, 26 Seedance takes · ~3:51 at the planned shot lengths

Full rows (setup, focus, light, cast, story day, ingredients, start/end positions): `step5/act_map.json` (built by `step5/act_map.py`). **Checks:** `angles.py` **PASS** (angles, shot library, focus, light) · `wardrobe.py` **PASS** · `visual_plan.py` **PASS** · `takes.py` 6 FAIL lines, all of one kind — see below.

**`takes.py` SPLIT:** its "length" check counts shots only (≤ 4) and ignores seconds, while its own TAKE+ check holds every take to 15 s. The six flagged pairs would run **21, 22, 25, 24, 17 and 18 s** as one take, over the 15 s limit, so each split stands. Noted for the owner (BUILD_NOTES); not changeable from this account.

| Beat | Take | Loc · day | Shot | Setup | Lines | Action | Rig | Music |
|---|---|---|---|---|---|---|---|---|
| SC01-SH01 | SC01-T1 | L-YARD · D1 | SH-WIDE+SH-34 | eye/three-quarter/WIDE | L001 | Greg pushes up from his chair at the table's middle, sways a little and taps his wine glass with a fork; the table turns to him smiling | F2 | none (room tone — script VN07) |
| SC01-SH02 | SC01-T1 | L-YARD · D1 | SH-MED+SH-LOW | low/three-quarter/MEDIUM | L001 | Greg, standing, glass raised, warm grin, delivers the toast to the table | F2 | none (room tone — script VN07) |
| SC01-SH03 | SC01-T1 | L-YARD · D1 | SH-EYE | eye/front/MCU | L001 | glasses rise around her; Susan almost smiles and lifts her glass an inch | F2 | none (room tone — script VN07) |
| SC01-SH04 | SC01-T2 (length) | L-YARD · D1 | SH-CU+SH-FGFOC | eye/three-quarter/CU | L002,L003 | Greg's voice above her goes quiet; her almost-smile goes; her eyes stay level, not on him; her right hand finds the edge of the table | F1 | none (room tone — script VN07) |
| SC01-SH05 | SC01-T3 (length) | L-YARD · D1 | SH-CU+SH-PROFILE | eye/profile/CU | L004 | Susan, without moving her body, says it low to him | F2 | none (room tone — script VN07) |
| SC01-SH06 | SC01-T3 | L-YARD · D1 | SH-HIGH | high/front/MCU | L005 | Greg's loose hand enters frame edge pointing across at her; Paula keeps her eyes on her plate | F2 | none (room tone — script VN07) |
| SC01-SH07 | SC01-T3 | L-YARD · D1 | SH-CU+SH-EYE | eye/front/CU | L005 | Susan absolutely still, eyes level, breathing once | F2 | none (room tone — script VN07) |
| SC01-SH08 | SC01-T4 (length) | L-YARD · D1 | SH-WIDE+SH-HIGH | high/three-quarter-back/WIDE | — | Greg drops back into his chair and reaches past the cake for his drink; nobody at the table moves | F2 | none (room tone — script VN07) |
| SC01-SH09 | SC01-T4 | L-YARD · D1 | SH-CU+SH-HIGH | high/front/CU | — | nothing moves; the bulb light flickers faintly on the white frosting | F2 | none (room tone — script VN07) |
| SC02-SH01 | SC02-T1 | L-YARD · D1 | SH-MED+SH-34 | eye/three-quarter/MEDIUM | — | Susan stands, folds her napkin once and sets it beside the cake | F2 | none (room tone — script: no music under the heaviest beats) |
| SC02-SH02 | SC02-T1 | L-YARD · D1 | SH-MED+SH-PROFILE | eye/profile/MEDIUM | L006 | Friend A, low, to Friend B; behind them Susan walks past toward the deck, soft | F2 | none (room tone — script: no music under the heaviest beats) |
| SC02-SH03 | SC02-T1 | L-YARD · D1 | SH-EYE | eye/front/MCU | L007 | Susan walking toward the camera at a steady pace; her eyes flick once, she keeps walking | F5 | none (room tone — script: no music under the heaviest beats) |
| SC02-SH04 | SC02-T1 | L-YARD · D1 | SH-WIDE+SH-REAR | low/behind/WIDE | — | Susan climbs the three deck steps, opens the glass-paned back door and closes it behind her | F2 | none (room tone — script: no music under the heaviest beats) |
| SC03-SH01 | SC03-T1 | L-PORCH-IN · D1 | SH-MED+SH-HIGH | high/front/MEDIUM | L008 | Susan leans back against the shut door, eyes closed, one slow breath out | F2 | MUS-OPEN |
| SC03-SH02 | SC03-T1 | L-PORCH-IN · D1 | SH-CU+SH-34 | eye/three-quarter/CU | L008 | she opens her eyes and looks at nothing; jaw set | F1 | MUS-OPEN |
| SC04-SH01 | SC04-T1 | P-HOUSE · D2 | SH-CU+SH-HIGH | high/front/CU | L009 | her hand turns a party invite face-down on the granite and sets her phone face-down on top of it | F2 | MUS-EXPOSE |
| SC04-SH02 | SC04-T2 | L-GATHERING · D3 | SH-REAR | eye/behind/FULL | L009 | the daughter waves her into the photo; Susan shakes her head, raises the phone and takes the picture of them, one step back | F2 | MUS-EXPOSE |
| SC04-SH03 | SC04-T3 | L-VANITY · D2 | SH-EYE | eye/front/MCU | L009 | Susan at the dressing table dabs foundation from a plain unlabelled bottle onto her cheek with a sponge | F2 | MUS-EXPOSE |
| SC04-SH04 | SC04-T3 | L-VANITY · D2 | SH-MACRO | eye/three-quarter/ECU | L009 | the beige foundation sits grey and dry in the crease beside her mouth, flaking at the edges as she smiles slightly | F2 | MUS-EXPOSE |
| SC04-SH05 | SC04-T3 | L-VANITY · D2 | SH-CU+SH-34 | eye/three-quarter/CU | L009 | the sponge stops halfway to her face; she lowers it slowly and just looks | F2 | none (drops out on the mirror — VN14) |
| SC05-SH01 | SC05-T1 | L-VANITY · D4 | SH-WIDE+SH-PROFILE | eye/profile/WIDE | L010 | Beth walks in from behind the camera, garment bag over her shoulder, stops in profile between the bed and the dressing table, looks at Susan and says it plainly | F2 | MUS-EDU |
| SC05-SH02 | SC05-T1 | L-VANITY · D4 | SH-HIGH+SH-34 | high/three-quarter/MCU | L011 | Susan doesn't get up; she says it to her hands | F2 | MUS-EDU |
| SC05-SH03 | SC05-T2 (length) | L-VANITY · D4 | SH-MED+SH-34 | eye/three-quarter/MEDIUM | L012 | Beth lays the garment bag on the bed and talks while she does it | F2 | MUS-EDU |
| SC05-SH04 | SC05-T2 | L-VANITY · D4 | SH-MED+SH-PROFILE | eye/profile/MEDIUM | L013 | Beth pulls the dressing-table stool out with one hand and nods Susan to it; Susan gets up from the bed and sits | F2 | MUS-EDU |
| SC05-SH05 | SC05-T3 (length) | L-VANITY · D4 | SH-34+SH-HIGH | high/three-quarter/MCU | L014 | Beth tilts Susan's chin to the window with two fingers, takes the closed violet stick from her pocket, her palm over the wordmark, and pulls the cap off the balm end | F2 | MUS-TURN |
| SC05-SH06 | SC05-T4 (insert) | L-VANITY · D4 | SH-MACRO+SH-PROFILE | eye/profile/ECU | L014 | the balm's flat crest draws one white stripe up Susan's cheekbone | F2 | MUS-AFTER |
| SC05-SH07 | SC05-T5 (insert) | L-VANITY · D4 | SH-CU+SH-EYE | eye/front/CU | L015 | the brush end works the white stripe in small circles; behind the brush the white turns to her own skin tone, ahead of it the stripe stays white | F2 | MUS-AFTER |
| SC05-SH08 | SC05-T6 (insert) | L-VANITY · D4 | SH-MED+SH-34 | eye/three-quarter/MEDIUM | L016 | Beth steps back one step behind Susan's shoulder and talks to her reflection | F2 | MUS-AFTER |
| SC05-SH09 | SC05-T6 | L-VANITY · D4 | SH-CU+SH-EYE | eye/front/CU | L016 | Susan leans an inch toward the mirror and looks at her cheek | F1 | MUS-AFTER |
| SC05-SH10 | SC05-T6 | L-VANITY · D4 | SH-CU+SH-LOW | low/three-quarter/CU | L017 | Susan turns her head a little toward Beth | F2 | MUS-AFTER |
| SC05-SH11 | SC05-T7 (length) | L-VANITY · D4 | SH-34 | eye/three-quarter/MCU | L018 | Beth nods once and says it | F2 | MUS-AFTER |
| SC06-SH01 | SC06-T1 | L-VANITY · D4 | SH-CU+SH-LOW | low/front/CU | L019 | Susan holds her own eyes in the mirror and says it almost to nothing | F1 | MUS-AFTER |
| SC06-SH02 | SC06-T1 | L-VANITY · D4 | SH-OTS+SH-MED | eye/ots/MEDIUM | L020 | Beth, in the reflection, rests a hand on Susan's shoulder and says it | F2 | MUS-AFTER |
| SC07-SH01 | SC07-T1 | L-HOSTS-FRONT · D5 | SH-WIDE+SH-PROFILE | eye/profile/WIDE | L021 | a silver sedan sits parked at the curb outside the house; nobody gets out | F2 | MUS-AFTER |
| SC07-SH02 | SC07-T1 | L-HOSTS-FRONT · D5 | SH-OCCL+SH-34 | eye/three-quarter/MCU | L021 | Susan's hands tighten on the wheel; Beth lays a hand on her forearm; Susan breathes out and takes the key out | F2 | MUS-AFTER |
| SC07-SH03 | SC07-T2 | L-YARD · D5 | SH-WIDE | eye/front/WIDE | — | Susan and Beth walk in from the side of the house onto the lawn; heads at the table turn; the talk stops, then Friend A's face lights up | F6 | MUS-AFTER |
| SC07-SH04 | SC07-T2 | L-YARD · D5 | SH-MED+SH-34 | eye/three-quarter/MEDIUM | L022 | Paula crosses the lawn to Susan, both hands out, and takes her hands | F5 | MUS-AFTER |
| SC07-SH05 | SC07-T3 (length) | L-YARD · D5 | SH-CU+SH-34 | eye/three-quarter/CU | L023 | Susan, holding Paula's hands, says it lightly | F2 | MUS-AFTER |
| SC07-SH06 | SC07-T3 | L-YARD · D5 | SH-MED+SH-PROFILE | eye/profile/MEDIUM | — | Paula catches it, a surprised breath, then a real laugh, the two of them laughing together; far behind, Greg goes still | F2 | MUS-AFTER |
| SC07-SH07 | SC07-T3 | L-YARD · D5 | SH-CU+SH-HIGH | high/front/CU | — | a knife cuts a slice from the white sheet cake and a hand passes the plate along | F2 | MUS-AFTER |
| SC08-SH01 | SC08-T1 | L-YARD · D5 | SH-OTS+SH-MED | eye/ots/MEDIUM | L024 | Greg, at her shoulder, speaks low; his hand half lifts and drops | F2 | MUS-AFTER |
| SC08-SH02 | SC08-T1 | L-YARD · D5 | SH-CU+SH-34 | eye/three-quarter/CU | L025 | Susan looks at him, kind, and says it | F2 | MUS-AFTER |
| SC08-SH03 | SC08-T1 | L-YARD · D5 | SH-REAR | eye/three-quarter-back/FULL | L026 | Susan turns away to Beth and Paula and laughs with them; Greg stays where he is | F2 | MUS-AFTER |
| SC08-SH04 | SC08-T2 (length) | L-YARD · D5 | SH-WIDE+SH-HIGH | high/three-quarter/WIDE | L026 | Susan in the middle of the group by the table, talking and laughing; Greg alone at the edge of the lawn | F1 | MUS-AFTER |
| SC09-SH01 | SC09-T1 | L-YARD · D5 | SH-34+SH-FGFOC | eye/three-quarter/MCU | L027 | a plate of cake is passed to Susan; she takes it, laughing at something Beth says | F2 | MUS-OFFER |
| SC09-SH02 | SC09-T2 | L-YARD-REV · D5 | SH-WIDE+SH-EYE | eye/front/WIDE | L027 | the long table full, people passing cake and talking under the bulbs | F2 | MUS-OFFER |
| SC09-SH03 | SC09-T3 | PRODUCT · P | SH-CU+SH-HIGH | high/front/CU | L027 | two closed violet sticks standing upright beside the white primer tube on a pale stone surface; slow push-in | F1 | MUS-OFFER |
| SC09-SH04 | SC09-T4 | L-YARD · D5 | SH-CU+SH-LOW | low/three-quarter/CU | L027 | Susan, laughing with someone off frame, glances down at the table and smiles to herself | F2 | MUS-OFFER |

### Takes (§24K part 5) — one Seedance call each

| Take | Kind | Shots | Seconds | Location | Ingredients | Start → end |
|---|---|---|---|---|---|---|
| SC01-T1 | multi | SH01, SH02, SH03 | 12 | L-YARD | C1, C2, C3, C5, C6, CAKE-CARD, L-YARD, N, VOICE-C1, X1 | the table full on both sides under the bulbs; Greg seated mid-table on the far side facing → Greg standing beside Susan on her left (frame right), glass raised; Su |
| SC01-T2 | one-take | SH04 | 9 | L-YARD | L-YARD, N | Susan seated, Greg standing on her left just out of frame, the white cake soft in the near → Susan still, hand on the table edge, eyes level |
| SC01-T3 | multi | SH05, SH06, SH07 | 13 | L-YARD | C2, L-YARD, N | Susan seated in profile facing frame left toward Greg standing just out of frame left → Susan still at the table, hand on the edge; Greg standing on her left |
| SC01-T4 | multi | SH08, SH09 | 7 | L-YARD | C1, C2, CAKE-CARD, L-YARD, N, X1 | Greg standing beside Susan, the table frozen → Greg seated with his drink, Susan beside him still, the cake untouched |
| SC02-T1 | multi | SH01, SH02, SH03, SH04 | 15 | L-YARD | C5, C6, CAKE-CARD, L-YARD, N | Susan seated at the table, napkin in her lap, the cake in front of her → the back door shut, Susan gone inside; the party behind the camera |
| SC03-T1 | multi | SH01, SH02 | 15 | L-PORCH-IN | L-PORCH-IN, L-YARD, N | Susan just inside the shut back door, her back to the glass, the party glow behind her hea → Susan against the door, eyes open |
| SC04-T1 | insert | SH01 | 5 | P-HOUSE | INVITE-CARD, N, P-HOUSE | a plain invite card face-up on the kitchen island, her hand coming in → invite face-down under the phone, her hand leaving |
| SC04-T2 | single | SH02 | 4 | L-GATHERING | C4, L-GATHERING, N | the family on the grey sectional around the cake, the daughter in the middle; Susan standi → Susan one step further back, phone up |
| SC04-T3 | multi | SH03, SH04, SH05 | 11 | L-VANITY | L-VANITY, N, OLD-FOUNDATION-CARD | Susan seated on the stool at the dressing table facing the mirror, a plain unlabelled foun → Susan at the dressing table, sponge lowered, still |
| SC05-T1 | multi | SH01, SH02 | 11 | L-VANITY | C3, L-VANITY, N, VOICE-C3 | Susan sitting on the end of the bed (frame left) in her sweatshirt, facing the room; the d → Susan on the end of the bed, Beth inside the door with the garment bag |
| SC05-T2 | multi | SH03, SH04 | 14 | L-VANITY | C3, L-VANITY, N | Beth standing by the bed with the garment bag; Susan on the end of the bed → Susan seated on the stool facing the mirror; Beth standing at her left |
| SC05-T3 | multi | SH05 | 10 | L-VANITY | C3, L-VANITY, N, PROD-BALM, PROD-CLOSED, PROD-HAND-CARD | Susan seated facing the mirror, Beth at her left shoulder → the balm end uncapped in Beth's right hand at Susan's cheek |
| SC05-T4 | insert | SH06 | 3 | L-VANITY | COLOUR-FRONT-CARD, N, PROD-BALM | the balm end at her cheekbone → a white stripe on her cheek, the stick lifting away |
| SC05-T5 | insert | SH07 | 8 | L-VANITY | COLOUR-FRONT-CARD, N, PROD-BRUSH | a white stripe on her cheek, the brush end touching its lower end → the cheek evened, every line still there |
| SC05-T6 | multi | SH08, SH09, SH10 | 15 | L-VANITY | C3, L-VANITY, N | Susan seated facing the mirror, Beth at her left shoulder holding the closed stick → Susan turned a little toward Beth |
| SC05-T7 | single | SH11 | 2 | L-VANITY | C3, L-VANITY | Susan seated at the mirror turned a little toward Beth behind her left shoulder → Susan seated at the mirror, Beth standing behind her left shoulder |
| SC06-T1 | multi | SH01, SH02 | 8 | L-VANITY | C3, L-VANITY, N | Susan seated at the mirror, Beth behind her left shoulder → the two of them in the mirror, Beth's hand on Susan's shoulder |
| SC07-T1 | multi | SH01, SH02 | 7 | L-HOSTS-FRONT | C3, L-HOSTS-FRONT, L-YARD, N | the car parked at the curb in front of the house, Susan at the wheel, Beth in the passenge → Susan and Beth in the car, about to get out |
| SC07-T2 | multi | SH03, SH04 | 10 | L-YARD | C2, C3, C5, L-YARD, L-YARD-REV, N | the party at the long table under the bulbs, the cake on the table; Susan and Beth at the  → Paula and Susan facing each other on the lawn, holding hands |
| SC07-T3 | multi | SH05, SH06, SH07 | 10 | L-YARD | C1, C2, CAKE-CARD, L-YARD, N | Paula and Susan facing each other on the lawn, holding hands → the party going on, Susan and Paula together on the lawn |
| SC08-T1 | multi | SH01, SH02, SH03 | 11 | L-YARD | C1, C2, C3, L-YARD, N, VOICE-C1, VOICE-N | Susan standing on the lawn near the table with Beth and Paula a step away; Greg arriving a → Susan with Beth and Paula by the table, Greg alone two steps behind |
| SC08-T2 | single | SH04 | 7 | L-YARD | C1, C2, C3, C5, C6, L-YARD, N, X1 | Susan with Beth and Paula by the table, friends around; Greg alone two steps behind → the same |
| SC09-T1 | multi | SH01 | 6 | L-YARD | C2, C3, CAKE-CARD, L-YARD, N | Susan at the table between Beth and Paula → Susan with a plate of cake, laughing |
| SC09-T2 | single | SH02 | 5 | L-YARD-REV | C2, C3, C5, C6, L-YARD-REV, N, X1 | the long table full under the bulbs, Susan in the middle between Beth and Paula → the table full |
| SC09-T3 | insert | SH03 | 8 | PRODUCT | HERO-CARD, PROD-CLOSED, PROD-PRIMER | the three products on the surface, wordmarks to camera → the same, closer |
| SC09-T4 | single | SH04 | 5 | L-YARD | L-YARD, N | Susan at the table under the bulbs, friends around her → the same, Susan smiling |

### Wardrobe map (§14A, §21, V7.89.0) — per story day and event

### Wardrobe map — per story day and event

One block per story day, in story order: the event, what makes it a day, each person's outfit, and the day's events with their beats. Never grouped by act (§21, V7.89.0).

### D1 — the thirtieth-anniversary dinner party in the hosts' back yard, golden hour into dusk

*Why it is a day:* stated: GREG "Thirty years." — the toast; scene heads 1–3

| Who | Outfit |
|---|---|
| Susan | dusty-blue loose chiffon blouse with a soft V neck, cream straight linen trousers, nude flats, small pearl drop earrings (her SUSAN OLD picture); hair loose, a little limp |
| Greg | navy textured blazer, pale blue open-collar shirt, khaki chinos, brown loafers (sheet) |
| Paula | plum satin cowl-neck sleeveless top, charcoal trousers, black mules (sheet) |
| Beth | emerald satin square-neck puff-sleeve top, dark indigo jeans, tan flats (sheet) |
| Friend A | mustard linen wrap dress, tan sandals (sheet) |
| Friend B | pale pink silk shirt, white wide-leg linen trousers, nude heeled sandals (sheet) |
| Party guests | summer dinner-party clothes in muted creams, blues and greys; nobody in red or wine |

| Event | Place | Beats |
|---|---|---|
| D1-E1 | L-YARD · VISIBLE | SC01-SH01, SC01-SH02, SC01-SH03, SC01-SH04, SC01-SH05, SC01-SH06, SC01-SH07, SC01-SH08, SC01-SH09, SC02-SH01, SC02-SH02, SC02-SH03, SC02-SH04 |
| D1-E2 | L-PORCH-IN · VISIBLE | SC03-SH01, SC03-SH02 |

### D2 — a weekday morning months later — the invite turned over, the mirror

*Why it is a day:* stated: VO "every morning the mirror agreed with them"; "I stopped going"

| Who | Outfit |
|---|---|
| Susan | grey marl cardigan over a plain white T-shirt, grey cotton lounge trousers, bare feet; hair pulled back in a loose claw clip |

| Event | Place | Beats |
|---|---|---|
| D2-E1 | P-HOUSE · HANDS | SC04-SH01 |
| D2-E2 | L-VANITY · VISIBLE | SC04-SH03, SC04-SH04, SC04-SH05 |

### D3 — a family birthday at the daughter's house, a Sunday afternoon

*Why it is a day:* stated: VO "Skipped the birthdays"; visual note VN13

| Who | Outfit |
|---|---|
| Susan | oatmeal crew-neck knit sweater, dark straight jeans, white trainers |
| Daughter | cream ribbed cardigan, white T-shirt, light-wash jeans (sheet) |
| Family (gathering) | relaxed Sunday clothes, a party hat on the birthday child |

| Event | Place | Beats |
|---|---|---|
| D3-E1 | L-GATHERING · VISIBLE | SC04-SH02 |

### D4 — the afternoon Beth lets herself in, before Saturday

*Why it is a day:* stated: BETH "There's a thing Saturday. Whole group. You're coming."

| Who | Outfit |
|---|---|
| Susan | faded sage-green crew sweatshirt, grey cotton lounge trousers, socks; hair unwashed in a low ponytail — the face goes from bare to the foundation on during SC05 (N-SUSAN face to SC05-SH06, N-SUSAN-AFTER face from SC05-SH07, hair unchanged) |
| Beth | light chambray shirt with sleeves rolled, white straight jeans, tan leather flats; a black garment bag over her shoulder |

| Event | Place | Beats |
|---|---|---|
| D4-E1 | L-VANITY · VISIBLE | SC05-SH01, SC05-SH02, SC05-SH03, SC05-SH04, SC05-SH05, SC05-SH06, SC05-SH07, SC05-SH08, SC05-SH09, SC05-SH10, SC05-SH11, SC06-SH01, SC06-SH02 |

### D5 — Saturday — the group's party in the same yard, late afternoon into dusk

*Why it is a day:* stated: VO "Saturday. The same yard I'd been hiding from for months."

| Who | Outfit |
|---|---|
| Susan | wine-red satin sleeveless top with a draped neckline, slim black ankle trousers, black low-heeled pumps, gold teardrop earrings (her SUSAN NEW picture — the top from Beth's garment bag); hair washed and in soft waves |
| Greg | white linen shirt with the sleeves rolled, grey chinos, brown loafers |
| Paula | navy wrap dress to the knee, gold egg-drop earrings, black sandals |
| Beth | cream linen blouse, olive wide-leg trousers, tan sandals |
| Friend A | teal cotton sundress, tan sandals |
| Friend B | black sleeveless silk blouse, white trousers, nude sandals |
| Party guests | summer party clothes in muted creams, blues and greens; nobody in red or wine |

| Event | Place | Beats |
|---|---|---|
| D5-E1 | L-HOSTS-FRONT · VISIBLE | SC07-SH01, SC07-SH02 |
| D5-E2 | L-YARD · VISIBLE | SC07-SH03, SC07-SH04, SC07-SH05, SC07-SH06, SC07-SH07, SC08-SH01, SC08-SH02, SC08-SH03, SC08-SH04, SC09-SH01, SC09-SH02, SC09-SH04 |

### P — the product hero for the offer — no people

*Why it is a day:* event: the offer, VN26

| Who | Outfit |
|---|---|

| Event | Place | Beats |
|---|---|---|
| P-E1 | PRODUCT · NONE | SC09-SH03 |

### Music Register Map (§40A, Build Sheet 5c) — one family: sparse piano, low bowed strings, a soft slow pulse (~70 bpm), a three-note motif

| Part | Shots | What the script is doing | Register | Cue in plain words | Entry / drop / hand-over |
|---|---|---|---|---|---|
| SC01 The toast | SC01-SH01–SH09 | the warm toast, then the verdict | **none — room tone only** | the script: "Room tone, no music" (VN07) — the party's own sound, then silence | glass clink and laughter, then nothing; the title lands in silence |
| SC02 The whisper | SC02-SH01–SH04 | the friends' verdict | **none — room tone** | the script: no music under the heaviest beats | ends on the door click |
| SC03 Inside | SC03-SH01–SH02 | she names what happened; the case opens | `MUS-OPEN` | a low drone and a slow pulse under the VO, one unresolved piano figure — investigation, never sad | enters just after the door click (the VO holds until after the door) |
| SC04 Disappearing | SC04-SH01–SH04 | the disappearing; the old foundation as the villain | `MUS-EXPOSE` | the drone darker, the pulse more present, a soft stinger on "the mirror agreed" | **drops out on the mirror (SC04-SH05, VN14)** |
| SC05 Beth (to the reveal) | SC05-SH01–SH04 | Beth concedes, reframes | `MUS-EDU` | a light repeating piano figure under the dialogue, low — curiosity | ducked under every line |
| **SC05-SH05 the stick** | product's first frame (~1:56) | the product appears | `MUS-TURN` | the drone lifts, the first warm chord, the motif turns major — **on the stick's first frame** (`product_at`) | |
| SC05–SC08 | SC05-SH06 → SC08-SH04 | the colour change, the mirror, the return, the redirect | `MUS-AFTER` | warm, hopeful, the motif carried by strings, a dignified lift — never cute | under the dialogue; swells on SC08-SH04 |
| SC09 CTA | SC09-SH01–SH04 | the offer | `MUS-OFFER` | confident, a steady pulse, a little brighter; drops under the offer line; ends on a held resolve | |

The music goes in at the edit (§24M) — never in a clip. Generated with `music.py plan --register` → `compose` → `check` at step 8, or laid by the team as CapCut lines at the §24M levels.

### Visual Instruction Ledger — assigned

| VN | Assigned to |
|---|---|
| VN01, VN02 | SC01-SH01 (+ CAKE-CARD: blank icing, post sets "Happy Anniversary" — F11) |
| VN03 | CapCut: "YOU LOOK LIKE MY MOTHER." on SC01-SH09 |
| VN04, VN05 | SC01-SH04 (push-in through the cake; Greg heard), SC01-SH07 |
| VN06, VN07 | SC01-SH06 (Paula; Greg's hand at frame edge; room tone) |
| VN08 | SC01-SH08 |
| VN09, VN10 | SC02-SH01–SH04 (SFX door click) |
| VN11 | SC03-SH01–SH02 |
| VN12 | SC04-SH01 (INVITE-CARD, blank — F11) |
| VN13 | SC04-SH02 |
| VN14 | SC04-SH03–SH05 (old foundation: OLD-FOUNDATION-CARD, blank bottle; music drops out) |
| VN15 | SC05-SH01, SC05-SH04 |
| VN16 | SC05-SH05 (violet stick, palm over the wordmark — F10) |
| VN17 | SC05-SH06 (swipe) + SC05-SH07 (the colour change, one continuous take, no ramp) |
| VN18 | SC05-SH05–SH07 |
| VN19 | SC05-SH08–SH09 (every line kept, `TERRAIN_LOCK`; "glowing" never in a prompt) |
| VN20 | SC06-SH01–SH02 |
| VN21 | SC07-SH03–SH04 |
| VN22 | SC07-SH05–SH06 |
| VN23 | SC07-SH07 (`mirror_of` SC01-SH09) |
| VN24 | SC08-SH01–SH03 |
| VN25 | SC08-SH04 |
| VN26 | SC09-SH01–SH03 (PRIMER photo; two sticks) |
| VN27 | CapCut overlay on SC09 (F8 on the 50,000) |

### Ingredient ledger — Seedance takes are made from information, never frames (V7.68.0)

| ID | Kind | What | Source | Made |
|---|---|---|---|---|
| N / N-A, C1–C6 | character | the cast sheets — **day outfits from the wardrobe map, never the sheet's; face-and-hair crops when the outfit differs (HT26, L21)**; Susan's face N to SC05-SH06, N-A from SC05-SH07 | board (To check) | ✓ |
| L-* / P-HOUSE | location | the eight plates | board (To check) | ✓ |
| VOICE-N, VOICE-C1, VOICE-C2, VOICE-C3, VOICE-C5, VOICE-C6 | voice | §24I film voice masters, one per speaking character | voice stage (next) | — |
| PROD-CLOSED, PROD-BALM, PROD-BRUSH | product | the advertiser's canonical three renders (never the two-unit render, never the ref sheet) | `product/` | ✓ supplied |
| PROD-PRIMER | product | `PRIMER.jpg` | `product/` | ✓ supplied |
| PROD-HAND-CARD | info | the closed violet stick at true size in a woman's hand — "like a fat marker pen, about as thick as a thumb" (sheet §9), palm over the wordmark | info card | at SC05 |
| COLOUR-FRONT-CARD | info | the colour front: white balm stripe ahead of the brush crown, matched to her skin behind it, every line unchanged (sheet §6, `TERRAIN_LOCK`) | info card | at SC05 |
| CAKE-CARD | info | the plain white sheet cake on its board, frosting blank — one layout card every yard shot copies (HT23) | info card | at SC01 |
| INVITE-CARD | info | a plain cream party invite card, no lettering | info card | at SC04 |
| OLD-FOUNDATION-CARD | info | a plain unlabelled beige foundation bottle and sponge — no brand (§10) | info card | at SC04 |
| HERO-CARD | info | two closed sticks + the primer on pale stone, wordmarks to camera | info card | at SC09 |

## Flags added at steps 4–5

| # | Where | Finding | Recommendation |
|---|---|---|---|
| **F16** | geography | the party yard read as the hosts' house (she drives there; she goes inside to their back hall) | confirm, or say if it's Susan and Greg's own yard (then SC07's car shot becomes her own driveway) |
| F17 | L-PORCH-IN v1 | through the glass it shows a house, not the yard | **you confirmed v1** — kept. (A v2 I started before reading your Confirm is kept off the board.) |
| F18 | runtime | the planned shot lengths add to ~3:51 (script ~2:50); the voice masters will set the real timing | film pace, no trimming (§24L) |
| F19 | takes.py | six "length" splits flagged by a shots-only count; each pair is 17–24 s, over the 15 s take limit | splits kept; noted for the owner |

## Next

The voices (§24I film voice masters — Susan, Greg, Paula, Beth, Friend A, Friend B), runs straight through in Manual, every render on the board. Then scene by scene: each scene's info cards and take cards on the board as `planned` when the scene starts (L31), the takes after their ingredients are confirmed. **Before the voice stage I need your ruling on F6 (the niacinamide / "settles into the lines" wording) — the voice is the script verbatim.**
