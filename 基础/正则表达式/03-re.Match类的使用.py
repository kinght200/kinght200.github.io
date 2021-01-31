# 调用 re.match、re.search或者re.finditer结果进行遍历
# 拿到的内容都是re.Match类型对象

import re

# . 任意字符 * 出现任意次数 贪婪模式
m = re.search(r'm.*a', 'odasidmhaifha')  # <re.Match object; span=(12, 13), match='m'>
# print(dir(m))
# print(m.pos, m.endpos)
print(m.span())  # 匹配到的结果字符串的开始和结束的下标

# 使用group方法可以获取匹配的字符串结果
# group 可以传参，表示第 n 个分组
print(m.group())  # mhaifha
print(m.group(0))  # mhaifha
# print(m.group(1))  # IndexError: no such group

# group方法表示正则表达式的分组
# 1.在正则表达式里使用 () 表示一个分组
# 2.如果没有分组，默认只有一组
# 3.分组的下标从 0 开始

# 正则表达式有 四个分组
m1 = re.search(r'(9.*)(0.*)(5.*7)', '0jj9jfs0ahfw5uwfiflsf7osxiadhs')
print(m1.group(0))  # 分组0：(9.*)(0.*)(5.*7),第0组就是把整个正则表达式当作一个整体
print(m1.group())  # 默认就是拿第0组
print(m1.group(1))  # 9jfs
print(m1.group(2))  # 0ahfw
print(m1.group(3))  # 5uwfiflsf7

print(m1.groups())  # ('9jfs', '0ahfw', '5uwfiflsf7')

# groupdict 作用是获取到分组组成的字典
print(m1.groupdict())

# (?P<name>表达式)  可以给分组起一个名字
m2 = re.search(r'(9.*)(?P<xxx>0.*)(5.*7)', '0jj9jfs0ahfw5uwfiflsf7osxiadhs')
# print(m2.groupdict())  # {'xxx': '0ahfw'}

print(m2.groupdict('xxx'))  # {'xxx': '0ahfw'}

# 可以通过分组名或者分组的下标获取到分组里匹配到的字符串
print(m2.group('xxx'))
print(m2.group(2))

print(m2.span())
