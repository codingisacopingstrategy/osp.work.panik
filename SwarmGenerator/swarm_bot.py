#!/usr/bin/env python

import os
import shoebot
from urllib import quote
from random import random
from shoebot.core import CairoCanvas, CairoImageSink, NodeBot


PATH = os.path.join('/', 'tmp','panik')

def swarm_bot(output_image, images, text=None):
    imgs = images
    
    sink = CairoImageSink(output_image, "svg", multifile = False)
    canvas = CairoCanvas(sink, enable_cairo_queue=True)
    bot = shoebot.core.NodeBot(canvas)
    
    scale = 18
    upto = 32
    if len(imgs) < 32:
        upto = len(imgs)
    
    points = [((i**2 % 25), i**2 / 25) for i in range(0, upto)]
    
    HEIGHT = 38 * scale
    WIDTH = 24 * scale
    bot.size(WIDTH, HEIGHT);
    bot.background(None)
    
    if text:
        texts = text.split("\n")
        nlines = len(texts)
        lineheight = HEIGHT / nlines
        
        for i, text in enumerate(texts):
            bot.align(bot.CENTER)
            bot.font("Reglo")
            bot.fontsize(lineheight / 1.2)
            otwidth, theight = bot.textmetrics(text)
            twidth = WIDTH * 0.9
            factor = twidth / float(otwidth)
            bot.scale(factor, 1)
            bot.text(text, (1 / factor) * WIDTH * 0.05, lineheight * i + lineheight / 1.2 )
            bot.reset()
        
    
    for i in range(0, upto):
        bot.image(imgs[i], points[i][0] * scale * random(), points[i][1] * scale)
    
    bot._canvas.flush(frame=0)

if __name__ == "__main__":
    from get_category_members import get_uris
    from retrieve import retrieve_uris
    from convert_images import convert_images
    from urllib import quote
    PATH = os.path.join('/', 'tmp','panik')
    category = "Category:Clothing_illustrations"
    category_path = os.path.join(PATH, quote(category))
    uris = get_uris(category)
    swarm_bot(category_path + '.svg', convert_images(retrieve_uris(category_path, uris), '#fd297e'), text='Panik!')