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

## Round 4: side-by-side blocking (master B), realistic movement

Direction: from "Can I show you something?" Barbara moves her chair round and sits beside Margaret. She shows her knee to Margaret, not to camera. Every pose must be physically real: weight in the chairs, feet flat, natural knee angles, trousers that behave like cloth. The first side-by-side pass (F12–F19, never committed) was dropped for awkward limbs and geography drift.

| Beat | Job | Result |
|---|---|---|
| SC05-F11-MASTER2 | ce8e414e-a0b2-40b4-8978-e56f1cb031ed | PASS: chosen master "B" |
| SC05-F20-CHAIR-MOVE (a) | 22a3a8f7-6b2c-4fee-acf7-6c2a0c8b8691 | FAIL: chair left standing, not being moved |
| SC05-F20-CHAIR-MOVE (b) | 4a483a45-e3f1-4aba-9dee-c1c68653542d | PASS: both hands on the chair rail, sliding it into place |
| SC05-F21-SIT-BESIDE | 9a876ae9-b2c6-44f0-bacb-18c85f7faa23 | PASS: lowering onto the seat, hand on the table taking her weight |
| SC05-F22-HITCH (a) | 77021768-4312-400d-a92b-6101972958f0 | FAIL: trouser leg slit open, impossible cloth |
| SC05-F22-HITCH (b) | a50f73b1-bb5b-40f2-ab19-982768e4dcc3 | FAIL: cardigan missing |
| SC05-F22-HITCH (c) | 5dd5ef6c-cc62-4ad8-b63a-c9dc3b5eca38 | PASS: edit of (b), cardigan restored |
| SC05-F23-REVEAL-2S | e00e245a-1b9b-497a-b41a-d8a77a22a847 | PASS: knee turned to Margaret, strap under the kneecap, Margaret leaning in |
| SC05-F24-REVEAL-INSERT | 1a85038a-dc53-4004-abb9-365edc7be41c | PASS: over Margaret's shoulder, leg bent, foot flat |
| SC05-F25-B-MCU-SIDE | 452b2f03-9a60-4d3d-8ad8-50341fcc17d0 | PASS |
| SC05-F26-M-MCU-SIDE | ac4e736f-da5f-4014-a961-60541901174d | PASS |
| SC05-F27-TENDON (a) | e4cdef86-273f-4030-a083-915296bc31ab | FAIL: too wide, no finger on the tendon |
| SC05-F27-TENDON (b) | 7915ab13-e377-4756-ae6c-c0ca72d25200 | FAIL: a strap appeared on Margaret's knee |
| SC05-F27-TENDON (c) | 71c9c328-01b3-479d-abec-64568ed54e5f | PASS: Margaret's finger through her trouser, Barbara's on the notch |
| SC05-F28-B-CU-TRUTH | 7d6900d2-a948-46a0-873a-a81a6cf2860d | PASS |
| SC05-F29-M-CU-RAW (a) | 85aef0f5-0770-477c-9a30-46c3c85e01e7 | FAIL: two-shot, not a close-up |
| SC05-F29-M-CU-RAW (b) | af76c426-02dc-4338-8a00-58d472647999 | FAIL: glasses hanging, not on her nose |
| SC05-F29-M-CU-RAW (c) | bb14c764-f8ab-45d4-aebf-bed8070e6009 | PASS |
| SC05-F30-PALM | e4ca8c68-5fdb-4581-8010-ad259c1604ff | PASS |

From C02's "Can I show you something?" onwards, round-3 frames F04–F10 are superseded by F20–F30. F01–F03 still cover the opening at the original seating.
Lesson: write the body mechanics into every prompt (weight, feet, knee angle, cloth), and build each movement beat as an edit of its neighbour so the action reads as one continuous motion.

## Round 5: Barbara backs up to show the strap, then moves beside for the tendon

Direction: Barbara backs her chair up and faces Margaret to show the strap. For the demonstration she gets up and moves beside Margaret.

| Beat | Job | Result |
|---|---|---|
| SC05-F31-BACK-UP (edits a–d) | 7a8d0be6 / 91e2fd39 / c78a19f2 / f0882ce7 | FAIL: the edit kept her at the table edge |
| SC05-F31-BACK-UP | 6cff3a38-3af4-422e-ac47-92b76f239a4b | PASS: fresh frame on master 1; chair out on open floor, facing Margaret |
| SC05-F32-HITCH-ACROSS | 30e6132a-4fea-448f-9b3d-d61cca6197c9 | PASS: draws the trouser up; Margaret leans over the table corner |
| SC05-F33-REVEAL-ACROSS | 1417587c-4bff-4fbf-bad3-8e9c8cc10cb2 | PASS: knee turned to Margaret, strap under the kneecap |
| SC05-F34-KNEE-INSERT | 7aca7e70-5307-4b3e-8aa1-4c663d1df554 | PASS: side view, Margaret soft behind |
| SC05-F35-B-MCU-BACKED (a) | cb0fadd9-3ba4-4b03-8478-f895b5379bb5 | FAIL: reads as sitting on the floor |
| SC05-F35-B-MCU-BACKED (b) | e4d22aa5-42a6-47f9-90f5-2462e6c1e6ce | PASS: on her chair, back door behind |
| SC05-F36-M-CU-ACROSS | d89e5b1a-f7cc-4b18-bc59-49edf08b36e2 | PASS: "That little thing?" |

Order: F01 → F03 → F31 back up → F32 hitch → F33 reveal → F34 insert → F35/F36 talk across (C03–C06) → F20 moves her chair → F21 sits beside → F11 master 2 → F22 draws the trouser up again → F27 tendon (C07–C08) → F25/F26, F28/F29 → F30 palm.
F23/F24 (reveal already beside her) are moved to rejected/ because the reveal now happens across the gap.

## Round 6: real-life drama coverage in the inspo reel's style

Direction: "these are not like real life scenarios". Diagnosis: the earlier sets were wide shots of the whole room from the doorway, evenly lit, which read as staged stock photography. The inspo reel is tight and intimate: faces fill the frame on an 85mm lens, light comes from the window side and falls off into shadow with a warm lamp in the background, skin is real, and shoulders and mugs sit soft in the foreground. The blocking is unchanged: Barbara backs up and faces Margaret to show the strap, then drags her chair beside Margaret for the tendon.

| Beat | Job | Result |
|---|---|---|
| SC05-F40-B-ASK | b29fb553-bfee-4cc0-a08a-208575763c9e | PASS |
| SC05-F41-BACK-UP | f8fcee53-804d-4802-b5fc-23a6b090e6dd | PASS |
| SC05-F42-HEM | 3cf6f163-804f-4ba1-a899-35d52ee96b54 | PASS |
| SC05-F43-M-LEAN | c5e06bea-677c-4d7a-a5a0-c1c1c9175da1 | PASS |
| SC05-F44-REVEAL-OTS | 528bea19-26d2-48d8-a5a7-5ecafa9c22a3 | PASS |
| SC05-F45-B-PROUD | 6ac42a08-4401-49e6-b669-cc28632b799c | PASS |
| SC05-F46-M-SCEPTIC | fd96999d-56c6-4e3a-a59f-aa71ba366c6c | PASS |
| SC05-F47-B-SIDEWAYS | 52c0c914-8acf-4e10-9448-3b438e13b485 | PASS |
| SC05-F48-CHAIR-DRAG | 7faabe4e-c3a0-47c2-a228-1936d16a16f5 | PASS |
| SC05-F49-BESIDE-2S | 9ca36851-21e1-4da7-8a2f-6655bb125b7e | PASS |
| SC05-F50-TENDON | 30ff8635-61ce-4e8e-84cd-eb0f4cbf7f00 | PASS |
| SC05-F51-M-YES | 75df5fbf-2bfb-4106-9845-7179885adcbc | PASS |
| SC05-F52-B-TRUTH | b2edff3b-82b5-4dec-9fca-77c49fcbb4b0 | PASS |
| SC05-F53-M-RAW | f133ada9-797b-43bb-b83b-0bc0ab4d184f | PASS |
| SC05-F54-PALM | 3efe0e73-0863-4b32-8b2e-8994b177c311 | PASS |

This set supersedes F04–F10, F20–F36 for the reveal-onward coverage. F01–F03 still cover the opening.
