# 序列化：将数据从内存持久化保存到硬盘的过程
# 反序列化：将数据从硬盘加载到内存的过程

# write时，只能写入字符串或者二进制
# 字典、列表、数字等都不能直接写入到文件里

# 将数据转换成为字符串：repr/str 使用json模块
# json 本质就是字符串，区别在于json里就是用双引号表示字符串
# 将数据转换成为二进制：使用pickle模块
import json

names = ['zhangsan', 'lisi', 'jack', 'wangwu']
# x = json.dumps(names)  # dumps 的作用是将数据转换成为字符串
# print(x)  # '["zhangsan", "lisi", "jack", "wangwu"]'

file = open('names.txt', 'w', encoding='utf8')

# file.write(x)


# json里将数据持久化有两个方法：
# dumps:将数据转换成为json字符串，不会将数据保存到文件里。
# dump：将数据转换成为json字符串的同时写入到指定文件

# json 反序列化也有两个方法：
# loads：将json字符串加载成为python里的数据
# load：读取文件，把读取的内容加载成为python里的数据
json.dump(names, file)
file.close()

# loads
x = '{"name":"zhangsan","age":18}'  # 符合json规则的字符串
p = json.loads(x)
print(p)
