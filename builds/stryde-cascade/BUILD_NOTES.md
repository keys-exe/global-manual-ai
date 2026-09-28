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
