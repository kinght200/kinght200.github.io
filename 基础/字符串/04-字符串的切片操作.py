# 字符串是不可变类型
# 不具备增、删、改等操作
# 切片操作时将产生新的对象
s = 'hello,python'
s1 = s[:5]  # 由于没有指定起始位置，所以从0开始
s2 = s[6:]  # 由于没有指定结束位置，所以切完
s3 = '!'
newstr = s1 + s3 + s2
print(s1)  # hello
print(s2)  # python
print(newstr)  # hello!python

print(id(s))  # 2001147738864
print(id(s1))  # 2001148093232
print(id(s2))  # 2001148080880
print(id(s3))  # 2001147738672
print(id(newstr))  # 2001148153520

print("--------------------------------")
print(s[1:5:1])  # ello 从1开始截到5（不包含5），步长为1
print(s[::2])  # hlopto 默认从0开始，没有写结束，默认到字符串的最后一个元素，步长为2，两个元素之间的索引间隔为2
print(s[::-1]) # nohtyp,olleh 默认从字符产的最后一个元素开始，到字符串的第一个元素结束，因为步长为负数

