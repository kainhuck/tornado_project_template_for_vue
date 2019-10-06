#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tornado.web
from views import index
import os
import config


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [

            # StaticFileHandler,注意要放在所有路由的最下面
            (r'/(.*)$', index.StaticFileHandler_,
             {"path": os.path.join(config.BASE_DIRS, 'static/html'), "default_filename": "index.html"})
        ]
        super(Application, self).__init__(handlers, **config.settings)
