# 1.完成merge（L1,L2）函数：输入参数是两个从小到大排好序的整数列表L1和L2，返回合成后的从小到大排好序的大列表X。例如：
# merge（[1,4,5][2,7]）会返回[1,2,4,5,7]; merge([],[2,3,4])会返回[2,3,4]

# def merge(y, z):
#     x = []
#     x.extend(y)
#     x.extend(z)
#     x.sort()
#     return x
#
#
# print(merge([1, 8, 6], [2, 3]))

# 2.用python实现简单计算器，要求分别定义 加、减、乘、除这四种功能的函数，然后定义一个函数进行运算调用实现计算器功能。
# def jiafa(i, o):
#     w = i + o
#     print(w)
#
#
# def jianfa(i, o):
#     w = i - o
#     print(w)
#
#
# def chengfa(i, o):
#     w = i * o
#     print(w)
#
#
# def chufa(i, o):
#     w = i / o
#     print(w)
#
#
# def jisuanqi(i, o):
#     jiafa(i, o)
#     jianfa(i, o)
#     chengfa(i, o)
#     chufa(i, o)
#
#
# a = int(input("请输入要运算的第一个数："))
# b = int(input("请输入要运算的第二个数："))
# jisuanqi(a, b)
#
#
# 3.编写函数，求出1+（1+2）+（1+2+3）+......+(1+2+3+4+....+n)的和，函数以n为参数，n由用户从键盘输入。
# def i():
#     b = 0
#     n = int(input('请输入你要计算的数字：'))
#     for a in range(1, n + 1):
#         for j in range(1, a + 1):
#             b += j
#     return b
#
#
# print(i())
#
# 4.已知有个列表[1,2,3,4,5],让列表的每个元素加1，把结果不能被2整除的元素筛查出来。（提示：用内置函数filter做）
# i = lambda o: o % 2
# list1 = [1, 2, 3, 4, 5]
# y = []
# for x in list1:
#     a = x + 1
#     y.append(a)
# list2 = list(filter(i, y))
# print('列表中不能被2整除的数是{}'.format(list2))
#
#
# 5.任意定义一个动物类
# 使用__init__方法，在创建某个动物对象时，为其添加name、age、color，food等属性，如‘熊猫’，5，‘黑白’，66，‘竹子’
# 为动物类定义一个run方法，调用run方法时打印相关信息，如打印出“熊猫正在奔跑”
# 为动物类定义一个get_age方法，调用get_age方法时打印出相关信息，如打印出“这只熊猫今年5岁了”、
# 为动物类定义一个eat方法，调用eat方法时打印相关信息，如打印出“熊猫正在吃竹子”
# 通过东未来分别创建出3值不同种类的动物，分别调用它们的方法，让他们“跑起来”，“吃起来”。
#
class Dongwu(object):
    def __init__(self, name, age, color, food):
        self.name = name
        self.age = age
        self.color = color
        self.food = food

    def get_age(self):
        print("年龄为%s" % self.age)

    def run(self):
        print("%s正在奔跑" % self.name)

    def eat(self):
        print("%s正在吃%s" % (self.name, self.food))


eagle = Dongwu("鹰", 6, "灰黑色", "昆虫")
eagle.run()
eagle.get_age()
eagle.eat()

giraffe = Dongwu("长颈鹿", 5, "黑色", "树叶")
giraffe.run()
giraffe.get_age()
giraffe.eat()

cat = Dongwu("猫", 1, "蓝色", "猫粮")
cat.run()
cat.get_age()
cat.eat()
