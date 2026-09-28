# Build notes — stryde-thirty-years (STRYDE · Thirty Years Making Braces, Manual)

Read this first when resuming. Build Sheet: `BUILD_SHEET.md` (steps 1–3) · `STEP4_5.md` (steps 4–5) · act map data `work/actmap.json` · voice `voice/`.

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/1yO_Hjayp5pbXc2AfvbAXeXZTj_jdzcpi
  ("C - VID | Talking Head | TOF | Maker Concession | New | Thirty Years Making Braces"). No OUTPUT subfolders.
- User message: `RUN MANUAL. BRITISH` → Manual; every character white British, British regional voice.
- **Board:** https://claude.ai/artifact/EG999Jm7UoVdq5YAY7iafV
- Inspo 1 (primary, the script's own Reference link) = `intake/inspo_hook.mp4` (trylymphoria lab-coat selfie, 1 take, 89.8s).
  Inspo 2 = `intake/inspo_body.mp4` (STRYDE's own grandmother ad, 90 shots, 267s) → the body's edit.
- `intake/` is gitignored: re-fetch with `fetch_drive.py stryde-thirty-years <link>` in a new session.

## Sessions
- session_01MBdnm3ZCUQQ5RgQYk55XR8 (2026-09-28 09:35–): steps 1–3. Board created; C1-MAKER and S1-WEARER sheets
  (Sunburst high 2k, jobs a866e6f7…, 7cc9a07d…) on the board as To check. 13.5 Higgsfield credits.
  Hourly Fix check `trig_01ERbz4gRWaJ3sZ2tPVgNCWC` bound to this session (:49 UTC). The old
  `trig_015ExzFatSnixWK2PEU5hVmP` no longer exists.

  2026-09-28 ~10:00: user confirmed both sheets ("I'VE CONFIRM PROCEED"). F1/F3/F4 not answered → run on the
  recommendations (F4 still open for the edit). Steps 4–5: plates P0-PROP-S, P1-S-LIVING (P0 attached), P2-WORKSHOP-BENCH,
  P3-WORKSHOP-RAIL (P2 attached) on the board as review (110.25 credits); act map (38 rows, angles.py PASS), wardrobe map,
  ledger assigned; docs locations/actmap/wardrobe on the Plan tab. §22U step 1 image C1-SEED (job 51f87b4b…, logged
  nano_banana_2) on the board as review. Kling takes G1–G3 written (`voice/C1_G*.kling.json`, ≤2,500), not sent.

  ~10:10: user confirmed all locations ("CONFIRM ALL LOCATION. PROCEED") and, when asked, C1-SEED. Voice takes G1–G3 sent
  (360 Kling credits); G3 failed the same-voice gate (+10.3%) and is excluded; `Thirty_clone_source.mp3` = G1+G2, 32.37s
  (`voice/VOICE_SOURCE.md`). Tagged TTS text `vo/ALL.tagged.txt` locked verbatim (2,354 chars).

## Where it stands
- **Waiting on the user: §22U step 6** — clone `voice/Thirty_clone_source.mp3` (board: VOICE-SOURCE) in ElevenLabs as
  `Thirty`, send the voice ID. Media is gitignored: in a new session re-download G1/G2 from the board (VOICE-G1/G2
  videoParts, join the parts) and rebuild with `voice_source.py C1_G1.mp4 C1_G2.mp4 --name Thirty`.
- **Then:** TTS `vo/ALL.tagged.txt`, eleven_v3, 4 takes, one request → split HK1/HK2/HK3/BODY → `vo_trim.py` house cut →
  the user's master listen (step 10) → HeyGen talking heads + hooks one by one (step 6).
- Open: F3, F4, F11, F12, F13 (see STEP4_5.md / BUILD_SHEET.md).
