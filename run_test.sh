#!/bin/bash
set -eo pipefail

export PYTHONDONTWRITEBYTECODE=1
export PYTHONUNBUFFERED=1
export CI=true

cd /workspace/csvkit
pytest -v --tb=short --no-cov -p no:cacheprovider tests/

