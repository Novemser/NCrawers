# coding="utf-8"
__author__ = 'Novemser'

url = 'http://sse.tongji.edu.cn/Notice/1004158'

import urllib2
from time import sleep
import thread

lock = thread.allocate_lock()
number = 0


def fuck_it(n):
    global number
    for i in range(1, n):
        urllib2.urlopen(url)
        lock.acquire()
        print number
        number = number + 1
        lock.release()
        sleep(1)
    thread.exit_thread()


if __name__ == '__main__':
    try:
        for m in range(0, 20):
            thread.start_new_thread(fuck_it, (10000,))
    except:
        print "hi"
    while(1):
        sleep(10)