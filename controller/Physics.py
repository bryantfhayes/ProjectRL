# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 15:01:39
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-06 15:24:02
from model.Message import Message, MsgType
from controller.System import System

import time

class Physics(System):
	def __init__(self, msgBus):
		System.__init__(self, msgBus)
		self.subscriptions.extend([MsgType.eMsgType_MoveEntity, MsgType.eMsgType_AddEntity, MsgType.eMsgType_RemoveEntity])
		self.entities = []
		self.lastUpdated = time.time()

	def init(self):
		System.init(self)

	def addEntity(self, entity):
		if entity not in self.entities:
			self.entities.append(entity)

	def removeEntity(self, entity):
		if entity in self.entities:
			self.entities.remove(entity)

	def handleMessage(self, msg):
		if msg.msgType == MsgType.eMsgType_MoveEntity:
			self.moveEntity(msg.data["entity"], msg.data["vector2D"])
		elif msg.msgType == MsgType.eMsgType_AddEntity:
			self.addEntity(msg.data)
		elif msg.msgType == MsgType.eMsgType_RemoveEntity:
			self.removeEntity(msg.data)

	def isValidLocation(self, entity, x, y):
		# TODO: Fix later, now it just prevents an entity to moving onto the same loc as another
		for e in self.entities:
			if e.x == x and e.y == y:
				return False
		return True

	def moveEntity(self, entity, vector2D):
		targetX = entity.x + vector2D[0]
		targetY = entity.y + vector2D[1]
		if self.isValidLocation(entity, targetX, targetY):
			entity.x = targetX
			entity.y = targetY
			return True
		return False

	def update(self):
		# Limit frame rate
		while (time.time() - self.lastUpdated) < (1.0 / 40.0):
			pass
		#print(time.time() - self.lastUpdated)
		self.lastUpdated = time.time()