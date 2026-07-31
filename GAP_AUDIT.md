# MGSF Cross-App Gap Audit

**Generated:** 2026-07-31 · **Refreshed:** 2026-07-31 (interactive, live data — post-merge) · **Owner:** Clifton
**Scope:** HubSpot, GitHub (mgsf-field-os + mgsf-marketing), Klyfton app, connected apps.

> **How this was produced & why it's not a cron job:** the findings below come from
> *live* HubSpot + GitHub + Vercel data, which requires MCP connectors. Overnight cron
> sessions have **no connectors**, so this audit can only be refreshed from an interactive
> session — not autonomously overnight. Re-run the same checks in a live session to update.
>
> **What changed on this refresh:** PRs **#72, #73, #75 merged** (memory persistence, 5 new
> modules, honest memory status) — field-os is on newest code. Only **2 stale draft PRs**
> (#71, #74) remain open. Exact branch cleanup list is now in **`PRUNE_LIST.md`** (say `prune`).
> HubSpot counts **unchanged** (333 / 70 owned / 8 deals / 0 web leads — expected, DNS not live).

---

## 1. HubSpot — data & pipeline gaps

| Metric | Value | Read |
|---|---|---|
| Contacts | **333** | Bulk-loaded 2026-07-09 (single import) |
| — with email | 328 / 333 | ✅ good coverage |
| — with an **owner** | **70 / 333** | ⚠️ **263 (79%) unassigned — nobody working them** |
| Deals | **8** | ✅ real pipeline, syncing from **Jobber** (deal names carry Jobber #s) |
| Example deal | Sam Durham — Spray Foam, **$15,089**, `contractsent`, 90% | active, owned |
| Web-form intake | **live** (`/api/intake` → `configured:true`) | 0 leads captured yet (just went live today) |

**Gaps**
- **263 orphan contacts** — the July-9 import is mostly **UNQUALIFIED, unworked, unassigned**. It's noise on the call list, not a worked pipeline.
- **No lead-source diversity** — every contact is `OFFLINE / INTERNAL_PROCESSING` (the import). The website has never produced a tracked lead (now fixable — intake is live).
- **Web-form contacts will have no email** (the form collects name+phone only) — fine for calling, but you can't email them a proposal. Consider adding an optional email field to the quote form.

**Owner actions (need your rule — CRM changes are consequential):**
1. Decide the 263 orphans: **assign to you** (so they're worked) or **archive the dead UNQUALIFIED ones** (so the call list is real leads). Tell me the rule and I'll execute in a live session.
2. Optional: add an email field to the website quote form (I can do this on the branch).

---

## 2. GitHub — repo hygiene gaps

**mgsf-field-os**
- ⚠️ **`main` is UNPROTECTED** — direct pushes and force-pushes to the production branch are allowed.
- ⚠️ **25 branches; 21 are deletable clutter** (18 dead `copilot/*` experiments + 3 already-merged branches). Exact list + delete commands in **`PRUNE_LIST.md`**.
- **2 open PRs left (both stale drafts):**
  - **#74** — "Resolving issues in the project" — draft, stale (07-31). Head: `copilot/fix-all-problems`.
  - **#71** — "Restore Vercel cron execution…" — draft, stale (07-24). Head: `copilot/mgsf-field-os-70-fix-vercel-issue`.
  - ✅ **#73, #72, #75 all MERGED 2026-07-31** (5 modules, memory persistence, honest memory status) — the #72-vs-#73 overlap flagged earlier is resolved (both landed cleanly).

**mgsf-marketing**
- ⚠️ **`main` is UNPROTECTED** (same as above).
- 3 branches: `main`, this working branch, and `vercel/install-vercel-web-analytics-5iq6ly` (verify Analytics is live on main, then deletable). PRs #2, #4, #5 merged (lead capture live).

**Owner actions (hard-to-undo — need your OK on the list):**
1. **Protect `main`** on both repos (require PR before merge). Do it in GitHub → Settings → Branches (no MCP tool for this; ~2 min each).
2. **Prune the 21 stale/merged field-os branches** — full verified list ready in `PRUNE_LIST.md`; say **`prune`** and I delete the SAFE set (keeps the 2 branches backing open drafts).
3. **Triage the 2 stale drafts** (#71, #74): close if superseded → their branches then join the safe-delete set.

---

## 3. Klyfton app + environment gaps

| Subsystem | State | Switch to turn on |
|---|---|---|
| Memory (semantic recall) | ✅ **ON — verified live** | pgvector schema applied + 32/32 notes backfilled + semantic recall proven (2026-07-31). Status now honest (`schemaReady` probe). No action needed. |
| Arms (email/SMS/CRM exec) | OFF | `ALERTS_WEBHOOK_URL` |
| ATS (budget throttle) | OFF | `KLYFTON_MONTHLY_BUDGET_USD` |
| Maps / drive-distance | OFF | `GOOGLE_MAPS_API_KEY` (mobilization math works keyless) |
| CREW_CODE (data-endpoint gate) | likely unset | `CREW_CODE` (else data endpoints are public) |

These are owner-gated env switches + a redeploy. `/api/health` (the Mechanic) reports them live.

---

## 4. Connected apps — coverage gaps

- **Google Ads NOT connected** (Windsor sees Meta/Facebook only) → paid *search* intent is dark.
- **Slack = only `#general`** → no `#leads` / `#alerts` / `#field` for Klyfton to post to.
- **Twilio unauthed** → missed-call-recovery texts off.
- **QuickBooks writes blocked** (subscription) → can read P&L/AR, can't push invoices.
- **Connected this refresh:** HubSpot, GitHub, Vercel, Supabase, InfraNodus (InfraNodus hit its 15-min rate cap mid-run — retrying; results land in §5).
- **Need re-auth in connector settings:** PandaDoc, Sentry, Adobe Experience Manager, plus the standing list (Stripe, Twilio, cloudinary…).

---

## 5. InfraNodus topical / SEO gap pass — PENDING (rate-limited)

**Status:** ⏳ **PENDING — InfraNodus account rate-limited (429) across 3 attempts** (2026-07-31). Every call — `analyze_google_search_results` on our 8 core queries + `generate_content_gaps` on the live spray-foam page — hit the shared "requests every 15 minutes" cap and never returned. **Re-run when the quota frees** (a quiet interactive session); the queries and the extracted site corpus are ready to go, so it's a one-shot when the limit lifts.

**What's queued (ready to run):**
- **Market gaps:** `analyze_google_search_results` on — spray foam cost · closed vs open cell · metal-building foam · SPF roof vs replacement · concrete leveling vs mudjacking · is spray foam worth it · spray foam Montana · attic foam problems.
- **Our-content gaps:** `generate_content_gaps` on `mgsf-marketing.vercel.app/spray-foam-insulation` (or feed the extracted 26-page corpus, 753 unique lines).

**Note on scope (unchanged):** InfraNodus is a topical text analyzer, not a CRM hook. The HubSpot corpus is still thin (no web-lead message text yet), so the valuable input is the **site copy + SERP results** (queued above), not HubSpot. When run, replace this section with the actual topical gaps + a short SEO to-do.

---

## Priority order (my picks)

1. **Protect `main`** on both repos — biggest risk, 2 minutes, reversible. *(owner: GitHub UI)*
2. **Resolve #72 vs #73 + prune 22 stale branches** — clears field-os so real work is findable. *(I'll list branches for your OK)*
3. **Work or archive the 263 orphan HubSpot contacts** — turn the dead import into a real call list. *(needs your assign-vs-archive rule)*
4. Turn on Klyfton env switches (memory/arms/maps/CREW_CODE) — owner-gated.
5. Reconnect InfraNodus + let web-leads accumulate before topical analysis.

---

*Living document — refresh from a live (connector-enabled) session; cron cannot regenerate it.*
