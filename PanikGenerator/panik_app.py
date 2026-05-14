#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# our departure point is http://commons.wikimedia.org/wiki/Category:Illustrations_by_subject

import os
import json
import xml.etree.ElementTree as ET
from urllib.request import Request, urlopen
from urllib.parse import quote
from flask import Flask, request, render_template, send_file, make_response
from retrieve import retrieve_uris
from swarm_bot import swarm_bot
from convert_images import convert_images

PATH = os.path.join('/', 'tmp', 'panik')
app = Flask(__name__)


def urlencode(s):
    return quote(s)


app.jinja_env.filters['urlencode'] = urlencode


def make_api_query(category, q_continue="", limit=32):
    url = 'https://commons.wikimedia.org/w/api.php?action=query&generator=categorymembers&gcmtitle=' + quote(
        category) + '&gcmlimit=' + '%s' % limit + '&prop=imageinfo&iiprop=url&iiurlwidth=120&format=json'
    print(url)
    headers = {"User-Agent": "PanikGenerator/1.0[](https://github.com/osp/osp.work.panik)"}
    req = Request(url, headers=headers)
    response = json.loads(urlopen(req).read())
    if response:
        response['url'] = url
    return response


@app.route("/<category>")
def display(category):
    response = make_api_query(category)
    members = []
    files = []
    if not response:
        return make_response("Page not found, 404", 404)
    try:
        for i in response['query']['pages'].values():
            if 'Category' in i['title']:
                members.append(i)
            elif 'File' in i['title'] and 'jpg' in i['imageinfo'][0]['url']:
                files.append(i)
    except:
        # this is bad an error should yield proper error output
        pass
    return render_template('view_basic.html', members=members, files=files, category=category)


def get_uris(category):
    response = make_api_query(category)
    uris = []
    for i in response['query']['pages'].values():
        try:
            uri = i['imageinfo'][0]['thumburl']
            if 'jpg' in uri:
                uris.append(uri)
        except KeyError:
            pass
    return uris


def setsize(s, size):
    tree = ET.parse(s)
    root = tree.getroot()
    root.attrib['width'] = size[0]
    root.attrib['height'] = size[1]
    tree.write(s)


@app.route("/<category>.svg", methods=['GET', 'POST'])
def generate(category):
    category_path = os.path.join(PATH, quote(category))
    colour = "#000000"
    text_data = None
    square = True
    size = ("12cm", "12cm")
    sizes = {"cd": ("12cm", "12cm"),
             "a2": ("42cm", "59.4cm"),
             "a3": ("29.7cm", "42cm"),
             "a4": ("21cm", "29.7cm"),
             "a5": ("14.8cm", "21.0cm")}

    # Process input data
    if request.method == 'POST':
        colour = request.form['colour']
        # For the typographic style, everything becomes
        # UPPERCASE:
        text_data = request.form['text'].upper()
        if request.form['papersize'] != "cd":
            square = False
        size = sizes[request.form['papersize']]

    # Get the uris for collage images
    uris = get_uris(category)

    # Run the SwarmBot
    output_file = category_path + '.svg'
    files = retrieve_uris(category_path, uris)
    swarm_bot(
        output_file, convert_images(
            files, colour=colour), text_data, size, square)

    # Change paper size relative to options
    # setsize(output_file, size)

    response = make_response(send_file(output_file))
    response.headers['Cache-Control'] = "no-cache"
    return response


@app.route("/")
def hello():
    return display("Category:Illustrations_by_subject")


if __name__ == "__main__":
    app.run(debug=True)
