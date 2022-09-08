import time

from selenium.webdriver import Edge
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

# from webdriver_manager.chrome import ChromeDriverManager
# service = ChromeService(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)


driver_url = r"E:/pycharm代码/爬虫/第五章/msedgedriver.exe"
# web = Edge(executable_path=driver_url)
web = Edge()
headers = {
    "User-Agent": UserAgent().edge
}


web.get("http://lagou.com")
# web.get_cookie(headers)

# 找到某个元素，点击它
el = web.find_element(By.XPATH, '//*[@id="changeCityBox"]/p[1]/a')
el.click()  # 点击事件

time.sleep(1)  # 让浏览器缓一会儿

# 找到输入框，输入python => 输入回车/点击搜索按钮
web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys("python", Keys.ENTER)

time.sleep(2)

# 查找存放数据的位置，进行数据提取
# 找到页面种存放数据的所有的li
li_list = web.find_elements(By.XPATH, '//*[@id="jobList"]/div[1]')

for li in li_list:
    # job_name = li.find_element(By.XPATH, './div[1]/div[1]/div[1]/div[1]/a').text
    # job_price = li.find_element(By.XPATH, './div[1]/div[1]/div[1]/div[2]/span').text
    # company_name = li.find_element(By.XPATH, './div[1]/div[1]/div[2]/div[1]').text
    print(li.text)
    # print(company_name, job_name, job_price)
web.close()
