# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 13:22:57
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-06 14:08:15
from queue import Queue
from model.Message import Message

class MessageQueue(Queue):
	def __init__(self):
		Queue.__init__(self)