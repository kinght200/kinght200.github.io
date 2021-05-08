import requests
from fake_useragent import UserAgent

url = 'https://movie.douban.com/j/chart/top_list'

# 重新封装参数
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20"
}
headers = {
    'User-Agent': UserAgent().chrome
}
resp = requests.get(url=url, params=param, headers=headers)
# print(resp.request.url)
print(resp.json())
resp.close()  # 关闭服务
