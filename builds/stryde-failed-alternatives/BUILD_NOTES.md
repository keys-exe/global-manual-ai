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
- **Waiting on the user:** Confirm/Fix N-VOICE-IMG (the paid takes wait on it, §22X); the six plates; the absorption; answers to F2, F4, F5, F6, F7, F9.
- **Next, no stop once the frame is confirmed:** set `start_approved: true` in the three call files → preflight → Kie `kling-3.0` takes G1–G3 (`kie.py kling --prompt-file voice/N_G<n>.kling.json --image <frame url> --duration 10 --sound`), every take on the board → `voice_source.py` (medium trim, ×1.2, same-voice gate, loop ≥ 30s) → `elevenlabs_clone.py clone … --name FailedAlternatives` (name refused if taken → `--character` suffix) → `tts_api.py` eleven_v4 speed ~0.85 on `vo/ALL.enhanced.fitted.txt`, takes on the board → split at the silences into HK1/BODY1/HK2/BODY2/HK3/BODY3 → `vo_trim.py` house cut per variant (≤ 210 wpm). Then hooks one by one (HK1-01, HK2-01, HK3-01 + HK-BR).
