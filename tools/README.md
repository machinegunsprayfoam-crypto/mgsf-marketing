# tools/ — maintenance scripts

Small, dependency-free Python scripts for keeping the marketing site healthy.
Run them from the **repo root** (the folder that contains `sitemap.xml` and the
`.html` pages), not from inside `tools/`.

## `qa_check.py` — pre-deploy QA gate

Verifies the things that must stay green before the site goes live:

- every `application/ld+json` block parses (valid JSON-LD),
- every internal `href="/…"` resolves to a real page (no broken links),
- every indexable page has a `<link rel="canonical">` and a `<meta name="robots">`
  (`404.html`, `privacy.html`, `terms.html` are exempt — they're noindex),
- every **FAQPage** entry's schema text exactly matches the visible FAQ copy on the
  page (Google requires an exact match, or the rich result is dropped).

```bash
python3 tools/qa_check.py      # prints PASS/FAIL; exit 0 = clean, 1 = issues found
```

Run it before every merge to `main` / deploy. Exit code 1 makes it CI-friendly.

## `sync_sitemap.py` — keep sitemap lastmod honest

Rewrites each `<lastmod>` in `sitemap.xml` to the real last-commit date of the page
that URL maps to, so the sitemap stops understating freshness to crawlers after edits.

```bash
python3 tools/sync_sitemap.py           # fix sitemap.xml in place
python3 tools/sync_sitemap.py --check   # report drift only; exit 1 if any (CI)
```

Run the plain form as a **pre-deploy step** (commit the result), and/or the `--check`
form in CI to catch a stale sitemap before it ships.

## Suggested order before a deploy

```bash
python3 tools/sync_sitemap.py    # refresh lastmod dates
python3 tools/qa_check.py        # confirm the site is clean
```

Both scripts are plain Python 3 with no third-party dependencies, so they run
anywhere Python 3 is available (local shell or a CI runner).

## `verify_all.sh` — one-command pre-push check

Runs the sitemap-drift check + the QA gate together and reports one result.

```bash
bash tools/verify_all.sh      # exit 0 only if everything is clean — gate commits/deploys on it
```

## `faq_gen.py` — matched FAQ generator (kills schema drift)

Emits the visible `<details>` HTML **and** the FAQPage JSON-LD from ONE list of Q&A
pairs, so they can't disagree (Google needs them identical after tag-strip +
entity-decode). Visible gets `&amp;`, JSON-LD gets raw `&` — they normalize equal.

```bash
python3 tools/faq_gen.py faqs.json      # faqs.json = [{"q":"…","a":"…"}, …]
echo '[{"q":"…","a":"…"}]' | python3 tools/faq_gen.py -
```
Paste each block into the page, then confirm with `python3 tools/qa_check.py`. The tool
formats claim-safe answers you supply — it does not invent numbers/claims.
