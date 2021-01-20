file = open('xxx.txt', 'rb')
try:
    while True:
        content = file.read(1024)
        if not content:
            break
        print(content)
finally:  # 最终都会执被执行的代码(需要命令运行，右键不可以)
    print('文件被关闭了')
    file.close()
