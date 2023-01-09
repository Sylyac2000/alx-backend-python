#!/usr/bin/env python3
"""defining  an async routine called wait_n"""
import random
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ asynchronous coroutine """
    list_delays = []
    for i in range(n):
        delay = await wait_random(max_delay)
        list_delays.append(delay)
    return sorted(list_delays)
