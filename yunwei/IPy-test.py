#/usr/bin/env python
# -*- coding:utf-8 -*-
import IPy
from IPy import IP
ip = IP ('192.168.0.0/16')
print ip.len()
#for x in ip:
#    print(x)

ip = IP('192.168.1.20')
print ip.reverseNames()
print ip.iptype()
print IP('8.8.8.8').iptype()
print IP("8.8.8.8").int()
print IP("8.8.8.8").strHex()
print (IP(0x8080808))
print IP("192.168.1.1").strHex()
print (IP(0xc0a80101))
print IP('8.8.8.8').strBin()

print (IP('192.168.1.0').make_net('255.255.255.0'))
print IP('192.168.1.0/24').strNormal(0)
print IP('192.168.1.0/24').strNormal(1)
print IP('192.168.1.0/24').strNormal(2)
print IP('192.168.1.0/24').strNormal(3)

print IP('10.0.0.0/24') < IP('12.0.0.0/24')
print '192.168.1.100' in IP('192.168.1.0/24')
print IP('192.168.1.0/24') in IP('192.168.0.0/16')

#判断网段重叠
print IP('192.168.0.0/23').overlaps('192.168.1.0/24')
print IP('192.168.1.0/24').overlaps('192.168.2.0')

