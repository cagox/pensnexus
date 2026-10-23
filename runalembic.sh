#!/usr/bin/env bash
set -euo pipefail

# Cache sudo access interactively
sudo -v

CREDS_DIR="$HOME/temp"

export CONFIG_PATH="$HOME/workspace/github/cagox/pensnexus/docs/ficsiteconf.json"
export DB_PASSWORD="$(sudo systemd-creds decrypt "${CREDS_DIR}/db_password.cred" -)"
export PEPPER="$(sudo systemd-creds decrypt "${CREDS_DIR}/pepper.cred" -)"
export SESSION_SECRET="$(sudo systemd-creds decrypt "${CREDS_DIR}/session_secret.cred" -)"

# Run whatever command you pass to this script (e.g., ./run.sh alembic revision --autogenerate -m "...")
exec "$@"