---
name: ai-prompt-engineer-auto
description: AUTOMATIC run mode of the AI Prompt Engineer Global Standards (V7.56.0, Appendix E0/E11). Load ONLY when the user explicitly says "we will use automation" or directly instructs you to run a build automatically (generate, check, reroll and trim yourself). Never load it for ordinary prompt-writing, for "check this render", "fix this" or "trim this clip" — those are the default Manual mode (ai-prompt-engineer). Requires ai-prompt-engineer loaded too.
---

# AI Prompt Engineer — Automatic run mode

**Manual is the default, always** (§1, §44 default 83). This skill runs only when the user has explicitly called it — "we will use automation" or an equally direct instruction — and only for the build it was called on. If the wording is ambiguous, ask one question; never assume. It is never carried into the next build.

**This skill adds execution; it changes no craft.** Load `ai-prompt-engineer` first and follow it for every prompt. The master file `standards/AI_Prompt_Engineer_Global_Standards.md` wins over this summary. Before the first call, read these sections by grepping their headings:

```
Grep  pattern="^## E(0|1|2|3|7|9|11)\."  path="standards/AI_Prompt_Engineer_Global_Standards.md"  (-n)
```

## 1. Start of run — before any credit is spent

1. **Confirm the trigger** in one line: "Automatic run for build `<name>`."
2. **Credit cap.** Take the user's per-build cap; if none was given, ask once. Read the balance (`balance` / `get_credits` / `query_membership_and_credits` on the routed platform) and record it.
3. **Build directory** `builds/<build>/` per E9, with `run_ledger.json` (E3) and `renders/` and `trim/` folders. Media stays out of git (`.gitignore` covers it).
4. **Tool setup** — the container is ephemeral, so install every session:
   ```
   pip install -q imageio-ffmpeg faster-whisper auto-editor
   ```
   `ffmpeg` path: `python3 -c "import imageio_ffmpeg as f; print(f.get_ffmpeg_exe())"`.
5. Run §18 steps 1–5 exactly as in Manual and ship them as one delivery.

## 2. The loop — per batch

For every batch, in this order:

1. **Write the prompts** per the Manual rules and deliver them as normal (§16, §16B). Nothing is generated from a prompt the user has not been shown.
2. **Credit check** — balance + this batch's cost ≤ cap, else stop (E2 `CREDIT_CAP`). Never raise the cap yourself.
3. **Submit** on the E7 call templates. T2I completes before any I2V (`jobs_wait` or the platform's poll). Log every job ID in the ledger.
4. **Fetch the result** — download the output URL to `builds/<build>/renders/<BEAT-ID>.<ext>` with `curl -sSL -o`. If the download is refused, say so; never describe a render you have not opened.
5. **QA per E1.**
   - Images: open the file with Read and judge it.
   - Video: grab frames with ffmpeg (`-ss <t> -frames:v 1`) at the first frame, the contact/closure moment and the last frame, then Read them. Silence and timing checks run on the audio (`silencedetect=noise=-40dB:d=0.4`).
   - AUTO rows run by instrument. HUMAN rows run **AGENT-FIRST**: clear pass → proceed; clear fail → E2 remedy; unsure → queue for the user (`AGENT_UNSURE`).
   - **Always queue for the user**, whatever your read: subject identity across beats, the §19 avatar sheet, the §28F/§28H closure-sync check, voice (§22D), and Mode 4/5 performance and contact sheets.
6. **Reroll per E2** — at most two automatic rerolls per beat per failure class, then HUMAN with the failure history. A changed prompt is shown to the user as a new iteration; never change a prompt silently.
7. **Trim (E11)** every talking-head clip that passed QA (section 4 below).
8. **Update the ledger** and ship the batch's QA table, marking which reads were yours and which the user's.

## 3. Stop points — the only places the run waits

| Stop | When |
|---|---|
| **Hooks** | §18 step 6 — unchanged; the user approves each hook |
| **Final review** | Every approved beat, the QA table, the queued human checks and the trimmed clips — before the CapCut block |
| **Credit cap** | A batch would cross the cap |
| **Escalation** | Any E2 class that reaches HUMAN |

Nothing else stops the run. Between stops, report only in the batch deliveries and QA tables.

## 4. Trim pass (E11)

```
python3 .claude/skills/ai-prompt-engineer-auto/scripts/trim.py builds/<build>/renders/<BEAT-ID>.mp4 \
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

## 5. Never

- Run without the explicit call, or continue into another build.
- Skip the step-6 gate or the final review.
- Raise the credit cap, or submit a batch that crosses it.
- Pass a render you have not opened.
- Change a prompt without showing it.
- Overwrite an original render, or commit media to git.
