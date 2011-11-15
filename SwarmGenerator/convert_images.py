#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import Image
import ImageOps
from urllib import quote

def convert_image(img_file, colour=(0,0,0,255)):
    try:
        im = Image.open(img_file)
    except IOError:
        return None
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

    output_name = img_file.replace('jpg','png')
    im.save(output_name)
    return output_name

def convert_images(imgs, colour=(0,0,0,255)):
    converted_images = []
    for img in imgs:
        converted_images.append(convert_image(img, colour))
    return [i for i in converted_images if i]

if __name__ == "__main__":
    from get_category_members import get_uris
    from retrieve import retrieve_uris
    from urllib import quote
    PATH = os.path.join('/', 'tmp','panik')
    category = "Category:Clothing_illustrations"
    category_path = os.path.join(PATH, quote(category))
    uris = get_uris(category)
    convert_images(retrieve_uris(category_path, uris), '#fd297e')

