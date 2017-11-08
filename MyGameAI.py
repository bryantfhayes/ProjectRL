# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 15:01:39
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-07 16:57:35
from model.Message import Message, MsgType
from controller.AI import AI

import random

class AIType():
	AIType_Zombie = 0

class MyGameAI(AI):
	def __init__(self, msgBus):
		AI.__init__(self, msgBus)

	def init(self):
		AI.init(self)

	def updateAgent(self, agent):
		if agent.aiType == AIType.AIType_Zombie:
			vector2D = agent.moves[random.randint(0, len(agent.moves)-1)]
			self.move(agent, vector2D)