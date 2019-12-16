import _thread
import time

# 为线程定义一个函数
def print_time( threadName, delay):
   count = 0
   while count < 3:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# 创建两个线程
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print ("Error: 无法启动线程")

#下面这两步是必须的，否则程序将直接退出
while True:
    time.sleep(1)