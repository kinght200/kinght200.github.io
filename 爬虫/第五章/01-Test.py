# 能不能让我的程序链接到浏览器，让浏览器来完成各种复杂的操作，我们只接受最终的结果
# selenium：自动化测试工具
# 可以：打开浏览器，然后像人一样去操作浏览器
# 程序员可以从selenium种直接提取网页上的各种信息
# 环境搭建：
#   pip install selenium -i 清华源
#   下载浏览器驱动:https://npm.taobao.org/mirrors/chromedriver（具体的需要看你自己喜欢啥浏览器）
#       把解压缩的浏览器驱动 chromedirver(和上一步的驱动一样，不仅限与chrome) 放在python解释器所在的文件夹
# 让selenium启动谷歌浏览器

from selenium.webdriver import Edge

# 1.创建浏览器对象
driver_url = r"E:\pycharm代码\pythonProject\爬虫\第五章\msedgedriver.exe"
# web = Edge(executable_path=driver_url)
web = Edge()
# 2.打开一个网址
web.get("http://www.baidu.com")

print(web.title)
# print(web.name)
