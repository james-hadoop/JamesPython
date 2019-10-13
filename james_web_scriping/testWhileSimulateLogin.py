#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import getpass

class FakeLogin(object):
	def __init__(self):
		self.name = 'king'
		self.password = 'haha,no pw'
		self.banner = 'hello, you have login system'
		self.run()

	def run(self):
		'''仿Linux终端登录窗口'''
		print(u"不好意思，只有一个用户king")
		print(u"偷偷的告诉你，密码是6个8哦")
		while True:
			print(u"Login:king")
			pw = getpass.getpass("Password:")
			if pw == '88888888':
				print(u"%s" %self.banner)
				print(u"退出程序")
				exit()
			else:
				if len(pw) > 12:
					print(u"密码长度应该小于12")
					continue
				elif len(pw) < 6:
					print(u"密码长度大于6才对")
					continue
				else:
					print(u"可惜，密码错误。继续猜")
					continue

				
if __name__ == '__main__':
	fl = FakeLogin()
