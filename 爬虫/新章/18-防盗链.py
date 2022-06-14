# 1.拿到contId
# 2.拿到videoStatus返回的json -> srcURL
# 3.srcURL里面的内容进行修整
# 4.下载视频

import requests
from fake_useragent import UserAgent
from pyquery import PyQuery

# 拉取视频的网址
url = "https://www.pearvideo.com/video_1764627"
conId = url.split("_")[1]
headers = {
    "User-Agent": UserAgent().chrome,
    # 防盗链：溯源，从当前本次请求的上一级是谁
    "Referer": url
}

videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={conId}&mrd=0.12215723084962571"
resp = requests.get(videoStatusUrl, headers=headers)
# print(resp.text)
dic = resp.json()
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
srcUrl = srcUrl.replace(systemTime, f"cont-{conId}")
# print(srcUrl)


# 下载视频
with open("a.mp4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)

# https://video.pearvideo.com/mp4/adshort/20220607/cont-1764627-15892168_adpkg-ad_hd.mp4
# https://video.pearvideo.com/mp4/adshort/20220607/cont-1764627-15892168_adpkg-ad_hd.mp4
# https://video.pearvideo.com/mp4/adshort/20220607/1654676176390-15892168_adpkg-ad_hd.mp4
