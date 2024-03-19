#!/usr/bin/env python3
'''Returns the values from async function run n times and sorted asc
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n time
    '''
    wait_times = await asyncio.gather(
        *(wait_random(max_delay) for i in range(n))
    )
    return sorted(wait_times)
