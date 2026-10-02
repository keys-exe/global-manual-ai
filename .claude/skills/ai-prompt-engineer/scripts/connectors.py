#!/usr/bin/env python3
"""§5 — the Connector Map: use the connectors this account has (V7.87.0).

Different accounts run this system for different clients and products, with different connectors
connected. At every build start and resume the agent lists what this session can reach and maps
every job to the first available route on its ladder — never stalls because a default is missing.

Usage:
  connectors.py --tools tools.txt [--md map.md] [--json map.json]

tools.txt: the session's tool names, one per line, as the agent sees them (e.g. mcp__Kling_STRYDE__image_to_video,
mcp__HIGGSFIELD__generate_image). Connectors are matched by what their tools do, never by their account-specific
names. API keys are read from the environment (KIE_API_KEY, ELEVENLABS_API_KEY, HEYGEN_API_KEY) — only whether
they are set, never their values.

Output: per job, the route used (the first available on its ladder), the model it runs, whether that is the
default route, and what to connect when nothing is available. Exit 0 always (the map is information);
jobs with no route are listed under "missing".
"""
import argparse, json, os, re
from pathlib import Path

# Each connector: how to recognise it from tool names (pattern on the server segment, plus a tool it must have)
CONNECTORS = {
    "higgsfield":   {"server": r"higgsfield", "tool": r"generate_image|generate_video|generate_audio", "label": "Higgsfield"},
    "kling":        {"server": r"^kling", "tool": r"image_to_video|text_to_image", "label": "Kling (Kling AI direct)"},
    "elevenlabs_c": {"server": r"elevenlabs", "tool": r"creative_generate|generate_speech|text_to_speech", "label": "ElevenLabs connector"},
    "heygen":       {"server": r"heygen", "tool": r"create_video_from_avatar|create_speech|clone_voice", "label": "HeyGen"},
    "higgsless":    {"server": r"higgsless", "tool": r"generate", "label": "Higgsless"},
    "gdrive":       {"server": r"google_?drive|gdrive", "tool": r"download_file|read_file", "label": "Google Drive"},
}
KEYS = {"kie": ("KIE_API_KEY", "Kie AI API (scripts/kie.py)"),
        "elevenlabs_api": ("ELEVENLABS_API_KEY", "ElevenLabs API (tts_api.py, elevenlabs_clone.py, music.py)"),
        "heygen_api": ("HEYGEN_API_KEY", "HeyGen API")}

# Job -> ladder of (route, model note, verified-in-production)
LADDERS = {
    "Images (sheets, plates, beat frames)": [
        ("higgsfield", "nano_banana_pro · nano_banana_2 · gpt_image_2_5 Sunburst (§18A)", True),
        ("kie", "nano-banana-pro · nano-banana-2 · gpt-image-2-5-sunburst (§18A)", True),
        ("elevenlabs_c", "its image models — check creative_get_model_guide for Nano Banana Pro / GPT Image; else nearest, alt_reason", False),
        ("higgsless", "Nano Banana models (no Sunburst — realistic beats take the nearest, alt_reason)", True),
        ("kling", "Kling's own image model only — alt_reason on every call", False)],
    "Kling video (B-roll, mechanism, hooks)": [
        ("kling", "kling-video-v3_0_omni / kling-video-v3_0 (§44)", True),
        ("kie", "kling-3.0/video (kie.py kling)", True),
        ("higgsfield", "kling3_0 via generate_video", True),
        ("elevenlabs_c", "Kling model if listed in creative_get_model_guide", False),
        ("higgsless", "Kling model if listed by list_models", False)],
    "Seedance 2.5 (films, ingredients)": [
        ("kie", "bytedance/seedance-2-5, 720p (kie.py seedance)", True),
        ("higgsfield", "Seedance via generate_video, 720p", False),
        ("elevenlabs_c", "Seedance if listed in creative_get_model_guide", False),
        ("higgsless", "Seedance if listed by list_models", False)],
    "Voice clone": [
        ("elevenlabs_api", "IVC clone (elevenlabs_clone.py)", True),
        ("heygen", "clone_voice from the §22U source audio", False),
        ("heygen_api", "voice clone API from the §22U source audio", False),
        ("higgsfield", "create_voice_from_confirmed_audio from the §22U source audio", False),
        ("elevenlabs_c", "creative_design_voice — a DESIGNED voice, not a clone: §22U bans it, only on the user's explicit go", False)],
    "Voice-over (TTS)": [
        ("elevenlabs_api", "eleven_v4 with speed (tts_api.py)", True),
        ("elevenlabs_c", "creative_generate_speech (no speed control — pace by tags)", True),
        ("heygen", "create_speech", False),
        ("higgsfield", "generate_audio", False)],
    "Talking heads": [
        ("heygen", "Avatar V (§22U)", True),
        ("heygen_api", "Avatar V", False),
        ("higgsfield", "a talking-avatar video model if listed — unverified", False)],
    "Music (BGM, music videos)": [
        ("elevenlabs_api", "eleven_music_v2 composition plan (music.py)", True),
        ("elevenlabs_c", "music node", True),
        ("higgsfield", "generate_audio music model — unverified", False)],
    "Sound effects, room tone, voice isolation": [
        ("elevenlabs_c", "eleven_text_to_sound_v2 · audio_isolation", True),
        ("elevenlabs_api", "sound-generation / audio-isolation endpoints", False),
        ("higgsfield", "generate_audio", False)],
    "Drive intake": [
        ("gdrive", "Google Drive connector", True),
        ("public_link", "fetch_drive.py on a link shared 'anyone with the link'", True)],
    "File hosting for references (public URLs)": [
        ("kie", "kie.py upload", True),
        ("higgsfield", "media_upload / media_import_url", True),
        ("elevenlabs_c", "creative_create_asset_upload", False)],
}
CONNECT_HINT = {
    "Images (sheets, plates, beat frames)": "connect Higgsfield (claude.ai connectors) or set KIE_API_KEY (environment secret)",
    "Kling video (B-roll, mechanism, hooks)": "connect Kling or Higgsfield, or set KIE_API_KEY",
    "Seedance 2.5 (films, ingredients)": "set KIE_API_KEY, or connect Higgsfield",
    "Voice clone": "set ELEVENLABS_API_KEY, or connect HeyGen",
    "Voice-over (TTS)": "set ELEVENLABS_API_KEY, or connect ElevenLabs",
    "Talking heads": "connect HeyGen",
    "Music (BGM, music videos)": "set ELEVENLABS_API_KEY, or connect ElevenLabs",
    "Sound effects, room tone, voice isolation": "connect ElevenLabs",
    "Drive intake": "connect Google Drive, or share the folder as 'anyone with the link'",
    "File hosting for references (public URLs)": "set KIE_API_KEY, or connect Higgsfield",
}


def detect(tools):
    have = {}
    servers = {}
    for t in tools:
        m = re.match(r"mcp__([^_].*?)__(.+)$", t.strip())
        if m:
            servers.setdefault(m.group(1), set()).add(m.group(2))
    for key, spec in CONNECTORS.items():
        for srv, names in servers.items():
            if re.search(spec["server"], srv, re.I) and any(re.search(spec["tool"], n, re.I) for n in names):
                have[key] = srv
                break
    for key, (env, _) in KEYS.items():
        if os.environ.get(env):
            have[key] = env
    have["public_link"] = "always"
    return have, sorted(servers)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tools", required=True)
    ap.add_argument("--md")
    ap.add_argument("--json")
    a = ap.parse_args()
    tools = [l for l in Path(a.tools).read_text().splitlines() if l.strip()]
    have, servers = detect(tools)
    label = {k: v["label"] for k, v in CONNECTORS.items()} | {k: v[1] for k, v in KEYS.items()} | {"public_link": "public Drive link"}
    jobs, missing = [], []
    for job, ladder in LADDERS.items():
        pick = next(((r, m, v, i) for i, (r, m, v) in enumerate(ladder) if r in have), None)
        if not pick:
            missing.append({"job": job, "connect": CONNECT_HINT[job]})
            jobs.append({"job": job, "route": None, "default": ladder[0][0]})
            continue
        r, m, v, i = pick
        jobs.append({"job": job, "route": r, "label": label[r], "found_as": have[r], "model": m,
                     "default": i == 0, "verified": v,
                     "note": "" if i == 0 else f"default {label[ladder[0][0]]} not on this account — using rung {i + 1}"
                             + ("" if v else "; unverified route: check the logged model on the first job (§5)")})
    out = {"connectors_found": {k: v for k, v in have.items() if k != "public_link"}, "servers_seen": servers,
           "jobs": jobs, "missing": missing}
    if a.json:
        Path(a.json).write_text(json.dumps(out, indent=1))
    if a.md:
        md = ["### Connector map", "", "What this account has, and the route each job takes (§5). The first route on each "
              "job's ladder that this account has is used; anything not the default is marked.", "",
              "| Job | Route | Model | Note |", "|---|---|---|---|"]
        for j in jobs:
            if j["route"]:
                md.append(f"| {j['job']} | {j['label']}{'' if j['default'] else ' ⚠'} | {j['model']} | {j['note'] or 'default'} |")
            else:
                md.append(f"| {j['job']} | **none** | — | {CONNECT_HINT[j['job']]} |")
        Path(a.md).write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
