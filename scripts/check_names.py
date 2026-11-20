"""Retired names (the rebrand plan, stage 6; the names are on docs/naming.md
in internal-docs). The brand before Flockadoo, the network client's word for
its network, the product's old word for what a provider runs, and the brand
on the wrong domain never come back, in any tracked file's content or path,
outside scripts/names-allow.txt. Each pattern is written so that this file
does not match it.

    python3 scripts/check_names.py              # the repository
    python3 scripts/check_names.py --self-test  # the negative case
"""

import fnmatch
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

RETIRED = [
    ("the old brand", re.compile(r"(?i)infer(?:oute|scale|bid)|sent[n]l")),
    ("the network's old name (say Winglink)", re.compile(r"(?i)tail[n]et")),
    ("the old word for a flock", re.compile(r"(?i)clus[t]er")),
    ("the brand on the wrong domain (it is flockadoo.ai)", re.compile(r"(?i)flockadoo(\\)?\.com")),
]


def read_allowed(text):
    out = []
    for line in text.splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        glob, expr = line.split("\t", 1)
        out.append({"source": line, "glob": glob, "line": re.compile(expr), "used": False})
    return out


def find_retired(files, allow):
    found = []
    for path in sorted(files):
        for n, line in [(0, path)] + list(enumerate(files[path].splitlines(), 1)):
            where = f"{path} (the path)" if n == 0 else f"{path}:{n}"
            for what, rx in RETIRED:
                if not rx.search(line):
                    continue
                ok = False
                for a in allow:
                    if fnmatch.fnmatchcase(path, a["glob"]) and a["line"].search(line):
                        a["used"] = ok = True
                if not ok:
                    found.append(f"{where}: {what}")
    stale = [a["source"] for a in allow if not a["used"]]
    return found, stale


def tracked_files():
    out = subprocess.run(["git", "-C", str(ROOT), "ls-files", "-z"], capture_output=True, check=True).stdout
    files = {}
    for p in out.decode().split("\0"):
        if not p:
            continue
        try:
            data = (ROOT / p).read_bytes()
        except FileNotFoundError:
            continue
        if b"\0" in data[:8192]:
            continue
        files[p] = data.decode("utf-8", errors="replace")
    return files


def self_test():
    brand, word = "Infer" + "oute", "clus" + "ter"
    files = {
        "docs/a.md": f"The {brand} client.\n",
        f"docs/{word}s.md": "# Page\n",
        "docs/_redirects": f"/provider/old-{word}s /provider/new/ 301\n",
        "docs/clean.md": "A flock on Winglink, at docs.flockadoo.ai.\n",
    }
    allow = read_allowed(f"docs/_redirects\t^/provider/old-{word}s \nnothing.md\t.\n")
    found, stale = find_retired(files, allow)
    want = ["docs/a.md:1: the old brand", f"docs/{word}s.md (the path): the old word for a flock"]
    assert found == want, found
    assert stale == ["nothing.md\t."], stale
    print("self-test passed")


def main():
    if sys.argv[1:] == ["--self-test"]:
        self_test()
        return 0
    allow = read_allowed((ROOT / "scripts" / "names-allow.txt").read_text())
    found, stale = find_retired(tracked_files(), allow)
    for f in found:
        print(f)
    for s in stale:
        print(f"scripts/names-allow.txt allows nothing any more; remove it: {s}")
    if found or stale:
        print(f"{len(found)} retired names, {len(stale)} stale entries; use the names on docs/naming.md (internal-docs)")
        return 1
    print("no retired names")
    return 0


if __name__ == "__main__":
    sys.exit(main())
