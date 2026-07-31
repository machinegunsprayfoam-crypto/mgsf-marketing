# MGSF Fire Schedule — one bounded task per cron fire

An **ordered** queue of pre-vetted, cron-safe (local, no-connector) tasks so each overnight
fire pulls the *next* one instead of choosing ad hoc. Companion to `TASK_PLANNER.md` (full
queue incl. owner-gated) and `NIGHT_LOG.md` (history). Governed by `mgsf-session-planner` +
`mgsf-overnight-ops`.

## Per-fire protocol
1. Read this file; take the **first unchecked `[ ]`** item.
2. **Verify it's still needed** (each item lists a check). If already satisfied → mark `[~]`
   N/A with a one-line note and take the next item.
3. Do that ONE item only. Keep existing style/CSS. Never fabricate; doctrine/mgsf-core wins.
4. Verify it parses / the gate is CLEAN (`bash tools/verify_all.sh`; field-os: `node -c` +
   `node tests/run-all.js`).
5. Commit (author "Machine Gun Spray Foam"), push the branch, check the box `[x]`, and add a
   2–3 line NIGHT_LOG entry. **Do not merge to main.**
6. If every item is `[x]`/`[~]` → **idle honestly** until an interactive session refills this.

Task-ordered, not calendar-dated — Sunday-agnostic (a fire that lands on a Sunday still only
does repo work; it never schedules business work/meetings/reminders).

---

## Queue (highest value first)

- [ ] **Fire 1 — Security headers in `vercel.json`** (marketing). Add a `headers` block:
  `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`,
  `X-Frame-Options: SAMEORIGIN`, `Permissions-Policy: camera=(), microphone=(), geolocation=()`.
  *Why:* real, safe hardening; site has none today. *Check needed:* `grep headers vercel.json`
  → absent. *Done:* valid JSON (`node -e "JSON.parse(require('fs').readFileSync('vercel.json'))"`),
  cleanUrls/existing config preserved, gate clean.

- [ ] **Fire 2 — `og:image:width` + `og:image:height`** on all indexable pages. Read the
  **real** pixel dimensions of the og:image asset (`file`/`identify` on the file in `img/`),
  never guess. *Why:* faster, correct social link previews. *Check needed:* `grep -L
  og:image:width` → missing. *Done:* dims equal the actual file; gate clean.

- [ ] **Fire 3 — Lazy-load below-the-fold images.** Add `loading="lazy" decoding="async"` to
  `<img>` that are NOT the hero/first image on each page (never lazy the hero). *Why:* only
  5/40 pages lazy-load. *Check needed:* per-page first `<img>` left eager. *Done:* hero
  untouched; others lazy; gate clean.

- [ ] **Fire 4 — Explicit `width`/`height` on `<img>` lacking them.** *Why:* cuts layout
  shift (CLS). *Check needed:* `grep '<img'` without both attrs. *Done:* dims from the real
  files; no visual change; gate clean.

- [ ] **Fire 5 — `aria-label` on icon-only links** (e.g. the ✉ / ☎ header links whose text
  is just a glyph). *Why:* screen-reader a11y. *Check needed:* icon links with no accessible
  name. *Done:* labels added; no visual change; gate clean.

- [ ] **Fire 6 — field-os: deepen tests for a thin pure module** (e.g. `dew-point` /
  `measure` edge cases beyond calc-invariants). *Why:* safety-relevant math regression net.
  *Check needed:* module's edge cases uncovered. *Done:* new tests green; `run-all.js` green.

- [ ] **Fire 7 — field-os: clarify ONE Klyfton brain/DOCTRINE block** for readability (no new
  claims, no number changes). *Why:* maintainability. *Check needed:* a confusing block.
  *Done:* `node -c api/klyfton.js` parses; `doctrine_reconcile.py` still ✓ in sync.

- [ ] **Fire 8 — Add `<link rel="sitemap" type="application/xml" href="/sitemap.xml">`** to
  each page `<head>` (aids some crawlers/tools). *Why:* minor discoverability. *Check
  needed:* absent. *Done:* present on indexable pages; gate clean.

> After Fire 8 the vetted local backlog is exhausted — **idle** and flag for an interactive
> session to (a) refill from `GAP_AUDIT.md` / new needs, or (b) run the owner-gated items in
> `TASK_PLANNER.md`. Do NOT invent padding work to stay busy.
