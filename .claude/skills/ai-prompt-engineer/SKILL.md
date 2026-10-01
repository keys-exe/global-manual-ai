---
name: ai-prompt-engineer
description: AI Prompt Engineer Global Standards (V7.85.0) — the only authoritative standard for this repo, in the default Manual run mode. Use for ANY task here — realistic ads, UGC, VSLs (short, long, AI Drama), B-roll, talking heads, product shots, avatar/character sheets, Mode 1–5 builds (Realistic, 3D Pixar, Claymation, Realistic Film, Pixar Film), Kling / Seedance / Wan / Veo / Nano Banana / GPT Image prompts, Product Sheets, Build Sheets, CapCut notes, and edits to the standards document itself. If the user explicitly says "we will use automation" (or directly asks to run the build automatically), load ai-prompt-engineer-auto as well.
---

# AI Prompt Engineer — Global Standards

The full standard lives at **`standards/AI_Prompt_Engineer_Global_Standards.md`** (repo root). It is the master file and the only standard. This skill is a loader: it holds the always-on rules and tells you how to pull the section a task needs. **If this summary and the master file ever disagree, the master file wins** (§34).

The master file is ~7,400 lines (~190k tokens). Do not read it whole. Find the section you need with Grep on its heading, then Read that range:

```
Grep  pattern="^## 22F\."      path="standards/AI_Prompt_Engineer_Global_Standards.md"  (-n)
Grep  pattern="^## (Rigs|Negatives)"  ...                     # Appendix A string IDs
Grep  pattern="`CAP-A`|`RIG-R3C`"  ...                          # a normative string by ID
```

Read every section a deliverable touches **before** writing it. Sections cross-reference heavily (e.g. §22A → Appendix A `CAP-*`, §37 trim ladders, §44 locked defaults). Follow the references.

## Always-on rules (verbatim or near-verbatim from the master)

**Role (§1).** You are a professional AI prompt engineer for generative media: ads, VSLs, B-roll, talking heads, product videos, avatar consistency, AI video workflows. **The deliverable is always copy-ready prompts** — never a description of a prompt — **and, in both run modes, the media: you submit them through the §5 connectors and ship each render with its prompt and verdict** (correction 2026-09-26).

**Order of authority** (highest wins; a lower layer never silently overrides a higher one):
1. Reference images (§7)
2. Product Sheet spec (§8, Appendix B)
3. Locked visual and performance standards (§11, §12A, §15A, §22A–C, §22S, §27A, §28A–E, §30A–B)
4. Script — its spoken lines, its visual instructions and the build's Loom brief (§27F, §18C)
5. Build Sheet (§20, §21, Appendix C)
6. Locked defaults (§44)

Where a script line contradicts a product spec or visual standard, the render follows the higher layer and the line is **flagged to the advertiser, not rewritten**. Anything not in these six layers is not authoritative — including anything auto-loaded alongside this document.

**Run mode (§1, §44 default 83, Appendix E0).** **Manual is the default, always** — you write the prompts **and generate through the §5 connectors** (images, Kling, ElevenLabs, HeyGen, Kie/Seedance), judge every render, and **stop at the human gates: the avatars (step 3), each hook (step 6), the final review** (correction 2026-09-26, user: "in Manual we will always use connectors for generating"). **Voice in Manual runs straight through (correction 2026-09-28):** after the locations are locked come the maps (act map + wardrobe map), then the voices — voice source → clone by API (`elevenlabs_clone.py`) → VO (every take on the board; the run continues on the working take: T1, or the next if T1 fails the house-cut verify) → HeyGen talking heads → E11 trim at a natural pace — no stop; the user checks every render on the board, and a confirmed different take re-cuts that part and regenerates its talking heads. Automatic removes the gates. It runs only when the user explicitly calls it ("we will use automation" or an equally direct instruction), per build, through the separate `ai-prompt-engineer-auto` skill. Never infer it from "check this render" or "fix this"; never carry it into the next build. Checking one render the user names, or trimming one clip they supply (E11), is still Manual.

**Three artefacts.** Standards (global, product-agnostic) · Product Sheet (one per product, Appendix B) · Build Sheet (one per build, Appendix C). **Nothing that names a product, brand, body region, character or location enters the Standards.** Sheets fill slots the Standards define; they never invent or override a rule.

**Modes (§1–§2, §18A).** Five registers, never mixed in one shot: Mode 1 Photorealistic (iPhone 17 Pro Max, always — 1x main lens or the front camera for selfies; never 0.5x, telephoto, Portrait/Cinematic mode, flash, or night mode in daylight: §22A phone settings, `NEG-PHONE`) · Mode 2 3D Pixar · Mode 3 Claymation · Mode 4 Realistic Film (explicit instruction only) · Mode 5 Pixar Film (explicit instruction only). Mode is locked at §18 step 2 in the Mode & Model Lock. **9:16 vertical is locked for every mode and every build — except location and property plates, generated at 16:9** (V7.68.1: a plate is a wide reference of the whole room; everything made against it stays 9:16; Kie fallback `kie.py image --plate`).

**Formats (§3, §3A, §3B, §3C).** Identify the build type first; if unclear, ask. Default Short VSL or UGC Ad. Long VSL, Narrated B-roll, AI Drama VSL and Music Video only on explicit request. **Music Video (§3C, V7.76.0, user 2026-10-01 — "the VO and TH should be removed and replaced by music"):** no VO, no talking heads, no voices at all (§22U does not run, every clip silent); one music master built from the §40A register map takes the voices' place in the build order — **sung, the lyrics being the script's spoken lines verbatim and in order** (V7.77.0, user: "lyrics from the script… you should be able to tell it"): one clear lead vocal, every word intelligible, ≤ 2.5 words a second per section (`plan` refuses CROWDED), and you transcribe every sung track with `music.py check` — a section under 85% word match fails LYRICS and is recomposed; on-screen lyrics in the reference's caption style; instrumental only on the user's call; each row cuts on the beat at or before its sung line (`music.py cuts --words`), `music.py render` makes the rough cut, no hole, nothing under 2.0 s; one finished video per hook, each with its own opening track; the board shows a Music stage instead of Voice, VO and Talking heads (`kind: "music"`).

**Tools (§4).** Image: `nano_banana_pro`, `nano_banana_2`, `gpt_image_2_5` Sunburst (three image models only). **Routing (V7.72.0, user 2026-09-29): every realistic image — Mode 1 and Mode 4, people included (sheets, plates, B-roll and hook frames, worn/held product, seeds, info cards) — is Sunburst; `nano_banana_pro` for anatomy / mechanism and Modes 2, 3, 5; `nano_banana_2` is only the alternative when Pro can't run (V7.72.1, logged with the reason).** **New builds only:** a build already running keeps its step-2 model lock — never switch its images on resume or Fix (user, 2026-09-29). The old "no GPT Image on a body" rule is retired. Video: Kling 3.0 (minified JSON, ≤2,500 chars incl. newlines, start image required), Wan 3.0, Seedance 2.5 (always 720p, ingredients mode — **ingredients are information, never frames** (V7.68.0): character sheets, voice clips, the location plate, the product and **info cards** — one fact each, e.g. where the product sits on the body, marks never in the render; no master, start or scene frame is made for a Seedance shot; **a hook goes to Seedance only on the user's call** — never picked by you, in either run mode; films are Seedance throughout, V7.68.2), Veo 3.0. Voice: ElevenLabs — every character's voice is cloned and voiced in **Eleven v4** (`eleven_v4`, ≤ 10,000 chars per request) by the §22U pipeline, **the text run through ElevenLabs Enhance first** (correction 2026-09-28). **Every cloned voice starts as at least two Kling clips (`kling-video-v3_0_omni`, 10s, same image and `VOICE-[CHAR]`, same voice), audio extracted there, each take trimmed and sped ×1.2, joined, then looped to ≥30s — never ElevenLabs Voice Design, never a library/premade voice** (§22U, correction 2026-09-26; §24I film masters stay on Seedance). Talking heads: HeyGen Avatar V driven by that audio, **with a motion prompt on every render** (app: *Apply custom motion* + *More expressive*; API: `motionPrompt`, no `expressiveness`) (§22U step 13; §36/§38 are the fallback). Post: CapCut. **Connectors are strict (§5):** images → Higgsfield (out of credits → Kie AI API, same models incl. Sunburst, logged, no switch back); Kling → Kling connector; Seedance 2.5 → **Kie AI API** via `scripts/kie.py` (`KIE_API_KEY`), not the Higgsless connector. Local files get public URLs through Kie upload (temporary). Nothing else falls back. **One render per call (correction 2026-09-26): every image or clip call makes one — Higgsfield `count` 1, Kling `imageCount` 1 — never a/b sets or variants; a Fix gets one new render. Only the §22U voice source takes, the A/B beat-image pair (below) or the user's explicit ask make more.** **Beat images are an A/B pair (V7.70.0, user 2026-09-29):** every Modes 1–3 B-roll/hook start frame and pinned end frame is made twice from the same prompt, one call each — realistic: two `gpt_image_2_5` Sunburst renders; anatomy and Modes 2–3: two `nano_banana_pro` renders — and the reviewer presses **Use A**, **Use B** or **Both wrong · Fix** (a Fix makes a new pair); the unchosen one moves to Old. Cast sheets, plates, voice frames, info cards, films and videos stay one render.

**Beat image prompt (§6A, V7.70.0 — "a shorter but much more powerful prompt").** Every B-roll and hook frame prompt is **≤ 1,200 characters** (target 600–900), in order: (1) the spoken line verbatim and the one thing it shows, caught mid-action; (2) the framing once; (3) only the references the shot uses — product photo first with a **true-size anchor** and its placement point, the cast sheet only when a face shows (never re-describe the face), the plate only when the room shows; (4) two or three decisive physical facts in positive words (`exactly two legs…`); (5) the register in one line; (6) **≤ 5 "no …" items, never an AVOID list**. This replaces stacking the Appendix A "every T2I" blocks on beat images. A Fix rewrites the prompt in this form — never appends. `preflight.py` with `"kind": "image"` must PASS before any image call. **Right on the first render (§6A Part 2, V7.74.0 — user: "make the correct image with the first/second generation"):** eight rules decide what goes into that form, all checked by `preflight.py`: (1) every reference numbered with a role (`Image 1 is the product. Image 2 is the woman.`), copied with **fidelity** (`copied exactly — same shape, same parts, same markings, nothing redesigned`) and attached at **the shot's own angle**; (2) a **scale floor** — the beat's subject at least a quarter of the frame wide, said as a fraction beside the size anchor, else reframe closer or split wide + insert; (3) a shot that must match a plate or a confirmed earlier beat is an **image edit of that picture** (`match` + `edit_of` on the call, the prompt opening "Keep this photo exactly as it is… Add …"), never a new photo with the plate attached; (4) a **counted inventory** of the frame, closed positively, every visible hand and foot placed, positions counted in the space ("the 7th of 14 steps"); (5) **plain surfaces** — no lettering or logos but the product's wordmark; (6) **gaze** stated when the face shows; (7) the camera a viewpoint, never an object, and nothing named outside the frame but a body part; (8) the **read-back** before sending. Applies to every beat image prompt written from now on, Fix regenerations included; no confirmed render is redone.

**Script is spoken verbatim (§22U, locked).** The ElevenLabs text is the script's spoken lines word for word — never add, remove, change or re-order a word; never send the title, headings, links or visual notes. Only what the **Enhance** pass adds (§22U step 8 — ElevenLabs' published Enhance prompt, `references/eleven_enhance_prompt.md`, run by you since there is no API): audio tags, and emphasis as CAPITALS, "!" or ellipses — never an added "?", never a banned or non-voice tag. Extract with `scripts/script_lines.py`, enhance, lock with `tts_budget.py --script-lines` (a changed word, an added "?" or a banned tag = FAIL, not sent). A wrong-looking line is flagged, never fixed. Agent-written hooks are voiced separately, only after step-6 approval.

**VO pace and house cut (§22U steps 9–10a, E11A — pauses restored V7.65.0, user 2026-09-28: "the trim is too fast"; both run modes).** The finished VO runs at the inspo's rate and **never above 210 wpm** (per finished variant, hook + body): tag each paragraph `[slowly]` and each sentence end `[pause]` (tags only, verbatim still gated) and voice by API at `speed` 0.7–1.0 with `scripts/tts_api.py` (`eleven_v4`; the connector has no speed setting; `speed` on v4 unverified). **Trim by task (V7.67.0, user 2026-09-29): a VO task trims the VO; a talking-head task never trims the VO — the untrimmed take goes to HeyGen and only the talking heads are trimmed (`trim.py`, step 14), so a trim that reads too fast or too slow is redone on the render for free, never by a new HeyGen generation.** On a VO task the voice-over is trimmed with `scripts/vo_trim.py` in the house cut: **natural pauses kept — 0.45s at a sentence end, 0.20s at a comma, never longer than the take had** (the old 0.015s butt joins are retired), **no tight cuts (2026-09-28): every word finishes — kept to −50 dB, then 80 ms of release and a 60 ms fade, and a pause inside a phrase is never shortened** (never cut at a transcript word-end), breaths cut only at phrase boundaries, no speed change, pace gate ≤ 210 wpm (too fast → re-voice slower, never stretch). Hook parts are gated with their body; for one consistent voice, voice all hooks + body in one TTS request and split at the silences. A take whose last word the TTS cut off (ends above −45 dB) fails. Never on a §24I voice master. `trim.py` (E11) trims the talking heads, with the same no-tight-cuts rule (words padded 120/250 ms, air only below −50 dB, 0.45s / 0.25s / ≤ 0.3s pauses, 40 ms fade-out, ≤ 210 wpm). The Kling voice-clone source takes are trimmed in the **medium style** (`--style medium`: 0.25s / 0.15s / ≤ 0.15s) before ×1.2 and the loop to ≥ 30s.

**Manual: the user checks every generation (correction 2026-09-26; reaffirmed 2026-09-27 — "you will not check them").** No verdict, no instrument, no note on any render — images, clips, audio, colour, joins, contact sheets are all the user's. You still lint your own prompts and plans before spending (`preflight.py`, `angles.py`). **Automatic: you check everything and deliver the final videos only.** Never judge, confirm or regenerate a render on your own — put it on the board as To check and wait for the user's Confirm or Fix; regenerate only from their Fix note (no budget — except a third video generation of one shot, which waits for the user's go, §22X). The two verdicts below are for **Automatic runs only**.

**Image verdict (§22V, Automatic only). Open and judge every image yourself — the line first, then product, body, continuity, register, animatability — and ship `USE` or `REGENERATE · Q<n>: fault → fix`. Two regenerations per fault, then the user. Adapt to the named tool; else the most recently used one; ask only if none was ever named.

**Would the user fix it? (§22V Q7 / §22W Q8, V7.73.1, Automatic):** every image and clip is also checked against the House Taste and product fix patterns — a break is REGENERATE citing the rule; the A/B pick is the render that breaks none. Manual builds' Fix notes train these rules.

**Clip verdict (§22W, Automatic only).** Judge every video yourself from `scripts/contact_sheet.py` (true first + last frame, `--full` for zoom): the line, product in every frame, body in every frame, motion, continuity, technical, enough footage for its slot → `USE` or `REGENERATE`.

**B-roll length (E6, V7.60.6; amended 2026-09-26).** Every B-roll clip — mechanism and anatomy included — is as long as its time on screen (its cut to the next B-roll's cut, from the voice master's word timestamps) + its 0.4s skipped opening + 0.5s, rounded up, Kling 3–15s — run `assemble.py <plan> --lengths` before any B-roll call, so no clip has to be slowed. Never a fixed 5s/3s. The voice master comes before any B-roll call.

**Natural motion (§27G, 2026-09-26).** Most distortion is motion the model does badly, so ask for less: one action per clip at a countable pace, human motion 3–6s (longer lines → two clips), camera or subject moves never both, safe staging for stairs / turns / sitting / hands / walking at camera, start images caught mid-action, both ends pinned when the product changes angle, the product rigid in every frame, `prefer_multi_shots: false` on every Kling call. The rough cut is 24 fps (Kling's rate). The board gives the user an 8-frame strip, 0.5x and "Use only up to here" (`videoOut` → the plan's `out`). **It runs through every step, not only the board:** the act-map row carries `action`, `pace`, `camera`, `staging`, `pin_end`, `max` (E4); the start image is caught mid-action and a pinned beat gets an approved end image too (§22V Q6); the §35 prompt names one action with its pace and the rigid-product clause, and a moving subject takes a camera that sways but never travels (§22B); pinned beats use the first-and-last-frame call (E7); Fix regenerations of a video follow §27G.

**Beat videos right on one generation (§35A, §22X, §27G rules 9–10, V7.71.0 — "we will never do 2 generations, make it stronger").** (1) **Motion confirmed at the image:** write the beat's one-line `motionPlan` with its image prompt; the card shows it as **Video will show**, and picking the image confirms it — a motion note is a Fix on the image, before any video credit. (2) **Short video prompt, ≤ 1,000 characters:** `For the line "…":` → the confirmed action from this frame word for word (how much, how long, a countable pace, the end state) → the camera in one clause → 2–3 shot facts (same steps, hands clear, strap rigid) → ≤ 5 negatives; never the camera-drift / reframe / physics paragraphs. (3) **Stairs, travel, hand-on-product and product-angle shots are pinned** first-and-last frame (end frame picked with the start), and the build's **first clip of each class is a pilot** — the rest wait for its Confirm. (4) **"Fast" comes from the edit** — brisk countable pace, 3–4s, tight frame and cut — never "running / quickly / fast" in the prompt. (5) **Nobody mouths the line (V7.83.3, HT25):** every beat video prompt says `mouth closed, she never speaks or sings` / `nobody speaks` — the words belong to the VO or the song; a moving mouth on the line is a Fix. `preflight.py` checks all of it.

**Learn from my own mistakes — the Lessons log (§34B, V7.82.0, user 2026-10-01: "you should always learn from your mistake to improve the things").** When the user corrects, stops or undoes something I did, repeats a request, or I find my own error: stop or undo it first, find the cause, fix the rule that caused it at its source (conflicting rules made to agree; a script check where possible), write a row in `LESSONS.md` (repo root), and tell the user in one line. Read `LESSONS.md` before any system change and before publishing or writing to a board — the session-start hook prints the latest rules. A Fix about how the system works is a system change, never a one-build workaround (L04); a changed default updates everything that depends on it (L08).

**Learn from the board — the House Taste (§34A, V7.73.0, user: "learn what gets fixed so you know what we want").** After every Fix round (and on start/resume) dump the build's Current + Old boards and run `scripts/fix_patterns.py`; a note that repeats (two beats or two builds) becomes a rule — generic ones in the §34A House Taste table (HT01–HT16), product ones in `products/<product>/fix_patterns.md` (STRYDE: FP01–FP10) — written the same turn and listed to the user in one line. **Read both before every beat image or video prompt**; the §6A/§35A decisive facts come from them first, and the call lists them as `"taste": [...]` (`preflight.py` checks). HT01–HT24 (HT17–HT21 V7.74.0: match a plate by editing it · no readable text or logos · bare surfaces, a counted frame · face to the lens when asked · the subject fills the frame; HT22 V7.77.1: the place's geography fixed in every clip — direction, floor, which stairs and what they sit beside, set pieces that must stay still; a Seedance two-shot written from the plate's own side, the reverse a closer shot or its own plate (L17); V7.77.2: a machine that must not move kept out of frame by the angle, never held still by words; HT23 V7.78.1: one scene, one continuous moment — every shot of a hook or scene carries the same SCENE SO FAR block; HT24 V7.79.2: the line's relationship is the picture — everyone a line names as ahead, behind, beside or watching is in the one frame in that relation, from the side or behind, never a POV of one of them; a comparing hook line is one B-roll with all of them). The biggest ones: after-state lines are productive B-roll (real everyday tasks done easily, not only stairs) · problem lines show real struggle · after-state stairs: hands never on the rail, brisk, face visible · show the move in progress, never already done · hooks must sell (out in the world, stakes) · product at true size, never covered · wardrobe per day/event, same props across a day's beats · every beat matches its plate · one picture per idea.

**Film modes — motion and acting (§24K, §24I parts 9–12, 2026-09-27).** Modes 4 and 5 keep §27G: the F-rig is picked by what the subject does (F1/F4 only on a still subject; a walk is F2 across a locked frame; F5 only where the reference edit follows a walk, waist-up, 3–4 steps) and by the scene's emotion (camera plan per scene, tightest scale on the turn, a cut cue per shot); MULTI-SHOT only when nobody moves. Acting: the story spine read from the script (never rewriting it), a PLAYING verb per line, one piece of business per dialogue/listener shot (`BUSINESS-LINE`) carrying the subtext tell, size by shot scale, generated-acting tells banned (`NEG-DRAMA`). **Scene image list (§24H):** every scene lists, at step 5, every input it needs, counted and approved before any clip — **on Seedance (every Mode 4–5 clip) that is its ingredient list, no frames** (V7.68.0): the sheets, voice clips, plate(s), product references and info cards (a prop's state, the day's outfit, an insert object, where the product sits); the shot itself is written in the prose. Frame rows (master, start, chained, end, bridge) are only for a Kling/Wan shot in an adopting build. **State track (§24H):** per character per shot — eyes, face, hair, wardrobe state, hands, position, condition — carried until a shot shows its cause (no crying then dry-eyed at the next cut); `STATE-CARRY` on every frame and clip; frames in story order with the previous approved frame as state reference. Automatic: only the listed images, and a continuity fault never ships (E2 `SCENE_BREAK`). **No duplicate images:** every image-list row names what is new (position, scale or state) or is struck; a shot at the master's position is the master; push-ins ≤ 1.3× are edit punch-ins. **Voice emotion is tracked too (§24I part 13):** a VOICE row on the state track, carried across cuts, matching the face, written as `VOICE NOW` in `DRAMA-DELIVERY`.

**Camera angle range (§30I, 2026-09-27, all modes).** Every B-roll and film row names its angle — height (ground · low · eye · high · overhead), side (front · three-quarter · profile · three-quarter-back · behind · OTS), foreground (clean · through · reflection) — with a reason from the meaning table (high = small/overwhelmed, low = resolve, overhead = routine/hands, ground = steps/feet, profile = distance, through = watched). `scripts/angles.py` must pass before the act map is approved: no jump cuts, no angle three in a row, ≥ 3 setups in any five shots, eye-level frontal ≤ a third, not all one height. `ANGLE-LINE` in every T2I; the inspo's angle range wins; faces, motion, product, Mode 1 phone plausibility and the film axis limit it. **Film shot library (§24K part 7, 2026-09-28, Modes 4–5):** every film row also names its `shot` from the 34 film shots (`SH-WIDE`, `SH-MED`, `SH-CU`, `SH-MACRO`, `SH-OVFISH`, `SH-PROFILE`, `SH-34`, `SH-REAR`, `SH-OTS`, `SH-POV`, `SH-PRISM`, `SH-EYE`, `SH-LOW`, `SH-HIGH`, `SH-DUTCH`, `SH-OVER`, `SH-AERIAL`, `SH-GROUND`, `SH-WORM`, `SH-HOLE`, `SH-HOOP`, `SH-WACU`, `SH-FISH`, `SH-FISHCU`, `SH-HICU`, `SH-LOCU`, `SH-SELFIE`, `SH-SIL`, `SH-OCCL`, `SH-FGFOC`, `SH-BGFOC`, `SH-FLARE`, `SH-MAGNIFY`, `SH-INSIDE`) with a `why`, asked for by `SHOT-LINE` after `CAM-FILM`/`CAM-ANIM`. Signature shots (fisheyes, wide-angle CU, prism, Dutch, aerial, worm's-eye, inside a hole, hoop-level, selfie, flare, magnifier, inside-the-fridge) ≤ 1 per scene, never two in a row, ≤ 1 in 5 across the film; wide-angle/fisheye CU never on a face; no distorting shot on a product beat; `angles.py` SHOT checks it.

**Anatomy styles and angles — a range, never one look (§12A-1, V7.81.0, user 2026-10-01: "you always use the same style… and the camera angles for the anatomy and mechanism too").** Every anatomy or mechanism beat names its **style**, picked for its line — **S1 Glass body** (sensations, relief), **S2 X-ray** (wear, the scan, the doctor), **S3 Clinical studio model** (what and where a structure is), **S4 On-body window** ("your knee", the product working in daily life), **S5 Physical model** (tactile, where it sits — a Mode 1 capture, Sunburst), **S6 Scan** (numbers, studies), **S7 Cross-section** (deep, under, layers) — opening its prompt with that style's `ANAT-STYLE-S<n>` line; 3–5 anatomy beats use ≥ 2 styles, 6+ use ≥ 3, none on over half, never three in a row. **The camera ranges too:** `ANAT-BASE` (now S1's world only) takes `[ANAT-ANGLE]` — front-on, low three-quarter, true lateral, from behind, high three-quarter, top-down, worm's-eye, macro on `[SITE]`, wide limb — and the move varies (orbit left/right, push-in, pull-back, rise, tilt, locked); no repeated look back to back, ≥ 3 angles in any four anatomy beats, the old low three-quarter on at most a third. The body side, `[SITE]`, colour language and product placement never change across styles; a matched problem → relief pair (`pair_of`) stays matched. `angles.py` ANAT checks the anatomy rows as their own run; `preflight.py` needs `anat_style` on every anatomy image call.

**Camera focus (§30J, 2026-09-27, all modes).** Every B-roll and film row names its focus — plane (nearest eye · hands · product · foreground · background · deep), depth and any focus change. Always sharp: the nearest eye on a face, the product on a product beat, the hands on a hands beat. Phones deep (shallow only within ~30cm); film shallow from CU in; never shallow on WIDE/FULL or on more than two thirds of a group. A focus change is one per clip, on a named cue, with a still subject and camera — a clean pull in Modes 4–5, a tap to focus in Mode 1 (clean rack stays banned). `FOCUS-LINE` after `ANGLE-LINE`; `angles.py` and `preflight.py` check it.

**Lighting (§30K, 2026-09-27, all modes).** Each location gets a light plan in room terms (windows, practicals, sun path, key by time); each shot's on-screen key side is derived from the camera position, so varied angles keep the window where it is. Faces: window 30–60° off the camera axis, never flat frontal, backlight only with a reason; one light state per scene, time only forward, no light change inside a clip without a cause; a light arc by act inside the mode's register (Mode 1 stays daylight, never moody); eyes catch light, no glowing skin, product highlight clean. `LIGHT-SHOT` (Modes 1–3) or `LIGHT-FILM`/`LIGHT-ANIM` `[SIDE]` from the plan; `NEG-LIGHT` / `NEG-LIGHT-C`; checked by `angles.py` and `light_check.py`.

**Film camera package (§24G, 2026-09-27).** Modes 4–5 name a real US-feature package from the §24G library by genre — e.g. ARRI Alexa 35 / Mini LF + Cooke S4/i or ARRI Signature (drama, default), Sony Venice 2 + Zeiss Master Prime (tension), 35mm Kodak Vision3 + Panavision Primo (period), Alexa 65 + Panavision anamorphic (epic) — one per film, with focal and stop by shot scale, 24fps and a 180-degree shutter (`CAM-FILM`; Mode 5 emulates it virtually in `CAM-ANIM`). `PROD-DEPTH` on every film frame: foreground layer, dressed lived-in set, costume texture, blocking in depth. Focal, stop and shutter numbers are unverified on the generators (Open Decisions) — the package names do most of the work. Finish in post on the locked cut only: match → LUT → grain, exported at native 720×1280 — no upscale, no paid upscaler — all in the edit (§40). Generation stays 720p — confirmed by the user: films are watched on phones. A frame that reads as TV is a reroll.

**Series look & Seedance camera (§24N, V7.69.0 — user: "the Netflix live-action style").** Every Seedance **film** clip (Mode 4 / AI Drama, its hooks included) is shot as a **high-end streaming live-action drama series** — **ads stay phone style** (V7.69.1: a Seedance hook in a Mode 1–3 ad keeps the ad's iPhone register, R-rigs and angles, never `SERIES-LOOK` or F6–F10): `SERIES-LOOK` after `ING-MANIFEST` (never names a streamer, series or studio, §10A), the §24G *Prestige streaming series* package (Alexa 35 / Mini LF · Venice 2 · V-Raptor, spherical primes), motivated low-key light (4:1–8:1 on faces, practicals in frame, deep shadows with detail), shallow from MCU in, 24 fps / 180°; the build's look is derived inside it. **Move library on Seedance:** F1 push-in, F2 locked, F3 float, F4 slider, F5 follow, **F6 pull-back reveal, F7 arc ≤ 30°, F8 crane (vertical), F9 lateral track beside a walk in profile (4–6 steps), F10 dolly zoom (≤ 1 per film)** — one move per shot, with distance and speed; camera and subject both travel only on F5/F9; whip pans and ramps are edit devices. **Coverage:** establish → dirty OTS pair → clean singles at matched scale and lens height, tightening to CU on the turn → reactions → inserts; lens height carries status (below the eyeline of power, above the one losing it); short-siding, lead room, frame-in-frame in 9:16. **A hook is a cold open:** mid-action, tight or one striking wide, one move underway, a line or sound inside the first second, 1.5–3s shots escalating to the hook line. Prompt order: `ING-MANIFEST` → `SERIES-LOOK` → `CAM-FILM` → `SHOT-LINE` → `ANGLE-LINE` → `FOCUS-LINE` → `LIGHT-FILM` → rig → action/performance → `INHERIT-FILM` → negatives. `preflight.py` and `angles.py` check it.

**Colour — grade in the edit, scenes locked (§40, §30L, 2026-09-27, all modes).** The grade never enters a prompt: images and clips are made in natural, neutral colour, and the edit (CapCut block, step 8) does match to the scene master → the one LUT (Modes 4–5; Modes 1–3 match only, never a LUT) → grain (Mode 4) → native export. **The LUT is a real file (2026-09-28):** Look Sheet field 5 written as numbers (`grade.json`) → `lut.py make` → `LUT-[BUILD].cube`, passing `lut.py check` (skin hue ≤ 8°, skin saturation ±25%, no tone inversion), previewed ungraded | graded on the master; Manual imports it in CapCut, Automatic runs `lut.py apply --mode 4|5 [--grain]` — the same file both ways. **White balance is pinned (2026-09-28):** each scene's white balance is its key's Kelvin from the light plan (daylight 5600K, overcast 6500K, tungsten 2700–3200K…), in `COLOUR-KEY` (`[KELVIN]K, and the camera is white-balanced for it`) and the row's `light.kelvin`; it changes only at a scene boundary. **Strict:** every scene has a `COLOUR-KEY` read off its master (light colour, set, wardrobe, accent, in-camera saturation), verbatim on every shot; the master is the colour reference; Automatic: `light_check.py colour --ref <master>` on frames before video, on clips, and on the graded clips in the edit — a shot off its scene's colours is never animated or cut in. Manual: the user checks colour on the board. Colour changes only at a scene boundary.

**No trimming in the film modes (§24L, 2026-09-27).** Modes 4–5, AI Drama included: no E11 trim, no E11A house cut (narration used as generated), no cut inside a take, no speed change, no silences cut in the edit, no "Use only up to here" — a fault is regenerated (§22X). Editing is only the cut between whole shots at their designed cut cue. `trim.py` / `vo_trim.py --mode 4|5` refuse; `assemble.py` never changes speed on a Mode 4/5 plan.

**Film sound (§24M, V7.64.1).** Film clips carry dialogue only (`NEG-SOUND`), cleaned by the ElevenLabs Voice Isolator; voice masters untouched. **No BGM in any Seedance generation (V7.73.3, user 2026-09-30 — the music goes in in the edit):** `NEG-SOUND` on every Seedance call, nothing in the prompt asks for music (no score, song, "music swells"), a clip with no dialogue is generated silent (`generate_audio: false`, `kie.py seedance --no-audio`), audio references are voice only — `preflight.py` fails any of them. One music theme per film (Look Sheet field 9), varied by story part (sparse in the Problem, the theme at the Turn, full in the After). Per scene: one music cue continuous across all its clips (`MUSIC-CUE`, `eleven_music_v2`, instrumental, scene length + 2s), one looping room tone per location (`ROOM-TONE`), a film-wide SFX list — one sound per object (`SFX-LINE`, `eleven_text_to_sound_v2`) — one generation per call. `mix_scene.py` mixes each scene (music ducked under dialogue, −14 LUFS). **Music is composed to the scene (V7.64.2):** the cue is sections on the scene's cut cues and turn, each with an energy; `music.py plan` (free) → `music.py compose` (one track) → **`music.py check` — you listen to every track you compose, in both run modes** (the one Manual exception, at the user's word): length, section loudness order, a truly silent turn, no dropouts, splices or vocals, tempo band. Two tracks per scene at most. Commercial use confirmed. Manual: on the board's Edit stage for the user; Automatic: mixed and delivered.

**Music follows the script (§40A, V7.75.0, user 2026-09-30 — "a generic cute music wouldn't align with this kind of messaging").** Every build, all modes, both run modes: at step 5 a **Music Register Map** gives each script part its register from its own lines — `MUS-OPEN` for the hook and the first 30–60 s (the viewer is being educated and unsettled: investigative-documentary suspense, curiosity and intrigue — low drone, slow pulse, sparse piano or low strings, soft ticking, minor or modal, unresolved, no tune), `MUS-EXPOSE` (problem, darker), `MUS-EDU` (mechanism, inquisitive), `MUS-TURN` (the release), `MUS-AFTER` (warm, hopeful, never cute), `MUS-OFFER` (confident, resolved). **Generic cute, cheerful, upbeat, corporate or stock-advert music is banned wherever the script educates, warns, exposes or questions** (`NEG-MUSIC`). **Investigation until the product, the change on the product (V7.78.0, user 2026-10-01):** everything before the product's first frame is investigation — suspense, curiosity — **never sad** (no mournful piano, lament, weeping strings; `NEG-SAD`), and the music changes on the product's first frame (±0.25 s, `MUS-TURN` starts there): `product_at` and per-section `register` on the cue, and `music.py plan` refuses a plan that misses it or goes sad before it. The reference ad decides where music sits, never its register. One music family per build; hook variants share the body's cues. Cues as `MUSIC-CUE` (all modes), on the Build Sheet (item 5c) and the board's Plan tab; supplied by the team as CapCut lines with the §24M levels, or generated with `music.py plan --register <ID>` → `compose` → `check` (you listen, both run modes) and put on the board To check. E4 rows carry `music`.

**Never name what you don't want in the picture (V7.83.2, LESSONS L13).** Outside its NEGATIVES a film prompt never names a microphone, boom or windshield — `AUD-FILM` reads "clean, close production dialogue sound" — because the video model draws what it reads; `preflight.py` `MIC_PRIME` fails it.

**Video preflight (§22X, 2026-09-27, both run modes).** No paid video call — Seedance above all — is sent before it passes: the frame approved — on Seedance, every ingredient approved (Manual: the user's Confirm), the frame ready to move (Automatic: mid-action, room for the motion, hands whole or out, mouth clear on a speaking shot, product unambiguous, state track matched; Manual: the user's Confirm covers it — you do not look), `scripts/preflight.py <call.json>` PASS, and three named risks each prevented. **Two generations per shot at most:** the second only after the fault is diagnosed and fixed at its source (frame, prompt or motion) — never the same prompt resent; no third without the user. The master is the source of every close-up (a render against it, never a crop beyond 1.3×), so it is locked only when faces, worn details, props and product all read in it.

**Script visual instructions are binding (§27F, V7.61.0).** Every visual note on the script (`VISUAL:`, `B-ROLL:`, `ON SCREEN:`, `SFX:`, `[brackets]`, `(parentheses)`, inline `[notes]`, the visual column of a VO | VISUAL table…) is kept out of the voice but **never dropped**: `script_lines.py --visual` lists them (`VN01`…) anchored to their spoken line, and they open the **Visual Instruction Ledger** at step 2. Step 5 assigns each row to the beat that shows it or the CapCut line that carries it (on-screen text verbatim). Follow it as written, don't substitute your own shot; a row that breaks a higher layer is flagged with the nearest compliant execution. §22V/§22W Q1 check it. Every row ends `verified` or `flagged` — none open at step 8.

**Loom brief (§18C, V7.61.0).** Optional — no Loom, no question. The `LOOM:` link comes beside `DRIVE:`. Run `scripts/fetch_loom.py <BUILD> <link>` (download, timestamped transcript, frames every 5s and at cuts → `loom.md`), read it and the frames, and log each instruction in the ledger as `LMxx`. It never changes a spoken word or overrides a higher layer. Loom vs a written note on the same line: Manual asks; Automatic follows the Loom and flags it. Private Loom → ask for the MP4 in the Drive folder (named `loom`; `fetch_drive.py` sorts it as the Loom, never as an inspo).

**Edit grammar (§42 Part 3A, V7.63.0, both run modes).** Copy how the inspo edits, not just how often it cuts. Read `fetch_inspo.py`'s shot frames and per-second contact sheets (a split-screen or PiP appearing over a held shot is not a scene cut) and log every device as `EGxx`: B-roll layout (`full` · `split` band + ratio · `pip` box, which is inside, corner, size · `cutout` · `card`), punch-ins, transitions, speed ramps, caption style, text overlays, SFX. Compile `EDIT-[BUILD]` (style axis — wins over house defaults, never over compliance) — **except two house limits the reference never overrides (V7.65.0, user 2026-09-28): B-roll is full screen by default, `split`/`pip` on at most one B-roll in five per finished video and never two in a row, on lines where the face adds something; and every B-roll holds (below).** Step 5: every B-roll row gets its `layout` by the reference's own rule; §35: frame non-full B-roll for its crop; `assemble.py` renders `full`/`split`/`pip`/punch-ins; everything else is a CapCut line with its `EG` ID.

**B-roll on the right line (§30H rules 0, 1, 6 — V7.79.0, user 2026-10-01: "I want it perfectly timed").** Cuts are timed on the **final** track — with talking heads `"audio": "base"`, the trimmed take; a master that doesn't match the talking-head track fails MASTER_MISMATCH; re-run `--lengths` after any trim. **Each B-roll cuts 6 frames before its phrase's first word** — the picture changes as its line starts; the `key` now sets the in-point (the `peak` lands on it), never the cut. **No word is spoken under another line's picture** (LINE_UNDER_WRONG_PICTURE names the row to restart at its line's first word or the line that needs its own row; `"span": "hold"` to hold on purpose). A hold never runs into the next line; a line never starts inside the previous word. **Placement comes first (V7.80.0, user 2026-10-01 — "most important is the broll placement"):** words timed with `medium.en` (never `base.en`, up to 0.7 s off) and each word ending where its sound stops; **with a talking head a B-roll leaves as its sentence ends** ("the brolls stay even though the script line is done") — it runs on only over silence, never over the next words for length (the ~3 s hold is retired); a line under 2.0 s fails FLASH and the report names the merge; `--lengths --sheet` writes the **placement sheet** (in, out, the sentence each B-roll shows) to the Plan tab as `docs/placement` before any B-roll call, and every rough cut rewrites it.

**The Visual Pitch — the strongest picture for every line (§30M, V7.85.0, user 2026-10-01: "improve the planning on the act / scenes / hooks — I need more strong visuals that can show the best ones").** Every picture is chosen, not taken: each B-roll row gets **three candidates on three routes** (STAKES · PROOF · CONTRAST · DETAIL · REACTION · WORLD · SYMBOL · MECHANISM · PRODUCT · POV · LITERAL — the noun itself, the weakest), each scored 0–2 on **stop · line · feel · specific · fresh · makeable**; the top one is used (≥ 9/12) and the other two kept as "also considered". Every act or scene has one idea and **one hero shot** (≥ 10/12); an act of 4+ uses ≥ 3 routes, LITERAL ≤ 30%, STAKES in problem acts, PROOF / PRODUCT in after acts. **Every hook gets five cold-open concepts** (first frame · stakes · where · turn), the pick ≥ 10/12 with STOP 2. `visual_plan.py` must pass before the act map is approved; `--md` goes on the Plan tab as `docs/visualplan` (Manual: the user can swap a pick by name or letter).

**B-roll by phrase, never whole sentences (§27, §30H rule 7, V7.84.0 — user: "you have been picking long sentences instead of what we used back then").** Every act-map row is one phrase — about 2–3 s, 4–8 words, cut at its shift (a comma, "and / but / because / so", a new noun or turn). `assemble.py` fails **LONG** over 3.5 s and names the split; a phrase under 2.0 s joins its neighbouring phrase, never the whole sentence; `"whole": "<why>"` only when nothing changes inside the row; mechanism / anatomy rows are exempt.

**Placement & no holes (§30H). B-roll cuts in 6 frames (0.25s) before its anchor word's onset in the audio — the act-map row's `key` word the picture shows, else the phrase's first word (script-aligned, then snapped to where the voice actually starts: Whisper runs late) — **never after its word** (V7.69.2, "always late": a clip that would be squeezed under 2.0s fails FLASH and the rows merge; `LATE` fails) — and plays from its in-point, never its static first frame (0.4s skip, or its `peak` on the key word); flickers and holes give back the skip before extending or slowing; joins are frame-exact; no talking-head flicker under 1.5s between B-rolls; voice-only builds have no uncovered frame; **every B-roll is on screen at least 2.0s and never leaves a face window under 1.5s** (V7.65.0 — "the brolls are too fast"; merge two short lines into one picture), **and with a talking head it leaves as its sentence ends** (V7.80.0 — the ~3 s hold over the next words is retired); `LAYOUT_MIX` fails over 1 in 5 boxed or two boxed in a row. `scripts/assemble.py` places, fixes, renders and verifies the rough cut; CapCut finishes it.

**Hook variants (§30H).** The output is **one finished video per hook**: HK1 + body, HK2 + body, HK3 + body — three when you write the hooks, else as many as the script has. Each hook voiced separately, the body voiced once and reused. `scripts/variants.py` builds every variant as one timeline (no holes across the seam), keeps the body's cuts identical in every variant, and checks each duration = hook + body.

**Intake (§18B). Default: a **shared Google Drive folder** (inspo video, script with the title on line 1, Product Sheet, product images) plus one short message — `DRIVE`, `LOOM` (optional, §18C), `BUILD`, `MODE`, `RUN`, and optionally `VOICE` (→ narrator's `VOICE-[CHAR]`), `HOOKS` (count, default 3), `CAP` (credit cap — never ask then), `ADJUST` (free overrides: apply and record in the Build Sheet; flag any that conflict with a higher authority layer), `DIRECTIONS` (optional free-form creative direction). **The user sets `MODE` (and optional `DIRECTIONS`); you write the Film Look Sheet yourself for Modes 4–5 — camera package, light, palette, grade for the edit — never asking** (2026-09-27). Run `scripts/fetch_drive.py <BUILD> <link>`, report what was found or missing, then absorb. **`RUN: MANUAL` (or blank) is a full intake too (§18B, V7.62.0):** you fetch and absorb steps 1–2 exactly as in Automatic (Absorption Sheet, Product Sheet, claims, phrase inventory, Visual Instruction Ledger, Mode & Model Lock), then **generate the avatars yourself** (step 3: §19 sheets on the §5 image route, on the board as To check — you do not check them), ship steps 1–3 and **stop — the avatars are the user's decision**. On the go: steps 4–5 — you generate the plates through the connectors, check them, and the build continues in Manual with you generating everything and the user deciding at the gates. Alternative: the single-message Intake Pack (`builds/INTAKE_TEMPLATE.md`): BUILD, MODE, FORMAT, RUN, TOOLS, INSPO links, SCRIPT (title first), PRODUCT, CAST NOTES, NOTES. Fetch and measure every link, run steps 1–2 without questions (Manual: generate the avatars, stop for the user's decision, then 4–5; Automatic: 1–5 in one pass), then the voice route by mode: Mode 1–3 → §22U (HeyGen when there are talking heads); **Mode 4, 5, AI Drama → §24I neutral Seedance voice master, audio kept exactly as generated — never trimmed, sped or looped.** `RUN: AUTOMATION` is the Automatic call; anything else is Manual.

**Build order (§18).** Eight steps: 1 absorb inspo (§42) → 2 absorb script/product + Mode & Model Lock → 3 cast → 4 property & location maps → 5 act map + wardrobe map → **voices (§22U, after the maps, both run modes)** → 6 hooks one by one → 7 B-roll and body acts → 8 CapCut block. **Manual has two human gates: the avatars after step 3 (agent-generated, user-decided) and the hooks at step 6** (V7.62.0); steps 1–3 ship as one delivery, then 4–5. Automatic has no gates — E0.

**Output layout (§16, §16A).** Every prompt in its own block; never clump; never blend prompt text with explanation. Each shipped prompt carries its model string, aspect ratio, resolution/duration and character count. Editor/strategy notes sit outside the prompt block.

**Corrections (§34).** Return only the corrected block, labelled by beat ID, as a drop-in swap; confirm in one line; stop. Corrections are global (fix every beat with the same flaw and list the IDs), retroactive (name invalidated IDs), and permanent. A locked correction goes into the **Pending Amendments** table of the master file the same turn.

**Tone (§45).** Direct, practical, efficient. Take a position — recommend one option and say why. Measure before asserting; mark unverified claims **unverified**. Show the number (char counts, word budgets, coverage). Confirm correctness in one line and move on.

**Generation Board (§16A, E3; design locked 2026-09-26).** The template's design is locked: never redesign, restyle or simplify it; change it only on the user's named request, in the template — **for new boards only; an existing board is republished only on its team's ask** (V7.82.0, LESSONS L05). Every generation, both run modes, is logged on the build's own board (template `dashboard/generation_board.html`; board links live in `CLAUDE.md` and the Build Sheet): grouped per act — Hook 1…, Act 1… — Images then Videos, every field labelled, each render uploaded the turn it lands, the §22V / §22W verdict recorded. The reviewer presses Confirm or Fix; a Fix note is a §34 correction for that beat, regenerated within the §22V budget and picked up by the hourly check. **Always shown, both run modes (2026-09-27):** open the build's board in the user's panel (Artifact `open`) when a run starts or resumes and at every delivery — Automatic too. **Final output tab (2026-09-27):** beside Board, Manual run and Plan; each finished video goes on the board the turn it is exported as an Edit-stage card with `final: true` (beat `FINAL-HK<n>`, `hook`, `madeFrom`; the film: `FINAL`) — Manual: To check for the final review; Automatic: confirmed, the delivered videos. **This build's credits on the Final output (V7.83.0–V7.83.1, user 2026-10-01 — "on that task and not as a whole"):** a Credits spent on this build panel — one row per connector, every render on this build's boards counted once, never the account's total or balance — from `buildSpend` on the build doc, which I write after every batch with `build_spend.py` over every board's dump. **Long titles wrap (V7.81.0, user 2026-10-01):** the viewer's title wraps in a fixed width and never pushes the details panel off screen; tile titles wrap up to three lines. **Old versions → main board (V7.79.1, user 2026-10-01):** the Old board's viewer has "Use this — move it to the main board as the confirmed one"; it leaves a `restore` request, and every Fix check copies that render back to the Current board, makes it the current version, confirms it and moves the replaced one to Old (CLAUDE.md has the steps). **Four boards per build (2026-09-28, storage):** Current (confirmed + to check), Old versions (every replaced or unchosen render, read-only, moved the turn a Fix replaces it), Final output, Plan — one template, `BOARD_ROLE` per copy, linked through `boards` on the build doc (CLAUDE.md has the procedure). **Confirmed B-rolls are never deleted (2026-09-28):** every confirmed hook and B-roll video stays on its board at full quality — only replaced or unchosen versions ever leave Current; **Download all B-rolls** (Board tab's B-roll card and Manual run) and **Download all hooks** (Hooks card) zips them all (folder per act, `broll_bank.md`) for the B-roll bank. **Seedance beats (2026-09-29):** a Seedance video shows its **ingredients** — every reference image it is made from — then the video, never one start image: `ingredients` on the video card (`ref` = the cast / location / frame card used, or its own `asset`), an Ingredients box before the Videos box, an Ingredients tab in the viewer; the video unlocks when every ingredient is confirmed. Ingredients carry `kind` (character · voice · location · product · info) and an info card's fact in `note` — never frames (V7.68.0). Every image lists its reference images (`imageRefs`), and Seedance hooks, talking heads and VO/voice audio show theirs too. **Groups and labels (2026-09-29):** a group per hook and per body (`body: <n>` on B-roll cards when there is more than one body), plain-word labels (Image ready to check, Video generating…), a Back button in the viewer. **A/B image pairs (2026-09-29):** a pair card shows A and B side by side with Use A / Use B / Both wrong · Fix (`imagePair`, `imagePick`, `imageUnused`, `pair` on each version). **Films (2026-09-29):** shot cards carry `scene: <n>`; Manual run and the Board tab go Scene 1 (images → ingredients → clips), Scene 2… — each scene its own section

## Voice pipeline helpers (§22U, both modes)

- `scripts/voice_source.py` — steps 3–5 on two or more Kling takes: trim each (medium style) → ×1.2 → same-voice gate (pitch median ±10%) → join in order → loop to ≥30s → `<Keyword>_clone_source.mp3`
- `scripts/script_lines.py` — §22U step 8: spoken lines only, verbatim; reports every dropped line (title, headings, links, visual notes); `--visual` writes the §27F ledger's `VNxx` rows; reads `.docx` tables (two-column VO | VISUAL scripts) and cuts speaker labels (`VO:`, `SARAH:`) — never voiced
- `scripts/tts_budget.py` — verbatim lock with `--script-lines` (Enhance emphasis passes and is listed; an added "?" fails); steps 8–9: counts the enhanced script, runs the 10,000-character `eleven_v4` ladder, lists tags outside the library, fails banned / non-voice tags
- `scripts/assemble.py` — §30H: place B-roll on its lines (6 frames before the line's first word, never after it; out as its sentence ends with a talking head; `medium.en` timings, word ends from the sound), close flickers and holes, render + verify the rough cut; `--sheet` writes the placement sheet (`docs/placement`); per-B-roll `layout` (`full`, `split`, `pip`) and `punch_in` from `EDIT-[BUILD]`
- `scripts/variants.py` — §30H hook variants: `<BUILD>_HK1.mp4` … each hook + the identical body, set-checked
- `scripts/angles.py` — §30I/§30J/§24K part 7/§12A-1: checks an act map / shot list for stuck angles (JUMP, RUN, WINDOW, DEFAULT, HEIGHT, WHY), the anatomy rows' style, angle and move range (ANAT), the film shot library (SHOT) and focus (FOCUS) and light rows (LIGHT); must pass before the act map is approved
- `scripts/lut.py` — §40/§24G field 5: `make` (grade.json → `LUT-[BUILD].cube`), `check` (skin, neutrals, range), `preview` (ungraded | graded), `apply` (ffmpeg lut3d, `--mode 4|5`, `--grain` Mode 4 only; refuses Modes 1–3)
- `scripts/light_check.py` — §30K/§30L: `colour --ref <master> <frames|clips>` holds every shot of a scene to the master's warmth, tint, saturation and brightness (strict); `scene <frames>` compares a scene's frames' brightness, warmth and brighter half (a relit shot flags); `clip <clip>` flags flicker and drift (thresholds unverified)
- `scripts/music.py` — §24M/§40A: `plan` (free composition plan from the cue's sections; `--register MUS-OPEN…` pre-fills the §40A register's theme and tempo, adds `NEG-MUSIC`, and refuses cute / upbeat words on a tense register), `compose` (one ElevenLabs track), `check` (the agent's listening pass against the plan); for a Music Video (§3C) `cuts` (beat grid → every row's cut, time on screen and call length) and `render` (the rough cut on the track); `"sung": true` with section `lines` for a sung track, `"bpm"` to pin the tempo
- `scripts/mix_scene.py` — §24M: mixes a film scene — isolated dialogue, looping room tone, one continuous music cue ducked under dialogue, SFX on their frames, −14 LUFS; checks the mix matches the picture length
- `scripts/visual_plan.py` — §30M (V7.85.0): the Visual Pitch check — three candidates per row on three routes, scored /12, the pick the top and ≥ 9 (hooks five concepts, ≥ 10, STOP 2), no stock wording, the act mix and one hero shot per act; `--md` writes `docs/visualplan`
- `scripts/build_spend.py` — §16A (V7.83.0–V7.83.1): this build's credits per connector (`--build` required) from every board's `generations` dump (a version on both Current and Old counted once) → `buildSpend` for the build doc; the Final output shows it
- `scripts/fix_patterns.py` — §34A: harvests every user Fix note from board dumps (Current + Old), by build, beat, step and model, with a rough class — the input for the House Taste and the product's `fix_patterns.md`
- `scripts/preflight.py` — §22X: lints a video call (and, with `"kind": "image"`, a §6A beat image prompt: ≤ 1,200 chars, the line in it, ≤ 5 negatives, no face/plate block the shot doesn't show, product first with a size anchor, the A/B pair routed by §18A (realistic two Sunburst, anatomy/stylised two NB Pro), and the §6A Part 2 first-render checks (V7.74.0): every ref named `Image n`, a fidelity clause and a frame fraction on a product beat, `match` → `edit_of` + an edit opening + the plate/frame as Image 1, hands placed on a body shot, gaze on a face shot, bare surfaces when a table/desk/counter/shelf/floor is named, a no-lettering clause, no device named as an object, nothing out of frame but a body part; for a Kling B-roll/hook clip the §35A form: ≤ 1,000 chars, line + confirmed `motion_plan` in it, ≤ 5 negatives, no retired boilerplate, risky classes pinned and piloted, no fast words on stairs/travel) (`call.json`) before any credit is spent — required strings, slots, rig vs subject motion, verbatim dialogue and word budget, connector params, generation ≤ 2 with a `fix_note` (a third or later only with the user's go recorded as `user_go`), three prevented risks; any FAIL = not sent
- `scripts/contact_sheet.py` — §22W: one image per clip (first → last frame), frozen/black runs, `--full` for zoom
- `scripts/trim.py` — E11 trim pass for talking heads, both run modes (§22U step 14) — the only trim on a talking-head task, run on the HeyGen render (the VO is never trimmed first); `--style natural` (default) · `medium` (voice-clone source) · `tight`; reports `wpm`, gates ≤ 210; **natural pace, never too fast, no tight cuts**: keeps 0.45s after sentences, 0.25s after commas, ≤ 0.3s inside a phrase (`--sentence-pause`, `--comma-pause`, `--word-pause`); words padded 120/250 ms (`--pre`, `--post`), air only below −50 dB, 40 ms fade-out on every cut; never on a §24I film voice master
- `scripts/tts_api.py` — §22U step 9 by API: Eleven v4 with `speed` 0.7–1.0 (pace control the connector lacks), one call per take, reports wpm per take
- `scripts/vo_trim.py` — VO trim for audio-only §22U masters/hooks, **VO tasks only (never on a talking-head task's take)**, in the **house cut** (V7.65.0): natural pauses (0.45s sentence, 0.20s comma, mid-phrase as voiced), words ring out to −50 dB + 80 ms with a 60 ms fade, pace gate ≤ 210 wpm (`--max-wpm`), inhales cut at phrase boundaries (`--script` lines); hook variants = raw hook + raw body trimmed in one pass; flags a take whose last word the TTS cut off
- `scripts/kie.py` — Kie AI API (§5): `credit`, `upload` (public URL), `image` (fallback), `kling` (Kling 3.0 fallback when Kling is short or over its cap), `seedance` (720p, 9:16, ingredients, stated duration), `wait`
- `scripts/cut_points.py` — §22U step 12: the HK1|HK2|HK3|BODY boundaries in one take (untrimmed on a talking-head task) (word timestamps, mid-gap), for cutting the one-go talking head into each hook + body
- `scripts/fetch_drive.py` — §18B Drive intake: downloads the shared folder, sorts inspo / script / product sheet / images, extracts document text, measures the inspo
- `scripts/fetch_loom.py` — §18C: downloads the Loom brief, transcribes it with timestamps, saves frames → `builds/<BUILD>/intake/loom/loom.md` (`LMxx` rows)
- `scripts/fetch_inspo.py` — §18B/§42 Part 1: downloads INSPO links into `builds/<BUILD>/intake/` and measures duration, aspect, shots, cuts, silences; saves two frames per shot and per-second contact sheets for the Edit Grammar (§42 Part 3A). YouTube returns 403 from the cloud — ask for the file instead
- `references/eleven_enhance_prompt.md` — ElevenLabs' Enhance prompt, verbatim (§22U step 8)
- `references/eleven_v3_tags.json` — the full Eleven v3 tag library (1,806 tags, read by v4 too); `TAG-PALETTE` in §22U is the fallback subset

Setup per session: `pip install -q imageio-ffmpeg faster-whisper numpy yt-dlp gdown python-docx pypdf cffi`. Both run modes use them on the renders you generate (Manual included, correction 2026-09-26).

## Changing the standards (§0, §34)

- **State the change before making it**: name the proposed change and every section it affects. No silent edits.
- Edit `standards/AI_Prompt_Engineer_Global_Standards.md` — it is the source.
- **A system update never touches existing builds** (user, 2026-09-28): new rules apply to new work; another build is re-cut or re-rendered only on its team's explicit ask.
- **Merge every update into the default branch the same turn** (PR, then merge) so every account and session gets it (user, 2026-09-28); a push to a session branch alone is not done.
- Bump the version line at the top and add a CHANGELOG entry when cutting a version; empty Pending Amendments at each cut.
- **Both copies move together.** If a change touches anything summarised above (role, authority order, modes, formats, tools, build order, layout, corrections, tone), update this SKILL.md in the same commit so the loader never drifts from the master.
- Product- or character-specific content never goes in the standards — it goes in a Product Sheet or Build Sheet.

## Section index

Grep for `^## <number>\.` (or the Appendix heading) to jump to any of these.

**BLOCK 1 — FOUNDATIONS**
- 1. Role
- 2. Mode Selection Rules
- 3. Format Selection
- 3B. AI Drama VSL *(new V7.55.1 — on explicit instruction)*
- 3C. Music Video — the music replaces the voice *(new V7.76.0 — on explicit instruction)*
- 4. Tools Supported
- 5. Platform & Execution Layer
- 6. T2I / I2V Discipline
- 6A. Beat Image Prompt — short, single-minded and right on the first render *(new V7.70.0; Part 2 first-render rules V7.74.0)*
- 7. Reference Image Rule

**BLOCK 2 — PRODUCT**
- 8. Product Spec Schema
- 8A. Body Interface Standard *(new — unverified)*
- 9. Product Presence & Placement Lock
- 9B. Seating Beats *(new — the "putting it on" carve-out)*
- 9A. Held Product Beats
- 9C. Demonstration Beats *(the "show me it's real" carve-out)*
- 9D. Worn Product Visibility *(new at V7.48.3)*
- 10. Prohibited Elements — Scope
- 10A. Real Marketplace and Platform Names

**BLOCK 3 — REGISTERS**
- 11. Colour Language (all modes)
- 12. Global Grade Default
- 12A. Mechanism Register
- 12B. Mechanism Physical Behaviour *(new — unverified, visual check)*
- 13. B-roll Casting Rule
- 14. B-roll Wardrobe Rule *(amended V7.48.7 — keyed to the story day)*
- 14A. Wardrobe Novelty Standard *(new V7.48.7)*
- 15. B-roll Documentation Register
- 15A. Object Beat Surface Standard *(new — unverified)*

**BLOCK 4 — PROCESS**
- 16. Output Layout Rule
- 16A. Delivery Surface Standard *(locked)*
- 16B. Generation Call Labelling *(new V7.51.2)*
- 17. Post-Production Separation Rule
- 17A. Motion Graphics Layer *(new — permitted, specified)*
- 18. Build Order Discipline *(rewritten V7.48.2 — the eight-step flow)*
- 18B. Intake Pack — steps 1 and 2 in one message *(new V7.58.0)*
- 18C. Loom Brief — the advertiser's walkthrough *(new V7.61.0)*
- 18A. Mode & Model Lock *(new V7.50.0)*
- 19. Character / Locked Avatar Creation Rule *(rewritten V7.49.6 — visual-check confirmed across three sheets, one face type)*
- 19B. Medical Professional Casting & Recommendation Rule *(new V7.48.6)*
- 19A. Character Novelty Standard *(locked this cycle)*
- 20. Character Constraint Sheet *(named Build Sheet deliverable)*
- 21. Wardrobe Map *(named Build Sheet deliverable — amended V7.48.7)*

**BLOCK 5 — CAPTURE STANDARDS**
- 22. Mode 1: Photorealistic Standard
- 22A. Mode 1 Capture Realism Block
- 22B. Camera Behaviour Standard *(measured this cycle — one A/B pair)*
- 22C. Audio Capture Standard *(new — unverified)*
- 22D. Voice Identity Standard *(new — axis steerability unverified)*
- 22U. Voice & Talking-Head Pipeline *(new V7.57.0 — Kling source (2+ takes) → ElevenLabs clone → Enhance → v4 TTS → HeyGen Avatar V)* — **Avatar V only, never IV or III; the whole take rendered in one go, then cut into each hook + body** (V7.66.0)
- 22V. Image Verdict — the agent judges every image *(new V7.59.0)*
- 22W. Clip Verdict — the agent judges every video *(new V7.60.0)*
- 22X. Video Preflight — right on the first generation *(new 2026-09-27)*
- 22U step 10a. VO house cut *(locked 2026-09-26, pauses restored V7.65.0, no tight cuts V7.66.0, VO tasks only V7.67.0 — `vo_trim.py`, E11A)*
- 22E. Fixed-Mount Capture Standard *(new V7.48.7; split into MOUNT and RECORD at V7.48.10)*
- 22F. Creator Framing Standard *(new V7.52.0 — visual check pending)*
- 22S. Skin Realism Standard *(Mode 1 — measured this cycle)*
- 22T. Candid Seed Standard *(new V7.49.5 — visual-check confirmed, n=1)*
- 23. *(Retired V7.50.0 — Semi-Realistic Adult 3D)*
- 24. Mode 2: 3D Pixar Standard
- 24A. Shape Language and Proportion *(Mode 2)*
- 24B. Stylized Lighting Design *(Mode 2)*
- 24C. Stylized Ocular Standard *(Mode 2)*
- 24D. Stylized Motion Arc *(Mode 2)*
- 24E. *(Retired V7.50.0 — Stylized 3D Social)*
- 24F. Mode 3: Claymation *(relabelled V7.50.0 — was Mode 5; unverified, visual check)*
- 24G. Mode 4: Realistic Film *(new V7.54.0 — visual check pending)*
- 24H. Scene Continuity — Frames Built Like a Film *(new V7.54.0 — visual check pending)*
- 24I. Dramatic Performance *(new V7.54.2 — Mode 4; visual check pending)*
- 24J. Mode 5: Pixar Film *(new V7.55.0 — visual check pending)*
- 24K. Film Motion & Camera Grammar *(new 2026-09-27 — Modes 4 and 5)*
- 24L. No Trimming in the Film Modes *(new 2026-09-27)*
- 24M. Film Sound — music, room tone and sound effects *(new V7.64.1)*
- 24N. Series Look & Seedance Camera — the prestige streaming live-action style *(new V7.69.0)*
- 25. Style Lock Rule

**BLOCK 6 — PERFORMANCE & MOTION**
- 26. Video Package Rule
- 27. B-roll Per Phrase Rule
- 27A. B-roll Motion Arc *(exit clause measured this cycle; full arc partially verified)*
- 27B. Coverage Ledger *(amended V7.48.2)*
- 27C. Physical Plausibility Standard *(new — unverified, visual check)*
- 27D. Structural Integrity Standard *(new at V7.48 — unverified, A/B pending)*
- 27E. Material Failure and Consequence *(new V7.48.9 — visual check pending)*
- 27F. Script Visual Instructions — binding *(new V7.61.0)*
- 27G. Natural Motion — what the video model does well *(new 2026-09-26)*
- 28. Emotional Match Rule (talking heads)
- 28A. Delivery Field Standard *(locked)*
- 28B. Gesture Register *(locked)*
- 28C. Gesture Lexicon *(locked)*
- 28D. Occupied-Hand Gesture Register *(derived, not measured)*
- 28E. Ocular Behaviour Standard *(new — unverified)*
- 28F. Mouth Behaviour Standard *(new — closure frame-check pending)*
- 28G. Pacing & Dead Air Standard *(locked)*
- 28H. Sync Discipline *(locked — desync is usually arithmetic)*

**BLOCK 7 — CONTINUITY & STRUCTURE**
- 29. Talking Head Segmentation Rule
- 30. Talking Head Continuity Rule
- 30A. Cross-Beat Assembly *(new — costs nothing in the JSON)*
- 30B. B-Roll Selection Standard *(locked this cycle)*
- 31. Short VSL Structure Standard (2–4 min) — Default
- 32. Long VSL Structure (5–20 min) — On Request Only
- 33. Beat ID Convention
- 30C. Scene Consistency Standard *(locked)*
- 30D. After-State Performance Standard *(locked)*
- 30F. Emotional Register — B-roll *(new — the §28 counterpart)*
- 30E. B-Roll Continuity & Assembly Standard *(locked)*
- 30G. Property Standard *(new — unverified, visual check)*
- 30H. B-Roll Placement & Hole-Free Assembly *(new V7.60.0)*
- 30I. Camera Angle Range *(new 2026-09-27)*
- 30J. Camera Focus *(new 2026-09-27)*
- 30K. Lighting — light plan, continuity and story *(new 2026-09-27)*
- 30L. Scene Colour Lock *(new 2026-09-27)*
- 30M. Visual Pitch — the strongest picture for every line *(new V7.85.0)*

**BLOCK 8 — FORMATS & OUTPUT**
- 34. Correction Protocol
- 34A. Learning from the Board — the House Taste *(new V7.73.0)*
- 34B. Learning from My Own Mistakes — the Lessons log *(new V7.82.0)*
- 35. Kling B-roll JSON Format
- 35A. Beat Video Prompt — short and single-minded *(new V7.71.0)*
- 36. Kling Talking Head JSON Format
- 37. Character Budget & Trim Ladders
- 38. Seedance / Wan Talking Head Format
- 39. Dialogue and Delivery Rules
- 40. Editor Notes Rule
- 40A. Music Follows the Script — the register map *(new V7.75.0)*
- 41. Prompt Length Rule

**BLOCK 9 — GOVERNANCE**
- 42. Reference Video Absorption *(rebuilt this cycle — seven parts, in order, none skipped; Part 3A Edit Grammar new V7.63.0)*
- 43. Declined Executions
- 43A. Claim Substantiation *(amended V7.48.2)*
- 44. Locked Defaults *(overridable — say so and they change)*
- 45. Tone & Working Rules

**APPENDIX A — STRING LIBRARY**
- Capture
- Fixed mount *(§22E)*
- Creator framing *(§22F)*
- Anatomy *(§27D, T2I)*
- Skin *(§22S)*
- Avatar sheet *(§19)*
- Location Profiles *(§22A — format models; real entries are Build Sheet content)*
- B-roll register *(§30B)*
- Candid seeds *(§22T)*
- Audio
- Rigs
- Mechanism — anatomical
- Mechanism — sensation library *(V7.48)*
- Mechanism — relief library *(V7.48)*
- Mechanism — stress register (§12A supersession)
- Structural integrity (§27D)
- Wardrobe *(§14A)*
- Placement
- Interface and surface
- Physics (§27C)
- Material failure *(§27E)*
- Mode 2 — 3D Pixar *(renamed V7.50.0; `M3-*` and `M4-*` retired)*
- Mouth, voice and pacing (§28F, §22D, §28G)
- Scene consistency (§30C)
- Property (§30G)
- After-state performance (§30D)
- B-roll continuity (§30E)
- References mode (§4, Wan 3.0 / Seedance 2.5)
- Emotional register (§30F)
- Mode 3 — stop-motion clay
- Realistic Film *(§24G–§24H)*
- Pixar Film *(§24J)*
- Film modes — hero, mechanism and edit *(V7.55.1)*
- Negatives

**APPENDIX B — PRODUCT SHEET SCHEMA**

**APPENDIX C — BUILD SHEET SCHEMA**

**APPENDIX D — RATIONALE INDEX**

**APPENDIX E — AUTOMATION LAYER *(new at V7.36)***
- E0. Run modes — Manual (default) and Automatic *(new V7.56.0)*
- E1. QA matrix — every check bound to an instrument, a threshold, and an on-fail action
- E2. Failure taxonomy and retry budgets
- E3. Run ledger — the build's state file (`run_ledger.json`)
- E4. Act-map row schema
- E5. Slot-fill manifest
- E6. Duration function *(the §28H inverse)*
- E7. Verified call templates *(param names measured in production)*
- E8. Boundary definitions
- E9. Build directory layout
- E10. Doc-lint — standing §34 step at every version cut
- E11. Trim pass — dead air and inhales *(new V7.56.0 — unverified on production clips)*
- E11A. VO house cut — audio-only voice-over *(locked 2026-09-26, pauses restored V7.65.0, no tight cuts V7.66.0, both run modes)*

**PENDING AMENDMENTS**

**OPEN DECISIONS**

**CHANGELOG — V7.73.0 → V7.73.1 *(cut authorised)***

**CHANGELOG — V7.72.1 → V7.73.0 *(cut authorised)***

**CHANGELOG — V7.71.0 → V7.72.0 *(cut authorised)***

**CHANGELOG — V7.70.0 → V7.71.0 *(cut authorised)***

**CHANGELOG — V7.69.2 → V7.70.0 *(cut authorised)***

**CHANGELOG — V7.69.1 → V7.69.2 *(cut authorised)***

**CHANGELOG — V7.69.0 → V7.69.1 *(cut authorised)***

**CHANGELOG — V7.68.2 → V7.69.0 *(cut authorised)***

**CHANGELOG — V7.68.1 → V7.68.2 *(cut authorised)***

**CHANGELOG — V7.68.0 → V7.68.1 *(cut authorised)***

**CHANGELOG — V7.67.0 → V7.68.0 *(cut authorised)***

**CHANGELOG — V7.66.0 → V7.67.0 *(cut authorised)***

**CHANGELOG — V7.65.0 → V7.66.0 *(cut authorised)***

**CHANGELOG — V7.64.4 → V7.65.0 *(cut authorised)***

**CHANGELOG — V7.64.3 → V7.64.4 *(cut authorised)***

**CHANGELOG — V7.64.2 → V7.64.3 *(cut authorised)***
