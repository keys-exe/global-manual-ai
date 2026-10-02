# facelove-paint-wall — Steps 4–5 (Manual)

Built against the **confirmed avatars** (user, 2026-10-02 "CONFIRM AND PROCEED"): N-BEFORE v4 · N-AFTER v1. The step 1–3 flags were not answered, so they are held on my defaults: **3 hooks** (F3), the claims voiced as written (F8–F10), no earrings, the after look foundation-only (F12).

**On the board as To check:** 2 location plates (16:9) and 2 prop cards. The act map below is **planned**. No beat image is generated until the plates and prop cards are confirmed, and every B-roll `duration` stays `pending-master` until the voice master exists (E6).

---

## Step 4 — Property, locations and light (§30C, §30G, §30K)

### Location Derivation Pass

| ID | Location | Owner | Beats | Tier | Plate |
|---|---|---|---|---|---|
| **L-SHELF** | her dressing room facing the two shelves of ~40 collected, unlabelled foundation bottles — the main talking-head set (Scenes 1–3, 8–10) | N | TH-01–04, TH-08–12 (+ hooks), B01–B10, B18, B22–B27 | **PLATED** | L-SHELF |
| **L-WALL** | the same room turned round: the bare warm peach-beige plaster wall with fine hairline cracks, prepared for painting — the analogy set (Scenes 4–7) | N | TH-05–07, B11–B17, B19–B21 | **PLATED** (reverse of L-SHELF) | L-WALL |

One room, two plates (HT22): the window is on the **left** looking at the shelves and on the **right** looking at the wall.

### Property Sheet (§30G, fields 1–4) — PROP-H, her house

| Field | PROP-H |
|---|---|
| 1 Type and era | a modern single-storey house in a quiet American suburb |
| 2 Shell | smooth plaster in soft warm white · plain square white skirting · flat white casings · white flat-panel doors, slim brushed-brass levers · flat white ceiling, recessed downlights (off) · pale whitewashed oak floorboards · white rocker switches |
| 3 Floor map | the dressing room: the shelf wall opposite the bare wall, the tall window on the side wall between them, the door to the hall beside the shelves |
| 4 Orientation | the window faces south — bright, clean daylight all day |

### Light plans (§30K)

| Location | Source | Key (this build) | Kelvin |
|---|---|---|---|
| L-SHELF | tall window, sheer linen curtain, camera-left | bright midday (REC); flat grey morning for the PAST beats | 5600 / 6500 |
| L-WALL | the same window, camera-right | bright midday, raking the plaster (REC) | 5600 |

**Light arc (Mode 1, daylight, never moody):** a flat grey morning for the years of foundations, then bright, clean, high-key daylight for the demonstration and the result — the inspo's airy look in a real room.

### Plates and prop cards (on the board, To check)

Higgsfield `gpt_image_2_5` · `sunburst` · `high` · `2k` · ODAQ B.V. · empty, no people, no FACELOVE product, one render each. Prompts in `plates/<ID>.prompt.txt` (`plates/build_plates.py`, Appendix A by ID).

| ID | What | Size | Job |
|---|---|---|---|
| L-SHELF | the shelf wall of ~40 unlabelled foundation bottles, white dresser, window left | 16:9 | 5e50168c |
| L-WALL | the bare warm plaster wall with fine cracks, drop cloth, open paint can + tray + roller, window right | 16:9 | fadbbc44 |
| PROP-BOTTLE | the one ordinary foundation bottle she holds (square frosted glass, black pump, orange-beige, no label) | 9:16 | a7db8e98 |
| PROP-PAINT | the plain white paint can of flat pinkish-beige paint, the tray and the roller (no label) | 9:16 | 06e22e8a |

The prop cards keep the generic bottle and the paint kit identical in every beat (ED04 — nothing branded).

---

## Step 5 — Act map, wardrobe, Visual Pitch, music

### Act map (`step5/act_map.json`, 39 rows: 27 B-roll + 12 talking heads; hooks at step 6)

**Face arc (F13):** she is bare-faced (N-BEFORE) from the hook through the demonstration; the stick goes on in the Scene 7 hero macro (B21); from Scene 8 on she is finished (N-AFTER) — the proof on one face, in one sitting. The years-ago beats (B06–B10, B18) wear her old foundation. The wall/cheek intercut (ED02) is B17 (wall) → B18 (her cheek, framed the same, `mirror_of: B17`); B18's frame is made from B17's so the cracks and lines match. The Scene 7 macro (ED03) is one unbroken row, B21. B-roll is one picture per phrase, full screen.

| Beat | Act | Line (phrase) | Type | Day | Location | Picture (action) | Angle | Face |
|---|---|---|---|---|---|---|---|---|
| TH-01 | Act 1 | I am fifty seven. | TH | REC | L-SHELF | talking head to the lens (N-VOICE-SHELF-B) | tripod, eye level | N-BEFORE |
| B01 | Act 1 | And for years I felt like my own face | BR | REC | L-SHELF | she turns her head from the lens and runs her eyes slowly along the rows of unlabelled bottles, one hand resting on the white dresser | eye · three-quarter-back · MEDIUM | N-BEFORE |
| B02 | Act 1 | had quietly turned on me. | BR | REC | L-SHELF | she lifts a round hand mirror to her face and holds it still; in the glass, her bare tired face looks back | eye · ots · CU | N-BEFORE |
| B03 | Act 1 | The dull, tired skin. | BR | REC | L-SHELF | in the mirror, her bare cheek and eye: dull, sallow, matte skin; she blinks once, slowly | high · front · ECU | N-BEFORE |
| B04 | Act 1 | The deep lines. | BR | REC | L-SHELF | side-on, her outer eye and temple: the deep crow's feet hold their shadows as her eyes narrow a little, then relax | eye · profile · ECU | N-BEFORE |
| B05 | Act 1 | The dark circles that made me look worn out | BR | REC | L-SHELF | her eyes lift from the mirror to the lens; the dark circles under both eyes plain in the window light | low · three-quarter · CU | N-BEFORE |
| TH-02 | Act 1 | even on a good day. So I did what we all do. | TH | REC | L-SHELF | talking head to the lens (N-VOICE-SHELF-B) | tripod, eye level | N-BEFORE |
| B06 | Act 1 | I bought the next foundation, then the next, | BR | PAST | L-SHELF | her hand sets one more unlabelled bottle at the end of a row on the shelf, then a second beside it | eye · front · CU | N-BEFORE |
| B07 | Act 1 | then the two hundred dollar one, | BR | PAST | L-SHELF | her hands lift a heavy faceted glass bottle with a gold cap out of white tissue paper in a plain cream box | high · three-quarter · CU | N-BEFORE |
| B08 | Act 1 | always sure the next one would finally fix it. | BR | PAST | L-SHELF | at the hand mirror she dots the new foundation on her cheek with one fingertip and looks, hopeful | low · three-quarter · MCU | N-BEFORE |
| TH-03 | Act 1 | Every single one did the same thing. | TH | REC | L-SHELF | talking head to the lens (N-VOICE-SHELF-B) | tripod, eye level | N-BEFORE |
| B09 | Act 1 | It sat on top, sank into my lines, | BR | PAST | L-SHELF | macro of her outer eye and cheek: a flat beige foundation sits cakey on the skin and has settled into every crow's foot, each crease a darker line of product; she blinks once | eye · profile · ECU | N-BEFORE+OLD-FOUNDATION |
| B10 | Act 1 | oxidized, and left me looking more tired than my bare face. | BR | PAST | L-SHELF | in the hand mirror, her caked face: the foundation gone patchy and orange along the jaw against her paler neck; she lowers the mirror slowly | eye · ots · MCU | N-BEFORE+OLD-FOUNDATION |
| TH-04 | Act 1 | I was sure something was wrong with me. It took me years to find out the real reason. | TH | REC | L-SHELF | talking head to the lens (N-VOICE-SHELF-B) | tripod, eye level | N-BEFORE |
| B11 | Act 2 | Think of your skin like a wall | BR | REC | L-WALL | she steps once to stand beside the bare warm plaster wall, the beige foundation bottle in one hand, and lays her other palm flat on the wall | low · front · WIDE | N-BEFORE |
| TH-05 | Act 2 | you are trying to paint to look flawless. | TH | REC | L-WALL | talking head to the lens (N-VOICE-WALL-B) | tripod, eye level | N-BEFORE |
| B12 | Act 2 | Every foundation you have ever bought | BR | REC | L-WALL | she raises the beige foundation bottle to shoulder height beside the wall and holds it there, eyes on the lens | eye · three-quarter · MCU | N-BEFORE |
| B13 | Act 2 | works exactly like a pre-mixed can of paint from a factory, | BR | REC | L-WALL | top-down: the open paint can of flat pinkish-beige paint on the drop cloth; her hand sets the beige foundation bottle down right beside it | overhead · front · CU | — |
| TH-06 | Act 2 | in one fixed shade, before anyone ever saw your wall. | TH | REC | L-WALL | talking head to the lens (N-VOICE-WALL-B) | tripod, eye level | N-BEFORE |
| B14 | Act 2 | You bring it home, put it on, | BR | REC | L-WALL | she rolls the beige paint up the bare wall in one long, slow stroke | eye · three-quarter-back · MEDIUM | N-BEFORE |
| B15 | Act 2 | and it is never quite your color. | BR | REC | L-WALL | she steps back from the wall, roller lowered; the rolled stripe sits flat and pinkish against the warm plaster around it, plainly the wrong colour; she tilts her head | low · front · FULL | N-BEFORE |
| B16 | Act 2 | It sits there as an obvious coat. | BR | REC | L-WALL | macro on the edge of the rolled stripe: a flat ridge of beige paint sitting on top of the plaster, a hard edge against the bare wall | high · three-quarter · ECU | — |
| B17 | Act 2 | And on a wall with any texture or fine cracks, | BR | REC | L-WALL | macro, square on the plaster: the roller's beige coat slides over a patch of fine hairline cracks and sinks into them, each crack turning to a darker line | eye · front · ECU | — |
| B18 | Act 2 | like skin over fifty, it sinks straight into them and makes them worse. | BR | PAST | L-SHELF | macro, square on her cheek, framed exactly like the wall: a beige foundation sinks into her fine lines, each line turning to a darker line of product in the same pattern as the wall's cracks | eye · front · ECU | N-BEFORE+OLD-FOUNDATION |
| TH-07 | Act 3 | A can of paint can only ever be the one color it was mixed as. | TH | REC | L-WALL | talking head to the lens (N-VOICE-WALL-B) | tripod, eye level | N-BEFORE |
| B19 | Act 3 | This does the opposite. It does not come in a shade. | BR | REC | L-WALL | she sets the beige bottle down on the drop cloth by the paint can, straightens and holds the closed violet FACELOVE stick up beside her face, wordmark to the lens | eye · three-quarter · MCU | N-BEFORE |
| B20 | Act 3 | It comes out pure white. I know what you are thinking. Stay with me. | BR | REC | L-WALL | she draws the cap straight off the balm end and turns the white balm toward the lens, a knowing smile | low · three-quarter · CU | N-BEFORE |
| B21 | Act 3 | It reads the warmth of your own skin and becomes your exact shade, right there on your face. No shade to pick. No wrong match. It adapts as it goes on. | BR | REC | L-WALL | one continuous macro of her bare cheek: the balm's flat crest lays a white stripe, then the brush end sweeps through it in slow circles — ahead of the crown it is still white, behind it it is her own shade — until the cheek is one even tone, every line still there | eye · profile · ECU | N-BEFORE->N-AFTER |
| B22 | Act 4 | It covers the lines, the dark circles, the tired. | BR | REC | L-SHELF | she turns her finished face slowly from profile to the lens in the window light; the tone even, the dark circles gone, every line still there | eye · profile · MCU | N-AFTER |
| TH-08 | Act 4 | And it still looks like my own skin. Not a thick coat sitting on top. | TH | REC | L-SHELF | talking head to the lens (N-VOICE-SHELF-A) | tripod, eye level | N-AFTER |
| B23 | Act 4 | My skin, on its best day. Finally the right match, | BR | REC | L-SHELF | she holds the beige foundation bottle up beside her finished cheek and looks at the lens: the flat factory beige next to her even, matched skin | eye · front · CU | N-AFTER |
| B24 | Act 4 | instead of a guess from a factory. | BR | REC | L-SHELF | she sets the beige bottle back on the shelf among the forty others and lets go | high · three-quarter-back · MEDIUM | N-AFTER |
| TH-09 | Act 4 | It was never your skin, and it was never your age. It was a color that was never yours to begin with. And now that I know that, I am not going back. | TH | REC | L-SHELF | talking head to the lens (N-VOICE-SHELF-A) | tripod, eye level | N-AFTER |
| TH-10 | Act 5 | It is called FACELOVE, and I have linked it below. Right now you get | TH | REC | L-SHELF | talking head to the lens (N-VOICE-SHELF-A) | tripod, eye level | N-AFTER |
| B25 | Act 5 | two Foundation Sticks for almost the price of one, | BR | REC | L-SHELF | her hand sets a second closed FACELOVE stick upright beside the first on the white dresser top, both wordmarks to the lens | high · front · CU | — |
| B26 | Act 5 | plus a free primer, a mystery gift, | BR | REC | L-SHELF | her hand sets the primer and then the small mystery gift box beside the two sticks, the box lid ajar on a fold of white tissue | eye · three-quarter · CU | — |
| TH-11 | Act 5 | and free shipping and a full thirty day money back guarantee. | TH | REC | L-SHELF | talking head to the lens (N-VOICE-SHELF-A) | tripod, eye level | N-AFTER |
| B27 | Act 5 | Stop paying for a color that was never yours. | BR | REC | L-SHELF | the closed FACELOVE stick stands upright on the white dresser and turns slowly a quarter turn in the soft window light, the wordmark coming round to the lens | eye · front · CU | — |
| TH-12 | Act 5 | Get the one that becomes it. | TH | REC | L-SHELF | talking head to the lens (N-VOICE-SHELF-A) | tripod, eye level | N-AFTER |

`angles.py` **PASS** (11 setups, focus, light) · `wardrobe.py` **PASS** (2 story days) · `visual_plan.py` **PASS**.

### Wardrobe map — per story day and event (§21, V7.89)

One block per story day, in story order: the event, what makes it a day, each person's outfit, and the day's events with their beats. Never grouped by act (§21, V7.89.0).

### PAST — the years of trying foundations — mornings at her shelf

*Why it is a day:* stated: 'for years… I bought the next foundation, then the next, then the two hundred dollar one'

| Who | Outfit |
|---|---|
| the narrator | a soft heather-grey crew-neck sweater, hair pushed back behind the ears, bare face then the old beige foundation (N-BEFORE) |

| Event | Place | Beats |
|---|---|---|
| PAST-E1 | L-SHELF · VISIBLE | B06, B07, B08, B09, B10, B18 |

### REC — today — filming the demonstration in her dressing room

*Why it is a day:* stated: 'I can show you exactly why in about thirty seconds'

| Who | Outfit |
|---|---|
| the narrator | sheet outfit: the oatmeal linen blazer open over a white ribbed tank, cream wide-leg trousers, nude block-heel mules — bare face until the Scene 7 macro, the stick on after (N-BEFORE → N-AFTER) |

| Event | Place | Beats |
|---|---|---|
| REC-E1 | L-SHELF · VISIBLE | B01, B02, B03, B04, B05 |
| REC-E2 | L-WALL · VISIBLE | B11, B12, B13, B14, B15, B16, B17, B19, B20, B21 |
| REC-E3 | L-SHELF · VISIBLE | B22, B23, B24, B25, B26, B27 |

### Talking heads — per recording day

| Recording day | Who | Outfit | Beats |
|---|---|---|---|
| REC | the narrator | the oatmeal linen blazer over the white tank (one sitting: bare face at the shelf and the wall, the stick on from Scene 8) | TH-01, TH-02, TH-03, TH-04, TH-05, TH-06, TH-07, TH-08, TH-09, TH-10, TH-11, TH-12 |

### Visual Pitch (§30M) — `step5/visual_plan.md`

One hero per act: **B09** (foundation caked in her crow's feet) · **B11** (she lays her palm on the wall — the room becomes the analogy) · **B21** (white to her shade in one unbroken macro) · **B22** (she turns her finished face into the light) · **B27** (the stick turning alone in soft light). Swap any pick by its beat and letter.

### Music Register Map (§40A)

| Part | Lines | Register | Placement |
|---|---|---|---|
| Hooks + Act 1 (the first ~45 s) | L1–L3 | MUS-OPEN — investigative suspense, low pulse, sparse piano, unresolved | under everything, below the voice |
| Act 2 (the paint wall) | L4–L5 | MUS-EDU — inquisitive, light ticking, still unresolved | under everything |
| Act 3 (the opposite, the macro) | L6–L7 | MUS-TURN — starts on B19's first frame (the stick revealed, `product_at`) | the release |
| Act 4 (the result) | L8–L9 | MUS-AFTER — warm, hopeful, never cute | under everything |
| Act 5 (offer, CTA) | L10 | MUS-OFFER — confident, resolved | to the end |

**The inspo runs one continuous music bed (EG05)**, so this build carries one too: one music family, composed after the voice master with `music.py plan --register` → `compose` → `check` (I listen) and put on the board To check. Nothing cute, cheerful or sad before the stick is revealed (`NEG-MUSIC`, `NEG-SAD`). The hook shows the stick closed in her hand (VN01); the music turns on its reveal in B19 (F14).

### Ingredient / reference ledger

- Product: CLOSED, BALM END DEPLOYED, BRUSH END DEPLOYED (attachable); PACKAGING if a carton shows; PRIMER, MYSTERY GIFT (B26); FACELOVE_REF_SHEET_01 is never attached.
- Faces: N-BEFORE v4 / N-AFTER v1 by row `face_state` (the PAST beats N-BEFORE + the old foundation).
- Props: PROP-BOTTLE in B11–B13, B19, B23–B24; PROP-PAINT in B13–B17; plates by row.

### Next — the voice (§22U), straight through in Manual
Voice frames N-VOICE-SHELF-B (bare, at the shelf), N-VOICE-WALL-B (bare, at the wall), N-VOICE-SHELF-A (finished, at the shelf) → two or more Kling voice-source takes → trim, ×1.2, join, loop ≥ 30 s → ElevenLabs IVC clone → Enhance → `eleven_v4` VO (hooks + body in one request) → HeyGen Avatar V talking heads → `trim.py`. Then placement (`assemble.py --lengths --sheet`), and the hooks at step 6.
