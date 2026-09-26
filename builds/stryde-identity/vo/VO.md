# Narrator VO — §22U steps 6–10 (stryde-identity)

**Clone (steps 6–7):** by API on the user's instruction, 2026-09-26 09:30 UTC. `Identity-Narrator` · voice ID
**`F5vpA7jC44a7w7td6GdQ`** · source `voice/Identity_clone_source.mp3` (41.27s) · background-noise removal on.
`Identity` was already on the account (Carol, `identity-callout-v2`), so the suffix was added (§22U step 7).

## One-go VO (user's instruction, 2026-09-26 09:47 UTC)

"Generate it in one go, all hooks and body, for consistent voice-over, then trim them. Delete the previous ones."
The first round (hooks and body as separate requests) was deleted from the board, the build tree and ElevenLabs history.

**Text (step 8):** `ALL.tagged.txt` = HK1, HK2, HK3, body, in script order, one request. Lock against the whole
`script.lines`: **PASS** · 1,354 chars · rung 1 · 8 tags (`[serious]` opens; body tags as before, its opening
`[serious]` dropped because HK1's already sets it).

**TTS (step 9):** ElevenLabs connector, `eleven_v3`, 4 takes, flow `tEAVkrzG6BhDg0yzhlqU` (≈ 5,416 credits).

**Split** (`split_vo.py`): medium.en word timestamps on each full take → cut in the middle of the silence after
"bone." / "work." / "anymore." → `HK1` `HK2` `HK3` `BODY`.

**Trim — redone 2026-09-26 on the user's correction** ("the cuts at the end of the hook are so fast the word doesn't
end; there are still inhales"). The first trim (`trim.py`, transcript word edges + 80 ms) cut 0.13–0.2s off every hook
ending and left the quiet inhales (~−47 dB) that Whisper folds into the next word. Replaced by
`scripts/vo_trim.py` (Pending Amendment 2026-09-26): word decays kept to −60 dB, breaths cut at the script's phrase
boundaries only (so "th" in "through" and "force and" stay), pauses 0.28s after a phrase end / 0.10s elsewhere.
All 16 pieces re-checked word for word (medium.en, beam 5): **all verbatim**.

| Take | HK1 | HK2 | HK3 | Body | Breaths cut (body) | Ending of the generation |
|---|---|---|---|---|---|---|
| T1 `2baq…` | 4.07 | 3.92 | 4.43 | 59.60s | 6 | ✗ cut off mid-"you" (−30 dB on the last frame) |
| T2 `3oxV…` | 4.16 | 4.26 | 4.55 | 62.13s | 8 | ✗ cut off mid-"you" (−29 dB) |
| T3 `H8WK…` | 4.04 | 3.88 | 4.11 | 60.47s | 4 | ✗ cut off mid-"you" (−25 dB) |
| **T4** `ZzBl…` | 4.09 | 4.34 | 4.33 | **62.02s (~170 wpm)** | 3 | ✓ decays to −54 dB |

Hook endings: every hook's last word now decays to −55…−60 dB before the 20 ms fade (was cut at speech level).

**Recommended: T4** — the only take whose last word is complete in the generation itself (ElevenLabs cut the
end of T1–T3; a trim cannot restore it, §22U step 10 (4)). Its hooks pass too, so the whole set stays one voice.
Each variant = HKn + BODY of the **same take**.

**Step 10 (Manual): the user listens and picks the take** (board → Voice, cards `VO-T<n>-<part>`). Accent and
realism are the ear's call (unverified by instrument).
