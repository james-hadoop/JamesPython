#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

class Annotation(object):
	'''这是一个用户示范注释的类，
多行注释如果在类或者函数的定义之后，
将被默认成doc string。
这里注释的是该类的功能性说明'''
	def __init__(self):
		self.run()

	def run(self):
		"""函数里的doc string，
这里注释的是该函数的功能性说明
注释用单引号和双引号没有任何区别 """
		x = 333 #定义了一个int类型的变量x
		print('x = %d' %x)
		'''好了，这里是单纯的注释了。可以注释多行当然也可以注释单行了 '''


if __name__ == '__main__':
	a = Annotation()
