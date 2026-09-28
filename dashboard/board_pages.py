#!/usr/bin/env python3
"""Keep every Generation Board on the current template (CLAUDE.md, "Board design sync").

  board_pages.py status [--owner TEXT]   boards whose publishedSha differs from the template (exit 1 if any)
  board_pages.py build OUTDIR [--owner TEXT] [--all]
                                         write each out-of-date board's page (its BOARD_ROLE + <title>) to OUTDIR
                                         and print "url  file" pairs to publish with Artifact (url = the board)
  board_pages.py mark URL [URL ...]      record that these boards now run the current template
  board_pages.py title URL "TITLE"       record a board's <title> (read it from the live board first)

The registry is dashboard/boards.json. A board with no recorded title is skipped by build until
its title is recorded, so a republish never renames a board.
"""
import hashlib, json, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(ROOT, "generation_board.html")
REGISTRY = os.path.join(ROOT, "boards.json")
ROLE_LINE = re.compile(r'^const BOARD_ROLE = "[a-z]+";', re.M)


def template_sha():
    return hashlib.sha256(open(TEMPLATE, "rb").read()).hexdigest()[:16]


def load():
    return json.load(open(REGISTRY))


def save(reg):
    with open(REGISTRY, "w") as f:
        json.dump(reg, f, indent=1, ensure_ascii=False)
        f.write("\n")


def pick(reg, args):
    owner = None
    if "--owner" in args:
        owner = args[args.index("--owner") + 1]
    sha = template_sha()
    for b in reg["boards"]:
        if owner and owner.lower() not in (b.get("owner") or "").lower():
            continue
        if "--all" in args or b.get("publishedSha") != sha:
            yield b


def page(board):
    html = open(TEMPLATE, encoding="utf-8").read()
    if not ROLE_LINE.search(html):
        sys.exit("template has no BOARD_ROLE line")
    html = ROLE_LINE.sub(f'const BOARD_ROLE = "{board["role"]}";', html, count=1)
    html, n = re.subn(r"<title>.*?</title>", f"<title>{board['title']}</title>", html, count=1)
    if not n:
        sys.exit("template has no <title>")
    return html


def main(argv):
    if not argv:
        sys.exit(__doc__)
    cmd, args = argv[0], argv[1:]
    reg = load()
    sha = template_sha()
    if cmd == "status":
        stale = list(pick(reg, args))
        for b in stale:
            print(f'{b["build"]:22} {b["role"]:8} {b["url"]}  owner: {b.get("owner")}'
                  f'{"  (title unknown)" if not b.get("title") else ""}')
        return 1 if stale else 0
    if cmd == "build":
        out = args[0]
        os.makedirs(out, exist_ok=True)
        for b in pick(reg, args[1:]):
            if not b.get("title"):
                print(f'SKIP {b["url"]}  title unknown: read the board, then `board_pages.py title {b["url"]} "<title>"`')
                continue
            path = os.path.join(out, f'{b["build"]}-{b["role"]}.html')
            open(path, "w", encoding="utf-8").write(page(b))
            print(f'{b["url"]}  {path}')
        return 0
    if cmd == "mark":
        urls = set(args)
        hit = [b for b in reg["boards"] if b["url"] in urls]
        for b in hit:
            b["publishedSha"] = sha
        save(reg)
        print(f"marked {len(hit)} board(s) at template {sha}")
        return 0 if len(hit) == len(urls) else 1
    if cmd == "title":
        url, title = args
        hit = [b for b in reg["boards"] if b["url"] == url]
        if not hit:
            sys.exit(f"{url} is not in the registry")
        hit[0]["title"] = title
        save(reg)
        return 0
    sys.exit(__doc__)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
