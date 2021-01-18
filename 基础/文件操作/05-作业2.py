# 建立一个汽车类Auto
# 包括轮胎个数，汽车颜色，车身重量，速度等属性，并通过不同的构造方法创建实例对象
# 至少要求 汽车能够加速 减速 停车

# 再定义一个小汽车类 CarAuto 继承Auto 并添加空调、cd属性
# 并且重新实现方法覆盖加速、减速的方法

class Auto(object):
    def __init__(self, color, weight, speed=0, wheel_count=4):
        self.color = color
        self.weight = weight
        self.speed = speed
        self.wheel_count = wheel_count

    def change_speed(self, x):
        """
        修改车速
        :param x: 表示要修改的车速值。如果是正数，表示加速，复数表示减速，0表示停车
        """
        if x == 0:  # 如果传递的参数0，表示要停车
            self.speed = 0
            return
        self.speed += x
        if self.speed <= 0 and x < 0:
            self.speed = 0  # 车速度本来就是0，又减速，减不了
            return  # return 后面可以什么数据都不加，表示函数结束


class CarAuto(Auto):
    def __init__(self, color, weight, ac, cd, speed=0, wheel_count=4):
        # self.color = color
        # self.weight = weight
        # self.speed = speed
        # self.wheel_count = wheel_count

        super(CarAuto, self).__init__(color, weight, speed, wheel_count)
        self.ac = ac
        self.cd = cd


car = CarAuto('白色', 1.6, '美的', 'Android')
print(car.color)
print(car.weight)
print(car.cd)
print(car.ac)
print(car.speed)
print(car.wheel_count)
