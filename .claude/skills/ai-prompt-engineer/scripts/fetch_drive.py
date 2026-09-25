#!/usr/bin/env python3
"""§18B Drive intake — pull a shared Google Drive folder and sort it into the Intake Pack.

Usage:
  fetch_drive.py BUILD DRIVE_FOLDER_URL

Downloads the folder (shared "Anyone with the link — Viewer") into
builds/<BUILD>/intake/, then sorts every file by name and type:
  video (.mp4 .mov .webm .m4v)          -> inspo   (a name containing "inspo" is primary;
                                                     else the first alphabetically)
  document named *script*               -> script
  document named *product* or *sheet*   -> product_sheet
  image (.jpg .jpeg .png .webp .heic)   -> product_images
  anything else                         -> unsorted (reported, never guessed)
Documents (.txt .md .docx .pdf) are converted to .txt beside the original.
Then runs fetch_inspo.py on the inspo videos for the §42 Part 1 measurements.
Prints a JSON report. Exit 0 = every required part found, 2 = something missing.

Setup (per session): pip install -q gdown python-docx pypdf imageio-ffmpeg yt-dlp
"""
import json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
VIDEO = {".mp4", ".mov", ".webm", ".m4v"}
IMAGE = {".jpg", ".jpeg", ".png", ".webp", ".heic"}
DOC = {".txt", ".md", ".docx", ".pdf"}
SHEET_CODE = {".py"}  # the Appendix B / E9 product_sheet.py


def to_text(path):
    ext = path.suffix.lower()
    if ext in {".txt", ".md"}:
        return path.read_text(encoding="utf-8", errors="replace")
    if ext == ".docx":
        import docx
        return "\n".join(p.text for p in docx.Document(str(path)).paragraphs)
    if ext == ".pdf":
        from pypdf import PdfReader
        return "\n".join((pg.extract_text() or "") for pg in PdfReader(str(path)).pages)
    return None


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    build, url = sys.argv[1], sys.argv[2]
    dest = Path("builds") / build / "intake"
    dest.mkdir(parents=True, exist_ok=True)

    r = subprocess.run(["gdown", "--folder", url, "-O", str(dest)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(json.dumps({"status": "FETCH_FAILED",
                          "error": (r.stderr.strip().splitlines() or ["unknown"])[-1],
                          "hint": "Share the folder as 'Anyone with the link — Viewer'."}, indent=2))
        sys.exit(2)

    files = sorted(p for p in dest.rglob("*") if p.is_file() and not p.name.endswith(".extracted.txt"))
    sorted_ = {"inspo": [], "script": [], "product_sheet": [], "product_images": [], "unsorted": []}
    for p in files:
        name, ext = p.stem.lower(), p.suffix.lower()
        if ext in VIDEO:
            sorted_["inspo"].append(p)
        elif ext in IMAGE:
            sorted_["product_images"].append(p)
        elif ext in DOC and "script" in name:
            sorted_["script"].append(p)
        elif ext in DOC | SHEET_CODE and ("product" in name or "sheet" in name):
            sorted_["product_sheet"].append(p)
        else:
            sorted_["unsorted"].append(p)
    # A script named after the ad title: exactly one unsorted document and no script -> script
    inferred = []
    docs_left = [p for p in sorted_["unsorted"] if p.suffix.lower() in DOC]
    if not sorted_["script"] and len(docs_left) == 1:
        sorted_["script"].append(docs_left[0])
        sorted_["unsorted"].remove(docs_left[0])
        inferred.append(f"script <- {docs_left[0].name} (only unsorted document)")
    sorted_["inspo"].sort(key=lambda p: ("inspo" not in p.stem.lower(), p.name.lower()))

    texts = {}
    for key in ("script", "product_sheet"):
        for p in sorted_[key]:
            if p.suffix.lower() in SHEET_CODE:
                continue  # read as code, not extracted
            t = to_text(p)
            out = p.with_name(p.name + ".extracted.txt")
            out.write_text(t or "", encoding="utf-8")
            texts[str(p)] = {"text_file": str(out), "chars": len(t or ""),
                             "first_line": (t or "").strip().splitlines()[0][:120] if (t or "").strip() else None}

    measures = []
    if sorted_["inspo"]:
        m = subprocess.run([sys.executable, str(HERE / "fetch_inspo.py"), build,
                            *[str(p) for p in sorted_["inspo"]]], capture_output=True, text=True)
        measures = json.loads(m.stdout) if m.stdout.strip() else [{"error": m.stderr[-400:]}]

    missing = [k for k in ("inspo", "script", "product_sheet", "product_images") if not sorted_[k]]
    unreadable = [k for k, v in texts.items() if v["chars"] == 0]
    report = {
        "status": "OK" if not (missing or unreadable) else "MISSING_PARTS",
        "missing": missing,
        "inferred": inferred,
        "unreadable_documents": unreadable,  # 0 chars: scanned PDF or empty file — ask for .docx/.txt
        "files": {k: [str(p) for p in v] for k, v in sorted_.items()},
        "primary_inspo": str(sorted_["inspo"][0]) if sorted_["inspo"] else None,
        "documents": texts,
        "inspo_measurements": measures,
    }
    print(json.dumps(report, indent=2))
    sys.exit(0 if report["status"] == "OK" else 2)


if __name__ == "__main__":
    main()
