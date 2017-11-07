# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 14:02:44
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-07 11:34:36

from model.Entity import Entity

class Player(Entity):
	def __init__(self, initialX, initialY, char, msgBus, aiType=None):
		Entity.__init__(self, initialX, initialY, char, msgBus, aiType)