import threading,time

import queue


#先进先出
q = queue.Queue(maxsize=5)
#q = queue.LifoQueue(maxsize=3)
#q = queue.PriorityQueue(maxsize=3)

def ProducerA():
    count = 1
    while True:
        q.put(f"冷饮 {count}")
        print(f"{time.strftime('%H:%M:%S')} A 放入:[冷饮 {count}]")
        count +=1
        time.sleep(1)

def  ConsumerB():
    while True:
        print(f"{time.strftime('%H:%M:%S')} B 取出 [{q.get()}]")
        time.sleep(5)

p = threading.Thread(target=ProducerA)
c = threading.Thread(target=ConsumerB)
c.start()
p.start()

