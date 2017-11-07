# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 14:55:37
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-06 15:22:12
# 
from controller.MessageBus import MessageBus
from controller.Console import Console
from controller.Physics import Physics
from controller.Audio import Audio
from controller.Renderer import Renderer
from controller.AI import AI
from controller.Logic import Logic
from controller.Input import Input
from model.Message import Message, MsgType
from controller import Utilities

import time

class Engine():
	def __init__(self):
		self.msgBus = MessageBus()
		self.systems = []
		self.running = False
		self.count = 0
		self.initialized = False
		self.lastUpdated = time.time()

	def init(self, windowWidth, windowHeight):
		self.initialized = True

		# Initialize self and all sub-systems
		self.console = Console(self.msgBus)
		self.console.init()
		self.systems.append(self.console)

		self.physics = Physics(self.msgBus)
		self.physics.init()
		self.systems.append(self.physics)

		self.audio = Audio(self.msgBus)
		self.audio.init()
		self.systems.append(self.audio)

		self.renderer = Renderer(self.msgBus)
		self.renderer.init(width=windowWidth, height=windowHeight)
		self.systems.append(self.renderer)

		self.ai = AI(self.msgBus)
		self.ai.init()
		self.systems.append(self.ai)
		
		self.input = Input(self.msgBus)
		self.input.init()
		self.systems.append(self.input)

	def update(self):
		while (not self.msgBus.isEmpty()):
			message = self.msgBus.getMessage()

			# Check for quit message
			if message.msgType == MsgType.eMsgType_Quit:
				self.running = False

			for system in self.systems:
				if message.msgType in system.subscriptions:
					system.handleMessage(message)

		for system in self.systems:
			system.update()

	def run(self):
		if (self.initialized == False):
			printf("Please call engine.init() first!")
			return

		self.running = True
		while (self.running):
			self.update()
