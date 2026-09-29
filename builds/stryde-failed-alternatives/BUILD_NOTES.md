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
- **Waiting on the user:** Confirm/Fix the six plates; the absorption; answers to F2, F4, F5, F6, F7, F9.
- Next (straight through after the plates, §22U, no stop): N's voice-source image → two Kling 10s takes with `VOICE-NARR` → `voice_source.py` → clone by API (`FailedAlternatives-Narrator`) → Enhance → Eleven v4, HK1+BODY1+HK2+BODY2+HK3+BODY3 in one request → VO takes on the board → `vo_trim.py` house cut (≤ 210 wpm). Then hooks one by one (HK1-01, HK2-01, HK3-01 + HK-BR).
