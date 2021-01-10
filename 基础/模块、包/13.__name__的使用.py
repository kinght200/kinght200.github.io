def division(a, b):
    return a / b


# __name__：当直接运行这个py文件的时候，值是__main__
# 如果这个py文件作为一个模块导入的时候，值是文件名
if __name__ == '__main__':
    print('demo里的name是：', __name__)
    print('测试一下division函数结果是', division(4, -6))
