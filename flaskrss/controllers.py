#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import render_template
from flaskrss import app

import feedparser

RSS_FEED = "http://planetpython.org/rss20.xml"

@app.route('/')
def get_feed():
    feed_results = feedparser.parse(RSS_FEED)

    return render_template("index.html", posts=feed_results["entries"])
