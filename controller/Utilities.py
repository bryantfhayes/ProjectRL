# -*- coding: utf-8 -*-
# @Author: Bryant Hayes
# @Date:   2017-11-06 15:19:11
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-06 15:20:51
from controller.MessageBus import MessageBus
from controller.Console import Console
from model.Message import Message, MsgType

def DebugPrint(msgBus, txt):
	msg = Message(None, None, MsgType.eMsgType_Debug, data="Hello!")
	msgBus.postMessage(msg)