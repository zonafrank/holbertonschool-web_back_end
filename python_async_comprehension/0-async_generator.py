#!/usr/bin/env python3
"""Module for coroutine async_generator"""
from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """loops 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
