from requests_html import HTMLSession

s = HTMLSession()
url = 'https://www.baidu.com'
h = s.get(url)
print(h.html.html)
