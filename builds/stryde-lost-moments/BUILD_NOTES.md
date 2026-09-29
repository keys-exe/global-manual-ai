# Build notes — stryde-lost-moments (STRYDE · Lost Moments, Manual)

Read this first when resuming. Build Sheet: `BUILD_SHEET.md` (steps 1–3).

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/1UD92i5fATH3qiiez2jqI2WFQXYxxuPLc
- User message: "run manual. british" → RUN: MANUAL, VOICE: British. MODE blank → Mode 1. HOOKS → 5 in script.
- Script (legacy `.dot`) read out word for word → `intake/script.txt`; per-variant `work/script_<A–E>.txt` and `.lines.txt`.
- Product Sheet V7.49.32 (wordmark lock) came with the folder → now `products/stryde/`.
- **Boards (since 2026-09-29, account iamnotkeysi@gmail.com):** Current https://claude.ai/artifact/HuZVrvs1M47vyzGNWmY1qU · Old https://claude.ai/artifact/4YwhNR2SEyter4U7XvfzJo · Final https://claude.ai/artifact/LHHTb3VdrPK6jf6usYXU5G · Plan https://claude.ai/artifact/3HLCjbPj6rHkMZ6gVxfFX9
- First board (other account, not readable from this one): https://claude.ai/artifact/BahH1QuzHm4bQ9FAdxXfKj
- **Hourly Fix check:** `trig_01QpbwhQm7KT5WJc8zDfvTip` (:47 UTC, session_01LDF4chVVFx9eyVTx6g8W8j, new boards). Old one on the other account: `trig_014cgd2iBMe2YGBTHFEEGFrY` (:47 UTC, bound to session_01QFtjcJsQcS8p957wEAS4kb, this board only; replaced `trig_01G3hn1iQuLVknpWifsZ4Hcp` on resume 2026-09-28 16:02 UTC).

## Sessions
- session_01H4ZN9xQDenS8RsLkEHVFiq (2026-09-28 13:00–13:20 UTC): steps 1–3. Absorption, ledger, phrase inventory,
  claims, Mode & Model Lock; 7 avatar sheets generated on Higgsfield (Sunburst, 2k, one each) and put on the board as
  To check; `docs/absorption` written. Higgsfield 19,676 credits before the cast.

- same session, 2026-09-28 13:25–14:05 UTC: user confirmed all 7 avatars ("I'VE CONFIRM PROCEED"; F1/F3/F4 not answered →
  voiced as written, flags open). Steps 4–5: 10 plates + DOG-BRAMBLE + GK1/GK2 sheets generated (Sunburst, one each) → board,
  To check. Act map for all five variants (`work/actmap.py` is the source; 76 beats, 125 cuts; `angles.py` PASS ×5);
  76 planned cards + docs/actmap, docs/wardrobe, docs/locations on the board. §22U step 1: narrator voice-source frame
  submitted (job b933463d…, nano_banana_pro requested — Higgsfield logs nano_banana_2 again, §5 routing fault as in stryde-identity).

- 14:00–14:15 UTC: user "I'VE CONFIRM PROCEED" — board shows the 10 plates confirmed; N-VOICE-IMG, DOG-BRAMBLE, GK1, GK2
  still To check (Kling voice takes wait for N-VOICE-IMG's Confirm, §22X). Step 6 started: Hook 1 images A-HKa (NB2) and A-HKb
  (NBP, SEAT_LOCK) generated → board To check (`work/beats.py` builds beat T2Is from Appendix A + Product Sheet). Product refs
  uploaded to Higgsfield: `work/higgsfield_media.json`. D-10 revised: never both knees (SIDE_RULE 3) → worn right + second strap held.
  Higgsfield logs NB2 as nano_banana_flash and NBP as nano_banana_2 (routing labels; recorded on the cards).

- 14:50–16:05 UTC (same session): narrator talking-head frame (N-VOICE-IMG) redone on the user's chat notes — v2 redo,
  v3 rebuilt around the script (own stairs, strap worn), v4 kitchen, v5 facing the camera, v6 straight-on eye-level chest-up.
  User asked for another option → N2-VOICE-IMG option B (Black British man, 66, south London), text-only person, To check.
  Board: DOG-BRAMBLE, GK1-AMARA, GK2-TOBI confirmed by the user (15:12).

- session_01QFtjcJsQcS8p957wEAS4kb (2026-09-28 16:00 UTC): resumed from the Drive link; merged `claude/vigilant-cannon-wre8v5`
  into `claude/amazing-bohr-tsowwg`; hourly Fix check moved here.

- 16:20 UTC: user "PROCEED TO VOICE" → narrator = option A (N-VOICE-IMG v6, the one the user kept refining after B was offered).
  Kling takes G1/G2 re-fitted to the v6 chest-up frame (hands rest on the table, small nod on the stress word instead of a hand lift;
  audio only is used), `preflight.py` PASS both (`voice/N_G*.call.json`). **Blocked: Kling balance 3.0 credits** — not sent.

- 16:20–19:50 UTC (session_01QFtjcJsQcS8p957wEAS4kb): **voice** — Kling had 3 credits → user: "use kie ai if not enough credits in kling" (now §5, V7.65.0).
  G1/G2 on Kie `kling-3.0/video` (pro, sound) → `voice_source.py` PASS (202.5 Hz both, 33.2s) → ElevenLabs clone **`Lost` `D20hb4HQVPwtiDd89W7m`**.
  VO: all five variants in one eleven_v3 request (4,802 chars, verbatim PASS), 4 takes; T1 split per variant; user confirmed VO-T1-HK1…HK5
  (old butt-join cut). Merged **V7.65.0** (blissful-brown): house cut with natural pauses — T1–T4 re-cut to `vo/trim/` (144–151 wpm, cap 179);
  not yet on the board. T1 V5 ends clipped (last word cut by the TTS) — user confirmed it anyway; flag.
  **Hook 1 done** (user confirmed both clips): A-HKa = from the foot of the stairs, down backwards holding both rails (user reference
  clip `hooks/ref_stairs_user.mp4`); A-HKb = strap snug under the kneecap, 3/4 side view like the user's photo `hooks/ref_strap_placement_user.jpg`
  (v7: strap lifted by hand + GPT Image 2.5 seam cleanup — Nano Banana edits kept lowering it). A-HKb took 4 video generations (user's go).
  Hook 2 started: B-HKa (struggling onto the bench) and B-HKb (placement like the user's photo) images on the board, To check.
  Lessons for every hook: show the struggle; product framed like the user's placement photo, notch against the kneecap, no hands over it.

## Where it stands
- Hooks 1–3 confirmed (C-HKb: frame v4 coffee mug + clip v4, 4th generation on the user's go). Hook 4: D-HKa, D-HKb frames v1 To check → their clips (5s, Kie kling-3.0 while Kling is short) after the Confirm. Then Hook 5 (E, Clifton).
- Lessons: GPT Image 2.5 edits need `resolution: 2k` and "same crop, do not zoom out" (1k default zoomed out and moved the strap). `kie.py kling --out` is the MP4 path, not a task file — log the full output to keep the task id.
- Put the V7.65.0 VO re-cuts (vo/trim) on the board as new versions; then `assemble.py --lengths` per variant on the chosen cut.
- Open flags: F1, F3, F4 (claims), F11 (`package_closed.jpg`); VO V5 last word clipped on T1.

- session_01LDF4chVVFx9eyVTx6g8W8j (2026-09-29 09:00 UTC, account iamnotkeysi@gmail.com): resumed; the first board set and sessions
  belong to the user's other account and can't be read here → user: "NEW BOARD". Four new boards from the template. Rebuilt from
  the repo + connectors: 9 cast, 11 plates/dog, narrator frame v6 (Higgsfield job URLs), hook frames + clips (Higgsfield / Kie task
  URLs), 66 planned B-roll cards from `work/actmap_rows.json`, plan docs. Only current versions moved (old versions stay on the first
  Old board). Take 1 re-downloaded from ElevenLabs history (AGEjLCNEsKA4hCC0ADOI), split at `split_T1.json` cuts, house cut →
  VO-T1-HK1…5 To check (V3: breath at 18.79s kept; V4: breath 32.14s + long pause 28.11–28.75s; V5: last word clipped by the TTS).
  **C-HKb clip v4 not recovered** (its Kie task id was never logged) — the user downloads it from the old board.
  D-HKa image Fix (user): "MAKE IT STRUGGLING ON HIS KNEE PAIN" → v5 nano_banana_pro edit of v4 (job 93103d12-eb4e-444a-b035-84ebaf026a33).
- 09:25 UTC: user "CONFIRM HOOK 4" — board shows D-HKa frame v5 + its existing clip (made from frame v4) and D-HKb frame v2 + clip v2 all confirmed. **Hooks 1–4 done.** Next: Hook 5 — E-HKa, E-HKb frames To check → their clips on Confirm.
- 09:30 UTC: user "CONFIRM HOOK 5" — E-HKa, E-HKb frames confirmed on the board. Clip calls v1 (5s, Kie kling-3.0, sound on → 135 credits each; earlier hooks ran 90) preflight PASS → E-HKa task 31d2f3cd…, E-HKb task 946c1dc7… → on the board To check (split in 2 parts, >15 MB). E-HKb motion: he lowers easily onto his LEFT knee on the rug (the story's "get down on the floor").
  Next after Hook 5's clips: voice lengths (`assemble.py --lengths` per variant on the house-cut VO) → B-roll Acts 1–6.
- 09:45 UTC: user "REDO THE HOOK C" (no Fix notes on Hook 3's cards) → re-made the missing C-HKb clip: same frame v4 + v4 prompt, generation 5 on the user's go, preflight PASS, Kie task 4c280f21… (90 credits, sound off) → board To check.
- 11:55 UTC: user Fix on A-HKb, B-HKb, C-HKb, E-HKb — "just change the wardrobs" (after the wardrobe talk: the strap-on half of each hook now wears the day-2 / after outfit). GPT Image 2.5 sunburst high 2k edits of the confirmed frames, clothes only, same crop, strap untouched: A 384c494b… (coral blouse, navy linen skirt), B 3437138c… (raspberry fleece, navy shorts), C b5a4abad… (burgundy gilet over grey sweatshirt, stone shorts), E ae70e9ca… (mustard-and-green shirt, olive shorts). Old frames → Old board. Clips wait for the frames' Confirm, then are re-made from them (A-HKb, B-HKb, C-HKb past 2 generations → need the user's go; the Confirm + "FIX THOSE" is read as the go).
  D-HKb (Graham) was not flagged — still day-1 garage outfit.
- 12:06 UTC: user confirmed the re-dressed A-HKb, B-HKb, C-HKb frames + "FIX THOSE" → clips re-made from them, same confirmed motion, subject line names the new clothes: A-HKb v8 (f1ed9bbe…), B-HKb v3 (b11b37ae…), C-HKb v6 (18f39bfb…), 90 credits each, preflight PASS → To check. Old-outfit clips → Old board. E-HKb re-dressed frame still To check; D-HKb unchanged (day-1).
- 12:20 UTC: user Fixes —
  A-HKb: "MAKE SHE DOWN STAIR WITH CONFIDENT WITHOUT TOUCHING THE HAND RAIL" → new shot (Higgsfield nano_banana_pro 391b10c8…): side view through the spindles, knee height, waist-down, walking down forwards mid-step, hands free, strap to camera, day-2 outfit. Old sitting frame + its clip → Old.
  E-HKa clip confirmed (user).
  E-HKb: "CHANGE THE SCENCE MAKE IT HE LIFTING HER GRANDCHILD HAPPY TOGETHER" → new scene (a798d588…): Clifton mid-lift of Amara on the rug, both laughing, hip height 3/4 from his right, day-2 outfits, strap uncovered. Old frame + clip → Old.
  Both frames To check; their clips (§27G staging: A two steps down reciprocal gait; E finishes the lift) after the Confirm.
- 12:28 UTC: A-HKb stairs frame confirmed (user) → clip v9 (Kie ddd7e120…, 90 cr): two steps down, reciprocal gait, hands free, side waist-down, camera still (§27G, STAIR-EASE/NEG-SUPPORT/NEG-EFFORT), preflight PASS → To check.
  E-HKb Fix "FIX THE PRODUCT" (the lifting frame had a flat fabric band) → GPT Image 2.5 edit 93a5c907… with product refs + placement photo: real strap under the kneecap; previous frame → Old. To check.
- 12:45 UTC: user Fixes —
  A-HKb clip: "JUST WALK DOWNSTAIR WITHOUT TOUCHING THE HANDRAIL" → diagnosed (contact sheet): her far hand drifts onto the WALL rail from ~1.5s; the rail sat at hand height in the frame. Fix at the source: GPT Image 2.5 edit f1d7edd9… removes the wall rail + brackets (same crop). Frame To check; clip re-made after Confirm.
  B-HKb: "MAKE SHE WALKING ON THE STREET HAPPY" → new frame 489afe1d… (side-on full body, right→left mid-stride, smile, day-2 outfit, high street).
  C-HKb: "MAKE IT HE WALKING WITH THE DOG HAPPY" → new frame f91a9b21… (side-on full body, right→left with Bramble on the red lead, smile, day-2 outfit, outside his house).
  E-HKb frame (real product) confirmed → clip v2 (Kie 0192fd30…, 90 cr): he finishes the lift and holds her, both laughing; preflight PASS → To check.
  Replaced frames/clips → Old. Walking clips (B, C) will use §27G: 3–4 steps across a locked frame.
- 12:51 UTC (hourly check): user confirmed the A-HKb rail-free frame, B-HKb walking frame, C-HKb dog-walk frame → clips A-HKb v10 (2930a670…), B-HKb v4 (8809278b…), C-HKb v7 (58c3447f…), 90 cr each, preflight PASS; walks = 3 steps across a locked frame (§27G) → To check.
- 12:58 UTC: user confirmed B-HKb (walking) and C-HKb (dog-walk) clips. A-HKb clip Fix "WALK CONFIDENTLY" → diagnosed: v10 stood on one step and shuffled from ~1s (2 slow steps in 5s = idle time). v11: 3s, three brisk steps each landing on the next lower tread, travelling down the frame, 'no standing still / no stepping in place' (Kie 385fc53b…, 54 cr), preflight PASS → To check. Lesson: stairs after-state = 3s and 3 steps, never 5s for 2.
- 13:00–13:20 UTC: user "I'VE CONFIRM PROCEED" — board: all 10 hook cards and VO-T1-HK1…5 confirmed → **hooks and VO locked** (`voLocked` on the build doc).
  Step 7 started. `work/plan_B…E.json` built from actmap.py ORDER lists (plan_A reproduced exactly); MECH-01 phrase fixed for B/E, MECH-02 phrase/key for B/D.
  `assemble.py --lengths` per variant on the house-cut VO (masters 65.8–67.9s) → `work/broll_lengths.json` (max across variants, 3–6s) → `duration` on every B-roll card.
  Flag: the closing line "Nothing to lose but the pain." gets < 2s in every variant (it ends the master) — hold the previous B-roll over it in the edit (§30H merge), no extra call.
  Act 1 (16 shared beats): `work/act1.py` builds the T2Is (Appendix A + Product Sheet; G-01…G-10 one-offs cast with the beat, ~half Black per VN01); sent condensed to Higgsfield (as the hooks were) — `work/prompts/<beat>.sent.txt`, jobs in `work/act1_jobs.json` / `act1_sent.json`. SH-04c first submit failed on Higgsfield (no render), resent. All 16 → board To check.
- 13:35 UTC: user "I'VE CONFIRM PROCEED" on the Act 1 images — the board had not saved the Confirms (all still review), so the chat message was taken as the Confirm and written to the cards. Act 1 clips: `work/act1_clips.py` → `work/clips/<beat>.v1.{kling,call}.json` (§35, §27G: one action at a named pace, camera propped, rigid product; NS-03b: the turn not animated — frame already turned; MECH: ANAT-STRESS-PC / -SC, trimmed ANAT/EXTERNAL negatives to fit 2,500). All 16 preflight PASS → Kie kling-3.0, sound off, E6 lengths (3–6s) → 1,116 credits → board To check.
- 13:50 UTC (hourly check): user Fix on NS-03a image "REMOVE THE CAMERA PHONE STYLE" — the render had the iPhone camera-app interface drawn over it (icon bar, PHOTO/VIDEO bar, shutter). GPT Image 2.5 edit 66e995eb… removed it, scene continued, same crop → To check; v1 image + its clip → Old; clip re-made after Confirm.
  Lesson for every condensed T2I from here: add "no camera app interface, no on-screen buttons, no icons, no text overlays" to AVOID (the short "Shot on an iPhone" line without CAP-FILE invites the UI).
- 13:57 UTC: user Fixes — NS-03b "USE THE PRODUCT REFERENCE" (v1 drew an open flat band) → GPT Image 2.5 edit fb3c20d8… with back.webp + front: the product as one closed loop, pad side to camera. NS-06 "NO STRYDE STRAP ON THISE SCENE" → edit d6d87309…: chino leg rolled fully down, no strap anywhere. Both To check; v1 images + clips → Old; clips re-made after Confirm.
- 14:08 UTC: user Fixes/Confirms — Act 1 clips confirmed: SH-02, SH-03, SH-04a/b/c, SH-05, SH-06, NS-04b, NS-07 (+ MECH-01 earlier state). Fixes:
  MECH-02 clip "FIX THIS ERROR DONT CHANGE THE PRODOCT MAKE IT CONSISTENT" → diagnosed: v1 orbited/cut to new angles, shell became a flat band, a skeleton hand appeared → v2 pinned first+last frame to the confirmed image (§27G rule 5), camera fully locked, one pulse/s, HOLD_PROD (Kie 4d8d1660…).
  SH-01 clip "FIX THE PROPER EXPRESSION" → v1 blank stare off to the side → v2 looks up to the patient, warm confident smile (Kie 7e7df09f…).
  NS-05 image "FIX THE PRODUCT USE THE PRODUCT SHEET" → floppy open strap → GPT edit 2a4c78bd… real product, closed loop.
  NS-06 frame confirmed → clip v2 (weight shift, fabric flat, no strap) (Kie 8e8ea911…).
  Still To check: NS-03a, NS-03b, NS-05 images (clips after Confirm).
