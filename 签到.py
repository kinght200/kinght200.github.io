import requests
from fake_useragent import UserAgent

url = 'http://www.baidu.com/'

# 浏览器请求头
# headers = {
#     'User-agent': UserAgent().chrome
# }
#
# reqs = requests.get(url=url, headers=headers)
# reqs.encoding = 'utf-8'
# ques = reqs.text
# print(ques)

def fun1():
    return 'hello','world'

print(fun1())
