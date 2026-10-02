# Build Sheet — stryde-the-impression

**STRYDE Precision Strap · "A - VID | AI Drama VSL | TOF | Discovery Story | New | The Impression"** · Standards V7.91.4 · **RUN: MANUAL · MODE 4 Realistic Film · AI Drama VSL · British** · 2026-10-02

Steps 1–3 of §18. **Stopped at the avatar review (§18B, V7.62.0)**: steps 4–5 wait for the user's go.
Boards: Current https://claude.ai/artifact/C7iJiu9zayETRq6wRpHERk · Old https://claude.ai/artifact/YHyjDG7UugdwLqpjL2Artq · Final https://claude.ai/artifact/7jESdNE8iA6sW9qtKVWMJr · Plan https://claude.ai/artifact/YR9p35toXVXK1EE1uPywym

---

## 0. Intake (§18B)

| Input | Found | Notes |
|---|---|---|
| Drive folder | `1myOChLFKSUBiQqn-Z5EoZ7ROwJ9sXeq2`. It matches no existing build, so this is a new build | fetched with `fetch_drive.py` → `intake/` |
| Inspo | `MY INSPO VIDEO (4).mp4` → `intake/inspo_sea_bass.mp4`. It is the Kivora "Sea Bass" AI Drama the script names as its format reference | 389.2s · 9:16 · 720×1280 · 24 fps · audio |
| Script | `SCRIPT.docx`, title on line 1 ✓ → `work/lines.json` (`work/parse_script.py`) | **1 hook (A) + 13 body blocks · 115 spoken lines · 911 words** · 3 parenthetical visual notes plus the STORY and VISUALS staging prose · 9 speakers |
| Product Sheet | `stryde_product_sheet_V7.49.32.py`, which is **older** than the repo's V7.49.38 | the repo's V7.49.38 is kept (`products/stryde/`) |
| Product images | 12, every one byte-identical to `products/stryde/stryde_refs/` | nothing new |
| Loom | none | — |

**Message fields:**
- "run manual" → **RUN: MANUAL**.
- "british" → **VOICE: British accents throughout** (the script's own casting line agrees). Every `VOICE-[CHAR]` is placed in West Yorkshire unless noted.
- MODE → **Mode 4 Realistic Film**. The message gives no mode; the script declares itself "An AI Drama VSL, photoreal, like a short film", which is the §2 / §3B explicit instruction. FORMAT → **AI Drama VSL** (§3B).
- HOOKS → **in script: 1 (A)** → **1 finished film** (F12).
- CAP → E0 default. DIRECTIONS → none.
- BUILD → `stryde-the-impression`.

**Account:** GitHub `mike-sj` (not the owner account). Build work stays in `builds/` only; no system change, no lesson (CLAUDE.md, §34B). Higgsfield: the one private workspace, 5,616.9 cr before (the ODAQ rule is for the owner's account only). Kie: 99,229.6 cr.

### Connector map (§5, `work/connectors.md`)

Every job has its default route except two, and neither needs anything connected:
- Talking heads → HeyGen API. This is a film with no talking heads, so the route is unused.
- SFX / voice isolation → the ElevenLabs API (rung 2).

Images go through Higgsfield (Sunburst), Seedance 2.5 through Kie (`kie.py`), and voice and music through the ElevenLabs API. There is no Drive connector, so there is no `OUTPUT/` tree (F16).

---

## 1. Absorption Sheet (§42)

### Part 1 — measured (`work/inspo_measure.json`, `work/inspo_transcript.json`)

| Instrument | Sea Bass inspo | Settles |
|---|---|---|
| Duration / aspect | 389.2s · 9:16 · 24 fps | 9:16 is locked; a 6–6½ min film is the format |
| Scene cuts | **156 shots, mean 2.5s.** Dialogue singles are 1–3s; establishing shots and silent beats (the lipstick developing, Paris) run 4–10s; the close is one held to-camera shot of 27s | dialogue cut on the line, singles and OTS; silent beats held |
| Silence (−40 dB) | none. At −30 dB only two gaps (145s, 214s) | a continuous sound bed; pauses live inside scenes |
| Words / pace | 1,067 words / 389s = **165 wpm** (dialogue + one inner VO + close) | our 911 words at 165 wpm ≈ **5:30 of speech + the silent beats ≈ 6:00–6:40** (F14) |
| Speech mix | almost all on-screen dialogue (≈ 90%); one inner-voice line ("Okay. One more time, Helen") over the test; **the lead to camera only in the close** (352–389s, on a high street, holding two tubes) | §3B: she looks at the lens only in Offer & Close (B13) |
| Captions (read off the frames) | **bold white UPPER-CASE sans with a thin black outline**, centred at ~78% height, 2–5 words, phrase by phrase, no box, no highlight | EG01 |
| Shot frames + per-second sheets | `intake/frames/inspo_sea_bass/` (13 sheets) | Edit Grammar below |

### Part 2 — structure map (Sea Bass → The Impression)

Our script is a story-for-story port of the inspo with the product swapped, and it maps scene for scene:

| t (inspo) | §3B act | Inspo shows | Our block |
|---|---|---|---|
| 0–18 | **Hook — cold open** | restaurant, candle-lit, the husband orders for her: "She'll have the sea bass." She pushes back; singles cross-cut, a wide two-shot over his shoulder | **HK-A1/A2** Sunday lunch: Oscar's impression, "Is that what I look like?", the promise "I'll walk him" |
| 18–43 | Before | the daughter at the kitchen table, daylight, a mug; "Dad says you've blown this out of all proportion" | **B01** the hall at night: "Film me." |
| 43–66 | Problem | a beauty counter: "something that isn't beige", the assistant offers nudes "for mature skin" | **B02** the chemist: "Have you thought about a stick?", the beige sleeve |
| 66–86 | Problem | the daughter finds the drawer: 43 lipsticks, "I counted them in March" | **B03** the drawer: 24 sleeves; the hill, the postbox, the mum with the buggy |
| 86–120 | Problem | a phone call from Paris; the husband at home under a lamp, "Did you notice I'd gone?" | **B04** the car: "It's what we can do." Roy down the stairs sideways (silent) |
| 120–146 | Turn | a Paris café: the waiter, "those women over there… every Thursday" | **B05** the school gate: the lollipop lady, "Wendy? Every day since Reception" |
| 146–193 | Turn — the mechanism | the stranger explains in dialogue: "it sits on the surface… paint always cracks"; "you've got 43 of something else" | **B06** Wendy: one spot, 2 cm under the kneecap, 17×; "twenty-four things that go round" |
| 193–214 | Turn — the decision | night, alone: "Is it expensive?" "25 pounds" | **B07** the price, the kitchen at night: "Thirty pounds. For two." "Get the two." |
| 214–228 | Turn — the test | bathroom mirror, inner voice "Okay. One more time, Helen", macro of the colour developing | **B08** the stairs: inner VO "One more time, Hazel", the hand comes off the rail |
| 228–275 | After — witnesses | the daughter: "Mum… that's beautiful", a stranger in a café: "What have you got on?" "It's called Kivora" | **B09** the hill (mum with buggy: "You got past the postbox") · **B10** the hall (Emma: "You look like you. Before.") |
| 275–312 | After — the husband | "You look lovely today." "Say it again." "Three years." "I stopped looking as well." | **B11** Roy: "Say it again." "You knew the day." "I'd stopped looking as well." |
| 312–350 | After — the loop paid | the drawer emptied; the daughter: "Can I have one?" B1G1 | **B12** the first day: "Oscar. Do the walk." "That's just walking, Nana." |
| 352–389 | **Offer & Close** | to camera on a London high street, product held up: "43 of them in a drawer… two tubes under 25 pounds, 90 days… Your turn." | **B13** Hazel to camera at the gate: "Twenty-four of them in a drawer… Two straps, under thirty pounds… Your turn." |

### Part 3 — Style Lock (copied)

- **Format:** AI Drama VSL, all dialogue, no narrator except one inner-voice line and the close to camera.
- **Visual grammar:**
  - restrained prestige-drama coverage in 9:16: tight singles (MCU/CU) for the arguments, OTS two-shots to place people, inserts for props;
  - faces off-lens until the close;
  - shallow depth from MCU in.
- **Light arc:**
  - Hook: warm tungsten interior.
  - Before/Problem: daylight kitchens, cool and overcast, and a lamp-lit night interior.
  - Turn: dusk.
  - After: bright, soft daylight.
  - Close: an outdoor overcast street, soft and even.
- **Rhythm:** a mean shot of 2.5s; dialogue cut line by line; silent beats held 4–10s; a new scene every 20–45s.
- **Tone of voice:** plain British, understated, dry, lines left hanging ("Before what?" "I don't know." "No. Neither did I.").

### Part 3A — Edit Grammar → `EDIT-IMPRESSION`

| ID | Device (inspo) | Where | Our build |
|---|---|---|---|
| EG01 | **phrase captions**: bold white upper-case sans, thin black outline, 2–5 words, centred at ~78% height, no box, no highlight | whole film | **kept** (CapCut) |
| EG02 | **full-frame shots only**: no split, no picture-in-picture, no cutouts | whole film | **kept** (every row `full`) |
| EG03 | **hard cuts** only; no transitions, ramps or punch-ins | whole film | kept; time jumps are carried by the dialogue, with no cards (the script has none) |
| EG04 | **macro insert** of the product working (the lips colouring over 15s) | 214–228 | kept as the strap going on bare skin under the kneecap (`HERO-FILM`), the one time the strap is seen in Hazel's story (VISUALS) |
| EG05 | **lead to the lens for the offer**, one long held shot, product in hand | 352–389 | kept as B13 at the school gate. **Without the product in hand** (the VISUALS: "nobody sees it for the rest of the ad"); see F15 |
| EG06 | a low music bed under the whole film, dipping under dialogue | whole film | music added in the edit (§24M, §40A), never generated in a clip |
| Light | tungsten → cool daylight → dusk → bright daylight | by act | the §30K light arc (Look Sheet field 3) |
| Focus | shallow from MCU in, deep on wides; no rack focus seen | — | §30J |
| Angles | eye-level singles, OTS pairs, a few high wides (the restaurant, Paris), the close frontal | — | the range is copied at step 5 (`angles.py`) |

### Part 4 — script absorption

**Story spine (§24I part 9), read from the script as written:**
- **Want:** walk Oscar up the hill to school on his first day.
- **Stakes:** her grandson copying her walk; the family planning around her.
- **Obstacle:** the walk, the hill and the postbox.
- **Failed fixes:** 24 sleeves, the stick, the car.
- **Turn:** Wendy at the gate.
- **Payoff:** "That's just walking, Nana."
- **Plants → payoffs:**
  - the impression → "Do the walk";
  - the postbox → "You got past the postbox";
  - the hall film → the second hall film side by side;
  - Roy sideways on the stairs → "There's one in your drawer";
  - "It goes round, it moves nothing".

**Voice fingerprint:** short declaratives; repetition as weight ("I said I'll walk him"); understatement ("I know what it is."); British domestic register (love, Mum, Nana, Reception, half seven, lollipop lady). Spoken verbatim (§22U); never changed.

### Part 5 — surfaced, not absorbed

| Inspo element | Disposition |
|---|---|
| Lipstick, macro on the lips | replaced by the strap: one insert going on bare skin (B08), Wendy's hem lifted (B06) |
| Paris (the escape) | not in our story; the hill is the world |
| The product held to camera in the close | not held (F15) |
| "Kivora" said by name in a witness scene | our B09 has "It's called Stryde. It's under my trousers." Voiced; the wordmark is never generated on screen |

### Part 6 — beat-it plan

| Inspo weakness | Our delta | Where |
|---|---|---|
| The mechanism is only talked about | Wendy lifts her hem to show it worn; the stairs scene shows it working, with the hand off the rail on the third step and the A/B test (off → hitch back, on → nothing in her hand) | B06, B08 |
| One hook | the script has one; more hooks can be written on request | F12 |
| 720p soft source, TV-flat restaurant | prestige-series package, `PROD-DEPTH` layers, motivated light (§24N) | every shot |
| The payoff is told | ours is shown: the same child repeats the walk, this time straight | HK-A1 ↔ B12 |

### Part 7 — confirmation

Conflicts are listed in **Flags**. **Confirm or correct the absorption along with the avatars.**

---

## 1b. Film Look Sheet (§24G) — written by the agent, shown for information

| # | Field | Value |
|---|---|---|
| 1 | Genre and reference | A British family drama shot like a prestige streaming series (§24N house base). It is set in a West Yorkshire hill town: a stone terraced house with a narrow hall and stairs, a high-street chemist, a steep residential hill with a red pillar box halfway up, and a primary-school gate at the top. Warm and restrained |
| 2 | Camera and glass | **ARRI Alexa 35 · Cooke S4/i primes (spherical) · ARRI colour science** · 24 fps, 180° shutter. Focal length by scale: WIDE 25–32 · FULL 32–40 · MED 40–50 · MCU 50–65 · CU 75 · INSERT 100 macro. Stop: T4–T5.6 on wides, T2 on CUs. Shallow from MCU in; one focus pull per clip at most, on a named cue (§30J) |
| 3 | Light | Motivated: a soft key from windows and practicals. **4:1 on faces in the Before/Problem, 2:1–3:1 in the After**, with practicals in frame. The arc: the Sunday lunch is overcast daylight (6500K) with one warm pendant (2800K); the hall at night is tungsten (3000K); the chemist is cool fluorescent mixed with daylight; the July hill is a flat overcast morning; the gate is late-afternoon sun (4800K). In the After: clear summer morning sun (5600K) on the hill and the stairs; the September first day is soft bright morning. The close is open shade at the gate |
| 4 | Palette | **Before:** gritstone grey, sage, navy, oatmeal, brick, with the beige of the sleeves. **After:** cream, soft green, honey. **Constant:** one pillar-box red on the hill in every hill scene. Hazel's wardrobe warms by story day (§14A at step 5) |
| 5 | Grade (the edit only) | warmth +0.015, contrast 1.08, saturation 0.95, a teal-blue shadow tint (210°, 0.035), an amber highlight tint (40°, 0.025), black lift 0.03, white point 0.97, skin protect 0.80 → `edit/grade.json` → **`edit/LUT-IMPRESSION.cube`, `lut.py check` PASS** (skin hue ≤ 3.0°, saturation −4…+5%) |
| 6 | Optical texture | soft highlight roll-off, a faint warm halation round bulbs and bright windows, clean glass with a gentle edge fall-off; no haze, no flare |
| 7 | Motion | the Seedance move library (§24N): F2 locked for dialogue; F1 a slow push on the turn lines ("Is that what I look like?", "You knew the day."); F9 a lateral track beside the walks on the hill (never on stairs); F6 a pull-back reveal at the gate; one move per shot. Connected action is one take (§24K part 5) |
| 8 | Performance | restrained (§28B); understatement. Hazel is never self-pitying. Roy says kind things too quickly. Emma covers with brightness. Oscar plays it straight (a child copying, not mocking). Wendy is certain and amused |
| 9 | Sound and post | Dialogue only in every clip (`NEG-SOUND`, no BGM, V7.73.3). A room tone per location. An SFX list: the cutlery at the lunch, the phone's record chime, the chemist's door, the drawer, the car door, the school bell, the lollipop sign. **Music (§40A):** `MUS-OPEN` investigative-curious for the hook and the problem, never sad; the change on the product's first frame (Wendy's hem, B06); warm in the After; resolved in the Offer. One family: sparse piano and low strings with a soft pulse. Grain is added in the edit (Mode 4) |

**`LOOK-IMPRESSION`** (verbatim on every Mode 4 frame — `cast/LOOK.txt`):
```
THE LOOK OF THIS FILM: A British family drama shot like a prestige streaming series — a stone terraced house on a steep Yorkshire hill, a Sunday lunch, a high-street chemist, a primary-school gate at the top of the hill, watched with warmth and restraint. Lived-in domestic colour: overcast grey-blue daylight and warm tungsten lamps in the rooms of the Before; muted sage, navy, oatmeal, gritstone and brick, one pillar-box red on the hill; warming to clear summer daylight, soft greens, cream and honey in the After. Highlights roll off softly with a faint warm halation around bulbs and bright windows; clean modern glass with a gentle fall-off toward the frame edges. Captured with natural, neutral colour and a gentle contrast, ungraded — the grade is added later in the edit. Every frame of this film shares exactly this look.
```

---

## 2. Script, product, claims, locks (step 2)

### Visual Instruction Ledger (§27F) — opened (every row → a beat at step 5)

The script's dialogue section has three parentheticals (VN01–VN03). Its STORY and VISUALS sections are, in its own words, "the staging", so every staging instruction in them is logged too (VN04–VN38).

| ID | Anchored to | Instruction (verbatim or as staged) | Status |
|---|---|---|---|
| VN01 | L001 | "Oscar crosses the room the way Nana does. Dan laughs first. Then Emma. Roy looks at his plate." | open → step 5 |
| VN02 | L002–L003 | "He does it again. Nobody laughs." | open |
| VN03 | L109–L110 | "He looks at her. He walks. Straight. He turns round." | open |
| VN04 | HK-A1 | "Sunday, the table cleared. Oscar slides off his chair and crosses the room the way Nana does: the hitch, a hand on every chair back, the shoulder dip." | open |
| VN05 | casting | Hazel 67: her face looks her age, but she **walks like a woman of 80**: a hitch on the bad knee, a hand on every chair back and wall, the shoulder dipping. **Do NOT age her face.** After the strap: the same woman, an ordinary walk | open (every Hazel walk row) |
| VN06 | casting | Roy "comes down the stairs sideways and thinks she hasn't noticed" | open (B04, B11) |
| VN07 | fixed point | "The same OSCAR in the hook and at the gate" | open |
| VN08 | fixed point | "the same hall for both films, framed the same" | open (B01 ↔ B10) |
| VN09 | fixed point | "the same hill and postbox in all three hill scenes" (July, August, September) | open (B03, B09, B12) |
| VN10 | casting | "A mum with a buggy, the same one in July and August" | open |
| VN11 | HK-A2 | "The look between Emma and Dan: Nana will wait in the car." | open |
| VN12 | B01 | "That night in the hall she hands Emma her phone: film me, kitchen to the door" | open |
| VN13 | B01 | "She watches it once." | open |
| VN14 | B02 | "She takes the same beige sleeve off the hook." | open |
| VN15 | B03 | "Emma finds the drawer" (24 beige sleeves) | open |
| VN16 | B03 | "They all go round." (the line; the sleeves shown going round, i.e. tubes) | open |
| VN17 | B03 | "July, 8:40, Hazel tries the hill alone with number twenty-four under her trousers. She gets to the postbox halfway up, hand on the wall." | open |
| VN18 | B03 | "A mum with a buggy asks if she's all right. She turns back." | open |
| VN19 | B04 | "Roy has spoken to Emma: they'll do it in the car" | open |
| VN20 | B04 | "Later, silent: Roy comes down the stairs for his glasses, sideways, one step at a time. Hazel watches from the kitchen door." | open |
| VN21 | B05 | "Last week of term, Hazel in Emma's car at pick-up." | open |
| VN22 | B05 | "A woman her age comes down the hill with two children and a book bag in each hand. No wall, no stick, no hitch." | open |
| VN23 | B06 | "Hazel gets out of the car and asks how she does the hill." | open |
| VN24 | B06 | "Wendy lifts her hem: a thin strap under the kneecap" (the product's first appearance, §3B) | open |
| VN25 | B07 | "Night, the kitchen, the phone. Roy comes down sideways." | open |
| VN26 | B08 | "Morning. The strap goes on bare skin, just under the kneecap, trousers over it." | open — **F11** |
| VN27 | B08 | "First step, hand on the rail, same as always. On the third step the hand comes off on its own." | open (FP23 `rail_ok` on steps 1–2 only: the script puts the hand there) |
| VN28 | B08 | "At the bottom she takes it off and goes back up: the hitch is back, the hand is back. She puts it on: down, nothing in her hand." | open |
| VN29 | B08 | "Roy in the kitchen doorway says nothing. She tells no one." | open |
| VN30 | B09 | "August, the hill, the postbox goes by." | open |
| VN31 | B10 | "End of August, the hall: Emma films again, two clips side by side, the hand on the wall and nothing." | open (the side-by-side is an edit device — CapCut, EG) |
| VN32 | B11 | "Early September, the hall." "She walks to the door and back." | open |
| VN33 | B11 | the day Roy names: "The March your knee went. The step outside the library. You grabbed the wall" | open (dialogue only; no flashback unless asked) |
| VN34 | B12 | "8:40, the hill, hand in hand, his pace, past the postbox, to the gate. Emma and Dan in the car behind, watching." | open |
| VN35 | B12 | "He runs in. She stands at the gate with nothing in her hands. In the car, Emma is filming." | open |
| VN36 | B13 | "Hazel to camera at the gate" | open |
| VN37 | VISUALS | "The strap is on bare skin under the kneecap, then under the trousers: nobody sees it for the rest of the ad." | open |
| VN38 | VISUALS | "Editor's call. The script below is dialogue only; the story above is the staging." | open |

### Phrase inventory (§27B) — dispositions: `SH` (spoken in a shot) · `VO` (inner voice over shots) · `TC` (to camera, close); beats assigned at step 5

| ID | Block | Speaker | Line (verbatim) | Disp |
|---|---|---|---|---|
| L001 | HK-A1 | Emma | Oscar. That’s enough. | SH |
| L002 | HK-A1 | Hazel | No. Let him. Do it again, Oscar. | SH |
| L003 | HK-A1 | Hazel | Is that what I look like? | SH |
| L004 | HK-A1 | Emma | He’s four, Mum. He doesn’t see it. | SH |
| L005 | HK-A1 | Hazel | Dan? | SH |
| L006 | HK-A1 | Dan | ...A bit. | SH |
| L007 | HK-A2 | Oscar | Nana. Will you walk me to school? When I’m big. | SH |
| L008 | HK-A2 | Emma | Nana’ll wait in the car, love. Nana’ll see you at the gate. | SH |
| L009 | HK-A2 | Hazel | I’ll walk him. | SH |
| L010 | HK-A2 | Emma | Mum. | SH |
| L011 | HK-A2 | Hazel | I said I’ll walk him. | SH |
| L012 | HK-A2 | Roy | Hazel. It’s a hill. | SH |
| L013 | HK-A2 | Hazel | I know what it is. | SH |
| L014 | B01 | Hazel | Film me. From the kitchen to the door. | SH |
| L015 | B01 | Emma | Why? | SH |
| L016 | B01 | Hazel | Because I’ve never seen it. | SH |
| L017 | B01 | Emma | It’s not that bad. | SH |
| L018 | B01 | Hazel | He got it exactly right, Emma. Down to the hand. | SH |
| L019 | B01 | Emma | You’re all right, Mum. | SH |
| L020 | B01 | Hazel | I’m not, though. Am I. | SH |
| L021 | B01 | Hazel | He’s four. This knee’s three. He has never once seen me walk. | SH |
| L022 | B02 | Assistant | Can I help at all? | SH |
| L023 | B02 | Hazel | Something for a hill. Ten minutes. With a four-year-old. | SH |
| L024 | B02 | Assistant | Lovely. Have you thought about a stick? Just for the school run. | SH |
| L025 | B02 | Hazel | A stick. | SH |
| L026 | B02 | Assistant | A lot of our customers find... | SH |
| L027 | B02 | Hazel | He’d copy the stick as well. | SH |
| L028 | B02 | Assistant | We do have that in a large. | SH |
| L029 | B02 | Hazel | I know. I’ve got twenty-three of them. | SH |
| L030 | B03 | Emma | Mum. What is all this? | SH |
| L031 | B03 | Hazel | Leave it. | SH |
| L032 | B03 | Emma | There must be twenty in here. | SH |
| L033 | B03 | Hazel | Twenty-four. As of Tuesday. | SH |
| L034 | B03 | Emma | You’ve counted them? | SH |
| L035 | B03 | Hazel | I counted them in March. Then I bought another one. | SH |
| L036 | B03 | Emma | Why? | SH |
| L037 | B03 | Hazel | Because the girl in the shop said it was supportive. They all say that. They all go round. And I still stop halfway up that hill. | SH |
| L038 | B03 | Mum With Buggy | You all right, love? | SH |
| L039 | B03 | Hazel | Fine. Just the knee. | SH |
| L040 | B04 | Roy | I’ve spoken to Emma. We’ll do it in the car. You walk him from the gate. It’s twenty yards. | SH |
| L041 | B04 | Hazel | Twenty yards. | SH |
| L042 | B04 | Roy | It’s the same thing, love. | SH |
| L043 | B04 | Hazel | It isn’t the same thing. | SH |
| L044 | B04 | Roy | It’s what we can do. | SH |
| L045 | B05 | Hazel | That woman. How long has she been doing that? | SH |
| L046 | B05 | Lollipop Lady | Wendy? Every day since Reception. Both of them. Rain or shine. | SH |
| L047 | B05 | Hazel | How old is she? | SH |
| L048 | B05 | Lollipop Lady | Seventy-four. Don’t tell her I told you. | SH |
| L049 | B06 | Hazel | Sorry. Can I ask you something ridiculous? How do you do that hill? | SH |
| L050 | B06 | Wendy | Which bit? | SH |
| L051 | B06 | Hazel | All of it. I get to the postbox. | SH |
| L052 | B06 | Wendy | What have you got on it? | SH |
| L053 | B06 | Hazel | A sleeve. | SH |
| L054 | B06 | Wendy | Mine were bone on bone. Both. They wanted to replace them at seventy-one. A sleeve goes round. That’s all it does. It doesn’t change where the weight lands. | SH |
| L055 | B06 | Hazel | Where does it land? | SH |
| L056 | B06 | Wendy | One spot. Two centimetres under the kneecap. Every step down that hill, seventeen times what you weigh goes through it. | SH |
| L057 | B06 | Hazel | Seventeen times. | SH |
| L058 | B06 | Wendy | That walk you do. I’ve watched you get out of that car. That’s your body keeping the weight off that spot. It’s doing the job. Badly. | SH |
| L059 | B06 | Hazel | Nobody’s ever put it like that. | SH |
| L060 | B06 | Wendy | This takes the weight before it gets there. So your body stops doing the walk. | SH |
| L061 | B06 | Hazel | That little thing? | SH |
| L062 | B06 | Wendy | That’s what I said. Three years with orthopaedic surgeons, for that little thing. | SH |
| L063 | B06 | Hazel | Straps slide down on me. Every one. | SH |
| L064 | B06 | Wendy | The Facebook copies slide. Those go round as well. This has a pad. It stays on the spot. And I’m not a small woman. | SH |
| L065 | B06 | Hazel | I’ve got twenty-four at home. | SH |
| L066 | B06 | Wendy | No. You’ve got twenty-four things that go round. It goes round, it moves nothing. | SH |
| L067 | B07 | Roy | What’s that? | SH |
| L068 | B07 | Hazel | Thirty pounds. For two. | SH |
| L069 | B07 | Roy | For what? | SH |
| L070 | B07 | Hazel | For the hill. | SH |
| L071 | B07 | Roy | Hazel. We’ve said the car. | SH |
| L072 | B07 | Hazel | If it works, I’ve spent three years saying no to him for nothing. | SH |
| L073 | B07 | Roy | And if it doesn’t? | SH |
| L074 | B07 | Hazel | Sixty days. They take it back. | SH |
| L075 | B07 | Roy | Get the two. | SH |
| L076 | B08 | Hazel | One more time, Hazel. | VO |
| L077 | B08 | Hazel | First step, hand on the rail. Same as always. Second step. On the third, my hand came off on its own. | VO |
| L078 | B09 | Mum With Buggy | You got past the postbox. | SH |
| L079 | B09 | Hazel | I did. | SH |
| L080 | B09 | Mum With Buggy | What have you done? | SH |
| L081 | B09 | Hazel | It’s called Stryde. It’s under my trousers. | SH |
| L082 | B09 | Mum With Buggy | Since when? | SH |
| L083 | B09 | Hazel | Half seven this morning. Five weeks of mornings. | SH |
| L084 | B10 | Emma | When did you stop doing that? | SH |
| L085 | B10 | Hazel | Five weeks ago. | SH |
| L086 | B10 | Emma | You never said. | SH |
| L087 | B10 | Hazel | You never asked. You said I was all right. | SH |
| L088 | B10 | Emma | ...You look like you. Before. | SH |
| L089 | B10 | Hazel | Before what? | SH |
| L090 | B10 | Emma | I don’t know. | SH |
| L091 | B10 | Hazel | No. Neither did I. | SH |
| L092 | B11 | Roy | The car’s at eight. | SH |
| L093 | B11 | Hazel | I’m walking him. | SH |
| L094 | B11 | Roy | Hazel. | SH |
| L095 | B11 | Hazel | Watch me. | SH |
| L096 | B11 | Roy | You’ve not done that in three years. | SH |
| L097 | B11 | Hazel | Say it again. | SH |
| L098 | B11 | Roy | You’ve not walked like that in three years. | SH |
| L099 | B11 | Hazel | When did I start, Roy? | SH |
| L100 | B11 | Roy | The March your knee went. The step outside the library. You grabbed the wall and you never let go of it. | SH |
| L101 | B11 | Hazel | You knew the day. | SH |
| L102 | B11 | Roy | I’ve known every day. I didn’t know what to do except the car. | SH |
| L103 | B11 | Hazel | I’m not angry. I’d stopped looking as well. | SH |
| L104 | B11 | Hazel | There’s one in your drawer. | SH |
| L105 | B11 | Roy | What for? | SH |
| L106 | B11 | Hazel | You come down our stairs sideways, Roy. | SH |
| L107 | B11 | Roy | I thought you’d not seen. | SH |
| L108 | B11 | Hazel | I’ve seen. It goes round, it moves nothing. That one doesn’t go round. | SH |
| L109 | B12 | Hazel | Oscar. Do the walk. | SH |
| L110 | B12 | Oscar | What walk? | SH |
| L111 | B12 | Hazel | Is that what I look like? | SH |
| L112 | B12 | Oscar | That’s just walking, Nana. | SH |
| L113 | B13 | Hazel | Twenty-four of them in a drawer. Every one went round my knee. Not one of them took the weight off it. It goes round, it moves nothing. The walk my grandson copied wasn’t my knee. It was my body carrying seventeen times my weight onto one spot, and doing it badly. This takes the weight before it lands. | TC |
| L114 | B13 | Hazel | I put it on at half seven this morning and I’ve not thought about it since. No wall. No stick. No car. He walked up that hill holding my hand and there was nothing to copy. He’s not why I’m telling you this. I’d stopped looking at myself walk. | TC |
| L115 | B13 | Hazel | Two straps, under thirty pounds, today at getstryde.co. Sixty days to send them back. No awkward questions. Keep one. Give the other to whoever’s been driving you. Then put it on, walk to your own front gate, and ask the little one to do your walk. Your turn. | TC |

**115 lines · 911 words:** 109 `SH` · 2 `VO` (L076–L077, Hazel's inner voice on the stairs) · 3 `TC` (L113–L115, the close) · 1 hook block pair (L001–L013, 66 words). Per speaker: Hazel 60 · Roy 17 · Emma 15 · Wendy 9 · Assistant 4 · Mum with buggy 4 · Oscar 3 · Lollipop lady 2 · Dan 1.

### Claims (§43A) — against the STRYDE claim register (`products/stryde/stryde_product_sheet.md` §9)

| Line | Claim | Register | Status |
|---|---|---|---|
| L058, L114 | "seventeen times what you weigh goes through it" (every step down) | 17× bodyweight every step, user-confirmed V7.49.29 | ✓ held. The number is never generated on screen (§17) |
| L062 | "Three years with orthopaedic surgeons" | user-confirmed V7.49.29 | ✓ held |
| L053 | "Mine were bone on bone. Both." | built for bone on bone, user-confirmed | ✓ held. Wendy's "They wanted to replace them at seventy-one" implies surgery was avoided — **F3** |
| L064 | "This has a pad. It stays on the spot." | the pad, user-confirmed (prompts say "the pad", never "silicone") | ✓ held |
| L072, L115 | "Sixty days. They take it back." / "Sixty days to send them back. No awkward questions." | 60-day guarantee, user-confirmed | ✓ held; "no awkward questions" is new wording — **F4** |
| L068, L115 | "Thirty pounds. For two." / "Two straps, under thirty pounds" | **no price in the register**; two straps = the B1G1 offer ✓ | **F1** |
| L057 | "One spot. Two centimetres under the kneecap." | site: the patellar tendon immediately below the kneecap; **2 cm is not advertiser-held** | **F2** |
| L060, L114 | "This takes the weight before it gets there" / "before it lands" | load-path wording; **the locked mechanism claim is protection** (load-path retired for this product) | voiced as written; pictured as protection — **F5** |
| L064 | "The Facebook copies slide." | names a platform (§10A) + a comparative knock-off claim | voiced verbatim, never pictured — **F6** |
| L115 | "today at getstryde.co" | URL not in the sheet | **F7** |
| L087, L110 | "Five weeks ago" / "That's just walking" | story outcomes, a character's own experience | voiced as written |

### Mode & Model Lock (§18A)

| Item | Lock |
|---|---|
| Mode | **4 — Realistic Film** (the script declares "photoreal, like a short film") |
| Format | **AI Drama VSL** (§3B), one hook → one film |
| Aspect | 9:16 everything; location/property plates 16:9 (V7.68.1) |
| Images (sheets, plates, outfit/prop/info cards) | **`gpt_image_2_5` Sunburst**, `quality: high`, `resolution: 2k` (cast sheets) — Higgsfield; Kie on out-of-credits (§5) |
| Film clips | **Seedance 2.5 on Kie (`kie.py seedance`), 720p, ingredients mode — no frames** (V7.68.0); takes for connected action (§24K part 5, `takes.py`) |
| Dialogue | inside the Seedance clips, each speaker's **§24I voice master** as the audio ingredient (voice-only refs, no BGM) |
| Inner VO (L076–L077) | ElevenLabs `eleven_v4` clone of Hazel's voice master (§22U, via the API), untrimmed (§24L) |
| Close (L113–L115) | a Seedance to-camera take with her master |
| Music / room tone / SFX | ElevenLabs (`music.py` with the §40A register map; `mix_scene.py`) |
| Grade | `edit/LUT-IMPRESSION.cube` in the edit only; no trimming (§24L) |
| Side | **right knee** (FP18; F13) |

---

## 3. Cast (step 3) — generated, on the board for your check

Everyone who speaks gets a sheet (the voice master needs a face), so there are **nine**: Hazel, Roy, Emma, Dan, Oscar and Wendy, plus the three one-offs who speak (the pharmacy assistant, the mum with the buggy and the lollipop lady). Non-speaking extras (the school-gate children, Wendy's two grandchildren, people on the hill) are cast at step 5 (§13).

| Sheet | Job | File | Board |
|---|---|---|---|
| N-HAZEL | `cf70f513-d352-4839-a8e2-50947d8790d8` | `cast/N-HAZEL_v1.png` | To check |
| C1-ROY | `6e67ffa6-a10c-4310-8563-47e1cdb1a577` | `cast/C1-ROY_v1.png` | To check |
| C2-EMMA | `ffa3001f-1942-4106-ae45-da9ca505901e` | `cast/C2-EMMA_v1.png` | To check |
| C3-DAN | `b39f8693-24de-4708-8a11-70eac6f393ff` | `cast/C3-DAN_v1.png` | To check |
| C4-OSCAR | `dd7583a9-42b5-443c-b10d-d621363cf0d0` | `cast/C4-OSCAR_v1.png` | To check |
| C5-WENDY | `60f65ab9-18ac-4625-8f60-55d426a0f68a` | `cast/C5-WENDY_v1.png` | To check |
| X1-ASSISTANT | `4b9f0bdf-746e-4a2c-920c-a655e8eb046f` | `cast/X1-ASSISTANT_v1.png` | To check |
| X2-MUM | `e4c9a212-e500-40d7-acd3-6e748367b295` | `cast/X2-MUM_v1.png` | To check |
| X3-LOLLIPOP | `8fcfb728-6aef-4d00-966e-54e24f3324bb` | `cast/X3-LOLLIPOP_v1.png` | To check |

Manual run: **not checked by me** (§18B step 3). Confirm or Fix each one on the board.

The prompts are in `cast/<ID>.prompt.txt` (8,456–9,882 chars), built from Appendix A by ID in `cast/build_sheets.py`, in this order:
- `CAM-FILM` (Alexa 35 + Cooke S4/i 50mm T4, tripod);
- `AVATAR-SHEET` + `SHEET-GRID`;
- `SKIN-T`;
- `LOOK-IMPRESSION`;
- `CAP-FILM`;
- `NEG-SHEET` + `NEG-GRID` + `NEG-FILM` + `NEG-DEFAULT-FACE`.

Three per-character adjustments:
- **Oscar** (a four-year-old) takes a child-skin line in place of `SKIN-T`, and child anti-defaults in place of `NEG-DEFAULT-FACE`.
- **The lollipop lady** drops "no glasses" (her glasses are her).
- **Emma and the mum** drop "no jewellery" (Emma's chain, the mum's nose stud).

Spend: 9 Sunburst jobs at 2.75 cr each = **24.75 Higgsfield cr**, one render each.

### Identity strings — read off the renders (§7)

| ID | Identity string |
|---|---|
| N | white English woman, 67, average height, soft; round face, wide cheekbones, hazel-brown eyes, kind mouth; silver-grey layered jaw-length bob with a left side parting; oatmeal cable-knit cardigan over a navy top, mid-grey skirt above the knee, navy loafers |
| C1 | white English man, 70, tall and lean, slightly stooped; long face, high forehead, deep-set grey eyes, long nose, large ears; thinning short white hair, clean-shaven; navy quilted gilet over a pale blue Oxford shirt, tan chinos, brown suede desert boots |
| C2 | white English woman, 39, slim; oval face, hazel-green eyes, freckles; mid-brown hair with honey highlights in a messy high ponytail; a thin gold chain; grey marl sweatshirt, dark straight jeans, white canvas trainers |
| C3 | British Indian man, 41, tall and solid; broad square face, dark brown eyes, thick black brows, full short black beard; black hair swept back, grey at the temples; dark green half-zip jumper over a white T-shirt, charcoal chinos, brown trainers |
| C4 | boy, 4, mixed heritage, light-brown skin; round face, big dark brown eyes; thick dark-brown curls; red-and-navy striped long-sleeve T-shirt, navy shorts, white socks, blue Velcro trainers |
| C5 | Black British woman (Barbadian heritage), 74, tall and heavyset; broad strong face, dark-brown eyes; close-cropped white hair; cobalt-blue cotton mac over a navy spotted dress just below the knee, black walking shoes, a canvas bag on the shoulder |
| X1 | British Bangladeshi woman, 25, petite; narrow oval face, large dark eyes, thick brows, a small mole above the right corner of the mouth; navy hijab; navy short-sleeved pharmacy tunic over a white long-sleeve top, black trousers, black trainers, a blank white name badge |
| X2 | white English woman, 32, tall and lean; long freckled face, pale blue eyes; copper-red low ponytail; faded denim jacket over a white T-shirt, black leggings, grey trainers, a small cross-body bag |
| X3 | white English woman, 63, short and round; round pink-cheeked face, blue eyes behind round tortoiseshell glasses; auburn hair under a white peaked cap with a black band; long fluorescent yellow-green hi-vis coat with silver bands, black trousers, black lace-ups |

### §19A axis tables

| Axis | N Hazel | C1 Roy | C2 Emma | C3 Dan | C4 Oscar | C5 Wendy | X1 Assistant | X2 Mum | X3 Lollipop |
|---|---|---|---|---|---|---|---|---|---|
| Face | soft round, wide cheekbones | long, lean, domed brow | longer round, freckled | broad square, strong jaw | round child | broad, strong, square chin | narrow oval | long, freckled | small round, glasses |
| Hair | silver layered bob, side parting | thinning white crop | brown-honey high ponytail | black, swept back, beard | dark curls | white close crop | navy hijab | copper low ponytail | auburn set wave, cap |
| Age | 67 | 70 | 39 | 41 | 4 | 74 | 25 | 32 | 63 |
| Build | average, soft | tall, lean, stooped | medium, slim | tall, solid | small, sturdy | tall, heavyset | petite | tall, lean | short, round |
| Wardrobe key | oatmeal / navy / grey | navy gilet / tan | grey marl / denim | green / charcoal | red-navy stripe | cobalt / navy spot | navy tunic | denim / black | hi-vis yellow |
| Marker | mole on left cheek | deep chin dimple | scar through left brow | scar on right cheekbone | freckle on nose tip | gold front tooth | mole above lip | nose stud | right-cheek dimple, crooked glasses |
| Voice | West Yorkshire, warm, plain | West Yorkshire, soft, practical | Yorkshire, quick, bright-covering | Leeds, easy, careful | small Yorkshire child | Leeds with a Bajan lilt | Bradford, bright, polite | Yorkshire, friendly | broad Yorkshire, chatty |

**Clearance:** every pair differs on ≥ 6 axes. ✓

Against the STRYDE roster:
- Hazel is set apart from the nearest roster faces:
  - half-my-age's narrator (steel-grey blunt bob with a fringe, beaked nose): face, hair, build, wardrobe and marker all differ;
  - three-regrets' women in their 70s.
- Wendy is set apart from half-my-age's Friend 2 (short, full-figured, Jamaican heritage, salt-and-pepper afro, mole): face, hair, build, wardrobe and marker all differ.
- The script's "grey bob, a good cardigan, kind face" is kept as written (layer 4); `NEG-DEFAULT-FACE` keeps her off the stock retiree.

### Voices (§22D) — for the §24I film voice masters, built after the maps (§18)

**`VOICE-HAZEL`** (Hazel's dialogue, the inner VO cast to her master, and the close)
```
An English woman of sixty-seven from West Yorkshire, Halifax: a warm, plain, mid-low voice with a little huskiness, flat northern vowels and short "u", unhurried. She says the hard things quietly and evenly and lets a line sit; dry rather than sad, never self-pitying. Statements fall at the end; questions only lift a little. Never theatrical, never sing-song.
```

| Character | `VOICE-[CHAR]` (short form; full string at the voice stage) |
|---|---|
| Roy | Englishman of 70, West Yorkshire, soft and practical, a little gruff, says kind things too quickly and fills silences with plans |
| Emma | Englishwoman of 39, Yorkshire softened by years in Leeds, quick and bright, covering worry with brightness |
| Dan | British Indian man of 41, Leeds-born, easy and warm, careful when he has to be honest |
| Oscar | a boy of four, small clear Yorkshire child's voice, matter-of-fact |
| Wendy | Black British woman of 74, Leeds with a Barbadian lilt from home, certain, amused, a laugh under the words |
| Assistant | British Bangladeshi woman of 25, Bradford, bright and polite, a shop voice |
| Mum with buggy | Englishwoman of 32, Yorkshire, friendly and direct |
| Lollipop lady | Englishwoman of 63, broad West Yorkshire, chatty and conspiratorial |

---

## Flags (decisions for the user — nothing below was changed silently)

| # | Where | Finding | Recommendation |
|---|---|---|---|
| **F1** | L068, L115 | "Thirty pounds. For two." / "Two straps, under thirty pounds": **the price is not in the claim register** | voiced as written; **please confirm the price** |
| **F2** | L057 | "Two centimetres under the kneecap": the register says "immediately below the kneecap", and 2 cm is not advertiser-held | voiced as written; please confirm |
| **F3** | L053 | "They wanted to replace them at seventy-one": implies the strap avoided surgery | voiced as written; please confirm the advertiser is happy with it |
| F4 | L115 | "No awkward questions": guarantee wording beyond "sixty-day money-back" | voiced; confirm it matches the terms |
| F5 | L060, L114 | "takes the weight before it gets there / lands": load-path wording, while the locked claim is **protection** | voiced as written; pictured as protection |
| **F6** | L064 | "The Facebook copies slide": names a platform (§10A) and makes a comparative knock-off claim | voiced verbatim, never pictured; confirm |
| **F7** | L115 | "getstryde.co": not in the product sheet | voiced; **confirm the domain** (and whether it is shown as an end card in the edit) |
| F8 | L082–L083, L087 | "Five weeks of mornings" (the August hill) and "Five weeks ago" (end of August): the same count on two dates | voiced as written; the hill scene sits late in August, just before the hall scene |
| F9 | Roy's day | "The March your knee went… three years": a flashback is possible but not in the script | dialogue only (no flashback) unless you want one |
| **F10** | B08 vs FP23 | the script puts her hand on the rail for steps 1–2 (VN27), and FP23 says nobody holds the banister | kept: the script's own action. `rail_ok` on those two steps only; the hand comes off on the third; every other stairs shot is hands free |
| **F11** | B08 vs FP13 | "The strap goes on bare skin, just under the kneecap, trousers over it". FP13: worn on screen the knee is bare, never trousers over or pushed up round the strap | **my read:** she sits on the edge of the bed in her nightdress (bare knee) and slides it up to the tendon (FP10), then pulls her trousers on over it with the strap no longer in shot. The insert shows the bare knee only. Confirm |
| F12 | Hooks | the script has **one** hook (A) → **one finished film** | say if you want more hooks (written by me only after your approval, §18 step 6) |
| F13 | side | the script never says which knee | **right knee** throughout (FP18) unless you say otherwise |
| F14 | length | 911 words at the inspo's 165 wpm ≈ 5:30 of speech + silent beats (the impression, the hill, the stairs A/B, the walk, the first day) ≈ **6:00–6:40** (inspo 6:29) | film pace, no trimming (§24L) |
| F15 | close | the inspo's lead holds the product to camera; our VISUALS say "nobody sees it for the rest of the ad" | the close is to camera at the gate **without the product in hand**; an end card with the two straps can be added in the edit (§17) if you want one |
| F16 | Drive | no Google Drive connector in this session → no `OUTPUT/` tree | every render is on the board |
| F17 | Hazel | "Do NOT age her face" (script) against the locked `SKIN-T` close-up texture (§22S) | the sheet keeps the locked skin standard with mild age features (her face reads 67); Fix on the board if it reads older |

## Next — on your go (§18B step 5)

Confirm or Fix each avatar on the board and answer F1, F2, F3, F6, F7, F11 (and anything else). Then steps 4–5 as one delivery:
- **Property and plates (16:9):** the Property Sheet (Hazel and Roy's stone terrace: the dining room for the lunch, the hall from the kitchen to the front door, the stairs, the kitchen, the bedroom) and its plates. Then the other locations: the chemist, the hill with its postbox (one location for all three hill scenes), the school gate, and Emma's car.
- **The plan:** the scene list with Scene Bibles, the act map (with takes) and the wardrobe map by story day, ingredient lists per take, and the `angles.py` / `takes.py` / `wardrobe.py` / `visual_plan.py` passes.
- **Then:** the §24I voice masters, then Hook A on Seedance.
