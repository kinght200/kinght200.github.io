# 集合是一个不重复的无序，可以使用{}或者set来表示
# {} 有两种意思：字典、集合
# {} 里如果放的是键值对，它就是一个字典；如果 {} 放的是单个的值，就是一个集合
person = {'name': 'zhangsan', 'age': 18}  # 字典
x = {'hello', 1, 'good'}  # 集合

names = {'zhangsan', 'lishi', 'jack', 'tony', 'jack', 'lisi'}
print(names)

# set能不能进行增删改查
names.add('阿珂')  # 添加一个元素
print(names)

names.pop()  # 删除一个，随机
print(names)

names.remove('jack')  # 删除一个指定的元素，没有这个元素就会报错
print(names)

# union 将多个集合合并生成一个新的集合
# A.update(B) 将B拼接到A里
print(names.union({'刘能', '赵四'}))
print(names)
# names.clear()   # 清空一个集合
# 空集合的表示方式不是 {}，{}表示的是空字典
# 空集合是set()
# print(names)
