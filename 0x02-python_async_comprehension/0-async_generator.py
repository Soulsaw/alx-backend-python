#!/usr/bin/env python3
"""Module doc"""
import random
import asyncio
from typing import Generator
""""Import module"""


async def async_generator() -> Generator[float, None, None]:
    """This function use the coroutines generators"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
