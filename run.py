#!/usr/bin/env python
# coding=utf-8
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
import logging
from tornado.options import define, options
define("port", default=8888, help="run on the gievn port", type=int)
from mylove import application

app = application

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(app)
    tornado.options.parse_command_line()
    logging.info("server start")
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
