# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 15:01:39
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-07 13:07:19
from model.Message import Message, MsgType
from controller.System import System

import socket, json

class NetworkRenderer(System):
	def __init__(self, msgBus, ip, port):
		System.__init__(self, msgBus)
		self.entities = []
		self.following = None
		self.offsetX = 0
		self.offsetY = 0
		self.subscriptions.extend([MsgType.eMsgType_AddEntity, 
								   MsgType.eMsgType_RemoveEntity, 
								   MsgType.eMsgType_CameraFollowEntity])

		self.ip = ip
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	def init(self, width, height, font='assets/arial_16x16.png', name='Renderer'):
		System.init(self)
		self.width = width
		self.height = height

	def handleMessage(self, msg):
		if msg.msgType == MsgType.eMsgType_AddEntity:
			self.addEntity(msg.data)
		elif msg.msgType == MsgType.eMsgType_RemoveEntity:
			self.removeEntity(msg.data)
		elif msg.msgType == MsgType.eMsgType_CameraFollowEntity:
			self.followEntity(msg.data)

	def followEntity(self, entity):
		self.following = entity

	def update(self):
		if self.following != None:
			self.offsetX = int(self.width / 2) - self.following.x
			self.offsetY = int(self.height / 2) - self.following.y
		else:
			self.offsetX = 0
			self.offsetY = 0

		# Draw all entities
		data = {"width" : self.width, "height" : self.height, "entities" : []}
		for entity in self.entities:
			entry = {}

			# If off-screen, dont draw entity
			if entity.x + self.offsetX >= self.width or entity.y + self.offsetY >= self.height or entity.x + self.offsetX < 0 or entity.y + self.offsetY < 0:
				pass
			else:
				if self.following == None:
					entry["char"] = entity.char
					entry["x"] = entity.x + self.offsetX
					entry["y"] = entity.y + self.offsetY
					data["entities"].append(entry)
				elif abs(self.following.x - entity.x) <= self.following.sightRange and abs(self.following.y - entity.y) <= self.following.sightRange:
					entry["char"] = entity.char
					entry["x"] = entity.x + self.offsetX
					entry["y"] = entity.y + self.offsetY
					data["entities"].append(entry)

		jsonData = json.dumps(data)
		msgBytes = jsonData.encode('utf-8')
		print(msgBytes)
		self.sock.sendto(msgBytes, (self.ip, self.port))

	def addEntity(self, entity):
		if entity not in self.entities:
			self.entities.append(entity)

	def removeEntity(self, entity):
		if entity in self.entities:
			self.entities.remove(entity)