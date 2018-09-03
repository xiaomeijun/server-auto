# -*- coding:utf-8 -*-
import psutil
import datetime
from subprocess import PIPE

#memory
mem= psutil.virtual_memory()
print mem
print mem.used
print mem.total
print mem.free
print psutil.swap_memory()


#cpu
cpu=psutil.cpu_times()
print cpu

cpu2=psutil.cpu_count()
print cpu2

#disk
disk=psutil.disk_partitions()
print disk
disk2=psutil.disk_usage('/')
print disk2
baifenbi=int(float(disk2.used) / float(disk2.total) * 100)
print str(baifenbi) + "%"

#net
i=psutil.net_io_counters()
print i
print i.bytes_sent,i.bytes_recv
j=psutil.net_io_counters(pernic=True)
print j

#systeminfo
user=psutil.users()
print user

#system-open-time
time=psutil.boot_time()
print time
date=datetime.datetime.fromtimestamp(time).strftime("%Y-%m-%d %H:%M:%S")
print date

#pid
pid=psutil.pids()
print pid
p=psutil.Process(2089)
print p
print p.name()
print p.exe()
print p.cmdline()
print p.status()
print p.create_time()
print p.uids()
print p.memory_info()
print p.memory_percent()
print p.io_counters()
print p.memory_info()
print p.num_threads() #进程开启打线程数

#popen方法启动打应用程序，可以跟踪程序运行相关信息
p=psutil.Popen(["/usr/bin/python", "-c", "print('hello')"],stdout=PIPE)
print p.name()
print p.username()
print p.communicate()

