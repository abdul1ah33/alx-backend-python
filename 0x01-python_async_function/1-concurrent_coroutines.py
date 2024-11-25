#!/usr/bin/env python3
'''Task 1's module.
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times.
    '''
    del_list = []
    tasks = []
    for i in range(n):
        wait_time = asyncio.create_task(wait_random(max_delay))
        tasks.append(wait_time)

    for task in asyncio.as_completed(tasks):
        sorted_task = await task
        del_list.append(sorted_task)

    return sorted(del_list)
