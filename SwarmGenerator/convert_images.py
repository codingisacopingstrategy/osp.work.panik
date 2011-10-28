#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import Image
import ImageOps
from urllib import quote

def convert_image(img_file):
    im = Image.open(img_file)
    im = im.convert("1")
    im = im.convert("RGBA")
    pixdata = im.load()

    for y in xrange(im.size[1]):
        for x in xrange(im.size[0]):
            if pixdata[x, y] == (255, 255, 255, 255):
                pixdata[x, y] = (255, 255, 255, 0)

    im.save(img_file.replace('jpg','png'))

def convert_images(category):
    category = quote(category)
    PATH = os.path.join('/', 'tmp','panik')
    images_folder = os.path.join(PATH, category)
    imgs = [os.path.join(images_folder, i) for i in os.listdir(images_folder) if 'jpg' in i]
    for img in imgs:
        convert_image(img)

if __name__ == "__main__":
    from get_category_members import get_uris
    from retrieve import retrieve_category
    category = "Category:Clothing_illustrations"
    uris = get_uris(category)
    retrieve_category(category, uris)
    convert_images(quote(category))

