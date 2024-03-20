#!/usr/bin/env python3
""" Runs async coroutine 10 times in parallet and test
run time
"""
import asyncio
import time


async_com = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> int:
    """Measure runtime for 4 coroutines running asycronously"""
    start_time = time.perf_counter()
    _ = await asyncio.gather(*(async_com() for i in range(4)))
    return time.perf_counter() - start_time
