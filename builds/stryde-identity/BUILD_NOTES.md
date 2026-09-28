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
- **VO stays on eleven_v3 (user, 2026-09-28):** the Eleven v4 + Enhance rule (§22U step 8) is forward only — "no re do
  just add this for next tasks". The locked T4 masters are not redone; any new VO on a later build uses v4 + Enhance.
- **Next:** E6 — set every B-roll row's duration from the body word timestamps (span of its line + 0.5s, Kling 3–15s),
  then step 6: the hooks one by one (HK1 first, split layout EG01), as prompts + generations on the board.
- Open flags from the Build Sheet: F2 (Pat's cropped trousers vs strap visibility), F4 (comparative claim P-005),
  F7 (`package_closed.jpg` missing), F8 (AVATAR-SHEET doc inconsistency), F10 (watermark omit).

- (2026-09-28, 15:05 UTC) **Board split into four (user: separate Final output, Plan and Old versions boards, for storage).**
  Current https://claude.ai/artifact/GKZDjmZkh4wwm7RxtXj7Tp · Old https://claude.ai/artifact/463LLedeKaxFUa38SA4tEJ (the earlier
  "archive" page, now the Old versions board) · Final https://claude.ai/artifact/9Y3ww3H8Bc3X6Xsp2JPVPW · Plan https://claude.ai/artifact/8BJ5uy6ejnwZdr9up5xjGk.
  50 old files copied to Old (plus the 57 already there); 44 Old cards written; the 12 unchosen VO takes (T1–T3) moved off Current.
  Current's version entries marked `archived` + `archiveAsset`. 7 of the 73 moved files deleted from Current; the other 66 wait for
  the user's go-ahead (the permission check stopped the deletes). 22 old files deleted earlier can't be moved.
- (2026-09-28, user: "delete them") Moved files removed from the Current board: 53 more deleted (60 in total with the
  first 7), 7 were already gone. Current board now 725 MB of 1 GB (other renders keep landing). 6 files (~34 MB) were
  blocked by the permission check and are still on Current, each with a copy on the Old board:
  57aef9eb49cf60d025ea100a37c8ccbc, aa0f6eb6917b659a3455f1bbc0c38e03, d7ca27c6d08d02e33eded7921da1eb57,
  da04e4485833c18ad677cb8ae012a9a6, e7ae5f54460e487f96978d2d1d335e74, ee2d7f040c106112397c9ab3b8de495f.
