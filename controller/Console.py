# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 15:01:39
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-06 15:24:02
from model.Message import Message, MsgType
from controller.System import System

class Console(System):
	def __init__(self):
		System.__init__(self)
		self.subscriptions = [MsgType.eMsgType_Debug]

	def handleMessage(self, msg):
		if msg.data:
			print("[{0} - {1}] {2}".format(msg.createTime, msg.targetTime, msg.data))

	def update(self):
		pass