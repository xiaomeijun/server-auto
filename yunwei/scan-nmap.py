# -*- coding:utf-8 -*-
import sys
import nmap
scan_row=[]
input_data = raw_input('Please input hosts and port: ')
scan_row = input_data.split(" ")
if len(scan_row)!=2:
    print "Input errors,example \"192.168.122.0/24 80,443,22\""
    sys.exit(0)
hosts=scan_row[0] #接收用户输入打主机
port=scan_row[1]  #接收用户输入打端口
try:
    nm = nmap.PortScanner()  #创建端口扫描对象
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(0)
except:
    print("Unexpected error:",sys.exc_info()[0])
    sys.exit(0)
