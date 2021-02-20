# requests 模块是第三方的模块，可以用来发送网络连接
# pip install requests

import requests

response = requests.get('http://www.baidu.com')
# print(response) 结果是一个Response 对象

# content 指的是返回的结果，是一个二进制,可以用来传递图片等信息
# print(response.content.decode('utf8'))    # 将二进制解码成为字符串

# 获取到的结果接收一个文本
print(response.text)

# 获取到状态码
print(response.status_code)  # 200

# 如果返回的结果是一个json字符串，可以解析json字符串
print(response.json())
