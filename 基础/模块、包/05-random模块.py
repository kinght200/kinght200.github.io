# random模块用来生成一个随机数
import random

# randint(a,b)  用来生成[a,b]的随机整数
print(random.randint(2, 9))

# random() 用来生成[0,1）的随机浮点数
print(random.random())

# randrange(a,b) 用来生成[a,b) 的随机整数
print(random.randrange(2, 9))

# choice 用来可迭代对象里随机抽取一个数据
print(random.choice(['zhangsan', 'lisi', 'jack']))

# sample 用来在可迭代对象里随机抽取n个数据
print(random.sample(['zhangsan', 'lisi', 'jack'], 2))
