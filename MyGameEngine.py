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
from NetworkInput import NetworkInput
from controller.Input import Input
from NetworkRenderer import NetworkRenderer

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

		self.remote_renderer = NetworkRenderer(self.msgBus, "127.0.0.1", 5006)
		self.remote_renderer.init(windowWidth, windowHeight)
		self.systems.append(self.remote_renderer)

		self.remote_input = NetworkInput(self.msgBus, "127.0.0.1", 5005)
		self.remote_input.init()
		self.systems.append(self.remote_input)

		self.input = Input(self.msgBus)
		self.input.init()
		self.systems.append(self.input)

		Engine.init(self, windowWidth, windowHeight)