#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

class ShowDict(object):
	'''该类用于展示字典的使用方法 '''
	def __init__(self):
		self.spiderMan = self.createDict()
		self.insertDict(self.spiderMan)
		self.modifyDict(self.spiderMan)
		self.operationDict(self.spiderMan)
		self.deleteDict(self.spiderMan)

	def createDict(self):
		print(u"创建字典:")
		print(u"执行命令spiderMan = {'name':'Peter Parker','sex':'male','Nation':'Americ','college':'MIT'}")
		spiderMan = {'name':'Peter Parker','sex':'male','Nation':'Americ','college':'MIT'}
		self.showDict(spiderMan)
		return spiderMan

	def showDict(self,spiderMan):
		print(u"显示字典")
		print(u"spiderMan = "),
		print(spiderMan)
		print('\n')

	def insertDict(self,spiderMan):
		print(u"字典中添加键age，值为31")
		print(u"执行命令spiderMan['age'] = 31")
		spiderMan['age'] = 31
		self.showDict(spiderMan)

	def modifyDict(self,spiderMan):
		print(u"字典修改键'college'的值为'Empire State University'")
		print(u"执行命令spiderMan['college'] = 'Empire State University'")
		spiderMan['college'] = 'Empire State University'
		self.showDict(spiderMan)

	def operationDict(self,spiderMan):
		print(u"字典的其它操作方法")
		print(u"###########################")
		print(u"显示字典所有的键，keyList = spiderMan.keys()")
		keyList = spiderMan.keys()
		print(u"keyList = "),
		print(keyList)
		print('\n')
		print(u"显示字典所有键的值，valueList = spiderMan.values()")
		valueList = spiderMan.values()
		print(u"valueList = "),
		print(valueList)
		print('\n')
		print(u"显示字典所有键和值的元组，itemList = spiderMan.items()")
		itemList = spiderMan.items()
		print(u"itemList = "),
		print(itemList)
		print('\n')
		print(u"取字典中键为college的值,college = spiderman.get('college')")
		college = spiderMan.get('college')
		print(u"college = %s" %college)
		print('\n')
	
	def deleteDict(self,spiderMan):
		print(u"删除字典中键为Nation的值")
		print(u"执行命令 del(spiderMan['Nation'])")
		del(self.spiderMan['Nation'])
		self.showDict(spiderMan)
		print(u"清空字典中所有的值")
		print(u"执行命令 spiderMan.clear()")
		self.spiderMan.clear()
		self.showDict(spiderMan)
		print(u"删除字典")
		print(u"执行命令 del(spiderMan)")
		del(spiderMan)
		print(u"显示spiderMan")
		try:
			self.showDict(spiderMan)
		except NameError:
			print(u"spiderMan 未被定义")


if __name__ == '__main__':
	sd = ShowDict()
