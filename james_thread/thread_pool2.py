from multiprocessing.dummy import Pool as ThreadPool
import time


def fun(n):
    time.sleep(2)


start = time.time()
for i in range(5):
    fun(i)
print("单线程顺序执行耗时:", time.time() - start)

start2 = time.time()
# 开8个 worker，没有参数时默认是 cpu 的核心数
pool = ThreadPool(processes=5)
# 在线程中执行 urllib2.urlopen(url) 并返回执行结果
results2 = pool.map(fun, range(5))
pool.close()
pool.join()
print("线程池（5）并发执行耗时:", time.time() - start2)
