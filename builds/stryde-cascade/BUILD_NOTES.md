# stryde-cascade — build notes

**Build:** STRYDE · The Cascade ("Four Hundred Houses"), picture-in-picture talking head + B-roll, Mode 1, 9:16.
**Run mode:** Automatic (user: "run automation", 2026-09-28). Final videos only; no mid-run messages.
**Drive task folder:** `1nOldjHSuTw6koTHeChJ5BDvZ1MtNBfld` · OUTPUT `1KbCoR11ZmdFzVQSFwqQxGfK5sXqilmaC` (IDs in `drive.json`).
**Board:** https://claude.ai/artifact/QK6FwiCxWuZqoWWVoEx2Yd

## Decisions
- Mode 1 (MODE not given, F5). Three hooks run as written (F4). Caps: E0 default (Higgsfield 600 · Kling 3,000 · Kie 2,000).
- Cast: N (rail fitter, 61, narrator/talking head), C1 (woman, 74; D1 lilac, D2 navy, D3 pink gown), C2 (man, 68, strap on the right knee).
- Voice: clone `Cascade` = `maQgQv00HcQWiW4KwvNq` from three Kling voice takes; TTS flow `PJKuAqmYuN2pReFBUBfa`, master take T4; house cut per variant (`vo/master/*.wav`).
- Talking heads: HeyGen photo avatar `c8d9b4ef04136707e55f0cc8c4447444`, Avatar IV fallback (F9). Videos `th/TH-*.mp4`.
- B-roll: 40 beats (9 hook, 31 body), frames on Higgsfield, clips on Kling `kling-video-v3_0_omni`, audio off (F7). Every frame and clip judged §22V/§22W; rerolls and faults on each board card.
- Assembly: `variants.json` → `variants.py` (hook + identical body). Act 1 "Then…" list cut on each "Then" (F16); A2-B3 `out` 2.1s.
- Finishing: `edit/CAPCUT.md` (captions, banners, 17× / 34% / 200,000 overlays, offer card).

## Delivered (2026-09-28)
- Finals: `edit/STRYDE-CASCADE_HK1/2/3.mp4` (2:03.4 / 2:02.2 / 2:02.4, 1080×1920, 24 fps) — each variant PASS; body identical to the frame (F18).
- Where: full-quality finals page https://claude.ai/artifact/3uDVLnVKanAFsfna7pxvSb (board storage full, Drive connector inline-only — F19). Board FINAL-HK1..3 cards link it.
- Drive 08_EDIT: `OUTPUT.md` (1kiCvVa7wmuPa_H1AHrin3sal2yiV-zBe), `CAPCUT.md` (1X5bJ7U--vksuYpLdORqkccUd5RV3_C89).
- Talking heads for the edit: `th/TH-*.pad.mp4` (held last frame; hooks cut to the VO frame count).

## Spend (start → end balance)
- Higgsfield 20,185.5 → 19,730.25 = **455** of 600.
- Kling 4,087 → 591 = **3,496** of 3,000 — over by 496 (F8: connector under-reports the charge ~2.8×).
- Kie: uploads only (F17).

## Open items
- Flags F1–F3 (claims/disclosure) are the advertiser's call before publishing.
- v2 re-edit (F20, BUILD_SHEET): slower VO (master v2 T2, 199–203 wpm), ~3s B-roll holds, 6/34 split/pip.
- **Resumed 2026-09-28 (session_01XyVmRtQqCbrULWxujVtka1):** the user is checking the B-rolls on the board and will leave Fix notes. Their Fixes are regenerated (no agent verdict), put back as To check; once confirmed, the three finals are re-assembled from the plans. Hourly Fix check `trig_01N8qwCCCFT9S55QL3zasmbh`. Media is not in git — a regenerate/re-assembly pulls clips, VO and heads back from the board assets. A2-M1, A2-M3, A2-M4 already have two video generations: a third waits for the user's go (§22X).

## Files
Prompts `prompts/` · calls `calls/` · act map `actmap.json` / `ACTMAP.md` · job ids `work/jobs.json`, `work/kling_jobs.json` · board cards `work/board/`. Media stays out of git (`renders/`, `th/`, `vo/`, `edit/*.mp4`).

## Fix round 1 (2026-09-28, user Fix notes on 19 B-roll videos)
- Diagnosed per §22X; prompts `prompts/frames/<b>.fix1.txt`, `prompts/clips/<b>.v2.kling.json`, calls `calls/<b>.v2.json` (all preflight PASS), scripts `work/fix1*.py`.
- Motion-only fixes (old frame kept): A1-B2 (step-to, both feet on each step), A1-B4, A1-B5 (visible struggle), A4-P1 (band swings with weight). Rendered and on the main board as To check (video v2).
- New frames (Higgsfield nano_banana_pro, 2k) + new clips: A2-B1, A2-B2, A3-B2, A4-B1, A4-B2, A4-M1, A4-P2, A4-P3, A5-B1 (N in work shorts lifting a toolbox), A5-B2, A5-B3, A5-B4, A5-B5, A5-F1. Clips rendered; job ids `work/fix1_jobs.json`, `work/fix1_kie/`.
- All 18 clips on Kie Kling 3.0 (`kling-3.0/video`, pro 1080p) — Kling account at 591 (§5 fallback). Kie spend 1,296 credits (230,736 → 224,010).
- A2-M4 not regenerated: it would be the third video generation (§22X) — waiting for the user's go.
- A4-P1 v2 flagged: the shell reads as lost mid-clip as the band swings; a third try needs the user.
- **Blocker:** the main board's asset store is full (1 GB). Fixes board https://claude.ai/artifact/VxngRxNy7t4faxWgNbGJkt created, 14 new frames uploaded there; uploading the 14 new clips was blocked by the session's permission check — waiting on the user. The 14 main-board cards stay `generating` until then. Orphan assets on the main board (~116 MB, unreferenced by any card) were found but not deleted.
- Local renders are not in git (`renders/fix/`); they are lost when this container ends — upload or re-fetch from the Kie URLs (valid ~24h–3 days) in `work/fix1_kie/`.

## Resumed 2026-09-28 (session_01Ped7M2rF4YGPDjZ9VcpKf8)
- Branch: merged `claude/resume-brolls-fixes-3qfdz6` (this build, V7.65.0 pace/B-roll holds) and `claude/happy-mendel-tasb0c` (board viewer fixes) onto the default branch (V7.64.4). The two parallel cuts are combined as V7.65.0: the pace rules sit on the Eleven v4 + Enhance step; `tts_api.py` now voices on `eleven_v4` (≤ 10,000 chars); `speed` on v4 unverified.
- Board is four boards now (Current / Old / Final / Plan, CLAUDE.md). The Fixes board VxngRxNy7t4faxWgNbGJkt is no longer used (it holds no cards).
- Storage freed on Current: the replaced v1 renders of the 18 Fix-round-1 beats (4 motion-only video v1s, 14 frame + clip v1s) copied to the Old board (sha256 checked), Old docs written per beat, Current version entries marked `archived` + `archiveAsset`, then deleted from Current. Three deletes were refused by the session's permission check and remain on Current as duplicates of their Old copies: `a8ffe9014df69f6eb915cabf474fed92` (A5-B3 frame v1), `b2e070378a7a870a09fb0db796790301` (A5-B4 clip v1), `88d0d72e19de937a674c43c61ed851df` (A5-F1 clip v1) — the user's call.
- The 14 blocked cards are on the Current board: new frame (vN, `review`) + new clip (v2, `review`), re-fetched from the Higgsfield / Kie URLs. (Higgsfield labels `nano_banana_pro` renders `nano_banana_2` — Build Sheet F6; the request was `nano_banana_pro`.)
- Waiting on the user: check the 18 Fix-round-1 cards (Confirm / Fix); A2-M4 and A4-P1 third video generations need the user's go (§22X). Once confirmed, the three finals are re-assembled.
- Hourly Fix check moved to this session: `trig_01R8nk1N86GQE63WkUuE6hEL` (old `trig_01N8qwCCCFT9S55QL3zasmbh` deleted).

## Fix round 2 (2026-09-28, user: "fix those" on 7 Fix notes)
- Every fault this round was in the start frame (§22X diagnosis in `work/fix2_motion.py` DIAG): A1-B3 flight ran into a wall; A2-M4 two overlapping leg outlines (the base mechanism prompt asked for a three-quarter view against a side-view beat — now strict profile); A4-B1 "productive results" → carrying laundry up the stairs, strap below the kneecap; A4-P1 held by the shell, not the band; A4-P2 the back of the strap (back reference only, front wordmark lock removed); A5-B3 whole body, face visible; A5-F1 an unbranded copy of the same shape, stretched in her hands, not a buckle strap.
- New frames: `work/fix2.py` → `prompts/frames/<b>.fix2.txt` (post-edits recorded in the script), Higgsfield jobs `work/fix2_jobs.json`, URLs `work/fix2_urls.txt`. On the Current board as `imageStatus: review`; each replaced frame and the video made from it moved to the Old board (ids in the version entries' `archiveAsset`) and deleted from Current.
- Videos: `work/fix2_motion.py` → `prompts/clips/<b>.fix2.kling.json`, `calls/<b>.fix2.json`; all preflight PASS except the start-image gate, which clears on the user's Confirm. Cards sit at `status: ready` with no video; the hourly check (step 2b) sends each on Kie Kling 3.0 once its frame is confirmed. A1-B3 is generation 2; the other six are generation 3 with the user's go recorded as `user_go`.
- `preflight.py`: a third or later generation now passes only with `user_go` (the user's words + date) and a diagnosed fix — the §22X "no third without the user" rule had no way to record the go.
- Hourly Fix check `trig_01R8nk1N86GQE63WkUuE6hEL` now also sends confirmed fix-2 frames' videos.

## Fix round 3 (2026-09-28, user: "fix those" after checking the board)
- Videos sent from confirmed fix-2 frames (Kie Kling 3.0, `work/fix_send.sh fix2`): A1-B3 (v2), A4-B1 (v3), A5-B3 (v3) — on the board as `review`.
- Video Fixes on confirmed frames (`work/fix3_motion.py`, generation 3, `user_go`): A4-M1 the strap glows blue and absorbs the whole load wave, nothing passes below it; A4-P3 the strap is only set down, never stripped; A5-B2 hands held off the handrail — on the board as `review`, the replaced v2s on the Old board.
- New frames (`work/fix3.py`, Higgsfield jobs `work/fix3_jobs.json`, URLs `work/fix3_urls.txt`): A2-B2 fingertip on the midline below the kneecap (not the side); A4-P1 held by the lower edge so the real two-peak shell reads (the fix-2 frame drew a rounded clip); A4-P2 back of the shell with a smooth unbroken pad (the thumb press drew holes). `imageStatus: review`, `status: ready`; their clip calls `calls/<b>.fix3.json` pass preflight except the start-image gate. The hourly check sends each once its frame is confirmed. A2-B2's old frame and its video moved to Old.
- Kie spend this round: 432 credits (6 clips).

## Fix round 4 (2026-09-28, user: "fix those and generate the other confirmed")
- Videos from confirmed frames: A2-B2 (v3, fix-3 frame), A2-M4 (v3, fix-2 frame), A5-F1 (v3, fix-2 frame) — `review`.
- A4-B1 video v4 (motion Fix, confirmed frame): climbs the stairs with the basket high and clear of the banister; he had walked into the hall with the basket against the rail and the strap lost shape — `review`.
- New frames (`work/fix4.py`, jobs `work/fix4_jobs.json`, URLs `work/fix4_urls.txt`), `imageStatus: review`, clip calls `calls/<b>.fix4.json` ready for the user's Confirm:
  - A4-M1 — user asked for a new picture with the strap protecting the tendon: blue shield over the tendon, the load wave stops at it (strict profile; the base mechanism prompt's three-quarter view removed).
  - A4-P1 — one hand at the lower edge; the second hand at the top of the shell removed.
  - A4-P3 — new straps: two whole straps on the bench, no hands; the clip moves only the light and camera.
  - A5-B2, A5-B3 — his hand kept grabbing the rail because the frame hung it beside the rail (A5-B2 three times): new frames on the wall side of the flight, car keys in the rail-side hand.
- Kie spend this round: 288 credits (4 clips).

## Fix round 5 (2026-09-28, user: "FIX THOSE")
- Clips from confirmed fix-4 frames (Kie Kling 3.0): A4-M1 (blue shield), A4-P1 (one hand), A5-B2 (wall side, keys), A5-B3 (wall side, keys, face) — `review`.
- New frames (`work/fix5.py`, jobs `work/fix5_jobs.json`, URLs `work/fix5_urls.txt`), `imageStatus: review`; clip calls `calls/<b>.fix5.json` (`work/fix5_motion.py`) wait for the user's Confirm:
  - A4-B1 — basket on his right hip, away from the banister (user: "move the basket he is carrying to his right side"); the v4 clip and the fix-2 frame moved to Old.
  - A4-P2 — "just use the back of the STRYDE, this is the wrong product": the fix-3 frame drew a rectangular watch-style pad; now the strap lies back-up on the bench from the back reference alone (two-peak outline), no hands; the clip moves only light and camera.
  - A4-P3 — "fix the strap, don't cut it": the bands drew as cut open straps; each band is now one closed loop slide to slide.
- The hourly check (step 2b) must also look for `calls/<b>.fix5.json` — updated.
- Kie spend this round: 306 credits (4 clips).

## Fix round 6 (2026-09-28, user: "fix those and generate the confirmed ones")
- Clips from confirmed fix-5 frames: A4-P2 (back of the strap on the bench, camera and light only), A4-P3 (two straps, closed bands) — `review`.
- A4-B1 — "instead of stairs it should be other activities": new frame (`work/fix6.py`, job `work/fix6_jobs.json`) — crouched in the hall lacing his walking boots, strap on the loaded right knee; clip call `calls/A4-B1.fix6.json` (`work/fix6_motion.py`) waits for the Confirm. The fix-5 frame moved to Old.
- Kie spend this round: 180 credits (2 clips).
- 2026-09-28 (round 7): A4-B1 clip v5 from the confirmed fix-6 frame (lacing boots), Kie 72 credits — `review`. No other Fix notes open; every other B-roll card is confirmed.
- 2026-09-28 (round 8): A4-B1 video Fix "he should just be getting up, not tying" → clip v6 on the confirmed boot frame: he rises from the crouch on the strapped knee (`work/fix7_motion.py`, `calls/A4-B1.fix7.json`), Kie 72 credits — `review`; v5 moved to Old.

## 2026-09-28 — edit stopped; narrator becomes a Japanese Kampo physician
- User: "ALL CONFIRMED PROCEED TO EDITING WITH CAPTIONS AND BGM", then stopped it: "STOP THE EDITING WE WILL CHANGE THE TALKING HEADS — Ancient Chinese / Japanese medical authority". Answers: rewrite as the healer · Japanese Kampo physician (Edo-era) · new voice.
- Found: the v2 finals never rendered (variants_report FAIL, ffmpeg SIGKILL/OOM — the one-graph concat of 49 inputs); FINAL-HK1..3 on the Final board are still v1. The v2 inputs are fetchable: VO v2 masters (`work/vo_urls_v2.txt`), HeyGen v2 heads (TH-HK1 ede4ba16…, TH-HK2 7dd3f3be…, TH-HK3 9a00c2c3…, TH-BODY 5c14d398…), and all 40 confirmed B-roll from each card's `videoUrl` (sizes verified).
- Script v3 draft: `script_v3_kampo.md` (7 changed lines, 3 B-roll to redo, flag F21). Waiting for the user's approval.
- Then the user withdrew the rewrite: "WE WILL NOT CHANGE THE SCRIPT — JUST THE VOICE". Final answer: **face and voice change, the script stays verbatim**; the new narrator is **a Japanese woman, a Kampo physician (late Edo period), voice "Japanese woman, almost neutral English"**. `script_v3_kampo.md` is marked WITHDRAWN, and the script-v3 docs were removed from the Plan and Current boards.
- Cast: `prompts/K_sheet.prompt.txt` (N_sheet template, gpt_image_2_5 high 2k) → card `N-KAMPO` v1 on Current (`review`), asset 8174f128…, Higgsfield job f6482362….
- Next, after her sheet is confirmed: voice source (Seedance clip, §22U), then the clone, then the VO of the unchanged script (pace ≤210 wpm, house cut), then the HeyGen talking heads. Every split/pip shows the new head. The B-roll that shows N (HK1-B2, HK2-B1, HK2-B3, A5-B1, A5-P1 hands) is to be raised with the user. Then the edit with captions and BGM (per-segment render, so it doesn't OOM).
- 2026-09-28 (cont.): user confirmed N-KAMPO, "keep the b-rolls, proceed with the voice". The voice is **Cascade-Haruko `l0eMc3UHUMWnvUdlMJPt`** (ElevenLabs IVC by API; `voice/VOICE-K.md`), built from 3 Kie Kling 3.0 clips with sound (`prompts/K_G1..3.kling.json`, start image = TH frame v1) → `voice_source.py` (same voice PASS, pitch ±1.2%, 36.6s source).
- TH frame: v1 had a phone on the table (the prompt had said "propped on the far edge of the low table"). User: "REMOVE THE CELLPHONE ON THE TABLE" → fix1 prompt (`prompts/K_TH_frame.fix1.prompt.txt`) → v2 (board K-TH-FRAME, review). HeyGen photo avatar `221319e8b9ee0b752e6f3293caa020bb` from v2.
- VO v3: `vo/v3/enhanced.txt` (Enhance tags + [slowly]/[pause], `tts_budget` verbatim PASS), eleven_v4 speed 0.8, 4 takes, one request split by `work/split_parts.py`, house cut with `vo_trim.py`. T1/T2 HK2 FAIL (breath left); **T3 = working take** (all PASS, verbatim by small.en; BODY 161.9s at 189 wpm, HK1 14.2s, HK2 12.6s, HK3 11.7s). URLs are in `work/vo_urls_v3.txt`. Board: VO-T1..T4-<PART> (review). The old VO-T4-* (rail fitter) and old TH-* files were moved to the Old board and deleted from Current.
- Talking heads v3: HeyGen Avatar V rejected motion_prompt (no digital twin, as F9) → Avatar IV, expressiveness high + motion prompt. Videos: TH-HK1 0c64f629…, TH-HK2 cc4f8a6a…, TH-HK3 afc78026…, TH-BODY 328b1035….
- User: "the voice feels robotic" (VO v3). Edit stopped before assembly. Diagnosis (§22X): (1) `speed 0.8` on Eleven v4 (unverified, a time-stretch), (2) a thin clone source (12s unique, looped 3×), (3) `[slowly]`/`[pause]` on every sentence. Samples on the board, HK1 only: **A** = same clone at speed 1.0 with expression tags only (house cut 14.4s, 204 wpm); **B** = new clone **Cascade-HarukoB `WrLHpBlNOo6gnGpaXBSt`** from 6 Kling clips (G4–G6 added, `prompts/K_G4..6.kling.json`, same voice PASS, 26s unique) at speed 1.0 (14.0s, 211 wpm hook alone). Finding: this clone paces at ~200 wpm at speed 1.0, so no slow-down is needed. Waiting for the user to pick; then the full VO, the 4 HeyGen heads, and the edit (captions + BGM) are redone with that voice.
- Talking heads v3 (Avatar IV) downloaded to `th/v3/` (TH-BODY not uploaded — superseded if the voice changes).
- User: "the cut is so fast" (voice samples, 204–211 wpm). Fix: a `[pause]` after each sentence (no `[slowly]`), speed 1.0, and a gentler house cut, `vo_trim.py --pause-stop 0.7 --pause-comma 0.35` (new options; default still 0.45/0.20, never longer than the take had). Samples v2: A 15.7s at 188 wpm, B 15.8s at 186 wpm. This build's VO will use 0.7/0.35 — a user override of §22U step 10a's 0.45/0.20, to be proposed as a standards change only if the user asks.
- User: "the trim is so fast" (samples v2, 186–188 wpm). Root cause: `vo_trim.py` squeezed every in-phrase pause over 0.12s to PAUSE_WORD 0.01s. New option `--pause-word`. Samples v3: `--pause-stop 1.0 --pause-comma 0.5 --pause-word 0.3` (each capped at the take's own pause) → A 17.0s at 173 wpm, B 17.1s at 172 wpm — only breaths and the end silence are removed. This build's VO will use these settings once the user picks A or B.
- User: "its trimmed even though she is not done talking" (samples v3). Root cause: vo_trim keeps only frames above −38 dB, and her soft word endings fall below that, so they were cut mid-word. Fix: **no cut inside the speech** — `work/ends_only.py` removes only the silence before the first word and after the last (−50 dB floor, 0.25s tail, 60 ms fade). Samples v4: A 17.35s, B 17.36s (~170 wpm), every word present (small.en). This build's VO will be voiced this way (Eleven v4, speed 1.0, `[pause]` per sentence) with no house cut — a user override of §22U step 10a for this build.
- User: "i need a new vo re do them cause we need an audible". Measured: the samples were very quiet (A −28.8, B −26.7, T3 −30.2 LUFS). Samples v5 were normalised to −15 LUFS / −1 dBTP. Asked what "audible" means; user: "ill make a pr wait for it". **On hold** — no full VO re-do until the user's PR lands; then follow it.

## 2026-09-29 — V7.66.0 pass (user's PR keys-exe/global-manual-ai#36 merged; "Proceed with the vo again")
- Merged the default branch (claude/laughing-meitner-x819t4, v7.66.0) into this branch. New rules: VO house cut −50 dB + 80 ms release, in-phrase pauses kept ≤0.6s; trim.py 120/250 ms padding; HeyGen **Avatar V only** (no motionPrompt where V refuses it), talking heads rendered **in one go** from the whole take, then cut per hook + body (`cut_points.py`).
- VO v4: voice **Cascade-HarukoB `WrLHpBlNOo6gnGpaXBSt`** (user: no preference between A/B; B has 26s source), Eleven v4 **speed 1.0**, `vo/v4/enhanced.txt` = Enhance tags + `[pause]` per sentence, no `[slowly]` (verbatim PASS). 4 takes, each house-cut whole in one pass (all PASS, 190–195 wpm). Verdicts (§22U step 10): **T1 FAIL** ("One knee only" voiced "One me only"); **T2 = master** (every word, ends "…rather you did."); T3/T4 PASS, not chosen. T2 ranges: HK1 0–16.10, HK2 –29.10, HK3 –42.23, BODY –204.36 → `vo/master/*.wav`. Per-variant pace ~189–192 wpm.
- Board: v3 VO takes, v3 Avatar IV hook heads and the voice samples moved to the Old board (VO-v3-*, TH-HK*-v3, VOICE-SAMPLE-*), files deleted from Current. VO-T1..T4-<PART> now hold v4 (T2 `use`).
- HeyGen TH-FULL `306975d4b06529aacfae34c6a3b7b820` (Avatar V, no motionPrompt, whole T2 take) rendering.
- Talking head: HeyGen `306975d4b06529aacfae34c6a3b7b820`, Avatar V, no motionPrompt (refused — no digital twin), whole T2 take in one go (204.34s), cut at the T2 ranges → `th/TH-<PART>.pad.mp4`. **Step 14 (trim.py) not applied**: the VO is already house-cut to V7.66.0; trim.py would take another 7.3s (46 cuts) out of her pauses and break sync with the master — against the user's "the trim is so fast". Recorded, for the user to overrule. Board: TH-HK1..3 uploaded; TH-BODY file not on Current (the 1 GB store is full; the body head is inside the finals and at the HeyGen link).
- BGM v2 (`edit/v4/bgm.cue.json`): re-timed to VO v4 (hook slot 16.5s; body sections at 58.5 / 85.8 / 129.7s), 'Try it' held at level. Check: levels −28.8/−21.3/−16.4/−14.1/−16.4 dB; flags = fade-in, tail, note attacks. USE. v1 moved to Old.
- Edit: `variants.py` (per-segment `assemble.py`) → PASS for all three, body identical, HK1 178.23 / HK2 175.13 / HK3 175.25s. `work/finish.py` (captions C1 213/212/210 cards; BGM `--music-db −29`, sidechain ducking, loudnorm), then audio −0.5 dB for true peak → −14.9/−14.7/−14.8 LUFS, TP −1.3/−1.3/−1.2. Frame check OK.
- Final board: FINAL-HK1..3 v2 (10 × 15 MB parts each), status `use` (Automatic §22W verdict); v1 cards moved to the Old board. `edit/OUTPUT.md` rewritten for v4.
- Pending: merge into the default branch (asked the user); Drive OUTPUT upload not done (the connector takes inline content only, ~140 MB files).
- User: "THIS FINAL OUTPUT ALSO DONT HAVE ANY AUDIO". Root cause: `loudnorm` in `work/finish.py` resamples internally and the mix left the AAC at **96 kHz stereo**, which browsers and phones don't play (it plays silent). Fix: finals re-encoded at 48 kHz (video copied, `+faststart`), still −14.9/−14.7/−14.8 LUFS, TP ≤ −1.2; `finish.py` now ends the mix with `aresample=48000`. Final board: FINAL-HK1..3 v3 (48 kHz); the 96 kHz v2 pieces were removed (same picture, unplayable sound; noted on each card). Other board audio (VO takes, BGM, heads) checked: 44.1/48 kHz, not affected. Could not play-test here (the sandbox Chromium has no AAC/H.264).
- Merged the default branch again: V7.67.0 (PR keys-exe/global-manual-ai#37: trim by task — a talking-head task sends the untrimmed take to HeyGen and trims only the heads). Not applied to this build (§34: a system update is never applied to an existing build without its team's ask).
