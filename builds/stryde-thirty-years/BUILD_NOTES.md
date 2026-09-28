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

  ~10:20: user cloned the voice in ElevenLabs as "Thirty Years Making Braces" (`I4gNUimdUeOgOcImvw0A`), said "VOICE ID:
  PROCEED" (ID found with creative_list_voices). TTS: `vo/ALL.tagged.txt`, eleven_v3, 4 takes, flow `mm9vGyG0eOcijTB5WgSA`
  (~9,415 credits), `vo/takes.json`. Split + verbatim (`vo/split.json`), house cut per hook variant (`vo/variants/`).
  T1/T3 FAIL (last word cut by ElevenLabs; T3 also drops "straps that look like this are"). **T2 = working master**
  (verbatim, 137.3s HK1+body, ~197 wpm); T4 passes too (121.3s, ~223 wpm). All 12 on the board (stage vo).
  ~10:45: user "CLONE THE VOICE AND CREATE THE TALKING HEADS" → body THs TH-01..07 cut from T2.HK1 by word timestamps
  (`vo/th/segments.json`, all match 1.0), HeyGen photo avatar `d54cb6fb17763dfb7682feedcd89c8d7` from C1-SEED.
  **Avatar V refused motionPrompt** (no digital twin in the group) → §22U fallback (c): Avatar IV, expressiveness high,
  motionPrompt kept (`vo/th/heygen.json`). All 7 rendered and on the board as review (~20 HeyGen credits).

## Where it stands
- **Waiting on the user:** the master listen (VO cards; T2 working master, say "T4" to switch — the THs are then re-cut),
  and the check of TH-01..07.
- **Next:** hooks one by one (step 6): HK1 (walking selfie, Kling + HeyGen lip-sync, F12), HK2 (seed with the brace in
  the vice, VN02), HK3 (sleeve insert + pull-back + TH). Then B-roll (E6 lengths from the T2 word timestamps first).
- TH-04 was planned with the strap held low in frame; C1-SEED has no strap, so TH-04 renders without it (product first
  seen at BR-11/BR-15a). Say if you want a TH-04 seed with the strap.
- Open: F3, F4, F11, F12, F13.
