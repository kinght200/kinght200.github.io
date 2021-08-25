from selenium.webdriver import Edge

driver_url = r"E:/pycharm代码/爬虫/第五章/msedgedriver.exe"
web = Edge(executable_path=driver_url)

# web.get("http://lagou.com")
#
# web.find_element_by_xpath('//*[@id="cboxClose"]').click()
#
# time.sleep(1)
#
# web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python", Keys.ENTER)
#
# time.sleep(1)
# web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').click()
#
# # 如何进入到新窗口中进行提取
# # 注意：在selenium的眼中，新窗口默认是不切换过来的
# web.switch_to.window(web.window_handles[-1])
#
# # 在新窗口中提取内容
# job_detail = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text
# print(job_detail)
#
# # 关掉子窗口
# web.close()
# # 变更selenium的窗口视角，回到原来的窗口中
# web.switch_to.window(web.window_handles[0])
# print(web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').text)

# 还有一种使用方式
# 如果页面中遇到了 iframe如何处理
web.get("http://www.91kanju.com/vod-play/541-2-1.html")

# 处理iframe的话，必须先拿到iframe，然后切换视角到iframe，然后才可以拿到数据
iframe = web.find_element_by_xpath('//*[@id="player_iframe"]')
web.switch_to.frame(iframe)  # 切换到iframe
# web.switch_to.default_content()  # 切换回原页面
tx = web.find_element_by_xpath('//*[@id="main"]/h3[1]').text
print(tx)
