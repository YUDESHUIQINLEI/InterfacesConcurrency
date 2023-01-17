# -*- coding: utf-8 -*-
# @Author : qinlei
# @Time : 2023/1/16 11:05 下午
# @Function:
import asyncio


class Event:
    event = None

    def __init__(self, task_list):
        event = asyncio.get_event_loop()
        ts = asyncio.gather(*task_list)
        try:
            event.run_until_complete(ts)
        except Exception:
            raise NotImplementedError('runError')
        try:
            event.close()
        except Exception:
            raise NotImplementedError('closeError')
