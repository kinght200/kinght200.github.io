import execjs

# 1.实例化一个node对象
node = execjs.get()

# 2.js源文件编译
ctx = node.compile(open('wechat.js', encoding='UTF-8').read())
# print(ctx)

# 3.执行js函数
funcName = 'getPwd("{0}")'.format('12345678')
pwd = ctx.eval(funcName)
print(pwd)
