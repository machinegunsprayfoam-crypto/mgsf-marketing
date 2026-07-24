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
- **Pass 8** — Fixed homepage og:image + schema image from relative (`img/foam-hero.jpg`) to absolute URL (relative paths break social/scraper previews). All other pages already absolute. Pricing + review link left untouched (owner-hold).
- **Pass 9** — Added Twitter/X Card meta (summary_large_image + title/description/image from OG) to all 19 pages so links render a large-image preview on X. Caught + fixed a script bug in the same pass (missing `>` on og:image / stray `>` after twitter:image) — all tags well-formed, JSON-LD re-validated.
- **Pass 10** — Read-only full QA sweep: all 19 pages pass (canonical 1, robots index 1, og:image 1, twitter:card 1, JSON-LD all valid); git tree clean. Site is structurally complete — **idling** further passes to avoid low-value churn. Remaining work is owner-input (Terra-Lok $2,800 confirm, review link g.pe→g.page, merge to main, Search Console) or the InfraNodus mirror (needs a live connected session).

- **Pass 11** — QA re-verify (read-only): all 19 pages pass — canonical 1, robots `content="index, follow"` 19/19 (note: format has a space after the comma — grep `index,follow` gives a false 0), JSON-LD valid (service/city = GeneralContractor+FAQPage+BreadcrumbList; index = GeneralContractor only, no self-breadcrumb — correct; spec = GeneralContractor+BreadcrumbList, no FAQ by design). Site structurally complete. **Idling** — remaining marketing work is either owner-gated (pricing, g.pe→g.page, merge, Search Console) or net-new pages (crawl-space encapsulation P1 per SEO_GAPS.md — bigger than a bounded safe fire). Brain being actively edited by owner this session — NOT touching it overnight to avoid conflict.

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

- **Pass 12** — Internal-linking fix: concrete.html was the only interior page with no home link in its nav (home:0 vs home:1 everywhere else). Added a "Home" link (`/`) matching sibling nav style. All 18 interior pages now link home. (Noted for owner: 6 service pages lack a "Free Estimate" CTA that city pages have — SEO_GAPS P2, left for review.)

- **Pass 13** — CTA consistency: seawall + soil closing CTAs said "Get a [service] assessment" while sibling service pages say "Get a *free* [service] assessment." Added "free" to both to match the site pattern (free assessment is MGSF's established offer across 14 pages). spec page left as-is (builder/spec audience, intentionally different). SEO_GAPS P2 now effectively closed — all homeowner-facing pages carry a free-offer CTA.

- **Pass 14** — QA: verified meta descriptions present on all 19 pages (162–266 chars). Note: ~12 exceed Google's ~160-char SERP display cap (will truncate) — a possible future trim, but NOT churned tonight (rewriting good copy risks altering claims/voice for marginal gain). Site remains structurally complete; **idling**. Remaining = owner-gated (pricing, g.pe→g.page, merge, Search Console) or net-new pages (crawl-space P1).
