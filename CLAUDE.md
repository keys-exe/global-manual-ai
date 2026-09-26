# global-manual-ai

This repo runs under the **AI Prompt Engineer — Global Standards** (currently V7.63.0).

- Master file (the only standard): `standards/AI_Prompt_Engineer_Global_Standards.md`
- Project skill that loads it: `.claude/skills/ai-prompt-engineer/SKILL.md` — the **Manual** run mode, always the default
- Automatic run mode: `.claude/skills/ai-prompt-engineer-auto/SKILL.md` — load **only** when the user explicitly says "we will use automation" (Appendix E0)

**At the start of every task, invoke the `ai-prompt-engineer` skill** and follow it. Before writing any deliverable, pull the relevant sections from the master file by grepping their headings (the file is too large to read whole). If this CLAUDE.md, the skill or anything else disagrees with the master file, the master file wins.

Changes to the standards follow §0 and §34: say what will change and which sections before editing; edit the master file; keep the skill's summary in sync in the same commit; bump the version and changelog on a cut.

Product Sheets and Build Sheets (Appendix B / C schemas) go under `products/` and `builds/` respectively. Nothing product-, brand-, character- or location-specific goes into `standards/`.

## Generation Board (standing instruction from the user, 2026-09-26)

Every generation goes on the **Generation Board**: https://claude.ai/artifact/HVPuUcnNK1MUrCYnou9UnJ (source: `dashboard/generation_board.html`). Both run modes, every build, no need to ask.

- One `builds/<build-id>` doc per build (name, product, mode, format, run, aspect, `folders` = Drive OUTPUT folder IDs from `drive.json`, `balances`, `balancesAt`).
- One `generations/<build-id>__<BEAT>` doc per beat: `build`, `stage` (`absorption` `cast` `locations` `voice` `hooks` `talking` `broll` `edit`), `beat`, `title`, `line` (verbatim script line), `imagePrompt` / `imageModel` (step 1), `prompt` / `model` (step 2 video, or the only prompt), `duration`, `credits`, `status` (`planned` `ready` `generating` `review` `use` `regenerate`), `imageStatus` (`review` `confirmed` `regenerate`), `fault` / `imageFault` (`Q<n>: fault → fix`), `regens` / `imageRegens`, `imageAsset` / `imageType`, `videoAsset` / `videoType`, and per step the connector record: `imageConnector` / `videoConnector` (Higgsfield, Kling, Kie AI…), `imageUrl` / `videoUrl` (the connector's original link), `imageCredits` / `credits`, `imageRes` (e.g. 1080×1920) / `duration` (s), `imageAt` / `videoAt` (ms); `updatedAt` (ms).
- Generations run through the connectors (§5). The page can't show a connector's CDN link directly, so every result is downloaded and uploaded to the board as an asset; the original link goes in `imageUrl` / `videoUrl`.
- Write with the `ArtifactData` tool (batch when more than two docs). When you write a prompt, add or update its doc (`status: ready`). When a render exists, download it locally, upload it with the Artifact tool (`url` = board, `asset: true`) and store the returned id in `imageAsset` / `videoAsset`. Record the §22V / §22W verdict the same turn.
- Manual run view: cast and locations have an image step only; hooks, talking heads and B-roll go image first, then video once the image is confirmed; the other stages have one file step.
