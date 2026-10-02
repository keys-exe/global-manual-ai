"""Finished videos (user 2026-10-02: "give me the final out put"): one per hook — the hook, then the same body, on a cut.
Each hook is rebuilt from its five confirmed shots with the body's sound: each shot's own sound with only the music taken
out (`unmusic.py`, §24M V7.92.0), the locked narration (VO-T1 v2) 0.3 s into SH05, the film LUT, -14 LUFS — the same
cut, shots and narration timing as the confirmed hook edit v3. The body is BODY_edit_v3 (build_body_edit.py). No music
bed yet: the Music Register Map (§40A) and its MUS cues are the next pass."""
import shutil, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_body_edit as E
import build_hook_edits as H

B, FF = E.B, E.FF
FINAL = B / "edit" / "final"
VERSION = 1
BODY = E.OUT / f"BODY_edit_v{E.VERSION}.mp4"


def hook_segment(hook):
    # reuse the hook edit's isolated dialogue (same shots, same order), so no second isolator call
    src = B / "edit" / "hooks" / "work" / f"{hook}.dialogue.iso.mp3"
    dst = E.OUT / "work" / f"body_{hook}.dialogue.iso.mp3"
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.exists() and not dst.exists():
        shutil.copy(src, dst)
    order = [(hook, [(f"{hook}-SH0{i + 1}", v) for i, v in enumerate(H.CONFIRMED[hook])])]
    E.build(order, name=hook, fixed=[(B / "edit" / "vo" / H.VO[hook], f"{hook}-SH05", 0.0)], version=f"F{VERSION}")
    return E.OUT / f"{hook}_edit_vF{VERSION}.mp4"


def final(hook):
    seg = hook_segment(hook)
    FINAL.mkdir(parents=True, exist_ok=True)
    out = FINAL / f"HalfMyAge_FINAL-{hook}_v{VERSION}.mp4"
    subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error", "-i", str(seg), "-i", str(BODY), "-filter_complex",
                    "[0:v]setsar=1[v0];[1:v]setsar=1[v1];[0:a]aresample=48000[a0];[1:a]aresample=48000[a1];"
                    "[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]",
                    "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-c:a", "aac", "-b:a", "192k",
                    "-ar", "48000", "-movflags", "+faststart", str(out)], check=True)
    print(hook, "->", out.name, f"{H.info(out)[0]:.2f}s")
    return out




# ---- v2 (user 2026-10-02: "next the final ones with the vo and the music") -------------------------------------------
# The §40A music under the v1 finals: MUS-HK under the hook, MUS-BODY-A under the body up to the product's first frame
# (SC0506-T1, 120.82 s into the body), MUS-BODY-B from that frame — the change lands on it (V7.78.0). Each track at
# -26 LUFS (12 dB under the -14 LUFS voices), ducked a further 8 dB under speech (sidechain on the v1 mix), 0.5 s fades,
# then the whole mix back to -14 LUFS. The picture is stream-copied from v1, never re-encoded.
MUSIC = B / "edit" / "music"
PRODUCT_AT = 120.82


def music_final(hook, mv="v1"):
    import json as _j
    v1 = FINAL / f"HalfMyAge_FINAL-{hook}_v1.mp4"
    hook_len = H.info(E.OUT / f"{hook}_edit_vF{VERSION}.mp4")[0]
    body_len = H.info(BODY)[0]
    out = FINAL / f"HalfMyAge_FINAL-{hook}_v2.mp4"
    # (file, at, in-point, length): MUS-BODY-A v1 falls silent at 119.6 s — a held breath before the product, no padding;
    # MUS-BODY-B v1 opens on 1.5 s of silence — read from its first note (1.45 s) so the change lands on the product frame
    tracks = [(MUSIC / "MUS-HK_v1.mp3", 0.0, 0.0, hook_len),
              (MUSIC / "MUS-BODY-A_v1.mp3", hook_len, 0.0, min(PRODUCT_AT, 119.6)),
              (MUSIC / "MUS-BODY-B_v1.mp3", hook_len + PRODUCT_AT, 1.45, body_len - PRODUCT_AT)]
    args, fc, lab = ["-i", str(v1)], [], []
    for i, (p, at, inp, d) in enumerate(tracks, 1):
        args += ["-i", str(p)]
        ms = int(at * 1000)
        fi = "afade=t=in:d=0.5," if i != 3 else "afade=t=in:d=0.08,"  # the product cut lands hard (±0.25 s)
        fo = f"afade=t=out:st={max(0, d - 0.3):.3f}:d=0.3"
        fc.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,atrim={inp:.3f}:{inp + d:.3f},asetpts=PTS-STARTPTS,"
                  f"loudnorm=I=-26:TP=-6:LRA=11,{fi}{fo},adelay={ms}|{ms}[m{i}]")
        lab.append(f"[m{i}]")
    total = hook_len + body_len
    fc.append("".join(lab) + f"amix=inputs=3:duration=longest:normalize=0,apad,atrim=0:{total:.3f}[mus]")
    fc.append("[0:a]aresample=48000,aformat=channel_layouts=stereo,asplit=2[v][key]")
    fc.append("[mus][key]sidechaincompress=threshold=0.02:ratio=8:attack=40:release=400:makeup=1[duck]")
    fc.append("[v][duck]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1:LRA=11[am]")
    subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error", *args, "-filter_complex", ";".join(fc), "-map", "0:v", "-map", "[am]",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", str(out)], check=True)
    print(hook, "->", out.name, f"{H.info(out)[0]:.2f}s")
    return out


if __name__ == "__main__":
    music = "--music" in sys.argv
    hooks = [a for a in sys.argv[1:] if not a.startswith("--")] or list(H.CONFIRMED)
    if not BODY.exists():
        E.build()
    for h in hooks:
        music_final(h) if music else final(h)
