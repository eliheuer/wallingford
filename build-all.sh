#!/bin/bash
set -e

sh sources/build.sh
python3 documentation/drawbot/specimen-001.py
