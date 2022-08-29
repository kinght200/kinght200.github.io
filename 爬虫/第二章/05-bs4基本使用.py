# 安装
# pip install ba4

# 1.拿到页面源代码
# 2.使用bs4进行解析，拿到数据

import csv

import requests
from bs4 import BeautifulSoup

url = 'http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml'
resp = requests.get(url)
# print(resp.text)

f = open('菜价.csv', 'w')
csvwriter = csv.writer(f)

# 解析数据
# 1.把页面源代码交给BeautifulSoup进行处理，生成bs对象
page = BeautifulSoup(resp.text, "html.parser")  # 指定HTML解析器
# 2.从bs对象张查找数据
# find(标签，属性=值) 从第一找，找到就返回
# find_all(标签，属性=值) 从全部找，找到返回

# table = page.find('table', class_='hq_table')  # class是python的关键字，所以要加一个 _
table = page.find('table', attrs={'class': 'hq_table'})  # 与上面代码一个意思，此时可以避免class
# print(table)
# 拿到所有数据行
trs = table.find_all('tr')[1:]
for tr in trs:  # 每一行
    tds = tr.find_all('td')  # 拿到每行中的所有td
    name = tds[0].text  # .text 表示拿到被标签标记的内容
    low = tds[1].text
    avg = tds[2].text
    high = tds[3].text
    gui = tds[4].text
    kind = tds[5].text
    date = tds[6].text
    csvwriter.writerow([name, low, avg, high, gui, kind, date])
f.close()
print('over')
