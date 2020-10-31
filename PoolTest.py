# -*- coding=utf-8 -*-
from multiprocessing import Pool
import os
import time

def task(name):
    print('子进程（%s）执行task %s...'%(os.getpid(),name))
    time.sleep(2)

if __name__=='__main__':
    print('父进程（%s）。'%os.getpid())
    p=Pool(3)
    for i in range(10):
        # 使用非阻塞方式调用task()函数
        p.apply_async(task,args=(i,))
    print('等待所有子进程结束。。。')
    p.close()
    p.join()
    print('所有子进程结束')