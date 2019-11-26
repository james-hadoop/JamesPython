#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

class ShowTuple(object):
	def __init__(self):
		self.T1 = ()
		self.createTuple()
		self.subTuple(self.T1)
		self.tuple2List(self.T1)

	def createTuple(self):
		print(u"创建元组：")
		print(u"T1 = (1,2,3,4,5,6,7,8,9,10)")
		self.T1 = (1,2,3,4,5,6,7,8,9,10)
		print(u"T1 = "),
		print(self.T1)
		print('\n')

	def subTuple(self,Tuple):
		print(u"元组分片：")
		print(u"取元组T1的第4个到最后一个元组组成的新元组，执行命令T1[3:]")
		print(self.T1[3:])
		print(u"取元组T1的第2个到倒数第2个元素组成的新元组，步长为2，执行命令T1[1:-1:2]")
		print(self.T1[1:-1:2])
		print('\n')

	def tuple2List(self,Tuple):
		print(u"元组转换成列表：")
		print(u"显示元组")
		print(u"T1 = "),
		print(self.T1)
		print(u"执行命令 L2 = list(T1)")
		L2 = list(self.T1)
		print(u"显示列表")
		print(u"L2 = "),
		print(L2)
		print(u"列表追加一个元素100后，转换成元组。执行命令L2.append(100) tuple(L2)")
		L2.append(100)
		print(u"显示新元组")
		print(tuple(L2))


if __name__ == '__main__':
	st = ShowTuple()
