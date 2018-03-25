import psutil
print("获取cpu信息")
print(psutil.cpu_times())
print(psutil.cpu_times(percpu=True))
print("#获取cpu个数")
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print("#获取内存信息")
print(psutil.virtual_memory())
print(psutil.virtual_memory().total)
print(psutil.virtual_memory().free)
print(psutil.swap_memory())
print("#获取磁盘信息")
print(psutil.disk_partitions())
print(psutil.disk_usage('/'))
print(psutil.disk_io_counters())

print("#网络信息")
print(psutil.net_io_counters())
print(psutil.net_io_counters(pernic=True))

print("当前登录用户信息")
print(psutil.users())
print("系统开机时间")
print(psutil.boot_time())

print("系统所有进程PID")
print(psutil.pids())

print("实例化一个进程")
p=psutil.Process(1083)
print(p.name())
print(p.exe())
print(p.status())
print(p.create_time())
print(p.uids())
print(p.gids())
print(p.cpu_times())
print(p.cpu_affinity())
print(p.memory_percent())
print(p.memory_info())
print(p.io_counters())
print(p.connections())
print(p.num_threads())

