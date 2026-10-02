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


if __name__ == "__main__":
    if not BODY.exists():
        E.build()
    for h in (sys.argv[1:] or list(H.CONFIRMED)):
        final(h)
