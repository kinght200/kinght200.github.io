age = input('请输入你的年龄：')  # input接受到的用户输入是一个字符串

# if age.isdigit():
try:
    age = float(age)
except ValueError as e:
    print('输入的不是数字')
else:
    if age > 18:
        print('欢迎来到我的网站')
    else:
        print('未满18岁，请自动离开')
