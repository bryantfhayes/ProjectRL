# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 15:01:39
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-06 15:24:02
from model.Message import Message, MsgType
from controller.Input import Input

# Libtcod library
import socket

class NetworkInput(Input):
	def __init__(self, msgBus, ip, port):
		Input.__init__(self, msgBus)
		self.ip = ip
		self.port = port

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind((self.ip, self.port))
		self.sock.setblocking(0)

	def init(self):
		Input.init(self)

	def update(self):
		# If there is any input from network, relay onto message bus
		try:
			data = self.sock.recv(256).decode('utf-8')
			data = data.split('~')
			if data[0] == "KEYDOWN":
				msg = Message(sender=self, target=None, msgType=MsgType.eMsgType_KeyPressed, data=data[1])
				self.msgBus.postMessage(msg)
			elif data[0] == "KEYUP":
				msg = Message(sender=self, target=None, msgType=MsgType.eMsgType_KeyReleased, data=data[1])
				self.msgBus.postMessage(msg)
		except:
			'''no data yet..'''