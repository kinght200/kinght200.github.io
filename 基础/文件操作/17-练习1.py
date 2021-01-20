# 定义一个点类 Pointer
# 属性是横向坐标x与纵向坐标y
# 定义一个园类 Circle
# 属性有圆心点 cp 与半径 radius
# 方法有：
# 1.求圆的面积
# 2.求圆的周长
# 3.求指定点与原的关系
# 提示：关系有三种[园内、园外、圆上]
# 涉及到的数学公式：指定点与圆心点之间的距离 与 圆的半径进行比较
import math


class Pointer(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(object):
    def __init__(self, cp, radius):  # cp = p，radius = 3
        self.cp = cp
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * math.pi

    def get_length(self):
        return self.radius * 2 * math.pi

    def relationship(self, point):  # point = p1
        """
        求一个点和园的关系.有三种关系：在园内、园外、园上
        :param point:需要判断的点
        """
        # 计算圆心到point的距离
        distance = (point.x - self.cp.x) ** 2 + (point.y - self.cp.y) ** 2
        if distance > self.radius ** 2:
            print('在园外')
        elif distance < self.radius ** 2:
            print('在园内')
        else:
            print('在园上')


p = Pointer(3, 4)  # 创建了一个Pointer对象

c = Circle(p, 5)  # 创建好的Pointer对象传递给了Circle对象c

print(c.get_area())
print(c.get_length())

p1 = Pointer(10, 10)
c.relationship(p1)
