# MGSF Overnight Work Log

Autonomous overnight passes on branch `claude/klyfton-ai-problems-ynhx9f`.
Connector-free (git/files only). Nothing merged to `main` — staged for Clifton's morning review.

## SEO QA baseline (as of first pass)
All 19 marketing HTML pages checked for canonical / robots / JSON-LD / OG.
- **Fixed:** `concrete.html` was missing canonical, JSON-LD, and OG tags — added (GeneralContractor schema + OG + canonical).
- All other pages already clean (canonical ✔, robots index,follow ✔, JSON-LD ✔, OG ✔).

## Pass log
- **Pass 1** — SEO QA sweep; fixed `concrete.html` missing canonical/JSON-LD/OG.

## Backlog (safe, additive — for later passes)
- Add breadcrumb JSON-LD (BreadcrumbList) to service pages.
- Add 1–2 more FAQ entries to city pages (currently 3 each).
- Cross-link soil/seawall from the concrete page body.
- Verify all internal nav links resolve to real files.

## Do NOT touch overnight (owner review required)
- Pricing / Terra-Lok rate.
- `g.pe` vs `g.page` review link (flagged mismatch).
- Any merge to `main`.
