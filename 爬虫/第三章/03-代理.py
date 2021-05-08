# 原理：通过第三方的一个机器去发送请求
import requests

# 准备好ip
# 47.95.178.212:3128
proxies = {
    # 分开，该走哪个走哪个
    # "http":""
    "https": "https://47.95.178.212:3128"
}

resp = requests.get('https://www.baidu.com', proxies=proxies)
resp.encoding = 'utf8'
print(resp.text)
