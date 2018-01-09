#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import os
import platform
import itertools
import time

class MakePassword(object):
	def __init__(self):
		self.rawList = []
		self.denyList = ['',' ','@']
		self.pwList = []
		self.minLen = 6
		self.maxLen = 16
		self.timeout = 3
		self.flag = 0
		self.run = {
'0':exit,
'1':self.getRawList,
'2':self.addDenyList,
'3':self.clearRawList,
'4':self.setRawList,
'5':self.modifyPasswordLen,
'6':self.createPasswordList,
'7':self.showPassword,
'8':self.createPasswordFile
}
		self.main()

	def main(self):
		while True:
			self.mainMenu()
			op = raw_input('输入选项:')
			if op in map(str,range(len(self.run))):
				self.run.get(op)()
			else:
				self.tipMainMenuInputError()
				continue

	def mainMenu(self):
		self.clear()
		print(u'||'),
		print(u'='*40),
		print(u'||')
		print(u'|| 0:退出程序')
		print(u'|| 1:输入密码原始字符串')
		print(u'|| 2:添加非法字符到列表')
		print(u'|| 3:清空原始密码列表')
		print(u'|| 4:整理原始密码列表')
		print(u'|| 5:改变默认密码长度(%d-%d)' %(self.minLen,self.maxLen))
		print(u'|| 6:创建密码列表')
		print(u'|| 7:显示所有密码')
		print(u'|| 8:创建字典文件')
		print(u'||'),
		print(u'='*40),
		print(u'||')
		print(u'当前非法字符为：%s' %self.denyList)
		print(u'当前原始密码元素为：%s' %self.rawList)
		print(u'共有密码%d个' %len(self.pwList))
		if self.flag:
			print(u"已在当前目录创建密码文件dic.txt")
		else:
			print(u"尚未创建密码文件")

	def clear(self):
		OS = platform.system()
		if (OS == u'Windows'):
			os.system('cls')
		else:
			os.system('clear')

	def tipMainMenuInputError(self):
		self.clear()
		print(u"只能输入0-7的整数,等待%d秒后重新输入" %timeout)
		time.sleep(timeout)

	def getRawList(self):
		self.clear()
		print(u"输入回车后直接退出")
		print(u"当前原始密码列表为:%s" %self.rawList)
		st = None
		while not st == '':
			st = raw_input("请输入密码元素字符串:")
			if st in self.denyList:
				print(u"这个字符串是预先设定的非法字符串")
				continue
			else:
				self.rawList.append(st)
				self.clear()
				print(u"输入回车后直接退出")
				print(u"当前原始密码列表为:%s" %self.rawList)

	def addDenyList(self):
		self.clear()
		print(u"输入回车后直接退出")
		print(u"当前非法字符为:%s" %self.denyList)
		st = None
		while not st == '':
			st = raw_input("请输入需要添加的非法字符串:")
			self.denyList.append(st)
			self.clear()
			print(u"输入回车后直接退出")
			print(u"当前非法字符列表为:%s" %self.denyList)
	
	def clearRawList(self):
		self.rawList = []

	def setRawList(self):
		a = set(self.rawList)
		b = set(self.denyList)
		self.rawList = []
		for str in set(a - b):
			self.rawList.append(str)

	def modifyPasswordLen(self):
		self.clear()
		while True:
			print(u"当前密码长度为%d-%d" %(self.minLen,self.maxLen))
			min = raw_input("请输入密码最小长度:")
			max = raw_input("请输入密码最大长度:")
			try:
				self.minLen = int(min)
				self.maxLen = int(max)
			except ValueError:
				print(u"密码长度只能输入数字[6-18]")
				break
			if self.minLen not in xrange(6,19) or  self.maxLen not in xrange(6,19):
				print(u"密码长度只能输入数字[6-18]")
				self.minLen = 6
				self.maxLen = 16
				continue
			if self.minLen == self.maxLen:
				res = raw_input("确定将密码长度设定为%d吗?(Yy/Nn)" %self.minLen)
				if res not in list('yYnN'):
					print(u"输入错误，请重新输入")
					continue
				elif res in list('yY'):
					print(u"好吧，你确定就好")
					break
				else:
					print(u"给个机会，改一下吧")
					continue
			elif self.minLen > self.maxLen:
				print(u"最小长度比最大长度还大，可能吗？请重新输入")
				self.minLen = 6
				self.maxLen = 16
				continue
			else:
				print(u"设置完毕，等待%d秒后回主菜单" %self.timeout)
				time.sleep(self.timeout)
				break

	def createPasswordList(self):
		titleList = []
		swapcaseList = []
		for st in self.rawList:
			swapcaseList.append(st.swapcase())
			titleList.append(st.title())
		sub1 = []
		sub2 = []
		for st in set(self.rawList + titleList + swapcaseList):
			sub1.append(st)
		for i in xrange(2,len(sub1) + 1):
			sub2 += list(itertools.permutations(sub1,i))
		for tup in sub2:
			PW = ''
			for subPW in tup:
				PW += subPW
			if len(PW) in xrange(self.minLen,self.maxLen + 1):
				self.pwList.append(PW)
			else:
				pass

	def showPassword(self):
		for i in xrange(len(self.pwList)):
			if i%4 == 0:
				print("%s\n" %self.pwList[i])
			else:
				print("%s\t" %self.pwList[i]),
		print('\n')
		print(u"显示%d秒，回到主菜单" %self.timeout)
		time.sleep(self.timeout)
	
	def createPasswordFile(self):
		print(u"当前目录下创建字典文件:dic.txt")
		time.sleep(self.timeout)
		with open('./dic.txt','w+') as fp:
			for PW in self.pwList:
				fp.write(PW)
				fp.write('\n')
		self.flag = 1


if __name__ == '__main__':
	mp = MakePassword()
