# ☀️ Morning Review — overnight work digest

_Branch: `claude/klyfton-ai-problems-ynhx9f` (both repos) · nothing merged to main · full detail in NIGHT_LOG.md_

**TL;DR:** Marketing site is polished and launch-ready on every locally-checkable dimension. Field-os
got a gap analysis, a warranty-cert button, and a doc-accuracy fix. Everything is staged for your OK.
The only build still pending is the **3D brain-graph boot screen** — blocked on the InfraNodus
connector. A few items need a decision or info **only you have**.

---

## ✅ Done & staged (review, then merge when ready)

**Marketing (`mgsf-marketing`) — SEO / performance / QA sweep, Passes 16–56:**
- SEO: every page has unique SERP-length title + meta description, canonical, robots, valid JSON-LD
  (GeneralContractor + FAQPage + BreadcrumbList), OG/Twitter + og:url.
- Content: crawl-space page built; FAQ on all service + city pages (localized); internal links fully
  clustered; homepage FAQ added.
- Performance (Core Web Vitals): hero `preload` + `fetchpriority=high` (LCP), `width/height` on all
  images (CLS), `decoding=async` on below-fold images.
- Discovery: sitemap with `lastmod` + **image sitemap** (23 real job photos w/ captions) → Google Images.
- Mobile/UX: `theme-color`, custom branded **404 page**.
- QA verified clean: 0 broken links, 0 mixed-content, domain + NAP consistency, form labels, H1 order.

**Field-os (`mgsf-field-os`):**
- `FRONTEND_BACKEND_GAP_ANALYSIS.md` — manual front+back gap map (16 of 44 endpoints wired to UI;
  the rest are legit cron/infra/calculators).
- **Warranty certificate** now has a "📄 Certificate" button in Ops→Warranty (was built but unreachable).
- `CLAUDE.md` — flagged the never-built "Silvr" layer so it stops misleading sessions.

---

## 🟡 Needs YOUR decision (≈5 min each)
1. **Merge to main** — everything above is inert until you merge (Vercel deploys from main).
2. **Change-order source of truth** (field-os) — client-side module vs the branded server PDF. Pick one.
3. **`g.pe` → `g.page`** review link — flagged; I don't touch it.

## 🟡 Needs something only YOU have
4. **Real Google reviews** — homepage cards are marked placeholder (I won't fabricate). Paste real ones.
5. **Business hours** — only the homepage publishes hours (`Mo-Sa 08:00-18:00`). Confirm them and I'll
   add `openingHours` schema + a footer hours line to all 20 pages (local-SEO win).
6. **Favicon** — needs your logo file + image tooling (neither available to the overnight cron).
7. **Hero photos are heavy** (0.7–1.7MB) — need compression I can't run in the cron env.
8. **Go-live env vars** (field-os `GO_LIVE.md`) — `ALERTS_WEBHOOK_URL`, `OPENAI_API_KEY`, budget vars.

## 🔵 Bigger build — waiting on you
9. **19-page redesign rollout** — homepage is on the new look; the 9 service + 10 city pages are still
   the old dark theme. Want me to convert **one** page as a proof so you approve the look, then roll the rest?

## ⏸️ Blocked on connector (not cron-doable)
10. **3D brain-graph boot screen** — capture the real InfraNodus knowledge-graph of Klyfton's brain and
    render it as the rotating 3D loader. InfraNodus keeps flapping; ready to run the instant it holds —
    open `/mcp`, confirm it's connected, and tell me "go."

---
_This digest is a convenience summary; NIGHT_LOG.md has the per-pass detail. Not merged to main._
