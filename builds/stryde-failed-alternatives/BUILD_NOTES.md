# Build notes — stryde-failed-alternatives (STRYDE · Failed Alternatives, voice-only Short VSL, Manual)

Read this first when resuming. Build Sheet: `BUILD_SHEET.md` (steps 1–3).

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/1GbYzHIQKw39DKonyeNI1owY3yE6hlcRn
- User message: "RUN MANUAL. BRITISH" → RUN: MANUAL, VOICE: British. MODE blank → Mode 1. HOOKS → 3 in script (A Sleeves, B NoneWorked, C Injections), **each with its own body** → 3 videos.
- Script header (ADJUST): different voice than the reference (British, ElevenLabs), different B-roll and editing, ~50% Black people on the B-roll, add music.
- Same reference ad as `stryde-too-bad` (re-measured: 51.96s, 33 shots, same transcript). New cast and voice all the same (§19A).
- Inspo came as `INSPO VIDEO` (no extension) → `intake/inspo.mp4`; script `Untitled document.docx` → `intake/script.docx`; spoken parts `work/script_{HK1,BODY1,HK2,BODY2,HK3,BODY3}.txt`.
- Product Sheet in the folder is V7.49.29; the repo's V7.49.38 is used.
- **Boards (account iamnotkeysi@gmail.com):** Current https://claude.ai/artifact/CXmyrmezBb25rcyXJYk1fF · Old https://claude.ai/artifact/1LogbiXVkVQ3EU8rBiza2A · Final https://claude.ai/artifact/BDpgxcW4UDgKZCpRMExQkL · Plan https://claude.ai/artifact/JdfqS1zzWJY4k27eV7wjt2
- **Hourly Fix check:** `trig_019LzSyoBti4K1s29jWjGaG7` (:12 UTC) → session_019EAqabibLetVJtKhsGQ6nN

## Sessions
- session_019EAqabibLetVJtKhsGQ6nN (2026-09-29 ~12:20 UTC): steps 1–3. Absorption, ledger (VN-H1, VN01–VN03), phrase inventory (HK1–3 + 36 body phrases), claims (F5–F9), Mode & Model Lock.
  Cast on Higgsfield Sunburst 2k, one each: N-NARR (voice only), R1-PATRICIA, R2-GORDON, R3-EMMANUEL, R4-SIAN. Higgsfield 17,448 credits before the cast.
  Four boards made; build doc on all four, cast on Current, docs/absorption on Plan + Current.

## Where it stands
- 2026-09-29: user confirmed N, R2 Gordon, R4 Sian; R1 Patricia and R3 Emmanuel sent back "change this avatar" → recast as **R1 Bernadette** (Black British, Nigerian, 69) and **R3 Delroy** (Black British, Jamaican, 60), one render each (card doc ids keep the old slot names `__R1-PATRICIA` / `__R3-EMMANUEL`, v2); Patricia and Emmanuel moved to the Old board.
- 2026-09-29: user confirmed R1 Bernadette and R3 Delroy (all five avatars confirmed) and said "go ahead with steps 4–5".
- 2026-09-29: **steps 4–5 delivered** (`STEP4_5.md`): six 16:9 plates on Higgsfield Sunburst, one render each — P0-PROP-B (Bernadette's hall/stairs/dresser), P1-G-KITCHEN (Gordon's kitchen + larder cabinet), P2-D-BOWLS (Delroy's bowls green), P3-PROP-S (Sian's passage/stairs), P4-S-KITCHEN (attached P3; redo if P3 is Fixed), P5-CLINIC. Act map: 34 unique beats, V1 20 / V2 19 / V3 19 shots, `angles.py` PASS on all three; Black share 53% / 50% / 46%. Wardrobe ledger written. Board: 6 plate cards (To check), 34 beat cards (planned), docs/locations, docs/actmap, docs/wardrobe on Plan + Current. Higgsfield 17,342 credits after.
- **F4 built on my recommendation** (our own clinic strap-on shot HK-BR, shared by all three hooks; all-new body footage) — swap it if the user sends existing footage.
- 2026-09-29: user "go ahead with the voice". §22U step 1: `voice/N_step1_v1.png` (job 0435a9aa…, nano_banana_pro requested, job reports nano_banana_2 — the known logging mismatch), made with the N sheet (job 994041a5…) + the sheet's face close-up crop (`voice/N_face_ref.png`, Higgsfield media 2699a634…) attached from the start; on the board as N-VOICE-IMG, To check.
  Step 2 ready: `voice/N_G1..G3.call.json` (2,452 / 2,458 / 2,483 chars; §37 TH ladder step 4: "Not a narrator, not an advert." dropped from all three to fit G3), preflight PASS but the frame's approval (§22X).
  **Kling connector has 3 credits → takes go via Kie `kling-3.0` (§5 fallback)**; Kie 171,214.8 credits. ElevenLabs clone `check` PASS (513 free slots).
  Step 8: `vo/ALL.enhanced.txt` (HK1+BODY1+HK2+BODY2+HK3+BODY3, one request) verbatim PASS, 3,687 chars.
- 2026-09-29: user confirmed the frame (and, on the board, all six plates) — "go ahead". §22U straight through:
  step 2: three Kie `kling-3.0` takes (10s, sound on, 270 credits each; tasks 219fde2a…, 96d8c736…, b905bc5c…) → board N-G1..G3 (split into 15 MB parts).
  steps 3–5: `voice_source.py` → `voice/Alternatives_clone_source.mp3` 40.23s; same-voice gate PASS (200.0 / 202.5 / 203.8 Hz), transcripts verbatim → board N-SRC.
  steps 6–7: clone by API, name **`Alternatives`** (one keyword from the title, §22U step 7), **voice ID `uh69ybRPQgahYncj0lYN`**.
  step 9: `tts_api.py` eleven_v4, speed 0.85, 4 takes of `vo/ALL.enhanced.fitted.txt` (186–188s, 152–154 wpm raw); every word present in every take.
  split: `vo/split_parts.py` (build-local; `cut_points.py` only knows HK1|HK2|HK3|BODY) → 24 part files → board VO-T<n>-<PART> (one row per part, takes as versions), all To check.
  step 10a: house cut on the working take T1, raw hook + raw body per variant, `vo_trim.py --max-wpm 180` (the inspo's rate): **V1 61.51s 154 wpm · V2 59.16s 157 wpm · V3 64.66s 152 wpm**, all verify PASS → `vo/VO_T1_V<n>.mp3`, board VO-CUT-T1-V<n> (stage edit, To check).
  Board audio goes up as AAC in .mp4 (the asset store refuses .mp3). Kie 168,280.8 credits after.
- 2026-09-29: user confirmed **take T4** for BODY1/2/3 on the board, no hook take confirmed, then "FIX ALL VOICE FOR HOOKS TO PROCEED THE HOOK 1". All 12 hook part-takes re-checked by transcript and level: verbatim, no clipped start or end.
  Fix = the variants were cut from T1 while the bodies are now T4 → **re-cut all three from T4 (T4 hook + T4 body, one pass, so the voice matches at the seam)**: V1 61.40s 154 wpm · V2 59.55s 156 wpm · V3 65.33s 151 wpm, verify PASS (`vo/VO_T4_V<n>.mp3`). Board: VO-CUT-T1-V<n> cards now v2 (T4); the T1 cuts moved to the Old board. Hook part-takes left for the user to confirm (T4 is the one the cuts use).
- Step 6, hook 1 (user: "proceed the hook 1"): start frames `hooks/HK1-01_start_v1` (NB2, job aa6aea54…, logs nano_banana_flash; R1 sheet + P0 attached) and `hooks/HK-BR_start_v1` (NBP, job c971988d…, logs nano_banana_2; front.webp media 1c84ea10…, worn_front f5263ed7…, R3 sheet, P5 attached), built by `hooks/build_hooks.py`. Both To check.
  HK-BR angle changed profile → low three-quarter front (a profile hides the wordmark SEAT_LOCK needs); act map, STEP4_5.md and docs/actmap updated, `angles.py` PASS on V1–V3. HK-BR negatives drop NEG_SEAT's "no second person" and "no product coming to rest low on the shin" (the surgeon seats it; the start frame is at mid-shin).
- **Waiting on the user:** Confirm/Fix HK1-01 and HK-BR frames (the clips wait on them, §22X); the hook VO takes; the absorption; F2, F4, F5, F6, F7, F9.
- **Next on the frames' Confirm:** Kling clips (Kie `kling-3.0`, §5 fallback while the connector has 3 credits): HK1-01 one push shut, 1.5–2s of use, sway, no pin; HK-BR SEAT_LOCK slide up, **pinned end frame** (product changes position → §27G/E7 first-and-last-frame: generate the seated end frame, To check, first). Lengths from `assemble.py --lengths` on the T4 house cut. Then hook 1's rough cut for the step-6 gate.
