# 1.一个函数作为另一个函数的返回值
def test():
    print('我是test函数')
    return 'hello'


def demo():
    print('我是demo函数')
    return test


def bar():
    print('我是bar函数')
    return test()


# x = test()
# print(x)

y = demo()  # y 是test函数
print(y)  # 打印函数的类型和内存地址
z = y()  # test赋值给z
print(z)  # hello

# a = bar()
# # a() a是一个字符串，不是一个函数，相当于内存地址
# print(a)

# 2.一个函数作为另一个函数的参数.lambda表达式的使用
# sort filter map reduce
# 3.函数内部再定义一个函数
