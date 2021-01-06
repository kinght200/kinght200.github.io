# 模块：在python里一个py文件，就可以理解为一个模块
# 不是所有的py文件都能作为一个模块来导入
# 如果想要让一个py文件能够被导入，模块名字必须要遵守命名规则
# python为了方便我们开发，提供了很多内置模块

import time  # 1.使用import模块名直接导入一个模块
from math import *  # 3.from模块名 import * 导入这个模块里的“所有方法”和变量
# 2.from 模块名 import 函数名，导入一个模块里的方法或者变量
from random import randint

# 导入这个模块以后，就可以使用这个模块里的方法和变量
print(time.time())

randint(0, 3)  # 生成[0,3]的随机整数
print(pi)
