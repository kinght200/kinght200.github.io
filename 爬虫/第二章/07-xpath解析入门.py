# xpath 是XML文档中搜索内容的一门语言
# html是xml的一个子集

# 安装lxml模块
# pip install lxml
# xpath解析
from lxml.html import etree

xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷若</nick>
        <nick id="joy">周杰伦</nick>
        <nick id="jolin">蔡依林</nick>
        <div>
            <nick>热热热热热1</nick>
        </div>
        <span>
            <nick>热热热热热2</nick>
        </span>
    </author>
    
    <parther>
        <nick id="ppc">胖胖胖</nick>
        <nick id="ppbc">胖胖不胖</nick>
    </parther>
</book>
"""
tree = etree.XML(xml)
# result = tree.xpath("/book")  # /表示层级关系，第一个/是根节点
# result = tree.xpath("/book/name")
# result = tree.xpath("/book/name/text()")  # text() 拿文本
# result = tree.xpath("/book/author/div/nick/text()")
# result = tree.xpath("/book/author//nick/text()")  # //后代
# result = tree.xpath("/book/author/*/nick/text()")  # * 任意的节点，通配符
result = tree.xpath("/book//nick/text()")

print(result)

# xpath的顺序是从1开始数的,[]表示索引
# [@xxx=xxx]，属性的筛选，取到后面的值
# 在xxx中继续去寻找，相对查找
# @属性，属性的值
