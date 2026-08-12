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
  5. OpenGraph consistency: where a page uses og: tags, og:url must equal the
     canonical URL and every og:image must point to a file that exists on disk
     (a wrong share URL or a renamed image silently breaks link previews).
  6. Title + meta description: every page has a non-empty <title>; every indexable
     page has a <meta name="description">, and no two indexable pages share the same
     description text (missing/duplicate descriptions hurt search rankings).

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
CANON_RE = re.compile(r'<link rel="canonical" href="([^"]*)"')
OG_URL_RE = re.compile(r'property="og:url" content="([^"]*)"')
OG_IMG_RE = re.compile(r'property="og:image" content="([^"]*)"')
TITLE_RE = re.compile(r'<title>(.*?)</title>', re.S | re.I)
DESC_RE = re.compile(r'<meta name="description" content="([^"]*)"', re.I)
ROBOTS_RE = re.compile(r'<meta name="robots" content="([^"]*)"', re.I)
NOINDEX_OK = {"404.html", "privacy.html", "terms.html"}
SITE = "https://www.machinegunsprayfoam.com"


def expected_canon(f):
    """The clean canonical URL a page should point at itself: index → site root, else /<slug>."""
    return SITE + "/" if f == "index.html" else SITE + "/" + f[:-len(".html")]


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
    descs = {}  # meta description -> [pages], for the duplicate check (indexable pages only)
    for f in pages:
        t = open(f, encoding="utf-8").read()

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

        # 3. canonical + robots (canonical must SELF-REFERENCE — a canonical pointing at the
        #    wrong URL silently de-indexes the page in favor of another, and merely checking
        #    presence would never catch it)
        if f not in NOINDEX_OK:
            cm = CANON_RE.search(t)
            if not cm:
                fails.append("[%s] missing canonical" % f)
            else:
                want = expected_canon(f)
                if cm.group(1).rstrip("/") != want.rstrip("/"):
                    fails.append("[%s] canonical does not self-reference: %s (expected %s)" % (f, cm.group(1), want))

        # 3b. robots directive VALUE (not just presence): an indexable page accidentally flipped
        #     to "noindex" silently drops from search; a utility page that loses "noindex" gets
        #     indexed when it shouldn't. Check the actual directive both ways.
        rm = ROBOTS_RE.search(t)
        if not rm:
            fails.append("[%s] missing robots meta" % f)
        else:
            robots = rm.group(1).lower()
            if f in NOINDEX_OK:
                if "noindex" not in robots:
                    fails.append("[%s] utility page should be noindex: robots=\"%s\"" % (f, rm.group(1)))
            else:
                if "noindex" in robots:
                    fails.append("[%s] indexable page is marked noindex: robots=\"%s\"" % (f, rm.group(1)))

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

        # 5. OpenGraph consistency (only where og: is used; utility pages exempt)
        if f not in NOINDEX_OK:
            canon_m = CANON_RE.search(t)
            ogurl_m = OG_URL_RE.search(t)
            if ogurl_m and canon_m and ogurl_m.group(1) != canon_m.group(1):
                fails.append("[%s] og:url != canonical: %s vs %s" % (f, ogurl_m.group(1), canon_m.group(1)))
            for im in OG_IMG_RE.findall(t):
                local = re.sub(r"^https?://[^/]+", "", im).lstrip("/")
                if local and not os.path.exists(local):
                    fails.append("[%s] og:image file missing: %s" % (f, im))

        # 6. title + meta description present (indexable pages); collect for dup check
        tm = TITLE_RE.search(t)
        if not tm or not norm(tm.group(1)):
            fails.append("[%s] missing/empty <title>" % f)
        if f not in NOINDEX_OK:
            dm = DESC_RE.search(t)
            if not dm or not dm.group(1).strip():
                fails.append("[%s] missing meta description" % f)
            else:
                descs.setdefault(norm(dm.group(1)), []).append(f)

    # 6b. no two indexable pages share the same meta description (dilutes SEO)
    for d, fs in descs.items():
        if len(fs) > 1:
            fails.append("duplicate meta description on %s: \"%s\"" % (", ".join(sorted(fs)), d[:60]))

    # 7. sitemap completeness: every indexable page is in sitemap.xml, and no noindex page is.
    #    (sync_sitemap.py keeps lastmod fresh but a NEW page silently missing from the sitemap,
    #    or a noindex page wrongly listed, would never be flagged by a lastmod-only check.)
    if os.path.exists("sitemap.xml"):
        sm = open("sitemap.xml", encoding="utf-8").read()
        sm_locs = set(re.sub(r"^https?://[^/]+", "", u).rstrip("/") or "/" for u in re.findall(r"<loc>([^<]+)</loc>", sm))
        for f in pages:
            path = "/" if f == "index.html" else "/" + f[:-len(".html")]
            listed = path in sm_locs
            if f in NOINDEX_OK and listed:
                fails.append("[sitemap] noindex page wrongly listed: %s" % f)
            if f not in NOINDEX_OK and not listed:
                fails.append("[sitemap] indexable page missing from sitemap: %s" % f)

    print("Checked %d pages, %d JSON-LD blocks." % (len(pages), ld_total))
    if fails:
        print("FAIL — %d issue(s):" % len(fails))
        for x in fails:
            print("  " + x)
        return 1
    print("PASS — JSON-LD valid, links resolve, canonical self-references, robots directive correct, FAQ schema matches visible, OG consistent, titles+descriptions unique, sitemap complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
