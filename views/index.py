import tornado.web
from tornado.web import RequestHandler, StaticFileHandler

# 上传文件使用
import config
import os

# 数据库使用
# from models import ClassName

# 定义自己的StaticFileHandler
class StaticFileHandler_(StaticFileHandler):
	def __init__(self, *args, **kwargs):

		super(StaticFileHandler, self).__init__(*args, **kwargs)
		self.xsrf_token

'''
# 在这里创建你的Handlers
class YourHandler(RequestHandler):
	pass
'''
