from wsgiref.simple_server import make_server


# demo_app 需要两个参数
# 第 0 个参数，表示环境(电脑的环境；请求路径相关的环境)
# 第 1 个参数，是一个函数，用来返回响应头
# 这个函数需要一个返回值，返回值是一个列表
# 列表里只有一个元素，是一个二进制，表示返回给浏览器的数据
def demo_app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html;charset=utf8')])
    return ['hello'.encode('utf8')]  # 浏览器显示的内容


if __name__ == '__main__':
    # demo_app 是一个函数，用来处理用户的请求
    httpd = make_server('', 8000, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")

    # 代码的作用是打开电脑的浏览器，并在浏览器输入下面的地址
    # import webbrowser
    # webbrowser.open('http://localhost:8000/xyz?abc')

    # 处理一次请求
    httpd.handle_request()  # serve one request, then exit
    # 服务器在后台一直运行
    httpd.serve_forever()
