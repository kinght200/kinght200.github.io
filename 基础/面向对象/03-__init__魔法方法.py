# 魔法方法也叫魔术方法，是类里的特殊的一些方法
# 特点：
# 1.不需要手动调用，会在合适的时机自动调用
# 2.这个方法，都是使用 __开始，使用 __ 结束
# 3.方法名都是系统规定好的，在合适的时机自己调用

# import datetime
#
# x = datetime.datetime(2021, 5, 6, 16, 17, 45, 200)
# print(x)  # __str__ 方法
# print(repr(x))  # __repr__ 方法


class Person(object):
    # 在创建对象时，会自动调用这个方法
    def __init__(self, name, age):
        print('__init__方法被调用了')
        self.name = name
        self.age = age

    def __del__(self):
        # 当对象被销毁时，会自动调用这个方法
        print('__del__方法被调用了')

    def __repr__(self):
        return 'hello'

    def __str__(self):
        return '姓名：{}，年龄：{}'.format(self.name, self.age)

    def __call__(self, *args, **kwargs):
        # print('__call__ 方法被调用了')
        # args 是一个元组，保存(1,2)
        # kwargs 是一个字典{fn=lambda x, y: x + y}
        print('args={},kwargs={}'.format(args, kwargs))
        fn = kwargs['fn']
        return fn(args[0] + args[1])


p = Person('张三', 15)
# 如果不做任何的修改，直接打印一个对象，打印的是对象的类型以及内存地址
# print(p)  # <__main__.Person object at 0x0000027A22B95FD0>

print(p)
# 当打印一个对象的时候，会调用这个对象的 __str__ 或者 __repr__ 方法
# 如果两个方法都写了，选着 __str__ 方法
# print(p)


# 手动调用
# print(repr(p))  # 调用内置函数 repr 会触发对象的 __repr__ 方法
# print(p.__repr__())  # 魔法方法，一般不手动的调用


# 对象名() ==> 调用这个对象的 p.__call__ 方法
p(1, 2, fn=lambda x, y: x + y)
