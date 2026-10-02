# Build Sheet — facelove-my-mother

**FACELOVE Changing Foundation Stick · "YOU LOOK LIKE MY MOTHER" (public shaming + the friends · live-action movie)** · Standards V7.90.7 · **RUN: MANUAL · MODE 4 Realistic Film · AI Drama VSL** · 2026-10-02

Steps 1–3 of §18. **Stopped at the avatar review (§18B, V7.62.0)**: steps 4–5 wait for the user's go.
Boards: Current https://claude.ai/artifact/Gyh667QAbW2fA3GYgjgM23 · Old https://claude.ai/artifact/KZ2UKhTA7GAysVcfgj7K41 · Final https://claude.ai/artifact/1NUkwd9icgtPGXenBTr5Ah · Plan https://claude.ai/artifact/VmUne7ypBrBQa52jVqXRrs

---

## 0. Intake (§18B)

| Input | Found | Notes |
|---|---|---|
| Drive folder | `1M1DbzCv_DwDnXnhwkztLtgEB69yjBUiZ` — matches no existing build → new build | fetched with `fetch_drive.py` → `intake/` |
| Inspo (primary) | `VIDEO INSPO.mp4` — the "Diane" AI drama (divorce, La Mer counter, café friend, the stick, the wedding) — **byte-identical to the script's "Execution reference L1424"** | 266.1s · 9:16 · 720×1280 · 24 fps · audio |
| Inspo (secondary) | `refs/story_source.mp4` — the script's "Story / angle source" (trendtrack) | 660.8s · 9:16 · 720×1280 · 30 fps · story beats only |
| Script | `Untitled document.docx` (table brief: concept, director's notes, cast, offer, 9 scenes VO / dialogue / visual, five make-or-break notes, open items). No title line — the concept heading is the title. Parsed by hand → `work/lines.json` | **27 spoken lines · 487 words (dialogue 306, VO 181)** · 27 visual notes |
| Product Sheet | `facelove_product_sheet.py` V7.49.5 (single-file sheet: slots, locked strings, ratios, claim register, packaging) | copied to `product/` (see F14 — `products/` is owner-only) |
| Product images | 7: `CLOSED`, `BALM_END_DEPLOYED`, `BRUSH_END_DEPLOYED` (the canonical three, attachable) · `FACELOVE_REF_SHEET_01` (**never attach**) · `PACKAGING` (mailer) · `PRIMER` (Dream Skin Primer, offer) · `MYSTERY_GIFT` (lilac gift box) | layer 1 (§7) |
| Cast pictures | Drive `1__Tfn0-oRlpOnPL9ev8zfii2Q9vAcqT0` (linked in the script): **SUSAN OLD, SUSAN NEW, GREG, PAULA, BETH** | layer 1 — each sheet copies its face (F1) |
| Loom | none | — |

**Message fields:** `RUN MANUAL` → **RUN: MANUAL**. `MODE` not given → **Mode 4 Realistic Film**, from the script's own instruction: "live-action movie", "⭐ EDITING STYLE — REAL MOVIE (not animation). Shot as a real film: real actors, real locations… Cinematic, not UGC, not animated" (F2). `FORMAT` → **AI Drama VSL** (§3B — a scripted story with a cast, no presenter). `HOOKS` → the script has one cold open (the toast) → **HK1 as written**; 2 more written at step 6 for your approval (F3). `VOICE` → derived (§22D, below). `CAP` → E0 default. `BUILD` → `facelove-my-mother`.

**Connector map (§5, `connectors.md`):** images → Higgsfield (Sunburst, ODAQ B.V. workspace — this account's rule); **Seedance → Higgsfield** (no `KIE_API_KEY` on this account — rung 2, unverified, the logged model is checked on the first job); Kling → Higgsfield; voices, music, SFX → ElevenLabs API; HeyGen present (no talking heads in a film). Nothing missing.

---

## 1. Absorption Sheet (§42)

### Part 1 — measured (`intake/inspo_measure.json`, `intake/inspo_transcript.txt`)

| Instrument | Drama inspo (primary, L1424) | Story source (secondary) | Settles |
|---|---|---|---|
| Duration / aspect | 266.1s · 9:16 | 660.8s · 9:16 | 9:16 locked; a 3–4½ min film |
| Scene cuts | **92 shots, mean 2.9s**; dialogue beats 1–2.5s, held reactions and establishing 4–11s | 148 shots, mean 4.5s | we cut at the primary's rhythm |
| Silence (−40 / −30 dB) | none — continuous bed | short gaps only | sound bed under everything; the script asks **no music** under the toast, the whisper and the mirror (VN07, VN14) |
| Words / pace | 671 words / 266s = **151 wpm** (VO + dialogue) | — | our **487 words at ~151 wpm ≈ 3:15**, plus the held silent beats (the frozen table, the walk-out, the colour change, the mirror) ≈ **3:20–3:45 per film** (script says ~2:50 — F13) |
| Speech mix | narrator VO over scenes ~55%, lip-synced dialogue ~45%; no to-lens address | — | §3B: narrator never to the lens (our script has no to-lens close) |
| Captions (read off the frames) | **sentence-case white bold, no box, no highlight, centred at ~70% height, 2–6 words**, every spoken word | — | EG01 |
| Shot frames + per-second sheets | `intake/frames/VIDEO INSPO/` (9 sheets, 184 shot frames) | `intake/frames/story_source/` | Edit Grammar below |

### Part 2 — structure map (inspo → our script)

| t | §3B act | Inspo shows | Our slot |
|---|---|---|---|
| 0–12 | **Hook — cold open** | porch at sunset, the last box, "You let yourself go." — VO over her stillness | **SC01 The Toast** (0:00–0:36): the party, the toast, "You look like my mother" |
| 12–48 | Before (the wound) | daughter's video call: the engagement party in 10 weeks, "Dad's going to be there" — her alone at night | **SC02 The Whisper** + **SC03 Inside / the VO** (back to the shut door) |
| 48–100 | Problem (failed fixes) | walks, dress, $1,012 at the La Mer counter, the cracking foundation macro, "nobody looked at me twice" | **SC04 Disappearing**: invite face-down, the family gathering (holds the camera), the mirror — foundation caking grey |
| 100–150 | Turn — the friend brings it | café: the friend reframes ("the face is what he named"), the violet stick on the table, "What is that, a glue stick?" | **SC05 Beth**: the Botox concede, the stick handed over, the colour change on her cheek |
| 150–175 | Turn — the first test | mirror, the swipe macro: white → her shade | **SC05 (end) + SC06 There She Is** |
| 175–235 | After — mirrored scenes | the café stranger's note, the wedding entrance, daughter "did you have work done?", the ex: "Diane, you look—" | **SC07 She Walks Back In** (Paula's boomerang) + **SC08 The Redirect** ("Go enjoy the party, Greg.") |
| 235–266 | Offer & Close | the swipe again over VO, two-stick hero on marble, offer + guarantee, warm party coda | **SC09 CTA + Offer** (Susan among her friends, the cake going round, the stick + primer hero) |

### Part 3 — Style Lock (copied)

- **Format:** AI Drama VSL — scenes with lip-synced dialogue, the protagonist narrating over them, no presenter.
- **Visual grammar:** prestige-drama coverage in 9:16 — MCU/CU singles off-lens, OTS pairs, inserts on hands and objects (the box, the receipt, the phone, the stick), wides only to place a scene; shallow from MCU in.
- **Light and colour arc:** Before at sunset and night (warm low sun outside, cool blue rooms, one warm practical); Problem in flat cool daylight (mirror, store); Turn in soft window daylight (café); After in warm tungsten and string-light gold (the party). Read off the frames — the §30K light arc.
- **Rhythm:** mean shot 2.9s; lines cut on the speaker or the listener's reaction; time jumps carried by the VO ("Six months on", "six weeks").
- **Tone of voice:** plain American, quiet, wry; the hurt is understated.

### Part 3A — Edit Grammar → `EDIT-MYMOTHER`

| ID | Device (inspo) | Where | Our build |
|---|---|---|---|
| EG01 | **captions**: every spoken word, sentence-case white bold, no box, centred ~70% height, 2–6 words | whole film | **kept** (CapCut); plus the script's one title card "YOU LOOK LIKE MY MOTHER." landing late in SC01 (VN03) |
| EG02 | **full-frame shots only** — no split, no PiP | whole film | kept (every row `full`) |
| EG03 | **hard cuts**; no transitions, no speed ramps | whole film | kept; **the colour change is one continuous take, no cut, no ramp** (VN17) |
| EG04 | **macro insert of the product in use** — white swatch on the cheek, blended to her shade | 177–197 | kept — the SC05 colour change (a real continuous take, Beth's hands) |
| EG05 | **product hero on a surface** — the stick on marble, then the two ends open side by side | 213–223 | kept for SC09 — the stick + the primer (the two-unit render is an edit cut-in only, never attached, product sheet §4) |
| EG06 | music bed under most of the film, dipping under dialogue | whole film | **changed by the script**: room tone only under SC01 and the mirror (VN07, VN14); music in the edit elsewhere (§24M, never in a clip) |
| Light | sunset/night → flat day → window day → string-light gold | by act | §30K light arc (Look Sheet field 3) |
| Focus | shallow from MCU in; one pull on the swipe macro | — | §30J |
| Angles | eye-level singles and OTS, low reverse on the ex, high wide on the empty table | — | range copied at step 5 (`angles.py`) |

### Part 4 — script absorption

The script is **the inspo's story spine retold in a new wound**: the inspo's private insult ("You let yourself go") becomes a **public** one (the drunk anniversary toast in front of thirty friends), and the inspo's café friend becomes **Beth doing Susan's face at her own vanity**. Two wounds up front (his insult, then the friends' whisper), the long disappearing, the friend's reframe (Paula's Botox conceded, then the no-needles stick), the colour change, and a payoff that **rhymes the opening** — the same yard, the cake now cut and passed, Paula crossing to ask *her*. The silent thread (the untouched cake) runs underneath. Spoken verbatim (§22U / §24I).

**Story spine (§24I part 9):** want — to stop being counted out · stakes — the group that witnessed the low point · obstacle — the face the mirror agrees with · failed fix — the old foundation caking into the lines · turn — Beth: "Watch this." · payoff — Paula: "what are you doing?" / "Go enjoy the party, Greg." · plants — the cake (SC01 → SC07), the yard (SC01 → SC07), the mirror (SC04 → SC06), "ask her what she does" (L005 → L023).

### Part 5 — surfaced, not absorbed

| Inspo element | Disposition |
|---|---|
| La Mer jars and receipt (a real brand on screen) | not in our script; and §10A / product sheet §7: **no real third-party brand in any frame** — the old foundation is a blank, unbranded bottle |
| The two-sticks-side-by-side hero | edit cut-in only (product sheet §4: never attached as a reference) |
| "80% skincare", "up to half off", "60 day guarantee" on screen | not ours — our offer is buy 2 + free primer + free shipping + 30-day guarantee (F9) |
| Video call on a phone | not in our script |

### Part 6 — beat-it plan

| Inspo weakness | Our delta | Where |
|---|---|---|
| The wound is private, said once in VO | the wound is **public and on screen** — the toast, the frozen table, then the whisper | SC01–SC02 |
| The friend explains in a café; the swipe is the narrator alone | **Beth does Susan's face with her own hands**, one continuous take — the stick handed over like a secret | SC05 |
| The payoff is one ex's reaction | the **group** that saw the low point sees the comeback; Paula, the woman she was compared to, asks *her* | SC07 |
| Generic party | one silent visual thread — the cake, untouched, then cut and passed around her | SC01 ↔ SC07 |

### Part 7 — confirmation

Conflicts are listed in **Flags**. **Confirm or correct the absorption along with the avatars.**

---

## 1b. Film Look Sheet (§24G) — written by the agent, shown for information

| # | Field | Value |
|---|---|---|
| 1 | Genre and reference | American suburban family drama shot like a prestige streaming series (§24N house base) — a backyard anniversary party under string lights, a quiet two-storey house, a bedroom vanity; warm, intimate, restrained |
| 2 | Camera and glass | **ARRI Alexa Mini LF, large format · ARRI Signature Prime (spherical) · ARRI colour science** · 24 fps, 180° shutter. Focal by scale: WIDE 24–32 · FULL 32–40 · MED 40–50 · MCU 50–65 · CU 75–85 · INSERT 100 macro (the swipe); stop T4–T5.6 wides → T1.8–T2 CU. Shallow from MCU in; one focus pull per clip at most, on a named cue (§30J) |
| 3 | Light | Motivated, soft key from the low sun, string-light bulbs, windows and lamps; 4:1 on faces in the wound and the Before, 2:1–3:1 in the After. Arc: **SC01–SC02 golden hour 3200–4300K + 2700K string lights** (warm and loud, so the drop is a freefall) · **SC03 dusk 6500K blue through the door glass, the party glow behind her** · **SC04 cool overcast 6500K / bathroom 4000K** · **SC05–SC06 soft warm window daylight 5000K at the vanity** · **SC07–SC09 late-afternoon gold 4300K into string-light dusk** (the rhyme) |
| 4 | Palette | dusty blue, cream, oatmeal, sage and grey-blue in the Before (Susan's wardrobe muted, cool); honey, amber, wine and warm white in the After (Susan in wine red, F12) |
| 5 | Grade (the edit only) | warm lift, gentle S, slight teal in the shadows, amber highlights, skin protected → `edit/grade.json` → `edit/LUT-MYMOTHER.cube` (made and checked with `lut.py` at step 8) |
| 6 | Optical texture | soft highlight roll-off, faint warm halation around bulbs and bright windows, clean glass with a gentle edge fall-off; no haze, no flare |
| 7 | Motion | Seedance move library (§24N): F2 locked for the toast (the camera lives on Susan), **F1 slow push-in on Susan's still face on "You look like my mother"** (director's note 1), F5 follow on the walk-out (the whisper mid-step), F2 locked for the colour change (one continuous take), F6 pull-back reveal on the return; one move per shot |
| 8 | Performance | restraint (§28B): Greg charming four seconds, then puzzled and quiet — a verdict, not a rant; Susan never screams or cries in front of them; Beth easy and honest; Paula mortified, then warm |
| 9 | Sound and post | dialogue only in every clip (`NEG-SOUND`, no BGM, V7.73.3); room tone per location; **no music under SC01, SC02's walk and SC04's mirror** (script); SFX: glass clink, the porch door click, forks still, the stick's cap; music register map at step 5 (§40A) — investigation, never sad, until the stick's first frame, the change on that frame |

**`LOOK-MYMOTHER`** (verbatim on every Mode 4 frame — `cast/LOOK.txt`):
```
THE LOOK OF THIS FILM: An American suburban family drama shot like a prestige streaming series — a backyard anniversary party under string lights, a quiet two-storey family house and a bedroom vanity, watched with warmth and restraint. Honey and amber golden-hour light and warm string-light bulbs at the party; cool blue-grey dusk and lamplit tungsten in the house of the Before; soft warm window daylight at the vanity; dusty blue, cream, sage, oatmeal and wine in the sets and clothes. Highlights roll off softly with a faint warm halation around bulbs and bright windows; clean modern glass with a gentle fall-off toward the frame edges. Captured with natural, neutral colour and a gentle contrast, ungraded — the grade is added later in the edit. Every frame of this film shares exactly this look.
```

---

## 2. Script, product, claims, locks (step 2)

### Visual Instruction Ledger (§27F) — opened (every row → a beat or CapCut line at step 5)

| ID | Anchored to | Instruction (verbatim, condensed only where the script repeats itself) | Status |
|---|---|---|---|
| VN01 | SC01 open | long dinner table, string lights, thirty friends. A sheet cake in the middle, "Happy Anniversary" in icing, untouched. Greg pushes up from his chair, sways, taps his glass | open — cake icing is generated **blank** and set in post (§17, F11) |
| VN02 | L001 | Golden hour, long table. He STANDS, fork clink, everyone smiling for a toast, so the turn is a freefall | open |
| VN03 | SC01 | On-screen text lands late: "YOU LOOK LIKE MY MOTHER." | open → CapCut line |
| VN04 | L002–L003 | his face changes, he looks down at her, and the room follows his eyes · the laughter dies mid-air. Susan's hand finds the edge of the table | open |
| VN05 | L003–L004 | Hold on SUSAN, absolutely still, the cake in soft focus between her and Greg. Never cut to him once it's cruel, only hear him · Push into HER face, never his, hold the frozen beat too long | open (L002, L003, L005 are `off` — Greg heard, not seen) |
| VN06 | L005 | loose gesture across the table at PAULA | open (heard; his arm may enter the frame edge) |
| VN07 | SC01 | ONE beat to Paula, staring at her plate. Room tone, no music | open |
| VN08 | SC01 end | he drops into his chair, reaches past the cake for his drink. Dead silence. Thirty forks not moving | open |
| VN09 | SC02 | Susan stands, folds her napkin, sets it beside the cake. As she passes two friends near the drinks table, low, not meant for her | open |
| VN10 | L007 | Time the whisper so she's mid-step when she hears it. She keeps walking · Susan doesn't break stride. The porch door clicks shut behind her | open (SFX door click) |
| VN11 | SC03 | Susan's back against the shut door, party glow behind the glass, her face half in the dark. The VO runs only now, after the peak | open |
| VN12 | SC04 | An invite face-down on the counter | open (blank card, F11) |
| VN13 | SC04 | At a family gathering she volunteers to hold the camera, steps out of frame | open (the daughter, C4) |
| VN14 | SC04 | Her mirror, the old foundation sinking grey into her smile lines. She stops mid-application, and just stops. No music | open — old foundation = a blank unbranded bottle (§10, product sheet §7) |
| VN15 | SC05 open | BETH lets herself in without knocking, garment bag over her shoulder. One look at Susan, and she pulls the vanity stool out | open |
| VN16 | L013 | Susan, disarmed, sits. Beth tilts her chin to the light and takes out a plain white stick | **F10** — the stick is violet (product sheet §14a); "plain white" read as *unlabelled* — see F10 |
| VN17 | L014–L015 | one swipe up Susan's cheek. White, then as Beth blends, it turns · The stick revealed unlabeled, handed over like a secret. The real continuous colour change, no cut, no speed ramp | open — the product sheet's colour-front rule (white ahead of the brush, matched behind) |
| VN18 | L015 | Intimate bedroom light, Beth doing Susan's face with her hands | open |
| VN19 | L016 | steps back so Susan can see the mirror · Susan stares at her own cheek, evened out, glowing, real | open — "glowing" never in a prompt (product sheet §3: banned word); lines unchanged (`TERRAIN_LOCK`) |
| VN20 | SC06 | Susan holding her own eyes in the mirror, not flinching for the first time. Beth over her shoulder | open |
| VN21 | SC07 | she comes in with Beth. Conversation stalls, then a friend lights up. PAULA crosses to her first, genuine, both hands out | open |
| VN22 | L023 | Paula catches it, a surprised breath, then a real laugh, the two of them together. At the edge of the yard, Greg goes still · Hold on the two women laughing. Greg small, soft focus, forgotten | open |
| VN23 | SC07 | Rhyme the opening, the same table, and this time the cake is being cut and passed, life moving, Susan in the middle of it | open — same yard plate as SC01 (`mirror_of`) |
| VN24 | SC08 | Greg, quiet now, at her shoulder · she's already turning back to Beth and Paula, laughing before he's finished | open |
| VN25 | L026 | Greg left standing alone. Susan in the middle of her friends, lit up | open |
| VN26 | SC09 | Susan lit up among her friends, the cake going around, then a soft hero of the stick + primer | open (PRIMER.jpg; the carton is white, the stick violet) |
| VN27 | SC09 | Overlay: 50,000+ WOMEN OVER 40 · BUY 2, GET A FREE PRIMER · FREE SHIPPING · 30-DAY GUARANTEE | open → CapCut line; **F8** on the 50,000 |

### Phrase inventory (§27B) — dispositions `SH` (acted on screen) / `off` (heard, speaker off screen) / `VO` (narration); beats assigned at step 5

| ID | Act · scene | Speaker | Line (verbatim) | Disp. | Claim | Visual note |
|---|---|---|---|---|---|---|
| L001 | HK · SC01 | GREG | Thirty years. Thirty. Somebody get this woman a medal for putting up with me, right? | SH | — | VN01–VN03 |
| L002 | HK · SC01 | GREG | …thirty years. And I look at you lately and I just, I don't know. | off | — | VN04 |
| L003 | HK · SC01 | GREG | You look like my mother, Susan. When did that happen? | off | — | VN04–VN05 |
| L004 | HK · SC01 | SUSAN | Greg. Sit down. | SH | — | VN05 |
| L005 | HK · SC01 | GREG | Paula's the same age as you. Exact same. Look at her, then look at you. Just ask her what she does. That's all I'm saying. | off | — | VN06–VN08 |
| L006 | BF · SC02 | FRIEND-A | …that was awful of him. | SH | — | VN09 |
| L007 | BF · SC02 | FRIEND-B | …I mean, though. She did kind of stop trying. It's just sad to watch. | SH | — | VN09–VN10 |
| L008 | BF · SC03 | SUSAN | He humiliated me in front of everyone we know. But that wasn't the part that kept me up. It was them. My friends. They'd already decided. And I stood there and couldn't argue, because some small part of me had decided the same thing. | VO | — | VN11 |
| L009 | PB · SC04 | SUSAN | So I made it true. I stopped going. Muted the group chat. Skipped the birthdays. And every morning the mirror agreed with them, my foundation caking into every line I owned, until I looked exactly like the word he used. | VO | villain = the old foundation (category, no brand) ✓ | VN12–VN14 |
| L010 | TN · SC05 | BETH | There's a thing Saturday. Whole group. You're coming. | SH | — | VN15 |
| L011 | TN · SC05 | SUSAN | So everyone can compare me to Paula again? She looks ten years younger than me, Beth. Everyone saw it. | SH | — |  |
| L012 | TN · SC05 | BETH | Paula had Botox last month. Of course she looks like that. That's needles, two thousand dollars, and doing it all again in twelve weeks. | SH | **F4** (named Botox, cost/timing) |  |
| L013 | TN · SC05 | BETH | I'm not saying you go do that. You don't need to. Come sit. Watch this. | SH | — | VN16 |
| L014 | TN · SC05 | BETH | Everything you've been wearing was built for a thirty year old, so it sits on top and sinks into your lines and ages you. This was made for us. Goes on white, don't panic. | SH | **F5** comparative · "goes on white" Tier 1 ✓ | VN17 |
| L015 | TN · SC05 | BETH | It reads your skin and becomes your exact shade. The niacinamide takes the red down. It settles into the lines instead of cracking on top. | SH | **F6** | VN17–VN18 |
| L016 | TN · SC05 | BETH | It won't erase a wrinkle, no. Nothing does, not even what Paula paid for. It just stops the wrinkle being the first thing anyone sees. No needles. No downtime. Thirty seconds. | SH | cover-not-erase ✓ · **F7** | VN19 |
| L017 | TN · SC05 | SUSAN | …and this is all you did? | SH | — |  |
| L018 | TN · SC05 | BETH | This is all I did. | SH | — |  |
| L019 | TN · SC06 | SUSAN | …there she is. | SH | — | VN20 |
| L020 | TN · SC06 | BETH | She never left. You just needed one person who didn't believe them. | SH | — | VN20 |
| L021 | AF · SC07 | SUSAN | Saturday. The same yard I'd been hiding from for months. I almost turned the car around. | VO | — | VN21 |
| L022 | AF · SC07 | PAULA | Susan. Look at you. You look incredible, what are you doing? | SH | — | VN21–VN22 |
| L023 | AF · SC07 | SUSAN | Funny. Greg told me to come ask you. | SH | — | VN22–VN23 |
| L024 | AF · SC08 | GREG | Susan. You look… I was wrong. You never gave up. Maybe we could talk— | SH | — | VN24 |
| L025 | AF · SC08 | SUSAN | Go enjoy the party, Greg. | SH | — | VN24 |
| L026 | AF · SC08 | SUSAN | I didn't get younger. I didn't take him back. I never gave up. I just stopped disappearing for people who'd already counted me out. | VO | — | VN25 |
| L027 | OC · SC09 | SUSAN | It's the Facelove Changing Foundation Stick, made for the skin we have now. Over fifty thousand women over forty are on it. Right now, buy two and they'll add their Dream Skin Primer free, with free shipping and a thirty day guarantee. If the people around you decided you'd given up, they were wrong. The link's below. | VO | **F8** · **F9** | VN26–VN27 |

### Claims (§43A) — against the supplied Product Sheet's claim register

| Claim | Where | Sheet tier | Disposition |
|---|---|---|---|
| Goes on white, becomes your shade as you blend | L014–L015 | Tier 1 | ✓ shown (the colour change, VN17) |
| Cover, not erase — "It won't erase a wrinkle… stops the wrinkle being the first thing anyone sees" | L016 | matches `TERRAIN_LOCK` | ✓ every after frame keeps every line |
| "It reads your skin… your exact shade" | L015 | "senses/reads your skin" banned; "exact/perfect" Tier 2 | voiced as written, **F6** |
| "The niacinamide takes the red down" | L015 | niacinamide **not on the published INCI** — Tier 3 BLOCKED on the sheet; the brief's own claim check lists it from the PDP | voiced as written, **F6** — please rule |
| "It settles into the lines instead of cracking on top" | L015 | the sheet's claim to build on is the opposite wording: "does **not** settle into wrinkles" | voiced as written, **F6** |
| "built for a thirty year old… sinks into your lines and ages you" | L014 | comparative (category, no brand) | **F5** |
| Botox named, "$2,000, again in twelve weeks" | L012, L016 | not a product claim; the brief: soften for paid Meta | **F4** |
| "No downtime. Thirty seconds." | L016 | not in the register | **F7** |
| "Over fifty thousand women over forty" | L027, VN27 | **Tier 3 BLOCKED** on the sheet (sources differ); the brief: "under the 100k cap" | **F8** |
| Buy 2 + free Dream Skin Primer + free shipping + 30-day guarantee | L027, VN27 | free shipping, 30-day guarantee Tier 1; free primer **unconfirmed** on the sheet | **F9** (the brief also asks to confirm the bundle at checkout) |
| Product name "Facelove Changing Foundation Stick" | L027 | website name ✓; the carton reads "COLOR CHANGING FOUNDATION STICK" | voiced as written; the carton's type is set in post (sheet §14d) |

### Mode & Model Lock (§18A)

| Item | Lock |
|---|---|
| Mode | **4 — Realistic Film** (F2) · format **AI Drama VSL** (§3B) · 9:16 (plates 16:9) · **no trimming** (§24L) |
| Cast sheets, plates, info cards, product cards | `gpt_image_2_5` **Sunburst**, `quality: high`, `resolution: 2k` (V7.72.0 — realistic) via Higgsfield, ODAQ B.V. workspace |
| Film clips | **Seedance 2.5**, 720p, ingredients mode (§4 — information, never frames), one take per connected action (§24K part 5, `takes.py`) — via Higgsfield (no Kie key; F15) |
| Voice | §24I film voice masters (Seedance), **untrimmed**; Susan's VO cast to her master (ElevenLabs v4 clone of it) |
| Music / SFX / room tone | ElevenLabs (`music.py`, sound generation) — never in a clip |
| Product | held and applied, never worn (`CONTACT_LOCK`); violet satin barrel, one wordmark; the working end always already deployed (`NEG-UNCAP`); terrain unchanged after (`TERRAIN_LOCK`) |
| Mechanism | none drawn — the colour change on her cheek *is* the mechanism (adaptation, §11 of the sheet) |

---

## 3. Cast (step 3) — generated, on the board for your check

Eight sheets. **Five from your cast pictures** (each face attached as Image 1 and copied — F1): Susan (before), **Susan after** (the same woman, foundation on, lines still there — your SUSAN NEW), Greg, Paula, Beth. **Three new faces** for the speaking/recurring roles with no picture: the daughter (SC04), Friend A ("…that was awful of him.") and Friend B ("She did kind of stop trying."). The rest of the group (the thirty friends) are one-off extras cast at step 5 (§13).

| Sheet | Job | File | Board |
|---|---|---|---|
| N-SUSAN | `47cd159a-30fa-41d7-b1f5-68d4871c20b3` | `cast/N-SUSAN_v1.png` | To check |
| N-SUSAN-AFTER | `73a1f9e2-ccd9-4ce8-8f46-b7b98175dc24` | `cast/N-SUSAN-AFTER_v1.png` | To check |
| C1-GREG | `5c5dd2ea-d555-4d43-ac32-6befddd3e2ce` | `cast/C1-GREG_v1.png` | To check |
| C2-PAULA | `ca74192d-f209-4bab-97dd-7b7814c9e7ea` | `cast/C2-PAULA_v1.png` | To check |
| C3-BETH | `9dd80ab1-1135-4ec8-ac17-60633c68f945` | `cast/C3-BETH_v1.png` | To check |
| C4-DAUGHTER | `c7ee4552-d66b-4208-879d-1161fb76fc2b` | `cast/C4-DAUGHTER_v1.png` | To check |
| C5-FRIEND-A | `9e17f3d8-44f6-4e9e-a9ca-914616a6feee` | `cast/C5-FRIEND-A_v1.png` | To check |
| C6-FRIEND-B | `36640bd2-6fc6-451a-a045-9e61290741ff` | `cast/C6-FRIEND-B_v1.png` | To check |

Manual run: **not checked by me** (§18B step 3) — Confirm or Fix each on the board. Prompts `cast/<ID>.prompt.txt` (9,181–9,780 chars), built from Appendix A by ID in `cast/build_sheets.py`: (supplied face clause) → `CAM-FILM` (Alexa Mini LF + Signature Prime 50mm T4, tripod) → `AVATAR-SHEET` + `SHEET-GRID` → `SKIN-T` → `LOOK-MYMOTHER` → `CAP-FILM` → `NEG-SHEET` + `NEG-GRID` + `NEG-FILM` (lens clause dropped) (+ `NEG-DEFAULT-FACE` on the three new faces). The after sheet swaps "bare face" for a light, even foundation with every line kept (cover, not erase). Spend: **8 Sunburst renders, 22.0 Higgsfield credits** (7,902.55 → 7,880.55, ODAQ B.V.).

### Identity strings — read off the renders (§7)

| ID | Identity string |
|---|---|
| N | white American woman, 49; long oval face, high flat cheekbones, hazel-green eyes under slightly heavy lids, straight brows, long straight nose, thin mouth turned down at the corners; deep forehead lines, crow's feet, grey shadows under the eyes, deep nose-to-mouth folds; shoulder-length layered honey-brown hair with blonde streaks and grey at the roots, worn loose and limp, side parting; freckles across the nose and upper chest; sheet outfit dusty-blue chiffon blouse, cream linen trousers, nude flats (the day's outfit comes from the wardrobe map, HT26) |
| N-A | the same woman after: even skin tone, redness gone, every line still there; hair washed and in soft waves with body at the crown; standing taller; sheet outfit wine-red satin sleeveless top, black ankle trousers, black pumps |
| C1 | white American man, 52; long rectangular face, strong square jaw, deep-set blue-grey eyes, wide thin mouth, deep cheek creases, weathered tanned skin; thick salt-and-pepper hair combed back and to the side; tall, broad; navy textured blazer, pale blue open-collar shirt, khaki chinos, brown loafers. **The close-up panel smiles** (his cast picture smiles) — on the board for your check |
| C2 | white American woman of Italian heritage, 49; oval face, high cheekbones, warm brown almond eyes, arched dark brows, full mouth; **smooth unlined forehead** (the Botox tell) against fine lines elsewhere; chin-length wavy chestnut bob with a grey streak at the left temple; plum satin cowl-neck top, charcoal trousers, black mules |
| C3 | white American woman, 49; long oval face, bright blue eyes, straight light-brown brows, wide mouth, pointed chin, freckles across the cheekbones; straight centre-parted honey-brown lob with fine blonde highlights; tall, slim; emerald satin square-neck puff-sleeve top, dark jeans, tan flats |
| C4 | white American woman, 26; oval face with her mother's long straight nose, hazel-green eyes, thick dark-blonde brows, full lower lip, small mole below the right mouth corner; long dark-blonde hair, centre parting; cream cardigan, white T-shirt, light jeans, white trainers |
| C5 | Black American woman, 51; round face, full cheeks, dark brown eyes, broad nose, full lips, a raised mole on the left cheek beside the nose; chin-length layered dark brown bob, grey at the temples; short, full-figured; mustard linen wrap dress, tan sandals |
| C6 | white American woman, 50; narrow heart-shaped face, pointed chin, pale grey close-set eyes, thin arched brows, small upturned nose, thin mouth, a thin scar through the left eyebrow; sleek platinum jaw-length bob; tall, thin; pale pink silk shirt, white wide-leg trousers, nude heeled sandals |

### §19A axis tables

| Axis | N Susan | C1 Greg | C2 Paula | C3 Beth | C4 Daughter | C5 Friend A | C6 Friend B |
|---|---|---|---|---|---|---|---|
| Face | long oval, flat cheekbones | rectangular, square jaw | oval, high cheekbones | long oval, pointed chin | oval, her mother's nose | round, full | narrow heart |
| Hair | honey-brown layers, grey roots | salt-and-pepper, combed back | chestnut wavy bob, grey streak | honey-brown straight lob | long dark-blonde | dark brown bob, grey temples | platinum sleek bob |
| Age | 49 | 52 | 49 | 49 | 26 | 51 | 50 |
| Build | medium, slim | tall, broad | medium, slim | tall, slim | medium, athletic | short, full | tall, thin |
| Wardrobe key | dusty blue → wine | navy / khaki | plum / charcoal | emerald / indigo | cream / denim | mustard | blush / white |
| Marker | freckles, nose + chest | cheek creases | the smooth forehead | freckles, cheekbones | mole below the mouth | mole beside the nose | scar through the brow |
| Voice | below | warm baritone, a drink in it | warm, low, a little husky | easy, honest, bright | — (no lines) | low, quick | soft, gentle (which is worse) |

**Clearance:** every pair differs on ≥ 6 axes ✓ (Susan and Beth share hair colour family and age — face, eyes, hair cut, build, wardrobe and marker differ; Beth's straight centre-parted lob vs Susan's layered side part). Against the repo's roster (STRYDE builds, all British/older): no repeat.

### Voices (§22D) — for the §24I film voice masters, built after the maps (§18)

**`VOICE-SUSAN`** (her dialogue, and the VO cast to her master)
```
An American woman of forty-nine from the suburban Midwest, a low, warm, slightly smoky voice, plain General American vowels, unhurried. She says the worst things quietly and flatly, almost to herself, and lets a line sit; a dry, tired humour under it in the After. Statements fall at the end; never breathy, never theatrical, never a crack in the voice in front of others.
```

| Character | `VOICE-[CHAR]` (short form; full string at the voice stage) |
|---|---|
| Greg | American man, 52, warm easy baritone loosened by drink; charming and loud in the toast, then quiet and puzzled for the verdict; ashamed and soft in SC08 |
| Paula | American woman, 49, warm and low, a little husky, East Coast Italian-American; mortified hush, then genuine delight |
| Beth | American woman, 49, bright, easy and honest, a smile in it; certain without selling |
| Friend A | American woman, 51, low and quick, genuinely sorry |
| Friend B | American woman, 50, soft and gentle — the kindness is what makes it cut |

---

## Flags (decisions for you — nothing below was changed silently)

| # | Where | Finding | Recommendation |
|---|---|---|---|
| **F1** | cast | §19 makes sheets from words with nothing attached; you supplied cast pictures (Susan old/new, Greg, Paula, Beth), which outrank it (§7, layer 1). Each sheet copies its face from the picture as Image 1 | done that way — Confirm keeps them; Fix if a face drifted from your picture |
| **F2** | mode | `MODE` wasn't in the message; the script says "live-action movie… REAL MOVIE (not animation)… Shot as a real film" | **Mode 4 Realistic Film, AI Drama VSL** — say if you meant another mode |
| **F3** | hooks | the script has one cold open (the toast). Default is 3 hooks → 3 films | HK1 = the toast as written; at step 6 I write **HK2 and HK3** (e.g. cold open on the whisper; cold open on the mirror) for your approval — or say "one hook" |
| **F4** | L012, L016 | Botox named (with "$2,000", "every twelve weeks"); your brief: "soften for paid Meta. Lars sign-off" | voiced as written (organic/advertorial cut); a paid-Meta line is your call — never rewritten by me |
| **F5** | L014 | "built for a thirty year old… sinks into your lines and ages you" — category comparative | voiced as written; the old foundation on screen is a blank bottle (no brand) |
| **F6** | L015 | "reads your skin" (sheet: never "senses/reads your skin" — the colour is pigment already in the stick) · "exact shade" (Tier 2) · **niacinamide not on the published INCI** (sheet: Tier 3 blocked; your brief lists it from the PDP) · "settles into the lines" vs the sheet's claim "does **not** settle into wrinkles" | voiced as written; **please rule on the niacinamide line and the "settles into the lines" wording** before the voice stage |
| **F7** | L016 | "No downtime. Thirty seconds." — not in the claim register | voiced as written; please confirm |
| **F8** | L027, VN27 | "Over fifty thousand women over forty" — the sheet marks it Tier 3 (sources differ); your brief says "under the 100k cap" | voiced and captioned as written once you confirm the figure |
| **F9** | L027, VN27 | free Dream Skin Primer with 2 — "unconfirmed" on the sheet; your brief: confirm the bundle at checkout | kept; please confirm |
| **F10** | VN16 | "takes out a plain white stick" — the stick is **violet** (sheet §14a, your photos); VN17 says "the stick revealed **unlabeled**" | the real violet stick, Beth's hand covering the wordmark as she takes it out (unlabelled to the viewer until SC09's hero) — say if you want it white |
| **F11** | VN01, VN12, VN27 | "Happy Anniversary" on the cake, the invite, the overlay — generated text garbles | the cake icing and the invite are made blank and set in post (§17); overlays are CapCut lines |
| **F12** | wardrobe | your SUSAN NEW picture wears wine-red satin; SUSAN OLD dusty blue | the wardrobe map (step 5, per story day) uses dusty blue at the toast and wine red for the return — confirm or change at step 5 |
| **F13** | length | 487 words at the inspo's 151 wpm + the held silent beats → **~3:20–3:45 per film** (script says ~2:50; the inspo is 4:26) | film pace, no trimming (§24L) |
| **F14** | product sheet | `products/` is owner-only (CODEOWNERS); this session runs as `Chicknben` | the sheet lives in `builds/facelove-my-mother/product/` for this build; a `products/facelove/` copy is noted for the owner in BUILD_NOTES |
| **F15** | Seedance route | no Kie API key on this account → Seedance runs through Higgsfield (rung 2, unverified) | the first clip's logged model is checked; add `KIE_API_KEY` to the environment for the default route |

---

## Next — on your go (§18B step 5)

Steps 4–5 as one delivery: the location plates at 16:9 (the backyard party yard with the long table — SC01/SC02/SC07/SC08; the porch door from inside — SC03; Susan's bathroom mirror and kitchen counter — SC04; the family gathering — SC04; Susan's bedroom vanity — SC05/SC06), the product info cards (the violet stick at true size in a hand; the colour front: white ahead of the brush, matched behind; the primer), then the act map with takes (`takes.py`), the visual pitch (`visual_plan.py`), angles (`angles.py`), the wardrobe map per story day (`wardrobe.py`), the music register map — then the voices.
