#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask
import feedparser

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'
