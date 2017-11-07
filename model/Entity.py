# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 14:02:40
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-07 11:47:13

from model.Message import MsgType, Message 

class Entity():
	def __init__(self, initialX, initialY, char, msgBus, aiType=None):
		self.x = initialX
		self.y = initialY
		self.char = char
		self.aiType = aiType
		self.msgBus = msgBus
		self.moves = [[0, 1], [-1, 0], [1, 0], [0, -1]]
		self.sightRange = 5
		if aiType != None:
			msg = Message(sender=self, target=None, msgType=MsgType.eMsgType_SubscribeAI, data=self)
			self.msgBus.postMessage(msg)