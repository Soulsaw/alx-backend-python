#!/usr/bin/env python3
"""Module doc"""
import random
import asyncio
from typing import List
""""Import module"""


async def async_generator() -> List[float]:
    """This function use the coroutines generators"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
