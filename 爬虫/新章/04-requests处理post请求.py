from fake_useragent import UserAgent
import requests

url = "https://fanyi.baidu.com/sug"

data = {
    "kw": input("请输入一个单词:")
}

resp = requests.post(url, data=data)

#
print(resp.text)  # 拿到的是文本字符串
print(resp.json())  # 此时拿到的直接是json数据
