# -*- coding:utf-8 -*-
"""
    index action demo
    author comger@gmail.com
"""
import tornado

from tornado import gen
from kpages import url, ContextHandler, LogicContext, get_context, service_async


@url(r"/")
class IndexHandler(ContextHandler,tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


@url(r"/company/about")
@url(r"/company/about.html")
class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('about.html')
    
@url(r"/company/zizhi.html")
class ZiziHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('zizi.html')


@url(r"/solution.html")
class SolutionHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('solution.html')
