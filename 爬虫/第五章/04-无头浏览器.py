import time

from selenium.webdriver import Edge

# 准备好参数配置
EDGE = {
    "browserName": "MicrosoftEdge",
    "version": "",
    "platform": "WINDOWS",

    # 关键是下面这个
    "ms:edgeOptions": {
        'extensions': [],
        'args': [
            '--headless',
            '--disable-gpu',
            '--remote-debugging-port=9222',
        ]}
}

driver_url = r"E:/pycharm代码/爬虫/第五章/msedgedriver.exe"
web = Edge(executable_path=driver_url, capabilities=EDGE)  # 把参数配置到浏览器中

web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")
time.sleep(2)
# 定位到下拉列表
# sel_el = web.find_element_by_xpath('//*[@id="OptionDate"]')
# # 对元素进行包装，包装成下拉菜单
# sel = Select(sel_el)
# # 让浏览器进行调整选项
# for i in range(len(sel.options)):  # i接受每一个下拉框选项的索引位置
#     sel.select_by_index(i)  # 按照索引进行切换
#     time.sleep(2)
#     table = web.find_element_by_xpath('//*[@id="TableList"]/table')
#     print(table.text)   # 打印所有的文本信息
#     print('==================')
#
# print('运行完毕')
# web.close()

# 如何拿到页面代码（经过数据加载以及js执行之后的结果的html内容）
print(web.page_source)
