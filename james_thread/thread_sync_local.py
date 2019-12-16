# encoding: utf-8
import threading

local_school = threading.local()


def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print("Hello,{} in {}".format(std, threading.current_thread().name))


def process_name(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


if __name__ == "__main__":
    t1 = threading.Thread(target=process_name, args=("Alice",), name="Thread-A")
    t2 = threading.Thread(target=process_name, args=("Bob",), name="Thread-B")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
