import time


def cal_time(fn):
    print('我是外部函数，我被调用了！！！')
    print('fn = {}'.format(fn))

    def inner():
        start = time.time()
        fn()
        end = time.time()
        print('代码耗时', end - start)

    return inner


@cal_time
def demo():
    x = 0
    for i in range(1, 100000000):
        x += i

    print(x)


# print('装饰后的demo = {}'.format(demo))
demo()


@cal_time
def foo():
    print('hello')
    time.sleep(5)
    print('world')


foo()
