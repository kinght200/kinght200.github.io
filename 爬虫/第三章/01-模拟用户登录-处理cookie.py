# 登录 -> 得到cookie
# 带着cookie 去请求到书架url -> 书上上的内容

# 必须得把上面的两个操作连起来
# 我们可以使用session进行请求 -> session可以认为是一连串的请求，在这个过程中的cookie不会丢失
import requests

# 翻译为会话
# session = requests.session()
# data = {
#     "loginName": "18089664450",
#     "password": "Rml1759552380."
# }
#
# # 1.登录
# url = "https://passport.17k.com/ck/user/login"
# session.post(url, data=data)
# # print(resp.text)
# # print(resp.cookies)   # 看cookies
#
# # 2。拿书架上的参数
# # 刚才的那个session中是有cookie的
# resp = session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
#
# print(resp.json())

# 会报错(用户登录信息错误)
resp = requests.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919', headers={  # 从浏览器复制cookie
    "Cookie": "GUID=1fe92851-3657-4d52-8a96-a134c8569e68; sajssdk_2015_cross_new_user=1; c_channel=0; c_csc=0; "
              "accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F07%252F87"
              "%252F07%252F76500787.jpg-88x88%253Fv%253D1617784544000%26id%3D76500787%26nickname%3DPeaces%26e"
              "%3D1633336805%26s%3Dcdf9b4b40ed6f7cc; "
              "sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2276500787%22%2C%22%24device_id%22%3A"
              "%22178ab768e14227-0bb162d94804e9-7166786d-1327104-178ab768e15b91%22%2C%22props%22%3A%7B%22"
              "%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer"
              "%22%3A%22https%3A%2F%2Fgraph.qq.com%2F%22%2C%22%24latest_referrer_host%22%3A%22graph.qq.com%22%2C%22"
              "%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A"
              "%221fe92851-3657-4d52-8a96-a134c8569e68%22%7D "
})
print(resp.text)
