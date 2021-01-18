# 在程序运行的过程中，由于各种原因等造成程序无法正常执行，此时程序就会报错
# 异常是为了保证程序的健壮性，很多编程语言都有异常处理机制

def div(a, b):
    return a / b


try:
    x = div(5, 0)
except Exception as e:  # 如果程序出错了，会立刻跳转到 except 语句
    print('程序出错了')
else:  # 程序运行如果没有出错，会执行else语句里的代码
    print('计算的结果是', x)
