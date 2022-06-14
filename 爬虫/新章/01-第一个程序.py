from urllib.request import urlopen

# 百度https会自动转到http
url = "https://www.baidu.com/"

resp = urlopen(url)
# 此时拿到的是页面源代码
print(resp.read().decode("utf-8"))

# 写入文件
# with open("mybaidu.html", mode="w", encoding='utf-8') as f:
    # f.write(resp.read().decode("utf-8"))

