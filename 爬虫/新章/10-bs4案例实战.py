from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests

f = open("新发地菜价.csv", mode="w", encoding="UTF-8")

# 服务器错误，网页进不去
url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
resp = requests.get(url)
# print(resp.text)

# 初始化bs4对象
page = BeautifulSoup(resp.text, "html.parser")
table = page.find("table", attrs={"class": "hq_table"})
trs = table.find_all("tr")[1:]  # 此时拿到了除了第一行以外的所有tr
for tr in trs:  # 每一行
    tds = tr.find_all("td")
    name = tds[0].text  # 拿到名称
    low = tds[1].text
    avg = tds[2].text
    hig = tds[3].text
    kind = tds[4].text
    dan = tds[5].text
    date = tds[6].text
    # print(name, low, avg, hig, kind, dan, date)
    f.write(f"{name},{low},{avg},{hig},{kind},{dan},{date}\n")

f.close()
resp.close()
print("成功")
