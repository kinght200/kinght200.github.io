import re

# findall:匹配字符串中所有的符合正则的内容
lst = re.findall(r'\d+', '我的电话号是：10086,我朋友的电话是：10010')
print(lst)

# finditer:匹配字符串中所有的内容[返回的是迭代器],从迭代器中拿到的内容需要.group()
it = re.finditer(r'\d+', '我的电话号是：10086,我朋友的电话是：10010')
for i in it:
    print(i.group())

# search,找到一个结构就返回，返回的结构是match对象。拿数据需要.group()
s = re.search(r'\d+', '我的电话号是：10086,我朋友的电话是：10010')
print(s.group())

# match是从头开始匹配
a = re.match(r'\d+', '我的电话号是：10086,我朋友的电话是：10010')
# print(a.group())

# 预加载正则表达式
# obj = re.compile(r'\d+')

# re.S:让点能匹配换行符
s = """
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋轶</span></div>
<div class='jolin'><span id='3'>大聪明</span></div>
<div class='jsylar'><span id='4'>范思哲</span></div>
<div class='tony'><span id='5'>胡说八道</span></div>
"""

# (?P<分组名字>正则表达式)  可以单独从正则匹配的内容中进一步提取内容
obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S)

result = obj.finditer(s)
for c in result:
    print(c.group('name'))
    print(c.group('id'))
