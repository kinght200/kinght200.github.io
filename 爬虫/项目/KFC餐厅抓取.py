import requests
from fake_useragent import UserAgent


# URL对象的准备，请求
def prepare_request(url, data, headers):
    resp = requests.post(url, data=data, headers=headers)
    resp.encoding = "UTF-8"
    return resp


# 对响应内容进行解析
def pares_data(resp, pageIndex):
    for i in range(1, pageIndex + 1):
        # 获取状态码
        # print(resp.status_code)
        resp_json = resp.json()
        # print(resp_json)

        # 查看Table1的元素个数是否为0，如果为0意味着该页面没有信息，所以循环退出
        if len(resp_json['Table1']) == 0:
            return 1
        # 如果Table1有信息，则吧该列表进行遍历
        for store_dict in resp_json['Table1']:
            print(store_dict)


if __name__ == '__main__':
    # 请求地址，POST请求
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"

    # UA信息
    headers = {
        "User-Agent": UserAgent().chrome
    }

    # 表单数据
    pageIndex = int(input("请输入你需要抓取的第几页的数据:> "))  # 拿取第几页的数据
    # print(i)
    data = {
        "cname": "",
        "pid": "",
        "keyword": "上海",
        "pageIndex": pageIndex,
        "pageSize": "10",
        # 防盗链：溯源，从当前本次请求的上一级是谁
        "Referer": "http://www.kfc.com.cn/kfccda/storelist/index.aspx"
    }

# 代理信息
proxy = {
    "http": "http://117.157.197.18:3128",
    "https": "https://117.157.197.18:3128"
}

resp = prepare_request(url, data=data, headers=headers)
pares_data(resp, pageIndex)
resp.close()
