#!/usr/bin/env bash
# Fetch CodeChef problem payloads to data/raw/<CODE>.json
# The practice problem endpoint needs no authentication.
set -uo pipefail
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36'
fetch_one() {
  code="$1"
  out="data/raw/${code}.json"
  [ -s "$out" ] && return 0
  curl -sS -m 30 -H "User-Agent: $UA" -H 'Accept: application/json' \
    "https://www.codechef.com/api/contests/PRACTICE/problems/${code}" -o "$out"
  if ! python3 -c "import json,sys; json.load(open('$out'))" 2>/dev/null; then
    echo "BAD $code"; rm -f "$out"
  fi
}
export -f fetch_one
export UA
mkdir -p data/raw
xargs -P 8 -I{} bash -c 'fetch_one "$@"' _ {} < "$1"
