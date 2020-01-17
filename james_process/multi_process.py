from multiprocessing import Process
import os
import time
# 子进程要执行的代码
def task_process(delay):
    num  = 0
    for i in range(delay*100000000):
        num+=i
    print(f"进程pid为 {os.getpid()},执行完成")

if __name__=='__main__':
    print( '父进程pid为 %s.' % os.getpid())
    t0 = time.time()
    task_process(3)
    task_process(3)
    t1 = time.time()
    print(f"顺序执行耗时 {t1-t0} ")
    p0 = Process(target=task_process, args=(3,))
    p1 = Process(target=task_process, args=(3,))
    t2 = time.time()
    p0.start();p1.start()
    p0.join();p1.join()
    t3 = time.time()
    print(f"多进程并发执行耗时 {t3-t2}")
