#!/bin/bash
# 1. Standards freshness (every session, local CLI and cloud): compares this
#    checkout with the repo's default branch, fast-forwards it when that is
#    safe, and otherwise tells the session it is behind — so nobody writes a
#    prompt on stale standards. Prints to stdout: Claude reads it as context.
# 2. Installs the tools the ai-prompt-engineer scripts use (Drive/inspo fetch,
#    script extraction, trim, voice source, clone, assembly) and pre-loads the
#    Whisper model trim.py uses. Cloud sessions only; safe to re-run.
set -euo pipefail

STANDARDS="standards/AI_Prompt_Engineer_Global_Standards.md"

standards_version() {  # $1 = git rev (or empty for the working tree)
  if [ -n "${1:-}" ]; then git show "$1:$STANDARDS" 2>/dev/null; else cat "$STANDARDS" 2>/dev/null; fi \
    | sed -n 's/^\*\*Version \([0-9][0-9.]*\).*/\1/p' | head -1
}

freshness() {
  cd "${CLAUDE_PROJECT_DIR:-.}" || return 0
  git rev-parse --git-dir >/dev/null 2>&1 || return 0
  local default behind local_v remote_v branch
  default=$(git symbolic-ref -q --short refs/remotes/origin/HEAD 2>/dev/null | sed 's#^origin/##' || true)
  if [ -z "$default" ]; then
    default=$(timeout 20 git remote show origin 2>/dev/null | sed -n 's/.*HEAD branch: *//p' | head -1 || true)
  fi
  [ -n "$default" ] || { echo "session-start: no default branch found on origin — check the standards version by hand"; return 0; }
  if ! timeout 30 git fetch -q origin "$default" 2>/dev/null; then
    echo "session-start: could not fetch origin/$default (offline?) — standards V$(standards_version) in this checkout, freshness unknown"
    return 0
  fi
  behind=$(git rev-list --count "HEAD..origin/$default" 2>/dev/null || echo 0)
  local_v=$(standards_version); remote_v=$(standards_version "origin/$default")
  if [ "$behind" -eq 0 ]; then
    echo "session-start: standards V${local_v:-?} — checkout up to date with origin/$default"
    return 0
  fi
  branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "")
  if [ "$branch" = "$default" ] && [ -z "$(git status --porcelain 2>/dev/null)" ] \
     && git merge -q --ff-only "origin/$default" 2>/dev/null; then
    echo "session-start: fast-forwarded $default by $behind commit(s) → standards V${remote_v:-?} (was V${local_v:-?})"
    return 0
  fi
  echo "session-start: THIS CHECKOUT IS $behind COMMIT(S) BEHIND origin/$default — standards here V${local_v:-?}, on origin/$default V${remote_v:-?}."
  echo "session-start: merge the default branch before writing any prompt or deliverable: git merge origin/$default  (on branch '$branch'; uncommitted changes, if any, are why it was not fast-forwarded for you)"
}

freshness || true

# 3. Lessons (§34B, user 2026-10-01: "always learn from your mistake"): the latest rules from LESSONS.md,
#    printed every session so no account repeats a mistake another session already made
lessons() {
  local f="${CLAUDE_PROJECT_DIR:-.}/LESSONS.md"
  [ -f "$f" ] || return 0
  local n
  n=$(grep -c '^| L[0-9]' "$f" || true)
  echo "session-start: LESSONS.md holds $n lessons — read it before changing the system or publishing to a board. Latest:"
  grep '^| L[0-9]' "$f" | head -5 | awk -F'|' '{gsub(/^ +| +$/,"",$2); gsub(/\*\*/,"",$7); gsub(/^ +| +$/,"",$7); print "  " $2 ": " $7}'
}
lessons || true

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# cffi: the system cryptography package (pulled in by pypdf) fails without it
pip install -q --disable-pip-version-check \
  imageio-ffmpeg faster-whisper auto-editor yt-dlp gdown python-docx pypdf cffi 2>&1 | grep -v "as the 'root' user" || true

python3 -c "import imageio_ffmpeg, faster_whisper, yt_dlp, gdown, docx, pypdf"

# trim.py default model; cached so the first trim does not wait on a download
python3 -c "from faster_whisper import WhisperModel; WhisperModel('base.en', device='cpu', compute_type='int8')" 2>/dev/null \
  || echo "session-start: Whisper model not pre-loaded (downloads on first trim)" >&2

# assemble.py times B-roll cuts with medium.en (V7.80.0, §30H rule 0): 1.5 GB, fetched in the background
# so the session starts at once and the first assembly does not wait (LESSONS L08)
nohup python3 -c "from faster_whisper import WhisperModel; WhisperModel('medium.en', device='cpu', compute_type='int8')" \
  >/dev/null 2>&1 &
