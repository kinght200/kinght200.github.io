import requests
from fake_useragent import UserAgent

content = input('请输入你要检索的内容：')
url = f"https://www.sogou.com/web?query={content}"

# 添加一个请求头信息，UA
headers = {
    "User-Agent": UserAgent().chrome
}

# 浏览器参数
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20"
}

# 处理一个小小的反爬
resp = requests.get(url, headers=headers)
print(resp.text)

# 查看当前的UA信息
# print(resp.request.headers)
