# def say_hello(city='北京'，name, age) # 缺少参数要放在后面
def say_hello(name, age, city='北京'):  # 形参city设置了一个默认值
    print('大家好，我是{}，我今年{}岁了，我来自{}'.format(name, age, city))


say_hello('jack', 19)  # 如果没有传递参数，会使用默认值
say_hello('tony', 20, '上海')  # 如果传递参数，就会使用传递的参数
# 如果由位置参数和关键字参数，关键字参数一定要放在位置参数的后面
say_hello('jerry', age=56, city='江苏')  # 可以直接传递单个参数，也可以使用变量赋值的形式传递
say_hello(name='herry', age=21, city='成都')

# 有些函数的参数是，如果你传递了参数，就使用传递的参数，如果没有传递参数，就使用默认的值。

# print函数里end就是一个缺省参数
print('hello world', end='')
print('hi')
