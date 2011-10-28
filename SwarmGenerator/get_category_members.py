#!/usr/bin/env python
# -*- coding: utf-8 -*-
# our departure point is http://commons.wikimedia.org/wiki/Category:Illustrations_by_subject

import sys
import json
import urllib2
from urllib import quote
from flask import Flask, render_template

app = Flask(__name__)

def make_api_query(category, q_continue=""):
    url = 'http://commons.wikimedia.org/w/api.php?action=query&generator=categorymembers&gcmtitle=' + quote(category) + '&gcmlimit=500&prop=imageinfo&iiprop=url&format=json'
    response = json.loads(urllib2.urlopen(url).read())
    return response

@app.route("/<category>")
def display(category):
    response=make_api_query(category)
    members = (i for i in response['query']['pages'].values() if 'Category' in i['title'])
    return render_template('view_basic.html', members=members)


@app.route("/")
def hello():
    return display("Category:Illustrations_by_subject")

if __name__ == "__main__":
    app.run(debug=True)