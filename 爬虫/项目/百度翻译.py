import requests
from fake_useragent import UserAgent

url = 'https://fanyi.baidu.com/sug'
data = {
    "kw": "boy"
}
ua = {
    "User-Agent": UserAgent().chrome
}

resp = requests.post(url, data=data, headers=ua)
resp.encoding = "UTF-8"
resp_json = resp.json()  # 此时拿到一堆json列表

# 服务器返回的数据都是字符串格式，所以要进一步解析他
# json格式的字符串要用json解析
# xml格式的字符串要用xml解析

# json.load()
# json.loads()

# json.dump()
# json.dumps()

# json_obj = json.loads(resp_json, encoding="UTF-8")
for i in resp_json["data"]:
    print(i)
