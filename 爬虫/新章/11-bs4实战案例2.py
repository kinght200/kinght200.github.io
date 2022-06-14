from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests

domain = "https://www.umei.cc/"
"""
注意：
    子页面的url如果开头是/，直接在前面拼接上域名即可
    子页面的url不是/开头，此时需要找到主页面的url，去掉最后一个/后面的所有内容，和当前获取到的url进行拼接
"""

url = "https://www.umei.cc/bizhitupian/xiaoqingxinbizhi/"

resp = requests.get(url)
resp.encoding = 'UTF-8'
# print(resp.text)

# 图片名称
n = 1

main_page = BeautifulSoup(resp.text, "html.parser")
li_list = main_page.find_all("li", attrs={"class": "swiper-slide"})
# print(len(li_list)) # 拿到每一个li，里面包含了a
for a_list in li_list:
    a = a_list.find_all("a")  # 拿到里面所有的a标签
    # print(a)
    for h in a:
        href = h.get("href")  # 拿取每个href的值
        child_url = domain + href
        # print(child_url)
        child_resp = requests.get(child_url)  # 请求到子页面
        child_resp.encoding = "UTF-8"
        # print(child_resp.text)
        # 子页面的bs对象
        child_bs = BeautifulSoup(child_resp.text, "html.parser")
        div = child_bs.find("a", attrs={"href": "NULL"})
        img_src = div.find("img").get("src")  # 拿到图片的下载路径
        # print(img_src)

        # 下载图片
        img_resp = requests.get(img_src)
        # print(img_resp.text) # 注意，图片不是文本，不能获取text的内容

        # 注意，此时写入到文件的是字节，所以必须是wb
        with open(f"{n}.jpg", mode="wb") as f:
            f.write(img_resp.content)  # 把图片信息写入到文件中

        print(f"{n}图片下载完毕")
        n += 1
