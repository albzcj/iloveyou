#!/usr/bin/env python
# coding=utf-8
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
import os.path

from client import IndexHandler

application = tornado.web.Application(
    [
        (r"/", IndexHandler),
    ],
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    debug=True,
    )
