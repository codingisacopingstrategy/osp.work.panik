# -*- coding: utf-8 -*-

import sys
import os
import urllib

class AppURLopener(urllib.FancyURLopener):
    version = 'Ḿozilla/5.0'

urllib._urlopener = AppURLopener()

PATH = os.path.join('/', 'tmp','panik')

def retrieve_category(category, uris):
    CATEGORYPATH = os.path.join(PATH, urllib.quote(category))
    if not os.path.exists(CATEGORYPATH):
        os.makedirs(CATEGORYPATH)
    # Only download if no files downloaded yet:
    if len(os.listdir(CATEGORYPATH)) == 0:
        for uri in uris:
            filename = uri.split("/")[-1]
            path = os.path.join(CATEGORYPATH, filename)
            urllib.urlretrieve(uri, path)

if __name__ == "__main__":
    from get_category_members import get_uris
    category = "Category:Clothing_illustrations"
    uris = get_uris(category)
    retrieve_category(category, uris)
