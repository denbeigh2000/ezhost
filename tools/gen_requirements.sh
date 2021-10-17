#!/bin/sh

set -euo pipefail

TMP_VIRTUALENV="$(mktemp -d)"
PIP_BIN="$TMP_VIRTUALENV/bin/pip"
REQ_IN="$REPO_ROOT/requirements.in"
REQ_TXT="$REPO_ROOT/requirements.txt"

python3 -m venv "$TMP_VIRTUALENV"

"$PIP_BIN" install -r "$REQ_IN"
"$PIP_BIN" freeze -r "$REQ_IN" -l > "$REQ_TXT"

rm -rf "$TMP_VIRTUALENV"
