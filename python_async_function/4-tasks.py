#!/usr/bin/env python3
"""Module for task_wait_n"""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """async routine that takes in 2 int arguments: n and max_delay.
    spawns task_wait_random n times with the specified max_delay.
    Returns the list of all the delays (float values) in ascending order
    """
    result = await asyncio.gather(*(
        task_wait_random(max_delay) for _ in range(n)))
    return sorted(result)
