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

  ~12:55: user approved HK1 image ("proceed HK2 and HK3"). Start images, no selfie, all PROPPED/overhead at P2 bench:
  HK2 (seated at the vice, half-built generic brace clamped beside him), HK3-BR (overhead, halves, hand mid-lift),
  HK3-BR2 (restaged for no selfie: sleeve half held up to the propped phone, he lowers it, focus taps to his eyes — still camera),
  HK3-TH (bench, sleeve half in hand). All on the board as review. Board file storage FULL (1 GB, every asset referenced):
  User chose to free space: removed TH-HK1/2/3-BODY v1 (untrimmed) + v2 (tight trim) files and the TH-ONEGO file
  (42 assets, ~571 MB; versions kept on the cards marked `deleted`, ONEGO stays on HeyGen). HK3-BR image then uploaded.
  NOTE for B-roll: ~560 MB free now; upload clips at source size, and plan Drive if the board fills again.

  ~13:18: HK1 video step 1 — Kling omni 5s walk clip (40 credits, Kling 135 left) from the confirmed HK1 image, propped camera,
  four slow steps towards the lens, no audio → board HK1 `review`. HK1 audio split at the phrase end (Whisper on the v3 trim):
  walk part 0–3.77s ("…coming from."), talk part 3.77–10.39s → `hooks/hk1/`. On Confirm: HeyGen create_lipsync (walk + walk audio),
  then Avatar V from the walk clip's last frame with the talk audio.

  ~14:05: user confirmed the walk → HeyGen create_lipsync (precision). LEARNED: HeyGen lip-sync needs speech in the source
  video's own audio track — no track → "audio missing"; a silent track → "audio track is silent". Working recipe: mux the
  target VO into the clip (video stream-copied), then lip-sync with the same VO. HK1 v2 (lip-synced walk, 5.04s) on the board
  as review; HK1-TH frame (walk's last frame) on the board as review.

  ~14:48: user "REDO ALL IMAGE FOR HOOKS" (asked: all incl. HK1; fault = his face/look). Diagnosed: the hook ID block had
  drifted from the C1 sheet (no crooked broken nose, no higher left mouth corner, "thick" moustache). Fixed in
  hooks/build_hooks.py (FACE from the sheet verbatim + face negatives; TH-IMAGE job c3137e88 attached as a second face ref;
  SKIN-B1/B3, EYES-A, HAIR-A on HK2/HK3-BR2/HK3-TH). Five new images (v2) → board review. Negatives on HK3-BR/BR2/TH were
  sent shortened (the builder files hold the full lists). HK1 walk + lip-sync kept as versions but must be remade from the
  new HK1 image after its Confirm; HK1-TH frame superseded.

  ~14:55: user confirmed all hook images v2, asked to redo the HK1 walk. Kling connector down to 3 credits → Kie AI
  kling-3.0/video pro 5s (90 Kie credits; 237,913 left), same motion prompt (preflight PASS, generation 2) → HK1 video v3
  (1072×1928) on the board as review.

  ~15:02: user confirmed the new walk ("redo the Hook 1 walk with voice") → HeyGen lip-sync (precision, voice muxed in first)
  → HK1 video v4 on the board as review. HK1-TH frame v2 = last frame of the new walk → review.

  ~15:10: user confirmed the voiced walk + HK1-TH frame → HeyGen photo avatar a92f6e9d… from the frame, Avatar V (no
  motionPrompt) with HK1 audio 3.77–10.39s → HK1-TH v1 (6.62s, video c35c56a5…) on the board as review.
  HK1 is then complete pending review: walk 0.4–4.17s + HK1-TH. Next: HK2, HK3 videos.

  Later (from commits, not written here at the time): HK1-FULL card — v1 join of HK1 v4 + HK1-TH v1; v2 one take (Kie
  kling-3.0/video 12s walk + stand + full HK1 line → HeyGen lip-sync); v3 Seedance 2.5 on Kie, ingredients (HK1 image v2,
  P3 plate, C1 sheet, TH-IMAGE, @audio1 = the talking-head voice's HK1 line), 15s 720p, native audio — user: "use the
  talking heads voice as voice clip … seedance 2.5 — hook only". All three on the board as review.

- session_018X2U8ag6qVk4WFeKKTMfRd (2026-09-28 16:00–): resumed. Merged `claude/vibrant-allen-sj2pso` into
  `claude/wonderful-dijkstra-np80sq` (conflicts in §22U/SKILL.md resolved keeping both 2026-09-28 corrections: one-go
  Avatar V + step 14 natural-pace trim). Hourly Fix check moved: `trig_01HjYaZr7JdTVsfKyCw1ytUD` (:49 UTC) bound here,
  `trig_01ERbz4gRWaJ3sZ2tPVgNCWC` deleted.

  ~16:05: user "T2, use v3 for HK2 and HK3" → VO-T2 cards `use`, VO-T4 back to review; HK1-FULL `use` (v3). HK2-FULL
  and HK3-FULL: one Seedance 2.5 take each on Kie (ingredients: start image v2, P2 plate, C1 sheet, TH-IMAGE, @audio1 = the
  T2 take's own hook line cut from `T2.ALL.mp3` at the cut points), preflight PASS. HK2 10s from HK2 v2 (630 credits,
  task d5fa3e99…); HK3 13s from HK3-BR2 v2 — sleeve half held to the lens, lowered on "I want to show you", focus taps to
  his eyes (819 credits, task d04e663b…). Both on the board as review. HK3-BR (overhead halves) unused by the one take —
  available as an insert over "cut in half" in the edit.

  ~16:25: user Fix on HK3-FULL image: "recreate this image without phone on the table". Cause: the HK3-BR2 prompt said the
  phone was "propped against the tin of rivets", so the model drew it. build_hooks.py fixed (the phone is the camera, never
  seen + negative). Image v2 = Higgsfield edit of HK3-BR2 v2 (job 2e1c583a…, logged nano_banana_2) → review; the HK3 video
  waits for its Confirm, then Seedance generation 2 from it (same prompt, voice ref, 13s).

  ~16:35: user confirmed the no-phone image, "regenerate the HK3 video" → Seedance generation 2 (task 437f5ac8…, 819 credits,
  13.06s) → HK3-FULL video v2 on the board as review. A third HK3 video needs the user's go (§22X).

## Where it stands (2026-09-28 16:20)
- VO master **T2** (confirmed). HK1-FULL v3 confirmed.
- **Waiting on the user (review):** HK2-FULL v1, HK3-FULL video v2 (from the no-phone image); TH-HK1/2/3-BODY v3 (gentle trim).
- **Next:** after the hooks are confirmed → B-roll (step 7): E6 lengths from `TH-HKn+BODY.trim2` word timestamps first.
- Board storage near its 1 GB cap — upload at source bitrate; Drive if it fills.
- Open: F3, F4, F11, F12, F13.
