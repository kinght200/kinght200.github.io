a = 100  # 这个变量是全局变量，在整个py文件里都可以访问
word = 'hell0'


def test():
    x = 'hello'
    print('x={}'.format(x))

    # 如果局部变量的名和全局变量同名，会在函数内部又定义一个新的局部变量
    # 而不是修改全局变量
    a = 10
    print('函数内部a={}'.format(a))

    # 函数内部如果想要修改全局变量？
    # 使用global对变量进行声明，可以通过函数去修改全局变量的值
    global word
    word = 'ok'
    print('locals = {},globals = {}0'.format(locals(), globals()))


test()
# print(x) # x只能在函数内部使用
print('函数内部a={}'.format(a))
print('函数外部word={}'.format(word))

# 内置函数  globals()  locals()  可以查看全局变量和局部变量
# 在python里，只有函数能够分割作用域
if 3 < 2:
    m = 'hi'
print(m)
