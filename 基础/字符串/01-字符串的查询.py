s = 'hello,hello'
# 正向索引
print(s.index('lo'))  # 3
print(s.find('lo'))  # 3
# 逆向索引
print(s.rindex('lo'))  # 9
print(s.rfind('lo'))  # 9

# 查询不存在的字符
# print(s.index('k')) # ValueError: substring not found
print(s.find('k'))  # -1
# print(s.rindex('k')) # ValueError: substring not found
print(s.rfind('k'))  # -1
