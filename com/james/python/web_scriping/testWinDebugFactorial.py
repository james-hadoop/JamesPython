#!/usr/bin/env python
#-*- coding:GBK -*-

def fac(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fac(n-1)

def main():
    print('这是一个求阶乘的程序\n')
    n = raw_input('请输入一个正整数:')
    try:
        n = int(n)
    except ValueError:
        print('输入错误，要求输入一个正整数，退出重来吧。')
    print('%d! = %d' %(n,fac(n)))


if __name__ == '__main__':
    main()
