from threading import Thread
from multiprocessing import Process


# def func():
#     for i in range(1000):
#         print('子进程', i)
#
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.start()
#
#     for i in range(1000):
#         print('主进程', i)

# def func(name):
#     for i in range(1000):
#         print(name, i)
#
#
# if __name__ == '__main__':
#     t1 = Process(target=func, args=("张三",))  # 传参必须是元组
#     t1.start()
#
#     t2 = Process(target=func, args=("李四",))
#     t2.start()
#
#     for i in range(1000):
#         print('主进程', i)

class MyProcess(Process):

    def run(self):  # 固定的   -> 当线程可以执行之后，被执行的就是run()
        for i in range(1000):
            print('子线程', i)


if __name__ == '__main__':
    t1 = MyProcess()
    # t1.run() # 方法的调用了 -> 单线程？？？
    t1.start()  # 开启线程

    for i in range(1000):
        print('主线程', i)
