# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 13:29:42
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-06 15:12:30
from model.MessageQueue import MessageQueue

class MessageBus():
	def __init__(self):
		self._queue = MessageQueue()

	def postMessage(self, msg):
		self._queue.put(msg)

	def peekNextMessage(self):
		if not self._queue.empty():
			return self._queue.queue[0]
		return None

	def peekQueueAsList(self):
		return self._queue.queue

	def isEmpty(self):
		return self._queue.empty()

	def getMessage(self):
		return self._queue.get()