from wsgiref.simple_server import make_server


def demo_app(environ, start_response):
    path = environ['PATH_INFO']

    # 状态码：RESTFUL ==> 前后端分离
    # 2xx：请求响应成功
    # 3xx：重定向到某一个页面
    # 4xx：客户端错误。 404 客户端访问了一个不存在的地址  405：请求方式不被允许
    # 5xx：服务器的错误

    status_code = '200 OK'  # 默认状态码是200
    if path == '/':
        response = '欢迎来到我的首页'
    elif path == '/test':
        response = '欢迎来到test页面'
    elif path == '/demo':
        response = '欢迎来到demo页面'
    else:
        status_code = '404 Not Found'  # 如果页面没有配置，返回404
        response = '页面走丢了'

    start_response(status_code, [('Content-type', 'text/html;charset=utf8')])
    return [response.encode('utf8')]  # 浏览器显示的内容


if __name__ == '__main__':
    httpd = make_server('', 8090, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    # 服务器在后台一直运行
    httpd.serve_forever()
