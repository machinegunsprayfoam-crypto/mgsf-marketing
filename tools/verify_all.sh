#!/usr/bin/env bash
# One-command pre-push verifier for the MGSF marketing site. Run from the repo root:
#   bash tools/verify_all.sh
# Runs the QA gate + a sitemap-drift check and reports one combined result.
# Exit 0 only if everything is clean — safe to gate a commit/deploy on it.
set -u
root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root" || exit 2
fail=0

echo "== MGSF marketing — verify_all =="

echo "-- sitemap lastmod drift"
if python3 tools/sync_sitemap.py --check; then :; else echo "   (run: python3 tools/sync_sitemap.py to fix)"; fail=1; fi

echo "-- QA gate (JSON-LD / links / canonical+robots / FAQ schema==visible)"
if python3 tools/qa_check.py; then :; else fail=1; fi

echo
if [ "$fail" -eq 0 ]; then echo "✓ ALL CLEAN — safe to commit/push"; else echo "✗ ISSUES FOUND — fix before pushing"; fi
exit "$fail"
