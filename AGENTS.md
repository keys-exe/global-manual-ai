# global-manual-ai — instructions for Codex and other agents

This repo runs under the **AI Prompt Engineer — Global Standards**. The rules are the same for every agent; this file only points to them, so nothing here can drift from them.

**Read these, in this order, at the start of every task:**
1. `standards/AI_Prompt_Engineer_Global_Standards.md` — the master file and the **only** standard. It is ~7,400 lines: never read it whole. Find a section by grepping its heading (e.g. `grep -n '^## 22F\.' standards/AI_Prompt_Engineer_Global_Standards.md`), then read that range, and follow its cross-references.
2. `.claude/skills/ai-prompt-engineer/SKILL.md` — the always-on rules and how to pull sections. **Manual** run mode, always the default.
3. `.claude/skills/ai-prompt-engineer-auto/SKILL.md` — the Automatic run mode. Load **only** when the user explicitly says "we will use automation" (Appendix E0).
4. `CLAUDE.md` — the repo's standing instructions (default-branch rule, "a system update never touches existing builds", the Generation Boards, resuming a build). They apply to you too.

If this file, `CLAUDE.md`, a skill or anything else disagrees with the master file, **the master file wins**.

**Before any work:** make sure the checkout is current with the default branch (`git fetch origin` then merge the default branch) — never write a prompt on stale standards.

**Where things go.** Product Sheets (Appendix B) under `products/`, Build Sheets (Appendix C) and a build's files under `builds/<build-id>/`. Nothing product-, brand-, character- or location-specific goes into `standards/`. Changes to the standards follow §0 and §34: say what will change and which sections first, edit the master file, keep the skill summaries in sync in the same commit, bump the version and changelog on a cut.

**What only Claude sessions can do.** The Generation Boards (claude.ai artifacts), their data store, the hourly Fix-check Routines and the connected generation accounts (Higgsfield, Kling, HeyGen, Kie…) are reached through Claude's own tools. Without them you can still read and write the standards, Product/Build Sheets, prompts, build notes and scripts. Do not edit a board or its data by other means; when a step needs the board or a connector, say so and leave it for a Claude session. Record what you did in `builds/<build-id>/BUILD_NOTES.md` so the next session picks it up.

**Publishing a change.** Commit, push, and merge into the repo's default branch the same task (a pull request into it, merged) — other accounts and new sessions start from the default branch.
