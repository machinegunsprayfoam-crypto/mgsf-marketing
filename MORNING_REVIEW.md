# ☀️ Morning Review — overnight work digest

_Branch: `claude/klyfton-ai-problems-ynhx9f` (both repos) · nothing merged to main · per-pass detail in NIGHT_LOG.md · through Pass 91_

**TL;DR:** The `.net` site is now a full, better-than-`.info` site — 32 pages, every SEO/QA dimension
clean, all topic clusters interlinked. New this stretch: a market scan of AI tools, an audit of every
connection you have, and the speed-to-lead system hardened + documented. A handful of high-value items
need a login or a decision **only you have** — those are the money moves.

---

## ✅ Done & staged (review, then merge when ready)

### Marketing (`mgsf-marketing`) — now 32 pages
- **Domain locked to `.net`** (this repo = the improved copy; ProFoam's `.info` stays put). All
  canonicals/og/sitemap/schema on `www.machinegunsprayfoam.net`.
- **Branded email everywhere** — `clifton@machinegunsprayfoam.info` (killed the old Gmail).
- **New pages built** (from your `.info` screenshots + net-new): **About, Contact** (with a working
  tap-to-text quote form), **Coatings, Financing** (your real Hearth widget), **Privacy, Terms**
  (noindex), plus the insulation cluster — **Types of Spray Foam, Attic, Ice Dam Prevention, Building
  Envelope, Spray Foam Strengthens Walls**.
- **Fully interlinked:** insulation cluster (9 pages), concrete family, and all **10 city pages
  cross-linked** ("nearby service areas"). 0 orphans, 0 broken links.
- **SEO/QA clean:** 32 pages, self-referential canonicals + robots correct, **85 JSON-LD blocks / 0
  invalid**, FAQ schema matches visible text on every page, robots.txt + sitemap consistent
  (29 indexable; privacy/terms correctly noindex/excluded), meta descriptions in SERP length.
- Fixed the two `.info` bugs on `.net`: correct click-to-call phone everywhere; branded email.
  **Did NOT** copy `.info`'s "dangerous mold" health claim (barred).

### Field-os (`mgsf-field-os`)
- **AI market scan** → `AI_MARKET_SCAN.md`: the one gap costing money is **speed-to-lead**; almost
  everything else you already own (see below).
- **Connections audit** → `CONNECTIONS.md`: every integration this session reaches, what it does, and
  which need you to authorize them.
- **Speed-to-lead hardened:** `api/missed-call.js` (already built) now has a 24-check regression test,
  is in the gate, and has Twilio wiring steps in `GO_LIVE.md`. Test gate: **5 suites, 124 checks green.**

---

## 🔴 The money moves — need YOU to authorize a login (~10 min each)
1. **Twilio** → turns speed-to-lead fully live (missed-call text-back). #1 ROI; code is built + tested.
   Steps in `GO_LIVE.md` (`ALERTS_WEBHOOK_URL` + point Twilio's no-answer at `/api/missed-call?event=1`).
2. **Cloudinary** → lets me build the Photo/Video Gallery page with your real job photos.
3. **Stripe or PayPal** → take deposits/payments on jobs.
4. Reconnect **QuickBooks** subscription → accounting automation resumes.

## 🟡 Needs your decision
5. **Merge to main** — both repos are staged; nothing is live until you merge.
6. **`.net` vs `.info` long-term** — two near-identical live sites split Google authority; eventually
   301-redirect one to the other. Your call which.
7. **`g.pe` → `g.page`** review link — flagged; I don't touch it.

## 🟡 Needs something only you have
8. **Real Google reviews** — homepage cards are placeholder (I won't fabricate). Paste real ones.
9. **Attorney review** of the Privacy + Terms pages before they're treated as final (both noindex now).
10. **Rebates page** — needs the real current MT/ND/SD/WY utility/rebate programs (won't invent them).
11. **Business hours, favicon, hero-photo compression** — hours confirm; logo file; image tooling
    (compression isn't runnable in the overnight cron).

## 🔵 Bigger build — waiting on you
12. **Old-theme redesign rollout** — the newest pages use the modern light theme; the older service +
    city pages are still the dark theme. Say the word and I convert them to match.

---
_This digest summarizes NIGHT_LOG.md (91 passes). Not merged to main._
