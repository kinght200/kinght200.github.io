# 列表推导式作用是使用简单的语法创建一个列表
# nums = [i for i in range(10)]
# print(nums)

# 上面式子由以下式子改变
# nums = []
# for i in range(10):
#     nums.append(i)
# print(nums)

# x = [i for i in range(10) if i % 2 == 0]
# print(x)

# 以上式子由以下式子转变而来
# x = []
# for i in range(10):
#     if i % 2:
#         x.append(i)

# points 是一个列表。这个列表里的元素都是元组
# points = [(x, y) for x in range(5, 9) for y in range(10, 20)]
# print(points)


# 请写出一段python代码实现分组一个list里面的元素，比如[1,2,3,.....100]变成[[1,2,3],[4,5,6]......]
m = [i for i in range(1, 101)]
print(m)
n = [m[j:j + 3] for j in range(0, 100, 3)]
print(n)
