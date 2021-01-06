def calc(a, b, fn):
    c = fn(a, b)
    return c


x1 = calc(5, 7, lambda x, y: x + y)
x2 = calc(14, 65, lambda x, y: x - y)
x3 = calc(98, 66, lambda x, y: x * y)
x4 = calc(99, 65, lambda x, y: x / y)
print(x1, x2, x3, x4)
