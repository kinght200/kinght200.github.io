# python里使用 open 内置函数用来打开一个文件
# file:文件的路径。相对路径和绝对路径
# mode：打开的模式。 r:只读  w：写入  b:二进制  t：文本形式打开
# mode 默认使用的 rt
# encoding；用来指定文件的编码方式。Windows系统里，默认是gbk

# file = open('xxx.txt')
# file = open('sss.txt', 'w', encoding='utf8')  # 创建一个新的文件
# file.write('你好')

file = open('sss.txt', encoding='utf8')
# print(file.read()) # 将所有的数据都读取出来
# print(file.readline())  # 只读取一行数据

# 读取所有行的数据，保存到一个列表里
# x = file.readlines()
# print(x)

# 指的是读取的长度
x = file.read(10)
print(x)

# 优化：没有绝对的优化，除非提示硬件
# 软件层面 时间/空间
file.close()
