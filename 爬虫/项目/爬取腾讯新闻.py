import requests

url = 'https://www.paddlepaddle.org.cn/'

resp = requests.get(url)
print(resp.text)
resp.close()
