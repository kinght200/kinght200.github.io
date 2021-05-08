# 1.拿到主页面源代码，然后提取到子页面的链接地址，href
# 2.通过href拿到子页面的内容，从子页面中找到图片的下载地址 img -> src
# 3.下载图片

import time

import requests
from bs4 import BeautifulSoup

url = 'https://www.umei.cc/bizhitupian/weimeibizhi/'
resp = requests.get(url)
resp.encoding = 'utf8'  # 处理乱码
# print(resp.text)

# 把源代码交给bs
main_page = BeautifulSoup(resp.text, 'html.parser')
alist = main_page.find("div", class_="TypeList").find_all("a")  # 把范围第一次缩小
# print(alist)
for a in alist:
    href = a.get('href')  # 直接通过get就可以拿到属性的值
    # 拿到子页面的源代码
    child_page_resp = requests.get(href)
    child_page_resp.encoding = 'utf8'
    child_page_text = child_page_resp.text
    # 从子页面拿到图片的下载路径
    child_page = BeautifulSoup(child_page_text, 'html.parser')
    p = child_page.find("p", align="center")
    img = p.find("img")
    # print(img)
    # 从img中提取到src关键字
    src = img.get('src')
    # 下载图片
    img_resp = requests.get(src)
    # img_resp.content    # 这里拿到的是字节
    img_name = src.split("/")[-1]  # 拿到url中的最后一个/以后的内容
    with open("img/" + img_name, 'wb') as f:
        f.write(img_resp.content)  # 图片内容写入文件

    print('over!!!', img_name)
    time.sleep(3)

print('all over')
