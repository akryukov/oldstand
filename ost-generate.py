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

import fontforge

base_name = "OldStandard"
full_name = "Old Standard"
styles = ("Regular", "Italic", "Bold")

def process_font(name, fname, style):
    filename = name + "-" + style
    font = fontforge.open(filename + ".sfd")

    # This breaks Graphite rendering in Evince: see the page 40 in the manual
    #font.head_optimized_for_cleartype = True

    # Set encoding to mac in order to get first 256 GID's mapped as in the MacRoman
    # codepage (otherwise we would get a defective cmap table for the Mac platform)
    font.encoding = "mac"

    # Add localized Fullname entries. Since we change family name for TTF output,
    # there is no reason to store them directly in the file
    ttnames = list( font.sfnt_names )
    for ttname in ttnames:
	if ttname[1] == 'SubFamily':
	    ttnames.append( ( ttname[0],'Fullname',"%s %s" % ( fname,ttname[2] ) ) )
    font.sfnt_names = tuple( ttnames )

    font.gasp_version = 1
    font.gasp = (
            ( 10   , ( 'antialias', 'symmetric-smoothing' ) ),
            ( 20   , ( 'gridfit', 'gridfit+smoothing' ) ),
            ( 65535, ( 'antialias', 'gridfit', 'symmetric-smoothing', 'gridfit+smoothing' ) ),
        )
    font.generate( filename + ".otf",flags=( "opentype","PfEd-colors","PfEd-lookups" ),layer="Fore" )

    woff_meta = base_name + "-WOFF-metadata.xml"
    f = file( woff_meta,'r' )
    lines = f.readlines()
    f.close()
    font.woffMetadata = "".join( lines )
    font.generate( filename + ".woff",layer="TTF" )

    # Append the 'TT' suffix to various font names, including localized entries
    for i in range( 0,len( ttnames )):
        ttname = ttnames[i]
	if ttname[1] == 'Fullname':
            ttnames[i] = ( ttname[0],'Fullname',ttname[2].replace( fname,fname + " TT" ) )
    font.sfnt_names = tuple( ttnames )
    font.familyname = fname + " TT"
    font.fullname = fname + " TT " + style
    font.fontname = name + "TT-" + style

    font.generate( filename + ".ttf",flags=( "opentype","old-kern","PfEd-colors","PfEd-lookups","dummy-dsig" ),layer="TTF" )

    font.close()

for style in styles:
    fontforge.setPrefs( "AutoHint",False )
    fontforge.setPrefs( "ClearInstrsBigChanges",False )
    fontforge.setPrefs( "CopyTTFInstrs",False )
    process_font( base_name, full_name, style )
