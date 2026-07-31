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

- [x] **Fire 1 — Security headers in `vercel.json`** ✅ Pass 187 (marketing). Add a `headers` block:
  `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`,
  `X-Frame-Options: SAMEORIGIN`, `Permissions-Policy: camera=(), microphone=(), geolocation=()`.
  *Why:* real, safe hardening; site has none today. *Check needed:* `grep headers vercel.json`
  → absent. *Done:* valid JSON (`node -e "JSON.parse(require('fs').readFileSync('vercel.json'))"`),
  cleanUrls/existing config preserved, gate clean.

- [x] **Fire 2 — `og:image:width` + `og:image:height`** ✅ Pass 188 on all indexable pages. Read the
  **real** pixel dimensions of the og:image asset (`file`/`identify` on the file in `img/`),
  never guess. *Why:* faster, correct social link previews. *Check needed:* `grep -L
  og:image:width` → missing. *Done:* dims equal the actual file; gate clean.

- [~] **Fire 3 — Lazy-load below-the-fold images.** N/A (Pass 189) — already done: all below-fold gallery imgs have `loading="lazy" decoding="async"`; the only eager imgs are heroes (`fetchpriority="high"` LCP) + logo, which must stay eager. Add `loading="lazy" decoding="async"` to
  `<img>` that are NOT the hero/first image on each page (never lazy the hero). *Why:* only
  5/40 pages lazy-load. *Check needed:* per-page first `<img>` left eager. *Done:* hero
  untouched; others lazy; gate clean.

- [~] **Fire 4 — Explicit `width`/`height` on `<img>` lacking them.** N/A (Pass 189) — audited: 0 imgs missing width/height. *Why:* cuts layout
  shift (CLS). *Check needed:* `grep '<img'` without both attrs. *Done:* dims from the real
  files; no visual change; gate clean.

- [~] **Fire 5 — `aria-label` on icon-only links** N/A (Pass 189) — audited: 0 icon-only links; all icon links (📞/✉/📍) carry visible text, and the nav toggle already has aria-label. (e.g. the ✉ / ☎ header links whose text
  is just a glyph). *Why:* screen-reader a11y. *Check needed:* icon links with no accessible
  name. *Done:* labels added; no visual change; gate clean.

- [x] **Fire 6 — field-os: deepen tests for a thin pure module** ✅ Pass 189 (dew-point spray-safety flag + margin; +18 checks) (e.g. `dew-point` /
  `measure` edge cases beyond calc-invariants). *Why:* safety-relevant math regression net.
  *Check needed:* module's edge cases uncovered. *Done:* new tests green; `run-all.js` green.

- [x] **Fire 7 — field-os: clarify ONE Klyfton brain/DOCTRINE block** ✅ Pass 190 (GraphRAG assembly comments; no logic/number change) for readability (no new
  claims, no number changes). *Why:* maintainability. *Check needed:* a confusing block.
  *Done:* `node -c api/klyfton.js` parses; `doctrine_reconcile.py` still ✓ in sync.

- [~] **Fire 8 — Add `<link rel="sitemap" type="application/xml" href="/sitemap.xml">`** N/A (Pass 191) — SKIPPED as padding: `robots.txt` already declares the sitemap via the authoritative `Sitemap:` directive (what Google/Bing actually read); the `<link rel="sitemap">` head tag is ignored by major search engines. Touching 40 pages for ~zero value violates the no-padding rule. to
  each page `<head>` (aids some crawlers/tools). *Why:* minor discoverability. *Check
  needed:* absent. *Done:* present on indexable pages; gate clean.

- [x] **Fire 9 — field-os: cover bpi-calc decision/formula logic** ✅ Pass 192 (tightness bands + ASHRAE 62.2 target + conversions; +19 checks). Found by re-checking: calc-invariants tested only the ACH50 identity, not the customer-facing decision logic — a real gap, not padding.

**Decision-logic test track (verify-needed each fire — only add if genuinely uncovered):**
- [x] `roi.js` — ✅ Pass 193: covered the financing cash-flow decision + clamps (+21 checks). calc-invariants had only the identities.
- [ ] `measure.js` — takeoff/measurement edge cases (check coverage first).
- Rule: read the module + its calc-invariants coverage; add a suite ONLY if decision/formula
  logic is uncovered (like dew-point Fire 6 / bpi-calc Fire 9). If already covered → N/A, idle.

> When the above are done/N-A the vetted local backlog is exhausted — **idle** and flag for an
> interactive session to (a) refill from `GAP_AUDIT.md` / new needs, or (b) run the owner-gated
> items in `TASK_PLANNER.md`. Do NOT invent padding work to stay busy.
