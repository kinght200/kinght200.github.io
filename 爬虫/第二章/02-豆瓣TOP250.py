# 拿到页面源代码
# 通过re来提取想要的有效信息

import csv
import re
import requests
from fake_useragent import UserAgent

url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent': UserAgent().edge
}
resp = requests.get(url, headers=headers)
# 拿到页面源代码
# print(resp.text)
page_content = resp.text

# 解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p calss="">.*?<br>(?P<year>.*?)&nbsp.*?<span '
                 r'class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                 r'<span>(?P<num>.*?)人评价</span>', re.S)
# 开始匹配
result = obj.finditer(page_content)
f = open('data.csv', 'w')
csvwriter = csv.writer(f)
for it in result:
    # print(it.group("name"))
    # print(it.group("score"))
    # print(it.group("num"))
    # print(it.group("year").strip())
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())
f.close()
print('over')
