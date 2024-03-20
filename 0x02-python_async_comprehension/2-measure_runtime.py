#!/usr/bin/env python3
""" Runs async coroutine 10 times in parallet and test
run time
"""
import asyncio
import time
from importlib import import_module as using


async_com = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure runtime for 4 coroutines running asycronously"""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_com() for _ in range(4)))
    return time.perf_counter() - start_time
