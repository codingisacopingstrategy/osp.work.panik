#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import Image
import ImageOps
from urllib import quote

def convert_image(img_file, colour=(0,0,0,255)):
    im = Image.open(img_file)
    im = im.convert("1")
    im = im.convert("RGBA")
    pixdata = im.load()
    
    # if colour is specified as html colour
    if isinstance(colour, basestring):
        colour = colour.replace("#","")
        colour = tuple([ord(c) for c in colour.decode('hex')] + [255])
    
    for y in xrange(im.size[1]):
        for x in xrange(im.size[0]):
            # make white pixels transparent:
            if pixdata[x, y] == (255, 255, 255, 255):
                pixdata[x, y] = (255, 255, 255, 0)
            # black pixels take on specified colour:
            else:
                pixdata[x,y] = colour

    im.save(img_file.replace('jpg','png'))

def convert_images(category, colour=(0,0,0,255)):
    category = quote(category)
    PATH = os.path.join('/', 'tmp','panik')
    images_folder = os.path.join(PATH, category)
    imgs = [os.path.join(images_folder, i) for i in os.listdir(images_folder) if 'jpg' in i]
    for img in imgs:
        convert_image(img, colour)

if __name__ == "__main__":
    from get_category_members import get_uris
    from retrieve import retrieve_category
    category = "Category:Clothing_illustrations"
    uris = get_uris(category)
    retrieve_category(category, uris)
    convert_images(category, '#fd297e')

