#coding: utf-8
import multiprocessing
import time

def task(name):
    print(f"{time.strftime('%H:%M:%S')}: {name} 开始执行")
    time.sleep(3)

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes = 3)
    for i in range(10):
        #维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
        pool.apply_async(func = task, args=(i,))
    pool.close()
    pool.join()
    print("hello")
