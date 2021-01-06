def add_many(iter):
    x = 0
    for i in iter:
        x += i
    return x


nums = [1, 2, 3, 4, 6, 7, 9, 55, 76]
print(add_many(nums))
print(add_many((2, 4, 5, 42, 45, 6, 23, 44, 46, 546, 88)))

print(add_many({5, 8, 9, 0, 3}))
print(add_many(range(1, 101)))
