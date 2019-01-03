#!/usr/bin/env python
# -*-coding:utf-8-*-


from flask import Flask

app = Flask(__name__)


def index():
    return '<h1>hello world!</h1>'


app.add_url_rule('/', 'index', index)
