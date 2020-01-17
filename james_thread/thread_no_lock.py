#!/usr/local/bin/python3
#-*- coding: utf-8 -*-
#Time: 2018/10/14 10:14:17
#Description:
#File Name: thread_no_lock.py

import time, threading

num = 0

def task_thread(n):
   global num
   for i in range(1000000):
       num = num + n
       num = num - n

t1 = threading.Thread(target=task_thread, args=(6,))
t2 = threading.Thread(target=task_thread, args=(17,))
t3 = threading.Thread(target=task_thread, args=(11,))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print(num)
