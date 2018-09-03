# -*- coding:utf-8 -*-
import pexpect
import sys
mypassword='xiao1983'
child = pexpect.spawn('ssh sean@172.20.10.5')
fout = file('mylog.txt','w')
child.logfile=fout
#child.logfile = sys.stdout
child.expect("password: ")
child.sendline('xiao1983')
print "before:" + child.before
print "after:" + child.after
