# -*- coding: utf-8 -*-

import os
import re
import hashlib
from time import sleep
from random import uniform
from urllib.request import urlopen, Request
from urllib.parse import urlparse, unquote


def safe_filename(url: str, max_length: int = 150) -> str:
    """Convert any URL into a safe, shortened filesystem filename."""
    # 1. Parse and get the last path component
    parsed = urlparse(url)
    original_name = unquote(parsed.path.split("/")[-1])  # decode %D0 etc.

    # 2. Remove query parameters (the ?utm_source=... part)
    if '?' in original_name:
        original_name = original_name.split('?')[0]

    # 3. Transliterate to ASCII + clean unsafe chars
    # Normalize + remove accents
    import unicodedata
    clean = unicodedata.normalize('NFKD', original_name)
    clean = clean.encode('ascii', 'ignore').decode('ascii')

    # Keep only safe characters
    clean = re.sub(r'[^a-zA-Z0-9._-]', '_', clean)
    clean = re.sub(r'_+', '_', clean)  # collapse multiple underscores
    clean = clean.strip('_')

    # 4. Shorten while keeping extension
    name, ext = os.path.splitext(clean)

    if len(name) > max_length:
        # Hash the original cleaned name for uniqueness
        hash_obj = hashlib.sha1(original_name.encode('utf-8'))
        short_hash = hash_obj.hexdigest()[:8]  # 8 hex chars is enough

        name = name[:max_length - 9] + '_' + short_hash

    final_name = name + ext
    return final_name


def retrieve_uris(path, uris):
    files = []
    if not os.path.exists(path):
        os.makedirs(path)
    for uri in uris:
        sleep(1.0 + uniform(0.2, 0.8))  # jitter
        filename = safe_filename(uri)
        output_file = os.path.join(path, filename)
        if not os.path.exists(output_file):
            req = Request(uri, headers={"User-Agent": "PanikGenerator/1.0[](https://github.com/osp/osp.work.panik)"})
            with urlopen(req) as response, open(output_file, 'wb') as out_file:
                out_file.write(response.read())
        files.append(output_file)
    return files


if __name__ == "__main__":
    from panik_app import get_uris
    from urllib import quote
    PATH = os.path.join('/', 'tmp', 'panik')
    category = "Category:Clothing_illustrations"
    category_path = os.path.join(PATH, quote(category))
    uris = get_uris(category)
    retrieve_uris(category_path, uris)
