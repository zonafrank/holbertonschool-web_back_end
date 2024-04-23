#!/usr/bin/env python3
"""Module for measure_time function"""
import time
import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """takes integers n and max_delay as arguments that
    measures the total execution time for wait_n(n, max_delay)
    returns total_time / n
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter() - s
    return elapsed_time / n
