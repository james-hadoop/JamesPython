from multiprocessing import Process
import os, time

#I/0密集型任务
def work():
    time.sleep(2)
    print("===>", file=open("tmp.txt", "w"))

if __name__ == "__main__":
    l = []
    print("本机为", os.cpu_count(), "核 CPU")  # 本机为4核
    start = time.time()
    for i in range(400):
        p = Process(target=work)  # 多进程
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop = time.time()
    print("I/0密集型任务，多进程耗时 %s" % (stop - start))