# Build notes — stryde-identity (STRYDE · Identity Callout, Manual)

Read this first when resuming. Build Sheet: `BUILD_SHEET.md` (steps 1–3) · `STEP4_5.md` (steps 4–5) · voice: `voice/VOICE_SOURCE.md`.

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/1tKlZFjNApDMf5U_q3qFPcRyGZLQsVcwE
  ("C - VID | AI VO | TOF | Identity Callout | New | A Must For V2"). No OUTPUT subfolders exist in it.
- The same folder was also run earlier as `identity-callout-v2` (Automatic, 2026-09-25, branch
  `claude/vigilant-archimedes-c5sh8z`). **stryde-identity is the live build** (Manual, 2026-09-26).
- **Board:** https://claude.ai/artifact/GKZDjmZkh4wwm7RxtXj7Tp

## Sessions
- session_01…(eloquent-darwin, 2026-09-26 08:00–09:17): steps 1–5, avatars (recast N and Pat on the user's call),
  six plates (all USE), narrator §22U steps 1–5 (G1–G3 USE, gate max 5.1%, 41.27s clone source).
- session_019jyz29Da9tQzhkoLnhKTSF (2026-09-26 09:20, resume): merged that work onto `main`'s board work;
  re-downloaded G1–G3 from Kling (links expire ~2026-09-27 09:10 UTC) and rebuilt `Identity_clone_source.mp3`
  with `voice_source.py` — identical figures; created the board and loaded 16 cards (5 cast confirmed,
  6 plates + 3 voice takes + clone source in review); moved the hourly Fix check here (`trig_01AkAtMoRj4zmTuGSkTRApUw`).
- (2026-09-26, later sessions, not written here at the time): step 6 started on HK1 — HK1-T reached image v25 /
  video v5, HK1-B image v15 / video v7, all on the board.
- session_01H75hV8rxRkMbx5zhnK11Eo (2026-09-28, resume): **the user asked for new sets of hook B-rolls and to delete
  the previous for a cleaner look.** HK1-T and HK1-B removed from the board; both cards (every prompt, version,
  Fix note and asset id) archived in `archive/board_2026-09-28/`. The asset files stay in the board's store,
  unreferenced, so any old render can still be restored. Hourly Fix check moved here (`trig_01JwbciTZag3vqU45rw5sf82`).
  **New hook set (same act-map shots, all three hooks):** prompts in `hooks/` (`hooks_v1.json`, `<beat>.t2i.txt`),
  built from last round's user-picked HK1 prompts. Six Higgsfield nano_banana_pro jobs were sent, then the user
  switched the route: **images now go through the Kie AI API with GPT Image** (`gpt-image-2-5-sunburst-image-to-image`,
  user, 2026-09-28) — the Higgsfield renders were not put on the board. The user asked to see one image first:
  HK1-T v1 and HK1-B v1 are on the board (review); HK2 and HK3 wait for the user's check of HK1.
  **HK1 videos (Kling, 5s, 1080p):** user confirmed both HK1 images ("create the video for this hk1 first").
  HK1-B: v1 JSON prompt (distorted, user) → v2 simple plain-text prompt "walks down the stairs" (user: text, not JSON,
  keep it simple) — To check; a third needs the user's go. HK1-T: end frame made (Kie), user fix → v2 with the band
  looped in front of the pad; video v1 = first-and-last frame (rendered before the user said "don't use end frame");
  v2 = start frame only, simple text prompt — To check. User preference: simple plain-text video prompts, not JSON.
  HK1-T final = the user's own clip (video v3, `hooks/HK1-T_video_v3_user.mp4`, board USE).
  HK2-T v1 and HK2-B v1 made (Kie GPT Image, same prompts/refs as hooks_v1.json) — on the board, To check.
  HK1-B video v2 confirmed by the user (USE). HK2-B image v2: user fix "from the back of the van, not already outside" → inside the van at the open back doors (To check).

## Where it stands
- **§22U steps 6–9 done:** clone `Identity-Narrator` = `F5vpA7jC44a7w7td6GdQ` (by API; `Identity` was taken by the
  v2 build's Carol). **VO redone in one go on the user's call (09:47 UTC):** HK1+HK2+HK3+body in one eleven_v3 request,
  4 takes, each split at the silences and E11-trimmed → 16 pieces, all verbatim, all on the board (`VO-T<n>-<part>`,
  review). The first round (separate requests) was deleted from board, repo and ElevenLabs history. Details: `vo/VO.md`.
- **Trim redone on the user's correction** (hook endings clipped, inhales left) with `vo_trim.py`; T1–T3 bodies
  had their last word cut off by ElevenLabs.
- **§22U step 10 done: T4 locked by the user**, then re-cut to the user's own reference edit (house cut:
  butt joins, words to −38 dB, no breaths). Masters HK1/HK2/HK3 = 57.85 / 57.91 / 58.08s, verbatim, on the board
  (`VO-MASTER-HK1…3`, review). Word timestamps in `vo/master/HK<n>.words.json`. Reference file: `vo/ref/`.
- **Next:** E6 — set every B-roll row's duration from the body word timestamps (span of its line + 0.5s, Kling 3–15s),
  then step 6: the hooks one by one (HK1 first, split layout EG01), as prompts + generations on the board.
- Open flags from the Build Sheet: F2 (Pat's cropped trousers vs strap visibility), F4 (comparative claim P-005),
  F7 (`package_closed.jpg` missing), F8 (AVATAR-SHEET doc inconsistency), F10 (watermark omit).
- (2026-09-28, later) **Hook videos switched to Seedance 2.5 (user: "re do all of them, use seedance instead of kling").**
  Via Kie (`kie.py seedance`, 720p, 5s, no audio, ingredients: @image1 = confirmed start image, @image2–3 = front/back).
  Top shots take the user's HK1-T clip as @video1, the movement to copy (user: "use the hk1t i sent for inspo in all
  the hk t"); `kie.py` gained `--ref-video` for it. HK1-T itself stays the user's clip. The Kling HK2 videos are kept as v1.

- (2026-09-28) **User: "please follow the visual"** (VN01–VN03 pasted again). Simple prompts must still carry every
  part of the visual note: HK1-B + camera eases back to her hand on the rail; HK2-B + walks off with a box on his
  shoulder (camera eases back to show it); HK3-B + camera eases back to the toddler on a scooter ahead, her keeping up;
  HK3-T holds the strap out (child's scooter against the wall behind). Seedance v2 of HK1-B / HK2-B sent with these.
- (2026-09-28, 08:45 UTC) **All six hook videos on the board (Seedance 2.5 via Kie, 720p, 5s), To check.** HK1-T/HK2-T/HK3-T
  take the user's HK1-T clip as @video1. HK1-B / HK2-B remade to follow the visual notes (rail reveal; box on shoulder).
  HK3-T has two takes (v1, v2 — the call was resent while v1 sat 35 min in Kie's queue). Seedance cost 315–380 Kie
  credits per clip. Next: the user's check of each hook clip, then the edit.

- (2026-09-28, 08:50 UTC) User confirmed all hook clips ("confirmed everything in the boards … give me the final
  hook"). Board picks: HK1-T v4 (Seedance), HK1-B v2 (Kling), HK2-T v2, HK2-B v3, HK3-T v2, HK3-B v1 (Seedance).
  **Final hooks** rendered by `final/make_hooks.py` (EG01 split 50/50, middle half of each clip from 0.4s, VO line
  as caption on the split per VN01–03 — the script's visual note outranks the Build Sheet's "no captions"; audio =
  locked VO master to "Because"): HK1 4.20s, HK2 4.16s, HK3 4.52s, 1080×1920, on the board as EDIT-HK1…3 (To check).
  ffmpeg via `pip install imageio-ffmpeg` (the standard's setup). Next: the body B-roll (act map BR/MECH rows), then
  the full variants (hook + body) for the Final output tab.
- (2026-09-28, 09:00 UTC) **Body B-roll started (user: "next make the body brolls").** E6 lengths from the body word
  timestamps → `work/body_lengths.json` (27 beats, Seedance floor 4s: 25 × 4s, BR-03 and BR-21 5s). Start-image
  prompts built by `body/body_prompts.py` from the act map, the wardrobe ledger and the product sheet strings
  (SEAT_LOCK, PLACE_BENT, PAD_BACK_SHOT, FAKE_BASE + "too small", PACKAGE_LOCK, ANAT-A/B with the sheet's slots) →
  `body/<BEAT>.t2i.txt`, `body/body_v1.json`. 27 cards on the board (stage broll, Act 1–5). Images through Kie GPT Image;
  videos (Seedance) wait for the user's Confirm of each image. F7: no `package_closed.jpg` — BR-22 uses the open-box
  reference plus PACKAGE text.
- (2026-09-28, 09:10 UTC) **User: "stop"**, then **"for brolls use kling and never seedance"** (standing rule for this
  build: body B-roll videos go through the Kling connector — `kling-video-v3_0_omni`, 9:16, 1080p, imageCount 1,
  prefer_multi_shots false, simple plain-text prompts; never Seedance). The image run was stopped part-way:
  16 start images made and on the board as To check (MECH-01/02/07/10/11/15, BR-03/04/05/08/09/12/13/14/16/19);
  BR-06 failed at Kie; BR-17/18/20/21/22/23 were killed mid-call (not on the board); BR-24/25/26a/26b never sent.
  Card video model set to Kling. E6 note: Kling's floor is 3s, so re-run the lengths with 3–15s before the video calls.
  Nothing more is sent until the user says go.
- (2026-09-28) **Strict image-route rule (user): anatomy / mechanism images → Higgsfield `nano_banana_pro` or
  `nano_banana_2` only. Kie GPT Image (`gpt-image-2-5-sunburst-image-to-image`) only for realistic (Mode 1 photo) images.**
  So MECH-01/02/07/10/11/15 v1 (made with Kie GPT Image before this rule) are the wrong route — kept on their cards as
  history, to be remade on Higgsfield (act map: NB2 for mechanism) when the user says go.
