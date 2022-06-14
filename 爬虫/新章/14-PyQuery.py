from pyquery import PyQuery

# 快速总结：
# 1.pyquery(选择器)
# 2.items()  当选择器选择的内容很多的时候，需要一个一个处理的时候
# 3.attr(属性名) 获取属性信息
# 4.text() 获取文本

html = """
    <ul>
        <li class="aaa"><a href="http://www.google.com">谷歌</a></li>
        <li class="aaa"><a href="http://www.baidu.com">百度</a></li>
        <li class="bbb" id="qq"><a href="http://www.qq.com">腾讯</a></li>
        <li class="bbb"><a href="http://www.yuanlai.com">猿来</a></li>
    </ul>
"""

# 加载html内容
page = PyQuery(html)
# print(page)
# print(type(page))

# pyquery对象直接（css选择器）
# a = page("a")
# print(a)
# print(type(a))

# 链式操作
# a = page("li")("a")
# print(a)

# a = page(".aaa a")  # class="aaa"
# print(a)

# a = page("#qq a")  # id="qq"
# print(a)

# href = page("#qq a").attr("href")  # 拿属性
# text = page("#qq a").text()  # 拿文本
# print(href,text)

# 坑,如果多个标签同时拿属性，只能默认拿到第一个
# href = page("li a").attr("href")
# print(href)

# 多个标签属性
# it = page("li a").items()
# for item in it:  # 从迭代器中拿到每一个标签
#     href = item.attr("href")  # 拿到href属性\
#     text = item.text()
#     print(text, href)

div = """
    <div><span>我爱你</span></div>
"""
p = PyQuery(div)
html = p("div").html()  # 全都要
text = p("div").text()  # 只要文本，所有的HTML标签呗过滤掉
print(html)
print(text)
