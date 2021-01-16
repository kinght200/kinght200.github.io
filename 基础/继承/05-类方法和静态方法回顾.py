class Person(object):
    type = 'human'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 这个方法要打印对象的名字
    def domo(self):
        print('姓名是', self.name)

    # 这个方法需要访问到类属性 type
    @classmethod
    def bar(cls):
        print(cls.type)

    # 这个方法只需要打印 hello
    @staticmethod
    def foo():
        print('hello')


p = Person('zhangsan', 18)
p.domo()  # 实例对象调用实例方法时，会自动将实例对象传递给self
Person.domo(p)

# 静态方法可以使用类对象和实例对象调用
p.foo()
Person.foo()

# 类方法可以通过类对象额实例对象来调用
p.bar()
Person.bar()
