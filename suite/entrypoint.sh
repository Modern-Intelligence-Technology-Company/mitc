#!/bin/bash
# Single-image entry: render mediamtx paths, then supervise broker + twins + API.
set -euo pipefail
export MITC_DATA_DIR="${MITC_DATA_DIR:-/data}"
export MITC_CAMERAS_FILE="${MITC_CAMERAS_FILE:-/app/config/cameras.twin.yaml}"
export MITC_TWIN_COUNT="${MITC_TWIN_COUNT:-8}"
export MITC_ENABLE_WORKER="${MITC_ENABLE_WORKER:-1}"
export PYTHONPATH=/app
mkdir -p "${MITC_DATA_DIR}/thumbs"
python3 /app/scripts/render_mediamtx.py
exec /usr/bin/supervisord -c /app/supervisord.conf -n
