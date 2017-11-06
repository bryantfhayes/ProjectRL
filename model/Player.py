# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 14:02:44
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-06 14:04:05

class Player(Entity):
	def __init__(self, initialX, initialY):
		Entity.__init__(self, initialX, initialY)