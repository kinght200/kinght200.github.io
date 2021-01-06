# 有几个内置函数和内置类，用到了匿名函数
nums = [4, 8, 6, 9, 2, 3, 7, 5]

# 列表的sort的方法，会直接对列表进行排序
# nums.sort()
# print(nums)

ints = (9, 8, 6, 2, 4, 7)
# sorted内置函数，不会改变原有的数据，而是生成一个新的有序的列表
x = sorted(ints)
print(x)  # [2, 4, 6, 7, 8, 9]

students = [
    {'name': 'zhangsan', 'age': 18, 'score': 98},
    {'name': 'lishi', 'age': 18, 'score': 98},
    {'name': 'wangwu', 'age': 18, 'score': 98},
    {'name': 'jack', 'age': 18, 'score': 98}
]

# 字典与字典之间不能使用比较运算
# students.sort()

# foo这个函数需要 0 个位置参数，但是在调用的时候传递了一个参数
# def foo(x):
# print('x={}'.format(x))
# return x['age']  # 通过返回值告诉sort方法，按照元素的哪个属性来进行排序


# 需要传递参数 key 指定比较规则
# key 需要的是一个函数
# 在sort内部实现的时候，调用了foo方法，并且传入了一个参数,参数就是列表里的元素
# students.sort(key=foo)

# 结合匿名函数可以这样写：
students.sort(key=lambda x: x['age'])
print(students)
