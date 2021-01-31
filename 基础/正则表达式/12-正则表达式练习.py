import re

# 用户名匹配
# 1.用户名只能包含数字、字母和下划线
# 2.不能以数字开头  3.长度在6到16位范围

# username = input('请输入用户名：')
# x = re.match(r'^\D[a-zA-Z0-9_]{5,15}$', username)
# x = re.fullmatch(r'[a-zA-Z_][a-zA-Z0-9_]{5,15}', username)
# if x is None:
#     print('输入的用户名不符合规范')
# else:
#     print(x)

# 密码匹配
# 1.不能包含！@%^&* 字符  2.必须以字母开头
# 3.长度在6到12位
# password = input('请输入密码')
# y = re.fullmatch(r'[a-zA-Z][^!@#$%^&*]{5,11}', password)
# if y is None:
#     print('输入的密码不符合规范')
# else:
#     print(y)

z = []
try:
    with open('demo.txt', 'r', encoding='utf8') as file:
        content = file.read()  # 读出所有的内容
        z = re.findall(r'1000phone.*', content)

        # while True:
        #     content = file.readline().strip('\n')
        #     if not content:
        #         break
        #     if re.match(r'^1000phone', content):
        #         z.append(content)
except FileNotFoundError:
    print('文件打开失败')

print(z)

# 匹配ip地址 0.0.0.0 ~ 255.255.255.255
# num = input('请输入一个数字:')
# \d:一位数    [1-9]\d:两位数     1\d{2}:1xx  2:00~55
# x = re.fullmatch(r'((\d|[1-9]\d|1\d{2}|2([0-4]\d|5[0-5]))\.){3}(\d|[1-9]\d|1\d{2}|2([0-4]\d|5[0-5]))', num)
# print(x)

# 找出数字并求和
x = '-3.14good87nice19bye'
o = re.finditer(r'-?(0|[1-9]\d*)(\.\d+)?', x)
for i in o:
    print(i.group())
