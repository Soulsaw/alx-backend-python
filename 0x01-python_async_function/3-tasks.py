#!/usr/bin/env python3
"""Module doc"""
import asyncio
"""Import of the random module"""


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Appel async methode"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))
