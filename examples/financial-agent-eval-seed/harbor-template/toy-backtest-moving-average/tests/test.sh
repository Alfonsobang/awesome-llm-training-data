#!/bin/bash

set -u

python -m unittest discover -s /tests -p "test_*.py"

if [ $? -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
