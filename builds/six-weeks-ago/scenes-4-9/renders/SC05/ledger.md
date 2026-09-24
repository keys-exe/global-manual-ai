# SC05 render ledger

| Beat | Job | Model logged | Result |
|---|---|---|---|
| SC05-F01-MASTER v1 | 6efe215c-22d4-445e-b1b0-ce2009891247 | nano_banana_2 (requested pro) | Kitchen floor rendered as sage carpet. Edited below |
| SC05-F01-MASTER v2 | b3caf264-ef49-4233-a0b5-0b2d9e2b2860 | nano_banana_2 | FAIL: film camera and tripod in frame; Margaret rendered dark-haired |
| SC05-F01-MASTER edit | d114a74b-a31c-489d-abff-811d7315cca3 | nano_banana_2 | Floor corrected to beige vinyl tile. Candidate master |

References: Margaret sheet 4aeeae33, Barbara sheet ac26a99c, kitchen plate 210cb8eb, Scene 1 look frame 0f6f2644.
Finding: CAM-FILM's "operated by a camera crew" put a camera rig in frame (v2), as AUD-FILM's boom mic did in JOAN-VM. Every frame prompt now carries a no-crew/no-equipment negative.
| SC05-F02-B-MCU v1 | d089876e-c60c-4a24-9766-2b256b10d04f | nano_banana_2 | FAIL: eyeline screen-right (wrong side) |
| SC05-F03-M-CU | 250f85e1-1c75-4e83-8011-c0ed86ae8c42 | nano_banana_2 | PASS |
| SC05-F04-REVEAL | 925e7638-108d-482d-9bc8-6f38b6519d68 | nano_banana_2 | PASS, note: wordmark sits left of the notch, spec says centred |
| SC05-F05-B-MCU-CANDID v1 | b81ef585-c01e-4b32-a785-64eb59ec457e | nano_banana_2 | FAIL: eyeline and OTS shoulder on the wrong side |
| SC05-F06-M-CU-SCEPTIC v1 | 3bb9fcf6-86e2-4a5b-817c-8e0408d66849 | nano_banana_2 | FAIL: Barbara's shoulder on the wrong side |
| SC05-F07-FINGER | 69c1ea58-8b1f-422b-b225-c19f63ef7c1b | nano_banana_2 | PASS |
| SC05-F08-B-CU-TRUTH v1 | eb09ecf6-1096-41f6-b1a6-9c293191ef7e | nano_banana_2 | FAIL: near lens eyeline |
| SC05-F09-M-CU-RAW | b9506936-26c7-4e7e-b8e1-9e0f2c8acdc6 | nano_banana_2 | PASS |
| SC05-F10-PALM | c9a3a012-afb4-442f-ad00-67d543ecb229 | nano_banana_2 | PASS |
| SC05-F02-B-MCU v2 | b5e4e666-6013-46d3-9686-0d9060c0aa5c | nano_banana_2 | PASS (screen-left eyeline) |
| SC05-F05-B-MCU-CANDID v2 | 29c6f029-d152-4b6f-bbde-8f0f6ff5e9aa | nano_banana_2 | PASS (OTS, Margaret's shoulder screen-left) |
| SC05-F06-M-CU-SCEPTIC v2 | 5fcbe7c9-d07c-4610-b17d-51c8d588729e | nano_banana_2 | PASS (OTS, Barbara's shoulder screen-right) |
| SC05-F08-B-CU-TRUTH v2 | 439d6018-6a08-4999-82e9-e6b0e7af78ac | nano_banana_2 | PASS (screen-left three-quarter) |

Contact sheet (§24H step 4): PASS. Light from the window side in every frame, same clothes, props in state, eyelines Barbara screen-left / Margaret screen-right, floor vinyl in the kitchen.
Cause of the eyeline failures: the scene data had the off-screen sides reversed for Barbara; corrected in scenes_b2.py.

## Round 3 — push-ins from the master camera (user: frames must connect to the master; worn placement must match the worn references)

Method: every coverage frame is the master's own camera position pushed in on a longer lens, with the master attached first. Barbara's singles are in near profile facing screen-left with the radio, cork board, back door and fridge behind her; Margaret faces camera with the window behind, glasses on her nose as in the master. The reveal uses the seated worn reference (54b04c4f) as the placement authority.

| Beat | Job | Result |
|---|---|---|
| SC05-F02-B-MCU | 9c342a32-5557-4c31-9c19-1c7f3184cfb9 | PASS |
| SC05-F03-M-CU | 3cdda2ba-6e14-4fac-9c5e-039116396fb8 | PASS |
| SC05-F04-REVEAL | a854e75d-ef5c-41fc-9156-a7cbaeadbf55 | PASS — near (left) knee, notch under the kneecap, chrome slide at the outer edge, band round behind |
| SC05-F05-B-MCU-CANDID (a) | 9cc7a6dd-8e32-4ee9-8e2e-3a362a08556d | FAIL — impossible over-the-shoulder geography |
| SC05-F05-B-MCU-CANDID (b) | e1403708-1ffc-4ae7-8692-9b6cd1a29d91 | FAIL — face drift, window moved behind her |
| SC05-F05-B-MCU-CANDID (c) | 412edf2f-5337-4ab6-8967-c8b49e4b29be | PASS — edit of F02, next moment |
| SC05-F06-M-CU-SCEPTIC (a) | 27d6a0b0-1f43-41f4-80ea-e6e8a5c37afa | FAIL — white top under Barbara's cardigan |
| SC05-F06-M-CU-SCEPTIC (b) | 26bf2be6-0090-4ca8-80b1-305100df6b2d | PASS — edit, purple t-shirt restored |
| SC05-F07-FINGER | 6383150e-769f-4873-a144-bd20c72584de | PASS |
| SC05-F08-B-CU-TRUTH | fce7baac-83ae-4b50-9281-d1852538dee1 | PASS |
| SC05-F09-M-CU-RAW | ea2fc906-6189-4838-a5b7-eda6d4e9ffea | PASS |
| SC05-F10-PALM | 360af344-863e-4fec-a771-71d95a9d2c42 | PASS |

Round 2 frames moved to rejected/. Contact sheet round 3: PASS.
Lesson: coverage built as push-ins or edits of an approved frame holds identity and geography; coverage described from scratch drifts.
