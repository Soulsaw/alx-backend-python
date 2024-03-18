#!/usr/bin/env python3
"""Module doc"""
import asyncio
import time
"""Import of the random module"""


def measure_time(n: int, max_delay: int) -> float:
    """Appel async methode"""
    wait_n = __import__('1-concurrent_coroutines').wait_n
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    e = (time.perf_counter() - s) / n
    return e
