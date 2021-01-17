# open 参数介绍
# file:用来指定打开的文件(不是文件的名字，而是文件的路径)
# mode：打开文件时的模式，默认是 r 表示只读
# encoding：打开文件时的编码方式

# windows系统里，文件夹之间使用 \ 分隔
# 在非Windows系统里，文件夹之间使用 / 分隔
# print(os.sep)

# 在python字符串里， \ 表示转义字符,再加一个斜线就好了
# 路径书写的三种方式： 1.\\  2.r'\'  3. '/'(推荐)

# 路径分为两种：
# 1.绝对路径：从电脑盘符开始的路径
# file = open('E:\\pycharm代码\\基础\\文件操作\\xxx.txt')
# file = open(r'E:\pycharm代码\基础\文件操作\xxx.txt', encoding='utf8')
# file = open(r'E:/pycharm代码/基础/文件操作/xxx.txt', encoding='utf8')
# print(file.read())

# 2.相对路径：以当前文件所在的文件夹开始的路径
# ../ 表示可以返回到上一级文件夹
# ./ 可以省略不屑，表示当前文件夹
file = open('xxx.txt')
print(file.read())
file.close()
