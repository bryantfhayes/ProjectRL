# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 15:01:39
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-07 11:55:56
from model.Message import Message, MsgType
from controller.Logic import Logic
from model.Player import Player
from model.Entity import Entity
from controller.AI import AIType

import random

class MyGameLogic(Logic):
	def __init__(self, msgBus):
		Logic.__init__(self, msgBus)
		self.subscriptions.extend([MsgType.eMsgType_KeyPressed, MsgType.eMsgType_KeyReleased])
		self.shiftModifier = False
		self.entities = []

	def addEntity(self, entity):
		# Send message to bus that a new entity is made
		msg = Message(sender=self, target=None, msgType=MsgType.eMsgType_AddEntity, data=entity)
		self.msgBus.postMessage(msg)
		self.entities.append(entity)

	def removeEntityAt(self, x, y):
		toRemove = []
		for entity in self.entities:
			if entity.x == x and entity.y == y:
				msg = Message(sender=self, target=None, msgType=MsgType.eMsgType_RemoveEntity, data=entity)
				self.msgBus.postMessage(msg)

				# Mark for removal
				toRemove.append(entity)

		# Remove all entities from local cache
		for entity in toRemove:
			self.entities.remove(entity)

	def init(self):
		Logic.init(self)

		# Init state of the game...
		self.player = Player(50, 50, "@", self.msgBus, aiType=AIType.AIType_Zombie)
		self.addEntity(self.player)

		# Force camera to follow player entity
		msg = Message(sender=self, target=None, msgType=MsgType.eMsgType_CameraFollowEntity, data=self.player)
		self.msgBus.postMessage(msg)

		self.generateMap(100, 100)

	def handleMessage(self, msg):
		if msg.msgType == MsgType.eMsgType_KeyPressed:
			self.keyPressed(msg.data)
		if msg.msgType == MsgType.eMsgType_KeyReleased:
			self.keyReleased(msg.data)

	def move(self, entity, vector2D):
		msg = Message(sender=self, target=None, msgType=MsgType.eMsgType_MoveEntity, data={"entity" : entity, "vector2D" : vector2D})
		self.msgBus.postMessage(msg)

	def action(self, entity, vector2D):
		# WASD button handling to interact with world
		if self.shiftModifier:
			self.removeEntityAt(entity.x + vector2D[0], entity.y + vector2D[1])
		else:
			self.addEntity(Entity(entity.x + vector2D[0], entity.y + vector2D[1], "#", self.msgBus))

	def keyReleased(self, key):
		if key.upper() == "SHIFT":
			self.shiftModifier = False

	def keyPressed(self, key):
		if key.upper() in MOVEMENT_KEYS:
			self.move(self.player, MOVEMENT_KEYS[key.upper()])
		elif key.upper() in ACTION_KEYS:
			self.action(self.player, ACTION_KEYS[key.upper()])
		elif key.upper() == "SHIFT":
			self.shiftModifier = True
		elif key.upper() == "Q":
			msg = Message(sender=self, target=None, msgType=MsgType.eMsgType_Quit)
			self.msgBus.postMessage(msg)

	def isTouchingCharacter(self, arr, ref, maxWidth, maxHeight, char):
		possibilities = [[ref[0], ref[1]-1], [ref[0]-1, ref[1]], [ref[0], ref[1]+1], [ref[0]+1, ref[1]]]
		for poss in possibilities:
			if poss[0] < 0 or poss[1] < 0 or poss[0] >= maxWidth or poss[1] >= maxHeight:
				continue
			curr = arr[poss[0]][poss[1]]
			if curr != None and curr == char:
				return True
		return False

	def generateMap(self, width, height):
		# Make empty 2D array
		arr = []
		for i in range(width):
			arr.append([])
			for j in range(height):
				arr[i].append(None)

		for y in range(height):
			for x in range(width):
				if self.isTouchingCharacter(arr, (x, y), width, height, '#'):
					chance = .35
				else:
					chance = .1

				# If random chance, or edge piece, add wall
				if (random.uniform(0, 1) < chance) or (x == 0 or y == 0 or x == width-1 or y == height-1):
					wall = Entity(x, y, "#", self.msgBus)
					self.addEntity(wall)
					arr[x][y] = wall.char

	def update(self):
		pass

# Create a dictionary that maps keys to vectors.
# Names of the available keys can be found in the online documentation:
# http://packages.python.org/tdl/tdl.event-module.html
MOVEMENT_KEYS = {
				 # standard arrow keys
				 'UP': [0, -1],
				 'DOWN': [0, 1],
				 'LEFT': [-1, 0],
				 'RIGHT': [1, 0],

				 # diagonal keys
				 # keep in mind that the keypad won't use these keys even if
				 # num-lock is off
				 'HOME': [-1, -1],
				 'PAGEUP': [1, -1],
				 'PAGEDOWN': [1, 1],
				 'END': [-1, 1],

				 # number-pad keys
				 # These keys will always show as KPx regardless if num-lock
				 # is on or off.  Keep in mind that some keyboards and laptops
				 # may be missing a keypad entirely.
				 # 7 8 9
				 # 4   6
				 # 1 2 3
				 'KP1': [-1, 1],
				 'KP2': [0, 1],
				 'KP3': [1, 1],
				 'KP4': [-1, 0],
				 'KP6': [1, 0],
				 'KP7': [-1, -1],
				 'KP8': [0, -1],
				 'KP9': [1, -1],
				 }
ACTION_KEYS = {
				 'W': [0, -1],
				 'S': [0, 1],
				 'A': [-1, 0],
				 'D': [1, 0]
}