# filter 对可迭代对象进行过滤，得到的是一个filter对象
# python2的时候是内置函数，python3修改成了一个内置类

# age = [12.33, 44, 55, 66]
# # filter可以给定两个参数，第一个参数是函数，第二个参数是可迭代对象
# # filter结果是一个filter 类型的对象，filter对象也是一个可迭代对象
#
# x = filter(lambda ele: ele > 18, age)
# # print(x)
# for i in x:
#     print(i)    # 44 55 66


# map的使用
age = [12, 18, 17, 20, 43]
m = map(lambda x: x + 2, age)
print(list(m))  # [14, 20, 19, 22, 45]

# reduce的使用
# reduce 以前是一个内置函数
# 内置函数和内置类都在 builtins.py文件里
from functools import reduce


def foo(x, y):  # x=100,y=98;x=198,y=97;x=295,y=82
    return x + y


scores = [100, 98, 97, 82]
print(reduce(foo, scores))
