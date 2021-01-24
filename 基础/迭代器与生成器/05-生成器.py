# 生成器本质也是一个迭代器，它是一个特殊的迭代器

# x = 5
# y = 10
# if x > y:
#     z = x
# else:
#     z = y
# z = x if x > y else y  # 三元表达式

# 最简单的生成器
# nums = [i for i in range(10)]  # 列表生成式(推导式)
# print(nums)
#
# g = (i for i in range(10))  # 得到的结果是生成器
# for m in g:  # 生成器是一个特殊的迭代器，也可以方法在for...in 后面
#     print(m)


# 迭代器是一个对象，定义class
# 生成器写法上像一个函数
def my_gen(n):
    i = 0
    while i < n:
        # return i    # 函数里的return表示函数的执行结束
        yield i  # yield关键字，将函数变成生成器
        i += 1


g = my_gen(10)
# for i in g
# next()返回迭代器的下一个项目，iter() 函数用来生成迭代器。
print(next(iter(g)))
print(next(iter(g)))
print(next(iter(g)))
