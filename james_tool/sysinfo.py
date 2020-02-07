import psutil

#监控cpu信息
psutil.cpu_times(percpu=True)   # 使用cpu_times 方法获取CPU完整信息，需要显示所有逻辑CPU信息，percpu = True可选
psutil.cpu_times().user         # 获取单项数据信息，如用户user 的CPU 时间比
psutil.cpu_count()              # 获取CPU 的逻辑个数，默认logical=True
psutil.cpu_count(logical=False) # 获取CPU 的物理个数
psutil.cpu_times(percpu=True)  # 获取每个cpu占用时间的详细信
psutil.cpu_percent()


#监控内存信息


psutil.virtual_memory()  # 获取内存信息
(psutil.virtual_memory().total ) # 获取内存总量
(psutil.swap_memory() ) # 获取swap信息
# (psutil.swqp_memory() ) # 获取swap总量
# 监控磁盘信息


psutil.disk_partitions()  # 获取各分区的信息
# psutil.disk_usage()  # 获取各分区的使用情况
psutil.disk_io_counters(perdisk=True)  # 获取各个分区的io情况
# psutil.disk_io_counters(perdisk=True)['sda1'].read_count  # 获取sda1的io读取情况
# 监控网络信息


psutil.net_io_counters()  # 获取所有网络接口io信息
psutil.net_io_counters(pernic=True)  # 获取每个网络接口的io信息

#进程信息


#psutil.Process(pid)  # 查看对应pid的进程信息
#psutil.Process(pid).username()  # 查看是哪个用户创建的该进程
#psutil.Process(pid).cmdline()  # 查看进程所在的路径
# 登录用户信息


psutil.users()  # 查看目前登录用户信息


import psutil

# ps = psutil.Process()
# for p in ps:
#     print(p)


import psutil
for proc in psutil.process_iter():
    try:
        pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
    except psutil.NoSuchProcess:
        pass
    else:
        if pinfo['name'].startswith('WeChat'):
           print(pinfo)

import psutil
for proc in psutil.process_iter(attrs=['pid', 'name', 'username','status','memory_info']):
    if proc.info['name'].startswith('WeChat'):
        print(proc.info)


import psutil

def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(attrs=['name']):
        if p.info['name'] == name:
            ls.append(p)
    return ls

import os
import psutil

def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(attrs=["name", "exe", "cmdline"]):
        if name == p.info['name'] or \
                p.info['exe'] and os.path.basename(p.info['exe']) == name or \
                p.info['cmdline'] and p.info['cmdline'][0] == name:
            ls.append(p)
    return ls

import psutil

def reap_children(timeout=3):
    "Tries hard to terminate and ultimately kill all the children of this process."
    def on_terminate(proc):
        print("process {} terminated with exit code {}".format(proc, proc.returncode))

    procs = psutil.Process().children()
    # send SIGTERM
    for p in procs:
        p.terminate()
    gone, alive = psutil.wait_procs(procs, timeout=timeout, callback=on_terminate)
    if alive:
        # send SIGKILL
        for p in alive:
            print("process {} survived SIGTERM; trying SIGKILL" % p)
            p.kill()
        gone, alive = psutil.wait_procs(alive, timeout=timeout, callback=on_terminate)
        if alive:
            # give up
            for p in alive:
                print("process {} survived SIGKILL; giving up" % p)




