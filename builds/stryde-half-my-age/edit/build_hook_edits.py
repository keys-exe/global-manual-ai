"""Hook edits for the user's check (user 2026-10-01: "give me the hook edit first, I'll check them").
Each hook: its five confirmed Seedance shots, whole (§24L, no trimming), in order; the clip dialogue at 0 dB; the locked
narration (VO-T1 v2) laid on SH05 (L004 for Hooks A/B/C — the same line as L008/L013 — and L016 for Hook E); the film LUT
(LUT-HALFMYAGE.cube); loudness -14 LUFS. No music yet: MUS-HK is composed after the Music Register Map (§40A) — the next pass.
v2 (user 2026-10-01: "I don't like the edit, it feels fast and also the BGM" → chose "keep the clips, fix sound only"): Seedance
put a constant background bed under every dialogue clip despite NEG-SOUND. Each hook's dialogue track is now run through the
ElevenLabs Voice Isolator as one piece (the isolator needs ≥ 4.6 s), then gated: only the spoken words are kept (120 ms before,
250 ms after, 40 ms fades — the §22U/E11 padding), everything between them is silence, so no bed survives."""
import os, re, subprocess, sys
import numpy as np, requests
from pathlib import Path
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
B = Path(__file__).resolve().parent.parent
OUT = B / "edit" / "hooks"
LUT = B / "edit" / "LUT-HALFMYAGE.cube"
CONFIRMED = {  # the version the user confirmed on the board
    "HKA": [1, 1, 1, 1, 1], "HKB": [1, 1, 2, 1, 3], "HKC": [3, 3, 2, 1, 3], "HKE": [3, 3, 3, 2, 3]}
VO = {"HKA": "L004_v2.m4a", "HKB": "L004_v2.m4a", "HKC": "L004_v2.m4a", "HKE": "L016_v2.m4a"}
VO_IN = 0.3  # the narration enters 0.3 s into SH05
VERSION = 2
PRE, POST, FADE = 0.12, 0.25, 0.04


def dialogue_track(hook, parts, shots):
    """The hook's clip audio as one track (silence on the silent shots), isolated and gated -> wav path."""
    work = OUT / "work"; work.mkdir(exist_ok=True)
    raw = work / f"{hook}.dialogue.raw.wav"; iso = work / f"{hook}.dialogue.iso.mp3"; out = work / f"{hook}.dialogue.v{VERSION}.wav"
    args, fc = [], []
    for (i, d, has_a), s in zip(parts, shots):
        args += ["-i", str(s)]
        fc.append(f"[{i}:a]aresample=44100,aformat=channel_layouts=mono,apad,atrim=0:{d:.3f}[a{i}]" if has_a
                  else f"anullsrc=r=44100:cl=mono,atrim=0:{d:.3f}[a{i}]")
    fc.append("".join(f"[a{i}]" for i, _, _ in parts) + f"concat=n={len(parts)}:v=0:a=1[ac]")
    subprocess.run([FF, "-y", "-loglevel", "error", *args, "-filter_complex", ";".join(fc), "-map", "[ac]", str(raw)], check=True)
    if not iso.exists():
        with open(raw, "rb") as f:
            r = requests.post("https://api.elevenlabs.io/v1/audio-isolation", headers={"xi-api-key": os.environ["ELEVENLABS_API_KEY"]},
                              files={"audio": (raw.name, f, "audio/wav")}, timeout=600)
        if r.status_code != 200:
            sys.exit(f"{hook} isolation: {r.status_code} {r.text[:300]}")
        iso.write_bytes(r.content)
    pcm = subprocess.run([FF, "-loglevel", "error", "-i", str(iso), "-ac", "1", "-ar", "44100", "-f", "s16le", "-"], capture_output=True).stdout
    a = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
    total = sum(d for _, d, _ in parts); n = int(total * 44100)
    a = np.pad(a, (0, max(0, n - len(a))))[:n]
    # gate on the spoken words themselves (faster-whisper word timestamps on the isolated track) — a level gate let the
    # louder parts of the Seedance bed through
    from faster_whisper import WhisperModel
    words = [w for seg in WhisperModel("small", device="cpu", compute_type="int8").transcribe(str(iso), word_timestamps=True, language="en")[0]
             for w in seg.words]
    def level(w):
        seg = a[int(w.start * 44100):max(int(w.end * 44100), int(w.start * 44100) + 441)]
        return 20 * np.log10(np.sqrt(np.mean(seg ** 2)) + 1e-9)
    # keep only words inside a shot that has a line (a silent shot never speaks) and with real energy under them
    import json as _json
    spans, t0 = [], 0.0
    for (i, d, _), sh in zip(parts, shots):
        call = _json.loads((sh.parent / (sh.stem.rsplit("_v", 1)[0] + ".call.json")).read_text())
        if call.get("dialogue"):
            spans.append((t0, t0 + d))
        t0 += d
    words = [w for w in words if level(w) > -40 and any(s0 <= (w.start + w.end) / 2 < e0 for s0, e0 in spans)]
    print(f"  {hook} kept:", " ".join(f"{w.word.strip()}@{w.start:.2f}" for w in words))
    wordgate = np.zeros(n, bool)
    for w in words:
        st = max(w.start, w.end - 0.8)  # Whisper stretches a word's start back over the silence before it
        wordgate[max(0, int((st - PRE) * 44100)):min(n, int((w.end + POST) * 44100))] = True
    # and only where the isolated track is actually speech-loud (the bed sits near -33 dB)
    hop = 441
    lv = np.array([20 * np.log10(np.sqrt(np.mean(a[j:j + hop] ** 2)) + 1e-9) for j in range(0, n, hop)])
    loud = np.repeat(lv > -30, hop)[:n]
    dil = np.zeros(n, bool)
    idx = np.flatnonzero(np.diff(np.concatenate(([0], loud.astype(np.int8), [0]))))
    for s0, e0 in zip(idx[::2], idx[1::2]):
        dil[max(0, s0 - int(PRE * 44100)):min(n, e0 + int(POST * 44100))] = True
    gain = (wordgate & dil).astype(np.float32)
    f = int(FADE * 44100)
    ramp = np.convolve(gain, np.ones(f) / f, mode="same")
    g = (a * np.minimum(ramp, 1.0) * 32767).astype(np.int16)
    subprocess.run([FF, "-y", "-loglevel", "error", "-f", "s16le", "-ar", "44100", "-ac", "1", "-i", "-", str(out)], input=g.tobytes(), check=True)
    kept = (gain > 0).mean() * total
    print(f"  {hook}: dialogue isolated + gated, {kept:.1f}s of speech kept of {total:.1f}s")
    return out


def info(p):
    s = subprocess.run([FF, "-hide_banner", "-i", str(p)], capture_output=True, text=True).stderr
    h, m, sec = re.search(r"Duration: (\d+):(\d+):([\d.]+)", s).groups()
    return int(h) * 3600 + int(m) * 60 + float(sec), "Audio:" in s


def build(hook):
    shots = [B / "hooks" / hook / f"{hook}-SH0{i + 1}_v{v}.mp4" for i, v in enumerate(CONFIRMED[hook])]
    args, parts, t, sh05_at = [], [], 0.0, 0.0
    for i, s in enumerate(shots):
        d, has_a = info(s)
        args += ["-i", str(s)]
        if i == 4:
            sh05_at = t
        parts.append((i, d, has_a))
        t += d
    n = len(shots)
    dlg = dialogue_track(hook, parts, shots)
    args += ["-i", str(B / "edit" / "vo" / VO[hook]), "-i", str(dlg)]
    fc = []
    for i, d, has_a in parts:
        fc.append(f"[{i}:v]scale=720:1280:force_original_aspect_ratio=decrease,pad=720:1280:(ow-iw)/2:(oh-ih)/2,fps=24,setsar=1,format=yuv420p[v{i}]")
    fc.append("".join(f"[v{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0[vc]")
    fc.append(f"[{n + 1}:a]aresample=48000,aformat=channel_layouts=stereo[ac]")
    fc.append(f"[vc]lut3d=file='{LUT}'[vg]")
    ms = int((sh05_at + VO_IN) * 1000)
    fc.append(f"[{n}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={ms}|{ms}[vo]")
    fc.append("[ac][vo]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1:LRA=11[am]")
    out = OUT / f"{hook}_edit_v{VERSION}.mp4"
    cmd = [FF, "-y", "-hide_banner", "-loglevel", "error", *args, "-filter_complex", ";".join(fc), "-map", "[vg]", "-map", "[am]",
           "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", str(out)]
    subprocess.run(cmd, check=True)
    d, _ = info(out)
    print(hook, f"{t:.2f}s of shots ->", out.name, f"{d:.2f}s", "VO at", f"{sh05_at + VO_IN:.2f}s")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for h in (sys.argv[1:] or CONFIRMED):
        build(h)
