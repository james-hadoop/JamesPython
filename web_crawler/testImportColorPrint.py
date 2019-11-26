#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import sys

class ColorPrint(object):
	def __init__(self,color,msg):
		self.color = color
		self.msg = msg
		self.cPrint(self.color,self.msg)

	def cPrint(self,color,msg):
		colors = {
'black'	:	'\033[1;30;47m',
'red'	:	'\033[1;31;47m',
'green'	:	'\033[1;32;47m',
'yellow':	'\033[1;33;47m',
'blue'	:	'\033[1;34;47m',
'white'	:	'\033[1;37;47m'}
		if color not in colors.keys():
			print(u"输入的颜色暂时没有，按系统默认配置的颜色打印")
		else:
			print(u"输入的颜色有效,开始彩色打印")
			print(u"%s" %colors[color])
			print(msg)
			print(u"\033[0m")
			

if __name__ == '__main__':
	cp = ColorPrint(sys.argv[1],sys.argv[2])
