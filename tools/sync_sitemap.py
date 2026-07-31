#!/usr/bin/env python3
"""Sync sitemap.xml <lastmod> dates to each page's real git commit date.

Why: every content edit changes a page's git commit date, so the sitemap's
<lastmod> values drift out of sync and start understating freshness to crawlers.
This rewrites each <loc>'s <lastmod> from `git log -1 --date=short` for the file
that URL maps to.

Usage (run from the repo root, i.e. the folder containing sitemap.xml):
  python3 tools/sync_sitemap.py            # fix sitemap.xml in place
  python3 tools/sync_sitemap.py --check    # report drift only; exit 1 if any (for CI)

No third-party dependencies. URL -> file mapping: "/" -> index.html,
"/foo" -> foo.html (or foo/ if that path exists). Entries whose file is missing
are left untouched.
"""
import os
import re
import subprocess
import sys

# \s* between </loc> and <lastmod> so a pretty-printed (line-broken/indented)
# sitemap still matches, not just the compact one-line form.
LOC_RE = re.compile(
    r'(<loc>https://www\.machinegunsprayfoam\.com/([^<]*)</loc>\s*<lastmod>)([^<]+)(</lastmod>)'
)


def url_path_to_file(path):
    if path == "":
        return "index.html"
    if os.path.exists(path):
        return path
    return path + ".html"


def git_date(f):
    return subprocess.run(
        ["git", "log", "-1", "--format=%cd", "--date=short", "--", f],
        capture_output=True, text=True,
    ).stdout.strip()


def main():
    check = "--check" in sys.argv[1:]
    sitemap = "sitemap.xml"
    if not os.path.exists(sitemap):
        print("ERROR: run from the repo root (sitemap.xml not found here)", file=sys.stderr)
        return 2

    src = open(sitemap, encoding="utf-8").read()
    drift = []

    def repl(m):
        prefix, path, old, suffix = m.group(1), m.group(2), m.group(3), m.group(4)
        f = url_path_to_file(path)
        if not os.path.exists(f):
            return m.group(0)
        d = git_date(f)
        if not d:
            return m.group(0)
        if d != old:
            drift.append((f, old, d))
        return prefix + d + suffix

    out = LOC_RE.sub(repl, src)

    if check:
        if drift:
            print("STALE lastmod entries (%d):" % len(drift))
            for f, old, new in drift:
                print("  %-48s %s -> %s" % (f, old, new))
            return 1
        print("sitemap lastmod is in sync (0 drift).")
        return 0

    if drift:
        open(sitemap, "w", encoding="utf-8").write(out)
        print("Updated %d lastmod entries." % len(drift))
    else:
        print("Already in sync (0 changed).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
