#!/bin/bash
set -e

fontmake -u sources/Wallingford.ufo -o ttf
rm -rf instance_ufo
mkdir -p fonts/ttf
#cp -r master_ufo/*.designspace sources/
#cp -r master_ufo/*.ufo sources/
rm -rf master_ufo
cp -r master_ttf/*.ttf fonts/ttf/
rm -rf master_ttf
