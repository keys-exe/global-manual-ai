#!/usr/bin/env python3
"""§24M (V7.92.0) — take the music out of a clip, keep the voice and the sound effects.

User, 2026-10-02: "we still getting ones with music in seedance can we integrate an editing tool here? a free one".
Seedance sometimes adds background music despite NEG-SOUND and `generate_audio: false` (§24M, V7.73.3). This
separates the clip's sound into dialogue / effects / music with TIGER-DnR (Tsinghua, ICLR 2025, Apache-2.0,
vendored in `vendor/tiger_dnr`), estimates the music, and subtracts it from the original — so the voice and the
effects are the original's own sound, untouched, with only the music taken out.

Usage:
  unmusic.py CLIP [CLIP ...] [--check] [--out-dir DIR] [--threshold DB] [--hq] [--json]

  CLIP           a video (.mp4/.mov) or audio (.wav/.mp3/.m4a) file
  --check        measure only: report how loud the music is and exit 1 if any clip has music (no files written)
  --out-dir      where to write (default: next to the clip)
  --threshold    music level, in dB relative to the whole mix, from which a clip counts as having music (default -20)
  --hq           overlapping passes (slower, smoother on clips over 12 s)
  --json         machine-readable report

Writes, for a clip with music (or for every clip when not --check):
  <stem>.nomusic.mp4   the same picture (stream-copied, never re-encoded) with the music taken out (AAC 192k)
                       — for an audio input, <stem>.nomusic.wav
  <stem>.music.wav     the music that was taken out, to listen to

Report per clip: music_db (music RMS relative to the mix, dB), music_peak_db (loudest 0.5 s window of music relative
to the mix there), has_music (music_db >= threshold or music_peak_db >= threshold + 6).

Needs (CPU is fine — about 5 s of processing per second of stereo audio):
  pip install torch --index-url https://download.pytorch.org/whl/cpu
  pip install soundfile huggingface_hub numpy
ffmpeg: the system one, else imageio_ffmpeg's bundled binary.
"""
import argparse, contextlib, io, json, os, shutil, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
AUDIO_EXT = {".wav", ".mp3", ".m4a", ".aac", ".flac", ".ogg"}
SR = 44100


def ffmpeg():
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        sys.exit("unmusic.py: no ffmpeg — install ffmpeg or `pip install imageio-ffmpeg`")


def need():
    miss = []
    for mod in ("torch", "soundfile", "huggingface_hub", "numpy"):
        try:
            __import__(mod)
        except ImportError:
            miss.append(mod)
    if miss:
        sys.exit("unmusic.py needs " + ", ".join(miss) + ":\n  pip install torch --index-url https://download.pytorch.org/whl/cpu\n"
                 "  pip install soundfile huggingface_hub numpy")


_model = None


def model():
    global _model
    if _model is None:
        import torch
        sys.path.insert(0, str(HERE / "vendor"))
        from tiger_dnr import TIGERDNR
        torch.set_num_threads(max(1, os.cpu_count() or 1))
        with contextlib.redirect_stdout(io.StringIO()):   # the upstream model prints its band widths on load
            _model = TIGERDNR.from_pretrained("JusperLee/TIGER-DnR")
        _model.eval()
    return _model


def music_of(audio, hq=False):
    """audio: float32 [channels, samples] at 44.1 kHz -> the music estimate, same shape.
    Each channel runs alone as mono (the model's own input shape); only the music network runs."""
    import numpy as np, torch
    m = model()
    out = np.zeros_like(audio)
    hop = 4.0 if hq else 12.0
    with torch.no_grad(), contextlib.redirect_stdout(io.StringIO()):
        for c in range(audio.shape[0]):
            x = torch.from_numpy(np.ascontiguousarray(audio[c:c + 1]))[None]          # [1, 1, T]
            est = m.wav_chunk_inference(m.music, x, target_length=12.0, hop_length=hop)  # [3, 1, T]
            out[c] = est[0, 0].numpy()                                                 # track 0 = music (as upstream forward)
    return out


def level(y):
    import numpy as np
    return 20 * np.log10(np.sqrt(np.mean(np.square(y))) + 1e-9)


def peak_rel(music, mix, win):
    """The loudest window of music relative to the mix in the same window (dB): music that swells in a gap."""
    best = -120.0
    for i in range(0, max(1, mix.shape[-1] - win + 1), win // 2):
        mx = level(mix[..., i:i + win])
        if mx < -50:          # near-silence: nothing to judge
            continue
        best = max(best, level(music[..., i:i + win]) - mx)
    return best


def run(clip, a, ff):
    import numpy as np, soundfile as sf
    clip = Path(clip)
    video = clip.suffix.lower() not in AUDIO_EXT
    with tempfile.TemporaryDirectory() as td:
        wav = Path(td) / "in.wav"
        r = subprocess.run([ff, "-v", "error", "-y", "-i", str(clip), "-vn", "-ac", "2", "-ar", str(SR), "-c:a", "pcm_f32le", str(wav)],
                           capture_output=True, text=True)
        if r.returncode or not wav.exists():
            return {"clip": str(clip), "error": "no audio track" if "does not contain any stream" in r.stderr or not r.stderr.strip() else r.stderr.strip()[-300:]}
        mix, sr = sf.read(str(wav), dtype="float32", always_2d=True)
        mix = mix.T
        if mix.shape[-1] < sr // 2 or level(mix) < -60:
            return {"clip": str(clip), "music_db": None, "music_peak_db": None, "has_music": False, "note": "silent or too short"}
        mus = music_of(mix, a.hq)
        rep = {"clip": str(clip), "seconds": round(mix.shape[-1] / sr, 2), "mix_db": round(level(mix), 1),
               "music_db": round(level(mus) - level(mix), 1), "music_peak_db": round(peak_rel(mus, mix, sr // 2), 1)}
        rep["has_music"] = rep["music_db"] >= a.threshold or rep["music_peak_db"] >= a.threshold + 6
        if a.check:
            return rep
        out_dir = Path(a.out_dir) if a.out_dir else clip.parent
        out_dir.mkdir(parents=True, exist_ok=True)
        rest = mix - mus
        peak = float(np.max(np.abs(rest))) or 1.0
        if peak > 0.999:
            rest = rest * (0.999 / peak)      # never clip; the subtraction only lowers the level in practice
        mwav = out_dir / f"{clip.stem}.music.wav"
        sf.write(str(mwav), mus.T, sr)
        rwav = Path(td) / "rest.wav"
        sf.write(str(rwav), rest.T, sr, subtype="FLOAT")
        if video:
            out = out_dir / f"{clip.stem}.nomusic.mp4"
            r = subprocess.run([ff, "-v", "error", "-y", "-i", str(clip), "-i", str(rwav), "-map", "0:v:0", "-map", "1:a:0",
                                "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(out)],
                               capture_output=True, text=True)
            if r.returncode:
                return {**rep, "error": r.stderr.strip()[-300:]}
        else:
            out = out_dir / f"{clip.stem}.nomusic.wav"
            sf.write(str(out), rest.T, sr)
        rep.update(out=str(out), music_file=str(mwav), left_db=round(level(rest), 1))
        return rep


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("clips", nargs="+")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--out-dir")
    ap.add_argument("--threshold", type=float, default=-20.0)
    ap.add_argument("--hq", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    need()
    ff = ffmpeg()
    reps = [run(c, a, ff) for c in a.clips]
    if a.json:
        print(json.dumps(reps, indent=1))
    else:
        for r in reps:
            if r.get("error"):
                print(f"ERROR  {r['clip']}  — {r['error']}")
            elif r.get("music_db") is None:
                print(f"OK     {r['clip']}  — {r.get('note')}")
            else:
                tag = "MUSIC" if r["has_music"] else "CLEAN"
                print(f"{tag:6} {r['clip']}  — music {r['music_db']} dB against the whole mix, {r['music_peak_db']} dB at its loudest"
                      + (f"  → {r['out']}" if r.get("out") else ""))
    sys.exit(1 if a.check and any(r.get("has_music") for r in reps) else 0)


if __name__ == "__main__":
    main()
