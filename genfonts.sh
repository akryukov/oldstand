#!/bin/bash

#####################################################################
#
# This file is part of Old Standard font family
# (http://www.thessalonica.org.ru/en/oldstandard.html) and is
# Copyright (C) 2006-2011 Alexey Kryukov <amkryukov@gmail.com>.
#
# This Font Software is licensed under the SIL Open Font License,
# Version 1.1.
#
# You should have received a copy of the license along with this Font
# Software. If this is not the case, go to (http://scripts.sil.org/OFL)
# for all the details including a FAQ.
#
#####################################################################/

ZIP="zip -DrX"
PACK_NAME=oldstandard
DOCS="OFL.txt OFL-FAQ.txt FONTLOG.txt"
VERSION="2.2"

fontforge -script ost-generate.py

for f in *.ttf; do
    BASENAME=${f%.ttf}
    wine cachett.exe $f ${BASENAME}_hdmx.ttf OldStandard.cfg
    mv ${BASENAME}_hdmx.ttf $BASENAME.ttf
    grcompiler -w3521 $BASENAME.gdl $BASENAME.ttf
    mv ${BASENAME}_gr.ttf $BASENAME.ttf
done

rm -f *.zip

$ZIP $PACK_NAME-$VERSION.ttf.zip *.ttf $DOCS
$ZIP $PACK_NAME-$VERSION.woff.zip *.woff $DOCS
$ZIP $PACK_NAME-$VERSION.otf.zip *.otf $DOCS
$ZIP $PACK_NAME-$VERSION.src.zip genfonts.sh ost-generate.py *.gdl *.cfg *metadata.xml *.sfd $DOCS
