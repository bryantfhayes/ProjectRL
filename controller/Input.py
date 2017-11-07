# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 15:01:39
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-06 15:24:02
from model.Message import Message, MsgType
from controller.System import System

# Libtcod library
import tdl

IGNORED_INPUTS = ['TEXT']

class Input(System):
	def __init__(self, msgBus):
		System.__init__(self, msgBus)

	def init(self):
		System.init(self)

	def handleMessage(self, msg):
		pass

	def update(self):
		for event in tdl.event.get(): # Iterate over recent events.
			if event.type == 'KEYDOWN':
				if event.keychar not in IGNORED_INPUTS:
					msg = Message(sender=self, target=None, msgType=MsgType.eMsgType_KeyPressed, data=event.keychar)
					self.msgBus.postMessage(msg)
			if event.type == 'KEYUP':
				if event.keychar not in IGNORED_INPUTS:
					msg = Message(sender=self, target=None, msgType=MsgType.eMsgType_KeyReleased, data=event.keychar)
					self.msgBus.postMessage(msg)