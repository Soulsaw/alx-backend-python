#!/usr/bin/env python3
"""Module doc"""
import asyncio
from typing import List
"""Import of the random module"""


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Appel async methode"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    delays.sort()
    return delays
