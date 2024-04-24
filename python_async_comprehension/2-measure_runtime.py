#!/usr/bin/env python3
"""Module for measure_runtime coroutine"""
import asyncio
import time

async_comprehension = __import__(
    "1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times in parallel
    using asyncio.gather and returns the total runtime.
    """
    s = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    print()
    elapsed_time = time.perf_counter() - s
    return elapsed_time
