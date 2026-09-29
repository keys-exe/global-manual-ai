#!/usr/bin/env python3
"""§22X — video preflight: lint a video call before any credit is spent.

Usage:
  preflight.py CALL.json [--json]

CALL.json describes one paid video call exactly as it will be sent:
  {
    "beat": "BF-SC02-SH03",
    "connector": "seedance" | "kling",
    "mode": 1-5,                       # §18A mode lock
    "kind": "dialogue" | "listener" | "insert" | "broll" | "multi",
    "prompt": "<the full prompt text, or a Kling §35/§36 JSON string>",
    "duration": 8,
    "resolution": "720p", "aspect_ratio": "9:16",
    "start_image": "<approved url or path>",
    "start_approved": true,            # Manual: the user's Confirm; Automatic: §22V USE + scene contact sheet
    "pinned": false, "end_image": null, "end_approved": false,
    "files": ["..."],                  # Seedance ingredients (images + videos + audios), each named in the manifest
    "audios": ["..."],                 # voice masters (dialogue)
    "dialogue": "the spoken words, verbatim from the script",
    "script_line": "the same line as script_lines.py extracted it",
    "pace": "unhurried" | "brisk",
    "subject_motion": "still" | "in_place" | "travels",
    "prefer_multi_shots": "false",
    "generation": 1,                   # 1 = first try, 2 = the one fix; 3+ only with user_go (§22X)
    "user_go": null | "the user's words giving the go for a 3rd+ generation, and the date",
    "fix_note": "diagnosed fault → the change made (required on generation 2)",
    "rack": null | {"from": "...", "to": "...", "cue": "..."},   # §30J focus change inside the clip
    "risks": [{"risk": "...", "prevented_by": "..."}]   # top three failure modes and the clause that prevents each
  }

Every check is PASS or FAIL. Any FAIL → exit 1 and the call is not sent.
"""
import argparse, json, re, sys
from pathlib import Path

# A signature sentence from each normative string (Appendix A), so a pasted string can be verified present.
SIG = {
    "INHERIT-FILM": "Nothing about the look changes across the clip",
    "INHERIT-ANIM": "Every character stays exactly on model",
    "STATE-CARRY": "None of it resets",
    "DRAMA-DELIVERY": "UNDER THE LINE",
    "VOICE NOW": "VOICE NOW",
    "PLAYING": "PLAYING:",
    "LISTEN-LINE": "The reaction arrives a beat after the words that cause it",
    "BUSINESS-LINE": "the hands never stop to gesture",
    "AUD-FILM": "clean production sound from a boom microphone",
    "AUD-ANIM": "clean studio voice performance recorded for animation",
    "NEG-SCENECUT": "no light direction changing within the scene",
    "NEG-DRAMA": "no theatrical acting",
    "NEG-FILM": "no phone camera look",
    "NEG-ANIMFILM": "no concept art",
    "MULTI-FILM": "within a single take",
    "NEG-SOUND": "no music, no score, no sound effects",
    "SERIES-LOOK": "The look of a high-end live-action drama series",
}
RIGS = {  # rig signature → F-rig (F6–F10: the Seedance move library, §24N)
    "F1": "steady push toward the subject", "F2": "Camera on a tripod", "F3": "Camera on an operator's shoulder",
    "F4": "Camera on a slider", "F5": "Camera on a stabiliser",
    "F6": "Camera pulling back on a dolly", "F7": "Camera arcing", "F8": "Camera on a crane",
    "F9": "Camera tracking alongside", "F10": "Camera performing a slow dolly zoom",
}
TRAVEL_RIGS = {"F1", "F4", "F5", "F6", "F7", "F8", "F9", "F10"}   # the camera moves through space
NOT_IN_PLACE = {"F1", "F4", "F5", "F6", "F7", "F9", "F10"}         # subject sits, stands, turns, reaches (§24K/§24N)
NOT_TRAVELS = {"F1", "F3", "F4", "F6", "F7", "F8", "F10"}          # subject walks: only F2, F5, F9
SEEDANCE_ONLY = {"F6", "F7", "F8", "F9", "F10"}
STREAMERS = re.compile(r"\b(netflix|hbo|max original|prime video|amazon original|apple tv|disney\+?|hulu|paramount\+?|peacock)\b", re.I)
WALK = re.compile(r"\b(walks?|walking|steps? (?:toward|into|across|down|up)|crosses|climbs?|stairs|runs?|running)\b", re.I)
PLACEHOLDER = re.compile(r"\[(?:[A-Z][A-Z0-9 ,:/'’\-]{2,}|NAME|WHO|WORD|STATE|PACE|SIDE|FOCAL)[^\]]*\]")
BANNED = re.compile(r"\bcinematic\b", re.I)


def words(t):
    return len(re.findall(r"[A-Za-z0-9’']+", t or ""))


def word_budget(d, pace):
    # §28H: 5s → 9 brisk / 8 unhurried; 10s → 20 / 18 (linear through both points)
    return int(2.2 * d - 2) if pace == "brisk" else int(2 * d - 2)


def run(c):
    res = []

    def check(name, ok, detail=""):
        res.append({"check": name, "result": "PASS" if ok else "FAIL", "detail": detail})

    p = c.get("prompt", "")
    conn = c.get("connector", "").lower()
    mode = int(c.get("mode", 1))
    kind = c.get("kind", "broll")
    film = mode in (4, 5)
    d = c.get("duration")
    gen = int(c.get("generation", 1))

    # 1. Generation budget
    go = (c.get("user_go") or "").strip()
    check("generation ≤ 2, or the user's go", gen <= 2 or bool(go), f"generation {gen}; a third call on the same shot needs the user (§22X)")
    if gen >= 2:
        fn = c.get("fix_note", "")
        check("gen 2 has a diagnosed fix", "→" in fn or "->" in fn, fn or "missing fix_note")

    # 2. Frames — on Seedance, ingredients: information, never frames (§4, V7.68.0)
    if conn == "seedance":
        check("every ingredient approved", c.get("ingredients_approved") is True, "Manual: the user's Confirm on every ingredient card")
        check("no frame in the pack", not c.get("start_image"), "a Seedance call carries no start, master or scene frame")
    else:
        check("start image approved", bool(c.get("start_image")) and c.get("start_approved") is True)
    if c.get("pinned"):
        check("pinned: end image approved", bool(c.get("end_image")) and c.get("end_approved") is True)
        check("pinned: runs on Kling first-and-last frame", conn == "kling", "pinned shots never run on Seedance (§24K)")

    # 3. Call parameters
    check("aspect 9:16", c.get("aspect_ratio") == "9:16")
    if conn == "seedance":
        check("Seedance 720p", c.get("resolution") == "720p")
        check("Seedance duration 4–30", isinstance(d, (int, float)) and 4 <= d <= 30, str(d))
        files = c.get("files", [])
        check("ingredients ≤ 30 files", len(files) <= 30, f"{len(files)} files")
        check("ingredient manifest present", "@image1" in p or "ING-MANIFEST" in p or "reference" in p.lower())
    elif conn == "kling":
        check("Kling duration 3–15", isinstance(d, (int, float)) and 3 <= d <= 15, str(d))
        check("prompt ≤ 2,500 chars", len(p) <= 2500, f"{len(p)} chars")
        check("prefer_multi_shots false", str(c.get("prefer_multi_shots", "")).lower() == "false")
    else:
        check("known connector", False, conn)

    # 4. Prompt hygiene
    ph = PLACEHOLDER.findall(p)
    check("no unfilled [SLOTS]", not ph, ", ".join(sorted(set(ph)))[:300])
    check("no banned word 'cinematic'", not BANNED.search(p))
    check("no streamer, series or studio name (§24N, §10A)", not STREAMERS.search(p), ",".join(sorted(set(m.group(0) for m in STREAMERS.finditer(p)))))

    # 5. Motion (§27G / §24K)
    rigs = [r for r, s in RIGS.items() if s in p]
    sm = c.get("subject_motion") or ("travels" if WALK.search(p) else "still")
    series = film and mode == 4 and conn == "seedance" or bool(c.get("series"))
    if film or series:
        check("one F-rig", len(rigs) == 1, ",".join(rigs) or "none found")
        bad = [r for r in rigs if (sm == "in_place" and r in NOT_IN_PLACE) or (sm == "travels" and r in NOT_TRAVELS)]
        check("camera or subject moves, never both — except F5/F9 on a walk (§24K, §24N)", not bad, f"subject {sm}, rig {','.join(rigs)}")
        if "F5" in rigs:
            check("F5 framed waist-up", "waist" in p.lower())
        if "F9" in rigs:
            check("F9: a walk in profile", sm == "travels" and "profile" in p.lower(), f"subject {sm}")
        if set(rigs) & SEEDANCE_ONLY:
            check("F6–F10 on Seedance only (§24N)", conn == "seedance", conn)
    if series:
        check("SERIES-LOOK (§24N)", SIG["SERIES-LOOK"] in p)
    if kind == "multi":
        check("MULTI-SHOT only when nobody moves", sm == "still", f"subject {sm}")

    # 5b. Focus (§30J)
    rk = c.get("rack")
    if rk:
        check("rack: cue named", bool(rk.get("cue")))
        check("rack: subject still", sm == "still", f"subject {sm}")
        if film:
            check("rack: no travelling rig", not (set(rigs) & TRAVEL_RIGS), ",".join(rigs))
            check("rack: pull written", "focus pulls" in p or "pulls focus" in p)
        else:
            check("rack: Mode 1 tap-to-focus", "tap" in p.lower(), "phones tap to focus — never a clean pull (§30J)")
        check("rack: one focus change", len(re.findall(r"focus (?:pulls|shifts|jumps)", p)) <= 1)
    if film:
        check("FOCUS-LINE", "FOCUS:" in p, "the shot names what is sharp (§30J)")

    # 6. Film strings
    if film:
        check("INHERIT string", SIG["INHERIT-FILM" if mode == 4 else "INHERIT-ANIM"] in p)
        check("NEG-SCENECUT", SIG["NEG-SCENECUT"] in p)
        check("NEG-FILM / NEG-ANIMFILM", SIG["NEG-FILM" if mode == 4 else "NEG-ANIMFILM"] in p)
        check("NEG-SOUND (clips carry dialogue only, §24M)", SIG["NEG-SOUND"] in p)
        if kind in ("dialogue", "listener", "multi", "broll") and kind != "insert":
            check("STATE-CARRY", SIG["STATE-CARRY"] in p)
            check("NEG-DRAMA", SIG["NEG-DRAMA"] in p)
        if kind in ("dialogue", "listener", "multi"):
            check("BUSINESS-LINE", SIG["BUSINESS-LINE"] in p)
        if kind in ("dialogue", "multi"):
            for k in ("DRAMA-DELIVERY", "PLAYING", "VOICE NOW"):
                check(k, SIG[k] in p)
            check("AUD string", SIG["AUD-FILM" if mode == 4 else "AUD-ANIM"] in p)
            check("voice master attached", bool(c.get("audios")), "audios_list empty")
        if kind == "listener":
            check("LISTEN-LINE", SIG["LISTEN-LINE"] in p)
        if kind == "multi":
            check("MULTI-FILM", SIG["MULTI-FILM"] in p)

    # 7. Dialogue: verbatim and inside the word budget
    dl = c.get("dialogue")
    if dl:
        sl = c.get("script_line")
        norm = lambda t: re.sub(r"\s+", " ", (t or "").strip())
        check("dialogue verbatim from the script", sl is not None and norm(dl) == norm(sl), "script_line missing" if sl is None else "")
        check("dialogue in prompt", norm(dl) in norm(p))
        if isinstance(d, (int, float)):
            b = word_budget(d, c.get("pace", "unhurried"))
            check("§28H word budget", words(dl) <= b, f"{words(dl)} words / {b} for {d}s")

    # 8. Failure-mode review
    risks = c.get("risks") or []
    ok = len(risks) >= 3 and all(r.get("risk") and r.get("prevented_by") for r in risks)
    check("top three risks, each prevented", ok, f"{len(risks)} listed")

    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("call")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    c = json.loads(Path(a.call).read_text())
    res = run(c)
    fails = [r for r in res if r["result"] == "FAIL"]
    if a.json:
        print(json.dumps({"beat": c.get("beat"), "pass": not fails, "checks": res}, indent=1))
    else:
        for r in res:
            print(f"{r['result']:4}  {r['check']}" + (f"  — {r['detail']}" if r["detail"] else ""))
        print(f"\n{c.get('beat', '?')}: {'PREFLIGHT PASS' if not fails else f'PREFLIGHT FAIL ({len(fails)}) — not sent'}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
