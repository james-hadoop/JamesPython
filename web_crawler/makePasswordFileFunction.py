#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import os
import platform
import itertools
import time

def main():
	'''主程序 '''
	global rawList #原始数据列表
	rawList = []
	global denyList #非法单词列表
	denyList = [' ','','@']
	global pwList #最终的密码列表
	pwList = []
	global minLen #密码的最小长度
	minLen = 6
	global maxLen #密码的最大长度
	maxLen = 16
	global timeout 
	timeout = 3
	global flag 
	flag = 0
	run = {
'0':exit,
'1':getRawList,
'2':addDenyList,
'3':clearRawList,
'4':setRawList,
'5':modifyPasswordLen,
'6':createPasswordList,
'7':showPassword,
'8':createPasswordFile
}

	while True:
		mainMenu()
		op = raw_input('输入选项:')
		if op in map(str,range(len(run))):
			run.get(op)()
		else:
			tipMainMenuInputError()
			continue

def mainMenu():
	'''主菜单 '''
	global denyList
	global rawList
	global pwList
	global flag
	clear()
	print(u'||'),
	print(u'='*40),
	print(u'||')
	print(u'|| 0:退出程序')
	print(u'|| 1:输入密码原始字符串')
	print(u'|| 2:添加非法字符到列表')
	print(u'|| 3:清空原始密码列表')
	print(u'|| 4:整理原始密码列表')
	print(u'|| 5:改变默认密码长度(%d-%d)' %(minLen,maxLen))
	print(u'|| 6:创建密码列表')
	print(u'|| 7:显示所有密码')
	print(u'|| 8:创建字典文件')
	print(u'||'),
	print(u'='*40),
	print(u'||')
	print(u'当前非法字符为：%s' %denyList)
	print(u'当前原始密码元素为：%s' %rawList)
	print(u'共有密码%d个' %len(pwList))
	if flag:
		print(u"已在当前目录创建密码文件dic.txt")
	else:
		print(u"尚未创建密码文件")
		
def clear():
	'''清屏函数 '''
	OS = platform.system()
	if (OS == u'Windows'):
		os.system('cls')
	else:
		os.system('clear')

def tipMainMenuInputError():
	'''错误提示 '''
	clear()
	print(u"只能输入0-7的整数,等待%d秒后重新输入" %timeout)
	time.sleep(timeout)
	
def getRawList():
	'''获取原始数据列表 '''
	clear()
	global denyList
	global rawList
	print(u"输入回车后直接退出")
	print(u"当前原始密码列表为:%s" %rawList)
	st = None
	while not st == '':
		st = raw_input("请输入密码元素字符串:")
		if st in denyList:
			print(u"这个字符串是预先设定的非法字符串")
			continue
		else:
			rawList.append(st)
			clear()
			print(u"输入回车后直接退出")
			print(u"当前原始密码列表为:%s" %rawList)

def addDenyList():
	'''添加非法词 '''
	clear()
	global denyList
	print(u"输入回车后直接退出")
	print(u"当前非法字符为:%s" %denyList)
	st = None
	while not st == '':
		st = raw_input("请输入需要添加的非法字符串:")
		denyList.append(st)
		clear()
		print(u"输入回车后直接退出")
		print(u"当前非法字符列表为:%s" %denyList)
		
def clearRawList():
	'''清空原始数据列表 '''
	global rawList
	rawList = []

def setRawList():
	'''整理原始数据列表 '''
	global rawList
	global denyList
	a = set(rawList)
	b = set(denyList)
	rawList = []
	for str in set(a - b):
		rawList.append(str)
		
def modifyPasswordLen():
	'''修改默认密码的长度 '''
	clear()
	global maxLen
	global minLen
	while True:
		print(u"当前密码长度为%d-%d" %(minLen,maxLen))
		min = raw_input("请输入密码最小长度:")
		max = raw_input("请输入密码最大长度:")
		try:
			minLen = int(min)
			maxLen = int(max)
		except ValueError:
			print(u"密码长度只能输入数字[6-18]")
			break
		if minLen not in xrange(6,19) or  maxLen not in xrange(6,19):
			print(u"密码长度只能输入数字[6-18]")
			minLen = 6
			maxLen = 16
			continue
		if minLen == maxLen:
			res = raw_input("确定将密码长度设定为%d吗?(Yy/Nn)" %minLen)
			if res not in list('yYnN'):
				print(u"输入错误，请重新输入")
				continue
			elif res in list('yY'):
				print(u"好吧，你确定就好")
				break
			else:
				print(u"给个机会，改一下吧")
				continue
		elif minLen > maxLen:
			print(u"最小长度比最大长度还大，可能吗？请重新输入")
			minLen = 6
			maxLen = 16
			continue
		else:
			print(u"设置完毕，等待%d秒后回主菜单" %timeout)
			time.sleep(timeout)
			break

def createPasswordList():
	'''创建密码列表 '''
	global rawList
	global pwList
	global maxLen
	global minLen
	titleList = []
	swapcaseList = []
	for st in rawList:
		swapcaseList.append(st.swapcase())
		titleList.append(st.title())
	sub1 = []
	sub2 = []
	for st in set(rawList + titleList + swapcaseList):
		sub1.append(st)
	for i in xrange(2,len(sub1) + 1):
		sub2 += list(itertools.permutations(sub1,i))
	for tup in sub2:
		PW = ''
		for subPW in tup:
			PW += subPW
		if len(PW) in xrange(minLen,maxLen + 1):
			pwList.append(PW)
		else:
			pass
		
def showPassword():
	'''显示创建的密码 '''
	global pwList
	global timeout
	for i in xrange(len(pwList)):
		if i%4 == 0:
			print("%s\n" %pwList[i])
		else:
			print("%s\t" %pwList[i]),
	print('\n')
	print(u"显示%d秒，回到主菜单" %timeout)
	time.sleep(timeout)

def createPasswordFile():
	'''创建密码字典文件 '''
	global flag
	global pwList
	print(u"当前目录下创建字典文件:dic.txt")
	time.sleep(timeout)
	with open('./dic.txt','w+') as fp:
		for PW in pwList:
			fp.write(PW)
			fp.write('\n')
	flag = 1


if __name__ == '__main__':
	main()
