#!/usr/bin/env python3
"""
coroutine named async_generator with no arguments.
"""

import random
import asyncio


async def async_generator():
    """loop 10 times, each time asynchronously wait 1 second"""
    n: int = 10
    delay: int = 1
    for i in range(n):
        await asyncio.sleep(delay)
        random_number = random.uniform(0, n)
        yield random_number
