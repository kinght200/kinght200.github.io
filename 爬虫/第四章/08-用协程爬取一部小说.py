# http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"} => 得到所有章节的内容（名称，cid）
# 第一章节内部的内容
# http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500"，“cid”:"4306063500|11348817","need_bookinfo":1}

import asyncio
import json

import aiofiles
import aiohttp
import requests

"""
1.同步操作：访问getCatalog 拿到所有章节的cid和名称
2.异步操作：访问getChapterContent 下载所有的文章内容
"""


async def diodownload(cid, b_id, title):
    data = {
        "book_id": b_id,
        "cid": f"{b_id}{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)
    url = f"http://dushu.baidu.com/api/pc/getChapterContent?data={data}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()

            async with aiofiles.open(title, 'w', encoding='utf-8') as f:
                await f.write(dic['data']['novel']['content'])  # 把小说内容写出


async def getCatalog(url):
    resp = requests.get(url)
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:  # item就是对应每一个章节的名称和cid
        title = item['title']
        cid = item['cid']
        # 准备异步任务
        a = asyncio.create_task(diodownload(cid, b_id, title))
        tasks.append(a)
    # asyncio.run(asyncio.wait(tasks))  与下句代码一致
    await asyncio.wait(tasks)


if __name__ == '__main__':
    b_id = "4306063500"
    url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + b_id + '"}'
    asyncio.run(getCatalog(url))
