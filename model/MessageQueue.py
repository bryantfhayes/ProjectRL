# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 13:22:57
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-07 09:12:27

import sys
if sys.version_info >= (3, 0):
	from queue import Queue
else:
	from Queue import Queue
from model.Message import Message

class MessageQueue(Queue):
	def __init__(self):
		Queue.__init__(self)