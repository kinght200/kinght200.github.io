# 设计两个类：
# 一个点类，属性包括x，y坐标
# 一个Rectangle类(矩形)，属性有左上角和右下角的坐标
# 方法：1.计算矩形的面积；2.判断点是否在矩形内
# 实例化一个点对象，一个矩形对象，输出矩形的面积，输出点是否在矩形内

class Point(object):
    # Point 方法在创建时，需要两个int类型的参数，用来表示x，y坐标
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Rectangle(object):
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def get_area(self):
        # 面积 = 长 * 宽
        length = abs(self.bottom_right.x - self.top_left.x)
        width = abs(self.top_left.y - self.bottom_right.y)
        return length * width

    def is_inside(self, point):
        if self.bottom_right.x >= point.x >= self.top_left.x and self.top_left.y >= point.y >= self.bottom_right.y:
            return True
        else:
            return False


p1 = Point(4, 20)  # 定义左上角的点
p2 = Point(30, 8)  # 定义右下角的点

r = Rectangle(p1, p2)  # 把左上角和右下角的点床底给矩形
print(r.get_area())

p = Point(10, 13)
print(r.is_inside(p))


# 计算器

class Calculator(object):
    # def add(self, a, b):
    #     return a + b
    @staticmethod
    def add(a, b):
        return a + b


# 没有必要创建一个实例对象
# c = Calculator()
# print(c.add(4, 5))
print(Calculator.add(4, 5))
