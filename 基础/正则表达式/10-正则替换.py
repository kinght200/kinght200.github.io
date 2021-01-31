# 正则表达式作用是用来对字符串进行检索和替换
# 检索：math search fullmatch finditer findall
# 替换：sub

import re

print(re.sub(r'\d', 'x', 'afo3591jdnabdud12uid'))  # afoxxxxjdnabdudxxuid
print(re.sub(r'\d+', 'x', 'afo3591jdnabdud12uid'))  # afoxjdnabdudxuid

p = 'hello35good23'  # 把字符串里的数字 *2 hello68good46


# 第一个参数是正则表达式
# 第二个参数是新字符或者一个函数
# 第三个参数是需要被替换的原来的字符串
def test(x):
    y = int(x.group(0))
    y *= 2
    return str(y)


# sub内部在调用test方法时，会把每一个匹配到的数据以re.Match的格式传参
print(re.sub(r'\d+', test, p))  # test函数是自动调用的
