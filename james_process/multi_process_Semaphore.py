import multiprocessing
import time

def worker(s, i):
    s.acquire()
    print(time.strftime('%H:%M:%S'),multiprocessing.current_process().name + " 获得锁运行");
    time.sleep(i)
    print(time.strftime('%H:%M:%S'),multiprocessing.current_process().name + " 释放锁结束");
    s.release()

if __name__ == "__main__":
    s = multiprocessing.Semaphore(2)
    for i in range(6):
        p = multiprocessing.Process(target = worker, args=(s, 2))
        p.start()