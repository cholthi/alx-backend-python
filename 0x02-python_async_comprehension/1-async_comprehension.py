#!/usr/bin/env python3
"""collects 10 random numbers using an async comprehensing
over async_generator
"""
import asyncio
from typing import List


async_gen = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collects 10 random asyncronously using aysnc
    comprehensions
    """
    return [i async for i in async_gen()]
