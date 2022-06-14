from fake_useragent import UserAgent
import requests
from pyquery import PyQuery

html = """
<HTML>
    <div class="aaa">哒哒哒</div>
    <div class="bbb">嘟嘟嘟</div>
</HTML>
"""
p = PyQuery(html)

# 在xxx标签后面添加xxx新标签
# p("div.aaa").after("""<div class="ccc">吼吼吼</div>""")
# p("div.aaa").append("""<span>我爱你</span>""")

# p("div.bbb").attr("class", "aaa") # 修改属性
p("div.bbb").attr("id", "12306")  # 新增属性，前提是该标签没有这个属性
p("div.bbb").remove_attr("id")  # 删除属性
p("div.bbb").remove()  # 删除标签
print(p)
