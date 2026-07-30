#!/usr/bin/env python3
"""Local QA gate for the MGSF marketing site — no third-party dependencies.

Runs the checks that must stay green before deploy:
  1. JSON-LD: every <script type="application/ld+json"> block parses.
  2. Internal links: every href="/..." resolves to a real file.
  3. Canonical + robots: every indexable page has a <link rel="canonical"> and a
     <meta name="robots">. (404/privacy/terms are allowed to be noindex.)
  4. FAQPage schema == visible text: each Question/Answer in a FAQPage block
     matches the page's visible <details><summary>/<p> or <h3>/<p> copy
     (rendered, tag-stripped, entity-decoded) — Google's exact-match requirement.

Usage (run from the repo root, i.e. the folder containing the .html files):
  python3 tools/qa_check.py

Exit code 0 = all clean; 1 = at least one failure (prints details). CI-ready.
"""
import glob
import html
import json
import os
import re
import sys

LD_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
HREF_RE = re.compile(r'href="(/[^"#?]*)"')
DETAILS_RE = re.compile(r'<details><summary>(.*?)</summary>\s*<p[^>]*>(.*?)</p>\s*</details>', re.S)
# question text holds no tags; [^<]* keeps a match from spanning across sibling <h3> blocks
H3_RE = re.compile(r'<h3>([^<]*)</h3>\s*<p[^>]*>(.*?)</p>', re.S)
NOINDEX_OK = {"404.html", "privacy.html", "terms.html"}


def norm(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()


def url_to_file(path):
    p = path.strip("/")
    if p == "":
        return "index.html"
    return p if os.path.exists(p) else p + ".html"


def main():
    fails = []
    pages = sorted(glob.glob("*.html"))
    if not pages:
        print("ERROR: run from the repo root (no .html files here)", file=sys.stderr)
        return 2

    ld_total = 0
    for f in pages:
        t = open(f).read()

        # 1. JSON-LD validity
        blocks = LD_RE.findall(t)
        ld_total += len(blocks)
        for b in blocks:
            try:
                json.loads(b)
            except Exception as e:
                fails.append("[%s] invalid JSON-LD: %s" % (f, e))

        # 2. internal links resolve
        for href in HREF_RE.findall(t):
            if not os.path.exists(url_to_file(href)) and not os.path.exists(href.strip("/")):
                fails.append("[%s] broken internal link: %s" % (f, href))

        # 3. canonical + robots
        if f not in NOINDEX_OK:
            if '<link rel="canonical"' not in t:
                fails.append("[%s] missing canonical" % f)
            if 'name="robots"' not in t:
                fails.append("[%s] missing robots meta" % f)

        # 4. FAQPage schema == visible
        vis = {}
        for m in DETAILS_RE.finditer(t):
            vis[norm(m.group(1))] = norm(m.group(2))
        for m in H3_RE.finditer(t):
            vis.setdefault(norm(m.group(1)), norm(m.group(2)))
        for b in blocks:
            if '"FAQPage"' not in b:
                continue
            try:
                d = json.loads(b)
            except Exception:
                continue
            for q in d.get("mainEntity", []):
                qn = norm(q.get("name", ""))
                an = norm(q.get("acceptedAnswer", {}).get("text", ""))
                if vis.get(qn) != an:
                    fails.append("[%s] FAQ schema/visible mismatch: %s" % (f, qn[:60]))

    print("Checked %d pages, %d JSON-LD blocks." % (len(pages), ld_total))
    if fails:
        print("FAIL — %d issue(s):" % len(fails))
        for x in fails:
            print("  " + x)
        return 1
    print("PASS — JSON-LD valid, links resolve, canonical+robots present, FAQ schema matches visible.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
