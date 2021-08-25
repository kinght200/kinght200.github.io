import time

from selenium.webdriver import Edge
from selenium.webdriver.common.keys import Keys

driver_url = r"E:/pycharm代码/爬虫/第五章/msedgedriver.exe"
web = Edge(executable_path=driver_url)

web.get("http://lagou.com")

# 找到某个元素，点击它
el = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
el.click()  # 点击事件

time.sleep(1)  # 让浏览器缓一会儿

# 找到输入框，输入python => 输入回车/点击搜索按钮
web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python", Keys.ENTER)

time.sleep(2)

# 查找存放数据的位置，进行数据提取
# 找到页面种存放数据的所有的li
li_list = web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li')
for li in li_list:
    job_name = li.find_element_by_tag_name('h3').text()
    job_price = li.find_element_by_by_xpath(".div/div/div[2]/div/span").text
    company_name = li.find_element_by_by_xpath('./div/div[2]/a').text
    print(company_name, job_name, job_price)
