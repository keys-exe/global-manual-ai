"""Finished videos v3 (user 2026-10-02: "fixes everything… also add captions… a proper ending there and a fade").
Each = the hook (edit v4) + the body (edit v4, its slowed-not-frozen timing, the missing lines in, the ending fade), then:
- the §40A music: MUS-HK under the hook, MUS-BODY-A to the product's first frame (re-read from the v4 timing),
  MUS-BODY-B from that frame; −26 LUFS, ducked 8 dB under speech, the whole mix −14 LUFS, the music fading with the picture;
- captions in the reference's style (EG01): word by word, bold lowercase white, the spoken word yellow, 2–3 words on
  screen, centred at ~77% height, no box. The words are the script's own (spelling, numbers, "Stryde"); their timing comes
  from faster-whisper medium.en on the mix, aligned to the script.
"""
import difflib, json, re, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_hook_edits as H
import build_edit_v4 as V

B, FF = V.B, V.FF
OUT = V.OUT
FINAL = B / "edit" / "final"
MUSIC = B / "edit" / "music"
FONTS = B / "edit" / "fonts"
VERSION = 3
HOOK_LINES = {"HKA": ["L001", "L002", "L003", "L004"], "HKB": ["L005", "L006", "L007", "L008"],
              "HKC": ["L009", "L010", "L011", "L012", "L013"], "HKE": ["L014", "L015", "L016"]}
BODY_LINES = [f"L{n:03d}" for n in range(17, 75)]


def inventory():
    return {m[1]: (m[2].strip(), m[3].strip()) for m in re.finditer(r"^\| (L\d{3}) \| [^|]* \| ([^|]*) \| ([^|]*) \|",
                                                                      (B / "BUILD_SHEET.md").read_text(), re.M)}


def norm(w):
    w = w.lower().replace("’", "'")
    w = {"ten": "10", "eleven": "11", "sixty": "60"}.get(re.sub(r"[^a-z0-9']", "", w), w)
    return re.sub(r"[^a-z0-9']", "", w)


def words_of(media):
    from faster_whisper import WhisperModel
    m = WhisperModel("medium.en", device="cpu", compute_type="int8")
    segs, _ = m.transcribe(str(media), word_timestamps=True, language="en", vad_filter=False)
    return [(x.word.strip(), x.start, x.end) for s in segs for x in s.words]


def caption_words(media, line_ids, cache):
    """The script's words in order, each with a start and end time on this media."""
    inv = inventory()
    script = []
    for L in line_ids:
        spk, text = inv[L]
        text = text.replace("...", " ").replace("…", " ")
        for w in text.split():
            script.append({"w": w, "line": L, "spk": spk})
    if cache.exists():
        heard = json.loads(cache.read_text())
    else:
        heard = words_of(media); cache.write_text(json.dumps(heard))
    a, b = [norm(s["w"]) for s in script], [norm(h[0]) for h in heard]
    for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
        for i in range(blk.size):
            script[blk.a + i]["t0"], script[blk.a + i]["t1"] = heard[blk.b + i][1], heard[blk.b + i][2]
    # fill words the recogniser wrote differently, between their timed neighbours
    for i, s in enumerate(script):
        if "t0" in s:
            continue
        j = i
        while j < len(script) and "t0" not in script[j]:
            j += 1
        lo = script[i - 1]["t1"] if i > 0 and "t1" in script[i - 1] else 0.0
        hi = script[j]["t0"] if j < len(script) else lo + 0.4 * (j - i)
        n = j - i
        for k in range(n):
            script[i + k]["t0"] = lo + (hi - lo) * k / n
            script[i + k]["t1"] = lo + (hi - lo) * (k + 1) / n
    missing = sum(1 for s in script if s.get("t1", 0) - s.get("t0", 0) <= 0)
    return script, len(a), sum(blk.size for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks())


def ass_time(t):
    t = max(0.0, t)
    return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"


def write_ass(words, path, end_at):
    head = ("[Script Info]\nScriptType: v4.00+\nPlayResX: 720\nPlayResY: 1280\nWrapStyle: 2\nScaledBorderAndShadow: yes\n\n"
            "[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, "
            "Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n"
            "Style: Cap,Montserrat Thin ExtraBold,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,4,1.5,2,40,40,268,1\n\n"
            "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")
    # chunks of up to 3 words: break at a sentence end, a change of speaker, or a pause over 0.5 s
    chunks, cur = [], []
    for i, w in enumerate(words):
        if cur and (len(cur) == 3 or w["spk"] != cur[-1]["spk"] or w["t0"] - cur[-1]["t1"] > 0.5
                    or re.search(r"[.?!…]$", cur[-1]["w"])):
            chunks.append(cur); cur = []
        cur.append(w)
    if cur:
        chunks.append(cur)
    ev = []
    for ci, c in enumerate(chunks):
        nxt = chunks[ci + 1][0]["t0"] if ci + 1 < len(chunks) else end_at
        c_end = min(c[-1]["t1"] + 0.35, nxt)
        for j, w in enumerate(c):
            st = w["t0"]
            en = c[j + 1]["t0"] if j + 1 < len(c) else c_end
            if en - st < 0.04:
                continue
            txt = " ".join(("{\\c&H0000E6FF&}" if k == j else "{\\c&H00FFFFFF&}") + re.sub(r"[^\w'’-]", "", x["w"]).lower()
                           for k, x in enumerate(c))
            ev.append(f"Dialogue: 0,{ass_time(st)},{ass_time(en)},Cap,,0,0,0,,{txt}")
    path.write_text(head + "\n".join(ev) + "\n")
    return len(chunks)


def product_at(body_takes):
    return next(k["at"] for k in body_takes if k["beat"] == "SC0506-T1")


def final(h):
    hook, body = OUT / f"{h}_v4.mp4", OUT / "BODY_v4.mp4"
    takes = json.loads((OUT / "BODY_v4.takes.json").read_text())
    hook_len, body_len, pa = H.info(hook)[0], H.info(body)[0], product_at(takes)
    joined = OUT / f"{h}+BODY_v4.nomusic.mp4"
    subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error", "-i", str(hook), "-i", str(body), "-filter_complex",
                    "[0:v]setsar=1[v0];[1:v]setsar=1[v1];[0:a]aresample=48000[a0];[1:a]aresample=48000[a1];[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]",
                    "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-c:a", "aac", "-b:a", "256k", str(joined)], check=True)
    a_len = min(pa, 119.6)
    tracks = [(MUSIC / "MUS-HK_v1.mp3", 0.0, 0.0, hook_len, 0.5, 0.5),
              (MUSIC / "MUS-BODY-A_v1.mp3", hook_len, 0.0, a_len, 0.5, 0.3),
              (MUSIC / "MUS-BODY-B_v1.mp3", hook_len + pa, 1.45, body_len - pa, 0.08, V.END_FADE)]
    args, fc, lab = ["-i", str(joined)], [], []
    for i, (p, at, inp, d, fi, fo) in enumerate(tracks, 1):
        args += ["-i", str(p)]
        ms = int(at * 1000)
        fc.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,atrim={inp:.3f}:{inp + d:.3f},asetpts=PTS-STARTPTS,"
                  f"loudnorm=I=-26:TP=-6:LRA=11,afade=t=in:d={fi},afade=t=out:st={max(0, d - fo):.3f}:d={fo},adelay={ms}|{ms}[m{i}]")
        lab.append(f"[m{i}]")
    total = hook_len + body_len
    fc.append("".join(lab) + f"amix=inputs=3:duration=longest:normalize=0,apad,atrim=0:{total:.3f}[mus]")
    fc.append("[0:a]aresample=48000,aformat=channel_layouts=stereo,asplit=2[v][key]")
    fc.append("[mus][key]sidechaincompress=threshold=0.02:ratio=8:attack=40:release=400:makeup=1[duck]")
    fc.append(f"[v][duck]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1:LRA=11,afade=t=out:st={total - V.END_FADE:.3f}:d={V.END_FADE}[am]")
    # captions from the hook and the body, each aligned on its own speech-only track
    hw, hn, hm = caption_words(hook, HOOK_LINES[h], OUT / f"{h}_v4.words.json")
    bw, bn, bm = caption_words(body, BODY_LINES, OUT / "BODY_v4.words.json")
    for w in bw:
        w["t0"] += hook_len; w["t1"] += hook_len
    ass = OUT / f"{h}_captions.ass"
    n = write_ass(hw + bw, ass, total)
    fc.append(f"[0:v]subtitles=filename='{ass}':fontsdir='{FONTS}'[vc]")
    out = FINAL / f"HalfMyAge_FINAL-{h}_v{VERSION}.mp4"
    subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error", *args, "-filter_complex", ";".join(fc), "-map", "[vc]", "-map", "[am]",
                    "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-movflags", "+faststart", str(out)], check=True)
    print(h, "->", out.name, f"{H.info(out)[0]:.2f}s", f"product at body {pa:.2f}s", f"captions {n} groups",
          f"script words matched: hook {hm}/{hn}, body {bm}/{bn}")
    return out


if __name__ == "__main__":
    for h in (sys.argv[1:] or ["HKA", "HKB", "HKC", "HKE"]):
        final(h)
