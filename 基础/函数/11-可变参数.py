# *args 表示可变位置参数，结果是元组，关键字参数和位置参数都只能有一个；可变位置参数必须在关键字参数之前
# **kwargs 表示可变的关键字参数，结果是字典
def add(a, b, *args, mul=1, **kwargs):
    print('a={},b={}'.format(a, b))
    print('args={}'.format(args))  # 多出来的可变参数会以元组的形式保存到args里
    print('kwargs = {}'.format(kwargs))
    c = a + b
    for arg in args:
        c += arg
    return c


# def add(*args):
#     pass


# add(1, 3)
print(add(0, 2, 3, 4, 51, 1, mul=3, x=8, y=0))
print(add(9, 8, 6, 4, 6, 2, 4, 51, 34))
