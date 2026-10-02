"""Body edit v1 for the user's check (user 2026-10-02: "all confirmed" — every scene clip and the hook edits confirmed).
The body runs SC02 → SC13. It uses every confirmed take whole, in story order, with no trimming (§24L). Each scene's clip
dialogue is isolated and gated exactly as the hook edits v3 do (the user's sound fix: no Seedance bed survives). The locked
narration (VO-T1 v2 lines, `edit/body/vo/L0xx.mp4`) is laid on the take that covers its act-map row: 0.3 s into that row's
shot, never before the previous line has ended, and never under a spoken clip line. If a line can't fit, the next take is
pushed later and the gap holds the last frame. A collision is reported, never mixed. The film LUT is applied, and loudness is
-14 LUFS. No music yet: the Music Register Map (§40A) and MUS-BODY come in the next pass."""
import json, re, subprocess, sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_hook_edits as H

B = H.B
OUT = B / "edit" / "body"
H.OUT = OUT
FF = H.FF
VERSION = 3
NOMUSIC = OUT / "nomusic"  # unmusic.py (§24M, V7.92.0): each clip with only its music taken out — voice and effects kept
VO_DIR = OUT / "vo"
VO_IN, VO_GAP, CLEAR = 0.3, 0.3, 0.15
OFF = {"L034": 10.0}  # SC04-T2 marks its beats by time, not SHOT n: L034 sits on the silent beat [10s-14s]
# the confirmed version of every take, in story order (board, 2026-10-02)
ORDER = [("SC02", [("SC02-SH01", 3), ("SC02-SH02", 1), ("SC02-SH03", 5), ("SC02-SH04", 2), ("SC02-SH05", 4), ("SC02-SH06", 3), ("SC02-SH07", 1)]),
         ("SC03", [("SC03-SH01", 1), ("SC03-SH02", 2), ("SC03-SH03", 1), ("SC03-SH04", 3), ("SC03-SH05", 1), ("SC03-SH06", 2), ("SC03-SH07-08", 1), ("SC03-SH09-10", 1)]),
         ("SC04", [("SC04-T1", 1), ("SC04-T2", 1)]),
         ("SC05", [("SC05-T1", 4), ("SC0506-T1", 1)]),
         ("SC07", [("SC07-T", 2)]),
         ("SC08", [("SC08-T1", 2), ("SC08-T2", 1), ("SC08-T3", 4)]),
         ("SC09", [("SC09-T1", 6), ("SC09-T2", 1), ("SC09-T3", 1)]),
         ("SC10", [("SC10-T1", 1), ("SC10-T2", 1), ("SC10-T3", 2), ("SC10-T4", 4), ("SC10-T5", 2)]),
         ("SC11", [("SC11-T1", 1)]),
         ("SC12", [("SC12-T1", 2), ("SC12-T2", 1), ("SC12-T3", 1)]),
         ("SC13", [("SC13-T1", 1), ("SC13-T2", 5)])]


def clip(beat, v):
    return next(B.glob(f"body/*/{beat}_v{v}.mp4"))


def call(beat):
    return json.loads(next(B.glob(f"body/*/{beat}.call.json")).read_text())


def act_rows():
    rows = []
    for l in (B / "STEP4_5.md").read_text().splitlines():
        m = re.match(r"\| (SC\d\d-SH\d\d) \| SC\d\d \| ([^|]*) \|", l)
        if m:
            rows.append((m.group(1), re.findall(r"L\d{3}", m.group(2))))
    return rows


def shot_starts(c):
    """Shot n's start in the take, from the prompt's 'SHOT n, [a s-b s]' — one shot = 0."""
    st = {int(n): float(a) for n, a in re.findall(r"SHOT (\d+), \[(\d+(?:\.\d+)?)s", c["prompt"])}
    return st or {1: 0.0}


def plan():
    vo_lines = sorted(p.stem for p in VO_DIR.glob("L0*.mp4"))
    takes, t = [], 0.0
    for scene, beats in ORDER:
        for beat, v in beats:
            p = clip(beat, v); d, has_a = H.info(p); c = call(beat)
            m = re.fullmatch(r"(SC\d\d)-SH(\d\d)-(\d\d)", beat)  # a one-take of two rows (SC03-SH07-08)
            covers = c.get("covers") or ([f"{m[1]}-SH{m[2]}", f"{m[1]}-SH{m[3]}"] if m else [beat])
            takes.append({"scene": scene, "beat": beat, "v": v, "path": p, "dur": d, "audio": has_a, "covers": covers,
                          "starts": shot_starts(c), "dialogue": bool(c.get("dialogue"))})
    row_take = {}
    for k in takes:
        for i, r in enumerate(k["covers"]):
            row_take[r] = (k, k["starts"].get(i + 1, 0.0))
    place, last = [], None
    for row, lines in act_rows():
        for L in lines:
            if L not in vo_lines or any(x["line"] == L for x in place):
                continue
            k, off = row_take.get(row, (None, None))
            if k is None:  # the row's own shot was merged into a take (L51) — follow the line before it
                k, off = last["take"], None
            off = OFF.get(L, off)
            place.append({"line": L, "take": k, "off": off, "dur": H.info(VO_DIR / f"{L}.mp4")[0]})
            last = place[-1]
    return takes, place


def speech_spans(wav, sr=44100):
    pcm = subprocess.run([FF, "-loglevel", "error", "-i", str(wav), "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"], capture_output=True).stdout
    a = np.abs(np.frombuffer(pcm, np.int16).astype(np.float32)) > 30
    idx = np.flatnonzero(np.diff(np.concatenate(([0], a.astype(np.int8), [0]))))
    spans = [(s / sr, e / sr) for s, e in zip(idx[::2], idx[1::2])]
    merged = []
    for s, e in spans:
        if merged and s - merged[-1][1] < 0.3:
            merged[-1] = (merged[-1][0], e)
        else:
            merged.append((s, e))
    return [(s, e) for s, e in merged if e - s > 0.15]


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    takes, place = plan()
    # dialogue per scene (isolate + gate, the hook-edit v3 sound), then its spoken spans in take time
    for scene, _ in ORDER:
        ks = [k for k in takes if k["scene"] == scene]
        if not any(k["dialogue"] for k in ks):
            for k in ks:
                k["spans"] = []
            continue
        parts = [(i, k["dur"], k["audio"]) for i, k in enumerate(ks)]
        wav = H.dialogue_track(f"body_{scene}", parts, [k["path"] for k in ks])
        t0 = 0.0
        sp = speech_spans(wav)
        for k in ks:
            k["wav"], k["wav_at"] = wav, t0
            k["spans"] = [(s - t0, e - t0) for s, e in sp if t0 <= (s + e) / 2 < t0 + k["dur"]]
            t0 += k["dur"]
    # timeline: each take starts after the one before, held longer only when a VO line needs the room
    t, prev_end, report = 0.0, 0.0, []
    by_take = {}
    for x in place:
        by_take.setdefault(id(x["take"]), []).append(x)
    for i, k in enumerate(takes):
        k["at"] = t
        for x in by_take.get(id(k), []):
            want = t + (x["off"] if x["off"] is not None else 0.0) + VO_IN
            s = max(want, prev_end + VO_GAP)
            # never under a spoken clip line: slide past any span it would cross
            moved = True
            while moved:
                moved = False
                for a, b in k["spans"]:
                    if s < t + b + CLEAR and s + x["dur"] > t + a - CLEAR:
                        s = t + b + CLEAR; moved = True
            x["at"] = s; prev_end = s + x["dur"]
            report.append(f'{x["line"]} on {k["beat"]} at {s:6.2f}s ({x["dur"]:.2f}s)' + (f'  slid {s - want:+.2f}s' if s - want > 0.05 else ""))
        # hold this take's last frame only when the narration still running would reach the next take's first spoken
        # line or its own narration line; otherwise the narration runs on over the next shots (a montage line)
        hold = 0.0
        if i + 1 < len(takes):
            nk = takes[i + 1]
            ev = [a for a, _ in nk["spans"]] + [(x["off"] or 0.0) + VO_IN for x in by_take.get(id(nk), [])]
            if ev:
                hold = prev_end + VO_GAP - (t + k["dur"] + min(ev))
        k["hold"] = round(max(0.0, hold), 3)
        t += k["dur"] + k["hold"]
    total = t
    # render
    args, fc, n = [], [], len(takes)
    for i, k in enumerate(takes):
        args += ["-i", str(k["path"])]
        pad = f",tpad=stop_mode=clone:stop_duration={k['hold']:.3f}" if k["hold"] > 0 else ""
        fc.append(f"[{i}:v]scale=720:1280:force_original_aspect_ratio=decrease,pad=720:1280:(ow-iw)/2:(oh-ih)/2,fps=24,setsar=1,format=yuv420p{pad}[v{i}]")
    fc.append("".join(f"[v{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0[vc]")
    fc.append(f"[vc]lut3d=file='{H.LUT}'[vg]")
    mix, j = [], n
    for k in takes:  # v3 (user 2026-10-02: "use the new unmusic to remove only the music"): each take's own sound, music out
        if not k["audio"]:
            continue
        src = NOMUSIC / f"{k['path'].stem}.nomusic.mp4"
        if not src.exists():
            sys.exit(f"no unmusic output for {k['path'].name} — run unmusic.py on it first")
        args += ["-i", str(src)]
        ms = int(k["at"] * 1000)
        fc.append(f"[{j}:a]atrim=0:{k['dur']:.3f},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,adelay={ms}|{ms}[d{j}]")
        mix.append(f"[d{j}]"); j += 1
    for x in place:
        args += ["-i", str(VO_DIR / f"{x['line']}.mp4")]
        ms = int(x["at"] * 1000)
        fc.append(f"[{j}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={ms}|{ms}[n{j}]")
        mix.append(f"[n{j}]"); j += 1
    fc.append(f"anullsrc=r=48000:cl=stereo,atrim=0:{total:.3f}[sil]")
    fc.append("[sil]" + "".join(mix) + f"amix=inputs={len(mix) + 1}:duration=first:normalize=0,loudnorm=I=-14:TP=-1:LRA=11[am]")
    out = OUT / f"BODY_edit_v{VERSION}.mp4"
    subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error", *args, "-filter_complex", ";".join(fc), "-map", "[vg]", "-map", "[am]",
                    "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-movflags", "+faststart", str(out)], check=True)
    sheet = [f"# Body edit v{VERSION} — {total:.1f}s", "", "| Take | v | At | Length | Hold |", "|---|---|---|---|---|"]
    sheet += [f"| {k['beat']} | v{k['v']} | {k['at']:.2f}s | {k['dur']:.2f}s | {k['hold']:.2f}s |" for k in takes]
    sheet += ["", "## Narration", ""] + [f"- {r}" for r in report]
    (OUT / f"BODY_edit_v{VERSION}.md").write_text("\n".join(sheet) + "\n")
    print("\n".join(report)); print(out, f"{H.info(out)[0]:.2f}s", "holds:", {k["beat"]: k["hold"] for k in takes if k["hold"]})


if __name__ == "__main__":
    if sys.argv[1:] == ["--plan"]:
        takes, place = plan()
        for x in place:
            print(x["line"], x["take"]["beat"], x["off"], f"{x['dur']:.2f}")
    else:
        build()
