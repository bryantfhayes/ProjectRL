# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 14:55:37
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-06 15:22:12
# 
from controller.Engine import Engine
from model.Message import Message, MsgType
from controller import Utilities

from MyGameAI import MyGameAI
from MyGameLogic import MyGameLogic

class MyGameEngine(Engine):
	def __init__(self):
		Engine.__init__(self)
	
	def init(self, windowWidth, windowHeight):

		# Custom Game Logic System
		self.logic = MyGameLogic(self.msgBus)
		self.logic.init()
		self.systems.append(self.logic)

		# Custom Game Logic System
		self.ai = MyGameAI(self.msgBus)
		self.ai.init()
		self.systems.append(self.ai)

		Engine.init(self, windowWidth, windowHeight)