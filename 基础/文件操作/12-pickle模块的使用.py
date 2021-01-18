# python 里存入数据只支持 字符串和二进制
# json:将python里的数据(str/list/tuple/dict/int/float/bool/None)等转换成为对应的json
# pickle：将python里任意的对象转换成为二进制

import pickle

# 序列化 dumps:将python的数据转换成为二进制
#       dump:将python数据转换成为二进制，同时保存到指定文件

# 反序列化 loads:将二进制加载成为python数据
#         load：读取文件，并将文件的二进制内容加载成为python数据

names = ['张三', '李四', '王五', '杰克']


# b_names = pickle.dumps(names)
# print(b_names)
#
# file = open('names.txt', 'wb')
# file.write(b_names)  # 写入的是二进制，不是纯文本
# file.close()
#
# file1 = open('names.txt','rb')
# x = file1.read()
# y = pickle.loads(x)
# print(y)
# file1.close()

# file2 = open('names.txt', 'wb')
# pickle.dump(names, file2)
# file2.close()
#
# file3 = open('names.txt', 'rb')
# pickle.load(file3)

class Dog(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color


d = Dog('大黄', '黄色')

# 保存到文件里
pickle.dump(d, open('dog.txt', 'wb'))

# 从文件里加载出来
dd = pickle.load(open('dog.txt', 'rb'))
print(dd.name, dd.color)
