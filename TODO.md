# MGSF — What's Left (to-do)

_As of 2026-07-30, Pass 169. Branch `claude/klyfton-ai-problems-ynhx9f`, both repos. Nothing merged to
main. Site is now **`.com`**, one **dark tactical (scarlet & gold)** theme, 40 pages, QA-clean._

## 🔴 Needs YOU — authorize a login (the money moves)
- [ ] **Twilio** → turns speed-to-lead (missed-call text-back) fully live. #1 ROI; code built + tested (`GO_LIVE.md`).
- [ ] **Cloudinary** → so I can build the **Photo/Video Gallery** page with your real job photos.
- [ ] **Stripe or PayPal** → take deposits/payments on jobs.
- [ ] **QuickBooks** → reconnect the lapsed subscription to resume accounting automation.
- [ ] **Semrush units** (or a free/paid Ahrefs API key) → I pull the full keyword + competitor report.
      _(Per `SEO_FINDINGS.md`: unauthenticated Ahrefs free-DR access was set to end 2026-08-10.)_

## 🔴 Go-live — a decision only you can make
- [ ] **Point `.com` live** — set `www.machinegunsprayfoam.com` as the Vercel primary domain + DNS.
- [ ] **Merge to main** — everything is staged on `claude/klyfton-ai-problems-ynhx9f`; inert until you merge.
- [ ] **`g.pe` → `g.page`** review link — flagged; I won't touch it without your OK.
- [ ] **Set `CREW_CODE`** in Vercel → locks the Klyfton read endpoints + AI to your crew.
- [ ] **`KLYFTON_MONTHLY_BUDGET_USD`** → raise it to take the AI out of battery/throttle mode.

## 🟡 Needs YOU — info only you have
- [ ] **Contractor registration #** (from Talia/ProTax) → I'll add a "Registered Montana Contractor #___" credential.
- [ ] **North Dakota phone number** → I'll wire it into the ND city pages like MT/WY/SD.
- [ ] **Real Google reviews** — paste them; the site shows none (I won't fabricate).
- [ ] **Attorney review** of the Privacy + Terms pages before they go public (both noindex now).
- [ ] **Job photos** → for a real gallery (pages currently share the hero image).
- [ ] **Square favicon** — a 512×512 PNG (+ optional `favicon.ico`). The tab icon currently uses your
      real wide logo (`img/logo-dark.jpg`); a square version renders sharper. Image tooling isn't
      available in the overnight cron.
- [ ] **Hero-photo compression** — the hero JPGs are heavy; needs image tooling I can't run in cron.

## 🟢 One decision for you
- [ ] **Title tags:** 37 pages have `<title>`s over ~60 chars (Google truncates the tail). Say the word
      and I'll trim them, keeping the front-loaded keywords.

## 🟢 I can do — no blockers (just say go)
- [ ] **Local-SEO prep pack** — NAP citation sheet (Google, Bing, Apple, Yelp, Angi, BBB, chamber,
      VOSB/SDVOSB dirs) + a Google Business Profile weekly-post plan. You submit/post.
- [ ] **More content** — additional service detail or blog-style pages if you want them.
- [ ] **Build the gallery page** once Cloudinary + photos are available.

## ✅ Done & staged (for reference — see NIGHT_LOG.md for per-pass detail)
- **`.com` rebuild** in one **dark tactical (USMC scarlet #c8102e + gold #e8a317)** theme, real
  black-background logo, favicon + apple-touch-icon site-wide. (The old light/navy theme and the
  `.net`-vs-`.info` domain question are obsolete — resolved to one dark `.com`.)
- Full copy deck across all core pages + the **Foam Roofing sub-cluster (6 pages)** and the
  **insulation cluster** (Types/Attic/Ice-Dam/Building-Envelope/Strengthens-Walls).
- **Crawl Space Encapsulation** page exists (was the P1 gap in `SEO_GAPS.md` — now built).
- **Internal linking** complete: every page links the Service Areas hub, Contact, and Financing;
  visible breadcrumbs on all 28 sub/service pages; Privacy + Terms in every footer.
- **FAQ + FAQPage schema** on homepage, About, Contact, all roofing subs, Service Areas, and the
  insulation/service pages — schema matches visible text (audited site-wide).
- **SEO/QA clean:** 110 JSON-LD / 0 invalid, 0 broken links, self-referential canonicals + robots,
  sitemap synced (real git `lastmod`), unique titles/meta, 100% alt, HTTPS-only.
- **Insurance** shown as **"Fully Insured"** ($1M GL + MT workers' comp, from your ACORD COI);
  **Financing = Hearth**; **state numbers** MT/WY/SD wired (no ND yet).
- **Tooling:** `tools/qa_check.py` (pre-deploy QA gate) + `tools/sync_sitemap.py` (lastmod sync),
  documented in `tools/README.md`.
- **Field-os:** speed-to-lead hardened + documented (`GO_LIVE.md`); Klyfton brain parses clean.

---
## Recommended order (my pick)
1. **Merge to main** + **point `.com` live** — get the site out.
2. **Twilio** — speed-to-lead (the money leak).
3. **GBP + reviews + citations** — biggest local-SEO lever (DR near 0; see `SEO_FINDINGS.md`).
4. **Cloudinary + job photos** → gallery page.
5. Send me the **contractor reg #** and **ND number** to finish those credentials.
