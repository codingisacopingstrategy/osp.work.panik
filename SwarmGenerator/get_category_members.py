#!/usr/bin/env python
# -*- coding: utf-8 -*-
# our departure point is http://commons.wikimedia.org/wiki/Category:Illustrations_by_subject

import sys
import os
import json
import urllib2
from urllib import quote
from flask import Flask, render_template, send_file
from retrieve import retrieve_category
from swarm_bot import swarm_bot
from convert_images import convert_images

PATH = os.path.join('/', 'tmp','panik')
app = Flask(__name__)

def urlencode(s):
    return quote(s)

app.jinja_env.filters['urlencode'] = urlencode

def make_api_query(category, q_continue=""):
    url = 'http://commons.wikimedia.org/w/api.php?action=query&generator=categorymembers&gcmtitle=' + quote(category) + '&gcmlimit=500&prop=imageinfo&iiprop=url&iiurlwidth=120&format=json'
    response = json.loads(urllib2.urlopen(url).read())
    response['url'] = url
    return response

@app.route("/<category>")
def display(category):
    response=make_api_query(category)
    members = []
    files = []
    for i in response['query']['pages'].values():
        if 'Category' in i['title']:
            members.append(i)
        elif 'File' in i['title'] and 'jpg' in i['imageinfo'][0]['url']:
            files.append(i)
    return render_template('view_basic.html', members=members, files=files, category=category)

def get_uris(category):
    response=make_api_query(category)
    uris = []
    for i in response['query']['pages'].values():
        try:
            uri = i['imageinfo'][0]['thumburl']
            if 'jpg' in uri:
                uris.append(uri)
        except KeyError:
            pass
    return uris

@app.route("/<category>.svg")
def generate(category):
    uris = get_uris(category)
    if len(uris) > 32:
        uris = uris[:32]
    retrieve_category(category, uris)
    convert_images(category)
    swarm_bot(category)
    return send_file(os.path.join(PATH, "%s.svg" % quote(category)))

@app.route("/")
def hello():
    return display("Category:Illustrations_by_subject")

if __name__ == "__main__":
    app.run(debug=True)