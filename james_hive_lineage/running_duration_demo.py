from time import time


def timeTest():
    start = time()
    print("Start: " + str(start))
    for i in range(1, 100000000):
        pass
    stop = time()
    print("Stop: " + str(stop))
    print(str(stop - start) + "秒")


def main():
    timeTest()


if __name__ == '__main__':
    main()
