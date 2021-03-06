# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 15:01:39
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-06 15:24:02
from model.Message import Message, MsgType
from controller.System import System

class Logic(System):
	def __init__(self, msgBus):
		System.__init__(self, msgBus)

	def init(self):
		System.init(self)

	# VIRTUAL
	def handleMessage(self, msg):
		pass

	# VIRTUAL
	def update(self):
		pass