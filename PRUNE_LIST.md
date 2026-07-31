# 🌿 Branch Prune List — read-only prep (nothing deleted yet)

**Generated:** 2026-07-31 (interactive, live GitHub data) · **Owner:** Clifton
**Action required from you:** one word — **`prune`** — and I delete the ✅ SAFE set below in a live session. I will NOT touch anything until you say so.

> Verified against live branch list + PR merge state. "Merged" = the branch's work is already in `main`, so the branch is pure clutter. "Dead experiment" = a `copilot/*` branch that never opened/merged a PR and hasn't moved in weeks.

---

## `mgsf-field-os` — 21 safe to delete, 4 to KEEP

### ✅ SAFE — work already merged into `main` (3)
| Branch | Why safe |
|---|---|
| `vercel-agent/persist-semantic-memory` | PR **#72** merged 2026-07-31 |
| `copilot/supabase-problems` | PR **#67** merged 2026-07-16 |
| `claude/klyfton-ai-review-1fw0on` | PRs **#61–66** merged 2026-07-15 |

### ✅ SAFE — dead `copilot/*` experiments, never merged, no open PR (17)
`copilot/audit-and-repair-repo-hygiene` · `copilot/audit-repair-repo-hygiene` ·
`copilot/build-agents` · `copilot/build-connect-capabilities` ·
`copilot/create-database-tables` · `copilot/create-leads-jobs-estimates-tables` ·
`copilot/create-mgsf-project-status` · `copilot/create-tables-for-leads-jobs-estimates-materials-l` ·
`copilot/feature-upgrade-interface` · `copilot/feature-user-profile-update` ·
`copilot/fix-crew-view-clock-in-out-bug` · `copilot/fix-obvious-issues` ·
`copilot/fix-whatevers-broken` · `copilot/have-done-everything` ·
`copilot/new-feature-development` · `copilot/repo-hygiene-fix` ·
`copilot/session-name-save-progress`

### ✅ SAFE — stale one-off (1)
| Branch | Why safe |
|---|---|
| `claude/github-pat-setup-38dl97` | old PAT-setup branch, abandoned, no PR |

### 🚫 KEEP — do NOT delete (4)
| Branch | Why keep |
|---|---|
| `main` | production |
| `claude/klyfton-ai-problems-ynhx9f` | **current working branch** (tonight's staged work) |
| `copilot/fix-all-problems` | backs **open draft PR #74** — triage the PR first |
| `copilot/mgsf-field-os-70-fix-vercel-issue` | backs **open draft PR #71** — triage the PR first |

---

## `mgsf-marketing` — 1 to verify, 2 to KEEP

| Branch | Verdict |
|---|---|
| `vercel/install-vercel-web-analytics-5iq6ly` | ⚠️ **verify first** — confirm Vercel Web Analytics is live on `main`, then safe to delete |
| `main` | 🚫 KEEP — production |
| `claude/klyfton-ai-problems-ynhx9f` | 🚫 KEEP — current working branch |

---

## Also for you (can't be done via tools — GitHub UI, ~2 min each)
- **Triage the 2 open draft PRs** in field-os: **#74** ("Resolving issues in the project", stale 07-31) and **#71** ("Restore Vercel cron execution", stale 07-24). Close both if superseded → then their branches (`copilot/fix-all-problems`, `copilot/mgsf-field-os-70-fix-vercel-issue`) join the safe-delete set.
- **Protect `main`** on both repos (Settings → Branches → require PR before merge). No MCP tool for this.

---

## The delete commands (for reference — I run these on your `prune`)
```bash
# field-os — 21 branches
for b in \
  vercel-agent/persist-semantic-memory copilot/supabase-problems claude/klyfton-ai-review-1fw0on \
  copilot/audit-and-repair-repo-hygiene copilot/audit-repair-repo-hygiene copilot/build-agents \
  copilot/build-connect-capabilities copilot/create-database-tables copilot/create-leads-jobs-estimates-tables \
  copilot/create-mgsf-project-status copilot/create-tables-for-leads-jobs-estimates-materials-l \
  copilot/feature-upgrade-interface copilot/feature-user-profile-update copilot/fix-crew-view-clock-in-out-bug \
  copilot/fix-obvious-issues copilot/fix-whatevers-broken copilot/have-done-everything \
  copilot/new-feature-development copilot/repo-hygiene-fix copilot/session-name-save-progress \
  claude/github-pat-setup-38dl97 ; do
  git push origin --delete "$b"
done
```
_(I use the GitHub MCP tools to delete, not raw git — same effect, tracked. Listed here so you can see exactly what goes.)_

---

*Read-only prep. Nothing is deleted until you say `prune`. Refresh from a live session — branch state changes.*
