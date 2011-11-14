#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scribus

names = []

for i in range(0, scribus.selectionCount()):
    names.append(scribus.getSelectedObject (i))

scribus.deselectAll()
    
for name in names: 
    scaling = 100
    scribus.setLineSpacing(scribus.getFontSize(name) * 1.2, name)
    lines = scribus.getTextLines(name)
    
    while scribus.getTextLines(name) <= lines and scribus.textOverflows(name) == False:
        scribus.setFontSize(scribus.getFontSize(name) + 1, name)
        scribus.setLineSpacing(scribus.getLineSpacing(name) + 1, name)
    scribus.setFontSize (scribus.getFontSize(name) - 2, name)
    scribus.setLineSpacing(scribus.getLineSpacing(name) - 2, name)
    scribus.setTextScalingV(scribus.getLineSpacing(name) + 100, name)

    #while scribus.textOverflows(name) == False:
    #    scaling = scaling + 1
    #    scribus.setTextScalingV (scaling, name)
    #scaling = scaling - 1
    #scribus.setTextScalingV (scaling, name)

