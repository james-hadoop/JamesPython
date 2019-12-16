from multiprocessing import Process
import os
import time
# 子进程要执行的代码
def task_process(delay):
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} 子进程执行开始。")
    print(f"sleep {delay}s")
    time.sleep(delay)
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} 子进程执行结束。")

if __name__=='__main__':
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} 父进程执行开始。")
    p0 = Process(target=task_process, args=(3,))
    #设置 daemon属性为True
    p0.daemon = True
    p0.start()
    p0.join()
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} 父进程执行结束。")
