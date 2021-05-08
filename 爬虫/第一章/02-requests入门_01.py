import requests
from fake_useragent import UserAgent

query = input('输入一个你喜欢的明星:')
url = f'https://www.douban.com/search?q={query}'
dic = {
    'User-Anger': UserAgent().chrome
}
resp = requests.get(url, headers=dic)
print(resp)  # 网页请求码 200
print(resp.text)  # 拿到网页源代码
resp.close()
