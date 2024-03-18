#!/usr/bin/env python3
"""Module doc"""
import random
import asyncio
"""Import of the random module"""


async def wait_random(max_delay: int = 10) -> float:
    """This function permit to wait for"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
