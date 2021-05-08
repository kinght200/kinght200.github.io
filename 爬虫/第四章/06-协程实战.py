# python编写协程的程序
import asyncio


# async def func():
#     print('你好啊，我叫xxx')
#
#
# if __name__ == '__main__':
#     g = func()  # 此时的函数是异步协程函数，此时函数执行得到的是一个协程对象
#     # print(g)
#     asyncio.run(g)  # 协程程序运行需要asyncio模块的支持

# async def fun1():
#     print('你好啊，我叫邹杰了')
#     # time.sleep(3)   # 当程序出现了同步操作的时候，异步就中断了
#     await asyncio.sleep(3)    # 异步操作的代码
#     print('你好啊，我叫邹杰了')
#
#
# async def fun2():
#     print('你好啊，我叫周杰伦')
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print('你好啊，我叫周杰伦')
#
#
# async def fun3():
#     print('你好啊，我叫王建国')
#     # time.sleep(4)
#     await asyncio.sleep(4)
#     print('你好啊，我叫王建国')
#
#
# if __name__ == '__main__':
#     f1 = fun1()
#     f2 = fun2()
#     f3 = fun3()
#     tasks = [f1, f2, f3]
#
#     t1 = time.time()
#     # 一次性启动多个任务
#     asyncio.run(asyncio.wait(tasks))
#     t2 = time.time()
#     print(t2-t1)


# python 希望的写法
# async def fun1():
#     print('你好啊，我叫邹杰了')
#     await asyncio.sleep(3)
#     print('你好啊，我叫邹杰了')
#
#
# async def fun2():
#     print('你好啊，我叫周杰伦')
#     await asyncio.sleep(2)
#     print('你好啊，我叫周杰伦')
#
#
# async def fun3():
#     print('你好啊，我叫王建国')
#     await asyncio.sleep(4)
#     print('你好啊，我叫王建国')
#
#
# async def main():
#     # 第一种写法
#     # f1 = fun1()
#     # await f1    # 一般awa挂起操作放在协程对象前面
#
#     # 第二种写法（推荐）
#     tasks = [
#         asyncio.create_task(fun1()),  # py3.8以后加上asyncio.create_task（）
#         asyncio.create_task(fun2()),
#         asyncio.create_task(fun3()),
#     ]
#     await asyncio.wait(tasks)
#
#
# if __name__ == '__main__':
#     t1 = time.time()
#     asyncio.run(main())
#     t2 = time.time()
#     print(t2 - t1)

# 在爬虫领域的应用
async def download(url):
    print('准备开始下载')
    await asyncio.sleep(2)  # 网络请求
    print('下载完成')


async def main():
    urls = [
        'http://www.baidu.com',
        'http://www.bilibili.com',
        'http://www.163.com'
    ]
    tasks = []
    for url in urls:
        d = asyncio.create_task(download(url))
        tasks.append(d)

    # 一次性把所有任务都执行
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
