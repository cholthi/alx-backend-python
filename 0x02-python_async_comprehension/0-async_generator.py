#!/usr/bin/env python3
"""
Provides an async generator that sleeps 1s between yields
"""
import asyncio
import random
from typing import Iterator


async def async_generator() -> Iterator[float]:
    """loops 10 times and waits for 1s asycronously,
    then yields a random value between 0 and 10
    """
    for i in range(10):
        result = random.random() * 10
        await asyncio.sleep(1)
        yield result
