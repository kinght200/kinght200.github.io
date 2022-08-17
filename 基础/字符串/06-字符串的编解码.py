s = "天涯共此时"
# 编码
print(s.encode('GBK'))  # 在GBK这种编码格式中 一个中文占两个字节
print(s.encode('UTF-8'))  # 在UTF-8这种编码格式中 一个中文占三个字节
# 解码
# byte代表就是一个二进制数据（字节类型的数据）
byte = s.encode('GBK')  # 编码
print(byte.decode('GBK'))  # 解码
