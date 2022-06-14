"""
1.提取到主页面中的每一个电影的背后的哪个url地址
    1.拿到”2022必看热片“那一块的HTML代码。
    2.从刚才拿到的HTML代码中提取到href的值

2.访问子页面，提取到电影的名称以及下载地址
    1.拿到子页面的页面源代码
    2.数据提取

"""
import requests
import re
from fake_useragent import UserAgent

url = 'http://www.dy2018.com/'

headers = {
    "User-agent": UserAgent().chrome
}

resp = requests.get(url, headers=headers)
resp.encoding = 'gb2312'
# print(resp.text)

# 1.提取2022必看热片部分的HTML代码。
obj1 = re.compile("2022必看热片.*?<ul>(?P<html>.*?)</ul>", re.S)
result1 = obj1.search(resp.text)
html = result1.group("html")
# print(html)

obj3 = re.compile(r'<div id="Zoom">.*?◎片　　名(?P<movie>.*?)<br />'
                  r'.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf">'
                  r'<a href="(?P<download>.*?)">', re.S)

# 2.提取a标签中href的值
obj2 = re.compile(r"<li><a href='(?P<herf>.*?)' title")
result2 = obj2.finditer(html)
for item in result2:
    # print(item.group("herf"))
    # 拼接出子页面的url
    child_url = url.strip("/") + item.group("herf")
    child_resp = requests.get(child_url)
    child_resp.encoding = 'gb2312'
    # print(child_resp.text)

    result3 = obj3.search(child_resp.text)
    movie = result3.group("movie")
    download = result3.group("download")
    print(movie, download)
