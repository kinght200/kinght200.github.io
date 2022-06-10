import requests
from fake_useragent import UserAgent

url = 'http://www.baidu.com/'

# 浏览器参数
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20"
}

# 浏览器请求头
headers = {
    'User-agent': UserAgent().edge
}

# 代理
proxies = {
    "https": "https://206.253.164.122:80"
}

reqs = requests.get(url=url, headers=headers)
reqs.encoding = 'utf-8'
# ques = reqs.text
print(reqs.text)

# tree = etree.HTML(page)
# res = tree.xpath(
#     "/html/body/font/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/table[24]/tbody/tr[3]//text()")
# print(res)
