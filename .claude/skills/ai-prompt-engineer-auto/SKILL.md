---
name: ai-prompt-engineer-auto
description: AUTOMATIC run mode of the AI Prompt Engineer Global Standards (V7.60.1, Appendix E0/E11, §5, §18B, §22U, §22V, §22W, §24I, §30H). Load ONLY when the user explicitly says "we will use automation", sends an Intake Pack or Drive intake with RUN: AUTOMATION, or directly instructs you to run a build automatically (generate, check, reroll and trim yourself). Never load it for ordinary prompt-writing, for "check this render", "fix this" or "trim this clip" — those are the default Manual mode (ai-prompt-engineer). Requires ai-prompt-engineer loaded too.
---

# AI Prompt Engineer — Automatic run mode

**Manual is the default, always** (§1, §44 default 83). This skill runs only when the user has explicitly called it — "we will use automation" or an equally direct instruction — and only for the build it was called on. If the wording is ambiguous, ask one question; never assume. It is never carried into the next build.

**This skill adds execution; it changes no craft.** Load `ai-prompt-engineer` first and follow it for every prompt. The master file `standards/AI_Prompt_Engineer_Global_Standards.md` wins over this summary. Before the first call, read these sections by grepping their headings:

```
Grep  pattern="^## (E(0|1|2|3|7|9|11)|5|18B|22U|22V|22W|24I|30H)\."  path="standards/AI_Prompt_Engineer_Global_Standards.md"  (-n)
```

## 1. Start of run — before any credit is spent

1. **Confirm the trigger** in one line: "Automatic run for build `<name>`." An Intake Pack with `RUN: AUTOMATION` is the trigger (§18B).
2. **Credit cap.** Take the user's per-build cap; if none was given, ask once. Read all three balances and record them: Higgsfield `balance`, Kling `query_membership_and_credits`, Kie `python3 .claude/skills/ai-prompt-engineer/scripts/kie.py credit`.
   **Routing is strict (§5):** images → Higgsfield (below the batch cost → Kie API `kie.py image`, same model as locked, logged, no switch back); Kling → Kling connector; Seedance → Kie API `kie.py seedance` (local refs auto-uploaded to temporary public URLs). Kling or Kie out of credits = stop.
3. **Build directory** `builds/<build>/` per E9, with `run_ledger.json` (E3) and `renders/` and `trim/` folders. Media stays out of git (`.gitignore` covers it). **Drive output (§18B):** create or reuse `<task folder>/OUTPUT/` with `01_ABSORPTION` … `08_EDIT` and `OUTPUT.md`; record the IDs in `builds/<build>/drive.json`. Text uploads through the Google Drive connector; media are indexed in `OUTPUT.md` by platform link.
4. **Tool setup** — the container is ephemeral, so install every session:
   ```
   pip install -q imageio-ffmpeg faster-whisper auto-editor yt-dlp gdown python-docx pypdf cffi
   ```
   `ffmpeg` path: `python3 -c "import imageio_ffmpeg as f; print(f.get_ffmpeg_exe())"`.
5. **Intake → steps 1–5 (§18B).** Drive: `python3 .claude/skills/ai-prompt-engineer/scripts/fetch_drive.py <BUILD> <folder link>`; links: `fetch_inspo.py <BUILD> <links…>`. Report any missing part, unreadable document or FETCH_FAILED link and ask for it before absorbing. Then absorb, and **generate every cast sheet (§19 panel check), the property plate (§30G) and every location plate (§30C)** — QA each per E1 — and ship steps 1–5 as one delivery.
6. **Voice route by mode** — Mode 1–3: §22U (section 5 below) before any talking-head beat. **Mode 4, 5, AI Drama: section 6 below** — no §22U, no HeyGen.

## 2. The loop — per batch

For every batch, in this order:

1. **Write the prompts** per the Manual rules and deliver them as normal (§16, §16B). Nothing is generated from a prompt the user has not been shown.
2. **Credit check** — balance + this batch's cost ≤ cap, else stop (E2 `CREDIT_CAP`). Never raise the cap yourself.
3. **Submit** on the E7 call templates. T2I completes before any I2V (`jobs_wait` or the platform's poll). Log every job ID in the ledger.
4. **Fetch the result** — download the output URL to `builds/<build>/renders/<BEAT-ID>.<ext>` with `curl -sSL -o`. If the download is refused, say so; never describe a render you have not opened.
5. **QA per E1.**
   - **Images: you are the judge (§22V).** Open every image with Read and answer the six questions — does it show the line, product, body, continuity, register, will it animate. Ship `USE` or `REGENERATE · Q<n>: fault → fix`. Two regenerations per fault, then the user with all three versions.
   - **Video: you are the judge (§22W).** `contact_sheet.py <clip>` → Read the sheet (true first and last frames); `--full` and Read single frames where hands, product or text need detail. Seven questions — line, product every frame, body every frame, motion, continuity, technical, enough footage for its slot → `USE` or `REGENERATE`. Silence and timing checks run on the audio (`silencedetect=noise=-40dB:d=0.4`).
   - AUTO rows run by instrument. HUMAN rows run **AGENT-FIRST**: clear pass → proceed; clear fail → E2 remedy; unsure → queue for the user (`AGENT_UNSURE`).
   - **Always queue for the user**, whatever your read: the §28F/§28H closure-sync check, voice (§22D), and Mode 4/5 performance on video. Images are not queued — they get your verdict.
6. **Reroll per E2** — at most two automatic rerolls per beat per failure class, then HUMAN with the failure history. A changed prompt is shown to the user as a new iteration; never change a prompt silently.
7. **Trim (E11)** every talking-head clip that passed QA (section 4 below).
8. **Update the ledger** and ship the batch's QA table, marking which reads were yours and which the user's.
9. **Assemble (§30H)** once an act's B-rolls pass: write `plan.json` (master, `script.lines.txt`, talking-head track or `null`, each B-roll with its phrase) → `assemble.py plan.json --out builds/<build>/edit/<act>.mp4`. Every FAIL is fixed (NEED_LONGER → regenerate that clip longer) before rendering. Then `contact_sheet.py` on the render and a frame either side of each cut, and judge the edit. Deliver rough cut + EDL + report to `08_EDIT`.
10. **Hook variants (§30H)** once the hooks are approved and voiced: write `variants.json` (the body plan once + one entry per hook) → `variants.py variants.json --build <BUILD> --outdir builds/<build>/edit/` → `<BUILD>_HK1.mp4`, `_HK2.mp4`, `_HK3.mp4`. The set must PASS with `body_identical_across_variants: true`. Judge each variant's hook and seam by §22W. Deliver every variant + the set report to `08_EDIT` and list them in `OUTPUT.md`.

## 3. Stop points — the only places the run waits

| Stop | When |
|---|---|
| **Hooks** | §18 step 6 — unchanged; the user approves each hook |
| **Final review** | Every approved beat, the QA table, the queued human checks and the trimmed clips — before the CapCut block |
| **Credit cap** | A batch would cross the cap |
| **Voice clone** | §22U step 6 — the user clones in ElevenLabs and gives the voice ID (skipped only if `ELEVENLABS_API_KEY` is set) |
| **Voice master** | §22U step 10 — the user hears the chosen master before any HeyGen render |
| **Escalation** | Any E2 class that reaches HUMAN |

Nothing else stops the run. Between stops, report only in the batch deliveries and QA tables.

## 4. Trim pass (E11)

```
python3 .claude/skills/ai-prompt-engineer/scripts/trim.py builds/<build>/renders/<BEAT-ID>.mp4 \
    --out builds/<build>/trim/<BEAT-ID>.trim.mp4 [--keep START:END ...]
```

- Cuts dead air and inhales using word timestamps (`faster-whisper`, default `base.en`) plus measured silence, keeps a 120 ms entry breath (`BREATH-A`), and keeps every designed silence from the §28G list passed as `--keep`.
- Never overwrites the original. Prints a JSON report (cut list, transcript, E1 verification). Exit 0 = PASS, 2 = `TRIM_FAIL` → one re-trim with adjusted `--pre/--post`, then HUMAN with the cut list sent as a CapCut line.
- `--dry-run` prints the cut list without rendering.
- Talking heads only. B-roll: head and tail only. Mode 4/5: no cuts inside the take.
- **Unverified on production clips** — tested on a synthetic clip only (17.4s → 9.5s, all gaps closed; the tiny model left ~0.3s of entry breath). The first real run is the E11 open decision; report its numbers.

**Other editing tools** (use when the case fits; all unverified in production):

| Tool | Use |
|---|---|
| `auto-editor <in> --margin 0.08s` | Fast loudness-only dead-air cut; no inhale detection |
| HeyGen `create_filler_word_removal` | Filler words ("um", "uh") on the platform |
| ElevenLabs `creative_transcribe_audio` | Word timestamps on the platform, if local whisper is unavailable |
| Higgsfield `upscale_video`, `reframe` | Upscale or reframe a finished clip — never to change 9:16 |

CapCut still does captions, overlays, motion graphics (§17A), the ambient bed, music and J-cuts. The CapCut block always ships.

## 5. Voice & talking-head pipeline (§22U)

Per speaking character, in order. The master file's §22U table is the rule; this is the run sheet.

| # | Do | How |
|---|---|---|
| 1 | Talking-head image | Higgsfield T2I (E7), 9:16, 2k |
| 2 | 10s voice source clip | Seedance ingredients, 720p, `duration: 10`, image first; opening script line within the 10s word budget; `VOICE-[CHAR]` first in delivery |
| 3–5 | Trim → ×1.2 → loop to ≥ 30s | `python3 .claude/skills/ai-prompt-engineer/scripts/voice_source.py builds/<build>/renders/<char>_voice10.mp4 --name <Keyword> --outdir builds/<build>/voice/` |
| 6 | Clone | **Stop:** hand the user `<Keyword>_clone_source.mp3` and the name; wait for the voice ID. (With `ELEVENLABS_API_KEY`: `POST /v1/voices/add`) |
| 7 | Name | One keyword from the script title (`Knee`); clash → add the first name (`Knee-Maria`) |
| 8–9 | Tag + TTS | **Verbatim:** `script_lines.py <script> --out lines.txt` (spoken lines only, no title/headings/links/visuals); tag a copy from `TAG-PALETTE` (tags only, no word changes); `tts_budget.py tagged.txt --script-lines lines.txt` → must say `verbatim: PASS`, fitted ≤ 5,000 per part; `creative_generate_speech` with `eleven_v3`, the clone ID, 4 takes; poll `creative_get_flow_run_status` |
| 10 | Pick + save | Transcribe each take (faster-whisper) and diff against the script; judge the four criteria; save `<Keyword>_master.mp3`; **stop — the user listens** |
| — | **Voice-only builds** (all B-roll, narrated, Mode 4/5, AI Drama) | Stop here. The master is the VO, or the Seedance `audios_list` ingredient |
| 11 | Avatar | HeyGen `create_asset_upload` → PUT → `complete_asset_upload` → `create_photo_avatar`, one per look |
| 12 | Split | Cut the master at sentence ends (word timestamps) into one segment per on-screen talking-head beat |
| 13 | Render | Upload each segment; `create_video_from_avatar` with `engine: {type: "avatar_v"}`, `audioAssetId`, `9:16`, `1080p`, `motionPrompt` = the beat's gestures. Rejected → Avatar IV + `expressiveness: "high"` + `motionPrompt`, logged. Then QA and E11 trim as normal |

## 6. Film voice masters (§24I) — Mode 4, Mode 5, AI Drama

Per speaking character, after the cast sheets pass:

1. Seedance ingredients, 720p, 9:16, `duration: 10`, `images_list: [<face-only sheet>]`, no audio. A plain informational line from the script inside the 10s word budget; delivery = `VOICE-[CHAR]` verbatim, then level, even, unhurried, no emotion.
2. `ffmpeg -i <clip> -vn -c:a copy builds/<build>/voice/<CHAR>_voice_master.<ext>` — **stream copy. No trim, no E11, no speed change, no loop, no cleanup.** Keep the clip too.
3. Check: one speaker, every word audible, neutral affect, no music. Fail → regenerate the clip; never edit the audio. Queue the master for the user to hear (voice is always queued).
4. Attach the same file in `audios_list` on every Seedance dialogue call for that character.
5. Narrator only: clone the untrimmed master (looped whole to ≥30s if short, no speed-up) and voice the VO in Eleven v3 per §22U steps 6–10.

## 7. Never

- Run without the explicit call, or continue into another build.
- Skip the step-6 gate or the final review.
- Raise the credit cap, or submit a batch that crosses it.
- Pass a render you have not opened.
- Change a prompt without showing it.
- Overwrite an original render, or commit media to git.
- Trim, speed up, loop or clean a film voice master.
