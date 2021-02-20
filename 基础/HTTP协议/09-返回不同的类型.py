import json
from wsgiref.simple_server import make_server


def demo_app(environ, start_response):
    path = environ['PATH_INFO']

    status_code = '200 OK'
    if path == '/':
        response = '欢迎来到我的首页'
    elif path == '/test':
        response = json.dumps({'name': 'zhangsan', 'age': 18})
    elif path == '/demo':
        with open('pages/xxx.txt', 'r', encoding='utf8')as file:
            response = file.read()
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
