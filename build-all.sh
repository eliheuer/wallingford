#!/bin/bash
set -e

sh sources/build.sh
python3 docs/drawbot/specimen-001.py
