import multiprocessing
import os

n = 100


def test():
    global n
    n += 1
    print('test==={}里n的值是{}'.format(os.getpid(), n))


def demo():
    global n
    n += 1
    print('demo==={}里n的值是{}'.format(os.getpid(), n))


# test()  # 101
# demo()  # 102

# 多线程,同一个主进程里的两个子线程。线程之间可以共享同一进程的全局变量
# t1 = threading.Thread(target=test)
# t2 = threading.Thread(target=demo)
# # 多线程运行
# t1.start()
# t2.start()

# 不同进程访问全局变量
if __name__ == '__main__':
    # 不同进程各自保存一份全局变量，不会共享全局变量
    p1 = multiprocessing.Process(target=test)
    p2 = multiprocessing.Process(target=demo)

    p1.start()
    p2.start()
