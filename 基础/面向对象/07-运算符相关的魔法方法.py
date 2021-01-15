class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        # if self.name == other.name and self.age == other.age
        #     return True
        # return False
        return self.name == other.name and self.age == other.age

    # def __ne__(self, other):  使用 != 运算符会自动调用这个方法
    #     return 'hello'

    def __gt__(self, other):  # greater than 使用 > 会自动调用这个方法
        return self.age > other.age

    # def __ge__(self, other): 使用 >= 运算符会自动调用
    # def __lt__(self, other): 使用 < 运算符会自动调用
    # def __le__(self, other): 使用 <= 运算符会自动调用
    def __add__(self, other):  # 使用 + 运算符会自动调用
        return self.age + other.age

    def __sub__(self, other):  # 使用 - 运算符会自动调用
        return self.age - other

    def __mul__(self, other):  # 使用 * 运算符会自动调用
        return self.name * other

    # def __truediv__(self, other): # 使用 / 运算符会自动调用
    def __str__(self):
        return 'hello'

    def __int__(self):
        return 40

    def __float__(self):
        return 100.5


p1 = Person('zhangsan', 18)
p2 = Person('zhangsan', 18)
p3 = Person('lisi', 19)
print(p1 is p2)  # False

# == 运算符本质其实是调用对象的 __eq__ 方法，获取 __eq__ 方法的返回结果
# a == b => a.__eq__(b)
print(p1 == p2)  # False p1.__eq__(p2)

# != 本质是调用 __ne__ 方法 或者 __eq__ 方法取反
print(p1 != p2)  # False

print(p1 > p3)

print(p1 + p3)

print(p1 - 2)

print(p1 * 2)

# str()将对象转换成为字符串，会自动调用 __str__ 方法
# 1.str()转换也会调用  2.打印对象也会调用
x = (str(p1))  # 转换成为字符串，默认会转换成为类型+内存地址
print(x)

# int() ==> 调用对象的 __int__ 方法
print(int(p1))

# float() ==> 调用对象的 __float__ 方法
print(float(p1))
