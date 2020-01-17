import multiprocessing
import time


def task1():
    n = 5
    while n > 1:
        print(f"{time.strftime('%H:%M:%S')} task1 输出信息")
        time.sleep(1)
        n -= 1


def task2():
    n = 5
    while n > 1:
        print(f"{time.strftime('%H:%M:%S')} task2 输出信息")
        time.sleep(1)
        n -= 1


def task3():
    n = 5
    while n > 1:
        print(f"{time.strftime('%H:%M:%S')} task3 输出信息")
        time.sleep(1)
        n -= 1


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=task1)
    p2 = multiprocessing.Process(target=task2)
    p3 = multiprocessing.Process(target=task3)
    p1.start()
    p2.start()
    p3.start()
