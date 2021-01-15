class Person(object):
    """
    这是一个人类
    """
    # 限制使用
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃饭')


# 'name':'zhangsan','age':'18','eat':<function>
p = Person('张三', 18)
# 列出这个对象所有属性
print(dir(p))

# 告诉你是什么类
print(p.__class__)  # <class '__main__.Person'>

# 把对象属性和值转换成为一个字典
print(p.__dict__)  # {'name': '张三', 'age': 18}

# 等价与dir(p)
print(p.__dir__())

# 查看当前类的说明文档
print(p.__doc__)  # 对象名.__doc__
print(Person.__doc__)  # 类名.__doc__

# 模块
print(p.__module__)  # __main__

# 限制属性
print(Person.__slots__)
