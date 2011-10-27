#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import Image
import ImageOps

PATH = os.path.join(os.getcwd(), 'example_imgs')
imgs = [os.path.join(PATH, i) for i in os.listdir(PATH)]

def convert_image(img_file):
    im = Image.open(img_file)
    im = im.convert("1")
    im = im.convert("RGBA")
    pixdata = im.load()

    for y in xrange(im.size[1]):
        for x in xrange(im.size[0]):
            if pixdata[x, y] == (255, 255, 255, 255):
                pixdata[x, y] = (255, 255, 255, 0)

    im.save(img_file.replace('example_imgs', 'converted_example_imgs').replace('jpg','png'))

if __name__ == "__main__":
    for img in imgs:
        convert_image(img)

