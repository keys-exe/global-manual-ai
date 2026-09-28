#!/bin/bash
# Keeps every session on the latest rules and board design (CLAUDE.md, "Staying in sync").
#   1. Merges the repo's default branch into the current branch when it has new commits.
#   2. Lists Generation Boards still on an older template, so the session republishes them.
# Runs at SessionStart and on every prompt (throttled to once per 10 minutes). Whatever it
# prints is added to the session's context. It never pushes and never blocks the session.

cd "${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null)}" 2>/dev/null || exit 0
git rev-parse --git-dir >/dev/null 2>&1 || exit 0

stamp="$(git rev-parse --git-dir)/sync-main.last"
if [ "${1:-}" = "--throttle" ] && [ -f "$stamp" ] && [ $(( $(date +%s) - $(cat "$stamp") )) -lt 600 ]; then
  exit 0
fi
date +%s > "$stamp"

base=$(git ls-remote --symref origin HEAD 2>/dev/null | sed -n 's|^ref: refs/heads/\(.*\)\tHEAD$|\1|p')
branch=$(git symbolic-ref --short -q HEAD)

if [ -n "$base" ] && [ -n "$branch" ] && [ "$branch" != "$base" ] \
   && timeout 60 git fetch -q origin "$base" 2>/dev/null; then
  if ! git merge-base --is-ancestor "origin/$base" HEAD; then
    if [ -n "$(git status --porcelain --untracked-files=no)" ]; then
      echo "sync-main: '$base' (the default branch) has new commits, but this checkout has uncommitted changes. Commit them, then run: git merge origin/$base"
    elif git merge -q --no-edit "origin/$base" >/dev/null 2>&1; then
      echo "sync-main: merged the latest '$base' (the default branch) into '$branch':"
      git log --oneline "HEAD@{1}..HEAD" --no-merges 2>/dev/null | head -15 | sed 's/^/  /'
      echo "Re-read CLAUDE.md and the skill if they changed (git diff HEAD@{1} --stat). Push with your next commit."
    else
      git merge --abort 2>/dev/null
      echo "sync-main: '$base' (the default branch) has new commits that conflict with '$branch'. Merge it by hand (git merge origin/$base), resolve, commit, push."
    fi
  fi
fi

if [ -f dashboard/board_pages.py ] && [ -f dashboard/boards.json ]; then
  stale=$(python3 dashboard/board_pages.py status 2>/dev/null)
  if [ -n "$stale" ]; then
    echo "sync-main: these Generation Boards are not on the current dashboard/generation_board.html yet. Republish the ones this account owns (CLAUDE.md, 'Board design sync'); leave the others listed for their owner:"
    echo "$stale" | sed 's/^/  /'
  fi
fi
exit 0
