import multiprocessing
import time


def task1(pipe):
    for i in range(5):
        str = f"task1-{i}"
        print(f"{time.strftime('%H:%M:%S')} task1 发送：{str}")
        pipe.send(str)
    time.sleep(2)
    for i in range(5):
        print(f"{time.strftime('%H:%M:%S')} task1 接收: { pipe.recv() }")


def task2(pipe):
    for i in range(5):
        print(f"{time.strftime('%H:%M:%S')} task2 接收: { pipe.recv() }")
    time.sleep(1)
    for i in range(5):
        str = f"task2-{i}"
        print(f"{time.strftime('%H:%M:%S')} task2 发送：{str}")
        pipe.send(str)


if __name__ == "__main__":
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=task1, args=(pipe[0],))
    p2 = multiprocessing.Process(target=task2, args=(pipe[1],))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
