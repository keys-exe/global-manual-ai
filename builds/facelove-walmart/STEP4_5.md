# Steps 4–5 — facelove-walmart (Mode 5 Pixar Film, Manual)

Built 2026-10-03 on the user's "CONFIRM AND PROCEED" (all five cast sheets confirmed). Flags F1–F17 run on my recommendations until you say otherwise.

## 4. Property and location maps (§30G, §30C)

### Story geography

- **Michelle's house** is a 1990s single-storey stucco ranch house in a Phoenix suburb — the same house for thirty years: the living room (the divorce), the bedroom vanity (the undoing, nothing worked, the change), the entry hall (the sister, the reveal), the back patio (the photos, the text, the close). One property plate (P-HOUSE, the hall) carries the finishes into every room.
- **The store** is a generic big-box superstore — blue and white, no name, no logo anywhere (§10A): one aisle seen both ways (L-AISLE, L-AISLE-REV) for the hook and the payoff, and the front doors for the exit.

### Location Sheets

| ID | Plate | Scenes | Landmarks (set map, step5/sets.json) | Light |
|---|---|---|---|---|
| L-AISLE | L-AISLE + L-AISLE-REV | SC01, SC09 | **end-cap** — the tall end-cap of plain blue boxes at the aisle's far corner — frame right from inside the aisle, frame left from the walkway; **paper shelves** — the shelves of paper towels and toilet paper — frame left from inside the aisle; **detergent shelves** — the shelves of orange, blue and green detergent bottles — frame right from inside the aisle; **walkway** — the wide main walkway crossing the aisle's far end | overhead store panels, cool white 4500K |
| L-LIVING | L-LIVING | SC02 | **armchair** — the dusty-rose wingback armchair, front left by the lamp; **lamp** — the pleated table lamp on the side table beside the armchair; **coffee table** — the low walnut coffee table, middle of the room; **sofa** — the oatmeal three-seat sofa along the right wall; **archway** — the rounded archway to the hall, back centre | table lamp, amber 2700K, dusk dying to dark |
| L-VANITY | L-VANITY | SC03, SC04, SC07 | **vanity** — the white vanity table with the oval mirror on its stand, against the far wall right of centre; **stool** — the small lilac stool in front of the vanity; **window** — the window with sheer white curtains, frame right beside the vanity; **bed** — the cream bed, frame left; **door** — the bedroom door, back wall left of centre | vanity bulbs at night 3500K (SC03) · cool morning 6000K (SC04) · golden morning 4300K (SC07) |
| L-HALL | P-HOUSE | SC05, SC06 | **front door** — the white front door at the end of the hall, the frosted sidelight on its left; **mirror** — the round brass-framed mirror over the console, left wall; **console** — the narrow dark-wood console table on the left wall; **archway** — the rounded archway to the living room, right wall; **pendant** — the globe pendant light hanging in the middle of the hall | globe pendant at night, 2900K |
| L-STORE-DOORS | L-STORE-DOORS | SC10 | **sliding doors** — the open automatic sliding doors, straight ahead; **carts** — the row of nested carts along the right wall; **mat** — the blue mat between the doors; **parking lot** — the golden parking lot and palms beyond the doors | low golden sun through the doors, 3800K |
| L-PATIO | L-PATIO | SC08, SC11, SC12 | **table** — the round wrought-iron mosaic table, middle; **bougainvillea** — the magenta bougainvillea on the right of the garden wall; **lemon tree** — the potted lemon tree and agave, frame left; **garden wall** — the sand stucco garden wall at the back | morning sun 4300K (SC08) · late sun 3800K (SC11–SC12) |

**Set checks:** every location plated (7 plates, all on the board To check) · light by time of day, one white balance per source per scene · the store never named in a picture.

### Product info cards (Seedance ingredients — information, never frames)

| Card | Fact |
|---|---|
| PROD-HAND-CARD | the closed violet stick in Rosa's hand — a little longer than her hand is wide, held low, wordmark clear, photoreal in the animated world (PIX-SPLIT) |
| COLOUR-FRONT-CARD | the colour front on Michelle's cheek: white ahead of the brush, her own shade behind, every line exactly as deep (TERRAIN_LOCK) |
| PROD-CLOSED / PROD-BALM / PROD-BRUSH | your three product photos, attached as they are |

## 5. Act map, takes, wardrobe, music

### Story spine (§24I part 9)

want — to stop disappearing · stakes — being seen by the man who left, and by herself · obstacle — the mirror · failed fix — every cream on the shelf · turn — Rosa: "It was never your age… It was the foundation." (SC05) and the stick (SC06) · payoff — the stare, the question, her silent smile (SC09) · plants → payoffs: the cart (SC01 → SC09), the mirror (SC03 → SC06/SC07), "a few weeks ago" (L004 → SC05), the photos (SC03 → SC08), the phone (SC11).

### Act map (E4) — 71 shots in 16 Seedance takes · ~4:22

Full rows (angle, library shot, move, focus, light, marks, motion, positions, ingredients): `step5/act_map.json` (built by `step5/act_map.py`). **Checks:** `takes.py` **PASS** · `blocking.py --sets` **PASS** · `angles.py` **PASS** (angles, shots, moves, focus, light) · `wardrobe.py` **PASS** · `visual_plan.py` **PASS**. Durations are planned; at the voice stage `takes.py --vo` measures every take from the narration master and rewrites them.

| Beat | Take | Act | Loc · day | Shot | Setup | Move | s | Words (dialogue / VO) | Action |
|---|---|---|---|---|---|---|---|---|---|
| SC01-SH01 | SC01-T1 | Hook 1 | L-AISLE · P1 | SH-WIDE+SH-34 | eye/three-quarter/WIDE | F13 | 3 | 🎙 At sixty three, I ran into my ex-husband in Walmart. | Michelle pushes her cart briskly up the aisle toward the walkway, the camera backing away in front of her; Peter's cart swings round the end-cap into her path |
| SC01-SH02 | SC01-T1 | Hook 1 | L-AISLE · P1 | SH-MED+SH-LOW | low/profile/MEDIUM | F19 | 2 | 🎙 He was with her. | the two carts collide nose to nose with a jolt, both carts rocking back; both pairs of hands lurch on the handles |
| SC01-SH03 | SC01-T1 | Hook 1 | L-AISLE · P1 | SH-34 | eye/three-quarter/MCU | F12 | 4 | 🎙 The woman he left me for. She is forty one. | Peter looks up annoyed, then his face changes completely — eyes widening, scanning her head to toe; behind him the woman stiffens |
| SC01-SH04a | SC01-T1 | Hook 1 | L-AISLE · P1 | SH-LOCU | low/three-quarter/CU | F1 | 3 | 🗣 Michelle? Is that you? My God, what happened, | Peter, staring, says it in one breath, his hand loose on the cart handle |
| SC01-SH04b | SC01-T1 | Hook 1 | L-AISLE · P1 | SH-34+SH-EYE | eye/three-quarter/MCU | F11 | 3 | 🗣 did you get work done? You look so much more beautiful. | Peter, staring, says it in one breath, his hand loose on the cart handle |
| SC01-SH05 | SC01-T1 | Hook 1 | L-AISLE · P1 | SH-CU+SH-34 | eye/three-quarter/CU | F2 | 3 | 🗣 It is just me. | Michelle holds his look for a beat, calm, cool, unbothered, and says it with one corner of her mouth lifting |
| SC01-SH06 | SC01-T1 | Hook 1 | L-AISLE · P1 | SH-REAR | eye/three-quarter-back/FULL | F14 | 4 | 🎙 The only reason I did not fall apart standing there | Michelle steers her cart around his and walks off along the walkway, unhurried, the camera following behind her |
| SC01-SH07 | SC01-T1 | Hook 1 | L-AISLE · P1 | SH-HIGH+SH-MED | high/front/MEDIUM | F6 | 5 | 🎙 is because of what my sister handed me a few weeks ago. | Peter stands frozen staring after her; the woman beside him turns from Michelle to Peter, stiffening |
| SC02-SH01 | SC02-T1 | Act 1 | L-LIVING · F1 | SH-WIDE+SH-34 | eye/three-quarter/WIDE | F18 | 4 | — | Peter, in his coat, stands by the coffee table and sets a plain manila envelope (a little larger than a sheet of paper) on it; Michelle sits in the armchair, very still |
| SC02-SH02 | SC02-T1 | Act 1 | L-LIVING · F1 | SH-HICU | high/front/CU | F12 | 2 | — | the plain manila envelope (a little larger than a sheet of paper) lies on the coffee table; Peter's fingers slide off it |
| SC02-SH03a | SC02-T1 | Act 1 | L-LIVING · F1 | SH-34 | eye/three-quarter/MCU | F11 | 3 | 🗣 I am sorry, Michelle. After thirty one years. | Peter says it to the floor, never meeting her eyes, then half turns toward the archway |
| SC02-SH03b | SC02-T1 | Act 1 | L-LIVING · F1 | SH-PROFILE+SH-MED | eye/profile/MEDIUM | F22 | 3 | 🗣 I just... I need something different. | Peter says it to the floor, never meeting her eyes, then half turns toward the archway |
| SC02-SH04 | SC02-T1 | Act 1 | L-LIVING · F1 | SH-CU+SH-EYE | eye/three-quarter/CU | F1 | 4 | 🗣 Thirty one years. | Michelle, very still in the armchair, eyes on the envelope, whispers it barely aloud |
| SC02-SH05 | SC02-T1 | Act 1 | L-LIVING · F1 | SH-OTS | eye/ots/FULL | F2 | 4 | — | over Michelle's shoulder, Peter walks away through the archway and out of sight; the front door closes beyond |
| SC02-SH06 | SC02-T1 | Act 1 | L-LIVING · F1 | SH-WIDE+SH-HIGH | high/three-quarter/WIDE | F16 | 4 | — | Michelle alone in the armchair as the light dies, the envelope on the table in front of her |
| SC03-SH01 | SC03-T1 | Act 2 | L-VANITY · F2 | SH-REAR+SH-MED | eye/behind/MEDIUM | F18 | 4 | — | Michelle sits on the stool at the vanity in her robe, looking at her reflection in the oval mirror |
| SC03-SH02a | SC03-T1 | Act 2 | L-VANITY · F2 | SH-CU+SH-34 | eye/three-quarter/CU | F1 | 4 | 🗣 When did I start looking like this? Tired. Worn out. | Michelle, hollow, says it to her reflection, touching the shadow under one eye with a fingertip |
| SC03-SH02b | SC03-T1 | Act 2 | L-VANITY · F2 | SH-EYE | eye/front/MCU | F12 | 4 | 🗣 Older than I am. No wonder he stopped looking at me. | Michelle, hollow, says it to her reflection, touching the shadow under one eye with a fingertip |
| SC03-SH03 | SC03-T1 | Act 2 | L-VANITY · F2 | SH-HICU | high/three-quarter/CU | F12 | 4 | 🎙 I stopped looking in mirrors. I stopped being in photos. | her hand lays a small framed photograph (the size of a paperback) face down on the vanity |
| SC03-SH04 | SC03-T1 | Act 2 | L-VANITY · F2 | SH-PROFILE+SH-LOW | low/profile/MCU | F15 | 5 | 🎙 And I buried my face under more and more makeup that only made it worse. | in profile, Michelle pats thick beige foundation from an unlabelled bottle over her cheeks with her fingers, layer on layer |
| SC03-SH05 | SC03-T1 | Act 2 | L-VANITY · F2 | SH-OTS | eye/ots/MEDIUM | F23 | 3 | — | over her shoulder, the mirror shows her face caked and grey; she looks away from it |
| SC04-SH01 | SC04-T1 | Act 3 | L-VANITY · F3 | SH-OVER | overhead/front/MEDIUM | F21 | 4 | 🗣 Every cream. Every serum. Every foundation on the shelf. | her hand moves across the crowded vanity top, touching one bottle after another |
| SC04-SH02 | SC04-T1 | Act 3 | L-VANITY · F3 | SH-34 | eye/three-quarter/MCU | F1 | 5 | 🗣 The Estée Lauder, the L'Oréal. And I look older in all of them. | Michelle, defeated, says it to the mirror, a jar in her hand |
| SC04-SH03a | SC04-T1 | Act 3 | L-VANITY · F3 | SH-HIGH+SH-REAR | high/three-quarter-back/FULL | F6 | 3 | 🎙 I decided this was just what sixty looked like, | Michelle sweeps the bottles into the vanity drawer, shuts it, and sits back on the stool, small in the cool room |
| SC04-SH03b | SC04-T1 | Act 3 | L-VANITY · F3 | SH-WIDE+SH-HIGH | high/three-quarter-back/WIDE | F8 | 3 | 🎙 and I made my peace with disappearing. | Michelle sweeps the bottles into the vanity drawer, shuts it, and sits back on the stool, small in the cool room |
| SC05-SH01 | SC05-T1 | Act 4 | L-HALL · F4 | SH-WIDE+SH-REAR | eye/three-quarter-back/WIDE | F14 | 4 | 🗣 Michelle, open the door. I brought wine and I am not leaving. | Michelle shuffles down the hall to the front door as Rosa's voice calls through it; she opens the door |
| SC05-SH02 | SC05-T1 | Act 4 | L-HALL · F4 | SH-OTS+SH-MED | eye/ots/MEDIUM | F17 | 4 | 🗣 ...Oh, honey. Look at you. Come here. | Rosa in the doorway holds up the bottle of red wine (held by its neck), sees Michelle's face, and her grin softens |
| SC05-SH03 | SC05-T1 | Act 4 | L-HALL · F4 | SH-34 | eye/three-quarter/MCU | F11 | 3 | — | Rosa steps in and takes Michelle's chin in her hand, tilting her tired face up to the hall light |
| SC05-SH04a | SC05-T1 | Act 4 | L-HALL · F4 | SH-LOCU | low/three-quarter/CU | F18 | 2 | 🗣 I am fine, Rosa. I am. | Michelle says it, eyes sliding away from Rosa's, toward the round mirror on the wall |
| SC05-SH04b | SC05-T1 | Act 4 | L-HALL · F4 | SH-PROFILE | eye/profile/MCU | F12 | 4 | 🗣 I just... I do not know who that woman in the mirror is anymore. | Michelle says it, eyes sliding away from Rosa's, toward the round mirror on the wall |
| SC05-SH05 | SC05-T1 | Act 4 | L-HALL · F4 | SH-PROFILE+SH-MED | eye/profile/MEDIUM | F7 | 5 | 🗣 He looked at me like a stranger the day he left, and lately so do I. | Michelle turns to the round mirror over the console and looks at herself as she says it; Rosa behind her |
| SC05-SH06 | SC05-T1 | Act 4 | L-HALL · F4 | SH-34 | eye/three-quarter/MCU | F2 | 3 | — | Rosa listens, her eyes wet, nodding once, and sets the wine on the console |
| SC05-SH07a | SC05-T2 | Act 4 | L-HALL · F4 | SH-OTS+SH-MED | eye/ots/MEDIUM | F2 | 2 | 🗣 Can I tell you something? | Rosa turns Michelle gently by the shoulders to face her and speaks low |
| SC05-SH07b | SC05-T2 | Act 4 | L-HALL · F4 | SH-34 | eye/three-quarter/MCU | F11 | 4 | 🗣 Two years ago, I felt exactly like that. Same mirror, same thoughts. | Rosa turns Michelle gently by the shoulders to face her and speaks low |
| SC05-SH08 | SC05-T2 | Act 4 | L-HALL · F4 | SH-HICU | high/three-quarter/CU | F18 | 3 | — | Michelle listens, her eyes lifting to Rosa's |
| SC05-SH09a | SC05-T2 | Act 4 | L-HALL · F4 | SH-34+SH-EYE | eye/three-quarter/MCU | F18 | 3 | 🗣 And I will tell you what I had to learn the hard way. | Rosa says it slowly, certain, holding Michelle's eyes |
| SC05-SH09b | SC05-T2 | Act 4 | L-HALL · F4 | SH-LOCU | low/three-quarter/CU | F1 | 4 | 🗣 It was never your age, Michelle. It was the foundation. | Rosa says it slowly, certain, holding Michelle's eyes |
| SC05-SH10 | SC05-T2 | Act 4 | L-HALL · F4 | SH-PROFILE+SH-MED | eye/profile/MEDIUM | F9 | 5 | 🗣 Made for young skin, so on ours it just sits on top and ages us. | Rosa taps her own cheek with two fingers as she says it; Michelle touches her own |
| SC06-SH01 | SC06-T1 | Act 5 | L-HALL · F4 | SH-MED+SH-34 | eye/three-quarter/MEDIUM | F4 | 4 | 🗣 This is the one that changed it for me. | Rosa reaches into her big woven shoulder bag and draws out the FACELOVE stick (a little longer than her hand is wide) |
| SC06-SH02 | SC06-T1 | Act 5 | L-HALL · F4 | SH-CU+SH-EYE | eye/front/CU | F20 | 3 | 🗣 Here, let me just show you. | Rosa's hand holds the closed violet FACELOVE stick (a little longer than her hand is wide) upright in the warm light, wordmark to the lens |
| SC06-SH03 | SC06-T1 | Act 5 | L-HALL · F4 | SH-OTS | eye/ots/MCU | F18 | 4 | 🗣 It comes out pure white. | Rosa uncaps the balm end and draws one short stripe of white balm across Michelle's cheekbone |
| SC06-SH04a | SC06-T1 | Act 5 | L-HALL · F4 | SH-34 | eye/three-quarter/MCU | F11 | 3 | 🗣 Then it reads the warmth of your own skin | Rosa turns the stick to its brush end as she speaks, her eyes crinkling at the corners |
| SC06-SH04b | SC06-T1 | Act 5 | L-HALL · F4 | SH-OTS+SH-CU | eye/ots/CU | F18 | 3 | 🗣 and turns into your exact shade, and it melts right in. | Rosa turns the stick to its brush end as she speaks, her eyes crinkling at the corners |
| SC06-SH05 | SC06-T2 | Act 5 | L-HALL · F4 | SH-MACRO | eye/profile/ECU | F2 | 12 | 🗣 It has jojoba, shea, vitamin E, so it feels like nothing and never cakes. It covers the lines, the tired, the circles, and it still looks like your own skin. | the brush end works the white stripe on Michelle's cheekbone in small circles; behind the brush the white warms into her own olive shade, ahead of it still white; every line stays |
| SC06-SH06 | SC06-T3 | Act 5 | L-HALL · F4 | SH-34 | eye/three-quarter/MCU | F15 | 4 | 🗣 Not a mask. You. | Rosa steps aside; Michelle turns to the round mirror and sees her even, warm face, every line still there |
| SC06-SH07 | SC06-T3 | Act 5 | L-HALL · F4 | SH-LOCU | low/front/CU | F1 | 3 | — | in the mirror Michelle's eyes fill and the corners of her mouth lift a little at herself |
| SC07-SH01 | SC07-T1 | Act 6 | L-VANITY · A1 | SH-REAR | eye/three-quarter-back/FULL | F14 | 4 | 🎙 I ordered my own before Rosa even left. And the first morning I tried it, | Michelle walks to the vanity in her robe and sits on the stool, her own violet stick (a little longer than her hand is wide) on the vanity |
| SC07-SH02 | SC07-T1 | Act 6 | L-VANITY · A1 | SH-HICU | high/three-quarter/CU | F18 | 3 | 🎙 the tired just lifted. | her hand draws the stick (a little longer than her hand is wide) across her cheek, white going on |
| SC07-SH03a | SC07-T1 | Act 6 | L-VANITY · A1 | SH-EYE | eye/front/MCU | F1 | 3 | 🎙 For the first time in years, | in the mirror Michelle meets her own eyes and holds them, her chin lifting a little |
| SC07-SH03b | SC07-T1 | Act 6 | L-VANITY · A1 | SH-OTS+SH-MED | eye/ots/MEDIUM | F7 | 3 | 🎙 I did not look away from my own reflection. | in the mirror Michelle meets her own eyes and holds them, her chin lifting a little |
| SC08-SH01 | SC08-T1 | Act 7 | L-PATIO · A2 | SH-LOW | low/front/FULL | F16 | 4 | 🎙 And it was more than my face. I stood taller. | Michelle rises from the patio table and straightens, shoulders back; Rosa beside her laughing |
| SC08-SH02 | SC08-T1 | Act 7 | L-PATIO · A2 | SH-SELFIE | high/front/MCU | F23 | 4 | 🎙 I got back in the photos. I stopped hiding. | Rosa holds her phone (a little smaller than her hand) up at arm's length; the sisters press cheek to cheek and laugh for the picture |
| SC08-SH03 | SC08-T1 | Act 7 | L-PATIO · A2 | SH-CU+SH-34 | eye/three-quarter/CU | F18 | 5 | 🎙 So by the time that cart hit mine in Walmart, I was not afraid of anyone. | Michelle lowers her face from the laugh, calm and sure, looking off past the lens |
| SC09-SH01 | SC09-T1 | Act 8 | L-AISLE · P1 | SH-MED+SH-PROFILE | eye/profile/MEDIUM | F11 | 3 | 🗣 Wait. That is your ex-wife? | the woman, unsettled, turns to Peter and asks; Peter still staring after Michelle |
| SC09-SH02a | SC09-T1 | Act 8 | L-AISLE · P1 | SH-34 | eye/three-quarter/FULL | F13 | 3 | 🗣 I am sorry, I just have to ask. | the woman hurries along the walkway after Michelle, catching up to her cart, the camera backing away in front of her |
| SC09-SH02b | SC09-T1 | Act 8 | L-AISLE · P1 | SH-OTS | eye/ots/MCU | F2 | 3 | 🗣 What do you use on your skin? You look amazing. | the woman hurries along the walkway after Michelle, catching up to her cart, the camera backing away in front of her |
| SC09-SH03 | SC09-T1 | Act 8 | L-AISLE · P1 | SH-LOCU | low/three-quarter/CU | F2 | 4 | — | Michelle turns her head to the woman, her lips closed, the corners of her mouth curving up warm and serene, saying nothing |
| SC09-SH04 | SC09-T1 | Act 8 | L-AISLE · P1 | SH-REAR | eye/three-quarter-back/FULL | F14 | 4 | — | Michelle turns her cart and walks away down the walkway, unhurried; the woman stops, left behind |
| SC09-SH05 | SC09-T1 | Act 8 | L-AISLE · P1 | SH-WIDE+SH-HIGH | high/front/WIDE | F6 | 3 | — | Peter stands alone at the end-cap behind his cart, small in the bright aisle, his hand slipping off the handle |
| SC10-SH01 | SC10-T1 | Act 9 | L-STORE-DOORS · P1 | SH-WIDE+SH-REAR | eye/behind/WIDE | F2 | 3 | 🎙 I did not need to say a thing. | Michelle walks her cart (a full-size store shopping cart, waist-high, holding a few household things) out through the open sliding doors into golden light |
| SC10-SH02 | SC10-T1 | Act 9 | L-STORE-DOORS · P1 | SH-LOW+SH-REAR | low/three-quarter-back/FULL | F12 | 3 | 🎙 I did not look back either. | Michelle passes through the outer doors into the sunlit parking lot without looking back |
| SC11-SH01 | SC11-T1 | Act 10 | L-PATIO · P2 | SH-MED+SH-34 | eye/three-quarter/MEDIUM | F7 | 4 | 🎙 Two weeks later, Peter texted me. First time in four years. | Michelle sits at the patio table with a cup of coffee; her phone (a little smaller than her hand) lights up on the table |
| SC11-SH02 | SC11-T1 | Act 10 | L-PATIO · P2 | SH-OVER | overhead/front/CU | F12 | 3 | 🎙 I read it, I smiled, | the phone (a little smaller than her hand) on the mosaic table lights up with a message; her hand picks it up |
| SC11-SH03 | SC11-T1 | Act 10 | L-PATIO · P2 | SH-LOCU | low/three-quarter/CU | F18 | 4 | 🎙 and I put my phone away. | Michelle's mouth curves up at one corner as she sets the phone (a little smaller than her hand) face down on the table, then lifts her coffee |
| SC12-SH01a | SC12-T1 | Act 11 | L-PATIO · P2 | SH-34 | eye/three-quarter/MCU | F1 | 4 | 🗣 So if someone ever looked at you and made you feel like you had faded, | Michelle, at the patio table in the late sun, turns from the garden to the lens and speaks to it, warm and direct |
| SC12-SH01b | SC12-T1 | Act 11 | L-PATIO · P2 | SH-CU+SH-EYE | eye/front/CU | F18 | 3 | 🗣 please hear me. It was never you. | Michelle, at the patio table in the late sun, turns from the garden to the lens and speaks to it, warm and direct |
| SC12-SH02a | SC12-T1 | Act 11 | L-PATIO · P2 | SH-MED+SH-LOW | low/front/MEDIUM | F11 | 4 | 🗣 The thing she wanted to know, I will tell you instead. | Michelle picks up the violet stick (a little longer than her hand is wide) and holds it up beside her face, wordmark to the lens |
| SC12-SH02b | SC12-T1 | Act 11 | L-PATIO · P2 | SH-34 | low/three-quarter/MCU | F4 | 3 | 🗣 It is called FACELOVE, and I have linked it below. | Michelle picks up the violet stick (a little longer than her hand is wide) and holds it up beside her face, wordmark to the lens |
| SC12-SH03a | SC12-T1 | Act 11 | L-PATIO · P2 | SH-LOCU | low/three-quarter/CU | F18 | 4 | 🎙 Right now you get two Foundation Sticks for almost the price of one, plus a free primer, a mystery gift, | Michelle lowers the stick and looks out at the garden, her face easy and open, the late sun on her cheek |
| SC12-SH03b | SC12-T1 | Act 11 | L-PATIO · P2 | SH-MED+SH-REAR | eye/three-quarter-back/MEDIUM | F13 | 4 | 🎙 and free shipping and a full thirty day money back guarantee. | Michelle lowers the stick and looks out at the garden, her face easy and open, the late sun on her cheek |
| SC12-SH04 | SC12-T2 | Act 11 | L-PATIO · P2 | SH-CU+SH-EYE | eye/front/CU | F2 | 5 | 🎙 Go be too busy glowing to look backward. | the FACELOVE stick (a little longer than her hand is wide) stands upright on the mosaic table in the late sun and turns slowly a quarter turn to bring the wordmark to the lens |

**Hook 1 = SC01** (the cold open) · Act 1 = SC02 … Act 11 = SC12. The colour-change shot SC06-SH05 is one unbroken 12 s take by the brief (`oner`); SC12-T2 (the stick turning) is a pinned Kling first-and-last-frame shot.

### Takes

One scene in one place is one take — one Seedance call up to 30 s (§24K part 5, V7.98.0), covered inside it in a new shot every 2–5 s (V7.99.0). 71 rows in 16 takes.

| Take | Kind | Rows | Length | Starts | Ends | Split |
|---|---|---|---|---|---|---|
| SC01-T1 | multi · conversation | SC01-SH01, SC01-SH02, SC01-SH03, SC01-SH04a, SC01-SH04b, SC01-SH05, SC01-SH06, SC01-SH07 | 27.0s | Michelle mid-aisle by the paper shelves pushing her cart toward the walkway, facing camera; Peter and the woman unseen beyond the end-cap on the walkway, about to turn in | Peter frozen at the end-cap behind his cart, staring frame right; the woman at his shoulder looking at him; Michelle gone along the walkway |  |
| SC02-T1 | multi · conversation | SC02-SH01, SC02-SH02, SC02-SH03a, SC02-SH03b, SC02-SH04, SC02-SH05, SC02-SH06 | 24.0s | Michelle sitting very still in the dusty-rose armchair by the lamp, facing the coffee table; Peter standing beside the coffee table in his coat, the envelope in his hand, the archway behind him | Michelle alone, small in the armchair by the lamp, the envelope on the coffee table, the room dark around her |  |
| SC03-T1 | multi · conversation | SC03-SH01, SC03-SH02a, SC03-SH02b, SC03-SH03, SC03-SH04, SC03-SH05 | 24.0s | Michelle seated on the stool at the vanity, back to camera, her face in the oval mirror, the bulbs on above it | Michelle on the stool at the vanity, face heavy with foundation, looking down away from the mirror |  |
| SC04-T1 | multi · conversation | SC04-SH01, SC04-SH02, SC04-SH03a, SC04-SH03b | 15.0s | Michelle on the stool at the vanity in the morning, her hand over a crowd of a dozen unlabelled bottles and jars | Michelle sitting back on the stool, the vanity bare, the drawer shut, the room cool and quiet |  |
| SC05-T1 | multi · conversation | SC05-SH01, SC05-SH02, SC05-SH03, SC05-SH04a, SC05-SH04b, SC05-SH05, SC05-SH06 | 25.0s | Michelle at the archway in an old grey sweatshirt walking toward the front door, back to camera; Rosa unseen outside the front door, calling through it | Michelle at the round mirror over the console, Rosa just behind her under the pendant, the wine on the console |  |
| SC05-T2 | multi · conversation | SC05-SH07a, SC05-SH07b, SC05-SH08, SC05-SH09a, SC05-SH09b, SC05-SH10 | 21.0s | Michelle at the round mirror over the console, Rosa just behind her under the pendant, the wine on the console | Rosa and Michelle face to face under the pendant in profile, Rosa's bag on her shoulder | length |
| SC06-T1 | multi · conversation | SC06-SH01, SC06-SH02, SC06-SH03, SC06-SH04a, SC06-SH04b | 17.0s | Rosa and Michelle face to face under the pendant, Rosa's bag on her shoulder | Rosa and Michelle face to face under the pendant, the white stripe on Michelle's cheek, the brush end of the stick in Rosa's hand |  |
| SC06-T2 | one-take | SC06-SH05 | 12.0s | extreme close on Michelle's cheekbone in profile, a short stripe of white balm on it, the brush end of the stick just touching its left end | the stripe blended into her own shade, the brush lifting away, every line of her face still there | user |
| SC06-T3 | multi | SC06-SH06, SC06-SH07 | 7.0s | Michelle turning from Rosa to the round mirror over the console, Rosa stepping back under the pendant | Michelle at the round mirror, almost smiling at herself; Rosa behind her under the pendant | user |
| SC07-T1 | multi | SC07-SH01, SC07-SH02, SC07-SH03a, SC07-SH03b | 13.0s | Michelle at the bedroom door in a cream robe walking toward the vanity, back to camera, golden sun through the curtains | Michelle on the stool at the vanity, smiling at her reflection, the stick in her hand |  |
| SC08-T1 | multi | SC08-SH01, SC08-SH02, SC08-SH03 | 13.0s | Michelle and Rosa seated at the round patio table in the morning sun, Michelle by the lemon tree, Rosa by the bougainvillea | Michelle standing at the patio table, calm and sure, Rosa beside her |  |
| SC09-T1 | multi · conversation | SC09-SH01, SC09-SH02a, SC09-SH02b, SC09-SH03, SC09-SH04, SC09-SH05 | 20.0s | Peter frozen at the end-cap behind his cart staring frame right; the woman at his shoulder looking at him; Michelle beyond them on the walkway, walking away | Peter alone at the end-cap behind his cart, small; Michelle gone |  |
| SC10-T1 | multi | SC10-SH01, SC10-SH02 | 6.0s | Michelle on the blue mat pushing her cart toward the open sliding doors, back to camera, the golden parking lot beyond | Michelle out in the golden parking lot, small, walking away |  |
| SC11-T1 | multi | SC11-SH01, SC11-SH02, SC11-SH03 | 11.0s | Michelle seated at the round patio table by the lemon tree in a lilac shirt, coffee cup in hand, her phone face up on the table | Michelle at the patio table, the phone face down, coffee raised, at peace |  |
| SC12-T1 | multi · conversation | SC12-SH01a, SC12-SH01b, SC12-SH02a, SC12-SH02b, SC12-SH03a, SC12-SH03b | 22.0s | Michelle seated at the patio table by the lemon tree in the late sun, looking at the garden wall, her violet stick on the table | Michelle standing by the bougainvillea in the late sun, the stick in her hand |  |
| SC12-T2 | one-take | SC12-SH04 | 5.0s | the stick upright on the mosaic table, wordmark turned a quarter away from the lens | the stick upright, wordmark square to the lens | pinned |


### Wardrobe map (§21, per story day)

### Wardrobe map — per story day and event

One block per story day, in story order: the event, what makes it a day, each person's outfit, and the day's events with their beats. Never grouped by act (§21, V7.89.0).

### F1 — the evening Peter left — the envelope on the coffee table

*Why it is a day:* stated: 'After thirty one years… I need something different.' (four years earlier, L005)

| Who | Outfit |
|---|---|
| Michelle | the dusty-mauve knit cardigan over a grey T-shirt and charcoal pull-on trousers, grey felt slippers (her before sheet) |
| Peter | a tan zip-up car coat over his navy quarter-zip, tan chinos, brown boat shoes — dressed to leave |

| Event | Place | Beats |
|---|---|---|
| F1-E1 | L-LIVING · VISIBLE | SC02-SH01, SC02-SH02, SC02-SH03a, SC02-SH03b, SC02-SH04, SC02-SH05, SC02-SH06 |

### F2 — a night in the months after — the mirror, the photos, the layers of makeup

*Why it is a day:* stated: 'I stopped looking in mirrors… I stopped being in photos' (L008)

| Who | Outfit |
|---|---|
| Michelle | a faded grey cotton bathrobe tied over a pale nightgown, grey felt slippers |

| Event | Place | Beats |
|---|---|---|
| F2-E1 | L-VANITY · VISIBLE | SC03-SH01, SC03-SH02a, SC03-SH02b, SC03-SH03, SC03-SH04, SC03-SH05 |

### F3 — another morning — every cream, every serum, every foundation on the shelf

*Why it is a day:* contrast: 'I decided this was just what sixty looked like' (L010)

| Who | Outfit |
|---|---|
| Michelle | the dusty-mauve knit cardigan over a grey T-shirt and charcoal pull-on trousers (her before sheet) |

| Event | Place | Beats |
|---|---|---|
| F3-E1 | L-VANITY · VISIBLE | SC04-SH01, SC04-SH02, SC04-SH03a, SC04-SH03b |

### F4 — the night Rosa came — the door, the wine, the stick

*Why it is a day:* stated: 'what my sister handed me a few weeks ago' (L004)

| Who | Outfit |
|---|---|
| Michelle | an old oversized faded-grey sweatshirt over charcoal pull-on trousers, grey felt slippers, hair limp |
| Rosa | the marigold-orange wrap blouse and long ink-blue skirt, tan sandals (her sheet), her big woven shoulder bag |

| Event | Place | Beats |
|---|---|---|
| F4-E1 | L-HALL · VISIBLE | SC05-SH01, SC05-SH02, SC05-SH03, SC05-SH04a, SC05-SH04b, SC05-SH05, SC05-SH06, SC05-SH07a, SC05-SH07b, SC05-SH08, SC05-SH09a, SC05-SH09b, SC05-SH10, SC06-SH01, SC06-SH02, SC06-SH03, SC06-SH04a, SC06-SH04b, SC06-SH05, SC06-SH06, SC06-SH07 |

### A1 — the first morning she tried it

*Why it is a day:* stated: 'the first morning I tried it' (L016)

| Who | Outfit |
|---|---|
| Michelle | a soft cream cotton robe over a lilac nightdress, hair brushed |

| Event | Place | Beats |
|---|---|---|
| A1-E1 | L-VANITY · VISIBLE | SC07-SH01, SC07-SH02, SC07-SH03a, SC07-SH03b |

### A2 — the weeks after — back in the photos with Rosa on the patio

*Why it is a day:* stated: 'I got back in the photos. I stopped hiding.' (L017)

| Who | Outfit |
|---|---|
| Michelle | a soft lilac blouse, white cropped trousers, tan sandals |
| Rosa | a turquoise peasant blouse, a long white skirt, tan sandals |

| Event | Place | Beats |
|---|---|---|
| A2-E1 | L-PATIO · VISIBLE | SC08-SH01, SC08-SH02, SC08-SH03 |

### P1 — the Walmart day — the carts hit, the payoff, out through the doors

*Why it is a day:* stated: 'At sixty three, I ran into my ex-husband in Walmart' (L001)

| Who | Outfit |
|---|---|
| Michelle | the soft cream boat-neck fine-knit sweater, high-waisted camel wide-leg trousers, tan leather loafers (her after sheet) |
| Peter | the navy quarter-zip over a white collared shirt, tan chinos, brown boat shoes (his sheet) |
| the woman, 41 | the camel cropped blazer over a white ribbed tank, black flared leggings, white platform trainers (her sheet) |

| Event | Place | Beats |
|---|---|---|
| P1-E1 | L-AISLE · VISIBLE | SC01-SH01, SC01-SH02, SC01-SH03, SC01-SH04a, SC01-SH04b, SC01-SH05, SC01-SH06, SC01-SH07, SC09-SH01, SC09-SH02a, SC09-SH02b, SC09-SH03, SC09-SH04, SC09-SH05 |
| P1-E2 | L-STORE-DOORS · VISIBLE | SC10-SH01, SC10-SH02 |

### P2 — two weeks later — Peter's text on the patio, then the close

*Why it is a day:* stated: 'Two weeks later, Peter texted me.' (L020)

| Who | Outfit |
|---|---|
| Michelle | a soft lilac linen shirt, cream wide-leg trousers, tan sandals, hair sleek |

| Event | Place | Beats |
|---|---|---|
| P2-E1 | L-PATIO · VISIBLE | SC11-SH01, SC11-SH02, SC11-SH03, SC12-SH01a, SC12-SH01b, SC12-SH02a, SC12-SH02b, SC12-SH03a, SC12-SH03b |



### Music Register Map (§40A) — one music family for the film; music only in the edit (never in a Seedance clip)

**Product's first frame:** SC06-SH01 (Rosa draws the violet stick from her bag) — `product_at` = the start of SC06. Everything before it is **investigation** (suspense, curiosity — never sad, `NEG-SAD`); the music **changes on that frame** (±0.25 s, `MUS-TURN` starts there).

| Part | Scenes | Lines | Register | What it sounds like |
|---|---|---|---|---|
| Hook — cold open | SC01 (the carts, the stare, "It is just me.") | L001–L004 | **MUS-OPEN** | a low pulsing drone and a soft ticking pulse under the crash; one muted piano note on the stare; unresolved, curious — the investigation starts here |
| Flashback — the wound | SC02 (the envelope, the door) | L005–L006 | **MUS-OPEN** (darker colour of it) | the same drone thinned to a single low string held under the room tone; silence on "Thirty one years." — tense, never mournful |
| The undoing, nothing worked | SC03, SC04 | L007–L010 | **MUS-EXPOSE** (inside the MUS-OPEN family) | the pulse returns slower, a sparse modal piano figure, questions not answers; no lament, no weeping strings |
| The sister | SC05 | L011–L013 | **MUS-EDU** | lighter, inquisitive: pizzicato over the drone, a little warmth when Rosa says "It was the foundation." — still unresolved |
| **The reveal (product's first frame)** | SC06 (from SH01) | L014–L015 | **MUS-TURN** | the change lands on the stick's first frame: the drone drops out, a warm sustained chord opens; under the colour-change oner one rising, resolving phrase |
| The change, back in the photos | SC07, SC08 | L016–L017 | **MUS-AFTER** | warm and hopeful — acoustic guitar and soft piano, light pulse, never cute or bouncy |
| The payoff, the doors, the text | SC09, SC10, SC11 | L018–L020 | **MUS-AFTER** (a quiet, knowing turn of it) | the payoff smile in near silence, the theme returning as she glides away; open and golden through the doors; a gentle resolve as the phone goes face down |
| CTA | SC12 | L021 | **MUS-OFFER** | confident, resolved, warm — the theme stated whole under the offer; a clean end on "look backward." |

**Banned everywhere it educates, warns or exposes (SC01–SC06):** generic cute, cheerful, upbeat, corporate or stock-advert music (`NEG-MUSIC`). **Supplied music:** none in the Drive folder → generated at step 8 (`music.py plan --register …` → `compose` → `check`, listened to by me, both run modes).


### Credit cap (§5B) — re-estimated from the act map


| Connector | Planned | Fix allowance | Cap | From |
|---|---|---|---|---|
| Higgsfield | 14,558 | 4,371 | **18,950** | estimate |
| ElevenLabs | 11,800 | 2,360 | **14,200** | estimate |

Credits are each connector's own — never added across connectors.

| Job | Connector | Model | Qty | Each | Credits | Price source |
|---|---|---|---|---|---|---|
| seedance | Higgsfield |  | 262 | 45 per second | 11,790 | unverified: Kie rate assumed |
| music | ElevenLabs |  | 11 | 1000 per track | 11,000 | unverified |
| seedance | Higgsfield |  | 60 | 45 per second | 2,700 | unverified: Kie rate assumed |
| sfx | ElevenLabs |  | 8 | 100 per sound | 800 | unverified |
| info_cards | Higgsfield | nano_banana_pro | 22 | 2 per image | 44 | measured: 2k image |
| plates | Higgsfield | nano_banana_pro | 7 | 2 per image | 14 | measured: 2k image |
| cast | Higgsfield | nano_banana_pro | 5 | 2 per image | 10 | measured: 2k image |


**Note:** the Seedance line is priced at the unverified Kie rate (45 cr/s). The last FACELOVE film measured **~8.2 Higgsfield credits a second** on Seedance 2.5 — at that rate the 16 takes (~262 s) + the voice masters (~60 s) come to **~2,650 credits**, ~3,450 with the Fix allowance. The private workspace holds **3,988**.
