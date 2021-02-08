import queue
import threading
import time


def produce():
    for i in range(10):
        time.sleep(1)
        print('生产了面包{}'.format(i))
        q.put('b{}'.format(i))


def consumer():
    while True:
        time.sleep(0.3)
        # q.get() 方法是一个阻塞的方法
        print('买到了面板{}'.format(q.get()))


# 创建一个q
q = queue.Queue()
# 创建两个不相关的线程
# 一条生产线
p1 = threading.Thread(target=produce, name='p1')

# 一条消费线
c1 = threading.Thread(target=consumer, name='c1')

p1.start()
c1.start()
