#!/usr/bin/env sh
set -eu

python -m unittest discover -s "$(dirname "$0")" -p "test_*.py"
