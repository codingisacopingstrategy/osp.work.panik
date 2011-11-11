#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scribus

names = []

for i in range (0, scribus.selectionCount()):
    names.append (scribus.getSelectedObject (i))

for name in names: 
    scribus.deselectAll()

    lines = scribus.getTextLines (name) 
    
    while 1 == 1:
        scribus.setFontSize (scribus.getFontSize(name) + 1, name)

        if scribus.getTextLines(name) > lines or scribus.textOverflows(name):
            scribus.setFontSize (scribus.getFontSize(name) - 2, name)
            break

    scaling = 100

    while 1 == 1:
        scaling = scaling + 1
        scribus.setTextScalingV (scaling, name)
        if scribus.textOverflows(name):
            scaling = scaling - 1
            scribus.setTextScalingV (scaling, name)
            break
