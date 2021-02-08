import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定ip
s.bind(('192.168.31.199', 8080))


# 创建文件接收消息
# file = open('消息记录.txt', 'w', encoding='utf8')


# 发消息
def send_msg():
    while True:
        msg = input('请输入你要发送的内容')
        s.sendto(msg.encode('utf8'), ('192.168.31.199', 9090))
        if msg == 'exit':
            break


# 接收消息,需要使用第三方工具
# data接收到的数据类型是一个元组
# 元组里第0个元素是接收到的数据
# 元组里第1个元素是发送方的ip地址和端口号
def recv_msg():
    while True:
        data, addr = s.recvfrom(1024)

        print('接收到了{}地址{}端口的消息，内容是：{}'.format(addr[0], addr[1], data.decode('utf8')),
              file=open('消息记录.txt', 'w', encoding='utf8'))


t1 = threading.Thread(target=send_msg)
t2 = threading.Thread(target=recv_msg)

t1.start()
t2.start()

s.close()
