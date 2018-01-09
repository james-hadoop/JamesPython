#!/usr/bin/env python
#-*- coding: GBK -*-
__author__ = 'hstking hstking@hotmail.com'

def strCase():
    "字符串大小写转换"
    print "演示字符串大小写转换"
    print "演示字符串S赋值为：'  ThIs is a PYTHON  '"
    S = '  ThIs is a PYTHON  '
    print "大写转换成小写：\tS.lower() \t= %s"%(S.lower())
    print "小写转换成大写：\tS.upper() \t= %s"%(S.upper())
    print "大小写转换：\t\tS.swapcase() \t= %s"%(S.swapcase())
    print "首字母大写：\t\tS.title() \t= %s"%(S.title())
    print '\n'

def strFind():
    "字符串搜索、替换"
    print "演示字符串搜索、替换等"
    print "演示字符串S赋值为：'  ThIs is a PYTHON  '"
    S = '  ThIs is a PYTHON  '
    print "字符串搜索：\t\tS.find('is') \t= %s"%(S.find('is'))
    print "字符串统计：\t\tS.count('s') \t= %s"%(S.count('s'))
    print "字符串替换：\t\tS.replace('Is','is') = %s"%(S.replace('Is','is'))
    print "去左右空格：\t\tS.strip() \t=#%s#"%(S.strip())
    print "去左边空格：\t\tS.lstrip() \t=#%s#"%(S.lstrip())
    print "去右边空格：\t\tS.rstrip() \t=#%s#"%(S.rstrip())
    print '\n'
    
def strSplit():
    "字符串分割、组合"
    print "演示字符串分割、组合"
    print "演示字符串S赋值为：'  ThIs is a PYTHON  '"
    S = '  ThIs is a PYTHON  '
    print "字符串分割：\t\tS.split() \t= %s"%(S.split())
    print "字符串组合1： '#'.join(['this','is','a','python']) \t= %s"%('#'.join(['this','is','a','python']))
    print "字符串组合2： '$'.join(['this','is','a','python']) \t= %s"%('$'.join(['this','is','a','python']))
    print "字符串组合3： ' '.join(['this','is','a','python']) \t= %s"%(' '.join(['this','is','a','python']))
    print '\n'

def strCode():
    "字符串编码、解码"
    print "演示字符串编码、解码"
    print "演示字符串S赋值为：'编码解码测试'"
    S = '编码解码测试'
    print "GBK编码的S \t = %s"%(S)
    print "GBK编码的S转换unicode编码"
    print "S.decode('GBK')= %s"%(S.decode("GBK"))
    print "GBK编码的S转换成utf8"
    print "S.decode('GBK').encode('utf8') = %s"%(S.decode("GBK").encode("utf8"))
    print "注意：不管是编码还是解码针对的都是unicode字符编码，\n所以要编码或者解码前必须先将源字符串转换成unicode编码格式"
    print '\n'

def strTest():
    "字符串测试"
    print "演示字符串测试"
    print "演示字符串S赋值为：'abcd'"
    S1 = 'abcd'
    print "测试S.isalpha() = %s"%(S1.isalpha())
    print "测试S.isdigit() = %s"%(S1.isdigit())
    print "测试S.isspace() = %s"%(S1.isspace())
    print "测试S.islower() = %s"%(S1.islower())
    print "测试S.isupper() = %s"%(S1.isupper())
    print "测试S.istitle() = %s"%(S1.istitle())


if __name__ == '__main__':
        strCase()
        strFind()
        strSplit()
        strCode()
        strTest()
