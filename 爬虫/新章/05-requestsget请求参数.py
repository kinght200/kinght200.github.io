from fake_useragent import UserAgent
import requests

url = "https://movie.douban.com/j/chart/top_list"

# 请求参数
data = {
    "type": "13",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20"
}

# UA防止反爬
headers = {
    "User-Agent": UserAgent().chrome
}

resp = requests.get(url, params=data, headers=headers)
print(resp.text)
# print(resp.request.url)
