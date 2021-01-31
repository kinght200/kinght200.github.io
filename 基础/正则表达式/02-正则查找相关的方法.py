# 查找相关的方法
# match 和 search:查找字符串，返回的结果是re.Match对象
# 共同点：1.只对字符串查询一次 2.返回值类型都是 re.Match类型的对象
# 不同点：math 是从头开始匹配，一旦匹配失败，就返回None；search是在整个字符串里匹配

# finditer: 查找到所有的匹配数据放到一个可迭代对象里
# findall: 把查找到的所有的字符串结果放到一个列表里
# fullmatch: 完整匹配，字符串需要完全满足正则规则才会有结果，否则返回None

import re
from collections.abc import Iterable

m1 = re.match(r'good', 'hello world good morning')
print(m1)  # None

m2 = re.search(r'good', 'hello world good morning')
print(m2)  # <re.Match object; span=(12, 16), match='good'>

# print(re.search(r'x', 'bgiftdy54svvfs4axcvb8yt86fyghoiuyoxjiiufuzxx'))

# finditer 返回的结果是一个可迭代对象
# 可迭代对象里的数据是匹配到的所有结果，是一个 re.Match 类型的对象
m3 = re.finditer(r'x', 'kxleisnaxxajafa')
print(isinstance(m3, Iterable))  # True
for i in m3:
    print(i)

m4 = re.findall(r'x', 'kxleisnaxxajafa')
print(m4)  # ['x', 'x', 'x']

m5 = re.fullmatch(r'hello world', 'hello world')
print(m5)  # <re.Match object; span=(0, 11), match='hello world'>

m6 = re.fullmatch(r'h.*d', 'h4541326849d')
print(m6)
