# -*- coding: utf-8 -*-
# @Author : qinlei
# @Time : 2023/1/16 11:09 下午
# @Function: 接口处理
import asyncio
import time

import aiohttp


async def interfaceTool(n, **kwargs):
    if kwargs['method'] == 'get':
        async with aiohttp.ClientSession() as session:
            print('协程{}开始执行……'.format(n))
            await asyncio.sleep(2)
            try:
                async with session.get(
                        url=kwargs['url'], headers=kwargs['headers']) as resp:
                    res = await resp.json()
                    print(time.time())
                    print(res)
                    print('协程{}执行结束……'.format(n))
            except Exception as result:
                print('接口执行异常'.format(result))
    else:
        async with aiohttp.ClientSession() as session:
            print('协程{}开始执行……'.format(n))
            await asyncio.sleep(2)
            try:
                async with session.post(
                        url=kwargs['url'], headers=kwargs['headers'], data=kwargs['body']) as resp:
                    res = await resp.json()
                    print(time.time())
                    print(res)
                    print('协程{}执行结束……'.format(n))
            except Exception as result:
                print('接口执行异常'.format(result))

