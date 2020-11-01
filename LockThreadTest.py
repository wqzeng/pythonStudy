# @author :xpzhuang
# @date : 2020/11/1

from threading import Thread
from threading import Lock
import time

# 100张票
n=100

def task():
    global n
    mutex.acquire()
    time.sleep(1)
    n-=1
    print('购买成功，剩余%d张电影票'%n)
    mutex.release()

if __name__=='__main__':
    mutex=Lock()
    tl=[]
    for i in range(10):
        t=Thread(target=task())
        tl.append(t)
        t.start()
    for t in tl:
        t.join()

