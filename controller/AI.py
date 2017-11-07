# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 15:01:39
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-07 11:57:10
from model.Message import Message, MsgType
from controller.System import System

import random

class AIType():
	AIType_Zombie = 0

class AI(System):
	def __init__(self, msgBus):
		System.__init__(self, msgBus)
		self.subscriptions.extend([MsgType.eMsgType_SubscribeAI, MsgType.eMsgType_AddEntity, MsgType.eMsgType_RemoveEntity])
		self.agents = []
		self.entities = []

	def addEntity(self, entity):
		if entity not in self.entities:
			self.entities.append(entity)

	def removeEntity(self, entity):
		if entity in self.entities:
			self.entities.remove(entity)

	def init(self):
		System.init(self)

	def handleMessage(self, msg):
		if msg.msgType == MsgType.eMsgType_SubscribeAI:
			self.agents.append(msg.data)
		elif msg.msgType == MsgType.eMsgType_AddEntity:
			self.addEntity(msg.data)
		elif msg.msgType == MsgType.eMsgType_RemoveEntity:
			self.removeEntity(msg.data)

	def move(self, entity, vector2D):
		msg = Message(sender=self, target=None, msgType=MsgType.eMsgType_MoveEntity, data={"entity" : entity, "vector2D" : vector2D})
		self.msgBus.postMessage(msg)

	def lookAround(self, agent):
		surroundingEntities = []
		for entity in self.entities:
			if abs(agent.x - entity.x) <= agent.sightRange and abs(agent.y - entity.y) <= agent.sightRange:
				surroundingEntities.append(entity)
		return surroundingEntities

	def updateAgent(self, agent):
		if agent.aiType == AIType.AIType_Zombie:
			print(self.lookAround(agent))
			#vector2D = entity.moves[random.randint(0, len(entity.moves)-1)]
			#self.move(entity, vector2D)

	def update(self):
		for agent in self.agents:
			self.updateAgent(agent)