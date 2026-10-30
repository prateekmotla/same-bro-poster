#!/usr/bin/env bash
# Instagram token store without a GitHub PAT.
# The current token lives encrypted in ig_token.enc (AES-256, key = TOKEN_KEY secret,
# which never appears in the repo). Falls back to the IG_ACCESS_TOKEN secret.
#   source scripts/ig_token.sh load    -> exports IG_ACCESS_TOKEN (masked)
#   bash   scripts/ig_token.sh refresh -> refreshes token, re-encrypts into ig_token.enc
set -euo pipefail
F=ig_token.enc
: "${TOKEN_KEY:?TOKEN_KEY missing}"
dec() { openssl enc -d -aes-256-cbc -pbkdf2 -iter 200000 -a -A -pass env:TOKEN_KEY -in "$F"; }
load() {
  if [ -f "$F" ] && T=$(dec 2>/dev/null) && [ -n "$T" ]; then
    echo "::add-mask::$T"; export IG_ACCESS_TOKEN="$T"
  fi
  : "${IG_ACCESS_TOKEN:?no Instagram token}"
  if [ -n "${GITHUB_ENV:-}" ]; then echo "IG_ACCESS_TOKEN=$IG_ACCESS_TOKEN" >> "$GITHUB_ENV"; fi
}
case "${1:-load}" in
  load) load ;;
  refresh)
    load
    NEW=$(curl -sf "https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token=${IG_ACCESS_TOKEN}" | jq -r .access_token)
    if [ -z "$NEW" ] || [ "$NEW" = "null" ]; then echo "Refresh failed"; exit 1; fi
    echo "::add-mask::$NEW"
    printf %s "$NEW" | openssl enc -aes-256-cbc -pbkdf2 -iter 200000 -a -A -salt -pass env:TOKEN_KEY -out "$F"
    echo "Token refreshed and stored." ;;
esac
