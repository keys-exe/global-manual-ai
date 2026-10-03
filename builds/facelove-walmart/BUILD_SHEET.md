# Build Sheet — facelove-walmart

**FACELOVE Changing Foundation Stick · "The Walmart — Go Be Too Busy Glowing To Look Backward" (USA_FL_MO1684, AI Animation Movie, TOFU)** · Standards V7.100.0 · **RUN: MANUAL · MODE 5 Pixar Film · AI Drama VSL** · 2026-10-03

Steps 1–3 of §18. **Stopped at the avatar review (§18B, V7.62.0)**: steps 4–5 wait for your go.
Boards: Current https://claude.ai/artifact/KDWnrhSUGd5cTmrB28MBcW · Old https://claude.ai/artifact/JCGVnxgDJ1wb4ijcTj5Yhn · Final https://claude.ai/artifact/MJYSNxQs8zmZauvGD9yAfM · Plan https://claude.ai/artifact/RgnvPVq64gwcwwqheqg9BY

---

## 0. Intake (§18B)

| Input | Found | Notes |
|---|---|---|
| Drive folder | `1Xvl_PR2jCEe3WJk177Vn5T-1efS1gt80` — matches no existing build → new build | fetched with `fetch_drive.py` → `intake/` |
| Inspo (primary) | `INSPO VIDEO.mp4` — the "Michelle at Walmart" Pixar-style AI drama (ex-husband + 41-year-old, Seoul colleague, pink Korean foundation, back to Walmart, "I'm too busy glowing") | 337.3 s · 9:16 · 360×640 · 23.98 fps · audio |
| Inspo (secondary) | `VISIUAL VIDEO HOOK.mp4` — a live-action street collision (books dropped, the meet-cute, the other woman arrives) — the brief's "visual hook reference" energy | 27.4 s · 9:16 · 720×1280 · 30 fps |
| Script | `SCRIPT.docx` — the brief (hypothesis, cast, production rules, editor notes) then `Script` with `VISUAL:` scene labels. **No speaker labels** — speakers inferred (F5). Parsed → `work/lines.json` | **21 spoken lines · 564 words (dialogue 290, VO 274)** · 2 action notes + 13 scene labels |
| Product Sheet | `facelove_product_sheet.py` V7.49.5 — byte-identical to the sheet already in `facelove-my-mother` | copied to `product/` (`products/` is owner-only — F14) |
| Product images | 7: `CLOSED`, `BALM_END_DEPLOYED`, `BRUSH_END_DEPLOYED` (canonical, attachable) · `FACELOVE_REF_SHEET_01` (**never attach**) · `PACKAGING` · `PRIMER` · `MYSTERY_GIFT` | layer 1 (§7) |
| Cast pictures | none — every face is new (§19A) | — |
| Loom | none | — |

**Message fields:** `RUN MANUAL` → **RUN: MANUAL**. `MODE` not given → **Mode 5 Pixar Film** from the brief: "AI-Animation-Movie", "Type: Movie Ad", "turn this into a movie, not a song… painterly visual style", and the inspo is a 3D animated film (F2). `FORMAT` → **AI Drama VSL** (§3B). `HOOKS` → the script has one cold open (the carts) → **HK1 as written**; two more at step 6 for your approval (F3). `VOICE` → derived (§22D). `CAP` → the §5B estimate. `BUILD` → `facelove-walmart`.

**Connector map (§5, `connectors.md`):** images → Higgsfield (**private workspace, your call this chat**); Seedance → Higgsfield (no `KIE_API_KEY` — rung 2); Kling → Higgsfield; voice, music, SFX → ElevenLabs API; HeyGen connected (no talking heads in a film). Nothing missing.

**Credit cap (§5B, draft from 564 words):** Higgsfield **16,500** · ElevenLabs **14,200** (`budget.md`). Re-estimated at step 5 from the act map. The private workspace holds **4,006** — enough for steps 4–5 and the voices, not for every film take (F16).

---

## 1. Absorption Sheet (§42)

### Part 1 — measured (`work/inspo_measure.json`, `work/inspo_transcript.txt`)

| Instrument | Inspo (primary) | Hook reference (secondary) | Settles |
|---|---|---|---|
| Duration / aspect | 337.3 s · 9:16 | 27.4 s · 9:16 | 9:16 locked; the inspo is a 5½-minute film |
| Scene cuts | **92 shots, mean 3.7 s**; narration over held 4–5 s shots, quick 1–2 s inserts | 6 shots, mean 4.6 s; the collision lands at 2.8 s | our rhythm: 3–4 s shots, the collision inside the first 3 s |
| Silence (−40 / −30 dB) | none — narration and a music bed under everything | none | sound bed throughout; music only in the edit (§24M) |
| Words / pace | ~1,065 words / 337 s ≈ **190 wpm** (narration-led, almost no lip-sync) | 6 short lines | our **564 words** — more of it acted on screen — ≈ **3:30–4:00** with the held beats (the carts, the payoff smile, the colour change, the epilogue) (F13) |
| Speech mix | ~95 % narration over the scenes; the few lines quoted, not lip-synced | dialogue only | ours: narration 49 %, lip-synced dialogue 51 % — five scenes are played, not told |
| Captions | rounded pink box, white sentence-case text, 1–4 words, centred at ~70 % height, every spoken word | none | EG01 (the brief: English subtitles throughout) |
| Shot frames + per-second sheets | `intake/frames/INSPO VIDEO/` (12 sheets, 184 shot frames) | `intake/frames/VISIUAL VIDEO HOOK/` | Edit Grammar below |

### Part 2 — structure map (inspo → our script)

| t | §3B act | Inspo shows | Our slot |
|---|---|---|---|
| 0–16 | **Hook — cold open** | the aisle, Michelle with toilet paper, Peter + the 41-year-old, "Michelle?" | **The Cold-Open Hook** — the carts **hit** in the first 3 s, Peter's double-take, "It is just me.", she glides away |
| 16–46 | Before — the wound | the armchair: Peter hands over the divorce papers, she breaks down | **The Divorce** — the envelope on the table, "Thirty one years.", the house goes silent |
| 46–74 | Problem — failed fixes | grey skin, layers of makeup, every product on every shelf | **The Undoing** (the mirror) + **Nothing Worked** (the vanity, every cream) |
| 74–190 | Turn — the messenger | a Seoul colleague, the pink bottle, the cracked-foundation macro, the white-to-shade swatch | **The Sister** (Rosa at the door with wine) + **The Reveal** (the violet stick, the colour change in one unbroken shot) |
| 190–216 | Turn — it works | glass skin, church compliment | **The Change** — the first morning, back in the photos |
| 216–286 | After — back to Walmart | the 41-year-old asks, Michelle names the product, walks away | **The Payoff** — the same aisle, "What do you use on your skin?", Michelle **says nothing**, smiles, glides away |
| 286–337 | Offer & close | product heroes, claims, "60 % off", PS: Peter texted, "I'm too busy glowing" | **The Epilogue** (the text, phone face down) + **CTA** (to the lens, the violet stick turning, the offer) |

### Part 3 — Style Lock (copied)

- **Format:** AI Drama VSL in 3D feature animation — the heroine narrates over scenes; others speak.
- **Visual grammar:** wide two- and three-shots in the aisle, MCU/CU singles for reactions (Peter's stare, Michelle's widening eyes), inserts (the papers, the cart wheels, the swatch), product macros; shallow focus from MCU in.
- **Light and colour arc (read off the frames):** bright flat-white store light with blue signage; warm amber lamplight in the divorce living room; cool sunset office; warm bathroom/vanity morning light in the After; product heroes on soft cream.
- **Rhythm:** mean shot 3.7 s; narration carries time jumps ("four years ago", "three months ago", "so back to Walmart").
- **Tone of voice:** plain American, wry, quietly triumphant; the hurt understated.

### Part 3A — Edit Grammar → `EDIT-WALMART`

| ID | Device (inspo) | Where | Our build |
|---|---|---|---|
| EG01 | **captions** on every spoken word — rounded pink box, white sentence case, 1–4 words, ~70 % height | whole film | **kept** — "English subtitles throughout"; the box colour is set in CapCut (we keep the shape; the colour can follow FACELOVE's lilac — your call at step 8) |
| EG02 | **full-frame shots only** — no split, no PiP | whole film | kept |
| EG03 | **hard cuts**, one dissolve into the flashback | 41 s | kept — the brief: "Image cools and dissolves back in time"; a dissolve or colour shift marks the four-years-earlier block |
| EG04 | **macro of the product working** — white swatch on skin resolving to tone | 180–190 s | kept — **The Reveal hero macro, one continuous unbroken shot, no cut during the colour change** (brief, non-negotiable) |
| EG05 | **product hero** held in a hand / on a surface | 286–316 s | kept for the CTA — the violet stick turning slowly, no offer badge (brief) |
| EG06 | **inspo's cracked-foundation macro** (the villain on skin) | 125–135 s | available for Nothing Worked — the old foundation caking on her face in the mirror (unbranded) |
| EG07 | **the low cart-wheel shot** as she walks away | 283 s | kept — the Payoff exit |
| Light | store white → amber flashback → warm morning After | by act | §30K arc (Look Sheet field 3) |
| Angles | eye-level two-shots, low on Peter, CU reactions, low cart insert | — | range set at step 5 (`angles.py`, F-moves F1–F24) |

### Part 4 — script absorption

Our script is **the inspo's own story** (same names — Michelle, Peter, the 41-year-old, the Walmart aisle, the PS text, "too busy glowing") **re-staged**: the Seoul colleague becomes **Rosa, her older sister, at her door with wine**; the narrated Walmart reunion becomes a **cart collision played on screen in the first 3 seconds**; Michelle explains nothing in the Payoff — **she smiles and glides away**; the product is FACELOVE, not the inspo's pink bottle. Cold open → four-year flashback (divorce, undoing, nothing worked, the sister, the reveal, the change) → back to the same aisle → epilogue → CTA. Spoken verbatim (§22U / §24I).

**Story spine (§24I part 9):** want — to stop disappearing · stakes — being seen by the man who left (and by herself) · obstacle — the mirror · failed fix — every cream, every foundation · turn — Rosa: "It was never your age… It was the foundation." · payoff — Peter's stare, the younger woman asking, Michelle saying nothing · plants — the cart (hook → payoff), the mirror (Undoing → Change), "a few weeks ago" (L004 → The Sister), the phone (Epilogue).

### Part 5 — surfaced, not absorbed

| Inspo element | Disposition |
|---|---|
| The **Walmart** logo and signage on every aisle shot | **never generated** (§10A: no platform logos in any prompt) — a generic big-box aisle in blue and white; the name stays only in the voice (F7) |
| Seoul / "Korean foundation", "Korean pharmacists", "251 % better", "2 million bottles", "98 % of women", "a quarter of your wrinkles gone", "60 % off" | not in our script; none are FACELOVE claims |
| The inspo's pink bottle (a real competitor) | never shown; our product is the violet FACELOVE stick |
| Toilet paper / smoothie / yoga mat props (inspo-specific) | our own props at step 5 (no brands on any packaging) |
| The inspo heroine's look (silver waves, pink sheath dress) | not copied — Michelle is designed new (§19A) |

### Part 6 — beat-it plan

| Inspo weakness | Our delta | Where |
|---|---|---|
| The reunion is narrated over standing two-shots | **the carts collide on screen at 0–3 s** — physical, fast, then the stare | Cold-Open Hook |
| The fix arrives from a colleague abroad, told in VO | **her sister at the door**, played on screen, love before the product | The Sister |
| The swatch is a back-of-hand demo | **one unbroken macro on Michelle's own face**, white warming into her shade | The Reveal |
| Michelle explains the product to the younger woman | **she says nothing** — a smile, the cart turns, she glides away; the product is told to the viewer instead (CTA) | The Payoff / CTA |
| The PS is a closing line | **the text arrives on screen** ("Peter: Hi Michelle how are you?"), she sets the phone face down | The Epilogue |

### Part 7 — confirmation

Conflicts are listed in **Flags**. **Confirm or correct the absorption along with the avatars.**

---

## 1b. Animated Film Look Sheet (§24J) — written by the agent, shown for information

| # | Field | Value |
|---|---|---|
| 1 | Genre and reference | A warm, grown-up American animated family drama made like a theatrical 3D feature (the brief: "cinematic tone, painterly visual style, emotional pacing") |
| 2 | Virtual camera | a virtual large-format sensor with spherical primes; 24 fps, 180° shutter. Focal by scale: WIDE 24–28 · FULL 32–35 · MED 40–50 · MCU 50–65 · CU 75–85 · MACRO 100 (the Reveal); deep focus on sheets and wides, shallow from MCU in; one pull per clip at most (§30J). The Hollywood-drama coverage of §24P (established place, 180° axis, the turn in close, reactions) |
| 3 | Light | motivated and designed (`LIGHT-ANIM`). **Present (hook, payoff):** bright cool-white store fluorescents from above, warm bounce off the floor, a soft key from the aisle end · **The Divorce:** amber table lamps at dusk dying to blue-grey night · **Undoing / Nothing Worked:** a cold bathroom vanity bulb, flat and unflattering · **The Sister / Reveal:** warm hallway light at night, then soft warm vanity bulbs · **The Change / Epilogue:** golden morning sun; the store doors open onto golden light; a sunlit patio · **CTA:** clean warm studio-like key in her own home |
| 4 | Palette | Present: clean white, cool blue, warm wood; Michelle in cream and camel. Before: amber, dusty mauve, faded grey (her cardigan). Turn: Rosa's marigold and ink blue. After: soft lilac (the stick), cream, gold |
| 5 | Grade (edit only) | warm highlights, soft teal shadows, gentle S, skin protected; **the flashback cooled and slightly desaturated** (the brief's colour-grade marker) → `edit/grade.json` → `LUT-WALMART.cube` at step 8 |
| 6 | Design and materials | stylised adults 5.5–6 heads tall, one dominant shape each (Michelle triangle, Peter square, Rosa round, the younger woman an inverted triangle); soft subsurface skin, sculpted hair in strands, real fabric weave; **the product photoreal (`PIX-SPLIT`)** |
| 7 | Motion and animation | naturalistic acting, small squash and stretch on bodies (never the product); camera script: **fast and physical in the hook** (F19 crash zoom on the impact at most once, F23 breathing handheld), patient and locked in the Before (F2, F18 creep), one slow push per turn (F1), travelling and open in the After (F13 lead, F14 follow, F6 pull-back reveal through the store doors); the full F1–F24 range checked at step 5 (`angles.py` MOVE) |
| 8 | Performance | restraint: Michelle calm, cool, unbothered in the present, hollow in the Before (never a sob in front of anyone); Peter self-assured, then frozen; the younger woman guarded, then urgent; Rosa warm, fierce and loving throughout |
| 9 | Sound | studio voice performance (`AUD-ANIM`); dialogue only in clips (`NEG-SOUND`); the cart crash, wheels, the envelope, the door, the cap, the phone buzz as SFX; music register map at step 5 (§40A) — investigation, never sad, until the stick's first frame, the change on that frame |

**`LOOK-WALMART`** (verbatim on every Mode 5 frame — `cast/LOOK.txt`):
```
THE LOOK OF THIS FILM: A warm, grown-up American animated family drama made like a theatrical 3D feature — a bright big-box store aisle, a lamplit family living room, a bedroom vanity and a sunlit patio, told with tenderness and quiet wit. Appealing stylised adults about five and a half to six heads tall, each built on one clear shape, large expressive eyes, soft rounded features and simple readable hands. Soft subsurface skin with no pores, sculpted groomed hair that catches the light in strands, fabric with real weave and weight, and surfaces with a light painterly softness. Bright clean whites, cool blues and warm wood in the store; amber lamplight, dusty mauve and faded grey in the house of the Before; soft lilac, cream, camel and warm gold in the After. Rendered with natural, balanced colour, ungraded — the grade is added later in the edit. Every frame of this film shares exactly this look.
```

---

## 2. Script, product, claims, locks (step 2)

### Visual Instruction Ledger (§27F) — opened (every row → a beat or CapCut line at step 5)

| ID | Anchored to | Instruction (verbatim, condensed) | Status |
|---|---|---|---|
| VN01 | Hook open | Open FAST, all VO in first 3 seconds, no build-up. Bright Walmart aisle, Michelle (after-state, glowing, elegant) pushing her cart | open — generic aisle, no logo (F7) |
| VN02 | Hook | Peter rounds the corner with the younger woman, not looking — carts HIT. Both lurch. The Instagram reference's energy: fast physical impact, immediate | open — "(the carts hit)" in the script |
| VN03 | L002 | Peter looks up annoyed, then his face changes completely — staring, scanning head to toe. The younger woman stiffening | open |
| VN04 | L003 | Michelle calm, cool, unbothered "It is just me", steering her cart around his and gliding away. Peter frozen | open |
| VN05 | L004 → L005 | Image cools and dissolves back in time — four years earlier: colour grade or dissolve to mark the flashback (The Divorce → The Change) | open → edit (EG03, grade) |
| VN06 | L005–L006 | Warm living room. Peter sets a manila envelope on the table, will not meet her eyes. Michelle sitting very still, the floor falling out from under her | open — blank envelope, nothing printed |
| VN07 | after L006 | Peter turns and walks out the door. Michelle alone in the armchair as the light dies, the house suddenly enormous and silent | open |
| VN08 | L007 | (to her reflection, hollow) — the mirror | open |
| VN09 | L009 | (at the vanity, defeated) — every cream, every serum, every foundation | open — **no real brand on any bottle** (F8) |
| VN10 | L011 | Rosa arriving at the door with wine, warm and resolute | open — unlabelled bottle |
| VN11 | L011–L012 | Rosa taking Michelle's chin, tilting her tired face to the hallway light | open |
| VN12 | L014 | Rosa draws the purple FACELOVE stick from her bag — hero macro | open — the violet stick (sheet §14a) |
| VN13 | L014–L015 | **The Reveal hero macro: one continuous unbroken shot, no cut during the colour change; pure white warming into her exact shade in real time, melting in, lines softening, dark circles gone, smooth glowing finish. Non-negotiable** | open — colour front per the sheet; **lines stay** (`TERRAIN_LOCK`) — F10; "Nadine's" read as Michelle's (F9) |
| VN14 | The Change | (no on-script note) her first morning, the photos, standing taller | open |
| VN15 | Payoff | RETURN TO WALMART: the exact same aisle, continuing from the cold open; Peter still staring | open — same plate as the hook |
| VN16 | L019 | the younger woman catching up to Michelle urgently, asking what she uses | open |
| VN17 | after L019 | **(a warm, serene smile, saying nothing)** — Michelle turns her cart and glides away; Peter small and forgotten | open |
| VN18 | L020 | Michelle walking out through the sliding doors into golden light, then a sunlit patio; her phone lights up "Peter: Hi Michelle how are you?"; at peace, she sets it face down | open — the phone text set in post (§17, F11) |
| VN19 | L021 | CTA: Michelle to camera, glowing and whole, clean cinematic hero shot; the purple FACELOVE stick turning slowly; **no offer badge** | open — Michelle the declared narrator, the one allowed look into the lens (§24J) |
| VN20 | whole film | English subtitles throughout. No on-screen text beyond captions. No offer badge | open → CapCut (EG01) |
| VN21 | whole film | Product render: purple stick | open — `PIX-SPLIT`, the real violet stick |

### Phrase inventory (§27B) — `SH` acted on screen · `VO` narration; beats assigned at step 5. **Speakers inferred** (the script has none — F5)

| ID | Scene | Speaker | Line (verbatim) | Disp. | Claim | Note |
|---|---|---|---|---|---|---|
| L001 | Hook | MICHELLE | At sixty three, I ran into my ex-husband in Walmart. He was with her. The woman he left me for. She is forty one. | VO | — | VN01–VN02 · Walmart (F7) |
| L002 | Hook | PETER | Michelle? Is that you? My God, what happened, did you get work done? You look so much more beautiful. | SH | — | VN03 |
| L003 | Hook | MICHELLE | It is just me. | SH | — | VN04 (calm, cool, unbothered) |
| L004 | Hook | MICHELLE | The only reason I did not fall apart standing there is because of what my sister handed me a few weeks ago. | VO | — | VN05 |
| L005 | The Divorce | PETER | I am sorry, Michelle. After thirty one years. I just... I need something different. | SH | — | VN06 |
| L006 | The Divorce | MICHELLE | Thirty one years. | SH | — | VN06–VN07 (barely a whisper) |
| L007 | The Undoing | MICHELLE | When did I start looking like this? Tired. Worn out. Older than I am. No wonder he stopped looking at me. | SH | — | VN08 (to her reflection) |
| L008 | The Undoing | MICHELLE | I stopped looking in mirrors. I stopped being in photos. And I buried my face under more and more makeup that only made it worse. | VO | — | |
| L009 | Nothing Worked | MICHELLE | Every cream. Every serum. Every foundation on the shelf. The Estée Lauder, the L'Oréal. And I look older in all of them. | SH | real brands named (F8) | VN09 |
| L010 | Nothing Worked | MICHELLE | I decided this was just what sixty looked like, and I made my peace with disappearing. | VO | — | |
| L011 | The Sister | ROSA | Michelle, open the door. I brought wine and I am not leaving. ...Oh, honey. Look at you. Come here. | SH | — | VN10–VN11 |
| L012 | The Sister | MICHELLE | I am fine, Rosa. I am. I just... I do not know who that woman in the mirror is anymore. He looked at me like a stranger the day he left, and lately so do I. | SH | — | |
| L013 | The Sister | ROSA | Can I tell you something? Two years ago, I felt exactly like that. Same mirror, same thoughts. And I will tell you what I had to learn the hard way. It was never your age, Michelle. It was the foundation. Made for young skin, so on ours it just sits on top and ages us. | SH | comparative (category) — F12 | |
| L014 | The Reveal | ROSA | This is the one that changed it for me. Here, let me just show you. It comes out pure white. Then it reads the warmth of your own skin and turns into your exact shade, and it melts right in. | SH | goes on white Tier 1 ✓ · "reads… your skin" · "exact shade" Tier 2 — F12 | VN12–VN13 |
| L015 | The Reveal | ROSA | It has jojoba, shea, vitamin E, so it feels like nothing and never cakes. It covers the lines, the tired, the circles, and it still looks like your own skin. Not a mask. You. | SH | jojoba, shea, vitamin E on the INCI ✓ · "never cakes" (Tier 2 "does not settle") · cover-not-erase ✓ | VN13 |
| L016 | The Change | MICHELLE | I ordered my own before Rosa even left. And the first morning I tried it, the tired just lifted. For the first time in years, I did not look away from my own reflection. | VO | — | VN14 |
| L017 | The Change | MICHELLE | And it was more than my face. I stood taller. I got back in the photos. I stopped hiding. So by the time that cart hit mine in Walmart, I was not afraid of anyone. | VO | — | Walmart (F7) |
| L018 | The Payoff | YOUNGER WOMAN | Wait. That is your ex-wife? | SH | — | (to Peter, unsettled) |
| L019 | The Payoff | YOUNGER WOMAN | I am sorry, I just have to ask. What do you use on your skin? You look amazing. | SH | — | VN16–VN17 |
| L020 | The Epilogue | MICHELLE | I did not need to say a thing. I did not look back either. Two weeks later, Peter texted me. First time in four years. I read it, I smiled, and I put my phone away. | VO | — | VN18 |
| L021 | CTA | MICHELLE | So if someone ever looked at you and made you feel like you had faded, please hear me. It was never you. The thing she wanted to know, I will tell you instead. It is called FACELOVE, and I have linked it below. Right now you get two Foundation Sticks for almost the price of one, plus a free primer, a mystery gift, and free shipping and a full thirty day money back guarantee. Go be too busy glowing to look backward. | VO (to the lens) | offer — F6 · "glowing" — F4 | VN19 |

### Claims (§43A) — against the supplied Product Sheet's claim register

| Claim | Where | Sheet tier | Disposition |
|---|---|---|---|
| Comes out pure white, turns into your shade, melts in | L014 | Tier 1 (goes on white, resolves to tone) | ✓ shown — the Reveal macro, colour front behind the brush |
| "reads the warmth of your own skin" | L014 | the sheet: the colour is pigment already in the stick; "reads/senses your skin" is the wording it warns off | voiced as written, **F12** |
| "your exact shade" | L014 | Tier 2 (one shade; "perfect/exact" overstates) | voiced as written, qualification in the editor note — **F12** |
| "jojoba, shea, vitamin E" | L015 | on the published INCI (jojoba seed oil, shea butter, tocopheryl acetate) | ✓ Tier 1 |
| "never cakes" | L015 | Tier 2 ("does not settle into wrinkles or pores" is the claim to build on) | voiced as written; shown as the film lying evenly in the creases |
| "covers the lines, the tired, the circles… still looks like your own skin. Not a mask." | L015 | cover, not erase — matches `TERRAIN_LOCK` | ✓ — every after frame keeps every line |
| "Made for young skin… sits on top and ages us" | L013 | category comparative, no brand | **F12** |
| "Every foundation… The Estée Lauder, the L'Oréal. And I look older in all of them." | L009 | two real competitor brands named in a disparaging line | **F8** — your / counsel's call; never shown on screen |
| "two Foundation Sticks for almost the price of one, plus a free primer, a mystery gift, and free shipping and a full thirty day money back guarantee" | L021 | free shipping, 30-day guarantee Tier 1; BOGO, free primer, mystery gift **unconfirmed** | **F6** |
| "Go be too busy glowing" | L021 | "glowing" is **banned outright, both channels** (sheet §3) | **F4** |
| Brief's Reveal: "lines softening… dark circles gone… smooth glowing finish" | VN13 | `TERRAIN_LOCK`: the crease is as deep in the last frame as the first; "glowing" banned | **F10** — the render evens colour and covers the circles; lines stay |

### Mode & Model Lock (§18A)

| Item | Lock |
|---|---|
| Mode | **5 — Pixar Film** (F2) · format **AI Drama VSL** (§3B) · 9:16 (plates 16:9) · **no trimming** (§24L) · Hollywood drama coverage (§24P) |
| Cast sheets, plates, info cards, beat frames | **`nano_banana_pro`** (§24J "Nano Banana only", §18A routing) via Higgsfield — **logged as `nano_banana_2`** (Higgsfield reroutes Pro; seen on every earlier Pixar build — F15) |
| Film clips | **Seedance 2.5**, 720p, ingredients mode (information, never frames), one take per scene up to 30 s, a new shot every 2–5 s inside it (§24K part 5), `SD-PROMPT` format (§4) — via Higgsfield (no Kie key) |
| Voice | §24I film voice masters (Seedance), **untrimmed**; Michelle's VO from an ElevenLabs v4 clone of her master; `AUD-ANIM` studio voice performance |
| Music / SFX / room tone | ElevenLabs (`music.py`, sound generation) — never in a clip |
| Product | held and applied, never worn (`CONTACT_LOCK`); the violet satin barrel, one wordmark, photoreal in the stylised world (`PIX-SPLIT`); the working end already deployed (`NEG-UNCAP`); terrain unchanged after (`TERRAIN_LOCK`) |
| Mechanism | none drawn — the colour change on her face *is* the mechanism |
| Real brands | Walmart, Estée Lauder, L'Oréal — **voice only, never in a picture** (§10A, sheet §7) |

---

## 3. Cast (step 3) — generated, on the board for your check

Five sheets, all new faces (no cast pictures in the folder). The rest of the store crowd are one-off extras cast at step 5 (§24O rule 10).

| Sheet | Job | File | Board |
|---|---|---|---|
| N-MICHELLE (before — flashback) | `e41bb60b-dd24-4808-8b8e-5956cbe2dda6` | `cast/N-MICHELLE_v1.png` | To check |
| N-MICHELLE-AFTER (present — hook, payoff, epilogue, CTA) | `7ee60be8-ae88-458d-8d13-d5ebfc2ff6a7` | `cast/N-MICHELLE-AFTER_v1.png` | To check |
| C1-PETER | `cd1173f1-ffef-4258-90f0-4c5143ea351b` | `cast/C1-PETER_v1.png` | To check |
| C2-YOUNGER (the woman, 41) | `260a0f37-7ab1-4b16-b87a-ccc9c4bba621` | `cast/C2-YOUNGER_v1.png` | To check |
| C3-ROSA (the sister) | `702ccb5a-64ac-4585-af45-b7b8443efba6` | `cast/C3-ROSA_v1.png` | To check |

Manual run: **not checked by me** (§18B step 3) — Confirm or Fix each on the board. Prompts `cast/<ID>.prompt.txt` (10.2–11.5k chars), built from Appendix A by ID in `cast/build_sheets.py`: `CAM-ANIM` (virtual large format, spherical prime 50 mm, deep focus) → render opening → `SHEET-GRID` → `AVATAR-SHEET` (photograph words read as render) → `PIX-SHAPE` + the shape and age in shape → `PIX-EYES` → `LOOK-WALMART` → `CAP-ANIM` → `NEG-SHEET` (anti-render clauses dropped) + `NEG-GRID` + `NEG-PIX` + `NEG-DEFAULT-FACE`. **Michelle after = her before sheet attached as Image 1** (face copied, clothes / hair / skin tone changed as written; every line kept — cover, not erase). Spend: **5 renders, 10 Higgsfield credits** (private workspace 4,016.35 → 4,006.35).

### Identity strings — read off the renders (§7)

| ID | Identity string |
|---|---|
| N | Latina American woman, 63, light olive skin; heart-shaped face, pointed chin, large dark-brown almond eyes, thin arched brows, slim straight nose, small mouth; a small dark beauty mark high on the cheekbone below the outer eye (it renders on her **right** cheek — viewer's left — not the left as asked; your call); chin-length straight dark ash-brown bob heavily threaded with grey, tucked behind one ear; slim, narrow, slightly stooped; dusty-mauve knit cardigan over a grey T-shirt, charcoal pull-on trousers, grey felt slippers |
| N-A | the same woman after: even warm skin tone, under-eye shadows covered, lines still there; the same bob, smoother; standing taller; cream boat-neck sweater, camel wide-leg trousers, tan loafers |
| C1 | white American man, 65, ruddy fair skin; broad square face, square jaw, small pale-blue eyes, thick grey brows, wide nose, thin mouth; short grey hair receding at the temples with a round grey tuft at the front, thin at the crown; tall, barrel-chested; navy quarter-zip over a white collar, tan chinos, brown boat shoes |
| C2 | white American woman, 41, fair skin; face wide at the cheekbones narrowing to a pointed chin, wide-set green eyes, angled brows, short upturned nose, thin wide mouth; freckles on the cheeks; long straight honey-blonde hair with dark roots in a high round bun; tall, athletic; camel cropped blazer, white ribbed tank, black flared leggings, white platform trainers |
| C3 | Latina American woman, 67, warm medium-tan skin, rosy cheeks; round face, warm dark-brown eyes, thick dark arched brows, broad rounded nose, full mouth; shoulder-length black hair with a straight blunt fringe and **one bold silver-white streak from the left temple**; short, soft and full-figured; marigold-orange wrap blouse, long ink-blue skirt, tan sandals |

### §19A axis tables

| Axis | N Michelle | C1 Peter | C2 the woman, 41 | C3 Rosa |
|---|---|---|---|---|
| Shape | triangle (narrow, tall) | square | inverted triangle | round |
| Face | heart, pointed chin | broad square, cleft chin | wide cheekbones, sharp chin | round, full cheeks |
| Hair | grey-threaded ash-brown bob | grey, receding, round tuft | honey-blonde high bun | black, blunt fringe, silver streak |
| Age | 63 | 65 | 41 | 67 |
| Build | slim, narrow | tall, barrel-chested | tall, athletic | short, full |
| Wardrobe key | mauve/grey → cream/camel | navy / tan | camel / black / white | marigold / ink blue |
| Marker | beauty mark on the cheekbone | cleft chin, one ear higher | freckles | the silver streak |
| Voice | below | confident baritone, a salesman's ease, then lost | bright, clipped, a little guarded → urgent | warm, husky, laughing, fierce |

**Clearance:** every pair differs on ≥ 6 axes ✓ (Michelle and Rosa are sisters — related colouring by design, everything else differs). Against the inspo: the inspo's Michelle (silver waves, pink sheath) and the inspo's 41-year-old (dark bob, athleisure) are **not** copied. Against the repo's roster (the other FACELOVE builds' Susan, Beth, Paula — realistic): no repeat.

### Voices (§22D) — for the §24I film voice masters, built after the maps (§18)

**`VOICE-MICHELLE`** (her dialogue, and the VO cast to her master)
```
An American woman of sixty-three, Latina, raised in the American Southwest — a warm, low, slightly husky voice with plain General American vowels and the faintest Spanish softness on her r's, unhurried and composed. In the present she is calm, cool and dry, a smile under the words; in the flashback quiet and hollow, almost to herself. Statements fall at the end; never breathy, never theatrical, never a sob.
```

| Character | `VOICE-[CHAR]` (short form; full string at the voice stage) |
|---|---|
| Peter | American man, 65, confident baritone with a salesman's ease; sorry but self-serving in the divorce; stunned and fumbling in the aisle |
| The woman, 41 | American woman, 41, bright and clipped, a little guarded; then urgent, all pretence dropped |
| Rosa | Latina American woman, 67, warm and husky, a laugh in it, fierce and loving, a light Spanish lilt |

---

## Flags (decisions for you — nothing below was changed silently)

| # | Where | Finding | Recommendation |
|---|---|---|---|
| **F1** | cast | no cast pictures in the folder | five new faces designed (§19A) — Confirm or Fix on the board |
| **F2** | mode | `MODE` wasn't in the message; the brief says "AI-Animation-Movie… a movie… painterly visual style" and the inspo is 3D animation | **Mode 5 Pixar Film, AI Drama VSL** — say if you meant another mode |
| **F3** | hooks | the script has one cold open (the carts). Default is 3 hooks → 3 films | HK1 = the cart collision as written; at step 6 I write **HK2 and HK3** for your approval — or say "one hook" |
| **F4** | L021, VN13, VN01 | "Go be too busy **glowing**" and the brief's "glowing" — the product sheet bans "glowing / radiant / luminous" **in both channels** | voiced as written (it is the CTA close); **never** in a prompt — the picture shows even, warm skin. Your call whether the line stays |
| **F5** | script | no speaker labels; speakers inferred from the action notes and the brief (L001/L004/L008/L010/L016/L017/L020/L021 Michelle's VO; L002/L005 Peter; L011/L013–L015 Rosa; L012 Michelle; L018/L019 the woman, 41) | say if any line belongs to someone else |
| **F6** | L021 | "two for almost the price of one, a free primer, a mystery gift" — **unconfirmed** on the sheet (free shipping and the 30-day guarantee are Tier 1) | kept; please confirm the bundle |
| **F7** | L001, L017, VN01, VN15 | **Walmart** named in the voice and the brief's "bright Walmart aisle" — §10A: a platform name in dialogue is your / counsel's call (default: a generic version too — "at the store"); **no logo or signage ever generated** | voiced as written; the aisle is a generic big-box store in blue and white, no name anywhere on screen. Say if you want the generic VO cut as well |
| **F8** | L009 | "The Estée Lauder, the L'Oréal. And I look older in all of them." — two real competitor brands in a negative line | voiced as written; **never shown** (her vanity bottles are blank, unbranded); counsel's call for paid Meta |
| **F9** | VN13 | the brief says "turning into **Nadine's** exact shade" — no Nadine in this script | read as **Michelle's** shade |
| **F10** | VN13 | "lines softening… dark circles gone… smooth glowing finish" — `TERRAIN_LOCK` (product sheet) keeps every crease as deep after as before; the sheet's Tier 3 also blocks "softens fine lines" | the macro shows the white warming into her shade, tone evening, the circles covered; **the lines stay** |
| **F11** | VN18 | "Peter: Hi Michelle how are you?" on her phone — generated type garbles | the phone screen is generated blank and the text set in post (§17) |
| **F12** | L013–L015 | "reads the warmth of your own skin" (the sheet: the colour is in the stick — it does not read anything) · "your exact shade" (Tier 2, one shade) · "made for young skin… ages us" (category comparative) | voiced as written; the qualifications go in the editor note |
| **F13** | length | 564 words, half of it acted, plus the held beats → **~3:30–4:00 per film** (the inspo runs 5:37) | film pace, no trimming (§24L) |
| **F14** | product sheet | `products/` is owner-only (CODEOWNERS); this session runs as `Chicknben` | the sheet lives in `builds/facelove-walmart/product/`; a `products/facelove/` copy is noted for the owner in BUILD_NOTES |
| **F15** | image model | Higgsfield logs every `nano_banana_pro` call as `nano_banana_2` (the same on every earlier Pixar build) | carried on; the fallback (Kie) needs a `KIE_API_KEY` this account lacks |
| **F16** | credits | your instruction this chat: Higgsfield bills the **private workspace** (4,006 left). The draft cap for this film is ~16,500 Higgsfield credits (Seedance rate unverified — the last FACELOVE film measured ~8 cr/s, which would put it nearer 4,000) | enough for steps 4–5 and the voices; before the film takes I re-estimate from the act map and tell you if the private workspace won't cover it |
| **F17** | cast | Michelle's beauty mark renders on her **right** cheekbone (viewer's left), not the left as written | it stays wherever you confirm it; every later frame copies the confirmed sheet |

---

## Next — on your go (§18B step 5)

Steps 4–5 as one delivery: the location plates at 16:9 (the big-box aisle — hook and payoff; the living room with the armchair — The Divorce; the bathroom mirror — The Undoing; the bedroom vanity — Nothing Worked, The Reveal; the front door and hallway — The Sister; the store's sliding doors and the sunlit patio — The Epilogue; her CTA set), the product info cards (the violet stick at true size in a hand; the colour front: white ahead of the brush, matched behind; the stick in Rosa's bag; the primer), the act map with takes (`takes.py`), the set maps and blocking (`blocking.py`), the visual pitch (`visual_plan.py`), angles and moves (`angles.py`), the wardrobe map per story day (`wardrobe.py`), the music register map — then the voices.
