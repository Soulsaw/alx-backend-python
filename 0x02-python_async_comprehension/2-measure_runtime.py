#!/usr/bin/env python3
"""Module doc"""
import asyncio
""""Import module"""
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """This function measure the async runtime"""
    s = asyncio.get_event_loop().time()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    e = asyncio.get_event_loop().time() - s
    return e
