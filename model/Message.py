# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 13:22:32
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-07 09:58:06
import time

class MsgType():
	eMsgType_None = 0
	eMsgType_Debug = 1
	eMsgType_AddEntity = 2
	eMsgType_RemoveEntity = 3
	eMsgType_KeyPressed = 4
	eMsgType_CameraFollowEntity = 5
	eMsgType_MoveEntity = 6
	eMsgType_KeyReleased = 7
	eMsgType_Quit = 8
	eMsgType_SubscribeAI = 9

class Message():
	def __init__(self, sender, target, msgType, data=None, targetTime=None):
		self.target = target
		self.sender = sender
		self.msgType = msgType
		self.data = data

		# Log time parameters
		currentTime = time.time()
		self.createTime = currentTime
		if targetTime == None:
			self.targetTime = currentTime