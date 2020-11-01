# @author :xpzhuang
# @date : 2020/11/1

import threading
from queue import Queue
import random
import time

class Producer(threading.Thread):
    def __init__(self,name,queue):
        threading.Thread.__init__(self,name=name)
        self.data=queue

    def run(self):
        for i in range(10):
            print("生产者%s将产品%d加入队列！"%(self.name,i))
            self.data.put(i)
            # random()生成0-1之间的随机数
            time.sleep(random.random())
        print("生成者%s完成！"%self.name)

class Consumer(threading.Thread):
    def __init__(self,name,queue):
        threading.Thread.__init__(self,name=name)
        self.data=queue

    def run(self):
        for i in range(10):
            val=self.data.get()
            print("消费者%s将产品%d从队列中取出！"%(self.name,val))
            time.sleep(random.random())
        print("消费者%s完成！"%self.name)

if __name__=="__main__":
    print("-------主线程开始-------")
    queue=Queue()
    producer=Producer("Producer",queue)
    consumer=Consumer("Consumer",queue)
    producer.start()
    producer.join()
    consumer.start()
    consumer.join()

    print('-------end----------')
