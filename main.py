import os
import time
from subprocess import Popen, DEVNULL

p = {}
for n in range(1, 255):
    ip = "192.168.88.%d" % n
    p[ip] = Popen(['ping', '-n', '-w5', '-c3', ip], stdout=DEVNULL)
while p:
    for ip, proc in p.items():
        if proc.poll() is not None:
            del p[ip]
            if proc.returncode == 0:
                print('%s active' % ip + ' ' +time.asctime() )
            elif proc.returncode == 1:
                print('%s no response' % ip + ' ' + time.asctime())
            else:
                print('%s error' % ip)
            break