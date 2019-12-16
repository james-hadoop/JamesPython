from multiprocessing import Process,Queue
import time

def ProducerA(q):
    count = 1
    while True:
        q.put(f"冷饮 {count}")
        print(f"{time.strftime('%H:%M:%S')} A 放入:[冷饮 {count}]")
        count +=1
        time.sleep(1)

def  ConsumerB(q):
    while True:
        print(f"{time.strftime('%H:%M:%S')} B 取出 [{q.get()}]")
        time.sleep(5)
if __name__ == '__main__':
    q = Queue(maxsize=5)
    p = Process(target=ProducerA,args=(q,))
    c = Process(target=ConsumerB,args=(q,))
    c.start()
    p.start()
    c.join()
    p.join()

