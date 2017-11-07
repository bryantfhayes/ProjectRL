# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 14:04:33
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-06 14:05:21

class System():
	def __init__(self, msgBus):
		self.subscriptions = []
		self.initialized = False
		self.msgBus = msgBus

	# VIRTUAL
	def init(self):
		self.initialized = True

	# VIRTUAL
	def handleMessage(self, msg):
		pass

	# VIRTUAL
	def update(self):
		pass