"""Edit v4 (user 2026-10-02): "you should timed it… have a pause to the vo to match the video and vo", "if the vo is much
longer than the video then that end part you should slow it down so it doesnt freezes", the sister's phone line "did not
come", L037 / L039 / L045 / L061 "not on the right time", "fixes everything… add captions… a proper ending… a fade".

What changes from v3 (build_body_edit.py):
- Every narration line lands on the shot its act-map row names. A line that runs across several rows is cut at its own
  pauses into phrases, and each phrase starts on its row's shot (SPLIT): "Physiotherapy" on the physio couch,
  "painkillers" on the pills, and so on.
- A phrase never slides past the dialogue it should come before. When it needs more room than the speech-free stretch
  of picture gives, that stretch is slowed (motion-interpolated, the take's own sound with it). The words keep their
  order and the next spoken line waits for the narration.
- No freeze frame anywhere. When narration runs past a take into a take that opens on speech or its own narration, the
  end of the first take is slowed instead of held.
- Off-screen lines that were missing go in: L027, the sister on the phone (her voice master, phone band), and L009, the
  station announcement in Hook C (VOICE-X1, public-address band and a little room).
- The ending: the last shot slows to hold 1.2 s past the last word, then the picture and sound fade to black over 1.5 s.
Sound: each take's own sound with only the music taken out (unmusic.py); the music is added in build_finals_v4.py.
"""
import json, re, subprocess, sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_hook_edits as H
import build_body_edit as E

B, FF = E.B, E.FF
OUT = B / "edit" / "v4"
TK = OUT / "takes"
VO_DIR = E.VO_DIR
NOMUSIC = E.NOMUSIC
VO_IN, VO_GAP, CLEAR = 0.3, 0.3, 0.15
MIN_SPEED = 0.4            # slowest a stretch of picture may run (2.5x), with motion interpolation
END_HOLD, END_FADE = 1.2, 1.5
WORDS = json.loads((VO_DIR / "words.json").read_text())

# a narration line across several rows: the word each phrase starts on, and its row
SPLIT = {"L019": [("Six", "SC02-SH03"), ("one", "SC02-SH04")],
         "L023": [("The", "SC03-SH01"), ("By", "SC03-SH02"), ("Physiotherapy", "SC03-SH03"), ("painkillers", "SC03-SH04"),
                  ("cortisone", "SC03-SH05"), ("every", "SC03-SH06")],
         "L030": [("Then", "SC04-SH01"), ("she's", "SC04-SH02")],
         "L035": [("Barbara", "SC05-SH01"), ("She", "SC05-SH02")],
         "L051": [("Barbara's", "SC09-SH02"), ("Her", "SC09-SH03")],
         "L052": [("I've", "SC10-SH01"), ("No", "SC10-SH02")],
         "L068": [("So", "SC12-SH08"), ("It's", "SC12-SH09", 3)]}   # the third "It's": "It's been designed…"
OFF = {"L034": 10.0}       # SC04-T2 marks its beats by time: L034 on its silent beat [10s-14s]
# off-screen lines: (line, file, in, out, row, filter, offset in the row's shot or None = after the line before, vo_in)
OFFSCREEN = [("L027", B / "voice" / "C4_voice_master.m4a", 0.0, 5.41, "SC03-SH09", "phone", 0.0, 0.25)]
# L009 is cut at its own pause around the commuter's reaction: "…the escalator is out of service." — "You're joking." —
# "Please use the stairs." — "It's only stairs, love." (the announcement keeps running while he groans)
HOOK_OFFSCREEN = {"HKC": [("L009#1", B / "voice" / "X1_voice_master_raw.mp4", 0.50, 4.30, "HKC-SH01", "pa", 0.0, 0.05),
                          ("L009#2", B / "voice" / "X1_voice_master_raw.mp4", 4.40, 6.85, "HKC-SH01", "pa", None, 0.0)]}
FILTERS = {"phone": "highpass=f=320,lowpass=f=3300,acompressor=threshold=0.1:ratio=4,volume=1.6",
           "pa": "highpass=f=400,lowpass=f=3600,aecho=0.8:0.55:70|140:0.35|0.2,volume=1.4"}


def norm(w):
    return re.sub(r"[^a-z0-9']", "", w.lower().replace("’", "'"))


def pieces(L):
    """The phrases of a narration line: [(row or None, in, out)] in the VO file's time; one piece when it isn't split."""
    d = H.info(VO_DIR / f"{L}.mp4")[0]
    if L not in SPLIT:
        return [(None, 0.0, d)]
    w = WORDS[L]
    cuts = []
    for spec in SPLIT[L]:
        word, row = spec[0], spec[1]
        nth = spec[2] if len(spec) > 2 else 1
        hits = [i for i, x in enumerate(w) if norm(x[0]) == norm(word)]
        i = hits[nth - 1]
        t = 0.0 if i == 0 else (w[i - 1][2] + w[i][1]) / 2
        cuts.append((row, t))
    return [(row, a, (cuts[j + 1][1] if j + 1 < len(cuts) else d)) for j, (row, a) in enumerate(cuts)]


def takes_of(order):
    takes = []
    for scene, beats in order:
        for beat, v in beats:
            p = E.clip(beat, v); d, has_a = H.info(p); c = E.call(beat)
            m = re.fullmatch(r"(SC\d\d)-SH(\d\d)-(\d\d)", beat)
            covers = c.get("covers") or ([f"{m[1]}-SH{m[2]}", f"{m[1]}-SH{m[3]}"] if m else [beat])
            if re.fullmatch(r"HK.-SH0\d", beat):
                covers = [beat]
            takes.append({"scene": scene, "beat": beat, "v": v, "path": p, "dur": d, "audio": has_a, "covers": covers,
                          "starts": E.shot_starts(c), "dialogue": bool(c.get("dialogue")), "items": [], "st": []})
    return takes


def place_items(takes, fixed=None, offscreen=()):
    row_take = {}
    for k in takes:
        for i, r in enumerate(k["covers"]):
            row_take[r] = (k, k["starts"].get(i + 1, 0.0))
    items, last = [], None

    def add(line, f, a, b, row, flt=None, off=None, vo_in=VO_IN):
        nonlocal last
        k, o = row_take.get(row, (None, None)) if row else (None, None)
        if k is None:
            k, o = (last["take"], None) if last else (takes[0], 0.0)
        if off is not None:
            o = off if row is None else o + off
        after = False
        if o is None and last:  # a line that follows another: after any on-screen line spoken between them
            L0, L1 = last["line"].split("#")[0], line.split("#")[0]
            between = [x for x, _ in inv if L0 < x < L1]
            after = any(spk[x] not in ("VO",) for x in between)
        it = {"line": line, "file": f, "a": a, "b": b, "dur": b - a, "take": k, "off": o, "row": row, "flt": flt, "vo_in": vo_in,
              "after_span": after}
        k["items"].append(it); items.append(it); last = it

    if fixed is not None:
        for line, f, beat, off in fixed:
            k = next(x for x in takes if x["beat"] == beat)
            it = {"line": line, "file": Path(f), "a": 0.0, "b": H.info(f)[0], "dur": H.info(f)[0], "take": k, "off": off,
                  "row": beat, "flt": None, "vo_in": VO_IN}
            k["items"].append(it); items.append(it)
        for j, (line, f, a, b, row, flt, off, vi) in enumerate(offscreen):
            k = next(x for x in takes if x["beat"] == row)
            it = {"line": line, "file": Path(f), "a": a, "b": b, "dur": b - a, "take": k, "off": off,
                  "row": row, "flt": flt, "vo_in": vi, "after_span": off is None}
            k["items"].insert(j, it); items.append(it)
        return items
    vo = {p.stem for p in VO_DIR.glob("L0*.mp4")}
    inv = [(m[1], m[2].strip()) for m in re.finditer(r"^\| (L\d{3}) \| [^|]* \| ([^|]*) \|", (B / "BUILD_SHEET.md").read_text(), re.M)]
    spk = dict(inv)
    offs = {o[0]: o for o in offscreen}
    for row, lines in E.act_rows():
        for L in lines:
            if L in offs:
                _, f, a, b, r, flt, off, vi = offs[L]
                add(L, f, a, b, r, flt, off, vi)
            if L not in vo or any(x["line"].split("#")[0] == L for x in items):
                continue
            for j, (prow, a, b) in enumerate(pieces(L)):
                r = prow or row
                add(f"{L}#{j + 1}" if L in SPLIT else L, VO_DIR / f"{L}.mp4", a, b, r, off=OFF.get(L) if j == 0 else None)
                if prow and r not in row_take:
                    pass
    for k in takes:  # within a take, keep script order (the act map's) — the anchors are only start hints
        pass
    return items


class Warp:
    """Picture time in a take (tau) → output time from the take's start, with slowed stretches [(a, b, extra)]."""

    def __init__(self):
        self.st = []

    def add(self, a, b, extra):
        for s in self.st:
            if abs(s[0] - a) < 1e-6 and abs(s[1] - b) < 1e-6:
                s[2] += extra
                return
        self.st.append([a, b, extra]); self.st.sort()

    def out(self, t):
        o = t
        for a, b, x in self.st:
            if t >= b:
                o += x
            elif t > a:
                o += x * (t - a) / (b - a)
        return o

    def inv(self, o):
        lo, hi = 0.0, 1e4
        for _ in range(60):
            m = (lo + hi) / 2
            if self.out(m) < o:
                lo = m
            else:
                hi = m
        return lo


def stretch(w, k, lo, hi, need, report):
    lo, hi = max(0.0, lo), min(k["dur"], hi)
    if hi - lo < 0.3:
        lo = max(0.0, hi - 0.3)
    have = w.out(hi) - w.out(lo)
    cap = (hi - lo) / MIN_SPEED - have
    x = min(need, max(0.0, cap))
    w.add(lo, hi, x)
    if need - x > 0.05:
        report.append(f"WARN {k['beat']}: {need - x:.2f}s more than the slowest stretch allows ({lo:.2f}-{hi:.2f})")
    return x


def plan(takes, ending=True):
    t, prev_end, report = 0.0, -10.0, []
    for i, k in enumerate(takes):
        w = Warp(); k["warp"] = w; k["at"] = t
        sp = k.get("spans", [])
        for it in k["items"]:
            if it["off"] is not None:
                want = t + w.out(it["off"] + it["vo_in"])
            else:
                want = prev_end + VO_GAP
            s = max(want, prev_end + VO_GAP)
            if it.get("after_span"):  # after the spoken line(s) that come before it in the script
                ts0 = w.inv(max(0.0, prev_end - t))
                grp, last_b = None, None
                for a, b in sorted(sp):
                    if b <= ts0 - 0.05:
                        continue
                    if grp is None or a - last_b < 0.6:
                        grp, last_b = a if grp is None else grp, b
                    else:
                        break
                if last_b is not None:
                    s = max(s, t + w.out(last_b) + CLEAR)
            moved = True
            while moved:  # never starts on top of a spoken clip line: after it
                moved = False
                ts = w.inv(s - t)
                for a, b in sp:
                    if a - CLEAR < ts < b + CLEAR - 0.005:
                        s = t + w.out(b) + CLEAR + 0.01; moved = True
            ts = w.inv(s - t)
            e = s + it["dur"]
            nxt = [a for a, b in sp if a > ts]
            if nxt:
                na = min(nxt)
                gap_end = t + w.out(na)
                if e + CLEAR > gap_end:  # the next spoken line would start under it: slow the speech-free picture before it
                    prev_b = max([b for a, b in sp if b <= na] + [0.0])
                    lo = max(prev_b, min(ts, it["off"] if it["off"] is not None else ts))
                    stretch(w, k, lo, na - 0.05, e + CLEAR - gap_end, report)
            it["at"] = s; prev_end = e
            report.append(f"{it['line']:8} {k['beat']:13} at {s:7.2f}s ({it['dur']:.2f}s)" + (f"  +{s - want:.2f}s after its mark" if s - want > 0.05 else ""))
        end = t + w.out(k["dur"])
        if i + 1 < len(takes):
            nk = takes[i + 1]
            ev = [a for a, _ in nk.get("spans", [])] + [x["off"] + x["vo_in"] for x in nk["items"] if x["off"] is not None]
            if ev and prev_end + VO_GAP > end + min(ev):
                last_b = max([b for a, b in sp] + [0.0])
                lo = max(last_b, k["dur"] - 4.0, 0.0)
                stretch(w, k, lo, k["dur"], prev_end + VO_GAP - end - min(ev), report)
        elif ending:
            need = prev_end + END_HOLD + END_FADE - end
            if need > 0:
                last_b = max([b for a, b in sp] + [0.0])
                stretch(w, k, max(last_b, k["dur"] - 4.0), k["dur"], need, report)
        k["out_dur"] = w.out(k["dur"])
        t += k["out_dur"]
    return t, report


def render_take(k, name):
    """The take with its slowed stretches: picture motion-interpolated back to 24 fps, its own sound (music out) slowed
    with it, pitch kept. Cached by its stretch list."""
    TK.mkdir(parents=True, exist_ok=True)
    import hashlib
    key = "_".join(f"{a:.2f}-{b:.2f}-{x:.2f}" for a, b, x in k["warp"].st) or "plain"
    out = TK / f"{k['beat']}_v{k['v']}__{hashlib.md5(key.encode()).hexdigest()[:8]}.mp4"
    k["render"] = out
    if out.exists():
        return out
    cuts = [0.0]
    for a, b, x in k["warp"].st:
        cuts += [a, b]
    cuts = sorted(set([c for c in cuts if 0 <= c <= k["dur"]] + [k["dur"]]))
    segs = []
    for a, b in zip(cuts, cuts[1:]):
        if b - a < 0.01:
            continue
        x = sum(s[2] for s in k["warp"].st if abs(s[0] - a) < 1e-6 and abs(s[1] - b) < 1e-6)
        segs.append((a, b, (b - a) / (b - a + x)))
    src = NOMUSIC / f"{k['path'].stem}.nomusic.mp4"
    has_a = k["audio"] and src.exists()
    args = ["-i", str(k["path"])] + (["-i", str(src)] if has_a else [])
    fc, vl, al = [], "", ""
    for j, (a, b, sp) in enumerate(segs):
        v = (f"[0:v]trim={a:.4f}:{b:.4f},setpts=PTS-STARTPTS,scale=720:1280:force_original_aspect_ratio=decrease,"
             f"pad=720:1280:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=24")
        if sp < 0.999:
            v += f",setpts=PTS/{sp:.5f},minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1"
        fc.append(v + f",format=yuv420p[v{j}]"); vl += f"[v{j}]"
        if has_a:
            tempo, r = [], sp
            while r < 0.5:
                tempo.append("atempo=0.5"); r /= 0.5
            tempo.append(f"atempo={r:.5f}")
            fc.append(f"[1:a]atrim={a:.4f}:{b:.4f},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo"
                      + ("," + ",".join(tempo) if sp < 0.999 else "") + f"[a{j}]")
        else:
            fc.append(f"anullsrc=r=48000:cl=stereo,atrim=0:{(b - a) / sp:.4f}[a{j}]")
        al += f"[a{j}]"
    n = len(segs)
    fc.append(f"{''.join(f'[v{j}][a{j}]' for j in range(n))}concat=n={n}:v=1:a=1[v][a]")
    subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error", *args, "-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-crf", "15", "-preset", "medium", "-r", "24", "-c:a", "pcm_s16le", str(out.with_suffix(".mkv"))], check=True)
    out.with_suffix(".mkv").rename(out.with_suffix(".mkv.done"))
    subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error", "-i", str(out.with_suffix(".mkv.done")), "-c:v", "copy", "-c:a", "aac",
                    "-b:a", "256k", str(out)], check=True)
    out.with_suffix(".mkv.done").unlink()
    return out


def spans_for(takes, order):
    for scene, _ in order:
        ks = [k for k in takes if k["scene"] == scene]
        if not any(k["dialogue"] for k in ks):
            continue
        cache = OUT / f"spans_{scene}.json"
        key = [str(k["path"]) for k in ks]
        if cache.exists() and json.loads(cache.read_text())["key"] == key:
            sp = json.loads(cache.read_text())["spans"]
        else:
            parts = [(i, k["dur"], k["audio"]) for i, k in enumerate(ks)]
            wav = H.dialogue_track(f"body_{scene}", parts, [k["path"] for k in ks])
            sp = E.speech_spans(wav)
            cache.write_text(json.dumps({"key": key, "spans": sp}))
        t0 = 0.0
        for k in ks:
            k["spans"] = [(s - t0, e - t0) for s, e in sp if t0 <= (s + e) / 2 < t0 + k["dur"]]
            t0 += k["dur"]


def build(order, name, fixed=None, offscreen=(), ending=True, dry=False):
    OUT.mkdir(parents=True, exist_ok=True)
    E.OUT.mkdir(parents=True, exist_ok=True)
    takes = takes_of(order)
    spans_for(takes, order)
    items = place_items(takes, fixed, offscreen)
    total, report = plan(takes, ending)
    if dry:
        print(name, f"{total:.1f}s")
        print("\n".join(report))
        for k in takes:
            st = "; ".join(f"{a:.2f}-{b:.2f} x{(b - a) / (b - a + x):.2f}" for a, b, x in k["warp"].st if x > 0.01)
            if st:
                print(f"  slow {k['beat']}: {st}")
        return None
    for k in takes:
        render_take(k, name)
    lst = OUT / f"{name}.concat.txt"
    lst.write_text("".join(f"file '{k['render']}'\n" for k in takes))
    pic = OUT / f"{name}.picture.mp4"
    subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(pic)], check=True)
    T = H.info(pic)[0]
    args, fc, mix = ["-i", str(pic)], [], ["[0:a]aresample=48000,aformat=channel_layouts=stereo[take]"]
    lab = ["[take]"]
    for j, it in enumerate(items, 1):
        args += ["-i", str(it["file"])]
        ms = int(it["at"] * 1000)
        flt = ("," + FILTERS[it["flt"]]) if it["flt"] else ""
        fc.append(f"[{j}:a]atrim={it['a']:.3f}:{it['b']:.3f},asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo{flt},"
                  f"afade=t=in:d=0.02,afade=t=out:st={max(0, it['dur'] - 0.04):.3f}:d=0.04,adelay={ms}|{ms}[n{j}]")
        lab.append(f"[n{j}]")
    vf = f"[0:v]lut3d=file='{H.LUT}'"
    af = f"{''.join(lab)}amix=inputs={len(lab)}:duration=first:normalize=0,loudnorm=I=-14:TP=-1:LRA=11"
    if ending:
        vf += f",fade=t=out:st={T - END_FADE:.3f}:d={END_FADE}"
        af += f",afade=t=out:st={T - END_FADE:.3f}:d={END_FADE}"
    fc = mix + fc + [vf + "[vg]", af + "[am]"]
    out = OUT / f"{name}_v4.mp4"
    subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error", *args, "-filter_complex", ";".join(fc), "-map", "[vg]", "-map", "[am]",
                    "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-movflags", "+faststart", str(out)], check=True)
    sheet = [f"# {name} edit v4 — {T:.1f}s", "", "| Take | v | At | Length | Shown for | Slowed stretches |", "|---|---|---|---|---|---|"]
    sheet += [f"| {k['beat']} | v{k['v']} | {k['at']:.2f}s | {k['dur']:.2f}s | {k['out_dur']:.2f}s | "
              + ("; ".join(f"{a:.2f}-{b:.2f}s ×{(b - a) / (b - a + x):.2f}" for a, b, x in k['warp'].st if x > 0.01) or "—") + " |" for k in takes]
    sheet += ["", "## Narration and off-screen lines", ""] + [f"- {r}" for r in report]
    (OUT / f"{name}_v4.md").write_text("\n".join(sheet) + "\n")
    json.dump([{"line": it["line"], "at": round(it["at"], 3), "dur": round(it["dur"], 3), "take": it["take"]["beat"]} for it in items],
              open(OUT / f"{name}_v4.items.json", "w"), indent=1)
    json.dump([{"beat": k["beat"], "at": round(k["at"], 3), "out_dur": round(k["out_dur"], 3)} for k in takes],
              open(OUT / f"{name}_v4.takes.json", "w"), indent=1)
    print("\n".join(report)); print(out, f"{H.info(out)[0]:.2f}s")
    return out


def hook_order(h):
    return [(h, [(f"{h}-SH0{i + 1}", v) for i, v in enumerate(H.CONFIRMED[h])])]


if __name__ == "__main__":
    dry = "--plan" in sys.argv
    what = [a for a in sys.argv[1:] if not a.startswith("--")] or ["BODY", "HKA", "HKB", "HKC", "HKE"]
    for w in what:
        if w == "BODY":
            build(E.ORDER, "BODY", offscreen=OFFSCREEN, ending=True, dry=dry)
        else:
            build(hook_order(w), w, fixed=[(B / "edit" / "vo" / H.VO[w], f"{w}-SH05", 0.0)],
                  offscreen=HOOK_OFFSCREEN.get(w, ()), ending=False, dry=dry)
