# MGSF Backlog — everything left, prioritized

_Compiled 2026-08 · the single "what's left" list (consolidates TASK_PLANNER, GAP_AUDIT, the weakness sweep)._

**Headline:** the **build backlog is essentially empty.** ~18 items remain and **~15 need YOU**
(merge, keys, go-live, business facts). Only ~3 are mine, and they're small. Nothing new is
blocking — the gap now is *turning on* what's built, not building more.

---

## 🔴 GO-LIVE — owner-gated, do first (nothing is live until these happen)
1. **Review + merge the branch** `claude/klyfton-ai-problems-ynhx9f` → main. The entire session is staged here: ~20 Klyfton modules + weakness fixes + the dashboard UI + go-live docs. Gate **34 suites / 708 checks** green. **Nothing runs until merged.**
2. **DNS** — `machinegunsprayfoam.com` still resolves to a **parking IP (208.91.197.27)**, not Vercel. The public .com isn't live. Add the A/CNAME records at the registrar.
3. **Vercel Deployment Protection OFF** — the app currently 403s the public/crew without a Vercel login. Turn it off (or add the custom domain) so people can reach it.
4. **Set keys in Vercel** (in the CMDB "biggest-unlock" order — see `field-os/db/SETUP.md`):
   `ALERTS_WEBHOOK_URL` (arms + universal bus → ~10 tools) → **Supabase URL + service key** + `OPENAI_API_KEY` then run the `db/*.sql` → `CREW_CODE` (gate endpoints) → `KLYFTON_MONTHLY_BUDGET_USD` → `GOOGLE_MAPS_API_KEY` → Twilio trio → any free-model key.
5. **Verify `HUBSPOT_TOKEN` write scope** — submit one live form lead, I confirm it lands + delete it (last unknown in the lead pipeline).

## 🟠 SAY-THE-WORD — I execute on your trigger (read-only prep already done)
6. **HubSpot 263 orphan contacts** → say **`assign`** (to you) or **`archive`** (dead July-9 import).
7. **Repo hygiene** → say **`prune`** (delete ~20 stale `copilot/*` + merged branches; list in `PRUNE_LIST.md`) + close stale drafts **#71 / #74**. Protect `main` on both repos (GitHub UI, ~2 min each).
8. **Test lead** through the live form (after DNS) → I confirm + clean up.
9. **GitGuardian** — clear the historical test-fixture false-positive in the dashboard (no code fix).

## 🟡 BUSINESS FACTS — only you can give these (I won't fabricate)
10. **Contractor registration #** → adds a "Registered Montana Contractor #___" credential.
11. **North Dakota phone number** → wire into the ND city pages (like WY/SD).
12. **Real Google reviews** → site has none (won't invent). Fix the **`g.pe` → `g.page`** review link (flagged).
13. **Attorney review** of Privacy + Terms.
14. **Job photos** → for a real gallery (pages currently share the hero image).
15. **Confirm Terra-Lok / soil-stabilization pricing** (still PENDING in doctrine).

## ⚪ MINE — remaining autonomous work (small)
16. **Brain-graph regen** — the GraphRAG knowledge map is a **2026-07-27 snapshot**; needs InfraNodus (rate-limited all session). Best-effort when the quota frees. *(The new modules already reach the brain via the tool bag, so this is low-severity.)*
17. **InfraNodus topical/SEO pass** (GAP_AUDIT §5) — pending, same rate-limit.
18. **Optional UI polish** — agents approve/dispatch flow, telemetry charts, wiki edit/delete. Nice-to-have, not needed.

---

## ✅ DONE this session (so the scope is visible)
- **Platform:** semantic memory, curriculum (+LLM-judge), tool bag + universal bus, wiki (+seed, semantic), projects/PM, CMDB, scenario builder (+deploy), unified RAG, agents runtime (closed loop + run-history), 9-provider hub w/ fallback.
- **Hardening:** boot self-map, CREW_CODE guard, idempotency, telemetry, live smoke tests.
- **UI:** dashboard pages — System, Agents, Wiki, Automations.
- **Docs/go-live:** `db/SETUP.md`, PROJECT_MEMORY, this backlog. Gate **34 suites / 708 checks**.
- **Marketing site:** 40 pages, dark tactical theme, lead capture live, SEO/QA clean (earlier passes).

_The one-line takeaway: **build is done; the needle now moves on merge + keys + DNS.**_
