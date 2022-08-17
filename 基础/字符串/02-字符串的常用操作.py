# 字符串的大小写转换操作方法
s = 'hello,python'
a = s.upper()  # 转成大写之后，会产生一个新的字符串对象
print(a)  # HELLO,PYTHON
print(s)
b = s.lower()  # 转换小写之后，会产生一个新的字符串对象
print(b)  # hello,python

s2 = 'hello,Python'
c = s2.swapcase()
print(c)  # HELLO,pYTHON

d = s2.title()
print(d)  # Hello,Python

# 字符串内容对齐操作的方法
hello = 'hello,Python'
# 居中对齐
print(hello.center(20, '*'))  # ****hello,Python****
# 左对齐
print(hello.ljust(20, '*'))  # hello,Python********
print(hello.ljust(10))  # hello,Python
print(hello.ljust(20))  # hello,Python
# 右对齐
print(hello.rjust(20, '*'))  # ********hello,Python
print(hello.rjust(10))  # hello,Python
print(hello.rjust(20))  # hello,Python
# 右对齐，使用0进行填充
print(hello.zfill(20))  # 00000000hello,Python
print(hello.zfill(10))  # hello,Python
print('-8910'.zfill(8))  # -0008910

# 字符串的切割
python = 'hello world Python'
# 从左边开始切割
lst = python.split()
print(lst)  # ['hello', 'world', 'Python']
s1 = 'hello|world|Python'
print(s1.split('|'))  # ['hello', 'world', 'Python']
print(s1.split(sep='|', maxsplit=1))  # ['hello', 'world|Python'] 切分后前面是一段，后面是一段
print(s1.split('|', 1))  # ['hello', 'world|Python'] 与上一句代码相同，参数可以省略
# 从右侧开始切割
print(python.rsplit())  # ['hello', 'world', 'Python']
print(s1.rsplit('|'))  # ['hello', 'world', 'Python']
print(s1.rsplit(sep='|', maxsplit=1))  # ['hello|world', 'Python'] 切分后前面是一段，后面是一段
print(s1.rsplit('|', 1))  # ['hello|world', 'Python'] 与上一句代码相同，参数可以省略

# 字符串的判断方法
p = 'hello,python'
# 判断是否为合法的标识符
print('1', s.isidentifier())  # False
print('2', 'hello'.isidentifier())  # True
print('3', '张三_'.isidentifier())  # True
print('4', '张三——123'.isidentifier())  # False
# 判断是否为全部由空白字符串组成（回车、换行、水平制表符）
print('5', '\t'.isspace())  # True
# 判断是否由字母组成
print('6', 'abc'.isalpha())  # True
print('7', '张三'.isalpha())  # True
print('8', '张三1'.isalpha())  # False
# 判断是否由10进制数字组成
print('9', '123'.isdecimal())  # True
print('10', '123四'.isdecimal())  # False
# 判断是否由数字组成
print('11', '123'.isnumeric())  # True
print('12', '123四'.isnumeric())  # True
# 判断是否由字母、数字组成
print('13', 'abc1'.isalnum())  # True
print('14', '张三123'.isalnum())  # True
print('15', 'abc!'.isalnum())  # False

# 字符串的替换与合并
qw = 'hello,Python'
print(qw.replace('Python', 'JAVA'))  # hello,JAVA
qw1 = 'hello,Python,Python,Python'
print(qw1.replace('Python', 'JAVA', 2))  # hello,JAVA,JAVA,Python

lsd = ['hello', 'java', 'Python']
print('|'.join(lsd))  # hello|java|Python
print('.'.join(lsd))  # hello|java|Python

t = ('hello', 'java', 'Python')
print(''.join(t))  # hellojavaPython

print('*'.join('python'))  # p*y*t*h*o*n
