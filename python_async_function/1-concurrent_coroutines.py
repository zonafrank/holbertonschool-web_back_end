#!/usr/bin/env python3
"""Module for async coroutine wait_n"""
from typing import List
import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """async routine that takes in 2 int arguments: n and max_delay.
    spawns wait_random n times with the specified max_delay.
    Returns the list of all the delays (float values) in ascending order
    """
    result = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(result)
