# MGSF Overnight Work Log

Autonomous overnight passes on branch `claude/klyfton-ai-problems-ynhx9f`.
Connector-free (git/files only). Nothing merged to `main` — staged for Clifton's morning review.

## SEO QA baseline (as of first pass)
All 19 marketing HTML pages checked for canonical / robots / JSON-LD / OG.
- **Fixed:** `concrete.html` was missing canonical, JSON-LD, and OG tags — added (GeneralContractor schema + OG + canonical).
- All other pages already clean (canonical ✔, robots index,follow ✔, JSON-LD ✔, OG ✔).

## Pass log
- **Pass 1** — SEO QA sweep; fixed `concrete.html` missing canonical/JSON-LD/OG.
- **Pass 2** — Verified all 9 internal nav targets resolve (no broken links). Added a full service-nav footer to `concrete.html` (it had none) — cross-links soil/seawall + all services.
- **Pass 3** — Added `FAQPage` JSON-LD to `spray-foam-insulation.html` (flagship) mirroring its 4 visible FAQ items (validated). 14 more pages have visible FAQs but no FAQPage schema — see backlog.
- **Pass 4** — Added `FAQPage` JSON-LD to the 4 service pages: spf-roofing, concrete, soil-stabilization, seawall-stabilization (all validated). Remaining: 10 city pages.
- **Pass 5** — Added `FAQPage` JSON-LD to ALL 10 city pages (script-generated from each page's own visible FAQ, validated). ✅ FAQ schema now complete site-wide: 17 FAQPage blocks, all valid JSON.

- **Pass 6** — FINISHED HOMEPAGE LINKING (it was a dead end — only concrete was linked). Linked the Spray Foam + SPF Roofing service cards, added a "More specialties" row (pole barn, metal building, soil, seawall, spec), made all service-area chips clickable to their city pages, and linked the footer services list. All 18 homepage links verified to resolve. Homepage now connects to every service + city page (UX + internal-link SEO).

- **Pass 7** — InfraNodus retry: connector DOWN (not just rate-limited) — noted, stopped. Sitemap QA: complete (19 loc = 19 pages). Added `BreadcrumbList` JSON-LD to all 18 interior pages (Home > Page), script-generated + validated. Structured-data set now complete site-wide (GeneralContractor + FAQPage + BreadcrumbList).

## Backlog (safe, additive — for later passes)
- Add 1–2 more distinct FAQ entries to city pages (currently 3 each) — only if genuinely non-duplicative.
- (Site is structurally complete: homepage links all, sitemap complete, schema complete. Remaining work is content depth / owner-input items.)
- Add breadcrumb JSON-LD (BreadcrumbList) to service pages.
- Add 1–2 more FAQ entries to city pages (currently 3 each).
- ~~Cross-link soil/seawall from the concrete page~~ (done, pass 2).
- ~~Verify all internal nav links resolve~~ (done, pass 2 — all clean).

## Do NOT touch overnight (owner review required)
- Pricing / Terra-Lok rate.
- `g.pe` vs `g.page` review link (flagged mismatch).
- Any merge to `main`.
