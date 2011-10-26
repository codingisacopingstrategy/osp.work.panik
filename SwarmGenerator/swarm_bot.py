# This needs to be run in shoebot

import os

# PATH = "/tmp/panik"
PATH = os.path.join(os.getcwd(), 'example_imgs')
imgs = [os.path.join(PATH, i) for i in os.listdir(PATH)]

from random import random

scale = 18
upto = 32

points = [((i**2 % 25), i**2 / 25) for i in range(0, upto)]

size(24 * scale, 38 * scale );

for i in range(0, upto):
    image(imgs[i], points[i][0] * scale * random(), points[i][1] * scale)

