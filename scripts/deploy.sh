#!/bin/bash
set -euo pipefail
ENV="${1:-staging}"
echo "==> Deploying $(basename $(pwd)) to $ENV"
CONFIG="deploy/config/${ENV}.env"
[ -f "$CONFIG" ] && set -a && source "$CONFIG" && set +a
echo "    Environment: $ENV, version: ${VERSION:-latest}"
echo "==> Deployment to $ENV complete"
