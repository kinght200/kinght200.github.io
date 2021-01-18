import sys

# sys.stdin  接受用户的输入，读取键盘里输入的数据
# sys.stdout 标准输出
# sys.stderr 错误输出

s_in = sys.stdin  # input 就是读取 sys.stdin 里的数据
# 控制台多行输入输出
# while True:
#     content = s_in.readline().rstrip('\n')
#     if content == '':
#         break
#     print(content)

# 标准输出
sys.stdout = open('stdout.txt', 'w', encoding='utf8')
print('hello')
print('yes')
print('good')

# 错误输出
sys.stderr = open('stderr.txt', 'w', encoding='utf8')
print(1 / 0)
