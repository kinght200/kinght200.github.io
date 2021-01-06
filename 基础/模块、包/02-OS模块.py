# os全程 OperationSystem操作系统
# os 模块里提供的方法就是用来调用操作系统里的方法
import os

# os.name ==> 获取操作系统的名字         windows系列 ==>nt  / 非windows ==> posix
print(os.name)  # nt
print(os.sep)  # 路径的分隔符  Windows \  非windows /

# os 模块里的 path 会经常使用
# abspath ==> 获取文件的绝对路径
print(os.path.abspath('01-导入模块的语法.py'))

# isdir判断是否是文件夹
print(os.path.isdir('01-函数的介绍.py'))  # false
print(os.path.isdir('venv'))  # false

# isfile 判断是否是文件
print(os.path.isfile('01-导入模块的语法.py'))  # True
print(os.path.isfile('xxx'))  # False

# exists 判断是否存在
print(os.path.exists('01-导入模块的语法.py'))  # True
print(os.path.exists('mm.py'))  # False

# splitext 实现分割
flie_name = '2021.1.5.py'
print(os.path.splitext(flie_name))  # ('2021.1.5', '.py')
