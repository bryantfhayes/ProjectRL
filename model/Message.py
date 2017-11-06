# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 13:22:32
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-06 15:25:09
import time

class MsgType():
	eMsgType_None = 0
	eMsgType_Debug = 1

class Message():
	def __init__(self, sender, target, msgType, data=None, targetTime=None):
		self.target = target
		self.sender = sender
		self.msgType = msgType
		self.data = data

		# Log time parameters
		currentTime = time.time()
		self.createTime = currentTime
		if targetTime == None:
			self.targetTime = currentTime