# ☀️ Morning Review — session digest

_Updated 2026-08-07 · through Pass 244 + the 8/7 council/cube session · per-pass detail in NIGHT_LOG.md_
_Branch: `claude/klyfton-ai-problems-ynhx9f`. Overnight work stages here; **PR #78 was merged to `main` this session** so the Klyfton app is live on production with all the new code._

**TL;DR:** The Klyfton app is **built, merged, and running in production** (verified via `/api/boot`). It's **one Vercel setting away from a live crew login**: `CREW_CODE` is set but **not in the Production environment scope**, so the access gate still reads dark. I confirmed it's **not a code bug** — the gate reads `CREW_CODE` correctly, so setting it in Production will flip it. Second-biggest unlock is `ALERTS_WEBHOOK_URL` (turns on ~10 tools + all automations). Everything else left is your-side (auth/clicks) or info only you can give.

---

## ✅ Shipped this session (merged to main + live in production)

### Klyfton app — went live (PR #78, production commit verified via `/api/boot`)
- **Customer Portal** (token-gated, allowlist-safe — no cost/margin leak), **Predictive Cost** (regression over your own completed jobs), **estimate→CRM auto-hallway** (saving an estimate creates/advances the lead), **9-cluster brain regen** (150 nodes/1125 edges, 2026-08-01), plus **business-audit / job-workflow / gov-programs** wired into the UI.
- **Crew-code frontend fix** — gated panels now send the stored code correctly (they'd have 401'd once the gate turned on; fixed pre-emptively).
- Production self-map confirms live: portal, predictive-cost, business-audit, gov-programs, hive, memory, HubSpot, storage, TTS — all `live:true`.

### Overnight hardening + content (staged on branch)
- **`llms.txt`** added (AI-crawler/answer-engine index — ChatGPT/Perplexity/AI Overviews), built from verified page content.
- **`.env.example` completed + guarded** — every env var the code reads is now documented (was missing 19), with a meta-suite test so the gap can't silently re-open.
- **Radiant-barrier FAQ** on `/cool-roofs` — closed the last open SEO backlog item (P5).
- **Field-os test gate: 88 suites / 1999 checks green.** Wiring guards added across the board (brain↔retriever, router tools, test registry, tool catalog, DB docs, calc wiring, brain-graph 3-file sync, dead-button/nav, env docs).
- `CLAUDE.md` rewritten to drop the dead "Silvr" fiction; marketing SEO/QA fully swept and clean (40 pages, 113 JSON-LD).

---

## 🌙 Tonight — the council/cube build (2026-08-07, field-os, staged on branch, NOT merged)

You drove a big restructure this session, then I kept building while you slept. All on the branch,
gate green end to end (**107 suites / 2621 checks**):

- **Klyfton is now a 6-division "cube" council — 12 → 34 specialists** (was a flat 12-face set). Six
  divisions (Estimating & Takeoff · Field & Production · Sales & Growth · Finance & Admin · Compliance
  & Risk · GovCon & Strategy), each with a **lead (center piece)**; genuinely new coverage (equipment,
  QC, AR/collections, cash-flow, payroll, bookkeeping, contracts/liens, licensing, warranty,
  capability statements, teaming, owner-strategy). Routing is hierarchical and can't drift from the roster.
- **Overlap teams (your Rubik's insight).** The 2-color edges & 3-color corners are cross-functional
  teams that fire in **one turn**: **14 featured plays** (Go/No-Go Bid, Federal Bid Package, Priced-to-Margin,
  Win-Rate, True Takeoff, Book-to-Capacity, Teaming Outreach, …) + an **algorithm that fills all 26 cube
  pieces** so every combination has a capability (`/api/combos`).
- **5 new arms** (send_proposal, request_review, send_payment_link, collections_notice, post_social) —
  still approval-gated, still inert until `ALERTS_WEBHOOK_URL`.
- **New/​hardened**: `api/calendar.js` (.ics generator, hard **no-Sunday** rule) + the GovCon SAM.gov
  lead pipeline is now test-locked (was untested).
- **Visuals** (private Claude artifacts): the 3D **cube brain-map** (`public/cube-map.html`, in-app under
  Command Center → Agents) and the earlier dodecahedron. _The cube artifact's last republish hit a
  transient claude.ai 403; the in-app file is current and will refresh on the next publish._

## 🔴 Needs YOU (priority order)

1. **`CREW_CODE` → Production scope — THE blocker.** It's set but the live app still reads the access gate as dark, so it's saved to the wrong environment (Preview/Dev) or not to Production. Fix: Vercel → mgsf-fieldos → Settings → Environment Variables → confirm the `CREW_CODE` row shows a **`Production`** tag (value `1775`), then redeploy once. Proven **not** a code bug. _Tell me what that row shows and I'll confirm the fix._
2. **`ALERTS_WEBHOOK_URL`** — biggest single unlock (arms + universal bus + all automation crons = ~10 tools). Needs a real URL (Slack/Zapier hook). I can stand one up so it's just a paste.
3. **Authorize Twilio** (claude.ai → Connectors) — turns on SMS / missed-call text-back (speed-to-lead). Also flip **Supabase + InfraNodus** on in-chat for full connector coverage.
4. **Repo consolidation → prune to 3** (you chose this). Archive the 4 dead repos (MGCC, GitHub, html-parsing, setup-assistant) + delete the html-parsing/setup-assistant **Vercel projects**. MGCC + GitHub carry unmerged branches — I can scan them for salvage first; say **`scan`**.
5. **Delete the `copilot/fix-issues` branch** — PR #79 (which leaked `CREW_CODE=1775` into `.env.example` on the public repo) is closed; the branch delete was classifier-blocked for me. GitHub → Branches → trash icon.
6. **Point `www.machinegunsprayfoam.info`** — currently unconfigured. Recommended: redirect it to the marketing site `www.machinegunsprayfoam.com`. ~2-min Vercel domain add (steps ready).
7. **Verify `.com` DNS** — as of 7/31 `machinegunsprayfoam.com` pointed at a parking IP; **not re-checked this session** (cron has no connectors). Confirm it resolves to Vercel before relying on the public domain.

## 🟡 Info only you can give me (I won't fabricate it)
- **Pricing reconcile** — the Drive 7/15 equipment-cost xlsx is higher than doctrine; flagged, untouched. Say the word to reconcile.
- **Contractor registration #** · **North Dakota phone #** · **Real Google reviews** (none on site; won't invent; `g.page` link untouched) · **Business hours** (only index publishes them) · **Attorney review** of Privacy/Terms · **Real job photos** + logo/hero image optimization (image-heavy pages).

## 🟢 Decisions waiting on you
- ✅ **Merged to main (#93, #94, #95) — LIVE.** The council/cube build + the 8/5 doctrine reconcile
  (R-values 7.0/3.8/6.3, coating mil-spec, measured-yield loop, consensus UI) are deployed. Gate 110/2673.
- **PRICING / DOCTRINE decisions (owner-only — flagged, not touched):**
  1. **Roofing product: NCFI 10-011 (R-6.3, 25 psi) vs 10-016 (R-6.7, 58 psi walkable)** — sets the
     roofing R-value AND whether the roof takes foot traffic. Roofing R stays UNCONFIRMED until you pick.
  2. **Confirm set invoice prices** (closed ~$4,124, roofing ~$2,550 are back-calculated — one invoice each locks it).
  3. **Concrete-lifting $10/lb sell rate** prices a 600 SF driveway ~45% light vs the $12/SF market check.
  4. **Thermal-barrier (DC315) coating has no price** — bid lists it as an exclusion, so every job needing one is a change order. Price it.
  5. **Manual Drive step:** rename + move `..._Estimating_Workbook_V2.xlsx` into 16_ARCHIVE (connector can't move/rename).
- **Consensus keys** — the 🤝 Consensus card is live in Owner Tools; needs ≥2 free AI provider keys in Vercel to fan out.
- **`ALERTS_WEBHOOK_URL`** — still the biggest functional unlock (all 12 arms + automations).
- **Title tags** — several `<title>`s exceed ~60 chars (Google truncates); say the word and I'll trim keeping front-loaded keywords.

---

_Reference on the branch: `NIGHT_LOG.md` (per-pass detail) · `SEO_GAPS.md` · `GAP_AUDIT.md` · `TASK_PLANNER.md` · `GO_LIVE.md`._
