#!/usr/bin/env python
# -*- coding:utf-8 -*-

# WebApp的启动文件，负责初始化数据库、初始化Web框架，然后加载urls.py，最后启动Web服务

import logging; logging.basicConfig(level=logging.INFO)

import os

from transwarp import db
from transwarp.web import WSGIApplication, Jinja2TemplateEngine

from config import configs

# init db:
db.create_engine(**configs.db)

# init wsgi app:
wsgi = WSGIApplication(os.path.dirname(os.path.abspath(__file__)))

template_engine = Jinja2TemplateEngine(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))

wsgi.template_engine = template_engine

import urls

wsgi.add_module(urls)

if __name__ == '__main__':
    wsgi.run(9000)