# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 14:55:37
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-06 15:22:12
# 
from controller.MessageBus import MessageBus
from controller.Console import Console
from model.Message import Message, MsgType
from controller import Utilities

class Engine():
	def __init__(self):
		self.msgBus = MessageBus()
		self.systems = [Console()]
		self.running = False
		self.count = 0

	def update(self):
		while (not self.msgBus.isEmpty()):
			message = self.msgBus.getMessage()
			for system in self.systems:
				if message.msgType in system.subscriptions:
					system.handleMessage(message)

		for system in self.systems:
			system.update()

		self.count += 1
		if self.count % 100000 == 0:
			Utilities.DebugPrint(self.msgBus, "Hello World!")

	def run(self):
		self.running = True
		while (self.running):
			self.update()