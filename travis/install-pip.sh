#!/usr/bin/env bash
# If you use this file as template, don't forget to `chmod a+x newfile`

set -e

echo "pip installing required python packages"
pip install -r requirements.txt

python --version
