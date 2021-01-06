def test(a, b):
    x = a // b
    y = a % b

    # 一般情况下，一个函数最多只会执行一个return语句
    # 特殊情况(finally语句)下，一个函数可能会执行多个return语句
    return [x, y]  # return语句表示一个函数的结束


print(test(15, 3))
