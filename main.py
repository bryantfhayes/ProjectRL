# -*- coding: utf-8 -*-
# @Author: bhayes
# @Date:   2017-11-06 13:08:59
# @Last Modified by:   Bryant Hayes
# @Last Modified time: 2017-11-06 15:06:13
import tdl
from controller.Engine import Engine

def main():
	print("Launching ProjectRL...")
	engine = Engine()
	engine.run()

if __name__ == "__main__":
	main()