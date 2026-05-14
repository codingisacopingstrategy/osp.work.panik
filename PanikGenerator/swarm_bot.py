#!/usr/bin/env python3

import os
import cairo
from random import random
import svgwrite
import base64
from PIL import Image

PATH = os.path.join('/', 'tmp', 'panik')


def swarm_bot(output_image, images, text=None, size=("12cm", "12cm"), square=True):
    imgs = images

    scale = 18
    upto = 32
    if len(imgs) < 32:
        # If there are less than 32 images, repeat existing up until 32:
        imgs = (32 // len(imgs)) * imgs + imgs[:(32 % len(imgs))]
    elif len(imgs) > 32:
        imgs = imgs[:32]

    points = [((i ** 2 % 25), i ** 2 // 25) for i in range(0, upto)]

    WIDTH = 24 * scale
    if square == True:
        HEIGHT = 24 * scale
    else:
        HEIGHT = int(24 * 2 ** 0.5 * scale)

    # Create a pycairo context for text metrics
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1, 1)
    ctx = cairo.Context(surface)

    svg = svgwrite.Drawing(output_image, size=(size[0], size[1]), profile='full', viewBox="0 0 %s %s" % (WIDTH, HEIGHT))

    for i, img in enumerate(imgs):
        f = open(img, 'rb')
        im = Image.open(img)
        img_data = "data:image/png;base64," + base64.b64encode(f.read()).decode('ascii')
        f.close()
        svg.add(
            svg.image(href=img_data, insert=(points[i][0] * scale * random(), points[i][1] * scale), width=im.size[0],
                      height=im.size[1]))

    if text:
        # split into lines, ignore blank lines:
        texts = [i for i in text.splitlines() if i]
        nlines = len(texts)
        theight = HEIGHT * 0.9
        lineheight = theight / nlines

        for i, text in enumerate(texts):
            ctx.select_font_face("Reglo", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
            ctx.set_font_size(lineheight)
            extents = ctx.text_extents(text)
            otwidth = extents.width
            twidth = WIDTH * 0.9
            factor = twidth / float(otwidth)
            svg.add(svg.text(text, insert=((1 / factor) * WIDTH * 0.05, lineheight * i + lineheight + 0.05 * HEIGHT),
                             font_family="Reglo", font_size=lineheight,
                             transform='scale(%s, 1)' % factor,
                             ))

    svg.save()


if __name__ == "__main__":
    from panik_app import get_uris
    from retrieve import retrieve_uris
    from convert_images import convert_images
    from urllib import quote
    PATH = os.path.join('/', 'tmp', 'panik')
    category = "Category:Clothing_illustrations"
    category_path = os.path.join(PATH, quote(category))
    uris = get_uris(category)
    swarm_bot(category_path + '.svg', convert_images(retrieve_uris(category_path, uris), '#fd297e'), text='Panik!')
