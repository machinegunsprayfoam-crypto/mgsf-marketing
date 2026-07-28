# ☀️ Morning Review — overnight work digest

_Branch: `claude/klyfton-ai-problems-ynhx9f` (both repos) · nothing merged to main · per-pass detail in NIGHT_LOG.md · current through Pass 124_

**TL;DR:** The marketing site is fully rebuilt for **`.com`** in your **dark tactical, USMC scarlet & gold**
look (no navy), with your real black-background logo on the header. All the new `.com` copy-deck pages are
built, the whole Foam Roofing sub-cluster exists, and every SEO/QA dimension is verified clean. Everything is
**staged, not merged** — review and merge when ready. What's left are decisions and logins **only you can do**.

---

## ✅ Done & staged (review, then merge when ready)

### The look — dark tactical, scarlet & gold (your call, no navy)
- Whole site (40 pages) converted to one **dark charcoal + USMC scarlet (#c8102e) + gold (#e8a317)** theme —
  previously a mix of navy-blue and light pages.
- Your **black-background logo** (`img/logo-dark.jpg`) on a black header, blended clean — no white box.
- Trust line standardized to **"Certified & Fully Insured."**

### Content — the `.com` copy deck is fully built
- **Domain = `.com`** everywhere (canonical/OG/sitemap/schema on `www.machinegunsprayfoam.com`); branded email
  `clifton@machinegunsprayfoam.info` throughout (not the deck's gmail).
- Deck copy dropped into all **core pages**: Home, About, Insulation pillar, Foam Roofing pillar, Concrete,
  Coatings, Financing, Contact, Service Areas.
- **Foam Roofing sub-cluster (6 pages)** built + interlinked: SPF Roof Benefits, SPF Roof Coatings, Cool Roofs,
  Seamless Systems, Sustainability, Wind Uplift Resistance — each with FAQ.
- **Service Areas hub** + all 10 city pages; **Rebates** page (real cited programs, no fabricated $; the federal
  25C credit correctly shown as ENDED 12/31/2025).
- **State phone numbers** wired: MT 406-939-8301 · WY 307-296-0625 · SD 605-349-2884 (all route to your AI
  receptionist). **No ND number yet.**
- **Insurance verified** from your ACORD COI: $1M general liability (Midvale, via Stockman) + Montana workers'
  comp → shown as **"Fully Insured."** "Licensed" dropped — Montana doesn't license this trade (your call).
- **Financing = Hearth** (live widget on Financing + $0-down blocks).

### SEO / QA — clean across the board
- **108 JSON-LD blocks / 0 invalid, 0 broken links, 0 orphan pages.**
- Self-referential canonicals + `index,follow` robots (privacy/terms/404 correctly noindex/excluded).
- Sitemap complete (37 indexable = 37 `<loc>`) with accurate per-page `lastmod` (real git dates).
- FAQ + FAQPage schema on homepage, all 6 roofing sub-pages, and Service Areas — schema matches visible text.
- Breadcrumb JSON-LD on every sub-page; exactly one H1 per page; 100% image alt-text; meta descriptions ≤160
  and all unique; all titles unique; OG/Twitter complete; HTTPS-only; viewport on every page.

---

## 🔴 Go-live — needs YOU (site is ready; these are the switches)
1. **Point `.com` live** — set `www.machinegunsprayfoam.com` as the **Vercel primary domain + DNS**.
2. **Merge the branch to main** — everything is on `claude/klyfton-ai-problems-ynhx9f`; nothing merged overnight
   per your rule. Review the diff, then merge.

## 🔴 Money-move logins (unlock features when you authorize — ~10 min each)
- **Twilio** → speed-to-lead fully live (missed-call text-back; code built + tested, steps in `GO_LIVE.md`). #1 ROI.
- **Cloudinary** → real job-photo / before-after gallery page.
- **Stripe or PayPal** → take deposits/payments.
- **Reconnect QuickBooks** → accounting automation resumes.

## 🟡 Info only you can give me (I won't fabricate it)
- **Contractor registration #** (Talia/ProTax) → adds a "Registered Montana Contractor #___" credential.
- **North Dakota phone number** → I'll wire it into the ND city pages like WY/SD.
- **Real Google reviews** → none on the site (won't invent). The g.page review link is left untouched as flagged.
- **Attorney review** of Privacy + Terms.
- **Job photos** → for a real gallery (pages currently share the hero image).

## 🟢 One decision for you
- **Title tags:** 37 pages have `<title>`s over ~60 chars (Google truncates the tail, usually the brand suffix).
  Mass-rewrite is your call — say the word and I'll trim them keeping the front-loaded keywords.

---

## Field-os (`mgsf-field-os`)
- Klyfton brain (`api/klyfton.js`) parses clean, no typos/doubled words. Speed-to-lead (`api/missed-call.js`)
  hardened + regression-tested; Twilio wiring in `GO_LIVE.md` (needs your Twilio auth to go live).

_Reference docs on the branch: NIGHT_LOG.md (per-pass detail) · AI_MARKET_SCAN.md · CONNECTIONS.md · GO_LIVE.md ·
SEO_FINDINGS.md · TODO.md. Not merged to main._
