# Build notes — stryde-71-stairs-pixar-song (STRYDE · 71 Stairs Pixar Song · Manual · Mode 2)

Read this first when resuming. Build Sheet: `BUILD_SHEET.md` (steps 1–3).

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/1VZ709_1L6_cNjSadgDKn-BIKDGy89a5C — task "A - VID | Pixar Song | TOF | Pure Mechanism | Iteration | 71 Stairs Black American Woman"
- User message: the Drive link + "run manual, the song is inside". → RUN: MANUAL; **Mode 2 — 3D Pixar** (the task title); HOOKS → 1 (the song is one fixed piece); no VOICE to make.
- **The song is the voice master:** `intake/song.mp3` (copy of `71 Stairs Afro American Woman.mp3`), 228.02 s, vocal 0–222.7 s, ~165 sung wpm, ≈74 bpm (unverified). The script sung word for word (VN01). Lyrics `work/lyrics.txt` (108 lines, 615 words); word-timed lines `work/lyrics.timed.json` (faster-whisper small; 603/615 words aligned, "Stryde." at line 37 not heard — F4). Never re-voice, trim or speed it.
- Inspo = the original 71 Stairs ad (same file as `stryde-71-stairs`): 155.55 s, 9:16, 82 shots, mean 1.9 s, no silences (`intake/inspo_report.json`, frames in `intake/frames/`).
- Script doc is a native Google Doc (exported .docx by the fetch). Product Sheet V7.49.32 in the folder = older than the repo's V7.49.38 → repo sheet kept. 11 product photos byte-identical to `products/stryde/stryde_refs/`.
- Cast = the `stryde-71-stairs` cast recast in Pixar (VN04 "same Afro American Black Woman and entourage"): N, C1 Loretta, C2 the daughter.
- **Boards:** Current https://claude.ai/artifact/NPMPgJeXr6cgTvtuFGhkZc · Old https://claude.ai/artifact/3pEQz2pWLJwTNX5TuBdccV · Final https://claude.ai/artifact/FYK7PCvgLG4SLzj72YdBPn · Plan https://claude.ai/artifact/VEE8gmwPVbvhVMNSC5rBLY (owner keysibaldonado@gmail.com)
- **Hourly Fix check:** `trig_01YXJhp6bfhh6W1Khk5oAPrk` (:20 UTC, bound to session_014b6n9bhiR2XgZ38wPBL12w).

## Sessions
- session_014b6n9bhiR2XgZ38wPBL12w (2026-10-01 ~10:00–10:30 UTC): steps 1–3. Four boards published from `dashboard/generation_board.html` (V7.75.1 template after the default-branch merge);
  absorption (song-clocked structure map, Edit Grammar `EDIT-STRYDE-71-SONG`), ledger VN01–VN05, phrase inventory with song times (42 phrases, 615 words),
  claims, Mode 2 & Model Lock; 3 Pixar avatar sheets on Higgsfield (`nano_banana_pro` requested, **logged `nano_banana_2`** — §5 routing fault, 2 cr each)
  → Current board To check (assets 78a2cc62…, dd77d413…, 6adbaf4d…); `docs/absorption` on Plan + Current. Higgsfield 11,355.4 before the cast.
  **Mode 2 sheet form built here (F10)** — `cast/build_sheets.py`: the master has no Mode 2 sheet recipe; proposed as a Pending Amendment on the user's word.
  **Waiting on the user's avatar decision** and F2 (full Pixar vs hybrid), F3 (sung-to-camera bookends or none), F4 (is "Stryde." sung at 84–87 s).

- same session, ~10:25–10:35 UTC — **Fix round 1 (user: "i want new ones and loretta should not be too thin they should be the same size as the narrator")**:
  three new characters written (`cast/build_sheets.py` v2 — N oval face / silver twist-out / mustard + denim; C1 square face / silver bob / teal + khaki,
  **the narrator's build**; C2 heart face / afro puff / olive + black), "no writing on the canvas" + one-side marker clauses added (v1 drew panel titles
  and mirrored the marker). 3 jobs on Higgsfield (nano_banana_pro requested, logged nano_banana_2, 2 cr each) → v2 on Current as To check
  (assets 21896d82…, f0d9e11e…, fda069ae…); v1 files copied to the Old board (a86adc7f…, f0b774bc…, 3128f425…), Old docs written, v1 deleted
  from Current. VN04 re-read: same roles, new faces (user's call). `fix_patterns.py` run on the Current + Old dumps (`work/fix_patterns.md`): 3 notes (6 rows, each seen on both boards), one beat each — no repeating rule yet; the Loretta build note is a beat fix.

- same session, ~10:35–10:50 UTC — user **"CONFIRMED ALL PROCEED"**: the three v2 avatars set `use`, `docs/absorption` confirmed; F2 full Mode 2,
  F3 variant A (no singing to camera), F4 caption carries "Stryde." — all on my recommendations. **Steps 4–5 delivered (`STEP4_5.md`):**
  Property Sheet PROP-N (7 fields), location derivation (8 plates + incidentals), light plans; **8 Pixar plates** (16:9, nano_banana_pro → logged
  nano_banana_2, 2 cr each; P1/P2 with P0 attached as `image_references`) on Current as To check (`plates/build_plates.py`, Mode 2 plate form);
  **act map on the song's clock** — 76 B-roll rows, no talking heads, all 108 lyric lines covered in order, E6 call lengths from the lyric word
  timestamps (no `pending-master`, no splits), `angles.py` PASS (`work/actmap.py` → `actmap_rows.json`, `angles.json`, `actmap.md`, `plan.json`);
  wardrobe map, story-day map, ledger assigned; 76 planned cards + `docs/actmap`, `docs/wardrobe`, `docs/locations` on Current + Plan.
  Flags F14 (Loretta's pant leg vs FP13), F15, F16. Higgsfield 11,355.4 → ~11,323 after the cast and plates (14 renders × 2 cr).

- same session, ~10:50–11:05 UTC — **V7.76.0 landed on the default branch (§3C Music Video)** and describes this build: adopted (nothing was generated
  against the act map yet). Boards republished on the V7.76.0 template (Music stage); build doc `kind: "music"`, `voices` removed, `music` block; the song
  on Current as **MUS-BODY** (audio card, mp3 wrapped in mp4, To check; `music/MUS-BODY.cue.json` = the §40A register map with the lyric lines per section,
  `music.py check` report on the card; beat grid `music/MUS-BODY.grid.json`, 73.8 bpm pinned). **Act map re-gridded (§3C):** every cut on the last beat at or
  before the lyric cut (never late), rows carry `section` + `bars`; 15 rows under the 2.0 s floor merged into their neighbours (the EG05 montage is one card)
  → **61 rows**, 108/108 lines, no FLASH, no split, `angles.py` PASS. Board: 15 planned cards deleted, 61 rewritten, `docs/actmap` rewritten (Current + Plan).

- same session, ~11:00–11:10 UTC — user **"FIX THOSE"**: six plates confirmed (P0, P3–P7); **Fix round 2** on two: P1-LANDING "NOT THE SAME AS THE P0 PROP N"
  → v2 as an image edit of the confirmed P0 (Image 1 as `image_references`, the same flight from its top, sides restated for the new angle — HT17);
  P2-KITCHEN "I NEED A NEW UNIQUE ARANGEMENTS HERE" → v2 a personal Southern grandmother's kitchen of the same house (sage-green cabinets, yellow
  counter, breakfast nook, skillets, church fan, crayon drawings), P0 attached. `plates/build_plates.py` V2 block, `plates/*.v2.prompt.txt`.
  Both on Current as To check; v1 files on the Old board (2aa94055…, fce7cec3…), deleted from Current. fix_patterns: the "same as P0" note is the
  third build with it (HT17 already covers it) — no new rule.

- same session, ~11:25–11:40 UTC — P2-KITCHEN v2 **confirmed** by the user. **Fix round 3 on P1-LANDING** (user: "FIX THE P1 I WANT IT CONNECTED TO THE
  P0", board note "STILL NOT CONNECTED"): v2 had drawn a return stair with a half-landing. v3 = an image edit of P0 on **Kie `nano-banana-pro`** (true Pro —
  Higgsfield reroutes every Pro call to nano_banana_2; §5 "can't run" case), P0 uploaded to Kie as `image_input`, the prompt counting one straight flight of
  fourteen steps from its top, every side restated (`plates/P1-LANDING.v3.prompt.txt`). **Kie spend measured 963 credits** (262,932.8 → 261,969.8 — far
  above the 18 noted on not-your-cartilage; unverified why). The render keeps the camera at the hall floor (reads as P0's own view with a short extra flight
  in the foreground) — on Current as To check with that said on the card; v2 to Old (d696aabd…). If it fails again: §30G says hall, stairs and landing are
  TRAVERSED (no location plate — they take the property plate), so the landing beats (HK-03a, P-02a) can be made as edits of P0 looking up the flight.

## Open (Flags in BUILD_SHEET.md)
F1 sung claims to confirm · F2 full Mode 2 (locked) vs hybrid · F3 narrator never sings to camera (default) vs two bookends · F4 "Stryde." · F10 Mode 2 sheet amendment / true Pro route on Kie · F12 BPM · F13 clipped master.

## Next
**Waiting on the plates' Confirm.** Then step 6 — the hook (HK-01a → HK-03a, 0–15.5 s): A/B beat images with `motionPlan`, then the Kling clips on the user's picks; then the body acts in order; CapCut block with lyric captions and the outro end card.

(Earlier plan, done:) steps 4–5 (property sheet + 16:9 Pixar plates on nano_banana_pro: house stairs/landing/kitchen, reception, store checkout, church steps, street; act map on the song's clock — E6 lengths from `work/lyrics.timed.json`, cuts on 3–4 beats, `angles.py` PASS; wardrobe map). No voice stage. Then hook (0–15.5 s) at step 6, body acts at step 7, CapCut block with lyric captions.
