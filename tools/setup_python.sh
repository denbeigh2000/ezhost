#!/bin/bash

set -euo pipefail

export ENV_DIR="$REPO_ROOT/env"
export STUBS_DIR="$REPO_ROOT/stubs"

if [[ "${MYPYPATH:-""}" = "" ]]
then
    export MYPYPATH="$STUBS_DIR"
else
    export MYPYPATH="$STUBS_DIR:$MYPYPATH"
fi

if ! which python3 >/dev/null
then
    echo "No Python3 found, please install before sourcing" >&2
    exit 1
fi

if ! python3 -m venv --help 2>&1 >/dev/null
then
    echo "Virtualenv not installed for Python3, please install before sourcing" >&2
    exit 1
fi

if ! [[ -e "$ENV_DIR" ]]
then
    python3 -m venv "$ENV_DIR"
fi

source "$ENV_DIR/bin/activate"
