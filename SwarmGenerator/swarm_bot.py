# This needs to be run in shoebot

import os
import shoebot
from urllib import quote
from random import random
from shoebot.core import CairoCanvas, CairoImageSink, NodeBot


PATH = os.path.join('/', 'tmp','panik')

def swarm_bot(category, text=None):
    category = quote(category)
    images_folder = os.path.join(PATH, category)
    output_image = os.path.join(PATH, "%s.svg" % category)
    imgs = [os.path.join(images_folder, i) for i in os.listdir(images_folder) if 'png' in i]
    
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
    
    if text:
        bot.align(bot.RIGHT)
        bot.fontsize(36)
        twidth, theight = bot.textmetrics(text, 392)
        bot.text(text, 20, HEIGHT - theight + 7.2, 392)
        bot.nofill()
        bot.stroke(0)
        bot.strokewidth(17)
        bot.beginpath(WIDTH - twidth - 30, HEIGHT - theight - 30 )
        bot.lineto(WIDTH - 10, HEIGHT - theight - 30)
        bot.lineto(WIDTH - 10, HEIGHT - 10)
        bot.lineto(WIDTH - twidth - 30, HEIGHT - 10)
        bot.endpath()

    for i in range(0, upto):
        bot.image(imgs[i], points[i][0] * scale * random(), points[i][1] * scale)
    
    bot._canvas.flush(frame=0)

if __name__ == "__main__":
    swarm_bot("Category:Clothing_illustrations", text="PANIK")