import re

# 在python的正则表达式里，默认是贪婪模式，尽可能多的匹配
# 在贪婪模式后面添加 ? 可以将贪婪模式转换成为非贪婪模式
m = re.search(r'm.*a', 'o3rjomjadas')
print(m.group())  # mjada

# 尽可能少的匹配
m = re.search(r'm.*?a', 'o3rjomjadas')
print(m.group())  # mja
