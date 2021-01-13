class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        # print('__eq__ 方法被调用了，other=',other)
        if self.name == other.name and self.age == other.age:
            return True
        return False


# 1.调用 __new__ 方法申请内存空间
p1 = Person('zhangsan', 18)

# 调用 __new__ 方法申请内存空间
p2 = Person('zhangsan', 18)

# p1和p2是同一个对象吗？
# 怎样比较两个对象是否是同一对象？比较的是内存地址
print('0x%X' % id(p1))  # 0x160C8255FD0
print('0x%X' % id(p2))  # 0x160C8255F10

# is 身份运算符 可以用来判断两个对象是否是同一个对象
print('p1 is p2', p1 is p2)  # False

# __eq__ 如果不重写，默认比较依然是内存地址
print('p1 == p2', p1 == p2)  # True p1 == p2 本质是调用 p1. __eq__(p2),获取这个方法的返回值

# is 比较两个对象的内存地址
# == 会调用对象的 __eq__ 方法，获取这个方法的比较结果
num1 = [1, 2, 3]
num2 = [1, 2, 3]
print(num1 is num2)  # False
print(num1 == num2)  # True
