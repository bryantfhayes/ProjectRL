# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 15:01:39
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-06 15:24:02
from model.Message import Message, MsgType
from controller.System import System
from playsound import playsound

class Audio(System):
	def __init__(self, msgBus):
		System.__init__(self, msgBus)
		self.subscriptions.extend([MsgType.eMsgType_RemoveEntity])

	def init(self):
		System.init(self)

	def handleMessage(self, msg):
		if msg.msgType == MsgType.eMsgType_RemoveEntity:
			playsound('assets/click.wav', block=False)

	def update(self):
		pass