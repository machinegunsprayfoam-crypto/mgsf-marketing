# MGSF Task Planner — live work queue

Forward-looking queue (companion to `NIGHT_LOG.md`, which is history). **Read this first**
every session. Update it in the same commit as the work. Managed via the
`mgsf-session-planner` skill.

**Where** = which session type can do it: `interactive` (needs connectors — HubSpot/GitHub/
Vercel/InfraNodus), `cron` (local repo-only), or `either`.
**Owner-gated** = don't execute unattended; do the read-only prep so it's one-tap.

_Last updated: 2026-07-31 (Pass 184 / interactive)._

---

## 🔴 Owner-gated — queued for one-tap approval (interactive)
| Task | Where | Ready action | Notes |
|---|---|---|---|
| Verify `HUBSPOT_TOKEN` has `crm.objects.contacts.write` scope | interactive | Owner submits 1 live form lead → I confirm it lands + delete it | Endpoint live, `configured:true`. Only unknown left in lead pipeline. |
| Assign or archive the **263 orphan HubSpot contacts** | interactive | Owner says `assign` (to Clifton) or `archive` (dead UNQUALIFIED import) → I run it | 263/333 unowned; July-9 bulk import. |
| Protect `main` on **both** repos | owner (GitHub UI) | Settings → Branches → require PR | No MCP tool for this; ~2 min each. Biggest risk. |
| Delete **20 orphan branches** (field-os) | interactive | Owner says `delete the 20` → I remove them | Safe list computed 2026-07-31 (no open-PR heads). |
| Close stale drafts **#71** (Vercel cron) + **#74** (fix-all-problems) | interactive | Owner says `close 71 and 74` → I close + delete their branches | Untouched since Jul 24 / stale. |
| Decide **#72** "Fix semantic memory persistence" | interactive | Owner says `check 72` → I read the diff + give keep/toss rec | Separate from #73; not a true overlap. |
| Klyfton env switches | owner (Vercel) | Set exact-name vars + redeploy | `OPENAI_API_KEY` (memory/TTS) + run pgvector SQL once; `CREW_CODE` (gate data endpoints); `ALERTS_WEBHOOK_URL` (arms); `KLYFTON_MONTHLY_BUDGET_USD` (ATS); `GOOGLE_MAPS_API_KEY`. |
| Reconnect dropped connectors | owner (connector settings) | Re-auth InfraNodus, Apollo, Supabase-MCP | Needed before InfraNodus topical analysis. |
| Coverage gaps | owner | Connect Google Ads (Windsor), add Slack `#leads`/`#alerts`/`#field`, auth Twilio, renew QBO for writes | From GAP_AUDIT §4. |

## 🟢 Autonomous — safe to do unattended
| Task | Where | Status |
|---|---|---|
| One bounded, safe repo improvement per cron fire | cron | ongoing (mgsf-overnight-ops) |
| Keep this planner + NIGHT_LOG current | either | ongoing |
| Refresh `GAP_AUDIT.md` from live data | interactive | as needed (cron can't — needs connectors) |
| InfraNodus topical corpus | interactive | **on hold** — no lead-message text yet; revisit once web leads accumulate |

## ✅ Recently shipped (see NIGHT_LOG for detail)
- Website lead capture live: `/api/intake` → HubSpot, `configured:true` (PRs #2, #4 merged).
- Optional email field on both quote forms + dedup-safe 409 handling (Pass 184).
- Case-insensitive `HUBSPOT_TOKEN` match (accepts `HubSpot_Token`).
- `GAP_AUDIT.md` cross-app audit (Pass 183); intake tests wired into the gate (Pass 182).

## 👁 Watching
- PR **#73** (field-os) — open, CI green; only red is the known GitGuardian false-positive (owner clearing in dashboard). ~60-min self check-ins armed.
