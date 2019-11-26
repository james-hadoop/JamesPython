#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import random

class GuessNum(object):
	'''这个类用于猜随机数 '''
	def __init__(self):
		print(u"随机产生一个0-100的随机数")
		self.num = random.randint(0,101)
		self.guess()

	def guess(self):
		i = 0
		while True:
			print(u"猜这个随机数，0-100")
			strNum = raw_input("输入你猜的数字:")
			i += 1
			try:
				print("****************")
				if int(strNum) < self.num:
					print(u"你猜得太小了")
					continue
				elif int(strNum) > self.num:
					print(u"你猜得太大了")
					continue
				else:
					print(u"你总算是猜对了")
					print(u"你总共猜了%d次" %i)
					break
			except ValueError:
				print(u"只能输入数字，继续猜吧")
				continue
			print(u"如果没有continue或break，就会显示这个，要不要试试？")


if __name__ == '__main__':
	gn = GuessNum()
