# 数学相关的内置函数：
# abs:数学中求绝对值的函数
print(abs(-10))  # 10
# divmod:求两个数相除的商和余数
# max:求最大数
# min:求最小数
# sum:求和
# pow:求幂运算
# round:四舍五入保留到指定小数位

# 可迭代对象相关的方法：
# all:查看所有元素转换成为布尔值，都是True，结果就是True；否则是False
print(all(['hello', 'good', 'yes']))
print(all(['hello', 0]))
# any:只要有一个元素转换成为布尔值是True，结果就是True
# len:获取长度
# iter:获取到可迭代对象的迭代器
# next:for..in循环的本质结束调用迭代器的next方法
# sorted:用来排序的

# 转换相关：
# bin:将数字转换成为二进制
# oct:将数字转换成为八进制
# hex:将数字转换成为十六进制
# chr:将字符编码转换成为对应的字符    chr(97) ==> a
# ord:将字符转换成为对应的编码      ord('a') ==> 97
# eval:执行字符串里的python代码

# 输入/输出相关：
# print:打印数据
# input:让用户输入内容

# 判断对象相关的方法：
# isinstance:判断一个对象是否是由一个类创建出来的
# issubclass:判断一个类是否是另一个类的子类

# 变量相关：
# globals:用来查看所有的全局变量
# locals:用来查看所有的局部变量

# dir:列出对象所有的属性和方法
# exit:以指定的退出码结束程序

# help:查看帮助文档

# id:获取一个数据的内存地址

# open:用来打开一个文件
