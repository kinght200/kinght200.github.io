# 房子(House) 有 户型、总面积、剩余面积和家具名称列表 属性
# 新房子没有任何的家具
# 将 家具的名称 追加到 家具名称列表中
# 判断 家具的面积 是否 超过剩余面积，如果超过，提示不能添加家具

class House(object):
    # 缺省参数
    def __init__(self, house_type, total_area, fru_list=None):
        if fru_list is None:  # 如果这个值是None
            fru_list = []  # 将fru_list 设置为空列表

        self.house_type = house_type
        self.total_area = total_area
        self.free_area = total_area * 0.6
        self.fru_list = fru_list

    def add_fru(self, x):  # x = bed
        # print('需要将家具添加到房子里')
        if self.free_area < x.area:
            print('剩余面积不足，放不进去了')
        else:
            self.fru_list.append(x.name)
            self.free_area -= x.area

    def __str__(self):
        return '户型={}，总面积等于={}，剩余面积={}，家具列表={}'.format(self.house_type, self.total_area, self.free_area, self.fru_list)


# 家具(Furniture) 有 名字 和 占地面积属性，其中
# 席梦思(bed) 占地 4平米
# 衣柜(chest) 占地 2平米
# 餐桌(table) 占地 1.5平米
# 将以上三件家具 添加到 房子中
# 打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表

class Furniture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area


# 创建房间对象的时候，传入户型和总面积
house = House('一室一厅', 20)

bed = Furniture('席梦思', 4)
chest = Furniture('衣柜', 2)
table = Furniture('餐桌', 1.5)
# 新家具
sofa = Furniture('沙发', 10)

# 把家具添加到房间里(面向对象关注点：让谁做)
house.add_fru(sofa)
house.add_fru(bed)
house.add_fru(chest)
house.add_fru(table)

# print打印一个对象的时候，会调用这个对象的 __str__或者 __repr__的返回值
print(house)
