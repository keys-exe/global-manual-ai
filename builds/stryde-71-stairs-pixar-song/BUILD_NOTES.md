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

- same session, ~12:10–12:20 UTC — **Fix round 4 on P1-LANDING** (board note "it should be the 2nd floor view"): diagnosis — the long prompts restating
  the whole hall anchored the model to P0's own viewpoint. v4 = a **short** edit of P0 (1,937 chars) with an HT22 geography block (camera upstairs, the hall one
  storey below, exactly one straight flight, sides stated), Higgsfield nano_banana_pro (logged NB2, 2 cr). The render is the view from the top of the flight
  looking down to the front door, photo wall left, rail right — but the model also drew a gallery balustrade across the top of the frame and a second
  landing rail on the right (not in P0). On Current as To check; v3 to Old (b7ddb7b6…). Default branch merged (V7.77.1, HT22).

- same session, ~12:25 UTC — user **"drop that"**: the landing plate P1 is dropped (§30G: hall, stairs and landing are TRAVERSED — they take the property
  plate). HK-03a and P-02a become image edits of P0 (the top of the flight, HT17); act map / STEP4_5 / docs updated; P1 card removed from Current, all four
  versions on the Old board. All seven remaining plates are confirmed → **step 6 (the hook) is unlocked.**

- same session, ~12:35–12:50 UTC — **Step 6, the hook: A/B start frames + pinned end frames on the Current board, all To check.** Four §6A short
  prompts (`hooks/build_hooks.py` → `hooks/<BEAT>.prompt.txt`, 1,183–1,199 chars, `preflight.py` kind image PASS on all seven): HK-01a and HK-03a are
  image edits of P0 (HT17, Image 1 = the plate, 9:16 crop on the flight / on the top of the flight), HK-01b (feet CU, no sheet) and HK-02a (C2 from the
  top looking down) carry P0 as a reference. Both renders of each pair on Higgsfield `nano_banana_pro` (logged `nano_banana_2` again, §5 fault noted on
  every card; Kie Pro not used — 963/render). **§27G rule 10 applied:** every stairs-class row is pinned — `actmap.py` now sets `pin_end = yes` on any
  `stairs:` staging (13 rows incl. PR-02a), act map / STEP4_5 / `docs/actmap` on Current + Plan re-synced, the 12 stairs cards carry `pinEnd: yes` +
  `endFrame`. The hook's three stairs beats got their end frames the same turn as their own cards — `HK-01a-END`, `HK-01b-END`, `HK-02a-END` (A = an
  edit of start A, B = of start B; "Use A with start A"). HK-03a (a head turn, staging none) is unpinned. 14 renders = 30 Higgsfield credits measured
  (10,377.65 → 10,347.65; 2.14 each on the cards). Assets `hooks/assets.json`, jobs `hooks/jobs.json`, connector links `hooks/urls.json`.
  What I saw (information only — the picks are the user's): HK-01a A/B both on P0's staircase, N two–three steps up (not the 6th), C2's hand on the newel;
  HK-01b A has a white top edge at the daughter's waist, B is shot through the balusters; HK-02a A has bare oak treads and a hall mat, B a tiled hall floor
  (both off the plate); HK-03a A puts N on the hall floor at the foot of the stairs (wrong end), B has her on the landing behind the balusters with C2 on
  the top step. Video pilot: HK-01a is the build's first stairs clip (§27G rule 10) — it runs alone after the picks, the other stairs clips wait on its Confirm.

- same session, ~13:00–13:20 UTC — user **"we dont need end frame generate new ones"** (after Use A on HK-01a and its END card). **End frames waived:**
  §27G rule 10's pin recorded as `pin_waived` on every stairs row (`actmap.py`: `pin_end: no · waived (user 2026-10-01)`; STEP4_5 / `docs/actmap` on
  Current + Plan re-synced; the 12 stairs cards `pinEnd: no`, `pinWaived`), the three END cards removed from Current and kept on Old with both renders.
  **New pairs** (v3/v4 = A/B) for HK-01b, HK-02a, HK-03a from rewritten prompts (`hooks/<BEAT>.v2.prompt.txt`, preflight PASS: HK-01b names the
  sweatshirt hem at the top edge; HK-02a asks for the runner, a rod on every step and the bare oak floorboards of the plate; HK-03a states the landing is a
  storey above the hall and the mother stands on the landing floor above the top step); v1 pairs to Old. Seen: HK-03a A again puts the mother at the foot of
  the stairs on the hall floor, B has both at the top; HK-02a A/B both on the runner with the oak floor below now. Higgsfield balance moved 82.25 for the
  6 renders (10,347.65 → 10,265.4) — far more than the 2.14/render measured on the first batch; cards carry 2.14, unverified why.
  **HK-01a clip (stairs pilot)** on Kling `kling-video-v3_0` (the lock said omni; v3_0 is the single-image first-frame route per who_am_i — same Kling 3.0),
  5 s, 1080p, `prefer_multi_shots false`, `enable_audio false` (the song is the sound), start = v1 A via its Higgsfield CDN link, §35A prompt 908 chars,
  preflight PASS with `pin_waived` + `pilot: first`; 40 Kling credits (44,563 → 44,523); 1072×1928, 5.04 s, 24 fps; on the card as To check
  (`clips/HK-01a_v1.mp4`, contact sheet `clips/HK-01a_v1.contact.jpg`: she climbs hands-free, the daughter's hand on the rail, camera still).

- same session, ~13:35–13:50 UTC — user **"FIX THOSE"** (board notes: HK-01b "WRONG CHARACTER", HK-02a "INCORRECT PLACEMENTS OF PICTURE FRAMES FIX THE
  LOCATION", HK-03a "WRONG LOCATION"). Default branch merged first (V7.78.1 — HT23 "one scene, one continuous moment"). Diagnosis: all three faults are
  fidelity to the confirmed scene — the characters in a no-sheet feet shot, the photo wall and the landing drawn free-hand from the plate. Fix at the source
  (HT17): each v3 pair is an **image edit of the confirmed HK-01a frame A** (Image 1 = that frame, the user's own pick — right staircase, right two women,
  right photo wall), with the HT23 "Scene so far" line on every prompt (`hooks/<BEAT>.v3.prompt.txt`, 1,182–1,200 chars, preflight PASS, `match: frame`).
  HK-02a's camera therefore bends to the frame's (from the hall floor, the daughter side-on near the top, face in profile) — the act map's "from the landing
  looking down" would have had to invent the wall again. v5/v6 = the new A/B; v3/v4 to Old. `fix_patterns.py` run (27 notes): the repeating note on this
  build is "use the location / connected to P0" (P1 ×3, HK-02a, HK-03a) — already HT17, now applied as edits of the confirmed frame; no new rule.

- same session, ~14:55 UTC — the six v3 Fix renders landed after ~65 min in Higgsfield's queue (the user asked for Kie if Higgsfield faulted; it cleared
  before a reroute was needed). v5/v6 on the Current board as To check, v3/v4 on Old. Seen: every render keeps the confirmed frame's camera, staircase,
  photo wall and both women (the three faults are gone), but the model kept the women low on the flight — HK-01b is a wide, not the feet close-up;
  HK-02a has the daughter at the newel with the mother mid-flight; HK-03a has the mother a few steps up turning back, the daughter at the foot. The
  user's picks decide. Higgsfield balance 10,091.15 (shared account — other users' renders move it between our batches).

- same session, ~15:00–15:15 UTC — user **"USE THE CINEMATIC CAMERA ANGLES CAUSE THIS HOOK IS TOO WEAK"** (after confirming the HK-01a clip, HK-02a A
  and HK-03a B, and a Fix "THEY ARE SO BIG" on HK-01b). The hook re-angled per §30I with the §24K part 7 shot names on the user's explicit call (the
  library is Modes 4–5; applied here as the user's instruction): HK-01a SH-LOW full from the foot through the newel, HK-01b SH-GROUND feet through the
  balusters (feet at true scale — the "so big" note), HK-02a SH-HIGH from the landing straight down the flight, HK-03a SH-OTS over the daughter's shoulder
  onto the mother on the landing with the window behind her. `actmap.py` rows rewritten (angles.py PASS), STEP4_5 / `docs/actmap` re-synced, cards carry
  `shot`. New viewpoints, so not edits: Image 1 = the confirmed HK-01a frame A (scene fidelity) + sheets (+ P0 on HK-02a); `hooks/<BEAT>.v4.prompt.txt`,
  preflight PASS. v4 pairs on Current as To check; the confirmed v1 A (and its clip, status use), v5 A and v6 B stay as versions; HK-01b/02a/03a v5–v6
  files to Old. Seen: HK-01b, HK-02a and HK-03a took the new angles (HK-02a B's daughter drifts off model); HK-01a stayed close to the confirmed frame's
  view in both renders — the frame reference dominated; if the user wants the low full shot, the next round drops the frame ref and uses P0 + sheets.

- same session, ~15:20–15:35 UTC (hourly Fix check) — the user picked the re-angled pairs: **HK-01a v3 (A)**, **HK-01b v7 (A)**, **HK-02a v7 (A)**
  confirmed; **HK-03a** Fix "wrong location" on the OTS pair (the model invented a bright landing room with a window — no plate exists for the landing).
  v5 = the OTS kept but built as an image edit of the user's confirmed v6 (the top of the flight from the hall), viewpoint moved up the flight
  (`hooks/HK-03a.v5.prompt.txt`, PASS); v9/v10 To check, v7/v8 to Old. Seen: both renders keep the P0 staircase; the camera landed at the foot
  behind the daughter, the mother mid-flight turning back. Unused picks (HK-01a v4, HK-01b v8, HK-02a v8) to Old. **Clips** from the three picks on
  Kling `kling-video-v3_0` (§35A, preflight PASS; HK-01a = clip v2 from the new frame, clip v1 kept as a version): HK-01a 5 s / 40 cr, HK-01b 5 s / 40 cr,
  HK-02a 6 s / 48 cr (44,019 before). `fix_patterns.py` re-run (29 notes): the repeated note of this build is still the location one (now 6 beats) —
  HT17; the new "THEY ARE SO BIG" is a one-off (scale against the steps written into every stairs prompt since).

- same session, ~15:35 UTC — the three hook clips landed (Kling `kling-video-v3_0`, 1072×1928, 24 fps): HK-01a clip v2 (5.04 s, from image v3 — both
  climbing away from the low viewpoint, hands free), HK-01b v1 (5.04 s — the pump and trainer climbing through the balusters), HK-02a v1 (6.04 s — the
  daughter climbing toward the high lens, face up). All To check (`clips/`, contact sheets beside). Kling 43,851 after (128 for the three).

- same session, ~15:45 UTC — user **"hk01 a and b should be a different location cause its woman half her age should be outside"**: HK-01a and HK-01b
  moved to the **church front steps (P5)** — the same Sunday (N-D4, church dress + the wide-brim hat per the wardrobe map), two one-off women in their
  thirties on the steps below her (HT05: the stakes in the picture). `actmap.py` rows rewritten (L-CHURCH, open-sky light; angles.py PASS), STEP4_5 /
  `docs/actmap` re-synced. HK-01a = an image edit of P5 (HT17, Image 1 = the plate, Image 2 = N's sheet); HK-01b = feet CU on the steps with P5 as the
  reference (`hooks/<BEAT>.v6.prompt.txt`, PASS). The home-stairs clips on both cards are superseded — kept as versions; new clips follow the new picks.

- same session, ~15:40–15:55 UTC — **HK-01a/b church pairs landed** (v5/v6 on HK-01a, v9/v10 on HK-01b, To check; the home-stairs picks and clips stay
  as versions on the cards — their files are still used by the clip versions, so not moved). Seen: N in the hat climbing past two younger women on the
  P5 steps; the feet CU on the concrete steps with the sandals. **HK-02a clip confirmed** by the user. **HK-03a** Fix "this should be at the second
  floor": v7 = an image edit of the user's confirmed HK-02a v7 (the view down the flight from the landing — the second floor the user confirmed), the
  mother's shoulder in the near foreground (OTS from the landing), the daughter on the top step (`hooks/HK-03a.v7.prompt.txt`, PASS; actmap row:
  high · ots · through, angles.py PASS). v11/v12 To check, v9/v10 to Old. Higgsfield 9,668.15 after (shared account).

## Open (Flags in BUILD_SHEET.md)
F1 sung claims to confirm · F2 full Mode 2 (locked) vs hybrid · F3 narrator never sings to camera (default) vs two bookends · F4 "Stryde." · F10 Mode 2 sheet amendment / true Pro route on Kie · F12 BPM · F13 clipped master.

## Next
**Waiting on:** picks on HK-01a (church, v5/v6), HK-01b (church, v9/v10) and HK-03a (second floor, v11/v12); HK-02a image + clip confirmed. Then the HK-01a/01b/03a clips; then the body acts. Then their clips (no end frames — waived; §35A ≤ 1,000 chars, preflight PASS); then the body acts in order; CapCut block with lyric captions and the outro end card.

(Earlier plan, done:) steps 4–5 (property sheet + 16:9 Pixar plates on nano_banana_pro: house stairs/landing/kitchen, reception, store checkout, church steps, street; act map on the song's clock — E6 lengths from `work/lyrics.timed.json`, cuts on 3–4 beats, `angles.py` PASS; wardrobe map). No voice stage. Then hook (0–15.5 s) at step 6, body acts at step 7, CapCut block with lyric captions.
- same session, ~15:50–16:05 UTC — **"i want new ones cause these hooks looks the same as the others i want more powerfull hooks" → the plaza hook.**
  A new hook concept, not another fix of the old one (HT05: the hook sells out in the world, the stakes in the picture): one monumental public
  staircase — the great outdoor entrance steps of a downtown arena plaza on a Sunday afternoon (new location L-PLAZA, plate **P8-PLAZA**, 16:9,
  `plates/build_plates.py --p8`, Higgsfield nano_banana_pro (logged nano_banana_2), on the Current board as To check — generated together with the
  hooks so the round didn't wait on a plate pick; it is the reference of all four hook frames). The younger crowd stopped on the steps is the stakes
  N climbs past. Act map, `STEP4_5.md` (locations table: L-PLAZA · PLATED · P8-PLAZA; light row), `docs/actmap` (Current v9 / Plan v9) and
  `docs/locations` (v3) re-planned on L-PLAZA; angles.py PASS (61 rows); stairs pin stays waived. Four §6A v8 prompts (`hooks/build_hooks.py --v8`,
  `hooks/<BEAT>.v8.prompt.txt`, all PASS, 1,148–1,198 chars): HK-01a an image edit of P8 (`match: plate`, HT17; Image 1 = P8, Image 2 = N sheet),
  SH-LOW FULL from the plaza, N on the 15th of 30 steps, a dozen younger people stalled below her; HK-01b SH-GROUND CU profile at tread height, her
  pumps past the stopped trainers (ref P8); HK-02a SH-HIGH MEDIUM from the top landing, the daughter ten steps below (refs C2, P8); HK-03a SH-OTS
  over the mother's shoulder from the top, the daughter stopped at the rail (refs N, C2, P8). 8 renders, one per call (jobs in `hooks/jobs.json`
  `<BEAT>@v8A/B`), ~2.14 cr each; Higgsfield balance 9,642.15 after. Board: **HK-01a v7/v8, HK-01b v11/v12, HK-02a v9/v10, HK-03a v13/v14** To check
  (`hooks/v8_cards.py`); the church pairs (HK-01a v5/v6, HK-01b v9/v10) and the second-floor pair (HK-03a v11/v12) copied server-side to Old
  (Old docs HK-01a v3, HK-01b v5, HK-03a v6), marked `archived` + `archiveAsset` on Current and deleted from Current. Kept on Current: HK-01a v1/v3
  and HK-02a v7 (their clips were made from them), HK-01b v7. The home-stairs clips (HK-01a v1/v2, HK-01b v1, HK-02a v1) stay as versions,
  superseded — new clips follow the plaza picks. Seen in the renders (no judgement, the user checks): all eight sit on the P8 flight (three lanes,
  two steel rails, glass doors, towers); HK-01a A/B each hold N in the middle lane with eight younger people on the lower steps (two bent hands on
  knees, one on the rail); HK-01b both show the black pump mid-step beside two pairs of white trainers; HK-02a both look down the flight from the
  landing at the daughter, hand on the rail, the plaza crowd behind; HK-03a both frame the daughter from over the mother's hat and shoulder with the
  towers behind. Higgsfield cleared the queue; Kie not needed (standing fallback stays).

- same session, ~16:08–16:20 UTC — user **"the hk1 should show woman half her age behind her and the hk02-03 should be different location"** (on the plaza round).
  HK-01a/b keep the plaza (P8-PLAZA): the crowd is replaced by **one woman half her age** (thirty-five, grey sweatshirt, black leggings, white
  trainers) stopped four steps behind her, bent with both hands on her knees; HK-01b her pump mid-stride past that woman's stopped trainers.
  HK-02a/03a move to a **different location — the church steps (L-CHURCH, confirmed plate P5-CHURCH)**: the line is "Last Sunday, my daughter
  walked behind me the whole way up", so the Sunday church is the story's own place and it is not the plaza; both are image edits of P5 seen from
  its top step (§6A rule 3, HT17): HK-02a SH-HIGH down the flight at the daughter on the 4th of 8 steps, HK-03a SH-OTS over the mother's shoulder,
  the daughter one step down. Four §6A v9 prompts (`hooks/build_hooks.py --v9`, `hooks/<BEAT>.v9.prompt.txt`, all PASS, 1,168–1,185 chars; the
  first HK-02a/03a drafts failed preflight — "Keep this church…" is not the rule-3 opener and 1,225 chars — rewritten to "Keep this photo exactly
  as it is — the church…" and trimmed). Act map (`work/actmap.py`: HK-01a/b subject + framing, HK-02a/03a L-CHURCH), `STEP4_5.md` (locations:
  L-CHURCH now carries HK-02a–HK-03a, L-PLAZA HK-01a–HK-01b), `docs/actmap` (Current/Plan v10), `docs/locations` (v4); angles.py PASS. 8 renders,
  one per call (`hooks/jobs.json` `<BEAT>@v9A/B`), Higgsfield nano_banana_pro (logged nano_banana_2); balance 9,471.15 after (shared account).
  Board: **HK-01a v9/v10, HK-01b v13/v14, HK-02a v11/v12, HK-03a v15/v16** To check (`hooks/v9_cards.py`, `hooks/patch/v9.ids.json`); the v8
  plaza pairs copied to Old (Old docs HK-01a v4, HK-01b v6, HK-02a v5, HK-03a v7), marked `archived` + `archiveAsset`, deleted from Current.
  Seen (no judgement — the user checks): HK-01a A/B both on the P8 flight, N mid-flight, one younger woman in grey bent hands-on-knees below her
  (A four steps below in the same lane, B further down and one lane left); HK-01b A/B the pump mid-stride and one pair of stopped trainers with a
  hand on the knee. **HK-02a A came back with brick steps and brick treads, not P5's concrete flight** (B keeps the concrete steps, hedges, cars).
  **HK-03a A and B both put the mother in a yellow tee and jeans, not the green church dress and hat** (the N sheet's wardrobe won over the prompt);
  B also looks at the church from across the street, not down its own steps. The daughter at church is in the wardrobe lock's sweatshirt and
  shorts (N-D4 wardrobe map) — a Fix note can change it. Kie not needed; the fallback stands.

- same session, 16:20 UTC hourly Fix check + user message, ~16:20–16:35 UTC — **HK-02a Fix "this should show walking behind her"** → v10: the daughter walking up the
  church steps two steps behind her mother, both in frame from the sidewalk at the foot of the steps (SH-LOW FULL, an image edit of the confirmed P5,
  `hooks/HK-02a.v10.prompt.txt`, PASS 1,189 chars after a trim from 1,309; actmap row HK-02a re-angled low/three-quarter-back). **HK-02a v13/v14** To check;
  v11/v12 to Old (Old doc v6). Seen: both renders — N ahead in the green dress and hat on the 6th step, the daughter two steps behind with her hand on
  the black rail, the church front and doors above; on model. **P8-PLAZA confirmed by the user** (status use).
  Then the user: **"I'm seventy-one, and I take the stairs faster than women half my age — should be 1 broll here showing her walking faster going up
  the stairs and at her back woman walking behind and she likes walking faster and left them"** → **HK-01 is one B-roll for lines 1–2 (0.00 → 8.01 s)**:
  HK-01a re-planned (`work/actmap.py`: lines (1, 2), `mx=10`, N + two women half her age, "three quick steps up, N pulling away; the women behind
  climb slowly and fall further back"), **HK-01b dropped** — its Current doc deleted, its v13/v14 files copied to Old and every version kept on the Old
  HK-01b doc (`dropped: true`); act map 60 rows, 108/108 lines, angles.py PASS; `STEP4_5.md`, `docs/actmap` (v12), `docs/locations` (v5) synced.
  v11 prompt (`hooks/HK-01a.v11.prompt.txt`, PASS 1,171 chars, edit of the confirmed P8): N mid-stride on the 15th step, chin up, a small pleased smile
  in part profile; two women of thirty-five in grey and navy sweatshirts walking up slowly on the 11th and 10th steps behind her, one hand on the rail,
  looking up at her back. **HK-01a v11/v12** To check (`hooks/v11_cards.py`); v9/v10 to Old (Old doc v5). Seen: A — N ahead smiling in part profile,
  the two women three and four steps behind, one hand on the left rail; B — the same, N a step higher and turned a little more to the lens. The clip
  will be one 8 s Kling shot from the picked frame (no end frame — waived). Higgsfield balance 9,309.65.
  `fix_patterns.py` re-run (66 notes): the note that repeated today is the line's relationship — "woman half her age behind her", "walking behind
  her", "at her back woman walking behind" → **House Taste HT24 (V7.79.2)**: every person a line names as ahead, behind, beside or watching is in the
  one frame in that relation, from the side or behind, never a POV of one of them; a comparing hook line is one B-roll with all of them in it
  (standards §34A + changelog, skill summary synced).

- same session, ~16:30–16:45 UTC — user **"hk01 she is facing the wrong way"** (the v11 pair had N side-on across the steps). v12: her back to the
  lens, facing up the flight to the doors, climbing away, the edge of a smile past the hat brim; the two women behind her with their backs to the
  lens too (`hooks/HK-01a.v12.prompt.txt`, PASS 1,177 chars after two trims; `face: True` — preflight refuses a face block on a no-face call; the
  actmap framing updated). **HK-01a v13/v14** To check (`hooks/v12_cards.py`); v11/v12 to Old (Old doc v6). Seen: A — N from behind on the 15th step,
  head turned a little so her cheek and smile show, the two women two and four steps below her, one hand on the right rail; B — the same from a
  touch lower, N glancing back over her left shoulder, the women closer together on the left lane. Higgsfield balance 9,190.15 (shared account).
  Merged the default branch first (V7.80.0 arrived from another session; this build's rules unchanged).

- same session, ~16:50–17:05 UTC — user **"fix those and generate the confirmed"**. Board state read: **HK-01a v13 (A) confirmed**, **HK-02a v13 (A) confirmed**
  (their B renders v14 moved to Old — Old docs v7/v7, files deleted from Current); **HK-03a Fix "this should be the same as the hk02 location but should
  be them talking to each other"**. No `restore` requests on the Old board.
  **HK-03a v13** (`hooks/HK-03a.v13.prompt.txt`, PASS 1,194 chars): an image edit of the confirmed HK-02a v13 A (the church steps from the sidewalk,
  HT17) — N stopped on the 6th step and turned back to her daughter, hand on hip, a small smile; the daughter two steps below, hand on the black rail,
  face up, mouth open mid-word (HT24, both in frame); actmap row re-angled low/three-quarter MEDIUM from the sidewalk, `docs/actmap` v14.
  **HK-03a v17/v18** To check (`hooks/v13_cards.py`); v15/v16 to Old (Old doc v8). Seen: both renders — the same church front and steps, N turned
  back on the step looking down at the daughter, the daughter looking up with her mouth open; A has N's hand on her hip, B the hand lower.
  **Clips (§35A, Kling kling-video-v3_0, 1080p, silent, one render each, no end frame — waived):** HK-01a clip **v3** from v13 A, 8 s / 64 cr
  (`clips/HK-01a.v3.call.json`, PASS, the card's motion plan verbatim; `clips/HK-01a_v3.mp4`, 7.0 MB), HK-02a clip **v2** from v13 A, 5 s / 40 cr
  (`clips/HK-02a.v2.call.json`, PASS; `clips/HK-02a_v2.mp4`, 8.1 MB). Both To check. Seen on the contact sheets: HK-02a — N climbs two steps toward
  the doors hands free, the daughter follows two behind, hand on the rail, as planned. **HK-01a — N climbs the whole flight fast, reaches the top
  and goes in through a door that opens, while the two women stay low on the steps; faster and further than the plan's three steps** (the user
  asked for "walking faster"; their call — a Fix note can slow it). The earlier home-stairs clips stay on the cards as versions. Kling balance
  42,739 after; Higgsfield 9,019.15.

- same session, ~17:00–17:10 UTC — user "fix those": board read — **HK-01a clip v3 and HK-02a clip v2 confirmed (status use)**; **HK-03a Fix "thry should
  be at the door already for this scene"**. v14 (`hooks/HK-03a.v14.prompt.txt`, PASS 1,190 chars): the same edit of the confirmed HK-02a v13 A, the
  mother on the top landing in front of the white doors turned back, the daughter on the top step with her hand on the top of the rail (actmap row
  updated, `docs/actmap` v15). **HK-03a v19/v20** To check (`hooks/v14_cards.py`); v17/v18 to Old (Old doc v9). Seen (the user checks): **both renders
  kept the women where the source frame had them — N on the 5th–6th step, the daughter at the foot of the flight; neither is at the doors.** The
  frame edit held the positions; if the user sends it back, the next pair is built on the empty P5 plate (the women placed at the top) rather than
  on the HK-02a frame. Default branch merged (V7.81.0; its new `angles.py` anatomy-beat check, §12A-1, fails this build's locked act map — a system
  update, not applied to this running build). Higgsfield balance 8,888.15.

- same session, ~17:15–17:25 UTC — user "fix those" + board note on the v14 pair: **"i want a new angle they should be inside like at the door step"**.
  v15 (`hooks/HK-03a.v15.prompt.txt`, PASS 1,197 chars after three trims): a new setup on the user's call — from inside the church's open front doorway
  looking out, the mother on the threshold turned back to her daughter on the doorstep, hand on the rail end, mouth open mid-word, the sunlit sidewalk
  beyond (refs P5 plate, N and C2 sheets; no plate match — nothing shows the inside; actmap row: eye · three-quarter · through · MEDIUM, `docs/actmap`
  v16). **HK-03a v21/v22** To check (`hooks/v15_cards.py`); v19/v20 to Old (Old doc v10). Seen: both from inside the doorway, the two at the doorstep
  turned to each other on model; A a dim vestibule with the white door leaves either side, B brighter with dark wood door frames and the street and
  houses behind. Higgsfield balance 8,840.15.

- 17:20 UTC hourly Fix check — **HK-03a Fix on the v15 pair: "make it a close up shot"**. v16 (`hooks/HK-03a.v16.prompt.txt`, PASS 1,125 chars; the first
  draft failed §6A rule 4 "every visible hand placed" — hands stated out of frame): the same doorway setup in close, an image edit of v21 A, both
  faces filling the frame, the mother in three-quarter profile turned back, the daughter beyond her mouth open mid-word (actmap row: eye · three-quarter
  · through · CU, shallow; `docs/actmap` v17). **HK-03a v23/v24** To check (`hooks/v16_cards.py`); v21/v22 to Old (Old doc v11). Seen: A — the daughter
  left in the frame facing the mother at right, the mother's profile under the hat brim, the white door leaf and the sunlit street behind; B — the
  mother at left in profile, the daughter at right facing her, both on model. No restore requests on Old. `fix_patterns.py` re-run (73 notes): the
  HK-03a run of notes is one beat being staged (talking → at the door → inside → close up), not a repeat across beats — no new rule. Default branch
  merged (V7.83.0; this build's locks unchanged). Higgsfield balance 8,676.65.

- same session, ~17:30–17:50 UTC — user **"confirm proceed"** ×2: **HK-03a v24 (B) confirmed** (v23 to Old, Old doc v12); **HK-03a clip v1** from it
  (`clips/HK-03a.v1.call.json`, PASS; Kling 4 s / 32 cr, `clips/HK-03a_v1.mp4` 3.5 MB) on the board To check — seen: the daughter's head tilts and
  her smile opens, the mother's smile widens, the frame holds. **Act 1 (the problem, N-D1) started:** eight §6A beat prompts, every one an image edit
  of its confirmed plate (P0 stairs, P2 kitchen v2, P7 clinic; N sheet; the N-D1 wardrobe) in `body/build_act1.py` → `body/<BEAT>.v<n>.prompt.txt`.
  **My error, caught before the board:** the v1 pair (16 renders, ~34 cr) came back as photographs — the body prompts had dropped the Mode 2 render
  line that every hook prompt carried. Fixed at the source: `preflight.py` now fails any Mode 2/3/5 image call without the mode's render line
  (`MODE_LINE`; proven on the v1 call = FAIL, v2 = PASS), **LESSONS L10** (numbered L09 before the merge). The v1 pair went to the Old board as a kept version (Old docs for the eight
  beats; P-03b v1 A failed on Higgsfield, no file) and was never shown as To check. v2 (the render line restored, all PASS 991–1,187 chars):
  **P-01a v3/v4, P-01b v3/v4, P-02a v3/v4, P-03a v3/v4, P-03b v3/v4, P-04a v3/v4, P-04b v3/v4, P-05a v3/v4** To check (`body/act_cards.py`,
  `body/patch/v2.ids.json`). Seen (the user checks): the Pixar look is back on all; P-01a A has her coming down facing forward, not backwards as the
  row says; P-04b A shows the therapist's face (the prompt asked shoulders down); P-05a B the heap pushed away as planned. Higgsfield balance
  8,409.15; Kling 42,707. Note: `assemble.py --sheet` placement (V7.80.0) is newer than this build's step-5 lock — the act map is already timed on
  the song's words by `work/actmap.py` (108/108 lines); not re-run here (system updates never touch a running build).

- ~18:00 UTC — user **"fixed those and proceed"** (board: HK-03a clip v1 confirmed; P-03a / P-04a / P-04b / P-05a picked A (v3); Fix notes on
  P-01a "should be looking up the stairs and stepping backwardd", P-01b "this should be the backwards also", P-02a "this should be her at the top
  of the stairs looking down", P-03b "the brace here should be same as the p03a"). **Act map re-angled for the three stairs beats** (`work/actmap.py`,
  60 rows, 108/108; `STEP4_5.md`, `docs/actmap` v18 on Current and Plan): P-01a low · behind from the foot of the stairs (her back to the lens,
  face up to the landing, one foot reaching back down), P-01b feet backwards (toes up the stairs, heel lowering to the step below), P-02a low ·
  front from the hall floor (the whole flight, her on the top step looking down it). **v3 prompts** (`body/build_act1.py 3`, PASS 1,163–1,197
  chars; P-03b attaches the confirmed P-03a frame as Image 2 "the brace, copied exactly"): **P-01a v5/v6, P-01b v5/v6, P-02a v5/v6, P-03b v5/v6**
  To check (`body/patch/v3.ids.json`, `act_cards.py` now takes per-beat `notes` and a `P03A` frame ref); their v3/v4 pairs and the four unused B
  renders (v4 of P-03a/P-04a/P-04b/P-05a) copied to Old (Old docs v2), archived on Current, the Current files deleted. Seen (the user checks):
  P-01a both from the foot of the flight, her back to the lens, face up to the landing, hands on the rail — a still can't show the direction of
  the step, the clip will; P-01b A/B the heel reaching down, toes up the stairs; P-02a A three-quarter / B frontal, on the top step looking down the
  full flight; P-03b A/B the P-03a brace (round hinges, wide straps) around the ankle. **Act 1 clips** from the confirmed A frames
  (`clips/build_act1_clips.py`, §35A PASS 564–684 chars; Kling 3.0 1080p, no audio): **P-03a v1** 5 s / 40 cr, **P-04a v1** 4 s / 32 cr, **P-04b v1**
  5 s / 40 cr, **P-05a v1** 6 s / 48 cr — To check (`clips/<BEAT>.v1.card.json`). Seen: P-03a one pull and the brace sags back; P-04a the hands
  push the pile apart but the framing drifts and the top of her head enters at the bottom edge; P-04b the knee bends further and holds; P-05a the
  push lands, then the heap thins out and vanishes by the end and her mouth moves as if talking (told the user; a Fix is theirs to call). Higgsfield
  balance 8,257.15; Kling 42,007 (build doc v20).

- 18:20 UTC hourly Fix check + user message **"p03a and b should be connected so same braces"**. Board: P-01b picked v5 A, P-02a picked v6 B;
  P-04a / P-04b clips confirmed; P-03a clip still To check; **P-01a Fix "she should be at the top of the middle of the stairs she should never be at
  the bottom"**; **P-05a (video) Fix "make this into 3 brolls"**. Done: **P-01a v7/v8** (`body/P-01a.v4.prompt.txt`, PASS 1,200 chars — two steps
  below the landing, the crop on the upper half of the flight; act-map framing updated) — seen: both renders still put her on the lower half of the
  flight (the model kept her mid-flight; told the user; the next Fix will crop the plate to the top of the flight first). **P-03b v7/v8**
  (`P-03b.v4.prompt.txt`, PASS; `match: "frame"`, a direct image edit of the confirmed P-03a frame, job 549092c2) — seen: A seated, the P-03a brace
  around the ankle, hand on the knee; B keeps the P-03a standing pose with the brace at the ankle; the earlier v5/v6 pair to Old. **P-05 split**
  (`work/actmap.py`: P-05a lines 16–16 · P-05b 17–17 · P-05c 18–18, 62 rows, 108/108; `STEP4_5.md`, `docs/actmap` v19 on Current and Plan): on the
  song's clock P-05a gets 1.6 s, P-05b 2.4 s, P-05c 0.8 s (the T-01a cut snaps to the grid at 42.97 — FLASH on P-05a and P-05c; the user asked for
  three, told them). New cards **P-05b v1/v2** (the heap at the far edge, `P-05b.v1.prompt.txt`) and **P-05c v1/v2** (her face sat back,
  `P-05c.v1.prompt.txt`) To check; **P-05a clip v2** (3 s / 24 cr, §22X: every object stays to the last frame, mouth closed — seen: the push lands,
  the heap stays, she sits back) To check, v1 kept as a version. **P-01b clip v1** (4 s / 32 cr — seen: the heel settles on the step below, the other
  foot follows, feet stay turned up the stairs) and **P-02a clip v1** (6 s / 48 cr — seen: she looks down the flight and away; her mouth opens into a
  smile mid-clip as if speaking; told the user) To check; the unused P-01b v6 and P-02a v5 to Old (Old docs v3). `act_cards.py` now sets new beats
  (`set`, base fields) and strips `__delete__` on a set (first batch was refused for it). `fix_patterns.py` re-run: "connected" repeats across P1-LANDING
  and P-03a/b → **FP14** in `products/stryde/fix_patterns.md` (the second beat on one prop is an edit of the first's confirmed frame). No restore
  requests on Old. Balances as printed: Higgsfield 8,167.15; Kling 41,743 (build doc v21).

- ~18:50 UTC — user **"i want new ones on the brolls. i dont like these, you should never talk the lyrics/script in broll"**; board: **P-01a Fix
  "she should be starting from the top to show case the moving backwards"**, **P-01b clip Fix "this hsould be stepping backwards"**, P-01b picked v5 A,
  P-02a picked v6 B. **Rule fixed at the source (V7.83.3):** §35A rule 6 + House Taste HT25 — nobody in a B-roll mouths the line; every beat video
  prompt says `mouth closed, she never speaks or sings` / `nobody speaks`; `preflight.py` fails a B-roll call without it (`NOSPEAK`; proven on the
  old P-03a call = FAIL); skill summary, CLAUDE.md version, **LESSONS L15**. **New clips** (`clips/build_act1_clips.py`, PASS): **P-01b v2** 4 s / 32 cr
  (seen: the first heel settles on the step below, but the second foot swings up and forward — still reads as climbing; a third generation waits for
  the user; the fix I'd propose is a pinned end frame with the feet one step lower, §27G rule 10 — the user waived pins on this build, so it is their
  call), **P-02a v2** 6 s / 48 cr (seen: looks down the flight and away, mouth closed throughout), **P-05a v3** 3 s / 24 cr (third generation on the
  user's own ask; seen: the push, she sits back, mouth closed, a few bottles stay to the end) — all To check; the replaced clips (P-01b v1, P-02a v1,
  P-05a v1/v2) copied to Old and archived. P-03a clip v1 (knee only, no mouth) left To check — not regenerated. **P-01a:** v7/v8 to Old; a v5 prompt on a
  crop of the plate (`plates/P0-PROP-N_top.png`, Higgsfield media 692d9e49) **still put her at the newel** (the crop kept the bottom of the flight) —
  **v9/v10 never shown**, straight to Old as kept versions (4.28 cr, agent error → **LESSONS L16**: a render that contradicts the user's note is never
  put up; fix the source first). v6 prompt (`body/P-01a.v6.prompt.txt`, PASS 1,147 chars): a direct image edit of the confirmed **P-02a v6 B** frame (her
  on the top step, the whole flight from the hall floor), stood up with her back to the lens and a foot reaching down (FP14) → **P-01a v11/v12** To
  check — seen: both at the head of the stairs from behind, hands on the rail, one slipper reaching down the step. `docs/actmap` v20 on Current and
  Plan (P-01a framing: starting from the top). Balances as printed: Higgsfield 8,085.15; Kling 41,559 (build doc v22).

- ~19:00 UTC — board: **P-01a picked v12 (B)** → **P-01a clip v1** 5 s / 40 cr To check (seen: from the top step she lowers one foot to the step
  below and the other follows, back to the lens, nobody speaks); v11 to Old. User **"THE WHOLE P03 I NEED NEW ONES THERE / FIX THEM ALL"** + board
  P-03a "NEW IMAGE", P-03b "USE THE P03A AS REFERENCE FOR THE BRACE": both beats re-staged (`work/actmap.py`: P-03a low · profile at knee height, seated
  on the kitchen chair; P-03b the same side at floor level, an edit of the P-03a frame; `STEP4_5.md`, `docs/actmap` v21): **P-03a v5/v6**
  (`body/P-03a.v7.prompt.txt`, PASS, edit of the P2 plate — seen: A seated with the right leg out, the hinged brace at the knee, hand on its top
  strap; B seated square to the table, the brace below the knee) and **P-03b v9/v10** (`P-03b.v7.prompt.txt`, PASS, a direct edit of the new P-03a A —
  seen: both the same seat and side at floor level, the brace bunched at the ankle, evening light; **if the user picks P-03a B, P-03b is made again
  from B**) To check. P-03a's old image (v3) and clip (v1) and P-03b's v7/v8 copied to Old (Old docs v3/v4), deleted from Current. Balances as printed:
  Higgsfield 8,054.15; Kling 41,519 (build doc v23).

- 19:20 UTC hourly Fix check — seven Fixes on the board. **P-01a clip** "SHOULD NOT BE STEPPING SO FAR DOWN IT SHOULD BE 1 STEP AT A TIME" → **clip v2**
  5 s / 40 cr (one slow step only, then she holds; seen: one foot lowers to the step below, the other joins, she holds), v1 to Old. **P-01b** "USE THE
  P01A AS REFERENCE HERE" → **v7/v8**, a direct edit of the confirmed P-01a v12 B frame closed in on her feet at the top of the flight (act map: low ·
  behind; seen: both from below on the top steps, slippers toes-up, the heel reaching down); the v5 image and clip v2 to Old. **P-02a** "USE A DIFFERENT
  CAMERA ANGLES" → **v7/v8** from the landing behind her shoulder, high, looking down the whole flight (act map: high · over-the-shoulder, no face;
  seen: A sitting on the top step, head down to the hall; B standing at the top with a hand on the newel — not sitting); the v6 image and clip v2 to
  Old. **P-03a** "MAKE THE BRACE A BIT MORE SHORT MUCH EASIER TO SHOW" → **v7/v8**, a short hinged brace a hand's length above and below the knee (seen:
  both seated from the side, the short brace at the knee, hand on its strap); v5/v6 to Old. **P-03b** "USE THE P03A AS REFERENCE AGAIN" → **v11/v12**,
  a direct edit of the new P-03a A (seen: the same seat at floor level, the short brace around the ankle, evening; if P-03a B is picked, P-03b is made
  again from B); v9/v10 to Old. **P-05b** "I NEED A DIFFERENT ONES HERE" → **v3/v4**, a different picture: at floor level by her chair, a dropped knee
  sleeve and a pill bottle beside her slipper (seen: both as asked, A with the bottle rolled, B the bottle open); v1/v2 to Old. **P-05c** same note →
  **v3/v4**, from behind her shoulder, high, head bowed over the heap on the table, no face (seen: A from behind at the table, the heap in front; B a
  wider three-quarter from behind, a sliver of profile); v1/v2 to Old. Act map rows re-staged (`work/actmap.py`, `STEP4_5.md`, `docs/actmap` v22 on
  Current and Plan). All replaced files copied to Old (Old docs: P-01a v7, P-01b v5, P-02a v5, P-03a v4, P-03b v5, P-05b/P-05c new) and deleted from
  Current. `fix_patterns.py`: the "use X as reference" notes (P1↔P0, P-03a↔P-03b, P-01a↔P-01b) are FP14 again — no new rule. No restore requests on
  Old. Balances as printed: Higgsfield 7,990.15; Kling 41,279 (build doc v24).

- ~19:40 UTC — user **"FIX THOSE"** (board: P-01a clip "SHOULD BE GOING BACK WARDS NOT UP", P-01b "SHE IS TOO BIG HERE", P-02a "WRONG LOCATION",
  P-05b / P-05c "WRONG PERSON ALSO SHOULD USE DIFFERENT TYPE OF BROLL"; P-03a picked v7 A, P-03b picked v11 A). **P-03a clip v2** 5 s / 40 cr (the hand
  pulls the short brace's strap, it sags back) and **P-03b clip v1** 4 s / 32 cr (one small foot shift) To check; the unused B renders to Old. **P-01b
  v9/v10** (`body/P-01b.v9.prompt.txt`, the same edit of the P-01a frame, a wider crop — seen: her legs small at the top, eight steps below). **P-02a
  v9/v10** (an edit of the confirmed P-02a v6 B frame, her own flight — the over-the-shoulder try had invented a landing; asked closer from mid-flight,
  **the render kept the wide framing** — told the user; a crop of the frame is the next step if they want it closer). **P-05b v5/v6** (a different kind
  of B-roll: the kitchen drawer stuffed with sleeves, a brace and pills, her hand pushing it shut — seen: A a brown hand, **B a pale hand, told the
  user**). **P-05c v5/v6** (N at the kitchen window in profile, her cast sheet attached — seen: both on model, looking out). Act map re-staged for the
  four (`docs/actmap` v23). **P-01a clip:** the third generation from the start frame alone (direction named three ways: down toward the lens, larger
  in the frame, farther from the landing; 40 cr) **still read as climbing — never shown (L16), kept on Old as v3**. The fix moves to **§27G rule 10, a
  pinned end frame**: card **P-01a-END** (v1/v2, an edit of the confirmed P-01a frame with her one step lower — seen: A both feet on the second step,
  B one foot lifting down) To check; once the user picks it, the P-01a clip runs first-and-last frame. Replaced files to Old (Old docs P-01a v9,
  P-01b v6, P-02a v6, P-03a v5, P-03b v6, P-05b v2, P-05c v2), deleted from Current. Balances as printed: Higgsfield 7,897.15; Kling 41,127 (build doc v26).

**Waiting on:** picks or Fix notes on P-01b v9/v10, P-02a v9/v10, P-05b v5/v6, P-05c v5/v6, **P-01a-END v1/v2** (the end frame); Confirm or Fix on the
clips P-03a v2, P-03b v1, P-05a v3. Then the P-01a pinned clip and the clips from the picks; then Act 2 (the wedding).

## 2026-10-01 — "FIC THESE" round (20:00–20:15 UTC)

- **P-01b** "I WANT A CLOSE SHOT OF THE LEGS HERE GOING DOWN BACLWRDS" → v11/v12 (A/B): a close side shot at step height on her legs alone (edit of the stair plate P0), the lower slipper on its step, the upper heel reaching back and down. To check. v9/v10 to Old.
- **P-05b** "WRONG DRAWER AND LOCATION" → v7/v8 (A/B): the middle drawer of the row right of the stove in her own kitchen (edit of the kitchen plate P2), pulled open and stuffed, her brown hand on its edge. To check. v5/v6 to Old.
- **P-02a** picked v9 A → clip v3 (Kling 3.0, 6 s, 48 cr): seated on the top step she looks down the flight, holds, turns her face aside, mouth closed. To check. Unused v10 to Old.
- **P-05c** picked v5 A → clip v1 (3 s, 24 cr): at the window she looks out, then her eyes drop to the sink. To check. Unused v6 to Old.
- **P-01a** — user: "I DONT NEED END FRAME IN P01" → the `P-01a-END` card dropped (its v1 A/B pair kept on **Old versions 2**, 4.28 cr), `pinEnd` removed. Clip **v4** from the confirmed start frame alone (gen 4 on the user's word; §22X: v1–v3 all read her stance on the top step, facing the landing, as a climb → the motion renamed as *backing away from the landing*: she sinks lower in the frame, her head drops below the window, the landing stays empty; 4 s, 32 cr). What I see: she backs down the flight toward the lens one step at a time, about four steps — the direction is finally right. To check; "Use only up to here" trims it to one step if wanted.
- **Old board full (1 GB).** The asset copy of the END pair failed `quota_or_state`; a new **Old 2** overflow board was published from the template (`BOARD_ROLE "old"`, title "STRYDE · 71 Stairs Pixar Song Old Versions 2") — https://claude.ai/artifact/SpS5N8dHyFM449QEpvgX4j — with its `builds` doc (`boards.old2`) and the `P-01a-END` Old doc. From now on replaced / unchosen renders go to Old 2; `boards.old2` + `boardsNote` written on all four build docs. `body/old_ids.json` marks Old 2 ids with an `old2:` prefix.
- Balances: Higgsfield 7814.15 · Kling 40793.
- Standards on the default branch moved to V7.85.0 (the Visual Pitch) — not applied to this running build (step-2 lock).

Waiting on: picks or Fix notes on P-01b v11/v12, P-05b v7/v8; Confirm or Fix on the clips P-01a v4, P-02a v3, P-05c v1, P-03a v2, P-03b v1.

## 2026-10-01 — P-01a clip v5 (user: "P01 SHOULD BE WALKING BACKRWARDS SLOWLY ONE STEP AT A TIME NOT SKIPPING STEPS OF THE STAIRS", 20:12 UTC)

- The user had pressed Confirm on v4 on the board, then sent this Fix in chat — the chat Fix is the later word, so v4 was replaced: copied to **Old 2** (`c74a4cf5…`, its Old doc there), deleted from Current.
- **Clip v5** (Kling 3.0, 5 s, 40 cr) from the same confirmed start frame: the "backs away from the landing" framing kept (it was what finally made v4 go down), the pace named outright — slowly, one step at a time, each heel to the step directly below, both feet on it before the next, two steps in the whole clip, never a step skipped. What I see: she backs down toward the lens slowly, one step at a time onto consecutive steps, face to the landing. To check.
- **Lesson L18 / V7.85.1** (PR #340, merged): the v1 note "1 STEP AT A TIME" was treated as settled once v4 went the right way — every Fix note on a shot now stays in force for every later generation: §22X, `preflight.py` fails a generation 3+ call without `fix_notes_all` (the clip builder writes it: `FIXALL`), LESSONS L18.
- Balances: Higgsfield 7814.15 · Kling 40633.

Waiting on: Confirm or Fix on the clip P-01a v5; picks or Fix notes on P-01b v11/v12, P-05b v7/v8; Confirm or Fix on the clips P-02a v3, P-05c v1, P-03a v2, P-03b v1.

## 2026-10-01 — 20:21 UTC hourly Fix check

- **P-03a** image Fix "THE BRACE SHOULD BE IN SHOULD ONE KNEE" (the v7 A frame's lower cuff sat behind the near shin and read as a brace across both legs) → v9/v10 (A/B): an edit of that confirmed frame changing only the brace — one short hinged brace on her right leg alone, both cuffs on that leg, the left leg bare and apart. To check. v7 A → **Old 2** (`185b07ce…`); the clip v2 made from it → Old 2 (`4fe78942…`), archived; the card waits for the new pick (status `ready`). **P-03b was made as an edit of the old P-03a frame (FP14)** — it is confirmed and untouched; if the user wants it to match the new P-03a brace, that is their call.
- **P-05c** clip Fix "NO TALKING ABOUT THE MUSIC" (the face strip at 6 fps shows her mouth opening as if singing along, although the prompt carried the mouth-closed clause at its end) → clip v2 (3 s, 24 cr): the lips clause first and strongest — lips sealed, jaw still, a silent clip, only the eyes move. Checked at 6 fps: lips closed first frame to last. To check. v1 → Old 2 (`6c1e2f26…`).
- `fix_patterns.py` on Current + Old + Old 2: two repeats written as rules — the mouth moved on three beats with the clause late in the prompt (HT25: the lips clause leads the prompt on any face-visible shot, V7.85.2); the team has dropped every pinned end frame on this build (hooks, P-01a) → `products/stryde/fix_patterns.md` FP15.
- Balances: Higgsfield 7706.15 · Kling 40579.

Waiting on: picks on P-03a v9/v10, P-01b v11/v12, P-05b v7/v8; Confirm or Fix on the clips P-01a v5, P-02a v3, P-05c v2, P-03b v1.

## 2026-10-01 — "FIX THOSE" round 3 (20:35 UTC)

- The user confirmed on the board: **P-01a clip v5, P-02a clip v3, P-05c clip v2, P-03b clip v1** (`use`); picked **P-05b v7 A**.
- **P-03a** "FIX THE IMAGE AND USE THE P03B AS REFERNCE FOR THE BRACE" → v11/v12 (A/B): an edit of the v9 A frame with the confirmed P-03b frame attached as Image 2 — the same short black hinged brace (straps, round side hinge, size) on her right knee, slid below the kneecap. To check. v9/v10 → Old 2 (`18284a81…` / `0be6c808…`), deleted from Current.
- **P-05b** clip v1 (3 s, 24 cr) from the pick: her hand pushes the stuffed drawer shut, it jams, a sleeve cuff caught over the edge. Unused v8 B → Old 2 (`b883a503…`).
- **P-01b card vanished from the Current board** (the 20:28 list of 73 docs had no P-01b; it was written at version 24 in the FIC THESE round and nothing in this session deleted it — the same thing happened to `P-01a-END` earlier). Re-set from the local mirror `board/json/beat_P-01b.json` (v11/v12 To check, both files still in the store). Cause unknown; every Fix check now compares the board's beats with the act map and re-sets any missing beat from its mirror.
- Balances: Higgsfield 7660.15 · Kling see below.
- P-05b clip v1 landed (what I see: the hand reaches but the drawer never shuts, the view widens at the end) — To check, the user decides. Kling 40325.

Waiting on: picks on P-03a v11/v12, P-01b v11/v12; Confirm or Fix on the clip P-05b v1.

## 2026-10-01 — "FIX THOSE" round 4 (21:00 UTC)

- The user picked **P-03a v11 A** and confirmed the **P-05b clip** (`use`).
- **P-01b** "WRONG PERSON" (the v11/v12 legs were a slim young woman's) → v13/v14 (A/B): the stair plate as Image 1 and the confirmed P-01a frame (her on the top step from behind) as Image 2 to copy her from — seventy-one, deep brown skin, heavy calves, thick ankles, her dress and slippers. To check (A from the side through the balusters, B from behind on the flight). v11/v12 → Old 2 (`64f1a064…` / `50a562cc…`). The V7.86.0 preflight now asks Mode 2 image prompts for a scale cue (§24O rule 3) and the stylised-hand line (rule 5): both written in.
- **P-03a** clip v3 (5 s, 40 cr) on the picked frame (generation 1 on the new frame): her hand hauls the brace up, it sags back down toward the ankle. To check. Unused v12 B → Old 2 (`be36efa5…`).
- Standards on the default branch moved to V7.86.0 (music-video camera, cast-sheet views) — merged into this branch; not applied to this running build beyond the preflight checks above.
- Balances: Higgsfield 7646.15 · Kling 40245.

Waiting on: a pick on P-01b v13/v14; Confirm or Fix on the clip P-03a v3. Then Act 1 is complete and the Act 2 B-roll images begin.

## 2026-10-01 — "FIX THOSE" round 5 (21:15 UTC)

- The user picked **P-01b v13 A** → clip v3 (4 s, 32 cr; the first clip on this frame): through the balusters the lower slipper settles on the step below, the upper foot follows down. To check. Unused v14 B → Old 2 (`e0b7ba5b…`).
- **P-03a** clip Fix "IT SHOULD FEELING DRIFTING DOWN" (v3 had her pull the brace up and it sagged back) → the act-map row's action and pace changed ("the brace drifts slowly down her shin on its own, her hand letting it go · one slow slide, about three seconds"; `actmap.py` PASS, STEP4_5 / `docs/actmap` v24 re-synced on Current + Plan, `motionPlan` on the card) → clip v4 (5 s, 40 cr): her hand lifts off to her thigh and the brace slides slowly down to just above the ankle. To check. v3 → Old 2 (`ee2be8f5…`).
- Balances: Higgsfield 7633.15 · Kling 40093.

Waiting on: Confirm or Fix on the clips P-01b v3 and P-03a v4. Then Act 1 is complete and the Act 2 B-roll images begin.

## 2026-10-01 — "FIX THOSE" round 6 (21:30 UTC)

- **P-01b** clip Fix "FIX HER STEPS" (the feet strip of v3 shows her slippers shuffling and crossing on one tread, never landing step by step) → clip v4 (4 s, 32 cr; generation 2 on the v13 frame): the one backward step spelled foot by foot — right slipper straight back and down, flat on the very next tread, heel first; the left joins it beside it, feet parallel a hand apart, each landing once. v3 → Old 2 (`39ab7a3a…`).
- **P-03a** clip Fix "SHOULD BE FALLING WHILE DRIFTING DOWN" → the act-map row's action/pace changed again ("the brace slips loose and falls down her shin, drifting to her ankle · one fall, about two seconds"; `docs/actmap` v25 on Current + Plan) → clip v5 (5 s, 40 cr; generation 3 on the v11 frame, sent on the user's "FIX THOSE" — `user_go` and `fix_notes_all` on the call): the top strap pops off the kneecap and the brace drops down her shin under its own weight to rest at the ankle. v4 → Old 2 (`2bf17fd5…`).
- New STRYDE rule **FP16** (repeat across P-01a and P-01b): a step on the stairs is spelled foot by foot — never "she steps down" alone.
- What I see: **P-01b v4** — each slipper lands flat on the next tread, one at a time, no shuffling or crossing; but the picked frame (v13 A) has her toes pointing down the stairs, so it reads as walking down forwards, not backwards (the v1 note "this should be stepping backwards" stays in force — L18). Put up To check with that flagged; a backwards version needs a new image pair facing up the stairs, the user's call. **P-03a v5** — the brace slides off the knee and drops down the shin to rest at the ankle. Both To check.
- Balances: Higgsfield 7623.15 · Kling 39941.

Waiting on: Confirm or Fix on the clips P-01b v4 and P-03a v5.

## 2026-10-01 — "FIX THOSE" round 7 (21:30–21:45 UTC)

- **P-01b** image Fix "NEW IMAGE PROPER FOOTING" (v13 had her toes pointing down the flight and the upper slipper half off its tread) → v15/v16 (A/B): facing UP the stairs — toes toward the landing, heels toward the lower steps, so she goes down backwards — each slipper whole and flat on its own tread; stair plate + her confirmed P-01a frame. The first A came out facing down the flight with a slipper off the edge and a grey dress — kept off the board (L16) on Old 2 (`1d43fe56…`, 2.14 cr); re-rendered with the direction tied to the way the handrail rises and her blue floral dress named. A and B are both from behind on the flight. v13 image and its clip v4 → Old 2. To check.
- **P-03a** clip Fix "THE KNEE BRACE DRIFTS DOWN THEN PULL IT UP AGAIN" → act-map row changed ("the brace drifts down her shin, then her hand pulls it back up over the knee · one slide down, one pull up"; `docs/actmap` v26). Clip v6 (40 cr): the brace fell to her ankle, she bent into frame to pull it and her mouth opened in a smile — the standing no-speech note broken, so it was never shown (L16, **L23**, STRYDE **FP17**); kept on Old 2 (`e98e775c…`). Clip v7 (40 cr): the brace drifts only to mid-shin, she stays upright with her head out of frame, the hand pulls it back over the knee. v5 → Old 2.
- What I see on **P-03a v7**: the brace still drops to her ankle (not mid-shin), she reaches down and hauls it back over the knee and holds it; her face dips into the top of the frame for about a second, mouth closed. No Fix note broken, so it is up To check with that flagged.
- Spent this round: Higgsfield 3 renders (6.42 cr), Kling 80 cr (v6 + v7). Balances: Higgsfield 7603.15 · Kling 39861.

Waiting on: a pick on P-01b v15/v16; Confirm or Fix on the clip P-03a v7.

## 2026-10-01 — "GENERATE" / "CONFIRM PROCEED" (21:40 UTC): Act 1 last clip, Act 2 images

- The user picked **P-01b v15 A** and confirmed the **P-03a clip v7** — Act 1 waits only on the P-01b clip.
- **P-01b** clip v5 (4 s, 32 cr; the first clip on the new frame): from behind, she steps backwards toward the lens one step, foot by foot (FP16), and ends one step lower facing up the stairs. To check. Unused v16 B → Old 2 (`62feeee1…`).
- **Act 2 — the wedding (N-D2), seven beats T-01a…T-04b**: A/B pairs on Higgsfield nano_banana_pro (14 renders), each an image edit of the confirmed **P3-RECEPTION** plate (Image 1) with the build's style frame attached (P-05c v5 A, `kind: style`, §24O rule 2); C1-LORETTA sheet on T-01b, N-NARR sheet on T-04a; wardrobe per N-D2 (N lavender chiffon + pearl studs; Loretta royal-blue satin + white slip-ons). Builder: `body2/build_act2.py` (all seven `preflight.py` PASS, with the V7.86.0 scale / facing / stylised-hands lines). Laughs written as closed-mouth grins so no clip reads as singing (HT25). **T-03a** "Both her knees was bone on bone too" → anatomy style **S2 X-ray** (a wear line, §12A-1): two knees in profile, the joint gap gone, a red-orange glow where bone meets bone. All seven To check; what I see is on each card (T-03a B has a stray small panel top right; T-04b's tablecloth hangs a little oddly over the knee).
- Balances: Higgsfield 7563.15 · Kling 39629.

Waiting on: Confirm or Fix on the P-01b clip v5; picks or Fix notes on the seven Act 2 pairs (T-01a, T-01b, T-02a, T-02b, T-03a, T-04a, T-04b).

## 2026-10-01 — "I WANT NEW IMAGES IN ALL OF THEM I WANT NEW WARDROBE TOO" (21:45–22:00 UTC): Act 2 redone

- **New N-D2 wardrobe** (wardrobe map in `STEP4_5.md`, `docs/wardrobe` v3 on Current + Plan): N in a **burgundy chiffon dress to mid-calf with flutter sleeves, gold hoop earrings, low gold heels** (was lavender chiffon, pearl studs); Loretta in a **fuchsia satin dress to the knee, white slip-on sneakers** (was royal-blue satin). Emerald was not used: it is N's church dress (N-D4), and §14A keeps every day's dress different.
- **New pictures** on all seven rows (`work/actmap.py`; `angles.py` PASS; `docs/actmap` v28 on Current + Plan):
  - T-01a: the bride hugs N at the edge of the floor, eye level.
  - T-01b: Loretta waves both hands overhead, from low.
  - T-02a: the line dance seen from high above the tables.
  - T-02b: the feet from the side at floor level.
  - T-03a: the S2 X-ray, now front-on on both knees.
  - T-04a: over N's shoulder to Loretta dancing.
  - T-04b: N's hand on her knee, front-on under the table.
- The act map's Act 8 cut order and Flags section on the board were re-synced from `STEP4_5.md`. The board held a stale 61-beat cut order.
- **The 14 new renders** come from `body2/build_act2.py`, written as `body2/T-*.v3.prompt.txt` / `.preflight.json`. All 7 prompts PASS. Each pair is v3 A / v4 B on Higgsfield `nano_banana_pro` (logged `nano_banana_2`, 2k, 9:16).
  - The sheets go in for the face and hair only, per HT26. Each prompt names the sheet's clothes as not worn: N's mustard top and denim skirt, Loretta's teal blouse and khaki shorts.
  - All 14 are To check, with `imagePair [3,4]`.
- What I see:
  - The wardrobe is right on all seven.
  - **T-01b A** has a stray guest's back at the left edge. B is clean.
  - **T-02a A** has six dancers, B has seven.
  - No Fix note is broken. There were no Fix notes on Act 2.
- The replaced v1/v2 pairs are on **Old 2**: the 14 files were copied server-side, and Old 2 now has docs for T-01a…T-04b. On Current they are marked `archived`, and their files are deleted from Current.
  - T-01a and T-04b had been confirmed (A). The user's ask replaces them, so they are back To check.
- Balances: Higgsfield 7523.15 · Kling 39629.

Waiting on: picks or Fix notes on the seven Act 2 pairs (v3/v4). Confirm or Fix on the P-01b clip v5.

## 2026-10-02 — "FIX THOSE AND GENERATE THE NEXT ACT" (08:40–09:35 UTC): Act 2 Fixes and clips, Act 3 pairs

- **T-02a / T-02b**: the user's Fix notes were "this should be loreta" and "wrong person". The v5/v6 pairs used Loretta's confirmed T-01b frame as Image 2:
  - T-02a uses it as `kind: character`, with Loretta leading the line nearest the lens.
  - T-02b uses it as `kind: frame`, because no face shows.
  - The user picked v5 A on both. The v6 B renders are now on **Old 2**, archived on Current, and their files deleted from Current.
  - Clips v1 were made on Kling 3.0 from the picks: T-02a is 5 s (40 cr), T-02b is 4 s (32 cr). Both are To check.
  - What I see on T-02a: Loretta side-steps at the front with the line. She smiles with her teeth showing the whole clip, but her mouth never forms words.
  - What I see on T-02b: the slip-ons and hem step forward in unison with the dress shoes and gold heels.
- **T-04a**: the Fix note was "SHE SHOULD NOT BE THE ONLY ONE ON THE DANCE FLOOR".
  - The v5/v6 pair is an edit of the v3 A frame with the floor full of guests dancing round Loretta. It is To check, with `imagePair [5,6]`.
  - The replaced v3 A and the clip made from it (v1) are on **Old 2**, archived on Current, and their files deleted from Current. The video waits for the new pick.
- **Act 3 (R-01a…R-07c, N-D3)**: A/B pairs on Higgsfield `nano_banana_pro` (logged `nano_banana_2`, 2k, 9:16), from `body3/build_act3.py`. Product beats are PIX-SPLIT (product photos first, the strap at least a quarter of the frame, 12 × 5 cm, the kneecap's lower edge in its notch).
  - Before posting, I checked every render against the standing notes (L16). These were kept off the board, and their causes fixed at source:
    - R-03a: both first renders put her in the cast sheet's khaki shorts.
    - R-04a A: a plain band, not the strap.
    - R-06b A: printed the lyric as a caption and wore the day-one dress from the style frame.
    - R-06b B: drew the strap as a box.
    - R-07a B: a hinged brace.
    - R-07c A: a sleeve brace.
  - Re-renders (`build_act3_fix.py`, `build_act3_fix2.py`, as v3/v4 prompt files) used:
    - face-and-hair crops of the sheets (`cast/*_face.png`, HT26);
    - prompts with no speech marks;
    - a style frame with no other day's outfit;
    - the strap's shape named.
  - Still kept off after the re-renders:
    - R-03a fix B and R-06b fix B came out light-skinned.
    - R-07a and R-07c fused the strap onto a sleeve.
    - R-07a fix2 printed a caption again.
    - R-07c fix2 showed another woman.
  - The 13 kept-off renders are on **Old 2** (docs R-03a, R-04a, R-06b, R-07a, R-07c), with their credits.
  - **On the board, To check:** nine pairs (`imagePair [1,2]`). R-03a pairs fix A with fix2 B. R-04a pairs fix A with the first B. R-06b pairs fix A with fix2 B.
  - **R-07a and R-07c are single pictures** after three tries each: R-07a is the first A, R-07c the first B. The card says so, and a Fix makes a new pair.
  - Flags written on the cards:
    - R-03a B has dark trousers, not the khaki of R-03b/R-04a.
    - R-07a has her low on the flight, not at the top as the act map has it.
    - R-07c has a teal sleeve (Loretta) soft at the right edge.
- Act map rows changed in `work/actmap.py`: T-02a (Loretta leads the line), R-03b (close from low), R-06a (on her palm), R-07a (from three steps below), R-07c (three-quarter, not profile). `angles.py` PASS. The rows are synced to `STEP4_5.md` and `docs/actmap` v29 (Current and Plan).
- **System (V7.88.1, LESSONS L28):**
  - No speech marks in a picture prompt (§6A rule 5, `preflight.py` check). It was tested on the empty case and on known-good prompts.
  - The day's clothes never come from a sheet or the style frame (§24O rule 9, HT26 extended).
  - From the Fix-note patterns (three "wrong person" notes): HT27, every cast member in the frame goes in by a picture, feet-only shots too.
  - Merged over the default branch twice (V7.87.0, then V7.88.0 with its L26–L27); ours is V7.88.1 / L28.
- Balances: Higgsfield 6487.15 · Kling 39093.

Waiting on:
- Picks or Fix notes on the nine Act 3 pairs and the two Act 3 singles.
- The T-04a v5/v6 pick.
- Confirm or Fix on the T-02a and T-02b clips.

## 2026-10-02 — "fix those and generate the videos" (09:35–10:00 UTC)

**Picks on the board.** The user picked frames for:
- R-01a (v1), R-02a (v1), R-02b (v2), R-03a (v1), R-03b (v1), R-06a (v2)
- T-04a (v5)

The unpicked image of each pair is now on **Old 2**: its file was copied server-side, then archived and deleted on Current.

**Clips on Kling 3.0** (silent, 1080p, from the picks; `clips/build_act3_clips.py`):
- R-01a v1, R-02b v1, R-03b v1, T-04a v2: all To check.
- R-02a, R-03a, R-06a: the v1 clips were kept off (L16, HT25) because their mouths moved as if speaking.
  - Two of the three lines quote speech, and that quote had gone into the clip prompt.
  - Clip v2 drops the speech marks and uses a "lips sealed and jaw still" clause.
  - The v1 clips are on Old 2 with their 120 credits.
- What I see in the v2 clips:
  - R-03a v2 is clean.
  - R-02a v2: the lips part slightly near the end.
  - R-06a v2: in profile, her lips still part a little. A third generation waits for the user's go (§22X).
- Flags written on the cards:
  - R-01a: Loretta walks several steps, not one.
  - R-03b: the hem goes down over the strap instead of up.
- Clip credits: 9 × 40 + 48 + 32 = 440 Kling credits.

**Image Fixes** (`body3/build_act3_fix3.py`, v5 prompts, plus v6 for R-07a). All are new A/B pairs on Higgsfield `nano_banana_pro`, To check:
- **R-04a** "this should be loreta same clothes too": her confirmed R-03b frame is the reference (skin, rolled khaki trouser, teal blouse), per HT27. Pair v3/v4.
- **R-05a** "product too small and wrong product": the product photos come first, with the shell's shape named and the strap half the frame wide. N comes from her R-06a frame. Pair v3/v4.
  - Flag: in B the strap rests on her fingertips, not flat in her palm.
- **R-06b** "wrong product and this is not the pixar anymore": the confirmed R-03b frame is the style (a stylized leg with the strap drawn right). N's skin and clothes come from her R-06a frame. Pair v3/v4.
- **R-07a** "wrong stairs", together with **R-07c** "this should be part of the r07a so it should be one take only":
  - R-07c is merged into R-07a as one take. The act map row now covers lines 44–49, 98.25 → 105.57 s, with a 9 s call, and the card has `covers: ["R-07a","R-07c"]`.
  - The R-07c card is deleted from Current. Its render is on Old 2 (`mergedInto`).
  - The image is an edit of the confirmed **P0-PROP-N plate** (her own staircase: runner, brass rods, square newel, photo wall), with N from her R-06a frame.
  - Three renders were kept off and are on Old 2:
    - the first A drew an open-kneecap sleeve;
    - one B came back on another staircase with her hand on the rail;
    - one Higgsfield job failed (no render).
  - v6 adds the worn-strap photo, with one shell below the kneecap and the kneecap bare. The pair on the board is v2/v3.
- The replaced pairs (R-04a, R-05a, R-06b) and the old R-07a single are on Old 2.

**Act map.** R-07c is merged in `work/actmap.py` (61 rows). `angles.py` PASS. Synced to `STEP4_5.md` and `docs/actmap` v30 (Current and Plan).

**System (V7.89.1, LESSONS L30)**, merged over the default branch's V7.89.0 and its L29:
- §35A rule 6: a clip prompt's line goes in without its speech marks, and a face shot uses "lips sealed and jaw still… the face holding the expression of the frame". `preflight.py` now fails speech marks inside a clip's line. Tested: it fails the two v1 prompts and passes the good Act 2 and Act 3 calls.
- §27 rule 3: one continuous action across consecutive lines is one row and one clip (≤ 15 s).

**Balances:** Higgsfield 6467.15 · Kling 38693.

**Waiting on:**
- Picks or Fix notes on the R-04a, R-05a, R-06b and R-07a pairs.
- Confirm or Fix on the R-01a, R-02a, R-02b, R-03a, R-03b, R-06a and T-04a clips.
- The user's go before a third R-06a clip.
- The R-07a clip, a 9 s single take, waits for its image pick.

## 2026-10-02 — "fix those and proceed to the next act" (10:00–10:20 UTC): Act 3 Fixes and clips, Act 4 pairs

**Act 3 Fixes**
- **R-04a** "this should be the right knee": a new pair v5/v6 (`body3/R-04a.v7`). Both knees are front-on; the strap is on her RIGHT knee at frame left and her left knee is bare at frame right. The skin and clothes come from Loretta's R-03b frame. The R-04a v3/v4 pair is on Old 2.
  - New product rule **FP18** (`products/stryde/fix_patterns.md`): name the strap's knee in picture terms.
- **R-07a** "she should be at the 2nd floor": an edit of the v2 frame (her own staircase). She is near the top under the second-floor landing, and the full flight below her is empty.
  - The v8 pair is on the board as v4/v5.
  - The v7 tries were kept off: B came out mid-flight, and A failed on Higgsfield. The v2/v3 pair is on Old 2.
- **R-03b clip** "she should be showing it not hiding": clip v2 pushes the hem up. It still slides down over the strap midway, and the strap shows again at the end. It is on the board with that note. A third generation waits for the user's go (§22X).

**Act 3 clips from the user's picks**
- **R-05a** (pick v4): clip v1 bent and curled the strap in her hand, so it was kept off (L16, rigid product) and is on Old 2.
  - Clip v2 keeps the palm flat and the strap rigid. Her fingers curl up briefly near the 4-second mark.
- **R-06b** (pick v4): clip v1 is clean.
- The unused images of both pairs are on Old 2.

**Act 4 (M-01a…M-06a)**: A/B pairs on Higgsfield `nano_banana_pro` (`body4/build_act4.py`), all To check.
- M-01a: an overhead shot of N on the PT table (P7 plate, her P-04b clinic frame as reference).
- M-04a: an edit of the confirmed P-04a frame, with her hands taken out and a syringe box added.
- M-06a: a ground-level shot of her slipper on the runner, with the strap on her right knee.
  - Pair v1A + C. The B render had a light-skinned leg, so it was kept off and is on Old 2.
- **Anatomy styles (§12A-1, new beats):**
  - M-02a: S2 X-ray card, with the T-03a X-ray as the style. Flag: B also draws a loose strap under the X-ray.
  - M-03a: S1 Ghost, with `references/anatomy/S1_ghost.webp` attached as the style.
  - M-05a: S7 cross-section.
  - M-05b: S1 Ghost with the strap.
  - The card records each style as `anatStyle`.

**Balances:** Higgsfield 6389.65 · Kling 38525.

**Waiting on:**
- Picks on R-04a, R-07a and all seven Act 4 pairs.
- Confirm or Fix on the R-03b v2, R-05a v2 and R-06b clips, plus the user's go for a third R-03b clip.
- After the R-07a pick, the 9 s one-take clip.

### 2026-10-02 10:20–10:45 UTC — "fix those and proceed to the next act" + "about all the anatomy here we will use the normal anatomy / fix those"

**The team's anatomy call:** every Act 4 anatomy beat is now the normal anatomy model. That is S3: natural tissue colours (red muscle, white tendons, ivory bone) on pale grey, with P-04a as the light frame only.
- This covers M-02a, M-03a, M-05a and M-05b.
- The earlier S1 Ghost, S2 X-ray and S7 versions are on Old 2. That includes M-05b v1, which the user had confirmed; "Use this" on Old 2 brings it back.
- The new pairs are To check:
  - M-02a v3/v4: two knee models, a sleeve on the left and the strap on the right.
  - M-03a v3/v4: side profile, a red point on the tendon.
  - M-05a v3/v4: the leg model with a sleeve outline and red pressure lines.
  - M-05b v3/v4: the strap seated, red fading to blue.
- **Kept off (L16), all on Old 2:**
  - M-02a v2: the X-ray Fix for "fix the product and placement", superseded before it was shown.
  - M-02a v3 pair: the worn-strap photo printed a real hairy leg and a room under the models. The worn photo is now dropped from anatomy beats (L34).
  - M-05b first A: the strap alone on a table.
- **System:** V7.89.3, §12A-1 rules 7–8, `angles.py` `anat.lock`, `preflight.py` (anatomy + worn photo fails). LESSONS L34.

**R-03b image Fix** "make her look like she is showing the stryde strap like flexing it": an image edit of her confirmed v1 A frame. Her right leg (frame left) stretches toward the lens, both hands present the strap, and she grins. The v4 pair is To check.
- **Kept off, all on Old 2:**
  - v3 A: a different woman.
  - v3 B: the strap on her left knee (FP18).
  - v4 B: a different woman in a hinged brace. B was re-rendered once (B2) with the same prompt.
- `preflight.py` could not pass an image edit that shows the product: product-first and edit-first conflicted. Now the edited picture is Image 1 and the product photo comes right after it (§6A, L35).
- v1 A (the old pick) is on Old 2. Clip v2 stays as the card's video until a new pick gets its clip.

**Clips from the picks (Kling 3.0, 1080p, silent), all To check:**
- M-01a, 6 s: v1 opened her mouth as her head settled (HT25), so it was kept off and is on Old 2. v2 holds her still with a slow push down.
- M-04a, 5 s: a slow push on the still heap.
- M-06a, 4 s: the slipper lands. Her leg then turns side-on and the strap is seen from the side.
- R-04a, 5 s: her fingertip taps the shell, with a slow push.
- R-07a, 9 s: one take of the whole walk down, hands off the rail, mouth closed.
- The unused images of each pair are on Old 2: M-01a v1, M-04a v2, M-06a v1, R-04a v6 and R-07a v5.

**Balances:** Higgsfield 6316.15 · Kling 38245 · Kie 261969.8.

**Waiting on:**
- Picks on the four anatomy pairs and on R-03b v4.
- Confirm or Fix on the five new clips, plus the earlier R-03b v2, R-05a v2 and R-06b clips.
- After the anatomy picks: their clips. M-02a, M-03a, M-05a and M-05b have no clip yet.

### 2026-10-02 ~11:05–11:20 UTC — "use the new pixar anatomy for all the anatomy / lets re do all the anatomy" + "the t03a too"

**Pixar anatomy (V7.90.2 Pixar S3, the team's locked no-muscle "normal anatomy")** is now on every anatomy beat. The look is written in words; `references/anatomy/S3_pixar_locked.jpg` is the bar each render was judged against and is never attached. The new pairs, all To check:
- M-02a v5/v6: two knee models, a sleeve on the left and the strap on the right.
- M-03a v5/v6: side profile, a warm glow on the tendon under the kneecap.
- M-05a v5/v6: a sleeve outline, the glow under the kneecap, warm lines down the thigh.
- M-05b v5/v6: the strap seated, warm fading to cool blue.
- T-03a v5/v6: both knees bone on bone, a warm glow where the bones meet.

What moved to Old 2:
- The realistic S3 versions of the four Act 4 beats.
- T-03a's confirmed S2 X-ray pick (v4). "Use this" brings it back.
- T-03a's clip v1 stays on the card until a new pick gets its clip. The status is planned.

**Kept off (L16, L36), on Old 2:** M-02a v5 A, M-05a v3 B and T-03a v5 A. The P-04a kitchen-table frame, attached "for the light only", drew its table, hands and brace around the models. Each slot was re-rendered once without the frame (M-02a v6, M-05a v4, T-03a v6). As a result, those three pairs mix two prompts that differ only by that frame.

**M-06a "wrong person":** a new pair with N herself in frame, from her confirmed R-07a v8 A frame (HT27): pink cardigan, denim skirt, silver twist-out, the strap on her right knee (frame left). Both renders framed her full-length coming down the stairs, so the strap reads small. Her old pick (v2) is on Old 2, and clip v1 stays until a new pick gets its clip.

**System (V7.90.3, L36):**
- "Normal anatomy" is S3 in the build's own mode.
- `ANAT-PIX` and the style line merge into one look paragraph so the beat fits §6A.
- No scene frame as the style on an anatomy beat.
- `pixar_anatomy: true` runs the Pixar checks on this pre-V7.90 build. `legacy_build` had switched them off.

**Balances:** Higgsfield 6195.15 (this account's private workspace; the ODAQ B.V. rule is for the other account) · Kling 38245.

**Waiting on:**
- Picks on M-02a, M-03a, M-05a, M-05b, T-03a, M-06a and R-03b. After the picks come the clips.
- Confirm or Fix on the clips To check.

### 2026-10-02 ~11:25–11:35 UTC — "fix those and generate the videos"

**Fixes, new pairs To check:**
- **M-03a** "the poin is the patellar tendon" (on the pick v5): an image edit of v5 (v7/v8). The tendon is drawn as a broad ribbon from the kneecap tip to the shin bump, with the glow on its middle and none on the kneecap.
- **M-05a** "the point is the patellar tendon": a new pair (v7/v8) with the same tendon wording. The first A put the glow on the kneecap again, so it was kept off and re-rendered once (A2).
- **M-06a** "i want a close up shot of the feet": a ground-level close-up of her feet in tan slippers landing on the runner, with the strap on her right knee (frame left) at the top of the frame (v5/v6). Her R-07a v8 A frame is the reference ("wrong person" still in force). The first B drew a hinged brace, so it was kept off and re-rendered once (B2). The old clip v1 stays on the card until a new pick gets its clip.
- The two repeated notes are now **FP21** (`products/stryde/fix_patterns.md`): the pain point sits on the patellar tendon ribbon, never on the kneecap.

**Clips on the confirmed Pixar picks (Kling 3.0, 1080p, silent, slow R4 push), To check:**
- **M-02a** v1, 6 s: the glow settles under the strap.
- **M-05b** v1, 5 s: warm fades to cool blue down the tendon.
- **T-03a** v2, 4 s: the bone-on-bone glow pulses once. The old X-ray clip v1 is on Old 2.
- The unused images of those pairs (v6) are on Old 2.

**Balances:** Higgsfield 6157.15 · Kling 38125.

**Waiting on:**
- Picks on M-03a, M-05a, M-06a and R-03b, then their clips.
- Confirm or Fix on the new clips.

### 2026-10-02 ~11:35–11:50 UTC — "R-03b video of this / and fix those and generate the next act"

**Clips, To check (Kling 3.0, 1080p, silent):**
- **R-03b** v3, 4 s, on the pick v3. This is the shot's third generation; the user's message was the go. She holds the pose with the strap to the lens, mouth closed, and tilts her head once with pride. Clip v2 and the unused image v4 are on Old 2.
- **M-02a** v2, 6 s. Fix "dont change the shape of the product": in v1 the camera pushed in and Kling redrew the strap as it grew in frame. v2 locks the camera and says the strap is one rigid object with the same outline in every frame. Only the glow under it builds. Clip v1 is on Old 2.
- **M-03a** v1, 5 s, on the pick v7: the glow on the tendon ribbon pulses once. The unused image v8 is on Old 2.

**Fix, new pair To check:**
- **M-06a** "wrong product and she should be going down the stairs not side ways": new pair v7/v8, shot from the foot of the stairs straight up the flight as she steps down toward the lens. The strap's shape is spelled out: the shell, two peaks round the notch, chrome slides, and the band round the back.
  - A: her front foot wears an open-toe slide, not her closed slipper.
  - B: closed slippers, three-quarter view.
  - v5/v6 are on Old 2. The old clip waits for the new pick.

**Act 5 (PR-01a…PR-06a), first pairs To check:**
- Kept off and re-rendered once (L16), with the first renders on Old 2:
  - PR-01a A printed the sung line as a caption.
  - PR-06a A drew the band as a separate loop.
  - PR-04a A drew two straps on one leg, and so did its re-render. The cause was the `In frame` list: it never counted the strap. The prompt now counts it (PR-04a v2, "exactly one strap on her right knee, her left leg bare"), and the A from it is clean.
- For your eye:
  - PR-05a's A and B both read closer to photographic than storybook.
  - PR-05b's trouser hem is rolled above the knee, not falling over the strap.
- PR-01a A is the second caption in this build (after R-06b A), with only the `For the line "…":` speech marks in the prompt. If it happens again, the proposed fix is the line without its speech marks in image prompts. Not changed yet.

**System (V7.90.4, L41):** a product shot's `In frame` list counts the product. `preflight.py` fails a product shot whose inventory doesn't count it.

**Balances:** Higgsfield 6116.65 · Kling 38005.

**Waiting on:**
- Picks on M-06a and on all seven Act 5 pairs, then their clips.
- Confirm or Fix on the R-03b, M-02a and M-03a clips.

### 2026-10-02 ~12:20–12:45 UTC — "fix those and generate the next act"

**Image Fixes, new pairs To check:**
- **M-06a** "wrong locastion": an image edit of her own staircase. The base is a crop of the confirmed R-07a v8 A frame round her legs (`body4/M06_base_R07crop.png`, Higgsfield media 6279fb3c). The strap is corrected from the front photo.
  - The first A drew pale legs on another staircase, so it was kept off (Old 2) and re-rendered once.
  - The new A and B are both her runner and brass rods, her skin and her slippers.
- **PR-03a** "fwrong product" and **PR-06a** "wrong product": the peaks had been drawn as horns at the shell's ends, and the band coiled. The shape line now puts two matching peaks close together at the middle, sloping down to a slide at each end (FP22, L47). PR-06a's strap lies flat with the band out straight.
- **PR-05b** "product placemetn is too low": the notch now cups the bottom of the kneecap, on the tendon. The trouser hem is still rolled above the knee.

**Clips, To check (Kling 3.0, 1080p, silent):**
- **M-02a** v3, 6 s. Fix "you should show blue glow to show that the stryde is better". The glow under the strap cools from amber to blue while the left knee keeps its amber. Locked camera; the strap keeps its shape. This is the shot's third generation; the user's "fix those" was the go. Clip v2 is on Old 2.
- **M-05a** v1, 5 s: pressure pulses down the thigh into the tendon spot.
- **PR-01a** v1, 4 s: he seats the strap.
- **PR-02a** v1, 5 s: she swings the strap to the lens and seats it on the model. The end frame was waived by the user's 2026-10-01 words. Flagged: the strap flattens mid-swing, and she grins open-mouthed once.
- **PR-04a** v1, 5 s: three jogging strides, one strap.
- **PR-05a** v1, 5 s: she seats the strap.
- The unused images of the picked pairs are on Old 2.

**Act 6 (L-01a…L-03a), the store-walk day N-D6, first pairs To check:**
- N wears a coral windbreaker, white T-shirt, light-blue jeans, white sneakers and a canvas tote, and goes in by her face-and-hair crop.
- Street and store shots are edits of P6-STREET and P4-STORE.
- L-03a's living room takes its materials from P0. The husband is a one-off, written in words.
- L-01b A's first job failed on Higgsfield and was resubmitted.
- L-03a A printed the line as a title, so it was kept off and re-rendered in the new form (below).

**System (V7.90.7, L46):**
- A picture prompt opens `For the line — … —:`, never with speech marks. This was the third caption from the opener's marks (R-06b, PR-01a, L-03a).
- `preflight.py` now fails any speech mark in an image prompt; clip prompts keep theirs.
- L47 / FP22: the short shape line keeps where the peaks sit.

**Balances:** Higgsfield 5995.65 · Kling 37765.

**Waiting on:**
- Picks on M-06a, PR-03a, PR-05b, PR-06a and the five Act 6 pairs.
- Confirm or Fix on the six new clips.

### 2026-10-02 ~13:00–13:40 UTC — "fix those and generate the next act" (Act 7)

**Fixes:**
- **M-05a clip v2** (Fix "should showcase the patellartendon is the one getting that animatuon"), 5 s: the glow now runs down the patellar tendon ribbon and pulses on it. The thigh lines stay still. Clip v1 is on Old 3.
- **PR-05b image v3 pair** (Fix "should show productive broll not showing the product"):
  - An edit of her R-07a v8 A staircase. She comes down facing the lens with a basket of folded towels, in a pale-yellow top and navy trousers, the strap hidden under them.
  - Act map row changed to L-N-STAIRS, CONCEALED, one step toward the lens (pin waived per the user's 2026-10-01 words). Card motion plan updated to match.
- **PR-06a image v3 pair** (Fix "should be the normal and not the long strap"): the normal strap lies by the mug with only a short stub of band past each slide. B shows her lap at the bottom edge, as the P-04a frame does. FP22 is amended and L48 written (below).

**Clips on the picks** (Kling 3.0, 1080p, silent; To check):
- L-01a, L-01b, L-02a, L-02b, L-03a.
- M-06a v2: the clip on the new v9 frame. Clip v1, made from the old v2 frame, is on Old 3.
- PR-03a. Flagged: mid-clip the golfer snaps back to address the ball and swings again, which reads as a jump.

**Act 7 (C-01a, C-02a, C-02b, C-03b, C-04a, C-05a), first pairs To check:**
- C-02a and C-02b are edits of P5. C-04a is an edit of P7. C-05a is an edit of P04A with the cheap copies.
- C-03b is Pixar anatomy S3 (`pixar_anatomy: true`, the M-05b look as style).
- C-02b v1 A and B each printed a film-style title ("Storybook in the Future", "PROUD STEPS"). Both were kept off (L16), copied to Old 3, and re-rendered once with the no-lettering clause. Flagged: the new C-02b A shows four watching ladies instead of three.

**Old 3 board created:** Old 2 hit its 1 GB store. https://claude.ai/artifact/NzdjptHWkDLzvNkmMzn78k
- `boards.old3` is set on the build doc on every board.
- 13 replaced or unused files were moved to Old 3 (copies confirmed) and deleted from Current.

**System (owner account):** FP22 is amended. A loose strap is written as "only a short stub of black band past each slide, not stretched long, never coiled", never "the band laid out straight" (L48).

**Balances:** Higgsfield 5949.65 · Kling 37333.

**Waiting on:**
- Picks on PR-05b, PR-06a and the six Act 7 pairs.
- Confirm or Fix on the eight new clips: M-05a, L-01a, L-01b, L-02a, L-02b, L-03a, M-06a, PR-03a.

### 2026-10-02 ~13:40–14:10 UTC — "fix those and generate the next act" (Act 8)

**Board read first (L49):** two cards on `regenerate`, C-02a and C-02b (image Fix "not a pixar" on both). Clips were owed on the picks C-01a, C-03b, C-04a, C-05a (v1), PR-05b and PR-06a (v5).

**Fixes, "not a pixar" — new pairs To check:**
- Cause: the church ladies have no cast sheet. They were written in words only, and the one style frame was hands on a table (P-04a), so the model drew realistic small-headed bodies.
- Fix: every woman's build is given in heads from the §24A elder ladder ("about 5.5 heads tall, big round heads, soft round bodies, big eyes"). The style frame is the PR-04a jogger, a confirmed full-body Pixar character who is not Loretta.
- C-02a v3/v4.
- C-02b v3/v4. The first B printed the line as a caption ("SO I'MA JUST SAY IT RIGHT HERE"), so it was kept off (L16), stored on Old 3 and re-rendered once with a no-captions clause.

**System (owner account, V7.91.1):**
- §24O rule 10: people with no sheet are drawn to the proportion ladder in words, and the style frame shows full-body Pixar people (`one_offs` on the call, `people: true` on that ref). `preflight.py` checks it.
- L52.
- `preflight.py` also counts a two-unit product ("exactly two straps").

**Clips on the picks (Kling 3.0, 1080p, silent; To check):**
- C-01a 5 s. Flagged: her hand pats more than once.
- C-03b 5 s: blue glow along the tendon, slow push-in.
- C-04a 6 s: the surgeon presses the strap.
- C-05a 5 s: the cheap copy stretched and sagging.
- PR-05b 5 s: stairs class, end frame waived by the user, stairs pilot confirmed. Flagged: she takes several steps, not one.
- PR-06a 7 s: steam and a slow push.
- The unused images of the picked pairs are on Old 3.

**Act 8 (C-06a, C-07a, C-08a, C-08b, C-09a, C-09c), first pairs To check:**
- C-06a, N-D5 sheet outfit: she holds up two straps on the sofa. The house comes from P0.
  - The first B drew another woman (the jogger style frame's face), so it was kept off (L16) and re-rendered once with the hands-only style frame.
  - Flagged: the re-render's straps look like luggage straps with metal clips.
- C-07a: an edit of P-04a from above, the open product box (`package_open.jpg`, newly imported to Higgsfield) with two straps, her hand setting the lid.
- C-08a, N-D0: an edit of R-07a v8 A, the old way — plum top, grey skirt, side-on, both hands on the rail, grey morning light.
- C-08b, N-D3: the same frame edited, with her on the 3rd step from the bottom facing the lens, hands free, strap on.
- C-09a: her hands tie a red bow on the closed box.
- C-09c, N-D7: an edit of the old HK-03a v7 A (the view down from the landing, her mustard shoulder in front). The climber is replaced by the sister (68, navy dress, the ribboned box), drawn to the ladder with the jogger as the style frame (rule 10).

**Balances:** Higgsfield 5913.65 · Kling 37069.

**Waiting on:**
- Picks on C-02a, C-02b and the six Act 8 pairs.
- Confirm or Fix on the six new clips.
- After Act 8's clips, every beat has its picture. The edit (CapCut / `music.py render`) comes next.

### 2026-10-02 ~14:25–15:00 UTC — "fix those and generate the clips"

**Board read first (L49).** Fix notes on the board:
- C-07a image "dont cover the box stryde logo"
- C-08a image "wrong avatar"
- PR-06a image "the strap is too big"
- PR-05b clip "she should not touch the hand rail"

Clips were owed on the confirmed picks C-06a (v1), C-08b (v2), C-09a (v1) and C-09c (v1). C-02a and C-02b still wait on your pick.

**Image Fixes (new pairs, To check):**
- **C-07a v3/v4:** an edit of your picked v1 A frame. Her hand is off the lid and the stryde wordmark on the lid is in full view.
- **C-08a v3/v4:** the same edit of R-07a v8 A, now with her face-and-hair crop attached and her face named ("the same round face, dark brown skin and silver twist-out"). Cause: an edit that changed her clothes and pose redrew a thinner, lighter-skinned woman.
- **PR-06a v7/v8:** an edit of your picked v5 frame. Only the strap's size changes, to true size against the mug ("a little longer than the mug is tall"). Cause: my prompt asked for "a quarter of the frame wide" in a wide overhead, which enlarged the strap.
  - Flagged: B is still on the large side.
  - The PR-06a clip v1 (made from the replaced v5 frame) stays as a version until the new pick has its clip.

**System (owner account, V7.91.2):**
- §6A rule 2: the frame fraction never enlarges the product past true size beside known objects; reframe closer instead (L53).
- §24O rule 7: an edit that changes a cast member's clothes or pose attaches her face crop. `preflight.py` checks it (L54).

**Clips (Kling 3.0, 1080p, silent; To check):**
- **PR-05b clip v2**, 5 s, your Fix "she should not touch the hand rail". Diagnosis: in v1 her right hand left the basket for the rail. Now both hands are named on the basket handles from the first frame to the last, she walks in the middle of the runner, and it's one step. The second generation of this shot; v1 is on Old 3. Flagged: she still walks a few steps.
- **C-06a v1**, 6 s: she lifts the two straps on the sofa.
- **C-08b v1**, 6 s: stairs class, end frame waived by your 2026-10-01 words, hands named off the rail. Flagged: several steps, not one.
- **C-09a v1**, 5 s: she pulls the bow tight.
- **C-09c v1**, 5 s: the sister climbs toward the lens with the gift.
- The unused images of the picked pairs (C-06a v2, C-08b v1, C-09a v2, C-09c v2) are on Old 3.

**Balances:** Higgsfield 5877.65 · Kling 36853.

**Waiting on:**
- Picks on C-02a, C-02b, C-07a, C-08a and PR-06a.
- Confirm or Fix on the clips: C-03b, C-04a, C-05a, C-06a, C-08b, C-09a, C-09c, PR-05b v2.
- Clips for C-07a, C-08a and PR-06a after their picks. Then every beat has its picture and the edit comes next.

### 2026-10-02 ~14:35–14:45 UTC — hourly Fix check (three new Fix notes)

- **C-02a** image Fix "make a new one the face looks the same" → v5/v6. Three different women, each written in her own clause:
  - lilac: short, plump, round glasses, white curls
  - coral: tall, slim, freckles, grey bun
  - cream: broad, very dark skin, silver braids

  Same Pixar ladder and jogger style frame. Cause: one shared description for the group. Fixed in V7.91.3 (§24O rule 10, L55, `preflight.py`).
- **C-02b** image Fix "use the c02a as rerefence for all of them" → v5/v6. The new C-02a A frame is attached as the ladies to copy; her face crop is kept and there are no captions. Flagged: in B the lady in cream is cut at the right edge. If you pick C-02a B instead of A, the ladies match anyway (A and B carry the same three women).
- **C-04a** clip Fix "she should not stretch it" → clip v2, the second generation. Diagnosis: v1 had her pulling the band. Now it's a thumb press on the shell only, the band never pulled, and the strap keeps its length. v1 is on Old 3.
- Balances after: Higgsfield 5869.65 · Kling 36805. Waiting on: picks on C-02a, C-02b, C-07a, C-08a, PR-06a; Confirm/Fix on C-04a clip v2 and the other open clips.

### 2026-10-02 ~15:00 UTC — "generate the videos"

You picked A on all five open pairs, and none of the cards had a Fix note waiting. Five clips are on the board as To check (Kling 3.0, 1080p, silent, lengths from the act map, `clips/build_videos14_clips.py`, preflight PASS):
- **C-02a v1**, 4 s: the woman in coral nudges the woman in lilac, who nods. The three stay three different women.
- **C-02b v1**, 5 s: stairs class, end frame waived by your 2026-10-01 words. It's an after-state shot, so her hand is named leaving the rail. Flagged: she comes down a few steps onto the pavement, not one.
- **C-07a v1**, 4 s: her hand slides the lid and lifts away. Flagged: mid-clip her fingers pass over part of the wordmark, though it's clear at the end.
- **C-08a v1**, 4 s: stairs class, the struggle line, so both hands stay on the rail. Flagged: by the end the view has turned toward her front.
- **PR-06a clip v2**, 7 s: the clip from your new pick (image v7, after the Fix "the strap is too big"). Same motion plan; the strap held at its size beside the mug. Clip v1 was made from the replaced frame and is now on Old 3.
- The unused B images (C-02a v6, C-02b v6, C-07a v4, C-08a v4, PR-06a v8) are on Old 3 and deleted from Current.
- `fix_patterns.py`: 0 notes from the owner (the boards are V7.79.1, which doesn't mark them), so no new rule this round.

**Balances:** Higgsfield 5869.65 · Kling 36613 (192 spent this round).

**Waiting on:**
- Confirm or Fix on the open clips: C-02a, C-02b, C-03b, C-04a v2, C-05a, C-06a, C-07a, C-08a, C-08b, C-09a, C-09c, PR-05b v2, PR-06a v2.
- Every beat now has its picture and clip. Once they're confirmed, the edit comes next (`music.py cuts --words` / `render`).

### 2026-10-02 ~15:10–15:35 UTC — "all are locked finish this": the finished video

All 61 act-map beats are confirmed (`use`). Their clips on disk match the board's current versions byte for byte.

**FINAL-HK1** is on the Final board as To check (status `review`; the final review is yours). It's 3:48 (228.04 s), 1080×1920, 24 fps, 123 MB, uploaded as 9 × 15 MB parts that the board joins back into the exact file. It was made with `edit/build_final.py`; the cut list is `edit/cutlist_HK1.json` and the captions are `edit/captions_HK1.ass`.
- **Picture:** the 61 confirmed clips cut on the act map's beat-snapped lyric cuts (`work/actmap_rows.json` t_in/t_out = `docs/actmap`), frame-exact on the 24 fps grid. Each clip enters 0.4 s in, except HK-01a (0.03 s) and HK-02a (0.11 s), whose clips are only a fraction longer than their slots. No speed change, nothing slowed.
- **Sound:** the song, whole and untouched (the only soundtrack, §3C).
- **Captions (EG01):** the 108 lyric lines verbatim, black on white boxes, one or two rows at ~72 % height, a long line split at its comma or into even halves. Line 37 "Stryde." is captioned at 84.5–86.3 s (F4).
- **End card (F16):** the 5.3 s instrumental outro (222.7–228.0 s) shows the last frame of the C-07a clip (two straps in the box, the lid aside, the wordmark clear) with a slow 6 % push. The overlays are "Buy 1 Get 1 Free" and "60-day money-back guarantee", both held claims (§17), never generated.
- Flagged: P-05a (1.6 s) and P-05c (0.8 s) run under the 2.0 s floor. This is the three-shot P-05 you asked for on 2026-10-01.
- **This build's spend** (`build_spend.py` over the Current, Old, Old 2 and Old 3 boards; written as `buildSpend` on the Current and Final build docs): Kling 3,928 credits / 99 clips · Higgsfield 855.76 / 401 images · Kie AI 963 / 1 image. Total 5,746.76 credits over 501 renders.
- **Balances:** Higgsfield 5869.65 · Kling 36613 (no generation this turn).

**Waiting on:** your Confirm or Fix on FINAL-HK1 on the Final board.

### 2026-10-02 ~15:40–16:10 UTC — FINAL-HK1 v2 ("the p01a reverse it to look walking backwards and slow it down, fix the broll placement also use a caption fitting for a music video and not the plain one")

- **Placement.** Measured on v1 against medium.en sung word times (`edit/words_medium.py`, `edit/align_words.py`: 585 of the 615 lyric words matched; the rest are placed between their matched neighbours): v1 cut on average **0.77 s before** each line, and in 54 of 60 rows the new picture came in under the end of the previous line. Cause: §3C's "the beat at or before the word", plus small-model word times. Fixed at the source, **V7.91.4 / L57**: `music.py lyric_cuts` now cuts 2 frames before the first sung word, or on a beat ≤ 0.25 s before it. It never cuts under the line before (EARLY), times words with medium.en, and searches forward so a repeated phrase finds its own line (T-04b "I always figured…" had matched T-04a's line). The re-cut sheet `edit/cuts_v2.json` PASSes; the placement table is `edit/placement_HK1.md` and `docs/placement` on the Plan and Current boards.
- **Short rows.** P-01b (1.34 s), L-01b (1.82 s) and T-03a (1.97 s) are under 2.0 s because their sung lines are; each picture holds exactly its line. P-05a and P-05c stay short, as before (your three P-05 shots).
- **P-01a:** played in reverse, so she comes down the stairs backwards toward the lens (the clip was rendered climbing away). It runs at 0.65x, motion-interpolated.
- **HK-01a** is 0.6 s shorter than its now-correct 8.64 s slot, so it plays at 0.93x, interpolated, with no frozen frame. C-05a runs at 0.998x.
- **Lyrics:** music-video captions (§3C V7.91.4). Poppins ExtraBold (OFL, `edit/fonts/`), dark outline and soft shadow, no box. Each word fills gold as it is sung (ASS `\kf` on the aligned word times), and each line pops in. The end-card offer and guarantee use the same style.
- **On the board:** FINAL-HK1 v2 is on the Final board as To check: 128 MB in 9 parts, 3:48. v1 was copied to Old 3 (FINAL-HK1 doc there) and its parts were deleted from Final.

**Waiting on:** your Confirm or Fix on FINAL-HK1 v2.

### 2026-10-02 ~16:20 UTC — "Pain pills. Cortisone shots. we need brolls for these 2"

Line 15 is now three pictures, one per phrase (`work/actmap.py`: the new `sub` / `t0` fields cut a row on its own first sung word; 63 rows, all 108 lines covered, `angles.py` PASS; `docs/actmap` re-synced on Plan and Current):
- **P-04b** keeps "Physical therapy." (its card's `line` is updated; its confirmed image and clip are unchanged).
- **P-04c — "Pain pills."** At her kitchen table (N-D1c), close at table height: her right hand tips an amber bottle and two pills fall into her open left palm, with a glass of water beside. The confirmed P-04a frame is Image 1 (her table, her hands and cardigan cuffs). Motion plan: the pills tip into her palm, one tip, about a second.
- **P-04d — "Cortisone shots."** In the clinic (N-D1b), close from low at the side of the table: a doctor's gloved hands, one steadying her knee and one holding a syringe at the side of the knee, her hand on the paper sheet. The confirmed P-04b frame is Image 1. Motion plan: the thumb presses the plunger, one slow press. Flagged: in both renders she sits on the edge of the table rather than lying as in P-04b.
- Both are A/B pairs on Higgsfield, nano_banana_pro requested and logged as nano_banana_2, as on every image of this build. Preflight PASS (`body9/build_split15.py`). On the Current board as To check.
- **Timing:** sung, "Pain pills." runs 36.96–37.92 s and "Cortisone shots." runs 38.14–38.84 s. On the V7.91.4 clock, P-04b, P-04c and P-04d are each on screen about 0.8–1.2 s (under the 2.0 s floor; your call, the song sings them that fast). The finished video takes them in once their clips are confirmed.
- Credits: Higgsfield 5699.65 → 5667.65 (32 for 4 renders, measured; written as 8 per render). Kling unchanged at 36613.

**Waiting on:** Use A / Use B (or Fix) on P-04c and P-04d. Then their clips, then FINAL-HK1 v3 with the three line-15 pictures.

### 2026-10-02 ~16:30–16:55 UTC — "confirm" / "all confirmed proceed to the final" → FINAL-HK1 v3

- You picked A on P-04c and P-04d. Their clips were made on Kling 3.0: 3 s each, 1080p, silent, 24 credits each, preflight PASS (`clips/build_split15_clips.py`).
  - P-04c: the pills tip into her palm.
  - P-04d: the gloved thumb presses the plunger at the side of her knee. The prompt has the sealed-lips clause because her chin is at the frame's top edge.
- Both clips are on the board as `use`, on your word "all confirmed". The unused B pictures were copied to Old 3 and deleted from Current.
- **FINAL-HK1 v3** is on the Final board as To check. It is 3:48, 64 rows, the cut sheet is `edit/cuts_v3.json` (PASS), and the board copy is 9 parts.
  - Line 15 is now three pictures, each on its own sung word: P-04b "Physical therapy." at 35.65 s, P-04c "Pain pills." at 36.88 s, P-04d "Cortisone shots." at 38.09 s. They are on screen for 1.2, 1.2 and 0.8 s.
  - Everything else is as v2. v2 was copied to Old 3 and its parts were deleted from Final.
- **Balances:** Higgsfield 5667.65 · Kling 36565.

**Waiting on:** your final review of FINAL-HK1 v3.

### 2026-10-02 ~17:00 UTC — "fix those" (two board Fix notes)

- **M-06a** image Fix: "wrong product and the knee that should be straight in the image is the one with the strap".
  - Diagnosis: the strap had come out as a plain black band, without the twin-peak shell. The strapped right leg also wasn't clearly the straight, weight-bearing one.
  - New pair, v11 (A) / v12 (B): an edit of the picked v9 A with the product photo as Image 2 and a tighter shape line (a wide shallow M, two peaks at the middle of the top edge cupping the kneecap, chrome slides). Her right leg (frame left) is straight on the upper tread taking her weight; her left leg bends, stepping down (`body9/build_fix14.py`, preflight PASS).
  - Moved to Old 3: v9 A and the clip made from it (v2).
- **T-04a** image Fix: "that is not loreta".
  - Diagnosis: the dancer in fuchsia had been drawn without Loretta's references.
  - New pair, v7 (A) / v8 (B): an edit of the picked v5 A in which only the dancer changes. She now takes Loretta from her confirmed wedding frame (T-02a v5 A, the day's outfit, HT27) plus her face-and-hair crop (HT26, L54).
  - Moved to Old 3: v5 A and the clip made from it (v2).
- Both pairs are on the Current board as To check. The clips follow your picks, then FINAL-HK1 v4.
- `fix_patterns.py`: 0 notes from the owner (the boards are V7.79.1, which doesn't mark them), so no new rule.
- Higgsfield balance 5667.65 → 5233.4. That is far more than 4 renders; the account is shared, so other work moved it. The cards carry 8 per render.

### 2026-10-02 ~17:10–17:40 — "fix that and generate the video", then "both confirmed"
- **M-06a** image Fix: "the product is distorted i need a new one thats why i said it should be straid leg". This is the second Fix in a row on the strap.
  - Diagnosis: both earlier pairs were edits of a small, angled crop of her staircase frame. The shell wrapped round the thigh with the peaks upside down. Higgsfield also logs NB2 under the Pro name.
  - New pair, v13 (A) / v14 (B): a fresh picture, not an edit, made with Kie AI nano-banana-pro (true Pro), 18 credits each. It is a front-on close-up at knee height with both legs straight and the shell flat to the lens, a third of the frame wide. Refs: Image 1 is front.webp, Image 2 is the R-07a frame (her stairs, denim skirt, tan slippers).
  - Motion plan: her left slipper steps down one tread toward the lens while the strapped right leg stays straight.
  - Moved to Old 3: v11 and v12.
  - The user said "both confirmed". I read it as M-06a A plus the T-04a clip. A is used and v14 B went to Old 3.
  - Clip v3 was made from v13 A on Kling (32 credits). The bare left foot stepped. The user said "the one who will step should be the one with the strap", so v3 went to Old 3.
  - Clip v4 was made from the same frame v13 A (32 credits): her right leg, the one with the strap, steps down. Generation 4 on that note; preflight PASS. The user confirmed it: "confirmed now for the final output" (status `use`). System change: V7.92.2 adds HT28, `preflight.py` PRODLIMB, L60 and FP25.
- **T-04a**: clip v3 was made from the pick v7 A (40 credits). The user confirmed it (status `use`). The unused v8 went to Old 3.
- **System (owner, keys-exe)**: V7.92.1. After a Fix calling a worn product distorted, the next render is fresh, never another edit. Changes: §6A rule 3, `preflight.py` PRODEDIT, LESSONS L59, FP24. Merged in keys-exe/global-manual-ai#453.
- Kie balance 94441.6 → 94405.6. Kling balance 36493 after the M-06a clip.
- FINAL-HK1 v4 is re-cut with T-04a v3 and M-06a v4.
- Hourly Fix check, 17:20 UTC: no cards on `regenerate`, so nothing was done.
