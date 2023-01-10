#!/usr/bin/env python3
"""
a coroutine called measure_runtime that takes no arguments.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """collect 10 random numbers using an async comprehensing"""
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.perf_counter()
    return end_time - start_time
