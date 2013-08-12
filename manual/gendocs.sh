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

#!/bin/bash

ZIP="zip -DrX"
PACK_NAME=oldstand-manual
VERSION="2.2"

rm -f *.toc *.aux *.out
xelatex $PACK_NAME.tex
xelatex $PACK_NAME.tex
xelatex $PACK_NAME.tex
rm -f *.zip

$ZIP ${PACK_NAME}-${VERSION}.src.zip gendocs.sh $PACK_NAME.tex *.png
