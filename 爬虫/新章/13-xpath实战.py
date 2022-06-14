from fake_useragent import UserAgent
from lxml.html import etree
import requests

"""
1.拿到页面源代码
2.从页面源代码中提取你需要的数据，价格、名称、公司名称

"""
url = "https://zunyi.zbj.com/search/f/?kw=saas"
resp = requests.get(url)
resp.encoding = "UTF-8"
# print(resp.text)


# 提取数据
et = etree.HTML(resp.text)
# Gsname = et.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div[1]/div/div/a[1]/div[1]/p/text()")[1]
# Jg = et.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div[1]/div/div/a[2]/div[2]/div[1]/span[1]/text()")
divs = et.xpath("//div[@class='new-service-wrap']/div")
# print(divs)
for div in divs:
    # 此时的div就是一条书库，对应一个商品信息
    # 商品价格
    price = div.xpath("./div/div/a/div[2]/div[1]/span[1]/text()")
    if not price:  # 过滤掉无用的数据
        continue
    price = price[0]
    # 公司名称
    company = div.xpath(".//*[@id='utopia_widget_76']/a[1]/div[1]/p/text()")[1]
    company = company.strip()
    # 名称
    name = div.xpath("//*[@id='utopia_widget_76']/a[2]/div[2]/div/p/text()")[1]  # //表示提取p的所有文本，包括所有内容
    name = "".join(name)
    print(name, company, price)
