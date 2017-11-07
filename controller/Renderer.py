# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 15:01:39
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-06 15:24:02
from model.Message import Message, MsgType
from controller.System import System

# Libtcod library
import tdl

class Renderer(System):
	def __init__(self, msgBus):
		System.__init__(self, msgBus)
		self.entities = []
		self.following = None
		self.offsetX = 0
		self.offsetY = 0
		self.subscriptions.extend([MsgType.eMsgType_AddEntity, 
								   MsgType.eMsgType_RemoveEntity, 
								   MsgType.eMsgType_CameraFollowEntity])

	def init(self, width, height, font='assets/arial_16x16.png', name='Renderer'):
		System.init(self)
		self.width = width
		self.height = height

		# Set rendered font
		tdl.setFont(font)

		# Create console window
		self.window = tdl.init(self.width, self.height, name)

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
		# Clean window
		self.window.clear()

		if self.following != None:
			self.offsetX = int(self.width / 2) - self.following.x
			self.offsetY = int(self.height / 2) - self.following.y
		else:
			self.offsetX = 0
			self.offsetY = 0

		# Draw all entities
		for entity in self.entities:
			# If off-screen, dont draw entity
			if entity.x + self.offsetX >= self.width or entity.y + self.offsetY >= self.height or entity.x + self.offsetX < 0 or entity.y + self.offsetY < 0:
				pass
			else:
				self.window.drawChar(entity.x + self.offsetX, entity.y + self.offsetY, entity.char)

		# Write window to screen
		tdl.flush()

	def addEntity(self, entity):
		if entity not in self.entities:
			self.entities.append(entity)

	def removeEntity(self, entity):
		if entity in self.entities:
			self.entities.remove(entity)