#!/usr/bin/env python3
"""Module doc"""
import time
import asyncio
""""Import module"""
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """This function measure the async runtime"""
    s = time.time()
    await asyncio.gather(
            *[async_comprehension() for _ in range(4)]
            )
    e = time.time() - s
    return e
