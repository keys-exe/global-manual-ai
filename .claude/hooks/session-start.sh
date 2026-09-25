#!/bin/bash
# Installs the tools the ai-prompt-engineer scripts use (Drive/inspo fetch,
# script extraction, trim, voice source, clone, assembly) and pre-loads the
# Whisper model trim.py uses. Cloud sessions only; safe to re-run.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# cffi: the system cryptography package (pulled in by pypdf) fails without it
pip install -q --disable-pip-version-check \
  imageio-ffmpeg faster-whisper yt-dlp gdown python-docx pypdf cffi 2>&1 | grep -v "as the 'root' user" || true

python3 -c "import imageio_ffmpeg, faster_whisper, yt_dlp, gdown, docx, pypdf"

# trim.py default model; cached so the first trim does not wait on a download
python3 -c "from faster_whisper import WhisperModel; WhisperModel('base.en', device='cpu', compute_type='int8')" 2>/dev/null \
  || echo "session-start: Whisper model not pre-loaded (downloads on first trim)" >&2
