# requests.get() 同步的代码 -> 异步操作aiohttp
# pip install aiohttp

import asyncio

import aiohttp

urls = [
    'http://kr.shanghai-jiuxin.com/file/2020/1031/774218be86d832f359637ab120eba52d.jpg',
    'http://kr.shanghai-jiuxin.com/file/2020/1031/6b72c57a1423c866d2b9dc10d0473f27.jpg',
    'http://kr.shanghai-jiuxin.com/file/2020/1031/563337d07af599a9ea64e620729f367e.jpg'
]


async def diodownload(url):
    # 发送请求
    # 得到图片内容
    # 保存到文件
    name = url.rsplit('/', 1)[1]  # 从末尾开始切，倒数第一个 / 为第1个，前面的为第0个，取第1个就取后面部分
    # with 自动关闭
    async with aiohttp.ClientSession() as session:  # requests
        async with session.get(url) as resp:  # resp = requests.get()
            # resp.content.read() => resp.content
            # 请求回来了，写入文件
            with open(name, 'wb') as f:
                # content 得到网页图片的二进制码，然后写入
                f.write(await resp.content.read())  # 读取内容是异步的，需要await挂起    resp.content.read() <==> resp.content
    print(name, '搞定')
    # s = aiohttp.ClientSession() 相当于 requests
    # 发送请求
    # 得到图片内容
    # 保存到文件


async def main():
    tasks = []
    for url in urls:
        # 先创建一个asyncio.create_task对象才能使用
        a = asyncio.create_task(diodownload(url))
        tasks.append(a)
    # 一次性把所有任务都执行
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
