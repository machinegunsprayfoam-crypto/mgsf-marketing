# MGSF Cross-App Gap Audit

**Generated:** 2026-07-31 (interactive session, live data) · **Owner:** Clifton
**Scope:** HubSpot, GitHub (mgsf-field-os + mgsf-marketing), Klyfton app, connected apps.

> **How this was produced & why it's not a cron job:** the findings below come from
> *live* HubSpot + GitHub + Vercel data, which requires MCP connectors. Overnight cron
> sessions have **no connectors**, so this audit can only be refreshed from an interactive
> session — not autonomously overnight. Re-run the same checks in a live session to update.
>
> **InfraNodus:** requested, but its MCP server is disconnected this session. It is a
> text-network *gap analyzer*, not a CRM integration — it can't "hook into" HubSpot live.
> Its real use is topical: feed it lead-message / deal-note text to surface conversation
> blind spots. See "InfraNodus corpus readiness" below — right now the corpus is too thin
> to be worth running (no web-form lead text yet).

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
- ⚠️ **25 branches, 22 are stale `copilot/*`** experiments (`fix-whatevers-broken`, `have-done-everything`, `fix-all-problems`, `supabase-problems`, …) — dead clutter.
- **4 open PRs:**
  - **#73** — "5 new modules (orchestrator, provider hub, lead-score, health, redact)" — ready, CI green (GitGuardian false-positive aside).
  - **#72** — "Fix semantic memory persistence" — **open, overlaps #73's memory work** → possible conflict; needs a decide-and-close.
  - **#74** — "Resolving issues in the project" — draft, stale.
  - **#71** — "Restore Vercel cron execution…" — draft, stale (last touched 07-24).

**mgsf-marketing**
- ⚠️ **`main` is UNPROTECTED** (same as above).
- Branches clean (main + this working branch + a Vercel analytics branch). PRs #2 and #4 merged.

**Owner actions (hard-to-undo — need your OK on the list):**
1. **Protect `main`** on both repos (require PR before merge). Do it in GitHub → Settings → Branches (no MCP tool for this; ~2 min each).
2. **Prune the 22 stale `copilot/*` branches** — I'll produce the exact delete list for your one-tap OK before removing anything.
3. **Triage the open PRs:** merge/close #73, resolve **#72 vs #73** overlap, close the two stale drafts (#71, #74).

---

## 3. Klyfton app + environment gaps

| Subsystem | State | Switch to turn on |
|---|---|---|
| Memory (semantic recall) | **OFF** | `OPENAI_API_KEY` (exact name — the `open_ai` misnaming is the blocker) + run the pgvector SQL once |
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
- **Disconnected this session** (need re-auth in connector settings): **InfraNodus**, Apollo, Supabase-MCP, plus the standing list (Stripe, PandaDoc, Sentry, cloudinary, Adobe…).

---

## 5. InfraNodus corpus readiness

InfraNodus needs a body of topical text. Right now that corpus is **thin**:
- Web-form lead messages: **none yet** (intake just went live).
- The 333 imported contacts carry **no inquiry text** (bulk import).
- Deals are **Jobber-synced names/refs**, not narrative notes.

**Recommendation:** don't run InfraNodus on HubSpot yet — there's nothing meaningful to analyze. It becomes valuable once real web-form leads accumulate (their "What's going on?" messages) or once won/lost deal notes are captured. When ready, I'll extract a **de-identified** corpus (names/emails/phones stripped — never commit customer PII to the repo) and feed it in.

---

## Priority order (my picks)

1. **Protect `main`** on both repos — biggest risk, 2 minutes, reversible. *(owner: GitHub UI)*
2. **Resolve #72 vs #73 + prune 22 stale branches** — clears field-os so real work is findable. *(I'll list branches for your OK)*
3. **Work or archive the 263 orphan HubSpot contacts** — turn the dead import into a real call list. *(needs your assign-vs-archive rule)*
4. Turn on Klyfton env switches (memory/arms/maps/CREW_CODE) — owner-gated.
5. Reconnect InfraNodus + let web-leads accumulate before topical analysis.

---

*Living document — refresh from a live (connector-enabled) session; cron cannot regenerate it.*
