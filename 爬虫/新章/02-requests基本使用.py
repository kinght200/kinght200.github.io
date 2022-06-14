import requests

url = "http://www.baidu.com/"

resp = requests.get(url)
resp.encoding ="UTF-8"
print(resp.text)