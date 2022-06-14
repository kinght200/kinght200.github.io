# 思路：
# 1.拿到页面源代码
# 2.编写正则，提取页面数据
# 3.保存数据

f = open("top250.csv", mode="w", encoding="UTF-8")

from fake_useragent import UserAgent
import requests
import re

url = "https://movie.douban.com/top250"

headers = {
    "User-agent": UserAgent().chrome
}

resp = requests.get(url, headers=headers)
resp.encoding = "UTF-8"  # 解决乱码问题
content = resp.text
# print(content)

# 编写正则表达式
# re.S 可以让正则中的.匹配换行符
obj = re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
                 r'.*?<p class="">.*?导演:(?P<dao>.*?)&nbsp;.*?<br>'
                 r'(?P<year>.*?)&nbsp;.*?<span class="rating_num" property="v:average">'
                 r'(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>', re.S)

result = obj.finditer(content)
# 拿结果
for item in result:
    name = item.group("name")
    dao = item.group("dao")
    year = item.group("year").strip()  # 去掉字符串左右两端的空白
    score = item.group("score")
    num = item.group("num")
    # print(name, dao, year, score, num)
    f.write(f"{name}，{dao}，{year}，{score}，{num}\n")

f.close()
resp.close()
print("豆瓣TOP250提取完毕\n")
