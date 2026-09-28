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

  ~16:45: user Fix on HK3 video: "make it 10 seconds". v2 had a 3.3s dead pause after "I want to show you" (the slow
  sleeve-lowering was tied to that phrase; 13s was too long for a 7s line). User chose a 10s regeneration over cutting
  the take, approving generation 3 and the §28H budget override (25 words / 20) — recorded in the call file (`user_go`).
  Prompt: sleeve lowered on "this morning" in ~1s, line straight through. HK3-FULL v3 (10.08s, 630 credits, task
  8235dfb1…) on the board as review. No more HK3 video generations without the user.

  ~16:50: user confirmed HK2-FULL and HK3-FULL v3 ("confirmed, proceed to B-roll"). Step 7 started:
  - E6 lengths: `work/broll/plan_HK1.json` (HK1+BODY trim2 audio + TH track) → `assemble.py --lengths` PASS, no failures
    (`work/broll/lengths_HK1.json`); MECH rows max 10s (no human motion); keys that sat on a phrase's last word dropped
    (BR-10/11/12/14a/15a); **BR-10 split into BR-10a ("One, the placement.", high front, fingertip trace) and BR-10b
    ("Two centimetres below the kneecap…", eye profile, still)** — 6.6s > 6s. Act map updated (39 rows), angles.py PASS.
  - Prompts: `broll/build_broll.py` → `broll/<BEAT>.t2i.txt`, `broll/broll_v1.json` (§22T seed + ANGLE/FOCUS/LIGHT/COLOUR
    lines, product strings from the STRYDE module, ANAT-A/B for MECH). Route as the user set for STRYDE builds: realistic
    B-roll → Higgsfield nano_banana_pro, anatomy → nano_banana_2. Product refs imported to Higgsfield (`broll/ref_ids.json`).
  - 27 start images (21 BR + 5 MECH + BR-10 split), one render each, jobs `broll/jobs_v1.json` (MECH-12's first job failed
    at Higgsfield and was resent unchanged). All on the board as To check (stage broll, video `planned`, Kling 3.0 omni,
    duration = E6 call length). Renders in `broll/renders/` (gitignored; board + Higgsfield URLs hold them).
  - Old HK3-BR / HK3-BR2 / HK3-TH cards are superseded by the HK3-FULL one take (left as they are).

  ~17:50–18:15: user Fix notes on B-roll images, three rounds (15 fixes), all regenerated on Higgsfield from the note, fixed at the
  prompt in `broll/build_broll.py` (FIX1/FIX2/FIX3 blocks): BR-02 (one fingertip under the kneecap, front on), BR-05a/BR-08 (POV),
  BR-11/BR-15a/BR-18a (product at its real small size, product photos attached first as the anchor), BR-12 (rear-worn ref first,
  band just below the knee crease), BR-13 (true side view through the spindles), BR-14b (copy with a visible knock-off shell),
  BR-15c (shell centred on the front of the shin), MECH-01 (tendon close-up), MECH-02 (cartilage, no tendon), **MECH-06 replaced by a
  real B-roll** (her rubbing the spot under her bare kneecap in the armchair — act map row updated, angles.py PASS).
  User "generate the confirm images": 18 confirmed images → §35 Kling JSON (`broll/build_video.py`, ≤2,500, preflight PASS all) →
  Kling 3.0 on Kie (`kling-3.0/video`, pro; the Kling connector is out of credits since HK1, no switch back), E6 lengths, one render
  each, 1,350 Kie credits. All 18 on the board as review (BR-07b in two 15 MB parts). BR-18b is pinned: end frame BR-18b-END made
  (Higgsfield edit of its start frame) and on the board as review — its video waits for that Confirm.
  Board storage hit 1 GB again: user chose to delete old-version files — 28 files (222 MB) removed, each version kept on its card
  marked deleted with prompt and connector link.

  ~18:40: user "fix those" + "generate the confirm images". Video Fixes (generation 2, §22X, `VFIX` in `broll/build_video.py`,
  preflight PASS): BR-05a (he held the wrap → hands let go on frame one, rest empty, propped rig), BR-05b (focus → propped, focus
  locked on the braces), BR-08 (her other hand went into the drawer → one hand only, POV rig with no free hand), BR-12 (she walked
  → boots planted, weight shift only). Root cause for BR-05a/BR-08: RIG-R2B's "free hand enters frame" line — not used for POV
  shots with a hand already in frame from now on. Image Fix BR-15a v3 (FIX4 in `build_broll.py`: wider frame, band tucked in his
  palm, worn photo as size anchor, "spanning the whole front of the knee" removed from its product line). New videos from confirmed
  images: BR-02, MECH-01, BR-18a (pin_end set to no — faces stay square, no angle change), BR-18b (first-and-last frame to
  BR-18b-END). 8 Kie calls, 684.0 credits. All on the board as review.

  ~18:50: user "fix those" + "generate the confirm images" (round 3). Video Fixes gen 2: BR-02 ("he's pointing the knee" →
  fingertip moves in and presses the tendon in the centre under the kneecap), BR-18b ("slowly zoom in" → slow push-in; its pinned
  end frame is now BR-18b-END v2 = the confirmed v1 cropped ~80% on the box, no new generation). Image Fixes: BR-15c v3 ("wrong
  product" → close frame on the shin so the shell renders as the product), BR-18a v3 ("remove the bracelet" → edit of v2 with the
  bands tucked into his palms; its v1 video is now out of date, a new one follows the Confirm). BR-11-END v1 made (the strap turns
  over, so BR-11 is pinned). New videos: BR-13, BR-14b, BR-15a (pin_end set to no — the lift keeps the face square). FIX5/END in
  `build_broll.py`, "Round 3" in `build_video.py`, preflight PASS. Third-generation Fixes on BR-05a ("arrage the product"),
  BR-05b ("close up the product, slowly zoom in") and BR-12 ("she's walking, front angle") wait for the user's go (§22X).

  Round 3 results: BR-02 v2, BR-18b v2 (two 15 MB parts), BR-13, BR-14b, BR-15a on the board as review (522 Kie credits with
  BR-15c below; BR-13's first submission was lost when the polling connection reset — no task id kept, ~90 credits gone, resent once;
  `kie.py` now logs the task id at creation and retries dropped polls/downloads). Board full again: user chose "delete old-version
  files" — BR-05a/05b/08/12 v1 videos, BR-15a/15c/18a v2 images, BR-18b-END v1 removed (~60 MB), then BR-18a v3 and BR-11-END v1
  (superseded this round), each version kept on its card marked deleted.
  ~19:00 round 4 (user "fix those" + "generate the confirm images"): BR-11-END v2 ("wrong product" → back product photo leads,
  PAD_BACK_SHOT), BR-18a v4 ("fix the holding" → BR-15a v3's grip in both hands), FIX6 in `build_broll.py`. BR-15c video v1 (its
  confirmed v3 already has the strap seated, so the clip is a press-and-release; pin_end → no). The user's answer on the three
  third-generation Fixes (BR-05a, BR-05b, BR-12) ticked every option including "None for now" — held, asked again.

  ~19:05–19:15: user answered "All three" → third tries (§22X gen 3, `user_go` on the call, preflight's only FAIL is the
  generation gate): BR-05a v3 (fingertips square the supports into a row, sliding, never lifting), BR-05b v3 (slow push-in onto the
  braces), BR-12 (new front-angle start image v3 — confirmed — then video v3: boots planted, weight settles). Round 5 ("fix those" +
  "generate the confirm images"): BR-13 v2 (walks on down confidently, two steps, no stopping), BR-14b v2 (hands low, the copy's shell
  kept down, only the band stretched — v1 read as showing our product), BR-18a v2 (remade from the confirmed v4 image), BR-11-END v3
  ("show the back starp" → held like the back product photo, band loop and keepers towards the lens). Each superseded file removed
  from the board to make room (user's "delete old-version files"), versions kept on the cards marked deleted.

  ~19:20 hourly Fix check: BR-11-END "show the back strap" again on v3 (shell tipped over, band underneath) → v4 copies the back
  product photo's composition (shell upright, peaks up, band loop in front with the keepers to the lens); FIX9 in `build_broll.py`;
  v3's file removed for room. BR-02's third try still waits for the user's go.

  ~19:25: user "Both" → BR-02 v3 (generation 3: three light taps on the tendon under the kneecap, one a second) and BR-12 v4
  (generation 4: same front shot, slow steady push-in on the strapped knee, feet planted); `user_go` on each call, preflight's only
  FAIL the generation gate. Superseded BR-02 v2 and BR-12 v2/v3 files removed for room.

  ~19:35: user "BR-11 generate this confirm image" → asked; user chose "Use END v4 as end frame" (BR-11-END v4 treated as
  confirmed on their word; its board card was gone by then, so the end frame is recorded on BR-11's card as `endFrame`). BR-11 v1:
  first-and-last frame, 3s, 54 Kie credits, on the board as review. BR-02 v3 and BR-12 v4 confirmed by the user.

## Where it stands (2026-09-28 19:35)
- Hooks done. VO master T2. TH-HK1/2/3-BODY v3 still To check.
- B-roll: every video confirmed ("use") except BR-11 v1 (To check) — the last B-roll clip.
- Any further Fix on BR-02, BR-05a, BR-05b, BR-12 is past the §22X limit — ask first.
- Board storage at the cap; each new render goes up after its superseded file is removed.
- Next: once BR-11 is confirmed, rough cut per hook (`assemble.py`, `variants.py`) → CapCut block.
