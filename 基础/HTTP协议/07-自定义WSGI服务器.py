from wsgiref.simple_server import make_server


def demo_app(environ, start_response):
    # environ 是一个字典，保存了很多的数据
    # 其中重要的一个是 PATH_INFO 能够获取到用户的访问路径
    path = environ['PATH_INFO']
    print('path={}'.format(path))
    start_response('200 OK', [('Content-type', 'text/html;charset=utf8')])
    return ['hello'.encode('utf8')]  # 浏览器显示的内容


if __name__ == '__main__':
    httpd = make_server('', 8090, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    # 服务器在后台一直运行
    httpd.serve_forever()
