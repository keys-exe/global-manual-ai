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

  ~11:20: user "IT SHOULD BE V" → TH-01..07 re-rendered on **Avatar V without motionPrompt** (Avatar V takes a motion
  prompt only with a digital twin in the group; the account has none and a generated character can't have one).
  Avatar IV renders kept as version 1 on each card. IDs in `vo/th/heygen.json` (`avatar_v_renders`).

  ~11:30: user "REDO THE TALKING HEADS … ONE GO … JUST TRIM THEM" → one Avatar V render of the whole T2 house-cut
  master (HK1 + body, 137.23s, HeyGen `cf21685a105b9d103e35639a1cac8c49`); TH-01..07 trimmed out of it at the same
  word timestamps (`vo/th/TH-0n.v2.mp4`, x264 CRF 16) → v2 on each card; TH-FULL card holds the whole render.
  The seven per-segment Avatar V renders sent earlier are superseded (not used). Standards updated the same day:
  Avatar V only + one go (§22U), Kling out of credits → Kie `kling-3.0/video` (§5, `kie.py kling`).

  ~11:40: user "CHANGE THE TALKING HEADS IMAGE, DON'T USE THE SELFIE STYLE, DELETE ALL THE TH, ONE GO, H1+BODY H2+BODY
  H3+BODY" → all TH cards deleted; new image TH-IMAGE (PROPPED, `voice/C1_TH_propped_v1.png`, job c3137e88…, confirmed by the
  user); whole T2 take house-cut in one pass (`vo/variants/T2.ALL.mp3`, 151.0s, PASS); HeyGen avatar `764d5cd1…`, one Avatar V
  render `22d3374e…` (151.0s); cut at `T2.ALL.mp3.cuts.json` (HK1 0–10.41, HK2 –16.86, HK3 –23.89, BODY –151.03) into
  `vo/th2/TH-HK1+BODY.mp4` (137.6s), `TH-HK2+BODY.mp4` (133.6s), `TH-HK3+BODY.mp4` (134.2s), 4 Mb/s like the source.
  Board: TH-HK1-BODY, TH-HK2-BODY, TH-HK3-BODY, TH-ONEGO (review). Standards §22U step 12 updated to this.

  ~12:10: user "TRIM THE TALKING HEADS" → trim.py (E11) on the three hook+body videos: HK1 137.6→122.0s, HK2 133.6→117.6s,
  HK3 134.2→119.8s (52–62 cuts each, all PASS, every word kept) → `vo/th2/TH-HKn+BODY.trim.mp4`, v2 on each card.
  NOTE for B-roll timing: the trim moved every line earlier, so E6 lengths come from the trimmed videos' own word
  timestamps (`TH-HKn+BODY.trim.json`), not from T2.ALL.

  ~12:30: user "THE TRIM IS TOO FAST" → re-trimmed gently (`trim.py --pre 0.12 --post 0.28`: pauses ≤~0.4s kept):
  HK1 134.4s, HK2 130.3s, HK3 130.7s (23–28 cuts, ~3.4s each, PASS) → `vo/th2/TH-HKn+BODY.trim2.mp4`, v3 on each card.
  Board file storage hit its 1 GB cap: deleted the unreferenced assets of the deleted TH cards (7 Avatar IV clips,
  7 one-go trims, 5 TH-FULL parts). NOTE: 1 GB will not hold the B-roll at this rate — store board copies at the source
  bitrate (~4 Mb/s) or make the Drive OUTPUT folders.
  Hooks: user — no selfie in the hooks either (override of VN01/VN02). HK1 start-image prompt `hooks/HK1_start.prompt.txt`.

  ~12:40: TH-HK1/2/3-BODY v3 (gentle trim) written to the board as `review` — the user's earlier Confirm was on the tight v2.
  HK1 start image v1 generated (Higgsfield job 996705d3…, logged nano_banana_2) → board card `HK1`, image To check.

## Where it stands
- **Waiting on the user:** the master listen (VO cards; T2 working master, say "T4" to switch — the THs are then re-cut),
  and the check of TH-01..07.
- **Next:** hooks one by one (step 6): HK1 (walking selfie, Kling + HeyGen lip-sync, F12), HK2 (seed with the brace in
  the vice, VN02), HK3 (sleeve insert + pull-back + TH). Then B-roll (E6 lengths from the T2 word timestamps first).
- TH-04 was planned with the strap held low in frame; C1-SEED has no strap, so TH-04 renders without it (product first
  seen at BR-11/BR-15a). Say if you want a TH-04 seed with the strap.
- Open: F3, F4, F11, F12, F13.
