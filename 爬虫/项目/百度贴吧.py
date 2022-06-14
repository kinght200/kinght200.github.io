from fake_useragent import UserAgent
import requests

if __name__ == '__main__':
    name = input("请输入你要爬取的贴吧:> ")
    page = int(input("请输入你要爬取的页数:> "))
    url = f"https://tieba.baidu.com/f?kw={name}&ie=utf-8&pn={(page - 1) * 50}"
    # print(url)

    headers = {
        "User-Agent": UserAgent().chrome
    }
    for i in range(1, page+1):
        resp = requests.get(url, headers=headers)
        resp.encoding = "UTF-8"
        # print(resp.text)
        with open("百度贴吧.html", mode="w", encoding="UTF-8") as f:
            f.write(resp.text)
        print(name, "下载完成")
print("所有文件下载完成\n")
