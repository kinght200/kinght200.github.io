# 1。拿到contId
# 2.拿到videoStatus返回的json. -> srcURL
# 3。srcURL里面的内容锦绣修整
# 4.下周视频
import requests
from fake_useragent import UserAgent

# 拉取视频的网址
url = 'https://www.pearvideo.com/video_1725952'
contId = url.split('_')[1]

videoStatusUrl = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.6952007481227842'
headers = {
    "User-Agent": UserAgent().edge,
    # 防盗链：溯源，当前本次请求的上一级是谁
    "Referer": url
}
resp = requests.get(videoStatusUrl, headers=headers)
dic = resp.json()
srcUrl = dic['videoInfo']['videos']['srcUrl']
systemTime = dic['systemTime']
srcUrl = srcUrl.replace(systemTime, f'cont_{contId}')
# print(srcUrl)

# 下载视频
with open('a.mp4', 'wb')as f:
    f.write(requests.get(srcUrl).content)

# https://video.pearvideo.com/mp4/adshort/20210408/cont_1725952-15650873_adpkg-ad_hd.mp4
# https://video.pearvideo.com/mp4/adshort/20210408/cont-1725952-15650873_adpkg-ad_hd.mp4
# https://video.pearvideo.com/mp4/adshort/20210408/1617873484270-15650873_adpkg-ad_hd.mp4
