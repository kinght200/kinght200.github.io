print('apple' > 'app')  # True
print('apple' > 'banana')  # False a:97,b:98,>False
print(ord('a'), ord('b'))

print(chr(97), chr(98))  # a b

"""
==与is的区别
==比较的是value
is比较的是id是否相等
"""
a = b = 'python'
c = 'python'
print(a == b)  # True
print(b == c)  # True
print(a is b)  # True
print(a is c)  # True
print(id(a))  # 2792103007216
print(id(b))  # 2792103007216
print(id(c))  # 2792103007216
