# 1.图像识别
# 2.选择互联网上成熟的验证码破解工具

import time

from selenium.webdriver import Edge

from chaojiying import Chaojiying_Client

driver_url = r"E:/pycharm代码/爬虫/第五章/msedgedriver.exe"
web = Edge(executable_path=driver_url)

web.get('http://www.chaojiying.com/user/login/')

# 处理验证码
img = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('1759552380', 'Rml1759552380.', '916752')
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']

# 向页面中填入用户名，密码，验证码
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('1759552380')
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('Rml1759552380.')
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)
time.sleep(5)

# 点击登录
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()
