# 代理，可以使用第三方的机器来代理你的请求
# 代理的弊端：
#   1.慢
#   2.代理ip不好找
import requests

# https://free.kuaidaili.com/free/


url = "http://www.baidu.com/"

# 准备代理信息
proxy = {
        "http": "http://117.157.197.18:3128",
        "https": "https://117.157.197.18:3128"
}
# proxies 代理
resp = requests.get(url)
resp.encoding = "UTF-8"
print(resp.text)

