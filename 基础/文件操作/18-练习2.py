# 宠物店类 PetShop
# 属性：店名，店中的宠物[使用列表存储宠物]
# 方法：展示所有宠物的信息

# 宠物狗类：PetDog
# 属性：昵称，性别，年龄，品种
# 方法：叫，拆家，吃饭

# 宠物猫类 PetCat
# 属性：昵称，性别，年龄，品种
# 方法：叫，撒娇，吃饭
# 注意：狗的叫声是汪汪  猫的叫声是喵喵
# 狗吃的是骨头 猫吃的是鱼

class PetShop(object):
    def __init__(self, shop_name, pet_list=None):
        self.shop_name = shop_name
        if pet_list is None:
            pet_list = []
        self.pet_list = pet_list
        # self.pet_list = []

    def show_pets(self):
        if len(self.pet_list) == 0:
            print('本店还没有宠物')
            return
        print('{}有{}个宠物，它们是：'.format(self.shop_name, len(self.pet_list)))
        for pet in self.pet_list:
            # print('姓名:{}:性别:{},品种:{}，年龄:{}'.format(pet.name, pet.gender, pet.breed, pet.age))
            print(pet)


class Pet(object):
    def __init__(self, name, gender, age, breed):
        self.name = name
        self.gender = gender
        self.age = age
        self.breed = breed

    def bark(self):
        print(self.name + '正在叫')

    def eat(self):
        print(self.name + '正在吃东西')

    def __str__(self):
        return '姓名：{}，性别：{}，年龄：{}，品种：{}'.format(self.name, self.gender, self.age, self.breed)


class PetDog(Pet):
    def bark(self):
        print(self.name + '正在汪汪汪')

    def build_home(self):
        print(self.name + '正在拆家')

    def eat(self):
        print(self.name + '正在啃骨头')


class PetCat(Pet):
    def __init__(self, name, gender, age, breed, eyes_color):
        super(PetCat, self).__init__(name, gender, age, breed)
        self.eyes_color = eyes_color

    def bark(self):
        print(self.name + '正在喵喵喵')

    def sajiao(self):
        print(self.name + '正在撒娇')

    def eat(self):
        print(self.name + '正在吃鱼')

    def __str__(self):
        x = super(PetCat, self).__str__()
        x += ',眼睛的颜色：{}'.format(self.eyes_color)
        return x


dog1 = PetDog('大黄', 'female', 3, '哈士奇')
dog2 = PetDog('二黄', 'male', 2, '萨摩耶')
cat1 = PetCat('tom', 'male', 2, '英短', 'blue')
cat2 = PetCat('包子', 'female', 3, '加菲', 'break')

ps = PetShop('萌宠', [dog1, dog2, cat1, cat2])
ps.show_pets()
