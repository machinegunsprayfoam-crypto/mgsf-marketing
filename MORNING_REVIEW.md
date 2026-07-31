# ☀️ Morning Review — session digest

_Updated 2026-07-31 · through Pass 195 + interactive work · per-pass detail in NIGHT_LOG.md_
_Branch: `claude/klyfton-ai-problems-ynhx9f`. **Major change since last review: 6 PRs were MERGED to main** — the apps are now on their newest code and redeploying. New overnight work still stages on the branch._

**TL;DR:** Two big things went from "staged" to **shipped + live** tonight: (1) **website lead capture** (quote form → HubSpot) and (2) the **Klyfton app upgrade** — 5 new modules + **persistent semantic memory that now actually works** (verified live: it recalls the right fact by meaning). The **one blocker left is DNS** — `machinegunsprayfoam.com` still points at a parking page, so the public site isn't live on your real domain yet. Reminder set for **Mon Aug 3, ~5 PM MT** to do it together.

---

## ✅ Shipped this session (merged to main + live on the Vercel URLs)

### Website lead capture — the money funnel (was a dead end)
- The old quote form only opened a text on the visitor's phone (silently lost on desktop; **never reached your CRM**). It now **POSTs to `/api/intake` → creates a real HubSpot lead** (name, phone, **optional email**, job details), tagged as a web lead, dedup-safe. Endpoint verified `configured:true`.
- Klyfton's lead-scoring already sorts these hot-first on the call list.

### Klyfton app (mgsf-field-os) — 5 new modules (PR #73)
- **orchestrator** (verify-and-correct loop), **provider hub** (Claude + ChatGPT/Grok/etc. w/ fallback), **lead-score** (wired into the HubSpot call list), **health** (the "Mechanic" self-check `/api/health`), **redact** (secret/PII guardrail on the hive).

### Persistent memory — now genuinely working (PRs #72, #75 + Supabase)
- Applied the pgvector schema in Supabase, **backfilled all 32 existing notes (32/32 embedded)**, and **verified semantic recall live** — a query worded differently from the stored note still pulls the right fact (proved it on your 1099/crew-classification notes).
- Fixed the status check so it can never again report "memory on" when the schema is actually missing.

### Hardening + hygiene
- **Security headers** added to the marketing site (had none).
- **og:image dimensions** on all 37 pages (correct social link previews).
- **Test gate: 19 suites / 434 checks** (added decision-logic coverage for dew-point, blower-door, ROI, roof/wall takeoff, the budget throttle, and memory).
- New durable skills so I stop re-learning things: **session-planner**, **tool-bag** (fixes the "I forgot Zapier could do that" problem). Living docs: `GAP_AUDIT.md`, `TASK_PLANNER.md`, `FIRE_SCHEDULE.md`.

_The marketing site rebuild (dark tactical theme, `.com` copy deck, roofing sub-cluster, 10 city pages, SEO/QA all clean) shipped in earlier passes and is now merged/live too — full history in NIGHT_LOG.md._

---

## 🔴 Needs YOU (priority order)

1. **DNS go-live — the #1 blocker.** `machinegunsprayfoam.com` resolves to a **parking IP (208.91.197.27), not Vercel** — the public .com shows a parking page. Everything works at `mgsf-marketing.vercel.app` / `mgsf-fieldos.vercel.app`, but customers on your real domain don't see it. Fix: mgsf-marketing Vercel project → Settings → Domains → add the shown A/CNAME records at your registrar. **Reminder set Mon Aug 3, ~5 PM MT** — I'll pull the exact records for you.
2. **Test lead** (after DNS): submit the live quote form once; I'll confirm it lands in HubSpot (verifies the token's write scope — the last unknown in the pipeline).
3. **Env switches** (field-os Vercel, exact names): **`CREW_CODE`** ⚠️ — currently unset, so data endpoints are likely **public**; set it to gate them. Then `ALERTS_WEBHOOK_URL` (arms), `KLYFTON_MONTHLY_BUDGET_USD` (spend cap), `GOOGLE_MAPS_API_KEY`, Twilio (missed-call text-back).
4. **HubSpot cleanup:** 263 of 333 contacts are unowned (a dead July-9 import). Tell me **`assign`** (to you) or **`archive`** and I'll run it.
5. **Repo hygiene:** `main` is unprotected on both repos; 20 stale `copilot/*` branches + draft PRs #71/#74 to triage. Say **`prune`** and I'll return the safe delete list.
6. **GitGuardian incident** — the historical test-fixture false-positive; clear it in the dashboard (no code fix needed).

## 🟡 Info only you can give me (I won't fabricate it)
- **Contractor registration #** → adds a "Registered Montana Contractor #___" credential.
- **North Dakota phone number** → I'll wire it into the ND city pages like WY/SD.
- **Real Google reviews** → none on the site (won't invent). The `g.page` review link is left untouched as flagged.
- **Attorney review** of Privacy + Terms. · **Job photos** → for a real gallery (pages currently share the hero).

## 🟢 One decision for you
- **Title tags:** 37 pages have `<title>`s over ~60 chars (Google truncates the tail). Say the word and I'll trim them keeping the front-loaded keywords.

---

_Reference on the branch: `NIGHT_LOG.md` (per-pass detail) · `GAP_AUDIT.md` · `TASK_PLANNER.md` · `FIRE_SCHEDULE.md` · `GO_LIVE.md`._
