from threading import Thread
import os, time

#计算密集型任务
def work():
    res = 0
    for i in range(100000000):
        res *= i

if __name__ == "__main__":
    l = []
    print("本机为",os.cpu_count(),"核 CPU")  # 本机为4核
    start = time.time()
    for i in range(4):
        p = Thread(target=work)  # 多进程
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop = time.time()
    print("计算密集型任务，多线程耗时 %s" % (stop - start))
