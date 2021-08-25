import time

from selenium.webdriver import Edge
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

from chaojiying import Chaojiying_Client

# 初始化超级鹰
chaojiying = Chaojiying_Client('1759552380', 'Rml1759552380.', '916752')

# 如果你的程序被识别到了怎么办？
# 1.chrome的版本号如果小于88 在你启动浏览器的时候（此时没有加载任何网页内容），向页面嵌入js代码，去掉webdriver
# web = Chrome()

# web.execute_cpd_cmd("Page.addScriptToEvaluateOnNewDocument",{
#   "source":"""
#   window.navigator.webdriver = undefined
#     Object.defineProperty(navigator,'webdriver',{
#       get:() => undefined
#     })
#   """
# })

# 2.如果Chrome的版本大于88
option = Options()
# option.add_experimental_option('excludeSwitches',['enable_automation'])
option.add_argument('--disable-blink-features=AutomationControlled')

driver_url = r"E:/pycharm代码/爬虫/第五章/msedgedriver.exe"
web = Edge(executable_path=driver_url, options=option)

web.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(2)

web.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(3)

# 先处理验证码
imgs = web.find_element_by_xpath('//*[@id="J-loginImg"]')
# 用超级鹰去识别验证码
dic = chaojiying.PostPic(imgs.screenshot_as_png, 9004)
result = dic['pic_str']  # x1,y,|x2,y2|x3,y3
rs_list = result.split("|")
for rs in rs_list:  # x1,y1
    p_temp = rs.split(",")
    x = int(p_temp[0])  # :"49"
    y = int(p_temp[1])
    # 要让鼠标移动到某一个位置，然后进行点击
    # 移动到某个节点，然后去偏移多少,进行点击执行
    ActionChains(web).move_to_element_with_offset(imgs, x, y).click().perform()

time.sleep(2)
# 输入用户名和密码
web.find_element_by_xpath('//*[@id="J-userName"]').send_keys("123456789")
web.find_element_by_xpath('//*[@id="J-password"]').send_keys("0987654321")

# 点击登录
web.find_element_by_xpath('//*[@id="J-login"]').click()
time.sleep(5)

# 拖拽
btn = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn, 300, 0).perform()
