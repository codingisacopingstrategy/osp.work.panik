# -*- coding: utf-8 -*-

import sys
import os
import urllib

class AppURLopener(urllib.FancyURLopener):
    version = 'Mozilla/5.0'

urllib._urlopener = AppURLopener()

def retrieve_uris(path, uris):
    files = []
    if not os.path.exists(path):
        os.makedirs(path)
    for uri in uris:
        filename = uri.split("/")[-1]
        output_file = os.path.join(path, filename)
        if not os.path.exists(output_file):
            urllib.urlretrieve(uri, output_file)
        files.append(output_file)
    return files

if __name__ == "__main__":
    from get_category_members import get_uris
    from urllib import quote
    PATH = os.path.join('/', 'tmp','panik')
    category = "Category:Clothing_illustrations"
    category_path = os.path.join(PATH, quote(category))
    uris = get_uris(category)
    retrieve_uris(category_path, uris)
