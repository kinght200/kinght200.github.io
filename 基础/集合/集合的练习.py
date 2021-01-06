# 去重排序
# nums = [5, 8, 7, 6, 4, 1, 3, 5, 1, 8, 4]
# x = set(nums)
# y = list(x)
# y.sort(reverse=True)
# print(y)

# 转换相关的方法
# 内置类 list tuple set
nums = [9, 8, 4, 3, 2, 1]
x = tuple(nums)  # 使用tuple内置类转换称为元组
print(x)

y = set(x)  # 使用set内置类转换称为集合
print(y)

z = list({'name': 'zhangsan', 'age': 18, 'score': 98})
print(z)

# python李有一个比较强大的内置函数eval，可以执行字符串里的代码
a = 'input("请输入你的用户名")'  # a是一个字符串
p = '1+1'
print(eval(p))

import json

# JSON的使用，把列表、元组、字典等转换为JSON字符串
person = {'name': 'zhangsan', 'age': 18, 'gender': 'female'}
# 字典如果想要把他转给前端页面或者把字典写入到一个文件里
# '{"name": "zhangsan", "age": 18, "gender": "female"}'
m = json.dumps(person)  # dumps将字典、列表、集合、元组等转换称为JSON字符串
print(m)
# print(type(m))  # <class 'str'>
# print(m['name'])  不能这样使用，m是一个字符串，不能再像字典一样根据key去获取value

n = '{"name": "zhangsan", "age": 18, "gender": "female"}'
# p = eval(n)
# print(type(p))
s = json.loads(n)  # loads可以将json字符串转换成为python里的数据
print(s)
print(type(s))
