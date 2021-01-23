# 系统内置的异常：
# ZeroDivisionError :除以0的异常 1/0
# FileNotFoundError :文件不存在异常  open('xxx.txt')
# FileExistsError   :多次创建同名的文件夹 os.mkdir('test')
# ValueError        :值不对  int('hello')
# KeyError          :值不存在 person = {'name':'zhangsan'} person['age']
# SyntaxError       :语法错误 print（‘hello’，‘world’）
# IndexError        :角标错误 names = ['zhangsan','lisi'] names[5]

# 要求：让用户输入用户名和密码，如果用户名和密码的长度在 6-12位 正确，否者不正确

class LengthError(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '长度必须要在{}和{}之间'.format(self.x, self.y)


password = input('请输入你的密码：')
m = 6
n = 12
if m <= len(password) <= n:
    print('密码正确')
else:
    # print('密码格式不正确')
    # 使用 raise 关键字可以抛出一个异常
    raise LengthError(m, n)

# 把密码保存到数据库里
print('将密码保存到数据库')
