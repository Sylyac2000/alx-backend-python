#!/usr/bin/env python3
"""
a coroutine called async_comprehension that takes no arguments.
"""

import random
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collect 10 random numbers using an async comprehensing"""
    return [_ async for _ in async_generator()]
