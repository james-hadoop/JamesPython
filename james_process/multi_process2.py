from multiprocessing import Process
import os
import time


class MyProcess(Process):
    def __init__(self, delay):
        super().__init__()
        self.delay = delay

    # 子进程要执行的代码
    def run(self):
        num = 0
        #for i in range(self.delay * 100000000):
        for i in range(self.delay * 100000):
            num += i
        print(f"进程pid为 {os.getpid()},执行完成")


if __name__ == "__main__":
    print("父进程pid为 %s." % os.getpid())
    p0 = MyProcess(3)
    p1 = MyProcess(3)
    t0 = time.time()
    print(p0.authkey)
    p0.start()
    p1.start()
    p0.join()
    p1.join()
    t1 = time.time()
    print(f"多进程并发执行耗时 {t1-t0}")
