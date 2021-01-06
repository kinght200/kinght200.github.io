# sys 系统相关的功能
import sys

print('hello world')
# print('hhhhhh')

print(sys.path)  # 结果是一个列表，表示查找模块的路径

# sys.exit(100)  # 程序退出，和内置函数exit功能一致，可以添加退出码

# sys.stdin  # 可以像input一样，接受用户的输入。接收用户的输入和input相关

# sys.stdout 和 sys.stderr 默认输出都是在控制台
# sys.stdout # 修改sys.stdout 可以改变默认输出位置
# sys.stderr # 修改sys.stderr 可以改变错误输出的默认位置
