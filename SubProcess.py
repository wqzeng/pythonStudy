# -*- coding:utf-8 -*-
__anthor__ = 'moke'

from multiprocessing import Process
import time
import os


class SubProcess(Process):
    def __init__(self, interval, name=''):
        Process.__init__(self)
        self.interval = interval
        if name:
            self.name = name

    # 重写Process类的run()方法
    def run(self):
        print("子进程（%s）开始执行，父进程为（%s）" % (os.getpid(), os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_stop = time.time()
        print("子进程（%s）执行结束，耗时%0.2f秒" % (os.getpid(), t_stop - t_start))


if __name__ == "__main__":
    print("------父进程开始执行-----")
    print("父进程PID：", os.getpid())
    p1 = SubProcess(1, 'testProcess')
    p2 = SubProcess(interval=2)
    p1.start()
    p2.start()

    print("p1.is_alive=", p1.is_alive())
    print("p2.is_alive=", p2.is_alive())

    print("p1.name=%s" % p1.name)
    print("p1.pid=%s" % p1.pid)

    print("p2.name=%s" % p2.name)
    print("p2.pid=%s" % p2.pid)

    print("--------等待子进程---------")

    # 是否等待进程实例执行结束，或等待多少秒
    p1.join()
    p2.join()
    print("p1.is_alive=", p1.is_alive())
    print("p2.is_alive=", p2.is_alive())

    print("--------父进程执行结束--------")