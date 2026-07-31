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

echo "-- intake endpoint logic (api/intake.js pure tests)"
if [ -f tools/test_intake.js ]; then
  if command -v node >/dev/null 2>&1; then
    if node tools/test_intake.js >/dev/null; then echo "   intake logic OK"; else echo "   intake tests FAILED (run: node tools/test_intake.js)"; fail=1; fi
  else
    echo "   (node not found — skipping intake tests)"
  fi
else
  echo "   (no tools/test_intake.js — skipping)"
fi

echo
if [ "$fail" -eq 0 ]; then echo "✓ ALL CLEAN — safe to commit/push"; else echo "✗ ISSUES FOUND — fix before pushing"; fi
exit "$fail"
