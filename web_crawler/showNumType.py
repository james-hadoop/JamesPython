#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

class ShowNumType(object):
	def __init__(self):
		self.showInt()
		self.showLong()
		self.showFloat()
		self.showComplex()

	def showInt(self):
		print(u"##########显示整型#############")
		print(u"十进制的整型")
		print("%-20d,%-20d,%-20d" %(-10000,0,10000))
		print(u"二进制的整型")
		print("%-20s,%-20s,%-20s" %(bin(-10000),bin(0),bin(10000)))
		print(u"八进制的整型")
		print("%-20s,%-20s,%-20s" %(oct(-10000),oct(0),oct(10000)))
		print(u"十六进制的整型")
		print("%-20s,%-20s,%-20s" %(hex(-10000),hex(0),hex(10000)))

	def showLong(self):
		print(u"##########显示长整型#############")
		print(u"十进制的整型")
		print("%-20Ld,%-20Ld,%-20Ld" %(-10000000000000000000,0,10000000000000000000))
		print(u"八进制的整型")
		print("%-20s,%-20s,%-20s" %(oct(-10000000000000000000),oct(0),oct(10000000000000000000)))
		print(u"十六进制的整型")
		print("%-20s,%-20s,%-20s" %(hex(-10000000000000000000),hex(0),hex(10000000000000000000)))

	def showFloat(self):
		print(u"##########显示浮点型#############")
		print("%-20.10f,%-20.10f,%-20.10f" %(-100.001,0,100.001))

	def showComplex(self):
		print(u"##########显示复数型#############")
		print(u"变量赋值复数 var = 3 + 4j")
		var = 3 + 4j
		print(u"var的实部是：%d\tvar的虚部是：%d" %(var.real,var.imag))


if __name__ == '__main__':
	showNum = ShowNumType()
