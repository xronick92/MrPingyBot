import os
import time
from subprocess import Popen, DEVNULL
import setting
import yaml

bot = setting.bot
group = setting.group

#pool ip addrs
#########################################################################
# for n in range(1, 255):                                               #
#     ip = "192.168.88.%d" % n                                          #
#     p[ip] = Popen(['ping', '-n', '-w5', '-c3', ip], stdout=DEVNULL)   #
#########################################################################
def test() :
    line = 0
    p = {}
    with open("list_ip.yaml", 'r') as ip:
        data_load = yaml.safe_load(ip)
    for ip in data_load['ip']:
        p[ip] = Popen(['ping', '-n', '-W3', '-c3', ip], stdout=DEVNULL)
    while p:
        for ip, proc in p.items():
            if proc.poll() is not None:
                del p[ip]
                if proc.returncode == 0:
                    print('%s active' % ip + ' ' +time.asctime() )
                elif proc.returncode == 1:
                    f = open('norep.txt', 'a')
                    b = open('norep.txt', 'r')
                    line += 1
                    print('%s no response' % ip + ' ' + time.asctime())
                    f.write('%s no response' % ip + ' ' + time.asctime() + '\n')
                    #f.write(ip + ' ' + time.asctime() + '\n')
                    if line >= 7:
                        reader = b.read()
                        bot.send_message(group, 'Получите распишитесь: \n'+reader)
                        line = 0
                        f.truncate(0)
                        b.close()
                else:
                    print('%s error' % ip)
                break
    f.close()
    b.close()

while True:
    test()
    time.sleep(10)


bot.polling()


