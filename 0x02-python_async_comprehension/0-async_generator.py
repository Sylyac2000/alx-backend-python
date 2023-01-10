#!/usr/bin/env python3
"""
coroutine named async_generator with no arguments.
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async_generator coroutine - loop 10 times, each time wait 1 second"""
    delay = 1
    for _ in range(10):
        await asyncio.sleep(delay)
        yield random.uniform(0, 10)
