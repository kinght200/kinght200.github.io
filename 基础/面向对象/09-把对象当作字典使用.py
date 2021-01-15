class Person(object):
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __setitem__(self, key, value):
        # print('setitem方法被调用了，key={}，value={}'.format(key, value))
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]


# 将对象转换成为字典{'name': '张三', 'age': 18}
p = Person('张三', 18, '北京')
print(p.__dict__)

# 不能直接把一个对象当作一个字典使用
p['name'] = 'jack'  # [] 语法会调用对象的 __setitem__ 方法
print(p.name)

# 获取值 会调用 __getitem__ 方法
print(p['name'])
