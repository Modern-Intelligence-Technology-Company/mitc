#!/usr/bin/env bash
#
# verify-deliverables.sh
#
# Non-trivial acceptance check for the MITC Bloomington ALPR bid documentation
# package. Ensures required artifacts exist, are readable, and exceed minimum
# substantive length so empty stubs cannot pass.
#
# Exit codes: 0 = all checks passed, 1 = one or more failures.
#
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# Minimum byte counts encourage real prose, not placeholders.
declare -A MIN_BYTES=(
  ["docs/business-plan.md"]=3500
  ["docs/alpr-technical-specification.md"]=4500
  ["docs/proposal-paper.md"]=5500
  ["docs/pitch-deck.md"]=2500
  ["docs/bid-cover-letter.md"]=1200
  ["docs/adr/0001-bloomington-alpr-bid-package.md"]=1500
  ["docs/adr/0001-bloomington-alpr-bid-package-aar.md"]=800
  ["LOG.md"]=400
)

REQUIRED_FILES=(
  "README.md"
  "docs/business-plan.md"
  "docs/alpr-technical-specification.md"
  "docs/proposal-paper.md"
  "docs/pitch-deck.md"
  "docs/bid-cover-letter.md"
  "docs/adr/0001-bloomington-alpr-bid-package.md"
  "docs/adr/0001-bloomington-alpr-bid-package-aar.md"
  "LOG.md"
)

failures=0

for f in "${REQUIRED_FILES[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "FAIL: missing required file: $f" >&2
    failures=$((failures + 1))
  fi
done

for f in "${!MIN_BYTES[@]}"; do
  min="${MIN_BYTES[$f]}"
  if [[ -f "$f" ]]; then
    size="$(wc -c < "$f" | tr -d ' ')"
    if [[ "$size" -lt "$min" ]]; then
      echo "FAIL: $f too small (${size} bytes; need >= ${min})" >&2
      failures=$((failures + 1))
    fi
  fi
done

# Proposal paper must reference local custody (thesis requirement).
if [[ -f "docs/proposal-paper.md" ]]; then
  if ! grep -qi 'local' docs/proposal-paper.md || ! grep -qiE 'on-?prem|in-?city|self-?host' docs/proposal-paper.md; then
    echo "FAIL: proposal-paper.md must discuss local/on-prem/in-city data custody" >&2
    failures=$((failures + 1))
  fi
fi

# Technical spec must name at least one open-source or standards anchor.
if [[ -f "docs/alpr-technical-specification.md" ]]; then
  if ! grep -qiE 'open source|open-source|Apache|MIT license|GPL|ONVIF|Docker' docs/alpr-technical-specification.md; then
    echo "FAIL: alpr-technical-specification.md must reference open-source or standard stack elements" >&2
    failures=$((failures + 1))
  fi
fi

# Technical spec must carry manufacturer reference URLs for COTS camera integration.
if [[ -f "docs/alpr-technical-specification.md" ]]; then
  if ! grep -qE 'axis\.com|hanwhavision\.com|boschsecurity\.com|uniview\.com' docs/alpr-technical-specification.md; then
    echo "FAIL: alpr-technical-specification.md must link to COTS camera manufacturer pages" >&2
    failures=$((failures + 1))
  fi
fi

if [[ "$failures" -gt 0 ]]; then
  echo "verify-deliverables: ${failures} check(s) failed" >&2
  exit 1
fi

echo "verify-deliverables: all checks passed"
exit 0
