# MGSF Task Planner — live work queue

Forward-looking queue (companion to `NIGHT_LOG.md`, which is history). **Read this first**
every session. Update it in the same commit as the work. Managed via the
`mgsf-session-planner` skill.

**Where** = which session type can do it: `interactive` (needs connectors — HubSpot/GitHub/
Vercel/InfraNodus), `cron` (local repo-only), or `either`.
**Owner-gated** = don't execute unattended; do the read-only prep so it's one-tap.

_Last updated: 2026-07-31 (post platform build-out — agents runtime shipped)._

---

## 🔴 Owner-gated — queued for one-tap approval (interactive)
| Task | Where | Ready action | Notes |
|---|---|---|---|
| **Review + merge the branch to main** | interactive | Owner reviews `claude/klyfton-ai-problems-ynhx9f` → I open a PR / merge on the word | **BIG:** the whole 2026-07-31 platform build-out is staged here (tool bag, wiki+seed, projects/PM, CMDB, scenarios, RAG, agents runtime, curriculum, free-model hub, universal bus). Gate 29 suites / 630 checks green. Nothing live until merged. |
| **Go-live keys (highest leverage first)** | owner (Vercel) | Set `ALERTS_WEBHOOK_URL` first | CMDB `biggestUnlock` = the webhook → lights 10 tools (arms + universal bus + all the sweeps). Then Supabase (memory/wiki), `OPENAI_API_KEY`, `CREW_CODE`, budget, Maps, any free-model key. `/api/cmdb` shows the live root-cause map. |
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
| One bounded, safe repo improvement per cron fire | cron | ongoing — **pull the next item from `FIRE_SCHEDULE.md`** |
| Keep this planner + NIGHT_LOG + PROJECT_MEMORY current | either | ongoing |
| Refresh `GAP_AUDIT.md` from live data | interactive | as needed (cron can't — needs connectors) |
| InfraNodus topical pass (§5 of GAP_AUDIT) | interactive | **pending** — account rate-limited (429 ×3); re-run when quota frees |

> **Note (2026-07-31):** the field-os **module build-out is essentially complete** — the genuine
> gaps this session named (wiki, projects/PM, CMDB, scenarios, RAG, agents, curriculum, free-model
> hub) are built + tested + staged, and the last four capability ideas came back "already have /
> skip." So the overnight loop should now favor **maintenance** (keep docs current, add a verified
> test only where something is *genuinely* uncovered) and **idle honestly** rather than inventing
> new modules — the real remaining value is owner-gated (review+merge, turn on keys). No padding.

## ✅ Recently shipped (see NIGHT_LOG for detail)
- **Klyfton platform build-out (2026-07-31, staged):** tool bag (52) + brain/router wiring · universal Zapier bus · curriculum (31 scenarios) · wiki + 8 seed articles · projects/PM engine + skill · CMDB (dependency graph + biggest-unlock) · scenario builder · unified RAG · agents runtime (PM=agent #1) · 4 free-model providers. Gate **29 suites / 630 checks**. Full record in `mgsf-field-os/PROJECT_MEMORY.md` §5.
- Website lead capture live: `/api/intake` → HubSpot, `configured:true` (PRs #2, #4 merged).
- Optional email field on both quote forms + dedup-safe 409 handling (Pass 184).
- Case-insensitive `HUBSPOT_TOKEN` match (accepts `HubSpot_Token`).
- `GAP_AUDIT.md` cross-app audit (Pass 183); intake tests wired into the gate (Pass 182).

## 👁 Watching
- PR **#73** (field-os) — open, CI green; only red is the known GitGuardian false-positive (owner clearing in dashboard). ~60-min self check-ins armed.
