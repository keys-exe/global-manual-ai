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
- **HK1 (step 6), 2026-09-26 11:10–11:40:** E6 = 5s per band (speech 3.88s). User restated VN01 (binding, §27F):
  top = hands, face cropped at the chin, lightbox + knee X-ray behind; bottom = **extreme close-up** of the knee, the
  hand on the rail revealed only as the camera eases back. **HK1-B v2 USE** (ECU, no hands; v1 was waist-to-feet with
  hands on the rails). **HK1-T:** v1 slide icons → v2 USE on product; the chin crop failed twice on regeneration (v3
  erased the head, v4 full face — the model composes the whole person from the subject sheet), so the two-regeneration
  budget is spent: **v2 is kept and the split band is cut from his chin (y=372 of 2752)** — `hooks/HK1_split_preview.png`.
  The hook split has two B-roll bands, which `assemble.py` can't build (its split needs a talking-head track) — HK1 is
  cut with ffmpeg: top band from his chin, bottom band centred.
- **HK1-T v5 (user: "strap too big"):** the two-hand grip had spread his hands and the shell grew to ~9–10 thumb-widths;
  v5 uses the open-palm grip (HELD_GRIPS), shell barely wider than his palm. Band from y=300. Preview `hooks/HK1_split_preview_v2.png`.
  I2V updated to the palm grip (2,458 chars).
- **HK1-T v6 (user: v5 "now too small"):** size anchored at ~16 cm (a hand's length, wrist crease to fingertips), 2
  variants: v6a USE, v6b REGENERATE (webbing band + loose rings). Band from y=470. `hooks/HK1_split_preview_v3.png`.
  **Product Sheet flag:** `SIZE_HELD` (5–6 thumb-widths ≈ 11 cm) rendered toy-sized — proposed: a hand's length (~16 cm).
  Waiting on the user to confirm the size and both images.
- **HK1-T v7/v8 (user: "strap at the normal state, not that long; X-ray too high and not full"):** v7a/b regenerated
  the scene (kept on the board, superseded). The user then sent v6a: "just edit this and make the strap not that long
  just the original lenght" → **v8 = edit of v6a** (`hooks/HK1-T.v8.edit.txt`, refs v6a + product front/back), band
  back to the original short closed loop. **v8b current (USE)**, v8a alt. Preview `hooks/HK1_split_preview_v4.png`
  (band from y=470). The lightbox still sits only partly in the top band (v6a's framing kept, as asked) — offered a
  follow-up edit if the X-ray must be fully in frame. Waiting on the user to confirm HK1-T v8b and HK1-B v2.
- **HK1-T v9/v10 (user: "re do the product", then "i need a new hk1-t"):** v8b's shell had twisted and its keepers read
  chrome. An edit of v8b (`HK1-T.v9.edit.txt`) was interrupted by the user and is kept unjudged. New render v9
  (`HK1-T.v9.t2i.txt`, v7 prompt + product locks): both REGENERATE (strap held upright, sideways wordmark, extra slides;
  v9b wide with the face). v10 (`HK1-T.v10.t2i.txt`, leaner, "held HORIZONTALLY as in the second photo", subject ref
  first): **v10a** strap horizontal and hand-sized, whole X-ray in the band (band from y=620; the raw frame has a seam
  at ~y=600 that the band skips), thumb over the "e" of the wordmark; **v10b** product exact, lightbox low-left and partly
  cut, strap smaller. Two-regeneration budget spent → the user picks. Recommended v10a + a small edit to lift the thumb.
  Previews `hooks/HK1_split_preview_v10a.png` / `_v10b.png`.
- **Then:** E6 — set every B-roll row's duration from the body word timestamps (span of its line + 0.5s, Kling 3–15s),
- **HK1 clips (step 6, 2026-09-26 13:00–13:25):** user confirmed HK1-T **v10b** and HK1-B v2 on the board. Kling
  `kling-video-v3_0_omni`, 9:16, 1080p, 5s, no audio. **HK1-B:** clip v1 REGENERATE (camera orbited the leg, no step),
  **clip v2 USE** (straight ease-back, step down, hand on the rail ~3.8s; the strap drops low late on — the split
  crop must track it). **HK1-T:** the VN01 turn to show the pad broke the rigid shell every time — v1 curled into a ring,
  v2 flipped upside down with an upright wordmark, v3 bent into a U-cup. Budget spent → user decides. Recommended:
  edit v10b so the pad already faces the camera (PAD_BACK_SHOT) + a small tilt, not a rotation. Prompts:
  `hooks/HK1-T.i2v.v1.json`, `.v2.json`, `HK1-T.i2v.json` (v3); `HK1-B.i2v.v1.json`, `HK1-B.i2v.json` (v2).
- **HK1 redo (user: "the broll didnt follow the visual", then "re make the hook a new set"), 18:20–18:40:** first-last
  frame clips on `kling-video-v3_0` (explicit `tail_image`; omni has none — logged deviation from the locked model).
  **HK1-T fl1 USE:** first = v10b cropped at the chin, last = edit with the pad facing camera → one rigid turn to the pad.
  **HK1-B fl1 USE:** first = ECU edit of v2, last = final frame of clip v2 (hand on the rail) → ECU eases back to the rail;
  fast pull-back ~2s blurs the wordmark briefly. Split preview `hooks/HK1_split_fl1.mp4` (bottom band tracks upward, so
  the strap leaves the band in the last half). New set: HK1-T v11 (T2I) + v12 (reframe edit) all REGENERATE (wrong
  product / face showing) — budget spent, user decides; HK1-B v3 not ECU, **v4a/v4b ECU USE** (edit of v3b).
- **User picks (18:45):** HK1-B = image v2 + clip v2 (set current, `use`); HK1-T = image v24 (new set v12b, confirmed).
  HK1-T clip from v24: first-last on `kling-video-v3_0`, v24 → edit of v24 with the pad facing camera
  (`hooks/HK1-T.i2v.v24.json`), on the board as video v5, To check. Merged the default branch (Manual: the user checks
  every generation — no agent verdicts or regenerations in Manual; board template already live).
- **HK1-B stairs clip (user: image v2 confirmed, "she should be going down the stairs"):** omni from image v2, two steps
  down, camera backing down ahead of her to her hand on the rail (`hooks/HK1-B.i2v.v3.json`) → board video v4, To check.
- **HK1-B fix (user: "going down the stair, not the same steps, normally, no other"):** omni from image v2, a normal walk
  down 3–4 stairs, camera travelling down with her at a fixed distance, no rail reveal (`hooks/HK1-B.i2v.v4.json`) →
  board video v5, To check.
- **HK1-B simplified (user: "simplify the prompt, just a simple going down the stairs B-roll"):** 417-char prompt
  (`hooks/HK1-B.i2v.v5.json`) from image v2 → board video v6, To check. Lesson: for a plain action B-roll a short prompt
  lets the model move naturally; the long product-physics blocks pinned her in place.
- **HK1-B placement (user: "the strap placement is not correct"):** image v2's shell had rotated to the outer side of
  the knee (wordmark off-centre, a slide on the front). Edit of v2 re-seating it per PLACE_LOCK with the locked
  placement refs (front f5263ed7, bent 8a8979ac) → board images v10/v11, To check. New clip waits for the user's pick.
- **HK1-B new set (user: "an overall new image, a new set for HK1-B"):** fresh T2I `hooks/HK1-B.v6.t2i.txt` (ECU on the
  stairs, PLACE-LOCK centred front, refs: subject, hall, product front/back, placement front + bent), 4 variants →
  board images v12–v15, To check. The stairs clip (simple prompt `HK1-B.i2v.v5.json`) runs from the user's pick.
- **HK1-B:** user picked image **v15** (confirmed); clip from it with the simple stairs prompt → board video v7, To check.
