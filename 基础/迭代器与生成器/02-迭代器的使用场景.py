class Demo(object):
    def __init__(self, x):
        self.x = x
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count <= self.x:
            return self.count - 1
        else:
            raise StopIteration


d = Demo(10)
# print(d.__iter__().__next__())

# i =d.__iter__()
# i.__next__()
# 和以下代码效果相同
i = iter(d)  # 内置函数 iter 可以获取到一个可迭代对象的迭代器
print(next(i))
