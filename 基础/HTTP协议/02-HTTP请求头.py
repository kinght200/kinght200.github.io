import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.3.139', 1657))
# 处理数据的长度
server_socket.listen(128)

client_socket, client_addr = server_socket.accept()

data = client_socket.recv(1024).decode('utf8')
print('接收到{}的数据{}'.format(client_addr[0], data))
"""
# GET 请求方式，GET/POST/PUT/DELETE......
# /index.html 请求的路径以及请求参数(会变化)
# HTTP/1.1 HTTP版本号
# 
GET / HTTP/1.1

Host: 192.168.3.139:1657    # 请求的服务器地址

Connection: keep-alive
Upgrade-Insecure-Requests: 1
# UA 用户代理，最开始设计的的目的，是为了能从请求头里辨识浏览器的类型
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
"""

client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))

client_socket.send('\n'.encode('utf8'))

client_socket.send('hello world'.encode('utf8'))
client_socket.send(client_addr[0].encode('utf8'))
