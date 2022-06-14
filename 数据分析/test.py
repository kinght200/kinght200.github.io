def lo():
    sum = 0
    a = int(input("请输入第一个二位数："))
    b = int(input("请输入第二个二位数："))
    c = int(input("请输入第三个二位数："))
    d = int(input("请输入第四个二位数："))
    e = int(input("请输入第五个二位数："))
    f = int(input("请输入第六个二位数："))
    g = int(input("请输入第七个二位数："))
    h = int(input("请输入第八个二位数："))
    i = int(input("请输入第九个二位数："))
    j = int(input("请输入第十个二位数："))
    sum = a + b + c + d + e + f + g + h + i + j
    print("这10位数的总和为：", sum)
    print("这10位数的平均值为：", sum/10)

lo()