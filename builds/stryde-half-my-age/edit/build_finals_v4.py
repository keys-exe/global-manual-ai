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
VERSION = 4
EV = V.EDIT_V
LEAD = 0.06       # a caption lands this much ahead of its word's first sound
THR = -36.0       # dBFS: speech on the voice-only track
HOOK_LINES = {"HKA": ["L001", "L002", "L003", "L004"], "HKB": ["L005", "L006", "L007", "L008"],
              "HKC": ["L009", "L010", "L011", "L012", "L013"], "HKE": ["L014", "L015", "L016"]}
BODY_LINES = [f"L{n:03d}" for n in range(17, 75)]
BODY_LINES[BODY_LINES.index("L038")], BODY_LINES[BODY_LINES.index("L039")] = "L039", "L038"  # the cut's one swap (FOLLOW_ON)


def inventory():
    return {m[1]: (m[2].strip(), m[3].strip()) for m in re.finditer(r"^\| (L\d{3}) \| [^|]* \| ([^|]*) \| ([^|]*) \|",
                                                                      (B / "BUILD_SHEET.md").read_text(), re.M)}


def norm(w):
    w = w.lower().replace("’", "'")
    w = {"ten": "10", "eleven": "11", "sixty": "60"}.get(re.sub(r"[^a-z0-9']", "", w), w)
    return re.sub(r"[^a-z0-9']", "", w)


def words_of(media, a=None, b=None):
    """faster-whisper medium.en word times on media (or its [a, b] part, times from a)."""
    from faster_whisper import WhisperModel
    global _M
    if "_M" not in globals():
        _M = WhisperModel("medium.en", device="cpu", compute_type="int8")
    src = media
    if a is not None:
        src = OUT / "cap_tmp.wav"
        subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error", "-i", str(media), "-ss", f"{a:.3f}", "-to", f"{b:.3f}",
                        "-ac", "1", "-ar", "16000", str(src)], check=True)
    segs, _ = _M.transcribe(str(src), word_timestamps=True, language="en", vad_filter=False,
                            hotwords="Sunday Stryde Barbara Barbara's cortisone Physiotherapy kneecap")
    return [(x.word.strip(), x.start, x.end) for s in segs for x in s.words]


def envelope(media, a=None, b=None):
    """The level in dBFS every 10 ms (of media, or its [a, b] part)."""
    import numpy as np
    cut = ["-ss", f"{a:.3f}", "-to", f"{b:.3f}"] if a is not None else []
    raw = subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-i", str(media), *cut, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    n = len(x) // 160
    r = np.sqrt((x[:n * 160].reshape(n, 160) ** 2).mean(1) + 1e-12)
    return 20 * np.log10(r)


def snap(env, t0, t1, thr=None):
    """A word's start moved to its first sound: back through sound that runs straight into it (≤ 0.35 s), or forward
    to the first sound when the recogniser put it early (≤ 0.3 s)."""
    THR_ = THR if thr is None else thr
    i = int(t0 * 100)
    if 0 <= i < len(env) and env[i] > THR_:
        j = i
        while j > 0 and i - j < 35 and env[j - 1] > THR_:
            j -= 1
        return j / 100 if (j == 0 or env[j - 1] <= THR_) and i - j < 35 else t0   # connected speech: keep its own start
    j = i
    while j < len(env) - 1 and j / 100 < t1 and env[j] <= THR_:
        j += 1
    return j / 100 if j / 100 < t1 else t0


def sound_end(env, t1, limit):
    """Where the sound after a word dies (0.15 s under the line), never past limit."""
    i = max(0, int(t1 * 100) - 5)
    quiet = 0
    while i < len(env) and i / 100 < limit:
        quiet = quiet + 1 if env[i] <= THR else 0
        if quiet >= 15:
            return (i - 14) / 100 + 0.08
        i += 1
    return limit


def align(script, heard, offset=0.0):
    a, b = [norm(s["w"]) for s in script], [norm(h[0]) for h in heard]
    n = 0
    for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
        for i in range(blk.size):
            script[blk.a + i]["t0"], script[blk.a + i]["t1"] = heard[blk.b + i][1] + offset, heard[blk.b + i][2] + offset
            script[blk.a + i]["src"] = "file" if offset else "mix"
        n += blk.size
    return n


def caption_words(media, line_ids, cache, items=()):
    """The script's words in order, each with its start and end on this media. Narration and off-screen lines are
    timed on their own clean file where the edit placed it (items); on-screen lines on the voice-only mix. Every start
    is snapped to its first sound; a word the recogniser missed sits in the sound just before the next word, never
    across a silence."""
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
    total = len(script)
    matched = align(script, heard)
    # narration / off-screen lines: their own file, placed where the edit put it
    fc = cache.with_name(cache.stem + ".files.json")
    fcache = json.loads(fc.read_text()) if fc.exists() else {}
    vo_lines = [L for L in line_ids if inv[L][0] == "VO"]
    by_line = {}
    for it in items:
        L = it["line"].split("#")[0]
        if L not in line_ids and vo_lines:   # a hook's narration file is named by its take (L004_v2): it speaks the hook's VO line
            L = vo_lines[-1]
        by_line.setdefault(L, []).append(it)
    for L, its in by_line.items():
        sw = [s for s in script if s["line"] == L]
        if not sw:
            continue
        heard_l = []
        for it in sorted(its, key=lambda x: x["at"]):
            k = f"{it['file']}|{it['a']}|{it['b']}"
            if k not in fcache:
                fcache[k] = words_of(Path(it["file"]), it["a"], it["b"])
            fenv = envelope(Path(it["file"]), it["a"], it["b"])
            thr = float(fenv.max()) - 32
            prev = -1.0
            for w, t0, t1 in fcache[k]:
                if t0 < it["b"] - it["a"]:
                    t = max(snap(fenv, t0, t1, thr), prev + 0.08) if t0 - prev > 0.08 else t0   # snapped on its own clean file
                    heard_l.append((w, it["at"] + t, it["at"] + t1)); prev = t
        for x in sw:
            x.pop("t0", None); x.pop("t1", None)
        align(sw, heard_l)
        for x in sw:
            if "t0" in x:
                x["src"] = "file"
    fc.write_text(json.dumps(fcache))
    env = envelope(media)
    # on-screen lines: timed on the scenes' isolated voice tracks (build_edit_v4.dialogue_words), mapped to this cut
    dlf = cache.with_name(cache.name.replace(".words.json", ".dlg.json"))
    if dlf.exists():
        onscreen = [x for x in script if x.get("src") != "file"]
        dl = json.loads(dlf.read_text())
        old = {id(x): (x.get("t0"), x.get("t1"), x.get("src")) for x in onscreen}
        for x in onscreen:
            x.pop("t0", None); x.pop("t1", None); x.pop("src", None)
        align(onscreen, dl)
        for x in onscreen:
            if "t0" in x:
                x["src"] = "dlg"
            elif old[id(x)][2] == "mix" and old[id(x)][0] is not None and (old[id(x)][1] - old[id(x)][0]) < 0.8:   # the mix's time, only if it isn't smeared
                x["t0"], x["t1"], x["src"] = old[id(x)]
        # keep the order: a mix-timed word that lands out of order with its timed neighbours is dropped (refilled below)
        last = -1.0
        for x in script:
            if "t0" not in x:
                continue
            if x["t0"] < last - 0.02:
                for k in ("t0", "t1", "src"):
                    x.pop(k, None)
                continue
            last = x["t0"]
    # what is left on the mix: the recogniser chains each word onto the one before, so a word's start sits in the silence before
    # it — moved to the start of the speech it belongs to (the edit's speech spans, in output time); its end to that
    # speech's end when the silence after it is longer
    spf = cache.with_name(cache.name.replace(".words.json", ".spans.json"))
    spans = json.loads(spf.read_text()) if spf.exists() else []
    for x in script:
        if x.get("src") != "mix":
            continue
        inside = [sp for sp in spans if sp[0] - 0.05 <= x["t0"] <= sp[1]]
        if not inside:
            later = [sp for sp in spans if x["t0"] < sp[0] < x["t1"] + 0.3]
            if later:
                x["t0"] = later[0][0]
                x["t1"] = max(x["t1"], x["t0"] + 0.15)
                inside = [later[0]]
        if inside and x["t1"] > inside[0][1] + 0.25 and not any(inside[0][1] < sp[0] < x["t1"] for sp in spans):
            x["t1"] = inside[0][1]
    # words the recogniser missed: in the sound just before the next timed word
    i = 0
    while i < len(script):
        if "t0" in script[i]:
            i += 1; continue
        j = i
        while j < len(script) and "t0" not in script[j]:
            j += 1
        n = j - i
        lo = script[i - 1]["t1"] if i > 0 else 0.0
        hi = script[j]["t0"] if j < len(script) else lo + 0.35 * n
        if hi - lo > 0.35 * n + 0.2:   # a silence between: they are spoken right before the next word
            k = int(hi * 100) - 1
            while k > lo * 100 and env[k] <= THR and hi * 100 - k < 40:
                k -= 1
            while k > lo * 100 and env[k - 1] > THR:
                k -= 1
            lo = max(lo, min(k / 100, hi - 0.3 * n))
        for m in range(n):
            script[i + m]["t0"] = lo + (hi - lo) * m / n
            script[i + m]["t1"] = lo + (hi - lo) * (m + 1) / n
        i = j
    for s in script:
        s["env"] = env
    return script, total, matched


def ass_time(t):
    t = max(0.0, t)
    return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"


def write_ass(words, path, end_at):
    head = ("[Script Info]\nScriptType: v4.00+\nPlayResX: 720\nPlayResY: 1280\nWrapStyle: 2\nScaledBorderAndShadow: yes\n\n"
            "[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, "
            "Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n"
            "Style: Cap,Montserrat Thin ExtraBold,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,4,1.5,2,40,40,268,1\n\n"
            "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")
    # words that start together (two words given one start) share the time up to the next start, so each one lights
    i = 0
    while i < len(words):
        j = i + 1
        while j < len(words) and words[j]["t0"] - words[i]["t0"] < 0.08 * (j - i):
            j += 1
        if j - i > 1:
            end = words[j]["t0"] if j < len(words) and words[j]["t0"] - words[i]["t0"] < 2.0 else words[j - 1]["t1"]
            end = max(end, words[i]["t0"] + 0.18 * (j - i))
            for m in range(i, j):
                words[m]["t0"] = words[i]["t0"] + (end - words[i]["t0"]) * (m - i) / (j - i)
        i = j
    # chunks of up to 3 words: break at a sentence end, a change of speaker, or a pause over 0.5 s
    chunks, cur = [], []
    for i, w in enumerate(words):
        if cur and (len(cur) == 3 or w["spk"] != cur[-1]["spk"] or w["t0"] - cur[-1]["t1"] > 0.35
                    or re.search(r"[.?!…]$", cur[-1]["w"])):
            chunks.append(cur); cur = []
        cur.append(w)
    if cur:
        chunks.append(cur)
    ev = []
    for ci, c in enumerate(chunks):
        nxt = chunks[ci + 1][0]["t0"] if ci + 1 < len(chunks) else end_at
        c_end = min(sound_end(c[-1]["env"], c[-1]["t1"], c[-1]["t1"] + 0.3), nxt - LEAD)
        for j, w in enumerate(c):
            st = max(0.0, w["t0"] - LEAD)
            en = c[j + 1]["t0"] - LEAD if j + 1 < len(c) else c_end
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
    hook, body = OUT / f"{h}_v{EV}.mp4", OUT / f"BODY_v{EV}.mp4"
    takes = json.loads((OUT / f"BODY_v{EV}.takes.json").read_text())
    hook_len, body_len, pa = H.info(hook)[0], H.info(body)[0], product_at(takes)
    joined = OUT / f"{h}+BODY_v{EV}.nomusic.mp4"
    subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error", "-i", str(hook), "-i", str(body), "-filter_complex",
                    "[0:v]setsar=1[v0];[1:v]setsar=1[v1];[0:a]aresample=48000[a0];[1:a]aresample=48000[a1];[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]",
                    "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-c:a", "aac", "-b:a", "256k", str(joined)], check=True)
    a_len = min(pa, 125.4)  # MUS-BODY-A v3 (re-timed to v4) falls silent at 125.4 s, a short breath before the product
    tracks = [(MUSIC / "MUS-HK_v1.mp3", 0.0, 0.0, hook_len, 0.5, 0.5),
              (MUSIC / "MUS-BODY-A_v3.mp3", hook_len, 0.0, a_len, 0.5, 0.3),
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
    hi = json.loads((OUT / f"{h}_v{EV}.items.json").read_text())
    bi = json.loads((OUT / f"BODY_v{EV}.items.json").read_text())
    hw, hn, hm = caption_words(hook, HOOK_LINES[h], OUT / f"{h}_v{EV}.words.json", hi)
    bw, bn, bm = caption_words(body, BODY_LINES, OUT / f"BODY_v{EV}.words.json", bi)
    for w in bw:
        w["t0"] += hook_len; w["t1"] += hook_len
    ass = OUT / f"{h}_captions.ass"
    n = write_ass(hw + bw, ass, total)
    fc.append(f"[0:v]subtitles=filename='{ass}':fontsdir='{FONTS}',format=yuv420p[vc]")   # 4:2:0 so every phone plays it
    out = FINAL / f"HalfMyAge_FINAL-{h}_v{VERSION}.mp4"
    subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error", *args, "-filter_complex", ";".join(fc), "-map", "[vc]", "-map", "[am]",
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-profile:v", "high", "-crf", "17", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-movflags", "+faststart", str(out)], check=True)
    print(h, "->", out.name, f"{H.info(out)[0]:.2f}s", f"product at body {pa:.2f}s", f"captions {n} groups",
          f"script words matched: hook {hm}/{hn}, body {bm}/{bn}")
    return out


if __name__ == "__main__":
    for h in (sys.argv[1:] or ["HKA", "HKB", "HKC", "HKE"]):
        final(h)
